# Hermes LifeOS executable architecture split concept plan

Date: 2026-05-18
Status: plan only / no content rewrite
Target page: `concepts/hermes-lifeos-executable-architecture.md`
Source triage: `_meta/plans/2026-05-18-long-page-triage.md`

## 1. Goal

Define a safe split-concept plan for `concepts/hermes-lifeos-executable-architecture.md` before any edit is made to the page itself.

The target page is a 387-line stable concept page. It is a central architecture hub, not an execution-plan query. Its durable wiki value is the top-level LifeOS/Hermes topology decision, the layer-boundary contract, and routing/promotion principles. It also contains several durable subtopics that may deserve separate concept pages if the page is split later.

## 2. Non-goals

This plan does not authorize:

- editing `concepts/hermes-lifeos-executable-architecture.md`;
- splitting, deleting, moving, or compressing target-page content in this step;
- changing the target page path, title, frontmatter, tags, `type`, or `status`;
- updating `index.md` in this step;
- creating new concept pages in this step;
- modifying memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files.

Any actual split must be a separate focused implementation after this plan is reviewed and approved.

## 3. Current baseline

Read-only evidence:

- Target page: `concepts/hermes-lifeos-executable-architecture.md`
- Current size: 387 lines, 11601 bytes
- Current frontmatter:
  - `title: Hermes LifeOS Executable Architecture`
  - `type: concept`
  - `status: stable`
  - tags: `[hermes, lifeos, architecture, workflow, governance]`
  - sources: `[concepts/companyos-to-lifeos-filesystem-philosophy.md, concepts/hermes-knowledge-architecture.md, concepts/hermes-memory-skills-wiki-boundaries.md, queries/hermes-layer-routing-edge-cases.md, session:2026-04-21-hermes-lifeos-vs-profile]`
- Current index entry exists under Concepts: `[[hermes-lifeos-executable-architecture]]`
- Triage category: **Split concept**
- Triage rationale: central concept page with multiple durable subtopics; should remain a hub and may split into boundary matrix / topology / promotion policy pages later.

Interpretation: the target is an architecture hub. The first implementation should preserve hub identity and extract only stable, link-worthy subtopics. Do not treat this like the earlier query-page compression passes.

## 4. Target-page outline and split classification

### Keep in the hub page

These sections define the core architecture and should remain in `concepts/hermes-lifeos-executable-architecture.md`, possibly shortened only after split pages exist:

- lines 13-14: `Summary`
- lines 16-23: `Goal`
- lines 25-36: `Core design decision`
- lines 203-220: `Recommended topology for your Hermes`
- lines 364-379: `Success criteria` / `Failure signs`
- lines 380-387: `Related`

Hub role after any future split:

- state the top-level architecture decision;
- route readers to layer-boundary, topology/profile, and promotion/operating-policy subpages;
- avoid duplicating full detail from split subpages;
- keep the page stable and index-friendly.

### Candidate split page A: layer boundary contract

Candidate path:

```text
concepts/hermes-lifeos-layer-boundary-contract.md
```

Candidate source sections:

- lines 38-184: `Hard boundaries`
- lines 186-202: `Boundary matrix`

Durable content:

- `wiki`, `memory`, `skill`, `cron`, `MCP`, `profile`, `session` responsibilities;
- allowed / forbidden content per layer;
- judgment sentence per layer;
- one-line routing matrix;
- anti-boundary-crossing rules.

Hub after split should keep only a compact summary matrix and link to the split page.

### Candidate split page B: topology and profile isolation policy

Candidate path:

```text
concepts/hermes-lifeos-topology-and-profile-policy.md
```

Candidate source sections:

- lines 25-36: `Core design decision` as shared context, summarized rather than duplicated;
- lines 203-220: `Recommended topology for your Hermes`;
- lines 313-331: `Phase 5: Add profiles only for real isolation needs`;
- related failure signs around profile proliferation.

Durable content:

- `default profile` as the main semantic brain;
- profiles as rare runtime-state isolation boundaries;
- acceptable profile use cases: work/personal isolation, public/bot identity, lab experimentation, high-risk automation isolation;
- anti-pattern: one profile per life domain.

Hub after split should still keep the top-level topology decision, but delegate profile-isolation detail to this page.

### Candidate split page C: promotion and operating policy

Candidate path:

```text
concepts/hermes-lifeos-promotion-operating-policy.md
```

Candidate source sections:

- lines 222-331: `Execution plan`, especially phase order;
- lines 332-354: `Operating policy`;
- lines 355-362: `Immediate next steps` if still relevant.

Durable content:

