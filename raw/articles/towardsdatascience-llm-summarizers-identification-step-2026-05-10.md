---
title: LLM Summarizers Skip the Identification Step
author: William Gieng
source: Towards Data Science
source_url: https://towardsdatascience.com/llm-summarizers-skip-the-identification-step/
published: 2026-05-10
captured: 2026-05-16
type: raw-source
status: raw
tags: [llm, workflow, validation, risk-control]
extraction: Browser DOM extraction because web_extract returned a generated summary-like artifact and Jina Reader was inaccessible; Gemini summary output preserved at ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260516-212602-LLM-Summarizers-Skip-the-Identification-Step-147832-915777280-summary.md.
---

# LLM Summarizers Skip the Identification Step

Extraction note: Clean article text extracted from live browser DOM because generic extraction returned a generated summary.
Title: LLM Summarizers Skip the Identification Step | Towards Data Science
Author: William Gieng
Published: May 10, 2026

LLM APPLICATIONS
LLM Summarizers Skip the Identification Step

A practitioner's argument that meeting summarizers fail in the same way regressions fail when you skip the part where you ask what the data can support.

William Gieng
May 10, 2026
15 min read

A meeting summarizer takes a five-minute exchange and returns eight clean sections. Decisions. Action items. Risks. Open questions. Each section reads like it was written by someone who was paying attention.

Read the underlying transcript, though, and you find that two of those sections were inferred from a single ambiguous sentence, one was invented entirely, and three were pattern-matched from the model’s prior on what a meeting summary should contain. Confident, formatted, structurally indistinguishable from a summary of a meeting where those things actually happened.

This is not a hallucination problem in the usual sense. The model is not making up a fact about the world. It is making up a fact about the meeting. And the failure mode is not visible in the output. It is just confident-sounding text that the reader cannot easily verify against the source.

There is a name for this failure mode in another field, and it is older than language models. It is what happens when you do estimation without identification.

This article is not a new summarization benchmark. It is an argument for a design pattern that I have not seen treated as the central design constraint in AI engineering literature: treat LLM-generated summaries as structured claims over a source, require each claim to declare its support category, and constrain review stages so they can only weaken unsupported claims rather than make the output smoother. I will walk through what that looks like in practice, what it produces, and where it breaks.

The missing step

Causal inference is the analytical tradition that formalizes the difference between identifying a quantity and estimating one. Identification is the argument that the data you have can support the claim you want to make. Estimation is the procedure that produces a number once identification is settled. The order is not negotiable. You cannot estimate a treatment effect you have not first argued is identifiable from your observational data, because the resulting number is meaningless. It looks like an effect. It is not an effect.

Practitioners who work in observational settings spend a substantial fraction of their time on identification. They draw causal graphs. They argue about confounders. They distinguish between what the data can support and what the data cannot. The estimation step, when it finally comes, is often the easy part.

Now consider what an LLM summarizer does. It receives a transcript. It produces structured claims about the content of that transcript: decisions made, commitments accepted, risks raised, next steps assigned. Each claim is, in a real sense, an estimate of a latent quantity. The decision was made or it was not. The commitment was accepted or it was not. The summary is asserting a value for each of these quantities.

There is no identification step. The model does not ask whether the transcript contains enough evidence to support the claim. It produces the claim because the format calls for one.

LLM summarization behaves like observational analysis, but it is often deployed without anything resembling an identification step.

The AI engineering literature has not been silent on the underlying problem. Hallucination detection, calibrated uncertainty, selective prediction and abstention, RAG grounding, citation verification, factual consistency, and claim verification: each of these is a serious line of work, and each addresses a real layer of the failure. What they have in common is that they treat fabrication as a model behavior to be measured, scored, or suppressed after the fact.

Identification is a different layer. It does not score the output for trustworthiness. It changes what the model is allowed to assert in the first place by requiring every claim to declare what it is and where it came from. The two layers are complementary. A pipeline that does identification well still benefits from calibration and grounding work downstream. A pipeline that does only the downstream work is filtering output that should never have been produced in the form it was produced.

What identification looks like for a transcript

Identification in observational data is a question about what the data can support. Identification for a transcript is the same question, narrowed to a specific source. Given this transcript, what can be observed directly, what can be inferred with stated assumptions, and what cannot be supported at all?

That is the whole move. Every claim a summarizer produces should declare which of those three categories it belongs to. Observed claims point to a specific span of the transcript and assert nothing beyond what that span says. Inferred claims declare the assumption being made and the evidence the inference is bridging. Recommendations declare that they are the model’s suggestion, not the participants’ decision.

A summarizer that cannot place a claim into one of those categories has no business producing the claim. The right output in that case is not a smoother claim. It is no claim.

