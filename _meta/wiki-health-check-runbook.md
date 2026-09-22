---
title: Wiki health check runbook
created: 2026-05-11
updated: 2026-09-22
type: meta
status: current
---

# Wiki Health Check Runbook

## Summary

Use the repository-local scripts for deterministic structure, tag, public-boundary, provenance and raw-integrity checks. The scripts do not modify Hermes runtime layers. Only `wiki_raw_hashes.py` writes, and only to the raw hash manifest.

## Root resolution

All maintenance scripts resolve the repository root in this order:

1. explicit `--root`;
2. existing `OBSIDIAN_VAULT_PATH`;
3. the repository containing the script.

The fallback is independent of the caller's working directory and does not depend on a username. For isolation-sensitive work, pass `--root` explicitly and set `OBSIDIAN_VAULT_PATH` to the same clone.

## Core commands

From the repository root:

```bash
WIKI_ROOT=/path/to/wiki
python3 _meta/scripts/wiki_health_check.py --root "$WIKI_ROOT"
python3 _meta/scripts/wiki_health_check.py --root "$WIKI_ROOT" --format markdown
python3 _meta/scripts/wiki_tag_audit.py --root "$WIKI_ROOT"
python3 _meta/scripts/wiki_public_content_check.py --root "$WIKI_ROOT"
python3 -m unittest discover -s _meta/scripts -p 'test_*.py' -v
git diff --check
```

`wiki_health_check.py` and `wiki_tag_audit.py` are read-only. `wiki_public_content_check.py` scans every repository file outside `.git` and `__pycache__`; it does not exempt code blocks, `raw/` or `_meta/`. Local `git diff --check` covers uncommitted changes; CI separately checks the event commit range so a clean checkout cannot hide whitespace errors already committed.

## Local `[!volatile]` result contract

For each supported local block, `wiki_health_check.py` validates real `YYYY-MM-DD` values, `verified_at <= review_by`, non-future verification, expiry, and exact membership of the local `source` in page frontmatter `sources`.

- P1: malformed/unsupported block, malformed date, future `verified_at`, invalid date order, or undeclared local source.
- P2: `review_by` is earlier than the injected/current date. The due date itself remains valid; expiry begins the next day.
- Multiple blocks are independent. Fenced, inline and indented code examples are ignored.
- A passing block validates only that claim scope. It does not set or refresh page-level `verified_at` and does not imply that the whole page is current.
- The block and page-level freshness fields remain optional. Existing pages are not required to add or refresh them.

Unsupported block syntax is reported rather than treated as success. The supported syntax is defined in `SCHEMA.md`.

## Public-content result contract

- **Violation**: deterministic public-boundary failure; the command exits `1`.
- **Candidate**: possible personal instance record that needs content review; candidates do not fail the command by themselves.
- **PASS**: no blocking rule matched. It does not mean candidates were adjudicated, attachments were reviewed, or the repository is absolutely safe.
- Reports contain only repository-relative paths and rule names, never matched values.
- Files containing NUL bytes and files that do not decode as UTF-8 are candidates marked `unreviewed-binary-or-non-utf8`; they cannot be counted as reviewed until inspected with an appropriate tool.
- Generic product paths, configurable examples and obvious credential placeholders are allowed. A synthetic example does not prove deployment or authorization.

## Reverse lookup

```bash
WIKI_ROOT=/path/to/wiki
python3 _meta/scripts/wiki_reverse_lookup.py --root "$WIKI_ROOT" --source raw/articles/example.md
python3 _meta/scripts/wiki_reverse_lookup.py --root "$WIKI_ROOT" --page concepts/example.md
```

Modes are mutually exclusive. Source mode returns direct formal-page paths; page mode returns sorted `declared_by`, `relation`, `target` records. Empty matches return `[]`; unreadable or malformed input exits `2` with an error on stderr and no success result on stdout.

## Raw hash manifest

`_meta/scripts/wiki_raw_hashes.py` writes `_meta/raw-source-hashes.json`. Run it after adding an approved public raw source. A changed existing hash is a finding to explain, not noise to regenerate away.

A public-boundary remediation may remove private metadata from raw or delete an ineligible raw file. Record a non-personal reason in `log.md`, verify that the manifest diff is limited to the declared files, then commit content and manifest together.

```bash
python3 _meta/scripts/wiki_raw_hashes.py --root "$WIKI_ROOT"
```

## External-link check

`_meta/scripts/wiki_link_check.sh` uses `lychee` and the repository's `_meta/lychee.toml`. It needs network access and is separate from deterministic health checks. Install a supported `lychee` version through the operator's package or release-verification process; the repository does not claim a machine-local installation.

```bash
_meta/scripts/wiki_link_check.sh --root "$WIKI_ROOT"
```

Extra arguments are passed through to `lychee`.

## Minimal CI

`.github/workflows/wiki-checks.yml` runs on pull requests and pushes to `main` with read-only repository permission. It uses only repository scripts and the Python standard library:

1. unit tests;
2. Wiki health check;
3. tag audit;
4. public-content check;
5. `git diff --check` over the pull-request merge base or pushed commit range.

The workflow does not use secrets, `pull_request_target`, write permissions, metadata/raw-hash writers, network link checks or AI review. External-link liveness remains the separate operator command above because it is network-dependent.

## Exit codes

For the Python checks:

- `0`: check completed and no blocking finding exists;
- `1`: check completed and found a blocking violation;
- `2`: CLI or runtime error.

## Health-check scope

The structural health check covers core files, frontmatter, type/status/tag enums, wikilinks, relative Markdown links, index coverage, semantic inbound links, log order, raw references, raw hashes, duplicate-page signals, freshness metadata and Relations syntax. It does not replace content review for public suitability, source quality, contradictions or current product behavior.

## Related

- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
