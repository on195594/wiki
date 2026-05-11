---
title: Draft query inventory
created: 2026-05-11
updated: 2026-05-11
type: meta
status: current
---

# Draft Query Inventory

## Summary

This page records unindexed `queries/` drafts that should not be mechanically promoted into `index.md`.

Current conclusion: all eight reviewed pages are intentionally outside the main index. They are either superseded by a stronger page or are low-value generated kickoff drafts that should stay discoverable only by search until the user explicitly resumes that project.

No draft page was deleted or edited during this review.

## Review date

2026-05-11

## Decisions

### Education fund weekly page

Decision: keep one resumption candidate, treat the other two as superseded drafts, do not index any of them yet.

- `queries/project-kickoff-education-fund-weekly-page-v2.md`
  - Status: draft
  - Decision: keep as the best resumption candidate
  - Reason: most specific title and intent: education fund weekly page as a family review entry
  - Index: no; still a kickoff draft, not a closed/stable knowledge artifact
  - Resume by: turning it into a project-local plan or a concrete weekly-page template

- `queries/project-kickoff-education-fund-weekly-page.md`
  - Status: draft
  - Decision: superseded by `project-kickoff-education-fund-weekly-page-v2.md`
  - Index: no

- `queries/qa-kickoff-education-fund-weekly-page.md`
  - Status: draft
  - Decision: superseded by `project-kickoff-education-fund-weekly-page-v2.md`
  - Index: no

Related stable pages:
- [[personal-finance-and-education-fund-model]]
- [[family-education-operating-model]]
- [[hermes-lifeos-executable-architecture]]

### Skill install review flow

Decision: archive all three as validation inputs / generated kickoff drafts; do not index.

- `queries/project-kickoff-20260423-195654.md`
  - Status: draft
  - Decision: archive as superseded/generated kickoff draft
  - Reason: the value of this idea was already captured by later workflow-governance and gstack validation pages; the page itself remains generic
  - Index: no

- `queries/qa-kickoff-skill-install-review-flow-v2.md`
  - Status: draft
  - Decision: archive as superseded/generated kickoff draft
  - Reason: duplicates the project kickoff variant closely
  - Index: no

- `queries/qa-kickoff-skill-install-review-flow.md`
  - Status: draft
  - Decision: archive as superseded/generated kickoff draft
  - Reason: useful historically as a generated sample, but not a current retrieval target
  - Index: no

Related stable pages:
- [[gstack-project-execution-lane-validation-case]]
- [[hermes-layer-routing-sample-cases]]
- [[hermes-layer-routing-edge-cases]]
- [[hermes-context-layer-operating-rules]]

### Hermes weekly health enhancement

Decision: archive both drafts as superseded by the operations page; do not index.

- `queries/project-kickoff-hermes-weekly-health-enhancement.md`
  - Status: draft
  - Decision: archive as superseded
  - Reason: the operational outcome already exists as `operations/hermes-health-dashboard.md`
  - Index: no

- `queries/qa-kickoff-hermes-weekly-health-enhancement.md`
  - Status: draft
  - Decision: archive as superseded
  - Reason: lower-value generated kickoff page; the stable retrieval target is the operations page
  - Index: no

Related stable page:
- [[hermes-health-dashboard]]

## Index policy from this review

Do not add these pages to `index.md` unless one of the following happens:

1. A draft becomes a stable operating model, closeout, validation result, or reusable decision page.
2. A project is resumed and the draft is converted into an implementation plan or validated template.
3. The page becomes the canonical retrieval target for a recurring workflow.

Generated kickoff drafts should normally remain unindexed.

## Cleanup policy

If future cleanup is approved, prefer one of these actions instead of deletion-first cleanup:

1. Keep only the best resumption candidate for a topic and mark older duplicates as archived.
2. Move superseded generated drafts into an explicit archive directory or archive manifest.
3. Preserve historically useful generated examples only when they support a validation case.

Current recommended next action: leave files in place; no index promotion.
