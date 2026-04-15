# Phase 3: Assumption Mapping — Detailed Steps

> Loaded by SKILL.md at the Phase 3 gate. Follow all steps in order.

Read `references/pyramid-thinking.md` for the Pyramid Principle methodology — used in Steps 4-6 for assumption ordering, leadline drafting, and logic tree construction.

> **Theory files available for review** (loaded in earlier phases, not re-read here): `references/rugged-landscapes.md`, `references/dynamic-capabilities.md`.

---

## Step 1: Identify Assumptions (QDT)

Ask first — for each selected solution: "What assumptions do you think need to be true for [Solution X] to be the right answer?" Wait for their response — user domain knowledge surfaces blind spots that structured frameworks miss.

Then expand using the assumption categories. Read `references/assumption-categories.md` for the full list. Aim for 8-10 total per solution; don't duplicate what the user identified, add to it. Present organized by category.

For platform growth moves, also include 2-3 assumptions from these platform-specific categories alongside the standard 8:

**Network Effect Assumptions:** Will this move strengthen or dilute existing network effects? Does cross-side synergy exist? Will existing users benefit? Example: "Adding [new side/interaction] will strengthen existing network effects rather than dilute them."

**Platform Governance Assumptions:** Is the governance mode right? Can the platform attract quality providers? Does existing trust infrastructure extend? Example: "The right governance mode for [interaction] is [own/partner/affiliate] because [rationale]."

**Portfolio Coherence Assumptions:** Does this fit the theme? Will users see it as natural? Does it cannibalize or complement? Example: "This interaction fits the unifying theme of [theme] and does not cannibalize [existing interaction]."

When generating assumptions for Resource & Capability and Operational categories, probe whether the firm's existing strengths could actually block the proposed change. Ask questions like: "Could the processes that make the firm good at X be the same ones that would prevent Y?" and "How deeply embedded are the routines that would need to change?"

Ask: "Any assumptions or categories to add?"

**Do NOT proceed until the assumption set is confirmed.**

## Step 2: Stress-Test (QDT Evaluation)

Ask first — for each assumption: "Likely true, uncertain, or likely false in your view?" Then add Claude's assessment with a brief rationale.

When prioritizing which assumptions are most critical, consider: which ones are "hub choices" — strategic decisions with high interdependence that affect many other elements of the strategy? Getting a hub choice wrong cascades through the entire configuration, potentially invalidating multiple downstream assumptions. Hub choices are assumptions where being wrong would require wholesale reconfiguration, not just minor adjustment. Identify them first: they are the assumptions the firm absolutely cannot afford to get wrong.

If a solution has assumptions that are clearly false, it is disqualified. Explain which assumption failed and why. Give the user the option to contest and continue anyway.

**Do NOT proceed until all assumptions are evaluated and disqualifications explained.**

## Step 3: Select Solutions to Continue

Announce: "Here are the solutions that passed the stress-test."

Present surviving solutions. Use `AskUserQuestion` to ask which to take into Phase 4.

**Do NOT begin Phase 4 until a final selection is made.**

## Step 4: Sequence Assumptions

Now that we know which solutions survived, put their assumptions in a logical order. This sequence determines both the order of research AND often becomes the argument structure of the final deck.

Ask first: "Looking at these assumptions — what order would you put them in, and why?"

Then introduce the four logical ordering methods (from the Pyramid Principle, read above):
1. **Deductively** — premise -> premise -> conclusion. Each assumption builds on the previous one. Good when assumptions form a causal chain (A must be true for B to matter).
2. **Chronologically** — ordered by when they'd play out in time. Good for implementation-sequenced strategies.
3. **Structurally** — grouped by category or domain (market assumptions together, operational assumptions together, etc.). Good when assumptions span multiple independent areas.
4. **Comparatively** — ordered by importance, most critical first. Good when assumptions are largely independent and you want to front-load kill-shots.

Ask: "Which ordering method fits this case best? Or would a hybrid work — for example, comparative ordering within structural groups?"

**Causal gating:** When assumptions within a group form a causal chain, order them so each gates the next. The dependent assumption comes AFTER its prerequisite. Example: "Is there demand for this category?" must come before "Can we capture this demand profitably?" — the second is meaningless if the first fails.

Persuasive ordering (lead with the strongest positive) is an alternative, but should be a conscious choice, not a default. Ask: "Are any of these assumptions causally dependent on each other? If so, the dependent one comes after its prerequisite."

After choosing a method, present the proposed sequence as a numbered list with a one-line rationale for each position. Ask: "Does this order make sense? Any you'd move?"

**Do NOT proceed until the sequence is confirmed.**

## Step 5: Draft and Refine Leadlines

Now convert the sequenced assumptions into analytical claims — the leadlines that will drive the deck.

**Leadline rules:**
- Leadlines are **positive analytical claims**, not testable hypotheses
- No hedge language ("sufficient," "adequate," "may," "could")
- No embedded statistics — stats belong in the slide body, not the leadline
- Each leadline is a complete sentence a decision-maker can act on
- Test: reading ONLY the leadlines should tell the full recommendation story

**Process (iterative, not linear):**
1. **Draft:** Write one leadline per assumption in sequence order
2. **Group:** Organize into logical deck sections (e.g., Why -> How -> Shareholder Value)
3. **Refine:** For each claim — does the available evidence actually support this wording? Adjust to match what's provable
4. **Flag:** Claims the data can't yet support become Phase 5 research priorities
5. **Re-check grouping:** Does the section flow still work after refinements?
6. **Present to user:** Walk through the leadlines and ask: "Do these tell the right story?"

Save as `{working-directory}/{case-prefix}-leadline-decisions.md`.

**Do NOT proceed until leadlines are confirmed.**

## Step 6: Skeleton Logic Tree

Build the argument skeleton BEFORE mock slides — this catches structural problems before you invest in data collection or slide design.

1. **Map the tree:** Problem -> Solution -> Sections -> Leadlines (from Step 5)
2. **Horizontal leadline test:** Read ONLY the leadlines in sequence. Does the story flow? Does each lead naturally to the next?
3. **Structural check:** Are there gaps in the argument? Sections that don't connect? Leadlines that repeat rather than advance?
4. **Flag structural weaknesses:** Mark any section where the logic feels thin or the transition is forced

Save as `{working-directory}/{case-prefix}-logic-tree.md` (skeleton version — evidence mapping added in Phase 6).

Present to user: "Here's the argument skeleton. Does the structure hold before we design slides around it?"

**Do NOT proceed to Phase 4 until the argument structure is approved.**
