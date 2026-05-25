---
title: Hermes AI Workflow Formalization Principles
created: 2026-04-16
updated: 2026-05-16
type: concept
tags: [hermes, llm, workflow, decision, note]
sources: [raw/articles/dijkstra-ewd667-natural-language-programming-1978.md, raw/articles/arixzone-dijkstra-ai-programming-2026-03-31.md, raw/articles/towardsdatascience-vibe-coding-spec-driven-development-2026-05-12.md]
status: stable
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

## Practical rules for Hermes
可以直接执行的规则：
- 先用自然语言获取需求，再尽快转成结构化表示
- 重要任务必须有显式验收标准
- 重要知识必须文件化，而不是只停留在聊天里
- 默认先查 wiki，再补外部，再回写 wiki
- 复杂流程优先复用 skills，而不是重复临场发挥
- 对 AI 生成内容保持“默认需要验证”的态度

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
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
