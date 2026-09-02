---
title: "How Warp builds self-improving agents on Claude"
created: 2026-09-02
updated: 2026-09-02
type: raw-source
tags: [agent, skills, feedback-loop, self-improvement, governance, human-in-the-loop, pull-request]
source: Claude by Anthropic
source_url: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
author: Michael Segner
published: 2026-08-26
captured: 2026-09-02
status: captured
extraction: "Structured complete capture compiled from the public Claude page and cross-checked against the Karakeep-backed gsummary source packet; it preserves every substantive section and finite list but is not a verbatim mirror. Navigation, related posts, subscription UI and footer were omitted. Local summary: ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260902-183412-How-Warp-builds-self-improving-agents-on-Claude-https-claude.com-blog-how-warp-b-2860662-862153320-summary.md"
---

# How Warp builds self-improving agents on Claude

## Provenance

- Publisher: Claude by Anthropic
- Author: Michael Segner
- Published: 2026-08-26
- Captured: 2026-09-02
- Source URL: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
- Extraction route: structured capture from the public-page extraction, cross-checked against the full Karakeep capture used by `gsummary`.
- Source quality: complete structured capture of the substantive sections and finite lists; not a verbatim article mirror.
- Limitations: this is an Anthropic-published customer case based on Warp's account. Company scale and usage figures are self-reported. The article gives no controlled comparison, accuracy improvement, bad-edit rate, reviewer-time cost, or long-term regression data for the self-improvement loop; it supports a design pattern and operating lessons, not unattended production self-modification.
- Local summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260902-183412-How-Warp-builds-self-improving-agents-on-Claude-https-claude.com-blog-how-warp-b-2860662-862153320-summary.md`

## Structured source capture

*In our series, we highlight how startups are transforming their industries with AI. In this article, we share how Warp turned stateless user feedback into a self-improvement loop for its agents.*

## The quick pitch

- Name: Warp
- Founded: 2020
- Founder: Zach Lloyd (CEO)
- Stack: Rust, Golang, GitHub Actions, internal agent orchestration platform (Oz), Claude Platform
- Growth reported by the article: $73M raised; 800K monthly developers; 56% of the Fortune 500 uses Warp; 10M Claude Code sessions inside Warp to date and 400K+ per week; 40M total Warp Agent conversations.

Agents need to handle recurring tasks reliably and effectively. A first-pass prompt that gets 80% of the task correct can create a noisy and annoying experience for the user. Warp learned this the hard way and used it to inform its product strategy.

Warp, the AI-powered terminal and agentic development environment, builds on the Claude Platform. The team ran into this noisy-experience problem with its internal code-review agent: engineers complained that it made unhelpful comments and produced low-quality output.

The team initially tried stopgap solutions, such as manually rewriting the prompt based on observed code-review failures. This made output more usable but did not scale. Improving context files such as `AGENTS.md` also helped but was not a complete fix.

Warp concluded that feedback to an agent typically disappears when the session ends, removing critical context from the agentic loop. Its response was an Agent Skills-based framework in which feedback compounds over time to refine agent output.

## Agent self-improvement loops built on skills

The central technique is a self-improvement loop using skills: file-based encodings of knowledge that keep instructions out of the raw prompt. Warp's architecture consists of two skills with human feedback between them.

The **inner/base skill** holds functional domain knowledge and instructions. For example, when a pull request opens, Warp's code agent uses the base skill and task context to produce a review.

**Human feedback** on the output is critical. A person can affirm that a comment was useful, but detailed reasons are more valuable. A correction such as “you suggested renaming this variable, but our codebase convention uses this naming context for this kind of global variable” tells the agent how to handle the case next time.

The **outer/improver skill** acts as an observer agent that runs on a schedule rather than per task. It pulls accumulated feedback, compares what the agent suggested with how humans responded, and proposes a small, focused edit to the base skill.

Because skills are plain files, these changes are reviewable, approvable and mergeable through a normal pull-request and code-review workflow. Only after a change is merged does the next run of the inner skill inherit it.

Warp applies the pattern to spec-writing, review and triage agents in its open-source repository. Zach Lloyd describes file-based skills as a way to encode knowledge outside the prompt so agents can look it up while working; the base skill carries domain knowledge and the improver refines it.

## How to write self-improving skills for agents

Warp gives six recommendations:

1. **Write principles, not rules.** Instruct a smart reasoner rather than exhaustively programming every case. “Look for repeated code” can generalize better than a long list of naming rules.
2. **Explain the why.** Rationale lets the agent reason and generalize instead of mechanically applying rigid instructions.
3. **Make feedback effortless to give.** Capture it where people already work, such as directly in pull requests or issues, without a separate submission step.
4. **Keep skills small and use progressive disclosure.** A skill should reference resource files and scripts instead of dumping everything into context.
5. **Feedback quality is more important than volume, though volume helps.** Detailed domain feedback from a senior engineer can be worth more than many binary votes because it explains why.
6. **Put extra effort into the improver skill.** The observer mechanism can be reused across domains even when base skills contain different specialist knowledge.

## The loop in action: Warp's issue-triage agent

Warp's issue-triage example starts when a new GitHub issue triggers an agent through GitHub Actions. The agent analyzes complexity and feasibility, assigns labels, and suggests a direction for a fix. Its inner skill defines the labels and how to research the codebase.

In one case, the first-stage agent omitted the `ready to spec` label, which indicates that contributors can begin product and technical specifications. A maintainer left feedback on the issue explaining both the expected label and the reason it applied.

The outer improver runs on Warp's Oz orchestration platform as a scheduled `update triage` agent. It authenticates to GitHub, runs a Python script bundled with the skill to collect recent issues containing feedback, summarizes them into JSON, and reads the result into context. Bundling the retrieval script avoids writing fresh code on every run.

The improver identified the feedback signal and proposed the smallest edit that captured it. It opened a pull request changing the inner skill so that an issue describing a real problem receives `ready to spec` even when the exact UI or UX has not yet been defined.

The pull request explained which feedback triggered the change and what it altered. A human reviewed, approved and merged it; subsequent triage runs inherited the updated knowledge. Human control over the final merge closes the loop.

## Best practices from the Warp team

- **Do not conflate skills with memory.** Skills are procedural and stable—how to do something, independent of a particular run, and changed deliberately. Memory is written during inference and changes continuously.
- **Do not necessarily create one improver per agent.** Use a templated base mechanism for shared logic and layer domain-specific weighting on top. A few agents can have dedicated improvers; a large fleet should share mechanisms.
- **Assume some feedback is wrong.** Do not accept it blindly. Give the improver context for sanity-checking, filter whose input counts, and retain a person in either the filtering or final-review stage.
- **Build the verification harness first when the domain is verifiable.** Create a reference corpus, compare output with the reference, fix and repeat.
- **Use deterministic evaluations and expert feedback when the domain is not fully verifiable.** Restrict subjective feedback to domain experts rather than accepting every signal.
- **Track system-level outcomes.** Warp suggests measures already watched by humans, such as time to merge, contributor count and cost, and recommends crawl-walk-run deployment.

The article concludes that agents can improve over time when systems capture human feedback, turn it into skill updates and keep a human in control of what actually changes.
