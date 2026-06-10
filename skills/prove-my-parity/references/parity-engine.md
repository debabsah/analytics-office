# Parity engine — prove-my-parity

Load at loop steps 2–5.

## The comparability checklist (gate BEFORE comparing)

Side-by-side for each side of the tie-out: population (who/what is counted; statuses,
test/internal rows), filters, window (and the timezone/date basis defining it), grain
(order vs line vs payment), units & currency (and FX date basis), timing basis (booking
vs cash, event vs load), rounding/precision, deduplication rules. **Any difference is
documented and either MAPPED (with the adjustment shown) or the tie-out is invalid** —
route a definitional dispute to kpi-contract. The worst tie-out outcome is not a gap; it
is agreement between two numbers that don't mean the same thing.

## Kit semantics (`parity_checks.py` — run via Bash on summaries provided)

- `tolerance_verdict(a, b, abs_tol, rel_tol)` — one comparison against the PRE-PINNED
  bounds; passes only within both.
- `stratified_diff(strata, abs_tol, rel_tol)` — the core: per-stratum verdicts, the total,
  `failing_strata`, and **`offsetting_error=True` when the total passes while strata
  fail** — that flag is a FAIL verdict, stated as such.
- `residual_summary(total_gap, classified)` — the honest remainder: classified amounts vs
  the total gap; `unexplained` above tolerance blocks sign-off.

## The residual taxonomy (every gap gets exactly one)

| Cause | Signature | Evidence that closes it |
|---|---|---|
| Timing | reverses in the adjacent period | the same strata next period; cut-off lists |
| Population | one side counts rows the other excludes | the row-class counts (test, internal, status) |
| Definition | the contracts differ (shipping, returns, FX basis) | the mapped adjustment recomputed |
| Units / FX | rate-date or precision basis differs | recompute at one basis |
| Duplicates | one side double-loads | distinct-vs-row counts on the suspect side |
| Defect | none of the above survives | routes to triage-my-number / review-my-query |
| **Unexplained** | the remainder | **blocks sign-off above tolerance — always** |

## Worked example — the cutover that totals blessed

Legacy vs new mart, May revenue: totals $14.203M vs $14.202M (0.007% — "ship it").
Comparability gate first: legacy includes shipping fees; the new contract excludes them
(~$0.31M) — so the matching totals ALREADY imply something is wrong elsewhere. Strata via
`stratified_diff`: AMER +$310k (the missing shipping inclusion), APAC −$312k (a dropped
late-arriving file) — `offsetting_error=True`. Verdict: **FAIL** — two real defects hiding
under a perfect total; residual ledger: definition +310k (mapped), defect −312k (routed to
triage), unexplained $1k (within the pinned $25k/0.2% tolerance). What clears it: load the
missing file, re-run the strata, owner re-accepts. The grand total never knew any of this.
