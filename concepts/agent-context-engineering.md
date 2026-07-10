---
title: Agent Context Engineering
created: 2026-05-20
updated: 2026-07-11
type: concept
tags: [agent, llm, context-engineering, hermes, workflow]
sources: [raw/articles/machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19.md, raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md, raw/articles/machinelearningmastery-context-vs-memory-engineering-agentic-ai-systems-2026-07-03.md, raw/articles/machinelearningmastery-tool-selection-ai-agents-2026-07-06.md, raw/articles/microsoft-developer-ai-coding-agents-use-technology-2026-05-27.md, raw/articles/thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26.md, concepts/llm-context-engineering-layer.md, concepts/hermes-context-engineering-design-priorities.md]
status: stable
description: 定义 Agent 执行过程中的上下文装配原则，用于控制工具、示例、状态和历史可见性。
aliases: [agent-context-engineering, context-engineering-for-agents]
---

# Agent Context Engineering

## Summary

可靠 Agent 的核心是“上下文工程”而非“修辞学”：通过即时装配（Just-in-time）系统指令、明确工具边界、精选 Few-shot 示例并动态裁剪消息历史，严格控制模型每一步的可见信息，从而避免上下文腐败（Context Rot）与多步执行偏航。

这页沉淀 MachineLearningMastery 文章 [[machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19]] 对 Hermes 的可迁移原则。它补充 `[[llm-context-engineering-layer]]` 与 `[[hermes-context-engineering-design-priorities]]`：前者讲 RAG 与 prompt 之间的上下文层，后者讲 Hermes 的预算、排序、压缩优先级；本页聚焦 Agent 执行过程中的上下文装配：system prompt、tools、examples、message history/state 在每一步如何被选择、裁剪和隔离。

## Core principle

Agent prompt engineering 不是把一次性聊天 prompt 写得更漂亮，而是设计一个会反复运行的上下文装配系统。

聊天 prompt 的失败通常会马上暴露，用户下一轮可以纠正；Agent 的失败会在多步任务中延迟显现：早期歧义、过宽工具、错误历史、冗余检索和过期状态会被后续步骤当成事实继续使用，最后表现为工具选择漂移、目标偏航、重复操作或看似合理但不可信的交付物。

因此 Agent 的默认问题应从“我该怎么措辞”改成：

> 模型在当前步骤需要看到哪些最小、最高密度、最可信的信息，才能做对下一步？

## Four context surfaces

### 1. System prompt: operating brief, not exhaustive script

System prompt 应定义角色、权限边界、工具使用原则、停止条件和输出契约，但不应试图用 if-else 穷举所有场景。

过度指定会让提示词脆弱、难维护，并压低模型处理新情况的能力；指定不足会让 Agent 用隐含假设补空白。更好的做法是保持“恰当高度”：少量高优先级原则 + 清晰验收标准 + 明确越界停止条件。

Hermes 映射：
- `SOUL.md`、`CLAUDE.md`、`AGENTS.md` 提供全局/项目级行为边界。
- skill 的 `Trigger`、`Workflow`、`Pitfalls`、`Verification` 提供任务级操作边界。
- 不应把某篇文章的 prompt 模板直接硬编码进全局提示词。

### 2. Tools: narrow action surface with negative boundaries

Agent 能调用工具不等于应该暴露更多工具。工具越宽、越相似、越缺少失败语义，模型越容易在多步执行中选错工具。

本页只保留上下文装配层的原则：工具描述应让模型知道“何时使用、何时不用、失败后怎么办、成本/风险是什么”。工具类型、schema、dependency injection 与 public API 边界详见 `[[typed-ai-agent-boundaries]]`，不要在本页重复维护。

Hermes 映射：
- 工具说明应包含用途、限制、失败语义和反向边界。
- 高风险工具不应靠 prompt 自觉控制，应配合权限、审批、审计和回滚。
- 给一个 Agent 挂载工具前，先问：当前任务真的需要它进入可见工具面吗？

#### AX 级联补充：可见不等于可用

Microsoft Developer 的 AX 文章补充了一个容易误判的点：工具安装或注册成功，只说明它可能进入 harness 的候选面，不说明模型一定能看到、理解、选择并正确使用它。工具可用性至少经过一条级联链：

1. harness 是否把工具描述装进上下文；
2. 模型是否把用户意图语义匹配到该工具；
3. 模型是否愿意调用工具，而不是用过时训练知识高置信猜测；
4. 工具 schema、参数和返回内容是否足够短、清楚、可执行；
5. 生成后，CLI/LSP/test 错误是否能让 agent 自修复。

Hermes 映射：评估 skill/tool/MCP 不应只看“是否被暴露”或“是否被调用”，还要看在真实组合上下文里是否被正确选择、低噪声返回、失败后可诊断。这条规则补充 `[[typed-ai-agent-boundaries]]` 的工具接口原则和 `[[ai-coding-assistant-context-budget-management]]` 的上下文预算原则。

#### 工具可用性与逐轮候选集分离

