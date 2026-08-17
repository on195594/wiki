---
title: Designing a Persistent Knowledge Layer That Refuses to Guess
author: Miodrag Cekikj
published: 2026-08-16
captured: 2026-08-17
type: raw-source
source: Towards Data Science
source_url: https://towardsdatascience.com/designing-a-persistent-knowledge-layer-that-refuses-to-guess/
status: captured
extraction: "Full rendered browser DOM main.innerText captured by the local gsummary workflow; cleaned source packet removed duplicate and boilerplate lines. Local summary: /home/lin/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260817-175356-Designing-a-Persistent-Knowledge-Layer-That-Refuses-to-Guess-3666181-660767840-summary.md"
---

# Designing a Persistent Knowledge Layer That Refuses to Guess

## Capture notes

- Source quality: full rendered article body.
- The Azure implementation is a worked example, not a Hermes architecture requirement.
- The property-insurance corpus, organizations, policies, people and figures are synthetic.
- Cost figures and the reported token break-even model are source-specific and should not be generalized as production evidence.

## Source text

ARTIFICIAL INTELLIGENCE
Designing a Persistent Knowledge Layer That Refuses to Guess

RAG Retrieves, It Never Remembers. A vendor-neutral blueprint for applications that accumulate understanding. Includes a complete Azure-native implementation (Microsoft Foundry, Azure AI Search, Cosmos DB, FastAPI) mapped to a property-insurance corpus.

Miodrag Cekikj
Aug 16, 2026
49 min read
Share
Photo by Will Grobbelaar on Unsplash

In my RAG-ING Ahead series I worked through a complete cloud-native retrieval stack: speech and document processing, chunking, embeddings, Azure AI Search, and an assistant layer sitting on top of it. That series answered the question I had at the time, which was essentially ‘how do I get a language model to answer questions about documents it was never trained on’?

The stack still works. Retrieval-Augmented Generation remains the most practical way to ground a model in private, domain-specific or recently changed information without retraining anything.[1] If you have a corpus and you need answers from it, RAG is still where you start.

But I have been running that pattern for a while now, on projects that lasted longer than a demo, and a different question started to bother me:

The system retrieves the same paragraph, reasons over it, produces a good answer — and then throws all that reasoning away. Tomorrow, someone asks a related question, and it does the identical work again, from scratch, at the same cost, with no guarantee of reaching the same conclusion.

My first instinct was to tune the machinery rather than question it. I experimented with different caching mechanisms based on embeddings: recognizing that an incoming question was semantically close to one the system had already answered, and serving the earlier response instead of paying for the full retrieval-and generation pass again. Semantic caching genuinely helps with cost and latency, and I would still recommend it. But it took me a while to admit what it actually is. It caches answers, not understanding. The cached response is exactly as disposable as the original one. Nothing about the system’s model of the domain has improved, and the moment a question falls outside the similarity threshold, the work starts from zero again. Whatever I tweaked, the main RAG architectural concept underneath remained the same.

Figure 1 – The semantic cache I was experimenting with. A hit is a shortcut past the pipeline; a miss starts from zero. Either way, nothing accumulates — the dashed box is the part that turned out to be missing. Image by author.

That is not a retrieval problem. Retrieval is doing exactly what it was designed to do. It is an architecture problem. There is nowhere in a standard RAG system for understanding to accumulate. No amount of caching, re-ranking or chunking strategy fixes that, because they all optimize the lookup, none of them gives the system a memory.

This article is about building that missing place. It is the result of my latest work and experimentation around RAG, GraphRAG and agentic reasoning over a corpus of documents, the point where the incremental tweaks stopped being enough and the design itself had to change. I will present it in three parts.

Part I is vendor-neutral. It describes the architecture as a design pattern: the layers, the object model, the failure modes it exists to survive, and the governance it demands. None of it depends on Azure, or on any particular database or model provider. If you are on AWS, GCP, or running Postgres with pgvector and a local model, the design still holds, and I would like it to be useful to you.

Part II is the Azure implementation. Service by service, with the reasoning for each choice, real infrastructure-as-code, and a running FastAPI application you can clone and deploy.

Part III is the demonstration. A synthetic property insurer called Ostermere Mutual, twenty-one interconnected documents, and three walkthroughs that show the pattern doing something a retrieval system genuinely cannot.

Everything in the dataset is synthetic. Ostermere Mutual does not exist. Neither does the regulator, the policy, the claims, the people, the wind zones or the figures. Nothing here is insurance, legal, underwriting or claims advice, and no page in the demo represents a real interpretation of any real policy.

Naming note: current Microsoft documentation uses Microsoft Foundry for the unified platform previously called Azure AI Foundry. I use Foundry throughout, while keeping the familiar Azure service names where they make the architecture easier to follow.

Part I – The design:

1. Where classic RAG works, and where it stops

2. Retrieval is not accumulated understanding

3. The three layers

4. What actually lives in the knowledge layer

5. The six failure modes

6. Writing knowledge is a different risk class

7. Query routing

8. When you should not build this

Part II – Implementing it on Azure:

9. Mapping the layers to services

10. Blob Storage

11. Document Intelligence

12. Azure AI Search

13. Cosmos DB

14. Microsoft Foundry

15. FastAPI on Container Apps

16. Identity

17. The ingestion lifecycle

Part III – The demonstration:

18. Ostermere Mutual

19. The scoped rule

20. The contradiction

21. The date of loss

22. The Obsidian vault

23. The cost argument

24. Governance

25. What I would build next

26. To sum it all up

The complete project (application, infrastructure, dataset and a ready-to-open Obsidian vault) is available in the accompanying GitHub repository at github.com/mcekikj/persistent-knowledge-layer, under the MIT license.

Part I – The design

A conventional RAG flow is simple enough to draw in one line.

Figure 2 – The classic RAG pipeline. Every question starts at the left. Nothing survives past the right. Image by author.

Documents are chunked, embedded, and stored in a vector-capable index. A question arrives, the system finds semantically or lexically similar chunks, and hands them to the model as context. The model, which knows nothing about your business, is temporarily made to look like it does.

This solves a real and important problem, and I do not want to undersell it. The organization’s private knowledge does not need to live in the model’s parameters. It is fetched when needed. That is a genuinely good idea and it is why the pattern spread so fast.

But look at what the architecture is optimized for. It is optimized for lookup at query time. Every question is treated as the first question anyone has ever asked.

Now consider a real user, working on a real problem, over several weeks:

What is Actual Cash Value?
How does it differ from Replacement Cost Value?
When can recoverable depreciation be paid?
Which earlier decision defined how we treat depreciation?
Which document introduced the exception, and why?
A colleague told me the threshold is 15 years. Is it?

