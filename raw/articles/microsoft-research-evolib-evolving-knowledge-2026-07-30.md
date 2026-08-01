---
title: EvoLib - Turning experience into evolving knowledge
author: Weijia Xu, Alessandro Sordoni, Zelalem Gero, Michel Galley, Eric Yuan, Jianfeng Gao
created: 2026-08-01
updated: 2026-08-01
type: raw-source
status: captured
source: Microsoft Research
source_url: https://www.microsoft.com/en-us/research/blog/evolib-turning-experience-into-evolving-knowledge/
published: 2026-07-30T09:00:00-07:00
captured: 2026-08-01
extraction: Direct deterministic fetch returned HTTP 403; web_extract recovered the full article prose, and browser DOM verified the displayed publication date and author list; navigation, podcast promotion, author cards, social links and footer boilerplate were omitted
tags: [agent, memory, research, workflow, evaluation]
---

# EvoLib - Turning experience into evolving knowledge

## Provenance

- Source URL: https://www.microsoft.com/en-us/research/blog/evolib-turning-experience-into-evolving-knowledge/
- Source: Microsoft Research
- Authors: Weijia Xu, Alessandro Sordoni, Zelalem Gero, Michel Galley, Eric Yuan, Jianfeng Gao
- Published: 2026-07-30T09:00:00-07:00
- Captured: 2026-08-01
- Local summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260801-161551-EvoLib-Turning-experience-into-evolving-knowledge-Microsoft-Research-2824354-379589320-summary.md`
- Extraction note: direct deterministic fetch returned HTTP 403; `web_extract` recovered the full article prose. The rendered Microsoft Research page was checked to verify the publication date and displayed author list. Navigation, an unrelated podcast promotion, author cards, social links and footer boilerplate were omitted.
- Source quality: official Microsoft Research blog with full article prose.
- Limitation: this page is a research-blog overview, not the complete paper. It does not expose the full prompts, mathematical formulation, benchmark numbers, hyperparameters, knowledge-capacity or pruning policy, concurrent-update cost, conflict policy, or production operating evidence.

## Why this source matters

This source extends [[agent-experience-consolidation-loops]] beyond layer routing. It distinguishes a growing archive of raw experiences from a knowledge library that extracts reusable skills and reflective insights, consolidates similar knowledge, and reweights knowledge units according to immediate and downstream utility.

It does not establish that EvoLib should be adopted as a Hermes runtime component. Its reusable value is the knowledge-evolution lifecycle and its evaluation questions.

## Source-backed capture

The following is a structured capture of the extracted article claims rather than a verbatim archive. The provenance and limitations above define its evidence boundary.

## At a glance

- Self-supervised. EvoLib enables large language models to learn from their own experience during inference, without requiring ground-truth labels or external feedback.
- From experience to knowledge. EvoLib transforms past attempts into reusable skills and reflective insights that can be applied to future tasks.
- Knowledge that evolves. Useful skills and insights are continually refined, consolidated, and reweighted, turning instance-specific observations into increasingly general knowledge over time.
- Learning that transfers across tasks. By turning experience into reusable knowledge, EvoLib helps AI models learn from past successes and failures and evolve the knowledge that has the highest potential on improving future performance.
- Built for today’s AI models. As EvoLib does not require model updates, it can be applied to black-box language models and AI systems deployed through APIs.

Memory has become an important AI agent capability: the ability to store and retrieve past experiences. But memory alone is not learning. A collection of past conversations, reasoning traces, or action histories can quickly grow into a vast archive of experiences, making it difficult to identify the most relevant knowledge for a new task—let alone refine and evolve this knowledge to improve performance over time.

Humans do not remember every detail of past experiences. Instead, they retain strategies that work, mistakes to avoid, and skills that transfer across situations. Over time, these lessons are refined into increasingly general and reusable knowledge.

In the paper *Test-Time Learning with an Evolving Library*, the authors introduce EvoLib, a framework that transforms raw experience into an evolving library of knowledge. Rather than treating memory as a growing archive, EvoLib extracts reusable knowledge and continually refines it as new experiences arrive. The stated goal is to make skills more general, insights more accurate, and downstream performance improve without updating the underlying model.

## How EvoLib works

A knowledge unit can be either a reusable skill distilled from a successful solution or a reflective insight learned from mistakes. EvoLib continually refines, consolidates and reweights existing knowledge as new experiences arrive.

- **Consolidation.** After extracting new knowledge from recent experience, EvoLib retrieves similar knowledge from the library and attempts to consolidate it with the new knowledge into a more general and reusable unit. This is intended to move knowledge beyond individual experiences and make it applicable across tasks.
- **Weighting mechanism.** EvoLib updates the importance of each knowledge unit based not only on immediate utility for the current task, but also on how much it contributes to generating useful knowledge on future tasks. Knowledge with greater claimed long-term impact becomes more prominent in the library.

## Key results reported by the authors

The authors evaluated EvoLib on three task types:

- mathematical reasoning;
- code generation under efficiency constraints;
- long-horizon environment exploration and interaction.

The blog reports that EvoLib outperformed retrieval-based memory approaches and other abstract memory mechanisms across these tasks while using tokens more efficiently. It also reports that EvoLib converted additional test-time compute into performance gains more effectively across most of the tested compute range.

The blog does not include the underlying numerical tables or enough experimental detail to independently assess effect size, statistical uncertainty, benchmark sensitivity, or operating cost. Those claims should therefore remain attributed to the authors and scoped to the reported experiments.

## Robustness to random task order

The authors also tested the same heterogeneous tasks under different encounter orders. The blog reports that EvoLib maintained improvement over existing memory-based learning approaches and stable performance across different orderings. The authors interpret this as evidence that EvoLib can learn from interleaved task streams without relying on a structured curriculum.

This supports testing knowledge systems against mixed task order rather than only a fixed curriculum, but it does not by itself establish production robustness.

## Local knowledge-layer interpretation

[推论] For Hermes, the useful abstraction is:

```text
session/project evidence
→ extract candidate skill or reflective insight
→ retrieve similar durable knowledge
→ consolidate, keep separate, supersede, or reject
→ evaluate immediate utility and downstream contribution
→ reuse in future tasks
→ revalidate, downweight, or retire
```

[推论] This lifecycle belongs first in wiki governance and project-local evidence handling. It does not authorize automatic writes to memory or skills, a consolidation cron, curator changes, a new storage backend, or runtime promotion.

## Related

- [[agent-experience-consolidation-loops]]
- [[hermes-memory-skills-wiki-boundaries]]
- [[agent-closed-loop-learning-from-corrections-to-rules]]
- [[progressive-knowledge-system-growth]]
