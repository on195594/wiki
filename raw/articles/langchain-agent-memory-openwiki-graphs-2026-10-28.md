---
title: Building Evidence-Grounded Agent Memory with OpenWiki and Graphs
created: 2026-10-29
updated: 2026-10-29
type: raw-source
tags: [agent, memory, knowledge-base, verification, architecture]
sources: [docs:https://www.langchain.com/blog/building-agent-memory-openwiki-graphs]
status: captured
---

# Building Evidence-Grounded Agent Memory with OpenWiki and Graphs

Source URL: https://www.langchain.com/blog/building-agent-memory-openwiki-graphs
Author: Eugene Liu, LangChain Blog
Publication date: 2026-10-28
Captured: 2026-10-29
Extraction route: public article text extracted from publisher page
Source quality: structured summary; not a full-text archive

## Source summary

OpenWiki compiles source documents into linked pages whose claims cite source lines and hashes. The authors add an evidence-navigation graph that connects claims, pages and paragraphs with typed edges derived from existing citations and explicit document references. Paragraph splitting and graph construction use deterministic processes without additional model calls; graph edges derived from the wiki still depend on the accuracy of model-generated citations. The graph is intended for evidence navigation rather than modeling all organizational knowledge.

## Reported evaluation

The authors tested 111 synthetic insurance documents with a ledger of 972 facts, using 80 simple lookup questions and 50 connected questions, each asked three times. The baseline was keyword search over original documents, not all forms of RAG. On connected questions, reported accuracy rose from 0.10 with search to 0.52 with the wiki; model cost per correct answer fell from approximately $0.55 to $0.19. On simple questions, search and wiki accuracy were 0.84 and 0.83, respectively, and latency increased from 9 to 12 seconds.

For the wiki agent, citation overlap fell from 0.74 on simple questions to 0.25 on connected questions. Citation overlap measures consistency, not correctness. Compared with the wiki alone, adding the graph reportedly improved accuracy by 27%, doubled citation consistency, reduced median answer time by 40%, and reduced model cost per correct answer by 58%. These are source-reported results, not independent replication.

Compilation of 111 documents reportedly cost $4.15; subsequently adding 17 documents cost about $0.09 each. Reported answer costs exclude compilation and updating. The authors describe graph construction as taking under one second for this test library.

## Evidence limitations

This is a vendor-authored experiment on a synthetic corpus, not evidence of production effectiveness or of performance against every retrieval approach. Deterministic edge construction does not verify the correctness of upstream model-generated citations. The experiment and its implementation were not independently reproduced during capture.
