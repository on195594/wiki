---
title: Hermes Wiki Knowledge Object Governance Closeout
created: 2026-06-18
updated: 2026-06-18
type: query
tags: [hermes, knowledge-base, governance, workflow]
sources: [queries/okf-for-hermes-wiki-governance-assessment.md, concepts/hermes-knowledge-architecture.md, concepts/hermes-wiki-page-writing-standards.md, concepts/hermes-wiki-lint-and-health-check-standards.md, skill:hermes-wiki-and-domain-knowledge, skill:coding-agent-delegation]
status: stable
description: 复盘 Hermes wiki knowledge-object metadata 治理，从 OKF 评估、5 页试点、真实查询验证到全 wiki 推广和反保守修正。
aliases: [knowledge-object-governance-closeout, wiki-metadata-rollout-closeout]
---

# Hermes Wiki Knowledge Object Governance Closeout

## Summary
本次治理把 OKF/knowledge-object 思路收敛为 Hermes wiki 的轻量机器可读增强：`description`、保守 `aliases`、白名单 `## Relations`。关键教训是：低风险、可回滚、health check 和真实查询验证已通过的 wiki metadata 改动，不应被继续观察拖延；应及时推广，再用真实使用修正。

## Outcome
已落地三阶段提交：

1. `104ae7e docs: 增强 wiki 机器可读治理规范`
2. `7c252d6 docs: 试点 wiki 知识对象元数据`
3. `451ec1b docs: 推广 wiki 知识对象元数据`

最终状态：
- formal pages: 88
- pages with `description`: 88
- pages with `aliases`: 57
- pages with `## Relations`: 43
- relation lines: 145
- wiki health check: P0=0, P1=0, P2=0

## What changed

### Local wiki conventions
- `SCHEMA.md` documented optional agent-readable metadata.
- `[[hermes-wiki-page-writing-standards]]` documented `description`, `aliases`, and relation vocabulary.
- `[[hermes-wiki-lint-and-health-check-standards]]` documented metadata and relation health-check direction.
- `[[okf-for-hermes-wiki-governance-assessment]]` recorded accepted, deferred, and rejected choices.

### Pilot
Five core governance pages received `description`, conservative `aliases`, and white-listed `## Relations`:
- [[hermes-knowledge-architecture]]
- [[wiki-ingestion-workflow]]
- [[hermes-wiki-page-writing-standards]]
- [[hermes-wiki-lint-and-health-check-standards]]
- [[hermes-memory-skills-wiki-boundaries]]

### Broad rollout
Codex `/goal` applied metadata across formal wiki pages. Hermes verified changed paths, relation-key whitelist, source preservation, sample diffs, `git diff --check`, and wiki health. AGY then performed read-only review and returned `APPROVE`.

## Decision correction
The initial recommendation to “observe for 1–2 weeks before rollout” was too conservative for this risk tier. It treated validation sufficiency as the main risk and underweighted governance-stall risk.

Corrected rule:
> For low-risk wiki/documentation metadata governance, if a narrow pilot has backup/rollback, small inspected diff, passing health check, no active-layer side effects, and several realistic queries show retrieval value, promote promptly to the intended wiki scope and fix mistakes from real use.

This rule does not apply to active skill/runtime/cron/MCP/memory/credential/production changes.

## Durable workflow updates
The lesson was moved out of memory-only handling and into workflow references:
- `hermes-wiki-and-domain-knowledge/references/okf-knowledge-object-governance.md`
  - Added anti-stall promotion rule.
  - Clarified post-pilot broad metadata rollout is acceptable after realistic-query validation and rollback/health gates.
- `coding-agent-delegation/references/delegation-lanes-and-contracts.md`
  - Added Codex `/goal` broad wiki/documentation rollout pattern.
  - Explicitly requires Hermes parent verification and read-only AGY review before commit.

Memory now only records the user's stable execution preference; the procedural rule lives in skill references and this wiki closeout.

## Verification evidence
Final verification after rollout:

```bash
python3 /home/lin/wiki/_meta/scripts/wiki_health_check.py --root /home/lin/wiki
```

Result:
- `pass=true`
- P0/P1/P2 all empty
- `git_status.dirty=false` after commit `451ec1b`

Reference updates were also read back after patching. The knowledge-governance validator currently reports pre-existing missing pointers in `hermes-knowledge-and-workflow-governance`; that validator failure is not caused by this closeout change and should be handled separately if that skill is edited.

## Remaining risks
- Some `description` text may be merely adequate rather than optimal; fix per real query failure.
- `aliases` are intentionally incomplete; add only when a real query misses a page.
- Most relations are `depends_on`; refine to `refines`, `conflicts_with`, or `supersedes` only when a real maintenance task proves the stronger relation.
- No validator yet enforces relation-key whitelist or description quality inside the wiki health check; parent/AGY scripts covered this rollout, but a future read-only validator can codify it.

## Relations
- refines: [[okf-for-hermes-wiki-governance-assessment]]
- depends_on: [[hermes-wiki-page-writing-standards]]
- depends_on: [[hermes-wiki-lint-and-health-check-standards]]
- depends_on: [[hermes-memory-skills-wiki-boundaries]]

## Related
- [[hermes-knowledge-architecture]]
- [[wiki-ingestion-workflow]]
- [[okf-for-hermes-wiki-governance-assessment]]
- [[index]]
- [[log]]
