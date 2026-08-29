---
title: How to Work with AI Coding Agents
author: Sara A. Metwalli
type: raw-source
tags: [ai-coding, agent, workflow, verification, human-in-the-loop]
status: captured
source: Towards Data Science
source_url: https://towardsdatascience.com/how-to-work-with-ai-coding-agents/
published: 2026-08-27
captured: 2026-08-29
extraction: Direct web extraction of the complete main article body; site navigation, author footer, sharing controls, and related articles were excluded. Gemini summary artifact: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260829-232211-towardsdatascience.com-how-to-work-with-ai-coding-agents-694873-599985520-summary.md
---

# How to Work with AI Coding Agents

## Provenance

- Publisher: Towards Data Science
- Author: Sara A. Metwalli
- Published: 2026-08-27
- Captured: 2026-08-29
- Source URL: https://towardsdatascience.com/how-to-work-with-ai-coding-agents/
- Extraction route: direct web extraction, bounded to the main article
- Source quality: complete article prose, headings, examples, checklist, and task-selection table; not a byte-faithful HTML archive

## Source limitations

- The article is a practitioner guide based on the author's experience, not a controlled benchmark or comparative evaluation of coding agents.
- Its recommendations are broadly applicable engineering heuristics; it does not quantify gains or compare specific models and agent harnesses.
- Product names and workflow categories are examples, not endorsements or Hermes defaults.

## Extracted source text

How to Work with AI Coding Agents
=================================

A practical guide to getting better code, not just more code

[Sara A. Metwalli](/author/saraametwalli/)

August 27, 20268 min read

