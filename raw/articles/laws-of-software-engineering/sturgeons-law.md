---
title: "Sturgeon's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/sturgeons-law/]
description: "Sturgeon's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-sturgeons-law
source_url: https://lawsofsoftwareengineering.com/laws/sturgeons-law/
source_category: Quality
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:898463b68d908cbb37be199c47c689119db4da12eae9c717138b7acc635c9b98
license: CC-BY-NC-ND-4.0
---

# Sturgeon's Law

90% of everything is crap.

## Takeaways

- It’s like an extreme form of the Pareto Principle (80/20 rule). The bulk of what’s being put out just isn’t good, and the good stuff is the exception
- In software, there are often many features or code paths that add very little value, and the critical challenge is to find a way to maximize the high-impact 10%.
- Most new concepts or technologies fail to deliver, while the exceptional ones stand out.

## Overview

In the tech sphere, Sturgeon’s Law implies that most code or features are not necessary. Perhaps 90% of experiments or features don’t pan out, and only 10% drive real value.

As an engineer, not every line of code you write is gold; as a product manager, many features don’t delight users.

It pairs with the idea of the 10x engineer not as someone who writes 10x more code, but as someone who identifies the 10% of work that delivers 10x value. The risk isn’t the lower quality of the 90%, it’s the pretense that it isn’t. When a team considers all work to have the same value, it introduces more complexity and slows down.

In practice, Sturgeon’s Law encourages continuous refinement, assumes there’s a lot of “noise,” and focuses on finding the “signal.”

## Examples

Consider an app with 100 features. User analytics might show that users heavily use 10 of these and the rest not at all, which is exactly what Sturgeon’s Law predicts: 90% of this stuff doesn’t provide significant value.

Another example: an organization may have many project ideas to develop each quarter. According to Sturgeon’s Law, most of these ideas won’t amount to anything, but a few will prove valuable.

In the area of code reviews, a significant amount of code has been written that is neither elegant nor required. This supports the hypothesis that less code is high-quality.

## Origins

Theodore Sturgeon, a science fiction author, coined this phrase in 1957, responding to criticism that “90% of science fiction is crap.” His response: “90% of everything is crap.”

It was first published as “Sturgeon’s Revelation” in a 1957 issue of Venture magazine.

## Further Reading

- [Sturgeon's Law - Wikipedia Overview of the law and its origins](https://en.wikipedia.org/wiki/Sturgeon%27s_law)
- [Over 50% of plugins in the WordPress repository haven't been updated in 2+ years Reddit discussion illustrating Sturgeon's Law in the WordPress plugin ecosystem](https://www.reddit.com/r/Wordpress/comments/1n0lnas/over_50_of_plugins_in_the_wordpress_repository/)

## Last updated

July 20, 2026

## Related Laws

- [Goodhart's Law](https://lawsofsoftwareengineering.com/laws/goodharts-law/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/sturgeons-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-quality]]
- indexed_by: [[software-engineering-laws-decision-map]]
