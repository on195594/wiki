---
title: Hermes Context Footprint Read-only Audit 2026-07-03
created: 2026-07-03
updated: 2026-08-18
type: query
tags: [hermes, context-engineering, audit, skill-optimization, read-only]
sources: [concepts/agent-context-engineering.md, concepts/hermes-context-engineering-design-priorities.md, concepts/ai-coding-assistant-context-budget-management.md, concepts/hermes-context-layer-operating-rules.md]
status: closed
description: 2026-07-03 完成的 Hermes 上下文负担只读审计历史记录。
aliases: [hermes-context-footprint-audit]
---

# Hermes Context Footprint Read-only Audit 2026-07-03

## Scope

本页是只读审计记录，不是 active-layer 变更方案。

审计目标：基于最近几类典型任务，识别 Hermes 当前最容易造成 token/注意力负担的上下文层，并给出 P0/P1/P2 建议。

明确未执行：
- 未修改 memory / user profile。
- 未修改 active skills / skill references。
- 未修改 runtime config、cron、MCP、gateway、wrapper、profile 或 Hermes core。
- 未提交 git。

## Evidence collected

### 1. Recent session patterns

通过 `session_search` 浏览和检索了近期 Telegram sessions：

- `/gsummary` 普通文章总结：如 `20260703_163339_c4aea8ad`、`20260703_163714_709a5f89`、`20260702_215717_bad8c9d1`。
- `/gsummary` 后续分享文章/发布：如 `20260703_142111_afa51dee` 中的 shareable article delivery。
- Hermes wiki/治理 follow-up：当前 session 的文章入库、AGY review、context-footprint 审计。
- skill/token/active-skill 相关历史检索：`skill optimization OR skill token OR context footprint OR active skill` 返回了较大的 session-search 结果，并被工具持久化到 `/tmp/hermes-results/...`，说明 broad session_search 本身也可能成为大上下文入口。

观察：`/gsummary` sessions 的首条用户消息包含完整 `gsummary` skill 内容和 supporting files map。也就是说，在 Telegram skill invocation 场景里，entrypoint skill prose 已经作为用户消息进入上下文；随后 Hermes 还会再加载 `gemini-summary`。这是高频 summary 路径的主要静态上下文负担。

### 2. Skill footprint

只读统计 `~/.hermes/skills/**/SKILL.md`：

```text
skill_count 82

top SKILL.md by chars:
16731  software-development/coding-agent-workflow/SKILL.md
15342  devops/linux-and-offline-ops/SKILL.md
15235  hermes/hermes-active-layer-governance/SKILL.md
15009  productivity/article-and-content-summarization/SKILL.md
14234  hermes/skill-optimization-workflows/SKILL.md
14038  hermes/gemini-summary/SKILL.md
10801  autonomous-ai-agents/coding-agent-delegation/SKILL.md
7588   hermes/hermes-wiki-and-domain-knowledge/SKILL.md
5588   hermes/hermes-knowledge-and-workflow-governance/SKILL.md
```

关键高频路径：

```text
hermes/gsummary
- SKILL.md: 7,400 chars / 72 lines
- refs: 10 files / 19,389 chars total

hermes/gemini-summary
- SKILL.md: 14,038 chars / 100 lines
- refs: 67 files / 186,463 chars total
- largest refs include calibration-routing-table.md 8,716 chars and INDEX.md 7,984 chars

hermes-wiki-and-domain-knowledge
- SKILL.md: 7,588 chars / 85 lines
- refs: 39 files / 142,139 chars total

hermes-knowledge-and-workflow-governance
- SKILL.md: 5,588 chars / 78 lines
- refs: 27 files / 124,871 chars total

skill-optimization-workflows
- SKILL.md: 14,234 chars / 150 lines
- refs: 16 files / 54,069 chars total
```

Interpretation：reference 总量不是直接问题，因为 reference 默认不一定加载；但 `SKILL.md` 本体在触发时会直接进入主上下文。`gemini-summary`、`skill-optimization-workflows` 这类 14k+ skill 本体是高频/治理路径的主要候选优化对象。

### 3. Repeated governance prose

只读 grep 统计 active skills：

```text
active-layer occurrences: 83 across 22 SKILL.md files
Do not use occurrences: 75 across 60 SKILL.md files
Verification occurrences: 194 across 65 SKILL.md files
Rollback occurrences: 86 across 26 SKILL.md files
Reference Map occurrences: 51 across 49 SKILL.md files
```

