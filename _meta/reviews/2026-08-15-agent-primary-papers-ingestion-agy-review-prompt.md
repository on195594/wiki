---
title: AGY adversarial review prompt — five primary Agent papers
created: 2026-08-15
updated: 2026-08-15
type: review-prompt
status: active
---

# AGY adversarial review prompt — five primary Agent papers

You are AGY acting as an adversarial, read-only reviewer of a proposed Hermes Wiki ingestion.

## Read-only boundary

Do not modify, create, delete, rename, format, commit or stage any file. Do not run tests or commands that create caches. Do not touch Hermes memory, skills, prompts, wrappers, runtime/config, cron, MCP, gateway, providers, profiles/plugins, credentials, dependencies or external services. You may only read the supplied candidate directory and `/home/lin/wiki`.

## Candidate under review

Candidate root:

`/tmp/agentic-five-papers-wiki-ingestion/candidate`

Read all eight candidate files:

- `raw/papers/arxiv-2210-03629-react.md`
- `raw/papers/arxiv-2302-04761-toolformer.md`
- `raw/papers/arxiv-2304-03442-generative-agents.md`
- `raw/papers/arxiv-2305-16291-voyager.md`
- `raw/papers/arxiv-2308-08155-autogen.md`
- `queries/agent-architecture-primary-paper-map.md`
- `concepts/agent-memory-reflection-planning-pipeline.md`
- `proposal.md`

Inspect these live Wiki pages for ownership and duplication:

- `/home/lin/wiki/SCHEMA.md`
- `/home/lin/wiki/concepts/agentic-programming-system-engineering.md`
- `/home/lin/wiki/concepts/ai-agent-tool-selection-architecture.md`
- `/home/lin/wiki/concepts/agent-self-validation-loops.md`
- `/home/lin/wiki/concepts/stateful-agent-environments-and-grounded-verification.md`
- `/home/lin/wiki/concepts/agent-orchestration-production-tradeoffs.md`
- `/home/lin/wiki/concepts/agent-context-engineering.md`
- `/home/lin/wiki/concepts/agent-experience-consolidation-loops.md`
- `/home/lin/wiki/concepts/hermes-memory-skills-wiki-boundaries.md`
- `/home/lin/wiki/index.md`

Primary sources:

- ReAct: https://arxiv.org/abs/2210.03629
- Toolformer: https://arxiv.org/abs/2302.04761
- Generative Agents: https://arxiv.org/abs/2304.03442
- Voyager: https://arxiv.org/abs/2305.16291
- AutoGen: https://arxiv.org/abs/2308.08155

## Review stance

Assume the candidate may be overbuilt, duplicative, historically interesting but operationally irrelevant, or too eager to map paper mechanisms into Hermes. Challenge it. Prefer dropping files or patches when the durable retrieval value is weak. Do not reward completeness for its own sake.

Check:

1. primary-source fidelity and whether any metric/mechanism is overstated;
2. source fact versus Hermes-local inference separation;
3. whether five raw records plus one query plus one concept is the smallest durable shape;
4. whether the new memory–reflection–planning concept duplicates existing pages;
5. whether each of four proposed existing-page patches has a real owner-level gap;
6. whether the query is a useful problem-oriented map rather than an incomplete taxonomy disguised as one;
7. active-layer boundaries, especially automatic memory, skill promotion, ReAct defaults and multi-agent defaults;
8. frontmatter, raw/formal routing, wikilinks and likely health-check failures;
9. whether index/log/hash-manifest plans are sufficient;
10. exact recommended patches, including deletions from the proposal.

## Required output

Use exactly these sections:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / REQUEST_CHANGES / REJECT
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`

For every finding, cite the candidate or live file path and the exact heading or text. Distinguish source-fidelity defects from design preferences. If recommending fewer files or patches, state the smallest acceptable landing shape.
