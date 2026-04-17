# Output Format Specification

Load this when compiling your output in Step 6 (and when building the Replacement Map in Step 4). This file owns the full format contract — SKILL.md only names the structure.

## Header

```
# 411 Re-Research: [Topic/Case Name]
## Iteration [N] — Targeted Gap-Fill
```

## Replacement Map (Step 4 output, reproduced at top of final output)

```
REPLACEMENT MAP
═══════════════════════════════════════
| Failed ID | Failed Data Point | Failure Reason | New ID | New Data Point | New Source | Strategy Used | Claim Impact | Status |
|:----------|:------------------|:---------------|:-------|:---------------|:-----------|:-------------|:-------------|:-------|
| S04 | "Market size $74B" | DEAD URL | S36 | "Market size $32B (2024)" | IBIS Report | Domain-Specific DB | Figure corrected $74B→$32B; L0 bullet revised | REPLACED |
| S07 | "60% adoption" | SINGLE SOURCE | S37 | "58% adoption" | Gartner 2025 | Lateral Discovery | Corroborates original; now has independent backup | CORROBORATED |
| S12 | "Patent filed 2024" | CLAIM NOT FOUND | — | — | — | Upstream + Archive | No patent in USPTO; claim appears fabricated | UNFILLABLE |
═══════════════════════════════════════
```

### Status values

- **REPLACED** — New source found that provides the same or equivalent data point. Replaces the failed source.
- **CORROBORATED** — Original claim confirmed from an independent source. Upgrades single-source claims.
- **UPDATED** — Found the data, but the figure or fact differs from the original. Note the change.
- **UNFILLABLE** — Exhaustive search failed. Claim should be dropped. Justification required per SKILL.md Step 5.
- **DOWNGRADED** — Could only find a lower-tier or Estimate-quality replacement. Better than nothing but weaker than original.

## L0 — Key Findings (Replacement Sources Only)

3-5 bullet points summarizing what was found to replace or corroborate failed sources. Bold key figures. Flag any UNFILLABLE claims and their impact.

## L1 — Detailed Analysis (Gap-Fill Narrative)

One subsection per failed source, grouped by assumption.

```
#### Replacing S04: [Original Data Point]
Failure: [reason from refine — e.g., "URL dead, confidence dropped 4→1"]
Strategy: [which strategies were tried]
Finding: [narrative with new [S36]-style citations]
Claim impact: [same data confirmed / figure updated from X→Y / claim dropped]
```

For UNFILLABLE claims:

```
#### S12: UNFILLABLE — [Original Data Point]
Failure: [reason]
Strategies attempted: [list]
Why unfillable: [explanation]
Impact: [what the analysis loses]
Proposed rewrite: [how to revise L0/L1 to not depend on this]
```

## L2 — Replacement Source Ledger & Research Notes

### Replacement Source Ledger

Same columns as `/411-research` output. IDs continue the sequence (never overwrite). Notes column includes the mapping (e.g., "Replaces S04").

| ID | Data Point | Source Name | Source URL | Date Accessed | Assumption | Tier | Confidence | Reliability | Context | Notes |
|:---|:-----------|:------------|:-----------|:--------------|:-----------|:-----|:-----------|:------------|:--------|:------|
| S36 | [fact] | [attribution] | [URL] | YYYY-MM-DD | [assumption] | [tier] | [1-5] | [Verified/Estimate — justification] | "[context]" | Replaces S04. Strategy: Domain-Specific DB. |

### Research Notes

- **Search Queries Used:** List every query, grouped by failed source ID. Mark which strategy each query belongs to.
- **Original Queries Avoided:** List the queries from the original `/411-research` that you deliberately did NOT reuse.
- **Sources Examined but Rejected:** With reasons.
- **Strategies Attempted per Failed Source:** Which strategies from the matrix were tried for each source.
- **UNFILLABLE Claims:** Summary list with one-line justifications.
- **Recommended Follow-up:** Any remaining issues for the next iteration or for the user.

## Source ID Continuity

Parse the maximum source ID from the input ledger (e.g., if the ledger goes to S35, new sources start at S36). **Never overwrite or reuse original IDs.** The audit trail must show old and new sources side by side.

## Residual Risk Section (Iteration 3 only)

On iteration 3's final pass, append a **Residual Risk** section after L2:

```
## Residual Risk
- **What the analysis cannot prove:** [list of UNFILLABLE claims]
- **Impact on recommendation:** [which parts of the /411-case analysis weaken]
- **Handoff:** This feeds into /411-case Phase 6 (Validation & Synthesis).
```
