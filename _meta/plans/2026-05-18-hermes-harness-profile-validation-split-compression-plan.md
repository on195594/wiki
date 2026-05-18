# Hermes harness profile validation page split/compression plan

Date: 2026-05-18
Status: plan only / no content rewrite
Target page: `queries/hermes-harness-profile-validation-detailed-plan.md`
Source triage: `_meta/plans/2026-05-18-long-page-triage.md`

## 1. Goal

Define a safe split/compression map for the 1324-line target page before any edit is made to the page itself.

The target page is currently a draft query page, but its body is mostly an execution plan with project scaffolding, document templates, prompt templates, fixtures, scripts, evaluation gates, and rollout policy. The durable wiki value should be a compact knowledge page: why the validation existed, what boundary it enforced, what was finally decided, and where evidence lives.

## 2. Non-goals

This plan does not authorize:

- editing `queries/hermes-harness-profile-validation-detailed-plan.md`;
- deleting or moving any target-page content in this step;
- changing the target page path, title, frontmatter, tags, or `type`;
- modifying `/home/lin/.hermes/projects/hermes-harness-profile-validation/`;
- modifying active memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core.

Any actual rewrite must be a separate focused change after this plan is reviewed/approved.

## 3. Current baseline

Read-only evidence:

- Target page: `queries/hermes-harness-profile-validation-detailed-plan.md`
- Current frontmatter:
  - `type: query`
  - `status: draft`
  - tags: `[hermes, optimization, harness, model-profiles, validation, workflow]`
- Current size: 1324 lines, 31486 bytes
- Code/template fences: 90 fence markers
- Triage category: **Move execution detail**
- Existing canonical project directory exists: `/home/lin/.hermes/projects/hermes-harness-profile-validation/`
- Existing project status: closed
- Existing project closeout: `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md`
- Existing wiki closeout referenced by project status: `queries/hermes-harness-profile-validation-final-closeout.md`

Project-local closeout says the project finished as a successful validation with narrow promotion:

- promoted: `writing-plans` and `requesting-code-review` narrow skill patches;
- not authorized: Hermes core, `SOUL.md`, runtime profiles, cron, memory, broad skill rewrites, article summary, coding/config.

## 4. Target-page outline and classification

### Keep in compact wiki page

These sections contain durable lookup value and should remain, compressed:

- lines 11-22: title and opening statement
- lines 23-47: `1. Executive Summary`
- lines 48-73: `2. Scope and Non-Scope`
- lines 74-91: `3. Current Baseline`
- lines 92-134: `4. Design Principles`
- lines 1152-1197: `13. Decision Gates`
- lines 1198-1234: `14. Rollback and Safety`
- lines 1291-1302: `16. Final Acceptance Criteria`
- lines 1303-1315: `17. Recommended Immediate Next Step`
- lines 1316-1324: `Related`

Compression rule: keep the intent, boundary, gates, safety constraints, and links; remove step-by-step file/template bodies from the wiki page.

### Replace with pointers to project-local evidence

These sections are execution detail and should not stay inline in the query page after approval:

- lines 135-189: `5. Target Project Structure`
- lines 190-355: `6. Workstream A — Bootstrap the Validation Project`
- lines 356-626: `7. Workstream B — Define Core Project Documents`
- lines 627-804: `8. Workstream C — Create Prompt Templates`
- lines 805-874: `9. Workstream D — Create Experiment Template and First Experiment Records`
- lines 875-946: `10. Workstream E — Fixtures`
- lines 947-1075: `11. Workstream F — Verification Scripts`
- lines 1076-1151: `12. Workstream G — Run the Four Evaluation Lanes`
- lines 1235-1290: `15. Milestone Timeline`

Replacement rule: summarize each workstream in 1-3 bullets and link to the existing project-local docs/evidence where available. Do not duplicate full templates or scripts in wiki.

### Treat as superseded by closeout

The original plan predates the final project outcome. The compact page should clearly state that the plan is superseded by:

- `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md`
- `queries/hermes-harness-profile-validation-final-closeout.md`

The compact page should become a navigation/decision page, not an implementation checklist.

## 5. Proposed final wiki page shape

Keep the existing path by default:

```text
queries/hermes-harness-profile-validation-detailed-plan.md
```

Recommended post-compression structure:

```markdown
# Hermes Harness Profile Validation Detailed Plan

## Status
- Historical plan, superseded by final closeout.
- Current project status: closed.
- Final promoted changes: narrow `writing-plans` and `requesting-code-review` skill patches.
- Explicitly not authorized: runtime/core/SOUL/memory/cron changes.

## Why this mattered
[Compressed from Executive Summary and Design Principles.]

## Scope and non-scope
[Compressed from section 2.]

## Durable design principles
[5 bullets max.]

## Evidence and canonical records
- Project README / STATUS
- Final project closeout
- Wiki final closeout
- Gate 6 regression evidence

## Original execution map
[One short bullet per workstream A-G; no inline templates/scripts.]

## Promotion and stop gates
[Compressed gate list.]

## Related
[Existing related links, plus final closeout link if missing.]
```

Expected result: reduce the page from 1324 lines to roughly 120-180 lines while preserving the decision trail and links.

## 6. Archive / migration policy

Preferred default: **do not create a duplicate full-text archive** unless human review asks for it.

Rationale:

- The current full text remains recoverable through git history.
- The project-local directory already contains the canonical evidence, docs, fixtures, prompts, and scripts.
- Duplicating the 1324-line execution plan into `_meta/` would preserve retrieval noise in another location.

If a browsable archive is still required later, use this explicit path and commit it separately:

```text
_meta/plans/archive/2026-04-30-hermes-harness-profile-validation-original-detailed-plan.md
```

Do not create that archive during the compression commit unless explicitly approved.

## 7. Required pre-edit checks for a future implementation

Before editing the target page:

1. Confirm wiki working tree is clean.
2. Confirm project-local working tree is clean or at least inspect its status without modifying it.
3. Read the target page and existing final closeout page.
4. Verify these project-local evidence files still exist:
   - `/home/lin/.hermes/projects/hermes-harness-profile-validation/README.md`
   - `/home/lin/.hermes/projects/hermes-harness-profile-validation/STATUS.md`
   - `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md`
   - `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/gate-6-post-patch-regression-2026-04-30.md`
5. Decide whether a browsable `_meta/plans/archive/...` copy is needed. Default answer: no.

## 8. Future implementation steps if approved

1. Create a rollback commit for this plan if not already committed.
2. Draft a compact replacement for the target page using the structure in section 5.
3. Preserve frontmatter unless there is explicit approval to change `status` or `type`.
4. Add or preserve links to final closeout and project-local evidence.
5. Run:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
git status --short
```

6. Commit only the compressed target page and any required `log.md` entry.

## 9. Stop conditions

Stop before implementation if any of these are true:

- project-local final closeout is missing;
- wiki final closeout is missing;
- health check fails before editing;
- compression would require changing the page path or index without explicit approval;
- implementation starts to modify active Hermes layers, project evidence, skills, memory, cron, runtime config, or Hermes core.

## 10. Review questions before actual compression

1. Should the target page remain `type: query`, or should a later schema-aware pass reclassify it as closeout/plan?
2. Is git history enough archive, or is a browsable `_meta/plans/archive/...` copy required?
3. Should the compact page link to project-local absolute paths, wiki links only, or both?

Default recommendation:

- keep path and frontmatter unchanged for the first compression;
- use git history as archive;
- include both wiki final closeout link and project-local evidence paths;
- do not touch active Hermes layers.
