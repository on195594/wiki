---
title: "Python Performance Optimization: A Practical Guide"
author: Mostafa Ibrahim
source: Real Python
source_type: article
source_url: https://realpython.com/python-performance-optimization-guide/
source_updated_at: 2026-10-21
captured_at: 2026-10-22
created: 2026-10-22
updated: 2026-10-22
type: raw-source
tags: [python, optimization, profiling, caching]
status: raw
---

# Python Performance Optimization: A Practical Guide

## Provenance and capture scope

- Author: Mostafa Ibrahim; publisher: Real Python.
- Source URL: https://realpython.com/python-performance-optimization-guide/
- The page displays “Updated Oct 21, 2026”; this is an update date, not a verified first-publication date. The filename uses the displayed update date.
- Captured on 2026-10-22 through direct web text extraction. The readable article body, conclusion and FAQ were available.
- This file is a **selective source capture**, not a full-text archive or a verbatim translation. The excerpts below preserve original wording; the section labels organize their provenance. Navigation, advertising, interactive widgets, downloads and most code examples are omitted.
- Source quality: authored educational tutorial, useful for principles and illustrative examples; not an independent benchmark study. No sample code was executed and no timing was reproduced. Separate direct HTML metadata retrieval returned HTTP 403, so the initial publication date was not established.

## Selected original excerpts

### Diagnosis versus measurement — Measure First With timeit

> Locating a bottleneck in a large, unfamiliar program is a job for a profiler like cProfile in the standard library or the third-party line_profiler.

> It doesn’t hunt for bottlenecks. It measures one so you can confirm your suspicion with a real number instead of a guess.

The second excerpt refers to `timeit`.

### Fix order — Choose Your Fix

> The sections below start with the fixes that pay off most for the least effort, so work through them only as far as you need to.

The source sections proceed through algorithms/data structures, built-ins/standard library, caching, then further options involving memory, concurrency and C extensions.

### Data structures — Choosing Better Algorithms and Data Structures

> Building the set isn’t free, though.

> Converting a list you’ll only search once will cost you more than it saves.

### Standard library — Reaching for Built-Ins and the Standard Library

> What makes Counter fast is that it pushes the per-item work down into C, not that it’s part of the standard library. When you swap in a built-in, measure it like any other change.

### Cache benchmarks — Caching Results With functools.cache

> The two timings aren’t measuring the same work.

> Adding @cache doesn’t make that first scan any faster. It still takes as long as the uncached version.

In the source example, an untimed first call fills the cache before the timed calls. The comparison therefore contrasts repeated full scans with warm-cache hits, not cold-cache computation.

### Cache correctness and capacity — Caching Results With functools.cache

> One trap to keep in mind is that @cache stores every unique set of arguments indefinitely.

> Caching is safe only when a function’s result depends solely on its arguments, so be careful when applying it to a function that reads external data.

The source warns that its example reads a global `numbers` list while keying only on `target`; changing the list can leave stale cached answers. It suggests a bounded `lru_cache` when unbounded growth is unsuitable.

### Continuing verification — Common Pitfalls

> Treat profiling as a regular habit rather than an emergency response, and you’ll catch a slowdown while it’s still small.

## Compilation target

Principles and explicitly labeled local implications are compiled into [[hermes-python-engineering-capability-checklist]], section “Performance work should be measurement-led”. Source timings and claimed conversion break-even constants are not adopted as general thresholds.
