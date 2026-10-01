---
title: "Kill the code review theater, keep the review"
author: Ankit Jain
source: The New Stack
source_url: https://thenewstack.io/kill-code-review-theater/
published: 2026-09-30
captured: 2026-10-01
type: raw-source
status: captured
tags: [ai-coding, workflow, governance, validation]
---

# Kill the code review theater, keep the review

## Source and capture scope

- Original: https://thenewstack.io/kill-code-review-theater/
- Author: Ankit Jain; the page identifies him as Aviator's cofounder and CEO.
- Publisher: The New Stack. The page explicitly discloses that Aviator sponsored the post; it also discloses that TNS owner Insight Partners is an investor in CrewAI, one of the tools mentioned.
- Published: 2026-09-30, displayed as “Sep 30th, 2026 10:00am”; the visible timestamp does not state its timezone.
- Captured: 2026-10-01.
- Extraction route: direct extraction of the original article page; the main body from the opening retrospective through “Kill the theater,” the five-layer table, and the author/sponsorship disclosures were read in full. Navigation, subscription forms, unrelated recommendations and sponsor advertising copy are excluded from this note.
- Retrieved source quality: full readable prose. Images were represented by alt text; their visual content was not verified. Linked studies, tools and product documentation were not independently examined.
- Stored representation: structured source note, not a verbatim full-article mirror or the generated Chinese summary. The outline below paraphrases the article; follow the original URL for its exact wording.
- Evidence class: sponsored engineering opinion and author retrospective, with secondary references to studies and industry reports; no controlled evaluation of the proposed replacement workflow is provided.

## Captured source outline

### Original proposal and the missing function

The author revisits a proposal made six months earlier: combine multiple imperfect verification filters to reduce human line-by-line review. The original five layers were comparing multiple options, deterministic guardrails, human-defined acceptance criteria, permission systems and adversarial verification.

Watching teams attempt the approach led him to distinguish implementation correctness, fidelity to intent and the human question of whether the team is building the right thing. He argues that code review also spreads knowledge and builds a shared mental model, so automating its mechanics without preserving that conversation can lose a function that tests do not replace.

### Review theater

The failure pattern is an agent writing code, AI reviewers commenting, the agent revising, and a human only skimming and merging. The author calls this review theater: the visible loop exists, but the human judgment and decision context are missing. His claims that AI reads every line consistently and cannot judge what should be built are opinion-level generalizations, not measured capabilities established by this article.

### Proposed replacement: five layers

1. **Argue:** move model disagreement ahead of PR creation; retain proposed and rejected alternatives and their reasons rather than attaching a machine verdict. Humans consider unresolved decisions. The author suggests two reviewers using different models and lists PR-Agent, Aider architect mode, AutoGen and CrewAI as possible tools, not evaluated equivalents.
2. **Capture:** record both intent (why the change is made) and acceptance criteria (how it should behave), incorporating questions and corrections during implementation and publishing necessary decisions on the PR. The author criticizes static upfront specifications without a feedback loop.
3. **Codify:** distinguish judgment-dependent design feedback from repeatable mechanical corrections. Turn patterns such as currency types instead of floats, no direct writes to the users table, structured logging and error-path counters into checked invariants. His suggested starting exercise is harvesting the last 1000 review comments and converting the top 20 repeated patterns; these counts are advice, not validated thresholds.
4. **Debate:** retain human discussion on the existing PR, centered on decisions the agents surfaced and could not settle. The author proposes leaving diffs to machines; this is his recommendation, not evidence that manual code inspection is unnecessary in all contexts.
5. **Own:** define who maintains the verification invariants and the system understanding behind them before an incident. The proposed shift of responsibility to invariant-maintaining teams is the author's framing, not a demonstrated universal allocation of author, reviewer or release responsibility.

### Source-reported research and metrics

The following are the article's secondary reports, not independently verified findings of this capture:

- The 2013 Microsoft study by Alberto Bacchelli and Christian Bird classified 570 review comments: 44% of developers ranked finding defects as the leading motivation, while 14% of actual comments concerned defects. The article says the 2018 Google study covering nine million reviewed changes reached a similar conclusion. Comment shares do not directly measure the value or severity of defects prevented.
- The Faros AI 2026 report reportedly covered 22000 developers across more than 4000 teams, with incidents per PR up 242.7%, bugs per developer up 54%, work restarts up 13.8%, and PRs merged without human or agent review up 31.3%. This page does not establish comparison baselines, causality or a denominator for the last increase.
- The article describes the DORA 2025 report as showing a tension between increased delivery throughput and increased delivery instability with AI adoption.
- Peter Naur's 1985 “Programming as Theory Building” is invoked to explain why losing a team's understanding can undermine continued system maintenance.

## Referenced evidence for future verification

- Microsoft study: https://ieeexplore.ieee.org/document/6606617/
- Google study: https://research.google/pubs/modern-code-review-a-case-study-at-google/
- Faros AI report: https://www.faros.ai/research/ai-acceleration-whiplash
- DORA report: https://dora.dev/research/2025/dora-report/
- Product-linked invariant documentation: https://docs.aviator.co/verify/concepts/invariants

## Limitations and relation

The source supports a useful distinction between automated checking and shared human understanding, but does not establish the effectiveness, cost, error independence or long-term maintainability of its five-layer workflow. Sponsorship and author affiliation should remain visible when interpreting product-linked claims. Model agreement is not independent verification; rejection of static specifications does not justify removing necessary specifications, approvals or manual inspection of high-risk code.

The bounded concept interpretation lives in [[hermes-ai-workflow-formalization-principles]]. This capture does not change active Skills, permissions, deployment gates or runtime automation.
