# AGY read-only review prompt: deterministic analytics / LLM reasoning boundary wiki ingestion

You are AGY reviewing a completed Hermes wiki ingestion. This is a read-only knowledge-quality review.

## Hard boundaries

- Read-only only: do not write files, commit, edit wiki pages, change memory, skills, cron, MCP, runtime config, wrappers, prompts, or Hermes core.
- Review the wiki artifact and commit quality; do not re-summarize the article unless needed to check fidelity.
- Treat deterministic checks as separate gates; focus on knowledge shape, source fidelity, duplication risk, layer routing, index/log consistency, and actionable patch recommendations.

## Scope under review

Wiki root: `/home/lin/wiki`
Commit under review: `3cc12067cd1c1ac1aafa54c6ebe5ef20f9708d3c` (`docs: 沉淀混合 AI 确定性分析边界`)

Files under review:
- `raw/articles/towardsdatascience-hybrid-ai-deterministic-analytics-2026-05-22.md`
- `concepts/deterministic-analytics-llm-reasoning-boundary.md`
- `index.md`
- `log.md`

Adjacent concepts to compare for duplication / link quality:
- `concepts/typed-ai-agent-boundaries.md`
- `concepts/constrained-toolbox-evaluator-loop.md`
- `concepts/hermes-ai-workflow-formalization-principles.md`
- `concepts/production-ai-agent-evaluation-framework.md`

## Review questions

1. Is the new concept page a valid smallest durable unit, or does it duplicate an existing concept too much?
2. Does the concept preserve source-backed claims accurately and avoid over-promoting Copilot Studio, manufacturing-specific schemas, or article-specific numbers into Hermes defaults?
3. Is the layer routing correct: raw source + concept + index/log only, with no implied memory/skill/runtime promotion?
4. Are wikilinks and relationships useful and not noisy?
5. Are there blocking or important issues that should be patched before this ingestion is considered clean?

## Required output format

Return exactly these sections:

- Verdict: PASS / PASS_WITH_MINOR_FIXES / NEEDS_CHANGES
- Blocking: bullet list, or `none`
- Important: bullet list, or `none`
- Minor: bullet list, or `none`
- Passes: bullet list of what is sound
- Recommended patches: concrete patch recommendations, or `none`

Keep the review concise and evidence-based. Reference exact file paths and line/section names where possible.
