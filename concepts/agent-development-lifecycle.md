---
title: Agent Development Lifecycle
created: 2026-05-11
updated: 2026-08-18
type: concept
tags: [agent, lifecycle, evaluation, deployment, monitoring, governance, hermes]
sources: [raw/articles/langchain-agent-development-lifecycle-2026-05-09.md, raw/articles/machinelearningmastery-agent-regression-tests-2026-08-17.md]
status: stable
description: 定义 Agent 从构建、测试、部署、监控到治理的工程生命周期。
aliases: [agent-lifecycle]
---

# Agent Development Lifecycle

## Summary
Agent 工程化的核心不是让模型一次跑通，而是建立 `Build → Test → Deploy → Monitor` 的闭环，并用 `Govern` 横切管理成本、权限、上下文、工具和复用资产。

核心原则：可靠 agent 不是一次性 demo，而是一个可循环改进的工程系统：先构建明确边界，再用 eval 和场景测试验证，受控部署到可恢复运行时，用 trace 和反馈监控真实行为，并由治理层管理成本、权限、上下文和资产复用。

## Source anchor
本页来自 LangChain 文章 `[[langchain-agent-development-lifecycle-2026-05-09]]`。

该文有产品导向：LangGraph、LangSmith、Deep Agents 等是 LangChain 生态中的参考实现，不应直接等同于 Hermes 的默认方案。本页只沉淀可迁移的生命周期模型。

## Core lifecycle
### 1. Build
Build 阶段先决定 agent 系统的抽象层级，而不是直接堆 prompt 或工具。

常见层级：
- agent framework：组合 model calls、tools、prompts、retrieval、structured outputs 和 loops
- agent runtime：管理 state、control flow、durability、branching、pause/resume 和 human intervention
- agent harness：提供 prompts、skills、MCP servers、hooks、middleware、filesystem 等执行周边
- no-code / low-code builder：让领域专家参与 prompt、workflow 和 context 编辑

可迁移原则：简单任务可以只需要 tool-calling loop；复杂 agent 需要工程师保留 hooks、middleware、auth、approval 和业务规则控制权。

### 2. Test
Test 阶段必须在生产前发生，但不必等完美评估集。

起点可以是：
- dogfooding 中发现的失败案例
- 真实用户反馈
- 边缘任务
- 多轮对话场景
- 工具调用失败路径
- 版本对比样本

多轮 agent 不能只靠单轮问答测试。客服、编程、检索、操作型 agent 都需要场景模拟，因为它们的关键能力是追问、查状态、调用工具、从歧义中恢复并完成端到端任务。

进入 Deploy 前，按系统实际能力选用 `[[production-ai-agent-evaluation-framework]]` 的结构性回归矩阵：上下文裁剪、外部写入、非可信检索、结构化输出、循环编排、RAG 和持久状态分别触发对应测试；不存在该能力时跳过，不把七项清单机械升级为所有 Agent 的统一门禁。真实失败再交给 `[[agent-failure-closed-loop-evaluation]]` 形成回归工件。

### 3. Deploy
Deploy 阶段不同于普通无状态应用部署。

生产级 agent 通常需要：
- durable execution：任务中断、报错或等待审批后可以恢复
- sandbox：隔离代码执行、文件写入和高风险工具调用
- human-in-the-loop：敏感动作、低置信度或外部副作用前暂停等待人工审批
- state persistence：跨步骤保存必要状态，而不是依赖聊天历史
- rollback boundary：输出、配置、权限和调度可回滚

### 4. Monitor
Monitor 阶段不能只看 uptime、latency、cost 或 API error rate。

Agent 可能没有报错，但在几步前选错工具、拿错上下文或传错参数，最后输出一个看似合理的答案。生产监控必须保留 trace：
- 用户输入
- 模型调用
- 工具调用
- 工具返回
- 中间判断
- 最终输出或动作
- 用户反馈或人工审查结果

Trace 的价值不是归档过程，而是让失败能被定位、复现，并转化成下一轮 eval。

### 5. Govern
Govern 横跨 Build、Test、Deploy、Monitor。

治理不是为了减速，而是为了让快速迭代不失控。核心对象包括：
- 成本追踪和预算
- 工具访问权限与审计
- 人类审批点
- prompt / skill / context / agent 资产的复用和版本化
- 生产行为可见性
- 多团队、多 agent 之间的一致边界

