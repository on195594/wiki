---
title: "How the Claude Code team does code review"
author: [Addy Osmani, Morgan Westlee Lunt, Qing Wang]
publisher: Anthropic (claude.dev Blog)
published: 2026-10-15
created: 2026-10-18
updated: 2026-10-18
type: raw-source
status: captured
tags: [agent, ai-coding, claude-code, workflow, governance, validation, verification]
sources: [https://claude.dev/blog/solving-code-review-at-anthropic/]
source_url: https://claude.dev/blog/solving-code-review-at-anthropic/
extraction_route: direct_webpage_text
source_quality: full
capture_scope: selected-paraphrased-source-note-with-original-excerpts
---

# How the Claude Code team does code review

## Provenance and capture scope

- Original: [How the Claude Code team does code review](https://claude.dev/blog/solving-code-review-at-anthropic/), by Addy Osmani, Morgan Westlee Lunt, and Qing Wang, published 2026-10-15 on the `claude.dev` Engineering blog (14 min read).
- Retrieved 2026-10-18 by direct webpage text extraction. The readable original covers the lead through "Where this is going", including the seven-layer review architecture, risk-tier table, reviewer evaluation loop, review-convergence metrics, and team adoption guide. Site navigation, newsletter prompts, and related-post cards are omitted. Diagram captions and text labels (`FIG A` through `FIG E`) were readable in the extraction, while diagram image pixels were not independently inspected.
- This file is a selected, paraphrased source note with attributed original-English excerpts, not a full-article mirror, verbatim snapshot, or generated-summary substitute. `source_quality: full` describes the retrieved input text, not the completeness of this note.
- Evidence boundary: first-party vendor engineering retrospective describing internal practices on the Claude Code repositories at Anthropic. Reported throughput, revert-share, comment-rate, and convergence figures are internal organizational observations without public raw datasets or controlled external replication. Linked blog posts, GitHub Actions, and product documentation were not separately verified.

## Problem framing: human time and attention as the scarce resource

The article reports that Claude writes roughly 90% of Claude Code's own codebase, while changes landing per day in Anthropic's monorepo grew from about 2,500 in May 2026 to more than 30,000 in September 2026. On the separate Claude Code repository, merged pull requests more than doubled from June to September 2026 while the share of PRs that had to be reverted fell by more than 40%.

At that volume, manual line-by-line review of every diff becomes a bottleneck. The authors separate code review into two jobs:

1. Finding and fixing issues before they ship.
2. Building shared context and codebase understanding across the team.

Rather than treating human line-reading as the definition of review, the team reframes the question:

> We think "did a human read the code?" is an imprecise proxy for "what could go wrong with this change, and which check—automated or human—is the right one to catch it?"

Human time includes both reviewing diffs and fixing production breakages caused by bad merges. The team's stated target across Claude Code repositories (CLI, desktop, web, and mobile apps) is that most PRs merge with at most one human in the loop—who can be the author—without raising reverts or incidents. They track human approvals per PR (median and 95th percentile), human comments, and time a PR waits on a person, using revert and incident rates as the guardrail.

## Seven layers of defense in depth ("Layers, not one gate")

### 1. Pre-PR verification and source-level instruction updates

Most review happens before a PR is opened. The authoring agent is given executable checks—tests, a build, a linter, or a UI screenshot comparison against design guidelines—and asked to show the output rather than merely claiming completion. A second subagent then reviews the diff in a fresh context, supplemented by internal skills for bug hunting, diff simplification, and end-to-end behavior checks.

> "Verification looks different for each domain. It might be as simple as running a bash command, or running a test suite, or testing the app in a browser or phone simulator."

When the automated reviewer repeatedly flags the same issue, the team fixes it at the source via skills, lint rules, or two repository instruction files:

- `CLAUDE.md`: kept short in large repositories (pointing to deeper docs), covering stack, conventions, goals, and non-goals. Every review loads it, flags code that breaks its conventions, and flags changes that leave a line in `CLAUDE.md` out of date.
- `REVIEW.md`: written by code owners to define what matters in their area. Effective `REVIEW.md` files stay short, state what failure looks like in that repository (for example, "it lies" for docs or "it misroutes" for config), cap nits, list paths to skip, require a specific file and line as evidence instead of guessing from names, and ask for a summary that starts with a finding count and states plainly when nothing needs fixing. The team checks separately whether the reviewer actually follows `REVIEW.md`.

### 2. Multi-agent AI review on every pull request

Every PR receives a Claude review against the full repository and the PR's stated intent (`Quick`, `Standard`, or `Deep` depth configured per repo; `Deep` is reserved where a missed bug costs more than extra review latency). After launching the internal research preview, the share of internal PRs receiving substantive review comments rose from 16% to 54%; most PRs over 1,000 lines get findings, while most small ones return clean.

To control false positives before humans read comments:

- Multiple agents hunt for bugs in parallel.
- A separate verifier group votes on each candidate finding; a finding is posted only when enough verifiers agree it is real.
- Style-only, diagnostic, or cleanup findings are dropped (retained after A/B testing on internal PRs).
- Surviving findings appear as inline comments sorted by severity and tagged `Important`, `Nit`, or `Pre-existing` (so pre-existing bugs are not blamed on the PR author).
- Every finding must be answered by either fixing it or resolving the thread with a reason; overnight agents often pick up fixes automatically.

### 3. Security review that can block

A separate automated security review pass runs alongside bug review (available publicly via the open-source security review GitHub Action or `/security-review`). A PR cannot merge while any finding from either the bug review or the security review remains open. Authors clear false positives by closing the thread with a short reason; if a subsequent commit fixes the issue, the finding clears automatically.

### 4. Automated CI checks that block

Platform-wide lint, type checks, test suites, builds, and packaging block merge on failure. The PR template asks how the change was tested and how to undo it; Claude can draft those fields, but the human who requested the change signs off on them.

### 5. Human approval scaled by risk

Risk tiers are assigned from the change itself rather than the author:

| Risk tier | Source examples | Required human approvals |
|---|---|---|
| Low | Docs, copy, internal-only features, additive changes behind a feature flag | None required once automated review and security checks are green |
| Medium | Ordinary product changes, and changes to sensitive areas such as caching, the auto-updater, or system prompts | One person |
| High | Highest-risk code, plus a small set of sensitive/CI workflow paths that always need two people | Two people |

Governance constraints on risk-tiered approval:

- **Change-driven classification**: one classifier selects the risk tier from the diff, and a second classifier checks whether a low-tier change still warrants another human reviewer. Owner-designated sensitive paths and any CI workflow file always require a person.
- **Trusted-author restriction**: lighter approval paths apply only to authors on the repository's trusted list (primarily the owning team); all other authors require a second human approver.
- **No bot substitution**: an agent's approval never counts toward a required human approval slot.
- **Prompting accountability**: "Whoever prompted the change is on the hook for it." On an agent-written PR, the human directing the agent counts as one of the required reviewers, just as if they had typed the code.
- **Commit-bound approval**: an approval covers one specific commit. If new commits land that the system cannot vouch for—such as an agent push or a manually resolved merge—the approval is dismissed and must be granted again.

### 6. Merge queue, feature flags, and gradual release

The merge queue re-runs all checks against the latest `main` with the change applied so individually green PRs cannot combine into a broken `main`. New behavior ships behind feature flags to Anthropic employees first for internal dogfooding, then rolls out to the public `latest` channel before the trailing `stable` channel.

### 7. Fast detection and fast rollback

Feature flags disable behavior without a redeploy, supported by a weekly on-call rotation and post-incident reviews that ask which layer should have caught the regression. The authors note an explicit current gap: they do not yet have automated circuit breakers that tighten approval rules when revert or incident rates move, and engineers want those in place before expanding zero-human merges further.

## Improving the reviewer: incident evals, noise tracking, and convergence

### Incidents as a daily regression eval

The team collected historical PRs that caused incidents or reverts, had domain engineers confirm each bug and its location, and runs the reviewer against that eval set daily. Changes to reviewer prompts, tools, or models are kept only if the eval score improves.

### Measuring noise via author actions and clean-PR runs

Every reviewer comment is categorized by how the human on the PR responded: fixed it, said it was wrong, said the behavior was intentional, or decided it did not matter. The team also runs the reviewer on PRs known to be clean and counts how often it reports something that would lead to a harmful change. Noise is more expensive when the author is an agent: while a human can wave off a nit in seconds, an agent fixes it, creating another commit and another review round.

### Forcing review convergence

An agent author and an agent reviewer can loop indefinitely—one internal CLI PR ran through more than 50 review-and-fix rounds overnight before its author stopped it. Running `git blame` on repeated late-round findings showed that roughly 59% of flagged lines had been present since the reviewer's first pass; the reviewer was surfacing older issues each round rather than regressions introduced by the fixes.

The team now tracks rounds-to-pass alongside recall and changed re-review behavior in four ways:

1. **Three-round cap**: after three rounds, the reviewer asks the author to step back and reconsider the approach.
2. **Diff-only re-review**: after the first few passes, re-review inspects only the new diff.
3. **Bug-class flagging**: flag the class of bug so the author fixes every instance at once rather than one line per round.
4. **No duplicate findings**: never repeat findings already posted.

Nightly review agents also scan existing repository code outside PRs so older bugs are caught asynchronously. Author-reported internal convergence results before and after these changes:

- Pass after one review-and-fix round: `65%` → `78%`.
- Need five or more rounds: `8.9%` → `1.5%`.
- Mean reviews to pass: `2.08` → `1.32`.

## Where humans stay in the loop and how context spreads

Human attention focuses on five decisions where automated checks remain weak:

1. **Should we build this at all?** Direction, taste, and scope—including keeping human review on external-team PRs and raising alternative directions early in open Slack threads rather than as late blocking comments on finished PRs.
2. **Risky code** such as billing, the auto-updater, and CI workflows.
3. **Architecture** that establishes patterns others will copy.
4. **Reading the evidence**: test output, executed commands and outputs, screenshots, and reviewer findings. If a reviewer cannot state what the automated checks would miss, they should request a real review rather than giving a quick approval.
5. **Owning the outcome ("You land it, you own it")**: supported by small diffs, reversible flags/staged releases, blast-radius-scaled scrutiny, fast telemetry, and blame-free incident reviews focused on system layers.

For code review's second job—spreading codebase understanding—nobody is expected to hold the entire codebase in their head by reading every diff. Instead, engineers ask Claude to generate an on-demand explainer or a small visual learning artifact for the specific module slice they are about to modify, complemented by defaulting to open Slack channels where work is visible in flight.

## Reusable interpretation and limits

**[推论]** Treat high-throughput code review as a defense-in-depth pipeline with an explicit outcome guardrail: shift routine defect and style detection into pre-PR self-verification, repository instruction files (`CLAUDE.md` / `REVIEW.md`), and multi-agent consensus PR checks, while binding human approval depth to change blast radius, author trust, and commit identity.

**[推论]** Whenever both the author and reviewer are agents, enforce explicit convergence bounds (round caps, incremental diff re-review, bug-class aggregation, and non-repetition) and measure comment noise alongside recall so automated review does not degenerate into multi-round churn.

The article does not justify removing human approval in repositories that lack blocking CI/security gates, merge queues, feature flags, staged rollouts, fast rollback, and revert/incident monitoring. Knowledge capture does not authorize changing repository branch protection, active Skills, runtime permissions, or deployment gates.

## Knowledge owner

- [[hermes-ai-workflow-formalization-principles]] owns the layered review architecture, risk-scaled approval boundaries, review convergence rules, and human-in-the-loop responsibilities.
- [[agent-self-validation-loops]] owns pre-PR target, feedback, and stop-condition verification loops.
- [[agent-failure-closed-loop-evaluation]] owns converting production incidents and reverts into regression evaluation cases.
- [[loop-engineering-hermes-agent-workflow]] owns bounded repair loops and maker-checker separation.
