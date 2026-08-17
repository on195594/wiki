---
title: RAG Workflow and Loop Engineering: The Dispatcher That Decides When to Loop and When to Stop
author: Angela Shi
published: 2026-08-14
captured: 2026-08-17
type: raw-source
source: Towards Data Science
source_url: https://towardsdatascience.com/rag-workflow-and-loop-engineering-the-dispatcher-that-decides-when-to-loop-and-when-to-stop/
status: captured
extraction: "Full rendered browser DOM main.innerText captured after direct HTTP returned 403. Local summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260817-200548-RAG-Workflow-and-Loop-Engineering-The-Dispatcher-That-Decides-When-to-Loop-and-W-3790819-403008560-summary.md"
---

# RAG Workflow and Loop Engineering: The Dispatcher That Decides When to Loop and When to Stop

## Capture notes

- Source quality: full rendered article body; trailing Towards Data Science promotion and related-series navigation are preserved as extraction context.
- The worked examples and reported latency/cost figures are source-specific and are not Hermes production measurements.
- The durable Hermes delta is the control boundary: models emit typed diagnostic signals while deterministic code owns routing, retry budgets, drift checks and stop decisions.

## Source text

LARGE LANGUAGE MODEL
RAG Workflow and Loop Engineering: The Dispatcher That Decides When to Loop and When to Stop

