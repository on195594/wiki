---
title: How we make AI coding more cost efficient without sacrificing task quality
created: 2026-09-03
updated: 2026-09-03
type: raw-source
tags: [hermes, agent, ai-coding, workflow, optimization, evaluation]
sources: [docs:https://github.blog/ai-and-ml/github-copilot/how-we-make-ai-coding-more-cost-efficient-without-sacrificing-task-quality/]
status: captured
author: Erik Kristensen and Napalys Klicius
published: 2026-09-02
extraction_route: web_extract
source_quality: full
limitations: GitHub-published vendor engineering article; reported metrics are workload-specific and not an independent audit or Hermes baseline.
---

[Skip to content](#start-of-content)
[Skip to sidebar](#sidebar)

[Blog](https://github.blog/)


* [Changelog](https://github.blog/changelog/)
* [Docs](https://docs.github.com/)
* [Customer stories](https://github.com/customer-stories)

[Try GitHub Copilot app](https://github.com/features/ai/github-app?utm_source=blog-header-button-cta&utm_medium=blog&utm_campaign=github-app-cli-Q1-push)
[Attend GitHub Universe](https://githubuniverse.com/?utm_source=Blog-button&utm_medium=GitHub&utm_campaign=blog_button_seb_uni_26)

* [AI & ML](https://github.blog/ai-and-ml/)
* [Developer skills](https://github.blog/developer-skills/)
* [Engineering](https://github.blog/engineering/)
* [Enterprise software](https://github.blog/enterprise-software/)
* [News & insights](https://github.blog/news-insights/)
* [Open Source](https://github.blog/open-source/)
* [Security](https://github.blog/security/)

[Home](https://github.blog/) / [AI & ML](https://github.blog/ai-and-ml/) / [GitHub Copilot](https://github.blog/ai-and-ml/github-copilot/)

How we make AI coding more cost efficient without sacrificing task quality
==========================================================================

Why shorter outputs can cost more, and how GitHub Copilot reduces wasted work across the complete coding task.

![Copilot hovering above a mosaic of green squares in a decorative scene.](https://github.blog/wp-content/uploads/2026/01/generic-github-copilot-commit-logo.png?resize=1600%2C850)

[Erik Kristensen](https://github.blog/author/erikkrogh/ "Posts by Erik Kristensen") & [Napalys Klicius](https://github.blog/author/napalys/ "Posts by Napalys Klicius")

September 2, 2026

|
11 minutes

* Share:

Output quality is important when working with AI coding agents, but true efficiency comes from getting work done quickly, efficiently, and with the right context.

That’s why token count of individual interactions alone isn’t a meaningful measure of efficiency. The goal shouldn’t be to use fewer tokens, but to tap into the right amount of context to move a task forward. A concise tool response can sometimes require additional calls or work if it leaves out information the agent needs, ultimately making the task slower and more expensive.

That’s why we want to optimize for the outcome rather than the tool call. This post examines four changes in GitHub Copilot that put that principle into practice:

* Preserve useful context while reducing repetitive output.
* Remove formatting that adds no value to the task.
* Shorten instructions without changing useful behavior.
* Deliver completed background work without an extra retrieval step.

Possible changes were evaluated offline using agentic coding benchmarks. The most promising changes were then validated through controlled online experiments before shipping. The examples in this post come from GitHub Copilot CLI. Multiple other Copilot products, such as the GitHub Copilot app and Copilot code review, use the same underlying harness and also become more efficient through these improvements.

![Chart showing 3.1% 'Remove view previxes', 5.5% 'Selective output compaction', 2.9% 'Compact task-tool prompt', and 2.3% 'Reduce notification roundtrips'.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-01.png?resize=1024%2C329)

Figure 1: Four independent A/B experiments using the same AI-credit metric. The segments are shown together for comparison; their effects are not necessarily strictly additive.

The local metric trap
---------------------

It’s common to shorten the output from each tool call as a way to reduce agent costs. [RTK](https://www.rtk-ai.app/docs) (Rust Token Killer) is a utility that shortens shell output before an agent reads it. We evaluated its effect on GitHub Copilot using our agentic coding benchmarks.

In our harness and benchmark configuration, RTK shortened some responses, but when the omitted text mattered, the model sometimes reopened the original output or reran the command to recover what it needed.

Those recovery steps added turns and carried more context forward. The individual tool response was shorter, but on average, the task used more tokens and took longer. We saved tokens locally and spent more globally.

![Flow chart showing: RTK, compresses shell output > Local win, tool output gets shorter > Useful detail is missing > Recovery, reread or rerun > More turns and context carried forward. Then the option of finishing at 'End-to-end result, Tokens and cost up, Task duration up, Task completion: steady,' or 'Recovery repeats' going back to 'useful detail is missing'.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-02.png?resize=1024%2C448)

Figure 2: A shorter tool response can make the completed task more expensive when missing details force the agent to reread output, rerun commands, and carry more context forward.

This result applies to the integration and workloads we tested, not to every RTK configuration or to output compression in general. This meant that tokens per tool call is the wrong objective. An efficiency change has to be evaluated across the complete task, from the user’s request through the final result.

More useful was to look at what can we remove without making the model repeat work.

Compress noise, preserve useful information
-------------------------------------------

The goal was to shorten repetitive output while preserving the context an agent needs to complete its task without retracing steps.

Analysis of benchmark runs showed that install, build, test, and lint output often contains repetitive noise, while source-like output and arbitrary command results are more likely to contain the information an agent needs. That analysis informed a selective output compressor, informed in part by RTK and similar approaches.

The prototype was evaluated on agentic coding benchmarks and a range of open source repositories, exercising their build, test, and lint systems.

Early versions were too aggressive. They made the model repeat work or read the full saved output, increasing end-to-end cost and reducing task success. For example, we initially compressed `git diff` but removed that filter after benchmark tasks showed agents reopening the original output to recover missing information.

Those early failures led to a three-part policy:

1. **Preserve source-like and arbitrary output.** Commands such as `cat`, `git diff`, `git show`, and arbitrary scripts are returned unchanged.
2. **Reorganize search results without dropping content.** Matches and file lists from tools such as `grep` can be grouped more efficiently while retaining every result.
3. **Compress repetitive noise selectively.** Install, build, test, and progress output is compressed only when the savings are substantial.

The shipped version emerged through repeated evaluation and refinement. It is conservative not because the goal was to build a conservative compressor, but because that is what the evaluations supported.

When output is compressed, the agent can still retrieve the complete original through a direct recovery path.

![Flowchart showing how GitHub Copilot handles shell-command output. Copilot calls a shell command, classifies the output, then chooses one of three paths: keep arbitrary/source output unchanged, reorganize search results without losing any matches, or selectively compress repetitive noise (like install/build/test logs) while preserving full output and providing a recovery path. The processed result is returned to Copilot.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-04.png?resize=1024%2C770)

Figure 3: The shipped compressor preserves source-like output, reorganizes search results without loss, and compresses only predictable repetitive noise while retaining the full original.

That recovery path is both a safety mechanism and an evaluation signal. We tracked whether the agent opened the saved original, reran commands, repeated exploration, narrowed its searches, or took additional turns. Frequent recovery would indicate that the compressor had removed something valuable.

On offline tasks where output compression triggered, no statistically significant task-success regression was detected, and agents extremely rarely opened the saved originals. In the online experiment, average cost decreased slightly with no material regression detected in the tracked quality metrics.

Remove formatting before removing information
---------------------------------------------

One clean token optimization came from the `view` tool, which agents use to read file contents into context.

Previously, `view` prefixed every line with a number before showing the contents to the model. Earlier file-editing tools used those numbers to target changes, but current tools instead match surrounding code and do not use line numbers. The line-number prefixes remained even though the normal workflow no longer used them.

Each prefix was small. Repeated across every line and every file read, however, that unused formatting accumulated throughout a session. So, we removed it.

![Before-and-after image of code snippets. The line-number prefixes re removed from the 'After' image.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-03.png?resize=1024%2C185)

Figure 4: Removing line-number prefixes preserves the source exactly while eliminating formatting that was repeated across every file read.

Line numbers remain useful in diffs and short snippets. They were wasteful here because they were attached to every file read without serving the current editing workflow.

Removing them caused model-inference cost to fall by roughly 5% in offline agentic coding benchmarks. Success rates stayed within the expected run-to-run variance, and edit failures did not increase.

We then tested the change with Copilot CLI users. The online experiment reduced average daily model-inference cost per user by about 3%, with no material regression detected in the quality or satisfaction metrics we tracked.

For developers, that means more of the context window is available for the work itself rather than formatting the agent does not use.

This was the ideal change: no new instructions for the model, no source of information to recover, and no additional decision to make. The file contents reached the model unchanged.

Compress prompts without compressing intent
-------------------------------------------

Prompts carry instructions that shape how an agent works, and they are sent to the model on every turn. Shortening them only improves efficiency if the agent keeps the behaviors developers depend on.

In GitHub Copilot, the task tool launches specialized agents for parallel work. Its guidance had accumulated across tool descriptions, schemas, agent definitions, system instructions, and companion tools.

A meta-prompting loop, in which Copilot iteratively wrote its own prompt, reduced that prompt by roughly half. Copilot produced and refined smaller candidates, and targeted behavioral tests checked the requirements we wanted to preserve.

The first online experiment found a regression that the initial offline evaluations had missed. The meta-prompting loop had rewritten cautious parallelism guidance into a hard scheduling policy, causing independent custom agents to run sequentially.

We stopped the experiment. Before changing the prompt again, we wrote a regression evaluation for the behavior users had exposed. The eventual fix replaced an explicit allowlist and denylist with one sentence:

*Independent agents can run in parallel; consider side effects.*

That sentence was shorter and less restrictive; it deferred the choice of whether to run sub-agents in parallel to the model instead of the previous explicit guidance. With it, our new behavior test passed without causing any existing behavioral tests to fail.

Prompt behavior needs tests. If a behavior is not tested, a shorter prompt can remove it without anyone noticing.

![Three-stage diagram labeled Compression → Regression + fix → Completed. Left panel shows an original prompt compressed by about 50%. Middle panel highlights a regression where agents became serialized, then a fix by editing one sentence to restore parallelism. Right panel shows final shipped prompt with restored behavior and cumulative savings of about 1,300 fewer tokens per turn across steps.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-05.png?resize=1024%2C550)

Figure 5 Prompt compression became safe only after a regression test exposed serialized agents and a one-sentence fix restored parallelism; the resulting token savings recur on every model turn.

The shipped prompt removes about 1,300 `task`-tool prompt tokens per turn, corresponding to approximately 1.8% fewer total prompt tokens per session and 2.9% lower normalized cost per active hour, with no quality regression detected in the measured evaluations.

Deliver completed background work without an extra retrieval turn
-----------------------------------------------------------------

Agents often run independent work in the background, such as a long-running shell command alongside a sub-agent investigation. Notifications let the agent continue until that work is ready without spending a tool call waiting.

If the agent does not explicitly wait for either task, the harness wakes the model and notifies it when the shell command or sub-agent finishes.

Previously, that notification did not include the completed result, so the agent had to spend another turn retrieving output Copilot had already received. When several tasks finished close together, that detour could repeat. Copilot now batches eligible completion notifications and delivers completed results directly in the existing tool-result format. The agent can continue with the information it needs, without spending an extra turn asking for it again. Explicit reads for work that is still running behave as before.

![Before-and-after sequence diagram comparing orchestration behavior.

Before: model waits on separate shell and sub-agent completions, causing retrieval detours and four LLM calls to process two results.
After: a harness batches related completions and emits synthetic tool events so background work continues while waiting; both results are processed together in a single LLM call.
The visual emphasizes reduced latency and fewer model round trips.](https://github.blog/wp-content/uploads/2026/09/Blog-Graphic-06.png?resize=1024%2C671)

Figure 6 Before, each background completion could wake a retrieval-only model turn. After, the harness batches eligible completions and delivers completed results in the existing tool-result format.

Before this change, each completed task required one model call to request its result and another to process it. For the shell command and sub-agent shown above, that meant four model calls before work could continue.

Now, the harness batches both completions and supplies their results together, so a single model call can process both. Removing those retrieval detours also avoids carrying the full session context through unnecessary calls.

By delivering completed results directly, without compressing, summarizing, or withholding anything, the harness reduced average token-related usage, as measured in AI Credits, by about 2.3%.

Measure changes in context
--------------------------

A change that saves tokens in one Copilot workflow can increase costs in another.

For example, a tighter set of file-tool instructions was inspired by positive results in Copilot code review. In a Copilot CLI online experiment, it increased cost, so we did not ship it.

By contrast, removing line-number prefixes and selectively compressing output each reduced average prompt tokens per review by roughly 5% in independent evaluations across a large set of Copilot code review tasks using the production model. We detected no material change in the tracked review-quality metrics.

These findings are separate from [the earlier migration of Copilot code review to the shared file tools](https://github.blog/changelog/2026-06-25-copilot-code-review-analysis-depth-and-efficiency-updates/), which, together with review-instruction tuning, reduced code review cost by about 20%.

Each change needs to be measured in the workflow where it runs.

Five lessons for building efficient AI coding agents
----------------------------------------------------

1. **Optimize the completed task, not the tool call.** Shorter output is not cheaper if the agent spends more turns recovering what was removed.
2. **Optimize orchestration, not just model output.** Eliminate model turns that perform work the harness can complete deterministically.
3. **Compress by what the output represents.** Preserve exact content, prefer lossless transformations, and measure how often agents use the recovery path.
4. **Prompt rewrites sometimes have unintended consequences.** Validate that intended behavior is preserved.
5. **Evidence is local to the workload.** Re-evaluate changes in offline benchmarks, online experiments, and every product surface where they ship.

None of these changes made the model smarter. They removed work the model never needed to do.

The changes described in this post are shipping across GitHub Copilot experiences that use the same underlying harness.

Bring agentic workflows to your terminal
with [GitHub Copilot CLI >](https://github.com/features/copilot/cli)

---

Tags:
-----

* [agentic AI](https://github.blog/tag/agentic-ai/)
* [GitHub Copilot](https://github.blog/tag/github-copilot/)
* [GitHub Copilot CLI](https://github.blog/tag/github-copilot-cli/)
* [GitHub Copilot code review](https://github.blog/tag/github-copilot-code-review/)
* [LLMs](https://github.blog/tag/llms/)
* [prompt engineering](https://github.blog/tag/prompt-engineering/)

Written by
----------

![Erik Kristensen](https://avatars.githubusercontent.com/u/54990334?v=4&s=200)

### [Erik Kristensen](https://github.blog/author/erikkrogh/)

[@erik-krogh](https://github.com/erik-krogh)

Erik Krogh Kristensen is a Staff Software Engineer at GitHub building at the intersection of AI, coding, and security. In the last few years at GitHub he's worked on an assortment of AI products such as Copilot Autofix, Copilot Code Review, and most recently Copilot CLI. He's a trusted source of how to make AI coding products better and more efficient.

![Napalys Klicius](https://avatars.githubusercontent.com/u/11835209?v=4&s=200)

### [Napalys Klicius](https://github.blog/author/napalys/)

[@Napalys](https://github.com/napalys)

Napalys Klicius is a Software Engineer at GitHub building agentic systems. His career has taken him from model checking to low-level C++ drone systems and static analysis, and more recently to teaching agents how to inspect code without getting lost.

* [agentic AI](https://github.blog/tag/agentic-ai/)
* [GitHub Copilot](https://github.blog/tag/github-copilot/)
* [GitHub Copilot CLI](https://github.blog/tag/github-copilot-cli/)
* [GitHub Copilot code review](https://github.blog/tag/github-copilot-code-review/)
* [LLMs](https://github.blog/tag/llms/)
* [prompt engineering](https://github.blog/tag/prompt-engineering/)

Table of Contents
-----------------

* [The local metric trap](#h-the-local-metric-trap)
* [Compress noise, preserve useful information](#h-compress-noise-preserve-useful-information)
* [Remove formatting before removing information](#h-remove-formatting-before-removing-information)
* [Compress prompts without compressing intent](#h-compress-prompts-without-compressing-intent)
* [Deliver completed background work without an extra retrieval turn](#h-deliver-completed-background-work-without-an-extra-retrieval-turn)
* [Measure changes in context](#h-measure-changes-in-context)
* [Five lessons for building efficient AI coding agents](#h-five-lessons-for-building-efficient-ai-coding-agents)

More on [agentic AI](https://github.blog/tag/agentic-ai/)
---------------------------------------------------------

### [Decoding the new AI lingo: Loops, harnesses, squads, hill climbing... oh my!](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/)

From loop engineering to harnesses, squads, and open weights, the GitHub Podcast breaks down the AI terms showing up in developer conversations.

[Cassidy Williams](https://github.blog/author/cassidoo/ "Posts by Cassidy Williams")

### [Evaluating performance and efficiency of the GitHub Copilot agentic harness across models and tasks](https://github.blog/ai-and-ml/github-copilot/evaluating-performance-and-efficiency-of-the-github-copilot-agentic-harness-across-models-and-tasks/)

Explore how the GitHub Copilot agentic harness delivers strong results across multiple benchmarks and leading token efficiency, while maintaining flexibility to choose among more than 20 models.

[Shibani Basava](https://github.blog/author/shibbas/ "Posts by Shibani Basava") & [Carlos Castro](https://github.blog/author/carlosscastro/ "Posts by Carlos Castro")

Related posts
-------------

![GitHub Podcast imagery](https://github.blog/wp-content/uploads/2025/07/LinkedIn-Light-Mode-16x9-1.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

### [Decoding the new AI lingo: Loops, harnesses, squads, hill climbing… oh my!](https://github.blog/ai-and-ml/decoding-the-new-ai-lingo-loops-harnesses-squads-hill-climbing-oh-my/)

From loop engineering to harnesses, squads, and open weights, the GitHub Podcast breaks down the AI terms showing up in developer conversations.

[Cassidy Williams](https://github.blog/author/cassidoo/ "Posts by Cassidy Williams")

![GitHub Copilot app for Beginners: Work that runs itself.](https://github.blog/wp-content/uploads/2026/08/Screenshot-2026-08-26-at-12.57.57-PM.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

### [GitHub Copilot app for Beginners: Automate Dependabot pull request triage](https://github.blog/ai-and-ml/github-copilot/github-copilot-app-for-beginners-automate-dependabot-pull-request-triage/)

Managing library updates can be tedious at times. Learn how the GitHub Copilot app can handle this type of repetitive task.

[Christopher Harrison](https://github.blog/author/geektrainer/ "Posts by Christopher Harrison")

![Decorative background featuring floating green cubes, including one with the GitHub invertocat logo.](https://github.blog/wp-content/uploads/2026/01/4ba0cd42388a255e04c78e5143548f22e577d68e0f15f68e6a3c76c18b927981-1920x1080-1.png?resize=400%2C212)

[AI & ML](https://github.blog/ai-and-ml/)

### [How to evaluate LLMs before production](https://github.blog/ai-and-ml/llms/how-to-evaluate-llms-before-production/)

These are the lessons we learned evaluating LLMs for real-world secret scanning.

[Mariko Wakabayashi](https://github.blog/author/mwakaba2/ "Posts by Mariko Wakabayashi") & [Zixiao Chen](https://github.blog/author/zixiaochen/ "Posts by Zixiao Chen")

Explore more from GitHub
------------------------

![Docs](https://github.blog/wp-content/uploads/2024/07/Icon-Circle.svg)

### Docs

Everything you need to master GitHub, all in one place.

[Go to Docs](https://docs.github.com/)

![GitHub](https://github.blog/wp-content/uploads/2024/07/recirculation-github-icon.svg)

### GitHub

Build what’s next on GitHub, the place for anyone from anywhere to build anything.

[Start building](https://github.com/)

![Customer stories](https://github.blog/wp-content/uploads/2024/07/Icon_da43dc.svg)

### Customer stories

Meet the companies and engineering teams that build with GitHub.

[Learn more](https://github.com/customer-stories)

![GitHub Universe 2026](https://github.blog/wp-content/uploads/2025/06/Universe26-Icon.svg)

### GitHub Universe 2026

Join us October 28-29 in San Francisco or online for GitHub Universe, our flagship developer event uniting people, agents, and the world’s code.

[Register now](https://githubuniverse.com/?utm_source=Blog&utm_medium=GitHub&utm_campaign=module_uni_26)

We do newsletters, too
----------------------

Discover tips, technical guides, and best practices in our biweekly newsletter just for devs.

Your email address


Your email address

Subscribe

Yes please, I’d like GitHub and affiliates to use my information for personalized communications, targeted advertising and campaign effectiveness. See the [GitHub Privacy Statement](https://github.com/site/privacy) for more details.

Subscribe

Site-wide Links
---------------

### Product

* [Features](https://github.com/features)
* [Security](https://github.com/security)
* [Enterprise](https://github.com/enterprise)
* [Customer Stories](https://github.com/customer-stories?type=enterprise)
* [Pricing](https://github.com/pricing)
* [Resources](https://resources.github.com/)

### Platform

* [Developer API](https://developer.github.com/)
* [Partners](https://partner.github.com/)
* [Atom](https://atom.io/)
* [Electron](https://www.electronjs.org/)
* [GitHub Desktop](https://desktop.github.com/)

### Support

* [Docs](https://docs.github.com/)
* [Community Forum](https://github.community/)
* [Training](https://services.github.com/)
* [Status](https://www.githubstatus.com/)
* [Contact](https://support.github.com/)

### Company

* [About](https://github.com/about)
* [Blog](https://github.blog/)
* [Careers](https://github.com/about/careers)
* [Press](https://github.com/about/press)
* [Shop](https://shop.github.com/)

* © 2026 GitHub, Inc.
* [Terms](https://docs.github.com/en/github/site-policy/github-terms-of-service)
* [Privacy](https://docs.github.com/en/github/site-policy/github-privacy-statement)
* Manage Cookies
* Do not share my personal information

* [GitHub on LinkedIn](https://www.linkedin.com/company/github)
* [GitHub on Instagram](https://www.instagram.com/github/)
* [GitHub on YouTube](https://www.youtube.com/github)
* [GitHub on X](https://twitter.com/github)
* [GitHub on TikTok](https://www.tiktok.com/@github)
* [GitHub on Twitch](https://www.twitch.tv/github)
* [GitHub’s organization on GitHub](https://github.com/github)
