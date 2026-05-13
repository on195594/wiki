---
title: How to Make Claude Code Validate its own Work
author: Eivind Kjosbakken
source_type: article
source_url: https://towardsdatascience.com/how-to-make-claude-code-validate-its-own-work/
publisher: Towards Data Science
published_at: 2026-05-05T15:00:00+00:00
captured_at: 2026-05-06 11:09:06 +0800
status: raw
tags: [claude-code, ai-coding, validation, verification, workflow, mcp, browser]
summary_path: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260513-133845-How-to-Make-Claude-Code-Validate-its-own-Work-Towards-Data-Science-389451-994746960-summary.md
---

# How to Make Claude Code Validate its own Work

## Source note
This raw page captures the reusable engineering pattern from Eivind Kjosbakken's Towards Data Science article about improving Claude Code by giving it validation tools and explicit expected outputs. The article was fetched from the canonical Towards Data Science URL through Jina Reader Markdown, then cookie/navigation boilerplate was trimmed before Gemini summarization.

## Core claim
Claude Code and similar coding agents perform better when they are allowed to validate their own work: run code, compare against expected output, inspect browser/UI results, iterate on failures, and report unresolved discrepancies instead of returning unverified code.

## Key points
- Treat agent coding as a feedback loop, not a one-shot prompt exercise.
- For backend/data-processing refactors, provide a known input and expected output from the old path, then require the agent to compare the new implementation against that baseline.
- For visual frontend tasks, give the agent browser/screenshot access so it can compare the rendered page with the target design.
- Validation does not need to require byte-for-byte equality when LLM outputs are stochastic; define an acceptable equivalence threshold.
- Agents should stop and report ambiguity or impossible discrepancies instead of guessing indefinitely.

## Hermes/LifeOS relevance
- Reinforces Hermes' existing rule: do not declare work complete without tool-backed verification.
- Turns browser/MCP/tool access into a quality gate, not a novelty feature.
- Supports future AI coding workflows where prompts include expected outputs, test commands, screenshots, or comparison scripts as first-class acceptance criteria.
- Complements [[claude-code-practical-workflow-tips]], [[agentic-content-pipeline-design-patterns]], and [[hermes-ai-workflow-formalization-principles]].

## Limitations
- The article is experience-based rather than a controlled benchmark.
- Chrome MCP and visual comparison loops may require non-trivial setup and can still misjudge design differences.
- Self-validation reduces uncertainty but does not remove the need for human review on ambiguous product/design decisions, permissions, rollback, or business correctness.

## Gemini summary

标题：How to Make Claude Code Validate its own Work
Source URL: https://towardsdatascience.com/how-to-make-claude-code-validate-its-own-work/

一句话结论：
通过为 Claude Code 设定预期基准或提供工具（如Chrome MCP），让其在输出代码后自主运行、比对并迭代修改，可以显著提升其一次性生成正确代码（one-shotting）的能力和处理复杂任务的成功率。

核心观点与论证：
- 观点：不给予测试权限会严重限制 Claude Code 的代码生成质量。
  依据/论证：作者使用斐波那契数列进行类比——要求程序员盲写完美代码且不准运行查看结果是极其困难的。同理，Claude Code 需要“测试-调整-再测试”的反馈循环来输出优质代码。
- 观点：后端逻辑重构任务可以通过设定“预期输出基准”来实现自我验证。
  依据/论证：案例中，作者需要解决一个长文本处理耗时过长（超2分钟）的问题。方案是将一个重度LLM API调用拆分为三个并行调用。作者将拆分前的输出作为“正确基准”，要求 Claude 自动运行其重构的代码，并比对新架构的输出与基准是否一致（考虑到LLM的随机性，只要求几乎一致），从而闭环完成任务。
- 观点：前端UI还原任务可通过赋予视觉能力（浏览器MCP）来实现自我验证。
  依据/论证：在将设计图转化为网页时，作者为 Claude 配置了 Chrome MCP。Claude 被指示完成初步编码后，启动本地服务器，在 Chrome 中加载页面并截图，将其与原始设计图进行视觉比对。若存在差异，Claude 会自动迭代代码直到视觉效果高度吻合。