A simple RAG application answers each of these independently. It retrieves chunks again, rebuilds context again, and asks the model to reason again. Each answer may well be good. But the synthesis is disposable, meaning that when the response is delivered, the understanding evaporates. Nothing about the sixth question is easier because the system already answered the first five.

And on the last question – is the threshold 15 years? – a retrieval system will do something worse than fail. It will find the chunk that says 15 years, and it will confidently tell you yes.

The analogy I keep coming back to is a researcher with a filing cabinet.

You ask a question. The researcher goes to the cabinet, pulls four documents, reads the relevant passages, and gives you a considered answer. This is genuinely useful. Then they put the documents back, throw away their notes, and forget the entire exercise. Tomorrow you ask a follow-up, and they start again at the cabinet.

A better researcher does something else while reading. They:

keep summaries of the important sources;
maintain a page for each recurring concept, and connect the concepts that turn out to be related;
write down decisions, and the reasoning behind them;
update a comparison when new evidence changes it;
record contradictions rather than quietly resolving them;
keep a running list of what they still cannot answer;
and keep a link from every claim back to the document it came from.

The first researcher is a query-time RAG system. The second is what I want to build.

This is close to the LLM Wiki pattern that Andrej Karpathy sketched out: raw sources stay where they are, while an agent maintains a set of Markdown pages (entities, concepts, comparisons, cross-references) that a human can read and navigate. Obsidian happens to be a convenient window onto the result.[2]

It is easy to get distracted by the Markdown here, so let me be precise about what the important idea actually is.

The important idea is not Obsidian. It is not even Markdown. It is that knowledge is compiled once into a durable artifact, instead of being reconstructed from raw chunks on every request.

That is an architectural claim, and it has architectural consequences.

I do not want to replace RAG. I want to give it somewhere to put what it learns.

The raw source is still the strongest thing you have whenever you need exact wording, a quotation, a clause reference, a newly uploaded document, or verification of something disputed. A generated page, however carefully maintained, is a derived interpretation. It is not evidence, and the moment you let it pretend to be evidence, you have built something dangerous.

So the design has three layers, and they answer three different questions.

Figure 3 – The hybrid knowledge architecture. Both layers derive from the same sources; neither replaces the other. Image by author.
Layer 	The question it answers 	Optimized for
Evidence 	What source material is relevant to this question, right now? 	Recall, exact wording, citation, freshness
Knowledge 	What has this system already worked out, and what does it currently believe? 	Continuity, relationships, synthesis, reuse
Orchestrator 	Which of those do I need to answer this safely? 	Routing, risk, temporal scope
Table 1 – The three layers and the question each one exists to answer. Neither replaces the other; they are optimized for different things. Table by author.

The distinction is practical, not philosophical. The evidence layer is a retrieval index. The knowledge layer is a maintained, structured, human-readable model of the domain. The orchestrator is the thing that knows a question about exact policy wording should go to the first, and a question about why we decided this should go to the second.

One rule holds the whole thing together, and it is worth stating on its own line:

A knowledge page is never a source. It is always traceable to one.

Break that rule and you no longer have a knowledge base. Instead, you have a collection of confident claims that nobody can verify.

The word wiki invites people to picture a folder of Markdown files. For a personal knowledge base that is genuinely fine. For an application, I want a structured store underneath, with Markdown as a view generated from it.

The object model I have settled on:

Figure 4 – The knowledge object model. Every derived object points back at the sources that justify it. Image by author.

Most of these are unsurprising. Three of them are the whole point, and I want to dwell on them.

Decision – because the why dies first

A decision object holds the rule, its scope, its effective date, its accountable owner, and its rationale, with a pointer to where the rationale came from.

That last field matters more than it looks. In my synthetic corpus, an underwriting update says a roof inspection is triggered above 15 years in one specific wind zone. The update does not say why 15. The reasoning exists in exactly one place: an email thread between an analyst and a head of underwriting, which explains that between 15 and 20 years, roof displacement in the severe-wind band runs about 3.4x the standard band, and which explicitly warns that people will read the number without the qualifier and apply it to the entire book.

An email is not a policy document. No retrieval system ranks it highly. And in eighteen months, when someone asks “why is it 15?”, that reasoning is gone — unless something deliberately preserved it.

Contradiction – a first-class object, not an error

This is the idea I would most encourage you to take away, whatever else you use from this article.

Real corpora contradict themselves. Two teams write two documents, both current, neither superseding the other, and they disagree. In any document set maintained by more than one team for more than a year, this is the normal state of affairs, not an edge case.

A retrieval system handles this catastrophically badly. It retrieves one chunk, or the other, or both, and then asks a language model to reconcile them in a single forward pass, under a system prompt that told it to be helpful. The model will produce an answer that will be fluent, confident, but it will have silently picked a side.

Worse, the heuristic it most naturally reaches for is the more recent document wins. That sounds sensible, and it is wrong. Recency is not applicability. A newer document may have narrower scope, may address a different product, or may have been written by a team with no authority over the question.

So, the contradiction gets its own object, with a status, both statements verbatim, their effective dates, an accountable owner, and an explicit field: why_not_resolved. The system’s job is to detect the conflict and refuse to settle it.

Open question – knowing what you don’t know

The natural companion. Some questions cannot be answered yet, often because they are blocked by contradiction. An open question that is visible is safe. The same question, quietly answered wrong, is the thing that ends up in a complaint file.

5. The six failure modes this architecture exists to survive

Here is the honest test of any architecture: what does it do that the simpler thing cannot?

I built the demonstration corpus specifically to answer that. It contains six distinct traps. A pure retrieval system falls into every one of them — and falls fluently, producing an answer that reads perfectly well.

5.1 Scoped supersession

A general rule says inspect roofs above 20 years. A later update says inspect above 15 years, but only in one wind zone, and only for new business.

Retrieval returns the 15-year chunk. The model says the threshold is 15 years. It is now demanding inspections on tens of thousands of ordinary roofs, and the broker complaints are entirely justified.

The knowledge layer stores a decision with scope: “New business only. Zone H3 only.” The number never travels without its qualifier.

5.2 Genuine contradiction

The Claims Handling Manual says trace-and-access costs are covered as standard up to €5,000 and handlers may authorize without referral. The Endorsement Catalogue says trace and access is an optional paid endorsement, not payable unless it is on the schedule.

Both documents are current. Neither supersedes the other. Different teams wrote them.

A RAG system picks one. The knowledge layer raises a contradiction, names an owner, and states that no answer is available.

5.3 Terminology drift

Across the corpus, the same concept appears as actual cash value, ACV, cash settlement basis and depreciated value. A broker email in the dataset literally lists six such terms and asks whether they are six things or one.

Without entity resolution, your wiki grows four separate pages that disagree with each other by omission. With it, one page, four aliases, and a query for any of them lands in the right place.

5.4 Effective-date scoping

A claim has a date of loss of 20 February 2026. A rule took effect on 1 March 2026. The rule cannot apply to that claim.

