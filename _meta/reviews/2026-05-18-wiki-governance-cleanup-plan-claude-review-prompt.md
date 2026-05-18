# Read-only independent review request

You are Claude Code acting as an independent reviewer. Review the wiki governance cleanup plan only. Do not edit files.

## Scope

Plan under review:

- `/home/lin/wiki/_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`

Wiki root:

- `/home/lin/wiki`

## Context

The plan was created after a read-only audit of the local Hermes wiki. It proposes three future cleanup lanes:

1. schema alignment
2. taxonomy round
3. long-page triage

The plan is intended to be plan-only and must not authorize direct content rewrites, page moves/deletions, memory updates, skill updates, cron/runtime/MCP/wrapper changes, or Hermes core changes.

## Files to inspect

Please inspect at least:

- `/home/lin/wiki/_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`
- `/home/lin/wiki/SCHEMA.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/_meta/scripts/wiki_health_check.py`
- `/home/lin/wiki/_meta/scripts/wiki_tag_audit.py`

Inspect representative pages only if needed to validate a finding.

## Review focus

Check:

1. Scope safety: does the plan clearly prevent accidental active-layer or content-layer mutation?
2. Schema alignment: are the proposed decisions consistent with current wiki structure and `SCHEMA.md`?
3. Taxonomy safety: are tag additions/aliases conservative enough? Are there semantic-loss risks?
4. Long-page triage: does the plan avoid turning triage into unapproved rewrites? Are candidate pages and classification rules sensible?
5. Verification gates: are commands, stop conditions, rollback paths, and evidence requirements sufficient?
6. Missing risks: anything important absent from the plan?

## Output format

Return a Markdown review with these sections:

# Claude Review — Wiki governance cleanup plan

## Verdict

One of: APPROVE / APPROVE_WITH_CHANGES / BLOCK.

## Inspected files and commands

List what you inspected. If you ran no shell commands, say so.

## Blocking findings

For each finding:

- ID
- Severity: blocking
- Evidence: file path and line/section
- Problem
- Recommended concrete patch text or exact change

If none, say `None`.

## Important findings

Same structure. These should be fixed before implementation but do not necessarily block saving the plan.

## Minor findings

Same structure.

## Non-promotion statement

Explicitly state whether the reviewed plan does or does not authorize changes to active Hermes layers: memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core.

## Overall recommendation

Give a concise recommendation for next action.
