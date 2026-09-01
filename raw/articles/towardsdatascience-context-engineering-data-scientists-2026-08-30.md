---
title: "Context Engineering Is Changing. Here’s What It Means for Data Scientists"
created: 2026-09-01
updated: 2026-09-01
type: raw-source
tags: [agent, context-engineering, skills, workflow, data-science]
source: Towards Data Science
source_url: https://towardsdatascience.com/context-engineering-is-changing-heres-what-it-means-for-data-scientists/
author: Piero Paialunga
published: 2026-08-30
captured: 2026-09-01
status: captured
extraction: "Full main article body reused from the Karakeep capture used by gsummary and cross-checked against the public page metadata; site navigation, image binaries, recommendations and author-promotion footer were omitted."
---

# Context Engineering Is Changing. Here’s What It Means for Data Scientists

## Provenance

- Source URL: https://towardsdatascience.com/context-engineering-is-changing-heres-what-it-means-for-data-scientists/
- Publisher: Towards Data Science
- Author: Piero Paialunga
- Published: 2026-08-30
- Captured: 2026-09-01
- Extraction route: full Karakeep content reused from the gsummary source packet; title, author and publication date cross-checked against the public page.
- Source quality: full substantive article body. The article is a practitioner interpretation of Anthropic guidance and the author's Claude Code experience; it does not provide a controlled comparison or universal thresholds.

## Extracted source

There are so many positive sides that come with using systems like Claude; all the repetitive, routine coding gets automated, researching is quicker, and debugging becomes easier. In general, for people in software, productivity goes up and allows teams to ship more.

However, the slight drawback of using tools like Claude is that you have to stay on track with these agents.

This is not only to avoid being left behind and using outdated technology. This is also because new models are trained to work slightly differently than their predecessors.

Ultimately, this means that you might find yourself asking, "What's wrong with Claude today? Why is it not working properly?" not realizing that you are not using Claude correctly according to the new expected procedures.

This is the reason why companies like Anthropic show not only that new models are objectively better than older ones according to some benchmarks, but they also communicate to users how they should change the way they interact with them.

Less than a month ago, Anthropic released "the new rules of Context Engineering for Claude 5 generation models".

The article explains in detail how the models are changing, and that prompt engineering is not the main character anymore, leaving space for context engineering, which is the collection of all the sources that LLMs use to answer your question/complete your ask.

In particular, this article talks about us, Data Scientists, and tries to answer this question:

"How do context engineering's new rules change our day-to-day work?"

But before we do that... what is even "context engineering"?

0. What is Context Engineering?

Photo by Wesley Tingey on Unsplash

You can think of two big ways to use Anthropic models: API Calls and Claude Code.

-

API calls are one-shot processing of the input. Your text (the input sequence string) gets processed by the LLM, which generates the output sequence string. Because you don't own the LLM, the processing happens online, and you pay for input and output tokens. That's it.

Systems like Claude Code (or Codex) work agentically. This means that the model is still being used and called through API calls, but it is doing much more than just reading the input. A multitude of API calls are executed, and every API call is responsible for something different (e.g., reasoning, coding, generating the output etc). What you see at the end is the final result of all the processing that went on through different API calls.

For cases where you need (1.), prompt engineering, which is the art of crafting the perfect input information, is extremely important: you are doing a specific task, all the information to execute the task is in the prompt, and you expect a reliable and verifiable answer.

When you use an agent (2.), prompt engineering is much less the main character. This is because agents are meant to be intuitive, easy to use, and generally more powerful as they leverage massive internal systems.

However, this doesn't mean that Claude can read your mind :)

All the information that is still necessary for Claude to do a good job should be in a set of documents, instruction files, and settings that are defined as "context." This context needs to be "engineered" in order to be used optimally by the agentic system. Anthropic gives us guidelines to do so.

Now, let's review these guidelines using our Data Science detective hat.

1. "Trust me, bro"

Photo by Nick Fewings on Unsplash