关键细节：
- 性能瓶颈的具体触发频率与耗时：在处理对话AI用户数据（获取文字记录、分类、提取）时，由于Token过多，大约每 10 次调用就有 1 次耗时从均值 30 秒飙升至 2 分钟以上。
- 后端验证的容错性考量：作者明确指出，由于 LLM 具有随机性（stochastic），在对比重构前后的API输出时，Claude 只需要验证结果“几乎完全相同（almost exactly the same）”即可，而非绝对相符。
- 前端验证的具体工具栈：依赖“Claude in Chrome (an MCP)”，这使得大模型具备了操作浏览器和获取视觉反馈的能力。
- 兜底沟通策略：作者在 UI 还原任务中专门向 Agent 设定了指令——如果发现设计无法实现或有不清晰的地方，必须主动报告差异并提问，而不是擅自做主。

可信度与局限：
- 证据强度：中等。文章基于作者在后端优化和前端还原两个真实开发场景下的个人实践经验，逻辑自洽，提供了一套可复现的方法论。
- 局限性（推演与主观）：文章缺乏量化数据来支撑“vastly improve（巨大提升）”的具体比例；此外，基于 Chrome MCP 的自动化 UI 比对和测试可能对环境配置和模型响应速度有较高门槛，作者将其描述得相对轻松，弱化了工程落地时可能遇到的错误循环或幻觉死锁问题。

对我的启发：
- 改变使用编码 Agent 的范式：从“尝试编写完美的 Prompt 一次性得到正确代码”，转变为“编写基础 Prompt + 提供基准答案/测试工具”，将 debug 的工作流也交给大模型自己闭环。

可执行建议：
- 在让 AI 重构复杂数据处理逻辑时，务必提供一份重构前的输入输出样本作为 Ground Truth，并在指令中硬性要求 AI：“请自行编写测试脚本比对新旧逻辑输出，不一致则重新修改，直到通过再返回最终代码”。
- 探索和配置 Model Context Protocol (MCP) 相关插件（如 Chrome MCP），在前端开发任务中引入视觉截图比对环节。
- 在给 Agent 的系统提示词中加入主动降级指令：“如果在执行验证循环时遇到无法获取的数据或有歧义的设计，停止重试，直接向我提问”。

## Extracted article text

Source URL: https://towardsdatascience.com/how-to-make-claude-code-validate-its-own-work/
Extraction: Jina Reader Markdown from canonical Towards Data Science URL; cookie/navigation boilerplate trimmed.

# How to Make Claude Code Validate its own Work | Towards Data Science

