---
title: Building Self-Correcting Memory in OpenWiki
created: 2026-08-26
updated: 2026-08-26
type: raw-source
tags: [agent, memory, knowledge-base, verification, architecture]
sources: [docs:https://www.langchain.com/blog/self-correcting-memory-openwiki]
status: captured
---

# Building Self-Correcting Memory in OpenWiki

Source URL: https://www.langchain.com/blog/self-correcting-memory-openwiki
Source title: Building Self-Correcting Memory in OpenWiki
Extraction route: deterministic JSON-LD Article.articleBody extraction
Captured: 2026-08-26
Source quality: structured summary
Publication date: not available in extracted source metadata

## Source summary

OpenWiki decomposes documentation knowledge into independently checkable claims, persists the code evidence and evidence version supporting each claim, marks claims stale when the evidence changes, and revalidates or corrects them when the relevant page is read or updated. The article reports a replay evaluation over 2,000 claims and presents Open Knowledge Format (OKF) v0.2 metadata as a portable trust summary.

## Reported evidence

The article reports supported claims increasing from 92.9% to 97.8%, stale claims decreasing from 3.5% to 0.5%, hallucinated claims decreasing from 0.7% to 0%, and unverified claims decreasing from 2.9% to 1.7%. These are source-specific results and are not Hermes benchmarks.

## Evidence limitations

This is a vendor/practitioner article. The extracted source does not independently establish that the same schema, stale-detection method, thresholds, or runtime behavior will transfer to Hermes. The full implementation and evaluation artifacts were not independently reproduced during capture.
