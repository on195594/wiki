---
title: Hermes Harness Profile Validation Detailed Plan
created: 2026-04-30
updated: 2026-04-30
type: query
tags: [hermes, optimization, harness, model-profiles, validation, workflow]
sources: [queries/hermes-system-model-specific-harness-optimization-plan.md, concepts/hermes-model-specific-harness-profiles.md, docs:hermes-agent, skill:writing-plans, skill:hermes-project-and-extension-management]
status: draft
---

# Hermes Harness Profile Validation Detailed Plan

> **For Hermes:** Use this plan as a staged validation project. Do not change Hermes core, runtime profile, global SOUL, memory, or active cron until the validation evidence says so.

**Goal:** Validate whether model-specific harness overlays can improve your Hermes workflows without bloating global prompts or destabilizing the current `default` profile.

**Architecture:** Create a small evidence-gathering project under `/home/lin/.hermes/projects/hermes-harness-profile-validation`. The project compares baseline prompts/workflows against narrow overlays for four representative Hermes tasks: coding/config, article summary, code review, and planning. Promotion is gated: wiki → project evidence → skill patch → wrapper/quick command → cron/profile only if repeated evidence supports it.

**Tech Stack:** Hermes Agent CLI, local wiki at `/home/lin/wiki`, Python 3.12/uv if scripts are needed, Markdown docs, shell scripts for verification, optional `delegate_task` for isolated evaluation runs.

---

## 1. Executive Summary

LangChain 的 Deep Agents 文章证明了一件事：Agent 的表现不只取决于底层模型，还取决于外部 harness。对 Hermes 来说，harness 不是单个 profile 文件，而是由以下层共同构成：

- system/developer 规则
- memory / user profile
- skills
- project-local `AGENTS.md`
- wrapper scripts / quick commands
- tool choice / tool naming
- subagent delegation pattern
- verification commands
- cron entrypoints
- wiki / project state

本计划的核心建议是：**不急着新增 runtime profile，而是先建立可验证的 harness overlay 机制。**

最终希望得到三个结果：

1. 明确哪些 Hermes 高频 workflow 需要模型/任务特化 overlay。
2. 用小型 eval 证明 overlay 是否真的有效。
3. 只把有效 overlay 提升到窄职责 skill、wrapper、cron 或 runtime profile。

---

## 2. Scope and Non-Scope

## 2.1 In Scope

本计划覆盖：

- 创建一个 Hermes-adjacent 验证项目。
- 设计 baseline vs overlay 的对比任务。
- 编写 evaluation rubric。
- 用真实或半真实任务验证 overlay 是否提升结果。
- 根据证据决定是否 patch 现有 skill。
- 形成后续是否需要 runtime profile / cron 的决策依据。

## 2.2 Out of Scope

本阶段不做：

- 不修改 Hermes core 源码。
- 不新增 `lab` / `claude` / `gemini` runtime profile。
- 不修改全局 `SOUL.md`。
- 不把模型差异写进 memory。
- 不创建新的长期 cron。
- 不把本计划直接升级成 skill。

---

## 3. Current Baseline

现场 baseline：

- Hermes config check：通过。
- Config version：22。
- 当前 Hermes profile：只有 `default`。
- 当前模型：`gpt-5.5`。
- Provider：OpenAI Codex。
- Gateway：running。
- 主要入口：Telegram。
- 本地 wiki：`/home/lin/wiki`。
- 相关 project workspace：`/home/lin/.hermes/projects/`。

这说明系统目前稳定，不应该为了实验牺牲主路径。

---

## 4. Design Principles

## 4.1 Default profile stays stable

`default` 是当前主脑，不作为 prompt/profile 实验场。所有实验先在 project 层做。

## 4.2 Overlay before core change

优先顺序：

1. Project-local prompt / AGENTS.md。
2. Wrapper script / quick command。
3. Narrow skill patch。
4. Cron automation。
5. Runtime profile。
6. Hermes core change。

