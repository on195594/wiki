#!/usr/bin/env python3
"""Check a repository for public-boundary violations and review candidates."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from wiki_root import resolve_root

SKIP_PARTS = {".git", "__pycache__"}
SYNTHETIC_LINE_MARKER = "public-check: synthetic"
AUTHOR_HOME = re.compile(r"(?:file://)?/home/" + "lin" + r"(?:/|\b)")
PRIVATE_SOURCE = re.compile(r"(?<![A-Za-z0-9_])(?:session:|project:/|filesystem:|skill:)")
PRIVATE_ARTIFACT = re.compile(
    r"\b(?:session|summary)\s+run\s+\d{8}-\d{6}\b|"
    r"\boff-wiki\s+(?:grounding\s+)?artifact\b|"
    r"\blocal\s+`?/?gsummary`?\s+(?:workflow|output|source\s+packet)\b|"
    r"\blocal\s+(?:output|summary(?:\s+path)?|source\s+packet)\b.{0,80}"
    r"\b(?:auxiliary\s+evidence|preserved|retained|recorded)\b",
    re.I,
)
PERSONAL_ENDPOINT = re.compile(r"(?:telegram:\d{6,}|\bjob_id\s*[:=]\s*[0-9a-f]{8,})", re.I)
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")
SECRET_ASSIGNMENT = re.compile(
    r"(?:^|(?<=[{,(]))[ \t]*(?:export[ \t]+)?[\"']?"
    r"(?:api[_-]?key|access[_-]?token|secret|password|passwd)[\"']?[ \t]*[:=][ \t]*"
    r'(?:"(?P<double>[^"\n]+)"|\'(?P<single>[^\'\n]+)\'|'
    r"(?P<bare>[A-Za-z0-9$][A-Za-z0-9_.$/+@={}-]*))",
    re.I | re.M,
)
SAFE_SECRET_VALUES = {
    "changeme",
    "dummy",
    "example",
    "placeholder",
    "test-only",
    "xxx",
    "your-api-key",
    "your-token",
    "your_api_key",
    "your_token",
}
SAFE_SECRET_PATTERN = re.compile(
    r"(?:your|example|sample|dummy|test)[_-](?:api[_-]?key|access[_-]?token|token|password|secret)",
    re.I,
)
ENV_REFERENCE = re.compile(r"\$(?:[A-Za-z_][A-Za-z0-9_]*|\{[A-Za-z_][A-Za-z0-9_]*\})")
CONFIG_SUFFIXES = {".cfg", ".conf", ".env", ".ini", ".json", ".toml", ".yaml", ".yml"}
CODE_SUFFIXES = {".c", ".cpp", ".go", ".js", ".jsx", ".php", ".py", ".rb", ".rs", ".sh", ".ts", ".tsx"}
GENERIC_HOME_NAMES = {"user", "example", "username", "name"}
HOME_PATH = re.compile(r"(?:file://)?/home/([A-Za-z0-9._-]+)(?:/|\b)")
PRIVATE_IPV4 = re.compile(r"(?<!\d)(?:10\.|192\.168\.|172\.(?:1[6-9]|2\d|3[01])\.)\d{1,3}\.\d{1,3}(?!\d)")
EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@([\w.-]+\.[A-Za-z]{2,})(?![\w.-])")
PERSONAL_STATE = re.compile(
    r"(?:当前运行基线|最近一次\s*`?ok|MEMORY\.md.{0,30}\d+/\d+|USER\.md.{0,30}\d+/\d+|"  # public-check: synthetic
    r"state\.db.{0,40}(?:MB|GB)|当前\s*open|恢复快照|实际调度|已部署到本机)",  # public-check: synthetic
    re.I | re.S,
)
PERSONAL_FINANCE = re.compile(
    r"(?:(?:真实|当前|我的).{0,16}(?:持仓|仓位|账户余额|现金余额|成本价|买入价)|"  # public-check: synthetic
    r"(?:金额基线|当前已知目标)\s*[:：])",  # public-check: synthetic
    re.S,
)
TASK_LEDGER = re.compile(  # public-check: synthetic
    r"(?:\bsession_id\s*[:=]|\bjob_id\s*[:=]|个人任务台账|会话记录|会话原文)", re.I  # public-check: synthetic
)


def frontmatter(text: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.S)
    return match.group(1) if match else None


def provenance_fields(metadata: str) -> str:
    """Return public-source metadata without needing a YAML dependency."""
    values: list[str] = []
    active = False
    for line in metadata.splitlines():
        field = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if field:
            active = field.group(1) in {"source", "sources", "source_url", "extraction", "provenance"}
            if active:
                values.append(field.group(2))
        elif active and line.startswith((" ", "\t")):
            values.append(line)
        elif line.strip():
            active = False
    return "\n".join(values)


def is_config_path(path: Path) -> bool:
    return path.name == ".env" or path.name.startswith(".env.") or path.suffix.lower() in CONFIG_SUFFIXES


def is_placeholder(value: str) -> bool:
    normalized = value.strip().lower()
    return (
        normalized in SAFE_SECRET_VALUES
        or normalized == "..."
        or re.fullmatch(r"<[^<>\n]+>", normalized) is not None
        or SAFE_SECRET_PATTERN.fullmatch(normalized) is not None
    )


def is_program_expression(text: str, match: re.Match[str], value: str, path: Path) -> bool:
    if is_config_path(path):
        return False
    line_start = text.rfind("\n", 0, match.start()) + 1
    line_end = text.find("\n", match.end())
    if line_end < 0:
        line_end = len(text)
    prefix = text[line_start : match.start()]
    suffix = text[match.end() : line_end]
    if value in {"os.environ", "os.getenv", "getenv"} and suffix.lstrip().startswith(("[", "(")):
        return True
    if re.fullmatch(r"(?:require|get|load|read)_[A-Za-z0-9_]+", value) and suffix.lstrip().startswith("("):
        return True
    identifier = re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.]*", value) is not None
    inside_call = prefix.rfind("(") > prefix.rfind(")")
    return identifier and (path.suffix.lower() in CODE_SUFFIXES or inside_call)


def credential_assignment_risk(text: str, path: Path) -> tuple[bool, bool]:
    """Return (violation, candidate) without returning matched values."""
    violation = False
    candidate = False
    for match in SECRET_ASSIGNMENT.finditer(text):
        quoted = match.group("double") is not None or match.group("single") is not None
        value = (match.group("double") or match.group("single") or match.group("bare")).strip()
        if is_placeholder(value) or ENV_REFERENCE.fullmatch(value):
            continue
        if not quoted and is_program_expression(text, match, value, path):
            continue
        if quoted or is_config_path(path) or re.search(r"[^A-Za-z_]", value):
            violation = True
        else:
            candidate = True
    return violation, candidate


def add(items: list[dict[str, str]], path: str, rule: str) -> None:
    record = {"path": path, "rule": rule}
    if record not in items:
        items.append(record)


def build_report(root: Path) -> dict[str, Any]:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"repository root does not exist or is not a directory: {root}")

    violations: list[dict[str, str]] = []
    candidates: list[dict[str, str]] = []
    scanned = 0
    for path in sorted(p for p in root.rglob("*") if p.is_file() and not SKIP_PARTS.intersection(p.relative_to(root).parts)):
        rel = path.relative_to(root).as_posix()
        scanned += 1
        data = path.read_bytes()
        if b"\x00" in data:
            add(candidates, rel, "unreviewed-binary-or-non-utf8")
            continue
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            add(candidates, rel, "unreviewed-binary-or-non-utf8")
            continue

        candidate_text = "\n".join(line for line in text.splitlines() if SYNTHETIC_LINE_MARKER not in line)

        if AUTHOR_HOME.search(text):
            add(violations, rel, "author-home-path")
        metadata = frontmatter(text)
        if metadata is not None and PRIVATE_SOURCE.search(provenance_fields(metadata)):
            add(violations, rel, "private-provenance")
        if PRIVATE_ARTIFACT.search(candidate_text):
            add(violations, rel, "private-session-artifact")
        if PERSONAL_ENDPOINT.search(text):
            add(violations, rel, "personal-endpoint-identifier")
        if PRIVATE_KEY.search(text):
            add(violations, rel, "private-key-material")
        secret_violation, secret_candidate = credential_assignment_risk(text, path)
        if secret_violation:
            add(violations, rel, "literal-secret-assignment")
        if secret_candidate:
            add(candidates, rel, "possible-secret-assignment")

        for match in HOME_PATH.finditer(candidate_text):
            if match.group(1).lower() not in GENERIC_HOME_NAMES and not AUTHOR_HOME.fullmatch(match.group(0)):
                add(candidates, rel, "non-generic-home-path")
                break
        if PRIVATE_IPV4.search(candidate_text):
            add(candidates, rel, "private-network-address")
        if any(match.group(1).lower() not in {"example.com", "example.org", "example.net", "test.invalid"} for match in EMAIL.finditer(candidate_text)):
            add(candidates, rel, "personal-email-address")
        if PERSONAL_STATE.search(candidate_text):
            add(candidates, rel, "personal-instance-state")
        if PERSONAL_FINANCE.search(candidate_text):
            add(candidates, rel, "personal-financial-record")
        if TASK_LEDGER.search(candidate_text):
            add(candidates, rel, "session-or-task-ledger")

    violations.sort(key=lambda item: (item["path"], item["rule"]))
    candidates.sort(key=lambda item: (item["path"], item["rule"]))
    return {
        "root": str(root),
        "scanned_files": scanned,
        "violations": violations,
        "candidates": candidates,
        "pass": not violations,
    }


def text_report(report: dict[str, Any]) -> str:
    lines = [
        f"public_content_pass: {str(report['pass']).lower()}",
        f"scanned_files: {report['scanned_files']}",
        f"violations: {len(report['violations'])}",
    ]
    lines.extend(f"  {item['path']} [{item['rule']}]" for item in report["violations"])
    lines.append(f"candidates: {len(report['candidates'])}")
    lines.extend(f"  {item['path']} [{item['rule']}]" for item in report["candidates"])
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args(argv)
    try:
        report = build_report(resolve_root(args.root))
    except Exception as exc:  # noqa: BLE001 - compact CLI boundary
        print(json.dumps({"pass": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(text_report(report), end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
