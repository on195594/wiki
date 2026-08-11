#!/usr/bin/env python3
"""Write the SHA-256 manifest that lets wiki_health_check.py detect raw/ drift.

SCHEMA.md calls raw/ immutable, but nothing enforced that: a raw capture could
be edited after a formal page cited it, and the citation would still resolve
while no longer pointing at what was read. This script records the hashes;
wiki_health_check.py only compares them, so it stays read-only.

Run it after ingesting new raw sources, and commit the manifest diff. A changed
hash on an existing file is a finding to explain, not noise to regenerate away.

Exit codes:
  0: manifest written (stdout says whether anything changed)
  2: CLI/runtime error
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

MANIFEST = "_meta/raw-source-hashes.json"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def raw_files(root: Path) -> list[Path]:
    return sorted(p for p in (root / "raw").rglob("*") if p.is_file())


def build_manifest(root: Path) -> dict[str, str]:
    return {p.relative_to(root).as_posix(): file_sha256(p) for p in raw_files(root)}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write the raw/ SHA-256 manifest")
    parser.add_argument("--root", default=os.environ.get("OBSIDIAN_VAULT_PATH", "/home/lin/wiki"))
    args = parser.parse_args(argv)

    try:
        root = Path(args.root).expanduser().resolve()
        manifest_path = root / MANIFEST
        current = build_manifest(root)
        previous: dict[str, str] = {}
        if manifest_path.exists():
            previous = json.loads(manifest_path.read_text(encoding="utf-8"))
        manifest_path.write_text(json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    except Exception as exc:  # noqa: BLE001 - CLI error path should be explicit and compact.
        print(f"error: {exc}", file=sys.stderr)
        return 2

    added = sorted(set(current) - set(previous))
    removed = sorted(set(previous) - set(current))
    changed = sorted(k for k in set(current) & set(previous) if current[k] != previous[k])
    print(f"{MANIFEST}: {len(current)} files (added {len(added)}, removed {len(removed)}, changed {len(changed)})")
    for label, items in (("changed", changed), ("removed", removed)):
        for item in items:
            print(f"  {label}: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
