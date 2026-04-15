# Phase 5: Data Collection — Detailed Steps

> Loaded by SKILL.md at the Phase 5 gate. Follow all steps in order.

---

## Step 1: Research via /411-research

Compile a structured handoff for `/411-research` containing:
- The sequenced assumptions from Phase 3 Step 4 (formatted as "Assumption 1: [text]" with numbered research questions from the analysis plan)
- Data scoping constraints from Phase 4 Step 3 (time period, source preferences, proxy tolerance)

Tell the user: "Invoking /411-research to execute the research plan against your assumptions."

Invoke `/411-research`. It will auto-detect 411-case mode from the structured assumptions and return an L0/L1/L2 research artifact with a Source Ledger organized by assumption.

**Assumption batching:** Research assumptions in focused batches, not all at once.

- **Batch together** (2-4 per run): Assumptions that share evidence sources, address the same market or player, or form a causal chain
- **Research separately** (1 per run): Assumptions requiring deep dives into unrelated domains — batching dilutes focus
- **Typical pattern:** Group by deck section (all market assumptions together, all competitive assumptions together, etc.)

Name files by the assumptions they cover:
- Batches: `{case-prefix}-research-assumptions-{ids}.md` (e.g., `research-assumptions-1-3-4.md`)
- Singles: `{case-prefix}-research-assumption{id}.md` (e.g., `research-assumption7.md`)

Save each to the working directory. Present each batch's L0 findings before moving to the next batch.

Present the **L0 Key Findings** to the user for a quick review. Ask: "Any findings that surprise you or seem off? Any gaps you want me to chase before we verify?"

**Fill gaps:** If `/411-research` identifies gaps (in its "Gaps Identified" section), use `/browse` to run targeted searches for those specific data points. Discuss with the user if exact data still isn't found — explore proxies, adjacent estimates, qualitative evidence, or sensitivity analysis.

## Step 1.5: Gap Analysis

After all batched assumption research runs are complete, consolidate and identify what's still missing:

1. Review every mock slide's "Data needed" zone against data collected so far
2. For each unfilled data point, formulate a specific research question
3. Prioritize by deck impact — which slides break without this data?
4. Compile a structured gap research agenda

Invoke `/411-research` with the gap agenda. Save as `{working-directory}/{case-prefix}-research-phase5-gaps.md`.

Present gaps to user: "Here's what's still missing after the initial research. These are the questions I'll chase next."

**All research must be consolidated before running `/411-refine` in Step 2.**

## Step 1b: Financial Model Inputs Research

If a financial model is planned (confirmed during Phase 6 discussion or obvious from case context), run a **separate** research track for numerical model inputs.

Evidence research answers "Is this assumption true?" Model input research answers "What specific number do we use?"

**Identify inputs needed:**
- Volume drivers and growth rates
- Pricing data and revenue per unit
- Cost structures and margins
- Commission/referral rates
- Conversion rates and frequency metrics

Compile a model inputs brief and invoke `/411-research` separately. Save as `{working-directory}/{case-prefix}-model-inputs-research.md`.

This track follows its own verification loop:
- `{case-prefix}-model-inputs-refined.md` (via /411-refine)
- `{case-prefix}-model-inputs-reresearch.md` (if sources fail)

**Do NOT mix model input research into assumption evidence runs.** They require different search strategies — model inputs need precise numbers from 10-Ks, earnings calls, and financial databases; evidence needs directional proof from multiple source types.

## Step 2: Verify & Refine via /411-refine

Invoke `/411-refine` with the full research artifact from Step 1. It will:
- Re-fetch every URL and confirm cited data points actually appear on page
- Cross-reference key claims against independent sources
- Recalibrate confidence scores and assign Verified/Estimate reliability labels
- Detect and resolve source conflicts
- Produce a Sources-Cited Handoff section formatted for `/sources-cited`

Present the **Verification Dashboard** to the user (confirmation rate, corroboration rate, dead URLs, conflicts detected, tier distribution).

If conflicts or low-confidence findings exist, review them with the user: "These claims had issues during verification — [list]. Options: (a) Run `/411-reresearch` to find replacement sources, (b) drop them, or (c) proceed with caveats."

**Do NOT proceed until the user approves the verified findings.**

## Step 2.5: Re-Research Loop (if option a)

If the user chooses to re-research failed sources:

1. Feed the full `/411-refine` output into `/411-reresearch`. It will parse the Verification Dashboard and Source Ledger, triage failures by priority, and run targeted searches using differentiated strategies.
2. Feed the `/411-reresearch` output (replacement sources) back into `/411-refine` for re-verification. Provide BOTH the original verified sources (entries that passed) AND the new replacement sources.
3. Check the **Convergence Dashboard** in the new `/411-refine` output.
4. If NOT CONVERGED and iteration < 3, repeat from step 1.
5. Present the final Convergence Status to the user before proceeding to Step 3.

Name re-research outputs with iteration numbers:
- `{case-prefix}-reresearch-iteration{n}.md`
- `{case-prefix}-refine-reresearch.md` (or `-iteration{n}` if multiple refine passes)

Save all to the working directory.

Maximum 3 iterations. After iteration 3, any remaining failures are declared UNFILLABLE with documented justification — carry these into Phase 6 as explicit limitations.

## Step 3: Generate Sources Document

`/411-refine` generates the .docx bibliography directly (via `/docx`) as part of its output. Sources are organized by assumption with Quality, Reliability, and tier distribution included. No separate `/sources-cited` invocation needed.

## Step 4: Evidence Stitching

After research is verified, connect the evidence to the argument structure. This is the bridge between data collection and deck construction.

1. **Source mapping:** For each leadline in the skeleton logic tree, list every supporting source by ID from the Source Ledger
2. **Strength audit:** Rate evidence strength per leadline based on source count, verification status, and tier distribution (e.g., 5-star = 3+ verified sources across tiers; 2-star = single source, estimate-based)
3. **Flag weaknesses:** Identify leadlines with the thinnest evidence — these are where the argument is most vulnerable to challenge
4. **Sensitivity nodes:** Which variables, if changed, swing the entire recommendation? Mark these in the tree.
5. **Re-run horizontal leadline test:** Has the argument structure changed based on what the evidence actually showed? If leadlines were revised during research, update the sequence and grouping.
6. **Update logic tree:** Overwrite the skeleton from Phase 3 with the enriched version — `{working-directory}/{case-prefix}-logic-tree.md`

Present the strength audit to the user. Ask: "Are you comfortable with the evidence behind each leadline? Any you want to strengthen before we build the deck?"

**Do NOT proceed to Phase 6 until the enriched logic tree is reviewed and approved.**