越靠后，证据门槛越高。

## 4.3 Eval before promotion

任何 overlay 进入 skill 或 cron 前，必须至少经过：

- 1 个 baseline run。
- 1 个 overlay run。
- 明确 rubric 评分。
- 结论：keep / revise / discard。

## 4.4 Keep model knowledge out of memory

模型行为差异不是 memory。它们属于：

- wiki concept
- project validation docs
- skill implementation details
- wrapper prompt templates

## 4.5 Verification is part of harness

一个 overlay 如果只让回答“更像样”，但没有提高验证率、 grounding、可复盘性，就不应该推广。

---

## 5. Target Project Structure

项目路径：

`/home/lin/.hermes/projects/hermes-harness-profile-validation`

建议文件结构：

```text
/home/lin/.hermes/projects/hermes-harness-profile-validation/
├── README.md
├── AGENTS.md
├── .gitignore
├── docs/
│   ├── project-brief.md
│   ├── validation-plan.md
│   ├── overlay-registry.md
│   ├── scoring-rubric.md
│   ├── promotion-policy.md
│   ├── next-questions.md
│   ├── adr/
│   │   └── 0001-project-boundary.md
│   └── experiments/
│       ├── TEMPLATE.md
│       ├── 001-coding-config-baseline.md
│       ├── 002-coding-config-overlay.md
│       ├── 003-article-summary-baseline.md
│       ├── 004-article-summary-overlay.md
│       ├── 005-code-review-baseline.md
│       ├── 006-code-review-overlay.md
│       ├── 007-planning-baseline.md
│       └── 008-planning-overlay.md
├── prompts/
│   ├── baseline/
│   │   ├── coding-config.md
│   │   ├── article-summary.md
│   │   ├── code-review.md
│   │   └── planning.md
│   └── overlays/
│       ├── codex-coding-config.md
│       ├── gemini-article-summary.md
│       ├── claude-code-review.md
│       └── codex-planning.md
├── fixtures/
│   ├── coding-config/
│   ├── article-summary/
│   ├── code-review/
│   └── planning/
└── scripts/
    ├── verify-project.sh
    └── score-experiment.py
```

---

## 6. Workstream A — Bootstrap the Validation Project

### Task A1: Check whether project path already exists

**Objective:** Avoid overwriting an existing validation workspace.

**Files:**

- Inspect: `/home/lin/.hermes/projects/hermes-harness-profile-validation`

**Command:**

```bash
test -e /home/lin/.hermes/projects/hermes-harness-profile-validation && echo EXISTS || echo ABSENT
```

**Expected:**

```text
ABSENT
```

If it exists, stop and inspect before writing.

### Task A2: Create project skeleton

**Objective:** Create the directory structure without touching Hermes core.

**Files:**

- Create directory tree under `/home/lin/.hermes/projects/hermes-harness-profile-validation`

**Command:**

```bash
mkdir -p /home/lin/.hermes/projects/hermes-harness-profile-validation/{docs/adr,docs/experiments,prompts/baseline,prompts/overlays,fixtures/{coding-config,article-summary,code-review,planning},scripts}
```

**Verification:**

```bash
find /home/lin/.hermes/projects/hermes-harness-profile-validation -maxdepth 3 -type d | sort
```

Expected: all directories above appear.

### Task A3: Write `README.md`

**Objective:** Make project purpose and boundary obvious.

**File:**

- Create: `/home/lin/.hermes/projects/hermes-harness-profile-validation/README.md`

**Content:**

```markdown
# Hermes Harness Profile Validation

This project validates whether model-specific harness overlays improve Hermes workflows.

## Boundary

This is an evidence-gathering project. It does not modify Hermes core, runtime profiles, global SOUL.md, memory, or cron by default.

## Current hypothesis

Hermes can improve reliability by adapting prompt/tool/verification overlays to workflow and model family before changing runtime profiles.

## Validation lanes

1. Coding/config
2. Article summary
3. Code review
4. Planning

## Promotion path

wiki → project evidence → narrow skill patch → wrapper/quick command → cron/runtime profile only after repeated evidence.
```

