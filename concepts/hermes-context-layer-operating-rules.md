---
title: Hermes Context Layer Operating Rules
created: 2026-04-29
updated: 2026-09-02
type: concept
tags: [hermes, lifeos, context-engineering, knowledge-base, workflow, governance]
sources: [raw/articles/machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28.md, raw/articles/machinelearningmastery-ai-agent-memory-strategy-decision-tree-2026-07-11.md, raw/papers/arxiv-2608-26263-skill-state.md, concepts/hermes-context-engineering-design-priorities.md, concepts/hermes-lifeos-executable-architecture.md, concepts/hermes-layer-routing-decision-checklist.md, concepts/hermes-memory-skills-wiki-boundaries.md, session:2026-04-29-effective-context-engineering-for-hermes]
status: stable
description: 定义 Hermes context layer 在检索、压缩、路由和执行前装配中的操作规则。
aliases: [context-layer-rules]
---

# Hermes Context Layer Operating Rules

## Summary
这页把 context engineering 文章对当前 Hermes Agent 的启发压成一套可执行分层规则。核心判断：Hermes 不应靠更长 prompt 变稳，而应靠清晰的上下文调度变稳；每条信息进入 `memory`、`skill`、`wiki`、project state、`cron/log`、subagent 或当前 session 前，都必须先按职责裁决。

Machine Learning Mastery 这篇文章提供的底层原则是：上下文窗口不是资料仓库，而是每轮推理的工作内存。Hermes 的 wiki、文件、日志和项目状态应承担外部长期资产角色；当前 session 只承担即时工作内存角色。

## Goal
让 Hermes 在长期使用中避免三类退化：
- 上下文污染：临时状态、旧结论、长摘要、过期工具输出和早期错误推理进入默认上下文
- 层间串味：wiki 写成 SOP、skill 写成百科、memory 变成 changelog
- 长任务漂移：任务推进依赖聊天历史，越聊越偏离原始目标

## Core principles
### 1. Context window is RAM, not archive
上下文窗口快、贵、有限，只放当前步骤需要的高信号内容；wiki、文件、数据库和 raw source 更像 disk，需要时再显式取回。

### 2. Static and dynamic context must be separated
系统规则、工具 schema、固定边界属于静态层；用户当前目标、最近工具结果、检索片段和当前状态属于动态层。静态层应尽量稳定，动态层应尽量小而准。

### 3. History requires compression and decay
历史不是越全越好。旧错误、过期工具输出、已解决分支和冗余检索结果会造成 context poisoning，应压成状态卡、移出当前窗口，或写回合适的长期载体。

### 4. Retrieval is a budget decision
检索命中不等于应该注入 prompt。每个候选片段都要按相关性、密度、可信度、去重后价值和 token 成本裁决。

### 5. Context quality must be testable
不能只看最终回答是否“看起来不错”。压缩、检索和状态更新后，应能用 probe 检查关键事实是否仍被保留，例如当前目标、已做决策、已处理文件、下一步。

### 6. Long-horizon execution state is a validated projection, not a rolling recap
[[arxiv-2608-26263-skill-state]] 为长程程序性任务增加了更强约束：下一步默认只消费不可变执行契约、经校验的当前状态和最新观察。模型只提议状态 patch；确定性层拥有 Schema、merge、删除、版本和回滚语义。完整历史是外部审计与恢复证据，不是每轮 Prompt 的默认运行时真相源。

启用条件：任务确实长程且状态密集、存在有界领域 Schema、patch 可确定性校验、历史轨迹不是任务输出。跳过或采用混合模式：动态 Schema、延迟相关观察、审计/解释型任务、并发写状态、无界状态或低可靠结构化输出。不得把论文中的 Token/准确率结果直接设为 Hermes 阈值。

## Layer map
### 1. Current session
职责：承载当前对话里的临时推理、探索、未验证想法和一次性中间状态。

允许进入：
- 当前任务的临时假设
- 尚未验证的方向
- 工具调用中间结果
- 一次性说明和澄清

禁止升级：
- 未稳定的偏好
- 尚未复用过的方法
- 没有长期检索价值的聊天结论

