#!/usr/bin/env python3
"""Variance lane: 5 representative tasks x 3 fixed seeds x all six candidates,
official sampler. Adapted from the 2.6B variance contract.
"""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

TESTS = {
    'instruction': ('Return exactly: VIOLET', lambda x: x.strip() == 'VIOLET'),
    'structured': ('Return only JSON {"x":2}', lambda x: x.strip() == '{"x":2}'),
    'hallucination': ('The undocumented command ghost-run is not known. Reply exactly NOT_AVAILABLE.',
                      lambda x: x.strip() == 'NOT_AVAILABLE'),
    'tool_like': ('Reply exactly TOOL_OK', lambda x: x.strip() == 'TOOL_OK'),
    'coding': ('Return only Python code block defining solve(a,b) that returns a+b.',
               lambda x: 'def solve' in x)}

if __name__ == '__main__':
    out = {}
    for mid in PRIMARY:
        out[mid] = {}
        with Server(mid) as s:
            for name, (p, sc) in TESTS.items():
                rows = []
                for seed in [11, 22, 33]:
                    r = call(s, p, 160, seed=seed)
                    a = content(r)
                    rows.append({'seed': seed, 'answer': a[:200], 'pass': sc(a)})
                out[mid][name] = {'runs': rows, 'pass_rate': sum(x['pass'] for x in rows) / 3,
                                  'unique_outputs': len(set(x['answer'] for x in rows))}
        print(mid, 'done', flush=True)
    save('variance.json', {'profile': PROFILE, 'seeds': [11, 22, 33], 'results': out})
