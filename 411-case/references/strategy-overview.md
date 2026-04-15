# Strategic Reasoning Overview (Internal Reference)

> **Preamble:** This file informs Claude's reasoning during case analysis. Never name these theories, models, or frameworks to students. Translate insights into plain strategic language or Socratic questions.

> **This is an index file.** It contains cross-cutting concepts that span all theory files, plus a routing table for when to read each file. The detailed theory content lives in the individual reference files.

---

## Strategy as Search

**Core insight: Strategy is SEARCH, not design. 67% of successful founders had no formal plan. Only 4% found their ideas through systematic search.**

### Deliberation + Emergence
Neither pure planning nor pure trial-and-error works:
- **Pure Emergence** risk: stranded on a low local peak (Tripod's unfocused experimentation)
- **Pure Deliberation** risk: wrong destination, no adjustment (USA Today's rigid early plan)
- **Winning combo:** deliberation gets you to a promising region; emergence helps you climb a nearby peak

### Good Search Process (Two Components)

**Good Starting Points:**
- Seek under-served or over-served customer needs
- Look for new arbitrage from tech/regulatory change
- Watch for danger signs: complex value flows, coordination requirements, spillover problems

**Intelligent Adjustment:**
- Consider multiple alternatives
- Choose sensors well and seek disconfirming data
- Once advantage is spotted, elaborate the entire value chain to support it
- Counter your own cognitive biases

### Six Building Blocks of Strategy Search

| Element | Definition |
|---------|-----------|
| **Personal values** | Managers' core beliefs and priorities — what counts as important, acceptable, worth pursuing |
| **Representations** | Mental models of how the business and environment work |
| **Heuristics** | Rules of thumb and decision routines that narrow the search space |
| **Activities** | Interdependent things a firm does — operations, marketing, R&D, sales |
| **Stocks** | Accumulated assets/liabilities built through activity (equipment, reputation, knowledge, routines) |
| **Sensors** | Mechanisms that detect and surface signals about environment and performance |

### Selective Flexibility Principle
- Hold firm on **hub choices** and accumulation-dependent activities
- Stay flexible on **peripheral choices**
- Shift toward rigidity as advantage becomes clear
- Hub choices = high-K elements (changing them cascades through many other choices)
- Peripheral choices = low-K elements (can be changed without systemic disruption)

### How Claude Uses This
- Bake hub-vs-peripheral thinking into assumption prioritization: critical assumptions = hub choices
- Frame problems as "where should the firm search?" not "what should the firm do?"
- Design sensors to gather disconfirming data, not just confirming evidence
- Recommend which parts of the strategy should be rigid vs. flexible

---

## Cross-Theory Vocabulary Map

The same strategic concept appears under different names. Claude should recognize all variants and translate between them silently.

| Concept | Rugged Landscapes | Firm Rigidity | Schumpeterian | Search/Navigation | Competitive Positioning |
|---------|------------------|---------------|---------------|-------------------|------------------------|
| Why firms get stuck | Local peak trap | Competence puzzle / routine rigidity | Incumbent inertia | Pure deliberation failure | Mobility barriers |
| Radical change | Long jump | Dynamic capabilities | Creative destruction | — | Blue Ocean / value innovation |
| Incremental change | Hill-climbing / local search | Routine refinement | Sustaining innovation | Emergence | Positional differentiation |
| What constrains firms | Path dependence + K | Routines + bounded rationality | Accumulated rent-earning assets | Stocks + activities | Path dependence |
| Landscape metaphor | Explicit (the theory itself) | Implicit (routines = why you're on a specific peak) | Implicit (destruction reshapes landscape) | Explicit ("promising region," "nearby peak") | Explicit (unifying theory) |

---

## Which File to Read When

| Case Phase | Read These Files | How Claude Uses Them |
|------------|-----------------|---------------------|
| **Problem Framing** (Phase 1) | `references/scqa-framework.md` + `references/rugged-landscapes.md` + `references/schumpeterian.md` | SCQA framing (S=industry/firm/current, C=core problem, Q=explicit). Which regime? Is the firm trapped? Is the landscape shifting? |
| **Solution Development** (Phase 2) | `references/dynamic-capabilities.md` + `references/competitive-positioning.md` | Find the Answer that completes the SCQA. Look for arbitrage. Apply ERRC. Choose attribute configuration. |
| **Assumption Mapping** (Phase 3) | `references/pyramid-thinking.md` + `references/assumption-categories.md` | Pyramid structure for ordering assumptions. Hub choices = critical assumptions. Leadlines, logic tree construction. |
| **Research Planning** (Phase 4) | `references/analytical-techniques.md` + `references/slide-best-practices.md` | Match assumptions to analysis types (includes strategic groups, strategy canvas, factor analysis). Mock slides. |
| **Data Collection** (Phase 5) | — | Research via /411-research + /411-refine. Evidence stitching: source mapping, strength audit, sensitivity nodes. Enriched logic tree. |
| **Deck Construction** (Phase 6) | `references/slide-best-practices.md` + `references/impact-modeling.md` | Apply SCQA (from Phase 1) + Pyramid (from Phase 3) to slides. Build handoff for /411-deck. |
| **Phases 1-3** (conditional) | `references/platform-strategy.md` | Platform business facing a growth/scope problem? Map sides, interactions, engagement. 2x2 matrix. Platform assumption categories inlined in Phase 3 file. |
