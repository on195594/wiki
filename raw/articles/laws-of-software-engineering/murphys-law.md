---
title: "Murphy's Law / Sod's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/murphys-law/]
description: "Murphy's Law / Sod's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-murphys-law
source_url: https://lawsofsoftwareengineering.com/laws/murphys-law/
source_category: Quality
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:26bdc366a5e93ae1122eb07663432a8e6ee6040dfd86ef1b8fd62852e115a4ca
license: CC-BY-NC-ND-4.0
---

# Murphy's Law / Sod's Law

Anything that can go wrong will go wrong.

## Takeaways

- If an error can happen, it will happen. Plan and code defensively with this in mind.
- Add error handling, backups, and checks.
- Edge cases will occur in production. Write tests for these kinds of scenarios.

## Overview

In software, Murphy’s Law is often used to explain bugs and production incidents: whatever can go wrong in code (a null pointer, a race condition, a network outage) eventually will manifest, especially in large user bases or at the worst possible time.

In practice, this law encourages developers to write more defensive code. This means checking for nulls, handling exceptions, validating inputs, and failing gracefully when errors occur. It also reminds DevOps teams to anticipate failures by implementing monitoring, enabling rollbacks, and maintaining contingency plans.

## Examples

If a web form field can accept text, someone will enter a 10,000-character string of weird symbols to see what happens, unless you’ve explicitly handled it. If memory can run out, it will be when multiple processes align just so.

A famous real-world instance was during a live demo (who remembers the Windows 98 presentation by Bill Gates?), if something can glitch, it likely will.

In coding, consider a function that assumes an input file exists. Murphy’s Law says that one day that file won’t be there or will be corrupted, so your code should handle the file-not-found or bad-data scenario rather than crash.

Another typical case is that the server will crash on your only day off, because that’s when it’s most likely to cause trouble. Engineers thus build highly available systems and pager rotations to mitigate Murphy’s Law.

## Origins

Attributed to Edward A. Murphy Jr., an engineer working on rocket sled experiments in 1949. It became popular in aerospace and then everywhere. In software, it’s been around as long as bugs have, constantly reminding us that if there’s one untested scenario, one user will find it.

## Sod's Law

In British English, the same principle may be referred to using the term “Sod’s Law”. It carries a similar meaning, although it may also reflect the element of spite, as the universe is somehow interfering in your endeavors.

Both versions may be used interchangeably in Software Engineering to highlight the significance of defensive programming.

## Further Reading

- [Murphy's Law - Wikipedia History and variations of the famous adage](https://en.wikipedia.org/wiki/Murphy%27s_law)
- [Windows 98 Crash During Live Demo Bill Gates' infamous BSOD during a Windows 98 presentation](https://www.youtube.com/watch?v=yeUyxjLhAxU)
- [Defensive Programming Programming practices to anticipate and handle errors](https://en.wikipedia.org/wiki/Defensive_programming)
- [CrowdStrike Channel File 291 RCA Exec Summary Root cause analysis of the CrowdStrike outage, a real-world example of Murphy's Law at scale](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/)

## Last updated

July 20, 2026

## Related Laws

- [Confirmation Bias](https://lawsofsoftwareengineering.com/laws/confirmation-bias/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/murphys-law/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-quality]]
- indexed_by: [[software-engineering-laws-decision-map]]
