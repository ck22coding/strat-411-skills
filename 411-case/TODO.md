---
name: 411-Case Skill To-Do List
description: Open work items for the 411-case skill including data source references, model routing, deliverables criteria, and PPTX guardrails.
type: project
status: active
---

# 411-Case Skill — To-Do List

> **Master view:** [personal-todo-checklist.md](personal-todo-checklist.md) — update status there, update specs/context here.

Last updated: 2026-04-01

## Completed
- [x] Expand `analytical-techniques.md` — 3-question framework, ASCII charts, worked examples for all analysis types
- [x] Flip human-in-the-loop order — Claude asks user's opinion before generating suggestions
- [x] Restructure phases — now 6 phases in `411-case.md` (~190 lines)
- [x] Add skill best practices — `allowed-tools`, gate language, status announcements, rationale on key instructions
- [x] **Theory mode switching** — Theories baked into process as background reasoning (not named to students). Created `references/strategy-theories.md` with 4-layer framework + vocabulary map. SKILL.md updated with theory-informed questions in Phases 1-3. (2026-03-17)
- [x] **Deck logic flow as HITL practice** — 6-step Pyramid Principle deck-building process added to `presentation-structure.md` Section 8. SKILL.md Phase 6 Step 3 walks students through all 6 steps every time. (2026-03-17)
- [x] **Slide ordering process** — Captured via Pyramid Principle: define top box → SCQA → key line → deductive/inductive structure → subpoints to completion → horizontal leadlines. (2026-03-17)
- [x] **Key implications throughout the case** — Implication writing standards added to `slide-best-practices.md` Section 6. Enforced in Phase 4 mock slides AND Phase 6 final deck. Strategic conclusions required, not data restatements. (2026-03-17)
- [x] **Deeper firm resources & capabilities analysis** — Added Phase 1 Step 2 "Industry & Firm Analysis" to SKILL.md. Claude proactively researches industry dynamics, competitive landscape, firm capabilities, and change signals before confirming understanding. (2026-03-17)
- [x] **401 frameworks as reference material** — Integrated into `references/strategy-theories.md` as background: Rugged Landscapes (NK model), Evolutionary Economics, Schumpeterian Competition, Search Process, Competitive Positioning (Blue Ocean, ERRC, Strategic Groups, Factor Analysis). (2026-03-17)
- [x] **Speaker notes: theory & reasoning** — Competence-puzzle questions added to assumption-categories.md. Hub-vs-peripheral thinking baked into assumption prioritization. Theory reasoning informs Claude's internal framing throughout. (2026-03-17)
- [x] **PPTX formatting guardrails** — Slide template zones strictly enforced in SKILL.md (leadline, graph title, chart, callout, footnotes, source). Recommendation slide principles added. Sensitivity analysis pattern added. Leadline vs graph title distinction captured. All in `slide-best-practices.md`. (2026-03-17)
- [x] **Extract all 10 PPTX course materials** — 197 slides extracted, Group A diffed against refs, Group B (5 theory lectures) fully cataloged. Analysis files at `~/Desktop/411/extractions/`. (2026-03-17)
- [x] **Split strategy-theories.md into focused files** — Replaced single 94KB file with 5 focused theory references enriched from lecture .pptx slides: `rugged-landscapes.md`, `schumpeterian.md`, `dynamic-capabilities.md`, `competitive-positioning.md`, `strategy-overview.md` (slim index). Old `strategy-theories.md` deleted. (2026-03-21)
- [x] **Clean up SKILL.md inline notes** — Implemented all `[][]` bracket notes: `/browse` for research, research scope questions, expanded competitive landscape bullets, theory lens instructions per phase, sources-cited invocation, problem restatement in Phase 2, firm positioning guidance. All brackets removed. (2026-03-21)
- [x] **Add assumption sequencing step** — Added Phase 3 Step 4 (Sequence Assumptions) to SKILL.md. Uses the four Pyramid Principle ordering methods (deductive, chronological, structural, comparative). HITL — asks user to propose ordering first. (2026-04-01)
- [x] **Basic Slide Template for 411-deck** — Copied `Basic Slide Template.pptx` into 411-deck skill folder. Updated 411-deck SKILL.md to use it as base template (simple, no fancy formatting). (2026-03-21)
- [x] **Estimate/verified labeling in sources-cited** — Added reliability field (Verified/Estimate) with one-sentence justification to source log and output document. (2026-03-21)
- [x] **Update reference table in SKILL.md** — Now lists all 5 theory files + 6 existing reference files with specific "When to Read" guidance per phase. (2026-03-21)

## Open

- [x] **Add leadline guidance to SKILL.md** (2026-04-14)
  Added to Phase 3 Step 5 (leadline rules + iterative refinement process) and Phase 4 Step 2 (quality check). Also added to `slide-best-practices.md` for /411-deck.

- [x] **Add iterative refinement loop to Phase 3 Step 4** (2026-04-14)
  Expanded into Phase 3 Step 5 (Draft and Refine Leadlines). Multi-pass loop: draft → group → refine → flag → re-check. Produces `leadline-decisions.md`.

