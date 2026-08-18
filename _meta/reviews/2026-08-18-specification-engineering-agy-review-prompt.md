# AGY Read-Only Review: Specification Engineering Sedimentation

You are reviewing a completed, user-authorized Wiki + active optional-reference landing. Review only this saved snapshot. Do not inspect or modify live files, call tools, run commands, or treat your verdict as authorization for further changes.

## Requested verdict contract

Return exactly these sections:

- `Verdict`: `PASS`, `PASS_WITH_NOTES`, or `REQUEST_CHANGES`
- `Blocking findings`: each with snapshot evidence, why it matters, and the smallest fix; or `None`
- `Important notes`: non-blocking observations; or `None`
- `Wiki placement assessment`: duplication, provenance, evidence limits, smallest durable unit
- `Active workflow assessment`: trigger/skip clarity, ceremony risk, Direct-path preservation, safety/authorization boundaries
- `Safety boundary assessment`: credentials, runtime/config, cron, MCP/tools, gateway, wrapper, provider, profile/plugin, external/destructive effects
- `Recommended next step`: exactly one action

## Intent and boundaries

Source: KDnuggets, “Specification Engineering: The New Skill After Prompt Engineering,” Kanwal Mehreen, 2026-08-10.

Intended landing:

1. Wiki: cleaned full rendered source under `raw/articles/`; update the existing owner concept `hermes-ai-workflow-formalization-principles`; refresh its existing index description and log the action. Do not create a duplicate concept.
2. Active workflow: add one optional reference under existing `spec-driven-development` plus one owner pointer. Do not create a new workflow or default spec gate.
3. Preserve `coding-agent-workflow` Direct for clear, local, reversible work with cheap deterministic verification.
4. Article benchmark/research numbers remain secondary-source claims, not Hermes thresholds.
5. No memory, runtime/config, cron, MCP, gateway, wrapper, provider, profile/plugin, credential, dependency, external-service, deployment, or destructive changes.

## Deterministic evidence before review

- Wiki health: PASS, P0=0, P1=0, P2=0; formal pages=114; index wikilinks=114.
- Wiki `git diff --check`: PASS.
- Raw hash manifest: added one source, changed zero existing raw hashes.
- Targeted `spec-driven-development` contract validation: PASS; line_count=77; local links valid; deep reference scan covered 4 Markdown files.
- Active backup: `/home/lin/.hermes/backups/specification-engineering-20260818_160606`.
- `skill_manage` write was blocked by false-positive scanning of an unrelated existing reference; the exact authorized reference and pointer were therefore written directly under the active skill with backup/diff/readback.

## Wiki raw-source snapshot

Frontmatter and provenance:

```markdown
---
title: Specification Engineering: The New Skill After Prompt Engineering
author: Kanwal Mehreen
source: KDnuggets
source_url: https://www.kdnuggets.com/specification-engineering-the-new-skill-after-prompt-engineering
published: 2026-08-10
captured: 2026-08-18
type: raw-source
status: raw
tags: [llm, ai-coding, workflow, software-engineering]
extraction: full rendered article body from div#post-, with promotional and related-post boilerplate removed
---
```

The source note records the browser DOM route, full-body quality, cleaned-text limitation, local Chinese summary path, and this boundary:

> Research figures and vendor claims remain secondary-source statements and require checking against the cited papers or official reports before becoming normative Hermes rules.

The body preserves the full article argument, eight suggested specification fields, benchmark/research claims, spec-driven coding example, six-step workflow, and author bio; only promotional inserts and “More On This Topic” boilerplate were removed.

## Existing concept delta

Existing owner: `concepts/hermes-ai-workflow-formalization-principles.md`. Added source and updated date, then inserted:

