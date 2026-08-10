---
title: "Inversion"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/inversion/]
description: "Inversion 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-inversion
source_url: https://lawsofsoftwareengineering.com/laws/inversion/
source_category: Decisions
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:bc5e26d47791e6ebd51677f1ca22bc6ac16cf369544c9ba6f0e825c2082b69a9
license: CC-BY-NC-ND-4.0
---

# Inversion

Solving a problem by considering the opposite outcome and working backward from it.

## Takeaways

- For any goal, also ask the inverted question. If the goal is ‘deliver the project on time,’ we should think about ‘what would make us miss the deadline?’ Making a list of those factors (scope creep, underestimating tasks, etc.) can help us achieve those goals and escape issues.
- Use techniques like pre-mortems. Our project failed, and we tried to determine what could have caused it. This critical thinking can show risks that optimistic planning overlooks.
- In design and testing, we can account for edge cases and use cases of your system. For example, how could a malicious user break this API? Inverting in this way leads to better solutions (e.g., adding validation, rate limiting, etc., once you understand how things break).

## Overview

The core idea is that specific insights become clear when you look at a problem from the opposite angle. In software engineering, instead of designing only for the best case, you deliberately design for the worst case: What if the database goes down? What if latency spikes?

By thinking of how things can fail, you add features like circuit breakers, retries, or failover strategies. Inversion pairs well with First-Principles Thinking and is a form of defensive design that leads to robust outcomes by avoiding possible problems.

## Examples

**Netflix’s Chaos Monkey** is a prime example. Usually, engineers try to keep systems running. Chaos Monkey does the opposite: it randomly terminates servers in production to test resilience. This allowed Netflix to build fault-tolerant services that survive server failures.

**Test-Driven Development (TDD)** applies inversion by writing a failing test first. You define the failure before writing code to make it pass, forcing you to think about how code could fail before implementing it.

## Origins

Inversion is explained by investor Charlie Munger’s famous quote: “All I want to know is where I’m going to die, so I’ll never go there.” Munger was inspired by 19th-century mathematician Carl Gustav Jacobi, who solved problems by inverting them and coined “Invert, always invert.”

In philosophy and Stoic practice, we also see a flavor of inversion. The Stoics had an exercise called premeditatio malorum (premeditation of evils), which means imagining in advance the worst things that could happen, just to be prepared. This is essentially inversion applied to life.

## Further Reading

- [Poor Charlie's Almanack - Charlie Munger Collection of Munger's speeches and talks on mental models including inversion](https://www.stripe.press/poor-charlies-almanack)
- [Antifragile - Nassim Nicholas Taleb Book exploring systems that gain from disorder and stress](https://en.wikipedia.org/wiki/Antifragile_%28book%29)

## Last updated

July 20, 2026

## Related Laws

- [First Principles Thinking](https://lawsofsoftwareengineering.com/laws/first-principles-thinking/)
- [Murphy's Law / Sod's Law](https://lawsofsoftwareengineering.com/laws/murphys-law/)
- [Premature Optimization (Knuth's Optimization Principle)](https://lawsofsoftwareengineering.com/laws/premature-optimization/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/inversion/
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
