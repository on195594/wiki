---
title: "First Principles Thinking"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/first-principles-thinking/]
description: "First Principles Thinking 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-first-principles-thinking
source_url: https://lawsofsoftwareengineering.com/laws/first-principles-thinking/
source_category: Decisions
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:7d0f0529801e674615df1ee8070c97c7db109ec495fbe955d670929454a628a3
license: CC-BY-NC-ND-4.0
---

# First Principles Thinking

Breaking a complex problem into its most basic blocks and then building up from there.

## Takeaways

- Do not accept the problem as it is. Break the problem down into its inherent parts and then question your assumptions: Are they really true, or are they just accepted standards? Once you grasp the underlying requirements, you may develop new solutions.
- Just because ’everyone uses Framework Y for this’ isn’t a reason you should do so. First principles thinking pushes you to ask why people do certain things the way they do.
- Rather than saying, ‘This feature will take 3 months because that’s how long similar features took,’ break the feature down. Estimate from the basics, which can sometimes show that the ‘similar’ feature had additional issues that you may not have anymore.

## Overview

First-principles thinking solves problems by questioning existing solutions rather than blindly copying them. Instead of “We’ll do X because that other project did X,” ask: “What are we really trying to accomplish? What are constraints versus assumptions?” This approach is good for incremental improvements but essential for fundamental changes.

In software design, first principles challenge how current systems work: “If we started from scratch today, how would we build this?” This thinking led to microservices (questioning the monolith) and serverless computing (questioning server management). The drawback is that it is mentally intensive and not always necessary. Many problems are well-solved by known patterns.

## Examples

Before SpaceX, launching rockets was costly because industry practice used expensive materials and discarded rockets after one use. Elon Musk applied first-principles thinking: What is a rocket made of? Mainly aluminum, titanium, copper, and carbon fiber. Raw material costs were a fraction of finished rocket prices. From that insight, SpaceX decided to build rockets from scratch and make them reusable.

In software, consider a company paying licensing fees for a proprietary analytics platform. An engineer challenged this by examining what the platform actually does: ingest data, run statistical computations, generate reports. These could be implemented using open-source software and custom programming. A proof-of-concept in Python showed 90% of the solution at a fraction of the cost.

## Origins

The term “first principles” has roots in classical philosophy. Aristotle referred to first principles as foundational propositions that cannot be deduced from anything else, the bedrock of knowledge. René Descartes emphasized starting from fundamental truths (“I think, therefore I am”).

In modern times, first-principles thinking gained fame through Elon Musk, who credits it for SpaceX and Tesla innovations. Instead of thinking “rockets are expensive,” he broke down raw material costs and realized building in-house was viable.

## Further Reading

- [First Principles: The Building Blocks of True Knowledge Farnam Street's comprehensive guide to first principles thinking](https://fs.blog/first-principles/)
- [Posterior Analytics - Aristotle Stanford Encyclopedia of Philosophy on Aristotle's foundational logic](https://plato.stanford.edu/entries/aristotle-logic/)
- [How to Solve It - George Pólya Classic book on mathematical problem-solving and heuristics](https://amzn.to/4b9q3Qo)

## Last updated

July 20, 2026

## Related Laws

- [Occam's Razor](https://lawsofsoftwareengineering.com/laws/occams-razor/)
- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/first-principles-thinking/
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
