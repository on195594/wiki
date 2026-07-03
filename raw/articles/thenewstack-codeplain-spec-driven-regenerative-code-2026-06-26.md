---
title: '"Code should be regenerated, not maintained": Codeplain makes the case for spec-driven development'
author: unknown
source_type: article
source_url: https://thenewstack.io/codeplain-spec-driven-regenerative-code/
published_at: unknown
captured_at: 2026-06-26
status: raw
tags: [ai-coding, spec-driven-development, agent, context-engineering, hermes]
extraction_limitations: HTML article body was extracted from The New Stack page container by the `/gsummary` workflow; this raw page stores the generated summary and source metadata rather than the full original article body.
---

# Codeplain spec-driven regenerative code

## Source
- URL: https://thenewstack.io/codeplain-spec-driven-regenerative-code/
- Title: `"Code should be regenerated, not maintained": Codeplain makes the case for spec-driven development`
- Source: The New Stack
- Captured: 2026-06-26
- Local summary artifact: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260626-155503-Code-3183861-356495120-summary.md`
- Extraction note: HTML article body extracted from `#tns-post-body-content` / `#tns-post-body` with bounded substring fallback; scripts/navigation/forms removed; duplicate blocks removed.

## Compiled concept pages
- [[codex-agent-workflow-layering]]
- [[agent-context-engineering]]

## Core claim
Codeplain argues that in AI-era software development, teams should maintain structured, human-readable specifications as the durable source of truth and regenerate implementation code from those specs, rather than treating generated code as the primary artifact to hand-maintain.

## Key points
- AI makes code generation cheap, but code review and long-term maintenance remain expensive.
- Codeplain's Plain specification language aims to make product intent, constraints, and system behavior the reviewable artifact.
- `plain-forge` lets agents such as Claude Code incrementally draft and update specs through conversation, reducing the burden of writing a complete spec upfront.
- Manual patches to generated code create provenance debt: the code changes, but the reason, constraint, and generation context behind the change may no longer be recoverable.
- The article cites an Incode integration-maintenance case and claims spec generation can use 5–10x fewer tokens than direct code generation.

## Hermes interpretation
- The article supports the existing Hermes principle that medium or risky AI coding work should first converge into a structured spec before planning, test writing, or agent execution.
- The reusable concept is not "adopt Codeplain" or "fully regenerate all code". It is the layer separation: maintain intent/spec/contracts; generate or patch implementation from that controlled source.
- In Hermes, this should first remain wiki knowledge and optional `spec-driven-development` reference material. It should not automatically promote active skill behavior, runtime config, MCP, cron, or memory changes.

## Limits
- The article describes an early company and product direction, not a mature cross-industry standard.
- Full code regeneration is risky for database migrations, production configuration, credentials, security policy, and other irreversible or high-risk surfaces.
- Poor specs can systematize errors; regeneration only helps when specs, tests, interface contracts, and review gates are strong.
