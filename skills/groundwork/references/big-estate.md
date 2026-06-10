# Big-estate protocol — groundwork at enterprise scale

Load when the estate is too large to read whole (hundreds of objects, multi-GB extracts).
The gap engine's quality depends on what got read FIRST; reading "whatever was handed over,
in the order it arrived" is how an orientation silently overfits to the corner it saw.

## Ingestion priority (read in this order)

1. **Consumers first** — the reports, dashboards, and decisions the estate serves. Purpose
   anchors everything else; an estate map with no consumers is a parts list.
2. **Contracts and docs** — anything that pins meaning: metric definitions, schema docs,
   runbooks, the tribal README. Cheap to read, disproportionate gap-engine fuel.
3. **The spine of the named deliverable** — the objects feeding the thing you were asked
   about, walked backward from its consumer. Depth-first here.
4. **Everything else — sampled, never exhaustive.** Pick by fan-in (the most-referenced
   objects first); breadth-sample the rest. The estate will not be exhausted; that is not
   the goal.

## Budget honesty — the coverage-denominator rule

- **State the denominator.** "Read 14 of ~400 objects; selection rule: the NRR spine plus
  top fan-in." A coverage claim without its denominator is the orientation overclaiming.
- **The unread set is a named unknown.** It goes to `open-questions.md` as a gap, and
  every absence claim is scoped: "no X *in the 14 objects read*" — never "the estate has
  no X."
- **Large extracts get sampled profiling**: head, a slice from the middle, and the
  boundaries (first/last periods, min/max keys) — and the record states what
  "representative" meant. A whole-file read of a multi-GB extract is a hand-off to a data
  task, not a `Read`.

## When to stop

Orientation at scale is depth-first on the deliverable's spine, breadth-sampled everywhere
else. Stop when the spine is mapped and the top gaps are named — the completeness model
still runs (the gap you can't see is the point), but its empty slots are answered with
named unknowns, not with more reading.
