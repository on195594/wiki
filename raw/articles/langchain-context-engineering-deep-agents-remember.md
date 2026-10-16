---
title: "Context Engineering with Deep Agents: How To Remember Without Keeping Everything In Context"
author: Jess Weng
publisher: LangChain
published: 2026-10-14
created: 2026-10-16
updated: 2026-10-16
type: raw-source
status: captured
tags: [agent, llm, context-engineering]
sources: [https://www.langchain.com/blog/context-engineering-deep-agents-remember]
source_url: https://www.langchain.com/blog/context-engineering-deep-agents-remember
extraction_route: direct_webpage_text
source_quality: full
capture_scope: selected-paraphrased-source-note-with-original-excerpts
---

# Context Engineering with Deep Agents: How To Remember Without Keeping Everything In Context

## Provenance and capture scope

- Original: [LangChain article](https://www.langchain.com/blog/context-engineering-deep-agents-remember), Jess Weng, published 2026-10-14. The live page displays the shorter heading “Context Engineering: How Deep Agents Remember”; its extracted document title is retained above.
- Retrieved 2026-10-16 by direct webpage text extraction. The readable original includes the lead, Key Takeaways, five technique sections, code examples and six closing strategies. Publication date and author were visible on the original page, not inferred from retrieval time.
- This file is a selected, paraphrased source note compiled from that original, with explicitly quoted English excerpts. It is not a full-article mirror, verbatim snapshot or generated-summary substitute. `source_quality: full` describes the retrieved input, not the completeness of this note.
- Navigation, related posts, footer, event promotion and installation/model-selection examples are omitted. Images and animations were not inspected; readable captions are not evidence of their full content.
- Source quality: first-party vendor explanation of Deep Agents mechanisms, not an independent evaluation. Linked documentation, implementation versions and source code were not separately verified; no agent run or cost/accuracy experiment was reproduced. Product defaults below describe the article's publication-time account, not current certification or universal recommendations.

## Thesis: prevent entry and manage accumulation

The article separates context engineering into preventing unnecessary information from entering the active window and managing information already accumulated there. Retrieval alone addresses selection, but long runs still collect messages, tool results, notes and stale drafts.

> “Retrieval methods (RAG, or filesystem search) help the agent pull in only what it needs, but that still only solves half the problem.”

Deep Agents applies controls through middleware at points such as agent startup, model calls and tool calls. The reusable distinction is when a control intervenes and which information growth it addresses, not a requirement to adopt this middleware architecture.

## Five techniques described by the source

### 1. Offloading: intercept a single large input

The article says `FilesystemMiddleware` writes a tool result exceeding roughly 20,000 tokens to `/large_tool_results/{tool_call_id}` before it enters the conversation. The model receives the first and last few lines plus the file path, and can page through the original with `read_file` when needed. Oversized user messages use a higher 50,000-token threshold and are saved under `/conversation_history/`.

These are source-specific example paths and publication-time thresholds, not deployment instructions or host filesystem locations.

### 2. Summarization: control cumulative history growth

`SummarizationMiddleware` checks usage before each model call. The article describes an 85%-of-window default trigger: a separate LLM call condenses older messages into a single summary, while the most recent messages remain verbatim. Later compaction cycles incorporate the previous summary; a topic change may also trigger summarization.

The original messages being summarized are written to `/conversation_history/{session_id}.md` for later retrieval. Recoverability comes from retaining those originals and a way to read them, not from treating the summary as lossless.

> Offloading stops the small spikes, while summarization “resets” the overall climb

### 3. Skills: defer task-specific know-how

`SkillsMiddleware` scans skill headers before startup and adds names/descriptions to the system prompt on model calls. The model reads full instructions only when it decides the skill is relevant. This progressive disclosure avoids carrying an infrequently needed report template throughout unrelated research. Actual skill loading and invocation semantics remain host-specific.

### 4. Subagents: keep known noisy work out of the parent window

`SubAgentMiddleware` allows separate prompts and tool sets for subagents. The example researcher consumes a company report in its own context and returns only three developments, rather than raw material. The article suggests that small, well-scoped tasks can often run on cheaper models or in parallel; it does not supply an end-to-end cost or quality evaluation.

A separate context window is not evidence of a security sandbox, process isolation or restricted filesystem access.

### 5. Long-term memory: persist selected information outside a conversation

The source describes memory as Markdown in user-controlled storage: `MemoryMiddleware` loads the file at run start, injects it into model calls, and the agent updates useful information such as formatting preferences. Reusing the same storage can preserve the file across model/provider changes.

File portability does not establish equivalent interpretation by different models, correct memory selection, safe automatic updates or permission to retain private material.

## Six source strategies: selected original excerpts

The following six bullets are quoted from the closing strategies section; they are source recommendations, not independently established guarantees:

> - **Large inputs should be offloaded, not truncated.** Truncation is lossy; offloading keeps it retrievable.
> - **Compaction should be recoverable.** After summarization, the agent can still get back the detail it needs.
> - **Know-how should load on demand.** Instructions for every task in the system prompt cost context on every call.
> - **Noisy work should be isolated.** Subagents with their own context keep the main agent focused.
> - **You should own the memory.** Memory in storage you control survives a model or provider switch.
> - **Defaults should be customizable.** Thresholds that suit one task rarely suit every task.

## Reusable interpretation and limits

**[推论]** Treat offloading and summarization as complementary controls: intercept single-input spikes before entry, then compact older accumulated history before the next model call. Skills defer irrelevant know-how; subagents isolate work expected to be noisy. Prefer existing host capabilities rather than adding a second context manager just to reproduce this vocabulary.

**[推论]** Verify that an evidence pointer resolves to the retained original when recovery matters. A short summary, a path string or re-running a changing tool alone does not prove recovery of the same observation. Retention and retrieval still need authorization and appropriate storage; private history must not be published as Wiki raw material.

The article does not establish universal trigger thresholds, lossless summarization, measured accuracy gains, total cost reductions, reliable self-learning or cross-model behavioral equivalence. Knowledge capture does not authorize product adoption, new dependencies, active Skill changes or runtime configuration.

## Knowledge owner

- [[agent-context-engineering]] holds the incremental distinction between input spikes and cumulative history growth.
- [[hermes-context-engineering-design-priorities]] owns budget ordering and task-level evaluation rather than isolated token savings.
- [[hermes-memory-skills-wiki-boundaries]] owns content placement and retention boundaries; plain files do not collapse memory, skills, knowledge and execution history into one layer.
