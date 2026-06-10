# Estate Map — template + composition

Write per mapping pass. Lives at `knowledge-base/estate-map.md` (append per view set,
newest on top); no `knowledge-base/` anywhere up-tree → create it now with this artifact
plus the stub `README.md` index (per the office convention in groundwork's
kb-core-templates); provided DDL/code gets dated copies in `inputs/`. Phase-tag
`[Understand]`.

```markdown
# Estate Map — <scope/anchor>  [Understand]
_Drawn <date>, by <who>. View: <ER / lineage>. Scope: <the anchor + boundary>.
**Derived from:** <file (as-of date)> · <file (date)> · … — re-run this skill to refresh;
`kb-reconcile` flags this map stale when the record outruns it._
_Coverage: <N> nodes · <E> evidenced edges · <U> unverified · <I> islands._

```mermaid
<the view — solid = evidenced; dashed/[unverified] = unsupported; islands labeled>
```

## Edge ledger
| Edge | Kind | Evidence | Status |
|---|---|---|---|
| <A → B> | FK / join / feed / ownership | <file:line / attributed statement> | evidenced / **[unverified]** + the confirming question |

## Gaps (the map's yield)
- <each dashed edge / island as a question, with who can answer it> → also append to
  `open-questions.md`.
```

## Composition with the knowledge base
- Dashed edges and islands → `open-questions.md` (they are groundwork interview fuel);
  the mapping pass → a dated `timeline.md` event (`by:`); add the map to the KB
  `README.md` index.
- A fabricated-edge avoided (plausible wiring refused, recorded as a gap instead) also
  appends one line to `knowledge-base/catches.md` — the wins ledger.
- When the office is git-tracked, offer the commit — `kb(map-my-estate): <scope> map — <E> evidenced, <U> unverified` — one artifact, one commit (the git-native convention in groundwork's kb-core-templates).
