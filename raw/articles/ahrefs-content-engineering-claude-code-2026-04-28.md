---
title: How I Do Content Engineering with Claude Code
author: Ryan Law
source_type: article
source_url: https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/
published_at: 2026-04-28T13:00:56+00:00
captured_at: 2026-04-30 12:51:54 +0800
status: raw
tags: [claude-code, content-engineering, agent, workflow, skill-files, seo, mcp]
---

# How I Do Content Engineering with Claude Code

## Source note
This raw page captures the reusable knowledge from Ryan Law's Ahrefs article about building a content automation workflow with Claude Code and custom skill files. The article was originally shared through a `share.google` link and resolved to the canonical Ahrefs URL.

## Core claim
Ahrefs built a high-quality content automation system by translating an existing human editorial process into a chain of Claude Code skill files, backed by real SEO/product data and human review. The important pattern is not "AI writes articles", but "expert workflow becomes a debuggable agentic pipeline".

## Key points
- The system uses about 23 custom skill files plus a main `blog-pipeline` skill to move from keyword idea to near-finished article draft.
- Draft generation reportedly takes 6-12 minutes, compared with an earlier ChatGPT-based process that still needed hours or days of manual intervention.
- The workflow had been used to publish about 15 articles and update about 30 more at the time of publication.
- The author stresses that quality depends on existing editorial expertise: the skill files work because they encode years of content marketing judgment.
- The workflow is scoped to informational SEO content on topics Ahrefs already understands and can verify.
- The system does not aim to scale content volume indiscriminately; it is meant to maintain an evergreen library and reduce editorial drudgery.
- Every pipeline stage emits an intermediate file so failures can be inspected, corrected, and restarted from a known-good point.
- Anthropic's `skill-creator` is used to test and improve the skill files by comparing outputs with and without custom guidance.
- Claude is connected to real data through Ahrefs MCP and other mandated sources: keyword metrics, SERP reports, competitor pages, research sources, and product feature documents.
- Human direction is front-loaded through a context parameter that gives the pipeline angle, sentiment, subtopics, and product emphasis before drafting begins.
- Generated articles are rendered into Ahrefs-style HTML previews for easier human review.
- The workflow is designed to be forked and personalized by other team members instead of enforcing one universal process.

## Hermes/LifeOS relevance
- Treats skills as executable process fragments, not just prompt snippets.
- Shows why strong source data and MCP/tool access matter more than model fluency alone.
- Reinforces the Hermes rule that complex outputs need intermediate artifacts and verification, not one-shot generation.
- Provides a concrete external case for turning expert judgment into a reusable pipeline without hiding the need for human review.

## Limitations
- Not directly reusable without strong editorial judgment and domain-specific data.
- Best suited to repeatable, well-understood content types rather than open-ended creative or unfamiliar domains.
- The article describes a company-specific workflow; the durable value is the design pattern, not the exact Ahrefs process.

## Extracted article text

Title: How I Do Content Engineering with Claude Code

URL Source: http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/

Published Time: 2026-04-28T13:00:56+00:00

Markdown Content:
Article Performance

Data from Ahrefs

*   Linking websites 

The number of websites linking to this post.

This post's estimated monthly organic search traffic.

Contents

