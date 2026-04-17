# Differentiation Strategy Matrix

Load this when selecting a search strategy in Step 2. The original `/411-research` uses three query angles: **direct**, **specific/technical**, **verification**. Every strategy here must differ from those — you are filling gaps, not repeating discovery.

## The 8 Strategies

| Strategy | Description | When to Use |
|----------|-------------|-------------|
| **Lateral Source Discovery** | Search for the CLAIM (the fact/stat itself), not the source. Find who else published it. | URL dead or claim not found — the data may exist elsewhere |
| **Upstream Tracing** | The failed source cited someone else. Find the original study, filing, or dataset. | Tier 2-3 source that can't be verified; trace upstream to Tier 1 |
| **Domain-Specific Databases** | Use site-specific searches: `site:sec.gov`, `site:bls.gov`, `site:census.gov`, `site:scholar.google.com`, EDGAR, PACER | Original research used general web searches |
| **Temporal Pivoting** | Search different time windows. A 2024 stat may appear in a 2025 annual review, earnings call, or year-in-review article. | Date-bounded search returned nothing |
| **Synonym/Reformulation** | Restate the claim using industry jargon, alternative metrics, or proxy measures. | Standard terminology failed to surface results |
| **Archive Recovery** | Use `web.archive.org` / Wayback Machine to recover dead URLs. | URL Status = DEAD specifically |
| **Inverse Search** | Search for REBUTTALS or criticism of the claim. If critics cite it, that proves it exists and gives you the real source. | AI-content suspected or unverifiable claims |
| **Adjacent Data** | When the exact stat is unavailable, find the closest available proxy and flag as Estimate. | After primary strategies exhaust — last resort |

## Hard Rules

- **Do NOT reuse search queries** from the original `/411-research` Research Notes. If the original notes are available, read them and avoid duplicates.
- **Document which strategy you selected** for each failed source and why. The next `/411-refine` pass needs to evaluate whether your replacement is genuinely independent.
- **Try at least 2 strategies per P1 failure** before declaring UNFILLABLE.
- **Escalation by iteration:**
  - Iteration 1 — any strategy from the matrix
  - Iteration 2 — proxy data and Adjacent Data acceptable for P2/P3
  - Iteration 3 — final pass; remaining failures declared UNFILLABLE

## Selection Heuristic

Pick strategy based on the **failure reason**, not the source type:

- **DEAD URL** → Archive Recovery first, then Lateral Source Discovery
- **CLAIM NOT FOUND** → Lateral Source Discovery, then Inverse Search
- **Confidence collapse (4→1)** → Upstream Tracing (find the real primary)
- **AI-content suspected** → Inverse Search (critics cite real sources)
- **Single-source vulnerability** → Lateral Source Discovery (find independent corroboration)
- **General web results only** → Domain-Specific Databases
- **Stale date** → Temporal Pivoting
- **Jargon mismatch** → Synonym/Reformulation
