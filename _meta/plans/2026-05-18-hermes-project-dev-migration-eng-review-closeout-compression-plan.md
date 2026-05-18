# Hermes project dev migration eng review closeout/compression plan

Date: 2026-05-18
Status: plan only / no content rewrite
Target page: `queries/hermes-project-dev-migration-plan-eng-review.md`
Source triage: `_meta/plans/2026-05-18-long-page-triage.md`

## 1. Goal

Define a safe closeout/compression map for `queries/hermes-project-dev-migration-plan-eng-review.md` before any edit is made to the page itself.

The target page is currently a 536-line draft query page. Its durable wiki value is the final engineering judgment, project-boundary rationale, migration phase order, non-scope boundaries, and evidence pointers. Much of the detailed architecture/test/layout review can be summarized or replaced with links to related pages and project-local state.

## 2. Non-goals

This plan does not authorize:

- editing `queries/hermes-project-dev-migration-plan-eng-review.md`;
- deleting or moving target-page content in this step;
- changing the target page path, title, frontmatter, tags, `type`, or `status`;
- modifying `/home/lin/.hermes/projects/investment-watch/`;
- modifying `/home/lin/.hermes/projects/project-kickoff/`;
- modifying active memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core;
- updating cron jobs, scripts, or project-local files as part of wiki compression.

Any actual rewrite must be a separate focused change after this plan is reviewed/approved.

## 3. Current baseline

Read-only evidence:

- Target page: `queries/hermes-project-dev-migration-plan-eng-review.md`
- Current frontmatter:
  - `type: query`
  - `status: draft`
  - tags: `[hermes, gstack, eng-review, migration, project-development]`
  - sources: `[filesystem:~/.hermes, filesystem:~/wiki, review:hermes-project-dev-office-hours-review]`
- Current size: 536 lines, 17523 bytes
- Fenced/code/layout blocks: 10 fence markers
- Triage category: **Closeout compress**
- Prior review source exists: `queries/hermes-project-dev-office-hours-review.md`
- Current project directories exist:
  - `/home/lin/.hermes/projects/investment-watch/`
  - `/home/lin/.hermes/projects/project-kickoff/`
- Old project-kickoff script path no longer exists:
  - `/home/lin/.hermes/scripts/project_kickoff.py`
- Related wiki closeout exists for investment-watch:
  - `queries/investment-watch-final-closeout.md`

Interpretation: the target page appears to be a historical engineering review / migration plan. At least some recommended migration outcomes now exist, so the future compact page should not read like an active implementation checklist without checking current state.

## 4. Target-page outline and classification

### Keep in compact wiki page

These sections contain durable lookup value and should remain, compressed:

- lines 11-22: title and `Summary`
- lines 23-103: `Step 0: Scope Challenge`
- lines 104-112: `Scope Decision`
- lines 113-187: `Architecture Review`
- lines 188-231: `Code Quality Review`
- lines 232-327: `Test Review`
- lines 328-342: `Performance Review`
- lines 412-420: `NOT in Scope`
- lines 502-515: `Completion Summary`
- lines 516-524: `Final Verdict`
- lines 533-536: `Related`

Compression rule: preserve the decision, rationale, risks, minimum viable scope, and verification expectations; remove detailed diagrams/layouts/checklists that are better recovered from git history or current project-local state.

### Replace with pointers or summarized decision notes

These sections are useful but too execution-heavy for the compact query page:

- lines 343-411: `Recommended Implementation Plan`
  - Keep only the three-phase order and critical concerns.
  - Do not keep exact step-by-step migration commands inline.
- lines 421-447: `Parallelization Strategy`
  - Keep only dependency summary: investment-watch and project-kickoff can proceed independently; scripts cleanup last.
- lines 448-457: `What already exists`
  - Merge into status/evidence pointers.
- lines 458-501: `Recommended File Layouts`
  - Replace with short pointer to current project directories and git history; do not keep full tree layouts inline.
- lines 525-532: `Next Step`
  - Treat as historical unless current state confirms the recommendation is still pending.

### Treat as historical / superseded by current state

The page recommends project-boundary migration for `investment-watch` and `project-kickoff`. Current read-only checks show both project directories now exist, and the old `~/.hermes/scripts/project_kickoff.py` path no longer exists. The compact page should therefore be framed as a historical engineering review and closeout/navigation record, not as a fresh instruction to mutate runtime/project files.

Before any future compression, verify whether there are current closeout/status documents for both projects. If no `project-kickoff` wiki closeout exists, do not invent one during this compression; simply point to project-local state and note the gap.

## 5. Proposed final wiki page shape

Keep the existing path by default:

```text
queries/hermes-project-dev-migration-plan-eng-review.md
```

Recommended post-compression structure:

