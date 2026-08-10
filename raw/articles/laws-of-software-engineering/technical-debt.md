---
title: "Technical Debt"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/technical-debt/]
description: "Technical Debt 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-technical-debt
source_url: https://lawsofsoftwareengineering.com/laws/technical-debt/
source_category: Quality
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:53551ad49f119e48c56bd839663021ce3ea5f3ce82b1a90f011f1a2307acf1ee
license: CC-BY-NC-ND-4.0
---

# Technical Debt

Technical Debt is everything that slows us down when developing software.

## Takeaways

- When we take a shortcut in code, we borrow time from the future. This gives an immediate benefit, but you owe principal (the work to fix) plus interest.
- If technical debt is not repaid, it accrues interest. Each minute spent on dirty code, bugs, and workarounds due to a lack of refactoring is interest on the debt.
- Not all technical debt is inherently bad. It is sometimes necessary, for instance, for market timing or prototyping.
- The way to pay down technical debt is to refactor code, add missing tests, and improve design.

## Overview

Technical debt highlights a fundamental tension in software engineering: speed vs. quality. The term helps explain to both developers and non-technical stakeholders why seemingly “done” software still needs ongoing work. When you write clumsy code or postpone cleanup, you’ve essentially taken out a loan: you get short-term feature delivery, but the complexity you introduce is the interest you’ll keep paying.

Properly managing technical debt means being conscious of when you’re adding a quick workaround or a “temporary” hack, and having a plan to revisit it. Teams often use tools to log technical debt items (like comments, issue tracker tickets, or dedicated debt backlogs).

When managed, technical debt can be an effective tool; you intentionally take on a bit of messiness to get feedback or meet a deadline, then clean it up. But if ignored, debt becomes a problem.

## Examples

A typical example is skipping automated tests. A team under deadline pressure releases a new feature without writing tests. The release is successful (debt incurred). But later, making changes becomes harder since every change risks unforeseen bugs because there’s no safety net of tests (interest payments). Eventually they must stop adding features and fix the debt by adding the missing tests and refactoring.

Another example is a startup that wants to deliver a quick prototyping effort to onboard the first customer. Developers do rapid but messy coding, with hardcoded variables and copy-and-paste code. This approach is made with technical debt in mind. The endeavor helps the startup win a customer; however, the startup’s codebase is now full of technical debt.

If they just continue to add to it, they will face bugs and slower performance due to the messy code (interest on debt). They realize this and therefore set up a “rehab” sprint to refactor the code, thereby resolving the most troublesome bits.

## Origins

The term “Technical Debt” was coined by Ward Cunningham (one of the authors of the Agile Manifesto) at the OOPSLA conference in 1992. He first used the financial metaphor while working on a finance application to explain to his boss why the team needed time to refactor code.

Ward compared developing software to borrowing money: it can be wise to take shortcuts (borrow) to achieve something sooner, provided you pay back the loan by cleaning up the code later.

## Further Reading

- [Debt Metaphor - Ward Cunningham Ward Cunningham's video explaining the original debt metaphor (OOPSLA 1992)](https://www.youtube.com/watch?v=pqeJFYwnkjE)
- [Technical Debt - Martin Fowler Martin Fowler's comprehensive blog post on technical debt](https://martinfowler.com/bliki/TechnicalDebt.html)
- [Technical Debt - Wikipedia Overview of the concept and its management strategies](https://en.wikipedia.org/wiki/Technical_debt)
- [Accelerate Forsgren, Humble, and Kim's research on how technical debt impacts software delivery](https://amzn.to/48Xugp3)

## Last updated

July 20, 2026

## Related Laws

- [Broken Windows Theory](https://lawsofsoftwareengineering.com/laws/broken-windows-theory/)
- [Hofstadter's Law](https://lawsofsoftwareengineering.com/laws/hofstadters-law/)
- [The Boy Scout Rule](https://lawsofsoftwareengineering.com/laws/boy-scout-rule/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/technical-debt/
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