## Hermes interpretation
这篇文章给 Hermes 的价值，是把已有零散原则放进一条生命周期总线。

Hermes 映射：
- Build：skills、project context、MCP、subagent、wrapper、runtime profile、wiki/context 层
- Test：fixture、eval、code review、browser/terminal verification、project validation lane
- Deploy：quick command、cron、gateway route、runtime profile；都需要单独批准和回滚边界
- Monitor：run logs、output paths、health checks、trace-like evidence、session/project closeout
- Govern：memory/skill/wiki/project/cron 分层、权限边界、人工审批、成本和工具暴露控制

## Relation to existing wiki
本页不是替代已有页面，而是提供上层 lifecycle frame：
- `[[agent-self-validation-loops]]`：落在 Test / Monitor 的目标-反馈-迭代结构
- `[[subagent-orchestration-patterns]]`：落在 Build 阶段的 agent 生命周期复杂度选择
- `[[agent-orchestration-production-tradeoffs]]`：落在 Build / Deploy 阶段的成本、延迟、准确率和复杂度取舍
- `[[hermes-model-specific-harness-profiles]]`：落在 Build 阶段的模型与 harness 适配
- `[[hermes-context-layer-operating-rules]]`：落在 Govern 层的 context、memory、skill、wiki、cron 分层
- `[[agent-experience-consolidation-loops]]`：落在 Monitor 之后，把失败、反馈和经验回灌成未来资产

## What not to copy blindly
- 不要因为文章强调 LangGraph / LangSmith / Deep Agents，就把它们视为 Hermes 的必选架构。
- 不要把生命周期页直接变成 skill；它当前是架构概念，不是本地已验证 SOP。
- 不要把 Monitor 理解成“保存全部聊天记录”；应保存足以定位失败和构造 eval 的 trace-like evidence。
- 不要把 Govern 理解成重流程审批；治理的目标是低风险快速迭代。

## Validation outcome
2026-05-11 首次项目级映射已完成，样例项目为本地 live worker `amazon-price-watch`。

证据路径：`/home/lin/.hermes/projects/amazon-price-watch/docs/reviews/2026-05-11-agent-development-lifecycle-checklist.md`。

结论：`agent-development-lifecycle` 可作为项目检查表框架使用，能把一个低风险、确定性 worker 映射到 `Build → Test → Deploy → Monitor`，并把 `Govern` 作为跨阶段边界记录：
- Build：README、AGENTS、source-analysis、methodology、typed CLI worker 和 runtime adapter 边界清楚
- Test：pytest、ruff、format、ty、diff check 与既有 review records 构成证据
- Deploy：已有 Hermes no-agent cron wrapper/job 的历史验证证据，但本次未改变 runtime
- Monitor：health、run reports、stdout contract 和 silent-when-healthy 语义可检查
- Govern：不登录、不绕 CAPTCHA、不自动购买、不提交本地 watchlist/data/debug，且 runtime/cron/skill/wiki/memory 推广均需单独批准

边界：这是项目级概念验证，不是 runtime、cron、skill、memory 或 wiki 方法论推广授权。项目证据留在 `amazon-price-watch`；本页只保存概念验证结果和检索入口。

## Validation and promotion path
当前状态：wiki concept 已完成首次项目级验证，但仍不改 memory、skill、cron 或 runtime。

后续若要转成 Hermes 操作实践，应继续在真实小项目或 Hermes-adjacent 项目中验证 lifecycle checklist：
1. Build artifact 是否明确？
2. Test/eval 是否存在？
3. Deploy 边界是否可回滚？
4. Monitor/trace/log 是否能定位失败？
5. Govern 权限、成本、人工审批和资产复用是否明确？

只有当该 checklist 在更多真实项目中证明可复用，再考虑 patch 现有 skills 或新增窄职责 `agent-lifecycle-review` skill；任何 active-layer 变更都需要单独决策、备份、回滚和用户批准。

## Related
- [[langchain-agent-development-lifecycle-2026-05-09]]
- [[agent-self-validation-loops]]
- [[subagent-orchestration-patterns]]
- [[agent-orchestration-production-tradeoffs]]
- [[hermes-model-specific-harness-profiles]]
- [[hermes-context-layer-operating-rules]]
- [[agent-experience-consolidation-loops]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[typed-ai-agent-boundaries]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
