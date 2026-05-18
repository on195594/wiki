# Wiki governance cleanup plan

Date: 2026-05-18
Status: draft / plan only
Scope: `/home/lin/wiki`

## 1. Goal

Bring the wiki governance rules back in line with how the wiki is now used, without rewriting content or changing conclusions.

This is a **docs-only remediation plan**. It plans three cleanup lanes:

1. schema alignment;
2. taxonomy round;
3. long-page triage.

The purpose is to improve maintainability, retrieval, source traceability, and future automation. The purpose is **not** to make the wiki smaller for its own sake or to normalize every historical artifact in one pass.

## 2. Current baseline

Read-only audit on 2026-05-18:

- Root: `/home/lin/wiki`
- Git working tree: clean before this plan was written
- Markdown files: 129
- Formal pages: 79
- Raw markdown files: 32
- `index.md` wikilinks: 79
- Backup candidates: 0
- Wiki health check: pass
  - P0: 0
  - P1: 0
  - P2: 0
- `git diff --check`: pass
- Tag audit:
  - declared tags: 45
  - tagged pages: 95
  - actual unique tags: 100
  - undeclared unique tags: 60
  - undeclared tag instances: 72
  - top undeclared tags: `gstack` 4, then `closeout`, `content-engineering`, `dreaming`, `position-sizing`, `project-development`, `pydantic`, `skill-files`, `structured-output`, `typed-boundary` at 2 each

Additional read-only findings:

- `SCHEMA.md` does not yet declare `operations/`, but the wiki has `operations/hermes-health-dashboard.md` and `index.md` has an Operations section.
- `queries/` contains question-answer pages, plans, closeouts, and validation cases.
- Several pages exceed the approximate 200-line split guideline in `SCHEMA.md`.
- `sources` values mix raw files, wiki pages, local projects, sessions, skills, docs, filesystem references, and temporary paths.
- `status` values have evolved beyond `draft | stable | raw`.

## 3. Non-goals and forbidden actions

This plan does **not** authorize implementation. It is only a planning artifact.

Do not do these during the planning/review phase:

- Do not rewrite wiki content pages.
- Do not rename or move pages.
- Do not delete raw sources.
- Do not bulk-edit frontmatter.
- Do not update Hermes memory, active skills, cron jobs, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core.
- Do not promote any wiki cleanup into runtime behavior.
- Do not try to drive undeclared tags to zero in one pass.
- Do not treat `/tmp/...` or local session references as automatically invalid without deciding the source policy first.

## 4. Issue-to-task matrix

| Issue | Risk | Remediation lane | Evidence / verification | Stop condition |
|---|---|---|---|---|
| `SCHEMA.md` omits `operations/` while the wiki uses it | Directory roles drift; future maintainers/tools get conflicting rules | Schema alignment | `SCHEMA.md`, `index.md`, `operations/hermes-health-dashboard.md`; health check stays pass | Stop if adding `operations/` to `SCHEMA.md` leads to a proposal to move or rename existing pages in the same pass. |
| `queries/` mixes Q&A, plans, closeouts, validation cases | Retrieval intent becomes unclear | Schema alignment | Decide allowed `type` values and directory semantics | Stop if plan proposes mass migration without separate approval |
| `status` values exceed schema enum | Machine-readable metadata is inconsistent | Schema alignment | Enumerate accepted formal/raw status values; later lint can validate them | Stop if changing page statuses would alter meaning |
| `sources` mixes raw/wiki/project/session/skill/docs/filesystem/tmp | Source traceability becomes ambiguous | Schema alignment | Define URI/source policy and temporary-path treatment | Stop if a source cannot be made durable without losing provenance |
| 60 undeclared unique tags | Tag-based retrieval and audits are noisy | Taxonomy round | `wiki_tag_audit.py` before/after counts | Stop if a proposed alias loses useful semantics |
| Very long formal pages | Retrieval noise and maintenance cost | Long-page triage | Page line counts, selected triage records | Stop if triage becomes content rewrite rather than routing decision |

## 5. Lane A — Schema alignment

