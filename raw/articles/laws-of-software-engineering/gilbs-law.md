---
title: "Gilb's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/gilbs-law/]
description: "Gilb's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-gilbs-law
source_url: https://lawsofsoftwareengineering.com/laws/gilbs-law/
source_category: Planning
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:e977bcec239f94b38754970c0993716b6d570ebdedf62f2b88a062253cc645bf
license: CC-BY-NC-ND-4.0
---

# Gilb's Law

Anything you need to quantify can be measured in some way better than not measuring it.

## Takeaways

- It is better to have some data or metric on a phenomenon than to be completely blind, as long as you understand the metric’s limitations.
- In contrast to Goodhart’s Law, which warns about misuse of metrics, Gilb’s Law reminds us not to throw out metrics entirely.
- Start with a basic measure and refine it over time. The act of measuring helps teams focus and identify trends.
- Even an approximate or indirect measurement is better than none.

## Overview

Gilb’s Law responds to the paralysis that Goodhart’s Law can cause. This law asserts that even an approximate or indirect measurement is better than none. When something is essential (performance, customer satisfaction, code maintainability), you should attempt to measure it, because otherwise you have no objective feedback.

Gilb’s Law is a good reply to the statement “this aspect is unmeasurable so we won’t try.” For example, measuring “code quality” is difficult, but you can measure indicators such as cyclomatic complexity, lint warnings, or defect rates as partial indicators. More such indicators can paint the bigger picture.

Those metrics won’t be perfect, but Gilb’s Law suggests that having them gives you some insight and a starting point for improvement, which is better than having no clue at all.

## Examples

Measuring **developer productivity** is notoriously hard (lines of code are poor proxies, story points can be inconsistent). However, you might use deployment frequency or change lead time (as in the DORA metrics for DevOps) as a proxy. They do not capture everything, but they give you actionable data. If deployment frequency decreases, something might be wrong with the pipeline.

Another example is **tracking Tech Debt**. No perfect measure of tech debt exists. But tracking things like code complexity scores, incident rates, and developer surveys gives you visibility you would not otherwise have. As Peter Drucker said: “We cannot improve what we do not measure.”

## Origins

Tom Gilb, a consultant and author on software engineering, formulated this law. It complements his other work on quantifying requirements and using metrics in planning, including Planguage and evolutionary project management.

## Balance with Goodhart's Law

Gilb’s Law and Goodhart’s Law form a complementary pair. Goodhart warns against making metrics into targets that distort behavior. Gilb reminds us that avoiding measurement entirely leaves us blind.

The key is to use metrics for awareness, and to continuously refine what you measure.

## Further Reading

- [Tom Gilb - Wikipedia Overview of Tom Gilb's contributions to software engineering](https://en.wikipedia.org/wiki/Tom_Gilb)
- [Competitive Engineering Tom Gilb's book on quantified requirements and design](https://amzn.to/49AqaT1)
- [DORA Metrics The four key metrics for measuring DevOps performance](https://dora.dev/guides/dora-metrics-four-keys/)

## Last updated

July 20, 2026

## Related Laws

- [Goodhart's Law](https://lawsofsoftwareengineering.com/laws/goodharts-law/)
- [Parkinson's Law](https://lawsofsoftwareengineering.com/laws/parkinsons-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/gilbs-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-planning]]
- indexed_by: [[software-engineering-laws-decision-map]]