[[ai-agent-tool-selection-architecture]] 进一步区分“系统允许使用哪些工具”和“当前推理步骤应让模型看到哪些工具”。Hermes toolset 已能提供平台、会话和任务级静态边界；动态 Top-K、语义路由或规划式选择只有在真实会话基线证明静态收窄仍不足时，才值得进入项目级试验。外部文章中的工具数量和阈值不应直接变成 active runtime 默认值。

### 3. Examples: demonstrate behavior, not only answers

Agent 的 Few-shot 示例不应只展示“输入 → 正确输出”。对多步任务，更有价值的是展示行为模式：如何澄清范围、何时暂停、如何处理工具失败、如何验证结果、如何在证据不足时降级回答。

Hermes 映射：
- skills 的 references、fixtures、validation records 可以承载局部 Few-shot。
- 示例应按任务即时加载，而不是塞进全局上下文。
- 至少为复杂工作流保留一个“识别歧义 → 停止执行 → 请求澄清”的样例。

### 4. Message history and state: dynamic, lossy, and task-scoped

历史消息不是越全越好。长历史会引入旧目标、旧错误、重复工具输出和无关上下文，让模型注意力被稀释。

Agent 运行状态应从“完整聊天记录”转成结构化状态：当前目标、已做决策、已验证事实、待办步骤、失败尝试、风险和停止条件。旧过程可以进入日志或 wiki raw source，但不应默认继续压进 prompt。

Hermes 映射：
- session context 保存当前对话的活跃意图。
- memory 只保存短小、稳定、跨任务默认有价值的事实。
- wiki 保存长期概念、raw source 和可检索知识。
- project logs / run artifacts 保存可审计过程证据。
- cron/log 保存 recurring 运行结果，不等于默认上下文。

这只是 Agent 运行状态视角下的简要映射；Hermes 全局层间路由规则以 `[[hermes-context-layer-operating-rules]]` 为准。

## Context rot and JIT defense

Context rot 不是单纯 token 不够，而是上下文质量随长度和噪音下降：旧错误被保留、重复输出占位、无关材料挤掉关键事实、模型在“看起来相关”的历史中迷路。

Hermes 的防腐原则：

1. **Just-in-time over pre-loaded**
   - 需要时再读取 wiki、文件、日志或 tool result。
   - 不把所有可能有用的资料预先塞进 prompt。

2. **State card over raw transcript**
   - 对长任务保留结构化状态卡，而不是完整消息历史。
   - 状态卡必须区分已验证事实、推论、待验证问题和下一步。

3. **Minimal shared context for subagents**
   - 子 Agent 只接收自己的任务、输入、边界和输出契约。
   - 不把主 Agent 的全部历史转交给子 Agent。
   - 这与 `[[subagent-orchestration-patterns]]` 的“从最简单编排开始”原则一致。

4. **Context choice should be explainable**
   - 对复杂任务，应能回答为什么选了某段上下文、为什么丢弃某段上下文。
   - 这与 `[[hermes-context-engineering-design-priorities]]` 的 budget、ranking、compression 顺序一致。

## Context vs. memory engineering boundary

Machine Learning Mastery 的 `Context vs. Memory Engineering in Agentic AI Systems` 把本页的一个隐含规则说得更清楚：**memory 决定可取信息集合，context assembly 决定本轮模型真正看到什么、放在哪里、占多少预算**。

Hermes 映射（参见 `[[hermes-memory-skills-wiki-boundaries]]`）：
- `memory` 只保存短小、稳定、跨任务默认有价值的事实；它不是文章、工作流、项目状态或历史日志的默认仓库。
- `wiki` 保存来源可追溯的概念和 raw source；适合承载本文这类外部架构原则。
- `skills` 保存可重复执行的方法、触发/跳过条件、pitfalls 和验证方式；文章启发只有在真实 Hermes 任务中证明可复用后，才考虑进入 skill reference。
- 当前任务状态、工具输出和 session 历史应先被压缩成结构化状态卡，再决定是否进入下一轮上下文。

这篇文章补充了两个可操作原则：
1. **预算先于检索**：检索条数不应只由 Top-K 或相似度阈值决定，而应先由上下文装配器计算当前步骤的 token 预算。
2. **位置是上下文质量的一部分**：关键指令靠前；当前任务、高相关检索结果和需要马上使用的状态靠近生成位置；不要把重要信息随机拼接到长上下文中间。

不应把这篇文章直接升级为 active Hermes 行为。它的合理落点是 wiki 概念和后续 `skill-optimization-workflows` / `hermes-knowledge-and-workflow-governance` 的参考材料；是否改 active skill、runtime 或 classifier，仍需要单独的项目级验证、审批和回滚证据。

## Provenance debt in generated code

The New Stack 对 Codeplain 的报道给这页补充了一个上下文工程视角：AI 生成代码被手工连续补丁后，容易产生 **provenance debt（出处债务）**。问题不只是代码变复杂，而是代码与它背后的需求、约束、spec、prompt、推理记录和验收证据之间的来源关系断开；后续 agent 再看到这段代码时，只能从实现反推意图，容易把临时修补当成设计事实。

