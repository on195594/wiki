---
title: "DRY (Don't Repeat Yourself)"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/dry-principle/]
description: "DRY (Don't Repeat Yourself) 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-dry-principle
source_url: https://lawsofsoftwareengineering.com/laws/dry-principle/
source_category: Design
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:531ca066d742602d88058eccb72711b0c65271661c28fe58f4e9973b72b20186
license: CC-BY-NC-ND-4.0
---

# DRY (Don't Repeat Yourself)

Every piece of knowledge must have a single, unambiguous, authoritative representation.

## Takeaways

- The DRY principle is about avoiding duplication of knowledge in code. If the same idea or logic is in multiple places, it’s a signal to refactor.
- When requirements change, you should update logic in only one place. Repeated code increases the risk of inconsistencies and bugs (you might fix a bug in one copy and forget about the others).
- Be careful to apply DRY wisely. It’s about knowledge repetition, not just duplication. Sometimes two pieces of code look alike but do different jobs; merging them could over-complicate things.

## Overview

The idea of DRY is simple: each fact or piece of logic in your system should be expressed once and only once. If you find the same code, formula, or rule in multiple modules, you’re violating DRY. Such repetition creates hidden maintenance cost. When the business rule changes, you must hunt down every duplicate instance.

By following DRY, developers strive for a single, unique implementation of any given behavior. This often means abstracting common code into a function or class, or consolidating configuration into a single file.

DRY also applies to database schemas, tests, and documentation.

However, remember that DRY is about duplicated intent, not just similar-looking code. Two pieces of code can look identical but serve different purposes in an application.

## Examples

An application has a database connection URL in five different source files. If the database host changes, you’d have to edit all five places. The DRY approach keeps that URL in a single configuration variable that all modules read.

If two parts of an app both format dates the same way, create a single `formatDate()` utility function and call it from both places. Now if the date format needs to change, there’s precisely one function to modify.

Large codebases benefit from DRY through shared libraries. If multiple applications need the same security logic, create a shared library instead of copying code across applications.

## Origins

The term “DRY” was coined in 1999 by Andy Hunt and Dave Thomas in their book The Pragmatic Programmer. They defined it as: “Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.”

Even earlier, avoiding code duplication was part of structured programming and the Unix philosophy. In Extreme Programming, a similar idea was known as “Once and Only Once.” Hunt and Thomas gave it a catchy name and expanded its scope beyond just code to all information.

## Further Reading

- [The Pragmatic Programmer, 20th Anniversary Edition The original source of the DRY principle by Hunt and Thomas](https://amzn.to/4piJutH)
- [DRY - Wikipedia Overview of the principle and related concepts](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)
- [Code Complete Steve McConnell's guide covering code duplication and abstraction](https://amzn.to/3N57T8t)

## Last updated

July 20, 2026

## Related Laws

- [SOLID Principles](https://lawsofsoftwareengineering.com/laws/solid-principles/)
- [Law of Demeter](https://lawsofsoftwareengineering.com/laws/law-of-demeter/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/dry-principle/
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
