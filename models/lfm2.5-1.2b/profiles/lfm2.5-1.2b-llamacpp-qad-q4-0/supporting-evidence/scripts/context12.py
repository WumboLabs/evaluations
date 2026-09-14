#!/usr/bin/env python3
"""Phase 10 context ladder: 4K/8K/16K/32K (card limit 32768).
Per rung: beginning/middle/end needle retrieval, trailing exact-format instruction,
absent-evidence probe. Finalists: QAD, PTQ, Q4_K_M, UD_Q4_K_XL. Mechanical scoring.
"""
from pathlib import Path
import json, sys
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

RUNGS = [4096, 8192, 16384, 32768]
MODELS = ['QAD_Q4_0', 'PTQ_Q4_0', 'Q4_K_M', 'UD_Q4_K_XL']
FILL = 'neutral filler statement about ordinary office supplies. '


def build(rung):
    # filler words -> tokens at roughly 1.35 tok/word; keep prompt <= rung-320
    target_words = int((rung - 320) / 1.35)
    n = len(FILL.split())
    reps = max(target_words // n, 1)
    seg = max(reps // 10, 1)
    a, b, c = f'CODE-ALPHA-{rung}', f'CODE-BRAVO-{rung}', f'CODE-CHARLIE-{rung}'
    text = ('Read carefully. Somewhere in this document three storage codes are hidden. '
            'At the very end of your reply output exactly the three codes in the order they appear, '
            'comma-separated, nothing else after them. '
            + FILL * seg + f' The storage code is {a}. '
            + FILL * (seg * 4) + f' The storage code is {b}. '
            + FILL * (seg * 4) + f' The storage code is {c}. ' + FILL * seg)
    absent_q = (f'\n\nSeparately: what is the value of storage code CODE-DELTA-{rung}? '
                'Reply exactly ABSENT if it never appears.')
    return text, [a, b, c], absent_q


def main():
    out = {}
    for mid in MODELS:
        out[mid] = {}
        with Server(mid, CTX_MAX_CARD, 8092) as s:
            for rung in RUNGS:
                text, codes, absent_q = build(rung)
                row = {'requested_rung': rung}
                try:
                    r = call(s, text, 256, seed=42)
                    ans = content(r)
                    flat = ' '.join(ans.split())
                    t = timing(r); u = r.get('usage', {})
                    row.update({
                        'actual_prompt_tokens': u.get('prompt_tokens'),
                        'answer_tail': ans[-200:],
                        'beginning_ok': codes[0] in ans,
                        'middle_ok': codes[1] in ans,
                        'end_ok': codes[2] in ans,
                        'all_three_in_order': all(c in ans for c in codes) and flat.find(codes[0]) < flat.find(codes[1]) < flat.find(codes[2]),
                        'prompt_tok_s': t.get('prompt_per_second'),
                        'generation_tok_s': t.get('predicted_per_second')})
                except Exception as ex:
                    row['error'] = str(ex)
                try:
                    r2 = call(s, absent_q, 60, seed=42)
                    row['absent_answer'] = content(r2)[:120]
                    row['absent_ok'] = 'ABSENT' in content(r2)
                except Exception as ex:
                    row['absent_error'] = str(ex)
                out[mid][str(rung)] = row
                print(mid, rung, row.get('actual_prompt_tokens'), row.get('beginning_ok'),
                      row.get('middle_ok'), row.get('end_ok'), row.get('absent_ok'), flush=True)
    save('context.json', {'method': 'per-rung three-needle retrieval (begin/middle/end), trailing exact-format instruction, absent-evidence probe; card limit 32768; official sampler',
                          'results': out})


if __name__ == '__main__':
    main()
