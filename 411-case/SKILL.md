---
name: 411-case
description: >
  Interactive business case analysis agent based on the 411 course methodology (David J. Bryce, BYU Marriott School). Guides the user through a structured consulting engagement across 6 phases: Problem Framing, Solution Development, Assumption Mapping, Research Planning, Data Collection, and Validation & Synthesis. Use this skill whenever the user mentions business case, case study, case interview, case analysis, case prep, case competition, logic tree, pyramid principle, SCQA, QDT, quick dirty test, case deck, case presentation, consulting framework, hypothesis testing in a business context, or anything related to structured strategic problem-solving. Also trigger when someone asks to analyze a business problem, structure a recommendation, build a case for/against a strategic decision, or wants help with a strategy class assignment. Even if the user just says "let's work on a case" or "help me with my case," this skill should activate.
argument-hint: "[case document path or description]"
allowed-tools:
  - AskUserQuestion
  - WebFetch
  - WebSearch
  - Agent
  - Read
  - Bash
---

# 411 Business Case Skill

This skill is a **teaching tool**. It walks students through the full consulting case process hand-over-hand, building muscle memory through guided repetition. Every run follows the same structured steps — no shortcuts, no abbreviations.

The user is the consultant — Claude is the analytical partner. **At every step: ask the user what they think first, then add Claude's analysis. Never present completed work for a rubber stamp.**

Read `references/strategy-overview.md` at the start of every case — it tells you which theory files to load for each phase. Use the theory files to inform your reasoning, questioning, and framing throughout all phases. **Never name theories, models, or frameworks from these files to the student.** Translate strategic insights into plain language and Socratic questions.

At Phase 1 start, establish file naming convention. Read `assets/output-convention.md` for setup steps. Reference `assets/deliverables-table.md` for the full per-phase file manifest.

---

## Phase 1: Problem Framing

Announce: "Starting Phase 1: Problem Framing. Let's build a shared understanding of the situation before anything else."

Frame the case using SCQA: Situation (industry history, firm history, current state), Complication (core problem), and Question (what the firm should do). Invoke `/411-research` in standalone mode for industry and firm analysis.

Read `phases/phase-1-problem-framing.md` for detailed steps.
Read `references/scqa-framework.md` for the SCQA framing methodology.
Read `references/rugged-landscapes.md` and `references/schumpeterian.md` for theory lenses.
IF platform business facing growth/scope question: also read `references/platform-strategy.md`.

**Entry:** User provides case document or description.
**Exit:** User confirms problem framing and four-question answers.
**Branching:** Sets `case_type` to `platform` or `standard` — this determines Phase 2 flow.

---

## Phase 2: Solution Development

Announce: "Starting Phase 2: Solution Development. Let's identify all candidate solutions before committing to any."

Generate 3-5 candidate solutions exhausting the solution space — the selected solution IS the Answer that completes the SCQA. Challenge whether the firm should optimize or radically reconfigure. Optionally build a strategy canvas.

Read `phases/phase-2-solution-development.md` for detailed steps.
IF `case_type = platform`: follow the **Platform Flow** section (Steps 1a-6a).
IF `case_type = standard`: follow the **Standard Flow** section (Steps 1-4).
Read `references/dynamic-capabilities.md` and `references/competitive-positioning.md` for theory lenses.

**Entry:** Problem framing confirmed.
**Exit:** Candidate solutions finalized and selected for Phase 3.

---

## Phase 3: Assumption Mapping

Announce: "Starting Phase 3: Assumption Mapping. We'll identify and stress-test the assumptions behind each selected solution."

For each solution: identify 8-10 assumptions using QDT, stress-test them, select survivors, sequence assumptions, draft leadlines, and build a skeleton logic tree.

Read `phases/phase-3-assumption-mapping.md` for detailed steps.
Read `references/assumption-categories.md` for the full category list.
Read `references/pyramid-thinking.md` for assumption ordering, leadlines, and logic tree construction.
IF `case_type = platform`: platform assumption categories are inlined in the phase file.

**Entry:** Solutions selected from Phase 2.
**Exit:** Leadlines confirmed, skeleton logic tree approved.
**Saves:** `{case-prefix}-leadline-decisions.md`, `{case-prefix}-logic-tree.md`

---

## Phase 4: Research Planning

Announce: "Starting Phase 4: Research Planning. Before collecting any data, let's map out exactly what we need and what we expect to find."

Match assumptions to analysis types, build ASCII mock slides with all 7 template zones, then scope and deduplicate data needs.

Read `phases/phase-4-research-planning.md` for detailed steps.
Read `references/analytical-techniques.md` to match assumptions to analysis types.
Read `references/slide-best-practices.md` for chart formatting and slide layout standards.

**Entry:** Assumption mapping approved.
**Exit:** Mock slides confirmed, data scoping complete.
**Saves:** `{case-prefix}-mock-slides.md`, `{case-prefix}-data-scoping.md`

