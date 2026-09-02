---
title: "SKILL.state: Scalable Long-Horizon Agent Skills"
authors: [Sanket Badhe, Priyanka Tiwari, Jonghyun Chung]
source_type: paper
source_url: https://arxiv.org/html/2608.26263v2
canonical_url: https://arxiv.org/abs/2608.26263v2
arxiv_id: "2608.26263v2"
published_at: 2026-08-26
revised_at: 2026-08-28
captured_at: 2026-09-02
venue_note: accepted at EMNLP
extraction_route: arXiv HTML via Karakeep full-content capture; arXiv abstract metadata independently checked
source_quality: full-paper evidence packet
local_summary_path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260902-074740-SKILL.state-Scalable-Long-Horizon-Agent-Skills-1927510-501119800-summary.md
type: raw-source
status: captured
---

# SKILL.state: Scalable Long-Horizon Agent Skills

## Source record

- Authors: Sanket Badhe, Priyanka Tiwari, Jonghyun Chung
- arXiv: [2608.26263v2](https://arxiv.org/abs/2608.26263v2)
- Full HTML: https://arxiv.org/html/2608.26263v2
- Submitted: 2026-08-26; revised: 2026-08-28
- arXiv subjects: Artificial Intelligence (cs.AI), Multiagent Systems (cs.MA)
- arXiv comment: accepted at EMNLP
- License shown by arXiv: CC BY 4.0

## Research question

The paper asks whether long-horizon procedural Agent execution should continue to use an append-only conversational transcript as its primary runtime substrate, or whether the transcript can be replaced by an explicit mutable execution state without losing task performance.

Its central claim is narrower than “memory is unnecessary”: for procedural execution, the next model call can depend on an immutable skill specification, the current structured state and the latest observation, while prior observations, actions and intermediate reasoning remain outside the next prompt.

## Architecture

At step `t`, the model receives:

```text
A_t = (P, Σ_t, O_t)
```

- `P`: immutable procedural or skill specification.
- `Σ_t`: current structured execution state.
- `O_t`: latest environment observation.

The model generates:

```text
(R_t, ΔΣ_t, a_t)
```

- `R_t`: within-step reasoning used only to compute the transition and action.
- `ΔΣ_t`: structured state patch represented as a JSON dictionary of mutations and deletions.
- `a_t`: action to execute.

The deterministic runtime then:

1. validates `ΔΣ_t`;
2. applies it as `Σ_(t+1) = Σ_t ⊕ ΔΣ_t`;
3. executes `a_t`;
4. discards `R_t` from subsequent prompts;
5. starts the next step from `P`, `Σ_(t+1)` and the new observation.

The merge operator uses null-deletion semantics. The paper states that invalid patches cannot corrupt persistent state because schema ownership and validation remain in the deterministic runtime; invalid output triggers rollback and retry.

## Schema ownership

Execution state is a domain-level runtime abstraction, not a task-specific transcript summary. The paper reports that all 100 InterCode CTF instances reuse one five-field schema:

- `discovered_flags`
- `tested_hypotheses`
- `active_files`
- `working_dir`
- `cmd_summary`

This is evidence that one bounded schema may cover a family of tasks, but not evidence that a universal Agent schema exists.

## Complexity claim

For append-only conversational execution, the prompt at step `t` grows as `O(t)`, giving cumulative prompt-token complexity `O(T²)` across horizon `T`.

For SKILL.state, each prompt contains only `P`, bounded `Σ` and the latest `O`; under the paper's bounded-state assumption, per-step prompt size is `O(1)` with respect to elapsed steps and cumulative prompt-token complexity is `O(T)`.

This is an asymptotic architecture claim. It depends on the skill specification, state and latest observation remaining bounded; a state object that itself grows with history would break the claimed constant prompt footprint.

## Evaluation design

### SkillExecBench

Two controlled, deterministically simulated domains isolate execution-state maintenance from open-ended search:

- Warehouse Management: 500 independent shelves with Store, Ship, Move and Wait actions.
- Software Repository: branches, commits, pull requests and CI status with graph-like dependencies.

### Public interactive benchmarks

- InterCode CTF: 100 Linux terminal capture-the-flag tasks; binary pass@1.
- Sierra τ-Bench Retail and Airline: simulated customer-service workflows over relational databases and policy-constrained transactional tools.

### Runtime baselines

Primary baselines:

- Prompt / ReAct-style: append every observation, reasoning trace and action.
- Memory: rolling three-step window plus periodically updated natural-language summary.
- Stateful / LangGraph-style: structured state plus the full growing conversational transcript.

Budget-matched controls:

- fixed-budget sliding-window truncation;
- token-capped natural-language summary;
- ReAct history compressed by LLMLingua.

### Models and statistics

- Gemini-3-Flash
- Gemma-4-31B-it
- Qwen-3-8B-it
- temperature `0.0`, top-p `1.0`
- synthetic experiments use five procedural-generator seeds
- the paper reports paired t-tests with `p < 0.01` for differences at horizons `T >= 50`

## Main evidence

### Long-horizon scaling

In Warehouse with Gemini-3-Flash:

- At `T=100`, Stateful consumes 1,062,387 tokens; SKILL.state consumes 65,408, reported as a 16.2× reduction.
- At `T=200`, SKILL.state reports 0.94 accuracy and about 122k tokens; the Memory baseline grows to about 6.1M tokens.
- SKILL.state mean prompt size remains roughly 1,736–1,905 tokens across the reported horizons.

These are source-specific results from the paper's simulator, prompts, schemas and token accounting; they are not Hermes performance forecasts.

### Noise robustness

At `T=50`, the authors inject 5, 20 or 50 irrelevant events per step. The Prompt baseline falls from 0.68 under low noise to 0.53 under high noise, while SKILL.state remains at or above 0.97. The proposed mechanism is that distractors not committed to state disappear after the current transition instead of accumulating in future prompts.

The noise is explicitly synthetic, irrelevant and non-state-altering. This experiment does not cover misleading but semantically relevant observations, adversarial state patches or noisy events whose significance becomes clear later.

### State recovery

For several silent external-drift scenarios in the warehouse and repository simulations, history-based baselines require multiple recovery turns, while SKILL.state reports zero recovery steps after the corrective observation. Some canceled/closed scenarios fail for all runtimes, so explicit state does not guarantee recoverability when the environment or action space cannot repair the situation.

### Public benchmarks

The paper reports:

- InterCode CTF: SKILL.state pass@1 `54.2%`, 7.8 percentage points above the strongest baseline and 12.4 points above Stateful; token use falls 60.4% versus ReAct and 65.9% versus Stateful.
- τ-Bench Retail: `58.3%` pass rate with the lowest reported token cost.
- τ-Bench Airline: `32.4%` pass rate; prompt footprint about 2,800 tokens per step versus baseline peaks above 11,000; 40.5% fewer tokens than ReAct and 45.4% fewer than Stateful.

The paper's public-benchmark results broaden the evidence beyond synthetic state tracking, but remain one implementation and one evaluation report; no independent reproduction is included in the paper.

### Budget-matched controls

At Warehouse `T=100` and about 1,800 prompt tokens:

- sliding-window truncation scores 0.18;
- LLMLingua scores 0.22;
- SKILL.state scores 0.94.

The authors interpret this as evidence that the gain comes from preserving exact relational state rather than merely shortening prompts. The comparison supports that conclusion inside the chosen warehouse environment; it does not establish that every structured schema is better than every learned compression method.

## Open-weight model failure taxonomy

For Gemma-4-31B-it at `T=100`, the paper reports score 0.42 and classifies logged failures as:

- 68% premature state overwrite or deletion;
- 20% schema comprehension or type coercion errors;
- 12% JSON syntax or formatting errors.

This is direct counterevidence to treating the architecture as model-agnostic in operational reliability. Deterministic validation prevents invalid persistence, but retries, constrained decoding and semantic patch checks still impose cost and may not repair incorrect but schema-valid updates.

## Assumptions and explicit limitations

The paper states that `Σ_t` must be a sufficient statistic for future execution. This can fail when:

1. no stable schema is known and state structure must be discovered dynamically;
2. an earlier observation was not recognized as relevant and therefore was not committed to state;
3. the task objective is defined over historical trajectory, including audit, provenance, debugging or explanation.

Additional boundaries:

- The evaluated implementation is single-agent. Multi-agent shared state requires deterministic conflict-resolution semantics for concurrent writes, which the paper does not evaluate.
- Schema validation protects state from malformed patches, not from semantically wrong but schema-valid patches.
- The constant-space claim excludes state or observations that grow with execution history.
- The paper separates future decision context from history; it does not argue that audit logs should be deleted.
- Exact data/code availability and independent replication were not established by this capture.

## Durable mechanism extracted

The reusable mechanism is:

```text
immutable procedure
+ versioned structured current state
+ newest observation
→ model proposes reasoning, state patch and action
→ deterministic runtime validates and merges the patch
→ runtime executes the action
→ reasoning and obsolete observations leave the next prompt
→ append-only evidence remains outside the prompt for audit/recovery
```

The architecture is most suitable when:

- the task has many sequential steps;
- a bounded domain schema can represent future-relevant state;
- tool outputs or observations are large/noisy;
- deterministic patch validation and rollback are available;
- complete history is not itself the task output.

It should be skipped or hybridized when:

- schema discovery is part of the task;
- delayed relevance is common;
- historical sequence is needed for compliance, debugging or explanation;
- concurrent writers lack conflict resolution;
- the selected model cannot reliably emit semantic state patches.

## Hermes interpretation boundary

The paper provides strong support for the existing Hermes direction of state cards over raw transcripts. It does not itself authorize a Hermes core/runtime rewrite. A bounded active-workflow adaptation can require explicit state for genuinely long-horizon, stateful execution while keeping ordinary direct tool calls and short workflows unchanged.

Hermes-local additions—state versioning, evidence pointers, verified-versus-inferred labels, side-effect ledger, approval state and external audit artifacts—are engineering inferences rather than claims made or evaluated by the paper.

## Related Wiki owners

- [[agent-context-engineering]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-context-engineering-design-priorities]]
- [[loop-engineering-hermes-agent-workflow]]
- [[agent-orchestration-production-tradeoffs]]
- [[typed-ai-agent-boundaries]]
- [[stateful-agent-environments-and-grounded-verification]]
