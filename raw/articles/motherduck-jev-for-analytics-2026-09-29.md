---
title: "Jev for analytics: turn text columns into gold, in plain SQL"
author: Mehdi Ouazza
publisher: MotherDuck
published: 2026-09-29
captured: 2026-09-30
type: raw-source
status: captured
source_url: https://motherduck.com/blog/jev-for-analytics/
extraction_route: direct_html
source_quality: partial
---

# Jev for analytics: turn text columns into gold, in plain SQL

## Capture provenance and limitations

- Source: https://motherduck.com/blog/jev-for-analytics/
- Author: Mehdi Ouazza; publisher: MotherDuck.
- Publication date: 2026-09-29, shown on the live page as `2026/09/29`.
- Capture date: 2026-09-30. Direct HTML-to-Markdown extraction; main prose, static tables, source links and SQL snippets retained below. Navigation, subscription prompts, copy-button labels and flattened interactive-diagram text omitted. Diagram-only examples and aggregate displays are not reproduced; this is a partial page snapshot, not a complete visual or interactive archive.
- Evidence scope: first-party product walkthrough and author-reported measurements, not independent reproduction. Model names and results are preserved as published, not independently verified. SQL is source material, not executed code. Linked launch benchmarks and documentation are references, not separately captured or validated here.

## Original article body (text and static tables)

Every now and then, we all end up with a table that has a big text column. A comment, some customer feedback, or worse, an address nobody parsed upstream. There are insights in that column, but they're hard to get out. And sometimes it's plain extra compute you keep paying for: the address never got parsed into typed columns, so every query parses text again, and parsing text is `$$$`.

Let's take a dataset with 100,000 complaints. Each row has a narrative (someone explaining what went wrong with a bank, a lender, or their credit report) and how the company responded. The column I actually want is missing: what was the person asking for?

It sounds like a job for an LLM. But running an LLM over every row just to pick one of seven known answers is like using a cannon to kill a fly. It's slow on a big table, so it scales badly, or it just burns your credit card.

`prompt_jev()` classified the 100,000 rows in 82.2 seconds, with no LLM generating the per-row answers. On the same complaints, gpt-5-nano through `prompt()` needed 6 minutes 9 seconds for only 10,000 rows (Jev: 12.5 seconds). On cost, the [launch benchmark](https://motherduck.com/blog/motherduck-supports-jev/) put Jev at $0.50 per 100,000 rows, against $1.58 for gpt-5-nano and $37.58 for GPT-5.6 Terra (API prices). That's about 1% of the frontier model's bill.

Faster and cheaper? Let's look at what Jev does, run it on the dataset, and see where I would (and wouldn't) trust the result.

### What Jev does

