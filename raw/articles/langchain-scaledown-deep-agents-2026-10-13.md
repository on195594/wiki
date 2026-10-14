---
title: Building Long-Running Agents with ScaleDown and Deep Agents
author: Sydney Runkle; Srimanth Tangedipalli; Neal Patel
publisher: LangChain
published: 2026-10-13
created: 2026-10-14
updated: 2026-10-14
type: raw-source
status: captured
tags: [agent, llm, context-engineering]
sources: [https://www.langchain.com/blog/building-long-running-agents-with-scaledown-and-deep-agents]
source_url: https://www.langchain.com/blog/building-long-running-agents-with-scaledown-and-deep-agents
extraction_route: direct_html
source_quality: full
capture_scope: selected-paraphrased-source-note
---

# Building Long-Running Agents with ScaleDown and Deep Agents

## Provenance and capture scope

- Original: [LangChain article](https://www.langchain.com/blog/building-long-running-agents-with-scaledown-and-deep-agents), published 2026-10-13; Sydney Runkle, Srimanth Tangedipalli and Neal Patel.
- Retrieved 2026-10-14 by direct webpage text extraction. The readable original body covered Key Takeaways through Get started, including the four model descriptions, middleware sections and code examples; navigation, related posts and footer were excluded. Diagram captions were readable; diagram pixels were not inspected.
- This file is a selected, paraphrased source note compiled from that original body, not a full-article mirror, verbatim snapshot or generated-summary substitute. `source_quality: full` describes the retrieved input, not this note's completeness.
- The article describes a vendor integration and quotes ScaleDown's own benchmarks. Linked documentation and trace results were not separately verified, and no code, API call, benchmark or model-quality evaluation was reproduced. Product capabilities and offers below are claims as of the article's publication, not current certification.

## Thesis and responsibility split

The article proposes moving repeated, narrow context-management operations to ScaleDown's task-specific constrained decoding models (CDMs), while retaining a general-purpose model for planning, coding and open-ended replies. The integration is `langchain-scaledown` for LangChain and Deep Agents; it ships three middleware components. Classification-based drift detection is illustrated separately as custom middleware, not a fourth prebuilt component.

## Four model capabilities reported by the article

1. **Summarize** produces short summaries of long input.
2. **Compress** selects context relevant to a supplied question.
3. **Extract** identifies described fields, returning confidence scores and source positions.
4. **Classify** scores predefined labels and can return a one-sentence explanation.

All four are described as accepting up to 1M input tokens. Images and scanned PDFs are explicitly mentioned for Extract, Summarize and Classify; the article does not make the same explicit multimodal claim for Compress. Output constraints and source positions do not establish semantic correctness.

## Four integration patterns

### 1. Summarize older history, preserve recent messages

`ScaledownSummarizationMiddleware` replaces Deep Agents' built-in summarization middleware. Its example sets `trigger=("fraction", 0.8)` and `keep=("fraction", 0.1)`: an 80% context-window trigger and a recent-message budget of 10% of the window, not 10% of message count. The default summary sections are intent, summary, artifacts and next steps. The agent's own model continues planning and generation. The article says a failed summary call leaves history unchanged and execution continues; it does not establish that the next main-model call will fit its context window.

### 2. Query-directed tool-result compression with a full-output escape path

`ScaledownToolCompressionMiddleware` exposes an optional `compression_query` in the model-facing tool schema. Middleware removes this parameter before calling the underlying tool, then compresses its output against the query. The tool implementation need not change; MCP tools are included in the stated applicability.

The returned output identifies itself as compressed, names the query, reports before/after character counts and tells the model to call again without `compression_query` for the full result. The article links one trace reporting nearly 90% reduction; a separate illustrative notice uses 18,402 → 3,110 characters. These are not interchangeable measurements or evidence of retained task correctness.

### 3. Extract user-supplied fields into agent state

`ScaledownExtractionMiddleware` reads user messages, not assistant replies, before the first model call of a run. Extracted fields are saved under `scaledown_extraction`; tools access its `fields`. Label-defined fields can use Classify. With a checkpointer, extraction re-runs on later turns as details are added.

The support-ticket example identifies order `A-1042`, error `ERR_PAYMENT_DECLINED` and issue type `billing`; an unmentioned email remains `None`. The example uses `context_chars=0` to omit evidence snippets. Reading only user input narrows provenance but does not prove the user's statement, ownership of an order, validity of an email or authorization to create a ticket.

### 4. Classify loops and drift in custom middleware

The custom `after_model` example posts the message history to Classify with labels `progressing`, `looping` and `drifting`. It stops when the top label is not `progressing` and that label's score is greater than `0.8`, returning the supplied reasoning. The article also suggests a gentler policy: nudge first, stop on recurrence. Neither policy is demonstrated as calibrated for an arbitrary workload.

Source-code inspection boundary: the shown `requests.post(...).json()` call has no explicit timeout, HTTP status check or response-shape validation. This is a demonstration, not a complete production failure policy; the source does not establish false-stop rates, privacy suitability or reliable behavior under provider failure.

## Vendor performance claims: preserve separate scopes

- Broad claim: ScaleDown reports narrow-task models as 200x faster and 467x cheaper than frontier models.
- [Provider benchmark link](https://docs.scaledown.ai/benchmarks/providers), with [methodology link](https://docs.scaledown.ai/benchmarks/methodology): the article compares against the average of GPT-5.5, GPT-5.4 Mini and GPT-5.4 Nano on public datasets. It reports Summarize as 41x cheaper and 2.7x faster, Compress as 138x cheaper and 1.8x faster, and higher accuracy for both.
- The broad claim and per-task results have different stated scopes. They are vendor reports, not independently reproduced results or end-to-end agent savings. They do not establish accuracy on Chinese tasks, preservation of safety constraints or classifier-score calibration.

## Publication-time product setup

The article's installation example uses `uv pip install -U langchain-scaledown` and the `SCALEDOWN_API_KEY` environment variable; it advertises 50M free tokens for new accounts.

It also reports LangSmith LLM Gateway support at `/scaledown`: an administrator stores the ScaleDown provider key in workspace secrets, clients use `SCALEDOWN_BASE_URL=https://gateway.smith.langchain.com/scaledown` and authenticate with their LangSmith key. Calls are described as traced and subject to shared spend/rate limits. These details require current official-document and data-handling-policy checks before adoption; no installation or dependency choice is implied here.

## Reusable interpretation and limits

**[推论]** The useful pattern is bounded context processing with explicit input provenance, visible lossy transformation and a recovery path—not adopting a particular vendor. Prefer existing deterministic extraction or filtering when it already satisfies the task; only compare semantic models where semantic judgment is actually needed.

**[推论]** Compression should preserve an accessible original or stable evidence pointer. Re-running a tool is a recovery method, not a guarantee of the same observation: changing pages and side-effectful tools may not be safely replayable. Evaluation should include task correctness, omitted constraints, rereads/retries, total latency/cost and false-positive stopping. Sensitive histories or identifiers require an authorized data-processing boundary before being sent to another provider.

## Knowledge owner

- [[agent-context-engineering]] holds the reusable context-processing mechanism.
- [[hermes-context-engineering-design-priorities]] owns budget/ranking/compression order and end-to-end evaluation boundaries.
- [[deterministic-analytics-llm-reasoning-boundary]] owns deterministic-versus-semantic task selection and probability-quality limits.
- [[agentic-programming-system-engineering]] owns behavioral-drift governance; a probabilistic label does not replace hard permission, iteration or resource limits.
