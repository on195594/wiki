# AGY Read-only Wiki Review: Context vs Memory Engineering Ingestion

你是 AGY，作为独立审查者。请对本次 Hermes wiki 变更做**只读知识质量审查**。

## Scope

工作目录：`/home/lin/wiki`

本次审查只覆盖以下文件/变更：

- `raw/articles/machinelearningmastery-context-vs-memory-engineering-agentic-ai-systems-2026-07-03.md`
- `concepts/agent-context-engineering.md`
- `index.md`
- `log.md`

相邻概念页可只读参考：

- `concepts/hermes-context-engineering-design-priorities.md`
- `concepts/hermes-context-layer-operating-rules.md`
- `concepts/llm-context-engineering-layer.md`
- `concepts/hermes-memory-skills-wiki-boundaries.md`

## Boundary

只读审查。不要写文件，不要提交，不要修改 memory、active skills、runtime config、cron、MCP、wrapper、gateway、profile、Hermes core，也不要建议未经验证的 active-layer promotion。

当前 wiki 工作区可能包含其他未提交历史变更；请不要把范围外变更作为本次 blocking，除非它们直接破坏本次文件的链接/索引/语义一致性。

## What changed

这次把 Machine Learning Mastery 文章 `Context vs. Memory Engineering in Agentic AI Systems` 作为 source-backed wiki 资产落地：

1. 新增 raw source note，包含来源、提取说明、Gemini summary excerpt、正文抽取。
2. 更新既有概念页 `agent-context-engineering.md`，没有新建重复概念页。
3. 新增 `Context vs. memory engineering boundary` section，核心主张是：
   - memory 决定可取信息集合；
   - context assembly 决定本轮模型真正看到什么、放在哪里、占多少预算；
   - 外部文章方法论不应直接扩大长期 memory 写入，也不应直接升级为 active Hermes 行为。
4. 更新 `index.md` 的更新时间。
5. 更新 `log.md`，明确 active-layer boundary。

Hermes 已跑过：

```text
python3 _meta/scripts/wiki_health_check.py --root /home/lin/wiki --format markdown
# Wiki Health Check: PASS
# P0=0, P1=0, P2=0

git diff --check
# no output
```

## Review questions

请重点检查：

1. 最小持久单元是否正确：这篇文章是应该更新 `agent-context-engineering.md`，还是应该新建独立概念页？
2. source fidelity 是否足够：raw source note 的 provenance、提取说明、局限和摘要是否足以支撑概念页新增内容？
3. 层级路由是否正确：是否清楚区分 wiki、memory、skill reference、active workflow？有没有暗示 active promotion？
4. wikilink 与邻近概念关系是否清楚：是否应该补/删任何链接，是否存在重复或概念漂移？
5. 是否存在 blocking / important / minor 问题；如果有，请给最小 patch 建议。

## Output format

请用中文输出，严格按以下结构：

```markdown
Verdict: PASS / PASS_WITH_NOTES / REQUEST_CHANGES

Blocking:
- ...

Important:
- ...

Minor:
- ...

Passes:
- ...

Recommended patches:
- ...
```

如果某一类没有问题，请写 `- None`。