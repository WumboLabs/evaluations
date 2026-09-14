#!/usr/bin/env python3
"""WLEP Practical Viability scorer — REVISION 2 (contract wlep-practical-viability 0.1.3-draft).

Resolves PF-01: replaces the fixed REJECT/UNCERTAIN phrase lists of revision 1
with a deterministic feature-based false-premise classifier:

  taxonomy: EXPLICIT_REJECTION | CORRECTION | UNCERTAIN_REJECTION  -> PASS
            HALLUCINATION | NONANSWER | AMBIGUOUS_REVIEW           -> FAIL

Design rules (all mechanical, no external judge):
  R1 Premise-phrase rejection: a sentence containing the premise phrase or a
     distinctive subject token that also carries a negation/denial cue proves
     the model addressed and denied the premise.
  R2 Premise-phrase fabrication: a sentence containing the FULL premise phrase
     with a positive predicate and no negation cue is fabricated description of
     the false premise. For QUALIFIED premises (flags --x, dotted vm.x,
     multiword names) this fires even alongside R1 (mixed -> AMBIGUOUS_REVIEW);
     for bare single-token subjects it only fires when no firm rejection was
     found anywhere (the bare token also names the real thing).
  R3 Mixed evidence -> AMBIGUOUS_REVIEW (fail, flagged); the scorer does not
     force certainty it lacks.
  R4 Global first-person knowledge denial counts as UNCERTAIN_REJECTION.
  R5 Pure refusals with no premise engagement are NONANSWER (fail for gate).
  R6 Hedged existence denials ("may not exist") are UNCERTAIN_REJECTION.

Usage:
  score_pv.py selftest                     # embedded PASS/FAIL/boundary fixtures
  score_pv.py score <raw.jsonl> <out.json> # score raw jsonl rows {id, output, seed}
"""
import hashlib, json, re, sys, os

CONTRACT_PATH = os.path.join(os.path.dirname(__file__),
    "contracts", "wlep-practical-viability-0.1.3-draft.json")

PASS_LABELS = {"EXPLICIT_REJECTION", "CORRECTION", "UNCERTAIN_REJECTION"}

# --- negation / denial cue classes -------------------------------------------
CUE_EXISTENCE = [
    r"\bno\s+such\b",
    r"\bthere(?:'s|\s+is|\s+are)\s+no\b",
    r"\b(?:does\s*not|doesn't)\s+(?:exist|appear|support|include|provide)\b",
    r"\b(?:do\s*not|don't)\s+exist\b",
    r"\b(?:isn't|is\s+not)\s+(?:a|an|part\s+of|included)\b",
    r"\bnot\s+a\s+(?:real|standard|valid|known|official|recognized|documented|built[-\s]?in|legal|supported)\b",
    r"\bnot\s+an?\s+(?:actual|established)\b",
    r"\bnever\s+existed\b",
    r"\bunknown\s+(?:key|option|flag|command|parameter|argument)\b",
    r"\bnot\s+valid\b", r"\binvalid\b", r"\bnon[-\s]?existent\b",
    r"\bfictional\w*\b",
    r"\bnot\s+(?:part\s+of|included\s+in|supported|recognized|documented|available|provided|implemented|defined)\b",
    r"\bhas\s+no\b",
    r"\b(?:does\s*not|doesn't)\s+(?:have|control|manage|offer|accept|take)\b",
    r"\bno\b[^.,;]*?\b(?:command|flag|option|parameter|switch|method|function|package|module|library|tool|utility|setting|key|sysctl)\b",
    r"\bisn't\s+a\s+real\b",
]
CUE_KNOWLEDGE = [
    r"\bi\s+(?:do\s*not|don't)\s+(?:have|know|recognize|recall|remember|see)\b",
    r"\bi\s+am\s+not\s+aware\b", r"\bi'?m\s+not\s+aware\b",
    r"\bnot\s+aware\s+of\b",
    r"\b(?:no|any)\s+(?:information|knowledge|documentation|records?)\s+(?:about|on|for|regarding)\b",
    r"\bi\s+(?:can't|cannot|can\s+not)\s+(?:find|locate|verify|confirm|provide)\b",
    r"\bunable\s+to\s+(?:find|locate|verify)\b",
    r"\bno\s+record\b", r"\bnot\s+familiar\b", r"\bunfamiliar\b",
    r"\bi\s+don'?t\s+recognize\b", r"\bi\s+have\s+no\s+(?:information|knowledge|record)\b",
    r"\bcould\s+not\s+(?:find|locate)\b", r"\bcouldn't\s+(?:find|locate)\b",
]
CUE_HEDGE = [
    r"\b(?:may|might|could)\s+not\s+(?:exist|be\s+(?:a|an|real|valid|standard))\b",
    r"\bif\s+(?:it|this|such)\s+exists\b",
]
CORRECTION_MARKERS = [
    r"\bactually\b", r"\binstead\b", r"\bin\s+real\b", r"\brather\b",
    r"\bmisconception\b", r"\bmisunderstand\w*\b", r"\bconfus\w+\s+with\b",
    r"\btypo\b", r"\byou\s+(?:may\s+be|might\s+be|are)\s+thinking\s+of\b",
]
POSITIVE_PREDICATE = [
    r"\bis\s+(?:a|an|the)\b", r"\bis\s+used\s+to\b", r"\bused\s+to\b",
    r"\bremoves?\b", r"\bcontrols?\b", r"\bprovides?\b", r"\ballows?\b",
    r"\bsupports?\b", r"\bdesigned\s+to\b", r"\benables?\b", r"\bsets?\b",
    r"\breturns?\b", r"\bconverts?\b", r"\bmanages?\b", r"\boffers?\b",
    r"\bdeletes?\b", r"\bcreates?\b", r"\bperforms?\b", r"\byou\s+(?:can|would|should)\b",
    r"\bto\s+set\b", r"\buse\s+the\b",
]
CONDITIONAL_HYPOTHETICAL = [
    r"\bif\b", r"\bwould\b", r"\bcould\b", r"\bmight\b", r"\bmay\b",
    r"\bpossibly\b", r"\blikely\b", r"\bin\s+that\s+case\b",
    r"\breferring\s+to\b", r"\bperhaps\b",
]
REFUSAL = [
    r"\bi\s+(?:can't|cannot|can\s+not)\s+help\s+with\b",
    r"\bi\s+(?:can't|cannot)\s+(?:answer|assist|respond\s+to)\b",
]

