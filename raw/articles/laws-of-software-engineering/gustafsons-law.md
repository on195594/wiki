---
title: "Gustafson's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/gustafsons-law/]
description: "Gustafson's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-gustafsons-law
source_url: https://lawsofsoftwareengineering.com/laws/gustafsons-law/
source_category: Scale
source_experience: senior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:988078c0091a3cb7706c8eb18961bbeaa4e833122acf89e247562654c811a6ed
license: CC-BY-NC-ND-4.0
---

# Gustafson's Law

It is possible to achieve significant speedup in parallel processing by increasing the problem size.

## Takeaways

- As computing resources grow, you can compute more problems in a given time, rather than solving the same issues faster.
- It opposes the pessimism of Amdahl’s Law by assuming the size of the problem to be solved will increase proportionally with computing power, so that parallel processors remain busy.
- Practically, Gustafson’s Law promotes the use of more resources in computation to achieve more in terms of the scope of tasks, rather than obtaining diminishing returns.
- Software should be designed to scale out: as more cores or machines are added, the problem size grows and the extra capacity does useful work.

## Overview

Gustafson’s Law is a principle in parallel computing that offers an optimistic view of scalability. Where Amdahl’s Law assumes a fixed problem size and concludes that speedup is limited by serial work, Gustafson’s Law changes the perspective.

It observes that when more processors are available, developers tend to increase the problem size to use that extra power. If you have a cluster twice as powerful, you might process twice as much data in the same time.

The parallel portion of work grows with N processors while the serial portion remains about the same, leading to “scaled speedup” that can be almost linear.

Gustafson’s insight is that developers naturally use more computing power by asking bigger questions.

## Examples

In high-performance computing, climate modeling or molecular simulations routinely increase model resolution when more processors are available. A weather simulation on 1000 CPUs won’t just finish 1000x faster; instead, they run a far more detailed global model in the same time, yielding a better forecast.

In big data processing, if analyzing 1 million records takes an hour on one machine, a 10-machine cluster might analyze 10 million records in an hour instead of finishing in 6 minutes.

Modern distributed systems like MapReduce and Spark encourage splitting datasets into more partitions as nodes increase, keeping all processors busy.

## Origins

Gustafson’s Law was formulated by computer scientist John L. Gustafson (with Edwin Barsis) in 1988, in a paper titled “Reevaluating Amdahl’s Law.” Gustafson was working at Sandia National Laboratories on high-performance computing.

At that time, Amdahl’s 1967 result cast doubt on massively parallel supercomputers. Gustafson observed that this held only if workload was kept constant. His 1988 argument demonstrated that by increasing problem size, a 1024-processor system could achieve near-1024x speedup on suitably scaled tasks.

## Further Reading

- [Reevaluating Amdahl's Law John L. Gustafson's original 1988 paper](https://dl.acm.org/doi/10.1145/42411.42415)
- [Gustafson's Law - Wikipedia Overview of the law and its relationship to Amdahl's Law](https://en.wikipedia.org/wiki/Gustafson%27s_law)

## Last updated

July 20, 2026

## Related Laws

- [Amdahl's Law](https://lawsofsoftwareengineering.com/laws/amdahls-law/)
- [Metcalfe's Law](https://lawsofsoftwareengineering.com/laws/metcalfes-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/gustafsons-law/
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
