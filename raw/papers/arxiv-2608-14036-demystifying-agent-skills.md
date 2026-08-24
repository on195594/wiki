---
title: "Demystifying Agent Skills: Why They Work—Until They Don’t"
created: 2026-08-24
updated: 2026-08-24
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2608.14036
arxiv_id: "2608.14036v1"
published_at: 2026-08-14
captured_at: 2026-08-24
status: captured
source_quality: primary-paper-full-pdf
---

# Demystifying Agent Skills: Why They Work—Until They Don’t

## Source metadata

- Authors: Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
- PDF reviewed: `https://arxiv.org/pdf/2608.14036`
- Version reviewed: arXiv v1, 2026-08-14
- Extraction note: full paper reviewed, including study design, main tables, trajectory taxonomy, retrieval experiments, appendices, prompts and limitations.
- Related Chinese guide: `https://yage.ai/share/skill-checklist-not-textbook-20260823.html`; used only as discovery/secondary interpretation, not as the quantitative evidence source.

## Research questions and design

The paper studies four separate questions rather than treating Skill use as a single success-rate comparison:

1. whether the same source trajectories behave differently when represented as Workflow Memory versus a structured Skill;
2. whether explicit success/failure outcome labels affect distilled guidance;
3. whether distilled guidance transfers across agent frameworks;
4. how candidate-pool size and semantic confusability affect identification, selection, actual use and downstream execution.

The authors normalize 8,135 trial records, open-code 240 sampled records into 238 valid unique labels, and use 528 matched Raw / Workflow Memory / Skill triples for the paired mechanism analysis. The principal task environments are containerized terminal, coding and tool-use benchmarks; this is not a general evaluation of browser, multi-agent or production workflows.

## Main findings captured from the paper

### Representation and aggregate result

In the 528 matched triples:

| Condition | Success rate |
| --- | ---: |
| Raw | 59.1% |
| Workflow Memory | 55.9% |
| Skill | 61.9% |

Paired differences reported by the paper:

- Skill vs Workflow Memory: +6.06 percentage points, 95% CI `[+0.76, +11.36]`;
- Skill vs Raw: +2.84 points, 95% CI `[-2.27, +7.95]`;
- Workflow Memory vs Raw: -3.22 points, 95% CI `[-8.14, +2.08]`.

Only the Skill-vs-Workflow-Memory interval excludes zero. The paper supports “distilled Skills outperform direct Workflow Memory under the matched protocol”; it does not establish a statistically clear universal advantage over no memory.

### Dominant mechanism

- Procedural anchoring: 65.7% of Skill cases.
- Explicit knowledge injection: 4.5%.

The strongest improvements are execution-layer failures:

- environment/infrastructure failure: 5.3% → 0.2%;
- output format or schema mismatch: 7.4% → 3.2%;
- background-service lifecycle failure: 2.7% → 0.8%;
- shell/code corruption: 1.1% → 0.2%.

The effect is weak for algorithmic logic errors and static-only verification. The paper therefore supports writing Skills around prerequisites, ordered actions, environment checks, lifecycle handling, failure boundaries and executable verification rather than encyclopedia prose.

### Outcome annotation

Explicit success/failure labels matter most when the source pool mixes successful and failed trajectories. All-failure source pools can underperform the Raw baseline even when labeled. The evidence supports preserving outcome and verifier provenance; it does not support blindly learning from every failure or treating a binary outcome label as sufficient causal attribution.

### Retrieval, selection and actual execution

When candidate pools grow from 5 to 100, actual-use precision falls from 29.6% to 3.3%, while end-task success remains comparatively stable. Similar distractors degrade offline identification more than random or dissimilar distractors. Exact ground-truth retrieval is therefore neither sufficient nor necessary for downstream success: related Skills can provide partial procedural support, while the nominally correct Skill can be misapplied, ignored or insufficient.

The paper reports Skill guidance misapplied or ignored in 10.0% of Skill-group trajectories, versus 0.8% for Raw and 0.4% for Workflow Memory. Applicability and adaptation are independent failure surfaces.

### Cost boundary

For the 83 matched tasks with complete Token records:

| Representation | Success rate | Total tokens |
| --- | ---: | ---: |
| Raw trajectories | 64.1% | 555.7K |
| Workflow Memory | 64.8% | 426.2K |
| Skill | 69.6% | 521.5K |

Skill is not automatically the cheapest representation. Evaluation must keep completion, cost and latency separate.

## Evidence limitations

- arXiv preprint v1; not peer reviewed at capture time.
- RQ1–RQ3 condition on tasks with source pools suitable for balanced success/failure mixtures, limiting population-level generalization.
- Main settings are terminal, coding and tool-use benchmarks in controlled environments.
- The full paired-mechanism labeling relies partly on an LLM judge; not every one of the 528 triples is independently human-coded.
- Model and harness coverage is limited and differs across research questions.
- Cross-framework transfer is tested only in bounded directions.
- Token analysis uses only the 83-task complete-data intersection.
- Results do not establish safe autonomous Skill creation, active publication or lifelong self-improvement.

## Durable interpretation boundary

The paper is strong evidence that Skills should be treated as governed procedural assets whose lifecycle separates representation, discovery, invocation, applicability, verified outcome, misuse and cost. It is not evidence that a larger Skill library, higher retrieval hit rate or more frequent automated revision is inherently beneficial.
