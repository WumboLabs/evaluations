#!/usr/bin/env python3
"""wlep-context deterministic corpus/prompt generator (DRAFT).
Deterministic filler from a seeded PRNG; needles at begin/middle/end;
absent-evidence probe; trailing instruction. No web access.
"""
import hashlib, json, random, sys

WORDS = ("harbor lantern meadow quartz ember thistle cobalt juniper slate marigold cinder willow "
         "granite zephyr amber tundra saffron basalt clover driftwood ridge falcon").split()

def build(rung_tokens: int, seed: int = 2026):
    rng = random.Random(f"{seed}:{rung_tokens}")
    needles = {"BEGIN": f"ORCHID-{rung_tokens}-B", "MIDDLE": f"ORCHID-{rung_tokens}-M", "END": f"ORCHID-{rung_tokens}-E"}
    # filler word budget: ~0.75 words/token
    n_words = int(rung_tokens * 0.72)
    third = n_words // 3
    def block(needle):
        return " ".join(rng.choice(WORDS) for _ in range(third)) + f"\nStorage code {needle}.\n"
    body = block(needles["BEGIN"]) + " ".join(rng.choice(WORDS) for _ in range(third)) + f"\nStorage code {needles['MIDDLE']}.\n" + \
           " ".join(rng.choice(WORDS) for _ in range(n_words - 2 * third)) + f"\nStorage code {needles['END']}.\n"
    absent_probe = "What is the storage code for section DELTA-NOPE?"
    prompt = (f"{body}\nAnswer the following in three short lines:\n"
              f"1) BEGIN storage code\n2) MIDDLE storage code\n3) END storage code\n4) {absent_probe}\n"
              "Use format 'B: <code>' / 'M: <code>' / 'E: <code>' / 'A: NOT_SPECIFIED'.")
    return {"prompt": prompt, "expected": {
        "B": needles["BEGIN"], "M": needles["MIDDLE"], "E": needles["END"], "A": "NOT_SPECIFIED"},
        "target_rung_tokens": rung_tokens, "seed": seed}

if __name__ == "__main__":
    d = build(int(sys.argv[1]), int(sys.argv[2]) if len(sys.argv) > 2 else 2026)
    print(json.dumps({"prompt_chars": len(d["prompt"]), "expected": d["expected"]}))
