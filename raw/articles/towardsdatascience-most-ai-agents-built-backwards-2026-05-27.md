---
title: Most AI Agents Fail in Production Because They’re Built Backwards
author: Benjamin Nweke
source: Towards Data Science
source_url: https://towardsdatascience.com/most-ai-agents-fail-in-production-because-theyre-built-backwards/
published: 2026-05-27
captured: 2026-05-29
created: 2026-05-29
updated: 2026-05-29
type: raw-source
status: raw
tags: [agent, architecture, orchestration, observability, anti-pattern]
extraction: Jina Reader article extraction; reader output begins mid-sentence (opening context before "agent system seriously fail in production" is missing), but main body sections, examples, and conclusion are intact. Gemini summary run 20260529-201234 was used as an off-wiki grounding artifact (local path only).
---

# Most AI Agents Fail in Production Because They’re Built Backwards

Source URL: https://towardsdatascience.com/most-ai-agents-fail-in-production-because-theyre-built-backwards/
Extraction note: Jina Reader article extraction was used because generic extraction returned an extractor-generated digest; the reader output begins mid-sentence (the opening context before "agent system seriously fail in production" is missing), but preserves the main article body sections, examples, and conclusion.

---

agent system seriously fail in production, it wasn’t dramatic. There was no crash. No error message. The system just kept running and producing outputs that looked reasonable until someone actually read them carefully enough to notice something was off.

When we decided to look into it, it took us two days’ worth of debugging to figure out what was going on. Funny enough, the model wasn’t hallucinating, and the input-output tools were delivering the correct results.

The problem, when we finally found it, was architectural. The model and the tools were set up correctly, but the idea was that reasoning would tie the whole thing together, which, as you would guess, obviously failed.

Turns out reasoning does not do that sort of thing.

That experience is what I keep coming back to when I think about why so many AI agents that work in demos don’t really survive real-world use.

It’s not a capability problem.

It’s an architectural one.

