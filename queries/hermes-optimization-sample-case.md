---
title: How We Optimized Hermes in April 2026 (Sample Case)
created: 2026-04-16
updated: 2026-04-16
type: query
tags: [hermes, workflow, configuration, debugging]
sources: [raw/transcripts/hermes-optimization-sample-case-2026-04.md]
status: stable
---

# How We Optimized Hermes in April 2026 (Sample Case)

## Summary
这是一个按 `[[hermes-knowledge-base-operating-flow]]` 重跑后的样板案例。
它展示了最近优化 Hermes 的过程如何从零散对话，收敛为 quick command 修复、cron 修复、wiki 基础设施、规范页面和 skill 这些可复用资产。

## Question
最近优化 Hermes 的过程，如何按当前知识库操作流重新整理成一个可复用样板？

## Step 1: intake
输入不是一个单独问题，而是一串连续优化需求：
- 晨报脚本和 quick command 不稳定
- 定时任务执行了但没发到 Telegram
- Hermes 需要长期知识库
- 知识库需要规则、lint 和维护方式
- 反复出现的工作流需要提升为 skill

如果只把这些留在聊天里，会迅速漂移。

## Step 2: classify
按 `hermes-formalized-ai-workflow` skill 与 `[[hermes-memory-skills-wiki-boundaries]]` 的规则，实际被分流到多层：
- quick command / cron / config -> 配置与执行层
- 知识库结构与规则 -> `wiki`
- 重复方法 -> `skills`
- 稳定偏好与环境事实 -> `memory`
- 临时调试过程 -> `sessions`

这一步的价值是先收窄接口，而不是先把所有内容混在一起处理。

## Step 3: capture
作为样板案例，先把最近优化过程汇总为 raw：
- `raw/transcripts/hermes-optimization-sample-case-2026-04.md`

这个 raw 不是最终答案层，而是把分散会话压成一个后续可编译的来源层。

## Step 4: compile
从 raw 与已验证产物中，可以归纳出这轮 Hermes 优化的 4 类正式成果：

### A. Quick command 收敛
- 脚本：`/home/lin/.hermes/scripts/utils/wd.py`
- 配置：`command: python3 ~/.hermes/scripts/utils/wd.py`
- 收敛动作：去掉 `{args}` 漂移，让脚本、配置和调用链重新对齐

### B. Cron 投递修复
- 任务：晨报
- deliver 已修到：`telegram:6346028803`
- last_status：`ok`
- 收敛动作：把“执行成功但没送达”从 local 输出改成真实 Telegram 投递

### C. 知识库基础设施
- 路径：`~/wiki`
- 已建立 SCHEMA / index / log / raw / concepts / comparisons / queries
- 收敛动作：把长期知识从聊天层迁移到文件化层

### D. 方法与规范沉淀
- 已沉淀规范页：检索、写作、lint、操作流、边界、架构
- 已创建 skill：`hermes-formalized-ai-workflow`
- 收敛动作：把一次次“怎么做”提升为正式方法层

## Step 5: retrieve
整理之后，未来再问类似问题时，不必重新翻整段聊天：
- 问架构和规则 -> 先查 `wiki`
- 问方法怎么跑 -> 查 `skills`
- 问具体历史过程 -> 查 `session_search`
- 问晨报现在怎么配 -> 读 config / cron 当前状态

这就是 `[[hermes-retrieval-priority-and-answer-path]]` 在真实场景里的落地。

## Step 6: maintain
这轮优化之所以能变成样板，不只是因为“做过了”，而是因为维护动作也完成了：
- 页面写作有 `[[hermes-wiki-page-writing-standards]]`
- 健康检查有 `[[hermes-wiki-lint-and-health-check-standards]]`
- 知识库流程被压成 `[[hermes-knowledge-base-operating-flow]]`
- 方法被提升成 skill，而不是继续困在聊天里

## Reusable pattern
这次样板的真正通用模式是：
1. 发现接口漂移或上下文漂移
2. 把问题分流到正确层
3. 先落 raw 或当前状态
4. 再编译成正式 artifact
5. 通过 index / log / lint 让结构稳定
6. 最后把重复方法提升为 skill

## Why this case matters
这个样板说明，优化 Hermes 本身时，最有效的方法不是继续增加聊天说明，而是不断生产和校正 durable artifacts：
- 配置
- 脚本
- cron
- wiki
- skill
- log

这也正是 `[[hermes-ai-workflow-formalization-principles]]` 所说的：
AI 的价值不在于维持模糊上下文，而在于帮助你更快地产出和维护形式化结构。

## Takeaway
一句话总结这个样板案例：
最近优化 Hermes 的过程，本质上就是把零散问题逐步压缩成可验证、可复用、可检索的长期资产。

## Related
- [[hermes-ai-workflow-formalization-principles]]
- [[hermes-knowledge-base-operating-flow]]
- [[hermes-retrieval-priority-and-answer-path]]
- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
