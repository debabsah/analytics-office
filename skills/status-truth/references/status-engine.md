# Status engine — status-truth

Load when building the ledger (loop step 3). Two jobs: name the green-wash move being
tempted, and grade every line so the report survives the follow-up question.

## The green-wash taxonomy (the moves to refuse)

| Move | What it looks like | The honest line instead |
|---|---|---|
| **Slip re-wording** | "progressing well" over a missed date | Slipped — was <date>, now <date> (+N days), because <attributed reason / unknown-asked> |
| **Silent re-base** | new plan, nothing "late" anymore | Re-based on <date> by <owner>; original delta +N — still reported |
| **Blocker aging-out** | the 3-week-old dependency vanishes from the update | Blocked <N> days — owner <who>, ask <what unblocks it> |
| **Risk evaporation** | a risk stops being mentioned | Open until its owner closes it; "no change" is a valid status, silence is not |
| **Verdict laundering** | last month's `trustworthy` reported as standing | Check `Re-audit when:` — condition met = EXPIRED → route to re-audit; overridden = visible |
| **Percent-done theater** | 60% → "nearly done"; 90% for three weeks | Done is evidenced; otherwise In-progress (attributed), with the last verifiable milestone |
| **Dependency optimism** | another team's promise booked as progress | Attributed In-progress at best, dependency named, confirmation asked |

## The ledger statuses (every line gets exactly one)

- **Done (evidenced)** — points at the artifact/event that proves it (timeline entry, merged
  change, signed-off contract).
- **In-progress (attributed)** — moving, per a named source (`by:`); the last verifiable
  milestone stated.
- **Slipped (delta)** — the old date, the new date, the delta, the attributed reason (or
  `unknown — asked`). A re-base is a slip with a decision attached.
- **Blocked (age + owner)** — what, since when, who owns the unblock, the explicit ask.
- **Risk (open, owner)** — unchanged is fine; closed only by the owner, with the closing
  event cited.
- **Unknown — asked** — you couldn't attribute it; the question is in the report, not a guess.

## RAG discipline + the watermelon test

Color only against pinned criteria — from `house-rules.md` when the org defines them, else
stated inline ("green = on plan ±3 days, no unowned blocker, no expired verdict"). Then the
**watermelon test**: scan the ledger — any red line inside (an unowned aging blocker, an
expired verdict carried into a decision, a slip past threshold) caps the outside at amber,
named. A green additionally states its red-condition: *"green — turns red if the vendor fix
misses Friday."* Status colors are claims; claims carry provenance like everything else.

## Worked example — the Friday steering update, done right

The record shows: cohort model build slipped 10 days (timeline, re-base decision by J.O.);
warehouse-access blocker open 18 days, no owner; last month's forecast-audit verdict
`trustworthy` with `Re-audit when: 4 new weekly actuals land` — 5 have landed; one item
genuinely done (contract v1.1 locked, signed off). The ask: "keep it tight and positive."

```markdown
# Status — week of <date>  [Operate]
**RAG: AMBER** (criteria: green = on plan ±3d, no unowned blocker, no expired verdict —
two lines below fail this; turns green when the blocker gets an owner and the re-audit runs)

| Item | Status | Says who / as of |
|---|---|---|
| NRR contract v1.1 locked | Done (evidenced) | kpi-contract lock, timeline 06-03, Finance sign-off |
| Cohort model build | Slipped (+10d; re-based 06-05 by J.O. — original date carried) | timeline + decisions |
| Warehouse access for QA | Blocked 18 days — NO OWNER; ask: platform team to assign | open-questions #4 |
| Demand forecast "trustworthy" | EXPIRED — re-audit condition met (5 new actuals vs 4) → re-audit before planning on it | forecast-audit 05-12 |
| Note | "Keep it positive" requested; honest version supplied | this report |
```

The wins still lead. The reds are named, aged, and owned. Nothing detonates in week six.
