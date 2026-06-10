#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "prove-my-parity", "references"))
from parity_checks import tolerance_verdict, stratified_diff, residual_summary

passed = 0

def check(name, cond):
    global passed
    assert cond, name
    passed += 1

# tolerance_verdict: within both bounds
v = tolerance_verdict(1000.0, 1000.5, abs_tol=1.0, rel_tol=0.001)
check("within both", v["within_tolerance"] and abs(v["diff"] - 0.5) < 1e-9)
# abs breach
check("abs breach", not tolerance_verdict(1000.0, 1002.0, 1.0, 0.01)["within_tolerance"])
# rel breach
check("rel breach", not tolerance_verdict(100.0, 101.0, 5.0, 0.001)["within_tolerance"])

# stratified_diff: THE OFFSETTING CATCH - totals match, strata wildly off
s = stratified_diff({"A": (1000.0, 1310.0), "B": (1000.0, 688.0)}, abs_tol=5.0, rel_tol=0.005)
check("offsetting flagged", s["offsetting_error"] and not s["parity"])
check("both strata fail", s["failing_strata"] == ["A", "B"])
check("total deceptively within", s["total"]["within_tolerance"])

# stratified_diff: genuine parity
s2 = stratified_diff({"A": (1000.0, 1000.2), "B": (500.0, 499.9)}, abs_tol=1.0, rel_tol=0.01)
check("genuine parity", s2["parity"] and not s2["offsetting_error"] and not s2["failing_strata"])

# residual_summary
r = residual_summary(100.0, {"timing": 60.0, "duplicates": 25.0})
check("unexplained remainder", abs(r["unexplained"] - 15.0) < 1e-9)
check("explained share", abs(r["explained_share"] - 0.85) < 1e-9)

print(f"{passed} tests passed")
