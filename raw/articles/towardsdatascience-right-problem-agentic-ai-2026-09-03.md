---
title: How to Solve the Right Problem in the Age of Agentic AI
author: Mike Huls
source: Towards Data Science
source_url: https://towardsdatascience.com/how-to-solve-the-right-problem-in-the-age-of-agentic-ai/
published: 2026-09-03
captured: 2026-09-06
type: raw-source
status: captured
tags: [ai-coding, software-engineering, workflow, specification]
extraction: full Karakeep-captured article body; local Chinese summary at ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260906-170106-How-to-Solve-the-Right-Problem-in-the-Age-of-Agentic-AI-Towards-Data-Science-67030-726380240-summary.md
---

# How to Solve the Right Problem in the Age of Agentic AI

## Source

- URL: https://towardsdatascience.com/how-to-solve-the-right-problem-in-the-age-of-agentic-ai/
- Author: Mike Huls
- Published: 2026-09-03
- Captured: 2026-09-06
- Extraction route: Karakeep full-content capture
- Source quality: full article body
- Limitation: practitioner framework supported mainly by first-person anecdotes and a hypothetical case-system walkthrough. Statements about tenfold speed, hundreds of wrong changes, effort parity, and reduced rework are not controlled Hermes measurements and must not become local thresholds or hard gates without independent evidence.
- Local Chinese summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260906-170106-How-to-Solve-the-Right-Problem-in-the-Age-of-Agentic-AI-Towards-Data-Science-67030-726380240-summary.md`

## Captured article

Before AI, implementation capacity was scarce. A bad requirement might waste a few engineers' time. With AI, that capacity expands dramatically. A bad requirement can now produce hundreds of wrong changes very cheaply. The bottleneck therefore moves upstream: towards problem definition, context, constraints, decisions and validation.

If the direction is wrong, all that extra speed just gets you to the wrong place ten times faster.

It's a fact that you're going to have to address uncertainty surrounding a project at one point. Why not do it when change is still cheap? It's much cheaper to change a blueprint than it is to rebuild whole parts of a building.

This article's goal is to provide you with the tools to reduce uncertainty as much as needed before implementation.

This article introduces a practical framework that does exactly that in 6 steps. Each step produces one short document that makes the decisions explicit, durable and usable by both humans and agents. It's a shared record of what's understood, decided and agreed.

With the framework you build:

-

The right thing: a solution that actually solves a real problem.

The right way: without wasting money, time, or resources.

As efficiently as possible: with enough clarity during development to prevent backtracking, waiting or guesswork.

The outcome is alignment. Both humans and AI agents work from the same playbook: a clear, shared understanding of the problem and intended solution. This prevents guesswork, rework and surprises.

···

Why this matters

The hardest problems in software development are rarely purely technical. They're about communication and alignment: key components in turning a vague problem into the right solution. Even the best engineers can't salvage a project if stakeholders can't agree on what they're building, why or for whom. Misalignment slows teams down and burns out good engineers because they lack the structure and direction needed to do their job.

Involving agents makes these risks even bigger. A single engineer heading in the wrong direction for a day can do limited damage. That same engineer deploying an entire fleet of agents can do a lot more damage, faster: one wrong assumption doesn't stay in one file anymore, it gets copied into every agent-generated change that touches the same pattern before a human ever reviews it.

Yet many teams treat requirements as a one-and-done event and then sprint into development, assuming the rest will sort itself out. You wouldn't build a house without blueprints. Why would you build a software project without proper preparation?

Yes, this takes investment up front. But "we don't have time for that" often turns out to be a very expensive sentence once you count the cost of compliance violations, reputational damage, competitive advantage and rework at scale.

From Risk to Asset: Designing a Practical Data Strategy That Actually WorksMake data work for your organizationMike Huls · 10 min read

The cost of being wrong

Spend effort where it's needed

Not every decision deserves the same amount of analysis. This is one of the principles behind the framework:

The more expensive a decision is to reverse, the more uncertainty you should eliminate before making it.

Choosing the label on a button is highly reversible. Decide quickly, adjust it later if needed. Choosing a data contract, system boundary, or integration architecture may not be, and getting it wrong is expensive to undo. That's where the scrutiny belongs.

This doesn't mean predicting everything up front. It means spending your preparation effort where a wrong decision would actually cost you, and deliberately leaving the rest flexible.

When to use this framework

Not every software change needs six documents.

A bug fix, a small internal script or a disposable prototype usually doesn't justify this level of preparation. Applying the full framework to every change would create bureaucracy rather than clarity.

The framework becomes valuable when the cost of getting the direction wrong is significant. Use it when several of these are true:

Multiple stakeholders or teams need to coordinate.

The problem or desired outcome is ambiguous.

The solution depends on existing systems, data or organizational constraints.

Important architectural or data decisions will be expensive to reverse.

Several people or AI agents will work in parallel.

A mistake could create significant financial, operational, compliance or reputational damage.

The project is large enough that rework would materially affect its outcome.

You also don't have to use every step with the same level of detail. For a relatively small project, the framework may be a few pages of decisions. For a large, complex project, each step may require substantial discovery and discussion.

The point is not to complete six documents, but rather to reduce the uncertainty that matters before you start implementing.

Use the framework when coordination and the cost of being wrong justify it.

And the framework is not a substitute for experimentation. When an assumption is uncertain, a prototype, spike or other experiment may be the fastest way to reduce that uncertainty. The result should then feed back into the relevant step rather than silently changing the direction of the project.

Layered Architecture for Building Readable, Robust, and Extensible AppsIf adding a feature feels like open-heart surgery on your codebase, the problem isn’t bugs, it’s structure. This article shows how better architecture reduces risk, speeds up change, and keeps teams moving.Mike Huls · 9 min read

The framework

The Project Preparation Framework systematically reduces uncertainty by working through one decision domain at a time. Each step builds on the last, bringing the most consequential questions forward while the cost of change is still low. Interpretations, assumptions, decisions and reasoning are documented in a shared file that the relevant stakeholders can review.

The framework is sequential, but it is not a waterfall. Later discovery can invalidate an earlier decision. When that happens, go back, update the affected artifact and make the changed decision explicit. The goal is not to prevent change, but to prevent unacknowledged change.

The table below is the framework at a glance.

Step

Document

Purpose

Business prerequisites

PID.md

Align on business problem,scope, organization, goals

IT prerequisites

discovery-report.md

Udnerstand the existing data, systems, feasibility, risks and constraints

Functional requirements

functional-requirements.md

Define what the solution must do

Technical requirements

technical-requirements.md

Define how the solution will work

Governance

governance.md

Define who's involved, who decides and who's responsible

Planning

roadmap.md

Define when, in what order and by whom

The first four steps establish what we know and what we intend to build. These steps already involve decisions and decision ownership. Step 5, therefore, does not introduce governance. It turns the decision structure that's needed for the build, launch and operation of the solution into an explicit agreement.

People should be able to challenge a decision, but disagreement should lead to a decision owner making a call, not to the decision sitting unanswered in someone's inbox.

Personal, Agentic Assistants: A Practical Blueprint for a Secure, Multi-User, Self-Hosted ChatbotBuild a self-hosted, end-to-end platform that gives each user a personal, agentic chatbot that can autonomously vector-search through files that the user explicitly allows it to access.Mike Huls · 9 min read

The framework, step by step

In this chapter we go through the framework, step by step. Each details the goal of the step, a "war story"/example, lessons learned from that war story and instructions on how to create the document.

I've created the Project Preparation Framework Repository on GitHub that contains one-pagers about each step in the framework and some "war stories". I very much intend to make this a community project so please contribute if you have some inspiring stories, improvements or additions.

1. Business prerequisites

Laying the foundation for solving the right problem

This step addresses one of the most expensive project failures: solving the wrong problem. It makes sure you focus on the real business problem, one that stakeholders actually want solved, with a clear scope. It secures buy-in and alignment early and prevents wasted efforts on something nobody needed.

Engineers can read the resulting document to understand the "why" behind their work, which makes day-to-day decisions easier and development clearer, with less ambiguity and fewer risks.

The webhook

A customer once told us they urgently needed a webhook. We dropped everything and started building. When we finished, it turned out the customer didn't really know what a webhook was and that they actually needed an API.

We delivered a flawless technical solution to a problem that didn't exist.

Lessons learned

The customer owns the problem, you own the solution. If you let the customer define the solution you're not doing your job. A short interview on the business goals would have caught this immediately.

How to:

Create PID.md (Product Initiation Document), defining the business problem, goals, users, and success metrics.

Read the guide - Use the template

2. IT prerequisits

Can we solve this within the existing environment?

Almost every solution has to be integrated with existing systems and processes. How well it succeeds depends heavily on what the existing landscape can actually support.

This step assesses the feasibility of solving the problem within the existing environment by understanding the data, systems and dependencies. We make sure every stakeholder is aware of what's possible and what isn't before development starts.

The real-time dashboard

We spent several sprints building a system to process real-time data for a dashboard. It turns out that the data source couldn't provide real-time data at all, only a batch every 12 hours. The product worked perfectly, it just couldn't be plugged into the company's existing ecosystem.

This is exactly the kind of thing you want to fail on early. Ideally, we'd have discovered we were "building a train for an organization with no railroads".

Create discovery-report.md to surface technical surprises proactively, before they derail the project.

Know your destination before packing your backpack. Photo by Danka & Peter / Unsplash

3. Fucntional requirements

What must the solution accomplish?

Here we define what a solution must actually be capable of doing. We aim to understand users, expected behaviour, frequency and scope before optimizing implementation. User stories help greatly with this. Clarity here also makes the next step much easier, since well-understood capabilities and goals are far simpler to translate into technical decisions.

This is the step I've seen skipped very often. Passionate engineers get carried away by what's technically possible and lose sight of what the customer actually asked for.

Essential automation

We once spent several sprints fully automating a process that everyone was convinced was essential. In the end, we spent 100+ hours automating something that took 10 minutes to do manually, once a month.

Additionally, a beautiful UI was created. The first question was whether an API was available instead. They were developers themselves and never meant to use the UI.

Skip functional requirements and you risk delivering a Ferrari (with a Ferrari price tag) when the customer needed a bicycle.

Before opening an IDE, make sure to understand who the user is, how they want to use the solution and how often. The conversation that would have caught this takes minutes while the rebuild took weeks.

Create functional-requirements.md and summarize all requirements there. Also add a list of user stories that determine who, how and how often certain users aim to use the solution.

4. Technical requirements

How can we make the solution real?

With the documents from the previous steps in hand, most of the fog has already lifted and the direction for your technical choices should be fairly clear. Still it's essential to turn that into a concrete plan and make deliberate technical choices, tying every previous step together: "Our business goal is to X, our existing systems do Y, our functional requirements say Z, so here's what we need to build".

Architecture happens before the build, not during.

Skip this and you get open-heart surgery on a half-finished product, changing direction mid-build or patching gaps that you should have spotted months earlier, at midnight, to make the deadline.

Database open-heart surgery

We chose PostgreSQL because it was our team's default. Only later did we discover that the domain model was fundamentally different between customers and changed frequently. We had already encoded these assumptions deeply into our schema and application. The eventual migration wasn't difficult because PostgreSQL was a bad database. It was difficult because we had made an expensive architectural decision before understanding the domain.

Lesson learned:

The right tool for the job isn't the one you know best but rather the one that fits the problem. A few conversations about the data model and how it was expected to evolve would have saved weeks of rework and a database migration.

This step is all about choosing the best technological fit for your solution, within the constraints of the organization. Summarize your findings and the reasoning behind them in technical-requirements.md. For every significant decision ask "If we get this wrong, how expensive will it be to change later?"

5. Governance

Who does what and who decides?

By this point, the business problem, the environment, the functional requirements and the technical direction have been worked through. Now we make the decision structure for execution explicit. Without governance, even the best-laid plans unravel through confusion, delay and a lack of accountability. Governance isn't about bureaucracy but enabling action.

Around in circles

A project stalled for weeks because nobody knew who could approve a critical design change. The request circulated through email chains between three teams, each assuming someone else had the authority. By the time the right person was found, the deadline had long passed, resulting in a disappointed customer and a frustrated team.

Lesson learned

Decisions get stuck in limbo, and die there, when nobody's sure who makes the call or who needs to be involved. A RACI matrix or short meeting about who's in the lead would have saved weeks of hassle.

Create governance.md to establish clarity around decision-making, escalation, communication and approval. Include a RACI-matrix that details who is Responsible, Accountable, Consulted, and Informed for each remaining decision, and who from earlier steps stays involved if something in their area comes up. Together, these keep the project moving instead of stalling in someone's mailbox.

6. Planning

When, in what order, and by whom?

At this point you know enough about what to build, why it matters and the constraints under which it must be built. Now we break the solution into actionable tasks with clear dependencies, timelines, and owners. The goal is a roadmap with clear tasks, allowing agents or coworkers to work on many of them at once, resulting in a smooth ride to the finish line.

Skip this step and you end up with teams waiting on each other, tasks that are either too large or too vague, and a missed deadline.

A hot mess

We started a project that looked simple, and everyone got to work immediately. Nobody had mapped the dependencies first: two developers built features that depended on an API that hadn't been designed yet. Another team integrated against an interface that later changed. By the time we caught the problem, several people had to stop, undo work and redo it in the right order.

We could have avoided the pile-up by figuring out who needed what from whom, and in what order, before anyone started coding. Good planning makes dependencies, sequencing and deliverables explicit and visible. In our case that would have saved a lot of frustration and wasted hours.

A good task should be small enough to understand, has a clear outcome, and makes its dependencies obvious. That lets people, or coding agents, work independently wherever possible, instead of everyone queuing behind the same bottleneck.

Architecture happens before the build, not during. Photo by Nwar Igbariah / Unsplash

Putting it all together

The framework in practice

Consider an organization that wants to build an AI-assisted system for processing incoming cases. The initial request sounds straightforward: “Use AI to read incoming documents, extract the relevant information and automatically decide how each case should be handled.”

Built immediately, this goes wrong in familiar ways. A few weeks in, the source documents turn out to be inconsistent, key data lives in another system, and the case workers didn't actually want the AI making decisions. They wanted help finding missing information and prioritizing their queue. Legal requires a human in the loop, which the architecture now makes awkward to add. The team has built something technically impressive around requirements nobody checked.

Run through the framework instead, and each of those surprises surfaces before it's expensive.

Business prerequisites reveal the real problem: not "automate decisions" but "reduce manual prep time while keeping the case worker in charge."

IT prerequisites surface the data inconsistencies and the identity model the solution has to fit into, before any code depends on them.

Functional requirements cut the scope to classification, summarization, and traceability, dropping the autonomous decision-making nobody needed.

Technical requirements build the human-in-the-loop and traceability into the architecture from the start instead of retrofitting them later.

Governance assigns ownership, so "can AI decide this?" has an answer before it's asked in production.

Planning sequences the work so document-quality assumptions get validated before the team scales up.

Ideally, none of this takes more time than the version above. It just spends that time before implementation instead of after, when undoing a wrong assumption is no longer cheap.

Conclusion

AI makes implementation cheap. Therefore, deciding what to implement becomes more important.

AI made implementation faster and cheaper. That capacity is only valuable if it's pointed at the right problem. The Project Preparation Framework doesn't eliminate uncertainty, it helps teams find the uncertainty that actually matters and deal with it as much as possible, while it's still cheap to do so. It makes the resulting decisions explicit, and preserve the context both humans and AI agents need to act on them in documents.

Good engineering has never been about writing the most code or spending the most tokens. More than ever now, it's about making good decisions under constraints and turning those decisions into systems that create real value. Agentic software development doesn't change that, it just raises the price of getting it wrong.

Try the Project Preparation Framework on your next initiative. Open an issue in the repo if it breaks, if you have suggestions or improvements or want to share war stories.