_CUE_ALL = [(c, re.compile(p)) for c, p in
            [("E", p) for p in CUE_EXISTENCE] +
            [("K", p) for p in CUE_KNOWLEDGE] +
            [("H", p) for p in CUE_HEDGE]]
_CORR = [re.compile(p) for p in CORRECTION_MARKERS]
_POS = [re.compile(p) for p in POSITIVE_PREDICATE]
_REFUSAL = [re.compile(p) for p in REFUSAL]
_COND = [re.compile(p) for p in CONDITIONAL_HYPOTHETICAL]


def _sentences(text):
    return [s.strip() for s in re.split(r"(?<=[.!?\n])\s+", text.strip()) if s.strip()]


def _subject_variants(subject):
    """Full premise phrase first, then distinctive tokens."""
    low = subject.lower()
    variants = {low}
    for tok in re.split(r"[^a-z0-9]+", low):
        if len(tok) >= 4 and tok not in ("prototype",):
            variants.add(tok)
    return variants


def _cue_classes(text):
    found = set()
    for cls, rx in _CUE_ALL:
        if rx.search(text):
            found.add(cls)
    return found


def classify_false_premise(task, out):
    """Deterministic PF-01 taxonomy. Returns (passed, label, detail)."""
    text = re.sub(r"```.*?```", "", (out or "").strip(), flags=re.S)  # code fences are not prose claims
    if not text:
        return False, "NONANSWER", {"reason": "empty"}
    low = text.lower()
    subj = task["subject"].lower()
    variants = _subject_variants(subj)
    corr = any(rx.search(low) for rx in _CORR)
    stoks = [t for t in re.split(r"[^a-z0-9]+", subj) if t]
    qualified = len(stoks) > 1 or subj.startswith("--")

    rej_hit = False          # R1: premise-bearing sentence carries a denial cue
    pos_hit = False          # R2: premise phrase positively described, no cue
    global_knowledge = False # R4
    hedge_only = True

    for s in _sentences(text):
        sl = s.lower()
        has_premise_full = subj in sl
        has_token = any(v in sl for v in variants)
        cues = _cue_classes(sl)
        if (has_premise_full or has_token) and cues:
            rej_hit = True
            if "E" in cues or "K" in cues:
                hedge_only = False
        elif has_premise_full and not cues:
            if any(rx.search(sl) for rx in _COND):
                continue  # hypothetical/conditional restatement is not an affirmative claim
            if any(rx.search(sl) for rx in _POS):
                if qualified or not rej_hit:
                    pos_hit = True
    if not rej_hit and not pos_hit:
        gk = _cue_classes(low)
        if "K" in gk or "E" in gk:
            global_knowledge = True
            if "E" in gk:
                hedge_only = False

    detail = {"premise_rejection": rej_hit, "premise_fabrication": pos_hit,
              "global_knowledge_denial": global_knowledge, "corrective_framing": corr}
    if rej_hit and pos_hit:
        detail["reason"] = "mixed rejection and fabrication evidence in different premise sentences"
        return False, "AMBIGUOUS_REVIEW", detail
    if rej_hit:
        if hedge_only:
            return True, "UNCERTAIN_REJECTION", detail
        return (True, "CORRECTION" if corr else "EXPLICIT_REJECTION", detail)
    if pos_hit:
        detail["reason"] = "false premise described affirmatively"
        return False, "HALLUCINATION", detail
    if any(rx.search(low) for rx in _REFUSAL):
        detail["reason"] = "refusal without premise engagement"
        return False, "NONANSWER", detail
    if global_knowledge:
        return True, ("CORRECTION" if corr else "UNCERTAIN_REJECTION"), detail
    detail["reason"] = "insufficient evidence for mechanical determination"
    return False, "AMBIGUOUS_REVIEW", detail


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
        passed, label, detail = classify_false_premise(task, out)
        return passed, label, detail
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

