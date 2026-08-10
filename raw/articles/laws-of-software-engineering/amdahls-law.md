---
title: "Amdahl's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/amdahls-law/]
description: "Amdahl's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-amdahls-law
source_url: https://lawsofsoftwareengineering.com/laws/amdahls-law/
source_category: Scale
source_experience: senior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:8aa55cf5eeea881d427f741ef4fee51e744eaff457c94c2f8fe15a25e4596b01
license: CC-BY-NC-ND-4.0
---

# Amdahl's Law

The speedup from parallelization is limited by the fraction of work that cannot be parallelized.

## Takeaways

- Sequential work sets the ceiling, and no amount of parallelism can overcome it.
- Scaling exposes bottlenecks. More resources make limits visible, not disappear.
- Fix before you scale: reduce sequential paths first. Parallelism comes second.
- It applies to people, too. Decision bottlenecks can dominate at the team scale.

## Overview

As you add CPU cores, only the parallelizable fraction of your code speeds up. The sequential fraction remains unchanged and eventually dominates total execution time. If “s” is the sequential fraction, the maximum speedup with infinite parallel resources is 1/s. So if 10% is sequential, maximum speedup is 10x. If 50% is sequential, maximum speedup is only 2x.

This applies beyond hardware. If your system has a database that can’t be parallelized, adding application servers hits a wall. The same holds for organizations: if one person or committee handles all architectural decisions, adding engineers increases coordination costs without increasing throughput.

## Examples

Adding application servers doesn’t help if all requests hit a single database instance. One database becomes the limit.

Another example: breaking a monolith into microservices won’t improve performance if all requests ultimately serialize through a shared dependency, such as an authentication or billing service.

## Origins

Gene Amdahl, a computer architect known for his work on IBM mainframes, introduced the law in 1967 at the AFIPS Spring Joint Computer Conference.

It was originally framed around processor performance but has since proven universally applicable to systems and organizations.

## Further Reading

- [Validity of the Single Processor Approach to Achieving Large Scale Computing Capabilities Gene Amdahl's original 1967 paper](https://dl.acm.org/doi/10.1145/1465482.1465560)
- [Amdahl's Law - Wikipedia Overview of the law with visual examples](https://en.wikipedia.org/wiki/Amdahl%27s_law)
- [The Mythical Man-Month Fred Brooks' classic on software engineering and scaling](https://amzn.to/3MUjDL7)

## Last updated

July 20, 2026

## Related Laws

- [Gustafson's Law](https://lawsofsoftwareengineering.com/laws/gustafsons-law/)
- [Metcalfe's Law](https://lawsofsoftwareengineering.com/laws/metcalfes-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/amdahls-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-scale]]
- indexed_by: [[software-engineering-laws-decision-map]]
