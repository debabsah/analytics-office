import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "skills", "triage-my-number", "references"))
import triage_checks as tc


def test_decompose_numerator_driven():
    # churn 4% -> 11% with a flat base: pure numerator move (the cancels jumped)
    r = tc.decompose_rate(40, 1000, 110, 1000)
    assert abs(r["delta"] - 0.07) < 1e-12
    assert abs(r["numerator_effect"] - 0.07) < 1e-12
    assert abs(r["denominator_effect"]) < 1e-12
    assert r["verdict"] == "numerator-driven"
    # exact identity
    assert abs(r["numerator_effect"] + r["denominator_effect"] - r["delta"]) < 1e-12


def test_decompose_denominator_driven():
    # same 40 cancels, but the start-base quietly shrank to 364: the grain-bug signature
    r = tc.decompose_rate(40, 1000, 40, 364)
    assert abs(r["rate_b"] - 40 / 364) < 1e-12
    assert abs(r["numerator_effect"]) < 1e-12
    assert abs(r["denominator_effect"] - (40 / 364 - 0.04)) < 1e-12
    assert r["verdict"] == "denominator-driven"
    assert abs(r["numerator_effect"] + r["denominator_effect"] - r["delta"]) < 1e-12


def test_decompose_mixed_and_guards():
    r = tc.decompose_rate(40, 1000, 55, 870)  # both legs moved
    assert r["verdict"] == "mixed"
    assert abs(r["numerator_effect"] + r["denominator_effect"] - r["delta"]) < 1e-12
    assert tc.decompose_rate(40, 1000, 40, 1000)["verdict"] == "no-change"
    try:
        tc.decompose_rate(40, 0, 40, 1000); assert False, "should have raised"
    except ValueError:
        pass


def test_mix_shift_pure_mix():
    # every segment's rate is FLAT; only the population mix moved (Simpson's signature):
    # enterprise (1% churn) shrinks 500->200, smb (8%) grows 500->800
    segs = [("enterprise", 5, 500, 2, 200), ("smb", 40, 500, 64, 800)]
    r = tc.mix_shift(segs)
    assert abs(r["overall_a"] - 0.045) < 1e-12
    assert abs(r["overall_b"] - 0.066) < 1e-12
    assert abs(r["delta"] - 0.021) < 1e-12
    assert abs(r["mix_effect"] - 0.021) < 1e-12
    assert abs(r["rate_effect"]) < 1e-12
    assert r["verdict"] == "mix-driven"
    # per-segment contributions sum exactly to delta
    assert abs(sum(s["total_contrib"] for s in r["segments"]) - r["delta"]) < 1e-12


def test_mix_shift_pure_rate():
    # mix constant, smb churn genuinely doubles: a real behavior change
    segs = [("enterprise", 5, 500, 5, 500), ("smb", 40, 500, 80, 500)]
    r = tc.mix_shift(segs)
    assert abs(r["mix_effect"]) < 1e-12
    assert abs(r["rate_effect"] - 0.04) < 1e-12
    assert r["verdict"] == "rate-driven"
    assert abs(r["mix_effect"] + r["rate_effect"] - r["delta"]) < 1e-12


def test_mix_shift_guards():
    try:
        tc.mix_shift([]); assert False, "should have raised"
    except ValueError:
        pass
    try:
        tc.mix_shift([("a", 1, 0, 1, 10)]); assert False, "should have raised"
    except ValueError:
        pass


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    for f in fns:
        f(); print("PASS", f.__name__)
    print(f"\n{len(fns)} tests passed")
