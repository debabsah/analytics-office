# Behavioral dry-run — groundwork

In a Claude Code session with the bi-copilot plugin enabled, run groundwork against
`tests/fixtures/inherited-estate-sample/` (the proc + ticket). It PASSES if it:

- [ ] Classifies this as an **inherited data estate** (loads Type A completeness model).
- [ ] Reads `usp_LoadSalesDaily.sql` as text WITHOUT asking to query any database.
- [ ] Surfaces the **loose threads**: (a) nothing populates `dbo.SalesStage`; (b) the hardcoded `RegionID = 7` is unexplained.
- [ ] Surfaces **completeness gaps** via questions: who consumes `SalesDaily`? what schedule/job runs this? what happens on failure (note the TRUNCATE → not restartable mid-fail)?
- [ ] Creates a `knowledge-base/` with the always-on core files + a root `AGENTS.md`.
- [ ] Appends a dated entry to `timeline.md`.
- [ ] Proposes a relevant catalog artifact (e.g., `lineage.md`) and does NOT instantiate the whole catalog.
- [ ] On a follow-up "catch me up", summarizes state + open questions from the KB.
