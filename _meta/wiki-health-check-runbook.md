---
title: Wiki health check runbook
created: 2026-05-11
updated: 2026-09-03
type: meta
status: current
---

# Wiki Health Check Runbook

## Summary

Use `_meta/scripts/wiki_health_check.py` for deterministic, read-only health checks of this wiki.

The script is wiki-local tooling. It does not modify files, update `index.md`, write `log.md`, create cron jobs, or touch Hermes runtime layers.

## Commands

Run JSON output:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki
```

Run Markdown output:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format markdown
```

Use default root resolution:

```bash
python3 _meta/scripts/wiki_health_check.py
```

Run the offline regression fixtures:

```bash
python3 -m unittest discover -s _meta/scripts -p 'test_wiki_health_check.py' -v
```

The fixtures cover broken wikilinks, unregistered tags, raw-source drift, malformed `review_by`, near-duplicate pages, required frontmatter fields, formal status enums, and closed-query index lifecycle. They create isolated temporary vaults and never modify `/home/lin/wiki`.

Root resolution order:

1. `--root`
2. `OBSIDIAN_VAULT_PATH`
3. `/home/lin/wiki`

## Companion scripts

Two checks cannot live inside the health check without costing it a property it depends on, so they are separate commands.

`_meta/scripts/wiki_raw_hashes.py` writes `_meta/raw-source-hashes.json`, the SHA-256 manifest that makes `raw/` immutability enforceable. The health check only compares against it, which is what keeps the health check read-only. Run it after ingesting raw sources and commit the manifest diff:

```bash
python3 _meta/scripts/wiki_raw_hashes.py
```

`_meta/scripts/wiki_link_check.sh` checks that the external URLs cited by formal pages are still reachable, using `lychee` and `_meta/lychee.toml`. It needs the network, so its result is not reproducible from the files alone — that is why it is not a health-check code. Extra flags are passed through to `lychee`:

```bash
_meta/scripts/wiki_link_check.sh
```

`lychee` is a prebuilt binary at `~/.local/bin/lychee`, outside this repository and outside any package manager — this machine has neither `lychee` in its distro repos nor a Rust toolchain to build it. It is recorded here because nothing else records it:

- version `0.24.2`, asset `lychee-aarch64-unknown-linux-musl.tar.gz` from `github.com/lycheeverse/lychee`
- archive SHA-256 `5d0b0e3aeab240f41920c633a6eaf97599be6eedda034b36e858ede7dba5e535`, verified against the published `.sha256` before install
- installed binary SHA-256 `29bc0ac5c5ac3cfe9c312a5783a94f8fca33118d1a7bb687323eab0b52735f79`, statically linked

To reinstall or upgrade, download the matching asset, check it against its published checksum, and `install -m 755` it into `~/.local/bin/`. Update the values above when you do.

Its scope is formal pages only. `raw/` captures contain roughly ten times more URLs (598 against 63), and those belong to archived third-party text we already hold, so including them would bury the signal that matters: a formal page citing evidence that has since disappeared.

## Exit codes

- `0`: health check passed; no P0/P1 issues
- `1`: health check ran, but P0 or P1 issues exist
- `2`: CLI/runtime error, such as an unreadable root

## Severity policy

### P0

Immediate blockers:

- missing core files
- broken wikilinks
- broken index targets
- line-prefix pollution in current pages

### P1

Important issues:

- broken relative Markdown links
- formal page missing H1
- formal page missing frontmatter
- formal page missing any required frontmatter field
- formal page whose `type` or `status` is outside the `SCHEMA.md` enum
- unexpected unindexed formal pages
- unreferenced raw source pages
- formal page carrying a tag not registered in the `SCHEMA.md` tag taxonomy
- `SCHEMA.md` tag taxonomy missing or unparseable, meaning tag registration is no longer enforced
- formal page whose `review_by` is not a plain `YYYY-MM-DD` date, meaning the expiry it declares can never fire
- raw source whose content no longer matches its recorded SHA-256, meaning pages citing it may no longer describe what it says
- `_meta/raw-source-hashes.json` missing or unparseable, meaning `raw/` immutability is no longer enforced
- non-markdown sidecar file in `_meta/reviews/`, violating `SCHEMA.md` review retention rules

### P2

Maintenance findings:

- tiny files
- remaining in-vault backup candidates
- known unindexed draft query pages
- formal page whose `review_by` date has passed and is due for a re-read
- raw source with no entry in `_meta/raw-source-hashes.json`, usually a new ingestion whose manifest update was skipped
- two formal pages overlapping above the near-duplicate threshold, usually the same subject ingested twice
- formal page with malformed `## Relations` line or relation key outside the `SCHEMA.md` whitelist

`queries/` pages with `status: closed` may stay outside the main index without producing a finding; Git history and direct search remain their archive path.

The `known_unindexed_draft_query` code currently has no instances. The eight draft query pages it was written for were deleted on 2026-05-15 at the user's request; see [[draft-query-inventory]]. The code is retained for future draft query pages, not because any exist today.

## Current expected result

As of 2026-08-18, the script passes on `/home/lin/wiki`.

Expected current interpretation:

- P0: `0`
- P1: `0`
- P2: `0`
- `pass`: `true`

Any nonzero count is a real finding, not a known-noise allowance.

`near_duplicate_pages` uses a Jaccard threshold of `0.45`, calibrated on 2026-08-11 against all 5995 formal-page pairs: median `0.055`, p99 `0.137`, observed max `0.270`. A half-rewritten copy of an existing page measures `0.566` and a verbatim copy `1.000`, so the threshold sits in the gap between real topic overlap and real duplication. Recalibrate it if the corpus changes shape; do not raise it to silence a finding.

`page_due_for_review` is the only check whose result changes over time on unchanged files: three pages carry `review_by: 2026-11-11`, so P2 is expected to become nonzero on that date without anything in the wiki having been edited. Clear it by re-reading those pages against their current upstream subject and either bumping `review_by` or correcting the page — not by deleting the field.

## When to run

- After adding or editing formal wiki pages
- After source ingestion sessions
- Before and after larger wiki cleanup
- Before creating any scheduled wiki-health cron job

## What this does not replace

This script catches structural issues. It does not replace human or AI review for:

- conceptual contradictions
- source-quality judgment
- stale conclusions that require domain knowledge
- whether a draft should become stable
- whether a workflow should be promoted to skill or cron

## Related

- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[draft-query-inventory]]
- [[index]]
- [[log]]
