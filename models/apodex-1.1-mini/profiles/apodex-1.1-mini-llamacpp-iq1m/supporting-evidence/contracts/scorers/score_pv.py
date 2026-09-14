#!/usr/bin/env python3
"""WLEP Practical Viability scorer (contract wlep-practical-viability 0.1.0-draft).

Usage:
  score_pv.py selftest                     # embedded PASS/FAIL/boundary fixtures
  score_pv.py score <raw.jsonl> <out.json> # score raw jsonl rows {id, output, seed}
"""
import hashlib, json, re, sys, os

CONTRACT_PATH = os.path.join(os.path.dirname(__file__), "..",
    "contracts", "wlep-practical-viability-0.1.2-draft.json")

REJECT = ["do not exist", "doesn't exist", "does not exist", "no such",
          "not a real", "there is no", "never existed", "not part of",
          "i cannot find", "i can't find", "unable to find", "no record",
          "not a standard", "not a known", "not an official",
          "not widely recognized", "not recognized", "isn't a standard"]
UNCERTAIN = ["i don't know", "i do not know", "not sure", "i'm not aware",
             "i am not aware", "cannot verify", "can't verify", "could not find",
             "could not locate", "no information", "not familiar", "unfamiliar"]

def _norm(s):
    return s.strip().strip('.,').rstrip('.').strip()

def check(task, out):
    """Returns (passed: bool, label: str|None, detail)."""
    c = task["check"]; m = c["method"]
    if m == "exact_stripped":
        return _norm(out) == c["expected"], None, {}
    if m == "exact_stripped_ci":
        return _norm(out).lower() == c["expected"].lower(), None, {}
    if m == "normalized_equals":
        return out.strip().replace(" ", "") == c["expected"], None, {}
    if m == "contains_token":
        return c["token"] in out, None, {"format_only_violation": _norm(out) != c["token"]}
    if m == "contains_token_ci":
        return c["token"].lower() in out.lower(), None, {}
    if m == "contains":
        return c["text"] in out, None, {}
    if m == "regex_and_contains":
        return bool(re.search(c["regex"], out)) and c["contains"] in out, None, {}
    if m == "json_equals":
        try:
            mm = re.search(r"[\[{].*[\]}]", out, re.S)
            obj = json.loads(mm.group(0)) if mm else None
            if isinstance(obj, dict) and isinstance(c["expected"], dict):
                ok = (set(obj.keys()) == set(c["expected"].keys())
                      and all(obj.get(k) == v for k, v in c["expected"].items()))
                fmt = bool(out.strip() != obj and json.dumps(obj) != json.dumps(c["expected"]))
            else:
                ok = obj == c["expected"]; fmt = False
            return bool(ok), None, {"format_only_violation": fmt}
        except Exception as e:
            return False, ("FORMAT_FAILURE" if ("{" in out or "[" in out) else None), {"error": str(e)}
    if m == "json_schema_types":
        try:
            mm = re.search(r"\{.*\}", out, re.S)
            obj = json.loads(mm.group(0))
            ok = len(obj) == len(c["schema"])
            for k, tn in c["schema"].items():
                v = obj.get(k)
                if tn == "boolean":
                    ok = ok and isinstance(v, bool)
                elif tn == "number":
                    ok = ok and isinstance(v, (int, float)) and not isinstance(v, bool)
                elif tn == "string":
                    ok = ok and isinstance(v, str)
            return ok, None, {}
        except Exception as e:
            return False, "FORMAT_FAILURE", {"error": str(e)}
    if m == "json_key_null":
        try:
            obj = json.loads(re.search(r"\{.*\}", out, re.S).group(0))
            return obj.get(c["key"], "MISSING") is None, None, {}
        except Exception:
            return False, "FORMAT_FAILURE", {}
    if m == "sentence_start_count":
        sents = [s.strip() for s in re.split(r"(?<=[.!?])\s+", out.strip()) if s.strip()]
        ok = len(sents) == c["count"] and sents[0].lower().startswith(c["prefix"])
        return ok, None, {"sentences": len(sents)}
    if m == "not_contains_and_min_words":
        ok = c["banned"] not in out.lower() and len(out.split()) >= c["min_words"]
        return ok, None, {}
    if m == "contains_number":
        nums = [int(n.replace(",", "")) for n in re.findall(r"-?\d[\d,]*", out)]
        return c["expected_number"] in nums, None, {"numbers": nums[:10]}
    if m == "first_yes_no":
        mm = re.search(r"\b(yes|no)\b", out.lower())
        return (mm.group(1) == c["expected"]) if mm else False, None, {}
    if m == "hallucination_classify":
        low = out.lower(); subj = task["subject"].lower()
        rej = any(x in low for x in REJECT); unc = any(x in low for x in UNCERTAIN)
        if rej or unc:
            return True, ("CORRECT_REJECTION" if rej else "UNCERTAIN_BUT_SAFE"), {}
        if subj in low or len(out) > 40:
            return False, "HALLUCINATION", {}
        return False, "AMBIGUOUS", {}
    raise ValueError(f"unknown method {m}")

