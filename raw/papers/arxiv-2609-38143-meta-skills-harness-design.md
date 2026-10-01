---
title: "Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI"
created: 2026-10-01
updated: 2026-10-01
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2609.38143v1
arxiv_id: "2609.38143v1"
published_at: 2026-09-29
captured_at: 2026-10-01
status: captured
source_quality: primary-paper-selected-source-note
---

# Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI

## Source metadata and capture scope

- Authors: Cheng Qian, Kunlun Zhu, Beibin Li, Zhenhailong Wang, Heng Ji.
- Publication: arXiv v1 preprint, submitted 2026-09-29; peer-reviewed acceptance is not established by this capture.
- Versioned abstract: https://arxiv.org/abs/2609.38143v1
- Versioned HTML: https://arxiv.org/html/2609.38143v1
- Discovery page: https://huggingface.co/papers/2609.38143
- Extraction route: direct arXiv HTML text. This note is based on the paper's method, experimental setup, results, analyses and relevant appendices, not solely its abstract or a generated summary.
- Capture form: selected, paraphrased source note with short original excerpts. It is not a verbatim full-paper mirror. Figures were not visually inspected; mathematical HTML contains duplicated renderings, so equations and figure-derived numeric values are not reproduced here. No code or benchmark was executed, and results below are author-reported rather than independently replicated.

## Selected original excerpts

From §3.1, the representation of a support principle:

> A meta-skill s = (when, provide, use) contains three fields: when identifies observable conditions that call for support; provide specifies the capability or resource the environment should supply; and use explains how the Target should employ that support and which judgments remain its responsibility.

The expression and italics in this excerpt are normalized from HTML to readable plain text; the three field names and their meanings are retained.

From §3, the compute-accounting boundary:

> The budget Cx covers only Target execution, excluding Builder computation for harness construction.

The subscript in the budget symbol is normalized to plain text.

## Research question and mechanism (§3; appendix B)

The paper distinguishes task-solving skills for a Target from support-design principles for a Builder. Both models' weights remain fixed. Learning changes an external meta-skill bank and the execution environment supplied to the Target, rather than training model parameters.

During development, the Builder constructs a harness, observes the Target's public execution record and development score, and compares the resulting lesson with the existing bank. Each update permits at most one addition or revision, or leaves the bank unchanged; additions and revisions must cite evidence from the current batch. Learning uses two development passes. Each meta-skill has `when`, `provide` and `use` fields, with a combined limit of 192 tokens. Superseded versions are archived.

The bank is frozen before testing. For each test task, the Builder receives the public task input and either the full bank or BM25 top-2 retrieved skills, then constructs a fresh harness. It cannot inspect test execution feedback, reference answers or evaluator internals. The Target retains responsibility for substantive reasoning and final submission.

Seven optional component families are exposed: instructions, memory, context organization, composed tools, execution control, verification and recovery, and workspace preparation. This is a construction space, not a requirement to install all seven components for every task.

## Experimental setup and main results (§4; table 3)

- Harness-Bench: 11 development tasks and 95 test tasks; agent workflows.
- NewtonBench: 32 development tasks and 292 test tasks; interactive scientific law discovery.
- Main Builder: GPT-5.6-Sol.
- Targets: Gemini-3.6-Flash, Qwen3.8-Flash and GPT-OSS-120B, as named in the paper.
- Target execution budgets are fixed within each benchmark; Builder learning and construction fall outside those budgets. Builder conditions have matched construction permissions and allowances.
- Failed construction or execution without a valid native score contributes zero; declared tasks remain in the evaluation denominator.

The full-bank meta-skill Builder reports a 65.31% macro-average across the six model–benchmark settings. The no-skill Builder reports 56.36%, and direct delivery of the same full bank to the Target reports 53.29%; the author-reported differences are +8.95 and +12.02 percentage points respectively. The former comparison controls for construction capability; the latter preserves skill content while changing whether a separate Builder installs support before Target execution. The direct-delivery Target is allowed to implement the guidance with its native tools, but must do so within its own execution budget.

These results support the value of learned and implemented support in the evaluated framework. They do not establish superiority under equal joint compute, latency or financial cost. Direct delivery of support-design meta-skills is also not equivalent to all ordinary task-solving skills or production Skill packages.

## Negative findings and evidence limits (§5; appendices A–B)

- Refinement is not monotonic: on Harness-Bench, Qwen drops 4.06 points from its first-pass peak after the second development pass.
- Cross-Builder transfer is configuration-dependent: the Sol-to-Qwen bank yields a +13.36-point gain with Sol on NewtonBench, but a −4.45-point change when Gemini-Pro implements that bank. The reported cross-Builder reuse comparisons have confidence intervals including zero; useful transfer is a possibility, not an established universal gain.
- Controller ablation on NewtonBench lowers the three Target scores by 13.36, 4.79 and 1.03 points respectively, but only Gemini's 95% interval excludes zero. These interventions remove controllers from already-constructed harnesses; they do not identify a universally optimal controller design.
- Memory plus context has positive estimated retention effects for Gemini and Qwen and a negative one for GPT-OSS; all three intervals include zero. More state is not proven universally beneficial.
- Full-bank access exceeds BM25 top-2 in five of six settings at the evaluated scale. This does not establish that large production skill libraries should be loaded wholesale, or that task/phase-aware retrieval is inferior.
- The main held-out claim concerns new instances within known workflow categories and physical mechanisms. Cross-dataset and unseen-task-family transfer are not established.
- The paper uses one adopted execution per task and condition. Paired task-bootstrap intervals characterize variation across the fixed task inventory, not variability across repeated model generations or independently learned banks.
- Construction cost, joint latency/compute tradeoffs and long learning histories remain open deployment questions. Same-model Builder/Target gains concern system-level support design with fixed weights, not autonomous production self-modification or weight-level learning.

## Concrete implementation example (appendix D.1)

A selected successful metric-migration episode requires four mutually consistent deliverables. The Builder turns a checkpointing principle into a generated auditor, a controller and a submission gate. Mechanical checks cover artifact presence, schemas, metric coverage, source values and agreement between deliverables; the Target remains responsible for interpreting whether a metric change is justified.

Writes through the tracked file-writing interface invalidate a previous clean audit, requiring a new check before submission. This connects artifact version, validation status and completion. It is a selected case illustrating implementation, not a typical-success-rate estimate, proof of complete write interception or isolated causal evidence for any single component.

## Related knowledge

- [[agent-experience-consolidation-loops]] owns the reusable distinction between task skills and support-design meta-skills, and the boundaries for experience promotion.
- [[agent-harness-search-regularization]] owns candidate-search and acceptance evaluation; this paper does not validate a combined system with that separate method.