This one is my favourite, because a retrieval system has no defence against it at all. Semantic similarity does not encode time. The chunk about the 15-year threshold is maximally relevant to a question about roof age on that claim – and completely inapplicable. The system is not merely wrong, it is wrong in the most convincing possible way.

The fix requires the orchestrator to know that the question is about a date, and to select the documentation in force on that date, including keeping a superseded document that was live at the time.

5.5 Rationale loss

Covered above. The reasoning lives in an email, the rule lives in a guideline, while the connection between them lives nowhere.

5.6 Multi-hop

“Why was this claim triaged Level 1?” requires the claim notes, then the triage guideline, then the water-damage concept, then the policy clause. Four hops. Top-k similarity search does not traverse, it ranks. Typed relationships do traverse.

Put together, these six are the argument — not that the wiki is nicer, but that there is a class of question retrieval answers confidently and wrongly, and the knowledge layer catches it.

6. Writing knowledge is a different risk class than answering

Here is the thing that took me longest to internalize, and it changed how I think about the whole design.

A wrong chat answer affects one conversation. A wrong canonical concept page affects every answer that is later built on top of it, for as long as it stays wrong, and nobody notices, because it looks like knowledge.

The moment your system starts writing persistent knowledge, it has crossed from “retrieval application” into “system of record”, and it needs the controls that come with that.

Everything is a patch

The model never writes to the store. It proposes a patch. The application validates it and, where the change is consequential, a human approves it.

Figure 5 – The patch lifecycle. The model proposes, the application disposes. Image by author.

Note where “resolve a contradiction” sits: never automatic. If the system could resolve contradictions on its own authority, the contradiction object would be pointless.

Provenance is a chain, not a field
Figure 6 – If any link in this chain is missing, the page is a polished note, not a knowledge object. Image by author.

An object whose sources cannot be identified should be deleted, not corrected. You cannot fix something when you don’t know where it came from.

Staleness is a property you must track

A page can be correct on Monday and wrong on Friday because a source was superseded underneath it. So every derived object carries last_validated_at, and the source it was derived from carries superseded_by. When a source is superseded, everything derived from it is marked stale and must not be presented as current until it is re-derived.

7. Routing: which layer answers this?

Not every question needs both layers, and sending everything to both is how you build something expensive and slow.

Figure 7 – Query routing. The contradiction check is a gate, not a footnote. Image by author.

Two things about this diagram are deliberate.

First, the temporal check belongs before retrieval, not after. If you rank by similarity first and discard inapplicable results afterwards, the inapplicable documents have already consumed your top-k. In production, put the effective and superseded dates on the index and filter in the query itself, so the candidate set is constrained before ranking. The demo takes a shortcut here that I should own up to: it applies the date filter immediately after retrieval, which behaves identically at this corpus size but would quietly starve top-k on a large one. The principle stands that the demo trades it for a simpler index schema.

Second, the contradiction check is a gate on the way out. It does not matter which route the question took. If the topic is contested, the system stops. In code, that is roughly:

def query(self, question, requested_mode, top_k, as_of=None):
    mode = self.choose_mode(question, requested_mode)

    wiki_items = self._search_wiki(question, top_k) if mode in {"wiki", "hybrid"} else []
    evidence = self.evidence.search(question, top_k) if mode in {"evidence", "hybrid"} else []

    if as_of:
        # The date the question is ABOUT - not the date it is asked.
        evidence = self._filter_by_date(evidence, as_of)

    # Pull in every contradiction touching a retrieved concept, even if the
    # contradiction object itself did not rank. Someone asking about trace and
    # access gets the conflict whether or not they used the word "contradiction".
    contradictions = self._contradictions_for(wiki_items)
    warnings = self._warnings(evidence, contradictions, as_of)

    context = self._build_context(wiki_items, evidence, contradictions, as_of)
    answer = self.model.answer(question, context)
    ...

And the instruction that goes to the model is unambiguous:

UNRESOLVED CONTRADICTIONS. You MUST present both positions with their sources and state that the position is unresolved. You MUST NOT choose between them, and you MUST NOT prefer the more recent document - recency is not applicability.

I would rather you skip this architecture than misapply it, so let me be direct about the cases where simple RAG is the better engineering choice.

Stay with plain RAG when:

the corpus is small and queried rarely, so there is nothing to amortize;
users overwhelmingly want exact source lookup, not synthesis;
documents churn so fast that any derived synthesis is stale before it is used;
there is no cross-session knowledge worth preserving;
it is a prototype with a short life;
ingestion latency has to be minimal;
your organization cannot yet govern AI-generated persistent knowledge. This one is not a technical constraint and it is the one people ignore.

Build the knowledge layer when:

the same domain is queried repeatedly, by people whose work continues across sessions;
cross-source synthesis is normal, not exceptional;
decisions and their rationale must survive staff turnover;
exceptions, scopes and contradictions actually matter;
domain experts need to see and correct what the system believes;
an audit trail from answer to source is a requirement, not a nice-to-have.

This is a workload decision rather than a matter of new good, old bad, and the honest answer for a lot of applications is that you do not need this.

Part II – Implementing it on Azure

Everything above is deliberately portable. Now let me build it properly on Azure, the platform I work with daily.

Figure 8 – The Azure-native architecture. The colours match Figure 3: red is evidence-at-rest, blue is the retrieval layer, green is the knowledge layer. Image by author.
Responsibility 	Azure service
Immutable raw sources 	Azure Blob Storage
Scanned PDFs, tables, forms, layout 	Azure AI Document Intelligence
Chunk, keyword, vector and hybrid retrieval 	Azure AI Search
Chat and embedding model deployments 	Microsoft Foundry
Structured wiki state 	Azure Cosmos DB for NoSQL
API and orchestration 	FastAPI on Azure Container Apps
Event-driven ingestion 	Event Grid → Container Apps Jobs
Identity and secrets 	Entra ID, managed identity, Key Vault
Telemetry 	Application Insights
Human inspection of the knowledge 	Obsidian, over exported Markdown
Table 2 – Each responsibility mapped to the Azure service that carries it. Nothing here is exotic — the design is in how the pieces are wired together, not in the pieces themselves. Table by author.
Figure 9 – The deployed resource group in the Azure portal’s Resource visualizer: the Container App and its environment, Foundry, Cosmos DB, Application Insights, Key Vault, the managed identity, AI Search and the storage account. Screenshot by author.
10. Blob Storage – the one thing you cannot regenerate

Everything else in this architecture is derived. Chunks can be re-chunked. Embeddings can be re-embedded. The entire wiki can, in principle, be recompiled from scratch. The original documents cannot be recovered from anything.

So they get treated accordingly:

raw-sources/
    {workspace-id}/
        {document-id}/
            original-file.pdf          ← never rewritten
            extracted-content.json     ← Document Intelligence output
            ingestion-metadata.json    ← what ran, when, which model version

