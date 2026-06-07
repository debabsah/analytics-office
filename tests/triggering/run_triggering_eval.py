#!/usr/bin/env python3
"""
Automated triggering eval for the analytics-office bench (zero deps).

Measures self-routing: for each labeled prompt it spawns a fresh headless `claude -p`
and records which Skill (if any) the model chooses to invoke, then classifies that
against the expected bench skill. This is the objective instrument behind the
no-router bet - that each skill's description is sharp enough to self-route correctly
as the bench grows - and it surfaces collisions with co-installed plugins (for example
superpowers:brainstorming winning a "design" prompt).

Design (settled empirically; see README.md):
  - Runs in your NORMAL logged-in environment. No config-dir or credential plumbing.
  - Each case runs in a fresh neutral temp dir (NOT this repo) so the model reads the
    prompt as an end-user analytics ask, not as repo-development work in analytics-office.
  - Wandering tools are blocked and max-turns is 1, so the model's first action is the
    routing decision: cheap, and deterministic to parse from the stream-json.

Usage:
  python3 tests/triggering/run_triggering_eval.py             # full sweep
  python3 tests/triggering/run_triggering_eval.py --limit 2   # smoke test (first N)
  MODEL=claude-haiku-4-5 python3 tests/triggering/run_triggering_eval.py --limit 2

Exit code: nonzero only on an INTRA-BENCH defect (the wrong bench skill fired, or a
bench skill fired on a true-negative). SHADOW (a co-installed non-bench skill won) and
MISS (nothing fired) are reported as warnings, because they depend on what else the
runner happens to have installed, not on the sharpness of our descriptions alone.
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
CASES = os.path.join(HERE, "cases.tsv")
NS = "analytics-office:"
BLOCK = "Bash,Read,Glob,Grep,Edit,Write,WebFetch,WebSearch,TodoWrite,Task,ToolSearch,NotebookEdit"
PER_CASE_TIMEOUT = 150


def load_cases(path):
    cases = []
    with open(path, encoding="utf-8") as f:
        for raw in f:
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#") or "\t" not in line:
                continue
            expected, prompt = line.split("\t", 1)
            cases.append((expected.strip(), prompt.strip()))
    return cases


def fired_skill(prompt, model):
    claude = shutil.which("claude") or os.path.expanduser("~/.local/bin/claude")
    cmd = [claude, "-p", prompt, "--output-format", "stream-json",
           "--verbose", "--max-turns", "1", "--disallowedTools", BLOCK]
    if model:
        cmd += ["--model", model]
    workdir = tempfile.mkdtemp(prefix="ao-eval-")  # neutral cwd, removed below
    try:
        proc = subprocess.run(cmd, cwd=workdir, capture_output=True,
                              text=True, timeout=PER_CASE_TIMEOUT)
    except subprocess.TimeoutExpired:
        return "__timeout__"
    finally:
        shutil.rmtree(workdir, ignore_errors=True)
    fired = None
    for line in proc.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except Exception:
            continue
        if obj.get("type") == "assistant":
            for blk in obj.get("message", {}).get("content", []):
                if blk.get("type") == "tool_use" and blk.get("name") == "Skill" and fired is None:
                    fired = (blk.get("input") or {}).get("skill")
    return fired


def classify(expected, fired):
    """Return (verdict, is_intra_bench_defect)."""
    if fired == "__timeout__":
        return ("TIMEOUT", False)
    is_bench = bool(fired) and fired.startswith(NS)
    short = fired[len(NS):] if is_bench else fired
    if expected == "none":
        if not fired:
            return ("PASS (correctly none)", False)
        if is_bench:
            return (f"FALSE-FIRE ({short})", True)
        return (f"ok (non-bench fired: {fired})", False)
    if not fired:
        return ("MISS (nothing fired)", False)
    if is_bench and short == expected:
        return ("PASS", False)
    if is_bench:
        return (f"WRONG-BENCH (got {short})", True)
    return (f"SHADOW (got {fired})", False)


def main():
    model = os.environ.get("MODEL", "").strip()
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    cases = load_cases(CASES)
    if limit:
        cases = cases[:limit]
    print(f"Running {len(cases)} cases" + (f" (model={model})" if model else "") + " ...\n")
    tally, defects, shadows, misses = {}, [], [], []
    for i, (expected, prompt) in enumerate(cases, 1):
        verdict, is_defect = classify(expected, fired_skill(prompt, model))
        tally[verdict.split(" ")[0]] = tally.get(verdict.split(" ")[0], 0) + 1
        print(f"[{'X' if is_defect else ' '}] {i:2d}. want={expected:24s} -> {verdict}")
        print(f"        prompt: {prompt[:88]}")
        if is_defect:
            defects.append((expected, prompt, verdict))
        elif verdict.startswith("SHADOW"):
            shadows.append((expected, verdict))
        elif verdict.startswith("MISS"):
            misses.append((expected, verdict))
    print("\n=== tally ===")
    for k in sorted(tally):
        print(f"  {k}: {tally[k]}")
    if shadows:
        print("\n=== shadows (a co-installed non-bench skill won; environment-dependent) ===")
        for e, v in shadows:
            print(f"  want {e}: {v}")
    if misses:
        print("\n=== misses (nothing fired) ===")
        for e, v in misses:
            print(f"  want {e}: {v}")
    if defects:
        print("\n=== INTRA-BENCH DEFECTS (these fail the build) ===")
        for e, p, v in defects:
            print(f"  want {e}: {v}")
            print(f"     {p[:88]}")
        sys.exit(1)
    print("\nNo intra-bench defects.")
    sys.exit(0)


if __name__ == "__main__":
    main()
