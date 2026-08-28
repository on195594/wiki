---
title: Using OKF with Knowledge Catalog to serve context for agents
created: 2026-08-28
updated: 2026-08-28
type: raw-source
tags: [agent, knowledge-base, governance, context-engineering, lifecycle, cloud]
source: Google Cloud Blog
source_url: https://cloud.google.com/blog/products/data-analytics/scale-okf-bundles-across-an-organization-with-knowledge-catalog
author: Firat Elbey; Sam McVeety
published: 2026-08-26
captured: 2026-08-28
source_quality: full-official-blog-main-body
status: captured
extraction: Main article body captured via deterministic web extraction; promotional lead-in and trailing related-article/footer chrome omitted. Code and API examples are preserved as flattened Markdown. Local Gemini summary: ~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260828-193516-Scale-OKF-bundles-across-an-organization-with-Knowledge-Catalog-Google-Cloud-Blo-3535604-884852560-summary.md
---

# Using OKF with Knowledge Catalog to serve context for agents

## Source

- Publisher: Google Cloud Blog
- Authors: Firat Elbey; Sam McVeety
- Published: 2026-08-26
- Captured: 2026-08-28
- URL: https://cloud.google.com/blog/products/data-analytics/scale-okf-bundles-across-an-organization-with-knowledge-catalog
- Extraction route: deterministic web extraction; main article retained through `Getting started`, trailing related-article/footer chrome omitted.
- Source quality: complete official article main body.
- Limitations: this is a Google Cloud product article and synthetic Acme Retail example, not independent evidence that Knowledge Catalog is necessary or superior for Hermes. Product APIs, IAM roles, limits and setup commands are current as published and require current official-documentation verification before implementation. Flattened extraction may not preserve interactive loading widgets or original code-block formatting exactly.
- Local summary: `~/.hermes/projects/hermes-gsummary-workflow/runs/outputs/20260828-193516-Scale-OKF-bundles-across-an-organization-with-Knowledge-Catalog-Google-Cloud-Blo-3535604-884852560-summary.md`

## Captured source

Data Analytics

Using OKF with Knowledge Catalog to serve context for agents
============================================================

August 26, 2026

##### Firat Elbey

Group Product Manager, Data Analytics

##### Sam McVeety

Tech Lead, Data Analytics

We continue to iterate on the [Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) (OKF), an open specification that formalizes the [LLM-wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) into a portable, interoperable format. But a big question remains: How can you share and govern access to an OKF bundle across an organization?

OKF v0.1 established a portable format for the context agents need: markdown files with YAML frontmatter, one required field, and five conventions. Then, [OKF v0.2](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals) added the trust signals (provenance, verification, freshness, attestation) that a machine-authored bundle requires to be relied on, allowing a team to publish a trustworthy bundle for its own agents. 

However, what OKF does not answer is how teams share their bundles across an organization. A git repo per bundle is portable, but it is not searchable alongside the data it describes, it cannot be secured and governed using the same organizational identity and compliance policies, and it does not sit next to the technical metadata (schemas, lineage, ownership) that data teams already work in. Every downstream agent must know where each bundle resides, and that does not scale beyond a small number of bundles.

