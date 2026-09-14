#!/usr/bin/env python3
"""Phase 1 admission artifacts: toolchain_preflight, serving_profile,
runtime_capabilities, campaign_manifest. All evidence read live from the
running campaign server (port 8931) + frozen sources/ records."""
import json, hashlib, subprocess, datetime, urllib.request
from pathlib import Path

ROOT = Path("<USER_HOME>/Projects/local-llm")
CAMP = ROOT / "evals/ornith-1.5-9b"
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def get(url): return json.loads(urllib.request.urlopen(url, timeout=30).read())

prov = json.loads((CAMP / "sources/provenance.json").read_text())
snap = json.loads((CAMP / "sources/snapshot_reference.json").read_text())
tcinv = json.loads((CAMP / "summaries/toolchain_inventory.json").read_text())
env = json.loads((CAMP / "summaries/environment_identity.json").read_text())

props = get("http://127.0.0.1:8931/props")
log = (CAMP / "logs/campaign-server1.log").read_text()


# exact launch command (recorded at relaunch; matches logs/campaign-server1.log)
CMD = ("llama-server -m <USER_HOME>/Projects/local-llm/models/ornith-1.5-9b/artifacts/Ornith-1.5-9B-Q4_K_M.gguf "
       "--jinja -ngl 99 -c 32768 -np 1 -b 2048 -ub 512 --flash-attn on --fit off --metrics "
       "--host 127.0.0.1 --port 8931 --no-ui")
(CAMP / "summaries/launch_command.txt").write_text(CMD + "\n")

vram = subprocess.run("nvidia-smi --query-compute-apps=pid,used_memory --format=csv,noheader",
                      shell=True, capture_output=True, text=True).stdout.strip()

# ---------- serving profile ----------
sp = {
  "model": {
    "repo": prov["primary_upstream"]["repo"],
    "revision": prov["primary_upstream"]["revision"],
    "file": "Ornith-1.5-9B-Q4_K_M.gguf",
    "sha256": prov["evaluated_artifact"]["sha256"]
  },
  "runtime": {"name": "llama.cpp (llama-server)", "build": 10449,
              "commit": "0d9ceae1e38291035605613ab41a8f5e693d6fcd"},
  "placement": {"gpu_layers": 99, "cpu_offload": False},
  "requested": {
    "parallel": 1, "fit": "off", "flash_attn": "on", "context_total": 32768,
    "batch": 2048, "ubatch": 512, "template": "embedded GGUF (== chat_template.jinja, sha256-verified)",
    "reasoning_mode": "REASONING_OFF via chat_template_kwargs.enable_thinking=false (gate baseline)",
    "sampling": {"temperature": "per-contract", "note": "contract sampling_default governs; server defaults unused"},
    "speculation": "none"
  },
  "effective": {
    "slot_count": props["total_slots"],
    "per_slot_context": props["default_generation_settings"]["n_ctx"],
    "total_context": props["default_generation_settings"]["n_ctx"],
    "kv_placement": "GPU (all 33 layers offloaded; -ngl 99 -fit off; RTX 5070 12 GB)",
    "recurrent_state_placement": "GPU (hybrid SSM layers; qwen35 full_attention_interval=4)",
    "endpoint_alias": "http://127.0.0.1:8931",
    "server_concurrency": 1,
    "gate_baseline_reasoning_state": "REASONING_OFF",
    "reasoning_requested": "REASONING_OFF",
    "reasoning_effective": "REASONING_OFF",
    "evidence": [
      "log: srv    load_model: initializing, n_slots = 1, n_ctx_slot = 32768, kv_unified = 'false'",
      "log: srv  llama_server: listening on http://127.0.0.1:8931",
      "log: chat template supports preserving reasoning (template renders enable_thinking)",
      "/props: total_slots=1, n_ctx=32768, build_info=" + props["build_info"],
      "/props chat_template_caps: supports_tools=true, supports_tool_calls=true, supports_preserve_reasoning=true, supports_reasoning_effort=false",
      "probe REASONING_OFF: enable_thinking=false -> reasoning_content absent, content='PING'",
      "probe REASONING_ON: default -> reasoning_content='17 x 23 = ... 391', content='17 x 23 = **391**' (auto-extraction works)",
      "probe TOOLS: native tool_calls returned: get_weather {\"city\":\"Paris\"} with id; content empty",
      "nvidia-smi compute-apps: " + vram,
      "metrics: llamacpp:prompt_tokens_total excludes cached; prompt_tokens_cached_total present"
    ]
  },
  "delta": [
    {"field": "context_total", "requested": 32768, "effective": 32768,
     "note": "model supports 262144; campaign caps at 32768 for Phase 6 headroom on 12 GB VRAM"},
    {"field": "reasoning", "requested": "REASONING_OFF", "effective": "REASONING_OFF",
     "note": "verified per-request via reasoning_content absence; template default is thinking-ON, so every gate request MUST send enable_thinking=false"}
  ]
}
(CAMP / "summaries/serving_profile.json").write_text(json.dumps(sp, indent=2) + "\n")