**Verification:**

```bash
test -s /home/lin/.hermes/projects/hermes-harness-profile-validation/README.md
```

### Task A4: Write `AGENTS.md`

**Objective:** Set project-local agent rules.

**File:**

- Create: `/home/lin/.hermes/projects/hermes-harness-profile-validation/AGENTS.md`

**Content:**

```markdown
# AGENTS.md

## Project boundary

- Do not modify Hermes core from this project.
- Do not modify global SOUL.md.
- Do not modify Hermes runtime profiles.
- Do not create cron jobs.
- Do not store secrets in this repository.
- Any proposed skill patch must be documented first in `docs/promotion-policy.md` and backed by experiment records.

## Validation discipline

For each experiment:

1. Record the exact input.
2. Record baseline prompt and overlay prompt.
3. Record observed behavior.
4. Score against `docs/scoring-rubric.md`.
5. Decide: keep, revise, or discard.

## Evidence standard

A change is not considered better unless it improves at least one measurable criterion without regressing safety, verification, or layer routing.
```

**Verification:**

```bash
grep -q "Do not modify Hermes core" /home/lin/.hermes/projects/hermes-harness-profile-validation/AGENTS.md
```

### Task A5: Write `.gitignore`

**Objective:** Prevent logs, caches, secrets, and run artifacts from being committed accidentally.

**File:**

- Create: `/home/lin/.hermes/projects/hermes-harness-profile-validation/.gitignore`

**Content:**

```gitignore
.env
.env.*
*.key
*.pem
*.token
__pycache__/
.pytest_cache/
.ruff_cache/
.cache/
runs/
logs/
tmp/
*.log
*.sqlite
*.db
```

**Verification:**

```bash
grep -q "^.env" /home/lin/.hermes/projects/hermes-harness-profile-validation/.gitignore
```

---

## 7. Workstream B — Define Core Project Documents

### Task B1: Write `docs/project-brief.md`

**Objective:** Capture problem, hypothesis, risks, and success criteria.

**File:**

- Create: `docs/project-brief.md`

**Required sections:**

```markdown
# Project Brief

## Problem
Hermes currently has strong general execution rules, but model/workflow-specific harness differences are mostly implicit.

## Hypothesis
Narrow overlays for high-frequency workflows can improve reliability more safely than global prompt expansion or runtime profile proliferation.

## Success criteria
- At least four workflow lanes have baseline and overlay prompts.
- Each lane has one baseline and one overlay experiment.
- Overlay improvements are measured with a shared rubric.
- Promotion decisions are evidence-based.

## Risks
- Prompt bloat without measurable improvement.
- Skill pollution.
- Overfitting to one example.
- Runtime profile proliferation.
- Accidentally encoding temporary behavior into memory.
```

**Verification:**

```bash
grep -q "## Success criteria" docs/project-brief.md
```

### Task B2: Write `docs/overlay-registry.md`

**Objective:** Create the first version of the harness overlay registry.

**File:**

- Create: `docs/overlay-registry.md`

**Required content:**

```markdown
# Overlay Registry

## Default / OpenAI Codex / gpt-5.5

### Intended use
Hermes default main-brain work, coding/config, system operations, planning.

### Overlay principles
- Batch independent reads/searches where possible.
- Prefer structured patching over shell text mutation.
- Verify before declaring done.
- Read files and system state before describing them.

### Candidate landing zones
- `hermes-dev-standards`
- `systematic-debugging`
- `writing-plans`
- `subagent-driven-development`

## Gemini / gsummary

### Intended use
Article and long-text Chinese summaries.

### Overlay principles
- Separate extraction from summarization.
- Preserve source limitations.
- Preserve output path.
- Use stable schema.

### Candidate landing zones
- `gemini-summary`
- `gsummary`
- `article-and-content-summarization`

## Claude / Claude Code

### Intended use
Reflection-heavy code review, planning, long-document analysis.

### Overlay principles
- Reflect after tool results.
- Use structured/XML-style instruction blocks where helpful.
- Never assert file/test state from memory.
- Prefer evidence-backed review.

### Candidate landing zones
- `claude-code`
- `github-code-review`
- `requesting-code-review`
```

