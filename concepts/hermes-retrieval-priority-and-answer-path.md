---
title: Hermes Retrieval Priority and Answer Path
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [hermes, knowledge-base, workflow, tool, configuration]
sources: []
status: stable
description: 定义 Hermes 回答问题时 wiki、memory、skills、sessions、raw 和外部检索的优先级。
aliases: [retrieval-priority, answer-path]
---

# Hermes Retrieval Priority and Answer Path

## Summary
Hermes 处理知识问题时，不应直接把当前模型记忆当答案来源，而应遵循固定的检索优先级与回答路径。
核心原则是：先用已沉淀知识，后补外部信息，最后把高价值结果重新沉淀回知识库。

## Priority order
默认优先级如下：
1. `wiki`
2. `memory`
3. `skills`
4. `sessions / session_search`
5. `raw` sources
6. external search / extract
7. write-back to `wiki` when the result has lasting value

这个顺序不是“谁更重要”，而是谁更适合作为当前问题的答案依据。

## Why this order
### 1. wiki first
- wiki 是正式知识层
- 内容经过整理、结构化、可交叉链接
- 最适合作为稳定回答依据

### 2. memory second
- memory 提供用户偏好、稳定事实、环境约束
- 它负责修正回答方式和操作边界
- 但它不是长篇知识库

### 3. skills third
- skills 提供执行方法
- 当问题是“怎么做”而不是“是什么”时尤其重要
- 适合补充步骤、命令、验证方式

### 4. sessions fourth
- sessions 适合回忆过去做过什么
- 用于补历史上下文，而不是替代正式知识

### 5. raw fifth
- raw 是原始材料层
- 适合在 wiki 缺内容时回溯来源
- 不能直接替代整理后的知识页

### 6. external last
- 外部检索用于补足当前知识缺口
- 不应成为每次都从零开始的默认路径
- 否则知识无法累积

## Answer path
标准回答路径如下：
1. 识别问题类型：知识解释、执行方法、历史回忆、实时事实
2. 先查 `[[index]]` 与相关 wiki 页面
3. 用 `memory` 修正回答约束与用户偏好
4. 若涉及具体操作，再加载相关 `skills`
5. 若用户引用“上次做过的事”，再查 `sessions / session_search`
6. 若 wiki 不足，再回读 `raw` 或外部资料
7. 给出答案
8. 如果答案具有长期价值，沉淀回 `wiki`

## Path by question type
### A. 概念 / 架构 / 方法论问题
默认路径：
- `wiki` → `memory` → `external if needed` → `write-back`

### B. 怎么做 / 怎么配置 / 怎么排障
默认路径：
- `wiki` → `skills` → `memory` → `sessions if relevant` → `external if needed`

### C. “上次我们怎么做的”
默认路径：
- `sessions / session_search` → `wiki` → `skills`

### D. 当前事实 / 实时信息
默认路径：
- live tools / external search → `wiki` write-back if durable

## Relationship with boundaries
这条路径依赖 `[[hermes-memory-skills-wiki-boundaries]]` 的分工：
- `wiki` 负责正式知识
- `memory` 负责约束和稳定事实
- `skills` 负责执行流程
- `sessions` 负责历史回忆

如果边界混乱，检索顺序也会混乱。

## Write-back rule
满足以下任一条件时，答案应考虑回写 `wiki`：
- 以后高概率还会再问
- 需要跨来源综合
- 对系统设计或工作流有长期价值
- 回答中形成了清晰的结构化结论

以下内容通常不回写：
- 一次性临时结果
- 纯执行日志
- 短期状态
- 没有复用价值的即时问答

## Anti-patterns
- 每次都直接外部搜索，绕过 wiki
- 把 memory 当成知识页来用
- 有 skill 却不用，导致重复解释步骤
- 把 session 历史当作唯一可信来源
- 有长期价值的答案说完就丢，不回写 wiki

## Practical checklist
回答前快速过一遍：
1. 这个问题能否先从 `wiki` 找到？
2. 有没有相关 `memory` 会影响答案格式或边界？
3. 有没有相关 `skills` 能直接给出稳定做法？
4. 需不需要查 `session_search` 回忆过去？
5. 如果本地知识不足，才去外部补充
6. 这次答案值不值得回写 `wiki`？

## Canonical loop
一句话概括：
先查 wiki，按 memory 校准，用 skills 执行，用 sessions 回忆，用外部补缺，再把高价值结果写回 wiki。

## Related
- [[hermes-knowledge-architecture]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[hermes-wiki-lint-and-health-check-standards]]
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