Hermes 的对应规则：
- 对 AI 生成或 agent 修改的代码，优先保留“为什么改”的来源：spec、acceptance criteria、ADR、project doc、测试或审查记录。
- 行为逻辑变更应先回写 spec / contract，再派生代码修改；不要让代码 diff 成为唯一事实源。
- 当只剩实现代码而没有来源上下文时，后续 agent 应把意图判断标为推论，并用测试、文档或用户确认补齐事实源。
- 不把外部文章中的全量 regenerate-code 主张直接推广为 Hermes 默认。出处债务用于提醒上下文保真，不等于允许 agent 无边界重写实现。

## Relationship to existing wiki

- `[[llm-context-engineering-layer]]`：讲 context engineering 作为 RAG 与 prompt 之间的系统层；本页讲 Agent 多步执行中各类上下文面的即时装配。
- `[[hermes-context-engineering-design-priorities]]`：讲 Hermes 应先做 budget、ranking、compression、history decay；本页补充为什么这些能力对 Agent prompt/context 稳定性必要。
- `[[hermes-context-layer-operating-rules]]`：定义 Hermes 全局层间路由规则；本页聚焦 Agent 执行过程中 prompt 四个上下文面的即时装配设计，而非通用层路由决策。
- `[[typed-ai-agent-boundaries]]`：讲 typed output、typed tools、dependency injection；本页只引用工具边界原则，不重复展开实现细节。
- `[[ai-coding-assistant-context-budget-management]]`：讲工具输出、日志、文件和历史如何占用上下文预算；本页补充工具是否能被发现和正确选择的 upstream 级联。
- `[[agent-development-lifecycle]]`：把 context、tool、prompt、monitor 放进 Build/Test/Deploy/Monitor/Govern 生命周期；本页提供 Build/Test 阶段的上下文装配原则。
- `[[subagent-orchestration-patterns]]`：讲 subagent 生命周期选择；本页补充子 Agent 应接收最小共享上下文，避免跨任务污染。
- `[[codex-agent-workflow-layering]]`：讲 prompt、AGENTS、skill、MCP、automation 以及 spec/generation layer 的职责分离；本页补充 provenance debt 如何导致 agent 上下文保真下降。
- `[[machinelearningmastery-context-vs-memory-engineering-agentic-ai-systems-2026-07-03]]`：补充 memory engineering 与 context engineering 的时间维度边界，强化“候选记忆库 ≠ 当前 prompt 输入”的原则。
- `[[hermes-memory-skills-wiki-boundaries]]`：定义长期能力归类边界；本页引用其对 memory/skills/wiki 的分类规则以防止概念漂移。

## What not to promote blindly

- 不把 CoT、ReAct、Reflexion 固化为 Hermes 默认执行模式；它们是可选推理架构，不是每个任务的最低成本路径。
- 不因为强调 context engineering 就扩大默认上下文窗口或默认注入更多历史。
- 不因为强调 memory engineering 就扩大长期 memory 写入范围；外部文章中的方法论优先进入 wiki 或 skill reference 候选，而不是用户/环境 memory。
- 不把文章中的经验值、示例 prompt 或 Few-shot 直接写入 `SOUL.md`、`AGENTS.md` 或全局 skill。
- 不把本页直接升级为 skill；只有当某个具体 Hermes 工作流在真实项目中验证出稳定 SOP，才考虑新增或补丁相关 skill。
- 不把工具边界内容复制成第二套规则；工具接口治理以 `[[typed-ai-agent-boundaries]]` 为主。

## Operating rules

- 对 Agent 任务，先定义当前步骤需要的最小上下文，再读取材料。
- 对长任务，维护结构化状态卡，定期裁剪原始历史。
- 对工具集，优先减少可见工具面，再优化工具描述。
- 对 Few-shot，优先展示澄清、失败处理和验证行为，而不是只展示成功输出。
- 对 subagent，传递任务契约和必要证据，不传递完整父上下文。
- 对任何 active-layer 变更，先走项目级验证和显式审批，不从外部文章直接推广。

## Relations
- depends_on: [[llm-context-engineering-layer]]
- depends_on: [[hermes-context-engineering-design-priorities]]

## Related

- [[machinelearningmastery-prompt-engineering-agentic-ai-2026-05-19]]
- [[machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28]]
- [[machinelearningmastery-context-vs-memory-engineering-agentic-ai-systems-2026-07-03]]
- [[machinelearningmastery-tool-selection-ai-agents-2026-07-06]]
- [[ai-agent-tool-selection-architecture]]
- [[microsoft-developer-ai-coding-agents-use-technology-2026-05-27]]
- [[thenewstack-codeplain-spec-driven-regenerative-code-2026-06-26]]
- [[llm-context-engineering-layer]]
- [[hermes-context-engineering-design-priorities]]
- [[typed-ai-agent-boundaries]]
- [[agent-development-lifecycle]]
- [[subagent-orchestration-patterns]]
- [[codex-agent-workflow-layering]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-context-layer-operating-rules]]
- [[ai-assumption-challenger-before-execution]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
