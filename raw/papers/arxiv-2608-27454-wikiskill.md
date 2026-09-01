---
title: "WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution"
created: 2026-09-01
updated: 2026-09-01
type: raw-source
source_type: paper
source_url: https://arxiv.org/abs/2608.27454
arxiv_id: "2608.27454v1"
published_at: 2026-08-27
captured_at: 2026-09-01
status: captured
source_quality: primary-paper-full-text
---

# WikiSkill: Compiling Agent Experience into Persistent Knowledge for Skill Evolution

## Source metadata

- Authors: Liyan Tang, Cyrus Rashtchian, Chun-Sung Ferng, Andrew Tomkins, Da-Cheng Juan, Tu Vu
- Affiliations reported by the paper: Google Research and Virginia Tech
- Abstract page: `https://arxiv.org/abs/2608.27454`
- PDF reviewed: `https://arxiv.org/pdf/2608.27454`
- Version reviewed: arXiv v1, 2026-08-27
- Extraction route: full arXiv HTML text recovered after Karakeep returned `content_unavailable`; appendices and embedded prompts were included in the review.
- Local summary artifact: `/home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260901-222742-WikiSkill-Compiling-Agent-Experience-into-Persistent-Knowledge-for-Skill-Evoluti-1244231-100858000-summary.md`

## Research question

Existing skill-evolution methods iterate over execution traces and skill proposals, but the knowledge used to improve skills is often scattered across optimization history. WikiSkill asks whether an agent can improve skill evolution by keeping three states separate:

1. immutable execution evidence;
2. persistent, structured knowledge compiled from that evidence;
3. executable skills whose candidate updates can be accepted or rolled back.

The paper evaluates whether persistent knowledge improves skill evolution, whether benefits change with model scale, and whether evolved skills transfer across models and model families.

## Architecture

WikiSkill represents iteration state as `(S_k, W_k)`: the active skill set and the persistent Wiki.

### Raw Layer

- Stores immutable execution trajectories and task outcomes.
- Provides detailed evidence for failure diagnosis and later knowledge compilation.
- Is not itself the executable instruction surface.

### Wiki Layer

- Stores distilled success strategies, failure patterns, evolution history, rejected proposals and skill-impact records.
- Persists and compounds across iterations even when a candidate skill update is rolled back.
- Is read selectively by the Wiki Maintainer and Skill Proposer rather than injected indiscriminately into every task execution.

### Skill Layer

- Stores the procedural instructions used by the Inference Agent.
- Changes through bounded create-or-patch proposals.
- Candidate changes are admitted only when validation improves; score degradation triggers rollback of the skill state, not deletion of accumulated Wiki knowledge.

## Evolution loop and role boundaries

Each iteration has four functional components:

1. **Inference Agent** — executes training tasks with the current active skills and produces trajectories.
2. **Wiki Maintainer** — reads trajectories, separates successful patterns from failure causes, and updates structured Wiki pages.
3. **Skill Proposer** — reads selected Wiki pages, prior skill-impact history and multiple relevant failed traces before proposing one skill creation, patch or no-action decision.
4. **Gating and Rollback** — compares validation performance and either accepts or reverts the candidate skill change.

A central design choice is that the Inference Agent does not receive direct Wiki access in the main configuration. The paper argues that traces should expose what the active skills and model can or cannot do; extra Wiki context can mask skill gaps and reduce the diagnostic value of those traces. This is a training/evaluation design choice, not a universal prohibition on knowledge retrieval during normal production tasks.

## Experimental design

The evaluation covers five task families:

- LiveMath for mathematical reasoning;
- SealQA for web search;
- SpreadsheetBench for spreadsheet manipulation;
- OfficeQA for long-context document question answering;
- ALFWorld for interactive embodied tasks.

Model families include Qwen, Gemma and Gemini. The reported complete-evolution results average three independent runs. The paper uses 1,000 paired bootstrap samples for significance testing.

All methods start from an empty skill set. The evaluation compares no-skill execution with skills evolved by EvoSkill, SkillOpt and WikiSkill.

## Main quantitative findings

WikiSkill's reported average test scores across the five models are:

| Model | WikiSkill average |
| --- | ---: |
| Qwen-3.5-4B | 38.5 |
| Qwen-3.5-9B | 47.4 |
| Qwen-3.6-27B | 63.3 |
| Gemma-4-31B | 54.9 |
| Gemini-3.5-Flash | 68.1 |

Relative to the strongest competing skill-evolution method for each model, the reported average gains are respectively 3.3, 5.1, 10.0, 5.8 and 12.0 percentage points.

For the Qwen family, average gains over no-skill execution increase with model scale:

