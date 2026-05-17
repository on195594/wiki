---
title: Repository-Level Code Intelligence Layer
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [ai-coding, architecture, workflow, context-engineering, agent]
sources: [raw/articles/marktechpost-repowise-repository-code-intelligence-2026-05-15.md]
status: draft
---

# Repository-Level Code Intelligence Layer

## Summary

仓库级代码智能层把代码库从“文件集合”转成可排序、可查询、可验证的工程图谱，为 AI coding agent 提供比全仓扫描更稳定、更低噪音的上下文入口。它的核心不是某个工具，而是先把仓库索引、图谱化、风险排序和决策记录结构化，再把这些结果压缩成 AI 可用的项目上下文。

这页编译自 [[marktechpost-repowise-repository-code-intelligence-2026-05-15]]，并补充 [[ai-coding-assistant-context-budget-management]]、[[codex-agent-workflow-layering]] 和 [[claude-code-practical-workflow-tips]]：这些页面分别关注上下文预算、agent 工作流分层和 Claude Code 使用方式；本页关注代码仓库本身如何变成可分析的知识层。

## Core principle

不要让 coding agent 以“读整个仓库”作为理解项目的默认入口。

更稳的入口是：先把仓库变成结构化信号，再把高价值信号交给 agent。仓库结构、依赖关系、核心节点、共变历史、死代码候选和架构决策记录，应当先被分析、排序、筛选，再进入 prompt、`AGENTS.md`、`CLAUDE.md` 或项目文档。

## Repository intelligence layers

### 1. Indexing layer

先建立仓库级索引，记录文件、模块、符号、文档和基础元数据。

作用：
- 给后续图谱、搜索和 AI 上下文生成提供统一底座。
- 避免每次任务都重新做全仓探索。
- 把项目理解从临时聊天状态转成可复用工程资产。

### 2. Dependency graph layer

把文件、模块、导入关系、调用关系或引用关系建成图。

作用：
- 把代码库从目录树转成依赖网络。
- 帮助识别核心文件、边界模块和高耦合区域。
- 为可视化、风险排序和上下文裁剪提供依据。

### 3. Centrality ranking layer

用 PageRank、degree centrality 或类似图指标识别“高影响节点”。

作用：
- 接手陌生项目时，优先阅读高权重文件。
- 修改前识别潜在高风险区域。
- 给 agent 明确起始文件，而不是让它盲目搜索。

注意：中心性高只表示结构影响大，不等于业务重要性一定最高；仍需要测试、Git 历史和人工判断校准。

### 4. Community detection layer

用社区检测识别代码图中的自然模块群。

作用：
- 辅助理解模块边界。
- 发现目录结构和实际依赖结构不一致的地方。
- 为重构、拆分、文档组织和 agent 任务分区提供线索。

### 5. Git intelligence layer

结合 Git blame、提交共变和历史改动模式理解维护风险。

作用：
- 找出经常一起变化的文件。
- 判断某个修改可能牵动哪些区域。
- 帮助区分“结构上相连”和“维护上相连”。

### 6. Dead-code candidate layer

死代码检测应输出候选，不应直接触发删除。

正确使用方式：
- 标记可能未使用的函数、文件或路径。
- 按安全度排序。
- 要求测试、静态分析和人工审查确认。
- 对生产脚本、插件入口、反射调用、CLI 入口、配置驱动代码保持保守。

### 7. Inline decision layer

把架构决策记录在靠近代码的位置，再自动汇总。

示例模式：
- `# DECISION:` 记录为什么这样设计。
- `# TECH_DEBT:` 记录已知债务和触发条件。
- `# SAFETY:` 记录不能随意修改的边界。

价值：决策离代码更近，不容易变成过期文档；同时又能被工具提取成全局 ADR 或项目上下文。

### 8. AI context generation layer

把仓库智能结果压缩成 AI assistant 可读的上下文文件，例如 `CLAUDE.md`、`AGENTS.md` 或项目内 architecture note。

应包含：
- 项目用途和入口。
- 核心模块和高影响文件。
- 构建、测试、验证命令。
- 关键架构决策。
- 高风险区域和禁止事项。
- 适合 agent 起步阅读的文件清单。

