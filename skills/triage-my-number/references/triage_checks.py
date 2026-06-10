"""Tested decomposition kit for the triage-my-number skill. Python stdlib only.
Runs on summary counts the user provides ONLY — never raw rows, never a live system, and
never the deliverable metric itself: these split the hypothesis space, nothing more."""

__all__ = ["decompose_rate", "mix_shift"]


def decompose_rate(num_a, den_a, num_b, den_b):
    """Exact two-period decomposition of a rate move: which leg moved it?
    rate = num/den; delta = numerator_effect + denominator_effect (exact identity):
      numerator_effect   = (num_b - num_a) / den_b
      denominator_effect = num_a * (1/den_b - 1/den_a)
    verdict by the numerator's share of delta: 'numerator-driven' (>= 0.75),
    'denominator-driven' (<= 0.25), else 'mixed'. Shares may leave [0, 1] when the legs
    oppose each other — that is itself a finding (offsetting moves)."""
    if den_a == 0 or den_b == 0:
        raise ValueError("denominators must be nonzero")
    rate_a, rate_b = num_a / den_a, num_b / den_b
    delta = rate_b - rate_a
    num_effect = (num_b - num_a) / den_b
    den_effect = num_a * (1.0 / den_b - 1.0 / den_a)
    share_num = num_effect / delta if delta else 0.0
    if delta == 0:
        verdict = "no-change"
    elif share_num >= 0.75:
        verdict = "numerator-driven"
    elif share_num <= 0.25:
        verdict = "denominator-driven"
    else:
        verdict = "mixed"
    return {"rate_a": rate_a, "rate_b": rate_b, "delta": delta,
            "numerator_effect": num_effect, "denominator_effect": den_effect,
            "share_numerator": share_num, "verdict": verdict}


def mix_shift(segments):
    """Two-period mix-vs-rate split for a segmented rate (the Simpson's lens).
    segments: iterable of (name, num_a, den_a, num_b, den_b).
    Exact identity: delta_overall = mix_effect + rate_effect, where
      mix_effect  = sum((w_b - w_a) * r_a)   — population re-weighting alone
      rate_effect = sum(w_b * (r_b - r_a))   — true within-segment movement
    A 'jump' that is all mix_effect is a composition change, not a behavior change.
    verdict: 'rate-driven' (rate share >= 0.75) / 'mix-driven' (<= 0.25) / 'mixed'."""
    segs = [tuple(s) for s in segments]
    if not segs:
        raise ValueError("need at least one segment")
    tot_da = sum(s[2] for s in segs)
    tot_db = sum(s[4] for s in segs)
    if tot_da == 0 or tot_db == 0:
        raise ValueError("total denominators must be nonzero")
    for s in segs:
        if s[2] == 0 or s[4] == 0:
            raise ValueError(f"segment {s[0]!r} has a zero denominator")
    overall_a = sum(s[1] for s in segs) / tot_da
    overall_b = sum(s[3] for s in segs) / tot_db
    delta = overall_b - overall_a
    rows, mix_effect, rate_effect = [], 0.0, 0.0
    for name, na, da, nb, db in segs:
        wa, wb = da / tot_da, db / tot_db
        ra, rb = na / da, nb / db
        m = (wb - wa) * ra
        r = wb * (rb - ra)
        mix_effect += m
        rate_effect += r
        rows.append({"segment": name, "rate_a": ra, "rate_b": rb,
                     "weight_a": wa, "weight_b": wb,
                     "mix_contrib": m, "rate_contrib": r, "total_contrib": m + r})
    share_rate = rate_effect / delta if delta else 0.0
    if delta == 0:
        verdict = "no-change"
    elif share_rate >= 0.75:
        verdict = "rate-driven"
    elif share_rate <= 0.25:
        verdict = "mix-driven"
    else:
        verdict = "mixed"
    return {"overall_a": overall_a, "overall_b": overall_b, "delta": delta,
            "mix_effect": mix_effect, "rate_effect": rate_effect,
            "share_rate": share_rate, "verdict": verdict, "segments": rows}
