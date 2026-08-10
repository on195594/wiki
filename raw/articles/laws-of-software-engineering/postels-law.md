---
title: "Postel's Law"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/postels-law/]
description: "Postel's Law 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-postels-law
source_url: https://lawsofsoftwareengineering.com/laws/postels-law/
source_category: Quality
source_experience: mid
source_updated_at: "July 10, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:fd7b7aa316b48807cbdd501a0b633f0d948abf83c298d4054f5783aff15a5a47
license: CC-BY-NC-ND-4.0
---

# Postel's Law

Be conservative in what you do, be liberal in what you accept from others.

## Takeaways

- When your system emits data or interacts with the outside world, adhere closely to protocols and standards.
- When receiving data, handle variations, minor errors, or deviations where possible. Don’t crash or reject communication over minor issues.
- In modern times, overly liberal acceptance can sometimes mask errors, so this law is occasionally tempered with security considerations.

## Overview

This law says that if your server sends HTTP responses, it should format headers exactly per spec. But if your server receives an HTTP request with an uncommon header order or an unusual format, you should still process it rather than drop the connection, as long as you can interpret it safely.

This principle contributed to the Internet’s resilience, meaning that different implementations can communicate because each side strives to be compatible.

In software in general, think of file readers: a robust one can open not-quite-perfect files (e.g., a tolerant XML parser might recover from a minor error), whereas a strict one might refuse. Postel’s Law would encourage the former. However, it has caveats. Being too liberal can allow sloppy producers to proliferate, and in security contexts, accepting malformed input can be risky. Some argue that overly tolerant software can cause long-term interoperability problems because producers never fix their bugs if everyone tolerates them.

## Examples

In **web browsers**, HTML on websites is often malformed. Browsers, following Postel’s spirit, perform extensive error correction and forgiving parsing. They’ll still render the page even if a tag isn’t closed correctly. If browsers were strict, half the web pages might not display.

In **APIs**, say your service expects a timestamp. If it receives a timestamp without a time zone, instead of rejecting, maybe you assume UTC or try to parse it anyway, being liberal in acceptance. But when your service returns data, you always include the time zone to be conservative and precise in output.

An **email client** that receives a slightly non-conforming email (missing a MIME boundary or incorrect newline encodings) will still attempt to show the email rather than throwing an error.

## Origins

Jon Postel wrote this in the specification of TCP in 1980 (RFC 761): “TCP implementations should follow a general principle of robustness: be conservative in what you send, be liberal in what you accept.” It became known as Postel’s Law or the Robustness Principle and influenced many protocol designs.

There’s a modern reconsideration: the HTML5 spec codified much of the error handling that browsers already do, arguing that all that “liberal acceptance” should itself be standardized to avoid ambiguity.

## Further Reading

- [Robustness Principle - Wikipedia Overview of Postel's Law and its applications](https://en.wikipedia.org/wiki/Robustness_principle)
- [RFC 761 - DoD Standard Transmission Control Protocol The TCP specification where Postel articulated the robustness principle](https://datatracker.ietf.org/doc/html/rfc761)
- [The Harmful Consequences of Postel's Maxim A critical examination of when being too liberal causes problems](https://datatracker.ietf.org/doc/html/draft-thomson-postel-was-wrong-00)
- [The Robustness Principle Reconsidered Eric Allman's ACM Queue article on security implications of liberal acceptance](https://queue.acm.org/detail.cfm?id=1999945)

## Last updated

July 10, 2026

## Related Laws

- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [The Law of Leaky Abstractions](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
- [Fallacies of Distributed Computing](https://lawsofsoftwareengineering.com/laws/fallacies-of-distributed-computing/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/postels-law/
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
