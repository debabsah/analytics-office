"""parity_checks - tested helpers for prove-my-parity. Stdlib only.

All functions take the summary numbers the user provides (never raw data) and return
dicts ready to paste into the parity proof. The offsetting-error catch is the point:
a grand total inside tolerance proves nothing while any stratum is outside it.
"""


def tolerance_verdict(a, b, abs_tol, rel_tol):
    """Verdict for one comparison under a pre-pinned tolerance.

    a, b: the two values. abs_tol: absolute tolerance (same units). rel_tol: relative
    tolerance as a fraction of max(|a|,|b|) (e.g. 0.001 = 0.1%). Passes only if the
    difference is within BOTH bounds that were pinned (a None tolerance is ignored).
    """
    diff = b - a
    base = max(abs(a), abs(b))
    rel = (abs(diff) / base) if base else 0.0
    ok = True
    if abs_tol is not None and abs(diff) > abs_tol:
        ok = False
    if rel_tol is not None and rel > rel_tol:
        ok = False
    return {"a": a, "b": b, "diff": diff, "rel_diff": rel, "within_tolerance": ok}


def stratified_diff(strata, abs_tol, rel_tol):
    """The offsetting-error catch. strata: dict name -> (a, b).

    Returns per-stratum verdicts, the total-level verdict, and offsetting_error=True
    when the TOTAL is within tolerance while one or more strata are not - the most
    dangerous false pass in any tie-out.
    """
    rows = {name: tolerance_verdict(a, b, abs_tol, rel_tol) for name, (a, b) in strata.items()}
    total_a = sum(a for a, _ in strata.values())
    total_b = sum(b for _, b in strata.values())
    total = tolerance_verdict(total_a, total_b, abs_tol, rel_tol)
    failing = sorted(n for n, r in rows.items() if not r["within_tolerance"])
    return {
        "strata": rows,
        "total": total,
        "failing_strata": failing,
        "offsetting_error": bool(total["within_tolerance"] and failing),
        "parity": bool(total["within_tolerance"] and not failing),
    }


def residual_summary(total_gap, classified):
    """Decompose a gap. classified: dict cause -> signed amount explained.

    The unexplained remainder is what blocks sign-off when it exceeds the pinned
    tolerance - 'rounding' is a classification someone defends, not a default.
    """
    explained = sum(classified.values())
    unexplained = total_gap - explained
    shares = {k: (v / total_gap if total_gap else 0.0) for k, v in classified.items()}
    return {
        "total_gap": total_gap,
        "explained": explained,
        "unexplained": unexplained,
        "explained_share": (explained / total_gap) if total_gap else 1.0,
        "by_cause": shares,
    }
