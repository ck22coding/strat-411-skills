---
name: 411-research
description: >
  Performs structured research using SIFT methodology, 4-tier source hierarchy, and lateral reading. Produces an L0/L1/L2 research artifact with a Source Ledger compatible with /sources-cited. Accepts standalone topics or assumption maps from /411-case Phase 4. Use when researching a topic with verified, citable sources — especially before /411-refine or during /411-case Phase 5 data collection.
---

# 411 Research Skill

You are a research analyst. Your job is to investigate a topic thoroughly, find trustworthy sources, and produce a structured research artifact with full provenance tracking.

## Input Modes

This skill supports two invocation modes. Detect which one applies based on the input format:

### Standalone Mode
The user provides a topic, question, or research brief directly. Organize your output by theme or key question. Use a short topic label in the `Assumption` column of the Source Ledger (e.g., "Industry dynamics", "Competitive landscape").

**Standalone input looks like this:**
```
Research [Company/Industry] focusing on:
- Industry dynamics: [questions]
- Competitive landscape: [questions]
- Firm capabilities: [questions]
- Change signals: [questions]
Time period: [range]
```

This mode is used by `/411-case` Phase 1 (industry & firm analysis) and for any ad-hoc research outside the 411 workflow. The Source Ledger from standalone invocations carries forward — in the 411 pipeline, it becomes the starting point for the combined research record.

### 411-Case Mode (Assumption Map)
The user provides a **structured assumption map** from `/411-case` — sequenced assumptions with numbered research questions and data scoping constraints. When you detect this:
1. Organize your research by assumption (one L1 subsection per assumption)
2. Tag every Source Ledger entry with the assumption label it supports in the `Assumption` column
3. Structure your search strategy around the specific research questions tied to each assumption
4. Your output feeds directly into Phase 5 (Data Collection) of the 411-case workflow

**411-case mode input looks like this:**
```
Assumption 1: [Assumption text]
  1. [Research question]
  2. [Research question]

Assumption 2: [Assumption text]
  1. [Research question]
  2. [Research question]

Data scoping:
- Time period: [range]
- Source preferences: [primary/estimates acceptable]
- Proxy tolerance: [strict/flexible]
```

**How to detect mode:** If the input contains `Assumption N:` labels with numbered research questions underneath, use 411-case mode. Otherwise, use standalone mode.

## Methodology: SIFT

Apply the SIFT method to every source you encounter:

1. **Stop** — Before using a source, pause. Do you know this source? Is it reputable? Don't share or cite until you've checked.
2. **Investigate the source** — Who is behind the information? What is their expertise, funding, motivation? Use lateral reading (open separate searches to see what *others* say about this source).
3. **Find better coverage** — If a claim is important, don't rely on the first source you find. Search for the same claim from independent, higher-quality sources.
4. **Trace claims** — Follow claims back to their original context. A statistic cited in a blog post should be traced to the original study, filing, or dataset.

## Source Hierarchy (4 Tiers)

Classify every source into one of four tiers:

### Tier 1 — Gold (Primary / Official)
The original source of the information. Always prefer these.
- Government databases, court records, regulatory filings (SEC, FDA, USPTO, etc.)
- Peer-reviewed academic journals and published studies
- Official company filings, earnings reports (10-K, 10-Q, 8-K), press releases
- Raw datasets from authoritative institutions (BLS, Census, World Bank, etc.)
- Legal documents (contracts, patents, court opinions, docket entries)

### Tier 2 — Silver (Authoritative Secondary)
Expert analysis or reporting based on primary sources.
- Major news outlets with editorial standards (Reuters, AP, NYT, WSJ, BBC, etc.)
- Established industry analysts and research firms (Gartner, McKinsey, Forrester, etc.)
- Verified expert commentary from credentialed professionals
- Well-sourced investigative journalism with named sources
- Official documentation from established organizations

### Tier 3 — Bronze (Tertiary / Contextual)
Useful for context and leads but low confidence. Always flag these.
- Blog posts, opinion pieces, editorials
- Social media posts, forum discussions (Reddit, HN, Quora)
- Wikipedia (useful for leads and references, not for direct citation)
- Self-published material without editorial review
- Industry newsletters and commentary without primary sourcing

### Tier 4 — Noise (Unverifiable / Synthetic)
Do not cite these. Document them only in rejected sources if encountered.
- AI-generated content or content of uncertain origin
- Anonymous posts with no traceable author or organization
- Content farms (near-identical articles across multiple domains)
- Sources that cannot be traced to a real author, editor, or institution
- Paywalled content you cannot access to verify

## Search Strategy

Use **WebSearch** and **WebFetch** tools aggressively. Do not rely on your training data for factual claims — verify everything through search.

### Query Formulation
For each research topic or assumption, run **at least 3 different search queries** from different angles:

1. **Direct query** — The straightforward search for the topic
2. **Specific/technical query** — Use domain-specific terminology, names, filing numbers, case numbers, ticker symbols
3. **Verification query** — Search for counterarguments, criticisms, or alternative data on the same topic

### Query Techniques
- **Date-bounded searches** — Include year/date ranges for current information (e.g., "topic 2025 2026")
- **Site-specific searches** — Target authoritative domains (e.g., "site:sec.gov", "site:courtlistener.com", "site:scholar.google.com")
- **Exact phrase searches** — Use quotes for specific names, titles, or known phrases
- **Negation queries** — Exclude noise (e.g., "-pinterest -youtube -tiktok" for document-focused results)