```markdown
---
[preserve verbatim from original: title, created, updated, type, tags, sources, status]
---

# Hermes Project Development Migration Plan Eng Review

## Status
- Historical engineering review / migration plan.
- Current page should be read as a decision record, not as an active migration command list.
- Current project directories observed: investment-watch and project-kickoff.
- Frontmatter/path/type/status remain unchanged in the first compression.

## Summary decision
[Compressed final recommendation: split business projects out of `~/.hermes/scripts/`, keep Hermes runtime as host layer.]

## Scope and non-scope
[Minimum scope: investment-watch, project-kickoff, scripts README cleanup. Non-scope: Hermes core, CI/CD, monorepo, global quick-command rewrite, project discovery registry, shared tooling abstraction.]

## Durable engineering findings
[Short bullets for architecture, code quality, testing, performance.]

## Historical implementation map
[Three phases only: investment-watch, project-kickoff, scripts cleanup. No full file trees.]

## Current evidence and pointers
- Prior office-hours page.
- Current project-local directories.
- investment-watch wiki closeout, confirmed present at `queries/investment-watch-final-closeout.md`.
- Note if project-kickoff wiki closeout is absent.

## Final verdict
[DONE_WITH_CONCERNS and the two non-negotiable concerns: cron/internal hardcoded paths and minimum tests. Also preserve that the review completed its major phases and explicitly surfaced 2/2 critical gaps, so the verdict is not read as a shortcut summary.]

## Related
[Existing links.]
```

Expected result: reduce the page from 536 lines to roughly 100-150 lines while preserving the engineering decision trail.

## 6. Archive / migration policy

Preferred default: **do not create a duplicate full-text archive**.

Rationale:

- The original full text remains recoverable through wiki git history.
- The compact page should reduce retrieval noise rather than move the same detailed review into `_meta/`.
- Current project-local directories provide the live operational evidence for what eventually happened.

If a browsable archive is explicitly required later, use a separate commit and this path:

```text
_meta/plans/archive/2026-04-24-hermes-project-dev-migration-plan-eng-review-original.md
```

Do not create that archive during the first compression unless explicitly approved.

## 7. Required pre-edit checks for a future implementation

Before editing the target page:

1. Confirm wiki repo is clean and committed.
2. Confirm target page still has the same path and frontmatter.
3. Confirm target page path appears in `index.md`; do not update that entry in the compression commit.
4. Confirm related source page exists: `queries/hermes-project-dev-office-hours-review.md`.
5. Inspect current project-local state without modifying it:
   - `/home/lin/.hermes/projects/investment-watch/`
   - `/home/lin/.hermes/projects/project-kickoff/`
6. Check whether related wiki closeout/status pages exist:
   - `queries/investment-watch-final-closeout.md`
   - any project-kickoff closeout/status page, if present.
7. Decide whether any missing closeout page is a follow-up gap; do not create it inside the compression commit.
8. Decide whether a browsable `_meta/plans/archive/...` copy is needed. Default answer: no.

## 8. Future implementation steps if approved

1. Confirm the wiki repo is in a clean, committed state so the pre-edit snapshot is recoverable via `git checkout`.
2. Draft a compact replacement for the target page using section 5.
3. Do not change frontmatter, `status`, `type`, tags, title, or path in the compression commit. Any reclassification requires a separate explicitly approved pass.
4. Preserve links to the prior office-hours review and existing related pages.
5. Add project-local evidence pointers only as read-only references; do not modify those projects.
6. Run:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
git status --short
```

7. Commit only the compressed target page and any required `log.md` entry.
8. Run an independent implementation review before declaring the compression complete.

## 9. Stop conditions

Stop before implementation if any of these are true:

- wiki health check fails before editing;
- target page path/frontmatter differs from this plan unexpectedly;
- implementation requires updating `index.md` for any reason;
- related office-hours source page is missing;
- compression would require changing `index.md` or page path without explicit approval;
- implementation starts to modify project-local files, cron jobs, scripts, memory, skills, runtime config, MCP, wrappers, quick commands, `SOUL.md`, or Hermes core;
- current project-local state contradicts the historical page so strongly that the compact page would need new fact-finding rather than compression.

## 10. Review questions before actual compression

1. Is git history enough archive, or is a browsable `_meta/plans/archive/...` copy required?
2. Should the compact page explicitly say the migration recommendations appear partially/fully superseded by current project directories?
3. Should a missing `project-kickoff` wiki closeout be recorded as a separate follow-up gap?

Default recommendation:

- keep path and frontmatter unchanged for the first compression;
- use git history as archive;
- frame the target as a historical engineering decision record, not an active migration checklist;
- include project-local paths as evidence pointers only;
- if `project-kickoff` lacks a closeout/status wiki page, record that as a follow-up gap rather than creating it here;
- do not touch active Hermes layers or project-local files.

## 11. Independent review disposition

Claude review artifact:

```text
_meta/reviews/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan-claude-review.md
```

Verdict: `APPROVE_WITH_CHANGES`.

Accepted patches:

- I-1: pre-edit checks now verify the target page is indexed and forbid `index.md` updates in the compression commit.
- I-2: proposed compact-page shape now includes an explicit preserve-verbatim frontmatter stub.
- I-3: investment-watch wiki closeout is an unconditional evidence pointer because `queries/investment-watch-final-closeout.md` is confirmed present.
- I-4: final verdict guidance now preserves the completion-summary signal and the 2/2 critical gaps, not only `DONE_WITH_CONCERNS`.

Minor note: Claude reported a 537-line count, while `wc -l` and the local Python scan reported 536 lines. The discrepancy is treated as counting-method/trailing-newline variance and does not affect the compression map.
