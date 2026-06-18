---
title: Hermes Harness Profile Validation Detailed Plan
created: 2026-04-30
updated: 2026-04-30
type: query
tags: [hermes, optimization, harness, model-profiles, validation, workflow]
sources: [queries/hermes-system-model-specific-harness-optimization-plan.md, concepts/hermes-model-specific-harness-profiles.md, docs:hermes-agent, skill:writing-plans, skill:hermes-project-and-extension-management]
status: draft
description: 规划 Hermes model-specific harness profile 验证的步骤、样例、标准和回滚边界。
aliases: [harness-validation-plan]
---

# Hermes Harness Profile Validation Detailed Plan

## Status

This page is a compact historical navigation page. The original 1324-line execution plan has been compressed according to:

```text
/home/lin/wiki/_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md
```

Current decision: historical plan, superseded by final closeout; project closed; only `writing-plans` and `requesting-code-review` were promoted as narrow skill patches.

Explicitly not authorized by this project: Hermes core, global `SOUL.md`, runtime profile, cron, memory, broad skill rewrite, article summary, or coding/config promotion.

Canonical closeout records:

- Wiki final closeout: [[hermes-harness-profile-validation-final-closeout]]
- Project workspace: `/home/lin/.hermes/projects/hermes-harness-profile-validation/`
- Project final closeout: `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md`
- Gate 6 regression: `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/gate-6-post-patch-regression-2026-04-30.md`

Git history remains the archive for the original full execution-plan text. No duplicate `_meta/plans/archive/` copy was created.

## Why this mattered

LangChain 的 Deep Agents / HarnessProfile 思路说明：Agent 表现不只取决于底层模型，还取决于外部 harness。对 Hermes 来说，harness 不是一个单独 profile 文件，而是多层组合：

- system/developer 规则
- memory / user profile
- skills
- project-local `AGENTS.md`
- wrapper scripts / quick commands
- tool choice and naming
- subagent delegation pattern
- verification commands
- cron entrypoints
- wiki / project state

核心判断是：**不要直接新增 runtime profile；先建立可验证的 harness overlay 机制。**

This mattered because the current Hermes default path was already stable. Any model/workflow-specific overlay needed evidence before promotion, especially before touching runtime profile, cron, memory, global prompt, or core behavior.

## Scope and non-scope

The validation project was designed to cover:

- Create a Hermes-adjacent validation project.
- Compare baseline vs overlay behavior across representative Hermes tasks.
- Define an evaluation rubric.
- Run realistic or semi-realistic tasks.
- Decide whether evidence justified patching existing skills.
- Produce a decision basis for any later wrapper, cron, runtime profile, or core consideration.

The validation project did not authorize:

- Hermes core changes.
- New `lab`, `claude`, `gemini`, or other runtime profiles.
- Global `SOUL.md` changes.
- Writing model differences into memory.
- Creating a long-running cron.
- Turning the validation plan itself into a skill.

## Durable design principles

1. **Default profile stays stable.** The current `default` profile is the main operating path, not the experiment surface.
2. **Overlay before core change.** Safer landing order: project-local prompt / `AGENTS.md` → wrapper or quick command → narrow skill patch → cron automation → runtime profile → Hermes core.
3. **Eval before promotion.** Any overlay must have baseline runs, overlay runs, rubric scoring, and a keep/revise/discard decision before promotion.
4. **Keep model knowledge out of memory.** Model/workflow behavior belongs in wiki concepts, project validation docs, skill details, or wrapper prompt templates, not memory.
5. **Verification is part of harness.** An overlay that merely sounds better but does not improve grounding, validation, rollback, or layer routing should not be promoted.

## Evidence and canonical records

Project-level records:

- README: `/home/lin/.hermes/projects/hermes-harness-profile-validation/README.md`
- Status: `/home/lin/.hermes/projects/hermes-harness-profile-validation/STATUS.md`
- Final closeout: `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md`
- Gate 6 regression: `/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/gate-6-post-patch-regression-2026-04-30.md`

