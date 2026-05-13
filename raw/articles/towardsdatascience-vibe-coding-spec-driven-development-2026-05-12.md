---
title: From Vibe Coding to Spec-Driven Development
author: Mariya Mansurova
source_type: article
source_url: http://towardsdatascience.com/from-vibe-coding-to-spec-driven-development/
publisher: Towards Data Science
published_at: 2026-05-12
captured_at: 2026-05-13 14:35:12 +0800
status: raw
tags: [ai-coding, spec-driven-development, workflow, agent, validation]
summary_path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260513-135202-From-Vibe-Coding-to-Spec-Driven-Development-Towards-Data-Science-401509-566400520-summary.md
---

# From Vibe Coding to Spec-Driven Development

## Source note

This raw page captures Mariya Mansurova's Towards Data Science article about moving from ad-hoc vibe coding to spec-driven development for AI-assisted software projects. The canonical URL was verified from the saved gsummary output and `web_extract` metadata.

Extraction limitation: `web_extract` returned a structured markdown summary rather than the full article body. The full local Gemini summary is preserved at `summary_path`.

## Core claim

For larger, longer-lived, multi-session, multi-agent, or collaborative AI-assisted software projects, spec-driven development is safer than vibe coding because it preserves requirements, decisions, roadmap, and validation criteria in repository-controlled documents instead of transient chat context.

## Key points

- Vibe coding works for small exploratory tasks but does not scale well when projects need shared conventions, durable reasoning, or multiple agents/humans.
- Spec-driven development decouples specification from implementation: the repo stores what is being built, why it exists, architectural decisions, technical constraints, and validation criteria.
- The developer role shifts toward agentic engineering: steering agents, writing/reviewing specs, making architectural calls, validating output, and updating plans when requirements change.
- The article's concrete example uses a Trainlytics fitness-tracking app built in roughly 4.5 hours with VS Code, Claude Code, and repo-local Markdown specs.
- GitHub Spec Kit is mentioned as an automation option, but the reusable Hermes lesson is the workflow shape, not adoption of a specific tool.

## Hermes relevance

- Reinforces the local Hermes rule that chat is an input channel, not the durable source of truth.
- Supports the existing `[[dijkstra-ai-programming-formalization]]` thesis: AI makes formalization cheaper; it does not remove the need for formalization.
- Supports `[[hermes-ai-workflow-formalization-principles]]`: long-lived work should be compressed into docs, specs, validation artifacts, wiki, and narrow skills.
- Complements `writing-plans` by explaining why larger agentic projects need a spec-driven shape before task execution.
- Does not justify new Hermes runtime, cron, memory, MCP, or core changes.

## Limitations

- The article is grounded in a greenfield personal app, not a large legacy system migration.
- Some claims, such as vibe coding being "over" or English becoming the primary programming interface, are trend judgments rather than benchmarked facts.
- GitHub Spec Kit and other tool examples should be treated as optional references, not Hermes defaults.
- The article supports workflow principles and skill refinements, not a standalone Hermes skill.

## Gemini summary excerpt

标题：From Vibe Coding to Spec-Driven Development

原文链接：http://towardsdatascience.com/from-vibe-coding-to-spec-driven-development/

一句话结论：
AI辅助开发正从随性的“直觉编程（Vibe coding）”转向系统化的“规范驱动开发（SDD）”，开发者的核心价值从直接编写代码转变为制定规范、编排AI智能体与架构审查。

核心观点：
- 直觉编程依赖简短提示词和反复试错，缺乏结构化方法和共享约定，在复杂或多人项目中难以扩展。
- SDD 将“规范（构建什么）”与“实现（代码）”解耦，通过仓库内 Markdown 文档持久化上下文。
- 软件工程师的角色正在向“智能体工程”转变，更强调监督、编排、架构决策、代码审查和需求修正。

可执行建议：
- 启动新项目时，先用 AI 辅助生成并版本控制项目级规范文档。
- 采用“计划 → 实现 → 验证”循环，让 agent 按文档执行而不是按聊天记忆执行。
- 阶段完成后引入 replanning，更新 roadmap 和变更记录。

全文路径：/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260513-135202-From-Vibe-Coding-to-Spec-Driven-Development-Towards-Data-Science-401509-566400520-summary.md

## Extracted article text

Source URL: http://towardsdatascience.com/from-vibe-coding-to-spec-driven-development/
Extraction: Hermes `web_extract` on 2026-05-13 returned a structured markdown summary rather than the full article body.

### Web extract summary

**Source:** Towards Data Science  
**Author:** Mariya Mansurova  
**Published:** May 12, 2026  
**Read time:** 16 min  
**Core claim:** For larger or collaborative AI-assisted software projects, spec-driven development is more robust than “vibe coding” because it preserves decisions, requirements, and context in version-controlled specifications.

The author demonstrates spec-driven development by building Trainlytics, a personal fitness tracking web app, in about 4.5 hours using LLM coding agents. The work is inspired by JetBrains’/DeepLearning.AI’s short course “Spec-Driven Development with Coding Agents”. The workflow uses VS Code, Claude Code plugin, a greenfield repository, Markdown specs stored in the repo, and LLM agents for planning, implementation, review, and replanning.

The article contrasts vibe coding with SDD. Vibe coding is a short-prompt iterative loop: ask for a change, run the app, notice mismatch, ask for adjustments, and repeat until good enough. Its problems are weak conventions, missing persistent reasoning, context decay, contradictory future agent behavior, and inconsistent patterns across a team or codebase.

SDD instead asks the developer to create structured Markdown documentation defining what is being built, why it is being built, architectural and technical decisions, requirements, validation criteria, roadmap, and phases. These specs are stored in the repo and updated alongside code.

## Related

- [[dijkstra-ai-programming-formalization]]
- [[hermes-ai-workflow-formalization-principles]]
- [[agent-self-validation-loops]]
- [[codex-agent-workflow-layering]]
- [[wiki-ingestion-workflow]]