**Verification:**

```bash
grep -q "Default / OpenAI Codex" docs/overlay-registry.md
```

### Task B3: Write `docs/scoring-rubric.md`

**Objective:** Make evaluation repeatable.

**File:**

- Create: `docs/scoring-rubric.md`

**Scoring model:** 0–2 points each.

```markdown
# Scoring Rubric

Each criterion is scored 0, 1, or 2.

## Criteria

1. Requirement fit
- 0: misses the task
- 1: partially satisfies task
- 2: satisfies all stated requirements

2. Grounding
- 0: claims facts without evidence
- 1: uses some evidence but misses key checks
- 2: reads or checks required sources before claims

3. Verification
- 0: no verification
- 1: partial verification
- 2: verification proves the result

4. Layer routing
- 0: writes information to wrong layer
- 1: minor layer ambiguity
- 2: respects wiki/memory/skill/project/cron boundaries

5. Output usability
- 0: vague or hard to reuse
- 1: usable with manual cleanup
- 2: directly actionable

6. Safety / reversibility
- 0: unsafe or irreversible
- 1: some safety handling
- 2: backups, clear rollback, no secrets

## Decision rule

- 10–12: candidate for promotion if repeated.
- 7–9: revise overlay and rerun.
- 0–6: discard or redesign.

A promoted overlay must not score lower than baseline on safety, verification, or layer routing.
```

**Verification:**

```bash
grep -q "A promoted overlay" docs/scoring-rubric.md
```

### Task B4: Write `docs/promotion-policy.md`

**Objective:** Prevent premature skill/profile/cron changes.

**File:**

- Create: `docs/promotion-policy.md`

**Required content:**

```markdown
# Promotion Policy

## Promotion ladder

1. Experiment note
2. Project-local prompt overlay
3. Wiki concept update
4. Narrow skill patch
5. Wrapper / quick command
6. Cron job
7. Hermes runtime profile
8. Hermes core change

## Minimum evidence

### Skill patch
- At least two successful overlay runs in the same lane.
- Clear trigger condition.
- Clear verification step.
- No skill scope expansion beyond the lane.

### Wrapper / quick command
- Stable input/output contract.
- Existing script or template passes verification.
- Failure mode is documented.

### Cron
- Method is already stable.
- Prompt is self-contained.
- Delivery target is explicit.
- Failure is observable.

### Runtime profile
- Skill/wrapper overlay is insufficient.
- Use case is high-frequency.
- Separate provider/model configuration is required.
- Rollback is documented.

## Hard stops

- Do not promote if evidence comes from one cherry-picked run.
- Do not promote if prompt length increases without measurable improvement.
- Do not promote if the change belongs in wiki but is being pushed into memory.
```

**Verification:**

```bash
grep -q "Runtime profile" docs/promotion-policy.md
```

### Task B5: Write ADR 0001

**Objective:** Record the architecture boundary decision.

**File:**

- Create: `docs/adr/0001-project-boundary.md`

**Content:**

```markdown
# ADR 0001: Validate harness overlays before changing Hermes runtime

## Status
Accepted

## Context
LangChain Deep Agents introduced model-specific Harness Profiles. Hermes has similar harness layers, but they are distributed across skills, project context, wrappers, tools, subagents, cron, and runtime profiles.

## Decision
This project validates narrow harness overlays before changing Hermes runtime profiles or core behavior.

## Consequences
- Runtime profile changes require evidence.
- Skill patches must stay narrow.
- Memory is not used for model-specific prompt knowledge.
- The default Hermes profile remains stable during validation.
```

