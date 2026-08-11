---
title: Wiki health check runbook
created: 2026-05-11
updated: 2026-08-11
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

Root resolution order:

1. `--root`
2. `OBSIDIAN_VAULT_PATH`
3. `/home/lin/wiki`

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
- unexpected unindexed formal pages
- unreferenced raw source pages
- formal page carrying a tag not registered in the `SCHEMA.md` tag taxonomy
- `SCHEMA.md` tag taxonomy missing or unparseable, meaning tag registration is no longer enforced
- formal page whose `review_by` is not a plain `YYYY-MM-DD` date, meaning the expiry it declares can never fire

### P2

Maintenance findings:

- tiny files
- remaining in-vault backup candidates
- known unindexed draft query pages
- formal page whose `review_by` date has passed and is due for a re-read

The `known_unindexed_draft_query` code currently has no instances. The eight draft query pages it was written for were deleted on 2026-05-15 at the user's request; see [[draft-query-inventory]]. The code is retained for future draft query pages, not because any exist today.

## Current expected result

As of 2026-08-11, the script passes on `/home/lin/wiki`.

Expected current interpretation:

- P0: `0`
- P1: `0`
- P2: `0`
- `pass`: `true`

Any nonzero count is a real finding, not a known-noise allowance.

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
