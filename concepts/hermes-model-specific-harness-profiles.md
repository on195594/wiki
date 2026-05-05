---
title: Hermes Model-Specific Harness Profiles
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [hermes, agent, harness, model-profiles, skills, context-engineering, verification]
sources: [raw/articles/langchain-tuning-deep-agents-different-models-2026-04-29.md, concepts/hermes-agent-workflow-layering-and-adoption-order.md, concepts/hermes-context-layer-operating-rules.md]
status: stable
---

# Hermes Model-Specific Harness Profiles

## Summary
LangChain 的 Deep Agents 文章给 Hermes 的核心启发是：Agent 的能力不是裸模型能力，而是 `模型 + harness` 的组合能力。对 Hermes 来说，harness 不只是 runtime profile；它包括 system/developer 指令、skills、工具暴露方式、subagent 使用、项目上下文、verification 纪律、cron 入口和 wiki/memory 注入策略。

因此 Hermes 下一阶段不应先扩张更多模型或更多 profile，而应建立“按模型适配执行方式”的治理规则：默认仍保持 `default` 主脑稳定，但把 Codex、Claude、Gemini 等模型的差异沉淀成可测试的 harness overlay，再用小项目验证是否值得升为 skill、quick command、cron 或 runtime profile。

## Source article in one paragraph
`[[langchain-tuning-deep-agents-different-models-2026-04-29]]` 介绍 Deep Agents 新增 `HarnessProfile`：按模型或 provider 声明式调整 prompt、tool naming、middleware、subagent 和 skills。文章给出的证据是，在 `tau2-bench` 困难子集上，custom profile 让 GPT 5.3 Codex 从 33% 提升到 53%，Claude Opus 4.7 从 43% 提升到 53%。这说明模型切换不能只换 model name，还要换外部执行环境。

## Hermes translation
### 1. Hermes 的 harness 层在哪里
在当前 Hermes 中，类似 Deep Agents harness 的东西分散在这些层：
- `SOUL.md` / developer rules：全局执行纪律、工具优先、验证要求
- memory / user profile：短小长期事实和偏好
- skills：某类任务的可重复方法
- project context / `AGENTS.md`：项目局部规则
- tools / MCP：可用动作空间
- subagents：上下文隔离和并行执行方式
- cron：稳定 workflow 的调度入口
- wiki：长期概念、架构原则和决策依据

所以 Hermes 的 model-specific harness 不是一个单点配置文件，而是一组跨层 overlay。

### 2. 当前不应马上新建 Hermes runtime profile
当前运行状态显示 Hermes 只有 `default` profile，模型为 `gpt-5.5`，provider 为 OpenAI Codex，Gateway 正常运行，Telegram 是主要入口。这符合现阶段策略：保持主脑稳定，不因为一篇文章就立刻增加 runtime profile。

更合理的顺序是：
1. 先在 wiki 记录模型差异原则。
2. 再在现有 skills 中做窄范围 prompt/tool 适配。
3. 用小型 eval project 验证某个适配是否真的改善结果。
4. 只有当稳定收益明确时，才考虑 quick command、skill、cron 或 Hermes profile 层的推广。

### 3. 不同模型的 Hermes 适配方向
#### OpenAI Codex / gpt-5.5 默认主脑
适合强化：
- 先读文件、搜索、列资源，再行动
- 独立读取和搜索尽量并行批量执行
- 文件修改优先用结构化 patch，而不是 shell 文本替换
- coding / config 任务必须有前后验证

落点：主要写进软件开发、Hermes runtime、project execution 类 skills，而不是 memory。

#### Claude / Claude Code 类工作流
适合强化：
- 工具结果后显式反思质量
- 用 XML/结构化段落约束工具使用和验证
- 不凭记忆断言文件、测试、系统状态
- 更适合长文档、代码审查、计划评审等需要反思的环节

落点：Claude Code / code review / planning skills 的 prompt overlay。

#### Gemini / gsummary 类工作流
适合强化：
- 抽取源文本与执行总结分离
- 对 share links、blocked pages、partial snippets 显式声明限制
- 输出稳定 schema，避免跨模型漂移
- 保留全文路径和 run logs，便于回放

落点：`gemini-summary`、`gsummary`、文章总结 workflow。

## Engineering principles for Hermes
### Principle 1: Model swap requires harness review
切换模型前必须问：当前 prompt、tools、skills、verification 是否适配这个模型？不能只看 benchmark 或模型名。

### Principle 2: Optimize overlays before core changes
先通过 skill、project context、wrapper script、quick command 形成窄 overlay。只有 overlay 经验证反复有效，才考虑改 Hermes core 或 runtime profile。

### Principle 3: Eval before promotion
任何 model-specific harness 改动都必须有小型可复现 eval：同一任务、同一输入、同一验收标准，对比 base 与 overlay。

### Principle 4: Do not bloat global prompt
模型差异不应全部塞进全局系统提示。能放 skill 的放 skill，能放项目上下文的放项目上下文，能放 wrapper 的放 wrapper。

### Principle 5: Verification is part of the harness
对 Hermes 来说，verification 不是任务末尾的一句话，而是 harness 的组成部分：读取、测试、状态检查、日志检查和输出路径确认都应成为模型适配的一部分。

## Promotion ladder
1. `session note`：一次性观察，默认不沉淀。
2. `wiki concept`：有长期架构价值的原则。
3. `skill patch`：已在同类任务中多次复用的执行方法。
4. `wrapper / quick command`：输入输出稳定、适合封装的流程。
5. `validation project`：需要 A/B 比较或多轮评估的 harness 改动。
6. `cron`：方法稳定且适合定时执行。
7. `Hermes runtime profile`：只有当运行时隔离有真实价值时才创建。

## Anti-patterns
- 因为读到“profile 有用”就马上创建多个 Hermes runtime profiles
- 把 Codex、Claude、Gemini 的所有差异塞进 memory 或全局 SOUL
- 没有 eval 就把 prompt overlay 推广到所有任务
- 用模型 benchmark 替代本地 workflow 评估
- 让 cron 运行还没稳定的 model-specific prompt 实验


## Validation outcome — 2026-04-30
The first Hermes harness-profile validation project is now closed. The result confirms the core principle but narrows the promotion path:

- Planning overlay produced repeated evidence and was promoted as a narrow `writing-plans` skill patch.
- Code review overlay produced repeated evidence and was promoted as a narrow `requesting-code-review` skill patch.
- Article summary overlay is useful but not promoted yet; source/extraction limitation handling needs a separate summary-only validation.
- Coding/config overlay is deferred because the baseline was already strong and no repeat round was run.
- No Hermes core, `SOUL.md`, runtime profile, cron, or memory changes were justified.

The validated promotion sequence is now:

```text
wiki concept → project-local evidence → repeated lane evidence → narrow skill patch → post-patch regression → wrapper/cron/runtime/core only with separate evidence
```

Detailed closeout: [[hermes-harness-profile-validation-final-closeout]].

## Related
- [[hermes-harness-profile-validation-final-closeout]]
- [[hermes-system-model-specific-harness-optimization-plan]]
- [[langchain-tuning-deep-agents-different-models-2026-04-29]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-context-engineering-design-priorities]]
- [[codex-agent-workflow-layering]]
- [[gemini-summary]]
- [[index]]
- [[log]]
