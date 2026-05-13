# Wiki tag taxonomy round 3 decision plan

Date: 2026-05-13
Status: draft / plan only
Scope: `/home/lin/wiki`

## 1. Goal

Decide how to handle the remaining high-frequency undeclared tags after the first two tag taxonomy cleanup rounds, without doing another broad mechanical replacement.

Focus tags:

- `lifeos` — 9 pages
- `kickoff` — 8 pages
- `gstack` — 4 pages
- `harness` — 4 pages

This round is a **semantic decision round**, not a bulk cleanup round.

## 2. Current baseline

After round 2:

- declared tags: 43
- undeclared unique tags: 61
- undeclared instances: 91
- duplicate tag files: 0
- wiki health: pass=true, P0=0, P1=0, P2=8 known draft query pages

Representative read-only inspection found:

### `lifeos`

Appears on stable concept pages about the user's cross-domain personal operating model:

- `concepts/lifeos-overview.md`
- `concepts/hermes-lifeos-executable-architecture.md`
- `concepts/family-education-operating-model.md`
- `concepts/personal-finance-and-education-fund-model.md`
- `concepts/personal-growth-operating-model.md`
- `concepts/system-governance-operating-model.md`
- `concepts/work-and-career-operating-model.md`
- plus `concepts/gstack-project-execution-lane.md` and `concepts/hermes-context-layer-operating-rules.md`

Interpretation: `lifeos` is a stable domain tag, not an alias.

### `kickoff`

Appears only on draft/generated query pages:

- `queries/project-kickoff-*.md`
- `queries/qa-kickoff-*.md`

Interpretation: `kickoff` marks generated project-intake drafts, not a durable subject area. It may be better represented by `project` + `workflow`, or by path/title rather than taxonomy.

### `gstack`

Appears on pages about a specific project-execution lane / skill family:

- `concepts/gstack-project-execution-lane.md`
- `queries/gstack-project-execution-lane-validation-case.md`
- `queries/hermes-project-dev-migration-plan-eng-review.md`
- `queries/hermes-project-dev-office-hours-review.md`

Interpretation: `gstack` is a project/tool-family identifier. It may deserve a taxonomy tag only if the wiki will keep using it as a durable project-execution lineage.

### `harness`

Appears on Hermes model/profile validation pages:

- `concepts/hermes-model-specific-harness-profiles.md`
- `queries/hermes-harness-profile-validation-detailed-plan.md`
- `queries/hermes-harness-profile-validation-final-closeout.md`
- `queries/hermes-system-model-specific-harness-optimization-plan.md`

Interpretation: `harness` is a stable Hermes/agent engineering facet. It should likely become a formal taxonomy tag.

## 3. Recommended decisions

### Decision A — Add `lifeos` to taxonomy

Reason:

- It is a stable cross-domain concept in this wiki.
- It has a central overview page.
- It ties together family, finance, work, growth, and system governance.

Implementation:

- Add `lifeos` under Domain tags in `SCHEMA.md`.
- Do not rename pages or alter content.

### Decision B — Add `harness` to taxonomy

Reason:

- It is a stable agent/runtime engineering facet.
- It appears in a concept page plus validation/closeout query pages.
- It supports future retrieval around model-specific execution wrappers and profile overlays.

Implementation:

- Add `harness` under Facet tags in `SCHEMA.md`.
- Do not merge it into `model-profiles`; they are related but not equivalent.

### Decision C — Keep `gstack` unchanged for now, but do not add it to taxonomy yet

Reason:

- It may be a local project/tool-family identifier rather than a general subject tag.
- The main concept page `concepts/gstack-project-execution-lane.md` is still `status: draft`; it should not be promoted into taxonomy before the concept stabilizes.
- Adding it to taxonomy now risks promoting a project-specific marker before the related pages are stabilized.

Implementation:

- Leave existing `gstack` tags unchanged.
- Add a note to the plan/log that `gstack` needs a later entity/project decision:
  - either keep as project/tool-family tag;
  - create an entity page if it becomes durable enough;
  - or map to `project` / `workflow` if the project-specific lineage is no longer useful.

### Decision D — Do not add `kickoff` to taxonomy; optionally normalize later

Reason:

- It appears only in draft/generated query pages.
- It describes a generation stage, not a durable knowledge subject.
- These pages are already known draft query P2 items and should not be mixed into taxonomy cleanup.

Implementation for this round:

- Leave `kickoff` unchanged.
- Do not add it to `SCHEMA.md`.
- Defer any `kickoff` cleanup to a separate draft-query governance pass.
- Note: `queries/gstack-project-execution-lane-validation-case.md` also has the related `project-kickoff` tag with count=1; if a later draft-query cleanup handles `kickoff`, handle `project-kickoff` in the same pass.

## 4. Execution plan if approved later

This current task stops at plan + independent review. If execution is later approved, do only this narrow change:

1. Confirm clean working tree:

```bash
git status --short
```

2. Update `SCHEMA.md`:

- Domain tags: add `lifeos`.
- Facet tags: add `harness`.

3. Do not edit any page frontmatter in this round.

4. Update `log.md` with:

- decisions for `lifeos`, `harness`, `gstack`, `kickoff`;
- before/after audit counts;
- validation commands.

5. Validate:

```bash
python3 _meta/scripts/wiki_tag_audit.py --root /home/lin/wiki --format json
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
```

Expected result:

- undeclared unique: `61 -> 59`
- undeclared instances: `91 -> 78` approximately (`lifeos` 9 + `harness` 4 removed from undeclared instances)
- duplicate tag files: 0
- wiki health remains pass=true, P0=0, P1=0

6. Commit:

```text
docs: 判定第三轮 wiki tag taxonomy
```

## 5. Files likely to change on execution

Expected:

- `SCHEMA.md`
- `log.md`

Not expected:

- individual concept/query/raw pages
- `index.md`
- Hermes memory
- Hermes skills
- cron/runtime/provider config

## 6. Risks and mitigations

Risk: promoting `lifeos` makes taxonomy more personal and less general.

- Mitigation: this wiki is explicitly the user's Hermes knowledge base; `lifeos` has stable concept pages and recurring use.

Risk: `harness` overlaps with `model-profiles`.

- Mitigation: document it as a broader execution-environment facet. `model-profiles` is narrower.

Risk: leaving `kickoff` undeclared keeps audit noise.

- Mitigation: accepted for now because those pages are draft/generated query artifacts; handle them in a separate draft-query cleanup.

Risk: leaving `gstack` undeclared keeps audit noise.

- Mitigation: accepted until the wiki decides whether `gstack` is a durable entity/tool family or a project-specific historical marker.

## 7. Independent review request

Ask Claude Code to review:

- whether `lifeos` and `harness` should be added to taxonomy;
- whether `gstack` and `kickoff` should remain deferred;
- whether the execution scope is narrow enough;
- whether any page-level edits are needed now.