TypeSafe calls Jev a ["System One" model](https://typesafe.ai/blog/introducing-system-one-models-and-jev), borrowing from Kahneman's [Thinking, Fast and Slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow). System 1 is the quick, intuitive answer. System 2 is the slow, deliberate one. A classic LLM is System 2: it reasons and writes its answer token by token. Jev is System 1: it reads the text once and scores the answers you allowed.

|  | System 2: a classic LLM | System 1: Jev |
| --- | --- | --- |
| How it answers | Writes text, token by token | Scores a fixed list of answers in one pass |
| What you get back | Free text (you parse it, or force a schema) | A typed label, probability, or score |
| Can invent a new answer | Yes | No, only the options you give it |
| Tells you how sure it is | Not directly | A probability per option, plus a confidence |
| 100k rows benchmark | 18 to 32 minutes, $1.58 to $37.58 | 40 seconds, $0.50 |
| Good at | New taxonomies, summaries, explanations | The same bounded decision over many rows |
| Example: customer request: "Please refund the two fees you charged me." | Answer is something like "The customer is asking for a refund of the two fees..." (a sentence to parse) | `{choice: 'refund', confidence: 1.0}` (real output, 3 labels) |

For SQL, think of it as a smart decision function: you give it one row of text, a question, and the allowed answers. You get back a typed decision, plus a number that tells you how sure it is.

There are three question shapes. Here they are on the same real complaint (10306039, someone charged low balance fees on an account they had closed):

| Shape | You ask | You get back | Real answer | SQL use |
| --- | --- | --- | --- | --- |
| Choice | "What outcome is the consumer asking for?" + 7 labels | one label + confidence | `refund_or_charge_reversal`, 0.95 | `GROUP BY` |
| Noul | "The complaint is about fees the bank charged." | a probability, 0 to 1 | 0.97 (and 0.02 for "reports identity theft") | `WHERE` |
| Score | "How urgent is this?" on low / medium / high | a position on the scale + confidence | 1.62 (0 = low, 2 = high), 0.43 | `ORDER BY` |

This walkthrough uses Choice, since each complaint should land in one request category.

How does that compare to what you already use?

* An LLM is the right tool for a new taxonomy, a summary, or an explanation. A schema can hold it to your labels, but it still writes each one out token by token. Jev picks from your list, so you always get back one of your strings.
* `CASE WHEN` or a regex only works when the rule is literal. People write "reverse the charge" instead of "refund", and mentioning money isn't always asking for it.
* A trained classifier scales well but is painful to run (labelled examples, a model to maintain). With Jev, you describe the categories in the query and try them right away.
* Parsing rules (JSON paths, address parsers) are static and break when the format changes. Jev works from what the text says, so messy input hurts it less.

Jev can only return one of the options you gave it, so poor options get you a neatly typed poor answer. Garbage in, garbage out.

#### About the dataset: complaints from CFPB

The complaints come from the U.S. Consumer Financial Protection Bureau ([CFPB's archive](https://www.consumerfinance.gov/foia-requests/foia-electronic-reading-room/cfpb-consumer-complaint-database-narratives-archive/)), the agency that collects complaints about banks, lenders, credit bureaus, and other financial services.

My table `complaints_100k` has (spoiler alert) 100,000 rows with `complaint_id`, `narrative`, `company_response`, and a few other fields. Here's what four rows look like:

| complaint_id | product | narrative (trimmed) | company_response |
| --- | --- | --- | --- |
| 9906201 | credit reporting | "This account is incorrectly being reported as a charged off account with a balance due. Please provide proof of the charge off and update the balance to {$0.00}..." | Closed with explanation |
| 10306039 | bank account | "I closed my Chase checking account in XXXX by sending Chase a letter via mail. Chase conveniently ignored the account closure request so they can charge low balance fees..." | Closed with monetary relief |
| 6084737 | debt collection | "I have no outstanding debts owed that I am aware of. Americollect has called numerous times almost daily..." | Closed with explanation |
| 2042216 | credit card | "I paid my credit card with a money order. They did not apply the payment to my account..." | Closed with monetary relief |

Let's get the gold out of that narrative column.

### Step 1: define the labels, then classify

Before classifying 100,000 rows, we need the categories. I sampled 40 narratives and asked MotherDuck's `prompt()` function, running gpt-5-mini, to suggest seven requested-outcome categories. That took 7.6 seconds. How you sample matters (and you can take a bigger one), but that's a business question more than a technical one.

Then Jev classifies every row against these categories, in less than 2 minutes:

Jev requires the question and the choices to be constants, so the simplest way is to paste the taxonomy straight into `choice :=`. Here's the classification step, with the same labels and descriptions as the measured run:

```sql
CREATE TABLE complaint_requests AS
SELECT complaint_id, company_response,
       prompt_jev(
         narrative,
         'What outcome is the consumer asking for?',
         choice := [
           {label: 'refund_or_charge_reversal',
            description: 'Consumer requests money returned, reversal of fees/charges, or reimbursement.'},
           {label: 'correct_or_remove_credit_report_entry',
            description: 'Consumer asks to fix, update, or remove inaccurate items on their credit report.'},
           {label: 'investigate_and_credit_transaction_error',
            description: 'Consumer requests investigation and correction of a transaction or deposit error and credit to their account.'},
           {label: 'stop_harassment_or_contact',
            description: 'Consumer asks for communications or collection calls/texts/emails to stop or follow rules.'},
           {label: 'address_identity_theft_or_fraud',
            description: 'Consumer requests action to resolve identity theft, fraudulent accounts, or unauthorized inquiries.'},
           {label: 'explain_decision_or_account_status',
            description: 'Consumer asks for clarification or explanation of a decision, account action, or why charges occurred.'},
           {label: 'other',
            description: 'Any requested outcome that does not fit the categories above.'}
         ]
       ) AS request
FROM complaints_100k;
```

`request` is a struct. `request.choice` is the picked label, and `request.confidence` and `request.probabilities` help you inspect the decision. Here's what came back for the Chase fees complaint (10306039):

```text
{
  choice: 'refund_or_charge_reversal',
  confidence: 0.95,
  probabilities: [
    {value: 'refund_or_charge_reversal', probability: 0.96},
    {value: 'other', probability: 0.03},
    {value: 'explain_decision_or_account_status', probability: 0.01},
    ... -- the other 4 labels at 0.00
  ]
}
```

#### Bonus: keep the labels in a table

Pasting 7 labels into a query is fine once. If the taxonomy sticks around (versioned, shared across queries, edited by the business), you'd rather keep it in a table. A subquery in `choice :=` doesn't work (`"choice" parameter must be a constant value`), but a DuckDB variable does, because it's resolved before the query runs:

```sql
SET VARIABLE request_labels = (
  SELECT list({label: label, description: description} ORDER BY label)
  FROM request_taxonomy
);

SELECT complaint_id,
       prompt_jev(narrative, 'What outcome is the consumer asking for?',
                  choice := getvariable('request_labels')) AS request
FROM complaints_100k;
```

Why bother: one source of truth for the labels, easy to version (add a `taxonomy_version` column), and the business can review the labels without reading SQL.

### Step 2: don't trust Jev blindly

Jev can't invent a label, but it can still pick the wrong one.

The first thing to look at is `confidence`. Jev scores every label, and `confidence` says how concentrated those scores are: 1.0 when one label takes everything, low when two or three labels share the probability.
Across the 100,000 rows, the mean confidence is 0.83, 65.8% of rows are at 0.8 or above, and 10.9% are below 0.5.

SQL gives you the review queue:

```sql
SELECT complaint_id, request.choice, request.confidence
FROM complaint_requests
WHERE request.confidence < 0.8
ORDER BY request.confidence;
```

0.8 is an example, and a row above it can still be wrong. Send uncertain rows to a human or a bigger model, and keep the rest in the analytics table once you've validated that cut on your data.

The second check is to compare against another model on a sample. On 300 rows, I labelled them twice: with GPT-5 through `prompt()` (the newest model MotherDuck's `prompt()` offers today) and with Claude Opus 5.5, which read each narrative blind, without seeing any other label. Here's what came out:

| Comparison on 300 rows | Agreement |
| --- | --- |
| GPT-5 vs Claude Opus 5.5 | 72.7% |
| Jev vs GPT-5 | 77.3% |
| Jev vs Claude Opus 5.5 | 74.0% |
| Jev, on the 218 rows where GPT-5 and Opus agree | 90.4% |
| Jev, on those rows with confidence >= 0.8 (161 rows) | 96.9% |

The two big LLMs agree with each other less often than Jev agrees with either of them. So the task itself is fuzzy: most disagreements sit on the boundaries we already saw (identity theft vs credit-report fix, "other" vs a specific label).

### Step 3: ask the question (the good boring part)

Once the requested outcome is a typed column, it's plain SQL:

```sql
SELECT request.choice AS requested_outcome,
       count(*) AS complaints,
       round(100.0 * avg(
         (company_response = 'Closed with monetary relief')::INT
       ), 1) AS pct_monetary_relief
FROM complaint_requests
GROUP BY 1
ORDER BY complaints DESC;
```

It runs in 0.9 seconds on MotherDuck. The 82.2 seconds of classification happen once, and every question after that costs what any other `GROUP BY` costs.

### When I would use this pattern

Use `prompt_jev()` when the same decision repeats across many rows and you can write the possible answers down: complaint intent, product family, "did they ask for a refund?", a severity rubric. Use an LLM when you need new categories, generated text, or an explanation a human will read. Or use both, like here: the LLM helps design the question, Jev applies it at scale.

The [MotherDuck launch benchmark](https://motherduck.com/blog/motherduck-supports-jev/) classified 100,000 short news articles in 40 seconds. My 82.2-second complaint run is a different task (longer narratives, seven described choices), so I wouldn't promise either number on your table. Test on a sample first :)

`prompt_jev()` is available on MotherDuck paid plans. The text is sent to TypeSafe for inference, so check your data-handling requirements before passing sensitive customer data. The [guide](https://motherduck.com/docs/key-tasks/ai-and-motherduck/classify-text-with-prompt-jev/) and [function reference](https://motherduck.com/docs/sql-reference/motherduck-sql-reference/ai-functions/prompt-jev/) have the full syntax.
