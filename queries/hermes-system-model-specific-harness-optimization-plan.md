---
title: Hermes System Model-Specific Harness Optimization Plan
created: 2026-04-30
updated: 2026-04-30
type: query
tags: [hermes, optimization, model-profiles, harness, workflow, validation]
sources: [concepts/hermes-model-specific-harness-profiles.md, raw/articles/langchain-tuning-deep-agents-different-models-2026-04-29.md, docs:hermes-agent]
status: draft
description: 制定 Hermes 系统针对不同模型优化 harness profile 的计划和验证路径。
aliases: [harness-optimization-plan]
---

# Hermes System Model-Specific Harness Optimization Plan

## Goal
把 LangChain Deep Agents 的 model-specific harness profiles 原则翻译成 Hermes 的系统优化路线：在不贸然改 Hermes core、不增加无验证 profile 的前提下，让不同模型/工作流拥有更合适的 prompt、tool、skill、verification 和 wrapper overlay。

## Current baseline
截至 2026-04-30 的现场检查：
- `hermes config check`：通过，config version 22
- `hermes profile list`：只有 `default` profile
- 当前模型：`gpt-5.5`
- Provider：OpenAI Codex
- Gateway：running
- 主要入口：Telegram

这意味着计划应围绕“稳定 default 主脑 + 局部 harness overlay + 小项目验证”推进，而不是先创建一堆 profile。

## Operating principle
一句话：**Hermes 不先追求更多模型，而先让每个高频 workflow 的 harness 与实际模型匹配。**

这里的 harness 包括：
- system/developer 指令
- skills
- project context / AGENTS.md
- wrapper scripts / quick commands
- tool choice and naming
- subagent delegation pattern
- verification command / log check
- cron entrypoint

## Phase 0 — Freeze scope and protect current stability
### Objective
确认这次优化是“方案与局部 overlay 设计”，不是立即修改 Hermes core。

### Actions
- 保持 `default` profile 作为主脑。
- 不新建 `lab` / `claude` / `gemini` runtime profile，除非后续验证证明运行时隔离有必要。
- 不把模型差异写入 memory；模型差异属于 wiki/skill/project context。
- 对任何后续配置或脚本改动先备份，再修改，再验证。

### Done when
- 当前原则记录在 `[[hermes-model-specific-harness-profiles]]`。
- 后续执行必须先从本计划挑一个小闭环，而不是泛化推进。

## Phase 1 — Build a Hermes harness overlay registry
### Objective
建立一个轻量 registry，列出高频模型/工作流对应的 harness 差异，不改 runtime。

### Initial registry
#### Default / OpenAI Codex / gpt-5.5
适配方向：
- 工具调用前批量确定所需文件、搜索和系统状态
- 独立读取/搜索并行化
- 文件改动优先 patch
- 修改后必须跑验证命令或读取状态

主要承载层：
- `hermes-dev-standards`
- `systematic-debugging`
- `writing-plans`
- `subagent-driven-development`
- Hermes runtime/config 相关 skills

#### Gemini / gsummary
适配方向：
- Hermes 负责 extraction 与 grounding
- Gemini 负责稳定中文 schema summary
- blocked/share link 限制必须进源文本和最终回复
- wrapper 输出路径必须保留

主要承载层：
- `gemini-summary`
- `gsummary`
- `article-and-content-summarization`

#### Claude / Claude Code
适配方向：
- 工具结果后 reflection
- XML/结构化提示约束
- 长文档、计划评审、代码审查任务优先使用
- 主动观察文件/测试/状态，禁止凭记忆断言

主要承载层：
- `claude-code`
- `github-code-review`
- `requesting-code-review`
- planning / review 类 skills

### Done when
- registry 先保存在 wiki；只有发现某类 overlay 被重复使用，才 patch 对应 skill。

## Phase 2 — Define a small eval suite before changing skills
### Objective
用小项目验证不同 overlay 是否真的改善 Hermes 输出，而不是靠感觉调 prompt。

### Proposed project
`/home/lin/.hermes/projects/hermes-harness-profile-validation`

### Eval cases
每个 case 都要有 base prompt 和 overlay prompt 对比：
1. **Coding/config case**：读取一个小 repo，修改一处配置，要求备份与验证。
2. **Article summary case**：share.google / canonical URL / blocked fallback，要求保留限制和全文路径。
3. **Code review case**：给定 diff，要求先查相关文件再评审。
4. **Planning case**：把一个模糊 Hermes 优化需求压成可执行计划，要求不越权改 core。

### Metrics
- 是否读了必要文件 / 状态
- 是否避免凭记忆断言
- 是否执行验证
- 是否保留输出路径 / 日志路径
- 是否减少无关上下文注入
- 是否遵守 layer routing

### Done when
- 每个 case 至少有 1 个 base run 和 1 个 overlay run。
- 有明确结论：保留、修改、还是丢弃 overlay。

## Phase 3 — Patch narrow skills, not global prompt
### Objective
只把验证有效的 overlay 写进对应窄职责 skill。

### Patch candidates
- Codex/default coding overlay → software-development / Hermes runtime 相关 skills
- Gemini summary overlay → `gemini-summary` / `gsummary`（已有较成熟，不重复扩张）
- Claude reflection overlay → `claude-code` / review / planning skills

### Rules
- 不把所有模型差异写进 `hermes-agent` index skill。
- 不把 workflow 方法写进 memory。
- 不改 `SOUL.md`，除非是跨所有任务都成立的执行纪律。
- 每次 skill patch 后要能说明：触发条件、边界、步骤、坑点、验证。

### Done when
- 每个被 patch 的 skill 都更窄、更可执行，而不是变成模型百科。

## Phase 4 — Decide whether runtime profiles are needed
### Objective
只有当 skill/wrapper overlay 不够时，才考虑 Hermes runtime profile。

### Runtime profile eligibility
必须同时满足：
- 某模型需要长期独立 provider/model 配置
- 使用场景稳定且高频
- 与 default 主脑混用会增加错误或成本
- 有小项目 eval 证明收益
- 有明确 rollback 路径

### Current recommendation
暂不新增 runtime profile。保持 `default` 为主；Gemini summary 继续用 wrapper；Claude/Codex 继续通过 skills/subagents/CLI 工具承接。

## Phase 5 — Automation only after the method stabilizes
### Objective
不要把 prompt 实验 cron 化。

### Eligible cron candidates
- 周度 Hermes harness drift check：只有当 eval suite 稳定后再考虑。
- gsummary regression：已有 wrapper/verifier 时可继续保留。
- wiki health check：已有明确标准时可调度。

### Not eligible
- “每周自动优化 prompt”这类无验收标准的任务。
- 需要人工大量判断的 model comparison。

## Concrete next actions
1. 保留本页作为计划，不立即改 Hermes runtime。
2. 如果要进入执行，先创建 `hermes-harness-profile-validation` 小项目。
3. 在该项目中写 4 个最小 eval cases。
4. 跑 default/base 与 overlay 对比。
5. 只把胜出的 overlay patch 到对应窄 skill。
6. 三轮以上稳定后，再评估是否需要 runtime profile 或 cron。

## Stop conditions
出现以下情况要停止扩张：
- overlay 只在一个样例中有效
- prompt 变长但验证收益不明显
- skill 开始变成模型说明书
- 需要改 Hermes core 才能继续，但没有可复现 eval
- runtime profile 的收益无法覆盖维护成本

## Relations
- depends_on: [[hermes-model-specific-harness-profiles]]

## Related
- [[hermes-model-specific-harness-profiles]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-knowledge-architecture]]
- [[hermes-health-dashboard]]
- [[index]]
- [[log]]
