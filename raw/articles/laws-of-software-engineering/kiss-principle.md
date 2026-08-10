---
title: "KISS (Keep It Simple, Stupid)"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/kiss-principle/]
description: "KISS (Keep It Simple, Stupid) 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-kiss-principle
source_url: https://lawsofsoftwareengineering.com/laws/kiss-principle/
source_category: Design
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:1e344a7ea85a3e5e6fab3a6e29a7c6b29f20dbee72d8473329e7e563d92503e9
license: CC-BY-NC-ND-4.0
---

# KISS (Keep It Simple, Stupid)

Designs and systems should be as simple as possible.

## Takeaways

- KISS primarily refers to avoiding complexity in solution designs. A solution that satisfies the requirement and is simple in design is better than a complex one.
- Simple code is easier and faster to understand and debug. It’s even easier to understand and fix if you’re your own future self. Smarter code may look impressive at first, but it often masks problems.
- The code solution should be as simple as possible. Anything that adds complexity unnecessarily is counter to the KISS Principle.

## Overview

The KISS principle is a reminder that simplicity should be a key goal. If you can solve a problem with a 50-line script versus a complex 500-line solution, KISS favors the 50-line solution because each line of code has the potential to cause an error.

Why is simplicity so important? Software has to be understood by humans. A simple design is much easier to maintain: new team members can get up to speed faster, bugs are easier to localize, and modifications cause fewer ripple effects.

The KISS principle encourages developers to resist “clever” code that does too much at once, and to avoid architecting solutions that address future problems at the cost of current complexity.

## Examples

A web application needs to generate reports. A KISS approach would use a simple script or existing library to query the database and output a CSV. A non-KISS approach would design a complete plug-in architecture “just in case” you need it more generically later. If requirements are small, the latter is overkill.

When writing a function to parse a file, a KISS implementation uses simple logic: open the file, read line by line, split fields, handle errors. A complex approach might implement a fully generic parser-combinator framework. Unless you truly need that generality, the simpler approach will be easier to get right and maintain.

Many experienced engineers advise: “First make it work, then make it right, then make it fast (if needed).”

## Origins

The phrase “Keep It Simple, Stupid” came from the U.S. military. It’s attributed to Kelly Johnson, a lead engineer at Lockheed’s Skunk Works in the 1960s. Johnson challenged his team: design an aircraft that could be repaired with basic tools by an average mechanic in the field.

Influential programmers such as Edsger Dijkstra and C.A.R. Hoare often discussed complexity. Hoare said, “There are two ways of constructing a software design: One way is to make it so simple that there are obviously no deficiencies, and the other way is to make it so complicated that there are no obvious deficiencies. The first method is far more difficult.”

The KISS principle has since become a cornerstone of software engineering best practices.

## Further Reading

- [A Philosophy of Software Design John Ousterhout's book on managing complexity in software](https://amzn.to/3N1uR0f)
- [KISS Principle - Wikipedia Overview of the principle and its origins](https://en.wikipedia.org/wiki/KISS_principle)
- [Code Complete Steve McConnell's practical handbook emphasizing simplicity in code](https://amzn.to/3N57T8t)

## Last updated

July 20, 2026

## Related Laws

- [YAGNI (You Aren't Gonna Need It)](https://lawsofsoftwareengineering.com/laws/yagni/)
- [Principle of Least Astonishment](https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/kiss-principle/
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
