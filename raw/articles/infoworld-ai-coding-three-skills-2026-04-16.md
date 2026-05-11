---
title: Three skills that matter when AI handles the coding
author: Matthew O’Keefe
source: InfoWorld
source_url: https://www.infoworld.com/article/4159838/three-skills-that-matter-when-ai-handles-the-coding.html
original_url: https://share.google/48vtwnZtpcYvWsGw7
published: 2026-04-16T19:48:44-07:00
captured: 2026-05-11
type: raw-source
tags: [ai-coding, prompt-engineering, software-engineering, verification]
extraction: share.google resolved to canonical InfoWorld article; full article text fetched through Jina Reader.
---

# Three skills that matter when AI handles the coding

Source URL: https://www.infoworld.com/article/4159838/three-skills-that-matter-when-ai-handles-the-coding.html
Original share.google URL: https://share.google/48vtwnZtpcYvWsGw7
Extraction note: share.google resolved to canonical InfoWorld article; full article text fetched through Jina Reader.

Title: Three skills that matter when AI handles the coding

URL Source: https://www.infoworld.com/article/4159838/three-skills-that-matter-when-ai-handles-the-coding.html

Published Time: 2026-04-16T19:48:44-07:00

Markdown Content:
Writing code has always been the most time- and resource-intensive task in software development. [AI is changing that](https://www.infoworld.com/article/4058076/vibe-coding-and-the-future-of-software-development.html), and faster than most engineering organizations are prepared for. Tools like [Claude Code](https://www.infoworld.com/article/4136718/claude-code-is-blowing-me-away.html) and [Cursor](https://www.infoworld.com/article/3540474/two-good-visual-studio-code-alternatives.html) are already handling significant parts of code construction, freeing developers to spend more time on requirements, architecture, and design.

But that shift creates a new challenge nobody is talking about enough. As AI takes on the heavy lifting, the skills that matter most are moving upstream: how to provide the right context for a prompt, how to evaluate what the model produces, and how to understand a problem deeply enough that you can’t be fooled by a confident but wrong answer.

This piece explores those three skills and why developers who master them will have a significant edge over those who don’t.

## Beyond coding: Mastering the art of the prompt

Software translation tools such as [compilers](https://www.infoworld.com/article/2337838/what-is-a-compiler-how-source-code-becomes-machine-code.html) and assemblers map a high-level description of code to a lower-level representation suitable for execution. Layering such tools led to the first dramatic improvements in coding productivity. [AI prompt engineering](https://www.infoworld.com/article/4122440/what-is-prompt-engineering-the-art-of-ai-orchestration.html) represents the next generation of layered translation software that sits above the compiler and assembler. With AI code generation, the focus will move from writing good code to writing good prompts.

What constitutes a good prompt? The answer is good context. But what provides the best context? Most importantly, the developer must have a good understanding of the task the software must perform. Consider what’s required to write a typical software module that is part of a larger system. The prompt should cover:

*   Expected inputs and outputs, like the software’s core functionality
*   Errors and exception conditions and how they should be handled
*   Performance expectations
*   Existing frameworks the software is surrounded by and the programming language used
*   Interface expected by the user
*   Required storage, compute, and network resources.

## How system design informs context

For new initiatives, the context for this module should be taken from a detailed system design. The system design is essentially the blueprint for the software, created by breaking down the overall design into smaller, separate parts called modules. Each of the modules is responsible for performing a specific function that the software needs to deliver. In [microservice](https://www.infoworld.com/article/2263327/what-are-microservices-your-next-software-architecture.html) implementations, domain-driven design breaks the business requirements into distinct subdomains that can be mapped to microservices.

Good system designs have a coherent architecture that provides a concept of operation like how the modules work together to meet the functional requirements. The best system designs result when well-understood requirements are combined with the right architecture.

By working backwards and building the context into a prompt we discovered the most important phases in the development life cycle including requirements analysis (what the software has to do), and architecture and system design (how it does it).

![Image 1: AI and Software Engineering Figure 1](https://b2b-contenthub.com/wp-content/uploads/2026/04/AI-and-Software-Engineering-Figure-1.png)

An example of a linear software life cycle.

Confluent

Although one design pass might work, often developers will need to iterate on their design to get the best outcome. This has been emphasized by many software experts over the years, but perhaps best put by the famous computer scientist Fred Brooks: “Plan to throw one away, you will anyway.”

![Image 2: AI and Software Engineering Figure 2](https://b2b-contenthub.com/wp-content/uploads/2026/04/AI-and-Software-Engineering-Figure-2.png)

An example of an iterative software life cycle.

Confluent

Iterative life cycles like spiral and evolutionary prototyping build the “throw one away” part into the process. Throwing something away sounds wasteful, but each iteration builds a deeper understanding of the problem: user requirements, architecture limitations, risks, and opportunities. Learning from each iteration greatly reduces the cost and complexity of the final product.

## How AI tools can impact developer productivity

AI translation tools have the potential to make us more productive, but also introduce the risk that we will become lazy and dependent on them. A recent [study](https://arxiv.org/abs/2506.08872) found that LLM-assisted essay writing reduced user’s cognitive energy associated with their work relative to those who wrote essays unassisted by LLMs. This effect was termed “cognitive debt.”

I work with a strength trainer because modern life is too easy. It doesn’t require heavy lifting or strenuous activity. So we have to simulate it to improve both our strength and health. AI coding tools are like robots that do the heavy lifting of code generation for us. Without different challenges for us to overcome, we’ll get weaker.

### Modern coding and AI tools

We need to find ways to keep our brains working hard while using AI tools, so that we have the capacity to think through the hard problems in our software design and its development work.

Writing optimized assembly code is no longer considered a good use of anyone’s time because compilers are so good at it. But until recently, writing good code for a compiler or run-time engine in [Java](https://www.infoworld.com/article/2335996/9-reasons-java-is-still-great.html), [Go](https://www.infoworld.com/article/2253031/whats-the-go-language-really-good-for-3.html), or [Python](https://www.infoworld.com/article/2253770/what-is-python-powerful-intuitive-programming.html) has been an important skill. In fact, these skills will remain important even as LLMs support code generation because developers will still need to review the generated code and verify that the LLM output meets certain standards. Experienced developers who have been writing code for years already have these skills. Both new and existing developers will be able to learn and expand their knowledge via interaction with LLM tools that expose them to new techniques and ideas.

We need to find the equivalent of strength training for coding that replaces some coding directly but retains understanding and judgement for the code the LLM produces. Where can we put our brains to work to avoid cognitive debt?

### Avoiding the cognitive debt danger

First, study and understand the code generated from your prompt. Then re-write your prompt to improve the generated code, or rewrite the generated code if it’s close enough to what you need. LLMs behave statistically, so the generated code might not meet design goals. LLM gaslighting is real: quite often what it generates won’t run or isn’t correct, but the LLM will insist confidently that all is well. Don’t trust. Always verify.

LLMs can generate alternative designs from the same or slightly different prompt. Many developers are already leveraging this capability to [explore the design space](https://www.linkedin.com/pulse/build-something-great-explore-space-matthew-o-keefe/?trackingId=2z1DgRJWTxe9uk1LM2BLIQ%3D%3D). Make sure you put the effort into understanding and modifying the code generated, and you’ll retain your coding skills.

Second, the focus of prompt engineering is to provide context to an LLM. So the key becomes creating that context, and understanding and judging the code that is generated. In addition to retaining their existing language and coding skills, software professionals should focus on other life-cycle elements, especially requirements, architecture, and design, so they have high-quality context for prompts.

Third, learn new languages and [data models](https://practicaldatamodeling.substack.com/p/the-era-of-the-mixed-model-artist), and understand where each one fits best.

Fourth, build an understanding of best practices in [code construction](https://www.amazon.com/Code-Complete-Practical-Handbook-Construction/dp/0735619670/ref=sr_1_1?crid=3LP54B6889KN5&dib=eyJ2IjoiMSJ9.uKnS_KWeq01ns81nQdT5TO9nHRn6DsgJ6K2r1cSZ3okGcmdYo2mken_kxibaarsm40T5urSbWQ4gksGE-0FilSFKWx-mbmQcn2n6R0o8CdGSUJQ2oP6sNqOg78sWHS2PnJu_FIJ8aT8dAtyVj7ZKyL7r1uzeNZiTUXDV28peXnkE3rCYkONFoWTWOzuwGuTbETXLnH8LtyOo-8WfOX6wXGv0mqClDZN6B53CJUJtvwU.21VMmd3-_aawglEHrReOvgpBHwSg7lPKg2uqGVPQUSw&dib_tag=se&keywords=code+complete&qid=1773060686&sprefix=code+complet%2Caps%2C157&sr=8-1) and [design](https://www.amazon.com/Philosophy-Software-Design-2nd/dp/173210221X/ref=sr_1_1?crid=1SBD2MIC7M4LG&dib=eyJ2IjoiMSJ9.tLS48uuwITT-xp5LTBc638LcMFzFtBKLlWZNIIDL_JA.sktetXGKewtR4IeHQxuOCJHG33NVdfgyEpY6WZ8C2Ow&dib_tag=se&keywords=ousterhout+a+philosophy+of+software+design&qid=1773060717&sprefix=ousterhout+desig%2Caps%2C155&sr=8-1), independent of languages, so you can judge generated code using best practices that work across many different languages.

To stay competitive, you should understand that the bar will be rising. Historically, [research](https://www.amazon.com/Rapid-Development-Taming-Software-Schedules/dp/1556159005/ref=sr_1_1?crid=2FJCO2BNWO7ZT&dib=eyJ2IjoiMSJ9.Vp09eBE0_5-tPrX1kWpRojamys-G_pe5601QYmEXoQ8ynuqYpdWlk0KwCrgINWsqQuA-UD-95llTgHHL93-vlg.W2ULx51sU-fD8gviZxVUcMBmtDB03TG4cGMCjDJZAgo&dib_tag=se&keywords=rapid+development+by+steve+mcconnell&qid=1773073146&sprefix=rapid+development+%2Caps%2C189&sr=8-1) has shown that the most productive individual developers are already about 10 times more effective than the least productive ones, and the best teams are about five times better than the weakest teams.AI tools could increase these differences by two or three times more, further widening the productivity gap. Many of these highly productive teams will work for your competitors.

AI will allow developers and teams that can crystallize requirements, architecture, and design to rapidly apply and evaluate different languages and data models to their project. AI will make iterative life cycles like spiral and evolutionary prototyping even more effective by allowing parallel development paths during each iteration. The key to success is leveraging AI in a way that allows you to focus on higher-level design issues while not losing control over code complexity. If you don’t learn these higher-level skills, developers and teams that do will be far more productive than you are.

![Image 3: AI and Software Engineering Figure 3](https://b2b-contenthub.com/wp-content/uploads/2026/04/AI-and-Software-Engineering-Figure-3.png)

Iterative life cycle with parallel paths and feedback loops.

Confluent

## Accidental vs. essential complexity – why AI cannot be a silver bullet

Some have argued that AI will significantly improve software productivity. They envision a future in which software developers need only write a few prompts and an LLM will produce software that can replace existing SaaS products. But as Fred Brooks argued in a famous 1986 paper, “[No Silver Bullet](https://www.cs.unc.edu/techreports/86-020.pdf),” this is still impossible because of the two types of complexity that remain—accidental complexity and essential complexity.

### Accidental complexity (or ‘accidents’)

Accidents are not inherent to the problem itself, but to the production process including the tools, languages, hardware limits, and implementation details we use to build the software. Historically, most productivity gains come from reducing accidental complexity. AI productivity can reduce accidental complexity, but developers must deal with its own challenges including hallucinations and poor-quality generated code that must be detected.

### Essential complexity (or ‘essence’)

Essence refers to the inherent, unavoidable complexity of the problem itself. It is the challenge of “fashioning the complex conceptual construct” such as the abstract, interlocking ideas, data relationships, algorithms, and behaviors that accurately model the real-world problem the software must solve.

AI cannot be a silver bullet because of software’s inherent complexity. Even if you could reduce the time for all the accidental tasks to zero, the essential tasks still will be your biggest challenge and take up most of your efforts. Nevertheless, AI is a powerful tool. When used properly to manage complexity and explore the design space, it can significantly increase the productivity of teams and the quality of the software developed.

_—_

[**_New Tech Forum_**](https://www.infoworld.com/blogs/new-tech-forum)_**provides a venue for technology leaders—including vendors and other outside contributors—to explore and discuss emerging enterprise technology in unprecedented depth and breadth. The selection is subjective, based on our pick of the technologies we believe to be important and of greatest interest to InfoWorld readers. InfoWorld does not accept marketing collateral for publication and reserves the right to edit all contributed content. Send all**_ _**inquiries to**_[**_doug\_dineley@foundryco.com_**](mailto:doug_dineley@foundryco.com)_**.**_

