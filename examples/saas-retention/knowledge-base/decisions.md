# Decisions & Assumptions  [all phases]
_Each: the decision, rationale, rejected alternatives, date, source event._

- 2026-05-20 - **Reframe the request** from a logo-churn dashboard to NRR + gross
  revenue churn + early-life churn by cohort. Rationale: logo churn cannot answer the
  funding decision and hides seat contraction. Rejected: building the dashboard as
  asked (logo-churn headline + 12-month decorative curve). (per timeline: the
  interrogation with Priya.)
- 2026-05-22 - **NRR is the headline retention metric; billing MRR is the source of
  record.** Rejected: Finance GL revenue (includes new logos, services, and timing)
  and the inherited logo view. (per timeline: contract lock v1.0.)
- 2026-05-22 - Pinned forks: start-of-period cohort base, trailing-12-month window,
  account grain, contraction included, trials excluded, fiscal US/Pacific, 5-day
  close then freeze. Left open: win-back cohort rule, Finance reconciliation bridge.
- 2026-05-28 - **Retire `vw_monthly_churn` as a source for the board retention number.**
  Reviewed against the locked contract, it implements neither contracted metric (logo
  churn, not MRR retention) and carries 4 Blocking defects. Rationale: it cannot be
  patched into NRR; the contracted metric is a separate build against billing MRR.
  Rejected: salvaging the view by bolting MRR onto the logo logic. (per timeline:
  `query-review.md`.)
- 2026-06-01 - **Hold the board recommendation** ("invest in growth, not onboarding")
  pending the Finance reconciliation and an early-life cohort cut. Rationale: the
  rehearsal cracked on the unreconciled gap. (per timeline: defense rehearsal.)
