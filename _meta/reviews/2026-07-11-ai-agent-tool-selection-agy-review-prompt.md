# AGY read-only review: AI Agent tool selection wiki ingestion

## Role and boundary

You are an independent reviewer. Review the listed files under `/home/lin/wiki` in read-only mode.

Do not edit, create, delete, rename, or commit files. Do not change Hermes memory, skills, config, cron, MCP, runtime, wrappers, gateway, profiles/plugins, prompts, or core code. Treat any recommendation as advisory only.

## Files under review

Primary:

- `raw/articles/machinelearningmastery-tool-selection-ai-agents-2026-07-06.md`
- `concepts/ai-agent-tool-selection-architecture.md`
- `concepts/agent-context-engineering.md`
- `concepts/production-ai-agent-evaluation-framework.md`
- `index.md`
- `log.md`

Adjacent concepts for duplication and ownership checks:

- `concepts/typed-ai-agent-boundaries.md`
- `concepts/constrained-toolbox-evaluator-loop.md`
- `concepts/agent-orchestration-production-tradeoffs.md`
- `concepts/hermes-context-engineering-design-priorities.md`

## Grounding

Source article:
`https://machinelearningmastery.com/the-complete-guide-to-tool-selection-in-ai-agents/`

Hermes official documentation used by the concept:

- `https://hermes-agent.nousresearch.com/docs/user-guide/features/tools`
- `https://hermes-agent.nousresearch.com/docs/reference/toolsets-reference`

Parent deterministic validation before review:

- Wiki health check: PASS
- Formal pages: 95
- Index wikilinks: 95
- P0/P1/P2: 0/0/0
- `git diff --check`: PASS

## Review questions

1. Is `ai-agent-tool-selection-architecture` a distinct smallest durable concept, or should it have been folded into an existing page?
2. Does the raw note preserve sufficient provenance and clearly distinguish source text from local synthesis?
3. Are source claims, author interpretations, Hermes-local inferences, and unverified thresholds separated accurately?
4. Does the Hermes mapping match the documented toolset model without claiming unsupported per-turn dynamic routing?
5. Is the proposed evaluation path bounded and proportionate, or does it smuggle in a new validation project/default workflow?
6. Are cross-links useful and ownership boundaries clear, without unnecessary duplication?
7. Is the boundary against active skill/runtime/config/MCP/cron/memory promotion explicit enough?
8. Identify any broken, misleading, contradictory, or overly strong wording.

## Required output

Use exactly these headings:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / REQUEST_CHANGES
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`

For every finding, cite the file and exact heading or quoted text. Keep recommendations wiki-only and minimal. If there are no findings in a category, write `None`.
