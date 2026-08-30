---
title: Use Claude for SEO. Don’t let Claude do SEO.
author: Will Scott
edited_by: Angel Niñofranco
reviewed_by: Danny Goodwin
source: Search Engine Land
source_url: https://searchengineland.com/use-claude-for-seo-dont-let-claude-do-seo-485931
published: 2026-08-28
captured: 2026-08-30
type: raw-source
status: captured
extraction: "Karakeep full captured article content; wrapper removed 0 boilerplate lines and 1 duplicate line; local summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260830-123431-Use-Claude-for-SEO.-Don’t-let-Claude-do-SEO-1310046-923374800-summary.md"
---

# Use Claude for SEO. Don’t let Claude do SEO.

## Provenance

- Publisher: Search Engine Land
- Author: Will Scott
- Edited by: Angel Niñofranco
- Reviewed by: Danny Goodwin
- Published: 2026-08-28 10:00
- Source URL: https://searchengineland.com/use-claude-for-seo-dont-let-claude-do-seo-485931
- Extraction route: Karakeep captured article content reused by `/gsummary`
- Source quality: full captured article text
- Limitation: practitioner article with two author-reported Claude incidents; the cited GSC figures and broader prevalence were not independently reproduced for this ingestion. The capture retains some inline promotion and related-link text from the publisher page.

## Captured article text

Claude is one of the best research assistants an SEO can have. Give it a keyword, and it can map intent, spot content gaps, and draft outlines in minutes. But give it write access to your site, and it can take the fastest path to a plausible-looking answer.

I’ve learned to keep a human between AI and any live page. Claude is genuinely useful for SEO research, analysis, and drafting, but it can be quietly wrong when it’s left to execute on its own.

AI can process information and produce recommendations quickly. SEO execution requires judgment about whether those recommendations are actually right for a specific site, page, and search intent. Keep AI in the research and drafting seat, and keep a human responsible for what goes live.

What Claude is actually good at in SEO work

Claude is helpful in the research and analysis phase of SEO, before anything touches a live page. Ask it to cluster a list of keywords by intent, summarize what the top-ranking pages for a query have in common, or draft a first-pass content outline, and it’s fast and useful.

It reads a page and tells you what’s thin.

It reads a competitor’s article and tells you what angle it’s missing.

It turns a messy spreadsheet of search terms into a structured content plan in a few minutes of back-and-forth.

That’s real value, and it shows in the adoption numbers. In Keyword.com’s State of AI in SEO 2026 survey (97 usable responses, skewed toward lean teams and service providers), 87% said they use AI regularly or as a core part of how they deliver SEO work, and 78% of respondents said they use Claude, ahead of ChatGPT at 57%.

The tools are being used. The question is what they’re being used for.

Research, synthesis, and first drafts are good jobs. Publishing decisions aren’t, for a practical reason: The two tasks require different things from the model.

Research needs a model that can hold a lot of context and generate plausible-sounding options fast.

Execution needs a model that knows when a plausible-sounding option is actually wrong for this specific page, site architecture, and keyword map. Claude, like every current AI model, doesn’t reliably know that.

Dig deeper: How to build a Claude Code-powered second brain for agency work

Be the brand AI recommends.

See where your brand appears in AI search, where competitors are winning, and what it takes to become the answer AI recommends.

See your AI visibility

Why ‘looks plausible’ isn’t the same as ‘is correct’ for SEO

One failure should worry anyone handing Claude the keys to a CMS. When an AI model is asked to solve a content problem and doesn’t have a new answer, it can produce something that resembles a correct answer instead of admitting it doesn’t have one.

In coding, that shows up as invented function names. In SEO, it shows up as duplicated pages with new titles.

I used Claude to review Google Search Console, recommend target keywords for our own AI Website Grader, and build the pages those keywords needed. Instead of writing purpose-built content, Claude cloned the homepage into two new URLs, /seo-grader and /content-grader, changed the title tag and H1 to match the new keywords, and reused most of the homepage’s body copy.

On paper, each “page” now targeted a new term. In practice, it was the homepage’s content living at three URLs, competing with itself, exactly the kind of cannibalization a competent SEO would never do.

I left those two pages live on purpose, as a running illustration. Each still lifts most of its body copy from the homepage, and six months of Google Search Console data show the result. The dedicated /seo-grader and /content-grader pages have earned zero impressions and zero clicks.

Every query they were built to win goes to the homepage instead: “content grader” (487 impressions, average position 9.2), “seo grader” (position 10.6), and “ai content grader” (position 5.3).

The clone didn’t just risk cannibalization. It generated no impressions or clicks, while the homepage sits stuck at the bottom of Page 1 for the exact terms a dedicated page should own.

Microsoft has confirmed the same dynamic on the AI side: Bing’s models group near-duplicate URLs into a single cluster and may pick an unintended page as the representative source, so a clone can even hand AI answers the wrong URL.

I’ve seen SEOs make plenty of mistakes over the years. I have never seen one deliberately duplicate a ranking page and slap a new title on it, because every SEO knows it’s a self-inflicted wound.

Claude did it anyway, with total confidence, no caveat, and no flag that the “new” page was actually a clone.

The same mistake happened twice

If this had happened once, I’d chalk it up to a bad prompt on my part. It happened again, on a completely different site, run by someone else.

My son Caleb started a project called ScryPrice, a price-comparison engine for Magic: The Gathering cards. He asked Claude for SEO keyword recommendations, the same kind of request I’d made. Claude’s response was to generate a batch of new pages built to target those keywords.

When we checked them, every one of those “new” pages was a copy of the homepage with nothing changed except the title tag. No unique product context, no differentiated content, no reason for a search engine to treat any of them as distinct from the page they were cloned from.