Wiki records:

- Final closeout: [[hermes-harness-profile-validation-final-closeout]]
- Split/compression plan: `_meta/plans/2026-05-18-hermes-harness-profile-validation-split-compression-plan.md`
- Claude plan review: `_meta/reviews/2026-05-18-hermes-harness-profile-validation-split-compression-plan-claude-review.md`

## Original execution map

The original full page included workstream-level implementation detail. Those details now belong in project-local records and git history, not inline in this query page.

- Workstream A — Bootstrap the validation project: project skeleton, README, `AGENTS.md`, `.gitignore`.
- Workstream B — Define core project documents: project brief, overlay registry, scoring rubric, promotion policy, ADR 0001.
- Workstream C — Create prompt templates: baseline and overlay prompts for coding/config, article summary, code review, and planning.
- Workstream D — Create experiment template and first experiment records.
- Workstream E — Fixtures for coding/config, article summary, code review, and planning.
- Workstream F — Verification scripts, including project verification and score parsing.
- Workstream G — Run four evaluation lanes and compare baseline vs overlay outcomes.

The original generated templates, scripts, fixtures, and task bodies were intentionally removed from the wiki page body to reduce retrieval noise. Use the project workspace and git history for full execution detail.

## Promotion and stop gates

The actual validation path had six gates:

1. **Gate 1: Project bootstrap complete** — project exists, required docs exist, verifier passes, git status is clean.
2. **Gate 2: Prompt templates complete** — baseline and overlay prompts exist with explicit verification expectations.
3. **Gate 3: First evaluation round complete** — eight experiment records exist, completed records have rubric scores, and at least one overlay shows measurable improvement.
4. **Gate 4: Promotion decision** — candidate overlay has repeated success in the same lane, no safety/verification/layer-routing regression, and a clear landing zone.
5. **Gate 5: Skill patch decision** — patch is narrow, trigger condition is clear, verification condition is clear, and the skill is not turned into a model encyclopedia.
6. **Gate 6: Post-patch regression** — project-local regression validated only `writing-plans` and `requesting-code-review`; both passed, and no rollback was required.

Final promotion result:

- `writing-plans`: promoted as a narrow Hermes-adjacent planning gate.
- `requesting-code-review`: promoted as evidence-first code review discipline with `what_was_checked`.
- `gemini-summary` / article summary: not promoted in this project.
- Coding/config overlay: deferred.
- Runtime profile / wrapper / cron / core / memory: not promoted.

## Rollback and safety

The original safety boundary remains valid:

- Do not run `hermes profile create ...` from this project.
- Do not run `hermes config set ...` from this project.
- Do not create cron from this project.
- Do not patch active skills further from this project without a new explicit validation scope and fresh repeat evidence.
- Do not write procedural rules into memory.
- Keep secrets in environment files, not project docs or prompts.

For this compressed wiki page, rollback is via wiki git history.

## Final acceptance criteria

The original plan succeeded when:

- a reproducible validation project existed;
- four Hermes workflow lanes had baseline/overlay comparison records;
- at least one overlay had a scored keep/revise/discard decision;
- no Hermes core/runtime/global memory pollution occurred;
- any promoted change had a narrow landing zone and verification path.

The final closeout confirms that the project met these criteria only for two narrow skill patches, not for broader harness/runtime changes.

## Reusable rule

The durable rule from this project is:

```text
wiki concept → project-local evidence → repeated lane evidence → narrow skill patch → post-patch regression → only then consider wrapper/cron/runtime/core
```

For future Hermes harness work, start with project-local validation and stop at the narrowest proven layer.

## Relations
- depends_on: [[hermes-system-model-specific-harness-optimization-plan]]
- depends_on: [[hermes-model-specific-harness-profiles]]

## Related

- [[hermes-harness-profile-validation-final-closeout]]
- [[hermes-system-model-specific-harness-optimization-plan]]
- [[hermes-model-specific-harness-profiles]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-knowledge-architecture]]
- [[index]]
- [[log]]
