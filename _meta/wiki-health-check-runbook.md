---
title: Wiki health check runbook
created: 2026-05-11
updated: 2026-09-20
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

`wiki_health_check.py` and `wiki_tag_audit.py` are read-only. `wiki_public_content_check.py` scans every repository file outside `.git` and `__pycache__`; it does not exempt code blocks, `raw/` or `_meta/`.

## Public-content result contract

- **Violation**: deterministic public-boundary failure; the command exits `1`.
- **Candidate**: possible personal instance record that needs content review; candidates do not fail the command by themselves.
- Reports contain only repository-relative paths and rule names, never matched values.
- Binary or non-UTF-8 files are candidates marked `unreviewed-binary-or-non-utf8`; they cannot be counted as reviewed until inspected with an appropriate tool.
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