### Objective

Update the governance rules so future wiki changes have clear metadata and directory semantics.

### Minimum landing change if later approved

Patch only schema/governance documentation. Do not alter individual content pages in this lane unless a later decision explicitly authorizes a tiny metadata correction. Lane A does **not** authorize changing the `type` field of existing `queries/` pages. The `type` enum expansion is a schema-documentation change only. Re-classifying existing pages requires a separate approved migration plan.

Expected files:

- Modify: `SCHEMA.md`
- Optional modify: `concepts/hermes-wiki-lint-and-health-check-standards.md`
- Modify after execution: `log.md`

Optional schema detail: document `_meta/plans/`, `_meta/reviews/`, and `_meta/scripts/` as recognized `_meta/` subdirectories in `SCHEMA.md` Directory Roles at the same time.

### Proposed schema decisions to review

1. Add `operations/` as a formal directory role.

   Suggested meaning:

   - `operations/`: stable operational dashboards, runbooks, maintenance contracts, and recurring governance surfaces.
   - It should not hold one-off project plans or raw review artifacts.

2. Clarify `queries/` scope.

   Two acceptable policies:

   - Conservative policy: `queries/` is for durable question-answer decision pages only; future plans/closeouts move to `_meta/plans/`, `_meta/reviews/`, or `operations/`.
   - Compatibility policy: `queries/` may retain historical plans/closeouts, but schema must define `type: query | plan | closeout | validation-case` and discourage future mixing unless intentionally indexed.

   Recommended default: compatibility policy for existing pages, stricter routing for future pages. Avoid mass migration now.

3. Expand `status` semantics.

   Suggested formal status values:

   - `draft`: not yet stable or intentionally provisional
   - `stable`: durable knowledge page
   - `active`: operational page that reflects current live process
   - `closed`: completed project/validation/closeout record
   - `current`: current-as-of page where time matters

   Suggested raw status values:

   - `raw`: captured source with no interpretation
   - `captured`: historical synonym to normalize later or accept explicitly

   Unaddressed values deferred to a later pass:

   - `current-as-of-<date>`: treat as `current` plus dated note, or accept as informal historical status.
   - `complete` / `completed`: `_meta/`-only values; defer or map to `closed` in a future metadata cleanup.
   - `raw-source`: raw-page historical status alias; defer or map to `raw`.

   Do not change pages with these values in Lane A. Record them for the next schema/metadata round.

4. Define `sources` policy.

   Suggested allowed source forms:

   - `raw/...`: captured raw source in the wiki
   - `concepts/...`, `queries/...`, `comparisons/...`, `operations/...`: derived wiki source
   - `project:/absolute/path`: local project evidence
   - `session:<stable-id>`: session-derived evidence
   - `skill:<skill-name>`: Hermes skill evidence
   - `docs:<name-or-url>`: documentation source
   - `filesystem:<path>`: local filesystem observation; should be used sparingly

   Suggested temporary-path rule:

   - `/tmp/...` should not be the only long-term source for a formal page. Later cleanup should either replace it with a durable artifact path, cite the stable derived wiki/review page, or explicitly mark it as historical non-replayable evidence.

5. Define normative pages.

   Some wiki self-governance pages naturally have no external source. Add an explicit policy instead of leaving them as implicit exceptions.

   Candidate frontmatter:

   ```yaml
   source_policy: normative
   ```

   Candidate rule:

   - `source_policy: normative` is allowed only for wiki rules, standards, operating policies, and self-authored governance pages.
   - Normative pages should still link to related wiki pages.

   Tooling gap:

   - `source_policy: normative` has no automated enforcement in the current scripts. A future lint rule should flag any page with `source_policy: normative` that is not under `_meta/`, `SCHEMA.md`, `index.md`, or `log.md`. Do not rely on this field for security gating without that lint.

### Verification for Lane A