And if you’ve read my previous piece here on TDS, [Why AI Engineers Are Moving Beyond LangChain to Native Agent Architectures](https://towardsdatascience.com/why-ai-engineers-are-moving-beyond-langchain-to-native-agent-architectures/), the pattern should sound familiar: systems built top-down, from goal to tools to model, with the quiet assumption that intelligent behavior fills in the gaps.

That assumption is what “built backwards” means. And it’s more common than most teams realize until something breaks.

## Agents Aren’t Entities. They’re Systems.

A production AI agent isn’t a single intelligent thing.

Rather, there is a set of interacting pieces with different responsibilities, failure modes, and levels of observability.

The LLM is one of those components, not the whole system. Just one piece of it.

It may sound obvious when you say it out loud. But the “autonomous agent” framing that dominated 2023 and most of 2024 kept pulling engineers toward a different mental model: one entity, one reasoning loop, everything handled by the model.

All you need is tools, a good system prompt, and a hope that everything will fall into place.

In contrast, engineers who have shipped real AI-based products rarely describe their systems that way. What they actually describe sounds a lot more like distributed systems architecture.

Not because they read a book about design patterns, but because they got burned enough times that they started putting structure more seriously in their workflow.

Building top-down, starting from “what should this agent do” and working backwards into tools and prompts, is quick to get started.

It’s also how you end up with a system where the model is responsible for too much, and nothing is individually debuggable.

The architecture was decided by the goal, not by the engineering requirements.

That’s the backwards part.

* * *

## So What Really Goes Into a Production System?

The abstract version is easy to nod along to. Here’s what it actually looks like.

Every production AI system I have seen that works cleanly has something like a **decision layer**, whether the team named it like this or not. It’s the part where the model lives and does its actual job.

The instinct is to push everything into this layer: parsing requests, managing memory, handling retries, resolving tool failures.

This is okay if you’re working in a Jupyter notebook. In production, under load, with real users, this becomes the part of your system where everything is everyone’s fault, and most times, nothing can be debugged.

The decision layer should do one thing well, and that is deciding what to do next, given a certain context that is already prepared for it.

That’s the whole job.

Who prepares the context? Something else. Who acts on the decision? Also something else.

That “something else” is the orchestration layer, and in most well-built systems, it’s genuinely just code: conditionals, asynchronous runners, retry handling, queue routing, maybe even a state machine depending on how involved the workflow is.

![Image 1](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/mermaid-diagram-2026-05-23-171820-1024x490.png)

Instead of expecting the model to do everything, treat it like just another component. Here, standard code does the heavy lifting with state and tools, so the LLM only has to worry about making the next decision. Image by author.

Many teams reach for frameworks here because bare orchestration code feels too simple, like surely there’s supposed to be more infrastructure.

There usually isn’t.

The less magic this layer contains, the faster you’ll find bugs when they appear. And they will appear.

From experience, I learned this the hard way on a project where the orchestration lived inside a framework’s execution model. Something was retrying tool calls in a way that was corrupting state downstream.

We spent two days finding the issue. Two days for a bug that could have been resolved in no time at all if the retry logic had been three lines of Python I wrote myself.

This leads us to the tools and execution layer, where all communication happens.

Now, the **tools and execution layer** is where things talk to the outside world. This layer usually has just one job, and that is to take a well-defined input and then produce a predictable output.

But the failure I kept seeing, and kept repeating, honestly, was tools that tried to be helpful by doing more than one thing. A single function that calls an API, updates a cache, and does other things.

In a setup like that, when it breaks, you don’t know where. Even when you try to replace the API, you’re untangling logic that shouldn’t have been tangled in the first place.

**Memory and state** is where I’d push hardest, because it’s where most teams are most underprepared.

Most teams think about memory as “what the model knows.” The more important question is what the _system_ knows, and whether that knowledge is current.

I remember one day when it took me an afternoon to debug what seemed to be a simple “model hallucination.” The model had kept referring to user preferences, which, however, had been updated twenty minutes ago.

That’s not a model problem.

That’s a systems problem.

And it’s surprisingly common.

In multi-agent systems, specifically, shared state is where subtle failures breed. One agent updates something. The others don’t know.

Everyone proceeds confidently in slightly different directions. The output looks almost right, which is [almost worse than looking wrong](https://towardsdatascience.com/the-multi-agent-trap/).

And then there’s **evaluation and observability**, which almost everyone always puts off until something goes wrong. I’ve been guilty of this, too.

The difference I keep in mind is that logging tells you what happened. Observability tells you _[whether what happened was correct](https://www.datadoghq.com/state-of-ai-engineering/)_. In a deterministic system, those are close to the same thing.

In an AI system, it’s not. You have to be able to follow the specific request from start to finish, including what information the model had to consider, what decision it made, what external API call it invoked, and how it acted upon its response.

* * *

## Building It the Right Way Around

It starts with the top-down approach: I want an agent to do X, so I’ll give it the tools, a nice system prompt, and if the model is smart enough, it will be fine.

And this is exactly what people use to make prototypes, and why wouldn’t they? They are not wrong.

But here’s the thing: the problem is that it treats the architecture as a consequence of the goal rather than as something you design deliberately.

Then the system grows. You know, more tools, more workflows, more edge cases, more users, and suddenly there’s no real foundation underneath any of it.

Bottom-up is more time-consuming, but it’s far more comfortable.

You start with the basic building blocks and make sure they actually work. Then you figure out what each part should communicate, what data it owns, and what it’s responsible for.

Eventually, the system takes shape naturally from the interaction of its parts.

This isn’t a “real engineers build everything from scratch” argument. It’s not even about tooling at all, actually. It’s about the mental model you’re building with.

I’ve seen engineers use sophisticated frameworks and build clean systems because they understood what each layer needed to do.

I have also seen engineers write vanilla Python and build an undebuggable mess because they were still thinking in terms of “the agent decides everything.” The tools follow from the model in your head, not the other way around.

The most robust multi-agent system I have had the opportunity to work with closely had almost no AI-specific infrastructure. When I first saw the repo, I honestly assumed I was looking at the wrong codebase.

A message queue, worker processes with distinct scopes, shared state storage with explicit read/write contracts, and a coordinator making routing decisions.

The language model queries were performed by the workers themselves, each receiving a set of context created upstream by a different process.

All in all, the whole thing was about a thousand lines of Python. I’ve seen demo agents with more code than that. Every part was traceable.

When something behaved unexpectedly, we’d usually find the problem in under an hour because there was no magic to look through. Just code with a clear path through it.

That system was built bottom-up. The goal was defined, but the architecture wasn’t derived from it. Components were designed first, evaluated on their own, and then composed in order to implement the desired functionality. The latter is the most important aspect, not the former.

* * *

## Where I Think This Is Going

As far as I can tell, the direction we’re heading in is slowly shifting away from “agent frameworks” and toward proper infrastructure, with systems for evaluation, model routing, fallbacks, and state management.

At least some of it already exists out there. The majority is yet to come as people solve hard production problems in this space.

The thing I see over and over again is that people building the most reliable systems rarely even use the best models. What they have instead is a clear understanding of everything that happens inside their systems.

The model used by such a system can be GPT-4, but it may as well be a small local model. It matters little when everything else works properly.

We’re moving from treating the model as the product to treating the system as the product. The model matters, but it’s only one component among many.

Most agents don’t fail because the model wasn’t good enough. They fail because the system around the model was designed backwards, starting from what the agent should do and assuming the architecture would sort itself out.

It doesn’t.

Building it the right way around, components first, behavior second, is what separates the systems that hold up from the ones that look impressive until they don’t.

* * *

## Before you go!

I write more about the real engineering decisions behind AI systems, where abstractions help, where they hurt, and what it takes to build reliably.

You can **[subscribe to my newsletter](https://thatcsguy.substack.com/?r=79lldp&utm_campaign=pub-share-checklist)** if you’d like more of that.

**Connect With Me**

*   [LinkedIn](http://www.linkedin.com/in/nwekebenjamin)
*   [Substack](https://thatcsguy.substack.com/)
