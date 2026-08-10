---
title: "Law of Unintended Consequences"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/law-of-unintended-consequences/]
description: "Law of Unintended Consequences 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-law-of-unintended-consequences
source_url: https://lawsofsoftwareengineering.com/laws/law-of-unintended-consequences/
source_category: Architecture
source_experience: senior
source_updated_at: "July 10, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:c5082b877561cf3f1429ca01dce6bd222fcceca1ee484a419f4e3ccef7f23944
license: CC-BY-NC-ND-4.0
---

# Law of Unintended Consequences

Whenever you change a complex system, expect surprise.

## Takeaways

- No matter how well you plan, any significant change in a complex system can produce results you cannot anticipate.
- Consequences can be unexpected benefits (happy surprises), unexpected drawbacks (side effects that hinder), or perverse results (the action makes the original problem worse).
- In software engineering, this often manifests as a fix or new feature introducing bugs or performance issues elsewhere.

## Overview

The Law of Unintended Consequences states that outcomes are not entirely predictable. Systems have complex interdependencies and human factors that can cause surprises.

Adding a new feature might unexpectedly degrade performance due to its interaction with an unrelated module. Simplifying a UI could lead to heavier backend load because users use the feature more often than expected.

It reminds engineers that systems are complex and our mental models are incomplete. When implementing changes, anticipate that “unknown unknowns” will crop up.

## Examples

Enabling a new logging feature to help with debugging might fill the disk and crash the system, a perverse result relative to the goal of stability.

A social network changes its algorithm to boost user engagement, but as an unintended consequence, it amplifies outrage or misinformation. A bug fix in one part of the code unexpectedly causes a regression in another module that depended on the original bug behavior (overlap with Hyrum’s Law).

## Origins

Sociologist **Robert K. Merton** popularized the term in the 20th century, though the concept dates back further. In a computing context, it’s more of a borrowed concept than a specific person’s law.

Merton identified five sources of unanticipated consequences: ignorance, error, immediate interest, basic values, and self-defeating prophecy.

## Further Reading

- [Unintended consequences - Wikipedia Wikipedia article on unintended consequences](https://en.wikipedia.org/wiki/Unintended_consequences)
- [The Unanticipated Consequences of Purposive Social Action Robert K. Merton's original 1936 paper](https://www.jstor.org/stable/2084615)
- [Freakonomics Popular economics blog and book series exploring unintended consequences](https://freakonomics.com/)

## Last updated

July 10, 2026

## Related Laws

- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/law-of-unintended-consequences/
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