This is uncomfortable for the consumer of summaries, because it means many sections will be empty when the underlying conversation was thin. That discomfort is the point. It is information. It tells the reader that the meeting did not, in fact, produce eight sections of substance, regardless of what the summarizer wanted to write.

A pipeline that enforces the discipline

The architecture follows from the framing. Three LLM stages and a deterministic renderer.

Figure 1. Pipeline architecture: three LLM stages, one deterministic renderer.
Image by Author

The first stage extracts structured facts from the transcript. Speaker turns, explicit commitments, explicit decisions, explicit quantities. This stage is deliberately conservative. It is allowed to miss things. It is not allowed to invent them.

The second stage synthesizes those facts into claim objects across eight sections. Each claim carries a label: observed, inferred, or recommendation. Each claim carries a pointer to the evidence in the extracted facts. Synthesis is where the analytical work happens, and it is also where the model is most likely to drift.

The third stage audits. This is the stage that does the identification work, and the constraint on it is the part of the design that matters most.

The audit stage cannot rewrite the analysis into something smoother. It cannot add a better-sounding recommendation. It cannot invent missing context.

It is given a bounded set of operations and forbidden from doing anything else. It can delete a claim. It can downgrade a claim from observed to inferred, or from inferred to recommendation. It can move a claim to a more appropriate section. It can replace a claim with an explicit insufficient-evidence placeholder. It can collapse an entire section when nothing in it survives review.

Figure 2. The five operations the audit stage is allowed to apply.
Anything not on this list is forbidden, including writing better claims.
Image by Author

The replace_with_insufficient_evidence operation deserves its own line. It is the system literally typing a placeholder into the output where a confident claim used to be. That is identification work made operational. The reader sees, in prose, exactly where the synthesis stage produced a claim that the source could not support.

Why the asymmetry matters. A reviewer that is allowed to improve the analysis becomes another source of the same problem the system is trying to solve. A reviewer that is only allowed to weaken or remove can only fail in one direction: by being too cautious. That is a tolerable failure mode. The opposite is not.

What the design produces, and what it refuses to produce

This is not a benchmark. It is a small fixture-based stress test designed to check whether the architecture produces the behavior it was built to produce. Three transcripts are not enough to make general claims about LLM summarization. They are enough to check whether a specific design choice has the consequences the design predicted.

The fixtures are: a decision meeting in which a pricing model was selected among three real alternatives, a working session that surfaced a measurement problem without resolving it, and a thin two-person sync that contained almost no decision content.

What did not happen. Across the three runs, the pipeline produced zero fabricated commitments and zero ungrounded quantities. This is what the architecture is designed to make harder. A claim cannot survive the pipeline if it does not have a pointer to evidence, and the audit stage cannot manufacture evidence to keep a claim alive. The result is not a guarantee. The deterministic renderer is the only stage that gives guarantees. Extraction, synthesis, and audit are still LLM calls and can still fail. The point is that the architecture pushes their failures toward removal rather than toward fabrication, and the fixtures are consistent with that.

What did happen. The result that I find more interesting is the abstention rate.

Figure 3. Abstention rate scales with the thinness of the input signal.
Across three fixture transcripts, the share of empty section slots rose from 17% to 58%.
Across all three fixtures: 0 fabricated commitments, 0 ungrounded quantities.
Image by Author

On the rich decision meeting, the pipeline left seventeen percent of section slots empty or replaced with the insufficient-evidence placeholder. On the working session, the figure rose to twenty-five percent. On the thin sync, it reached fifty-eight percent. The system produced roughly three and a half times as many empty sections when the input signal was thin compared to when it was rich.

That is the behavior the design is trying to produce. A summarizer that fills the same eight sections regardless of input is not summarizing. It is generating output that conforms to a template. The template is doing the work, and the model is the cosmetic finish.

A summarizer that abstains in proportion to the thinness of the input is doing something different. It is treating the transcript as a source whose content varies, and it is letting that variation show up in the output. The empty sections are not failures of the model. They are the model declining to assert what the source does not support.

Figure 4. What identification looks like in the rendered output.
Excerpts from the decision-meeting fixture, with the categorical labels surfaced inline.
Image by Author

Reading the result. The labels are not decoration. They change what the reader does with the output. An observed claim invites verification against the transcript. An inferred claim invites scrutiny of the assumption that produced it. An insufficient-evidence placeholder invites the reader to either look at the source themselves or accept that the meeting did not, in fact, produce a claim of that shape.

The objection from the consumer

There is an argument that empty sections are a usability problem. The reader expected a summary. The reader got a partial summary with explicit gaps. The reader has to do more work.

That objection deserves a direct answer. The reader who got a fluent eight-section summary of a five-minute exchange was already doing more work, just invisibly. They were going to read the summary, act on it, and at some point discover that two of the action items were not actually agreed to and one of the risks was never raised. The cost of that discovery is high. It is paid in misallocated meetings, missed commitments, and the slow erosion of trust in the tooling.

