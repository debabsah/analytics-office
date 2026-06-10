# Parity Proof — template + composition

Write per tie-out. Lives at `knowledge-base/parity-proof.md` (append per proof, newest on
top); no `knowledge-base/` anywhere up-tree → create it now with this artifact plus the
stub `README.md` index (per the office convention in groundwork's kb-core-templates);
provided extracts get dated copies in `inputs/`. Phase-tag `[Validate]`.

```markdown
# Parity Proof — <number> · <side A> vs <side B> · <window>  [Validate]
_Proven <date>, by <who>. Gates: <the cutover / close / trust decision>. Pressure noted:
<if any>. **Tolerance (pinned BEFORE results):** abs <x> / rel <y%>, owner <who>, <date>._

## Comparability map
| Dimension | Side A | Side B | Same? / Mapped how |
|---|---|---|---|
| population / window / grain / units / timing / rounding | … | … | … |

## Stratified results (kit: parity_checks.stratified_diff)
| Stratum | A | B | diff | rel | within? |
|---|---|---|---|---|---|
**Total:** <…> · failing strata: <list> · offsetting flag: <true/false>

## Residual ledger (kit: residual_summary)
| Cause | Amount | Evidence | Routed to |
|---|---|---|---|
**Unexplained: <amount> — <within tolerance / BLOCKS sign-off>.**

## Verdict
**PARITY / QUALIFIED (residuals accepted by <owner>, <date>) / FAIL** — <one sentence>.
What clears a FAIL: <the exact steps>. **Re-audit when:** <next period lands / next
cutover step / either side's definition changes>.
```

## Composition with the knowledge base
- Residuals needing work → `open-questions.md` (owners); the proof → a dated `timeline.md`
  event (`by:`); add to the KB `README.md` index.
- A definitional difference found at the gate → kpi-contract (and note it in the
  contract's file); a defect → triage-my-number / review-my-query.
- A false-pass stopped (the offsetting total that almost shipped) appends one line to
  `knowledge-base/catches.md`.
- When the office is git-tracked, offer the commit — `kb(prove-my-parity): <number> <A-vs-B> — <verdict>` — one artifact, one commit (the git-native convention in groundwork's kb-core-templates).