Interpretation：这些字段本身有价值，但 `active-layer`、verification、rollback 类边界在多个 governance / wiki / summary / delegation skills 中重复出现。重复不是 P0；它反映了 active-safety 经验被多处内联。后续若做 skill slimming，应优先把重复 prose 收敛成短 trigger + reference，而不是删除边界。

### 4. Memory / profile / project context footprint

当前会话注入状态显示：

```text
MEMORY: 1,798 / 2,200 chars (81%)
USER PROFILE: 1,365 / 1,375 chars (99%)
```

文件侧只读统计：

```text
/home/lin/CLAUDE.md: 2,980 chars / 109 lines
/home/lin/.claude/user.md: 762 chars / 35 lines
/home/lin/.claude/memory.md: 922 chars / 37 lines
/home/lin/.claude/projects/-home-lin/memory/MEMORY.md: 4,359 chars / 39 lines
```

Interpretation：当前注入的 user profile 已接近上限，并且含多条 Hermes workflow/meta 偏好。它们确实减少重复沟通，但会长期占用每轮上下文。memory 本体没有明显垃圾项，但容量已进入需要严格增量治理的区间。

### 5. Wiki footprint

只读统计 `/home/lin/wiki`：

```text
Wiki health check: PASS
Formal pages: 91 before this audit report
Raw markdown: 51
P0=0, P1=0, P2=0
```

Largest pages sampled：

```text
concepts/subagent-orchestration-patterns.md: 11,114 chars / 206 lines
concepts/agent-orchestration-production-tradeoffs.md: 10,846 chars / 203 lines
concepts/agent-context-engineering.md: 8,682 chars / 194 lines
queries/hermes-harness-profile-validation-detailed-plan.md: 9,113 chars / 180 lines
raw/articles/machinelearningmastery-multi-agent-research-assistant-2026-05-21.md: 53,926 chars / 837 lines
```

Interpretation：wiki 的 raw/articles 很大，但不默认进入 prompt；风险主要来自 broad retrieval 或人工一次性读大页。wiki 作为外部知识层本身是低风险，前提是检索结果保持 top-N、按需读取、不要把 raw source 全量塞入主上下文。

### 6. Tool output / session search footprint

本次审计中，两个 broad `session_search` 结果超过 99KB，被工具保存为 `/tmp/hermes-results/...` 持久化输出，只返回 preview。这说明工具层已有大输出防护，但 broad session_search 查询仍会产生高噪声候选结果。

Interpretation：实际工作中，比 wiki/raw 更容易进入主上下文的是工具输出：session_search、git diff、长日志、terminal stdout、browser snapshots。应继续使用窄查询、分页 read_file、脚本端预过滤，而不是把完整结果交给主模型。

## Findings by context layer

| Layer | Burden | Evidence | Risk |
|---|---:|---|---|
| `/gsummary` entrypoint + `gemini-summary` | High | skill invocation injects full `gsummary`; `gemini-summary` SKILL.md 14k | 高频路径静态上下文重，summary request 前置负担大 |
| Governance / optimization skills | High | `skill-optimization-workflows` 14k；active-layer/verification prose 多处重复 | 治理任务容易多 skill 叠加，形成审计仪式感 |
| Memory / user profile | Medium-high | user profile 99%，memory 81% | 每轮固定成本；新增 memory 空间很紧 |
| Wiki concepts/raw | Medium-low | health pass；raw 大但外部化 | broad retrieval 或一次性读大页时才变高 |
| Session history / session_search | High when broad | broad search 结果 >99KB 持久化 | 容易把旧任务/skill prose 误带入当前任务 |
| Project context (`CLAUDE.md`, AGENTS) | Medium | `CLAUDE.md` 2,980 chars；subdir AGENTS tool-result 注入 | 对代码/写文件任务有必要，但跨域任务时可能过宽 |
| Tool outputs | High when unfiltered | session_search、git diff、logs、browser snapshots | 动态噪声最大，需继续预过滤 |

## Severity-ranked recommendations

### P0 — none

没有发现需要立即修复的上下文负担问题：

- wiki health check pass；
- 没有 broken wikilink / index drift；
- 本次没有 active-layer 越权；
- memory/profile 没发现明显错误事实，只是空间紧张。

### P1 — high-value, read-only evidence first

