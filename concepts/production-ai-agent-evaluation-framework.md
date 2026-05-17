---
title: Production AI Agent Evaluation Framework
created: 2026-05-15
updated: 2026-05-17
type: concept
tags: [agent, evaluation, validation, monitoring, harness, workflow]
sources: [raw/articles/towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13.md]
status: stable
---

# Production AI Agent Evaluation Framework

## Summary
生产级 AI Agent 的可靠性不应只评估最终答案，而应同时评估检索、生成、工具行为、多步轨迹、成本和延迟。评估基础设施应在上线前建设，而不是上线后补救。

这页编译自 `[[towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13]]`，并与 `[[agent-self-validation-loops]]`、`[[agent-development-lifecycle]]` 和 `[[agent-orchestration-production-tradeoffs]]` 衔接。

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

### 4. Production layer
用于评估系统是否可持续运行。

检查项：
- Cost per Query：单次查询的模型、工具、基础设施总成本。
- P99 Latency：尾部延迟是否会伤害用户体验或任务完成率。

工程含义：可用的 Agent 还必须可负担、可观测、可调优。平均延迟和平均成本会隐藏长尾失败。

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
- Tool Execution Success
- Multi-Step Coherence
- Retrieval Latency

目的：优化运行系统，而不是只判断能否上线。

## Directional benchmarks from the source

以下阈值只作为“数量级参考”，不要当成强制标准。不同业务、风险等级、成本结构和用户体验目标都可能需要重新校准。

- Context Relevance：作者建议目标约 `>0.85`，低于 `0.70` 需要调查。
- Context Recall：作者建议 benchmark queries 约 `>0.90`。
- Context Precision / MRR：作者建议约 `>0.80`。
- Retrieval Latency：作者建议 p95 小于约 `200ms`，p99 小于约 `500ms`。
- Answer Faithfulness：监管行业约 `>0.95`，一般场景约 `>0.90`。
- Hallucination Rate：生产 Agent 约 `<2%`，监管行业约 `<0.5%`。
- Tool Selection Accuracy：二选一工具约 `>0.92`，5+ 工具场景约 `>0.85`。
- Tool Execution Success：作者建议约 `>0.98`。
- P99 Latency：对话型 Agent 约 `<3s`，分析型 Agent 可放宽到约 `<10s`。
- LLM-as-judge 成本：作者经验约为推理成本的 `30%–50%`。

## Source-backed cautionary claims

这些数字也应视为作者团队经验，而不是普适定律：

- MVP 后补评估通常要 4–6 周，期间信任损害可能已经发生。
- 测试集 95% accuracy 的 RAG Agent，真实用户问题仍可能高幻觉。
- 工具从 3 个增至 12 个时，工具选择准确率可能显著下降。
- 多步 trace 从 2 步扩展到 6 步时，多步连贯性可能大幅下降。
- 用同一模型同时做生成和裁判，可能导致评估分数虚高。

## What to preserve, what not to preserve

保留：
- 四层评估结构。
- 12 项检查项的定义。
- 阶段化建设路径。
- 经验阈值的数量级参考。
- “离线 eval 防回归，在线 eval 捕捉真实流量漂移”的闭环。

不保留为核心知识：
- 文章完整摘要。
- 具体阈值的硬编码版本。
- 工具评价的主观排序。
- “模型是商品，评估是差异化”这类口号。

工具线索可作为延伸阅读：Ragas、TruLens、DeepEval、LangSmith、OpenTelemetry。是否选型应另做项目级验证。

## Hermes mapping

### Wiki
本页是概念层：回答“生产 Agent 应该评估什么”。它不直接授权修改 Hermes runtime、skills、cron、MCP 或 gateway。

### Skill/reference candidate
这篇文章适合作为 Hermes Agent 质量评估 reference 的候选材料，但不应直接进入 active skill。原因是外部阈值和工具评价尚未通过 Hermes 本地任务验证。

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

## Relationship to LLM engineering map

`[[llm-engineering-knowledge-map]]` frames evaluation as the final control layer of the LLM engineering stack. This page keeps the narrower production Agent eval checklist for retrieval, generation, tool behavior, cost, and latency.

## Related
- [[towardsdatascience-production-ai-agent-evaluation-harness-2026-05-13]]
- [[agent-self-validation-loops]]
- [[agent-development-lifecycle]]
- [[agent-orchestration-production-tradeoffs]]
- [[llm-summary-identification-step]]
- [[typed-ai-agent-boundaries]]
- [[hermes-ai-workflow-formalization-principles]]
- [[index]]
- [[log]]