**Verification:**

```bash
grep -q "Accepted" docs/adr/0001-project-boundary.md
```

---

## 8. Workstream C — Create Prompt Templates

### Task C1: Create baseline coding/config prompt

**File:** `prompts/baseline/coding-config.md`

```markdown
# Baseline: Coding/Config

You are asked to inspect a small project and make one configuration change.

## Task
[Insert task here]

## Output
Summarize what changed.
```

### Task C2: Create overlay coding/config prompt

**File:** `prompts/overlays/codex-coding-config.md`

```markdown
# Overlay: Codex Coding/Config

You are working in a Hermes-adjacent coding/config task.

## Rules
1. Inspect files before editing.
2. Back up any file before modifying it.
3. Prefer structured patch/edit tools over shell text mutation.
4. Batch independent reads/searches when possible.
5. After editing, run a verification command or read back the changed file.
6. Do not declare success without evidence.

## Required final output
- Files changed
- Backup path
- Verification command
- Verification result
- Remaining risks
```

### Task C3: Create baseline article summary prompt

**File:** `prompts/baseline/article-summary.md`

```markdown
# Baseline: Article Summary

Summarize the provided article or URL in Chinese.

## Input
[Insert URL or text here]

## Output
Give a concise summary.
```

### Task C4: Create overlay article summary prompt

**File:** `prompts/overlays/gemini-article-summary.md`

```markdown
# Overlay: Gemini Article Summary

Summarize the article in Chinese with source-grounding discipline.

## Rules
1. Separate extraction status from summary generation.
2. If the source is blocked or partial, state that clearly.
3. Preserve canonical URL and share URL if available.
4. Preserve wrapper output path if available.
5. Use stable sections: 一句话结论, 核心观点, 关键细节, 局限, 对我的启发, 可执行建议.

## Required final output
- Summary
- Source limitation, if any
- 全文路径
```

### Task C5: Create baseline code review prompt

**File:** `prompts/baseline/code-review.md`

```markdown
# Baseline: Code Review

Review the provided diff and identify issues.

## Input
[Insert diff here]

## Output
List findings.
```

### Task C6: Create overlay code review prompt

**File:** `prompts/overlays/claude-code-review.md`

```markdown
# Overlay: Claude-style Code Review

Review the code with evidence-first discipline.

<tool_usage>
Before making findings, inspect the relevant surrounding files or state when available. Do not infer file behavior from the diff alone if surrounding context is required.
</tool_usage>

<tool_result_reflection>
After each relevant file inspection, reassess whether the finding still holds. Drop findings that are not supported by evidence.
</tool_result_reflection>

## Required final output
- Finding
- Evidence
- Severity
- Suggested fix
- What was checked
```

### Task C7: Create baseline planning prompt

**File:** `prompts/baseline/planning.md`

```markdown
# Baseline: Planning

Create a plan for the requested Hermes improvement.

## Input
[Insert request here]

## Output
List phases and next steps.
```

### Task C8: Create overlay planning prompt

**File:** `prompts/overlays/codex-planning.md`

```markdown
# Overlay: Hermes Planning

Create a Hermes optimization plan without overreaching.

## Rules
1. Identify current state before proposing changes.
2. Separate plan from execution.
3. Do not modify Hermes core in the plan phase.
4. Route outputs to the right layer: wiki, skill, memory, project state, cron, MCP.
5. Include explicit stop conditions and promotion gates.
6. Include verification steps for every later implementation phase.

## Required final output
- Goal
- Scope / non-scope
- Current baseline
- Phases
- Tasks
- Verification
- Promotion gates
- Rollback / stop conditions
```

### Verification for C tasks

Run:

```bash
find prompts -type f | sort
```

