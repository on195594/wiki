---
title: "Price's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/prices-law/]
description: "Price's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-prices-law
source_url: https://lawsofsoftwareengineering.com/laws/prices-law/
source_category: Teams
source_experience: senior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:a74036f06a4769a81c86085a9b4ae3e305f773db834f3470a926f582c3c240e3
license: CC-BY-NC-ND-4.0
---

# Price's Law

The square root of the total number of participants does 50% of the work.

## Takeaways

- A small fraction of people often contribute a significant fraction of the results. In a 100-person engineering org, about 10 people might produce half of the output.
- As teams grow, productive output doesn’t scale linearly. Adding more people increases total output, but many will make smaller contributions than the core group.
- Knowing this helps in team planning and understanding why losing specific individuals has a significant impact on productivity.
- It’s wise to identify and retain the small group of people who are essential to the company’s output.

## Overview

You probably noticed that most of the major work depends on just a few people in your organization, and that is not false. In software teams, it means a relatively small group of engineers will deliver a disproportionately large part of the value. This is similar to the Pareto principle (80/20 rule) but even more extreme for larger groups.

Price’s Law suggests that simply hiring more developers won’t necessarily scale output as expected. Beyond a point, many may contribute little or be working on peripheral tasks. It’s an argument for focusing on quality when hiring: a single excellent engineer can outperform several average ones. However, we must be careful with this “law” as we don’t want to make other people feel useless, as they may be doing essential tasks that are given less importance.

It highlights a risk: if those top √N contributors leave, you lose a large chunk of productivity, so retention and preventing burnout for them are critical.

## Examples

Take an open-source project on GitHub with 30 contributors. Often, you’ll see that maybe 5 contributors (roughly √30 ≈ 5) are responsible for about half the code commits or major features. The rest contribute smaller patches or documentation.

A notable example is when Twitter cut staff after Musk bought it, yet the product kept running. Before the takeover, Twitter had roughly 7,500 employees, meaning √7,500 ≈ 87. Price’s law suggests that when the new leadership decided to lay off almost 50% of staff, the platform could still operate if the core 80-100 people stayed. But this holds only if the proper people are selected. The law won’t predict reliability, as layoffs strip redundancy in SRE, security, and moderation. Twitter even asked some laid-off workers to return, a signal that it missed critical skills.

## Origins

**Derek de Solla Price**, a British physicist, historian of science, and information scientist, discovered this pattern while studying his peers in academia. He noticed that there were always a handful of people who dominated publications within a subject.

He introduced this concept in his 1963 book “Little Science, Big Science” as part of his broader research on scientific productivity and information dynamics. The law has since been generalized to various fields, though empirical data suggests it’s more of a model than an absolute rule, as the related Lotka’s law often fits better.

## Further Reading

- [Price's Law - Wikipedia Wikipedia article on Price's Law and its empirical challenges](https://en.wikipedia.org/wiki/Price%27s_law)
- [Derek J. de Solla Price - Wikipedia Biography of the scientist who discovered the law](https://en.wikipedia.org/wiki/Derek_J._de_Solla_Price)

## Last updated

June 24, 2026

## Related Laws

- [The Ringelmann Effect](https://lawsofsoftwareengineering.com/laws/ringelmann-effect/)
- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Dunbar's Number](https://lawsofsoftwareengineering.com/laws/dunbars-number/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/prices-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-teams]]
- indexed_by: [[software-engineering-laws-decision-map]]
