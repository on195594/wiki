---
title: "Cunningham's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/cunninghams-law/]
description: "Cunningham's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-cunninghams-law
source_url: https://lawsofsoftwareengineering.com/laws/cunninghams-law/
source_category: Decisions
source_experience: junior
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:bc2ad54106fb982203f104f717ea4dfed6dec4a1bb8abf4e5682fc391a939f05
license: CC-BY-NC-ND-4.0
---

# Cunningham's Law

The best way to get the correct answer on the Internet is not to ask a question, it's to post the wrong answer.

## Takeaways

- People online love correcting errors. If you’re stuck on a problem, sometimes proposing a solution (even if it might be wrong) can get you to the right solution faster.
- Asking a question might evoke only silence, but confidently stating something (even if incorrect) often provokes a reaction.
- Instead of endlessly asking ‘How should we do X?’, propose a draft or prototype. Even if it’s not entirely correct, having a concrete starting point often gets more feedback (‘No, not like that, do it this way’).

## Overview

Cunningham’s Law arose in the context of online communities, particularly wikis and forums. The underlying observation is that assertions draw more engagement than questions. On Wikipedia, if someone posts incorrect information, other editors will rush in to fix it.

In software engineering, you see this on Stack Overflow and mailing lists. A user asks a question and gets few responses, but if someone posts a slightly wrong answer, others quickly chime in to correct it. By putting something out there, you transform a passive question into an active discussion.

## Examples

A developer stuck on configuring an open-source library posts a question and gets no replies. Using Cunningham’s Law, they post: “For anyone else struggling, the solution is to set ConfigMode to False.” If wrong, someone (possibly the library maintainer) will quickly reply: “Actually, no, you should leave ConfigMode true, it’s another setting you need to change.”

A new developer uncertain about implementing a feature submits a pull request with their best attempt rather than asking in the abstract. Senior engineers review it and point out improvements. By presenting a “proposed answer,” the developer gets the team’s knowledge and ends up with the right approach.

## Origins

Cunningham’s Law is named after Ward Cunningham, the American programmer best known for creating the first wiki software. The actual phrasing of the law is often attributed to a colleague of Cunningham, Steven McGeady, who formulated the adage and named it after Cunningham.

According to McGeady, Ward Cunningham gave him advice in the 1980s regarding early internet forums (Usenet), and McGeady later described it in a comment on a New York Times blog in 2010.

The irony is that Ward Cunningham’s invention, the wiki, is a platform built precisely on the idea that people will collaboratively correct and improve content.

The French have a proverb, “Prêcher le faux pour savoir le vrai” (preach the false to know the true), which captures a similar concept.

## Further Reading

- [The Wiki Way - Bo Leuf & Ward Cunningham Book about wiki philosophy and collaborative knowledge building](https://en.wikipedia.org/wiki/The_Wiki_Way)
- [How to Ask Questions the Smart Way - Eric S. Raymond Classic guide on effective communication in technical communities](http://www.catb.org/~esr/faqs/smart-questions.html)
- [Cunningham's Law - Wikipedia Wikipedia article on the law and its origins](https://meta.wikimedia.org/wiki/Cunningham%27s_Law)

## Last updated

July 20, 2026

## Related Laws

- [Linus's Law](https://lawsofsoftwareengineering.com/laws/linuss-law/)
- [Broken Windows Theory](https://lawsofsoftwareengineering.com/laws/broken-windows-theory/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/cunninghams-law/
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