To scale an OKF bundle across an organization, you can use [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog), Google Cloud's context engine for agents. By mapping the bundle onto [Knowledge Catalog's existing types](https://docs.cloud.google.com/dataplex/docs/catalog-overview#terminology), every concept becomes discoverable, governed, and reachable by any agent already reading from the catalog.

### **Knowledge Catalog is the context engine for agents**

Every agent that queries Knowledge Catalog reads from one governed index over what the organization already has in BigQuery, Cloud Storage, operational databases, and applications. Each entry carries schema, lineage, ownership, and tags, and can be extended with typed aspects that add domain-specific fields. The same catalog exposes search and cross-project lookup to retrieve optimized context for each agentic query. The context retrieval is secure and governed by IAM controls, so agents can only see the entries they have access to based on IAM identity. 

Publishing an OKF bundle into Knowledge Catalog takes a one-time setup and a single push. Both use the OKF [sample code](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo/okf) in the Knowledge Catalog repository, whose wrappers call `gcloud dataplex` for setup and delegate push to `kcmd` (the Metadata-as-Code CLI in the same repository).

The setup registers three Knowledge Catalog resources: an EntryGroup to hold the bundle, an EntryType named `okf-bundle` for its concepts, and an AspectType named `okf` that carries the OKF signal fields (from the `okf-aspect.json` schema in the [sample code](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo/okf)). The push then creates one `okf-bundle` Entry per concept, each with two Aspects: an `overview` Aspect for the markdown body, and an `okf` Aspect for the structured signals. Display name, description, and tags live on the Entry itself. The bundle's `index.md` navigation files and its root `log.md` are also published as Entries: index files carry only the `overview` Aspect (no OKF frontmatter), and `log.md` carries both Aspects with `okf_type: Log`.

Everything Knowledge Catalog already does for technical metadata (search, IAM, lineage, cross-project discovery) applies equally to OKF bundles, alongside the data they describe.

### **The** **okf** **AspectType**

The [`okf-aspect.json`](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/toolbox/mdcode/demo/okf/okf-aspect.json) schema in the sample code defines the AspectType. It carries 13 fields covering the full [OKF v0.2 spec](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md):

| **#** | **Field** | **Type** | **Purpose** |
| --- | --- | --- | --- |
| 1 | `okf_type` | string | The OKF document type (freeform, e.g. `BigQuery Table`, `Metric`, `Attested Computation`). |
| 2 | `generated` | record `{by, at}` | Actor and timestamp for the last meaningful change. |
| 3 | `sources` | array of `{id, resource, title, author, usage_count, last_modified}` | Materials the concept derives from, with credibility signals. |
| 4 | `verified` | array of `{by, at}` | Verification events. A `human:` actor marks the highest trust tier. |
| 5 | `status` | string | Lifecycle state: `draft`, `stable`, or `deprecated`. |
| 6 | `stale_after` | datetime | Absolute point in time (RFC3339 with an explicit offset) on or after which the content is stale. |
| 7 | `usage_window` | record `{from, to}` | Period the source usage counts were measured over. |
| 8 | `runtime` | string | How an Attested Computation runs (e.g., `bigquery`). |
| 9 | `parameters` | array of `{name, type, required}` | Typed named holes a caller may fill. The only surface a caller may vary. |
| 10 | `computation` | string | Path to a file holding the computation body. |
| 11 | `executor` | record `{resource, receipt[]}` | How the computation runs and what evidence it must return. |
| 12 | `attester` | record `{resource}` | Deterministic code that takes a receipt and returns a verdict. |
| 13 | `extra` | string | Producer-defined frontmatter the template does not model, as JSON `[path, value]` pairs. Keeps the round-trip lossless. |

Every field is annotated with a display name, a description, and a mandatory index. Any top-level scalar field in the `okf` Aspect (`okf_type`, `status`, `stale_after`, `runtime`, `computation`, `extra`) can drive Knowledge Catalog search predicates directly, so `aspect:acme-analytics.us-central1.okf.okf_type=Metric` returns every OKF Metric in scope. Scalar subfields of record fields (`generated.by`, `usage_window.from`, `executor.resource`, `attester.resource`) also drive predicates. The array fields (`sources`, `verified`, `parameters`) are not server-side searchable on their subfields; agents narrow on them client-side after `entries.get` with `view=ALL`. One caveat for search predicates on `datetime`-typed fields (`stale_after`, `generated.at`, `usage_window.from`/`.to`), use a bare date (`stale_after=2026-12-31`) or a range comparison (`stale_after>2026-01-01`), not the full RFC3339 timestamp.

### **Pushing a bundle**

`kcmd push` reads an OKF bundle from git and writes each concept as an Entry in the target Knowledge Catalog EntryGroup. `index.md` files become Entries too, and each concept is parented to the index above it, so the bundle's directory structure survives as a browsable hierarchy.

`kcmd` expects a bundle in the Documents Layout: markdown files under a `catalog/` subdirectory, and a `catalog.yaml` at the bundle root that lists the snapshot's entry and aspect types. The [sample code](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo/okf)'s `setup.ts` generates `catalog.yaml` from its `--entry-group` flag (default `okf_demo`), so a reader wiring the sample to a new bundle passes the flag rather than editing `catalog.yaml` by hand.

Here is an end-to-end workflow for the [Acme Retail bundle](https://github.com/GoogleCloudPlatform/open-knowledge-format/tree/main/bundles/acme_retail) that we introduced in the [OKF v0.2 blog](https://cloud.google.com/blog/products/data-analytics/okf-v0-2-adds-trust-signals?e=48754805):

Loading...

# One-time setup (if required): install bun, clone the repo, build kcmd, configure gcloud
curl -fsSL https://bun.sh/install | bash
export BUN\_INSTALL="$HOME/.bun" && export PATH="$BUN\_INSTALL/bin:$PATH"
git clone https://github.com/GoogleCloudPlatform/knowledge-catalog
cd knowledge-catalog/toolbox/mdcode && npm install && npm run build
# Authenticate, set project and enable dataplex apis
gcloud auth login
gcloud config set project <your-project>
gcloud config set compute/region <your-location>
gcloud services enable dataplex.googleapis.com
gcloud auth application-default login
# Push the Acme Retail bundle
cd demo/okf
bun run setup.ts # creates the EG (default 'okf\_demo')
bun run push.ts # pushes okf/bundles/acme\_retail into the EG setup created

To pick a different EntryGroup name or push a different bundle, pass `--entry-group your-name` to `setup.ts` and `--bundle path/to/your/bundle` to `push.ts`. For example: `bun run setup.ts --entry-group acme-bundle` followed by `bun run push.ts`. This regenerates the manifest, so subsequent `push`, `pull`, and `cleanup` all target the new EG; delete earlier EGs manually with `gcloud dataplex entry-groups delete <name> --project <your-project> --location <your-location>`.

The [Acme Retail bundle](https://github.com/GoogleCloudPlatform/open-knowledge-format/tree/main/bundles/acme_retail) is a synthetic OKF bundle for a US retailer's BigQuery estate. It contains nine leaf concepts across six directories (`attesters`, `tables`, `metrics`, `computations`, `policies`, `skills`), each with its own `index.md`, plus a bundle root with its own `index.md` and `log.md`. That's 17 pushed Entries in total; Dataplex auto-creates one `<eg>_entry` alongside, so `gcloud dataplex entries list` returns 18 rows.

After the push completes:

* Every concept markdown file is a Knowledge Catalog Entry, discoverable by search across the whole project or organization, depending on IAM configuration.
* The `revenue-ytd` Attested Computation appears in the console with its sanctioned SQL, its executor, its attester, its verification history, and the full concept body.
* An analyst searching Knowledge Catalog for "revenue" finds Acme Retail's business definition alongside the BigQuery table it computes from, both under one permission model.
* A downstream agent that already calls LookupContext for BigQuery table Entries retrieves the bundle's context by adding the OKF entry names to its `resources` list.

Further, `metrics/revenue.md` becomes an Entry with two Aspects. The full `entries.get` response (with `view=ALL`) looks like:

Loading...

{
"name": "projects/acme-analytics/locations/us-central1/entryGroups/acme-retail/entries/metrics/revenue",
"entryType": "projects/acme-analytics/locations/us-central1/entryTypes/okf-bundle",
"createTime": "2026-08-15T00:48:39.123456Z",
"updateTime": "2026-08-15T00:48:57.234567Z",
"parentEntry": "projects/acme-analytics/locations/us-central1/entryGroups/acme-retail/entries/metrics/index",
"entrySource": {
"displayName": "Revenue",
"description": "Recognized revenue for a period, per Acme's FY2026 revenue-recognition policy. Backed by an Attested Computation.",
"labels": {
"finance": "true",
"revenue": "true",
"headline-metric": "true"
},
"location": "us-central1"
},
"aspects": {
"dataplex-types.global.overview": {
"aspectType": "projects/dataplex-types/locations/global/aspectTypes/overview",
"createTime": "2026-08-15T00:48:57.111111Z",
"updateTime": "2026-08-15T00:48:57.111111Z",
"aspectSource": {},
"data": {
"content": "# Definition\n\nRevenue for a fiscal year is the sum of `net\_amount` over orders that (a) reached `order\_status = 'delivered'`, (b) completed the 30-day return window, and (c) fall in the fiscal year by `order\_ts`. Multi-currency orders are converted to USD at the `order\_ts` daily reference rate. [^revenue-policy]\n\nThe sanctioned computation is [`computations/revenue-ytd.md`](../computations/revenue-ytd.md). Consumers MUST run and attest that computation rather than composing their own SUM. The attester rejects any receipt whose executed SQL does not match the sanctioned form.\n\n# Reporting cuts\n\n- \*\*By fiscal year:\*\* the sanctioned computation takes `year` as its sole parameter.\n- \*\*By channel or category:\*\* these are approved narrations, not new metrics. Join the receipt's row-level result to `orders.channel` or to `order\_lines` × `products.category` client-side. Do NOT rewrite the sanctioned SQL.\n\n# Trust and freshness\n\n- \*\*Verified:\*\* VP Finance sign-off on 2026-07-01, against the FY2026 policy.\n- \*\*Stale after 2026-12-31:\*\* Finance re-issues the revenue recognition policy each January. Consumers of this concept after 2027-01-01 MUST re-verify the definition against the new policy before serving.\n\n[^revenue-policy]: Revenue Recognition Policy (FY2026)",
"contentType": "MARKDOWN"
}
},
"acme-analytics.us-central1.okf": {
"aspectType": "projects/acme-analytics/locations/us-central1/aspectTypes/okf",
"createTime": "2026-08-15T00:48:57.222222Z",
"updateTime": "2026-08-15T00:48:57.222222Z",
"aspectSource": {},
"data": {
"okf\_type": "Metric",
"generated": { "by": "reference\_agent/gemini-2.5-pro", "at": "2026-06-30T14:00:00Z" },
"verified": [ { "by": "human:jsmith@acme", "at": "2026-07-01T09:00:00Z" } ],
"status": "stable",
"stale\_after": "2026-12-31T00:00:00Z",
"sources": [
{
"id": "revenue-policy",
"resource": "policies/revenue-recognition.md",
"title": "Revenue Recognition Policy (FY2026)",
"author": "human:jsmith@acme",
"last\_modified": "2026-06-15T00:00:00Z"
}
]
}
}
}
}

The `overview` Aspect holds the full body of `revenue.md`. The `okf` Aspect carries the structured signal fields, so agents get provenance, source, and OKF type in a form they can filter on directly instead of parsing markdown. Server-side searchEntries filters on the top-level scalar fields and on the scalar subfields of record fields; agents narrow further on the array-element subfields client-side after entries.get. (Aspects and EntryTypes are keyed by project number in real API responses and search predicates; the `acme-analytics` project ID is shown throughout for readability.)

### **What pushing your OKF to Knowledge Catalog enables**

Once the bundle is in Knowledge Catalog, it provides two capabilities to any agent that reads from the catalog:

* **Discoverability across the organization.** Agents find bundle concepts through the same searchEntries and LookupContext APIs they already use for cataloged data, so an OKF bundle appears alongside BigQuery tables and other resources in every query it matches.
* **Governance.** Bundle Entries inherit IAM from the EntryGroup, so a single agent call returns exactly what the caller is permitted to read, with no parallel permission model to maintain.

**Discoverability across the organization**OKF bundle Entries appear in searchEntries results alongside BigQuery tables and other cataloged resources, so an agent already querying the catalog picks up new bundles automatically. To retrieve a concept's body, trust signals, or linked concepts from a match, the agent moves to LookupContext and `entries.get`.

A LookupContext call looks like this:

Loading...

POST https://dataplex.googleapis.com/v1/projects/acme-analytics/locations/us-central1:lookupContext
{
"resources": [
"projects/acme-analytics/locations/us-central1/entryGroups/acme-retail/entries/metrics/revenue"
],
"options": { "format": "yaml", "context\_budget": "8000" }
}

The response is a single `context` field containing a pre-formatted YAML block. The block carries the entry's `catalogEntry`, its type, its description, its tags as labels, and its `overview`: the full markdown body of the concept, including its trust and freshness section. LookupContext does not render custom Aspects, so an agent that needs the structured OKF signal fields (`okf_type`, `generated`, `sources`, and the other ten) reads them with `entries.get` and `view=ALL` alongside the LookupContext call.

There is no repository clone, no manual Aspect merging, and no re-parse of frontmatter. The agent uses the same API call any Knowledge Catalog client already makes.

An agent traversing an OKF bundle typically follows a three-step flow. An agent that already knows the specific Entry names it needs skips step 1. An agent that already knows the target EntryGroup and wants to enumerate the bundle exhaustively substitutes `entryGroups.entries.list` for step 1.

1. searchEntries returns candidate Entry names and descriptions. Its `scope` accepts a project or organization; narrowing within that scope happens through query terms, including aspect predicates like `aspect:acme-analytics.us-central1.okf.okf_type=Metric`.
2. LookupContext on the top few Entry names (up to ten per call) returns the full concept body as pre-formatted YAML; `context_budget` caps the response size.
3. `entries.get` with `view=ALL` on any Entry returns its structured OKF signals (`okf_type`, `generated`, `sources`, and the other ten) directly, which the agent can then filter or attest on.

When a concept's `sources[]` references another concept by path, the agent calls LookupContext on that Entry name to walk the reference.

The full response for the Revenue Entry:

Loading...

resources:
-
catalogEntry: projects/acme-analytics/locations/us-central1/entryGroups/acme-retail/entries/metrics/revenue
type: OKF Document
description: Recognized revenue for a period, per Acme's FY2026 revenue-recognition
policy. Backed by an Attested Computation.
overview: |-
# Definition
Revenue for a fiscal year is the sum of `net\_amount` over orders that (a) reached `order\_status = 'delivered'`, (b) completed the 30-day return window, and (c) fall in the fiscal year by `order\_ts`. Multi-currency orders are converted to USD at the `order\_ts` daily reference rate. [^revenue-policy]
The sanctioned computation is [`computations/revenue-ytd.md`](../computations/revenue-ytd.md). Consumers MUST run and attest that computation rather than composing their own SUM. The attester rejects any receipt whose executed SQL does not match the sanctioned form.
# Reporting cuts
- \*\*By fiscal year:\*\* the sanctioned computation takes `year` as its sole parameter.
- \*\*By channel or category:\*\* these are approved narrations, not new metrics. Join the receipt's row-level result to `orders.channel` or to `order\_lines` × `products.category` client-side. Do NOT rewrite the sanctioned SQL.
# Trust and freshness
- \*\*Verified:\*\* VP Finance sign-off on 2026-07-01, against the FY2026 policy.
- \*\*Stale after 2026-12-31:\*\* Finance re-issues the revenue recognition policy each January. Consumers of this concept after 2027-01-01 MUST re-verify the definition against the new policy before serving.
[^revenue-policy]: Revenue Recognition Policy (FY2026)
labels:
finance: 'true'
revenue: 'true'
headline-metric: 'true'

**Governance**Permissions on the EntryGroup use standard Knowledge Catalog IAM. An agent that names both a bundle concept and the BigQuery table it grounds against in one call receives both, each subject to its own existing access control list (ACL), so the response carries only what the caller is already permitted to read. There is no parallel permission model to maintain.

Reading agents use `roles/dataplex.catalogViewer`, which grants the read paths: `entries.get`, LookupContext, and searchEntries. The identity that runs `kcmd push` uses `roles/dataplex.catalogEditor`, which grants the write paths: `entries.create` and `entries.patch`. One EntryGroup per bundle-owning team is the multi-team pattern, and IAM on the EntryGroup cascades to its Entries.

LookupContext resolves the entry names it is given, up to ten per call, within a single location. It does not follow links out of a concept's body, so an agent that wants a referenced concept must name it explicitly. Place the bundle's EntryGroup in the same location as the data it describes to fetch both in one call.

### **Lifecycle**

`kcmd push` is an idempotent upsert. Re-running is safe (no duplicates, no error), but every push writes every Entry. Concept deletes require an explicit `kcmd delete` on the Entry, or `cleanup.ts` to remove the whole EntryGroup at once; `cleanup.ts` deletes only the EntryGroup and its Entries, so the shared `okf` AspectType and `okf-bundle` EntryType stay in place for other bundles that reference them. For continuous ingestion in production, wire a CI job to `kcmd push` on every commit to the bundle repository, using a service-account credential with `roles/dataplex.catalogEditor` on the target EntryGroup.

### **Getting started**

OKF defines what a trustworthy bundle looks like. Knowledge Catalog makes it reachable across the organization. To get started, check out the following resources:

1. Read the [OKF v0.2 spec](https://github.com/GoogleCloudPlatform/open-knowledge-format/blob/main/SPEC.md) and browse the [Acme Retail bundle](https://github.com/GoogleCloudPlatform/open-knowledge-format/tree/main/bundles/acme_retail).
2. Author a small bundle for one domain your team owns.
3. Sync it into your Knowledge Catalog project using the [sample code](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/toolbox/mdcode/demo/okf)'s `setup.ts` (which registers the resources) and `push.ts` (which delegates to `kcmd`).
4. Point your existing agents at Knowledge Catalog. New context becomes reachable through the same LookupContext and searchEntries calls they already use.
