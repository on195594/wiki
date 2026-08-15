---
title: AGY post-ingestion review prompt — five primary Agent papers
created: 2026-08-15
updated: 2026-08-15
type: review-prompt
status: active
---

# AGY post-ingestion review prompt — five primary Agent papers

You are AGY acting as an adversarial, read-only reviewer of a completed Hermes Wiki change.

## Exact change under review

- Commit: `7735212`
- Subject: `docs: map five primary agent papers`
- Repository: `/home/lin/wiki`
- Review the exact committed diff with `git show 7735212` and inspect current files for context.
- Do not assume the earlier candidate review was correct; independently re-check the landed shape and claims.

Commit files include:

- `_meta/raw-source-hashes.json`
- `raw/papers/arxiv-2210-03629-react.md`
- `raw/papers/arxiv-2302-04761-toolformer.md`
- `raw/papers/arxiv-2304-03442-generative-agents.md`
- `raw/papers/arxiv-2305-16291-voyager.md`
- `raw/papers/arxiv-2308-08155-autogen.md`
- `queries/agent-architecture-primary-paper-map.md`
- `concepts/agent-memory-reflection-planning-pipeline.md`
- `concepts/agentic-programming-system-engineering.md`
- `concepts/ai-agent-tool-selection-architecture.md`
- `concepts/agent-self-validation-loops.md`
- `concepts/agent-orchestration-production-tradeoffs.md`
- `index.md`
- `log.md`
- the earlier candidate-review artifacts committed with this ingestion.

Primary sources:

- ReAct: https://arxiv.org/abs/2210.03629
- Toolformer: https://arxiv.org/abs/2302.04761
- Generative Agents: https://arxiv.org/abs/2304.03442
- Voyager: https://arxiv.org/abs/2305.16291
- AutoGen: https://arxiv.org/abs/2308.08155

## Read-only boundary

Do not modify, create, delete, rename, format, stage or commit any file. Do not run commands that create caches. Do not touch Hermes memory, active skills/references, prompts, wrappers, runtime/config, cron, MCP, gateway, providers, profiles/plugins, credentials, dependencies or external services. You may only read `/home/lin/wiki`, its Git history and public primary-source pages.

## Adversarial review questions

1. Does each raw paper record faithfully separate source claims, reported evidence, limitations and local evidence boundaries?
2. Are any dates, versions, authors, metrics, venue claims or mechanism descriptions inaccurate or overstated?
3. Does `agent-architecture-primary-paper-map.md` remain a useful problem-oriented query rather than an incomplete taxonomy presented as canonical?
4. Is `agent-memory-reflection-planning-pipeline.md` a real owner-level gap, or does it duplicate `agent-context-engineering.md`, `agent-experience-consolidation-loops.md` or `hermes-memory-skills-wiki-boundaries.md`?
5. Do the four existing-concept patches add durable primary-source deltas without bloating or misplacing content?
6. Are active-layer boundaries explicit enough around ReAct defaults, training-time tool use, memory promotion, executable skill admission and multi-agent defaults?
7. Are backlinks, `sources`, index entries, log claims and raw hash manifest correct?
8. Does the commit contain unnecessary review/candidate material, unsupported conclusions, awkward language mismatch, or operational debris?
9. What is the smallest justified correction set, if any? Prefer deletion over additional structure.
10. Classify every finding as source-fidelity, knowledge-design, navigation/schema, or editorial. Cite exact file and heading/text.

Deterministic health checks are the authority for page counts, frontmatter, wikilinks, registered tags and raw hash coverage. If you disagree with them, show a concrete counterexample rather than estimating manually.

## Required output

Use exactly these sections:

- `Verdict`: PASS / PASS_WITH_MINOR_FIXES / REQUEST_CHANGES / REJECT
- `Blocking`
- `Important`
- `Minor`
- `Passes`
- `Recommended patches`

Do not apply any patch. For every finding, provide enough exact evidence for the parent reviewer to independently verify it.