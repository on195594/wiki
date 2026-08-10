---
title: "Linus's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/linuss-law/]
description: "Linus's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-linuss-law
source_url: https://lawsofsoftwareengineering.com/laws/linuss-law/
source_category: Quality
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:f64981652ff1d115e8f71db8948e19229ce29c3a6aa707614b60a4469659d057
license: CC-BY-NC-ND-4.0
---

# Linus's Law

Given enough eyeballs, all bugs are shallow.

## Takeaways

- Linus’s Law highlights the strength of peer review and community in software development. If a codebase is accessible to many developers, someone will eventually have the expertise to identify and fix a given bug.
- The rule is often cited as a key advantage of open-source software. When source code is widely available, you accumulate a large pool of contributors.
- Linus’s Law assumes those eyeballs are indeed looking, i.e., an active community. Simply being open-source doesn’t magically fix bugs.

## Overview

Linux’s open development model, releasing code early and often to the public, results in rapid bug-finding. When many people use and review a piece of software, problems become apparent to someone.

What is a perplexing bug to you might be trivial to another programmer who spots it. Or among thousands of users, one will stumble on the exact reproduction steps, and another might submit a fix.

This law shows the core of open-source: that transparency and collaboration lead to more robust, reliable software.

However, it’s not absolute. Coordination and quality control are still needed. But as a guiding principle, Linus’s Law captures the self-correcting nature of a large developer ecosystem.

The “many eyeballs” principle is also why internal code reviews and pair programming can be effective.

## Examples

Consider the Apache HTTP Server, an open-source web server used by millions. Because its code is open and it has a vast user base, many developers have at some point debugged or improved it. If there’s a security flaw or bug, odds are high that someone in the global community will discover it and report it. The infamous “Log4Shell” vulnerability in the Log4j library was identified and patched by the community.

In contrast, consider an enterprise software product that is proprietary with only a few clients. If a subtle bug appears, only the vendor’s small team and a few client implementers are likely to notice it. It might take a long time to surface and debug because of limited “eyeballs.”

## Origins

The law is named after Linus Torvalds, the creator of Linux, but Eric S. Raymond formulated it in the late 1990s. In “The Cathedral and the Bazaar”, Raymond writes: “Given enough eyeballs, all bugs are shallow” and calls this Linus’s Law in honor of Torvalds’ open development approach.

The idea was inspired by the Linux community, where hundreds of developers worldwide were debugging the kernel simultaneously. The essay was first presented in 1997 and published as a book in 1999.

## The Heartbleed Counterexample

Although Linus’s Law is correct, it was shown to be imperfect in 2014 when the Heartbleed bug was discovered in OpenSSL. In this instance, because OpenSSL is open source, it had been overlooked for two years. In this scenario, having many eyeballs was ineffective because no one was watching.

## Further Reading

- [The Cathedral and the Bazaar Eric S. Raymond's influential essay on open-source development](https://amzn.to/49cYD9Y)
- [Linus's Law - Wikipedia Overview of the law and its implications](https://en.wikipedia.org/wiki/Linus%27s_law)
- [With Enough Eyeballs, All Bugs Are Shallow - TechCrunch Analysis of the law in context of real-world vulnerabilities](https://techcrunch.com/2012/02/23/with-many-eyeballs-all-bugs-are-shallow/)
- [Revisiting Linus's Law: Benefits and Challenges of OSS Peer Review Academic study on the impacts of member differences on open source peer review](https://www.sciencedirect.com/science/article/abs/pii/S1071581915000087)
- [An Empirical Study of Build Maintenance Effort - IEEE IEEE study examining software maintenance and the many-eyes hypothesis](https://www.computer.org/csdl/magazine/mi/2012/01/mmi2012010072/13rRUzphDuy)
- [Timeline of the xz open source attack Russ Cox's detailed timeline of the xz backdoor, a striking counterexample to many-eyes review](https://research.swtch.com/xz-timeline)

## Last updated

July 20, 2026

## Related Laws

- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Sturgeon's Law](https://lawsofsoftwareengineering.com/laws/sturgeons-law/)
- [Bus Factor](https://lawsofsoftwareengineering.com/laws/bus-factor/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/linuss-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-quality]]
- indexed_by: [[software-engineering-laws-decision-map]]