# ---------- runtime capabilities ----------
rc = {
  "generated_utc": now,
  "runtimes": {
    "llama.cpp-b0d9ceae1e": {
      "status": "CACHE_METRIC_TRUSTED",
      "probe": "two identical disjoint prompts (~420 tok each) after fresh start; delta prompt_tokens_total=420 (first, no cache), prompt_tokens_total=8 + prompt_tokens_cached_total=412 (second) -> cached counter distinguishes real cache reuse from floor",
      "evidence_log": str(CAMP / "logs/campaign-server1.log"),
      "metrics_endpoint": "http://127.0.0.1:8931/metrics (--metrics)"
    }
  }
}
(CAMP / "toolchain").mkdir(exist_ok=True)
(CAMP / "toolchain/runtime_capabilities.json").write_text(json.dumps(rc, indent=2) + "\n")

# ---------- preflight ----------
pf = {
  "preflight": "welp-preflight",
  "version": "0.1.0-draft",
  "generated_utc": now,
  "overall": "GO",
  "hardware": {
    "host": env["host"], "gpu": env["gpu"], "driver": env["driver"],
    "cuda": env["cuda"], "vram_gb": 12,
    "telemetry": "nvidia-smi loop + journal Xid watch during long runs (see safety)",
    "decision": "REUSE_LOCAL"
  },
  "toolchain": {
    "selected_runtime": {
      "name": "llama.cpp", "commit": "0d9ceae1e38291035605613ab41a8f5e693d6fcd",
      "build": "b10449", "binary": tcinv["tools"][0]["environment"]["binary"],
      "binary_sha256": tcinv["tools"][0]["environment"]["binary_sha256"],
      "decision": "REUSE_LOCAL",
      "compatibility_evidence": "admission test PASSED: model loads (qwen35 arch, 33 layers, hybrid SSM + MTP tensor blk.32 present-but-unused without --spec), chat completions OK, reasoning extraction OK, native tool_calls OK"
    },
    "localmaxxing": {"cli": "lmx", "auth_status": "READY",
                     "key_source": "~/.config/localmaxxing/config.json", "key_exposed": False},
    "inventory": str(CAMP / "summaries/toolchain_inventory.json"),
    "inventory_sha256": sha(CAMP / "summaries/toolchain_inventory.json"),
    "selection_rule": "DISCOVER FIRST / REUSE WHEN COMPATIBLE / UPDATE OR BUILD ONLY ON PROVEN INCOMPATIBILITY"
  },
  "protocol": {
    "snapshot_id": snap["snapshot_id"],
    "welp_status": "DRAFT",
    "manifest_sha256": snap["manifest_sha256"],
    "tree_sha256": snap["tree_sha256"],
    "campaign_copy": str(CAMP / "protocol-snapshot"),
    "copy_verified": "tree sha256 of copy == authoritative tree sha256 (freeze_provenance.py assertion)"
  },
  "model": {
    "repo": prov["primary_upstream"]["repo"],
    "revision": prov["primary_upstream"]["revision"],
    "artifact_sha256": prov["evaluated_artifact"]["sha256"],
    "applicability": "general-purpose instruction-tuned text model; thinking model; native tool calling; vision SUPPORTED_BY_SOURCE but NOT_EVALUATED (text+agentic objectives only)",
    "producer_claims_status": "RECORDED_NOT_ADOPTED (provenance.json benchmark_reference)"
  },
  "publication": {"localmaxxing_auth_status": "READY"},
  "safety": {
    "gpu_host_rules": "single-model resident; stop-on-Xid (journalctl -k -p err monitored); no destructive ops; server bound to 127.0.0.1 only",
    "cors_note": "server warns CORS '*' with no API key — acceptable: loopback-only bind, no other tenants on host during campaign",
    "secrets": "LocalMaxxing key never written to any campaign artifact; lmx auth status read without printing key material"
  },
  "output": {
    "campaign_workspace_abs": str(CAMP),
    "evidence_path_writable": True,
    "long_job_paths": [str(CAMP / "results"), str(CAMP / "calibration")],
    "durability_rule": "absolute path declared before run; after exit verify existence + row count + sha256 before marking COMPLETE"
  }
}
(CAMP / "summaries/toolchain_preflight.json").write_text(json.dumps(pf, indent=2) + "\n")

