---
title: AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation
created: 2026-08-15
updated: 2026-08-15
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2308.08155
arxiv_id: "2308.08155v2"
published_at: 2023-10-03
captured_at: 2026-08-15
status: captured
source_quality: primary-paper-full-pdf
---

# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

## Source metadata

- Authors: Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun Zhang, Jiale Liu, Ahmed Awadallah, Ryen W. White, Doug Burger, Chi Wang
- PDF reviewed: `https://arxiv.org/pdf/2308.08155`
- Extraction note: full paper reviewed, including framework abstractions, application evaluations, discussion and ethics statement.

## Mechanism captured from the paper

AutoGen introduces customizable conversable agents and conversation programming. An agent can combine LLMs, humans, tools and code execution; interaction behavior can be programmed in natural language and code, including static, dynamic and group-chat patterns.

## Reported evidence

- The paper demonstrates applications across mathematics, retrieval-augmented question answering and code generation, ALFWorld, optimization-oriented coding and group conversation.
- In the paper's ALFWorld setup, adding a grounding agent produced an average `15%` gain over its two-agent variant.
- In a 100-task safe/unsafe coding dataset created for the paper, separating Writer and Safeguard roles improved unsafe-code identification F1 by `8%` with GPT-4 and `35%` with GPT-3.5-turbo.
- The authors report reduced workflow code and manual interaction in selected application case studies.

## Limits stated or exposed by the paper

- The work is described as early experimental research, not a unified proof that multi-agent designs dominate single-agent systems.
- Optimal topology, conversation pattern, efficiency and automation-versus-human-control balance remain open questions.
- More agents and degrees of freedom add safety, accountability and traceability challenges.
- External code execution and package installation can create harmful side effects without safeguards.
- Results mix benchmarks, pilots and application demonstrations rather than one uniform evaluation protocol.

## Evidence boundary

AutoGen supports conversation programming as one reusable orchestration abstraction. It does not justify making multi-agent execution the default, treating role separation as an independent security boundary, or allowing unapproved code and tool side effects.
