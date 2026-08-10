---
title: "The Ringelmann Effect"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/ringelmann-effect/]
description: "The Ringelmann Effect 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-ringelmann-effect
source_url: https://lawsofsoftwareengineering.com/laws/ringelmann-effect/
source_category: Teams
source_experience: mid
source_updated_at: "July 10, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:a8c9aca0b3ac4fd19594c71eef95d85236ddf949a96660a4ee6065cf3046f693
license: CC-BY-NC-ND-4.0
---

# The Ringelmann Effect

Individual productivity decreases as group size increases.

## Takeaways

- In large teams, some people put in less effort because they assume others will pick up the slack or because their contributions are less visible.
- More people mean more communication, meetings, and alignment needed. Time spent coordinating increases, leaving less time for actual work.
- There is a point at which adding people yields diminishing returns, or even negative returns per person. Small, focused teams often outperform poorly coordinated larger teams.
- Smaller teams or individuals feel greater ownership and responsibility.

## Overview

The Ringelmann Effect states that as more people work together, individual effort decreases. In software teams, productivity per person often declines in larger groups due to coordination overhead and some individuals contributing less when in a crowd.

This effect warns that adding team members can make each existing member less efficient. Along with Brooks’s Law, it shows that teamwork doesn’t scale linearly. Teams must be structured to mitigate this with clear roles and small, focused groups.

## Examples

In a brainstorming session with 3 people, each might contribute many ideas. In a session with 15 people, many participants will say nothing, assuming others will speak.

If 10 developers work on one module, merging code, resolving conflicts, and communicating design decisions can consume significant time. This effect motivates Amazon’s “Two Pizza Rule” (a team feedable by two pizzas, roughly 5-8 people).

## Origins

Named after **Max Ringelmann**, a French agricultural engineer who observed it in physical tasks around 1913. He found that when people pulled on a rope together, each individual exerted less force than when pulling alone.

The phenomenon was later termed “social loafing” in psychology. It has been demonstrated in many group situations beyond rope pulling, from cognitive tasks to workplace productivity.

## The Amazon Two Pizza Rule

This rule says that any efficient team should be small enough to feed with two pizzas, typically 5-8 people. Small teams move faster because communication stays simple: in a team of 4, you have 6 relationships to manage; in a team of 6, that jumps to 15.

## Further Reading

- [Ringelmann Effect - Wikipedia Wikipedia article on the Ringelmann effect](https://en.wikipedia.org/wiki/Ringelmann_effect)
- [Social Loafing - Wikipedia The psychological phenomenon behind the effect](https://en.wikipedia.org/wiki/Social_loafing)
- [The Two Pizza Rule Amazon's approach to keeping teams small and effective](https://aws.amazon.com/executive-insights/content/amazon-two-pizza-team/)
- [The Tipping Point Malcolm Gladwell's book exploring how small changes can have big effects](https://amzn.to/4jfJ1Hb)
- [From Aristotle to Ringelmann: A Large-Scale Analysis of Team Productivity and Coordination in Open Source Software Projects Scholtes, Mavrodiev & Schweitzer (2016) - empirical study of team productivity and coordination in OSS projects](https://doi.org/10.1007/s10664-015-9406-4)

## Last updated

July 10, 2026

## Related Laws

- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Dunbar's Number](https://lawsofsoftwareengineering.com/laws/dunbars-number/)
- [Conway's Law](https://lawsofsoftwareengineering.com/laws/conways-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/ringelmann-effect/
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
