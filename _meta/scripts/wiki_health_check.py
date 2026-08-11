#!/usr/bin/env python3
"""Deterministic read-only health check for the local Hermes wiki.

Default root resolution: --root, OBSIDIAN_VAULT_PATH, then /home/lin/wiki.
Exit codes:
  0: pass (no P0/P1 issues)
  1: health check ran but P0/P1 issues exist
  2: CLI/runtime error
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from typing import Any

CORE_FILES = {"index.md", "log.md", "SCHEMA.md"}
TINY_THRESHOLD = 120
RAW_HASH_MANIFEST = "_meta/raw-source-hashes.json"
# Calibrated 2026-08-11 against all 5995 formal-page pairs: median 0.055,
# p99 0.137, max 0.270 (the top pair being two genuinely distinct orchestration
# pages). 0.45 sits well clear of that, so it fires on a real re-ingestion
# rather than on topic overlap. Recalibrate if the corpus changes shape.
NEAR_DUPLICATE_THRESHOLD = 0.45
ALLOWED_SOURCE_PREFIXES = (
    "raw/",
    "concepts/",
    "queries/",
    "comparisons/",
    "operations/",
    "project:",
    "session:",
    "skill:",
    "docs:",
    "filesystem:",
)


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def is_live_file(root: Path, path: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return False
    if ".git" in parts:
        return False
    if parts and parts[0] == "_backups":
        return False
    if ".bak." in path.name:
        return False
    return True


def is_backup_candidate(root: Path, path: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return False
    return ".bak." in path.name or bool(parts and parts[0] == "_backups")


def is_formal_page(root: Path, path: Path) -> bool:
    r = rel(root, path)
    return not (
        r in CORE_FILES
        or r.startswith("_meta/")
        or r.startswith("raw/")
    )


def strip_code(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"`[^`]*`", "", text)
    return text


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_frontmatter(text: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    return match.group(1) if match else None


def parse_inline_list(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        return [item.strip().strip("'\"") for item in value.strip("[]").split(",") if item.strip()]
    return [value.strip().strip("'\"")]


def frontmatter_value(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", frontmatter, flags=re.M)
    if not match:
        return None
    return match.group(1).strip()


def is_allowed_source(source: str) -> bool:
    return source.startswith(ALLOWED_SOURCE_PREFIXES) or bool(re.match(r"https?://", source))


def declared_tags(root: Path) -> set[str]:
    """Tags registered in the SCHEMA.md Tag Taxonomy section.

    An empty result means the section is missing or unparseable. Callers must
    report that as an issue rather than skip quietly: a tag check that silently
    stops enforcing is the failure this check exists to prevent.

    Code blocks are stripped first: a bullet inside a fenced example would
    otherwise register itself as a real tag, which is the one failure mode here
    that loosens the check without producing any output.
    """
    schema = root / "SCHEMA.md"
    if not schema.exists():
        return set()
    text = strip_code(read_text(schema))
    match = re.search(r"^## Tag Taxonomy\s*$(.*?)^## ", text, flags=re.S | re.M)
    if not match:
        return set()
    return set(re.findall(r"^- ([a-z0-9-]+)\s*$", match.group(1), flags=re.M))


def parse_review_by(value: str) -> date | None:
    """Parse a `review_by` value, or None if it is not a plain YYYY-MM-DD date.

    The regex is not redundant: `date.fromisoformat` also accepts `20261111`
    and ISO week forms, and SCHEMA.md declares one written format.
    """
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value.strip()):
        return None
    try:
        return date.fromisoformat(value.strip())
    except ValueError:
        return None


def content_tokens(text: str) -> set[str]:
    """Bag of words used to compare two pages for near-duplication.

    Frontmatter and code blocks are dropped: shared tags and shared shell
    snippets make unrelated pages look alike. CJK is split into bigrams rather
    than whole runs, so `持仓监控` and `持仓管理` share a token instead of none.
    """
    text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
    text = re.sub(r"```.*?```", "", text, flags=re.S).lower()
    tokens = set(re.findall(r"[a-z0-9][a-z0-9-]{2,}", text))
    for run in re.findall(r"[一-鿿]+", text):
        tokens.update(run[i : i + 2] for i in range(len(run) - 1))
    return tokens


def load_raw_hashes(root: Path) -> dict[str, str] | None:
    """Recorded raw/ hashes, or None if the manifest is missing or unreadable.

    None means "cannot check", which the caller reports; it must never be
    confused with an empty manifest, which would silently pass every file.
    """
    path = root / RAW_HASH_MANIFEST
    if not path.exists():
        return None
    try:
        loaded = json.loads(read_text(path))
    except json.JSONDecodeError:
        return None
    return loaded if isinstance(loaded, dict) else None


def add_issue(issues: dict[str, list[dict[str, Any]]], severity: str, code: str, path: str, message: str, **extra: Any) -> None:
    item: dict[str, Any] = {"code": code, "path": path, "message": message}
    item.update(extra)
    issues[severity].append(item)


def resolve_wikilink(root: Path, current: Path, target: str, stems: dict[str, list[str]]) -> bool:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return True
    candidates: list[Path] = []
    if target.endswith(".md"):
        candidates.extend([root / target, current.parent / target])
    elif "/" in target:
        candidates.extend([
            root / f"{target}.md",
            root / target,
            current.parent / f"{target}.md",
            current.parent / target,
        ])
    else:
        return target in stems
    for candidate in candidates:
        try:
            resolved = candidate.resolve()
            if resolved.exists() and resolved.is_relative_to(root.resolve()):
                return True
        except OSError:
            continue
    return False


def git_status(root: Path) -> dict[str, Any]:
    git_dir = root / ".git"
    if not git_dir.exists():
        return {"is_repo": False, "branch_line": None, "short_status": [], "dirty": False}
    proc = subprocess.run(
        ["git", "status", "--short", "--branch"],
        cwd=root,
        text=True,
        capture_output=True,
        check=False,
    )
    lines = proc.stdout.splitlines()
    branch = lines[0] if lines else None
    short = lines[1:] if len(lines) > 1 else []
    return {
        "is_repo": True,
        "branch_line": branch,
        "short_status": short,
        "dirty": bool(short),
        "returncode": proc.returncode,
    }


def build_report(root: Path) -> dict[str, Any]:
    if not root.exists() or not root.is_dir():
        raise FileNotFoundError(f"wiki root does not exist or is not a directory: {root}")

    all_files = [p for p in root.rglob("*") if p.is_file() and ".git" not in p.parts]
    live_md = sorted([p for p in all_files if p.suffix == ".md" and is_live_file(root, p)])
    backup_candidates = sorted([p for p in all_files if is_backup_candidate(root, p)])
    raw_md = [p for p in live_md if rel(root, p).startswith("raw/")]
    formal = [p for p in live_md if is_formal_page(root, p)]

    distribution: dict[str, int] = {}
    for p in live_md:
        parts = p.relative_to(root).parts
        top = parts[0] if len(parts) > 1 else "(root)"
        distribution[top] = distribution.get(top, 0) + 1

    stems: dict[str, list[str]] = {}
    for p in live_md:
        stems.setdefault(p.stem, []).append(rel(root, p))

    issues: dict[str, list[dict[str, Any]]] = {"P0": [], "P1": [], "P2": []}
    notes: list[str] = []
    today = date.today()
    taxonomy = declared_tags(root)
    if not taxonomy:
        add_issue(issues, "P1", "unreadable_tag_taxonomy", "SCHEMA.md", "Tag Taxonomy section missing or unparseable; tag registration is not being enforced")

    for core in sorted(CORE_FILES):
        if not (root / core).exists():
            add_issue(issues, "P0", "missing_core_file", core, f"Missing core file: {core}")

    for p in live_md:
        r = rel(root, p)
        text = read_text(p)
        lines = text.splitlines()
        if any(re.match(r"^\d+\|", line) for line in lines[:20]):
            add_issue(issues, "P0", "line_prefix_pollution", r, "Line-number prefix pollution near file start")
        stripped = text.strip()
        if not stripped:
            add_issue(issues, "P1", "empty_file", r, "Empty markdown file")
        elif len(stripped) < TINY_THRESHOLD:
            add_issue(issues, "P2", "tiny_file", r, f"Tiny file below {TINY_THRESHOLD} non-whitespace characters", chars=len(stripped))
        if is_formal_page(root, p):
            body = re.sub(r"^---\s*\n.*?\n---\s*\n", "", text, flags=re.S)
            if not re.search(r"^#\s+\S", body, flags=re.M):
                add_issue(issues, "P1", "missing_h1", r, "Formal page missing H1 heading")
            if not text.startswith("---\n"):
                add_issue(issues, "P1", "missing_frontmatter", r, "Formal page missing YAML frontmatter")
            frontmatter = extract_frontmatter(text)
            if frontmatter is not None:
                tags_value = frontmatter_value(frontmatter, "tags")
                if tags_value is not None and taxonomy:
                    for tag in parse_inline_list(tags_value):
                        if tag not in taxonomy:
                            add_issue(issues, "P1", "unregistered_tag", r, "Tag is not registered in the SCHEMA.md tag taxonomy", tag=tag)
                review_by_value = frontmatter_value(frontmatter, "review_by")
                if review_by_value is not None:
                    review_by = parse_review_by(review_by_value)
                    if review_by is None:
                        add_issue(issues, "P1", "malformed_review_by", r, "review_by is not a YYYY-MM-DD date, so the expiry it declares can never fire", value=review_by_value)
                    elif review_by < today:
                        add_issue(issues, "P2", "page_due_for_review", r, "review_by date has passed; re-read the page against its current upstream subject", review_by=review_by_value)
                sources_value = frontmatter_value(frontmatter, "sources")
                if sources_value is None:
                    add_issue(issues, "P2", "missing_sources", r, "Formal page missing sources frontmatter")
                else:
                    for source in parse_inline_list(sources_value):
                        if "/tmp/" in source or source.startswith("/tmp/"):
                            add_issue(issues, "P2", "tmp_source", r, "Source uses non-durable /tmp path", source=source)
                        if not is_allowed_source(source):
                            add_issue(issues, "P2", "unexpected_source_form", r, "Source does not match SCHEMA.md allowed source forms", source=source)

    for p in live_md:
        r = rel(root, p)
        text = strip_code(read_text(p))
        for match in re.finditer(r"\[\[([^\]]+)\]\]", text):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if not resolve_wikilink(root, p, target, stems):
                add_issue(issues, "P0", "broken_wikilink", r, "Broken wikilink", target=target)
        for match in re.finditer(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text):
            url = match.group(1).strip()
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", url) or url.startswith("#"):
                continue
            target = url.split("#", 1)[0].strip()
            if not target:
                continue
            candidate = (p.parent / target).resolve()
            try:
                inside = candidate.is_relative_to(root.resolve())
            except OSError:
                inside = False
            if inside and not candidate.exists():
                add_issue(issues, "P1", "broken_markdown_link", r, "Broken relative Markdown link", target=url)

    index_path = root / "index.md"
    index_links: set[str] = set()
    if index_path.exists():
        index_text = strip_code(read_text(index_path))
        for match in re.finditer(r"\[\[([^\]]+)\]\]", index_text):
            target = match.group(1).split("|", 1)[0].split("#", 1)[0].strip()
            if target:
                index_links.add(target)
                if not resolve_wikilink(root, index_path, target, stems):
                    add_issue(issues, "P0", "broken_index_target", "index.md", "Index target does not resolve", target=target)
    else:
        add_issue(issues, "P0", "missing_index", "index.md", "Missing index.md")

    known_unindexed_drafts = 0
    for p in formal:
        r = rel(root, p)
        no_ext = r[:-3] if r.endswith(".md") else r
        if p.stem in index_links or no_ext in index_links:
            continue
        text = read_text(p)
        status_match = re.search(r"^status:\s*(.+)$", text, flags=re.M)
        status = status_match.group(1).strip().strip('"') if status_match else None
        if r.startswith("queries/") and status == "draft":
            known_unindexed_drafts += 1
            add_issue(issues, "P2", "known_unindexed_draft_query", r, "Draft query intentionally outside main index", status=status)
        else:
            add_issue(issues, "P1", "unexpected_unindexed_formal_page", r, "Formal page missing from index", status=status)

    non_raw_corpus: list[tuple[str, str]] = []
    for p in live_md:
        r = rel(root, p)
        if not r.startswith("raw/"):
            non_raw_corpus.append((r, read_text(p)))
    for raw in raw_md:
        r = rel(root, raw)
        no_ext = r[:-3] if r.endswith(".md") else r
        needles = [raw.stem, r, no_ext, f"[[{raw.stem}]]", f"[[{no_ext}]]"]
        if not any(any(needle in text for needle in needles) for _, text in non_raw_corpus):
            add_issue(issues, "P1", "unreferenced_raw_source", r, "Raw source page has no non-raw reference")

    recorded_hashes = load_raw_hashes(root)
    if recorded_hashes is None:
        add_issue(issues, "P1", "unreadable_raw_hash_manifest", RAW_HASH_MANIFEST, "Raw source hash manifest missing or unparseable; raw/ immutability is not being enforced")
    else:
        for p in raw_md:
            r = rel(root, p)
            recorded = recorded_hashes.get(r)
            if recorded is None:
                add_issue(issues, "P2", "unhashed_raw_source", r, f"Raw source has no entry in {RAW_HASH_MANIFEST}; run wiki_raw_hashes.py")
            elif recorded != hashlib.sha256(p.read_bytes()).hexdigest():
                add_issue(issues, "P1", "raw_source_drift", r, "Raw source content no longer matches its recorded hash; pages citing it may no longer describe what it says")

    # ponytail: O(n^2) over formal pages — 5995 pairs at 110 pages is instant.
    # Around 1000 pages this becomes the slowest check; switch to MinHash/LSH
    # then rather than raising the threshold to hide the cost.
    formal_tokens = {rel(root, p): content_tokens(read_text(p)) for p in formal}
    for (left, left_tokens), (right, right_tokens) in itertools.combinations(sorted(formal_tokens.items()), 2):
        if not left_tokens or not right_tokens:
            continue
        similarity = len(left_tokens & right_tokens) / len(left_tokens | right_tokens)
        if similarity > NEAR_DUPLICATE_THRESHOLD:
            add_issue(issues, "P2", "near_duplicate_pages", left, "Formal pages overlap enough to be a re-ingestion of the same subject", other=right, similarity=round(similarity, 3))

    if backup_candidates:
        add_issue(
            issues,
            "P2",
            "in_vault_backup_candidates",
            ".",
            "In-vault backup artifacts remain",
            count=len(backup_candidates),
            sample=[rel(root, p) for p in backup_candidates[:20]],
        )

    if known_unindexed_drafts:
        notes.append(f"{known_unindexed_drafts} draft query page(s) are intentionally outside index.md; see _meta/draft-query-inventory.md.")
    notes.append("Inline-code and fenced-code wikilink examples are ignored during link checks.")
    notes.append("Root core files and _meta/ pages are excluded from formal frontmatter/H1 requirements.")
    notes.append(f"`page_due_for_review` is evaluated against today's date ({today.isoformat()}); it is the one check whose result changes over time on unchanged files.")

    result = {
        "root": str(root),
        "counts": {
            "live_markdown": len(live_md),
            "formal_pages": len(formal),
            "raw_markdown": len(raw_md),
            "index_wikilinks": len(index_links),
            "backup_candidates": len(backup_candidates),
            "distribution": dict(sorted(distribution.items())),
        },
        "git_status": git_status(root),
        "issues": issues,
        "notes": notes,
        "pass": not issues["P0"] and not issues["P1"],
    }
    return result


def markdown_report(result: dict[str, Any]) -> str:
    status = "PASS" if result["pass"] else "FAIL"
    counts = result["counts"]
    lines = [
        f"# Wiki Health Check: {status}",
        "",
        f"Root: `{result['root']}`",
        f"Git: `{result['git_status'].get('branch_line')}`; dirty: `{result['git_status'].get('dirty')}`",
        "",
        "## Counts",
        f"- Live markdown: `{counts['live_markdown']}`",
        f"- Formal pages: `{counts['formal_pages']}`",
        f"- Raw markdown: `{counts['raw_markdown']}`",
        f"- Index wikilinks: `{counts['index_wikilinks']}`",
        f"- Backup candidates: `{counts['backup_candidates']}`",
        "",
        "## Issues",
    ]
    for severity in ("P0", "P1", "P2"):
        items = result["issues"][severity]
        lines.append(f"### {severity}: {len(items)}")
        if not items:
            lines.append("- None")
        else:
            for item in items:
                target = f" target=`{item['target']}`" if "target" in item else ""
                extra = f" count=`{item['count']}`" if "count" in item else ""
                lines.append(f"- `{item['code']}` `{item['path']}` — {item['message']}{target}{extra}")
        lines.append("")
    lines.append("## Notes")
    for note in result["notes"]:
        lines.append(f"- {note}")
    return "\n".join(lines).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Read-only Hermes wiki health check")
    parser.add_argument("--root", default=os.environ.get("OBSIDIAN_VAULT_PATH", "/home/lin/wiki"))
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args(argv)

    try:
        report = build_report(Path(args.root).expanduser().resolve())
    except Exception as exc:  # noqa: BLE001 - CLI error path should be explicit and compact.
        print(json.dumps({"pass": False, "error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(markdown_report(report), end="")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