- sequence: freeze architecture contract -> build wiki domain map -> extract skills -> add cron -> add MCP -> add profiles;
- intake policy;
- promotion policy;
- deletion policy;
- guardrail: important does not equal persistent;
- guardrail: cron schedules stable methods; it does not define them.

Hub after split should keep a short phase ladder and link to this policy page.

## 5. Recommended first implementation if approved later

Do not split all three pages at once by default.

Recommended first split:

```text
concepts/hermes-lifeos-layer-boundary-contract.md
```

Reason:

- It is the largest self-contained subtopic.
- It overlaps with existing pages such as `hermes-memory-skills-wiki-boundaries`, `hermes-layer-routing-decision-checklist`, and especially `hermes-context-layer-operating-rules`, so an implementation must reconcile duplication carefully.
- The split is only justified if the new page is differentiated as a LifeOS architecture contract: it must emphasize `profile` as a runtime-state isolation layer and the default-profile LifeOS topology framing, rather than duplicating the generic context-layer routing map.
- If that differentiation cannot be maintained during implementation, defer the split instead of creating a redundant boundary page.
- Extracting it first would reduce hub length while preserving the architecture page as a navigation layer.

Implementation shape:

1. Create the new boundary-contract concept page with its own frontmatter and `## Summary`.
2. Move or restate the detailed layer definitions there.
3. Replace the hub's `Hard boundaries` and `Boundary matrix` detail with a compact summary and link to the new page.
4. Update `index.md` only for the new page entry.
5. Update `log.md` with exact files changed and the explicit no-archive decision; do not create an `_meta/` archive unless separately approved.
6. Keep target page frontmatter, path, `type`, and `status` unchanged.

## 6. Index and link policy

For this plan-only step:

- Do not modify `index.md`.

For a future split implementation:

- If a new concept page is created, add exactly one `index.md` entry under Concepts.
- Preserve the existing `[[hermes-lifeos-executable-architecture]]` entry.
- Add reciprocal links:
  - hub -> new split page;
  - new split page -> hub;
  - new split page -> directly related routing/boundary pages.
- Do not create aliases or move the hub page unless separately approved.

## 7. Archive policy

Preferred default: **do not create a duplicate full-text archive**.

Rationale:

- The target page remains the hub.
- Any future split should leave durable summaries in the hub and move/restate detail into formal concept pages, not hide it in `_meta/`.
- Git history preserves the pre-split version.

If a future implementation needs a rollback reference, use git history rather than an `_meta/plans/archive/` copy unless explicitly approved.

## 8. Required pre-edit checks for a future implementation

Before editing the target page or creating a split page:

1. Confirm wiki repo is clean and committed.
2. Confirm target page still has the same path and frontmatter.
3. Confirm target page remains indexed in `index.md`.
4. Read these related pages to avoid duplicating or contradicting existing concepts:
   - `concepts/hermes-memory-skills-wiki-boundaries.md`
   - `concepts/hermes-layer-routing-decision-checklist.md`
   - `concepts/hermes-context-layer-operating-rules.md`
   - `concepts/hermes-knowledge-architecture.md`
   - `concepts/hermes-knowledge-base-operating-flow.md`
5. Decide whether the first split creates one new page only, or whether the user explicitly approved more.
6. Stop if the split requires changing memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, Hermes core, or project-local files.

## 9. Stop conditions

Stop before implementation if any of these are true:

- wiki health check fails before editing;
- target page path/frontmatter differs unexpectedly;
- the planned split would duplicate an existing page rather than clarify it;
- more than one new concept page seems necessary without explicit approval;
- implementation would require changing active Hermes layers or project-local files;
- new page naming cannot be made stable and descriptive;
- the hub would lose the top-level architecture decision and become only a link list.

## 10. Review questions before actual split

1. Should the first implementation create only `hermes-lifeos-layer-boundary-contract.md`, or should it defer because existing routing/boundary pages already cover enough?
   - Current answer: create it only if the implementation can preserve clear differentiation around LifeOS topology and the `profile` layer. If it becomes a generic context-layer routing page, defer.
2. Should `hermes-lifeos-executable-architecture.md` remain a stable hub with unchanged `status: stable`, or should any split require a separate status review?
3. Is the candidate topology/profile page necessary now, or should profile-policy detail remain in the hub until profile pressure increases?

Default recommendation:

- create no split page in this plan-only step;
- if implementing later, split only the layer boundary contract first;
- preserve the hub path/frontmatter/status;
- update `index.md` only for the new concept page in the implementation commit;
- do not touch active Hermes layers;
- do not create an `_meta/` archive.