Expected: 8 prompt files.

---

## 9. Workstream D — Create Experiment Template and First Experiment Records

### Task D1: Write experiment template

**File:** `docs/experiments/TEMPLATE.md`

```markdown
# Experiment: [ID] [Lane] [Baseline|Overlay]

## Metadata
- Date:
- Lane:
- Mode: baseline | overlay
- Prompt file:
- Input fixture:
- Runner:

## Input

```text
[Paste exact task input]
```

## Expected behavior

## Observed behavior

## Evidence

## Scores

- Requirement fit:
- Grounding:
- Verification:
- Layer routing:
- Output usability:
- Safety / reversibility:
- Total:

## Decision
keep | revise | discard

## Notes
```

### Task D2: Create 8 experiment stubs

**Files:**

- `docs/experiments/001-coding-config-baseline.md`
- `docs/experiments/002-coding-config-overlay.md`
- `docs/experiments/003-article-summary-baseline.md`
- `docs/experiments/004-article-summary-overlay.md`
- `docs/experiments/005-code-review-baseline.md`
- `docs/experiments/006-code-review-overlay.md`
- `docs/experiments/007-planning-baseline.md`
- `docs/experiments/008-planning-overlay.md`

Each stub should copy `TEMPLATE.md` and fill metadata only.

**Verification:**

```bash
find docs/experiments -maxdepth 1 -type f | wc -l
```

Expected: `9` including `TEMPLATE.md`.

---

## 10. Workstream E — Fixtures

### Task E1: Coding/config fixture

**Objective:** Create a tiny safe project where config edits can be evaluated.

**Files:**

- Create: `fixtures/coding-config/app_config.yaml`
- Create: `fixtures/coding-config/README.md`

**Fixture idea:**

`app_config.yaml`:

```yaml
app:
  name: harness-demo
  log_level: info
  retries: 2
```

Task input:

```text
Change log_level from info to debug. Back up the file and verify the final value.
```

### Task E2: Article summary fixture

**Objective:** Reuse the LangChain article summary path and share URL case.

**Files:**

- Create: `fixtures/article-summary/input.md`

**Content:**

```markdown
Share URL: https://share.google/i7rcqOBBckeuD4pf3
Canonical URL: https://www.langchain.com/blog/tuning-deep-agents-different-models
Existing summary path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260430-202136-LangChain-Tuning-Deep-Agents-to-Work-Well-with-Different-Models-355972-188762818-summary.md
Task: summarize and preserve source/output limitations.
```

### Task E3: Code review fixture

**Objective:** Create a fake diff requiring context inspection.

**Files:**

- Create: `fixtures/code-review/diff.patch`
- Create: `fixtures/code-review/src/config_loader.py`

The diff should include a small change whose correctness depends on surrounding code.

### Task E4: Planning fixture

**Objective:** Use a realistic Hermes improvement request.

**Files:**

- Create: `fixtures/planning/request.md`

**Content:**

```markdown
请基于 LangChain Deep Agents 的 Harness Profiles 原则，帮我优化 Hermes。要求不要贸然修改 Hermes core，不要污染 memory，先用小项目验证。
```

---

## 11. Workstream F — Verification Scripts

### Task F1: Write `scripts/verify-project.sh`

**Objective:** Check project structure and obvious safety issues.

**File:** `scripts/verify-project.sh`