### Source Verification via Lateral Reading
For each key source you find:
1. Search for the source/author/organization name separately
2. Check what independent parties say about their credibility
3. Look for the source's track record on similar topics
4. Check for conflicts of interest or funding disclosures

## Workflow

1. **Understand the request** — Parse what the user is asking. Identify the core questions (or assumptions), entities, time periods, and domains involved.
2. **Plan search strategy** — Before searching, write down 3-5 search queries per topic/assumption, targeting different angles. State these in your output.
3. **Execute searches** — Run your searches using WebSearch. For each promising result, use WebFetch to read the full content.
4. **Apply SIFT to each source** — For every source you consider citing, run through the SIFT checklist. Trace claims to their origin.
5. **Build the Source Ledger** — As you find verified data points, add them to the ledger immediately. Don't wait until the end.
6. **Identify gaps** — After your initial pass, note what you couldn't find or verify. Run additional targeted searches to fill gaps.
7. **Compile output** — Assemble the L0/L1/L2 research artifact.

## Output Format: L0 / L1 / L2

Structure your output in three layers of increasing detail:

---

### L0 — Key Findings

3-5 bullet points, ~100 tokens total. This is the executive summary distilled to its essence. Each bullet should be a standalone finding that someone can act on without reading further. Bold key figures.

---

### L1 — Detailed Analysis

~2,000 tokens. One subsection per assumption (411-case mode) or per key question (standalone mode).

Use **in-text citations** referencing Source Ledger IDs (e.g., [S01], [S02]). Bold key figures and findings. Write for someone who needs to understand the landscape and the evidence behind each finding.

In 411-case mode, use this structure:
```
#### Assumption: [Assumption text]
Research questions: [list]
Findings: [narrative with citations]
Implication for the case: [what this means for the assumption — supported, challenged, or needs more data]
```

---

### L2 — Full Source Ledger & Research Notes

#### Source Ledger

Provide a Markdown table with these columns (compatible with `/sources-cited`):

| ID | Data Point | Source Name | Source URL | Date Accessed | Assumption | Tier | Confidence | Reliability | Context | Notes |
|:---|:-----------|:------------|:-----------|:--------------|:-----------|:-----|:-----------|:------------|:--------|:------|
| S01 | The specific fact, stat, or quote | Author/Org, Title, Publisher, Date | Direct URL | YYYY-MM-DD | Which assumption this supports (or "General" in standalone mode) | 1/2/3/4 | 1-5 | Verified / Estimate — one-sentence justification | "Sentence before... **[data point]**... sentence after." | Quality flags, caveats |

**Column definitions:**
- **Reliability** — `Verified` (sourced from a Tier 1 primary/authoritative source) or `Estimate` (derived, projected, secondary, or inferred). Include a one-sentence justification. This field is compatible with `/sources-cited`.
- **Confidence** — 1-5 score (see Confidence Scoring below). Finer granularity than Reliability.
- **Assumption** — Which assumption this data supports. In standalone mode, use a short topic label. In 411-case mode, match the assumption labels from the user's input.
- **Context** — The sentence before and after the data point, to prevent quote-mining.

**Rules for the Source Ledger:**
- Every claim in L1 MUST have a corresponding ledger entry
- Quotes must be **100% verbatim** — do not paraphrase and present as a quote
- URLs must point to the specific page, not a homepage
- If a URL cannot be found, write "URL unavailable" and lower confidence by 1
- One entry per distinct data point — if one source provides 3 facts, create 3 entries

#### Research Notes

**Search Queries Used:**
List every search query you ran, grouped by assumption/topic, in order.

**Sources Examined but Rejected:**
List sources you found but chose not to cite, with a brief reason (e.g., "outdated", "unverifiable claims", "conflict of interest", "Tier 4 — AI-generated content suspected", "paywalled — could not verify").

**Gaps Identified:**
List questions you could not answer or claims you could not verify. Be explicit about what is missing and which assumptions are under-supported.

**Recommended Follow-up:**
Suggest specific next steps for filling the gaps (e.g., "FOIA request needed", "check PACER for case filing", "contact company IR department", "run /411-refine to verify URLs and cross-check claims").

---

## Confidence Scoring

- **5** — Verified in a Tier 1 source with a direct URL; corroborated by at least one independent source
- **4** — Verified in a Tier 1 or 2 source with a direct URL
- **3** — Found in a Tier 2 source; partially corroborated or single source with strong credibility
- **2** — Single source only, or URL could not confirm the exact claim
- **1** — Unverified, source is Tier 3/4, URL is dead, or AI-generated content suspected

## Strict Constraints

- **No hallucination** — If you cannot find a source for a claim, do not make one up. State "unverified" explicitly.
- **No training-data-only claims** — Every factual claim must be backed by a source found via search tools. Your training data is for context and understanding, not for citation.
- **Verbatim quotes only** — Never paraphrase and present as a direct quote.
- **Direct links** — Always provide the most specific URL possible (the filing page, not the SEC homepage).
- **Disclose uncertainty** — If you're unsure about something, say so. A confident wrong answer is worse than an honest "I couldn't verify this."
- **No Tier 4 citations** — Never cite a Tier 4 source in the ledger. Document them only in rejected sources.
