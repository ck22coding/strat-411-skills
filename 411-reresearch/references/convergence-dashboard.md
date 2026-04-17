# Convergence Dashboard Specification

Load this when producing the convergence dashboard at the end of each iteration (SKILL.md "Convergence" section).

## Dashboard Template

```
CONVERGENCE STATUS — Iteration [N]
═══════════════════════════════════════
Total claims in original ledger:    X
Claims passing refine (conf 3+):    X  (X%)
Claims failing refine:              X
  - Replaced this iteration:        X
  - Corroborated this iteration:    X
  - Marked UNFILLABLE:              X
  - Still open (carry to next):     X

L0 coverage:  X/X key findings fully sourced
L1 coverage:  X/X assumptions have >=1 conf 4+ source

PASS CRITERIA:
  [ ] All L0 findings backed by conf 3+ source
  [ ] Every assumption has >=2 independent sources (or 1 Tier 1)
  [ ] No DEAD/CLAIM NOT FOUND URLs remain
  [ ] Zero AI-content flags
  [ ] All UNFILLABLE claims removed from L1 narrative
  [ ] Verified rate >= 60%

VERDICT: [CONVERGED / NOT CONVERGED — X criteria failing]
═══════════════════════════════════════
```

## Verdict Logic

- **CONVERGED** — All 6 pass criteria check. Loop terminates.
- **NOT CONVERGED** — One or more criteria fail. State which ones and what the next iteration should focus on.
- **CONVERGED WITH CAVEATS (iteration 3 hard stop)** — On iteration 3, declare convergence regardless of remaining criteria. Dashboard shows which criteria still fail, and the Residual Risk section (see `output-format.md`) documents impact.

## Counting Rules

- **Total claims in original ledger** — count entries in the original `/411-refine` input ledger, not cumulative across iterations.
- **Claims passing refine** — entries with verified confidence ≥3 AND URL Status not DEAD/CNF.
- **Replaced / Corroborated / UNFILLABLE** — from this iteration's Replacement Map.
- **Still open** — failed-refine entries not resolved by this iteration's Replacement Map.
- **L0 coverage** — count L0 bullets; each must trace to at least one conf ≥3 ledger entry.
- **L1 coverage** — count assumptions in the case; each must have ≥1 ledger entry at conf ≥4.

## Iteration Detection

Check the input for prior Replacement Maps or "Iteration [N]" headers:

- Found → increment counter
- Not found → iteration 1

## Termination Discipline (Hard Rules)

- **Iteration 1** — standard strategies; most failures resolve here.
- **Iteration 2** — escalate to proxy data and Adjacent Data for P2/P3 failures only; focus remaining effort on P1.
- **Iteration 3** — final pass; remaining failures declared UNFILLABLE with full justification; produce Residual Risk section.
- **Hard stop after iteration 3** — do not invoke a fourth iteration regardless of convergence status.
