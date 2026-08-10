---
title: "Law of Demeter"
created: 2026-08-10
updated: 2026-08-10
type: raw-source
status: captured
tags: [research, architecture]
sources: [docs:https://lawsofsoftwareengineering.com/laws/law-of-demeter/]
description: "Law of Demeter 详情页的本地来源捕获，供软件工程经验法则检索与校准。"
aliases: []
source_id: lse-law-of-demeter
source_url: https://lawsofsoftwareengineering.com/laws/law-of-demeter/
source_category: Design
source_experience: mid
source_updated_at: "July 20, 2026"
extracted_at: 2026-08-10T16:00:08Z
source_hash: sha256:a76a7051a29e128b1a0189b293f5217b04ecd7a0dc10b2009a7dd30053854dd0
license: CC-BY-NC-ND-4.0
---

# Law of Demeter

An object should only interact with its immediate friends, not strangers.

## Takeaways

- An object should only call methods of: itself, its direct components, its function parameters, or objects it creates. It should not navigate through one object to reach another (‘don’t talk to strangers’).
- If object A only calls B (its immediate friend) and doesn’t reach into B’s internals (like C), then changes to C or removal of C don’t affect A. Each class knows as little as possible about others, reducing the impact of changes
- It often leads to adding wrapper methods or delegations. While that might increase the number of methods, it results in cleaner interactions.

## Overview

The Law of Demeter, also known as “don’t talk to strangers” or the “principle of least knowledge,” was formulated to minimize the knowledge that any given object has about the overall system structure.

In practice, if object A has a reference to object B, and B has a reference to C, A should not call methods on C through B (like `a.b.getC().doSomething()`). A can talk to B, and B can talk to C, but A shouldn’t directly get involved with C.

This fosters loose coupling. If you break LoD, your code assumes the structure extends beyond its immediate neighbors. For example, if `OrderProcessor` does `order.getCustomer().getAddress().getZipCode()`, it knows that an Order has a Customer with an Address. If Customer is changed to have multiple addresses, OrderProcessor breaks. If instead Order had a method `getShippingZip()` that internally navigates its customer/address, OrderProcessor could call that and be oblivious to structural changes.

LoD aligns with information hiding: each object hides its internals and only exposes necessary interfaces.

## Examples

Consider a `Presenter` object with a reference to a UI View containing a `TextField`. Without LoD, the presenter might do `view.getTextField().setText("Hello")`. LoD encourages View to provide `setUserMessage(String)`, internally calling `textField.setText`. The Presenter doesn’t need to know there’s a TextField specifically. If later the View uses a Label instead, the Presenter code doesn’t change.

You can identify violations by counting dots: `a.getB().getC().doSomething()` has two dots, one too many. A single dot `a.doSomething()` or at most `a.getB().doSomething()` is preferable.

By adhering to LoD, each component remains more self-contained, and systems become a network of “friends” rather than a tangle of strangers reaching through each other.

## Origins

The Law of Demeter was first described around 1987 by Ian Holland and colleagues at Northeastern University as part of the Demeter Project on adaptive and aspect-oriented software development. It’s named after the project, which itself was named after the Greek goddess of agriculture, signifying a “growing” approach to software.

The researchers, including Karl Lieberherr, sought ways to make software more maintainable and developed this style rule. They summarized it with the motto “Only talk to your friends.”

## Further Reading

- [Object-Oriented Programming: An Objective Sense of Style Original paper by Lieberherr, Holland, and Riel](https://www2.ccs.neu.edu/research/demeter/papers/law-of-demeter/oopsla88-law-of-demeter.pdf)
- [Law of Demeter - Wikipedia Overview of the principle with examples](https://en.wikipedia.org/wiki/Law_of_Demeter)
- [The Paperboy, The Wallet, and The Law Of Demeter Introduction paper by David Bock with the famous Paperboy example](https://www2.ccs.neu.edu/research/demeter/demeter-method/LawOfDemeter/paper-boy/demeter.pdf)
- [Design Patterns: Elements of Reusable Object-Oriented Software The Gang of Four book with patterns that enforce loose coupling](https://amzn.to/3LnM5o6)

## Last updated

July 20, 2026

## Related Laws

- [SOLID Principles](https://lawsofsoftwareengineering.com/laws/solid-principles/)
- [The Law of Leaky Abstractions](https://lawsofsoftwareengineering.com/laws/law-of-leaky-abstractions/)
- [Hyrum's Law](https://lawsofsoftwareengineering.com/laws/hyrums-law/)
- [KISS (Keep It Simple, Stupid)](https://lawsofsoftwareengineering.com/laws/kiss-principle/)

## Capture metadata

- Source site: [Laws of Software Engineering](https://lawsofsoftwareengineering.com/)
- Canonical URL: https://lawsofsoftwareengineering.com/laws/law-of-demeter/
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
