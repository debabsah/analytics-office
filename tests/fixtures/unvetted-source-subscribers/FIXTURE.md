# unvetted-source-subscribers fixture (answer key — never inline into a cold run)

HELD-OUT recall fixture for audit-my-assumptions. Different domain (SaaS subscriptions, not
travel/packages) and a different trap mechanism than `unvetted-source/`, so a GREEN run cannot
pattern-match the skill's worked example (the package case). Same class of trap: an inherited,
load-bearing **definition** that has gone stale, INVISIBLE in a clean single-window number.

## The buried defect (invisible by design)
`usp_ActiveSubscribers` defines an active subscriber as `s.PLAN_TYPE IN ('monthly','annual')` (plus
`STATUS_CODE = 2`). In the business this models, a **usage-based / PAYG plan** (`PLAN_TYPE = 'usage'`)
launched in 2024 and is the fastest-growing segment — and it is **silently excluded** by the inherited
inclusion-list. So "active subscribers" is now a *shrinking subset* of real active customers, and the
board number undercounts and masks the growth. The defect is INVISIBLE in the clean 2025 figure
(4,182 / $512,640) — nothing on the page signals it. It only surfaces if you (a) question whether
`PLAN_TYPE IN ('monthly','annual')` still captures every active subscriber, (b) ask whether new plan
types exist, (c) profile the population/trend by plan type, or (d) route "what counts as an active
subscriber" to the owner.

## PASS (detection lift) — the audit STOPS and excavates
- Does NOT just publish the headline on the inherited definition.
- Flags `PLAN_TYPE IN ('monthly','annual')` as an inherited definition to validate (TRUNK / NEEDS-DECISION),
  noting the code's inclusion-list may not match the business term "active subscriber".
- Bonus (strong): asks whether new plan types exist / calls for a by-plan-type trend / flags that the
  inclusion-list silently drops any plan not enumerated.
- Routes the intent-type assumptions to the owner; produces a graded register, not a board figure.

## FAIL (no lift) — publishes the number
Writes the 4,182 / $512,640 headline + takeaway, inheriting the stale inclusion-list silently
(a peripheral caveat about STATUS_CODE meaning or as-of date does NOT count as catching the trunk).

## Secondary inherited-assumption traps (a complete audit names them)
- `STATUS_CODE = 2` magic constant — still "active"? other active-like statuses (past-due, paused)?
- `IS_INTERNAL = 0` exclusion — current and complete?
- as-of / point-in-time semantics; whether MRR_USD is single-currency and net/gross.

## Use
RED in-situ (no skill) → expected FAIL (inherits the definition). GREEN in-situ (skill available among
distractors) → expected PASS (general method catches an unseen trap). Keep this file out of any cold-run dir.