- [x] **Add deductive ordering guidance to Phase 3 Step 4** (2026-04-14)
  Added "Causal gating" guidance after the four ordering methods. Dependent assumptions come after prerequisites.

- [ ] **Build data source reference file** (`references/data-sources.md`)
  Trusted sites by data type: market data, financials, competitive intel, macro. Include credibility guidance (primary vs. secondary, when to trust, when to verify).
  **Priority guidance:** Define where to look first and which sources we trust most — not just a flat list, but a ranked hierarchy.

- [ ] **Model routing guidance**
  Which model (Opus / Sonnet / Haiku) to use at each of the 6 phases and why. Goes in main `411-case.md` or a reference file.

- [x] **Final deliverables & output criteria** (2026-04-14)
  Added Output Convention section to SKILL.md with per-phase deliverable manifest, naming convention, and working directory setup.

- [ ] **DOCX / output voice consistency**
  When producing deliverables (docx, summaries, etc.) mid-case or after research, output must follow global CLAUDE.md voice (clear, concise, direct). Investigate whether the `/docx` skill overrides global tone settings and fix if so.

- [x] **Data gathering skill** (separate but feeds into 411)
  Fulfilled by `/411-research` (SIFT methodology, 4-tier source hierarchy, L0/L1/L2 output, standalone + assumption-map modes) and `/411-refine` (URL verification, cross-referencing, confidence recalibration, sources-cited handoff). Both installed 2026-04-08.

- [~] **Move data scoping from Phase 4 Step 3 → Phase 1** — **WON'T DO** (2026-04-14)
  Airbnb case evidence confirms Phase 4 Step 3 placement is correct. You need mock slides to know what data to scope. Moving it to Phase 1 means scoping before knowing your analyses.

- [x] **Run `/kpi-setter` on 411-deck** (2026-04-17)
  kpi.md v2 at `~/Claude/autoresearch/411-deck/kpi.md` + context.md. Originally planned 17 phase KPIs + 5 holistic; during the session the architecture was restructured around a **signed handoff contract** between /411-case and /411-deck. Argument-structure checks (leadline phrasing, horizontal story, implication quality, recommendation completeness) are now enforced upstream in /411-case Phases 3-6 and cryptographically sealed via `scripts/deck_signature.py`. /411-deck Phase 1 verifies the signature instead of re-checking the argument; Phase 4 narrowed to rendering-fidelity checks only. Final KPI structure: 4 phases, 13 phase KPIs + 5 holistic, 5 test scenarios (happy path / missing signature / hash mismatch / rendering defects / Unicode+single-point). Autoresearch not run — restructured skill is mostly deterministic, so there's less surface area to optimize; future regression testing can still use the KPI file.

- [ ] **Run `/kpi-setter` on 411-case**
  KPIs for the HITL skill: gate enforcement, assumption coverage (8+ per solution across categories), handoff file completeness.

- [~] **Run autoresearch on updated skills** — **IN PROGRESS (2026-04-17)**
  - [x] `/411-refine` — compliance fixed to 13/13; kpi.md + context.md written at `~/Claude/autoresearch/411-refine/`; baseline score 0.572 (phase 0.494, holistic 0.650); iter-1 atomic edit (Rendering Contract) staged in SKILL.md, awaiting re-run. See `~/Claude/autoresearch/411-refine/progress.md`.
  - [ ] `/411-refine` — continue loop via `run-iteration.sh` until phase KPIs ≥90% (est. 10-20 more iterations, 2-3 hrs wall).
  - [~] `/411-deck` — KPIs defined (2026-04-17) but autoresearch skipped intentionally: skill was restructured to a signature-verify design with minimal judgment calls, leaving little for the optimizer to improve. Future regression testing can still use `~/Claude/autoresearch/411-deck/kpi.md`.
  - [x] `/411-research` — compliance 13/13 (unchanged); kpi.md written at `~/Claude/autoresearch/411-research/kpi.md` (7 phases, 26 phase KPIs, 5 holistic, 5 scenarios). No HITL context needed (skill is autonomous). Fresh-session autoresearch prompt saved in `~/.claude/plans/411-research-refinement.md`. Not yet run.
  - [ ] `/411-research` — run autoresearch in fresh session.
  - [ ] `/411-case` — still to do (run `/kpi-setter` first).

- [~] **Add deck QA checklist to Phase 6 Step 2** (2026-04-13)
  Partially addressed via the 2026-04-17 restructure: the QA checklist items now live in `/411-deck` Phase 4 as rendering-fidelity KPIs (template zones, verbatim content, chart data, sensitivity, source cleanliness, placeholders, superscript integrity) and in `/411-deck`'s holistic KPIs (vertical alignment, source accuracy, v1/v2 consistency). `/411-case` Phase 6 no longer needs to run the checklist itself — the signed-handoff contract defers rendering checks to /411-deck. Remaining open: if you want `/411-case` to preview the checklist to students for pedagogical purposes, that's a separate doc.

- [x] **Add Phase 4.5: TA Feedback checkpoint** (2026-04-14)
  Added as formal gated phase between Phase 4 and Phase 5. Five steps: present to TA, record feedback, gap-analyze, apply changes with before/after changelog, confirm. Gate: do not proceed to Phase 5 until TA feedback incorporated.
