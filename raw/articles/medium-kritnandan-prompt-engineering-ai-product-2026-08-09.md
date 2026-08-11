---
title: Why Prompt Engineering Alone Won’t Save Your AI Product
author: [Kritnandan]
created: 2026-08-12
updated: 2026-08-12
type: raw-source
status: captured
source: Medium
source_url: https://medium.com/@kritnandan3/why-prompt-engineering-alone-wont-save-your-ai-product-8a5f63129767
published: 2026-08-09
captured: 2026-08-12
extraction: Jina Reader fallback from the canonical Medium URL; article prose preserved, Medium sign-in/newsletter/share chrome and image-only prompts removed; not byte-faithful HTML
tags: [agent, evaluation, validation, prompt-tuning, system-design]
---

# Why Prompt Engineering Alone Won’t Save Your AI Product

## Provenance

- Source URL: https://medium.com/@kritnandan3/why-prompt-engineering-alone-wont-save-your-ai-product-8a5f63129767
- Source: Medium
- Author: Kritnandan
- Published: 2026-08-09
- Captured: 2026-08-12
- Local summary (local-only auxiliary path, not a stable long-term source): `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260812-005023-Why-Prompt-Engineering-Alone-Won’t-Save-Your-AI-Product-1327607-753220800-summary.md`
- Extraction route: Jina Reader Medium fallback
- Source quality: complete article prose; Medium UI boilerplate and image-only prompts removed; not a byte-faithful HTML capture

## Source limitations

- This is a first-person practitioner account from three projects, not a controlled comparative study or production incident dataset.
- The reported scores, failure rates, sample sizes and thresholds are source-specific experience values; the article does not provide its scoring rubric, variance, datasets or raw runs.
- The claim that validation-error feedback works better than static repair instructions is supported by the author’s experience, not a published benchmark in this source.
- Schema validation catches structural failures but does not establish semantic correctness; the author explicitly states this limitation.

## Extracted article body

You can’t prompt your way out of a systems problem.

Our extraction prompt was on version 47. I know the exact number because the file was literally called extract_v47.txt and it was sitting in a folder with 46 ancestors, none of which anyone had deleted.

Then a teammate did something obvious that none of us had done. He ran v12 and v47 against the same 200 test documents. v12 scored 82 percent. v47 scored 83 percent.

Five weeks of prompt rewriting for one point.

That afternoon was the first time I properly understood something that now shapes how I build: if every bug you hit gets fixed by adding another line to the system prompt, you don’t have a prompt problem. You have an architecture that routes every failure to the same place, because it’s the only place you built.

## A prompt controls one call. Your product is thousands of them.

A prompt is an instruction attached to a single model call. That’s the whole scope. It can shape tone, format, reasoning style, and the examples the model pattern matches against. That is genuinely a lot, and I’m not here to tell you prompting doesn’t matter.

But look at what happens after that call returns.

The output gets parsed. It gets validated, or it doesn’t. It gets passed to a tool that may be down. The tool result gets appended to a context window that is already 60 percent full. Some state gets written somewhere. Something retries, or fails silently, or loops.

None of that is inside the prompt. The prompt ended the moment the tokens came back.

So when your agent books a meeting for a date that doesn’t exist, the honest question is not “how do I word this better.” It’s “which of the twelve things that happen after the model call was supposed to catch this, and why didn’t it exist.”

I wrote earlier this week about the seven layers every reliable agent ends up having. The prompt lives in exactly one of them. Trying to fix problems from the other six by editing the prompt is like fixing a database timeout by renaming a variable.

## The plateau is real and you can measure it in one afternoon

Here’s the test I now run on any project where prompt versions have gotten out of hand.

Take your oldest prompt version that still runs. Take your newest. Run both against the same fixed set of at least 100 real inputs. Score them the same way.

If the gap is under three points, stop writing prompts today.

That number isn’t magic, it’s just where measurement noise stops being an excuse. What it tells you is that your accuracy ceiling is no longer set by wording. It’s set by something structural: the model can’t see the data it needs, or the output has no validator, or the retrieval index is three weeks stale, or the tool it’s calling returns garbage on Tuesdays.

Prompt work has a real curve. Steep early, flat fast. Most teams keep climbing after it goes flat because prompting feels like progress. You change something, you rerun it, you see different output. It scratches the same itch as debugging without any of the payoff.

## Five bugs I tried to prompt away

These are real, from three different projects. In each one I lost days before I gave up and wrote actual code.

The model returned JSON wrapped in a friendly sentence. I tried “respond with only valid JSON.” Then “do not include any explanation.” Then all caps. Then a threat, which I’m not proud of. What fixed it: a parser that extracts the first JSON object, a Pydantic model that validates it, and a repair call that gets the parse error fed back as text. Ten minutes of work. I had spent about three hours on wording.

