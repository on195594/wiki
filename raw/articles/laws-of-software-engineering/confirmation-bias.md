---
title: "Confirmation Bias"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/confirmation-bias/]
description: "Confirmation Bias 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-confirmation-bias
source_url: https://lawsofsoftwareengineering.com/laws/confirmation-bias/
source_category: Decisions
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:b3927427f3ea3557b4d7492a561b0a2f2c222044d7e6f1416fc0d5e411a4f666
license: CC-BY-NC-ND-4.0
---

# Confirmation Bias

A tendency to favor information that supports our existing beliefs or ideas.

## Takeaways

- When reviewing code or debugging, notice if you’re only looking for evidence that supports your initial hunch.
- Challenge yourself when actively thinking about problems. If you have an opinion about an issue, try to ask, ‘What would I expect to see if I’m wrong?’ In this, we can counteract our natural bias only to confirm.
- Regarding team decision-making (for example, tech stacks and/or design decisions), seek input from people with differing opinions. Bias confirmation can be overcome by looking into alternative solutions. For example, if the whole team ‘feels’ that technology X is the superior choice, assign someone to look into the opposing view on technology X.
- Base decision-making on objective criteria (facts, not opinions). Automated tests, performance criteria, and experimentation (A/B tests) can provide truths regardless of human bias.

## Overview

We all like to be right. Confirmation bias is our mind’s way of cheating to feel right more often. Psychologically, once we form an opinion, we subconsciously filter information, noticing bits that support our view and ignoring those that contradict it.

In software, a typical scenario is debugging. A developer convinced that module A caused a production issue will comb through module A’s code intensively. If module B (assumed to be fine) is also throwing errors, they might not even look there, missing the real cause. Awareness of this bias leads to asking “What am I missing? Maybe there is another explanation?” and encouraging environments where beliefs are constructively questioned.

## Examples

In code reviews, a reviewer who trusts a colleague’s skills might skim over potential issues, assuming the code is probably fine. Or the opposite: a reviewer expecting sloppy code from a junior developer might find “issues” that aren’t really important.

Confirmation bias also affects testing. A developer may write unit tests that assert the code works on typical inputs (happy path), but might not try edge cases that could break it. Teams combat this through code reviews with fresh eyes, writing tests specifically aimed at breaking their own code, and post-mortems asking “What went wrong and why didn’t we see it?”

By checking for confirmation bias, engineers can become better at solving problems with an open and critical mind.

## Origins

One of the first to identify confirmation bias was Peter Cathcart Wason, an English cognitive psychologist. In 1960, he conducted a famous experiment (Wason’s rule discovery task) where participants had to guess a rule for a sequence of numbers. He found people tended to test sequences that would confirm their initial thoughts rather than those that could prove them wrong.

Wason coined the term “confirmation bias” to explain this phenomenon. Since then, countless studies have confirmed the existence of confirmation bias in human reasoning.

## Further Reading

- [Confirmation Bias: A Ubiquitous Phenomenon in Many Guises Raymond Nickerson's comprehensive 1998 review of confirmation bias research](https://journals.sagepub.com/doi/10.1037/1089-2680.2.2.175)
- [On the Failure to Eliminate Hypotheses in a Conceptual Task Peter Wason's 1960 foundational paper on the rule discovery task](https://www.tandfonline.com/doi/abs/10.1080/17470216008416717)
- [Thinking, Fast and Slow Daniel Kahneman's exploration of cognitive biases including confirmation bias](https://amzn.to/48WboH0)

## Last updated

July 20, 2026

## Related Laws

- [Dunning-Kruger Effect](https://lawsofsoftwareengineering.com/laws/dunning-kruger-effect/)
- [Hanlon's Razor](https://lawsofsoftwareengineering.com/laws/hanlons-razor/)
- [Goodhart's Law](https://lawsofsoftwareengineering.com/laws/goodharts-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/confirmation-bias/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-decisions]]
- indexed_by: [[software-engineering-laws-decision-map]]
