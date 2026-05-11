---
title: Wiki health check automation plan
created: 2026-05-11
updated: 2026-05-11
type: meta
status: completed
---

# Wiki Health Check Automation Plan

## Goal

Create a repeatable, deterministic, read-only wiki health check for `/home/lin/wiki` so future audits do not depend on ad hoc Python snippets or model-only judgment.

## Scope

This phase will create:

1. A deterministic script: `_meta/scripts/wiki_health_check.py`
2. A short runbook: `_meta/wiki-health-check-runbook.md`
3. A log entry in `log.md`

The script will output JSON by default and a concise Markdown report with `--format markdown`.

## Non-scope

This phase will not:

- Create or modify cron jobs
- Change Hermes runtime config, gateway routing, memory, skills, MCP, or `SOUL.md`
- Delete or rewrite wiki content
- Auto-fix broken links or index coverage
- Promote draft query pages into `index.md`
- Move archived/draft files

## Layer routing

- Script: wiki-local tooling under `_meta/scripts/`
- Runbook: wiki-local meta documentation under `_meta/`
- Log entry: wiki audit trail in `log.md`
- No memory entry
- No skill promotion in this phase
- No cron scheduling in this phase

## Current baseline evidence

- Vault path: `/home/lin/wiki`
- Git status before planning: clean on `main`
- Existing standards: `concepts/hermes-wiki-lint-and-health-check-standards.md`
- Existing draft inventory: `_meta/draft-query-inventory.md`
- Existing operational page: `operations/hermes-health-dashboard.md`
- Current health findings from the previous audit:
  - live markdown pages: 107 before draft-inventory page, 108 after it
  - broken wikilinks: 0
  - broken relative Markdown links: 0
  - line-prefix pollution: 0
  - formal page missing frontmatter: 0
  - in-vault backup candidates: 0 after backup cleanup
  - unindexed formal pages: 8 known draft query pages, intentionally left outside `index.md`

## Script checks

The script should:

1. Resolve the vault path from `--root`, `OBSIDIAN_VAULT_PATH`, or `/home/lin/wiki`.
2. Exclude `.git/`, `_backups/`, and files whose name contains `.bak.` from live-page checks.
3. Count live markdown files and directory distribution.
4. Check current live pages for:
   - line-prefix pollution matching `^\d+\|` near the start of a file
   - empty files
   - tiny files below 120 non-whitespace characters
   - missing H1 heading on formal live pages, excluding root core files and `_meta/`
   - missing frontmatter on formal pages, excluding root core files and `_meta/`
5. Resolve `[[wikilinks]]` by stem and relative/vault path, while ignoring code fences and inline-code examples.
6. Resolve relative Markdown links against the filesystem, while ignoring external URLs and anchors.
7. Parse `index.md` wikilinks and report:
   - index target links that do not resolve
   - formal pages missing from the main index
   - whether missing-index pages are draft query pages
8. Check `raw/` pages for at least one non-raw reference by raw stem, relative path, or wikilink target.
9. Count remaining in-vault backup candidates.
10. Include git status if the vault is a git repo.
11. Produce severity buckets:
   - P0: broken wikilinks, broken index targets, missing core files, line-prefix pollution in current pages
   - P1: broken relative Markdown links, formal pages missing H1/frontmatter, unreferenced raw source pages, unexpected unindexed non-draft formal pages
   - P2: tiny files, remaining backup candidates, known unindexed draft query pages

## Output contract

JSON output should include:

- `root`
- `counts`
- `git_status`
  - `is_repo`
  - `branch_line`
  - `short_status`
  - `dirty`
- `issues` grouped by `P0`, `P1`, `P2`
- `notes`
  - expected benign findings and interpretation hints, such as known unindexed draft queries, code-span wikilink examples, or excluded meta/core files
- `pass`

`pass` should be true only when P0 and P1 are empty.

The script should exit with code `0` when `pass` is true and code `1` when P0 or P1 issues make `pass` false. CLI/runtime errors, such as an unreadable root, should use exit code `2`.

Markdown output should lead with the conclusion and then list key counts and issues by severity.

## Verification gates

After implementation:

1. Run:
   - `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki`
   - `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format markdown`
2. Confirm JSON is parseable and `pass` is true for the current wiki state.
3. Confirm the eight known draft query pages appear as P2 or notes, not as P0/P1.
4. Run `git diff --check`.
5. Confirm wikilinks remain valid after adding the runbook.
6. Commit only intentional wiki-local artifacts.

## Third-party review gate

Before implementation, run a read-only third-party AI review of this plan. Ask the reviewer to check:

- Whether the scope is narrow enough
- Whether any active Hermes layer is accidentally being promoted
- Whether the script checks match the existing wiki standards
- Whether output/pass criteria are too strict or too loose
- Whether any missing verification step could cause false confidence

Accepted review findings should be patched into this plan before implementation.

### Review result

Reviewer: Gemini CLI with `gemini-2.5-flash`, read-only plan mode, 2026-05-11.

Verdict: no Blocking findings. The plan is executable and scoped correctly.

Accepted findings patched into this plan:

1. Add explicit exit-code semantics: `0` for pass, `1` for P0/P1 failure, `2` for CLI/runtime errors.
2. Make `git_status` more detailed than a clean/dirty boolean.
3. Define expected `notes` content.
4. Apply the same formal-page exclusion logic to missing-H1 checks as to frontmatter checks.

Deferred finding:

- Fixture vault regression tests are useful for a later hardening phase, but not required for this small first implementation. This phase will keep fixture creation out of scope to avoid turning wiki-local tooling into a larger test project.

## Stop conditions

Stop and ask the user if:

- The review recommends cron/runtime/memory/skill changes as required for this phase
- The script would need to mutate wiki files to pass
- The current wiki has a P0/P1 issue that should be fixed before creating a reusable health checker
- Any command would expose credentials or read outside the wiki/backups scope unnecessarily

## Execution result

Implemented on 2026-05-11.

Created:

- `_meta/scripts/wiki_health_check.py`
- `_meta/wiki-health-check-runbook.md`

Verification evidence:

- `python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki` exited `0`
- JSON parsed successfully with `python3 -m json.tool`
- Current result: `pass=true`, P0=`0`, P1=`0`, P2=`8`
- The eight P2 findings are the known unindexed draft query pages recorded in `_meta/draft-query-inventory.md`
- Markdown output path tested with `--format markdown`
