#!/usr/bin/env python3
"""WLEP Phase 3 practical screen runner + mechanical scorer.
Runs each contract task once (fixed seed) against the local server, scores mechanically,
writes per-task raw output + compact scored summary."""
import json, re, sys, time, urllib.request

BASE = "http://127.0.0.1:8471"
CONTRACT = json.load(open("prompts/practical_contract.json"))
OUT_RAW = "results/practical/raw.jsonl"
OUT_SCORED = sys.argv[1] if len(sys.argv) > 1 else "results/practical/scored.json"

def gen(task):
    content = task["prompt"]
    if "passage" in task:
        content = f"Passage:\n{task['passage']}\n\n{task['prompt']}"
    payload = {"model": "nemotron-3-nano-4b-q4km", "temperature": CONTRACT["sampling"]["temperature"],
               "top_p": CONTRACT["sampling"]["top_p"], "seed": CONTRACT["sampling"]["seed"],
               "max_tokens": 300, "messages": [{"role": "user", "content": content}]}
    req = urllib.request.Request(BASE + "/v1/chat/completions",
        data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        body = json.loads(r.read())
    return body

def score(task, text):
    c = task["check"]; t = text.strip(); tl = t.lower()
    if c == "exact_stripped":
        return t == task["expected"], {}
    if c == "exact_stripped_contains":
        ok = task["expected"].lower() in tl and len(t) < 60
        return ok, {"length": len(t)}
    if c == "contains_exact_line":
        return any(line.strip() == task["expected"] for line in text.splitlines()), {}
    if c == "lines_1_to_5":
        nums = [ln.strip() for ln in t.splitlines() if ln.strip()]
        return nums == ["1", "2", "3", "4", "5"], {"lines": nums}
    if c == "json_fields":
        try:
            m = re.search(r"\{.*\}", t, re.S)
            obj = json.loads(m.group(0))
            exp = task["expected"]
            shipper_ok = str(obj.get("shipper", "")).lower() == str(exp["shipper"]).lower()
            ok = (obj.get("pears") == exp["pears"] and shipper_ok
                  and int(re.sub(r"[^\d]", "", str(obj.get("total_dollars")))) == exp["total_dollars"])
            return bool(ok), {"parsed": obj}
        except Exception as e:
            return False, {"error": str(e)}
    if c == "json_schema_prime17":
        try:
            m = re.search(r"\{.*\}", t, re.S)
            obj = json.loads(m.group(0))
            ok = isinstance(obj.get("is_prime"), bool) and obj["is_prime"] is True \
                 and isinstance(obj.get("label"), str) and re.search(r"17|seventeen", obj["label"], re.I)
            return bool(ok), {"parsed": obj}
        except Exception as e:
            return False, {"error": str(e)}
    if c == "json_array_schema":
        try:
            m = re.search(r"\[.*\]", t, re.S)
            arr = json.loads(m.group(0))
            cities = [o.get("city") for o in arr if isinstance(o, dict)]
            keys_ok = all(set(o.keys()) == {"city", "country"} for o in arr if isinstance(o, dict))
            return len(arr) == 3 and cities == task["expected_cities"] and keys_ok, {"parsed": arr}
        except Exception as e:
            return False, {"error": str(e)}
    if c == "contains_any":
        ok = all(w in tl for w in task.get("must_contain", [])) and any(w in tl for w in task["expected_any"])
        return ok, {}
    if c == "first_yes_no":
        m = re.search(r"\b(yes|no)\b", tl)
        got = m.group(1) if m else None
        return got == task["expected"], {"got": got}
    if c == "uncertainty_markers":
        asserted_person = bool(re.search(r"(?:won|was awarded to|went to|received).*\b(?:Dr\.?|Prof\.?|Mr\.?|[A-Z][a-z]+ [A-Z][a-z]+)", t)) and not any(x in tl for x in task["expected_markers"])
        found = any(x in tl for x in task["expected_markers"])
        return found or not asserted_person, {"uncertainty_found": found}
    if c == "contains_number":
        nums = [int(n.replace(",", "")) for n in re.findall(r"-?\d[\d,]*", t)]
        return task["expected_number"] in nums, {"numbers": nums[:10]}
    raise ValueError(f"unknown check {c}")

rows, scored = [], []
for task in CONTRACT["tasks"]:
    b = gen(task)
    msg = b["choices"][0]["message"]
    text = msg.get("content") or ""
    reasoning = msg.get("reasoning_content")
    ok, detail = score(task, text)
    row = {"id": task["id"], "category": task["category"], "pass": bool(ok),
           "output": text, "reasoning_content": reasoning,
           "detail": detail,
           "usage": b.get("usage", {}), "finish_reason": b["choices"][0]["finish_reason"]}
    rows.append(row)
    scored.append({"id": task["id"], "category": task["category"], "pass": bool(ok)})
    print(json.dumps({"id": task["id"], "pass": bool(ok)}))
    with open(OUT_RAW, "a") as f:
        f.write(json.dumps(row) + "\n")

npass = sum(r["pass"] for r in scored)
out = {"contract": CONTRACT["contract"], "version": CONTRACT["version"],
       "sampling": CONTRACT["sampling"], "tasks": scored,
       "passed": npass, "total": len(scored),
       "fraction_pass": round(npass / len(scored), 4),
       "note": "No WLEP advancement threshold exists; this fraction is reported without a gate decision.",
       "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
json.dump(out, open(OUT_SCORED, "w"), indent=2)
print(f"PASS {npass}/{len(scored)}")