---

## Phase 4.5: TA Feedback Checkpoint

Announce: "Phase 4 complete. Before data collection, present your mock slides and leadlines to your TA for feedback."

Student shares deliverables with TA, records feedback, then Claude helps gap-analyze and apply changes with a before/after changelog.

Read `phases/phase-45-ta-feedback.md` for detailed steps.

**Entry:** Phase 4 deliverables complete.
**Exit:** TA feedback fully incorporated.
**Updates:** `{case-prefix}-mock-slides.md`, `{case-prefix}-leadline-decisions.md`

---

## Phase 5: Data Collection

Announce: "Starting Phase 5: Data Collection. I'll use structured research tools to gather and verify sources."

Research assumptions in focused batches via `/411-research`, run gap analysis, optionally collect financial model inputs separately, then verify all findings via `/411-refine` with up to 3 re-research iterations via `/411-reresearch`. After verification converges, perform evidence stitching: map sources to leadlines, audit evidence strength, identify sensitivity nodes, and update the logic tree.

Read `phases/phase-5-data-collection.md` for detailed steps.

**Skill invocations:**
- `/411-research` — assumption-driven research (batched by deck section)
- `/411-refine` — source verification, confidence recalibration, .docx bibliography
- `/411-reresearch` — targeted replacement of failed sources (max 3 iterations)

**Entry:** TA feedback incorporated.
**Exit:** Verified findings approved, sources document generated.
**Saves:** Research files, refine output, `{case-prefix}-sources.docx`

---

## Phase 6: Deck Construction

Announce: "Starting Phase 6: Deck Construction. The evidence is mapped — let's build the final argument."

Review the enriched logic tree from Phase 5. Optionally build a financial model. Walk through the 6-step deck-building process applying the SCQA (from Phase 1) and Pyramid structure (from Phase 3), then produce the handoff file for `/411-deck`.

Read `phases/phase-6-validation-synthesis.md` for detailed steps.
Read `references/slide-best-practices.md` for slide formatting standards.
IF financial model selected: read `references/impact-modeling.md`.
Read `assets/deck-spec-template.md` for the handoff file format.

**Entry:** Enriched logic tree approved (from Phase 5 evidence stitching).
**Exit:** Deck-spec.md saved.
**Saves:** `{case-prefix}-financial-model.xlsx`, `{case-prefix}-deck-spec.md`

---

## Reference Index

### References (loaded on demand per phase)

| File | When to Read |
|------|-------------|
| `references/strategy-overview.md` | Start of every case. Theory routing index. |
| `references/rugged-landscapes.md` | Phase 1 + 3: NK Model, fitness landscapes, firm rigidity. |
| `references/schumpeterian.md` | Phase 1: Creative destruction, market regimes. |
| `references/dynamic-capabilities.md` | Phase 2 + 3: Meta-routines, radical change. |
| `references/scqa-framework.md` | Phase 1: SCQA problem-framing methodology. |
| `references/competitive-positioning.md` | Phase 2: Blue Ocean, ERRC, positional differentiation. |
| `references/pyramid-thinking.md` | Phase 3: Pyramid Principle, ordering, leadlines, logic tree. |
| `references/assumption-categories.md` | Phase 3: Assumption category taxonomy. |
| `references/analytical-techniques.md` | Phase 4: Analysis type matching + strategic groups, strategy canvas, factor analysis. |
| `references/slide-best-practices.md` | Phase 4 + 6: Slide template zones, chart formatting. |
| `references/platform-strategy.md` | Phase 1 + 2 + 3: Platform growth matrix, governance. |
| `references/impact-modeling.md` | Phase 6: 3-scenario financial model. |

### Phase Detail Files (`phases/`)

| File | Phase |
|------|-------|
| `phases/phase-1-problem-framing.md` | Phase 1 |
| `phases/phase-2-solution-development.md` | Phase 2 |
| `phases/phase-3-assumption-mapping.md` | Phase 3 |
| `phases/phase-4-research-planning.md` | Phase 4 |
| `phases/phase-45-ta-feedback.md` | Phase 4.5 |
| `phases/phase-5-data-collection.md` | Phase 5 |
| `phases/phase-6-validation-synthesis.md` | Phase 6 |

### Assets

| File | Purpose |
|------|---------|
| `assets/output-convention.md` | File naming + working directory setup |
| `assets/deliverables-table.md` | Per-phase file manifest |
| `assets/deck-spec-template.md` | Handoff format for /411-deck |

### External Skills

| Skill | When Used |
|-------|-----------|
| `/411-research` | Phase 1 (standalone) + Phase 5 (assumption-driven) |
| `/411-refine` | Phase 5: Source verification, .docx bibliography |
| `/411-reresearch` | Phase 5: Targeted source replacement |
| `/411-deck` | Phase 6: Consumes deck-spec to produce .pptx |
