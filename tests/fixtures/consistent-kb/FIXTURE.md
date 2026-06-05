# consistent-kb fixture (answer key — never copy into a cold-run dir)

PRECISION / CLEAN CONTROL for kb-reconcile. A genuinely CONSISTENT KB — the inverse of `drifted-kb`.

Hard negatives (each tempts a false positive):
- **NRR 108%** looks like an unsourced headline, but `nrr-reconciliation.md` (billing↔GL, signed off
  2026-05-28, tie-out 0.3%) backs it → flagging it "unsourced / no source on hand" is a FALSE POSITIVE.
- The brief says "reconciliation closed / board-ready" AND `kpi-contract.md` status is updated to
  **RECONCILED** to match, with `decisions.md` + `timeline.md` agreeing → there is NO partial-update
  drift (the exact trap in `drifted-kb` is RESOLVED here) → manufacturing that contradiction is a FALSE
  POSITIVE.
- The APAC **[Open]** item is correctly tracked in `open-questions.md` and labelled non-blocking in the
  brief → escalating it as drift is a FALSE POSITIVE.

PASS: reconciles with the per-claim checks shown; **no Blocking drift**; confirms contract ↔ brief ↔
decisions/timeline agree; marks 108% **sourced / verified per `nrr-reconciliation.md`** (at most a
caution to "re-run to confirm freshness", since a stored result is not a live run); invents no
contradiction; leaves the APAC item as correctly-open.

Cold-run method (per the kb-reconcile confound rule): scrub THIS `FIXTURE.md`, point the agent at a
neutral copy of `knowledge-base/` + `AGENTS.md` only.
