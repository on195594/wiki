---
title: Investment Watch Final Closeout
created: 2026-05-08
updated: 2026-05-08
type: query
tags: [investment, monitoring, automation, hermes, validation, closeout]
sources: [project:/home/lin/.hermes/projects/investment-watch]
status: closed
---

# Investment Watch Final Closeout

## Final status

`investment-watch` 已完成当前项目知识层 closeout。

当前状态：

```text
validated locally; promotion deferred unless separately approved
```

这意味着：项目已经在本地验证了一条从基金监控脚本到 typed、contract-backed、reviewable、read-only 投资观察系统的演进路径；但它还不是自动交易系统，也没有自动授权 Hermes cron/runtime、skill、memory 或全局 wiki 方法论推广。

Project path:

- `/home/lin/.hermes/projects/investment-watch`

Primary project closeout:

- `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-final-project-knowledge-closeout.md`

Consolidation plan:

- `/home/lin/.hermes/projects/investment-watch/docs/plans/2026-05-08-final-knowledge-consolidation-plan.md`

## What was validated

### 1. Local project boundary

项目验证了一个重要边界：Hermes 负责调度和 Telegram 入口，投资业务逻辑保留在独立项目中。

有效结构：

```text
Hermes scheduler / Telegram delivery
→ project-local code, data, tests, contracts, reviews
→ explicit promotion gates before any runtime change
```

### 2. Script-to-system typed evolution

项目验证了脚本型个人自动化可以按阶段演进，而不是一次性重写：

```text
usable watcher script
→ git baseline
→ typed decision contract
→ typed portfolio plan
→ operational diagnostics
→ typed exposure
→ report / decision outcome contract
→ read-only strategic rebalance
→ read-only cash constraint
→ read-only post-signal review
→ warning-only risk guardrails
→ standalone read-only data lifecycle audit
→ project knowledge closeout
```

关键方法：

- 一次只收窄一个 typed boundary。
- JSON 输出从结构化数据渲染，不从中文文本反解析。
- 新报告字段 additive 扩展，不破坏既有输出。
- 高风险报告/决策改动必须保留 safety semantics。
- 每个 phase 都用 closeout 明确 closure 和 non-closure。

### 3. Read-only 投资观察层

项目证明了 read-only / warning-only 层可以提升决策纪律，而不必马上改变交易策略。

已经验证的观察层包括：

- `exposure_report`
- `strategic_rebalance_report`
- `cash_constraint_report`
- `post_signal_review_report`
- `risk_guardrail_report`
- standalone `data_lifecycle_audit_report`

这些层提供组合暴露、再平衡观察、现金约束、执行/信号复盘、风险警告和数据卫生视角，但不自动改变买卖候选、排序、阈值、目标权重、预算、cooldown、基金列表、报价策略或运行时行为。

## What was not validated or promoted

本 closeout 不代表以下事项已完成或获准：

- 自动交易；
- 自动投资建议；
- 策略变更；
- 阈值、目标权重、基金列表、优先级、预算、cooldown、报价符号或汇率变更；
- cash-state 真实数据创建或写入；
- trade-log / fund-state / fund-rules 修复、迁移、normalize、backfill；
- 把 strategic rebalance 当作卖出指令；
- 把 risk guardrails 当作自动候选 blocker 或 creator；
- 把 post-signal review 用作信号生成输入；
- 把 data lifecycle audit findings 用作自动状态更新；
- 把 data lifecycle audit 接入 `market_watch` 日常输出；
- Hermes cron/runtime/config/provider/gateway/wrapper/SOUL/AGENTS 变更；
- memory 或 skill 推广。

这些都需要单独计划、备份、验证和明确批准。

## Evidence paths

Core project documents:

- Roadmap: `/home/lin/.hermes/projects/investment-watch/docs/plans/2026-05-01-next-development-plan.md`
- Report contract: `/home/lin/.hermes/projects/investment-watch/docs/contracts/report-decision-outcome-contract.md`
- Final knowledge plan: `/home/lin/.hermes/projects/investment-watch/docs/plans/2026-05-08-final-knowledge-consolidation-plan.md`
- Final project closeout: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-final-project-knowledge-closeout.md`

Phase closeouts:

- Phase 13 strategic rebalance: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-phase-13-strategic-rebalance-closeout.md`
- Phase 14 cash state / new money: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-phase-14-cash-state-new-money-closeout.md`
- Phase 15 post-signal review: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-phase-15-post-signal-review-closeout.md`
- Phase 16 risk guardrails: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-phase-16-risk-guardrails-closeout.md`
- Phase 17 data lifecycle audit: `/home/lin/.hermes/projects/investment-watch/docs/reviews/2026-05-08-phase-17-data-lifecycle-state-hygiene-closeout.md`

Source/evidence areas:

- Source: `/home/lin/.hermes/projects/investment-watch/src/investment_watch/`
- Tests: `/home/lin/.hermes/projects/investment-watch/tests/`
- Data: `/home/lin/.hermes/projects/investment-watch/data/`
- Backups and smoke evidence: `/home/lin/.hermes/projects/investment-watch/backups/`

## Promoted knowledge

Promoted to wiki:

- This closeout retrieval page.

Promoted to concept page:

- Not yet. Next step is to add a short validation outcome to an existing concept page, likely [[public-info-monitoring-automation-methodology]] or a typed-boundary / local-project evolution concept if one is chosen.

Promoted to skill:

- Nothing from this step.
- Candidate future targets, only after concept validation and explicit approval:
  - `market-watch-automation`
  - `public-info-monitoring-automation`
  - `post-session-knowledge-review`

Promoted to memory:

- Nothing. Project progress, phase logs, market state, holdings, and one-off closeout status belong in project docs or wiki, not memory.

Promoted to runtime/core/cron:

- Nothing.

## Reusable rule

For personal automation projects that may later become Hermes workflows:

```text
working local script
→ project-local boundary
→ typed contracts
→ additive structured outputs
→ read-only / warning-only observation layers
→ phase closeouts with non-closure boundaries
→ wiki retrieval page
→ concept validation outcome
→ only then consider skill/runtime promotion with explicit approval
```

The strongest lesson is not investment-specific: do not promote automation just because a project has useful output. Promote only after the layer below has evidence, closure, and explicit non-closure boundaries.

## Next step

Recommended next knowledge step:

- Add a short validation outcome to an existing concept page.

Candidate concepts:

- [[public-info-monitoring-automation-methodology]]
- [[personal-investment-operating-rules]]
- [[ordinary-investor-investment-system]]
- [[hermes-context-layer-operating-rules]]

Do not patch skills or change runtime until the concept-level validation outcome exists and the user explicitly approves promotion.

## Related

- [[public-info-monitoring-automation-methodology]]
- [[personal-investment-operating-rules]]
- [[ordinary-investor-investment-system]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-layer-routing-decision-checklist]]
- [[gsearch-knowledge-validation-closeout]]
- [[hermes-harness-profile-validation-final-closeout]]
- [[index]]
- [[log]]
