# Claude review prompt — Hermes harness validation split/compression plan

You are an independent reviewer. Review the plan only. Do not modify files.

## Context

Wiki root: `/home/lin/wiki`

Plan under review:

```text
_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md
```

Target long page, not to be edited in this review:

```text
queries/hermes-harness-profile-validation-detailed-plan.md
```

Prior triage:

```text
_meta/plans/2026-05-18-long-page-triage.md
```

Relevant project-local evidence, read-only only:

```text
/home/lin/.hermes/projects/hermes-harness-profile-validation/README.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/STATUS.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md
/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/gate-6-post-patch-regression-2026-04-30.md
```

## Review goal

Check whether the page-specific split/compression plan is safe, scoped, reversible, and sufficiently concrete before any future rewrite of `queries/hermes-harness-profile-validation-detailed-plan.md`.

The intended implementation later is only to compact a 1324-line historical execution plan into a shorter wiki navigation/decision page, while preserving evidence through links/git history/project-local records.

## Hard constraints

Flag as BLOCKING if the plan would allow or imply any of these without explicit later approval:

- editing the target long page during the planning/review step;
- deleting evidence rather than preserving it through git history or explicit archive policy;
- modifying `/home/lin/.hermes/projects/hermes-harness-profile-validation/`;
- modifying memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core;
- changing page path, title, frontmatter, tags, `type`, or index entries without an explicit future decision;
- relying on missing project-local closeout/evidence files;
- weakening the closed-project boundary that says no further skill/runtime/core/memory/cron changes are authorized.

## Questions to answer

1. Verdict: `APPROVE`, `APPROVE_WITH_CHANGES`, or `REJECT`.
2. Blocking findings, if any.
3. Important findings that should be patched into the plan before implementation.
4. Minor findings or wording improvements.
5. Whether the default archive policy is acceptable: use git history + existing project-local evidence by default; create a browsable `_meta/plans/archive/...` copy only if explicitly approved.
6. Whether the proposed final wiki page shape is enough to preserve durable lookup value.
7. Whether the pre-edit checks and stop conditions are sufficient.

## Output format

Write a concise markdown review with these sections:

```markdown
# Claude Review — Hermes harness validation split/compression plan

Verdict: APPROVE | APPROVE_WITH_CHANGES | REJECT

## Blocking findings
- ...

## Important findings
- ...

## Minor findings
- ...

## Archive policy assessment
...

## Page-shape assessment
...

## Pre-edit gate assessment
...

## Recommended patch list
1. ...
```

Be specific: cite file paths and plan sections when possible.
