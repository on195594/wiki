---
title: "Brooks's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/brooks-law/]
description: "Brooks's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-brooks-law
source_url: https://lawsofsoftwareengineering.com/laws/brooks-law/
source_category: Teams
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:d2e843938a22185874e6abbbeae31aacd84f71887a80e0dfc8464bf2d54c2391
license: CC-BY-NC-ND-4.0
---

# Brooks's Law

Adding manpower to a late software project makes it later.

## Takeaways

- Simply throwing more developers at a project that’s running behind schedule usually slows it down further initially.
- New people take time to get up to speed, consuming existing team members’ time for training and coordination, which reduces overall productivity.
- Instead of hoping manpower will solve slippage, adjust the scope or timeline. Be wary of ‘just hire more coders’ as a solution to lateness.

## Overview

Brooks’s Law challenges the belief that a software development effort is perfectly divisible among people. In reality, adding a person to a project incurs training costs and increases the number of communication paths. This can outweigh that person’s contribution for a while.

If a project is already late, adding new developers can cause further delays as they learn the system and may introduce new bugs. Brooks illustrated this with the observation that “the bearing of a child takes nine months, no matter how many women are assigned.” The law doesn’t say adding people never helps, but as a response to lateness, it’s usually counterproductive.

## Examples

A project is one month behind schedule, so management adds 3 new developers to a 5-person team. Over the next few weeks, progress slows. The original developers spend much of their time explaining the design and code to newcomers, and merging their work causes integration headaches. The project slips further, now two months late.

A complex bug required deep knowledge of the system. Adding more people didn’t help because only the original dev understood it, and more debuggers only made things worse. Scaling a software team isn’t linear. After a point, more members yield less and less output per person.

## Origins

**Frederick P. Brooks Jr.**, who managed the IBM OS/360 project, formulated this law based on painful experience. His book *The Mythical Man-Month* (1975) explores why software projects fail and where management assumptions break down.

The book famously challenged the notion that “man-months” are interchangeable. Brooks demonstrated through real-world examples why the assumption that 12 programmers can do in one month what one programmer does in 12 months fails in software development.

## Little's Law Makes Brooks's Law Measurable

Little’s Law (L = λ × W) connects work in progress, throughput, and lead time. If your team completes 5 tasks per week with 20 in progress, average lead time is 4 weeks. Push WIP to 40 with the same throughput, and lead time doubles.

When you add people to a late project, WIP grows but throughput stays flat. Little’s Law shows the result: longer lead times, not shorter ones. If you want faster delivery, reduce WIP before adding people.

## Further Reading

- [The Mythical Man-Month Fred Brooks's classic book on software engineering](https://amzn.to/4peJbjC)
- [Brooks's Law - Wikipedia Wikipedia article on Brooks's Law](https://en.wikipedia.org/wiki/Brooks%27s_law)
- [No Silver Bullet Fred Brooks's essay on essential vs accidental complexity](https://en.wikipedia.org/wiki/No_Silver_Bullet)

## Last updated

July 20, 2026

## Related Laws

- [Conway's Law](https://lawsofsoftwareengineering.com/laws/conways-law/)
- [Second-System Effect](https://lawsofsoftwareengineering.com/laws/second-system-effect/)
- [Law of Unintended Consequences](https://lawsofsoftwareengineering.com/laws/law-of-unintended-consequences/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/brooks-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-teams]]
- indexed_by: [[software-engineering-laws-decision-map]]
