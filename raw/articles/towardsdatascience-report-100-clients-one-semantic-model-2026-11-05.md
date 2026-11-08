---
title: How to Report for 100+ Clients With One Semantic Model
author: [Val Ye]
source: Towards Data Science
source_url: https://towardsdatascience.com/how-to-report-for-100-clients-with-one-semantic-model/
published: 2026-11-05
captured: 2026-11-08
type: raw-source
status: captured
tags: [architecture, workflow, configuration, verification]
---

# How to Report for 100+ Clients With One Semantic Model

## Source

- URL: https://towardsdatascience.com/how-to-report-for-100-clients-with-one-semantic-model/
- Author: Val Ye (Lead BI Engineer, former media buying agency analytics team)
- Published: 2026-11-05
- Captured: 2026-11-08
- Retained material: structured secondary summary attributed to the linked article, not a verbatim article capture. The original prose, complete code specifications and extraction output are not retained here.
- Verification limit: direct access returned HTTP 403 during review; full-text fidelity and code details have not been independently checked. Do not use this summary as an exact quotation or as proof of the original implementation.
- Companion repository: the summary names `config-driven-reporting` with synthetic data and fictional clients (BrewBox, PulseFit, Juniper); no repository URL or code snapshot is retained, so these details remain unverified.
- Limitations: this is a practitioner report from a media buying agency. Reported efficiency improvements (~70% reduction in dashboard build time, ~33% reduction in weekly reporting workload, 100+ clients served) are self-reported author claims, not independently verified causal benchmarks. Platform implementations and synthetic datasets serve as design examples rather than default system standards.

## Secondary summary — not original article text

The following sections are paraphrases, not quotations. Implementation names and author-reported outcomes require checking against the original article or repository before adoption.

## Problem and reported outcome

Reporting to many distinct external audiences (e.g., agencies serving multiple clients, consultancies with distinct engagements, or enterprises reporting across brands/business units) frequently results in creating a separate dashboard or report per audience.

The resulting operational friction:
- About ten analysts each carried between 8 and 20 client accounts; every account had its own report copy.
- Growth required adding another analyst for every 10 new clients (linear headcount scaling).
- Copied formulas and slight variations caused metric definitions to drift silently.
- Traditional metrics layers assume a single organization with unified vocabulary, consistent calendars, and homogeneous data schemas. They fail when 100+ unrelated clients share one model while using different names for metrics, watching different KPIs, and providing inconsistent subsets of data.

The replacement architecture used one shared dimensional model, one metric catalog, one report template, and a lightweight per-client configuration record:
- Build time for client dashboards fell by roughly 70% (from hours to minutes).
- Weekly reporting maintenance work fell by approximately one-third.
- The single report template scaled to serve more than 100 clients.
- Definition drift ceased, account coverage became interchangeable across analysts, and configuration records became joinable database tables for cross-account operational analytics.

## Core architecture and design mechanisms

### 1. Fixed dimensional model and grain

The foundation is a single shared fact table at a strict, uniform grain: one row per `client`, `campaign`, `channel`, and `date`.

Key design rules:
- The fact table stores only additive raw measures (`spend`, `impressions`, `sessions`, `conversions`, `revenue`).
- Clients, campaigns, channels, and dates act as dimensions.
- The client is merely a filter dimension in queries (`where client = ...`), not a separate table, schema, or ETL pipeline.

### 2. The ratio trap: store parts, compute ratios dynamically

The fact table strictly excludes ratio columns such as CPA, ROAS, or conversion rate:
- Averaging daily ratios yields mathematically false results (e.g., averaging Monday CPA of $20 with Tuesday CPA of $100 gives $60, whereas total spend divided by total conversions yields the true campaign CPA of $33.33).
- For this design's ratios of additive measures, aggregate the components before division:
  `sum(numerator) / nullif(sum(denominator), 0)`