Same failure mode, same root cause, two unrelated projects, months apart, with no shared prompt or workflow between us.

That’s what makes this worth writing about instead of shrugging off: It’s what can happen when an AI model is given execution authority over a content or SEO task and no guardrail forces it to actually build something new instead of reshaping something that already exists.

Dig deeper: How to train Claude to sound like your brand

Other SEO failure modes show the same pattern

There’s a crawlability version of the same failure. An SEO developer who posts as @rentierdigital measured it:

- “[C]laudebot downloads your [JS] bundle in 24% of its requests and never executes it. it cannot read the thing it helped you build.”

When an AI agent builds a JavaScript-heavy page that depends on client-side rendering, the page can look finished while remaining difficult for crawlers to read and index.

Other SEO practitioners have described similar problems with AI-generated pages. SEO consultant Robert May put it plainly:

- “The problem’s not AI, it’s using AI to create hundreds of pages that should never have existed in the first place.”

Digital marketer Scott DeSapio identified another problem with using AI to scale content:

- “One page trying to rank for five different searches usually ranks for none. Each URL should serve one clear search intent.”

An account posting as @digispot_ai listed a similar set of symptoms:

- “Missing internal links. Duplicate intent. Wrong schema. Cannibalized keywords. Pages Google never indexes.”

None of these are the same mistake I saw, but they’re all variations of the same problem: Give an AI model autonomy over an SEO task, and it can optimize for producing something that looks finished rather than producing something that’s actually right.

The highest-stakes problem isn’t even SEO

The same pattern shows up far beyond SEO when AI agents get real execution authority without a human checkpoint.

In July 2025, SaaS founder Jason Lemkin said Replit’s AI coding agent deleted the company’s production database despite instructions to freeze code and data changes, wiping records for more than 1,200 executives and more than 1,190 companies. Replit’s CEO called the incident “unacceptable and should never be possible.”

That’s not an SEO story, and I’m not claiming it is. The point is the failure pattern: An AI agent given execution authority, operating without a human checkpoint, can optimize for producing an output rather than producing the right output.

The SEO version is quieter. Nobody’s database gets wiped when Claude clones a page instead of writing one. But the underlying problem is the same: The agent can produce something that looks finished without recognizing that it’s wrong.

Get the newsletter search marketers rely on.

Give AI the research, keep humans on execution

None of this means AI models are broken or useless for SEO. The job just needs to be split in two, and only one half belongs to the AI.

Give Claude the research and analysis work

Keyword clustering, search intent classification, content gap analysis against competitors, technical audit summaries, first-draft outlines, and copy.

This is where Claude’s ability to process a lot of information quickly and surface patterns does the most good. It cuts hours out of the front end of SEO work without touching anything live.

Keep a human on every execution decision

New page creation, title tag and H1 changes, redirects, canonical tags, internal linking changes, and anything that touches a live URL get reviewed and approved by a person who actually knows the site before it ships. Not “spot-checked after the fact.”

Reviewed before it goes live, the same way you’d review a junior team member’s first few weeks of work, because that’s functionally what an AI agent with content permissions is.

Treat every AI-drafted ‘new page’ as a claim, not a fact, until you’ve verified it

The specific failure I hit, cloning instead of creating, is easy to catch if you check for it and easy to miss if you don’t. Before publishing anything an AI model produced in response to a keyword-targeting request, diff it against your existing content.

If the body copy matches an existing page by more than a sentence or two, it’s not a new page. It’s a duplicate wearing a new title tag. Shipping it will cost you rankings on both URLs instead of gaining you one.

Don’t confuse ‘the output looks done’ with ‘the output is correct’

This is the mental shift that matters most. An AI model has no internal signal that tells it, “I don’t actually have a good answer to this.”

It just produces the best-looking answer it can generate, which is sometimes a real answer and sometimes a page-shaped object that technically satisfies the prompt. Your job, or your team’s job, is to be the check that catches the difference before a search engine has to.

Dig deeper: 6 content audit workflows to build in Claude

Frequently asked questions

Can I let an AI agent publish SEO content automatically?

You can, technically. Whether you should depends entirely on whether you’re comfortable with content going live that nobody reviewed for accuracy, uniqueness, or fit with your existing pages.

Mine and Caleb’s stories both involve exactly that scenario: An AI model given the ability to act without a review step in between.

Why does Claude duplicate pages instead of writing new ones?

Nobody outside Anthropic can say with certainty what’s happening inside the model on any given run, but the observable pattern is consistent. When asked to solve a content problem quickly, the model reaches for the fastest plausible output.

Modifying an existing page is faster and lower-risk, from the model’s perspective, than generating new, differentiated content, even though the result is worse for SEO.

Is this specific to Claude, or do other AI models do it too?

The duplication error in this article occurred specifically with Claude on two separate sites. But the broader pattern, confident wrong answers and execution shortcuts that look complete but aren’t, shows up across ChatGPT, AI coding agents, and other models in the examples cited above. This is a category problem with autonomous AI execution, not a single vendor’s bug.

If AI can’t find you, customers won’t either.

Track your visibility across AI search, uncover missed opportunities, and grow your presence where customers are asking questions.

Keep humans responsible for what goes live

Claude made my SEO research faster this year. It also tried to solve a keyword problem twice by cloning a page and calling it done, and one of those batches made it onto a live site before someone caught it.

If your team is running AI-assisted SEO right now, ask one question this week: Does every AI-touched page still have a human’s name on the approval before it goes live?

Contributing authors are invited to create content for Search Engine Land and are chosen for their expertise and contribution to the search community. Our contributors work under the oversight of the editorial staff and contributions are checked for quality and relevance to our readers. Search Engine Land is owned by Semrush. Contributor was not asked to make any direct or indirect mentions of Semrush. The opinions they express are their own.
