---
title: "CAP Theorem"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/cap-theorem/]
description: "CAP Theorem 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-cap-theorem
source_url: https://lawsofsoftwareengineering.com/laws/cap-theorem/
source_category: Architecture
source_experience: senior
source_updated_at: "June 24, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:3de9fb5d9a6ef88fe588f68138e8f3c40e87d0c2738d6e4700190366a8f32d00
license: CC-BY-NC-ND-4.0
---

# CAP Theorem

A distributed system can guarantee only two of: consistency, availability, and partition tolerance.

## Takeaways

- A distributed system can only guarantee two out of three things at once: Consistency, Availability, and Partition Tolerance. When the network is healthy you can have all three, but the moment a partition happens, you have to give one up.
- When a network split occurs, you face a choice: stay consistent (every node agrees, but some requests may fail) or stay available (every request gets an answer, but the data might be slightly out of date). You can’t fully have both.
- Real databases pick a side. MongoDB leans toward consistency, blocking writes during a partition so all replicas stay in sync. Cassandra leans toward availability, keeping the lights on and serving queries even if replicas briefly disagree.

## Overview

The CAP theorem states that a distributed system cannot simultaneously provide all three guarantees: **Consistency** (all nodes see the same data), **Availability** (every request receives a response), and **Partition Tolerance** (the system operates despite network failures).

Since network partitions are unavoidable in practice, systems must be partition-tolerant. This means choosing between consistency and availability when designing distributed architectures. The CAP theorem is a useful starting point, though it is a simplification that doesn’t cover all aspects of the design space.

## Examples

The **Domain Name System (DNS)** is designed as AP (Available and Partition-tolerant). If some name servers are partitioned, they still reply (availability), even if their information might be slightly outdated until zones sync up.

**MongoDB** is a CP (Consistent and Partition-Tolerant) database, blocking writes during a partition so all replicas stay in sync. **Cassandra** is an AP (Available and Partition-Tolerant) database, serving queries even if replicas briefly disagree.

## Origins

Eric Brewer created the theorem in 2000 in the context of web services, and it was later formalized by Gilbert and Lynch in 2002. Brewer observed that designers of large-scale systems faced three concerns: keeping data consistent across nodes, keeping the service up, and handling network unreliability.

The formal proof showed that in a distributed system with shared data, you **must sacrifice either consistency or availability when a network partition occurs**. CAP became a guiding principle in the NoSQL movement and distributed database design in the 2000s.

## Further Reading

- [Brewer's CAP Theorem Eric Brewer's reflection on CAP, twelve years later](https://www.infoq.com/articles/cap-twelve-years-later-how-the-rules-have-changed/)
- [CAP Twelve Years Later: How the 'Rules' Have Changed Brewer's 2012 IEEE paper revisiting and refining the CAP theorem](https://sites.cs.ucsb.edu/~rich/class/cs293b-cloud/papers/brewer-cap.pdf)
- [Gilbert & Lynch 2002 Paper The formal proof of the CAP theorem](https://groups.csail.mit.edu/tds/papers/Gilbert/Brewer2.pdf)
- [Designing Data-Intensive Applications Martin Kleppmann's comprehensive guide covering CAP and distributed systems](https://amzn.to/4pVAwU5)
- [A Critique of the CAP Theorem Martin Kleppmann's 2015 paper arguing the theorem's definitions are ambiguous](https://www.cl.cam.ac.uk/research/dtg/archived/files/publications/public/mk428/cap-critique.pdf)

## Last updated

June 24, 2026

## Related Laws

- [Fallacies of Distributed Computing](https://lawsofsoftwareengineering.com/laws/fallacies-of-distributed-computing/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/cap-theorem/
- Author/site owner: Dr. Milan Milanović
- Extraction route: deterministic HTML `.content-wrapper` plus source-declared related laws
- Source quality: full detail-page capture of the principal text sections
- License: [CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)
- Limitation: the site characterizes most entries as rules of thumb rather than scientific laws; evidence strength varies by entry.
- Limitation: navigation, promotional book callout, hidden citation widget and decorative images were excluded.
- Redistribution boundary: retained for local, non-commercial research; public or commercial redistribution requires separate license review.

## Relations

- grouped_by: [[software-engineering-laws-architecture]]
- indexed_by: [[software-engineering-laws-decision-map]]