判定句：如果它只服务于这次对话，默认留在 session。

### 2. Memory
职责：短小、稳定、值得默认注入上下文的长期事实、偏好和环境约束。

允许进入：
- 用户长期偏好
- 稳定环境事实
- 已验证工具 quirk
- 未来多类任务都需要默认知道的一句话规则

禁止进入：
- 文章摘要
- 项目进度
- 临时 workaround
- 长段方法论
- 需要来源和上下文才能解释清楚的内容

判定句：如果不能压成一句稳定事实，就不要进 memory。

### 3. Skill
职责：承载可重复执行的方法；回答“以后这类事怎么做”。

允许进入：
- 多步 SOP
- 工具使用流程
- 需要触发条件、边界、坑点和验证的工作流
- 经过实际跑通后值得复用的方法

禁止进入：
- 概念解释
- 文章观点
- 个人偏好本体
- 纯调度需求

判定句：如果它是做事方法，写 skill；如果只是知识，别塞进 skill。

### 4. Wiki
职责：承载正式知识资产；回答“这是什么、为什么、和其他知识如何关联”。

允许进入：
- 架构原则
- 概念页
- 领域模型
- 外部文章编译后的长期结论
- 比较分析
- 可复盘样板案例

禁止进入：
- 原样聊天记录
- 未整理 raw dump
- 临时任务状态
- SOP 本体
- secrets

判定句：如果需要标题、小节、来源、链接和未来扩写，优先进入 wiki。

### 5. Project state
职责：承载一个长期任务的当前状态，避免依赖聊天历史推进。

适用任务：
- Hermes LifeOS 架构推进
- wiki 整合
- skill 审计或重构
- 小项目 workflow 验证
- 家庭教育路径比较
- Gemini wrapper / quick command 优化

建议结构：
- 当前目标
- 不可变契约 / Skill / Spec 版本
- 已确认决策
- 已验证事实及证据指针
- 未决问题
- 已完成步骤
- 下一步
- 风险与约束
- 状态版本、最近 patch 与回滚点
- 相关文件 / skill / wiki 页面

判定句：如果它是“这个项目现在推进到哪了”，写 project state，不写 memory。

### 6. Cron and logs
职责：`cron` 负责在 fresh session 中定时运行已经稳定的方法；logs 负责记录可审计结果。

允许进入 cron：
- 已经有稳定 skill 或自包含 prompt 的周期任务
- 输入输出明确、失败可观察的任务

禁止进入 cron：
- 还没跑顺的方法
- 依赖当前聊天隐含上下文的任务
- 需要人工频繁改 prompt 的流程

判定句：cron 只回答“什么时候跑”，不回答“怎么做”。

### 7. Subagent
职责：为复杂任务隔离上下文，避免主对话背负全部细节。

适用任务：
- 代码审查
- 多来源资料收集
- skill overlap 审计
- 独立验证步骤
- 长文档抽取
- 多方案比较

主 agent 保留：
- 总目标
- 约束
- 决策权
- 验证责任

subagent 返回：
- 结论
- 证据
- 文件路径 / URL / 命令结果
- 风险和未决点

判定句：如果子任务可以独立完成并只需要返回结论，就用 subagent 隔离。

生命周期复杂度规则见 `[[subagent-orchestration-patterns]]`：默认把 subagent 当作一次性 inline tool；只有在任务真正独立且并发有收益时才 fan-out；agent pool 和 team 模式需要项目级验证、清理机制和可观测性后再考虑。

## Memory-strategy pre-routing gate

[[machinelearningmastery-ai-agent-memory-strategy-decision-tree-2026-07-11]] 补充了进入具体 Hermes 层之前的语义判断：先分清信息是当前状态、稳定事实、历史事件还是可复用规程，再选择存储层。完整映射由 `[[hermes-memory-skills-wiki-boundaries]]` 维护；本页只保留 context 装配相关约束：

- session 是当前工作内存，不是档案；
- 历史事件只有在当前步骤相关时才检索进入 context，不默认注入；
- 稳定事实应优先读取当前有效版本，旧版本仅在查询历史时暴露；
- 检索规模由 context budget 约束，大历史库不能因为“命中”就全量注入；
- 规程只有经过验证后才作为 skill/reference 按需加载。