The model invented product codes. Beautifully formatted, correct prefix, completely fictional. No amount of “only use codes from the provided list” fully stopped it. What fixed it: validate every generated code against the actual catalog after generation, and reject the ones that don’t exist. The model is allowed to be wrong. The system is not allowed to pass it on.

The model ignored a hard rule after turn 15. The rule was in the system prompt. It was in bold. It was repeated twice. It still got buried under 40k tokens of conversation and tool output. What fixed it: a permission check in code before the action executed. Rules that must never break do not belong in a prompt, they belong in an if statement.

The model called a tool with a malformed argument. Roughly one call in twenty. I added examples. It went to one in thirty. What fixed it: schema validation on the tool input, and on failure, send the validation error back to the model and let it try again. Failure rate reaching the user went to near zero, and I could finally see the retry count on a dashboard instead of guessing.

The model’s answers got too long for the UI. I asked for brevity in six different ways. What fixed it: max_tokens, plus a truncation rule in the renderer. Obvious in hindsight. Almost everything on this list is obvious in hindsight.

The pattern across all five: anything you can check in code should never be pleaded for in a prompt.

## The loop that replaced my last three prompt rewrites

This is the smallest version of the thing that made the biggest difference. It validates, and on failure it hands the model the actual error instead of a vaguer instruction.

```python
from pydantic import BaseModel, ValidationError

class Invoice(BaseModel): vendor: str amount_cents: int due_date: str

def extract(text, max_attempts=3): messages = [{“role”: “user”, “content”: PROMPT.format(text=text)}] for attempt in range(max_attempts): raw = call_model(messages) try: return Invoice.model_validate_json(raw) except ValidationError as e: messages.append({“role”: “assistant”, “content”: raw}) # the error text is the correction, not a reworded instruction messages.append({“role”: “user”, “content”: f”That failed validation:\n{e}\nReturn corrected JSON only.”}) raise ValueError(“extraction failed after retries”)
```

Two things worth noticing.

The correction is the validation error itself. Specific, machine generated, different every time. That works far better than a static line in the prompt that says “make sure the amount is an integer,” because the model now sees exactly which field broke and why.

And the loop has a ceiling. Three attempts, then it raises. An unbounded repair loop is just a slower way to burn your API budget, which I learned in a way I’d rather not repeat.

## Prompts are code. Store them like code.

Somewhere along the way prompts got treated as configuration. A string in a settings file, or worse, a text box in an admin panel that anyone can edit at 11pm.

They’re not configuration. They’re logic. They change behavior more than most of your functions do.

What that means in practice is boring and takes about an hour to set up. Prompts live in files in the repo, one per file, with a version. Changes go through a pull request so someone else sees the diff. Every prompt has a small eval set attached, twenty to fifty real cases with expected outputs, and you run it before merging. When something regresses, you roll back a commit instead of trying to remember what v43 said.

The first time you get to say “the accuracy drop started with commit 8f2a1c” instead of “I think someone changed the prompt last week,” the hour pays for itself.

## When prompting actually is the answer

I’ve spent this whole post pushing you toward code, so here’s the honest boundary.

Prompting is the right tool when the thing you want is genuinely a matter of expression. Tone, voice, and register. Output format and structure, at least as a first pass before validation catches the rest. Reasoning approach, like asking the model to work through constraints before answering. Few shot examples for edge cases that are hard to describe in rules but easy to demonstrate.

Anything subjective, anything where you can’t write a test that says pass or fail, is prompt territory. That’s not a small area. A great prompt with three well chosen examples will beat a mediocre prompt with a validator sitting on top of it.

The failure mode isn’t prompting. It’s using prompting for problems that have a deterministic answer. Reach for the prompt when the target is a matter of judgement, and reach for code when the target is a matter of fact.

And one more limitation I should admit, since I’ve been confident for about 1,400 words now. Validators catch structural failures, not semantic ones. My Invoice model will happily accept a vendor name that the model hallucinated, as long as it’s a string. Schema validation gives you well formed wrong answers instead of malformed wrong answers. That’s a real improvement and it is not the same thing as correctness. Catching the semantic failures needs evals, which is a whole post on its own and one I’ll get to later this month.

## Three things to do this week

Run your oldest and newest prompt version against the same 100 inputs and write down both numbers. Decide based on the gap, not on how the outputs feel.

Pick the one instruction in your system prompt that you’ve reworded the most times, and go implement it as a validator instead.

Move your prompts into version controlled files with an eval set attached, even if the eval set is only twenty cases to start.

Day 27 is the full structured outputs playbook, where I go much deeper on schemas and repair strategies.

If you have a prompt version number you’re embarrassed about, tell me in the comments. I’ll go first: 47.
