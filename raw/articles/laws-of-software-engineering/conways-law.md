---
title: "Conway's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/conways-law/]
description: "Conway's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-conways-law
source_url: https://lawsofsoftwareengineering.com/laws/conways-law/
source_category: Teams
source_experience: senior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:b49284d54820565a682d39c96d3e4efb74ff6f17da80f8c1f4118e7af475c18a
license: CC-BY-NC-ND-4.0
---

# Conway's Law

Organizations design systems that mirror their own communication structure.

## Takeaways

- The architecture of software systems often mirrors the organization’s org chart or team structure.
- If your company is organized in silos, you might end up with siloed software modules that don’t communicate well, reflecting those barriers.
- To achieve a desired software architecture (e.g., microservices), you might need to restructure teams accordingly, because teams build software aligned with their communication paths.
- When starting a project, realize that how you split teams or departments will likely lead to software boundaries at the same places.

## Overview

Conway’s Law states that **software systems reflect the communication structure of the organization that builds them**. A company with separate frontend, backend, and database departments will likely produce a three-tier architecture. Small, distributed teams tend to produce modular service architectures, while large, collocated teams tend to build monoliths.

To mitigate this, teams can use the **Inverse Conway Maneuver**: intentionally structuring the organization to match the desired software architecture.

## Examples

A company had separate departments for frontend, backend, and database. The software they built had a three-tier architecture, with each tier independently designed by its respective department. Integration between tiers was painful because the teams had misaligned goals.

Amazon famously organized “two-pizza teams”, each owning a specific service. Conway’s Law suggests that’s why Amazon’s architecture is service-oriented, with clear API contracts between services.

## Origins

**Melvin Conway** introduced the idea in his 1967 paper “How Do Committees Invent?” After Harvard Business Review rejected it for lacking formal proof, Datamation published it in 1968.

Fred Brooks later named it “Conway’s Law” in *The Mythical Man-Month*, which established the concept as foundational in software engineering.

## The Spotify Model

The Spotify Model organizes teams around features rather than technologies. Cross-functional **Squads** (6-12 people) own end-to-end features, grouped into **Tribes** by business area. **Chapters** and **Guilds** provide skill-sharing across squads. It works when it solves real coordination problems, but fails when copied blindly.

## Further Reading

- [How Do Committees Invent? Melvin Conway's original 1968 paper](https://www.melconway.com/Home/Committees_Paper.html)
- [Conway's Law Martin Fowler's explanation of Conway's Law](https://martinfowler.com/bliki/ConwaysLaw.html)
- [Spotify Engineering Culture The original Spotify Model blog post](https://engineering.atspotify.com/2014/3/spotify-engineering-culture-part-1)
- [Team Topologies Modern application of Conway's Law to organizational design](https://amzn.to/4jgRZ6V)

## Last updated

June 24, 2026

## Related Laws

- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)
- [The Law of Leaky Abstractions](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/conways-law/
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
