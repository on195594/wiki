---
title: "Hanlon's Razor"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/hanlons-razor/]
description: "Hanlon's Razor 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-hanlons-razor
source_url: https://lawsofsoftwareengineering.com/laws/hanlons-razor/
source_category: Decisions
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:371e88bf244460a1f8797830aea7dfdfa7295e71561938bc6720db2969a8a514
license: CC-BY-NC-ND-4.0
---

# Hanlon's Razor

Never attribute to malice that which is adequately explained by stupidity or carelessness.

## Takeaways

- When something goes wrong, it’s likely not malicious but rather an error or misunderstanding.
- Don’t jump to ’the system is hacked’ or ‘someone intentionally broke this.’ First, consider simpler explanations (e.g., a configuration file was missed or a typographical error).
- If a colleague’s code is problematic, it’s probably not sabotage. It may be due to being rushed or unaware of something. Try to approach with questions, not accusations.

## Overview

Hanlon’s Razor advises against assuming bad faith when an outcome may be due to human error or ignorance. If a commit introduces a security hole, it’s probably a mistake, not intentional sabotage. So one responds with help and fixes, not with blame.

This doesn’t mean ignoring the possibility of malice when truly warranted (security does consider malicious actors). But for day-to-day development and operations, Hanlon’s Razor keeps you grounded: the build failed likely due to a misconfiguration, not because someone deliberately broke it.

## Examples

A customer reports that your software “deleted all my data!” It’s easy to panic and think a disgruntled employee planted a logic bomb. But Hanlon’s Razor would have you first check for a mundane bug, perhaps a boundary condition in a delete function that wipes more than intended. Indeed, you find a bug where, when a user’s account name was empty, the cleanup script deleted all records. No malice, just a bug.

In security, consider a sudden spike in server traffic. Before screaming “it’s a DDoS attack!”, check first if it’s a misconfigured client spamming or a known pattern. Most weird behaviors in systems are due to mistakes, not malicious intent.

## Origins

**Robert J. Hanlon** submitted this principle to a 1980 compilation of Murphy’s Law variations. It echoes similar statements by Napoleon and Goethe about not attributing malice where incompetence can explain it.

## Further Reading

- [Hanlon's Razor - Wikipedia Overview of the principle and its origins](https://en.wikipedia.org/wiki/Hanlon%27s_razor)
- [Blameless Postmortems - Etsy How Etsy applies blameless culture in incident response](https://www.etsy.com/codeascraft/blameless-postmortems/)
- [The Field Guide to Understanding Human Error Sidney Dekker's book on human factors in system failures](https://amzn.to/3LbyIas)

## Last updated

July 20, 2026

## Related Laws

- [Occam's Razor](https://lawsofsoftwareengineering.com/laws/occams-razor/)
- [Goodhart's Law](https://lawsofsoftwareengineering.com/laws/goodharts-law/)
- [Postel's Law](https://lawsofsoftwareengineering.com/laws/postels-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/hanlons-razor/
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
