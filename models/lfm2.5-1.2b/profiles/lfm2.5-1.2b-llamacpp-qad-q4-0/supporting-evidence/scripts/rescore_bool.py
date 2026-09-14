#!/usr/bin/env python3
"""Re-score the corrected bool_field task (25 is not prime) across all candidates
and update practical_quality/structured_output summaries in place."""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

PROMPT = 'Is 25 prime? Return only {"prime":true} or {"prime":false}.'


def json_eq(exp):
    def f(x):
        import re as _re
        m = _re.search(r'\{.*\}', x, _re.S)
        if not m:
            return False
        try:
            return json.loads(m.group(0)) == exp
        except Exception:
            return False
    return f


chk = json_eq({'prime': False})
raw = json.loads((RESULTS / 'practical_raw.json').read_text())
for mid in PRIMARY:
    with Server(mid) as s:
        r = call(s, PROMPT, 60, seed=42)
        ans = content(r)
        raw[mid]['bool_field'] = {'answer': ans, 'pass': chk(ans)}
        print(mid, repr(ans), raw[mid]['bool_field']['pass'])
(RESULTS / 'practical_raw.json').write_text(json.dumps(raw, indent=2))

# re-aggregate from raw using suite task table
from suite import T, CHECKS
out = {}
for mid in PRIMARY:
    agg = {}
    for cat in CHECKS:
        ids = [t['id'] for t in T if t['category'] == cat]
        rows = [raw[mid][i] for i in ids]
        entry = {'tasks': len(ids), 'passes': sum(bool(r['pass']) for r in rows),
                 'rate': round(sum(bool(r['pass']) for r in rows) / len(rows), 4)}
        if CHECKS[cat] == 'label':
            from collections import Counter
            entry['labels'] = dict(Counter(r['label'] for r in rows))
        agg[cat] = entry
    out[mid] = agg
save('practical_quality.json', {
    'method': '52 unique tasks; mechanical scoring; official sampler temp .1/top-k 50/rp 1.05 seed 42; '
              'bool_field corrected after review (25 is composite); all other results unchanged',
    'per_model': out})
save('structured_output.json', {m: out[m]['structured'] for m in out})
print('RESCORE_DONE')