- This definition holds true across any requested aggregation level (day, week, channel, quarter), eliminating discrepancies between daily and weekly totals.

### 3. Decoupling mathematical definitions from client display names

Clients frequently agree on mathematical definitions but disagree on terminology (e.g., CPA vs. CPO; sessions vs. visits; ROAS vs. ROI):
- Mathematical formulas are defined once in a central metric catalog (`metrics.yaml`).
- Terminology, custom labels, and primary conversion types (e.g., `Trial`, `Install`, `Order`) are declared in each client's configuration (`clients.yaml`).
- Placeholders like `{conversion}` in catalog templates resolve dynamically from client configuration (e.g., producing "Cost per Trial" for BrewBox).
- Clients specifying different calculations under the same label (e.g., revenue/spend vs. profit/spend both called "ROI") map to distinct catalog formulas while reusing identical report slots.
- Reporting week starts (e.g., `week_start: monday`) are isolated in client configuration to ensure weekly aggregations match client expectations.

### 4. Dynamic KPI slots and goal-oriented templates

Report templates avoid hardcoding specific metric columns:
- The template defines generic slots (`KPI 1` through `KPI N`).
- The metric catalog bundles metrics into goal-oriented templates (e.g., CPA template: spend, conversions, CPA, sessions, CVR; ROAS template: spend, revenue, ROAS, conversions, AOV).
- A resolver merges selected templates in order and removes duplicates.
- Conditional column visibility hides unused slots, preventing empty columns.

### 5. Explicit input dependencies and missing data disclosure

External clients control what data they provide; third-party agencies do not own client tracking infrastructure:
- Every metric declares its prerequisite input columns in `metrics.yaml` (e.g., CVR requires `conversions` and `sessions`).
- Every client explicitly declares the columns it sends in `clients.yaml` (`sends: [...]`).
- The resolver cross-references wanted metrics with available client inputs. Supported metrics populate template slots; unsupported metrics are omitted.
- Missing metrics are explicitly listed on the report in a "Not shown" section stating the exact reason (e.g., `Conversion rate: needs sessions, which this client does not send`).
- This avoids displaying misleading zero values, prevents report crashes, standardizes client data intake, and turns complaints into clear data requests.

### 6. Managing heterogeneous data grains without fabrication

When data arrives at coarser granularities (e.g., a radio vendor sending weekly totals):
- Coarser data is stored in a separate fact table at the weekly grain.
- Finer-grained daily tables are aggregated upward to weekly totals and joined at the coarser grain.
- Weekly totals are never artificially spread or divided across days, as this fabricates unmeasured detail.
- Weekly sources whose week definitions do not align with the client's configured `week_start` fail the build rather than guessing realignment.

## Retrospective and evolution recommendations

Val Ye highlights three architectural improvements for modern implementations:
1. **Configuration in version control**: Store configuration records in Git with diffs, pull request reviews, and automated validation against actual data, rather than in CRM fields.
2. **Declare metric inputs from day one**: Formalize input dependencies as strict schema contracts rather than relying on setup-time manual judgment.
3. **Adopt mature semantic layers at scale**: For large teams, build upon established semantic layer tooling while maintaining the same core disciplines: fix the grain, declare metric inputs, and explicitly verify client data availability.

## Editorial implications for deterministic analytics and Agent architectures

These are local interpretations, not original article text or independently verified implementation requirements.

- Fix the operational grain early and enforce additive base measures in physical tables.
- Keep calculations strictly decoupled from display naming and presentation slots.
- For ratios of additive measures, divide aggregated components rather than taking an unweighted mean of per-row rates. Persisted ratios are not inherently invalid; their rollup semantics must be explicit. Distinct counts and other non-additive components require metric-specific recomputation.
- Enforce explicit input dependency checks; expose missing inputs transparently rather than guessing or defaulting to zero.
- Treat configuration files as first-class software assets subject to version control, schema validation, and review gates.