```bash
#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "README.md"
  "AGENTS.md"
  ".gitignore"
  "docs/project-brief.md"
  "docs/validation-plan.md"
  "docs/overlay-registry.md"
  "docs/scoring-rubric.md"
  "docs/promotion-policy.md"
  "docs/adr/0001-project-boundary.md"
  "docs/experiments/TEMPLATE.md"
  "prompts/baseline/coding-config.md"
  "prompts/overlays/codex-coding-config.md"
  "prompts/baseline/article-summary.md"
  "prompts/overlays/gemini-article-summary.md"
  "prompts/baseline/code-review.md"
  "prompts/overlays/claude-code-review.md"
  "prompts/baseline/planning.md"
  "prompts/overlays/codex-planning.md"
)

for path in "${required[@]}"; do
  test -s "$root/$path" || { echo "missing or empty: $path" >&2; exit 1; }
done

if grep -R --line-number -E '(api[_-]?key|token|secret|password)\s*[:=]\s*[^[:space:]]+' "$root"   --exclude-dir=.git   --exclude='.gitignore'; then
  echo "possible secret found" >&2
  exit 1
fi

echo "verify-project: ok"
```

**Verification:**

```bash
chmod +x scripts/verify-project.sh
./scripts/verify-project.sh
```

Expected:

```text
verify-project: ok
```

### Task F2: Write `scripts/score-experiment.py`

**Objective:** Parse experiment records and print scores.

**File:** `scripts/score-experiment.py`