Run after any later patch:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki
git diff --check
git diff --stat
```

Expected result:

- health check stays pass
- P0 remains 0
- P1 remains 0
- schema changes are limited to governance docs and `log.md`
- tag audit may still exit 1 if undeclared tags remain intentionally deferred

## 6. Lane B — Taxonomy round

### Objective

Reduce tag audit noise with conservative taxonomy decisions and obvious alias cleanup, without flattening useful semantics.

### Minimum landing change if later approved

Do one small taxonomy round. It may update `SCHEMA.md`, `log.md`, and a small number of frontmatter tag lists only when the alias is obvious and deduplicated.

Expected files:

- Modify: `SCHEMA.md`
- Optional modify: selected formal pages with obvious tag aliases
- Modify after execution: `log.md`

### Current tag baseline

- declared tags: 45
- actual unique tags: 100
- undeclared unique tags: 60
- undeclared tag instances: 72

Top undeclared tags:

- `gstack`: 4
- `closeout`: 2
- `content-engineering`: 2
- `dreaming`: 2
- `position-sizing`: 2
- `project-development`: 2
- `pydantic`: 2
- `skill-files`: 2
- `structured-output`: 2
- `typed-boundary`: 2

### Decision rules

Use these before editing tags:

1. Add a tag to `SCHEMA.md` only if it has stable retrieval value.
2. Prefer existing broader tags for one-off or article-only labels.
3. Do not normalize project/tool names without deciding whether they are tags, entities, or path/title metadata.
4. Deduplicate tag lists after any replacement.
5. Count raw tags, but prioritize formal pages for first-pass replacements.
6. Do not treat `wiki_tag_audit.py` exit code 1 as failure when remaining undeclared tags are explicitly deferred.

### Candidate decisions to review

Likely add to taxonomy if semantic inspection supports it:

- `closeout`: if closeout pages remain a durable wiki pattern; otherwise model as `status: closed` plus `type: closeout` instead of a tag.
- `content-engineering`: if it recurs as a method area; otherwise map to broader `workflow` / `automation`.
- `position-sizing`: likely useful under investment/trading, but may be better represented by page title + `trading` / `risk-control`.
- `pydantic`: likely a tool/entity marker; decide whether tool-specific tags are allowed.
- `structured-output`: likely a reusable AI engineering facet; may be worth adding if more pages appear.
- `typed-boundary`: likely close to `typed-ai-agent-boundaries`; decide whether canonical tag should be `typed-boundary`, `structured-output`, or existing `risk-control`/`verification`.

Likely defer:

- `gstack`: project/tool-family marker; decide later whether to create an entity/project page or keep as a taxonomy tag.
- `dreaming`: product/pattern marker from Anthropic-style workflow; defer until more stable concept pages exist.
- `project-development`: may duplicate `project` + `workflow`.
- `skill-files`: may duplicate `skills` + `configuration`.

### Verification for Lane B

Before patch:

```bash
git status --short
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki
```

After patch:

```bash
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
```

Expected result:

- undeclared unique and instance counts decrease or intentional deferrals are recorded
- duplicate tag files remain zero, confirmed via `wiki_tag_audit.py --format json` `.duplicate_tag_files[]`
- no broken links or index regressions
- `log.md` records before/after counts and deferred tags

## 7. Lane C — Long-page triage

### Objective

Identify long formal pages that should be split, summarized, or rerouted, without doing the rewrite in the same pass.

### Minimum landing change if later approved

Create a triage record and choose a small first landing page. Do not split all long pages at once.

Expected files:

- Create or modify: `_meta/long-page-triage.md` or a dated `_meta/plans/...long-page-triage.md`
- Optional later modify: one selected long page after a separate approved split plan
- Modify after execution: `log.md`

### Current high-priority candidates

Highest priority:

1. `queries/hermes-harness-profile-validation-detailed-plan.md` — 1325 lines
2. `queries/hermes-project-dev-migration-plan-eng-review.md` — 537 lines
3. `concepts/hermes-lifeos-executable-architecture.md` — 388 lines

Other notable long pages:

- `concepts/public-info-monitoring-automation-methodology.md` — 348 lines
- `concepts/gstack-project-execution-lane.md` — 266 lines
- `queries/hermes-layer-routing-edge-cases.md` — 251 lines
- `concepts/hermes-context-layer-operating-rules.md` — 251 lines
- `concepts/hermes-layer-routing-decision-checklist.md` — 243 lines
- `concepts/agent-closed-loop-learning-from-corrections-to-rules.md` — 214 lines
- `queries/gstack-project-execution-lane-validation-case.md` — 210 lines

### Triage classification

For each long page, classify it as one of:

- Keep as-is: long but useful as a complete reference.
- Add summary only: keep body, add a short top summary and navigation anchors.
- Split concept: extract stable subtopics into concept pages and keep original as hub.
- Move execution detail: keep durable conclusion in wiki, move procedural detail to project-local docs or `_meta/plans/`.
- Closeout compress: keep outcome/evidence/promotion boundary, archive or relocate detailed transcript-like sections.

### First recommended target

Start with `queries/hermes-harness-profile-validation-detailed-plan.md` because it is far above the threshold and likely contains project execution detail rather than a durable query answer.

Suggested first action if later approved:

1. Read the page and identify durable sections vs execution detail.
2. Preserve the original file until a split plan is reviewed.
3. Draft a split map:
   - durable conclusion / status summary
   - evidence paths
   - promotion boundaries
   - detailed plan sections to keep only as project-local or `_meta/plans/` artifacts
4. Ask for approval before editing the page.

### Verification for Lane C

For triage-only landing:

```bash
test -f _meta/long-page-triage.md || test -f _meta/plans/2026-05-18-long-page-triage.md
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
```

For any later page split:

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki
git diff --check
git diff --stat
```

