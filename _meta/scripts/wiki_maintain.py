#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from wiki_catalog import check_catalog, write_catalog
from wiki_health_check import (
    build_report as build_health_report,
    extract_frontmatter,
    frontmatter_value,
    is_formal_page,
    is_live_file,
    parse_review_by,
    rel,
)
from wiki_public_content_check import build_report as build_public_content_report
from wiki_raw_hashes import MANIFEST as RAW_HASH_MANIFEST, build_manifest as build_raw_manifest
from wiki_root import resolve_root
from wiki_tag_audit import build_report as build_tag_report

HOOK_SIGNATURE = "# Wiki pre-commit hook: automated enforcement of catalog, health, tags, privacy, and tests"


def run_unit_tests(root: Path) -> bool:
    loader = unittest.defaultTestLoader
    scripts_dir = root / "_meta" / "scripts"
    suite = loader.discover(str(scripts_dir), pattern="test_*.py")
    runner = unittest.TextTestRunner(stream=sys.stdout, verbosity=1)
    result = runner.run(suite)
    return result.wasSuccessful()


def check_git_diff(root: Path, staged: bool = False) -> bool:
    try:
        cmd = ["git", "diff", "--check"]
        if staged:
            cmd.insert(2, "--cached")
        proc = subprocess.run(
            cmd,
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        if proc.returncode != 0:
            print(f"ERROR: {' '.join(cmd)} reported whitespace or conflict errors:\n" + proc.stdout + proc.stderr, file=sys.stderr)
            return False
        return True
    except Exception as exc:
        print(f"WARN: could not run git diff: {exc}", file=sys.stderr)
        return True


def check_all(root: Path, is_staged: bool = False) -> bool:
    print(f"=== Running Wiki Maintenance Checks ({'staged snapshot' if is_staged else 'working tree'}) ===")
    all_ok = True

    # 1. Unit tests
    print("[1/6] Running unit tests...")
    if not run_unit_tests(root):
        print("FAIL: Unit tests failed.", file=sys.stderr)
        all_ok = False
    else:
        print("PASS: All unit tests passed.")

    # 2. Catalog sync check
    print("[2/6] Checking catalog.json synchronization...")
    if not check_catalog(root):
        print("FAIL: _meta/catalog.json is missing or out-of-date. Run 'python3 _meta/scripts/wiki_maintain.py --fix' to sync.", file=sys.stderr)
        all_ok = False
    else:
        print("PASS: catalog.json is up-to-date.")

    # 3. Health check
    print("[3/6] Running Wiki health check...")
    health = build_health_report(root)
    p0 = health["issues"]["P0"]
    p1 = health["issues"]["P1"]
    p2 = health["issues"]["P2"]
    if p0 or p1 or p2:
        print(f"FAIL: Health check found issues: P0={len(p0)}, P1={len(p1)}, P2={len(p2)}", file=sys.stderr)
        for issue in p0 + p1 + p2:
            print(f"  - [{issue.get('code')}] {issue.get('path')}: {issue.get('message')}", file=sys.stderr)
        all_ok = False
    else:
        print("PASS: Health check passed with 0 issues.")

    # 4. Tag audit
    print("[4/6] Running tag taxonomy audit...")
    tag_report = build_tag_report(root)
    undeclared = tag_report.get("undeclared_instance_count", 0)
    if undeclared > 0:
        print(f"FAIL: Tag audit found {undeclared} undeclared tag instances.", file=sys.stderr)
        all_ok = False
    else:
        print("PASS: Tag taxonomy audit passed (0 undeclared tags).")

    # 5. Public content check
    print("[5/6] Checking public boundary and privacy...")
    public_rep = build_public_content_report(root)
    violations = public_rep.get("violations", [])
    if violations:
        print(f"FAIL: Public content check found {len(violations)} blocking violations.", file=sys.stderr)
        all_ok = False
    else:
        print("PASS: Public boundary check passed (0 violations).")

    # 6. Git diff check
    if not is_staged:
        print("[6/6] Checking git whitespace and format...")
        if not check_git_diff(root):
            all_ok = False
        else:
            print("PASS: Git diff format clean.")
    else:
        print("[6/6] Staged diff whitespace verified.")

    print("========================================")
    if all_ok:
        print("ALL CHECKS PASSED: Wiki is fully healthy and synchronized.")
    else:
        print("CHECKS FAILED: Please fix reported issues above.", file=sys.stderr)
    return all_ok


def check_staged(root: Path) -> bool:
    print("=== Checking Staged Index (pre-commit gate) ===")
    if not check_git_diff(root, staged=True):
        return False

    proc = subprocess.run(["git", "diff", "--cached", "--name-only"], cwd=root, capture_output=True, text=True, check=False)
    staged_files = [f.strip() for f in proc.stdout.splitlines() if f.strip()]
    if not staged_files:
        print("No staged changes to verify; checking working tree.")
        return check_all(root)

    with tempfile.TemporaryDirectory() as tmp_dir:
        staged_root = Path(tmp_dir) / "staged"
        staged_root.mkdir(parents=True)
        prefix = str(staged_root) + "/"
        res = subprocess.run(
            ["git", "checkout-index", f"--prefix={prefix}", "-a"],
            cwd=root,
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode != 0:
            print(f"ERROR: Failed to export staged index ({res.stderr.strip()}). Aborting pre-commit gate.", file=sys.stderr)
            return False

        staged_script = staged_root / "_meta" / "scripts" / "wiki_maintain.py"
        if not staged_script.exists():
            print("ERROR: Staged index is missing _meta/scripts/wiki_maintain.py.", file=sys.stderr)
            return False

        sub = subprocess.run(
            [sys.executable, str(staged_script), "--root", str(staged_root), "--check", "--snapshot-mode"],
            cwd=staged_root,
            check=False,
        )
        return sub.returncode == 0


def fix_all(root: Path) -> bool:
    print("=== Auto-syncing Wiki Metadata and Manifests ===")

    # 1. Update raw hash manifest with drift protection (SCHEMA.md:32)
    raw_manifest_path = root / RAW_HASH_MANIFEST
    current_raw = build_raw_manifest(root)
    previous_raw: dict[str, str] = {}
    if raw_manifest_path.exists():
        try:
            previous_raw = json.loads(raw_manifest_path.read_text(encoding="utf-8"))
        except Exception as exc:
            print(f"ERROR: Cannot auto-fix: existing raw hash manifest at {raw_manifest_path} is unreadable or corrupted: {exc}", file=sys.stderr)
            print("Per SCHEMA.md:32, you must restore a valid manifest baseline before auto-fixing.", file=sys.stderr)
            return False

        if not isinstance(previous_raw, dict) or not all(
            isinstance(k, str) and isinstance(v, str) and len(v) == 64 and all(c in "0123456789abcdefABCDEF" for c in v)
            for k, v in previous_raw.items()
        ):
            print(
                f"ERROR: Cannot auto-fix: existing raw hash manifest at {raw_manifest_path} is structurally invalid "
                "(must be a JSON object mapping file paths to 64-character SHA-256 hex digests).",
                file=sys.stderr,
            )
            print("Per SCHEMA.md:32, you must restore a valid manifest baseline before auto-fixing.", file=sys.stderr)
            return False

    drifted = [k for k in previous_raw if k in current_raw and previous_raw[k] != current_raw[k]]
    if drifted:
        print(f"ERROR: Cannot auto-fix: detected {len(drifted)} raw source file(s) with changed hashes (drift):", file=sys.stderr)
        for d in drifted:
            print(f"  - {d}: previous={previous_raw[d]}, current={current_raw[d]}", file=sys.stderr)
        print("Per SCHEMA.md:32, existing raw hash changes must be investigated and explained, not silently overwritten.", file=sys.stderr)
        return False

    merged_raw = dict(previous_raw)
    added_count = 0
    for k, v in current_raw.items():
        if k not in merged_raw:
            merged_raw[k] = v
            added_count += 1

    removed_count = 0
    for k in list(merged_raw.keys()):
        if k not in current_raw:
            del merged_raw[k]
            removed_count += 1

    raw_manifest_path.parent.mkdir(parents=True, exist_ok=True)
    raw_manifest_path.write_text(json.dumps(merged_raw, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Updated {RAW_HASH_MANIFEST} (total {len(merged_raw)}, added {added_count}, removed {removed_count})")

    # 2. Update catalog.json
    written_cat = write_catalog(root)
    try:
        cat_display = rel(root, written_cat)
    except ValueError:
        cat_display = str(written_cat)
    print(f"Updated {cat_display}")

    print("Auto-sync complete. Run '--check' to verify health.")
    return True


def report_freshness(root: Path, days: int = 30) -> list[dict[str, Any]]:
    today = datetime.now(timezone.utc).date()
    horizon = today + timedelta(days=days)

    formal_files = [p for p in sorted(root.rglob("*.md")) if is_live_file(root, p) and is_formal_page(root, p)]
    items: list[dict[str, Any]] = []

    for path in formal_files:
        text = path.read_text(encoding="utf-8")
        fm = extract_frontmatter(text) or ""
        rev_val = frontmatter_value(fm, "review_by")
        vol_val = frontmatter_value(fm, "volatility")
        if not rev_val and vol_val != "high":
            continue

        rev_date = parse_review_by(rev_val) if rev_val else None
        p_rel = rel(root, path)

        if rev_date is None and vol_val == "high":
            items.append({
                "path": p_rel,
                "status": "missing_review_by",
                "volatility": vol_val,
                "review_by": None,
                "days_left": None,
            })
        elif rev_date is not None:
            days_left = (rev_date - today).days
            if days_left < 0:
                items.append({
                    "path": p_rel,
                    "status": "expired",
                    "volatility": vol_val,
                    "review_by": rev_date.isoformat(),
                    "days_left": days_left,
                })
            elif rev_date <= horizon:
                items.append({
                    "path": p_rel,
                    "status": "expiring_soon",
                    "volatility": vol_val,
                    "review_by": rev_date.isoformat(),
                    "days_left": days_left,
                })

    print(f"=== Wiki Freshness Report (Horizon: {days} days, Today: {today.isoformat()}) ===")
    if not items:
        print("All pages with review_by are within safe date windows.")
    else:
        for it in items:
            stat = it["status"]
            if stat == "expired":
                print(f"[EXPIRED] {it['path']}: expired {abs(it['days_left'])} days ago (due {it['review_by']})")
            elif stat == "expiring_soon":
                print(f"[EXPIRING SOON] {it['path']}: {it['days_left']} days left (due {it['review_by']})")
            elif stat == "missing_review_by":
                print(f"[MISSING REVIEW_BY] {it['path']}: high volatility without review_by")
    return items


def get_git_hooks_dir(root: Path) -> Path:
    try:
        proc = subprocess.run(
            ["git", "rev-parse", "--git-path", "hooks"],
            cwd=root,
            capture_output=True,
            text=True,
            check=True,
        )
        p = Path(proc.stdout.strip())
        return p if p.is_absolute() else (root / p).resolve()
    except Exception:
        return (root / ".git" / "hooks").resolve()


def install_git_hook(root: Path, force: bool = False) -> Path:
    hooks_dir = get_git_hooks_dir(root)
    hooks_dir.mkdir(parents=True, exist_ok=True)

    pre_commit_path = hooks_dir / "pre-commit"
    if pre_commit_path.exists() and not force:
        existing = pre_commit_path.read_text(encoding="utf-8")
        if HOOK_SIGNATURE not in existing:
            raise RuntimeError(
                f"Existing pre-commit hook found at {pre_commit_path} not generated by wiki_maintain. "
                "Use --force to overwrite, or manually integrate the wiki check."
            )

    hook_content = f"""#!/usr/bin/env bash
{HOOK_SIGNATURE}
set -e

if [ -n "$SKIP_WIKI_CHECKS" ]; then
  exit 0
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

python3 "$REPO_ROOT/_meta/scripts/wiki_maintain.py" --root "$REPO_ROOT" --staged
"""
    pre_commit_path.write_text(hook_content, encoding="utf-8")
    pre_commit_path.chmod(0o755)
    try:
        display = rel(root, pre_commit_path)
    except ValueError:
        display = str(pre_commit_path)
    print(f"Installed pre-commit hook at {display}")
    return pre_commit_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Wiki automated maintenance and quality gate CLI")
    parser.add_argument("--root", help="Wiki root directory")
    parser.add_argument("--check", action="store_true", help="Run all deterministic validation gates (default mode)")
    parser.add_argument("--snapshot-mode", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--staged", action="store_true", help="Run validation on git staged index snapshot")
    parser.add_argument("--fix", action="store_true", help="Auto-sync catalog.json and raw hash manifest with drift protection")
    parser.add_argument("--freshness", action="store_true", help="Scan and report pages expiring soon or overdue")
    parser.add_argument("--days", type=int, default=30, help="Days horizon for freshness scan (default 30)")
    parser.add_argument("--install-hooks", action="store_true", help="Install Git pre-commit hook")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing hooks when installing")
    args = parser.parse_args()

    root = resolve_root(args.root)

    if args.install_hooks:
        try:
            install_git_hook(root, force=args.force)
            return 0
        except Exception as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 1

    if args.fix:
        success = fix_all(root)
        return 0 if success else 1

    if args.freshness:
        report_freshness(root, args.days)
        return 0

    if args.staged:
        success = check_staged(root)
        return 0 if success else 1

    success = check_all(root, is_staged=args.snapshot_mode)
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