![Image 11: Revisit consent button](https://cdn-cookieyes.com/assets/images/revisit.svg)

We value your privacy

We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic. By clicking "Accept All", you consent to our use of cookies.

Customise Reject All Accept All

Customise Consent Preferences![Image 12](https://cdn-cookieyes.com/assets/images/close.svg)

We use cookies to help you navigate efficiently and perform certain functions. You will find detailed information about all cookies under each consent category below.

The cookies that are categorised as "Necessary" are stored on your browser as they are essential for enabling the basic functionalities of the site. ...Show more

Necessary Always Active

Necessary cookies are required to enable the basic features of this site, such as providing secure log-in or adjusting your consent preferences. These cookies do not store any personally identifiable data.

*   Cookie BCTempID 
*   Duration 10 minutes 
*   Description No description available. 

*   Cookie __cf_bm 
*   Duration 1 hour 
*   Description This cookie, set by Cloudflare, is used to support Cloudflare Bot Management.  

*   Cookie AWSALBCORS 
*   Duration 7 days 
*   Description Amazon Web Services set this cookie for load balancing. 

*   Cookie _cfuvid 
*   Duration session 
*   Description Cloudflare sets this cookie to track users across sessions to optimize user experience by maintaining session consistency and providing personalized services 

*   Cookie li_gc 
*   Duration 6 months 
*   Description Linkedin set this cookie for storing visitor's consent regarding using cookies for non-essential purposes. 

*   Cookie __hssrc 
*   Duration session 
*   Description This cookie is set by Hubspot whenever it changes the session cookie. The __hssrc cookie set to 1 indicates that the user has restarted the browser, and if the cookie does not exist, it is assumed to be a new session. 

*   Cookie __hssc 
*   Duration 1 hour 
*   Description HubSpot sets this cookie to keep track of sessions and to determine if HubSpot should increment the session number and timestamps in the __hstc cookie. 

*   Cookie wpEmojiSettingsSupports 
*   Duration session 
*   Description WordPress sets this cookie when a user interacts with emojis on a WordPress site. It helps determine if the user's browser can display emojis properly. 

*   Cookie BCSessionID 
*   Duration 1 year 1 month 4 days 
*   Description Blueconic sets this cookie as a unique identifier for the BlueConic profile. 

*   Cookie _octo 
*   Duration 1 year 
*   Description No description available. 

*   Cookie logged_in 
*   Duration 1 year 
*   Description No description available. 

*   Cookie __Secure-YEC 
*   Duration past 
*   Description YouTube sets this cookie to stores the user's video player preferences using embedded YouTube video 

*   Cookie __eoi 
*   Duration 6 months 
*   Description Description is currently not available. 

*   Cookie AWSALBTGCORS 
*   Duration 7 days 
*   Description No description available. 

*   Cookie login-status-p 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie AWSALBTG 
*   Duration 7 days 
*   Description No description available. 

*   Cookie csrf_token 
*   Duration session 
*   Description No description available. 

*   Cookie token_v2 
*   Duration 1 day 
*   Description Description is currently not available. 

*   Cookie D 
*   Duration 1 year 
*   Description Description is currently not available. 

*   Cookie PHPSESSID 
*   Duration session 
*   Description This cookie is native to PHP applications. The cookie stores and identifies a user's unique session ID to manage user sessions on the website. The cookie is a session cookie and will be deleted when all the browser windows are closed. 

*   Cookie VISITOR_PRIVACY_METADATA 
*   Duration 6 months 
*   Description YouTube sets this cookie to store the user's cookie consent state for the current domain.  

*   Cookie cookietest 
*   Duration session 
*   Description The cookietest cookie is typically used to determine whether the user's browser accepts cookies, essential for website functionality and user experience. 

*   Cookie __Host-airtable-session 
*   Duration 1 year 
*   Description This cookie is used to enable us to integrate the services of Airtable. 

*   Cookie __Host-airtable-session.sig 
*   Duration 1 year 
*   Description This cookie is used to enable us to integrate the services of Airtable. 

*   Cookie m 
*   Duration 1 year 1 month 4 days 
*   Description Stripe sets this cookie for fraud prevention purposes. It identifies the device used to access the website, allowing the website to be formatted accordingly. 

*   Cookie BIGipServer* 
*   Duration session 
*   Description Marketo sets this cookie to collect information about the user's online activity and build a profile about their interests to provide advertisements relevant to the user.  

*   Cookie __cfruid 
*   Duration session 
*   Description Cloudflare sets this cookie to identify trusted web traffic. 

*   Cookie _GRECAPTCHA 
*   Duration 6 months 
*   Description Google Recaptcha service sets this cookie to identify bots to protect the website against malicious spam attacks. 

*   Cookie __Secure-YNID 
*   Duration 6 months 
*   Description Google cookie used to protect user security and prevent fraud, especially during the login process. 

*   Cookie cookieyes-consent 
*   Duration 1 year 
*   Description CookieYes sets this cookie to remember users' consent preferences so that their preferences are respected on subsequent visits to this site. It does not collect or store any personal information about the site visitors. 

Functional

- [x] 

Functional cookies help perform certain functionalities like sharing the content of the website on social media platforms, collecting feedback, and other third-party features.

*   Cookie lidc 
*   Duration 1 day 
*   Description LinkedIn sets the lidc cookie to facilitate data center selection. 

*   Cookie brw 
*   Duration 1 year 
*   Description No description available. 

*   Cookie brwConsent 
*   Duration 5 minutes 
*   Description Description is currently not available. 

*   Cookie WMF-Uniq 
*   Duration 1 year 
*   Description Description is currently not available. 

*   Cookie loom_anon_comment 
*   Duration 1 year 
*   Description No description available. 

*   Cookie loom_referral_video 
*   Duration session 
*   Description Description is currently not available. 

*   Cookie VISITOR_INFO1_LIVE 
*   Duration 6 months 
*   Description A cookie set by YouTube to measure bandwidth that determines whether the user gets the new or old player interface. 

*   Cookie yt-remote-connected-devices 
*   Duration Never Expires 
*   Description YouTube sets this cookie to store the user's video preferences using embedded YouTube videos. 

*   Cookie ytidb::LAST_RESULT_ENTRY_KEY 
*   Duration Never Expires 
*   Description The cookie ytidb::LAST_RESULT_ENTRY_KEY is used by YouTube to store the last search result entry that was clicked by the user. This information is used to improve the user experience by providing more relevant search results in the future. 

*   Cookie yt-remote-device-id 
*   Duration Never Expires 
*   Description YouTube sets this cookie to store the user's video preferences using embedded YouTube videos. 

*   Cookie yt-remote-session-name 
*   Duration session 
*   Description The yt-remote-session-name cookie is used by YouTube to store the user's video player preferences using embedded YouTube video. 

*   Cookie yt-remote-fast-check-period 
*   Duration session 
*   Description The yt-remote-fast-check-period cookie is used by YouTube to store the user's video player preferences for embedded YouTube videos. 

*   Cookie yt-remote-session-app 
*   Duration session 
*   Description The yt-remote-session-app cookie is used by YouTube to store user preferences and information about the interface of the embedded YouTube video player. 

*   Cookie yt-remote-cast-available 
*   Duration session 
*   Description The yt-remote-cast-available cookie is used to store the user's preferences regarding whether casting is available on their YouTube video player. 

*   Cookie yt-remote-cast-installed 
*   Duration session 
*   Description The yt-remote-cast-installed cookie is used to store the user's video player preferences using embedded YouTube video. 

*   Cookie cp_session 
*   Duration 3 months 
*   Description Codepen sets this cookie for Help systems found in the website. 

*   Cookie loid 
*   Duration 1 year 1 month 4 days 
*   Description This cookie is set by the Reddit. The cookie enables the sharing of content from the website onto the social media platform. 

Analytics

- [x] 

Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics such as the number of visitors, bounce rate, traffic source, etc.

*   Cookie __hstc 
*   Duration 6 months 
*   Description Hubspot set this main cookie for tracking visitors. It contains the domain, initial timestamp (first visit), last timestamp (last visit), current timestamp (this visit), and session number (increments for each subsequent session). 

*   Cookie hubspotutk 
*   Duration 6 months 
*   Description HubSpot sets this cookie to keep track of the visitors to the website. This cookie is passed to HubSpot on form submission and used when deduplicating contacts. 

*   Cookie _ga 
*   Duration 1 year 1 month 4 days 
*   Description Google Analytics sets this cookie to calculate visitor, session and campaign data and track site usage for the site's analytics report. The cookie stores information anonymously and assigns a randomly generated number to recognise unique visitors. 

*   Cookie _ga_* 
*   Duration 1 year 1 month 4 days 
*   Description Google Analytics sets this cookie to store and count page views. 

*   Cookie __Host-psifi.analyticsTrace 
*   Duration 6 hours 
*   Description Description is currently not available. 

*   Cookie __Host-psifi.analyticsTraceV2 
*   Duration 6 hours 
*   Description Description is currently not available. 

*   Cookie _gh_sess 
*   Duration session 
*   Description GitHub sets this cookie for temporary application and framework state between pages like what step the user is on in a multiple step form. 

*   Cookie YSC 
*   Duration session 
*   Description YSC cookie is set by Youtube and is used to track the views of embedded videos on Youtube pages. 

*   Cookie ajs_anonymous_id 
*   Duration 1 year 
*   Description This cookie is set by Segment to count the number of people who visit a certain site by tracking if they have visited before. 

*   Cookie vuid 
*   Duration 1 year 1 month 4 days 
*   Description Vimeo installs this cookie to collect tracking information by setting a unique ID to embed videos on the website.  

Performance

- [x] 

Performance cookies are used to understand and analyse the key performance indexes of the website which helps in delivering a better user experience for the visitors.

*   Cookie AWSALB 
*   Duration 7 days 
*   Description AWSALB is an application load balancer cookie set by Amazon Web Services to map the session to the target. 

*   Cookie acq 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie acq.sig 
*   Duration past 
*   Description Description is currently not available. 

*   Cookie ptc 
*   Duration 2 years 
*   Description No description available. 

Advertisement

- [x] 

Advertisement cookies are used to provide visitors with customised advertisements based on the pages you visited previously and to analyse the effectiveness of the ad campaigns.

*   Cookie muc_ads 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to collect user behaviour and interaction data to optimize the website. 

*   Cookie guest_id_marketing 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. 

*   Cookie guest_id_ads 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. 

*   Cookie personalization_id 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to integrate and share features for social media and also store information about how the user uses the website, for tracking and targeting. 

*   Cookie guest_id 
*   Duration 1 year 1 month 4 days 
*   Description Twitter sets this cookie to identify and track the website visitor. It registers if a user is signed in to the Twitter platform and collects information about ad preferences. 

*   Cookie bcookie 
*   Duration 1 year 
*   Description LinkedIn sets this cookie from LinkedIn share buttons and ad tags to recognize browser IDs. 

*   Cookie __Secure-ROLLOUT_TOKEN 
*   Duration 6 months 
*   Description YouTube sets this cookie to manage feature rollout and experimentation. It helps Google control which new features or interface changes are shown to users as part of testing and staged rollouts, ensuring consistent experience for a given user during an experiment. 

*   Cookie yt.innertube::nextId 
*   Duration Never Expires 
*   Description YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen. 

*   Cookie yt.innertube::requests 
*   Duration Never Expires 
*   Description YouTube sets this cookie to register a unique ID to store data on what videos from YouTube the user has seen. 

*   Cookie session_tracker 
*   Duration session 
*   Description This cookie is set by the Reddit. This cookie is used to identify trusted web traffic. It also helps in adverstising on the website. 

*   Cookie edgebucket 
*   Duration session 
*   Description Reddit sets this cookie to save the information about a log-on Reddit user, for the purpose of advertisement recommendations and updating the content. 

*   Cookie did 
*   Duration 1 year 
*   Description Arbor sets this cookie to show targeted ads to site visitors.This cookie expires after 2 months or 1 year. 

Uncategorised

Other uncategorised cookies are those that are being analysed and have not been classified into a category as yet.

No cookies to display.

Reject All Save My Preferences Accept All

[Skip to content](http://towardsdatascience.com/how-to-make-claude-code-validate-its-own-work/#wp--skip-link--target)

[![Image 13: Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)

Publish AI, ML & data-science insights to a global community of data professionals.

[Sign in](http://towardsdatascience.com/how-to-make-claude-code-validate-its-own-work/)

[Submit an Article](https://contributor.insightmediagroup.io/)

*   [Latest](https://towardsdatascience.com/latest/)
*   [Editor’s Picks](https://towardsdatascience.com/tag/editors-pick/)
*   [Deep Dives](https://towardsdatascience.com/tag/deep-dives/)
*   [Newsletter](http://towardsdatascience.com/tag/the-variable/)

* * *

*   [Write For TDS](https://towardsdatascience.com/submissions/)

[![Image 14: Towards Data Science](https://towardsdatascience.com/wp-content/uploads/2025/02/TDS-Vector-Logo.svg)](https://towardsdatascience.com/)

Toggle Mobile Navigation

*   [LinkedIn](https://www.linkedin.com/company/towards-data-science/?originalSubdomain=ca)
*   [X](https://x.com/TDataScience)

Toggle Search

Search 

[LLM Applications](https://towardsdatascience.com/category/artificial-intelligence/llm-applications/)

# How to Make Claude Code Validate its own Work

Improve Claude Code performance by having it validate its own work

[Eivind Kjosbakken](https://towardsdatascience.com/author/oieivind/)

May 5, 2026

 8 min read

 Share 

![Image 15](https://towardsdatascience.com/wp-content/uploads/2026/05/image-9-1.jpg)

In this article, I’ll cover how you can make Claude Code verify its own work to vastly improve Claude Code performance. Image by ChatGPT.

Claude Code is a very powerful model out of the box. To leverage its full capabilities, however, you need to give it access to validate and verify its own work.

In a previous article, I mentioned Claude validating its own work as an important part of how I optimize my own use of Claude Code. In this article, however, I’ll dive deeper into how I make Claude validate its own work.

The benefits are incredible. When you make Claude validate its own work, you get:

*   A model better at one-shotting implementations (spends less time iterating)
*   A model that can run for longer (the model keeps going until it’s successfully able to verify its own work)
*   The model can complete more complex work

I’ll dive deeper into some specific tasks where I ask Claude to verify its own work, where I save a lot of time. I’ll also cover my thought process when setting up Claude in this way.

![Image 16: Vastly improve Claude Code performance](https://contributor.insightmediagroup.io/wp-content/uploads/2026/05/image-11-1024x683.png)

In this article I’ll discuss how to let Claude code verify its own work to increase performance. Image by ChatGPT.

## Why should you have Claude verify its own work?

The number one reason you should make Claude verify its own work is that it simply makes Claude perform better. You can imagine this with the following scenario:

Imagine you had to implement a piece of code to calculate the Fibonacci sequence. Obviously, some people have done this exact task before, and it’s going to be relatively simple for them to do. However, imagine that you have to complete this task perfectly without ever getting the opportunity to run the code and see the output, i.e., you have to create the perfect code on your first attempt at the problem. So, naturally, this is way harder than if you get the opportunity to test the code yourself, tweak it if you see it’s not producing the exact correct numbers, and continue like that until your piece of code is producing the correct output.

The same exact concept applies to Claude Code. If you don’t give it the chance to verify its own work, it’s like asking it to write code for the Fibonacci sequence without letting it ever see the output of the code. Obviously, you’re putting Claude Code in a worse position where it’s going to produce inferior results compared to when Claude Code gets the opportunity to test its own code.

## How to make Claude verify work in practice

The wording “make Claude verify its own work”, often gets thrown around, for example on LinkedIn and X. However, I notice relatively few people explaining exactly how they do it themselves, which makes it hard for others to replicate.

Thus, I’ll cover some real-world examples of how I made Claude verify its own work. I’ll cover the process from:

1.   Hearing about a problem
2.   Understanding what’s causing the problem
3.   Implementing a solution with Claude and ensuring it can verify its own work

### Long LLM processing times

My first concrete example is a case where I was analyzing user data from an interaction with a conversational AI agent. After the conversation, I have to process the chat, such as fetching the transcript and performing classification and data extraction on the transcript.

I started investigating the problem by reproducing it and running the LLM processing on the same conversation multiple times, and seeing how long it took. It turned out that the median and average time were relatively acceptable, around 30 seconds, but around every tenth time, processing time would be over two minutes, which is, of course, completely unacceptable. I explained the situation to Claude Code and asked him what could be causing this issue.

The most likely cause, it turned out, was that I was simply inputting a lot of tokens and outputting a lot of tokens, which in some situations take a lot of time to produce. Thus, the solution was to take this one single LLM call and split it into three to make the number of output tokens it had to produce fewer, so that it can run in parallel.

This is an example of a perfect task where Claude Code can verify its own work:

> A perfect task to verify your own work is a task where you have a known expected output you want to produce and you can keep working and iterating on the problem until you reach that exact output.

This is great because what I have now is a number of input tokens that are run, and an expected output, which is what I expect if I do everything in one LLM call. And I can simply ask Claude Code to split a LLM call into three pieces and to make sure that you’ve done it correctly, compare the result from the split LLM calls versus the single monolithic LLM call, they are almost exactly the same (not exactly the same because LLMs are stochastic)

I prompted my Claude Code instance with all this information. It kept iterating on its code until it ensured the outputs were the same, and it successfully one-shot the problem, coming back to me with a successful solution.

### Designing a web page

The last example I provided was great because it’s very simple for the LLM or Claude Code to verify the results. It can simply perform an API call, compare outputs, and see if it’s correct.

However, what happens when the output you want to produce is a visual?

My second example includes a problem where I received a design for what a web page should look like, and I wanted Claude Code to produce that exact design. Of course, given the framework of the application and the existing codebase it was written for.

This might sound like a harder task because it involves visually looking at results. Luckily, we have Claude in Chrome, which is an MCP where you can give Claude access to your Google Chrome and let it visually inspect results.

So I was provided with a screenshot of a design of what the page should look like, including how the page was organized into different components and the coloring scheme used in the design.

This task is pretty straightforward. I simply gave Claude Code screenshots and asked him to implement the design. If your design is quite simple, this might just work out of the box. However, some more complex designs are harder to one-shot, especially if you’re doing it in an existing large codebase that has a lot of dependencies and design protocols.

Thus, to give Claude Code the best chance at one-shotting the problem itself, I gave it access to Google Chrome. If you want to set this up yourself, you can simply ask your Claude Code instance, _how do I give you access to Google Chrome?_

I instructed my Claude agent to first attempt implementing the design, then go into Google Chrome, load the relevant page after spinning up the servers, of course, taking a screenshot and comparing the designs. If it saw any discrepancies, it should continue iterating until the designs look almost the same.

* * *

Furthermore, I asked my agent to inform me of any discrepancies between the two designs if it was not possible to implement something or if it was unclear how to implement something. This is a great tactic because it makes Claude come to you with questions instead of you having to instruct Claude on absolutely everything regarding the design. Overall, this is a great technique to work better with your coding agents.

## Conclusion

In this article, I covered how to make Claude Code validate its own work, to vastly improve the performance of your Claude Code instance or coding agent in general. I discussed why it’s so important to highlight how allowing Claude to verify its own work simply makes it perform a lot better with a higher success rate on one-shot implementations, and letting the agent work for longer periods of time, and still successfully completing tasks. I covered two specific situations I was put in where I gave Claude Code access to verify its own work, including splitting an LLM call into three separate calls to improve latency and following the designs made for a web page and implementing it into my application. Both of these are specific situations that I’ve been put in where I’ve successfully allowed Claude to verify its own work and increase its performance.
