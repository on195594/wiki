---
title: "Occam's Razor"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/occams-razor/]
description: "Occam's Razor 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-occams-razor
source_url: https://lawsofsoftwareengineering.com/laws/occams-razor/
source_category: Decisions
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:96c77d7b924ca6b7a3e979e7557808634343c66d549cabe45a70a748b182eb54
license: CC-BY-NC-ND-4.0
---

# Occam's Razor

The simplest explanation is often the most accurate one.

## Takeaways

- Simple code is easier to understand, maintain, and debug, whereas complex code has more potential points of failure. Remove or avoid unnecessary moving parts in system architecture.
- When debugging, start with the simplest explanation before jumping into complex theories.
- Adding more features to the app can only complicate a product without adding real value. Occam’s Razor reminds us that less is more in many cases.

## Overview

Occam’s Razor is a problem-solving principle that reminds us that when we have multiple possible solutions, the simplest one is preferred.

In software, this principle supports the KISS (“Keep It Simple, Stupid”) approach. When we decide to keep our implementations simple, we reduce the risk of further complications.

For example, if a software architecture can achieve its goals with a monolith and one database, there is no need to split it into five microservices and two databases. These extra components would only introduce complexity and potential integration and coordination issues, but no benefits.

This is a reminder to avoid the temptation of over-engineering and keep things simple.

## Examples

A classic example of applying Occam’s Razor while debugging is that of the broken build. Let’s assume that your build system has failed. A complex thinker might think that there is some subtle regression in the compiler code, or maybe some dependency is damaged. An Occam’s Razor thinker would start with simpler explanations: a typo, a missing semicolon, or a misconfiguration.

A saying often attributed to Einstein goes, “Everything should be made as simple as possible, but not simpler,” which best applies to this law in engineering.

## Origins

Occam’s Razor dates back to William of Ockham, a philosopher from 14th-century England. His original version in Latin, “Pluralitas non est ponenda sine necessitate,” can be translated to “plurality should not be posited without necessity,” or “Don’t multiply entities or assumptions beyond what’s required.”

Over time, Occam’s Razor has evolved as a cornerstone of scientific methodology and logical reasoning.

## Further Reading

- [Ockham's Razors: A User's Manual Elliott Sober's comprehensive analysis of parsimony in science](https://amzn.to/4jfnRZX)
- [Inference to the Best Explanation Peter Lipton's exploration of explanatory reasoning and simplicity](https://www.routledge.com/Inference-to-the-Best-Explanation/Lipton/p/book/9780415242028)
- [Simplicity (Stanford Encyclopedia of Philosophy) In-depth philosophical analysis of Occam's Razor and parsimony principles](https://plato.stanford.edu/entries/simplicity/)
- [No Silver Bullet Fred Brooks on accidental vs essential complexity in software](https://en.wikipedia.org/wiki/No_Silver_Bullet)

## Last updated

July 20, 2026

## Related Laws

- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
- [YAGNI (You Aren't Gonna Need It)](https://lawsofsoftwareengineering.com/laws/yagni/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/occams-razor/
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
