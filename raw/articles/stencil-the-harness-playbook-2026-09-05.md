---
title: "The Harness Playbook"
created: 2026-09-05
updated: 2026-09-05
type: raw-source
tags: [agent, harness, runtime, state, sandbox, orchestration, evaluation]
source: Stencil
source_url: https://stencil.so/blog/harness-playbook
author: Can Bölük
published: 2026-09-02
captured: 2026-09-05
status: captured
extraction: "Structured capture based on the completed Hermes URL-summary run; the local output is preserved separately. This file is not a byte-for-byte extraction of the publisher page."
local_summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260905-161356-The-Harness-Playbook-2991970-819941600-summary.md
---

# The Harness Playbook

## Provenance and evidence boundary

- Source URL: https://stencil.so/blog/harness-playbook
- Publisher/site: Stencil
- Captured: 2026-09-05
- Capture type: structured source capture derived from the completed URL-summary run.
- Source limitation: author, publication date, title, and section structure were checked against the publisher page on 2026-09-06, but byte-level full article text is not stored here; numerical claims and implementation details remain source claims.
- Hermes boundary: this source supports concept-level architecture review, not authorization for runtime, skill, MCP, cron, gateway, or configuration changes.

## Captured claims

The article presents Agent Harnesses as stateful execution systems rather than simple model/tool loops. It uses game-engine architecture as an analogy and evaluates four scenarios: multiplexed local workspaces, remote-driven clients, observer views, and autonomous software factories.

The proposed architectural principles are:

1. one authoritative session state from which rewind, fork, resume, synchronization, and inspection are derived;
2. a trusted control plane that owns policy, routing, approvals, session ownership, and logging;
3. constrained work units with timeouts, resource limits, cancellation, and observability;
4. explicit model/provider compatibility rules instead of scattered conditionals;
5. views as projections of authoritative state rather than independent sources of truth.

The article argues that plugin-local state is a major source of rewind, fork, resume, and recovery bugs. It discusses stateful examples involving checkpoints, plans, counters, dynamic tools, bookmarks, commits, and games, and proposes materializing session state in one authoritative tree with append-only change records.

The runtime boundary is split between a trusted host and an execution sandbox. The host owns state, inference, security, routing, approvals, and logs; the sandbox executes restricted instructions and must not become the policy authority. The article also recommends copy-on-write isolation for child agents, a unified job abstraction for shell, child agents, background processes, and long-lived services, centralized output truncation, and physical termination in addition to cooperative cancellation.

The control-plane section discusses declarative runtime variables, a decision stack for competing control logic, explicit model-family/provider compatibility, staged forced-tool behavior, and reducing the permanent tool schema surface. Long-tail capability is proposed through a dynamic CLI or a small number of broad native tools.

The rendering section treats terminal output as a formal streaming protocol with semantic block lifecycles, a logical history ledger, physical terminal rows, speculative slots, and width-independent committed history. The article presents typed/structured streaming and formal verification as ways to avoid rendering drift and speculative data leakage.

The article recommends Rust for a constrained core and Python for reflective extensions, but these are technology choices in the source proposal, not Hermes adoption requirements.

## Hermes-relevant extraction [推论]

- Treat harness state, plugin state, child-agent lifecycle, jobs, cancellation, and external side effects as one recovery and verification problem.
- Keep control-plane decisions in the trusted parent/host; keep execution workers narrow and bounded.
- Derive views, prompts, and inspections from authoritative state where recovery or branching semantics matter.
- Verify completion, cancellation, resume, and side-effect outcomes from the strongest available authoritative state rather than UI changes or process return alone.
- Prefer the smallest existing Hermes layer: concept Wiki first; project-local rules only after a real failure or repeated need.

## Claims not promoted to Hermes defaults

The source does not authorize adopting an XML/DOM session tree, Director stack, KDL model taxonomy, Rust/Python split, dynamic CLI, five-tool limit, copy-on-write workspace implementation, TLA+ protocol, or any specific benchmark/latency number. These remain proposals requiring independent local evidence and explicit project/runtime approval.

## Related Hermes concepts

- [[agent-development-lifecycle]]
- [[stateful-agent-environments-and-grounded-verification]]
- [[subagent-orchestration-patterns]]
- [[agent-orchestration-production-tradeoffs]]
- [[agent-self-validation-loops]]
