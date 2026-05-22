---
title: AGY read-only review prompt for constrained toolbox evaluator loop ingest
date: 2026-05-22
reviewer: agy
scope: read-only wiki ingestion review
---

# Rewritten user request

请对本次 NVIDIA 多智能体金融信号发现文章的 Hermes wiki 沉淀做一次独立只读审查。审查范围只限 wiki 知识质量与入库边界，不要修改任何文件、不要提交、不要升级到 memory/skill/cron/MCP/runtime。请检查新增 raw source、概念页、index/log 和相关交叉链接是否符合 Hermes wiki 的长期知识沉淀目标，并按 Blocking / Important / Minor / Passes 输出结论。

# What changed from the vague request

- 明确 reviewer 是 AGY，并且只能只读审查。
- 明确审查对象是已提交的 wiki 沉淀，不是重新总结原文。
- 明确输出格式：Blocking / Important / Minor / Passes。
- 明确层级边界：只审查 wiki，不建议或执行 active-layer 变更。

# Files to review

Repository root: `/home/lin/wiki`

Primary changed files from commit `b876f8e docs: 沉淀受限工具箱评估闭环`:

- `raw/articles/nvidia-financial-signal-discovery-multi-agent-2026-05-21.md`
- `concepts/constrained-toolbox-evaluator-loop.md`
- `concepts/typed-ai-agent-boundaries.md`
- `concepts/production-ai-agent-evaluation-framework.md`
- `concepts/agent-orchestration-production-tradeoffs.md`
- `index.md`
- `log.md`

Relevant existing adjacent concept for boundary comparison:

- `concepts/agent-resource-optimization.md`

# Review questions

1. Provenance and traceability
   - Does the raw source page preserve title, source URL, publisher/date, extraction date, summary path, and limitations clearly enough?
   - Are article-specific claims separated from interpreted Hermes concepts?

2. Durable unit and concept quality
   - Is `constrained-toolbox-evaluator-loop` a useful narrow concept rather than a duplicate of existing pages?
   - Does it avoid turning NVIDIA financial thresholds, vendor tools, or model names into Hermes-wide rules?
   - Does it define applicability, anti-patterns, and relation to adjacent concepts clearly?

3. Cross-linking and bookkeeping
   - Are index/log updates consistent with the new formal page?
   - Are backlinks from adjacent concept pages useful and not noisy?
   - Are frontmatter `updated` dates and source references reasonable?

4. Layer boundary
   - Does the change remain wiki-only?
   - Flag any language that implies unauthorized promotion to memory, skill, cron, MCP, runtime, or operational policy.

5. Health and hygiene
   - Note any Markdown/link/frontmatter issues likely to fail deterministic checks.
   - Note any formula/math formatting that could be misread as Markdown links.

# Output format

Return a concise review in Chinese with these sections:

- Verdict: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES
- Blocking findings: numbered list, or `None`
- Important findings: numbered list, or `None`
- Minor findings: numbered list, or `None`
- Passes / strengths: short bullets
- Recommended patches: exact file + section + proposed change, only for findings worth applying

Reminder: This is a read-only independent review. Do not modify files.