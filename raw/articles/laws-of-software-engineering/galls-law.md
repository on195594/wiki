---
title: "Gall's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/galls-law/]
description: "Gall's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-galls-law
source_url: https://lawsofsoftwareengineering.com/laws/galls-law/
source_category: Architecture
source_experience: senior
source_updated_at: "July 10, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:406df8c5faa27a1615a80bce2d996cabc49f50f94bcec3ee0e71157370d2c2fe
license: CC-BY-NC-ND-4.0
---

# Gall's Law

A complex system that works is invariably found to have evolved from a simple system that worked.

## Takeaways

- Don’t build a complex system from scratch. Instead, make a simple version that works, then iterate and add complexity. This approach serves as a launching pad for experimentation and innovation.
- Successful large systems often grow organically. A fully designed-from-scratch complex system usually fails because you can’t foresee all interactions.
- This law argues for creating a Minimum Viable Product (MVP), a simple working core, and then growing it, rather than a big-bang approach.
- Systems that grow tend to adapt and handle complexity better because they’ve been tested and refined at each stage. An overly complex initial design can break when something unexpected happens.

## Overview

John Gall observed that **successful complex systems start as successful simple systems**. If you attempt to create a complex system from the beginning, it usually doesn’t work because there are too many unknowns you haven’t validated.

Instead, start with a simple architecture and learn from real-world usage. Add features or complexity incrementally, ensuring each change still works. When you start with a small, functional core, you can validate assumptions early. Every new capability added incrementally is tested against reality, forcing the system to adapt.

## Examples

**Facebook** started as a simple website for Harvard students. It was essentially a basic user profile system that worked at that small scale, then expanded gradually, adding features and handling more users. If Mark Zuckerberg had tried to build today’s Facebook from scratch in 2004, it would almost certainly have collapsed under its own complexity.

In the era of microservices, a common piece of advice influenced by Gall’s Law is: don’t start with microservices. Start with a monolith (a simpler architecture) that works. As it grows, identify pieces to split off into separate services. Those pieces have the benefit of prior existence, you know their requirements from the monolith, and thus are more likely to work once isolated.

## Origins

**John Gall**, an American pediatrician with a sideline in systems theory, published *Systemantics: How Systems Work and Especially How They Fail* in 1975. 30 publishers initially rejected the book before it became a cult classic.

The third edition (2002) of the book is named *The Systems Bible*.

## Further Reading

- [The Systems Bible John Gall](https://amzn.to/4svZT0K)
- [The Mythical Man-Month Fred Brooks](https://amzn.to/4b4GU72)
- [Monolith First Martin Fowler](https://martinfowler.com/bliki/MonolithFirst.html)
- [Thinking in Systems Donella Meadows' primer on systems thinking and complexity](https://amzn.to/4qgVSvH)

## Last updated

July 10, 2026

## Related Laws

- [Conway's Law](https://lawsofsoftwareengineering.com/laws/conways-law/)
- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [The Law of Leaky Abstractions](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
- [Hofstadter's Law](https://lawsofsoftwareengineering.com/laws/hofstadters-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/galls-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-architecture]]
- indexed_by: [[software-engineering-laws-decision-map]]
