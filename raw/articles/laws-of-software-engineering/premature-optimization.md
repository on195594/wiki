---
title: "Premature Optimization (Knuth's Optimization Principle)"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/premature-optimization/]
description: "Premature Optimization (Knuth's Optimization Principle) 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-premature-optimization
source_url: https://lawsofsoftwareengineering.com/laws/premature-optimization/
source_category: Planning
source_experience: junior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:2cd0d8361f37661e4ebeace0607391b17919b95ae989c1fe70159ed5d6a731d4
license: CC-BY-NC-ND-4.0
---

# Premature Optimization (Knuth's Optimization Principle)

Premature optimization is the root of all evil.

## Takeaways

- Most code doesn’t run in performance-critical hotspots, so obsessing over micro-optimizations everywhere wastes time and makes code harder to read and maintain.
- According to Knuth, we should forget about small efficiencies about 97% of the time, and focus on clean design and correct functionality.
- Optimized code is often more complex or less readable. If done prematurely, you incur this cost even when it’s unnecessary.
- Get it working correctly first, then make it fast, then make it pretty.

## Overview

Knuth’s Optimization Principle captures a fundamental trade-off in software engineering: performance improvements often increase complexity. Applying that trade-off before understanding where performance actually matters leads to unreadable systems.

Early in development, your focus should be on a clear design. If you optimize too soon, you might introduce bugs or inflexibility, all to speed up parts of the code that may not even be bottlenecks. It’s often cited that 20% of the code may consume 80% of the execution time (a Pareto-like notion). Optimizing anything outside that critical 20% is wasted effort and adds risk. The principle advises writing simple code, then profiling and improving only the parts that truly need it.

## Examples

A developer writes a low-level C routine with complex bit-twiddling to squeeze out speed, spending two days on it, only to find that the function is called once at startup, taking 0.001% of runtime. The effort was wasted, and the code is now more complex to understand. Meanwhile, another part of the program (such as a sorting function on a large dataset) was the real bottleneck, but remained unoptimized because time was spent on the wrong thing.

Another example is prematurely choosing a complex data structure for theoretical efficiency (say, a custom tree for log(N) lookups) when the simpler approach (like a linear search) would have been acceptable for the data sizes involved.

In contrast, following Knuth’s advice, you implement simply, measure, then find that 80% of time is spent in one loop, you optimize that loop or use a better algorithm there. This gives real improvements with minimal added complexity elsewhere.

## Origins

Donald Knuth, a legendary computer scientist, made this statement in his 1974 paper “Structured Programming with Go To Statements” published in ACM Computing Surveys.

The full quote provides important context: “We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil. Yet we should not pass up our opportunities in that critical 3%.”

He didn’t literally mean all evil, but the quote caught on because it resonates with developers who have seen codebases twisted by needless optimizations.

Over time, this quote became almost a proverb in software engineering. It’s taught to juniors: first make it work, then make it right, then (if needed) make it fast.

## Further Reading

- [Structured Programming with go to Statements Donald Knuth's original 1974 paper in Computing Surveys](https://pic.plover.com/knuth-GOTO.pdf)
- [Code Complete Steve McConnell's comprehensive guide to software construction](https://amzn.to/4b6YVBx)
- [Program Optimization - Wikipedia Overview of optimization techniques and when to apply them](https://en.wikipedia.org/wiki/Program_optimization)

## Last updated

June 24, 2026

## Related Laws

- [YAGNI (You Aren't Gonna Need It)](https://lawsofsoftwareengineering.com/laws/yagni/)
- [Hofstadter's Law](https://lawsofsoftwareengineering.com/laws/hofstadters-law/)
- [Gall's Law](https://lawsofsoftwareengineering.com/laws/galls-law/)
- [Kernighan's Law](https://lawsofsoftwareengineering.com/laws/kernighans-law/)
- [Amdahl's Law](https://lawsofsoftwareengineering.com/laws/amdahls-law/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/premature-optimization/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-planning]]
- indexed_by: [[software-engineering-laws-decision-map]]
