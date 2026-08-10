---
title: "YAGNI (You Aren't Gonna Need It)"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/yagni/]
description: "YAGNI (You Aren't Gonna Need It) 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-yagni
source_url: https://lawsofsoftwareengineering.com/laws/yagni/
source_category: Design
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:158f18a000384a07b17bd65cbd66fe1059bcd0798d2d3a0421881052356a0e22
license: CC-BY-NC-ND-4.0
---

# YAGNI (You Aren't Gonna Need It)

Don't add functionality until it is necessary.

## Takeaways

- YAGNI is here to remind developers to focus on current tasks rather than implementing features that aren’t needed now.
- Anticipating future needs often leads to over-engineering, and this adds complexity and maintenance issues.
- YAGNI encourages iterative development. You implement minimal solutions and refine or extend them when needed.

## Overview

YAGNI captures a core philosophy of agile development: don’t write code for features that haven’t been requested or aren’t immediately needed.

If you’re implementing Module A and think “in the future we might need Module B to do X, so I’ll code some hooks for that now,” YAGNI advises against it because that future feature may never come or may change drastically.

This principle directly fights over-engineering. To apply YAGNI successfully, teams rely on confidence in refactoring. You defer a feature only if you trust you can add it later at low cost.

Agile methods provide that safety net via good test coverage, refactoring tools, and continuous integration. YAGNI pushes the problem of complexity to when it’s actually needed.

## Examples

You’re building a feature with specific behavior. You think “maybe in the future someone will want to toggle this on/off, so I’ll add a configuration flag now.” YAGNI challenges that. Unless there’s a current requirement for configurability, implement only expected behavior, nothing more.

You’re working on a library function that currently does one thing. You realize it might be useful more generally, so you might add parameters or abstraction tiers. YAGNI says implement it for the original task.

Your app needs JSON export? Implement simple JSON, not a full serialization library supporting XML, YAML, etc.

Teams that adopt YAGNI are often comfortable refactoring because they trust that when the feature set grows, they’ll have more information about real use cases, leading to better abstractions.

## Origins

YAGNI was part of the Extreme Programming (XP) paradigm in the late 1990s. It was promoted by Ron Jeffries, one of XP’s founders, who wrote: “Always implement things when you actually need them, not when you just foresee that you need them.”

The slogan was adopted in XP literature, such as Extreme Programming Installed (2001).

## Further Reading

- [YAGNI on Martin Fowler's website Clear explanation with practical examples](https://martinfowler.com/bliki/Yagni.html)
- [Extreme Programming Installed Ron Jeffries, Ann Anderson, Chet Hendrickson](https://amzn.to/4siycbq)
- [You Aren't Gonna Need It on C2 Wiki Original XP community discussion](http://wiki.c2.com/?YouArentGonnaNeedIt)

## Last updated

July 20, 2026

## Related Laws

- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
- [DRY (Don't Repeat Yourself)](https://lawsofsoftwareengineering.com/laws/dry-principle/)
- [Premature Optimization (Knuth's Optimization Principle)](https://lawsofsoftwareengineering.com/laws/premature-optimization/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/yagni/
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