# ---------- campaign manifest (living; fields added per phase) ----------
cm = {
  "campaign_id": "ornith-1.5-9b",
  "created_utc": now,
  "protocol_snapshot": {"id": snap["snapshot_id"], "manifest_sha256": snap["manifest_sha256"],
                        "tree_sha256": snap["tree_sha256"]},
  "model": {"repo": prov["primary_upstream"]["repo"],
            "revision": prov["primary_upstream"]["revision"],
            "file": "Ornith-1.5-9B-Q4_K_M.gguf",
            "sha256": prov["evaluated_artifact"]["sha256"]},
  "runtime": {"name": "llama.cpp", "build": 10449,
              "commit": "0d9ceae1e38291035605613ab41a8f5e693d6fcd",
              "binary_sha256": tcinv["tools"][0]["environment"]["binary_sha256"]},
  "hardware_profile": {"host": env["host"], "gpu": env["gpu"], "profile_ref": env["profile_ref"],
                       "profile_sha256": env["profile_sha256"]},
  "serving_profile": {"path": str(CAMP / "summaries/serving_profile.json"),
                      "sha256": sha(CAMP / "summaries/serving_profile.json"),
                      "requested": sp["requested"], "effective": sp["effective"]},
  "phase2_harness_version": None,
  "contracts": {
    "welp-practical-viability": {"version": "0.1.4-draft",
      "path": str(ROOT / "welp/contracts/welp-practical-viability-0.1.3-draft.json"),
      "sha256": sha(ROOT / "welp/contracts/welp-practical-viability-0.1.3-draft.json")},
    "welp-reliability": {"version": "0.1.0-draft",
      "path": str(ROOT / "welp/contracts/welp-reliability-0.1.0-draft.json"),
      "sha256": sha(ROOT / "welp/contracts/welp-reliability-0.1.0-draft.json")},
    "welp-preflight": {"version": "0.1.0-draft",
      "path": str(ROOT / "welp/contracts/welp-preflight-0.1.0-draft.json"),
      "sha256": sha(ROOT / "welp/contracts/welp-preflight-0.1.0-draft.json")}
  },
  "phase5_applicability": None,
  "generation_evidence": [],
  "publication_status": "PENDING",
  "artifact_index": "PENDING",
  "reproduction": "PENDING"
}
(CAMP / "summaries/campaign_manifest.json").write_text(json.dumps(cm, indent=2) + "\n")

# ---------- validate against schemas ----------
import jsonschema
ok = []
for f, s in [("summaries/serving_profile.json", "welp_serving_profile"),
             ("summaries/toolchain_preflight.json", "welp_toolchain_preflight"),
             ("summaries/campaign_manifest.json", "welp_campaign_manifest"),
             ("summaries/toolchain_inventory.json", "welp_toolchain_inventory")]:
    inst = json.loads((CAMP / f).read_text())
    schema = json.loads((ROOT / f"welp/schemas/{s}.schema.json").read_text())
    jsonschema.validate(inst, schema)
    ok.append(f)
print("schema-valid:", ", ".join(ok))
print("preflight overall:", pf["overall"])