![](https://assets.insightmediagroup.io/media/wp-content/uploads/2026/08/pexels-dkomov-34804015-scaled.jpg)

[Image](https://www.pexels.com/photo/laptop-with-code-editor-and-plush-crab-toy-34804015/) by Daniil Komov from Pexels

Let me start this by saying I am a big fan of coding agents; they help streamline code production. But based on the questions I get asked and the experiences people share with me, they are not used in the best way.

That being said, let's talk about coding agents. The main premise of a coding agent is that it is a tool that helps you write better code. You can do that by providing coding agents with context, breaking down problems, reviewing their work, and keeping yourself in control.

That last part is the most important! Not that long ago, when you were able to use AI to generate code, you would get only a few lines of autocomplete. Then came AI coding assistants capable of producing entire functions or explaining errors.

Fast forward a couple of years and many technological advances, and we now have a different situation.

*Coding agents.*

Rather than just proposing code, an agent can examine a repository, create and modify files, run tests, read error messages, make further changes, and repeat the process until the desired goal is achieved. You, as a developer, are no longer asking the AI, "Could you write that function? Instead, you are now asking: Can you take on this problem, go through the codebase, and put in a solution?

Some may now argue that if AI takes on more of the programming work, then what should the programmer actually be doing?

I like to think about it as the programmer still doing the heavy thinking and planning, and using AI as a tool to make the process more efficient (for the most part)!

What makes coding agents different?
-----------------------------------

Before we go any deeper, we need to distinguish the different forms of AI-assisted programming available and how they progressed over time.

Let’s start with autocomplete tools. An autocomplete tool can predict the next line of code. These tools are available in most code editors and on online platforms like Google Colab. Their whole job is to try to predict what you will type next.

Then, we have AI assistants, which can respond to simple requests such as:

text

```
Write a Python function to parse this file.
```

Finally, we have coding agents that can turn a high-level goal into reality.

text

```
Add support for parsing CSV input.Use the existing parser architecture,add tests, and make sure the currenttest suite still passes.
```

The difference is the loop. So, instead of just generating text, the agent can interact with its environment. Which is precisely what gives it its power and which makes working with it different.

![](https://assets.insightmediagroup.io/media/wp-content/uploads/2026/08/fig1-2-1024x518.png)

Image by the author

You have probably come across this scenario if you've used a coding agent. You give it a seemingly straightforward instruction:

text

```
Build authentication for my application.
```

The agent begins enthusiastically to change your files; it creates new classes, adds dependencies, and maybe even alters the database.

In the end, you end up with a great deal of code, code that may not be the code you actually wanted.

This is the point where people start giving up on coding and agents, and blaming the model. But the issue here wasn’t the model; rather, the instructions specify too little.

A better request might be:

text

```
Add email/password authentication.First inspect the existing user and authenticationcode. Do not modify the database yet.Follow the existing error-handling pattern.Add tests for:valid logininvalid passwordunknown userBefore making changes, explain your plan.
```

The second request gives the agent something much more valuable than additional words; it gives it constraints.

Context Matters More than Prompts
---------------------------------

The prompt you use is very important, but without context, it can only do so much. If you are asking an agent to modify repo, the repo itself contains a alot of context, such as existing architecture, naming conventions, dependencies, tests, configuration, and documentation.

Giving an agent a prompt without context is like driving a car without a GPS in a new country! Both will get you somewhere, but not where you want to go.

For example, a prompt like:

text

```
Fix the bug in the parser.will not get you the same results as this one:Fix the bug in src/parser.py.Before changing anything, read:README.mdsrc/parser.pytests/test_parser.pyFollow the existing error-handling pattern.Run the parser tests after making the change.
```

The second prompt provides the model with an improved environment for reasoning. That is why project-level instructions and documentation are becoming increasingly important when working with coding agents.

It is worth pausing here and emphasizing that longer prompts aren't necessarily better. In most cases, a good prompt is the one that shows the agent where to look.

Another important thing to pay attention to is: don’t ask the agent to change code right away, insted follow this loop:

***Ask → Inspect → Plan → Implement → Test → Review.***

Start by asking the agent to inspect the repository without making changes.

For example:

text

```
First inspect the repository.Do not modify any files.Identify:Where this functionality currently lives.Which files are likely to change.Existing tests related to it.Any architectural constraints.Then propose an implementation plan.
```

This step will save you a lot of time ( and potential mistakes), as it gives you a chance to spot a misunderstanding before the agent acts on it by modifying 15 files. Once you can see the agent’s logic, you can start prompting precise changes.

Focus on Small, Testable Problems
---------------------------------

One thing I see a lot of people do is give the agent a massive task, like:

text

```
Rewrite this entire application.
```

It will be difficult to review the agent's ability to make large changes, because you will have a lot of code to go through! Instead, break the work into small tasks and, ideally, test after each addition:

text

```
Task 1:Add the parser class.Task 2:Add unit tests.Task 3:Integrate it with the existing pipeline.Task 4:Refactor duplicated code.
```

In this case, if there's a problem, you'll have a good idea of the location where it happened! Which is a skill that is useful beyond AI; it is good software engineering.

It helps to remember that an agent doesn't have an inherent knowledge of whether the code works in your particular environment. That is how you can utilize these agents. For example, if you ask an agent to implement a function and run the test suite, and three tests fail, the agent can read the traceback, identify the relevant code, make a change, and rerun the tests.

This is one reason good tests become even more valuable in an agent-driven development workflow. See, tests aren’t just for developers anymore; rather, they can become part of the agent’s environment.

Let’s take a step back: an agent can make every test pass and still produce a bad implementation. This is where developers (like you and me most of the time) are still very essential. When you review agent-generated code, you need to check:

* Is this the right design?
* Does it fit the existing architecture?
* Did the agent make unnecessary changes?
* Are there hidden assumptions?
* Did it introduce a dependency?
* What happens with unusual inputs?
* Is the code maintainable?
* Are there security implications?

We all know that AI makes producing code cheap, but understanding code is still expensive.

When Should You Use an Agent?
-----------------------------

Okay, I must point out that not every programming task needs an autonomous agent. For a small question, a normal AI assistant may be faster, or even a hand-written implementation.

For example:

*“Why does this Python expression return None?”*

There’s little reason to give an agent access to an entire repository. However, something like:

“Find why these integration tests are failing, identify the root cause, implement the fix, and run the relevant tests.”

Is a much better fit for an agent. A smple rule of thumb is something like:

| Task | AI assistance type |
| --- | --- |
| “Explain this error” | **AI assistant** |
| “Write this small function” | **Coding assistant** |
| “Refactor this file” | **Coding assistant/agent** |
| “Find and fix this bug” | **Coding agent** |
| “Add this feature across the repository” | **Coding agent** |
| “Investigate why the test suite is failing” | **Coding agent** |
| “Rewrite the entire application” | **Agent + human checkpoints** |
| “Make this code better” | **Neither—define the problem first** |

The more the task involves exploration, multiple actions, and feedback, the more useful an agent becomes. And it is only useful if you provide it with 5 things:

A good coding-agent request usually contains five things:

text

```
Goal:Add support for XYZ input.Context:Inspect src/parser.py and the existing parser tests.Constraints:Do not change the public API.Acceptance criteria:Existing tests continue to pass and addtests for XYZ input.Validation:Run pytest tests/test_parser.py.
```

The only question remaining now is, ***what agent to use?***

Today, a growing ecosystem of coding agents that exist, including those integrated into IDEs as well as terminal- and cloud-based agents. What you need to ask yourself is:

*Which workflow fits my problem?*

If you spend most of your time inside an IDE, an IDE-integrated agent may feel natural. If you work primarily from the terminal, a terminal-based agent may make more sense. If your development workflow revolves around GitHub, repository and pull-request integration may be more important.

Final thoughts
--------------

Over the years, programmers have had to adapt to the latest technological advancements. That hasn’t been more prevalent than it has been with the appearance of coding agents. The skill set needed when programming using coding agents is slightly different. You need to understand algorithms and architecture, and you still have to carry out debugging! You also need to get good at assigning work to a machine that can act on your behalf.

You should define the problem, provide some context, set out the constraints, and then review the result. The point is that an AI agent can work much faster and produce much more code in a short period of time. Which means that good delegation becomes all the more important. The most interesting question about coding agents isn’t:

***How much of programming can be automated by AI?***

We are transitioning from a situation in which developers mainly wrote code to one in which they are increasingly responsible for directing, assessing, and coordinating code-generating systems.

That fact does not reduce the importance of programming. In certain respects, it makes understanding software more important. The hard part does not consist in writing the code, which can be done in just a few seconds.

The difficult part is knowing what those ten lines should do, and whether they should exist at all. The best developers of the agent era won’t necessarily be the people who write the most code.

They’ll be the people who know which problems to give to the machine, how to give them, and when not to trust the answer.
