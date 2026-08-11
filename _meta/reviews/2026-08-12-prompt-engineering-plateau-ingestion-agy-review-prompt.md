# AGY read-only review prompt

You are AGY acting as an independent reviewer. Review the current uncommitted Hermes Wiki ingestion in `/home/lin/wiki`.

## Boundary

- Read-only review only. Do not edit, create, delete, rename, format, commit, stage, or restore any file.
- Do not modify memory, active skills/references, prompts, wrappers, runtime/config, cron, MCP, gateway, profiles/plugins, credentials, dependencies, or external services.
- Treat the article as external practitioner evidence, not authorization to change active Hermes behavior.
- Base findings on the exact live files and current uncommitted diff. Cite paths and line numbers where practical.

## Files under review

- `raw/articles/medium-kritnandan-prompt-engineering-ai-product-2026-08-09.md`
- `concepts/production-ai-agent-evaluation-framework.md`
- `index.md`
- `log.md`
- `_meta/raw-source-hashes.json`

## Adjacent owner pages to compare

- `concepts/typed-ai-agent-boundaries.md`
- `concepts/agent-failure-closed-loop-evaluation.md`
- `concepts/agent-self-validation-loops.md`
- `concepts/production-agent-evaluation-baselines.md`
- `concepts/deterministic-analytics-llm-reasoning-boundary.md`

## Review questions

1. Does the raw page preserve source provenance, publication/capture dates, extraction route, useful article content and explicit limitations without presenting source-specific anecdotes as validated benchmarks?
2. Is updating `production-ai-agent-evaluation-framework` the smallest correct durable unit, or does the change duplicate/misplace material owned by adjacent pages?
3. Are source facts, author interpretation and Hermes-local implications separated correctly?
4. Are the 100-input comparison, three-point stopping heuristic, 20–50-case Eval set and three-attempt retry ceiling correctly kept as source-specific values rather than Hermes defaults?
5. Does the concept preserve the critical boundary that Schema-valid output is not semantic correctness?
6. Are wikilinks, frontmatter, index wording, raw hash entry and log entry coherent?
7. Is there any over-promotion into active skills, runtime, wrapper, memory, cron, MCP, gateway or default workflow behavior?
8. Identify only evidence-backed fixes. For each finding, explain why it matters and give the smallest recommended patch. Do not recommend a new concept, project, evaluator, monitor or active workflow unless the current files demonstrate a concrete gap that cannot be handled by a bounded edit.

## Required output

Use exactly these sections:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / REQUEST_CHANGES
- `Blocking`: numbered findings or `None`
- `Important`: numbered findings or `None`
- `Minor`: numbered findings or `None`
- `Passes`: concise list of what is correct
- `Recommended patches`: smallest exact changes, or `None`