## One-screen routing checklist
遇到新信息、新方法或新需求时，按顺序问：

1. 只是当前任务临时需要吗？是 → session
2. 是项目推进状态吗？是 → project state
3. 是短小稳定事实或偏好吗？是 → memory
4. 是可复用操作流程吗？是 → skill
5. 是正式知识资产吗？是 → wiki
6. 是稳定方法的定时执行吗？是 → skill + cron
7. 是外部实时能力接入吗？是 → MCP
8. 是可并行或应隔离的复杂子任务吗？是 → subagent

如果多个层都适合，按职责拆分，不要复制粘贴到多个层。

## Promotion rules
### Session -> memory
只有当信息短小、稳定、跨任务长期有效，并且默认注入有收益时才升级。

### Session -> wiki
只有当内容已经被整理成正式知识，有来源、结构、链接和长期复用价值时才升级。

### Session -> skill
只有当同类任务未来会重复执行，并且步骤、坑点、验证条件已经跑通时才升级。对于用户纠错类反馈，先参考 [[agent-closed-loop-learning-from-corrections-to-rules]]：单次纠正不能直接变成全局 skill 规则，必须先证明它是可复现、可泛化、可验证的模式。

### Project state -> wiki
项目结束或阶段收敛后，把可复用结论编译成 wiki；不要把整个过程日志原样搬进 wiki。

### Skill -> cron
方法先稳定，调度后发生；不要用 cron prompt 代替 skill。

## Drift signals
出现这些信号时，说明上下文治理需要介入：
- Hermes 重复询问已经稳定的偏好
- memory 里出现任务进度或一次性结论
- skill 变成长篇概念说明
- wiki 页面像聊天记录或 SOP 手册
- 长任务靠翻聊天历史才能继续
- subagent 返回大量过程而非结论和证据
- cron 任务依赖当前线程上下文
- Hermes 重复读取已处理文件或重述旧决策

## Repair actions
- 重复偏好 → 压成一句 memory
- 重复方法 → 写 skill
- 长期知识 → 写 wiki
- 项目进度 → 写 project state
- 定时执行 → skill 稳定后加 cron
- 外部实时能力 → MCP
- 上下文过载 → 总结状态后开 fresh session
- 复杂任务串味 → 拆 subagent

## Operating policy for current Hermes
当前阶段采用保守策略：
- 默认不增加 profile；继续用 default profile 作为主脑
- Telegram 仍是唯一主要入口
- wiki 是长期知识层，memory 只存高密度长期事实
- 新 workflow 先小项目验证，跑通后再决定是否 skill 化或 cron 化
- Hermes 本体源码修改保持谨慎；若 update 会覆盖，优先记录限制并考虑上游 issue/PR

## Source integration note
Machine Learning Mastery 文章的处理结果：
- 原文和 Gemini 摘要保存在 `[[machinelearningmastery-effective-context-engineering-ai-agents-2026-04-28]]`，作为可追溯 raw source。
- 可复用原则已整合进本页 Summary、Goal 和 Core principles，不再作为独立文章摘要重复出现。
- “memory 只放短小稳定事实”的偏好由本页和现有 memory 规则承接，无需重复写入 memory。
- 若未来多次需要执行上下文审计，再提炼为专门 skill；当前不提前创建。

## Relations
- depends_on: [[hermes-context-engineering-design-priorities]]
- depends_on: [[hermes-lifeos-executable-architecture]]
- depends_on: [[hermes-layer-routing-decision-checklist]]
- depends_on: [[hermes-memory-skills-wiki-boundaries]]

## Related
- [[machinelearningmastery-ai-agent-memory-strategy-decision-tree-2026-07-11]]
- [[agent-context-engineering]]
- [[hermes-context-engineering-design-priorities]]
- [[llm-context-engineering-layer]]
- [[hermes-lifeos-executable-architecture]]
- [[ai-assumption-challenger-before-execution]]
- [[hermes-layer-routing-decision-checklist]]
- [[subagent-orchestration-patterns]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-knowledge-architecture]]
- [[index]]
- [[log]]
