#!/usr/bin/env python3
"""Read-only, on-demand source and relation lookup; stdout is a sorted JSON list."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

from wiki_health_check import (
    ALLOWED_RELATION_KEYS, RELATION_VALUE_PATTERN, extract_frontmatter,
    frontmatter_value, is_formal_page, is_live_file, rel, strip_code,
)


def sources(frontmatter: str) -> list[str]:
    """Accept the Wiki's inline lists and indented block lists, fail on ambiguity."""
    matches = list(re.finditer(r"^sources:[ \t]*(.*)$", frontmatter, re.M))
    if len(matches) != 1:
        raise ValueError("expected exactly one sources field")
    match = matches[0]
    value = match.group(1).strip()
    if not value:
        block = re.split(r"^[^ \t\n]", frontmatter[match.end():], maxsplit=1, flags=re.M)[0]
        lines = [line for line in block.splitlines() if line.strip()]
        items = [re.fullmatch(r"[ \t]+-[ \t]+(\S.*)", line) for line in lines]
        if not items or any(item is None for item in items):
            raise ValueError("invalid sources block list")
        result = []
        for item in items:
            scalar = item[1].strip()
            if scalar[:1] in {"'", '"'}:
                if len(scalar) < 2 or scalar[-1] != scalar[0]:
                    raise ValueError("invalid quoted source item")
                scalar = scalar[1:-1]
            if not scalar or any(char in scalar for char in "[]{}\n"):
                raise ValueError("invalid source item")
            result.append(scalar)
        return result
    elif not (value.startswith("[") and value.endswith("]")):
        raise ValueError("sources must be a list")
    value = frontmatter_value(frontmatter, "sources") or ""
    # Wiki source identifiers are plain strings or quoted strings. Unsupported
    # YAML constructs fail explicitly rather than silently changing an edge.
    token = r'''(?:'[^'\n]+'|"[^"\n]+"|[^\s,\[\]{}'"#]+)'''
    if not re.fullmatch(r"\[\s*(?:" + token + r"(?:\s*,\s*" + token + r")*)?\s*\]", value):
        raise ValueError("invalid or unsupported source list")
    items = re.findall(token, value[1:-1])
    return [item[1:-1] if item[:1] in {"'", '"'} else item for item in items]


def resolve_target(root: Path, current: Path, target: str, pages: list[Path]) -> str:
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    if not target:
        return rel(root, current)
    if "/" not in target and not target.endswith(".md"):
        candidates = {p for p in pages if p.stem == target}
    else:
        names = [target] if target.endswith(".md") else [target, target + ".md"]
        candidates = {(base / name).resolve() for base in (root, current.parent) for name in names}
        candidates.intersection_update(pages)
    if len(candidates) != 1:
        raise ValueError(f"unresolved or ambiguous relation target {target!r}: {sorted(str(p) for p in candidates)}")
    return rel(root, candidates.pop())


def markdown_pages(root: Path) -> list[Path]:
    def scan_error(error: OSError) -> None:
        raise error

    pages = []
    for directory, dirs, files in os.walk(root, onerror=scan_error):
        dirs[:] = [d for d in dirs if is_live_file(root, Path(directory) / d)]
        if any((Path(directory) / d).is_symlink() for d in dirs):
            raise ValueError(f"symlinked Wiki directory is not supported: {directory}")
        pages.extend(Path(directory) / f for f in files if f.endswith(".md") and is_live_file(root, Path(directory) / f))
    return sorted(pages)


def lookup(root: Path, *, source: str | None = None, page: str | None = None) -> list:
    root = root.expanduser().resolve()
    if not root.is_dir():
        raise ValueError(f"wiki root is not a directory: {root}")
    if (source is None) == (page is None):
        raise ValueError("specify exactly one of source or page")
    if source is not None and not source.strip():
        raise ValueError("source must not be empty")
    # No persisted index: Markdown remains canonical, one scan per query.
    pages = markdown_pages(root)
    if any(p.resolve() != p or not p.resolve().is_relative_to(root) for p in pages):
        raise ValueError("symlinked Markdown is not supported")
    if page is not None:
        target = root / page
        if Path(page).is_absolute() or not target.resolve().is_relative_to(root):
            raise ValueError("page must be a Wiki-relative path")
        target = target.resolve()
        if target not in pages:
            raise ValueError(f"page does not exist: {page}")
        target.read_text(encoding="utf-8")  # Never treat unreadable input as no matches.
        page = rel(root, target)
    dependents: set[str] = set()
    relations: set[tuple[str, str, str]] = set()
    for path in pages:
        if not is_formal_page(root, path):
            continue
        try:
            text = path.read_text(encoding="utf-8")
            fm = extract_frontmatter(text)
            if fm is None:
                raise ValueError("missing or malformed frontmatter")
            page_sources = sources(fm)
            if source is not None:
                if source in page_sources:
                    dependents.add(rel(root, path))
                continue
            body = strip_code(text.split("\n---", 1)[1])
            sections = list(re.finditer(r"^##[ \t]+Relations[ \t]*$", body, re.M))
            for section in sections:
                block = re.split(r"^#{1,2}[ \t]+", body[section.end():], maxsplit=1, flags=re.M)[0]
                for line in block.splitlines():
                    if not line.strip() or line.lstrip().startswith("#"):
                        continue
                    match = re.fullmatch(r"\s*- ([a-z_]+):\s*(.*?)\s*", line)
                    if not match or match[1] not in ALLOWED_RELATION_KEYS or not RELATION_VALUE_PATTERN.fullmatch(match[2]):
                        raise ValueError(f"invalid Relations line: {line}")
                    for link in re.findall(r"\[\[([^\]]+)\]\]", match[2]):
                        resolved = resolve_target(root, path, link, pages)
                        if resolved == page:
                            relations.add((rel(root, path), match[1], resolved))
        except (OSError, UnicodeError, ValueError) as exc:
            raise ValueError(f"{rel(root, path)}: {exc}") from exc
    if source is not None:
        return sorted(dependents)
    return [{"declared_by": p, "relation": k, "target": t} for p, k, t in sorted(relations)]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=os.environ.get("OBSIDIAN_VAULT_PATH", "/home/lin/wiki"))
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--source")
    mode.add_argument("--page")
    args = parser.parse_args(argv)
    try:
        result = lookup(Path(args.root), source=args.source, page=args.page)
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