不应包含：
- 全量源码解释。
- 过长工具输出。
- 未验证的死代码删除建议。
- 一次性任务细节。

## Hermes mapping

### Wiki

本页是概念层：回答“代码仓库如何成为 AI 可用的结构化知识层”。它不等同于 Repowise 使用手册，也不直接授权安装工具或修改 Hermes runtime。

### Coding workflow

对 Hermes coding 任务的启发：
- 子任务开始前，先给 agent 起始文件和结构化上下文。
- 对陌生仓库，优先生成或读取仓库智能摘要，而不是让 agent 全仓扫描。
- 高噪音探索适合交给 subagent，主会话只接收核心文件、风险和验证建议。
- `AGENTS.md` / `CLAUDE.md` 应短而准，可由仓库智能辅助生成，但仍需人工审查。

### Skill/reference candidate

这篇文章不应直接升级为 active skill。只有在本地项目验证过仓库图谱、死代码候选、上下文生成质量后，才适合把其中某个窄动作沉淀为 skill/reference，例如：
- 陌生项目结构分析 checklist。
- 项目 `AGENTS.md` 生成前检查。
- 死代码候选审查流程。

## Relationship to existing concepts

- `[[ai-coding-assistant-context-budget-management]]` 关注减少无关上下文进入模型；本页补充“如何先把仓库压成高密度上下文”。
- `[[codex-agent-workflow-layering]]` 说明 prompt、AGENTS.md、skills、MCP 和 automation 的分层；本页补充 AGENTS/CLAUDE 这类 repo context 可以由仓库智能辅助生成。
- `[[claude-code-practical-workflow-tips]]` 强调 coding agent 要能验证和拿到正确上下文；本页补充上下文来源应包含结构化仓库图谱，而不是只靠人工描述。
- `[[llm-engineering-knowledge-map]]` 是更上层的 LLM 工程总览；本页是 AI coding 场景下的仓库知识层。

## What to preserve, what not to preserve

保留：
- 仓库是依赖图，不只是目录树。
- PageRank / centrality 可辅助定位高影响文件。
- 社区检测可辅助识别模块边界。
- Git 共变关系可提示修改风险。
- 死代码检测只能作为候选发现。
- 源码邻近的架构决策标签可以降低 ADR 腐化。
- AI 上下文文件应由结构化仓库信号辅助生成。

不保留为核心知识：
- Repowise 的完整安装教程。
- `itsdangerous` 示例细节。
- `safe_to_delete_threshold: 0.7` 这类工具默认值作为通用标准。
- Anthropic/OpenAI provider 自动选择逻辑作为 Hermes 默认规则。
- 将 Repowise 直接纳入 Hermes 默认 coding workflow。
- 自动删除死代码或自动接受 AI 架构解释。

## Practical checklist

接手陌生项目或准备让 agent 处理大型仓库前：

1. 是否已有项目索引或结构摘要？
2. 是否知道高影响文件和主要模块边界？
3. 是否能区分依赖关系、调用关系和 Git 共变关系？
4. 是否有可验证的测试/构建入口？
5. 是否有靠近代码的架构决策或安全边界记录？
6. 是否能生成短小、可审查的 `AGENTS.md` / `CLAUDE.md`？
7. 死代码候选是否经过测试和人工审查，而不是直接删除？

## Limits

文章是工具教程，示例只覆盖较小的 Python 项目 `itsdangerous`。它没有证明 Repowise 在大型 monorepo、跨语言仓库、动态入口、插件系统、反射调用或低测试覆盖项目中的准确性和性能。因此，本页只沉淀仓库智能层的设计模式，不沉淀 Repowise 作为默认工具选择。

## Related

- [[marktechpost-repowise-repository-code-intelligence-2026-05-15]]
- [[ai-coding-assistant-context-budget-management]]
- [[codex-agent-workflow-layering]]
- [[claude-code-practical-workflow-tips]]
- [[llm-engineering-knowledge-map]]
- [[subagent-orchestration-patterns]]
- [[index]]
- [[log]]