The first point of the article talks about "CLAUDE.md" which is the file that gets created by Claude Code when you initialize a folder. [If you are lost, you should probably check this out before you keep reading]

About "CLAUDE.md", Anthropic team basically says: stop patronizing Claude and giving it too many instructions; you are only confusing it. The point that they make is that new models can fill the gap, and by adding an excessive amount of info, you are just adding the probability of this info being incompatible with each other.

This means you can write in "CLAUDE.md" whether the folder is an EDA folder, a research folder, or a "code to be delivered in production" folder.

Then, Claude will be able to understand that it needs to be extra careful when implementing a feature if it is to be delivered in production, and you will probably use .py files rather than notebooks, while the opposite will be true in an EDA folder.

We'll come back to this concept. Let's keep going.

2. "No spoilers!"

Photo by Hu Chen on Unsplash

Claude is designed to use skills. You can think of a skill as something that saves you time: when you are doing the same thing over and over again, you set this information in a given file, and you redirect your conversation to that file rather than explaining from scratch and repeating yourself.

For example, you might have a notebook.md skill where you instruct Claude on how to work with your notebooks, what colors you prefer for the plots, what libraries to use to compute the statistics, etc.

Anthropic is basically telling us: "If you put everything in one long skill, Claude will not know what is actually relevant in your ask." In other words, they are asking us to be specific.

Let's watch this from a Data Science perspective. We have many different tasks to take care of, and they are different from each other. Sometimes we load the data, sometimes we just explore it, sometimes we set up Databricks and spin up a cluster, sometimes we train a model. Each microtask should create a skill, which is ultimately wrapped in another macro skill. At the end of our design, we will build a taxonomy, i.e., a tree of skills. For example:

Image made by author with the help of AI tools. (ChatGPT)

You are not building a data.md skill that loads data, checks the quality, and transforms it. Actually, data.md will be short and sweet, and it will direct you to the right subskill for a specific smaller ask. For example, if you ask Claude to load the data, Claude will read the data.md file and then refer to loading.md

3. "Thanks for the memories!"

Photo by Ian Wetherill on Unsplash

Another short but important update that the Anthropic team is sharing with us is the following: Claude models are very good at remembering your habits. This means that across our work, the CLAUDE.md will be updated regularly with meaningful information about our preferences.

I want to add my personal take to this. When I find that my skill is not working exactly like I want it to, I ask Claude to update it so that it will work better next time.

For example, if the preprocessing in preprocessing.md is done in a way that is too extreme (e.g., completely filtering out NaNs without exploring them first), I ask Claude to modify certain parts of the skill.

4. "You underestimate my power!"

Photo by Zanyar Ibrahim on Unsplash

Lastly, the Anthropic team reminds us that Claude can work with many different files and formats.

If you have .py and .json files that are meaningful, for example, a hyperparameter.json with the set of parameters for your training, you can let the training.md skill know, and the file will be analyzed and explored when necessary.

Not only that, you can use rich HTML files, which are called artifacts.

These files are great for presenting results, reviewing the output internally, testing different parts of the pipelines, and exploring the data. [Take a look at the official documentation here]

5. Long Story Short...

The moral of the story is the following:

When the model fails, it is because it is looking at the wrong information and doesn't have enough context.

The way to avoid this kind of failure and use the most amount of power is through "context engineering".

In practice, we need to:

Trust Claude to navigate through the asks. We must give general direction but avoid overspecificity to prevent contradictory info.

Modularize our skills into a set of small but specific routines. This keeps Claude's context modular and efficient.

Use Claude's self-updating memory and correct skills as we go at the end of our sessions.

Adopt artifacts to enrich our visualization and exploratory power.

While this is Claude-specific, the trend goes in the same direction for other providers: models keep getting smarter, and context engineering is the main character to unlock their full potential.

This means that tools like Codex will probably need a translation of this guide, but they won't be that far off in terms of "spirit".
