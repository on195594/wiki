---
title: How We Built LangChain's Paid Media Agent
author: [Amal Irgashev, Danny Lambert, Jan Gomez]
source: LangChain Blog
source_url: https://www.langchain.com/blog/paid-media-agent
published: 2026-09-13
captured: 2026-09-15
type: raw-source
status: captured
tags: [agent, context-engineering, multi-agent, orchestration, workflow, governance]
extraction: structured capture from the complete public article body; local Chinese summary at ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260915-111744-How-We-Built-LangChain’s-Paid-Media-Agent-349075-842889800-summary.md
---

# How We Built LangChain's Paid Media Agent

## Source

- URL: https://www.langchain.com/blog/paid-media-agent
- Authors: Amal Irgashev, Danny Lambert, Jan Gomez
- Published: 2026-09-13
- Captured: 2026-09-15
- Extraction route: complete public-page extraction; this Wiki note is a structured capture rather than a verbatim mirror
- Source quality: full main article available at capture time
- Local Chinese summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260915-111744-How-We-Built-LangChain’s-Paid-Media-Agent-349075-842889800-summary.md`
- Limitation: this is a LangChain vendor/practitioner report. Business outcomes, latency, cost and token figures are self-reported and were not independently reproduced for Hermes. Product-specific choices such as Deep Agents, LangSmith Sandbox and LangSmith Deployment are examples, not local adoption decisions.

## Problem and reported outcome

LangChain wanted a small marketing team to operate five paid-media channels while reconciling incompatible advertising schemas, campaign settings and downstream warehouse outcomes. The resulting Slack-based agent creates weekly summaries and PDFs, answers follow-up questions and proposes campaign changes for human approval.

The authors report:

- paid media grew from 0% to 20% of marketing pipeline in six months;
- qualified-lead cost fell 30% from June to August while monthly spend rose about 60%;
- LinkedIn qualified-lead cost was 40% below the January baseline;
- bringing analysis and reporting in-house saved about USD 5,000 per month;
- an early reporting workflow became about 40 times cheaper and 13 times faster after deterministic computation replaced model-side calculation.

These are source claims, not controlled causal evidence. Campaign strategy, market conditions, product releases and other operational changes may also explain the business results.

## Workspace and context architecture

The implementation treats a coding agent as a knowledge worker with a task-specific computer:

- an isolated microVM and shell for each run;
- analysis and document-generation software such as pandas, DuckDB, openpyxl, WeasyPrint and Jinja2;
- six progressively disclosed Skills;
- a nineteen-page company Wiki;
- 218 live data and operation calls;
- deterministic code for calculations, date windows, account matching and hard safeguards.

The system prompt acts as a map rather than a knowledge store. It points to five layers ordered roughly by change rate:

1. system prompt for role, navigation and output rules;
2. Skills for reusable methods;
3. Wiki for company-specific facts and decisions;
4. live tools for current values;
5. deterministic code for reproducible calculations and non-bypassable safeguards.

The article's boundary is explicit: a Skill should describe a reusable way of working that could work at another company; the Wiki holds LangChain-specific campaign context.

## One runtime, capability profiles by entry point

The first architecture used separate graphs for scheduled PDF reports and Slack questions. LangChain abandoned that split after five weeks because capabilities had to be implemented twice, features drifted between entry points, Slack could not process report attachments, and Slack could not answer follow-ups using PDFs produced by the other graph.

The replacement uses one runtime instantiated for each request, with isolated state and different capability profiles:

- scheduled runs receive a single delegation tool and create one subagent per advertising platform;
- Slack runs receive a broader read, warehouse and campaign-operation surface;
- each thread receives its own sandbox and checkpoint.

The durable lesson is to reuse one execution owner when entry points share the same analysis and source rules, while narrowing capabilities per entry point instead of cloning the workflow.

## Model judgment versus deterministic computation

The first weekly report loaded campaign rows, keywords, pipeline records and landing-page checks into model context and asked the model to calculate and interpret everything. On a frozen test set, one report processed about 3.9 million input tokens, ran for 1,112 seconds and cost slightly more than USD 3.

The revised workflow uses Python to fetch data, align date windows, calculate totals and comparisons, apply fixed rules and write compact results. The model then explains likely causes, evaluates campaigns against their goals and recommends actions. The article reports runtime falling to 85 seconds and cost falling by about 40 times.

This supports a narrow engineering rule: use deterministic code for work that must be reproducible; reserve the model for context-sensitive judgment. The reported multiplier is workload- and implementation-specific.

## Authority by metric, not by system

The implementation does not force every metric into one canonical platform. It defines authority separately:

- advertising platforms own spend, impressions and clicks;
- the warehouse owns leads, opportunities and pipeline after conversion.

A keyword-based warehouse join omitted about 10% of Google spend because video campaigns do not always have keywords. Meta showed conversion counts, while the warehouse better distinguished outcomes such as Contact Sales from Sign Up. When data cannot be joined reliably, the agent preserves the gap and reports source, date window and attribution model rather than fabricating reconciliation.

The durable lesson is that source authority should be explicit at metric granularity, and incompatible sources should retain uncertainty instead of being normalized into false agreement.

## Progressive tool discovery

Loading even the smaller read-only portion of a catalog of more than 200 advertising tools initially consumed about 38,000 tokens before the user question was considered. LangChain replaced this with three catalog operations:

1. search for up to eight relevant tools;
2. read the selected schemas;
3. run the selected tool through the server, with campaign writes routed separately through approval.

For warehouse analysis, the agent can describe tables and fields and issue an analytical query, while fixed tools remain as a fast path for routine questions. Across 60 live runs, the article reports that query-enabled variants answered all analytical questions. The first-turn tool context fell to about 12,000 tokens and was reported as four times cheaper at the same judged quality.

These figures justify progressive disclosure as a candidate tactic, not a universal Top-K value or Hermes runtime default.

## Subagent isolation failures

The team compared separate runs per platform, one agent for all platforms, and a parent delegating to one subagent per platform. It chose parent-plus-subagents to retain cross-channel synthesis while giving each platform an isolated context window.

Two failures showed that separate context windows are insufficient:

- two subagents wrote reports to the same location and shared one `done` flag, so the first completion could cause the other to stop without producing a report;
- a subagent unable to confirm PDF rendering repeatedly checked files, consumed tokens and eventually attempted to rebuild the PDF.

The fixes were separate report paths and completion state for every platform, plus a reduced subagent tool surface: read context, compute and render. A successful render became the mechanical completion condition.

The reusable rule is to isolate writable paths and lifecycle state, define the exact return artifact and failure behavior, and give each child a bounded completion condition. Context isolation alone is not execution isolation.

## Analysis-to-action boundary

The agent can propose keyword, geographic-targeting and campaign changes in Slack. A server checks Slack user IDs; only designated people can approve or edit changes. Approval cards show current and proposed values. Code applies the approved change and queries the advertising platform to confirm the resulting state.

This separates model recommendation, human authorization, deterministic execution and authoritative readback. The article does not justify unattended writes.

## Interface boundary

Slack works for focused questions, discussion and lightweight approvals. It becomes awkward for bulk edits, many advertising groups or plans requiring repeated revision, so LangChain is moving complex work into a dedicated interface while retaining Slack for narrow interaction and approval.

## Reusable implications

- Treat the prompt as a navigation map and load context just in time.
- Keep reusable methods in Skills and organization-specific facts in the Wiki.
- Use one execution owner with capability profiles when several entry points share the same underlying workflow.
- Put calculations, reconciliation rules and hard safeguards in deterministic code.
- Define the authoritative source per metric and preserve unresolved gaps.
- Retrieve tool schemas progressively instead of exposing a large catalog at once.
- Isolate subagent files, state, tools, outputs and completion conditions—not only context windows.
- Separate recommendation, authorization, execution and authoritative readback.
- Judge efficiency alongside task completion and answer quality.

## Non-adoption boundary

This capture does not authorize a new Skill, runtime, sandbox provider, MCP router, cron job, campaign integration, production write path or autonomous monitoring service. Any active adoption requires a concrete local problem, project-level comparison, explicit authorization and rollback appropriate to the target layer.

## Related

- [[agent-context-engineering]]
- [[subagent-orchestration-patterns]]
- [[agent-development-lifecycle]]
- [[ai-agent-tool-selection-architecture]]
- [[hermes-memory-skills-wiki-boundaries]]