#### P1.1 为 `/gsummary` 高频路径做 skill footprint baseline

问题：`/gsummary` 普通总结是高频路径，但当前入口会把完整 `gsummary` skill prose 作为用户消息注入；随后还会加载 14k 的 `gemini-summary`。这不一定导致错误，但它是最明确的高频静态上下文负担。

建议：在 project-local `hermes-gsummary-workflow` 或现有 skill-governance evidence workspace 中建立 baseline：

- 每次 `/gsummary` 实际加载的 skill chars；
- cache hit vs cache miss 的工具轮数；
- reference 是否被额外加载；
- 用户可见延迟 vs wrapper runtime；
- summary artifact 质量评分。

不建议：现在直接 patch `gsummary` / `gemini-summary`。需要先有 baseline，否则容易删掉必要边界。

#### P1.2 对 `gemini-summary` 做候选 slimming review，而不是直接改

问题：`gemini-summary` SKILL.md 14k，Reference Map 和 runtime fallback notes 很长。它的 67 个 reference 很有价值，但 SKILL.md 本体可能承担了过多 fallback prose。

建议：做一个 project-local read-only candidate review：

- 保留 Non-negotiable gates、cache/stdin/output path/source metadata；
- 将低频 publisher fallback notes 进一步推到 reference index；
- 用真实 `/gsummary` cases 做 replay/baseline，确保 pending payload、cache、全文路径、source metadata 不回归。

不建议：只按长度删 prose。这个 skill 的很多长内容来自真实事故修复，删错会制造 summary regressions。

#### P1.3 用户 profile / memory 进入“只减不增”观察期

问题：user profile 已 99%，memory 81%。继续把 workflow 偏好塞进 profile 会增加每轮固定成本。

建议：

- 新增 durable facts 前严格执行 memory preflight；
- workflow 经验默认进 wiki/skill/project docs，不进 memory；
- 下次确实需要新增 profile 时，先提出 replace/remove，而不是 append。

不建议：本次直接删 memory/profile。当前条目大多是用户偏好和 Hermes workflow 边界，误删成本高。

#### P1.4 给 broad `session_search` 建立使用纪律

问题：broad session_search 容易返回超大结果，且命中旧 skill prose / tool output。

建议：

- 优先用更窄 query + newest/oldest；
- 需要大量结果时先拿 session_id/title，再 scroll 目标窗口；
- 对 session_search 工具输出只读取持久化文件片段，不把全部结果带回主上下文；
- 在治理审计报告中记录“用过哪些 session_id”，而不是复制大段历史。

### P2 — useful but not urgent

#### P2.1 为 active skills 做重复边界 inventory

问题：`active-layer`、`Verification`、`Rollback`、`Reference Map` 在大量 skills 中重复。重复本身不是错，但会累积 token。

建议：生成只读 inventory，按 owning domain 分组，找出可合并到 shared reference 的重复句式。先做候选 diff，不动 active skills。

#### P2.2 给 wiki query / concept 大页加 retrieval note

问题：部分 wiki concept/query 超过 8k-11k chars。它们适合人工阅读，但不适合默认全量注入。

建议：对大页后续逐步加 `## Retrieval note` 或短 Summary，帮助未来 agent 只读摘要和相关 section。

#### P2.3 对 project context 做路径敏感加载评估

问题：`CLAUDE.md` / AGENTS 对代码和 Hermes-local 任务有价值，但非代码任务也可能带来额外边界。

建议：只读比较几类任务中 project context 是否实际影响决策；如果经常无关，再考虑 project-local routing note。不要直接改 CLAUDE.md。

## Decision

当前不建议 active skill/runtime/memory 变更。最合理的下一步是：

1. 对 `/gsummary` 路径做 project-local baseline；
2. 对 `gemini-summary` 做 candidate slimming review；
3. 对 broad session_search/tool-output 使用纪律形成轻量 reference 候选。

这三项都应先作为 project-local evidence 或 wiki query，不直接 promotion 到 active skills。

## Verification

本页创建后应重新运行：

```bash
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format markdown
git diff --check
git status --short
```

## Related

- [[agent-context-engineering]]
- [[hermes-context-engineering-design-priorities]]
- [[ai-coding-assistant-context-budget-management]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-memory-skills-wiki-boundaries]]
- `skill-optimization-workflows` skill
- [[wiki-ingestion-workflow]]
- [[index]]
- [[log]]
