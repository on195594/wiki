---
title: Hermes Project Development Migration Plan Eng Review
created: 2026-04-24
updated: 2026-04-24
type: query
tags: [hermes, gstack, eng-review, migration, project-development]
sources: [filesystem:~/.hermes, filesystem:~/wiki, review:hermes-project-dev-office-hours-review]
status: draft
---

# Hermes Project Development Migration Plan Eng Review

## Status

This is now a compact historical engineering decision record, not an active migration command list.

Preserved boundaries:

- Path, title, frontmatter, tags, `type`, `status`, and the `index.md` entry are unchanged.
- No project-local files, cron jobs, runtime config, memory, skills, MCP config, wrappers, quick commands, `SOUL.md`, or Hermes core were changed.
- No browsable full-text archive was created; git history remains the full original archive.

Current evidence observed during compression:

- `/home/lin/.hermes/projects/investment-watch/` exists.
- `/home/lin/.hermes/projects/project-kickoff/` exists.
- `queries/investment-watch-final-closeout.md` exists.
- No `project-kickoff` wiki closeout/status page was found; treat that as a follow-up gap, not something this page creates.

## Summary decision

The original review concluded that the safest and smallest path was not more cleanup inside `~/.hermes/scripts/`, but moving already independent business/project code into explicit project roots.

Durable decision:

- Hermes remains the host/runtime layer: config, orchestration, cron, memory, skills, and gateway behavior.
- Business projects keep project-local code, data, tests, docs, and rules.
- Project boundaries should be visible from paths, not reconstructed from chat context or memory.

Recommended migration order:

1. `investment-watch`
2. `project-kickoff`
3. `~/.hermes/scripts/README.md` and remaining quick-command/runtime-helper cleanup

## Scope and non-scope

In scope for the original migration plan:

- Create real roots for `investment-watch` and `project-kickoff`.
- Move code/data under those roots where appropriate.
- Replace hardcoded old paths with project-relative path resolution.
- Add minimal project-local `AGENTS.md`, `pyproject.toml`, `README.md`, and tests.
- Clarify that `~/.hermes/scripts/` is for quick commands and runtime helpers after the migrations.

Out of scope:

- Hermes core changes, CI/CD, monorepo packaging, global quick-command rewrites, automatic project discovery, shared tooling abstractions, plugin redesign, or runtime-profile redesign.

## Durable engineering findings

Architecture:

- `investment-watch` originally had code and state split across runtime/data directories, so there was no single project root.
- `project_kickoff.py` was project code, not a quick-command helper.
- The intended durable shape was `~/.hermes/projects/<project>/` with project-local code, docs, tests, data, and rules.

Code quality:

- Absolute path coupling was the main risk.
- The repair was project-relative path resolution, preferably centralized in a small paths module.
- `~/.hermes/scripts/README.md` needed to stop treating the directory as a home for independent business project code.
- Project-level `AGENTS.md` files were needed so local constraints did not live only in global Hermes rules.

Testing:

- Tests were part of the migration, not optional cleanup.
- The review identified 20 migration/test gaps across directory creation, imports, data path resolution, CLI behavior, old-path references, cron entrypoints, and smoke execution.
- Two critical gaps were non-negotiable: cron/internal path references and minimum tests.

Performance:

- No performance blocker was found.
- The review warned against turning boundary cleanup into a service-layer or modularization rewrite.

## Historical implementation map

Phase 1: `investment-watch`

- Intent: create `/home/lin/.hermes/projects/investment-watch/`, keep code/tests/docs/data/backups under it, resolve paths from the project root, update cron/README/internal references as part of verified migration, and add smoke/pytest coverage.
- Current pointers: project path exists; wiki closeout exists at [[investment-watch-final-closeout]].

Phase 2: `project-kickoff`

- Intent: create `/home/lin/.hermes/projects/project-kickoff/`, keep generator code under `src/project_kickoff/`, tests under `tests/`, preserve CLI contract `--idea`, `--slug`, optional `--title`, and refuse overwriting existing generated wiki pages.
- Current pointers: project path exists; no matching wiki closeout/status page was found during compression.

Phase 3: `scripts/` cleanup

- Intent: treat `~/.hermes/scripts/` as quick-command/runtime-helper space only, after the two project boundaries are real.

## Current evidence and pointers

Wiki records:

- Prior office-hours diagnosis: [[hermes-project-dev-office-hours-review]]
- Investment-watch closeout: [[investment-watch-final-closeout]]
- Related validation case: [[gstack-project-execution-lane-validation-case]]
- Related layering concept: [[hermes-agent-workflow-layering-and-adoption-order]]

Project-local evidence paths, read-only references only:

- `/home/lin/.hermes/projects/investment-watch/`
- `/home/lin/.hermes/projects/project-kickoff/`
- `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-final-project-knowledge-closeout.md`
- `/home/lin/.hermes/projects/investment-watch/docs/plans/2026-05-08-final-knowledge-consolidation-plan.md`

Full original detail: recover from wiki git history before this compression commit.

## Final verdict

Original verdict: `DONE_WITH_CONCERNS`.

Meaning:

- The migration direction was clear enough to execute.
- The review completed its major phases: scope challenge, architecture review, code quality review, test review, performance review, non-scope definition, existing-state review, and parallelization strategy.
- It explicitly surfaced 2/2 critical gaps, so the verdict was not a shortcut approval.

The two concerns that could not be skipped:

1. Migration must handle cron and internal hardcoded paths.
2. Migration must include minimum tests in the same round; otherwise it only reorganizes directories without restoring determinism.

## Reusable rule

When a Hermes-adjacent capability has independent business intent, state, execution entrypoints, and tests, treat it as a project.

Do not let `~/.hermes/scripts/` become a project incubator by default. Use it for host/runtime helpers and quick commands; move durable project code into explicit project-local roots.

## Related

- [[hermes-project-dev-office-hours-review]]
- [[investment-watch-final-closeout]]
- [[gstack-project-execution-lane-validation-case]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
