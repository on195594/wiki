---
title: "Goodhart's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/goodharts-law/]
description: "Goodhart's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-goodharts-law
source_url: https://lawsofsoftwareengineering.com/laws/goodharts-law/
source_category: Planning
source_experience: senior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:0b45c192ce12d873dd60b9a1488e0b136556c9b438c0d1fcddd06c572ca076c3
license: CC-BY-NC-ND-4.0
---

# Goodhart's Law

When a measure becomes a target, it ceases to be a good measure.

## Takeaways

- If you set a particular metric as a goal (e.g., lines of code written, number of features closed), people will find ways to optimize for that metric.
- Metrics are proxies for what you value (productivity, quality, etc.). Once they’re targets, people meet the metric even if it undermines the original intent.
- Metrics are useful for insight, but they must be used in context and balanced with qualitative judgment.
- Combine multiple metrics to avoid a singular focus that can be gamed.

## Overview

Goodhart’s Law comes from economics and is very relevant to software teams. For instance, a manager might set a target that “we must close 100 bug tickets this month.” Developers, feeling pressure, might start closing tickets that are not truly resolved or splitting a single bug into multiple tickets to inflate numbers.

The metric (tickets closed) goes up, but software quality might not. Making the metric a goal distorts the process, so it loses its correlation with actual success. This is why experienced leaders use metrics as indicators rather than targets, and always consider the broader context.

## Examples

A software team was rewarded based on the lines of code written. Developers start writing verbose code and copying and pasting into multiple places (violating DRY) to increase the line count. The software becomes bloated while the metric looks great.

Another example: a QA team measured by the number of test cases executed favored running many easy tests rather than doing proper testing. They met objectives but missed critical bugs.

Similarly, when teams focus on **code coverage percentage** as a primary target, developers write trivial unit tests that do not assert meaningful behavior, while necessary integration tests are skipped.

A recent variant is measuring AI tokens consumed per engineer (a practice sometimes called **tokenmaxxing**), where more tokens are considered better and token counts even become goals that people need to fulfill for their performance reviews.

## Origins

Named after economist Charles Goodhart, who originally described this phenomenon in the context of monetary policy metrics. Marilyn Strathern later provided the commonly cited phrasing: “When a measure becomes a target, it ceases to be a good measure.”

This concept has been discussed extensively in education and business KPIs, and certainly applies to software engineering metrics where velocity, code coverage, and bug counts are often used as targets.

## The Cobra Effect

A related concept is the Cobra Effect, where a solution to a problem makes it worse. During British colonial rule in India, a bounty on cobras led people to breed cobras for income. When the program was cancelled, breeders released their snakes, increasing the cobra population. Similarly, poorly designed metrics can create perverse incentives that worsen the original problem.

## Further Reading

- [Goodhart's Law: How Measuring The Wrong Things Drive Immoral Behaviour Deep dive into Goodhart's Law and its implications for organizations](https://coffeeandjunk.com/goodharts-campbells-law/)
- [Goodhart's Law - Wikipedia Overview of the law's origins and applications](https://en.wikipedia.org/wiki/Goodhart%27s_law)
- [The Tyranny of Metrics Jerry Muller's book on the unintended consequences of metric fixation](https://amzn.to/4ji7rzY)
- [Enshittification - Wikipedia How platforms degrade quality once metrics replace user value as the goal](https://en.wikipedia.org/wiki/Enshittification)

## Last updated

July 20, 2026

## Related Laws

- [Dilbert Principle](https://lawsofsoftwareengineering.com/laws/dilbert-principle/)
- [Parkinson's Law](https://lawsofsoftwareengineering.com/laws/parkinsons-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/goodharts-law/
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
