# Status Report — template + composition

Write at the end of every reporting pass. Lives at `knowledge-base/status-report.md`
(append per period, newest on top); no `knowledge-base/` anywhere up-tree → create it now
with this artifact plus the stub `README.md` index (per the office convention in
groundwork's kb-core-templates). Phase-tag the heading `[Operate]`.

```markdown
# Status — <period>  [Operate]
_For: <audience>. Composed <date> from the record + attributed updates.
RAG: <GREEN/AMBER/RED> (criteria: <pinned or stated>; <the red-condition for a green / what
clears an amber>). Watermelon test: <passes / capped by line N>._

## The ledger
| Item | Status | Says who / as of |
|---|---|---|
| <item> | Done (evidenced) / In-progress (attributed) / Slipped (+<delta>) / Blocked (<age>, <owner>) / Risk (open, <owner>) / Unknown — asked | <source · date> |

## Carried verdicts (with age)
- <artifact verdict> — <date>; `Re-audit when:` <condition> — <not met / MET → expired,
  routed back to <audit>>; <overridden gates ride here visibly>.

## Next period (owner-attributed commitments)
- <commitment> — <owner>.

## Asks
- <the unblock / decision / owner assignment needed, addressed to whom>.

## Notes
- <pressure asks recorded; re-bases named; anything the reader would otherwise learn late>.
```

## Composition with the knowledge base
- Newly surfaced blockers/risks → append to `open-questions.md` with age + owner.
- Append the report as a dated event in `timeline.md` (happened: reported <period> status —
  <RAG>; next: <top ask>), with `by:`.
- An expired verdict found while composing → flag it here AND recommend the re-audit; do
  not re-grade it yourself (that is the audit skill's lane).
- Add the Status Report to the KB `README.md` index.

When the office is git-tracked, offer the commit — `kb(status-truth): <period> status — <RAG>` — one artifact, one commit (the git-native convention in groundwork's kb-core-templates).