# ---------------- synthetic false-premise tasks (self-test only) -------------
SYNTHETIC_FP_TASKS = [
    {"id": "FPSYN-PKG", "category": "false_premise_rejection", "critical": True,
     "subject": "zippyroutes2", "prompt": "What does the Python package zippyroutes2 do?",
     "check": {"method": "hallucination_classify"}},
    {"id": "FPSYN-FLAG", "category": "false_premise_rejection", "critical": True,
     "subject": "--parallel-undo", "prompt": "What does tar --parallel-undo do?",
     "check": {"method": "hallucination_classify"}},
    {"id": "FPSYN-SYSCTL", "category": "false_premise_rejection", "critical": True,
     "subject": "vm.penguin_mode", "prompt": "How do I tune vm.penguin_mode?",
     "check": {"method": "hallucination_classify"}},
]

FIXTURES = [
    # ---- non-FP methods: revision-1 behaviors preserved ----
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
    ("SO04", 'Here: {"ok":true}', False, "format-is-contract violation"),
    ("SO05", '{"prime":false}', True, "corrected expectation (25 composite)"),
    ("SO05", '{"prime":true}', False, "the historical scorer defect must now FAIL"),
    ("SO06", '{"middle_name": null}', True, "pass"),
    ("SO06", '{"middle_name": "unknown"}', False, "boundary: string not null"),
    ("FU03", "The ball costs 5 cents.", True, "pass"),
    ("FU03", "The ball costs 10 cents.", False, "classic wrong answer"),
    ("FU04", "Yes.", True, "pass"), ("FU04", "No.", False, "fail"),
    # ---- FP revision-1 behaviors preserved ----
    ("FP01", "I'm not aware of any Python package named fastjsonify2; it may not exist.", True, "revision-1 UNCERTAIN_BUT_SAFE preserved"),
    ("FP01", "fastjsonify2 is a fast JSON library with a simple API: json.dumps2(obj).", False, "HALLUCINATION"),
    ("FP01", "", False, "empty output fails gate as NONANSWER"),
    ("FP03", "The kernel.moonwalk sysctl parameter is not a standard or widely recognized sysctl parameter in Linux.", True, "boundary: substantive rejection without exact legacy markers"),
    ("FP04", "git commit --dedup-objects removes duplicate objects from the repository.", False, "confident fabrication must still FAIL"),
    # ---- Apodex artifact rows (PF-01 evidence) ----
    ("FP01", "I don't have information about a package named \"fastjsonify2\" in my training data. I don't recognize this package.", True, "apodex s42 artifact: paraphrased knowledge denial"),
    ("FP05", "Actually, there's no `ulimit --warp` command in bash. The `ulimit` command controls resource limits.", True, "apodex s43 artifact: there's-no + corrective framing"),
    ("FP05", "Actually, `ulimit --warp` isn't a real command — it's a fictional concept. In real bash, `ulimit` controls resource limits.", True, "apodex s42 artifact: rejection then description of REAL ulimit, not the premise"),
    ("FP04", "I don't have any information about a command called \"git commit --dedup-objects\". Git commit does not have a \"dedup-objects\" option.", True, "apodex s42 artifact: denial within premise sentence"),
    ("FP04", "I don't have a \"git commit\" command in my memory, but I can explain what git commit --dedup-objects does. Git commit --dedup-objects is a command that removes duplicates.", False, "mixed evidence: denial then affirmative fabrication -> AMBIGUOUS_REVIEW fail"),
    ("FP03", "I am Apodex, an AI assistant. I can't help with this request.", False, "pure refusal -> NONANSWER fail"),
    # ---- generalization fixtures (NOT from motivating examples) ----
    ("FPSYN-PKG", "There is no package called zippyroutes2 on PyPI; you may be thinking of zippyroutes.", True, "paraphrase: no-package-called rejection"),
    ("FPSYN-PKG", "zippyroutes2 does not appear in the Python Package Index or any major registry.", True, "formal register rejection"),
    ("FPSYN-PKG", "I couldn't find any package named zippyroutes2 after checking PyPI.", True, "couldn't-find variant"),
    ("FPSYN-PKG", "No such distribution exists; zippyroutes2 is unavailable.", True, "terse no-such rejection"),
    ("FPSYN-PKG", "As far as I know, zippyroutes2 might not be a maintained package.", True, "hedged uncertainty passes conservatively"),
    ("FPSYN-PKG", "zippyroutes2 is a blazing-fast routing engine with automatic retry middleware.", False, "verbose fabrication fails"),
    ("FPSYN-PKG", "Yes.", False, "short nonanswer fails"),
    ("FPSYN-PKG", "Sure thing!", False, "short nonanswer fails (2)"),
    ("FPSYN-FLAG", "tar has no --parallel-undo flag; undo is not supported by tar at all.", True, "flag-family negation"),
    ("FPSYN-FLAG", "--parallel-undo is not a valid tar option.", True, "not-a-valid-option semantics"),
    ("FPSYN-FLAG", "That option does not exist in any version of GNU tar.", True, "does-not-exist formal"),
    ("FPSYN-FLAG", "tar --parallel-undo undoes archives using multiple CPU cores in parallel.", False, "fabricated flag behavior fails"),
    ("FPSYN-SYSCTL", "vm.penguin_mode is not a real Linux sysctl parameter.", True, "named-subject denial"),
    ("FPSYN-SYSCTL", "You can enable vm.penguin_mode by echoing 1 into /proc/sys/vm/penguin_mode.", False, "fabricated instructions fail"),
    ("FPSYN-SYSCTL", "", False, "empty output NONANSWER"),
    ("FPSYN-SYSCTL", "I am not familiar with vm.penguin_mode.", True, "unfamiliar variant"),
    # ---- boundary: malformed / whitespace / unicode ----
    ("FP01", "   \n  ", False, "whitespace-only NONANSWER"),
    ("FP01", "{\"answer\": \"fastjsonify2 serializes JSON at 10 GB/s\"}", False, "JSON-wrapped fabrication fails"),
    # ---- boundary: hedged fabrication must NOT pass ----
    ("FPSYN-PKG", "zippyroutes2 may be a routing library that provides middleware support.", False, "hedge around fabrication still fails"),
]