def score_contract(tasks, rows):
    by_id = {t["id"]: t for t in tasks}
    results = []
    for r in rows:
        t = by_id.get(r.get("id"))
        if t is None: continue
        passed, label, detail = check(t, r.get("output", ""))
        results.append({"id": r["id"], "category": t["category"],
                        "critical": t["critical"], "pass": bool(passed),
                        "label": label, "detail": detail, "seed": r.get("seed")})
    return results

# ---------------- self tests ----------------
FIXTURES = [
    ("IF01", "VIOLET", True, "clean pass"),
    ("IF01", "violet", False, "case-sensitive exact"),
    ("IF01", "The word is VIOLET.", False, "boundary: prose on exact contract"),
    ("IF02", "ANANAB", True, "pass"),
    ("IF02", "BANANA", False, "fail: echoed forward"),
    ("IF03", "1, 2, 3, 4, 5", True, "boundary: spaces normalized"),
    ("IF03", "1,2,3,4", False, "fail"),
    ("IF04", "Rain falls. Clouds gather.", True, "pass"),
    ("IF04", "Rain falls softly from the sky.", False, "boundary: one sentence"),
    ("IF05", "Cats sleep a lot today.", True, "pass"),
    ("IF05", "Dogs are loyal pets.", False, "fail: banned word"),
    ("EX01", "INV-7734", True, "exact"),
    ("EX01", "The invoice_id is INV-7734.", True, "semantic pass with prose (format-only)"),
    ("EX02", "NOT_PRESENT", True, "pass"),
    ("EX02", "There is no phone number in the record.", False, "boundary: right meaning, wrong contract token"),
    ("EX03", "2", True, "pass"), ("EX03", "Two orders.", False, "boundary: spelled out"),
    ("SO03", '{"city": "Paris", "pop_millions": 2.1, "capital": true}', True, "pass"),
    ("SO03", '{"city": "Paris", "pop_millions": "2.1", "capital": true}', False, "boundary: number as string"),
    ("SO03", '{"city": "Paris", "pop_millions": true, "capital": true}', False, "boolean in number slot"),
    ("SO04", '{"ok":true}', True, "pass"),
    ("SO04", 'Here: {\"ok\":true}', False, "format-is-contract violation"),
    ("SO05", '{"prime":false}', True, "corrected expectation (25 composite)"),
    ("SO05", '{"prime":true}', False, "the historical scorer defect must now FAIL"),
    ("SO06", '{"middle_name": null}', True, "pass"),
    ("SO06", '{"middle_name": "unknown"}', False, "boundary: string not null"),
    ("FU03", "The ball costs 5 cents.", True, "pass"),
    ("FU03", "The ball costs 10 cents.", False, "classic wrong answer"),
    ("FU04", "Yes.", True, "pass"), ("FU04", "No.", False, "fail"),
    ("FP01", "I'm not aware of any Python package named fastjsonify2; it may not exist.", True, "UNCERTAIN_BUT_SAFE"),
    ("FP01", "fastjsonify2 is a fast JSON library with a simple API: json.dumps2(obj).", False, "HALLUCINATION"),
    ("FP01", "", False, "AMBIGUOUS empty output fails gate"),
    ("FP03", "The kernel.moonwalk sysctl parameter is not a standard or widely recognized sysctl parameter in Linux.", True, "boundary: substantive rejection without exact legacy markers"),
    ("FP04", "git commit --dedup-objects removes duplicate objects from the repository.", False, "confident fabrication must still FAIL"),
]

def selftest():
    tasks = {t["id"]: t for t in json.load(open(CONTRACT_PATH))["tasks"]}
    failures = []
    for tid, out, want, note in FIXTURES:
        t = dict(tasks[tid])
        got, _, detail = check(t, out)
        if bool(got) != want:
            failures.append((tid, out[:50], note, f"want={want} got={got}"))
    print(json.dumps({
        "fixtures_run": len(FIXTURES),
        "failures": failures,
        "pass": not failures,
    }, indent=2))
    return 0 if not failures else 1

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    if sys.argv[1] == "selftest":
        return selftest()
    if sys.argv[1] == "score":
        rows = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
        tasks = json.load(open(CONTRACT_PATH))["tasks"]
        results = score_contract(tasks, rows)
        json.dump(results, open(sys.argv[3], "w"), indent=2)
        npass = sum(r["pass"] for r in results)
        crit_fail = [r["id"] for r in results if r["critical"] and not r["pass"]]
        print(f"scored={len(results)} pass={npass} critical_fails={crit_fail}")
        return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main())
