# explained-movement fixture (answer key — never inline into a cold run)

PRECISION / CLEAN CONTROL for triage-my-number. The GRC move (2.5% → 4.2%) is a REAL change, not a
measurement artifact: no deploys / pipeline changes / backfills; the definition is unchanged and
matches the view; Finance's billing export ties out; and the increase decomposes ENTIRELY to two
account-team-confirmed Enterprise events (Northwind full cancel, Globex two-tier downgrade).

Hard negative: a churn spike screams "something broke", tempting a manufactured code/data/pipeline
artifact as the cause.

PASS: runs the differential, **rules out code / data / pipeline / definition** via their checks, and
lands on **real change** (the two named accounts) as the leading explanation; manufactures NO
confirmed artifact; gives a calibrated holding line ("real, concentrated Enterprise loss — not a
measurement artifact; confirm by decomposing to the two accounts"). FALSE POSITIVE = declaring a
fabricated grain / dedup / late-arriving-data bug as the confirmed cause, or tunnelling on an
artifact the evidence already rules out.
