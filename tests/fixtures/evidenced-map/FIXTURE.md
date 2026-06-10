# evidenced-map fixture (answer key — never copy into a cold-run dir)

CLEAN control for map-my-estate (the false-alarm side). Every edge is documented:
billing API → CHARGES (attributed: load_charges, S. Lee, 06-08), ACCOUNTS→CHARGES (FK in
ddl), CHARGES→vw_daily_charges (the view's own SELECT), vw_daily_charges→Finance
dashboard (attributed, Finance, 06-08).

## PASS
- All four edges SOLID, each cited (FK / view text / attributed landscape entries);
  derived-from header + ledger; coverage line "4 evidenced, 0 unverified, 0 islands".
- No manufactured dashes, no invented uncertainty on a fully-documented slice.

## FAIL
- Cry-wolf: dashing the attributed edges ("owner statements aren't evidence") or inventing
  gaps — the cartography edition of the auditor who cries Blocking on clean code.
  (Attributed owner statements ARE evidence per the engine.)