- 4B: +12.3 points;
- 9B: +17.5 points;
- 27B: +23.9 points.

SpreadsheetBench shows the strongest scale interaction in that family: +6.5, +9.3 and +40.9 points respectively. The evidence supports complementarity between stronger models and evolved skills in these benchmarks; it does not establish a universal scaling law for production agents.

A smaller model with evolved skills can outperform a larger no-skill model in the reported setup: Qwen-3.5-9B with WikiSkill averages 47.4, compared with 39.4 for Qwen-3.6-27B without skills.

## Persistent-knowledge ablation

For Gemini-3.5-Flash, the paper reports:

| Configuration | Average score |
| --- | ---: |
| No persistent Wiki | 48.7 |
| Wiki available to Skill Proposer | 63.7 |
| Wiki also available to Inference Agent | 60.9 |

This ablation supports two bounded claims:

1. persistent knowledge accumulation materially contributes to the reported skill-evolution result;
2. indiscriminate Wiki injection into the rollout actor is weaker than keeping Wiki access with the proposal/maintenance roles in this setup.

It does not show that normal Hermes tasks should never retrieve Wiki knowledge. The result applies to trajectories being used to diagnose and evolve skills.

## Rejected-proposal accumulation example

The ALFWorld case shows why knowledge persists independently of skill state:

1. an initial `goal-directed-action` proposal fails to improve validation and is rejected;
2. the rejection and observed failure remain in the Wiki;
3. the system next learns the narrower rule not to place an object back where it came from;
4. after observing another loop variant, it generalizes to executing each operation type at most once per object.

The durable mechanism is not “retain every proposal.” It is: preserve proposal, evidence, outcome and rejection reason so later candidates can avoid repeating failed search paths and can refine a partially useful idea.

## Cross-model transfer and negative transfer

Skills evolved by one model can transfer to another and sometimes outperform self-evolved skills:

- Qwen-3.6-27B skills raise Qwen-3.5-9B SpreadsheetBench performance to 50.5%, versus 24.3% without skills and 33.6% with self-evolved skills.
- On ALFWorld, Qwen-3.5-9B reaches 70.2% using Qwen-3.6-27B skills, versus 63.4% with its own skills.

Transfer can also fail sharply. A Qwen-3.5-4B SpreadsheetBench skill containing single-line Python constraints, string-conversion rules and fragmented diagnostics restricts Gemini-3.5-Flash from using complete scripts and can consume its interaction budget; reported performance falls from 50.5% to 18.1%.

The paper therefore supports compatibility validation across `skill × model × harness × tool environment`. File-format portability is not behavioral portability.

## Task-specific failure boundaries

- LiveMath benefits broadly across the evaluated models.
- OfficeQA exposes a capability ceiling: smaller models sometimes cannot execute a complex long-document workflow and fall back to default reading behavior.
- Gemini-3.5-Flash already reaches full ALFWorld validation performance, so all evolution methods remain at 85.9% on that task's test set.

These cases show that skill evolution cannot repair every model capability limit and may have no optimization signal after validation saturation.

## Evidence limitations

- arXiv preprint v1; peer-review status was not established at capture time.
- Skills are directly injected into system prompts to isolate skill quality; the study does not evaluate production retrieval, triggering or selection behavior.
- Every skill modification must immediately improve the validation score. This may reject neutral intermediate changes that would enable later gains.
- The Wiki accumulates pattern pages, logs and diffs without an automatic pruning mechanism.
- The benchmarks do not cover tasks requiring hundreds of actions or hours of execution.
- The study does not evaluate online skill adaptation inside one long-running task.
- Reported percentages and role topology are source-specific evidence, not mandatory Hermes thresholds or runtime architecture.
- The results do not authorize autonomous active-skill publication, automatic Wiki-to-Skill promotion, cron-driven self-modification or removal of independent review.

## Durable Hermes interpretation

The paper provides strong primary evidence for a governed, two-state learning model:

```text
immutable evidence
→ persistent compiled knowledge
→ bounded skill candidate
→ independent validation
→ accept or roll back skill
→ retain evidence, rejection reason and reusable knowledge
```

For Hermes, the smallest faithful mapping is:

```text
session_search / project traces / test evidence
→ audited pattern extraction
→ Wiki concept, rejection history and candidate rationale
→ project-local skill candidate and frozen evaluation
→ explicit active-layer promotion or rollback
```

The role-specific access result is an optional rule candidate only for skill-evolution experiments: when rollouts are diagnostic inputs for future skill changes, keep Wiki knowledge available to maintainers/proposers but do not give it to the rollout actor by default. Promote this into default optimization guidance only after a frozen local A/B comparison shows cleaner failure attribution or better held-out skill evolution without unacceptable task-quality loss.
