#!/usr/bin/env python3
"""Read-only tag taxonomy audit for the local Hermes wiki.

Exit codes:
  0: audit complete, no undeclared tags found
  1: audit complete, undeclared tags found
  2: CLI/runtime error
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DEFAULT_ROOT = "/home/lin/wiki"


def rel(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def is_live_markdown(root: Path, path: Path) -> bool:
    try:
        parts = path.relative_to(root).parts
    except ValueError:
        return False
    return (
        path.suffix == ".md"
        and ".git" not in parts
        and not (parts and parts[0] == "_backups")
        and ".bak." not in path.name
    )


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def extract_frontmatter(text: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, flags=re.S)
    return match.group(1) if match else None


def parse_inline_tags(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if value.startswith("[") and value.endswith("]"):
        try:
            parsed = ast.literal_eval(value)
            if isinstance(parsed, list):
                return [str(item).strip() for item in parsed if str(item).strip()]
        except (SyntaxError, ValueError):
            pass
        return [item.strip().strip("'\"") for item in value.strip("[]").split(",") if item.strip()]
    return [value.strip().strip("'\"")]


def parse_frontmatter_tags(frontmatter: str) -> list[str]:
    lines = frontmatter.splitlines()
    tags: list[str] = []
    for idx, line in enumerate(lines):
        if not re.match(r"^tags\s*:", line):
            continue
        _, value = line.split(":", 1)
        if value.strip():
            return parse_inline_tags(value)
        for next_line in lines[idx + 1 :]:
            if not next_line.startswith((" ", "\t")):
                break
            item = next_line.strip()
            if item.startswith("-"):
                tag = item[1:].strip().strip("'\"")
                if tag:
                    tags.append(tag)
        return tags
    return []


def parse_declared_tags(schema_text: str) -> list[str]:
    match = re.search(r"^## Tag Taxonomy\s*\n(.*?)(?=^##\s|\Z)", schema_text, flags=re.S | re.M)
    if not match:
        return []
    body = match.group(1)
    body = body.split("\nRules:", 1)[0]
    tags: list[str] = []
    seen: set[str] = set()
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        candidates = re.findall(r"`([a-z0-9][a-z0-9-]*)`", stripped)
        if not candidates:
            bullet = stripped[1:].strip()
            if re.fullmatch(r"[a-z0-9][a-z0-9-]*", bullet):
                candidates = [bullet]
        for tag in candidates:
            if tag not in seen:
                tags.append(tag)
                seen.add(tag)
    return tags


def build_report(root: Path) -> dict[str, Any]:
    if not root.exists() or not root.is_dir():
        raise FileNotFoundError(f"wiki root does not exist or is not a directory: {root}")
    schema_path = root / "SCHEMA.md"
    if not schema_path.exists():
        raise FileNotFoundError(f"missing schema: {schema_path}")

    declared = parse_declared_tags(read_text(schema_path))
    declared_set = set(declared)
    tag_counts: Counter[str] = Counter()
    files_by_tag: dict[str, list[str]] = defaultdict(list)
    duplicate_tag_files: list[dict[str, Any]] = []
    tagged_pages = 0

    for path in sorted(p for p in root.rglob("*.md") if is_live_markdown(root, p)):
        frontmatter = extract_frontmatter(read_text(path))
        if frontmatter is None:
            continue
        tags = parse_frontmatter_tags(frontmatter)
        if not tags:
            continue
        tagged_pages += 1
        counts = Counter(tags)
        duplicates = sorted(tag for tag, count in counts.items() if count > 1)
        if duplicates:
            duplicate_tag_files.append({"path": rel(root, path), "duplicates": duplicates})
        for tag in tags:
            tag_counts[tag] += 1
            files_by_tag[tag].append(rel(root, path))

    undeclared = {tag: count for tag, count in sorted(tag_counts.items()) if tag not in declared_set}
    declared_unused = [tag for tag in declared if tag not in tag_counts]
    high_frequency_candidates = {
        tag: count
        for tag, count in sorted(undeclared.items(), key=lambda item: (-item[1], item[0]))
        if count >= 3
    }

    return {
        "root": str(root),
        "declared_count": len(declared),
        "declared_tags": declared,
        "tagged_pages": tagged_pages,
        "actual_unique_count": len(tag_counts),
        "actual_tag_counts": dict(sorted(tag_counts.items(), key=lambda item: (-item[1], item[0]))),
        "undeclared_unique_count": len(undeclared),
        "undeclared_instance_count": sum(undeclared.values()),
        "undeclared_tags": dict(sorted(undeclared.items(), key=lambda item: (-item[1], item[0]))),
        "declared_unused_tags": declared_unused,
        "high_frequency_candidates": high_frequency_candidates,
        "duplicate_tag_files": duplicate_tag_files,
        "files_by_tag": {tag: files_by_tag[tag] for tag in sorted(files_by_tag)},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit wiki frontmatter tags against SCHEMA.md taxonomy")
    parser.add_argument("--root", default=os.environ.get("OBSIDIAN_VAULT_PATH", DEFAULT_ROOT))
    parser.add_argument("--format", choices=["json", "text"], default="text")
    args = parser.parse_args()

    try:
        root = Path(args.root).expanduser().resolve()
        report = build_report(root)
    except Exception as exc:  # noqa: BLE001 - CLI boundary
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f"declared_count: {report['declared_count']}")
        print(f"tagged_pages: {report['tagged_pages']}")
        print(f"actual_unique_count: {report['actual_unique_count']}")
        print(f"undeclared_unique_count: {report['undeclared_unique_count']}")
        print(f"undeclared_instance_count: {report['undeclared_instance_count']}")
        print("top_undeclared:")
        for tag, count in list(report["undeclared_tags"].items())[:30]:
            print(f"  {tag}: {count}")

    return 1 if report["undeclared_unique_count"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
