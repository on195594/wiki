---
title: "Tesler's Law (Conservation of Complexity)"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/teslers-law/]
description: "Tesler's Law (Conservation of Complexity) 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-teslers-law
source_url: https://lawsofsoftwareengineering.com/laws/teslers-law/
source_category: Architecture
source_experience: senior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:b28b5b26f71fdce983de5e74e914c2c10de438299f4371d77778b51c944cee15
license: CC-BY-NC-ND-4.0
---

# Tesler's Law (Conservation of Complexity)

Every application has an inherent amount of irreducible complexity that can only be shifted, not eliminated.

## Takeaways

- Good design often requires that developers absorb most of the complexity (through smart defaults, algorithms, etc.) so that the user’s interaction is simpler.
- If your UI requires the user to manage many settings or steps, you’ve conserved complexity in the wrong place (on the user side). Often, it’s better to design the product to manage that complexity internally.
- Good design often hides complexity without eliminating it by handling it internally.

## Overview

Tesler’s Law, also known as the Law of Conservation of Complexity, states that for any system, there is a certain amount of complexity that cannot be removed; it’s inherent to the problem. The key is **who deals with it**.

If you design software that’s very simple for the user, it likely means the software is doing a lot of complex work under the hood. If you make the software very simple internally, it might dump complexity on the user (e.g., requiring many manual steps).

Tesler’s Law encourages designers to **move complexity away from the user experience** whenever possible.

## Examples

A classic example is **scheduling meetings**, which is inherently complex (finding a common time). A tool like Calendly hides that complexity from the user (the software handles it), whereas an email chain to schedule a meeting places that complexity on the user to figure out.

In system architecture, imagine designing a database vs. putting logic in application code. Sometimes pushing logic into the DB (such as stored procedures) can simplify app code but add complexity to the DB layer, or vice versa. Complexity isn’t gone, just relocated.

In the end, the law reminds us that no design is without complexity. It’s all about smartly allocating complexity to the right place.

## Origins

**Larry Tesler**, who worked on Apple Lisa and early GUI concepts, formulated this principle in the 1980s. He observed that you can’t make everything simple without someone handling complexity. It’s a fundamental trade-off in design.

## Further Reading

- [Why Life Can't Be Simpler Farnam Street on the conservation of complexity](https://fs.blog/why-life-cant-be-simpler/)
- [Law of Conservation of Complexity Deep dive into Tesler's Law and its implications](https://humanist.co/blog/law-of-conservation-of-complexity/)
- [Simplicity is Overrated Why chasing simplicity isn't always the answer](https://marvelapp.com/blog/simplicity-is-overrated/)
- [Law of Conservation of Complexity (Wikipedia) Wikipedia article on Tesler's Law](https://en.wikipedia.org/wiki/Law_of_conservation_of_complexity)

## Last updated

June 24, 2026

## Related Laws

- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [Occam's Razor](https://lawsofsoftwareengineering.com/laws/occams-razor/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/teslers-law/
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
