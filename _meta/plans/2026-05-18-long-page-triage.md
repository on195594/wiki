# Wiki long-page triage

Date: 2026-05-18
Status: triage only / no content rewrite
Scope: `/home/lin/wiki`

## 1. Goal

Classify long formal wiki pages so future cleanup can reduce retrieval noise and maintenance cost without rewriting content in bulk.

This document is the Lane C landing artifact from `_meta/plans/2026-05-18-wiki-governance-cleanup-plan.md`.

## 2. Non-goals

This triage does not authorize:

- editing the long pages themselves;
- deleting content;
- moving pages;
- changing page `type`, `status`, tags, or sources;
- modifying memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core.

Any actual split/compression requires a separate page-specific plan or explicit approval.

## 3. Scan baseline

Read-only scan found 15 formal pages above the approximate 200-line guideline in `SCHEMA.md`:

| Lines | Page |
|---:|---|
| 1325 | `queries/hermes-harness-profile-validation-detailed-plan.md` |
| 537 | `queries/hermes-project-dev-migration-plan-eng-review.md` |
| 388 | `concepts/hermes-lifeos-executable-architecture.md` |
| 348 | `concepts/public-info-monitoring-automation-methodology.md` |
| 266 | `concepts/gstack-project-execution-lane.md` |
| 251 | `queries/hermes-layer-routing-edge-cases.md` |
| 251 | `concepts/hermes-context-layer-operating-rules.md` |
| 243 | `concepts/hermes-layer-routing-decision-checklist.md` |
| 214 | `concepts/agent-closed-loop-learning-from-corrections-to-rules.md` |
| 210 | `queries/gstack-project-execution-lane-validation-case.md` |
| 208 | `queries/investment-watch-final-closeout.md` |
| 208 | `queries/how-i-should-scale-into-and-out-of-a-position.md` |
| 204 | `concepts/agent-experience-consolidation-loops.md` |
| 203 | `queries/when-i-should-not-trade.md` |
| 201 | `queries/how-i-should-convert-trading-lessons-into-hard-rules.md` |

## 4. Triage categories

Use one category per page:

- **Keep as-is**: long but intentionally complete as a reference.
- **Add summary only**: keep body, add short top summary/navigation later.
- **Split concept**: extract stable subtopics into separate concept pages and keep original as hub.
- **Move execution detail**: keep durable conclusion in wiki, move procedural detail to project-local docs or `_meta/plans/`.
- **Closeout compress**: keep outcome/evidence/promotion boundary, compress or relocate detailed transcript-like sections.

## 5. Initial triage decisions

### 5.1 `queries/hermes-harness-profile-validation-detailed-plan.md`

- Lines: 1325
- Current type/status: `type: query`, `status: draft`
- Observed structure: full implementation plan with project skeleton, file templates, prompt templates, fixtures, verification scripts, evaluation lanes, gates, rollback, and acceptance criteria.
- Triage category: **Move execution detail**
- Rationale: This is closer to a project implementation plan than a durable query answer. The stable wiki value is the summary, hypothesis, evidence/promotion boundary, and link to the validation project; most file templates and task bodies are execution detail.
- Recommended next action: create a page-specific split/compression plan before editing. Preserve original until the split map is reviewed.

Suggested split map:

- Keep in wiki page:
  - goal / executive summary
  - scope and non-scope
  - current conclusion/status
  - promotion gates and hard stops
  - evidence paths
  - related pages
- Move or archive outside the query page:
  - project skeleton task bodies
  - complete file templates
  - prompt template bodies
  - experiment stub details
  - script implementation snippets
- Candidate landing location for detail:
  - project-local docs under `/home/lin/.hermes/projects/hermes-harness-profile-validation/`, if that project remains canonical;
  - otherwise `_meta/plans/` as an archived execution plan.

### 5.2 `queries/hermes-project-dev-migration-plan-eng-review.md`

- Lines: 537
- Current type/status: `type: query`, `status: draft`
- Observed structure: engineering review with scope challenge, architecture review, code/test/performance review, implementation phases, layouts, final verdict.
- Triage category: **Closeout compress**
- Rationale: The durable value is the final verdict, migration rationale, phase ordering, and non-scope boundaries. Much of the detailed review can remain as evidence or be summarized.
- Recommended next action: do not edit now. If revisited, compress into a closeout/decision page that links to the original review or preserves detailed evidence in `_meta/reviews/`.

### 5.3 `concepts/hermes-lifeos-executable-architecture.md`

- Lines: 388
- Current role: central concept page for LifeOS / Hermes executable architecture.
- Observed structure: hard boundaries, boundary matrix, recommended topology, execution plan, operating policy, success/failure signals.
- Triage category: **Split concept**
- Rationale: This page contains multiple durable subtopics. It is not just execution detail; it should remain a hub and may split into boundary matrix / topology / promotion policy pages later.
- Recommended next action: add no immediate patch. Later split only if related pages continue growing.

### 5.4 `concepts/public-info-monitoring-automation-methodology.md`

- Lines: 348
- Current role: reusable methodology page for public information monitoring.
- Observed structure: standard workflow, source modeling, fixtures, architecture, state, diff, notifications, runtime, health checks, knowledge routing, examples.
- Triage category: **Add summary only**
- Rationale: It is long but appears to be a coherent methodology reference. A short top summary and navigation may be enough before any split.
- Recommended next action: defer. If used frequently, add a compact decision card at the top rather than splitting immediately.

### 5.5 `concepts/gstack-project-execution-lane.md`

- Lines: 266
- Current role: concept page for the 5-skill project execution lane.
- Observed structure: summary, five-skill lane, recommended sequence, common failure modes, Hermes fit, practical benefit.
- Triage category: **Add summary only**
- Rationale: Slightly above threshold but structurally coherent. Its length is not currently the main retrieval risk.
- Recommended next action: defer. Revisit after deciding whether `gstack` becomes a taxonomy tag, entity page, or historical project marker.

## 6. Priority order

Recommended order for any later page-specific cleanup:

1. `queries/hermes-harness-profile-validation-detailed-plan.md` — first target; huge execution plan in query layer.
2. `queries/hermes-project-dev-migration-plan-eng-review.md` — compress/closeout candidate.
3. `concepts/hermes-lifeos-executable-architecture.md` — split only after hub/subpage design.
4. `concepts/public-info-monitoring-automation-methodology.md` — summary/navigation only.
5. `concepts/gstack-project-execution-lane.md` — defer pending gstack taxonomy/entity decision.

## 7. First recommended landing change if approved later

Create a page-specific plan for `queries/hermes-harness-profile-validation-detailed-plan.md`.

Minimum requirements for that future plan:

- read the whole page before editing;
- identify exact sections to keep in the wiki page;
- identify exact sections to move or archive;
- preserve source links and related links;
- update `index.md` only if page title/path changes, which should be avoided by default;
- run health check and diff checks;
- stop before moving execution detail into any active runtime or project directory without explicit approval.

## 8. Verification commands for this triage artifact

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format json
git diff --check
git diff --stat
git status --short
```

Expected result:

- health check remains pass;
- only this triage document and `log.md` should change in the triage-only landing;
- no content pages are changed.
