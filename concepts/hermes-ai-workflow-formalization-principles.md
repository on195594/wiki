---
title: Hermes AI Workflow Formalization Principles
created: 2026-04-16
updated: 2026-05-31
type: concept
tags: [hermes, llm, workflow, decision, note, skills, governance]
sources: [raw/articles/dijkstra-ewd667-natural-language-programming-1978.md, raw/articles/arixzone-dijkstra-ai-programming-2026-03-31.md, raw/articles/towardsdatascience-vibe-coding-spec-driven-development-2026-05-12.md, raw/articles/addyosmani-agent-skills-2026-05-03.md, raw/articles/langchain-interpreter-skills-2026-05-30.md]
status: stable
description: 把形式化思想转译为 Hermes AI 工作流中的规格、边界、验证和可回滚原则。
---

# Hermes AI Workflow Formalization Principles

## Summary
基于 EWD667 与 2026 AI 编程文章的双来源对照，Hermes 的工作流应明确采用“自然语言输入 + 形式化约束 + 验证闭环”的路线。
Hermes 不应把对话本身当作最终控制面，而应不断把模糊意图压缩为 spec、检查清单、测试、结构化知识和可执行约束。

## Principle 1: language is for intent, not for final control
自然语言适合表达目标、背景、偏好和方向。
但在 Hermes 工作流里，真正决定质量的不是“说了什么”，而是最后有没有被收敛成可验证结构。

实践含义：
- 用户消息是起点，不是终点
- 长任务要转成 todo、wiki 页面、skills、配置项或明确检查项

## Principle 2: prefer narrow interfaces
接口越宽，歧义越多，返工越多。
在 Hermes 里，窄接口意味着：
- 明确的任务边界
- 简短而稳定的工具调用输入
- 可复查的文件化产物
- 明确的验收标准

实践含义：
- 能落文件就别只停留在对话里
- 能拆成小页面、小技能、小检查项就不要做成大杂烩

## Principle 2.5: durable projects need a spec source of truth
`[[towardsdatascience-vibe-coding-spec-driven-development-2026-05-12]]` 对 Hermes 的补充是：当工作跨多轮会话、多 agent 或多人协作时，聊天历史不能承担 source of truth。真正稳定的控制面应该是项目内 docs/spec 文件、计划、验收标准和验证记录。

实践含义：
- durable agent/project work should use docs/spec files as the source of truth, not chat history
- 需求或实现过程中发现约束变化时，先更新 spec，再调整实现和测试
- 临时聊天指令不能成为唯一决策记录
- 具体 spec 目录形态参考 `writing-plans` skill 的 “Spec-driven development for agentic projects”，不要在 wiki concept 里重复维护文件清单

## Principle 3: formal artifacts are the real memory of work
真正可靠的长期资产不是聊天记录，而是形式化产物：
- `wiki` 页面
- `skills`
- 配置文件
- 测试
- 检查清单
- 结构化日志

实践含义：
- 复杂结论进 wiki
- 可复用方法进 skills
- 偏好与稳定事实进 memory
- 临时过程只留在 sessions

## Principle 4: verification is mandatory
AI 输出的最大风险不是不会说，而是会在模糊处自动补全。
所以 Hermes 必须强调验证。

实践含义：
- 写完文件后要读回验证
- 改完配置后要跑 check 或 smoke test
- 建完知识页后要更新 index 和 log
- 长流程要有显式 completion criteria

## Principle 5: use AI to reduce the cost of formalization
AI 最有价值的地方不是取代结构，而是更快地生成结构。

实践含义：
- 用 AI 草拟 spec、总结要点、生成测试框架、补充分类与交叉链接
- 但最后仍由人或规则层负责验收与裁决

## Principle 6: context should be compressed, not endlessly widened
长上下文会污染后续输出。
Hermes 的更优路径不是无限追加聊天，而是持续压缩。

实践含义：
- 复杂对话结论写回 wiki
- 重复流程沉淀为 skills
- 多步骤任务写入 todo
- 历史事项用 session_search 回忆，而不是把整段旧上下文塞回来

## Principle 7: skills should be executable workflows, not explanatory prose
Addy Osmani 的 `Agent Skills` 文章对 Hermes 的补充是：面向 AI coding agent 的长期规则不能只写成“最佳实践说明书”。如果规则希望约束 agent 行为，它必须变成可触发、可执行、可验证、有退出条件的 workflow。

实践含义：
- `skills` 主路径应优先写触发条件、步骤、检查点、证据和退出条件，而不是堆叠背景理念。
- 说明性原则可以进入 wiki/concept；重复执行流程才适合进入 skill。
- 原文的 `/spec`、`/plan`、`/build`、`/test`、`/review`、`/ship`、`/code-simplify` 是 Osmani 项目的 SDLC 命令设计，只能作为生命周期类比，不应直接沉淀为 Hermes 命令方案。
- GitHub stars、安装命令、具体 skill 数量属于来源背景，不是 Hermes 质量标准。

### Anti-rationalization tables as agent shortcut interceptors
`Anti-rationalization tables` 的价值不是口号，而是 agent 行为拦截器：先列出 agent 或疲劳工程师可能用来跳过流程的借口，再写出预设反驳和停止条件。