wiki-export/
        Home.md
        Concepts/ · Decisions/ · Contradictions/ · Sources/

In Bicep, the part that matters is three properties:

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-05-01' = {
  parent: storage
  name: 'default'
  properties: {
    // Originals must survive an ingestion bug. Versioning and soft delete are the
    // cheapest insurance available on the one artifact the system cannot regenerate.
    isVersioningEnabled: true
    deleteRetentionPolicy: { enabled: true, days: 30 }
    containerDeleteRetentionPolicy: { enabled: true, days: 30 }
  }

And on the storage account itself, one line that I would argue for in any production deployment:

allowSharedKeyAccess: false   // no connection strings, ever

The wiki-writing process must never be able to touch the originals. That is a provenance, audit and deletion-workflow requirement, and it is much easier to enforce with separate containers and narrow role assignments than with good intentions.

11. Document Intelligence – used selectively

My demo corpus is .txt and .md, so the application reads it directly. Real insurance documents are scans, forms, tables and signatures, and the layout itself is often load-bearing. A table of endorsement limits flattened into a paragraph is worse than useless.

Azure AI Document Intelligence gives you prebuilt and custom models that return text, tables, selection marks and structure.[3] My rule of thumb:

clean text and Markdown → a simple parser, no charge;
machine-readable PDFs → a PDF parser, if it is genuinely sufficient;
scans, forms, complex layout, tables → Document Intelligence;
always persist the extracted JSON next to the original and keep the page and span offsets so a citation can point at a location, not just a document.

That last point pays for itself the first time a compliance reviewer asks “where exactly does it say that?”

12. Azure AI Search – the evidence layer

Each indexed record carries both searchable text and its vector:

