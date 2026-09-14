#!/usr/bin/env python3
"""Phase 1 admission + Phase 2 matched performance (5 measured reps + 1 warmup)."""
from pathlib import Path
import json, re, sys, time
sys.path.insert(0, str(Path(__file__).parent))
from lfm12b import *

PROMPT = 'Give a concise, technically accurate two-sentence explanation of why deterministic tests should avoid time-dependent assertions.'


def parse_load_info(mid):
    txt = (LOGS / f'{mid}-ctx4096.log').read_text(errors='replace')
    ngl = re.findall(r'offloaded (\d+)/(\d+) layers?', txt)
    model_mib = re.findall(r'model buffer size\s*=?\s*([0-9.]+)\s*(?:MiB|MB)', txt)
    kv_mib = re.findall(r'KV buffer size\s*=?\s*([0-9.]+)\s*(?:MiB|MB)', txt)
    compute_mib = re.findall(r'compute buffer size\s*=?\s*([0-9.]+)\s*(?:MiB|MB)', txt)
    return {'layers_offloaded': '/'.join(ngl[-1]) if ngl else None,
            'model_buffer_mib': float(model_mib[-1]) if model_mib else None,
            'kv_buffer_mib': float(kv_mib[-1]) if kv_mib else None,
            'compute_buffer_mib': float(compute_mib[-1]) if compute_mib else None}


def main():
    admissions = {}; perf = {}
    for mid in PRIMARY:
        with Server(mid) as s:
            peak = max(x['memory_used_mib'] for x in s.samples)
            minfree = min(x['memory_free_mib'] for x in s.samples)
            pw = [x['power_w'] for x in s.samples]; tc = [x['temperature_c'] for x in s.samples]
            smoke = call(s, PROMPT)
            admissions[mid] = {
                'file': FILES[mid], 'load_success': True, 'ready_s': round(s.ready_s, 2),
                'placement': 'GPU' if s.loaded_proc_mib else 'CHECK',
                'loaded_proc_vram_mib': s.loaded_proc_mib,
                'desktop_baseline_vram_mib': s.before['memory_used_mib'],
                'loaded_vram_mib': s.loaded['memory_used_mib'],
                'peak_vram_mib': peak, 'min_free_vram_mib': minfree,
                'peak_power_w': max(pw), 'peak_temp_c': max(tc),
                'smoke_output': content(smoke)[:400],
                **parse_load_info(mid)}
            vals = []
            # warmup excluded
            call(s, PROMPT, max_tokens=128)
            for rep in range(5):
                r = call(s, PROMPT, max_tokens=128, seed=100 + rep)
                t = timing(r)
                vals.append(t)
            perf[mid] = {
                'context': 4096, 'profile': PROFILE, 'warmup_excluded': True, 'reps': 5,
                'prompt_tok_s': stats([v.get('prompt_per_second', 0) for v in vals]),
                'generation_tok_s': stats([v.get('predicted_per_second', 0) for v in vals]),
                'ttft_ms': stats([v.get('prompt_ms', 0) for v in vals]),
                'completion_tokens': [v.get('predicted_n', 0) for v in vals],
                'power_and_temperature_samples': s.samples}
        print(f'{mid}: done', flush=True)
    save('admission.json', admissions)
    save('performance.json', perf)


if __name__ == '__main__':
    main()
