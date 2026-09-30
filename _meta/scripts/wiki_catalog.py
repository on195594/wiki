#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from wiki_health_check import (
    ALLOWED_RELATION_KEYS,
    extract_frontmatter,
    frontmatter_value,
    is_formal_page,
    is_live_file,
    parse_inline_list,
    rel,
    strip_code,
)
from wiki_root import resolve_root

DEFAULT_CATALOG_PATH = "_meta/catalog.json"


def extract_relations(text: str) -> dict[str, list[str]]:
    clean_body = strip_code(text)
    match = re.search(r"^##\s+Relations\s*$", clean_body, flags=re.M)
    if not match:
        return {}
    section = clean_body[match.end() :]
    next_heading = re.search(r"^##\s+", section, flags=re.M)
    if next_heading:
        section = section[: next_heading.start()]

    relations: dict[str, list[str]] = {}
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        line_content = line[2:].strip()
        if ":" not in line_content:
            continue
        k, v = line_content.split(":", 1)
        k = k.strip()
        v = v.strip()
        if k in ALLOWED_RELATION_KEYS:
            if v == "[]":
                relations.setdefault(k, [])
            else:
                links = [l.strip() for l in re.findall(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]", v)]
                existing = relations.setdefault(k, [])
                for link in links:
                    if link not in existing:
                        existing.append(link)
    return relations


def build_catalog(root: Path) -> dict[str, Any]:
    formal_files: list[Path] = []
    for path in sorted(root.rglob("*.md")):
        if is_live_file(root, path) and is_formal_page(root, path):
            formal_files.append(path)

    pages: list[dict[str, Any]] = []
    for path in formal_files:
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text) or ""
        p_rel = rel(root, path)

        tags_val = frontmatter_value(fm, "tags") or ""
        aliases_val = frontmatter_value(fm, "aliases") or ""

        page_data: dict[str, Any] = {
            "path": p_rel,
            "type": frontmatter_value(fm, "type") or "",
            "title": frontmatter_value(fm, "title") or path.stem,
            "description": frontmatter_value(fm, "description") or "",
            "status": frontmatter_value(fm, "status") or "",
            "tags": parse_inline_list(tags_val),
            "aliases": parse_inline_list(aliases_val),
            "volatility": frontmatter_value(fm, "volatility"),
            "review_by": frontmatter_value(fm, "review_by"),
            "verified_at": frontmatter_value(fm, "verified_at"),
            "updated": frontmatter_value(fm, "updated") or "",
            "relations": extract_relations(text),
        }
        pages.append(page_data)

    return {
        "format": "okf-bundle-catalog",
        "version": "0.2",
        "total_pages": len(pages),
        "pages": pages,
    }


def write_catalog(root: Path, output_path: Path | None = None) -> Path:
    target = output_path or (root / DEFAULT_CATALOG_PATH)
    data = build_catalog(root)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return target


def check_catalog(root: Path, catalog_path: Path | None = None) -> bool:
    target = catalog_path or (root / DEFAULT_CATALOG_PATH)
    if not target.exists():
        return False
    current_catalog = json.dumps(build_catalog(root), indent=2, ensure_ascii=False) + "\n"
    on_disk = target.read_text(encoding="utf-8")
    return current_catalog == on_disk


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or verify OKF-aligned wiki catalog")
    parser.add_argument("--root", help="Wiki root directory")
    parser.add_argument("--check", action="store_true", help="Check that catalog.json is up-to-date")
    parser.add_argument("--output", help="Output catalog JSON path")
    args = parser.parse_args()

    root = resolve_root(args.root)
    output_path = Path(args.output).resolve() if args.output else None

    if args.check:
        if check_catalog(root, output_path):
            print("OK: catalog is up to date.")
            return 0
        else:
            print("ERROR: catalog is missing or out-of-date. Run wiki_catalog.py without --check to update.")
            return 1

    written = write_catalog(root, output_path)
    try:
        display_path = rel(root, written)
    except ValueError:
        display_path = str(written)
    print(f"Generated catalog at {display_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
