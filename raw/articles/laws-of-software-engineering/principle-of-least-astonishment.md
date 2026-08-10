---
title: "Principle of Least Astonishment"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/]
description: "Principle of Least Astonishment 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-principle-of-least-astonishment
source_url: https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/
source_category: Design
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:1da08c33ea824f586c7aa970ae1eb73ea9e9596b44bc565200170bd1c8159c0d
license: CC-BY-NC-ND-4.0
---

# Principle of Least Astonishment

Software and interfaces should behave in a way that least surprises users and other developers.

## Takeaways

- Design decisions should align with user expectations. When someone uses a component (a UI element, API, etc.), its behavior should not be surprising or counterintuitive.
- Following platform norms or standard conventions yields the least astonishment.
- In practice, it improves usability and developer experience. Users can predict how to interact with the software, and developers can predict how to use an API by analogy with similar ones. Surprises often lead to mistakes.

## Overview

The Principle of Least Astonishment (POLA) is a general design principle in user interface design, software API design, coding, and documentation. The idea is simple: don’t surprise the user.

The system should behave in a way that matches the user’s mental model of how it ought to work. Violating this principle doesn’t necessarily break functionality, but it breaks trust and ease of use.

In coding, this principle states that your code should behave as the developer expects when name, type, and context are taken into account. We should choose defaults and behaviors that match standard conventions and avoid “surprise” side effects.

## Examples

In software APIs, POLA means designing functions and behaviors that meet standard expectations. If you have a method `deleteFile()`, one would expect it to remove the file. It should not secretly archive it or throw an error if the file doesn’t exist.

If your method works similarly to a well-known one in another library, keep naming and behavior aligned. A `toString()` method should return human-readable text, not a binary blob.

POLA also covers error handling and defaults. Sensible defaults cause the least surprise. For developers, code surprises are equally problematic. If a function `parseDate(str)` internally modifies a global date format setting, that’s surprising.

Following standard naming conventions matters: a variable named `isReady` should be boolean, a function named `compute` should return something rather than modify global state.

A delighted user or developer uses something and it “just works” as expected.

## Origins

The concept of least astonishment has roots in early human-computer interaction. An early mention appears in PL/I programming language documentation around 1967, complaining that certain behaviors violated the “law of least astonishment.”

The principle was explicitly stated in a 1972 publication on programming language design, recommending that language constructs behave as their syntax suggests and follow widely accepted conventions.

Since then, it has been emphasized across various domains. In the Unix community, Eric Raymond’s Art of Unix Programming references it as the “Rule of Least Surprise.”

## Further Reading

- [The Art of Unix Programming Eric S. Raymond's book including the Rule of Least Surprise](https://amzn.to/4q4uTTY)
- [How to Design a Good API and Why it Matters Joshua Bloch's talk on API design principles](https://www.youtube.com/watch?v=aAb7hSCtvGw)
- [Principle of Least Astonishment - Wikipedia Overview of the principle with history and examples](https://en.wikipedia.org/wiki/Principle_of_least_astonishment)

## Last updated

July 20, 2026

## Related Laws

- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)
- [Postel's Law](https://lawsofsoftwareengineering.com/laws/postels-law/)
- [Law of Demeter](https://lawsofsoftwareengineering.com/laws/law-of-demeter/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/principle-of-least-astonishment/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-design]]
- indexed_by: [[software-engineering-laws-decision-map]]