Hermes skill 自查时应单独问：
- 这个 skill 是否写明了常见偷懒路径？
- 当 agent 说“太简单不用 spec / 测试之后补 / 手动验证够了 / 顺手重构一下”时，skill 是否有明确阻断规则？
- 这些阻断规则是否连接到可验证证据，而不是只停留在价值判断？

### Read-only check against current Hermes skills
本次只读抽查 3 个现有 skill，作为概念页有效性的最小本地验证；这不是 active skill 修改授权。

- `test-driven-development`：强匹配。已有 `When to Use / When Not to Use`、RED/GREEN/REFACTOR workflow、验证清单、completion report，并包含 `Common Rationalizations` 表，能直接拦截“测试之后补”“太简单不用测”等借口。
- `gsummary`：基本匹配。它是 thin entrypoint，已有触发条件、payload capture workflow、pending-payload verification 和 compaction regression pitfalls；但它的反合理化机制主要写在 pitfalls 中，不是显式表格。当前无需修改 active skill，除非后续复盘证明 agent 仍会把入口任务扩张成治理/开发任务。
- `gemini-summary`：基本匹配。它有明确 backend workflow、cache/source/gate/`全文路径` contract 和 failure fallback；反偷懒规则以 non-negotiable gates / pitfalls 呈现，适合 backend skill。当前无需因为外部文章直接改动。

### Promotion boundary
本原则只在以下情况才考虑升级为 active skill/reference 修改依据：
- 复盘发现某个 skill 因缺少检查点、退出条件或反合理化规则，导致 agent 实际走了捷径；
- 新建或重构 skill 时，需要质量自查清单；
- 独立审查指出某个 skill 已退化为说明性散文，缺少可执行证据链。

未满足这些条件时，本页只作为 wiki 概念与评审标准，不自动触发 memory、skill、cron、MCP、runtime、wrapper 或 Hermes core 变更。

## Principle 8: let the model route, let deterministic code execute
LangChain 的 `[[langchain-interpreter-skills-2026-05-30]]` 对本页的增量价值不是提出“再加一个 skill 形态”，而是给 Hermes 已有实践命名：**外层由模型判断是否适用、如何传参；内层由可审查代码执行确定性流程并返回可验证结构**。

这与 Hermes 当前的 `gsummary` → `gemini-summary` → wrapper/scripts/validators 模式相近，但 LangChain 的形式更明确：`SKILL.md` 描述何时使用，TypeScript module 承载可执行 API。对 Hermes 的可迁移原则是声明层和执行层分离，而不是照搬 TypeScript interpreter。

### Candidate status
- concept: “模型路由 + 确定性执行”适合保留在 wiki，作为 agent workflow 设计概念。
- rule candidate: 当某个 Hermes 子流程高频、可复用、容易跑偏，且已经有 schema / fixture / validator / rollback 证据时，才考虑把该原则提炼进对应 skill/reference。
- active proposal: 当前没有。本文不授权修改 Hermes runtime、cron、MCP、gateway、wrapper、active skill 或 core。

### Design checks before promotion
- 这个流程是否已经重复出现，而不是一次文章启发？
- 模型负责的是路由/参数选择，还是被迫在上下文里手动维护大量状态？
- 确定性代码是否有输入 schema、输出 shape、错误路径和回滚/重试边界？
- 现有 Hermes skill/script 是否已经覆盖该实践，只需要命名或链接，而不是新增规则？
- 如果沉淀进 wiki 后长期不用，是否应标记为 stale 或归档，而不是继续充当 active 依据？

### What not to promote
- 不把 LangChain 的 TypeScript interpreter 当作 Hermes 当前实现目标。
- 不把 `SKILL.md + module` 直接等价为 Hermes active skill 规范。
- 不因本文直接增加工具面、子代理权限、MCP、cron 或 runtime capability。
- 不把“确定性执行”理解为跳过模型判断；外层路由错误仍会让内部确定性流程失效。

## Practical rules for Hermes
可以直接执行的规则：
- 先用自然语言获取需求，再尽快转成结构化表示
- 重要任务必须有显式验收标准
- 重要知识必须文件化，而不是只停留在聊天里
- 默认先查 wiki，再补外部，再回写 wiki
- 复杂流程优先复用 skills，而不是重复临场发挥
- 对 AI 生成内容保持“默认需要验证”的态度
- 写新 skill 或重构旧 skill 时，检查它是否是可执行 workflow，而不是说明性散文
- 对高风险/高频偷懒路径，优先写反合理化规则和停止条件

## Concrete mapping inside Hermes
把原则映射到 Hermes 内部：
- `memory`：保存稳定事实与偏好
- `skills`：保存可复用方法
- `wiki`：保存正式知识
- `todo`：保存进行中的结构化任务
- `session_search`：提供历史回忆，不替代知识层
- `tools`：执行动作并提供外部验证能力

## Takeaway
如果用一句话概括 Hermes 的实践原则：
不要让 AI 直接统治模糊上下文；要让 AI 帮你更快地产出、维护和验证形式化结构。

## Related
- [[dijkstra-ai-programming-formalization]]
- [[dijkstra-ewd667-vs-ai-programming-article]]
- [[towardsdatascience-vibe-coding-spec-driven-development-2026-05-12]]
- [[llm-summary-identification-step]]
- [[hermes-knowledge-architecture]]
- [[hermes-knowledge-base-operating-flow]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[deterministic-analytics-llm-reasoning-boundary]]
- [[langchain-interpreter-skills-2026-05-30]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
