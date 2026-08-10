---
title: "Dunning-Kruger Effect"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/dunning-kruger-effect/]
description: "Dunning-Kruger Effect 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-dunning-kruger-effect
source_url: https://lawsofsoftwareengineering.com/laws/dunning-kruger-effect/
source_category: Decisions
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:b3478bd162442613e675a308e3f67c72d01b081c003e7b399b1a71a6d8de0a18
license: CC-BY-NC-ND-4.0
---

# Dunning-Kruger Effect

The less you know about something, the more confident you tend to be.

## Takeaways

- Confidence without context is unreliable. Early confidence often signals ignorance, not mastery.
- Awareness grows faster than skill. Learning initially reduces confidence, only to rebuild it.
- Real experts speak in ranges, trade-offs, and probabilities, not with confidence about every topic.

## Overview

The Dunning-Kruger Effect explains a gap between confidence and competence. When people know little about a domain, they lack the awareness required to judge their own ability. As a result, they overestimate how well they understand the problem.

As learning progresses, people discover the depth and complexity of the domain.

Awareness of unknowns grows faster than capability, leading to a drop in confidence, often called the “valley of despair.” Only after experience does confidence rise again, now with fundamental understanding.

## Examples

New developers often give confident, precise estimates, while experienced developers give ranges (the famous “it depends” answer). The juniors aren’t being careless; they simply don’t yet know what they don’t know (unknown-unknowns).

Peak enthusiasm for a new technology often comes from those who have used it least. Those with deep experience are more measured.

We should also note that *Impostor syndrome* reflects miscalibration in the opposite direction. Skilled individuals underestimate their competence because they are deeply aware of complexity and edge cases.

## Origins

The effect was described by psychologists **David Dunning** and **Justin Kruger** in a 1999 study at Cornell University. Their experiments showed that people with low performance consistently overestimated their ability on logic, grammar, and humor tests, while high performers underestimated their ability.

The proposed mechanism is simple: the skills required to perform well are often the same skills needed to assess performance accurately.

One caveat: the original study measured how people rank themselves against peers. Low performers overestimated their relative standing, but they were not more confident than experts; the popular “peak of confidence” curve is a later simplification of the findings.

## Impostor Syndrome

Impostor syndrome is the tendency of competent people to believe they are inadequate and attribute their success to luck or fraud. In software engineering, this is most evident in top performers. As engineers gain experience, they develop a better sense of complexity and how things can fail, but greater knowledge can bias self-evaluation.

Contrary to the Dunning-Kruger Effect, impostor syndrome arises out of expertise. What usually happens in software teams: juniors overestimate themselves, while seniors underestimate themselves. Healthy teams deal with both by grounding decisions in evidence, reviews, and shared learning rather than self-perception.

## Further Reading

- [Dunning-Kruger Effect - Wikipedia Comprehensive overview of the cognitive bias and its research](https://en.wikipedia.org/wiki/Dunning%E2%80%93Kruger_effect)
- [Unskilled and Unaware of It - Original 1999 Paper The original study by Kruger and Dunning in the Journal of Personality and Social Psychology](https://psycnet.apa.org/doi/10.1037/0022-3514.77.6.1121)
- [We Are All Confident Idiots - David Dunning David Dunning's accessible article in Pacific Standard explaining the effect](https://psmag.com/social-justice/confident-idiots-92793)
- [Thinking, Fast and Slow Daniel Kahneman's seminal book on cognitive biases and decision-making](https://amzn.to/48WboH0)

## Last updated

July 20, 2026

## Related Laws

- [Brooks's Law](https://lawsofsoftwareengineering.com/laws/brooks-law/)
- [Hanlon's Razor](https://lawsofsoftwareengineering.com/laws/hanlons-razor/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/dunning-kruger-effect/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-decisions]]
- indexed_by: [[software-engineering-laws-decision-map]]
