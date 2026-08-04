---
title: Agent Shared Wiki Index
created: 2026-08-04
updated: 2026-08-04
type: operation
tags: [agent, knowledge-base, context-engineering, multi-agent]
sources: [concepts/hermes-context-layer-operating-rules.md, concepts/hermes-retrieval-priority-and-answer-path.md]
status: active
source_policy: normative
description: Claude Code、Codex、AGY 与 Hermes 的共享 Wiki 入口和读写边界；AGY 常驻加载入口，其余按需进入。
aliases: [shared-agent-context, cross-agent-wiki-index]
---

# Agent Shared Wiki Index

## Summary

这是 Claude Code、Codex、AGY 与 Hermes 共用的 Wiki 路由入口。AGY 在每个新会话启动时读取本页，Claude Code、Codex 和 Hermes 按需读取；任何 Agent 都不在启动时加载或遍历整个 `/home/lin/wiki`。

## Canonical sources

- Wiki 根目录：`/home/lin/wiki`
- 总索引：`/home/lin/wiki/index.md`（[[index]]）
- 结构与写入规范：`/home/lin/wiki/SCHEMA.md`
- 上下文层边界：[[hermes-context-layer-operating-rules]]
- 检索顺序：[[hermes-retrieval-priority-and-answer-path]]
- memory / skills / wiki 分工：[[hermes-memory-skills-wiki-boundaries]]

## When to continue into Wiki pages

入口加载后，只在任务需要以下内容时继续检索正文页面：

- 用户问“之前如何决定”“已有方法是什么”“Wiki 中怎么规定”；
- 需要跨 Claude、Codex、AGY、Hermes 复用已经沉淀的架构、工作流、运维或研究知识；
- 当前项目文档引用某个 Wiki 概念；
- 外部检索前，需要确认本地是否已有可复用结论。

普通编码、明确的一次性任务、实时系统状态和当前会话中已经给出的事实，不要求先查 Wiki。

## Retrieval procedure

1. 先读项目内适用的 `AGENTS.md`、`CLAUDE.md`、README、ADR 和源码；项目规则优先于共享 Wiki。
2. 用用户原词、中文同义词、英文别名和较窄技术词搜索 Wiki。
3. 优先读取 `concepts/`、`operations/` 和 `queries/` 中最相关的少量页面；不要遍历或注入整个 Vault。
4. 回答时区分 Wiki 直接结论、本地推论和需要实时工具验证的当前事实。
5. 找不到时明确说明检索词和缺口，再决定是否查外部来源；不要把“未找到”说成“从未讨论”。

## Tool mapping

- **Claude Code**：通过本地文件搜索和读取 `/home/lin/wiki`；由 `~/.claude/CLAUDE.md` 指向本页。
- **Codex**：通过本地文件搜索和读取 `/home/lin/wiki`；由 `~/.codex/AGENTS.md` 指向本页。
- **AGY**：通过本地文件搜索和读取 `/home/lin/wiki`；全局规则 `~/.gemini/GEMINI.md` 要求每个新会话常驻加载本页，再按任务相关性读取正文。
- **Hermes**：优先使用已注册的只读 `wiki_readonly` 搜索/读取工具；必要时再使用本地只读文件工具。

## Write boundary

- 默认只读。只有用户明确要求创建、更新或摄取 Wiki 时才写入。
- 写入必须遵守 `SCHEMA.md`，同步更新 `index.md` 和 `log.md`，并运行 Wiki health check。
- 不写入凭证、Token、私密聊天原文、瞬时任务进度、未经验证的猜测或很快过期的系统状态。
- 多 Agent 不并发改同一页面；交接时给出具体文件路径和未提交 diff，而不是宣称拥有自动一致的“共享记忆”。

## Freshness and authority

- Wiki 是长期知识层，不是当前系统状态监控器；涉及版本、进程、端口、磁盘、市场或外部政策时必须重新使用实时工具验证。
- 页面内容与项目代码或项目级指令冲突时，以当前项目证据为准，并显式报告冲突。

## Relations

- depends_on: [[hermes-context-layer-operating-rules]]
- refines: [[hermes-retrieval-priority-and-answer-path]]
- related: [[hermes-memory-skills-wiki-boundaries]]
