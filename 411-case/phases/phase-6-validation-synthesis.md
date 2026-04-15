# Phase 6: Deck Construction — Detailed Steps

> Loaded by SKILL.md at the Phase 6 gate. Follow all steps in order.

---

## Step 1: Review Enriched Logic Tree

The enriched logic tree from Phase 5 carries the evidence stitching, strength audit, and sensitivity analysis. Present it to the user for final review.

Ask: "Here's the argument with all evidence mapped. The enriched logic tree from Phase 5 shows strength ratings for every leadline. Are you ready to build the deck, or do you want to strengthen any points first?"

**Do NOT proceed until the user confirms the enriched logic tree.**

## Step 2: Offer Additional Deliverables

Use `AskUserQuestion` to ask which the user wants to build:

1. **Financial model** — 3-scenario impact model (read `references/impact-modeling.md`, invoke `xlsx` skill)
2. **Deck argument structure** — built using the Pyramid Principle, produces a handoff file for the `411-deck` skill (see Step 3 below)

## Step 3: Build Presentation Deck

If the user selects the presentation deck, walk them through the **6-step deck-building process** every time. Do not skip steps or abbreviate — repetition builds the muscle memory.

Read `references/slide-best-practices.md` for all formatting standards.

The SCQA framing was established in Phase 1. The Pyramid structure was established in Phase 3. Apply both to the deck argument.

**Platform portfolio cases:** When the case involves a platform portfolio recommendation, structure the deck argument in three sections:
- **Section 1:** The growth opportunity (2x2 matrix current state, competitor comparison, theme rationale)
- **Section 2:** The portfolio and sequence (quadrant map with new opportunities, value curve, sequencing timeline)
- **Section 3:** Deep-dive on the first investment (market analysis, financial impact, assumptions, risks)

Add to handoff spec frontmatter for platform cases: `platform_case: true`, `theme`, `quadrant_map` (q1/q2/q3/q4 lists), `governance` (own/partner/affiliate lists), `sequence` (ordered list), `deep_dive` (first investment name).

**Step 1: Define the Top Box**
Ask: "What is the subject we're presenting on? What question are we answering? And what is our answer — our recommendation?"

**Step 2: Write the SCQA Introduction**
The SCQA was framed in Phase 1. Walk the user through applying it to the deck introduction: Situation, Complication, Question, and Answer. Refine for presentation context.

**Step 3: Find the Key Line**
Ask: "Our answer is [X]. What new question does that raise in the audience's mind? That question drives the structure of the entire deck."

**Step 4: Choose Deductive or Inductive Structure**
The structure type was chosen in Phase 3 (assumption sequencing). Apply it to the deck. Ask: "Should we structure the argument deductively (premise -> premise -> conclusion) or inductively (group evidence -> state significance)? What's the 'plural noun' — 'three reasons,' 'four factors'?"

**Step 5: Build Subpoints to Completion**
For each point, follow it all the way to its supporting evidence before moving to the next. Never introduce a new idea halfway through a section.

**Step 6: Add Leadlines That Connect Horizontally**
Each slide gets a leadline (analytical statement, not a label). Test: reading ONLY the leadlines should tell the full story of the deck.

## Step 4: Generate Handoff File

After the deck structure is set, produce the handoff file that the `411-deck` skill will consume to build the `.pptx`.

The Phase 4 mock slides are the foundation — you're enriching them with final data, not rebuilding from scratch.

1. Take Phase 4 mock slides and enrich them with final data collected in Phase 5
2. Layer on the Pyramid Principle structure from Step 3 (SCQA, key line, structure type, argument flow, leadlines)
3. For each slide, populate all required fields: leadline, chart type, chart title, data table, axis labels, callout items, footnotes, source line, and any formatting notes
4. Flag sensitivity slides (slides where the outcome is particularly sensitive to one assumption)
5. Build the recommendation slide specification per the principle-based format:
   - Clear recommendation with supporting rationale
   - Decision criteria so the audience understands WHY
   - Key risks or contingencies
   - When multiple viable options exist: numbered options with "choose this if..." criteria
   - When one clear winner: direct recommendation + top risks + next steps
6. Save as `{working-directory}/{case-prefix}-deck-spec.md` using the handoff format from `assets/deck-spec-template.md`. The original mock-slides file is preserved as the audit trail of the pre-data argument structure.
7. Tell the user: "Deck argument saved to `{case-prefix}-deck-spec.md`. Review the file, then invoke `411-deck` to produce the .pptx."
