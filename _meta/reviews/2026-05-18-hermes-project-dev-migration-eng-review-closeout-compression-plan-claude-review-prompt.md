# Claude review prompt — Hermes project dev migration eng review closeout/compression plan

You are an independent reviewer. Review the plan only. Do not modify files.

## Context

Wiki root:

```text
/home/lin/wiki
```

Plan under review:

```text
_meta/plans/2026-05-18-hermes-project-dev-migration-eng-review-closeout-compression-plan.md
```

Target long page, not to be edited in this review:

```text
queries/hermes-project-dev-migration-plan-eng-review.md
```

Prior triage:

```text
_meta/plans/2026-05-18-long-page-triage.md
```

Related source page:

```text
queries/hermes-project-dev-office-hours-review.md
```

Relevant project-local paths, read-only only:

```text
/home/lin/.hermes/projects/investment-watch/
/home/lin/.hermes/projects/project-kickoff/
```

## Review goal

Check whether the page-specific closeout/compression plan is safe, scoped, reversible, and concrete enough before any future rewrite of `queries/hermes-project-dev-migration-plan-eng-review.md`.

The intended later implementation is only to compact a 536-line historical engineering review into a shorter wiki decision/navigation page, while preserving the decision trail through git history, related wiki pages, and project-local evidence pointers.

## Hard constraints

Flag as BLOCKING if the plan would allow or imply any of these without explicit later approval:

- editing the target long page during the planning/review step;
- deleting evidence rather than preserving it through git history or explicit archive policy;
- modifying `/home/lin/.hermes/projects/investment-watch/` or `/home/lin/.hermes/projects/project-kickoff/`;
- modifying memory, skills, cron, runtime config, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core;
- changing page path, title, frontmatter, tags, `type`, `status`, or index entries during the first compression;
- treating historical migration recommendations as current commands without checking current project-local state;
- creating a project-kickoff closeout/status page as part of the compression commit instead of recording it as a separate follow-up gap.

## Questions to answer

1. Verdict: `APPROVE`, `APPROVE_WITH_CHANGES`, or `REJECT`.
2. Blocking findings, if any.
3. Important findings that should be patched into the plan before implementation.
4. Minor findings or wording improvements.
5. Whether the default archive policy is acceptable: use git history by default; create a browsable `_meta/plans/archive/...` copy only if explicitly approved.
6. Whether the proposed final page shape preserves enough durable lookup value.
7. Whether the pre-edit checks and stop conditions are sufficient.
8. Whether the plan correctly handles the fact that current project directories already exist and the target page may be historical/superseded.

## Output format

Write a concise markdown review with these sections:

```markdown
# Claude Review — Hermes project dev migration closeout/compression plan

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

## Historical/current-state handling
...

## Recommended patch list
1. ...
```

Be specific: cite file paths and plan sections when possible.