{
  "id": "INS-SYN-004-0",
  "workspace_id": "ostermere-insurance-demo",
  "source_id": "INS-SYN-004",
  "title": "High-Wind Zone Underwriting Update",
  "content": "For new Hearthmere business in zone H3...",
  "chunk_number": 0,
  "content_vector": [0.012, -0.008, 0.031, "..."]

Azure AI Search fits this design well for one specific reason: text and vector fields coexist in a single index, and a hybrid query runs the full-text and vector queries in parallel, fusing the rankings with Reciprocal Rank Fusion. Semantic ranking can then reorder the top results.[4]

That matters more than it might sound. In insurance, half the queries are conceptual (“what counts as sudden water damage”) and half are lexical (“what does HS-TA-01 cover”). Vector search is good at first and unreliable at second: embeddings are known to be weak with exact identifiers, clause numbers and product codes. BM25 handles those well but cannot handle paraphrasing. You want both, and you want them fused rather than chosen between.

from azure.search.documents.models import VectorizedQuery

vector_query = VectorizedQuery(
    vector=self.model.embed(query),
    k_nearest_neighbors=max(top_k, 10),
    fields="content_vector",
)

results = self.client.search(
    search_text=query,                                        # BM25 leg
    vector_queries=[vector_query],                            # vector leg
    filter=f"workspace_id eq '{self.workspace_id}'",          # security trim
    select=["id", "source_id", "title", "content", "chunk_number"],
    top=top_k,

Note the filter, because it is doing security work, not relevance tuning.

⚠️ Vector similarity is not authorization. Nothing about cosine distance respects your permission model. Security trimming must be a hard filter on an indexed field, applied at query time, on every single query. It must be applied identically to the knowledge layer and to the exported Markdown. A wiki page that synthesizes three documents the user cannot read is still a data leak, just a nicely formatted one.

For larger systems, integrated vectorization can move chunking and embedding into the indexer pipeline.[5] I keep the embedding calls in the application here purely, so the flow is visible and explainable in an article.

One sizing note from actually deploying this: the demo runs on the free Search tier, and vector plus hybrid search work fine there for a 21-document corpus. What the free tier gives up is the semantic ranker and managed-identity support on the service itself, both are conditionals in the Bicep, so treat basic as the floor for production and free as a perfectly good way to validate the design for nothing.

Figure 10 – Search Explorer over the insurance-evidence index on the free tier: 33 chunk documents, 763.9 KB of vector storage, and a hybrid query ranking the H3 rationale email (INS-SYN-018) first by @search.score. Screenshot by author.
13. Cosmos DB – the knowledge layer

Cosmos DB for NoSQL holds the structured wiki. The whole design fits in three decisions.

Partition key is /workspace_id. Every wiki object carries a type discriminator, so concepts, decisions, contradictions and open questions all live in one container. That means a single-partition query can pull an entire workspace’s knowledge with no cross-partition fan-out, which is exactly the access pattern this system has.

partitionKey: {
  paths: ['/workspace_id']
  kind: 'Hash'

No graph database — yet. People reach for Gremlin or Neo4j the moment they hear “relationships”. I would push it back. Explicit relationship records in a document store handle everything this system actually does: find neighbours, follow a typed edge, render a concept page with its links. That is one or two hops.

A graph store earns its place when deep traversal is itself the workload: multi-hop impact analysis, centrality, path-finding across a large network. If you are not doing that, you are paying for a second database and a second query language to avoid writing WHERE c.source_id = @id.

Serverless, for now. Billing follows consumed request units, which suits a demo and a spiky early workload. Move to provisioned throughput once you have measured real RU consumption, not before, and not because the word serverless is fashionable.[6]

Data-plane access uses Cosmos’s own RBAC system (SQL role assignments), which is separate from Azure RBAC and catches people out:

resource cosmosDataRole 'Microsoft.DocumentDB/databaseAccounts/sqlRoleAssignments@2024-11-15' = {
  parent: cosmos
  name: guid(cosmos.id, identity.id, 'data-contributor')
    principalId: identity.properties.principalId
    // 00000000-...-000000000002 is the built-in Cosmos DB Data Contributor
    roleDefinitionId: '${cosmos.id}/sqlRoleDefinitions/00000000-0000-0000-0000-000000000002'
    scope: cosmos.id

Combined with disableLocalAuth: true, there is no key to leak.

Figure 11 – The con-001 contradiction as it lives in Cosmos DB: status unresolved, both statements with their sources and effective dates, an accountable owner, and the reasons it stays open. A contradiction is a stored, queryable object, not a footnote. Screenshot by author.
14. Microsoft Foundry – models now, agents later

Foundry provides the chat and embedding deployments. The application talks to it through the Azure OpenAI v1 interface using the standard OpenAI Python SDK, which means no api-version parameter to chase every few months:[7]

from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider

credential = get_bearer_token_provider(
    DefaultAzureCredential(), "https://cognitiveservices.azure.com/.default"
client = OpenAI(base_url="https://YOUR-RESOURCE.openai.azure.com/openai/v1/", api_key=credential)

response = client.responses.create(model="YOUR-CHAT-DEPLOYMENT", input=prompt)

For this demo, the FastAPI app orchestrates explicitly: embed, retrieve, search the wiki, build context, call the model, validate, write. I did that on purpose since every step is visible, and you can put a breakpoint in any of them.

The natural evolution is Foundry Agent Service, where the same orchestration becomes an agent with a constrained toolset:[8]

search_evidence()
search_wiki()
get_concept()
check_contradictions()      ← the gate, as a tool
propose_wiki_patch()        ← proposes only; cannot apply
apply_approved_patch()      ← requires an approval token
export_obsidian_vault()

I would not hand an agent unrestricted database access on day one. Each tool enforces its own validation, authorization, logging and narrow input schema. Note that propose_wiki_patch and apply_approved_patch are separate tools: the agent can reach the first and cannot reach the second without a human in between. That separation is the whole governance model, expressed as an API surface.

For extraction, use structured outputs, which constrain the response to a JSON Schema instead of merely requesting valid JSON.[9] The difference becomes obvious the first time a production extraction returns almost-valid JSON.

I can report that from experience now, because deploying this stack produced two field notes worth passing on:

Truncated JSON, on the very first document. gpt-5-mini is a reasoning model, and its reasoning tokens are spent from the same max_output_tokens budget as the answer. With a 5,000-token cap, the extraction JSON arrived cut off mid-string. The fix in the repo: a 16,000-token budget, reasoning: {“effort”: “low”} for extraction work, JSON mode (text.format: json_object) to constrain the decoder, and one retry. A detail that cost me two failed seeding runs: the first full seed succeeded without JSON mode, then two later runs failed on different documents. Prompt-only JSON does not fail reliably – it fails intermittently, which is worse. Schema-constrained structured outputs remain the real fix; this is the pragmatic one.
A deployment naming quirk. An embedding deployment named identically to its model (text-embedding-3-small) came up healthy in every status check and then returned unknown_model on every single call, on both the v1 and the classic route. An identical deployment named embed-3-small worked on the first request. Chat deployments do not show the problem. The Bicep now keeps the deployment name and the model name as separate parameters, with this story in the description.

The API surface:

GET  /health
GET  /wiki                      list objects, filterable by type
GET  /wiki/contradictions       the contradiction register
GET  /wiki/{item_id}
POST /query                     { question, mode, top_k, as_of }
POST /ingest/text
POST /ingest/file
POST /cost-estimate
POST /export/obsidian
POST /export/obsidian.zip

One implementation detail that cost me some debugging time and is worth passing on: /wiki/contradictions must be declared before /wiki/{item_id}, or FastAPI matches the path parameter first and cheerfully looks for a wiki object with the id “contradictions”. Route order is significant.

Container Apps is the right runtime here because it is container-based without asking me to run Kubernetes.[10] The scaling choice is worth a word:

scale: {
  // For production, 1 warm replica avoids cold starts; for a demo, 0 costs nothing.
  minReplicas: minReplicas
  maxReplicas: 3

minReplicas is a parameter (default 1) because the right answer depends on what you are running. In production, scale-to-zero looks like free money and then charges you a cold start plus a model handshake on the first request after every scale-in. For a demo that is exercised from a developer machine, zero is exactly right — the validated deployment in this article ran at zero and cost nothing while idle.

16. Identity – no keys, anywhere

The whole deployment runs on a user-assigned managed identity with narrowly scoped roles, and every service has local auth disabled. The Container App gets AZURE_CLIENT_ID in its environment, DefaultAzureCredential picks it up, and no secret is ever issued to the application.

{ name: 'AZURE_CLIENT_ID', value: identity.properties.clientId }

This matters more in this architecture than in a plain RAG app, and it is worth spelling out why. A retrieval system reads. This system writes persistent knowledge that other answers will be built on. The blast radius of a compromised credential is not “someone read your documents” – it is “someone edited what your organization believes”. Treat the write path accordingly.

The full infra/main.bicep in the repo provisions everything: storage with versioning, AI Search with disableLocalAuth, Cosmos with serverless and SQL role assignments, Foundry with both model deployments, Key Vault, Log Analytics, Application Insights, the Container Apps environment and the app itself, plus the six role assignments that wire them together – and, when you pass your own deployerPrincipalId, a mirrored set for your user account, which is what lets the seeding script and the tests run from a developer machine without a single key.

az group create -n rg-wikirag-demo -l swedencentral
az deployment group create -g rg-wikirag-demo -f infra/main.bicep -p namePrefix=wikirag
Figure 12 – Full ingestion. Note steps 11-13: the existing wiki is loaded into the extraction context, which is what makes entity resolution possible. Image by author.

That detail in the middle is the one people miss. When the model extracts concepts from a new document, it must see what the wiki already knows. Otherwise, it invents “Cash Settlement Basis” as a brand-new concept, without knowing that actual-cash-value already exists with that exact alias, and your knowledge base quietly forks.

Entity resolution in the demo:

def _resolve_concept(self, name, aliases):
    """Exact id → title → alias.

    Without this, 'cash settlement basis', 'depreciated value' and 'ACV' each become
    their own page and the wiki fragments into synonyms. The demo stops at alias
    matching. A production system adds embedding similarity and an LLM adjudication
    step for the ambiguous middle, which is where the interesting failures live.
    """
    candidates = {name.lower(), *(a.lower() for a in aliases)}
    for concept in self.repository.list_items("concept"):
        if concept["id"] == slugify(name):
            return concept
        known = {concept["title"].lower(), *(a.lower() for a in concept.get("aliases", []))}
        if candidates & known:
    return None

The demo ships with a passing test that ingests a document using the phrase “depreciated value” and asserts that no new concept page is created, but it resolves onto the existing actual-cash-value.

And here is what happens without the stronger resolution steps, measured rather than argued. When I ran all twenty-one documents through live gpt-5-mini extraction on the deployed stack, the model proposed concepts that alias matching could resolve only partially. The result was 149 concept objects where the curated graph has 19 – a roughly 7x fragmentation factor. The machine-extracted concepts are not wrong, they are just named in ways no alias list anticipated (“Roof Inspection Requirement”, “EUR 5,000 authorization limit”). That number is the concrete argument for embedding similarity and LLM adjudication in the resolution chain.

Part III – The demonstration

The synthetic corpus is twenty-one documents for an imaginary property insurer. It is small enough to read in an afternoon and deliberately engineered so that the six failure modes from stage 5 are all live in it.

Class 	Documents
Policy & product 	Policy overview v1.2, superseded v1.1, Section 4 wording (escape of water), endorsement catalogue
Underwriting 	Roof guideline (20 yrs), H3 update (15 yrs), wind-zone register, referral matrix, surveyor panel note
Claims 	Triage guideline, claims manual ch.7, three claim files (CLM-1042, CLM-1108, CLM-1155)
Regulatory & compliance 	Veyland circular (fictional regulator), fair claims handling standard, knowledge provenance standard
Informal 	Two email threads, working-group meeting minutes, customer FAQ
Table 3 – The twenty-one-document synthetic corpus by class. The informal sources at the bottom are where the contradiction is recorded and where the only rationale for the 15-year threshold exists. Table by author.

Those informal sources are not decoration. The meeting minutes are where the contradiction is formally recorded as unresolved. The email thread is where the only explanation of the 15-year threshold exists. In my experience, this is exactly how real organizations work; the rules are in the documents, and the reasons are in someone’s inbox.

A note on data provenance: every document in the corpus is synthetic and written by me (polished with AI) for this article, so there are no licensing constraints on its use. The dataset ships with the repository under the same MIT license as the code.

Compiled, that corpus produces:

21 sources · 19 concepts · 28 typed relationships · 4 comparisons · 5 decisions · 2 contradictions · 4 open questions · 2 processes

19. Walkthrough one – the scoped rule
curl -X POST http://localhost:8000/query -H 'Content-Type: application/json' -d '{
  "question": "What is the roof inspection threshold?",
  "mode": "hybrid"
}'

Plain retrieval finds the H3 update, which says 15 years, and says “15 years”.

The knowledge layer returns the decision object:

  "id": "h3-roof-inspection-threshold",
  "type": "decision",
  "summary": "For new Hearthmere business in zone H3, request a roof inspection when the
              primary roof covering is more than 15 years old. Outside H3, the general
              threshold of more than 20 years remains in force...",
  "scope": "New business only. Zone H3 only. Does not apply to in-force policies
            written before the zone model existed.",
  "rationale": "Between 15 and 20 years, the frequency of total or near-total covering
                displacement in the severe-wind band runs at roughly 3.4x the standard
                band at the same roof age...",
  "rationale_source": "INS-SYN-018",
  "accountable_owner": "D. Lindqvist (Head of Property Underwriting)"

The number never appears without its scope. And the rationale, recovered from an email, is right there, which means that in eighteen months, when someone asks why 15, the answer exists.

The email’s author, incidentally, predicted this exact failure in writing:

<em>“Please do not let this become a general 15-year rule. If someone reads the update without the zone qualifier they will apply it to the whole book, we will demand inspections on tens of thousands of perfectly ordinary roofs, and the broker complaints will be entirely justified.”</em>

That is a synthetic quote I wrote to make a point, but I do not think it is an unrealistic one.

20. Walkthrough two – the contradiction

This is the one I would put in front of a sceptical architect.

curl -X POST http://localhost:8000/query -H 'Content-Type: application/json' -d '{
  "question": "Is trace and access covered under Hearthmere?",
  "mode": "wiki"

A retrieval system answers this. It retrieves a chunk (from the claims manual, or from the endorsement catalogue) and tells you either “yes, up to €5,000 as standard” or “only if you bought HS-TA-01”. Both answers are supported by a real document. Both are wrong, because the firm does not have a position.

The hybrid system responds:

  "answer": "The position is NOT SETTLED. The knowledge base holds an unresolved
             contradiction covering this question, so no answer is given...",
  "warnings": [
    "UNRESOLVED CONTRADICTION (con-001): Trace and Access - Standard Cover or Paid
     Endorsement? The system will not choose between the conflicting sources.
     Owner: Y. Tanaka (Product)."
  ],
  "contradictions": [{
    "id": "con-001",
    "status": "unresolved",
    "accountable_owner": "Y. Tanaka (Product)",
    "statements": [
      { "source_id": "INS-SYN-012", "locator": "Chapter 7.3",
        "effective_date": "2025-11-01",
        "statement": "Trace-and-access costs are covered as standard under Hearthmere,
                      up to EUR 5,000..." },
      { "source_id": "INS-SYN-008", "locator": "HS-TA-01",
        "effective_date": "2026-01-01",
        "statement": "Trace and access is an optional endorsement (HS-TA-01)...
                      Where it does not appear on the policy schedule, trace-and-access
                      costs are not payable." }
    "why_not_resolved": "Both documents are current. Neither supersedes the other. They
      were written by different teams. The Endorsement Catalogue is the more recent
      document, but recency is not applicability..."
  }]

Both statements. Both sources. Both dates. An accountable human being. And no answer, because there is no one.

That JSON is demo mode’s deterministic scaffold. Here is what the deployed stack does with the same question – gpt-5-mini, live, over Cosmos DB and AI Search:

There is an UNRESOLVED CONTRADICTION relevant to this question. Do not treat the issue as settled.

INS-SYN-012 (Chapter 7.3, effective 2025-11-01): “Trace-and-access costs are covered as standard under Hearthmere, up to EUR 5,000. Handlers should authorize reasonable expenditure up to this limit without referral.”
INS-SYN-008 (HS-TA-01, effective 2026-01-01): “Trace and access is an optional endorsement (HS-TA-01), limit EUR 5,000, indicative premium EUR 24. Where it does not appear on the policy schedule, trace-and-access costs are not payable.”

This contradiction is UNRESOLVED. Accountable owner: Y. Tanaka (Product) [con-001].

I cannot resolve or state whether trace-and-access is covered under Hearthmere because of the unresolved conflict above.

The model was not asked to be cautious in general. It was handed the contradiction object and one rule, and it followed the rule.

The second-order effect is the part I find genuinely interesting. Once a contradiction is a stored object, other things can depend on it. The corpus contains a policyholder question on claim CLM-1155 (is the leak-detection survey cost payable?) which cannot be answered until this conflict is resolved. So, it is stored as an open question with blocked_by: “con-001”.

The system knows why it cannot answer, and it knows who has to decide before it can.

21. Walkthrough three – the date of loss

Claim CLM-1108: storm damage, roof covering displaced, date of loss 20 February 2026. The roof is 18 years old. The property, under today’s classification, would be in zone H3.

Ask a retrieval system whether an inspection was required, and it will find the H3 rule (15 years, and 18 > 15) and tell you the roof was over threshold, and no inspection was on file. It sounds like a finding. It is the beginning of a wrongful declinature.

Because the H3 rule took effect on 1 March 2026. Nine days after the loss. And the policy was written in September 2025, before the zone model existed at all, so the property carried no zone classification on the day the roof came off.

curl -X POST http://localhost:8000/query -H 'Content-Type: application/json' -d '{
  "question": "What roof inspection threshold applied to this property?",
  "mode": "evidence",
  "as_of": "2026-02-20"

The as_of parameter is the date the question is about – not the date it is asked. With it set, INS-SYN-004 is excluded from the candidate set entirely. It was not in force. The applicable threshold was the general 20-year rule, the roof was 18 years old, it was under threshold, and no requirement was breached.

The same mechanism runs in the other direction. Ask about settlement basis with as_of: “2025-08-01” and the system retrieves the superseded policy v1.1, because that is the version that governed a loss on that date, and marks it:

  "source_id": "INS-SYN-009",
  "in_force_at_as_of": true,
  "note": "superseded today, but in force on 2025-08-01 - this is the version that
           governs a loss on that date"

Under v1.1, depreciation was not recoverable. Under today’s v1.2, it is. Same term, same policy, opposite answer – and the only thing that distinguishes them is a date that similarity search cannot see.

Both behaviours are covered by tests in the repo, and both reproduce on the live deployment. At as_of: 2026-02-20 the deployed model answered:

Short answer: The general >20-year inspection threshold applied. [INS-SYN-003]

Why: On 2026-02-20 the Hearthmere guideline required an inspection when the primary roof covering is more than 20 years old [INS-SYN-003]. The H3 15-year threshold … did not take effect until 1 March 2026; this policy was written 14 Sep 2025 (so the H3 rule did not apply to it) and the roof was ~18 years old at loss. [INS-SYN-018] [INS-SYN-013]

And at as_of: 2025-08-01:

Settlement basis: Actual Cash Value (ACV) – defined as replacement cost less depreciation – for eligible building claims under Ostermere Hearthmere v1.1. [INS-SYN-009]
Is depreciation recoverable? No. Under v1.1 depreciation is not recoverable after repair. [INS-SYN-009]

They are the two tests I would keep if I had to delete every other one.

One more, live and unscripted: the multi-hop question

Section 5.6 claimed that typed relationships let the system traverse where similarity search only ranks. I had not scripted a demo for it, so I asked the deployed stack directly: “Explain why the CLM-1042 water loss was placed at triage Level 1 under the property claim triage process.” The answer walked the whole chain:

Governing Level-1 criteria: Level 1 – Standard is defined as “Minor visible damage, no safety concern, no continuing water entry, and estimated exposure below EUR 5,000” [INS-SYN-002].
How CLM-1042 matches those criteria: property remained habitable, no reported electrical fault [INS-SYN-005]; water flow stopped within approximately 40 minutes [INS-SYN-005]; damage confined to the water path [INS-SYN-005; INS-SYN-014]; initial repair estimate EUR 3,800, under EUR 5,000 [INS-SYN-005; INS-SYN-002].
Supporting operational guidance: the Claims Handling Manual lists indicators of a sudden escape of water … which align with CLM-1042’s facts [INS-SYN-012]. CLM-1155 explicitly contrasts CLM-1042 as a datable, sudden failure [INS-SYN-014].
Note on provisional status: coverage and exclusions remain subject to a formal coverage determination by an authorized claims professional [INS-SYN-005].

Four sources, four hops, and the human-decision boundary preserved at the end without being asked for.

One honest observation from the same session: my first phrasing of that question (“…and how does the water damage cover apply to it?”) got gated by the contradiction – CLM-1042’s evidence touches the contested trace-and-access concept, so the system presented con-001 and declined to make a settled determination instead of answering the triage part. The gate errs on the side of stopping. For a claims workflow I consider that the right default, but it is a real trade-off: an aggressive gate will sometimes hold back an answer the user legitimately needed and tuning that boundary is part of operating the system.

22. Seeing it: the Obsidian vault

The application exports the entire Cosmos DB state into a vault. Fifty-five pages, all generated, nothing hand-written:

obsidian_vault/
    Open Questions.md
    Concepts/          19 pages
    Sources/           21 pages
    Decisions/          5 pages
    Comparisons/        4 pages
    Contradictions/     2 pages   ← con-001, con-002
    Processes/          2 pages
Figure 13 – A slice of the generated knowledge graph. The red cluster is the unresolved contradiction and everything it blocks. Image by author.
Figure 14 – The generated vault’s graph view: 55 pages, all produced by the exporter from the structured store. Concepts, comparisons, contradictions and sources form one connected map, with Home as the hub. con-001 and con-002 sit inside it as ordinary nodes, not footnotes. Screenshot by author.

Open the folder in Obsidian, and you can navigate links, inspect backlinks, follow the graph, spot orphan pages, and, most importantly, see what the system believes and tell it that it is wrong.

That last capability is, I think, the strongest argument for this entire architecture. A vector index is operationally excellent and completely opaque to a domain expert. You cannot hand an underwriter a 1,536-dimension embedding and ask, “does this look right to you?” You can hand them a Markdown page that says the threshold is 15 years, but only in H3, and only for new business, and here is why, and here are the four documents it came from.

They will tell you within thirty seconds whether it is right. Markdown makes the memory auditable by the people who actually know the domain. No other part of the stack does that.

23. The cost argument, honestly

The knowledge layer costs more at ingestion. I am not going to pretend otherwise.

A RAG pipeline extracts and embeds each document once. The hybrid pipeline additionally summarizes, extracts concepts and claims, resolves entities against the existing wiki, generates relationship and comparison patches, validates, and regenerates Markdown. The write amplification is real, and it is not small.

The argument is that this front-loaded cost buys down repeated query-time reasoning. So, the question is not whether the wiki costs more to build (it plainly does) but whether the compilation is amortized across enough future use.

The model in cost_model/cost_model.py:

Compilation = D × Td × M
Simple RAG = Q × Tr
Hybrid = Q × (Tw + V × Tv)

With the illustrative defaults – 50 documents, 6,000 tokens each, 1,000 questions, 6,000 retrieved context tokens per RAG question versus 1,350 wiki context tokens, raw verification on 25% of questions:

Measure 	Tokens
Source corpus 	300,000
Wiki compilation 	501,000
Simple RAG, 1,000 questions 	6,000,000
Hybrid, 1,000 questions 	1,725,000
Context saved 	4,275,000
Break-even 	~117 questions
Table 4 – Token volume for the illustrative defaults: 50 documents, 1,000 questions. Compilation costs 501,000 tokens up front and saves 4,275,000 at query time, breaking even at roughly 117 questions. Table by author.
Figure 15 – The hybrid line starts above zero: that is the compilation cost. It crosses at roughly 117 questions. Image by author.

Now the caveats, because a chart like this can easily mislead:

This is token volume, not price. It ignores output tokens, embedding costs, AI Search capacity, Cosmos RUs, Container Apps compute, and Document Intelligence pages.
It treats every token as equal. In practice, ingestion and answering can use different model classes, and that is where much of the real saving lives, because a small model can answer from concise wiki context while a stronger one is reserved for reconciliation and updates.
It does not guarantee anything. A badly governed agent that rewrites the whole wiki on every ingestion will erase any saving you modelled. The economics depend entirely on disciplined update policies.

One measured data point, from deploying this exact stack: ingesting all twenty-one documents through live gpt-5-mini extraction and embeddings, running every walkthrough in this article, and regenerating the vault from Cosmos DB cost roughly $0.20-0.30 in total. The idle stack – free-tier search, scale-to-zero Container App, serverless Cosmos – burns about $0.05 a day. At this corpus size the compilation cost is coffee money. The economics only become interesting at scale, which is what the model above is for.

Figure 16 – Cost analysis for the resource group over the full validation period: $0.16 in total, effectively all of it gpt-5-mini tokens. Cosmos DB, Storage and Log Analytics register in cents, and the free-tier search at zero. Screenshot by author.

The context-size assumption also survived contact with the deployed system. Measured across a set of conceptual questions on the live stack, the wiki context averaged roughly 500 tokens against roughly 1,750 for the equivalent evidence context – a 3.5x ratio, in the same range as the 4.4x the model assumes. The absolute numbers are smaller than the model’s, because the synthetic documents are short. The ratio is the part that transfers to a real corpus. If anything, the measured ratio is slightly more conservative than the assumed one, which moves the break-even later, not earlier — worth knowing before you quote the model at a budget meeting.

Run /cost-estimate with your own assumptions. Then throw them away and use telemetry from your actual corpus and query mix, priced with the current Azure calculator.[11]

And honestly, the token argument is the weakest argument for this architecture. The real returns are:

consistent terminology across sessions and across people;
decisions and rationale that survive the person who made them leave;
contradictions that are visible instead of silently resolved;
an audit trail from any answer to its source;
a knowledge artifact a domain expert can review;
continuity across agent sessions and across model upgrades.

I would take over a few million input tokens.

24. Governance, restated

Because the system writes, it needs to control a read-only system does not.

Preserve provenance. Every statement traces to a chunk, to a span, to a document, at the version it was derived from.

Patch, never write. The model proposes; deterministic validation and, for anything consequential, a human disposes.

Detect staleness. last_validated_at, superseded_by, source_effective_date. When a source is superseded, everything derived from it is stale until re-derived.

Trim security at every layer. Blob paths, search records, Cosmos objects, Markdown exports, agent tools, caches, telemetry. Consistently. A synthesized page must never surface information the reader could not access in the source.

Keep the human decision human. In the demo, the AI may summarize an intake, retrieve policy evidence, identify missing information, propose a provisional triage level and flag conflicting rules. It may not determine coverage, decline a claim, assess fraud, rate a risk, resolve a contradiction, or tell a customer a decision has been made.

The synthetic working-group minutes contain the best articulation of this that I managed to write, and I will let it stand as the governance principle for the whole architecture:

Handlers currently adopt the assistant’s proposed triage level in roughly 90% of cases, which is fine, but only because they are reading the intake themselves. Removing the handler from the loop removes the thing that makes the 90% trustworthy.

That is the trap in one sentence. An automated system earns credibility under human review, and then that credibility is used as the argument for removing the review.

The repo is a baseline, not a product. The gaps I am most conscious of:

Event Grid and queue-driven async ingestion (the demo ingests synchronously because it is easier to run locally).
Document Intelligence with page and span preservation, so citations point at locations.
Strict JSON Schema structured outputs on every extraction and patch.
Entity resolution with embedding similarity and LLM adjudication, not just alias matching.
A human approval UI for high-risk patches: right now the lifecycle exists in the design and the low-risk path exists in the code.
Foundry Agent Service tools, with propose and apply as separately-permissioned surfaces.
Evaluation sets for retrieval, synthesis and the hard one: update accuracy. How do you test that a knowledge base changed correctly?
Freshness and contradiction dashboards. A contradiction register nobody looks at is just a log file.
Per-tenant security trimming, end to end.
Model routing by task complexity and risk.

Number 7 is the genuinely open research problem, and I do not have a good answer to it yet.

RAG is the evidence engine of this architecture, and nothing here is its obituary. It gives the model access to original, relevant, current source material, and there is no substitute for that.

What it does not do is remember.

The knowledge layer adds the thing that was missing: a maintained, structured, inspectable representation of what the system has already worked out, with the scopes intact, the rationale preserved, the contradictions visible, and a line back to the evidence for every claim.

RAG asks: What should I retrieve for this question?

The knowledge layer: What should be durably true after processing everything so far?

The orchestrator: Which of those do I need to answer this safely, right now?

On Azure that separation maps cleanly:

Blob Storage preserves the originals — the only thing you cannot regenerate.
Document Intelligence extracts the difficult content and keeps the spans.
Azure AI Search stores retrievable, security-trimmed evidence.
Cosmos DB stores the evolving concepts, relationships, decisions and contradictions.
Microsoft Foundry provides the models, and the path to agents.
FastAPI on Container Apps runs the orchestration, the temporal scoping and the contradiction gate.
Obsidian makes the whole thing visible to the people who know whether it’s right.

It is more work than simple RAG, and it costs more to ingest. In exchange you get organizational memory, consistent synthesis, explicit relationships, a visible decision history, and, the part I keep coming back to, a system that will tell you “two of our documents disagree and nobody has decided yet” instead of confidently making something up.

That last capability is not a feature. It is the reason to build it.

The application is no longer searching a pile of documents. It is slowly building a reviewable model of a domain, while keeping the original evidence close enough to check every important conclusion against.

Thank you for taking the time to explore this architecture with me. It turned into a longer piece than I intended, because the design kept having one more part worth explaining. The FastAPI project, the Bicep templates, the twenty-one synthetic documents and the Obsidian vault are all in the repository, and I strongly believe they give you a practical starting point for building a persistent knowledge layer of your own. Clone it, run it in demo mode without any Azure credentials, and try to break it — I would genuinely like to hear where it fails.

Disclosure: I am a Microsoft MVP. This article reflects my own independent work and opinions; Microsoft had no involvement in or review of its content. All Azure usage described is based on public documentation and my own deployment.

References

[1] P. Lewis et al., Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks (2020), NeurIPS 2020

[2] A. Karpathy, LLM Wiki (2025), GitHub Gist

[3] Microsoft, Document Intelligence Layout Model (2026), Microsoft Learn

[4] Microsoft, Hybrid Search Overview – Azure AI Search (2026), Microsoft Learn

[5] Microsoft, Integrated Vectorization in Azure AI Search (2026), Microsoft Learn

[6] Microsoft, Azure Cosmos DB Serverless (2026), Microsoft Learn

[7] Microsoft, Azure OpenAI v1 API Lifecycle (2026), Microsoft Learn

[8] Microsoft, Foundry Agent Service Overview (2026), Microsoft Learn

[9] Microsoft, Structured Outputs with Azure OpenAI (2026), Microsoft Learn

[10] Microsoft, Deploy a Flask or FastAPI Web App on Azure Container Apps (2026), Microsoft Learn

[11] Microsoft, Plan and Manage Costs of Azure AI Search (2026), Microsoft Learn
