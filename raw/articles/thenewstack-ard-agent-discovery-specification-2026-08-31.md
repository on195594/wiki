---
title: MCP was supposed to solve the agent tooling problem. It missed a step.
author: Amanda Caswell
source_type: article
source_url: https://thenewstack.io/ard-agent-discovery-specification/
published_at: 2026-08-31
captured_at: 2026-09-02
status: raw
tags: [agent, mcp, tool, architecture, workflow]
extraction_limitations: Full article prose was obtained from the existing Karakeep capture; direct web extraction also contained substantial navigation boilerplate. This note preserves a source-backed synthesis rather than a verbatim article snapshot.
---

# Agentic Resource Discovery (ARD): discovery before invocation

## Source

- URL: https://thenewstack.io/ard-agent-discovery-specification/
- Title: `MCP was supposed to solve the agent tooling problem. It missed a step.`
- Author: Amanda Caswell
- Published: 2026-08-31
- Captured: 2026-09-02
- Extraction route: Karakeep full-content capture
- Source quality: full
- Local summary artifact: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260902-091039-MCP-was-supposed-to-solve-the-agent-tooling-problem.-It-missed-a-step.-https-the-2046515-593366480-summary.md`

## Core claim

The article argues that MCP standardizes connecting to a known external tool or data service, but does not itself answer how an agent discovers an appropriate service when resources are spread across clouds, SaaS products, and internal systems. Agentic Resource Discovery (ARD) is presented as a draft, open discovery layer for that preceding step.

## Source-backed details

- ARD calls MCP servers and other externally connectable capabilities “agentic resources.”
- The v0.91 proposal described in the article uses JSON-LD and a REST interface; `POST /search` is required and browsing endpoints are optional.
- ARD is intended to federate catalogs rather than require resources to move into one registry: an organization can retain a private catalog and policy while searching approved external discovery services.
- A search can return several plausible resources, unlike DNS’s usual name-to-location resolution. Each discovery service therefore defines its own return and trust rules.
- The article identifies Junjie Bu (Google), R.V. Guha (Microsoft), and Shaun Smith (Hugging Face) as authors, reports Apache 2.0 licensing, and lists participation by several infrastructure vendors. It also says governance remained unsettled at publication.

## Hermes interpretation

ARD adds an upstream distinction to the existing tool-selection model:

1. **Discovery**: find candidate capabilities or registries that might satisfy a task.
2. **Availability and admission**: decide which discovered or preconfigured tools are permitted and trusted in this environment.
3. **Candidate reduction, selection, execution, and fallback**: decide what the model sees and invokes for the current step.

The reusable principle is to keep discovery/catalog infrastructure separate from the tool invocation protocol and from local authorization. Dynamic discovery creates a larger candidate set; it does not replace capability verification, permission checks, schema validation, user approval, execution-result verification, or fallback behavior.

## Limits

- This is a secondary news article about an early proposal, not the ARD specification or an interoperability evaluation.
- The article’s “DNS for agents” framing is only a metaphor: ARD can return multiple semantically plausible candidates whose trust and suitability still need adjudication.
- The article does not demonstrate that Hermes currently needs dynamic discovery. Hermes has a bounded local tool/MCP registration model; any adoption would require evidence of fragmented catalogs or repeated discovery friction, plus separate security, evaluation, approval, and rollback work.

## Compiled concept pages

- Canonical owner: [[ai-agent-tool-selection-architecture]]

## Adjacent boundary concepts

- [[agent-context-engineering]]
- [[typed-ai-agent-boundaries]]
