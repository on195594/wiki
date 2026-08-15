---
title: Generative Agents: Interactive Simulacra of Human Behavior
created: 2026-08-15
updated: 2026-08-15
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2304.03442
arxiv_id: "2304.03442v2"
doi: https://doi.org/10.1145/3586183.3606763
published_at: 2023-08-06
captured_at: 2026-08-15
status: captured
source_quality: primary-paper-full-pdf
---

# Generative Agents: Interactive Simulacra of Human Behavior

## Source metadata

- Authors: Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, Michael S. Bernstein
- Venue: UIST 2023
- PDF reviewed: `https://arxiv.org/pdf/2304.03442`
- Extraction note: full paper reviewed, including architecture, controlled evaluation, ablation, limitations and ethics sections.

## Mechanism captured from the paper

The architecture combines:

1. a natural-language memory stream;
2. retrieval scored by recency, importance and relevance;
3. reflection that synthesizes higher-level inferences and writes them back to memory;
4. hierarchical planning that decomposes plans into progressively finer actions and reacts to new observations.

The reported implementation used equal weights for the three retrieval terms, a prompted importance score, and a source-specific accumulated-importance threshold to trigger reflection.

## Reported evidence

- Twenty-five agents were simulated in the Smallville environment.
- A controlled evaluation with 100 human evaluators compared the full architecture with ablated conditions across self-knowledge, memory, planning, reaction and reflection questions.
- The full architecture ranked above the evaluated ablations on behavioral believability.
- A two-day end-to-end simulation exhibited information diffusion, relationship formation and coordinated activity.

## Limits stated or exposed by the paper

- Evaluation covers a short simulation and believability, not long-term factual reliability or accurate prediction of real people.
- The two-day, 25-agent run cost thousands of dollars in token credits and took multiple days.
- Robustness to prompt hacking, memory hacking and hallucination remained largely unknown.
- Underlying model bias and stereotypes can propagate into agent behavior.
- The authors warn against substituting simulated agents for real human participants and discuss parasocial and misinformation risks.

## Evidence boundary

The source-specific retrieval weights, importance scale and reflection threshold are implementation choices, not universal memory defaults. The paper supports a reusable memory–reflection–planning pipeline for simulated behavior; it does not validate direct promotion into Hermes default memory or autonomous long-term knowledge writes.
