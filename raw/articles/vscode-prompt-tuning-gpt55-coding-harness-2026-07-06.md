---
title: How Prompt Tuning Improved GPT-5.5 in VS Code
created: 2026-07-07
updated: 2026-07-07
type: raw_source
tags: [ai-coding, agent, prompt-tuning, vscode, coding-harness, evaluation]
source_url: https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers
source_title: How Prompt Tuning Improved GPT-5.5 in VS Code
author: VS Code Team
published: 2026-07-06
captured: 2026-07-07
source_quality: full
extraction_note: web_extract fallback after deterministic HTML extraction returned empty; extracted core article body, experiment setup, prompt excerpts, and scorecard metrics.
status: captured
---

# How Prompt Tuning Improved GPT-5.5 in VS Code

## Source

- Source URL: https://code.visualstudio.com/blogs/2026/07/06/optimizing-vscode-coding-harness-model-providers
- Title: How Prompt Tuning Improved GPT-5.5 in VS Code
- Author: VS Code Team
- Published: 2026-07-06
- Captured: 2026-07-07
- Extraction quality: full article body from `web_extract` after deterministic HTML/JSON-LD extraction returned empty.
- Local summary artifact: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260707-200524-code.visualstudio.com-blogs-2026-07-06-optimizing-vscode-coding-harness-model-pr-2513611-587550680-summary.md`

## Abstract

VS Code Team describes a two-week production A/B test, run with OpenAI, that tuned the GPT-5.5 system prompt inside the VS Code coding harness. The tested hypothesis was that a coding agent should spend less effort on broad exploration and move earlier through evidence, action, and validation. The winning treatment reorganized the prompt into explicit `Before_the_first_edit` and `After_the_first_edit` sections and became the default `GPT-5.5` system prompt in VS Code.

## Extracted source notes

### Hypothesis

The VS Code team observed that GPT-5.5 could spend substantial tokens searching, rereading, and comparing nearby paths before making a useful edit. They proposed a testable harness change: make the agent start from a concrete anchor, gather only enough local context to state a falsifiable hypothesis, perform a grounded edit, and validate immediately after the first substantive edit.

### Treatments

- Control: `PRPT_CTRL`, the current default prompt.
- Treatment A: `PRPT_SRCH`, a compact `<economical_search_and_edit>` reminder.
- Treatment B: `PRPT_LRG`, larger prompt sections covering the full edit-and-validate loop.

Treatment A told the agent to start from a concrete anchor, gather only enough nearby context, prefer targeted search over broad exploration, act once a cheap discriminating check is known, and avoid rereading unchanged context.

Treatment B added explicit `Before_the_first_edit` and `After_the_first_edit` sections. Before the first edit, the model should find a concrete anchor, gather enough evidence for one falsifiable local hypothesis and one cheap check, then make a small grounded edit. After the first edit, it should validate with the cheapest behavior-scoped or failing check, then a narrow test, then a narrow compile/lint/typecheck where available.

### Scorecard

The two-week scorecard compared treatment groups with the control group across quality, latency, token efficiency, and tool calls.

Key Treatment B results:

- p50 Time to First Edit: -5.68%, 3.9 seconds faster, p=2e-5.
- p95 Time to First Edit: -9.30%, 38.8 seconds faster, p=1e-10.
- p95 total tokens: -7.64%, 0.5M fewer tokens, p=0.0003.
- Average tool calls: -8.54%, 2.04 fewer calls, p=1e-12.
- 10-minute survival rate: -0.44%, p=0.0493, a small negative quality movement.
- Commit survival rate: +0.68%, p=0.1533, not statistically significant.

The team judged Treatment B to have the strongest overall profile: significant latency and efficiency gains, fewer tool calls, and mostly stable quality guardrails. They shipped Treatment B as the default GPT-5.5 system prompt.

## Local reading boundary

This is strong evidence for a specific VS Code + GPT-5.5 coding harness, not a universal proof that all coding agents should always edit earlier. For Hermes, the reusable principle is a bounded control pattern: when a coding task has a concrete anchor and cheap validation path, reduce broad exploration before the first edit and validate immediately after the first substantive edit. It supports an optional `coding-agent-workflow` reference, but is not evidence to change Hermes runtime, cron, MCP, provider routing, memory, or active skill defaults.

## Links

- Concept extraction: [[first-edit-economy-for-coding-agents]]
- Related: [[loop-engineering-hermes-agent-workflow]]
- Related: [[agent-self-validation-loops]]
- Related: [[agent-context-engineering]]
- Related: [[codex-agent-workflow-layering]]