Honest emptiness pushes the cost forward. The reader sees the gap immediately and can decide how to handle it. Open the transcript. Ask a participant. Treat the meeting as inconclusive. Each of those is a better response than acting on a confident summary that was generated from a confidence the source did not earn.

This is the same trade observational analysts make when they refuse to report a point estimate without identification. The consumer would prefer a number. The analyst declines. The decision the consumer makes from no number is, on average, better than the decision they would have made from a number the data could not support.

Generalizing the pattern

The architecture transfers. Any LLM workflow that produces structured claims from a source can be reframed as observational analysis and given an identification layer.

Document review for legal discovery. Patient note summarization. Customer call analysis. Code review summaries. Each of these is currently deployed as a one-shot generation problem, with a model producing structured output from a source and the consumer trusting the result. Each of them has a version of the same failure mode the meeting summarizer has, and each can be made more auditable with a similar architecture: an extraction stage that is conservative about what it pulls from the source, a synthesis stage that produces labeled claims with evidence pointers, and an audit stage that is forbidden from adding or strengthening anything. The implementation and the risk profile differ across these domains. The pattern transfers. The specifics do not.

The labels and the evidence pointers are not optional features. They are the identification step made operational. A claim without a label is not identifiable. A claim without an evidence pointer cannot be audited. The audit stage’s monotonic-weakening constraint is what prevents identification work from being undone by a model that wants to produce smoother output.

What this means for the people building these systems

Calibrated uncertainty estimates are valuable. Hallucination benchmarks are valuable. Grounding and citation work are valuable. None of them substitute for the discipline of refusing to produce a claim that the source does not support.

That discipline is missing from many LLM systems partly for cultural reasons. The field grew out of machine learning, where the goal of a model is to produce an output for every input. The notion that the right output is sometimes no output is not foreign to the literature, but it is foreign to the default disposition of a generative model trained to fill in what comes next. It is, however, native to observational analysis, where the right answer to many questions is that the data cannot support an answer.

So the techniques for making LLM analytical systems trustworthy may not come primarily from within the LLM literature. They may come from disciplines that have already worked out what it means to do honest analysis under conditions where the source is the binding constraint. Causal inference is one of those disciplines. Survey methodology is another. Forensic accounting is another.

The people who already know how to refuse to estimate without identification have an unusually good vantage point on what is wrong with current LLM analytical tooling, and what to do about it.

Causal inference taught a generation of practitioners not to estimate what they have not first identified. LLM summarizers make the same mistake, just in prose instead of numbers. The fix is not just a better model. The fix is to put back the step that observational analysis never let go of, and to enforce it with an architecture that cannot be talked out of doing the right thing.

A few closing pitfalls
Treating the labels as cosmetic. If the labels are not enforced upstream, they are decoration. They have to be assigned at synthesis with a pointer to evidence and audited downstream against that pointer. A synthesis stage that produces a label without an evidence pointer is not doing identification work. It is producing a category that looks like identification.
Letting the audit stage be helpful. This is the easy mistake. A reviewer that can add a recommendation, supply missing context, or rewrite a clumsy claim feels useful. It is also exactly the failure mode the synthesis stage already has, just dressed up as quality control. Constrain the audit to a fixed set of weakening operations. Anything else is the system arguing with itself.
Confusing abstention with low quality. A summarizer that returns mostly empty sections on a thin meeting is not failing. A summarizer that returns confident eight-section output on the same thin meeting is failing, just invisibly. The way to evaluate these systems is not summary completeness, it is whether the abstention rate scales with the signal in the source.
Reasoning from three fixtures to general claims. Three transcripts are enough to check whether a design choice produces the behavior it was built to produce. They are not enough to make claims about LLM summarization in general. If you build a version of this, you will need your own fixture set and your own definition of what counts as the right level of abstention for your use case.
The asymmetry that matters

A pipeline that can only weaken its outputs has a single failure mode: it can be too cautious. A pipeline that can strengthen its outputs has every failure mode the literature has been documenting for the last several years.

Choosing the first kind over the second kind is not a technical decision. It is a decision about what the system is for. If the system is for producing fluent text, the second kind wins on every metric. If the system is for producing claims a reader can audit before acting, only the first kind is defensible.

Most current tooling is built for the first goal and deployed as if it had been built for the second. Treating that gap as a methodological problem rather than a model-quality problem is what changes the available remedies.

Repository, evaluation harness, and example outputs are available on GitHub. The full notebook walks one transcript through every stage and runs the eval harness across all three fixtures.

Staff Data Scientist focused on causal inference, experimentation, and decision science. I write about turning ambiguous business questions into decision-ready analysis.


Ai Engineering
Causal Inference
Deep Dives
Hallucinations
Prompt Engineering


