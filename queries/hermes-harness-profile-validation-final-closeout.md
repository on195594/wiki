---
title: Hermes Harness Profile Validation Final Closeout
created: 2026-04-30
updated: 2026-04-30
type: query
tags: [hermes, harness, validation, skills, governance, closeout]
sources: [concepts/hermes-model-specific-harness-profiles.md, queries/hermes-harness-profile-validation-detailed-plan.md]
status: stable
---

# Hermes Harness Profile Validation Final Closeout

## Summary
Hermes model-specific harness validation 已完成。结论不是立刻扩张 runtime profile，而是确认一条更安全的推广路径：先在 wiki/project 中形成概念和证据，再用重复验证推动窄 skill patch，最后通过 post-patch regression 证明没有明显副作用。

本轮最终只推广两个窄 skill patch：

1. `writing-plans`：加入 Hermes-adjacent planning gate。
2. `requesting-code-review`：加入 evidence-first review discipline 和 `what_was_checked` 输出要求。

没有推广 `gemini-summary`、coding/config、runtime profile、Hermes core、`SOUL.md`、cron 或 memory 变更。

## Source project
Project workspace:

```text
/home/lin/.hermes/projects/hermes-harness-profile-validation
```

Final closeout doc:

```text
/home/lin/.hermes/projects/hermes-harness-profile-validation/docs/final-project-closeout-2026-04-30.md
```

Final project commit:

```text
e4d4bc1 docs: add final harness validation closeout
```

## Evidence path
### First evidence round

- Coding/config baseline: `11/12`
- Coding/config overlay: `12/12`
- Article summary baseline: `9/12`
- Article summary overlay: `10/12`
- Code review baseline: `6/12`
- Code review overlay: `11/12`
- Planning baseline: `5/12`
- Planning overlay: `12/12`

Gate 4 deferred promotion because one successful run was not enough.

### Repeat evidence round

- Planning overlay repeat: `11/12`
- Code review overlay repeat: `11/12`
- Article summary wrapper repeat: `10/12`

Repeat evidence supported only Planning and Code Review promotion review. Article summary remained useful but not ready for patching because source/extraction limitation preservation still needs narrower validation.

### Skill patch decision

Promoted as narrow active-skill patches:

- `writing-plans`: planning gate for Hermes-adjacent changes.
- `requesting-code-review`: evidence-first review rules.

Backups before patch:

```text
/home/lin/.hermes/backups/gate5-skill-patch-20260430-223004/
```

### Post-patch regression

Gate 6 validated only the two patched skills:

- `writing-plans`: PASS.
- `requesting-code-review`: PASS.

No rollback needed.

## Final lane decisions
### Planning
Final decision: **promoted** to `writing-plans`.

Reason: repeated improvement across Hermes-adjacent planning tasks, with clear layer routing, promotion gates, verification, and rollback discipline.

### Code review
Final decision: **promoted** to `requesting-code-review`.

Reason: repeated improvement on context-dependent review fixtures and lower risk of speculative findings.

### Article summary
Final decision: **not promoted in this project**.

Reason: wrapper path preservation is proven, but source/extraction limitation handling needs a summary-only validation before patching `gemini-summary` or `article-and-content-summarization`.

### Coding/config
Final decision: **deferred**.

Reason: current Hermes baseline was already strong, and no repeat evidence round was requested.

## Reusable governance rule
The reusable rule from this project is:

```text
wiki concept → project-local evidence → repeated lane evidence → narrow skill patch → post-patch regression → only then consider wrapper/cron/runtime/core
```

This matters because the external HarnessProfile idea is valid, but Hermes should not translate it directly into runtime profiles. Runtime profile changes are late-stage promotions, not the first move.

## What this changes in future Hermes work
When future work proposes model/workflow-specific harness changes:

1. Start with a small validation project or project-local fixture.
2. Compare baseline vs overlay on the same task.
3. Require repeat evidence before touching active skills.
4. Patch only the narrow skill that owns the behavior.
5. Run post-patch regression against the patched skill path.
6. Do not promote to wrapper, cron, runtime profile, core, or memory without separate evidence.

## Related
- [[hermes-model-specific-harness-profiles]]
- [[hermes-harness-profile-validation-detailed-plan]]
- [[hermes-system-model-specific-harness-optimization-plan]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[index]]
- [[log]]
