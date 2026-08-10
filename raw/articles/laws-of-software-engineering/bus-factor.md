---
title: "Bus Factor"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/bus-factor/]
description: "Bus Factor 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-bus-factor
source_url: https://lawsofsoftwareengineering.com/laws/bus-factor/
source_category: Teams
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:4c50d75d6a7abc06c0ac39054b317f72d0cafd537be01d4c35dc057883fdd6a1
license: CC-BY-NC-ND-4.0
---

# Bus Factor

The minimum number of team members whose loss would put the project in serious trouble.

## Takeaways

- A bus factor of 1 means one person holds critical knowledge; if they disappear, the project is essentially ‘doomed’ or stalled. A higher bus factor (e.g., 5) means the project could lose any one of five specific people before stopping work.
- It’s basically a measure of knowledge distribution and risk. A high bus factor is good (knowledge is shared among many), while a low is bad (single points of failure in expertise).
- Teams should work to increase their bus factor by sharing knowledge, documenting critical systems, having code reviews, and rotating responsibilities.

## Overview

The Bus Factor highlights the human single point of failure in projects. In many software teams, one or two people might understand the legacy system, a crucial algorithm, or have all the deployment knowledge. If those people leave, others cannot easily pick up the work.

The concept encourages actively avoiding such dependency. Improving bus factor overlaps with knowledge management practices: pair programming, code reviews, documentation, mentorship, and rotating responsibilities.

## Examples

If a startup’s only database expert is Alice, the bus factor for database knowledge is 1. If Alice quits, nobody else knows the backups, schema intricacies, or tuning.

The **Left-pad incident** reflects a bus factor of 1 for the broader ecosystem: a single maintainer pulled a tiny NPM package, and thousands of builds broke.

## Origins

The concept was popularized in the 1990s in discussions of project risk. The term is somewhat morbid, so some call it “lottery factor” (flipping the scenario to a positive reason someone leaves).

It’s not attributed to a single person but emerged as slang in software teams. An early reference appears in patterns literature (1994 PLoP conference), discussing “truck number” in organizational patterns. The idea likely existed informally even earlier.

## The Dead Sea Effect

Bruce F. Webster coined this pattern in 2008. In dysfunctional organizations, talent vanishes while mediocrity accumulates, just like the Dead Sea where water escapes but salt remains. Skilled engineers have options and won’t tolerate dysfunction for long. Those who stay are often the ones who can’t easily find work elsewhere.

A team suffering from the Dead Sea Effect has knowledge concentrated in the wrong people. When these “residue” employees finally leave, the organization discovers its institutional knowledge was never institutional at all.

## Further Reading

- [Bus Factor - Wikipedia Overview of the Bus Factor concept and its implications](https://en.wikipedia.org/wiki/Bus_factor)
- [Left-pad incident - Wikipedia A real-world example of bus factor risk in open source](https://en.wikipedia.org/wiki/Npm_left-pad_incident)
- [The Dead Sea Effect - Bruce F. Webster The original article describing how talent drains from dysfunctional organizations](https://brucefwebster.com/2008/04/11/the-wetware-crisis-the-dead-sea-effect/)
- [If Guido was hit by a bus? Michael McLay's 1994 mailing list post, one of the earliest references to the bus factor concept](https://legacy.python.org/search/hypermail/python-1994q2/1040.html)
- [Organizational Patterns of Agile Software Development Coplien & Harrison (2004) - patterns for building effective software organizations](https://www.wiley.com/en-us/Organizational+Patterns+of+Agile+Software+Development-p-9780131467408)

## Last updated

July 20, 2026

## Related Laws

- [Conway's Law](https://lawsofsoftwareengineering.com/laws/conways-law/)
- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Dunbar's Number](https://lawsofsoftwareengineering.com/laws/dunbars-number/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/bus-factor/
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
