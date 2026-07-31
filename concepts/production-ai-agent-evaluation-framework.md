---
title: Production AI Agent Evaluation Framework
created: 2026-05-15
updated: 2026-07-31
type: concept
tags: [agent, evaluation, validation, monitoring, harness, workflow]
sources: [raw/articles/towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13.md, raw/articles/machinelearningmastery-tool-selection-ai-agents-2026-07-06.md, raw/articles/kdnuggets-llm-latency-inference-cost-2026-07-18.md, raw/articles/langchain-similarweb-long-form-agent-report-evaluation-2026-07-29.md]
status: stable
description: 定义生产级 AI Agent 的任务成功、成本、延迟、风险和回归评估框架。
aliases: [agent-evaluation-framework]
---

# Production AI Agent Evaluation Framework

## Summary
生产级 AI Agent 的可靠性不应只评估最终答案，而应同时评估检索、生成、工具行为、多步轨迹、成本和延迟。评估基础设施应在上线前建设，而不是上线后补救。

这页编译自 `[[towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13]]`，并由 `[[machinelearningmastery-tool-selection-ai-agents-2026-07-06]]`、`[[kdnuggets-llm-latency-inference-cost-2026-07-18]]` 和 `[[langchain-similarweb-long-form-agent-report-evaluation-2026-07-29]]` 补充工具选择、生产延迟/成本基线与长篇研究报告的 Rubric 校准案例；它与 `[[agent-self-validation-loops]]`、`[[agent-development-lifecycle]]`、`[[agent-orchestration-production-tradeoffs]]` 和 `[[agent-failure-closed-loop-evaluation]]` 衔接。

## Core principle

不要把 AI Agent 的生产质量压缩成一个“准确率”指标。

生产环境中的失败通常来自链路中某一层失真：检索取错上下文，生成不忠实，工具选错或参数错误，多步状态断裂，或者成本/延迟失控。评估系统应覆盖这些层，并能在上线前、软发布、稳定运行阶段持续提供反馈。

## Evaluation layers

### 1. Retrieval layer
用于评估 RAG、知识库查询、文档搜索等上下文获取质量。

检查项：
- Context Relevance：取回片段是否与用户问题相关。
- Context Recall：是否取回了回答所需的全部关键信息。
- Context Precision：最相关片段是否排在前面。
- Retrieval Latency：检索阶段是否拖慢整体响应。

工程含义：坏检索不能靠后续 prompt 补救；如果输入上下文错了，生成层只能在噪声上做推断。

### 2. Generation layer
用于评估模型最终回答是否可靠、贴题、少幻觉。

检查项：
- Answer Faithfulness：回答中的原子事实是否被上下文支持。
- Answer Relevance：回答是否真正回应了用户问题。
- Hallucination Rate：回答是否编造事实、数字、人名或不存在的依据。

工程含义：高准确率 benchmark 不代表真实流量可靠。真实用户问题会偏离评估集，必须单独看忠实度、相关性和幻觉率。

### 3. Agent behavior layer
用于评估多工具、多步骤、目标导向 Agent 的过程质量。

检查项：
- Tool Selection Accuracy：是否为当前意图选择了正确工具。
- Tool Execution Success：工具调用参数、格式、返回是否成功。
- Multi-Step Coherence：多步执行是否保持逻辑、状态和目标一致。

工程含义：Agent 不只会“答题”，还会行动。工具越多、步骤越长，错误可能断崖式增加，因此要单独评估过程轨迹，而不是只看最终输出。

#### Tool selection evaluation must separate stages

[[ai-agent-tool-selection-architecture]] 补充了工具选择评测的拆分方式。不要只记录“最后是否调用成功”，至少区分：目标工具是否进入候选集、首次选择是否正确、参数是否有效、执行是否成功，以及任务最终是否完成。对比全量工具面、静态收窄 toolset 和动态 Top-K 时，还应同时记录输入 Token 与端到端延迟，防止只优化 Prompt 长度却增加路由器成本或错召回。

### 4. Production layer
用于评估系统是否可持续运行。

检查项：
- Cost per Query：单次查询的模型、工具、基础设施总成本。
- P99 Latency：尾部延迟是否会伤害用户体验或任务完成率。

工程含义：可用的 Agent 还必须可负担、可观测、可调优。平均延迟和平均成本会隐藏长尾失败。

生产观测字段、延迟/成本诊断顺序、控制层边界和外部经验阈值由 `[[production-agent-evaluation-baselines]]` 单独维护。本页只保留 Production layer 在四层框架中的位置。

## Phased implementation

### Phase 1: Pre-launch
优先建设：
- Context Relevance
- Context Recall
- Context Precision
- Answer Faithfulness

目的：上线前先拦截最常见的检索错误和不忠实回答。

### Phase 2: Soft launch
新增：
- Hallucination Rate
- Answer Relevance
- Tool Selection Accuracy

目的：用真实流量暴露评估集覆盖不到的用户意图、幻觉类型和工具选择错误。

### Phase 3: Production stable
新增或强化：
- Cost per Query
- P99 Latency
- Queue time / TTFT / Inter-token latency
- Input/output Token、LLM calls per task、Cache-hit rate
- Tool Execution Success
- Multi-Step Coherence
- Retrieval Latency

目的：优化运行系统，而不是只判断能否上线。

## Production baselines and source thresholds