Expected result:

- index links remain valid
- source links remain valid or improve
- long-page count decreases only for the selected page
- no mass content rewrite occurs without separate approval

## 8. Independent review request

Before implementing any lane, request a read-only independent review.

Preferred Claude Code command shape:

```bash
claude -p --permission-mode plan --tools Read,Grep,LS --add-dir /home/lin/wiki < /home/lin/wiki/_meta/reviews/2026-05-18-wiki-governance-cleanup-plan-claude-review-prompt.md > /home/lin/wiki/_meta/reviews/2026-05-18-wiki-governance-cleanup-plan-claude-review.md
```

Reviewer should inspect:

- `/home/lin/wiki/_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`
- `/home/lin/wiki/SCHEMA.md`
- `/home/lin/wiki/index.md`
- `/home/lin/wiki/_meta/scripts/wiki_health_check.py`
- `/home/lin/wiki/_meta/scripts/wiki_tag_audit.py`
- representative long pages and tag examples as needed

Ask reviewer to return:

- blocking findings
- important findings
- minor findings
- explicit non-promotion statement
- whether the three-lane split is safe and complete
- concrete patch text for any plan changes they recommend

## 9. Execution order if later approved

Recommended order:

1. Create review prompt and run Claude read-only review.
2. Patch this plan for accepted blocking/important findings.
3. Commit or otherwise preserve the reviewed plan/review artifacts before mutating schema or page metadata.
4. Execute Lane A first: schema alignment.
5. Execute Lane B second: conservative taxonomy round.
6. Execute Lane C third: long-page triage record only.
7. Stop before any actual page split unless separately approved.

## 10. Rollback and stop conditions

Rollback principle:

- Keep each lane as a focused change so `git restore <files>` or a focused revert can undo it.

Stop immediately if:

- `git status --short` is dirty before starting a mutating lane and the dirty state is unrelated.
- health check produces any P0 or P1 regression.
- tag cleanup requires semantic guesses.
- source cleanup would erase provenance.
- long-page triage turns into content rewriting.
- any active Hermes layer would be touched without explicit dated approval.

## 11. Completion criteria for this plan

This plan is complete when:

- the file exists at `/home/lin/wiki/_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`;
- it covers schema alignment, taxonomy round, and long-page triage;
- it states non-goals and active-layer non-promotion boundaries;
- it includes verification commands for each lane;
- it is ready for Claude read-only review.
