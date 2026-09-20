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
PRIVATE_SOURCE = re.compile(r"(?:^|[\[,\s])(?:session:|project:/|filesystem:|skill:)")
PERSONAL_ENDPOINT = re.compile(r"(?:telegram:\d{6,}|\bjob_id\s*[:=]\s*[0-9a-f]{8,})", re.I)
PRIVATE_KEY = re.compile(r"-----BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY-----")
SECRET_ASSIGNMENT = re.compile(
    r"\b(?:api[_-]?key|access[_-]?token|secret|password|passwd)\b\s*[:=]\s*(['\"])([^'\"\n]{8,})\1",
    re.I,
)
SAFE_SECRET_MARKERS = (
    "example",
    "placeholder",
    "your_api_key",
    "your-api-key",
    "your_token",
    "your-token",
    "dummy",
    "test-only",
    "changeme",
    "<",
    "${",
    "...",
    "xxx",
)
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


def source_field(metadata: str) -> str:
    match = re.search(r"^sources:\s*(.*)$", metadata, re.M)
    if not match:
        return ""
    value = match.group(1)
    if value.strip():
        return value
    block = []
    for line in metadata[match.end() :].splitlines():
        if not line.strip():
            continue
        if not line.startswith((" ", "\t")):
            break
        block.append(line)
    return "\n".join(block)


def has_literal_secret(text: str) -> bool:
    for match in SECRET_ASSIGNMENT.finditer(text):
        value = match.group(2).strip().lower()
        if not any(marker in value for marker in SAFE_SECRET_MARKERS):
            return True
    return False


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
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            add(candidates, rel, "unreviewed-binary-or-non-utf8")
            continue

        candidate_text = "\n".join(line for line in text.splitlines() if SYNTHETIC_LINE_MARKER not in line)

        if AUTHOR_HOME.search(text):
            add(violations, rel, "author-home-path")
        metadata = frontmatter(text)
        if metadata is not None and PRIVATE_SOURCE.search(source_field(metadata)):
            add(violations, rel, "private-provenance")
        if PERSONAL_ENDPOINT.search(text):
            add(violations, rel, "personal-endpoint-identifier")
        if PRIVATE_KEY.search(text):
            add(violations, rel, "private-key-material")
        if has_literal_secret(text):
            add(violations, rel, "literal-secret-assignment")

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