`[[production-agent-evaluation-baselines]]` 保存队列、TTFT、Token 间延迟、端到端分位数、Token/调用/缓存/工具耗时、控制层边界以及来源给出的方向性阈值。所有外部数字都只是数量级参考，必须针对本地业务、风险和成本结构重新校准。

## Rubric calibration

`[[agent-evaluation-rubric-calibration]]` 单独维护评测尺失准的诊断与校准方法：普通问答可使用 Golden Answer 语义比较，开放式长报告应使用分维度 Rubric、忠实度检查和基线 A/B；聚合分数只作诊断指针，必须回溯具体 Case、分项评语和 Trace。分数与证据冲突时，先审计评分维度、锚点和错误激励，再修改 Agent。

该方法来自 `[[langchain-similarweb-long-form-agent-report-evaluation-2026-07-29]]` 的单一实践案例，不把具体权重、评分锚点或 LangSmith 产品依赖提升为 Hermes 默认规则。

## What to preserve, what not to preserve

保留：
- 四层评估结构。
- 12 项检查项的定义。
- 阶段化建设路径。
- 队列、TTFT、Token 间、端到端分位数与 Token/调用/缓存组成的生产基线。
- 应用可控层、托管 provider 内部层与自托管 serving 层的边界。
- 经验阈值的数量级参考。
- “离线 eval 防回归，在线 eval 捕捉真实流量漂移”的闭环。

不保留为核心知识：
- 文章完整摘要。
- 具体阈值的硬编码版本。
- 未经本地验证的路由、缓存、批处理、量化或 serving 优化默认值。
- 工具评价的主观排序。
- “模型是商品，评估是差异化”这类口号。

工具线索可作为延伸阅读：Ragas、TruLens、DeepEval、LangSmith、OpenTelemetry。是否选型应另做项目级验证。

## Hermes mapping

### Wiki
本页是概念层：回答“生产 Agent 应该评估什么”。它不直接授权修改 Hermes runtime、skills、cron、MCP 或 gateway。

### Skill/reference candidate
这些来源适合作为 Hermes Agent 质量评估的 Wiki 证据，但不应直接进入 active skill。外部阈值、路由、缓存和 serving 建议尚未通过 Hermes 本地任务验证；已有专项延迟 reference 覆盖真实故障时，优先复用而不是复制本页清单。

### Local checklist candidate
如果后续要落地到 Hermes，可另建更窄的 `Hermes Agent 任务执行质量评估清单`，把通用指标改写为本地可观察项：

- 工具是否选对。
- 是否读前写。
- 是否验证后再声明完成。
- 是否保留输出路径、日志、命令或文件证据。
- 是否区分事实、推论和建议。
- 是否避免无依据结论。
- 多步任务是否保持上下文、目标和状态一致。
- 失败时是否有降级路径和停止条件。

### Relationship to existing concepts
- `[[agent-self-validation-loops]]` 关注单个任务如何通过目标、反馈、迭代完成自我验证。
- `[[agent-development-lifecycle]]` 关注 Build → Test → Deploy → Monitor 的生命周期。
- `[[agent-orchestration-production-tradeoffs]]` 关注不同 Agent 编排模式在成本、延迟、准确性和规模之间的取舍。
- `[[llm-summary-identification-step]]` 补充摘要/分析类输出在生成前应先判定 claim 是否被来源支持。
- 本页补充生产级 eval 指标层：如何观察和量化一个 Agent 系统是否可靠。

## Relationship to document fidelity risk

`[[ai-agent-document-fidelity-risk]]` adds a content-preservation failure mode to this evaluation framework: long-horizon Agent tests should not only measure final task success, but also whether source documents survive multi-step edits without silent rewrites, omissions, or hallucinated substitutions.

## Relationship to closed-loop learning

`[[agent-closed-loop-learning-from-corrections-to-rules]]` extends this evaluation framework from quality measurement into behavior promotion: user corrections should not become default Agent behavior until a candidate rule or prompt passes offline replay, shadow evaluation, or an equivalent scoped gate.

## Relationship to LLM engineering map

`[[llm-engineering-knowledge-map]]` frames evaluation as the final control layer of the LLM engineering stack. This page keeps the narrower production Agent eval checklist for retrieval, generation, tool behavior, cost, and latency.

## Relationship to research evidence gates

`[[agent-research-evidence-gate]]` applies this evaluation frame to research workflows: the Judge gate evaluates source sufficiency and missing information before an Analyst produces the final report. It is narrower than this page because it focuses on evidence readiness rather than the whole production evaluation stack.

## Related
- [[towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13]]
- [[kdnuggets-llm-latency-inference-cost-2026-07-18]]
- [[langchain-similarweb-long-form-agent-report-evaluation-2026-07-29]]
- [[agent-evaluation-rubric-calibration]]
- [[production-agent-evaluation-baselines]]
- [[agent-research-evidence-gate]]
- [[agent-self-validation-loops]]
- [[agent-closed-loop-learning-from-corrections-to-rules]]
- [[agent-development-lifecycle]]
- [[agent-orchestration-production-tradeoffs]]
- [[llm-summary-identification-step]]
- [[typed-ai-agent-boundaries]]
- [[ai-agent-document-fidelity-risk]]
- [[constrained-toolbox-evaluator-loop]]
- [[ai-agent-tool-selection-architecture]]
- [[hermes-ai-workflow-formalization-principles]]
- [[deterministic-analytics-llm-reasoning-boundary]]
- [[index]]
- [[log]]