*   [Important caveats](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#important-caveats "Important caveats")
*   [1. Mimic human workflows by chaining editorial skills](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#one "1. Mimic human workflows by chaining editorial skills")
*   [2. Output every step of the process for iteration and troubleshooting](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#two "2. Output every step of the process for iteration and troubleshooting")
*   [3. Create test cases for recursive self-improvement](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#three "3. Create test cases for recursive self-improvement")
*   [4. Give LLMs great data from great sources](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#four "4. Give LLMs great data from great sources")
*   [5. Front-load human directions](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#five "5. Front-load human directions")
*   [6. Build interactive previews for review and editing](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#six "6. Build interactive previews for review and editing")
*   [7. Fork and personalise](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/#seven "7. Fork and personalise")

Here’s how I built a high-quality content automation system for the Ahrefs blog using Claude Code and 23 skill files.

Back in August 2025, I shared the [AI content process](https://ahrefs.com/blog/my-complete-ai-content-process-for-ahrefs/) I had developed for the Ahrefs blog. It used ChatGPT projects and custom GPTs to speed up certain types of content creation from several days to a couple of hours, but still required tons of manual intervention.

Now, barely eight months later, I’m sharing our new process. I use Claude Code and 23 custom skill files, chained together, to generate publish-ready article drafts in six to twelve minutes. We have published around 15 articles with this new process, and updated some 30 or so more.

I’ve been using AI to help create content marketing since 2020. It has been useful in effortful, piecemeal ways. But today it is good enough to automate important parts of content marketing with no loss in quality (and even a significant gain in some areas, like research). Or as I put in a recent article: [AI content wasn’t good enough. Now it is.](https://ahrefs.com/blog/ai-content-wasnt-good-enough-now-it-is/)

As a result, I suggested a pretty bold direction in our company Slack, back in February:

![Image 1](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-1.png)

Here’s our AI current content process.

Watch this process on YouTube

Check out this episode of the [Ahrefs podcast](https://www.youtube.com/watch?v=iVZrVeESnFQ) to watch me demo our content automation system to Ahrefs’ CMO, Tim Soulo.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)Important caveats

Before we get to the good stuff, I once again want to direct your attention to some important caveats:

### [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)Experience matters

AI content is not, by default, good. This process works well because it mirrors our existing human editorial process, built from decades of collective content marketing experience. Or as someone in a [LinkedIn comment](https://www.linkedin.com/feed/update/urn:li:activity:7443574113673129984?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7443574113673129984%2C7443604427044896768%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287443604427044896768%2Curn%3Ali%3Aactivity%3A7443574113673129984%29) put it, very articulately:

> _“Ryan’s SKILL files are good because Ryan already knew what to put in them. Most people using blank-slate tools don’t have 13 years of editorial experience to build from. The gap isn’t just in the tool. It’s in the person behind it too.”_

![Image 2](https://ahrefs.com/blog/wp-content/uploads/2026/04/2026-04-27_14-13-22.png)

### [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)Topic selection still matters

This process is geared specifically towards informational SEO content. I only use this process on topics that I understand well, so that I can review each article to validate its claims, correct misinformation, and make sure I feel happy putting it out into the world.

I also focus primarily on topics that Ahrefs has already covered (in some capacity), allowing us to use hundreds of existing, high-quality articles as a reference point for new content.

### [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)We have no plans to “scale content” with AI

I could use this process to scale the Ahrefs blog to tens of thousands of articles. I will not. It would not be in the interests of Ahrefs or our customers.

Instead, I am using this workflow to help us maintain an evergreen library of useful content on a handful of core topics. My goal is to remove drudgery and focus human grey matter on the parts of marketing that benefit most from it.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)1. Mimic human workflows by chaining editorial skills

At the heart of this process are ~23 skill files that correspond to different parts of the Ahrefs editorial process, from conducting keyword research to topic gap analysis to structural outlining:

![Image 3](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-2.png)

Each skill file includes a Markdown-formatted explanation of how Claude (or any LLM) should conduct each process, best-practice examples to emulate, and formatting instructions for the expected output.

Many of these skills are adapted from our existing, human-written process documentation. Others are written from scratch, and some are generated and edited entirely by AI.

![Image 4](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-3.png)

Every skill can be used in isolation, but I also created a main skill (`blog-pipeline`) that instructs the LLM to trigger each of these skills in a particular order, working sequentially through every process to take a keyword idea through to (nearly) finished article:

![Image 5](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-4.png)

Theoretically, this process can be _fully automated._ Using the skill files I created, Claude can trigger a daily content gap analysis using the [Ahrefs MCP](https://docs.ahrefs.com/mcp/docs/introduction), review and prioritize the best keywords to target, and kick off the entire `blog-pipeline` workflow, notifying me when new article drafts are ready for review.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)2. Output every step of the process for iteration and troubleshooting

One risk of agentic content creation: if you get an article at the end of a ten minute run, and it’s bad, it’s hard to diagnose precisely where and why the process went wrong.

For that reason, every step of this process produces its own output file. For example, when the outline is generated, the outline is handed over to the next stage of the process, but also saved as a markdown file in the outlines folder.

![Image 6](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-5.png)

I can review every single stage of the process, tweak that particular output (and the corresponding skill file), and restart from the last stage that meets my quality criteria.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)3. Create test cases for recursive self-improvement

As LLM model capabilities get better and better, I’m often surprised at how good frontier models are at very specific tasks, even without any concrete direction or examples provided. Sometimes, convoluted skill files are actually inferior to giving the model a single-sentence prompt and getting out of its way.

We’ve been using Anthropic’s skill-creator skill to test and improve our workflow. [The skill](https://github.com/anthropics/skills/tree/main/skills/skill-creator) tests each stage of the process, generating outlines, research primers and drafts both with and without the guidance provided in our custom skill files.

![Image 7](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-6.jpg)

The LLM reviews the outputs and makes suggestions for how to improve the skill file for more consistent results.

It’s easy for skill files to become long and bloated, and in doing so, make it less likely that their guidance will be correctly applied by the LLM. This process allows me to continually shorten skills to their most effective essence, and remove skills that don’t have any real bearing on my desired output.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## 4. [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)Give LLMs great data from great sources

This process is only possible because Claude has access to the [Ahrefs MCP](https://docs.ahrefs.com/mcp/docs/introduction).

Instead of hallucinating fake SEO data, Claude can pull keyword metrics, parent topic, and long-tail keyword variations for every article, straight from Ahrefs.

It uses the questions report to surface commonly asked questions and groups them into themes, and it retrieves the SERP overview to understand the dominant search intent and what type of content is ranking.

![Image 8](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-7.png)

As well as great SEO data, my skill files also include specific instructions to use other important data sources, like:

*   **Competitor data:** key topics, headers and content gaps are extracted from top-ranking articles on the same keyword.
*   **Deep research:** trusted news and research sources are reviewed for recent information on the target keyword.
*   **Product features:** the LLM has access to an overview of every Ahrefs product and feature, saved in a Markdown document, along with their most important use cases.

By default, LLMs are very convincing bloviators: they can generate content that sounds coherent, without containing any concrete data or substance. Mandating specific data sources to use is key to getting great results.

Get Ahrefs data in your AI tools

The Ahrefs API and MCP are now available in all paid plans from Lite and above, so it’s easier than ever to get world-class Ahrefs SEO and AEO data in your dashboard, application or content workflow.

Need some inspiration to get started? Read this: [15 Ahrefs MCP Use Cases for SEOs & Digital Marketers](https://ahrefs.com/blog/mcp-use-cases/)

![Image 9](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-8.png)

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## 5. [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)Front-load human direction

A big part of our previous AI content process was front-loading human input. My thesis is that small amounts of expert direction provided at the _start_ of the content creation process are vastly more effective than lots of human editing at the end.

I wanted to allow for this direction without requiring a full-blown content brief to be created, so I added a context parameter to the `blog-pipeline` skill that allows the user to provide context to guide the content creation process.

If you want to generate an article about “content gap analysis”, you can add high-level direction like this:

> _“Take a ‘steal your competitors’ best content’ angle, feature Keywords Explorer’s Content Gap tool heavily, and include a section on finding quick-win keywords your competitors rank for but you don’t.”_

![Image 10](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-9.jpg)

I use this to mention specific sub-topics to cover, overarching angles and sentiments to shape the article, and specific product features to mention. This context is saved to a dedicated file and used as a reference in the drafting skill.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## 6[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/). Build interactive previews for review and editing

I read every word of every article that makes its way onto the Ahrefs blog. Reading Markdown files in VS Code isn’t my idea of a good time, so I use a simple skill that turns each generated article into a Ahrefs-style HTML preview that opens automatically in Chrome.

![Image 11](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-10.png)

Sidenote.

As you can see in the image above, blog post images are not a solved problem, yet—I’m currently experimenting with skills to trigger a headless browser that can navigate to specific Ahrefs reports, take screenshots, annotate them, and insert them into the article draft.

I’m also experimenting with interactive previews that allow me to accept or decline updates to existing content, and leave in-line comments for Claude to action. At this point, we’re straying into fully-fledged application territory, so stay tuned for the v3 of my content process.

![Image 12](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-11.jpg)

When I’m happy with the article draft and ready to upload and add images, I trigger a final skill that formats the article with all the correct tables and shortcodes we need.

[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)
## 7[](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/). Fork and personalise

This content process is built to my personal specifications. It references my favourite articles to shape each articles tone and style. It prioritises my favorite data sources. And most importantly, it’s built to mirror my writing process, approaching content creation in a way that matches how my brain operates.

But there is no “best” way to create content. Even on the Ahrefs blog team, there are a wealth of different styles, preferences and workflows that shapes how content gets made.

I want our AI content processes to reflect all our idiosyncrasies, so I encouraged the team to fork this repo and use Claude Code to modify it to their unique specifications, adding and removing steps of the process, changing the data sources and reports it uses, and learning from the style and voice of their own best articles.

![Image 13](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-12.jpg)

The goal is for everyone on the team to have their own personalised content copilot, able to work to their specifications and play to their strengths.

## [](http://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/)The future

If you follow the Ahrefs blog, I’d wager that you haven’t noticed any major changes, despite the fact that we’ve been using generative AI to help with more and more of our work.

That’s because we’re not using AI to “scale our output” and publish thousands of articles, and we’re not making trade-offs by substituting quality for speed. Instead, we’re using it to automate the most formulaic parts of work, and only in those situations where AI can do the job as well as, or even better than, a skilled human could.

AI is helping us to fill content gaps and update our evergreen library of search content. In the meantime, the Ahrefs blog team can use our energy in other ways: conducting research and writing thought leadership, hosting webinars and giving in-person talks, and building systems to further automate the most tedious parts of our lives.

For all the fear-mongering around AI and content creation, this is a lot of fun.

_P.S. I’m already building version three of this content system, and it’s something you can use too. [Join this waitlist](https://ahrefs.com/agent-a) to get early access._

![Image 14](https://ahrefs.com/blog/wp-content/uploads/2026/04/word-image-196558-13.jpg)

