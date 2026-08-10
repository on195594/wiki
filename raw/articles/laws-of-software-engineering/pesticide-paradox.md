---
title: "Pesticide Paradox"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/pesticide-paradox/]
description: "Pesticide Paradox 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-pesticide-paradox
source_url: https://lawsofsoftwareengineering.com/laws/pesticide-paradox/
source_category: Quality
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:79f37022c5b69295147b08584b061971c388c9dc791404b80430ae08eb629541
license: CC-BY-NC-ND-4.0
---

# Pesticide Paradox

Repeatedly running the same tests becomes less effective over time.

## Takeaways

- Over time, an outdated test suite will identify fewer bugs. The tests are still helpful, but no longer effective at detecting new defects.
- This paradox illustrates the need to infuse new test data continuously. It is essential for testers not to become complacent with their test scripts, thinking that these alone will be sufficient in the future.
- By periodically creating new tests (by altering existing ones), you effectively ‘refresh the pesticide,’ thereby providing an opportunity to catch new bugs. This involves extending tests for new functionality, trying new input combinations, or perhaps just investigating new boundary cases.

## Overview

The “Pesticide Paradox” analogy comes from agriculture. When the same pesticide is used repeatedly, pests develop resistance to it.

In software, the first runs of a new test suite might find many bugs. Those bugs get fixed. If you keep running the same tests without changes, you won’t find more bugs there. The software has become “immune” to those specific tests.

The testing process cannot be stagnant. Test cases must be maintained regularly. After every release cycle, testers should assess which bugs made it to production and enhance the test suite accordingly.

This paradox also argues for exploratory testing, where testers approach the application in new ways each iteration, uncovering problems a static regression suite would miss. The paradox doesn’t mean regression testing is useless, as old tests catch regressions. But to catch *new* bugs, you must design *new* tests.

## Examples

Let’s consider a mobile app where, in the first release, testers wrote extensive tests for the login and user profile features, finding and getting ten bugs fixed in those areas. In the subsequent releases, those test cases all pass (no new bugs in login or profile, great). Meanwhile, the app has added a messaging feature, but the test suite didn’t add many cases for it. However, within a couple of releases, complaints started trickling in regarding the messaging functionality crashing. Unfortunately, the test suite failed to identify these because it was not updated to test messaging, which is predominantly centered on login and profile.

This is the pesticide paradox, which states that as testing became green (no defects remained in the code tested), new defects began to emerge, thereby requiring new tests. However, after the group includes their messaging tests, they begin to uncover these issues before they become releases. This process continues until those tests no longer find new issues, and the pattern repeats with the following features that emerge.

## Origins

The concept was articulated by Dr. Boris Beizer, a software testing expert, and became widely known as one of the “seven principles of testing” in ISTQB (International Software Testing Qualifications Board) materials.

Beizer stated something to the effect of: every method of testing will yield a pesticide paradox, bugs adapt to tests, leaving more subtle bugs behind.

## Further Reading

- [Software Testing Techniques Boris Beizer's comprehensive book on testing techniques](https://amzn.to/3Yg3jH4)
- [ISTQB Foundation Level Syllabus Official ISTQB syllabus covering the seven principles of testing](https://www.istqb.org/certifications/certified-tester-foundation-level)
- [Lessons Learned in Software Testing Practical wisdom on software testing by Kaner, Bach, and Pettichord](https://amzn.to/3YNqIzD)

## Last updated

July 20, 2026

## Related Laws

- [Lehman's Laws of Software Evolution](https://lawsofsoftwareengineering.com/laws/lehmans-laws/)
- [Testing Pyramid](https://lawsofsoftwareengineering.com/laws/testing-pyramid/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/pesticide-paradox/
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