```python
#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

FIELDS = [
    "Requirement fit",
    "Grounding",
    "Verification",
    "Layer routing",
    "Output usability",
    "Safety / reversibility",
]


def parse_score(text: str, field: str) -> int | None:
    pattern = rf"- {re.escape(field)}:\s*([0-2])\b"
    match = re.search(pattern, text)
    return int(match.group(1)) if match else None


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: score-experiment.py EXPERIMENT.md", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    text = path.read_text()
    scores = {field: parse_score(text, field) for field in FIELDS}
    missing = [field for field, score in scores.items() if score is None]
    if missing:
        print(f"missing scores: {', '.join(missing)}", file=sys.stderr)
        return 1

    total = sum(score for score in scores.values() if score is not None)
    print(f"{path.name}: {total}/12")
    if total >= 10:
        print("decision band: promote candidate if repeated")
    elif total >= 7:
        print("decision band: revise and rerun")
    else:
        print("decision band: discard or redesign")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

**Verification:**

```bash
chmod +x scripts/score-experiment.py
python3 scripts/score-experiment.py docs/experiments/TEMPLATE.md
```

Expected: template may fail until scores are filled. That is acceptable. Run against completed experiment records later.

---

## 12. Workstream G — Run the Four Evaluation Lanes

## Lane 1: Coding/config

### Baseline run

- Prompt: `prompts/baseline/coding-config.md`
- Fixture: `fixtures/coding-config/`
- Expected weakness: may modify without backup or verification.

### Overlay run

- Prompt: `prompts/overlays/codex-coding-config.md`
- Fixture: `fixtures/coding-config/`
- Expected improvement: backup path, final readback, explicit verification.

### Promotion condition

Promote only if overlay improves verification/safety without adding unnecessary complexity.

## Lane 2: Article summary

### Baseline run

- Prompt: `prompts/baseline/article-summary.md`
- Fixture: `fixtures/article-summary/input.md`
- Expected weakness: may omit source limitation or output path.

### Overlay run

- Prompt: `prompts/overlays/gemini-article-summary.md`
- Fixture: `fixtures/article-summary/input.md`
- Expected improvement: preserves share URL/canonical URL/path and limitation.

### Promotion condition

Patch only `gemini-summary` / `gsummary` if current behavior misses these fields repeatedly.

## Lane 3: Code review

### Baseline run

- Prompt: `prompts/baseline/code-review.md`
- Fixture: `fixtures/code-review/`
- Expected weakness: review diff without enough context.

### Overlay run

- Prompt: `prompts/overlays/claude-code-review.md`
- Fixture: `fixtures/code-review/`
- Expected improvement: checks surrounding file and drops unsupported findings.

### Promotion condition

Patch review skills only if overlay reduces false positives or improves evidence quality.

## Lane 4: Planning

### Baseline run

- Prompt: `prompts/baseline/planning.md`
- Fixture: `fixtures/planning/request.md`
- Expected weakness: may jump directly to profile/core changes.

### Overlay run

- Prompt: `prompts/overlays/codex-planning.md`
- Fixture: `fixtures/planning/request.md`
- Expected improvement: separates plan from execution, includes stop conditions and layer routing.

### Promotion condition

Patch planning-related skills only if overlay produces more executable and safer plans.

---

## 13. Decision Gates

## Gate 1: Project bootstrap complete

Pass criteria:

- Project exists.
- Required docs exist.
- `verify-project.sh` passes.
- Git repo initialized with clean status.

## Gate 2: Prompt templates complete

Pass criteria:

- 4 baseline prompts exist.
- 4 overlay prompts exist.
- Each overlay has explicit verification expectations.

## Gate 3: First evaluation round complete

Pass criteria:

- 8 experiment records exist.
- All completed records have rubric scores.
- At least one overlay shows measurable improvement.

## Gate 4: Promotion decision

Pass criteria:

- Candidate overlay has at least 2 successful runs in the same lane.
- No regression in safety, verification, or layer routing.
- Candidate landing zone is identified: wiki, skill, wrapper, cron, or runtime profile.

## Gate 5: Skill patch decision

Pass criteria:

- Skill patch is narrow.
- Trigger condition is clear.
- Verification condition is clear.
- Existing skill is not turned into model encyclopedia.

---

## 14. Rollback and Safety

## File rollback

Every mutable wiki update should keep timestamped backups:

```text
/home/lin/wiki/index.md.bak.<timestamp>
/home/lin/wiki/log.md.bak.<timestamp>
```

Every project-local experiment can be rolled back with Git:

```bash
git status --short
git diff
git restore <file>
```

## Runtime safety

Do not run:

```bash
hermes profile create ...
hermes config set ...
hermes cron create ...
```

unless a later plan explicitly authorizes it and includes rollback.

## Secret safety

All API keys remain in environment files, not project docs or prompts.

---

## 15. Milestone Timeline

## Milestone 1 — Project bootstrap

Target: 1 focused session.

Deliverables:

- Project directory.
- README / AGENTS / .gitignore.
- Core docs.
- Git initial commit.

## Milestone 2 — Prompt and fixture setup

Target: 1 focused session.

Deliverables:

- 8 prompt templates.
- 4 fixture lanes.
- Experiment template.
- Verification script.

## Milestone 3 — First eval round

Target: 1–2 focused sessions.

Deliverables:

- 8 experiment records.
- Scores for baseline/overlay.
- Initial decision notes.

## Milestone 4 — Promotion review

Target: 1 focused session.

Deliverables:

- Keep/revise/discard decision for each overlay.
- Candidate skill patch list.
- No runtime/profile changes unless justified.

## Milestone 5 — Narrow implementation

Target: only after evidence.

Deliverables:

- Patch one existing skill at a time.
- Run skill-specific verification.
- Update wiki/log if principle changes.

---

## 16. Final Acceptance Criteria

The plan is successful when:

- There is a reproducible validation project.
- Four Hermes workflow lanes have baseline/overlay comparison records.
- At least one overlay has a clear keep/revise/discard decision backed by scores.
- No Hermes core/runtime/global memory pollution occurred.
- Any promoted change has a narrow landing zone and verification path.

---

## 17. Recommended Immediate Next Step

Start with **Workstream A + B only**:

1. Bootstrap project skeleton.
2. Write README / AGENTS / .gitignore.
3. Write project brief, overlay registry, rubric, promotion policy, ADR.
4. Commit the clean skeleton.

Do not run experiments until the project boundary and scoring rubric are in place.

---

## Related

- [[hermes-system-model-specific-harness-optimization-plan]]
- [[hermes-model-specific-harness-profiles]]
- [[hermes-context-layer-operating-rules]]
- [[hermes-agent-workflow-layering-and-adoption-order]]
- [[hermes-knowledge-architecture]]
- [[index]]
- [[log]]
