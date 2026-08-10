---
title: "The Law of Leaky Abstractions"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/]
description: "The Law of Leaky Abstractions 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-law-of-leaky-abstractions
source_url: https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/
source_category: Architecture
source_experience: mid
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:41d63d10b3c6c1dcf5d93de00aaf4b8f1c5b9f27fb42e60f9f11026795d35c68
license: CC-BY-NC-ND-4.0
---

# The Law of Leaky Abstractions

All non-trivial abstractions, to some degree, are leaky.

## Takeaways

- No matter how well-designed, abstractions (libraries, frameworks, etc.) have edge cases that depend on internal details.
- Developers should understand that using a high-level tool doesn’t absolve them from knowing what’s happening underneath, at least at a basic level.
- “Leaky” means you might encounter performance issues, bugs, or behavior that force you to consider the underlying system (e.g., networking, OS) on which the abstraction sits.
- When creating abstractions, strive to minimize leakage and document the cases in which it might break.

## Overview

This law observes that in complex systems, the abstractions we create, meant to hide complexity, *inevitably fail in some scenarios*, revealing the underlying complexity to the programmer.

For example, consider an ORM (object-relational mapper) that lets you treat database entries as objects. Most of the time it works, but occasionally you hit a case where performance is terrible and you have to think about the SQL queries being generated. The abstraction “leaks” details of the database.

The law isn’t saying abstractions are bad. They are essential. But it reminds us that **one must be prepared for when they break**.

## Examples

A good example is **memory management in high-level languages**. Languages like Java and Python abstract away manual memory allocation thanks to garbage collection. Yet leaks still happen (objects not being freed due to lingering references), or you encounter the abstraction’s limits (such as GC pauses affecting performance). Suddenly, the developer needs to know how garbage collection works internally, and the abstraction of “infinite memory” has leaked.

Web developers often treat an HTTP request as something fast, abstracting away the network. However, when latency spikes or packets drop, the network’s reality leaks into your application.

## Origins

Joel Spolsky introduced this law in a 2002 blog post. He gave examples such as TCP (which abstracts reliable connections over IP, but on a bad network the abstraction leaks, causing timeouts) or the virtual memory abstraction.

The concept resonates with many earlier thoughts in computing, essentially a restatement of “there’s no free lunch” with abstractions.

## All Models Are Wrong (George Box's Law)

George Box said, “*All models are wrong, but some are useful.*” Every abstraction you build, whether a class hierarchy, an API contract, or a data model, is a lie. It’s basically **a simplified version of reality that ignores inconvenient details**. The question isn’t whether your model is wrong. It’s whether it’s wrong in ways that matter.

Your database schema assumes users have one email address, until they don’t. Your payment model treats refunds like reversed payments, until chargebacks arrive. Accept that every model will leak, and design for the leak, not against it.

## Further Reading

- [The Law of Leaky Abstractions Joel Spolsky's original blog post](https://www.joelonsoftware.com/2002/11/11/the-law-of-leaky-abstractions/)
- [A Note on Distributed Computing Fallacies of Distributed Systems](https://scholar.harvard.edu/waldo/publications/note-distributed-computing)
- [Towards a New Model of Abstraction in Software Engineering Gregor Kiczales' foundational paper on open implementations and abstraction leakage](https://web.archive.org/web/20110604013045/http://www2.parc.com/csl/groups/sda/publications/papers/Kiczales-IMSA92/for-web.pdf)

## Last updated

June 24, 2026

## Related Laws

- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/
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
