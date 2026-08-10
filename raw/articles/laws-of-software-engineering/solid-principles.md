---
title: "SOLID Principles"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/solid-principles/]
description: "SOLID Principles 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-solid-principles
source_url: https://lawsofsoftwareengineering.com/laws/solid-principles/
source_category: Design
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:aea44cb60954a577fead62ebe245e687c5a91e94e03d87481a96c036c9ad4f0e
license: CC-BY-NC-ND-4.0
---

# SOLID Principles

Five main guidelines that enhance software design, making code more maintainable and scalable.

## Takeaways

- Following SOLID leads to software that is easier to extend, test, and refactor without breaking existing functionality. Each principle addresses a different aspect of good OO design.
- A class with a single responsibility (SRP) that depends on well-defined interfaces (ISP, DIP) and uses inheritance appropriately (LSP) and polymorphism for extensions (OCP) will likely be easy to maintain.
- Changes to one part of the system won’t cascade into breakages elsewhere, because the code is loosely coupled and well-encapsulated.
- SOLID does not guarantee a perfect design, but it provides proven guidelines for object-oriented programming.

## Overview

The SOLID principles are five high-level guidelines for object-oriented design: **Single Responsibility** (one concern per class), **Open/Closed** (open for extension, closed for modification), **Liskov Substitution** (subclasses must be substitutable for their parent), **Interface Segregation** (no forced dependency on unused interfaces), and **Dependency Inversion** (depend on abstractions, not concretions).

When applied together, these principles produce systems that are modular, extensible, and robust under change. Code becomes easier to test, refactor, and extend without breaking existing functionality.

## Examples

For the **Single Responsibility Principle**, consider a web application managing user accounts. An anti-SRP design might have a single `UserManager` class handling validation, database operations, sending emails, and logging. A better design separates these into `UserValidator`, `UserRepository`, `EmailService`, and a `UserRegistrationService` that orchestrates them. Each class has one focus, and if the email format changes, you only touch `EmailService`.

For the **Dependency Inversion Principle**, imagine a `NotificationService` that sends alerts. Without DIP, it directly uses `EmailSender` or `SMSSender`. With DIP, you define an `INotificationChannel` interface, and all senders implement it. The service depends only on the abstraction, making it easy to add new channels or swap in test doubles.

## Origins

The five SOLID principles emerged over the years and were collected and popularized by Robert C. Martin (Uncle Bob). The acronym SOLID was coined around 2004 by Michael Feathers, who noticed the initial letters spelled out a catchy word.

Uncle Bob described SRP, OCP, LSP, ISP, and DIP in various articles from the late 1990s and early 2000s, including his “Principles of Object-Oriented Design” papers and his 2002 book Agile Software Development: Principles, Patterns, and Practices. These principles drew from earlier thinkers: OCP from Bertrand Meyer (1988), LSP from Barbara Liskov (1987), ISP from work at Xerox PARC, and DIP and SRP were Martin’s formulations inspired by layering and cohesion practices.

## When SOLID goes too far

It’s possible to overapply the SOLID principles. Sometimes, too many small interfaces or too many abstract layers are overkill for a problem and create complexity, the so-called “AbstractFactoryFactory” problem.

When used correctly, though, these principles are genuinely helpful in managing object-oriented system complexity, which is why they’ve become so popular to teach.

## Further Reading

- [Design Principles and Design Patterns Robert C. Martin's foundational paper on OO design principles](https://web.archive.org/web/20150906155800/http://www.objectmentor.com/resources/articles/Principles_and_Patterns.pdf)
- [Agile Software Development: Principles, Patterns, and Practices Uncle Bob's comprehensive book introducing SOLID principles](https://amzn.to/497oH7H)
- [Clean Architecture Robert C. Martin's guide to software architecture and design](https://amzn.to/4jeeN7k)
- [SOLID - Wikipedia Overview of all five principles with examples](https://en.wikipedia.org/wiki/SOLID)
- [Design Patterns: Elements of Reusable Object-Oriented Software The Gang of Four's classic on OO patterns that complement SOLID](https://amzn.to/3LnM5o6)

## Last updated

July 20, 2026

## Related Laws

- [Law of Demeter](https://lawsofsoftwareengineering.com/laws/law-of-demeter/)
- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [The Law of Leaky Abstractions](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
- [DRY (Don't Repeat Yourself)](https://lawsofsoftwareengineering.com/laws/dry-principle/)
- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
- [YAGNI (You Aren't Gonna Need It)](https://lawsofsoftwareengineering.com/laws/yagni/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/solid-principles/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-design]]
- indexed_by: [[software-engineering-laws-decision-map]]
