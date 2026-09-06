---
title: Capable language models can outgrow the benefits of collaboration
created: 2026-09-04
updated: 2026-09-04
type: raw-source
tags: [agent, multi-agent, orchestration, evaluation, research]
author: Yubin Kim et al.
published: 2026-07-24
source: Nature Machine Intelligence
source_url: https://www.nature.com/articles/s42256-026-01268-y
doi: https://doi.org/10.1038/s42256-026-01268-y
captured: 2026-09-04
status: captured
extraction: Structured capture from the public article page and the completed Hermes URL-summary run; not a byte-for-byte copy of the full paper.
local_summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260904-164505-Capable-language-models-can-outgrow-the-benefits-of-collaboration-1722218-662728120-summary.md
---

# Capable language models can outgrow the benefits of collaboration

## Provenance

- Public article metadata checked against the publisher page: published 24 July 2026, Nature Machine Intelligence 8, 1157–1172.
- The study covers 260 configurations, six benchmarks, five architectures, and three LLM families under matched prompts, tools, and compute budgets.
- The publisher page links the preprint at https://arxiv.org/abs/2512.08296. The completed summary also records the experiment code at https://github.com/ybkim95/agent-scaling and archive at https://doi.org/10.5281/zenodo.20388843.
- This file is a structured evidence capture, not the full paper text. Numerical claims require rechecking against the paper before reuse as thresholds.

## Reusable claims

- Multi-agent collaboration is not generally better than a single agent.
- Benefits depend more on task decomposability and genuine parallelism than on nominal task complexity.
- Strong single-agent baselines raise the burden of proof for adding coordination.
- Communication, context compression, extra inference, merge work and correlated errors can erase collaboration gains.
- [推论] Agreement among similar agents is not independent evidence when their errors are correlated.
- The study's thresholds, benchmark deltas and coordination multipliers are source-specific observations, not Hermes defaults.

## Hermes implication [推论]

Use the single-agent baseline first. Add fan-out only for independently verifiable subtasks with an explicit merge and verification contract. Keep parent-level evidence review. Do not create a new default multi-agent router, pool, team or global gate from this paper alone.

## Evidence limitations

The study compares fixed configurations across six benchmarks and reports weak cross-domain predictive power. Results are bounded by the tested models, prompts, tasks and budgets; they should guide local comparison experiments, not serve as universal scaling laws.