Enterprise Document Intelligence [Vol.1 #13] – Putting the patterns together, and why this is what “agentic RAG” should look like

Angela Shi
Aug 14, 2026
32 min read
Share
Photo by Fernando Narvaez, via Pexels.

Over the last few articles, we built loop patterns one at a time: a re-parse when a page check fails, a second retrieval when the answer points to another section, an aggregation sweep when the question asks for a complete list. Each pattern has its own article, its own trigger, and its own test. Each one works fine on its own.

Real questions do not arrive one pattern at a time. Take one a compliance officer would actually ask on the NIST Cybersecurity Framework (US Government work, public domain in the US, see NIST copyright statement): “What are all the Categories under GOVERN, and which one covers supply chain risk?” The question sounds ordinary. Inside the pipeline, it fires three patterns at once:

TOC retrieval, to land on the right section;
listing aggregation, to enumerate every Category, not just the most-cited ones;
a synthesis step, to pick the one that covers supply chain risk.

Each of the three carries its own iteration mechanic: a re-retrieval here, a re-generation there, an LLM flag that triggers a second pass. Run them on the same question and a practical problem shows up: which one decides when to stop? Leave that undecided and every new kind of question becomes another special case bolted on the side, and nobody can say what the pipeline will do next.

The fashionable answer today is to hand that decision to an agent and let the model orchestrate. For an enterprise pipeline, we prefer a piece of code we can read: a dispatcher that turns the parsed question and the document profile into an explicit plan, and bounded loops that say, in code, how far each pattern may iterate. That is what this article builds: the feedback loops, the bounded iteration, and the dispatcher that composes them into one workflow.

This article closes Part III of Enterprise Document Intelligence, a series that builds an enterprise RAG system from four bricks: document parsing, question parsing, retrieval, and generation.

🧭 New to the series? Start with the map: Prompt, Context, Loop sets out the three engineering layers every RAG system is built on, the prompt (the call itself), the context (what fills the model’s window), the loop (when the next call fires and when it stops), and walks the whole series through that lens, article by article. It is the shortest way to see what is covered and where this one sits.

where this article sits in the series: Article 13 (the workflow pipeline), closing Part III – Image by author

📓 The runnable companion drives the loop machinery yourself: you run pdf_qa_loop on a question that fails its first pass, print the IterationRecord history showing what each retry changed, and watch should_continue cut the loop when the candidates stop moving. On GitHub: doc-intel/notebooks-vol1.

The public companion-code repo at doc-intel/notebooks-vol1 – Image by author

In production, real questions stack the patterns: “List the obligations of the seller, including any referenced standards” on a contract adds two-hop reference resolution on top of listing. The iteration mechanics ride alongside them.

It helps to place this article on a five-rung climb, each rung a more capable version of the same PDF question-answering function. The baseline (Article 1) chains the four bricks once with keyword retrieval: one pass, return the answer. The upgraded version (Article 9, the four bricks upgraded contract by contract) keeps the single pass but makes it richer, with a full relational parse and TOC routing, and it returns a typed answer carrying feedback fields (is the context complete? did the parse hold?), produced but not yet acted on. The workflow rung, this article, turns that pass into one step inside a bounded loop: a dispatcher picks which patterns fire, and the loop reads the feedback fields to decide whether to retry, with the control staying in code.

The multi-intent rung (follow-up work) widens the entrance: a chat entry classifies what the user wants (a question, a translation, a summary, or just “hello”, which deserves a direct reply and no pipeline at all) and routes to the right pipeline, the decision still in code. The agentic rung (further out) moves the control loop into the LLM, which picks the next step itself; this article stops two rungs below, where the pipeline is still reproducible and auditable. Rungs one to four keep control in code; only the last jump moves who holds the loop from code to model.

Five levels of control, control in code until the last rung; this article is the workflow rung – Image by author

This article is about the composite pipeline: a single orchestrator function that takes a question, decides which patterns to activate, runs them, manages the feedback loops, and produces an answer. The function is pdf_qa_loop: the single pass from the upgraded pipeline, grown one rung, dispatching across Part III’s patterns within (pdf, qa). Follow-up work adds the entry points above it (other document formats, other intents); that scope sits outside this article. The patterns become a toolkit. pdf_qa_loop becomes their orchestrator.

Four patterns ON, three OFF; only ON patterns reach the Answer – Image by author

The dispatcher is where “amplify the expert” lands at the composition layer. The team’s routing wisdom (which patterns fire for which question types, in which order) gets written down once, in deterministic Python, and runs across every future question. The LLM appears at every brick. It never chooses the next call. Pattern selection is the dispatcher’s job; the iterate-or-stop decision is the loop machinery’s. Both stay in code, reviewable by the people whose judgment they codify.

1. One layer composes, the bricks stay apart

A workflow like this needs exactly one new home in the codebase: the composition layer. It holds the pieces that exist only because bricks are being combined: the dispatcher that picks which patterns fire, the feedback machinery that reads the typed flags, and one flow per intent. Nothing else moves. The four bricks keep living in their own modules, and the patterns of Part III stay where they belong as sub-functions of their brick: TOC retrieval in the retrieval module, escalation in parsing, two-hop resolution across retrieval and generation. The two layers talk through typed objects (a ParsedQuestion, a DocumentProfile, an AnswerWithEvidence), never through each other’s internals.

One way to lay that out on disk, the one this series uses: a pipeline/ folder sitting next to the brick modules:

pipeline/ holds the composition layer; the bricks themselves live next door – Image by author

Inside the composition layer, code is organised by intent (one subpackage per intent, one file per format inside), with the cross-intent infrastructure flat at the root; Article 18 (code architecture) develops the file layout in detail.

This split makes the system maintainable. When you improve TOC retrieval, you change the retrieval module only. When you fix a bug in two-hop resolution, the orchestrator stays untouched. The contract between orchestrator and bricks is the interface (a ParsedQuestion, a DocumentProfile, an Activations dict, an AnswerWithEvidence), not the implementation.

A senior engineer can trace any request from input to highlighted answer in a few minutes: pdf_qa_loop (pipeline/qa/pdf_flow.py) reads the question, calls decide_pipeline_patterns for activations, runs the four-brick pass (the same parse and retrieval entry points as Article 9’s pdf_qa) with those activations, reads the generation feedback fields, and either returns the answer or queues a loop. No hidden state, no agent loop.

The file layout has a runtime twin: how the handlers nest when a request actually runs. Each layer calls the one inside it and adds exactly one concern, and the control loop stays in code at every level.

Each ring calls the one inside and adds one concern, with the control loop always in code – Image by author
2. The orchestrator

The orchestrator does three things, in order:

1. It reads the parsed question (ParsedQuestion from Article 6) and decides which patterns to activate. Some questions need all of them. Most don’t.

2. It runs the active patterns, passing the right inputs to each. The order matters: TOC retrieval before keyword retrieval (so structural anchors come first), primary retrieval before two-hop (so the two-hop step has something to follow from), and so on.

3. It manages feedback loops. When the generation step signals an incomplete answer, the orchestrator decides whether to iterate and how many times. Multiple loops can fire on one question (parsing escalation, vocabulary expansion, reference expansion, listing iteration). The orchestrator picks the order across iterations (parsing first, vocabulary next, references next, listing last) and shares one budget across all of them. Two to three iterations cover the vast majority of cases; the composite’s hard cap is four, because several loops can fire on one question and each needs its own pass. Order matters because re-retrieving on bad parsing wastes the iteration; better keywords improve every later step.

Concretely:

# pdf_qa_loop, condensed
# decide_pipeline_patterns and iterate_with_bound come from the companion notebook.

def pdf_qa_loop(pdf_path, question, *, registry=None, max_iterations=4):
    registry = registry or PatternRegistry.default()
    # 1. Question understanding
    parsed = registry.parse_question(question)
    # 2. Cheap layer-1 parse of the document
    line_df, page_df, toc_df = registry.parse_layer1(pdf_path)
    # 3. Document profile
    doc_profile = registry.detect_document_type(pdf_path)
    # 4. Dispatcher : which patterns fire ?
    activations = decide_pipeline_patterns(parsed, doc_profile)
    # 5-7. Retrieval + generation inside a bounded feedback loop
    state = _State(parsed=parsed, line_df=line_df,
                   page_df=page_df, toc_df=toc_df)
    outcome = iterate_with_bound(
        initial_state=state,
        run_pass=lambda s: _one_pass(s, registry, activations, pdf_path),
        is_satisfactory=lambda a: not _needs_iteration(a),
        adjust=lambda s, a: _adjust_state(s, a, registry,
                                          activations, pdf_path),
        record=_build_record,
        max_iterations=max_iterations,
    )
    return CompositeOutput(answer=outcome.result, activations=activations,
                           history=outcome.history,
                           exhausted=outcome.exhausted)

That’s the whole orchestrator. The pdf_qa_loop body is a page of glue code sitting on top of the per-pattern modules. The third bullet (feedback loops) has its own dedicated machinery; section 3 walks through it. The first two bullets (pattern selection, run order) are deterministic once decide_pipeline_patterns returns its column of ON/OFF flags; section 4 walks through the dispatcher itself.

3. The feedback loop pattern

The composite pipeline’s distinguishing feature, compared to a naive RAG, is that the answer is treated as a provisional output that the system itself critiques. The loop machinery sits between generation and the final return.

3.1 From naive RAG to feedback-driven RAG

A naive RAG pipeline runs the four bricks in sequence and returns whatever comes out: parse the document, parse the question, retrieve, generate.

The four bricks chained once; parsed_q reaches Retrieval and Generation, no critique step – Image by author

If retrieval missed the right passage, the answer is wrong. If parsing was insufficient, the LLM hallucinates around the gap. The user never knows.

The composite pipeline adds a critique step at the end of the row, with two feedback rails that loop back whenever the LLM signals a problem: back into retrieval when the answer is incomplete (complete_answer_found=false, expand the keywords and re-retrieve), and back into parsing when the context came out unstructured (context_structured=false, re-parse the flagged pages):

Same four bricks plus Critique; two rails re-inject on a trigger, the green arrow exits on convergence – Image by author

The critique step reads the structured feedback fields the LLM produced (Article 8): is the context complete? did the LLM discover new keywords during reading? was the parsing sufficient? If anything is off, the pipeline takes targeted action and re-generates.

These rails are the pipeline’s big loops: the ones that cross bricks, triggered by generation reading its own input (adaptive parsing in Article 10, reference resolution in Article 11, scope feedback here). Each brick also runs its own small bounded loops inside (the image cascade in parsing, the TOC descent in retrieval, the schema retry in generation); those never reach the orchestrator. The dispatcher owns the big ones only.

This is what most vendors now market as agentic RAG. The term covers three quite different things; section 6 sorts them out.

3.2 Signal, trigger, action

Each loop has three dimensions: the signal (what the LLM or a programmatic check reports), the trigger (which state of the output starts a retry), and the action (what the pipeline changes for the next pass). Together with the bounds of section 3.3, these are the three control surfaces every loop in the series wears: signal plus trigger decide when a new pass fires, the action is the recovery (the one thing that changes before the retry), and the bounds are the termination.

Signals come from three sources:

LLM self-assessment: Fields like complete_answer_found, confidence, caveats. Soft signal, broadest coverage.
Programmatic checks: Deterministic code validates citations, format constraints, cardinality. Stronger signal because the check itself does not depend on the LLM’s judgment, even though it runs on the LLM’s output.
External validation: A separate model, a downstream tool, or a human. Strongest, most expensive. Reserved for high-stakes outputs.

Triggers map to specific actions (each was introduced once in Part II or III; here is the consolidated catalogue):

Incomplete answer (complete_answer_found=False from Article 9’s AnswerWithEvidence, or is_likely_complete=False from Article 12’s ListAnswer) → expand retrieval scope or activate a new pattern (listing, two-hop).
Insufficient context (context_structured=False, Article 10) → trigger adaptive parsing on the failing pages.
Discovered vocabulary (llm_discovered_keywords populated, Article 8) → re-retrieve with the expanded vocabulary.
Pending references (pending_references non-empty, Article 11) → run two-hop retrieval on each reference.
Cardinality mismatch (Article 12) → iterate with expanded keywords or a broader section restriction until the count matches or a bound is hit.
Failed validation (any programmatic check failed) → re-retrieve or ask the LLM to correct.

Each trigger maps to a named, targeted action, which keeps the loop debuggable.

3.3 Bounding the loops

The main risk of iterative pipelines is unbounded iteration. Three controls.

Maximum iterations: A ceiling on pdf_qa_loop’s max_iterations parameter. Two or three iterations cover the vast majority of cases. Beyond that, returns diminish sharply.

def iterate_with_bound(
    *,
    initial_state: TState,
    run_pass: Callable[[TState], TResult],
    is_satisfactory: Callable[[TResult], bool],
    adjust: Callable[[TState, TResult], TState],
    record: Callable[[int, TResult, TState, TResult | None], IterationRecord],
    max_iterations: int = 3,
) -> IterationOutcome[TState, TResult]:
    """Run a bounded pipeline-with-feedback loop."""
    state = initial_state
    history: list[IterationRecord] = []
    result = run_pass(state)
    previous_result: TResult | None = None
    if is_satisfactory(result):
        history.append(record(0, result, state, previous_result))
        return IterationOutcome(result=result, history=history, exhausted=False)
    for i in range(1, max_iterations):
        next_state = adjust(state, result)
        history.append(record(i, result, next_state, previous_result))
        previous_result = result
        state = next_state
        result = run_pass(state)
        if is_satisfactory(result):
            return IterationOutcome(result=result, history=history, exhausted=False)
    return IterationOutcome(result=result, history=history, exhausted=True)

A loop that hits max_iterations doesn’t crash. It returns the best output produced so far, flagged so the user and the audit trail know iteration was exhausted.

Termination conditions: Beyond max iterations, the loop stops when:

No new signal: The same trigger fires twice with the same suggested action.
No new candidates: Retrieval returned the same set of passages as last iteration.
Decreasing confidence: The loop is making things worse, not better. Stop iterating and return the highest-confidence answer seen so far.
def should_continue(history: list, current: _ResultProto,
                    confidence_drop_threshold: float = 0.1) -> bool:
    """Decide whether the iteration loop should run another pass.

    Three reasons to stop, in order of priority:
      1. Candidates are stable (same set as last pass): nothing new will be found.
      2. Suggested keywords are stable: the LLM is repeating itself.
      3. Confidence is decreasing past the threshold: the loop is making things worse.
    """
    if history:
        prev = history[-1]
        if getattr(prev, "candidates", None) == current.candidates:
            return False
        if getattr(prev, "suggested_keywords", None) == current.suggested_keywords:
            return False
        prev_conf = getattr(prev, "confidence", None)
        if prev_conf is not None and current.confidence < prev_conf - confidence_drop_threshold:
            return False
    return current.needs_iteration()

Without these, even with a max-iterations bound, the pipeline burns three full iterations on cases where it had clearly stopped progressing after the first.

Drift detection: A subtler failure: the loop iterates successfully (each pass finds new candidates) but the answer drifts away from the original question. Keyword expansion picked up a tangent. The user asked about “premium”, the LLM saw “insurance”, expanded to “policy”, then to “coverage”, then to “reinsurance”, and the answer ends up about reinsurance economics.

The fix is to keep the original question in scope at every iteration. Expanded keywords add to the retrieval, they don’t replace the original anchors. Generation always sees the original question.

def expand_query_safely(parsed, new_keywords: list[str],
                        max_keywords: int = 15):
    try:
        expanded = parsed.model_copy(deep=True)
    except AttributeError:
        import copy as _copy
        expanded = _copy.deepcopy(parsed)

    originals = list(expanded.retrieval.anchor_keywords or [])
    additions = [k for k in new_keywords if k not in originals]
    combined = originals + additions
    if len(combined) > max_keywords:
        kept_originals = originals[:max_keywords]
        room = max_keywords - len(kept_originals)
        combined = kept_originals + additions[-room:] if room > 0 else kept_originals
    expanded.retrieval.anchor_keywords = combined
    return expanded

A drift check at each iteration: if the new candidates have low overlap with the original anchor keywords, that’s drift, and the loop should stop.

3.4 Anti-patterns and audit trail

Five anti-patterns to keep out of the orchestrator:

Iterating on confidence alone: Confidence is noisy. An LLM can be highly confident on a wrong answer or low confidence on a correct one. Use confidence as one signal among several, never alone.
Unbounded keyword expansion: Cap the keyword set size (10 to 15) and prune the least informative when the cap is hit. Otherwise after three iterations the retrieval query is fifty terms long and signal-to-noise collapses.
Re-parsing more than necessary: When context_structured=False is signaled, re-parse only the pages the LLM flagged, not the whole document.
Hiding iteration from the audit trail. Every iteration must produce an IterationRecord. Compliance contexts require this; debugging contexts benefit from it.
Deciding to iterate purely with the LLM. The LLM can contribute signal to the iteration decision but the decision to iterate or stop must be in code, with explicit rules. should_continue (above) is where those rules live. The dispatcher decides only which patterns to fire upfront, not whether to loop.
{
  "iteration_number": 2,
  "trigger": "vocabulary_gap",
  "action_taken": "re-retrieve with `excess`",
  "result_summary": "page 7 joined the candidate set; confidence rose by 0.22",
  "confidence_before": 0.62,
  "confidence_after": 0.84
}

The full iteration history travels with the final answer. For audit and compliance, this is the difference between “the system gave this answer” and “the system gave this answer through these specific steps, each justified by an explicit trigger.” The UI presents a one-line narration per iteration so the user sees the system making informed choices rather than running blind retries.

4. The dispatcher

The dispatcher (decide.py) is where most of the explicit decisions happen. It takes the parsed question and the document profile, and returns a dictionary of pattern activations.

def decide_pipeline_patterns(
    parsed: ParsedQuestion,
    doc_profile: DocumentProfile,
) -> Activations:
    activations = dict(DEFAULT_ACTIVATIONS)

    # TOC retrieval: enable whenever the document has a usable TOC.
    if doc_profile.has_usable_toc:
        activations["toc_retrieval"] = True

    # Dense retrieval (embeddings): only as a fallback for questions whose
    # vocabulary may not match the document's wording.
    if parsed.intent in ("open_scoped", "open_corpus_wide"):
        activations["dense_retrieval"] = True

    # Two-hop references: enable when the question carries a structural
    # hint that points outside its primary passage.
    if parsed.retrieval.section_hint or parsed.retrieval.layout_hint:
        activations["two_hop_references"] = True
    if parsed.intent in ("section_retrieval", "open_scoped"):
        activations["two_hop_references"] = True

    # Listing aggregation: enable when the question intent is listing.
    if parsed.intent == "listing":
        activations["listing_aggregation"] = True

    return activations

This function encodes the team’s understanding of which questions need what. As the system runs in production, it evolves: new question types, new heuristics, edge cases observed in evaluation feed back into the dispatcher.

The dispatcher is also the file the team should iterate on with care. A bad activation rule can either over-engineer simple questions (running listing aggregation when not needed) or under-engineer complex ones (skipping two-hop on questions that need it). Each rule should have a test case attached.

5. Worked example: a listing-plus-references question on the Transformer paper

The previous articles have looked at NIST CSF listing questions. To make the dispatcher do something more, we pick a question on the Attention Is All You Need paper (Vaswani et al. 2017; arXiv non-exclusive distribution license, declared on the arXiv abstract page) that fires two retrieval patterns at once. Runnable code paths call OpenAI services governed by OpenAI’s Terms of Use.

Question: “What regularization techniques does the Transformer paper use, and where do they show the impact on BLEU?”

The first half is a listing question (Article 12 already covered it: three techniques, Section 5.4). The second half is a cross-reference question (Article 11: the impact numbers live in Table 3, not in Section 5.4). Both have to fire on the same call.

5.1 The inputs: parsed question and document profile

The orchestrator’s two inputs are a ParsedQuestion (from Article 6) and a DocumentProfile (a cheap probe on the PDF). Both are constructed below from real code. detect_document_type opens the Transformer PDF; the ParsedQuestion is what the LLM-backed parse_question would produce for the question above.

{
  "original_question": "What regularization techniques does the Transformer paper use, and where do they show the impact on BLEU?",
  "keywords": ["regularization", "dropout", "label smoothing", "BLEU"],
  "intent": "listing",
  "retrieval": {
    "main_query": "regularization techniques and their impact on BLEU",
    "rewrites": ["Residual Dropout", "Attention Dropout", "Label Smoothing", "Pdrop", "label smoothing epsilon", "Table 3"],
    "anchor_keywords": ["regularization", "dropout", "label smoothing", "Table 3"],
    "section_hint": "5.4",
    "layout_hint": "table"
  }
}

The three fields the dispatcher reads: intent = "listing", section_hint = "5.4", layout_hint = "table". The first activates listing aggregation; the other two activate two-hop references.

{
  "total_pages": 15,
  "has_usable_toc": true,
  "is_likely_scanned": false,
  "suggested_strategy": "native_text_only"
}

The profile is cheap: one fitz.open call, no body parsing. Page count, TOC presence (has_usable_toc = True because the Transformer paper carries 22 bookmarks), and a scan flag (False here, since the PDF is native text). The dispatcher reads has_usable_toc to enable TOC retrieval.

5.2 Dispatcher decision

decide_pipeline_patterns(parsed_q, doc_profile) reads the two objects above and returns an activation column. The output below is the real result from running the dispatcher on this question and this document:

{
  "toc_retrieval": true,
  "keyword_retrieval": true,
  "dense_retrieval": false,
  "two_hop_references": true,
  "listing_aggregation": true,
  "adaptive_parsing": false,
  "iterative_feedback": true
}

Four out of seven patterns activated (plus iterative feedback as the always-on safety net). The two-hop pattern makes this question different from a plain listing.

5.3 First pass: retrieval, listing, and the gap signal

pdf_qa_loop runs its pass (the same parse and retrieval entry points as Article 9’s pdf_qa) with the activation flags above. Inside that pass:

TOC retrieval (Article 9) jumps to Section 5.4 “Regularization” (page 7). The keyword retrieval, anchored on regularization, dropout, label smoothing, reinforces pages 7-8 (where the bold headers Residual Dropout and Label Smoothing sit). RRF fusion ranks pages 7-8 first.
Listing aggregation (Article 12) restricts to Section 5.4 and picks up three techniques: sub-layer dropout (Pdrop = 0.1, on the output of each sub-layer before add+layernorm, page 8), embedding dropout (Pdrop = 0.1, on the sum of token and positional embeddings, page 8), and label smoothing (εls = 0.1, page 8). The first two share the Residual Dropout paragraph in the paper; label smoothing is its own paragraph. The cardinality cue “We employ three types of regularization during training” at the bottom of page 7 confirms the count.
First generation pass produces an answer with the three techniques but no validation numbers. The LLM sets complete_answer_found=False and pending_references=["Table 3"] because the prose says results are reported in Table 3 but Table 3 wasn’t in the candidate set.

The pipeline doesn’t return an answer yet. The pending_references trigger fires.

5.4 Second pass: two-hop fetches Table 3, generation closes the loop

The orchestrator’s feedback machinery sees pending_references = ["Table 3"] and runs the two-hop pattern (Article 11). Page 9 carries Table 3: Variations on the Transformer architecture. The relevant rows for this question are:

Row (D): varies Pdrop at 0.0 / 0.1 / 0.2.
Row (E): varies εls at 0.0 / 0.1 / 0.2, plus a positional-embedding variant.

Rows (A), (B), (C) vary attention heads, key dimension, and model size and are not relevant to the regularization question. The two-hop retriever pulls page 9 and joins it to the candidate set, then pdf_qa re-runs generation with Section 5.4 plus Table 3 in the context:

The Transformer paper uses three regularization techniques during training: 1. Residual Dropout -- Pdrop = 0.1, page 8 (Section 5.4, bold header) Validated in Table 3 row (D), page 9: varying Pdrop changes BLEU on newstest2013 (4.92 PPL / 25.8 BLEU at the base 0.1 value). 2. Attention Dropout -- Pdrop = 0.1, page 8 (same paragraph as Residual Dropout) Same Table 3 row (D) covers it: Pdrop is applied uniformly. 3. Label Smoothing -- epsilon_ls = 0.1, page 8 (Section 5.4, bold header) Validated in Table 3 row (E), page 9: varying epsilon_ls changes BLEU. The text notes this "hurts perplexity but improves accuracy and BLEU". Cardinality: Section 5.4 opens with "We employ three types of regularization during training" (page 7). All three are present in this list.

complete_answer_found=True, pending_references=[]. The orchestrator stops. The answer is structured (3 enumerated techniques), exhaustive (cardinality cue confirmed), and complete (each technique has both its definition page and the Table 3 row that varies it).

5.5 Cost breakdown

Indicative cost shape for a 15-page native PDF on a typical OpenAI-class model. The numbers are rough; what matters is the shape: the LLM calls dominate, everything else is sub-second.

Cheap parsing (PyMuPDF on 15 pages): well under one second.
Document profile (one fitz.open + TOC read): ~50 ms.
Combined retrieval (TOC + keyword + RRF fusion): a few hundred ms.
Listing aggregation + cardinality check: a few hundred ms.
Two-hop reference resolution (one regex sweep + a re-retrieve on page 9): under one second.
Two generation calls (gpt-4-class): ~2 to 4 seconds each.
Total: typically 5 to 9 seconds for a question that activates four patterns and loops once on a reference. The two generation calls drive almost all of it.

Without the dispatcher, you would either pay for every pattern on every call, or hand-code the routing for every question shape. Dense retrieval and adaptive parsing stayed OFF here because the profile said they were not needed; that decision sits in decide.py, not in the question itself.

6. Dispatched RAG vs autonomous agents

Section 3 noted that the feedback-loop shape is what most vendors call agentic RAG. The term is used three different ways, and choosing between them shapes the whole architecture.

Usage 1: agentic as marketing: Any pipeline more sophisticated than embed → retrieve → generate gets called agentic. The label is empty. We can ignore this usage.

Usage 2: feedback-driven control: The LLM produces signal (complete_answer_found, llm_discovered_keywords, context_structured), and deterministic Python code reacts to that signal. This is what we’ve built. The LLM is in the system but not in control of the system. Control stays in the dispatcher.

Usage 3: autonomous agents: The LLM has a set of tools and decides at each step which one to call next. The control loop is in the LLM itself. The Python code executes whatever the LLM requests.

The distinction between Usage 2 and Usage 3 is the architectural decision that matters most for enterprise RAG.

6.1 What an autonomous agent looks like

In Usage 3, the orchestrator above would be replaced by something like:

# Autonomous agent - what we are NOT building
tools = [retrieve_by_toc, retrieve_by_keywords, retrieve_dense,
         re_parse_with_camelot, follow_reference, ask_clarification]

state = {"question": question, "history": []}
while not is_satisfied(state):
    next_action = llm.choose_next_tool(state, tools)
    result = execute(next_action)
    state["history"].append((next_action, result))

The LLM decides which tool to call, with which arguments, in which order. The pipeline is generated at runtime by the LLM, not authored by the engineer.

This is appealing in theory: the LLM can combine tools in ways the engineer didn’t anticipate. In practice, for enterprise RAG, three things go wrong.

Reproducibility breaks: The same question on the same document can take different paths on different runs. For audit, compliance, legal review, this is disqualifying. “Why did the system retrieve this passage?” has no single answer when the LLM chose the path freely.

Costs explode: Each tool decision is an LLM call. Five to ten tool calls per question. At realistic scale, the cost is one to two orders of magnitude higher than the dispatcher pattern. For a system answering thousands of questions per day, this is the difference between affordable and impossible.

Debugging becomes guesswork: When an autonomous agent produces a bad answer, you have to read its reasoning trace to understand what went wrong. The trace is long, branchy, and not always coherent. Compared to the dispatcher pattern, where you can pinpoint exactly which activation rule fired or didn’t, autonomy is a step backward in maintainability.

6.2 What we keep from “agentic”

The valuable part of the agentic idea isn’t autonomy. It’s that the pipeline thinks about the question before searching, and reacts to its own outputs. Both of those are present in our composite pipeline:

The pipeline thinks about the question (Article 6, question understanding).
The pipeline reacts to its own outputs through feedback fields (Article 8, generation feedback).
The pipeline iterates when needed (section 3 above, bounded by the orchestrator).

What we don’t keep is the autonomy of the LLM in choosing tool sequences. That decision belongs to the dispatcher, in code, where it’s testable, auditable, and reproducible.

A more honest name is structured RAG or dispatched RAG. “Agentic” survives because the field has settled on it, but the architecture stays in code, not in the LLM.

6.3 When autonomy is the right choice

Autonomous agents have their place. They’re the right pattern when:

The set of tools is open and changes frequently. A research assistant that needs to combine retrieval, web search, code execution, calculator, etc., across very different question types.
The question space is too varied to dispatch deterministically. “Help me plan this trip” legitimately needs different combinations of tools each time.
Reproducibility isn’t a hard requirement. Consumer applications, exploratory tooling, internal R&D.

For enterprise RAG on documents, which is what this series is about, the structure of the problem is well-understood. We know what a document looks like, what kinds of questions get asked, what kinds of patterns help. The dispatcher pattern captures that knowledge. Autonomy adds cost and unpredictability without adding capability.

6.4 The team-level implication

Dispatched RAG has a property that autonomous RAG doesn’t: the team’s understanding of the problem is encoded in the dispatcher. When a new engineer joins, they read decide.py and learn how the team thinks about question types and pattern activations. When a question fails in production, the team adds a test case and updates the dispatcher. When a new pattern is added (say, table-comparison retrieval for cross-document questions), it gets a new activation rule.

An unaudited autonomous agent has no such artifact: its behavior emerges from the LLM’s reasoning at runtime, which doesn’t accumulate, doesn’t get reviewed, and doesn’t transfer between team members. This is part of why the dispatcher pattern has held up in production: the dispatcher is something a team can own, review, and hand off. The layer that sits on top, where the agent picks among patterns like the ones dispatched here, is follow-up work.

7. Conclusion

The architectural commitment that holds the four bricks together is one sentence: decisions live in decide.py, not in an LLM prompt at runtime. The orchestrator runs the bricks in order, the feedback-loop machinery turns generation’s structured output into a bounded retry decision, and the dispatcher picks the patterns from the parsed question and the document profile.

The remaining articles address what surrounds the pipeline rather than what is inside: scaling from one document to a corpus (Part IV), and evaluating, running, storing, and securing the system in production (Part V).

8. Sources and further reading

The workflow-versus-agent debate was named by Anthropic in Building Effective Agents (Dec 2024). The dispatcher in this article is a workflow in that sense. The reflection-token idea from Asai et al. (Self-RAG, ICLR 2024) shows up directly in the structured feedback fields the orchestrator reads. The agentic side, with the patterns dispatched here as the agent’s audited toolkit, is follow-up work.

Earlier in the series:

Document Intelligence: series intro. What the series builds, brick by brick, and in what order.

What works, what breaks

Baseline Enterprise RAG, from PDF to highlighted answer. The four-brick pipeline end to end: PDF in, highlighted answer out.
Embeddings Aren’t Magic: The Predictable Failure Modes of RAG Retrieval. Where embedding similarity wins (synonyms, typos, paraphrase), where it predictably breaks (unknown terms, negation, term-vs-answer relevance), and how to use it anyway.
Rerankers Aren’t Magic Either: When the Cross-Encoder Layer Is Worth the Cost. What a cross-encoder adds over bi-encoder embeddings, measured, and when it is worth the latency.
RAG is not machine learning, and the ML toolkit solves the wrong problem. Why chunk-size sweeps and finetuning optimize the wrong thing; route by question type instead.
From regex to vision models: which RAG technique fits which problem. Two axes, document complexity and question control, that pick the technique for each case.
10 common RAG mistakes we keep seeing in production. Ten production mistakes, organized brick by brick, with the fix for each.

Document parsing

Beyond extract_text: the two layers of a PDF that drive RAG quality. The first half of the parsing brick: the document’s nature, signals, and summary.
Stop returning flat text from a PDF: the relational tables RAG needs. The second half of the parsing brick: the relational tables every downstream brick reads.
When PyMuPDF can’t see the table: parse PDFs for RAG with Azure Layout. The same tables from Azure Layout: native table cells, OCR, paragraph roles.
Parse PDFs for RAG locally with Docling: rich tables, no cloud upload. The same tables computed locally with Docling: TableFormer cells, nothing leaves the machine.
Vision LLMs are PDF parsers too: reading charts and diagrams for RAG. Vision as a parser: the pictures become searchable text.
Parse scanned PDFs for RAG with EasyOCR: free OCR gives you words, not a document. Where traditional OCR stops: text recovered, structure lost.
Making a PDF’s images searchable for RAG, without paying to read them all. The image cascade: filter cheap, classify, describe only what is worth reading.
Reconstructing the table of contents a PDF forgot to ship, so RAG can scope by section. Rebuilding toc_df when the PDF prints a contents page but has no outline.

Question parsing

RAG questions need parsing too: turn the user’s string into briefs for retrieval and generation. The thesis of question parsing: why a user string needs the same parsing as a document, and how it splits into a retrieval brief and a generation brief.
What the question parser extracts from a user string: keywords, scope, shape, decomposition, clarification. The five families of columns the parser reads straight from the user’s question, with the code that fills each one.
Dispatching the parsed RAG question: chunk strategy, model tier, activations, audit. The decisions the parser makes on top of the user string, using the document’s profile: dispatch, activations, full schema, the audit trail (pipeline_trace.json), and a broker-corpus walkthrough.
The Clarification Loop and Learned Defaults: When the Question Is Not Precise Enough. One focused clarification when the question is too vague, and the default learned from the answer.
Context engineering for RAG question parsing: from a raw question to typed fields that steer retrieval and generation. What enters the question-parse call and the typed fields that come out, steering retrieval and generation.

Retrieval

Retrieval is filtering, not search: a mental model for enterprise RAG. Retrieval reframed as filtering on line_df and toc_df: anchors small, context large.
Anchor detection for RAG: parallel detectors, then one LLM call at the end. Parallel anchor detectors: keyword always, embeddings alongside, one LLM call at the end.
Letting an LLM pick the right RAG page: the arbiter pattern at the end of retrieval. The LLM arbiter: candidates ranked with reasons, one typed JSON out.
Context Engineering: The Four Typed Inputs Behind Every Answer. Context engineering given a structure: the four typed pieces (fixed system prompt, retrieved lines, doc-context block, PromptContext wrapper) that fill one single-document RAG LLM call.

Generation

Stop returning text from RAG: the typed answer contract that prevents hallucination. The answer schema as the contract: typed values, items with evidence spans, self-assessment fields, and the completeness signal the pipeline computes itself.
Assemble each RAG generation prompt from a base prompt plus the rules each question needs. The dispatcher: a fixed BASE prompt plus the rules each question needs, the schema picked from the registry, and the full trace kept on every call.
Validating the RAG answer before the user sees it: spans, quotes, and the feedback loop. The post-generation validator (spans, verbatim quotes, formats), not-found as a first-class answer, and the feedback loops that close the pipeline.

One-document pipelines

A production RAG pipeline for PDFs: relational parsing, TOC retrieval, typed answers. Each of the four bricks upgraded one contract at a time: relational parsing, corpus-aware questions, TOC-routed retrieval, typed answers.
One RAG pipeline, four very different PDFs: same four bricks, every answer typed and cited. The four upgraded bricks wired into one call, run end to end on a paper, a compliance doc, and a broken-TOC document.
Loop engineering with adaptive PDF parsing: start cheap, pay for a heavier parser only when the page needs it. The escalation cascade and the free deterministic checks that flag a failed parse before you pay for a deeper one.
Loop engineering with adaptive parsing in action: flattened tables to Azure, figures to a vision LLM. The LLM as last line of defence, then two real escalations: a flat table to Azure, a figure to a vision model.
Loop engineering for cross-references: when RAG answers ‘see Section 7.2’ instead of the actual answer (link to come). When the answer says “see Section X”, the pipeline loops back and fetches it.
Loop engineering for listing questions: when the answer is every passage, not the top one (link to come). Listing questions: the answer is all the passages, not one, and the aggregation that finds them.

WRITTEN BY

angela shi
See all from angela shi

Deep Dives
Llm
loop engineering
Rag
Rag Architecture

Share This Article

Share on Facebook
Share on LinkedIn
Share on X

Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.

Write for TDS
