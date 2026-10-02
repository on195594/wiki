---
title: How to Build a Model Router in the Harness
author: [Sydney Runkle, Eugene Yurtsev]
source: LangChain Blog
source_url: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
published: 2026-10-01
captured: 2026-10-02
type: raw-source
status: captured
tags: [agent, harness, optimization, evaluation]
---

# How to Build a Model Router in the Harness

## Source and capture scope

- Authors: Sydney Runkle and Eugene Yurtsev; publisher: LangChain; published 2026-10-01.
- Original: https://www.langchain.com/blog/how-to-build-a-model-router-in-the-harness
- Captured 2026-10-02 by direct web extraction; the extracted file contained the complete readable page. The initially truncated display was supplemented by reading the omitted “What's next” section.
- Quality: full readable prose; chart images were represented by alt text, not independently inspected. The numerical results below are stated in the prose.
- This is a selected, paraphrased source note, not a full-article mirror, academic paper, independent replication or verified snapshot of the linked code and documentation. Linked benchmarks, middleware and provider guides were not independently assessed.
- Evidence limits: first-party Open SWE engineering report from the vendor offering the framework and observability products; outcomes and costs are author-reported, with sparse user feedback and incomplete coverage of code quality. The authors call the router a proof of concept.

## Captured mechanism

- LangChain analyzed one week of internal Open SWE interactive threads using traces, task labels, cost and invocation count. Cost and turns were approximate complexity signals; repeated invocations can also indicate that a model struggled.
- Three model tiers were chosen along a benchmark intelligence/cost frontier, with task-specific criteria derived from traffic analysis and provider guidance. The classifier chooses the least expensive tier likely to complete the request.
- Middleware selects a model on the first human message and retains it for the whole thread. The authors argue that the harness normally has task context absent from a generic gateway.
- The original classifier used an LLM with structured output; the later Jev classifier reportedly made classification almost 50 times faster. This is not an independently reproduced latency benchmark.

## Author-reported experiments

- First test: 973 threads, 50/50 router versus always GPT-6 Astra. Merged PRs per thread were 29.2% versus 27.3% (p = 0.49); PR opening rates were 38.9% versus 39.6% (p = 0.82).
- Median LLM cost per thread was $0.94 versus $2.61, reported as a 64% reduction; mean cost fell 42% and P90 cost fell 37%. These are thread-level LLM-cost comparisons against the strongest-model baseline, not a measured reduction in total operating cost.
- Routed threads used balanced / fast / performance tiers in proportions 56% / 34% / 10%. This is a traffic distribution, not a budget recommendation.
- Second test: 50/50 router versus always the fast model, terminated within one day after engineers reported low output quality and disruption to productivity. The authors explicitly say it ended before statistically meaningful results were available.

## Implementation limits and future work

- First-message selection does not adapt when a question becomes a harder task. Subagents choose models independently and are not controlled by this router.
- Mid-thread re-routing, controlled coding benchmarks and mining frustration signals are proposed future work, not completed verification.
- Switching models requires re-reading context and may lose prompt-cache benefits. The authors note that a short TTL, such as five minutes, can already expire between asynchronous human replies; this is a conditional example, not a provider-independent cache policy.
- The three named tiers are a September 2026 case configuration, not current recommendations: GLM-5.3-Flash (xhigh), GPT-5.6 Sol (medium), GPT-6 Astra (low).

## Synthesis destinations

- [[agent-resource-optimization]] owns the reusable task-to-model matching interpretation and its limits.
- [[production-agent-evaluation-baselines]] owns the short metric-interpretation caution. Non-significant differences do not establish equivalence; the reported proxies do not cover all quality dimensions.