```markdown
## Principle 2.6: specification is an agreement, not an eight-field ritual

`[[kdnuggets-specification-engineering-2026-08-10]]` 把 prompt 与 specification 的边界说得更直接：prompt 解决“如何提问”，specification 解决“参与者如何共同判断做对了”。可复用的最小检查面是目标、必要上下文与输入、输出契约、约束、验收标准、边缘情况和验证方式；但这些是风险检查面，不是每个任务必须填写的固定模板。

Hermes 映射：
- 需求、边界或验收不清，或任务跨模块、跨会话、跨 agent、涉及 active/high-risk surface 时，进入 `spec-driven-development`；
- 规格草案应让 AI 指出缺失条件，但生成者的自检不能替代独立测试、结构化校验或人工判断；
- 只针对失败的验收项定向修正，并记录最终假设、已知局限和 contract 变化；
- 明确、局部、可回滚且有便宜确定性验证的小修继续走 `coding-agent-workflow` 的 Direct 路径，不为形式完整度增加仪式。

证据边界：原文是二手工程综述；ROPE、SWE-bench/SWT-Bench 和 DORA 数字在成为强制门禁或本地阈值前，需要回到原论文或官方报告核验。
```

Index description changed only for the existing concept; formal page count remains unchanged.

## Active `SKILL.md` delta

```diff
-## Reference map
+## Reference Map
+
+Use `references/specification-engineering-preflight.md` when an AI-assisted task needs a risk-triggered definition-of-done check without turning the full template into a default gate.
 See `references/INDEX.md`; load only the template or active-layer gate that matches the task.
```

The heading capitalization came from the existing reference-map synchronizer.

## New active optional reference snapshot

```markdown
# Specification Engineering Preflight

Use this optional preflight when an AI-assisted coding task needs a shared definition of “done correctly” before implementation.

## Trigger

Use it when one or more are true:

- requirements, constraints, interfaces, edge cases, or acceptance criteria are unclear;
- work crosses modules, sessions, agents, or an active/high-risk surface;
- a plausible-looking output could satisfy visible checks while violating an implicit business or safety constraint;
- the implementation will be delegated and needs a stable handoff contract.

## Skip

Skip it for clear, local, reversible work with a known owning seam, cheap deterministic verification, and no unresolved contract or high-risk side effect. Use the `coding-agent-workflow` Direct path instead.

## Smallest useful preflight

Capture only the fields needed to remove implementation guesswork:

- objective and user/business outcome;
- necessary context, allowed inputs, and owning source of truth;
- output or interface contract;
- constraints, forbidden actions, and non-goals;
- acceptance criteria and the closest relevant edge cases;
- verification owner and evidence;
- rollback or stop conditions when failure has material cost.

Then ask the drafting agent to identify missing or conflicting requirements. Treat that answer as a hypothesis: resolve decision-changing gaps with repository evidence or the user, and do not let self-review replace independent tests, structured validation, or human judgment.

During execution, revise only against failed acceptance evidence. If required behavior changes, update and re-approve the contract before changing implementation. Record final assumptions and known limitations in the owning spec, ADR, or project documentation.

## Evidence boundary

The checklist is a bounded adoption of “specification engineering,” not a mandatory eight-field template. External articles and benchmark figures are supporting rationale, not Hermes thresholds or proof that every task needs a saved spec.

## Verification

- The preflight made decision-relevant ambiguity explicit.
- Acceptance criteria are executable or clearly labeled human judgment points.
- The task still has one primary execution path.
- Small Direct work was not escalated merely for template completeness.
```

## Review questions

1. Does the Wiki update belong in the existing formalization concept rather than a new concept or `agent-context-engineering`?
2. Does the active reference add a real, bounded operational delta without duplicating the full spec template or creating an always-on gate?
3. Are trigger and skip rules sufficiently aligned with the existing Direct-vs-Spec boundary?
4. Is “revise only against failed acceptance evidence” too absolute, or is it safely bounded by the following contract-change sentence?
5. Are source limitations and non-promotion boundaries explicit enough?
6. Is any smallest correctness/safety fix required before closeout?
