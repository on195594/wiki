---
title: ReAct: Synergizing Reasoning and Acting in Language Models
created: 2026-08-15
updated: 2026-08-15
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2210.03629
arxiv_id: "2210.03629v3"
published_at: 2023-03-10
captured_at: 2026-08-15
status: captured
source_quality: primary-paper-full-pdf
---

# ReAct: Synergizing Reasoning and Acting in Language Models

## Source metadata

- Authors: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
- Venue: ICLR 2023
- PDF reviewed: `https://arxiv.org/pdf/2210.03629`
- Extraction note: full arXiv PDF text reviewed; equations, tables, error analysis and discussion were checked rather than relying on the abstract alone.

## Mechanism captured from the paper

ReAct expands the task action space with language actions and interleaves `Thought`, task-specific `Action`, and environment `Observation`. Reasoning maintains and adjusts plans; external actions retrieve information or change the environment; observations become new context for later decisions.

## Reported evidence

- Knowledge tasks: HotpotQA and FEVER, compared with Standard, CoT, CoT-SC and Act prompting.
- Interactive tasks: ALFWorld and WebShop.
- Table 1 shows that ReAct is not uniformly better than CoT: on HotpotQA, ReAct EM is `27.4` versus CoT `29.4`; on FEVER, ReAct accuracy is `60.9` versus CoT `56.3`. Hybrid fallback variants perform better on parts of these tasks.
- Paper-reported interactive-task gains include an absolute success-rate improvement over prior methods on ALFWorld and WebShop in the evaluated setups.
- Error analysis distinguishes reasoning errors, search-result failures, hallucinations and label ambiguity.

## Limits stated or exposed by the paper

- More reasoning examples and larger action spaces can exceed in-context limits.
- ReAct can loop, pursue a wrong subgoal, or fail because search returns empty or irrelevant evidence.
- External interaction reduces some unsupported internal reasoning but introduces environment and retrieval failure paths.
- Main prompting experiments depend on PaLM models that were not publicly available.

## Evidence boundary

This paper supports ReAct as a selectable reasoning–action–observation control pattern. It does not establish that every task should expose chain-of-thought traces, use external tools, or prefer ReAct over simpler prompting and deterministic workflows.
