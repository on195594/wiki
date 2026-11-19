#!/usr/bin/env python3
"""Emit unique HTTP(S) source URLs from raw Markdown frontmatter, not bodies."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from wiki_health_check import extract_frontmatter
from wiki_root import resolve_root


def source_urls(root: Path) -> list[str]:
    urls: set[str] = set()
    for path in (root / "raw").rglob("*.md"):
        frontmatter = extract_frontmatter(path.read_text(encoding="utf-8"))
        if frontmatter is None:
            continue
        source = re.search(r"^source_url:[ \t]*(\S[^\r\n]*)$", frontmatter, flags=re.M)
        if source:
            url = source[1].strip()
            if len(url) >= 2 and url[0] in "\"'" and url[0] == url[-1]:
                url = url[1:-1]
            if re.fullmatch(r"https?://[^\s<>]+", url, flags=re.I):
                urls.add(url)
    return sorted(urls)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path)
    args = parser.parse_args()
    for url in source_urls(resolve_root(args.root)):
        print(url)


if __name__ == "__main__":
    main()
