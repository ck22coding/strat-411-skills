# Phase 4: Research Planning — Detailed Steps

> Loaded by SKILL.md at the Phase 4 gate. Follow all steps in order.

---

## Step 1: Plan the Analyses

For each assumption, identify what type of analysis would confirm or refute it, and what a confirming result looks like. Read `references/analytical-techniques.md` to match assumptions to the right analysis types.

Present the full plan. Ask: "Does this look right? Any analyses you'd approach differently?"

**Do NOT proceed until the analysis plan is confirmed.**

## Step 2: Create Mock Slides (ASCII)

For each planned analysis, build a mock slide that **strictly follows the slide template zones**:

1. **Leadline** (top) — an analytical takeaway sentence, not a label. States what the data means if the assumption is true.
2. **Graph title** (on the chart) — a descriptive label of what the chart shows. Distinct from the leadline.
3. **ASCII chart** (center) — expected shape of the data. Use the chart type guidance from `references/analytical-techniques.md`.
4. **Callout section** (right side) — labeled "Key Implications" or "Key Takeaways." Each implication must be a **strategic conclusion**, not a data restatement. Answer: "So what? What should the decision-maker DO with this?"
5. **Footnotes** (bottom) — key assumptions, methodology notes, caveats
6. **Source line** (bottom) — "Source: [specific source], [year]"
7. **Data needed** — what to go collect and where to look

Read `references/slide-best-practices.md` for chart formatting, implication writing, and slide layout standards.

**Leadline quality check:** Every mock slide leadline must follow the leadline rules from Phase 3 Step 5:
- Positive analytical claim (not a hypothesis or question)
- No hedge language
- No embedded statistics
- Reads as a standalone decision-relevant sentence

If a leadline doesn't meet these criteria, revise it before proceeding.

For any analysis where the outcome is particularly sensitive to one assumption, flag it and plan a sensitivity presentation: show the range of outcomes under different assumption values.

Ask: "Do these mock slides capture the right argument?"

**Do NOT proceed until confirmed.**

## Step 3: Data Scoping

**Part 1: Enumerate data needs per slide.**
Walk through every mock slide from Step 2 and extract each discrete data point from the "Data needed" zone. Present as a table:

| Slide | Data Point | Likely Source Type |
|-------|------------|--------------------|
| 1 | [specific fact/stat needed] | [primary / secondary / estimate] |
| 1 | [another data point] | ... |
| 2 | ... | ... |

**Part 2: Deduplicate and cross-reference.**
Identify data points that appear on multiple slides. Consolidate into a single collection list — each data point collected once, tagged with which slides use it. This prevents collecting the same stat twice from different sources and ensures consistent figures across the deck.

Present the deduplicated list. Ask: "Any data points missing, or any you'd source differently?"

**Part 3: Scope and flag.**
Use `AskUserQuestion` to ask:

1. What time period of data are we looking for?
2. Raw/primary data, or are published estimates acceptable?
3. Are reasonable proxies and assumptions okay where exact data isn't available?
4. Any specific sources you already know about?

**Proxy/estimate flagging rule:** Any data point where primary data is not available must be explicitly marked. When `/411-research` collects the data, it assigns a `Reliability` label (`Verified` or `Estimate`). That label must carry through to:
- The Source Ledger (`Reliability` column)
- The mock slide footnotes (e.g., "^1 Estimate based on [methodology]")
- The final deck source line (e.g., "Source: [source], [year] (estimate)")

Ask the user to review the data list and approve which points are acceptable as estimates/proxies vs. which require primary sources. Mark each accordingly before proceeding.

Save the deduplicated data collection list, cross-slide dependencies, and scoping decisions as `{working-directory}/{case-prefix}-data-scoping.md`. This file is the structured handoff for Phase 5 — it defines every data point the deck requires.

**Do NOT proceed to Phase 5 until scoping is complete.**