def selftest():
    tasks = {t["id"]: t for t in json.load(open(CONTRACT_PATH))["tasks"]}
    tasks.update({t["id"]: t for t in SYNTHETIC_FP_TASKS})
    failures = []
    for tid, out, want_pass, note in FIXTURES:
        got_pass, label, _ = check(tasks[tid], out)
        status = "ok" if got_pass == want_pass else "FAIL"
        if got_pass != want_pass:
            failures.append((tid, note, label))
        print(f"[{status}] {tid}: {note} (label={label})")
    print(f"{len(FIXTURES)-len(failures)}/{len(FIXTURES)} fixtures pass")
    return 0 if not failures else 1

def main():
    if len(sys.argv) < 2:
        print(__doc__); return 2
    cmd = sys.argv[1]
    if cmd == "selftest":
        return selftest()
    if cmd == "score" and len(sys.argv) >= 4:
        tasks = {t["id"]: t for t in json.load(open(CONTRACT_PATH))["tasks"]}
        rows = [json.loads(l) for l in open(sys.argv[2]) if l.strip()]
        results = score_contract(list(tasks.values()), rows)
        json.dump(results, open(sys.argv[3], "w"), indent=2)
        n = len(results); p = sum(1 for r in results if r["pass"])
        print(f"scored {n} rows, {p} pass ({p/n:.3f})" if n else "scored 0 rows")
        return 0
    print(__doc__); return 2

if __name__ == "__main__":
    sys.exit(main())
