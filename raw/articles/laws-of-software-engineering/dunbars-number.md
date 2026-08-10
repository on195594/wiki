---
title: "Dunbar's Number"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/dunbars-number/]
description: "Dunbar's Number 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-dunbars-number
source_url: https://lawsofsoftwareengineering.com/laws/dunbars-number/
source_category: Teams
source_experience: senior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:b1986bda5f5be27b85ebe6a54e316995c803080bb2054d0ca7f646494e4d84eb
license: CC-BY-NC-ND-4.0
---

# Dunbar's Number

There is a cognitive limit of about 150 stable relationships one person can maintain.

## Takeaways

- Dunbar’s number (~150) is the size of a community in which everyone knows each other’s identities and roles. Beyond this, our brains struggle to track relationships.
- In software organizations, teams larger than ~100-150 will require more hierarchy or splitting into subgroups to function effectively. Coordination overhead rises sharply.
- Smaller limits exist for closer relationships. Effective working groups might be much smaller than 150, but 150 is an upper bound for a community feeling.
- Strong collaboration happens in groups far below the 150 threshold. Small teams win.

## Overview

Dunbar’s Number means that an engineering department of 150 might function informally, but as it grows past that, you start needing more formal rules, communication channels, and management layers. Informal knowledge (“I know who to talk to about X”) begins to fail, and teams feel impersonal.

The rule encourages designing sub-teams or “teams of teams” that are small enough to work together effectively. Dunbar also proposed smaller social layers: ~5 intimate relationships, ~15 trusted collaborators, ~50 close working relationships, and ~150 stable social connections.

For software teams, high-trust work happens in tiny groups, teams larger than ~10-15 lose cohesion, and the 150 limit applies to departments or communities, not day-to-day collaboration.

## Examples

Many startups report that around the 150-employee mark, the culture shifts. You no longer know everyone’s name, informal communication falters, and you start needing all-hands meetings and internal newsletters. That’s Dunbar’s number in action.

The **Linux kernel community** has thousands of contributors, but within it are maintainers and subsystem teams that are relatively small. Communication is structured into mailing lists by subsystem, so any given person communicates only with a small number of peers.

Amazon’s “two-pizza teams” (5-10 people) show that even within 150, effective working teams are smaller units.

## Origins

**Robin Dunbar** introduced this number in a 1992 paper and popularized it in his book *Grooming, Gossip, and the Evolution of Language*. He found a correlation between primate neocortex size and social group size, predicting human size at ~150.

Examples such as historical village sizes, military company units, and communal groups often hover around 100-200, lending credence to the figure.

## Further Reading

- [Dunbar's Number - Wikipedia Wikipedia article on Dunbar's number](https://en.wikipedia.org/wiki/Dunbar%27s_number)
- [Grooming, Gossip, and the Evolution of Language Robin Dunbar's book introducing the concept](https://www.amazon.com/Grooming-Gossip-Evolution-Language-Dunbar/dp/0674363361)

## Last updated

June 24, 2026

## Related Laws

- [Conway's Law](https://lawsofsoftwareengineering.com/laws/conways-law/)
- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/dunbars-number/
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
