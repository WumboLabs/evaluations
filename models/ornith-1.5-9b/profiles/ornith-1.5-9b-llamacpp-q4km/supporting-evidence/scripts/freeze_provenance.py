#!/usr/bin/env python3
"""Phase 0 provenance freeze for WELP campaign ornith-1.5-9b.
Computes every hash/line-count live; writes sources/ + summaries/ identity records.
NOTE: special token literals are built via chr() to avoid serializer corruption."""
import json, hashlib, subprocess, datetime
from pathlib import Path

ROOT = Path("<USER_HOME>/Projects/local-llm")
CAMP = ROOT / "evals/ornith-1.5-9b"
ART = ROOT / "models/ornith-1.5-9b/artifacts"
WELP = ROOT / "welp"
now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def nlines(p): return sum(1 for _ in open(p, "rb"))
def tok(name): return "<|" + name + "|>"

GGUF = ART / "Ornith-1.5-9B-Q4_K_M.gguf"

# NOTE: canonical welp-practical-viability contract embeds all 30 task prompts
# inline (no external corpus files; run_module.py corpus-injection path is
# unused for this contract). No corpora to freeze.
TPL = ART / "chat_template.jinja"
MMPROJ = ART / "mmproj-Ornith-1.5-9B-BF16.gguf"

IM_END = tok("im_end")
THINK = tok("think")

# ---------- sources/provenance.json ----------
prov = {
  "recorded_utc": now,
  "note": "All values fetched live from official sources on 2026-08-27 during WELP campaign ornith-1.5-9b.",
  "primary_upstream": {
    "repo": "ornith-ai/Ornith-1.5-9B",
    "revision": "489cb97981b8654bcfcf30ce1f94ed1b62e07b53",
    "last_modified": "2026-08-23T06:24:01Z",
    "architecture": "Qwen3_5ForConditionalGeneration",
    "model_type": "qwen3_5",
    "license": "mit",
    "parameters": "9B dense (hidden 4096, 32 layers + 1 nextn/MTP layer, GQA 16q/4kv, head_dim 256, ffn 12288)",
    "max_position_embeddings": 262144,
    "vocab_size": 248320,
    "hybrid_attention": "linear (SSM: conv_kernel 4, state 128, group 16, inner 4096) x3 then full_attention, full_attention_interval=4",
    "mtp_num_hidden_layers": 1,
    "vision": {
      "status": "SUPPORTED_BY_SOURCE / NOT_EVALUATED",
      "evidence": "config.json vision_config present; HF tag image-text-to-text; official mmproj-Ornith-1.5-9B-BF16.gguf (921704672 B) downloaded; campaign objectives are TEXT+AGENTIC only"
    },
    "reasoning_mechanism": f"assistant turn begins with {THINK} ... {IM_END} reasoning span; thinking controlled via chat_template_kwargs enable_thinking (template default true)",
    "official_quantizations": "MXFP4_MOE, FP8, BF16, Q8_0, Q6_K, Q5_K_M, Q4_K_M, Q4_0 (8 GGUFs); Q4_K_M chosen per campaign objective (12 GB VRAM)",
    "companion_repos": {
      "ornith-ai/Ornith-1.5": "model card + blog (release 2026-08-23)",
      "ornith-ai/Ornith-1.5-GGUF": "unsloth-mirrored GGUFs, same files/size/commit date; NOT used (single-source rule)"
    }
  },
  "evaluated_artifact": {
    "file": str(GGUF), "bytes": GGUF.stat().st_size, "sha256": sha(GGUF),
    "quant": "Q4_K_M (general.file_type=15, quantization_version=2)",
    "gguf_metadata": {
      "general.architecture": "qwen35", "general.name": "Ornith-1.5-9B",
      "qwen35.context_length": 262144, "qwen35.block_count": 33,
      "qwen35.nextn_predict_layers": 1, "qwen35.attention.layer_norm_eps": 1e-6,
      "tokenizer.ggml.model": "gpt2", "tokenizer.ggml.pre": "qwen35",
      "tokenizer.ggml.eos_token_id": 248046, "tokenizer.ggml.padding_token_id": 248020,
      "tokenizer.ggml.utf8_incremental_decoding": True
    },
    "template_note": "embedded template == separate chat_template.jinja (sha256-identical); template renders enable_thinking default true; tool calls emitted as XML function tags inside content (no native tool_calls parsing by server)",
    "chat_template": {"file": str(TPL), "sha256": sha(TPL), "bytes": TPL.stat().st_size}
  },
  "excluded": {
    "mmproj": {"file": str(MMPROJ), "bytes": MMPROJ.stat().st_size, "sha256": sha(MMPROJ),
               "reason": "vision not evaluated (no vision objectives)"},
    "other_quants": {"reason": "single-artifact rule; Q4_K_M pinned by VRAM constraint"}
  },
  "benchmark_reference": {
    "status": "NOT_ADOPTED",
    "note": "Upstream blog claims (SWE-rebench 42.6, Terminal-Bench 2.1 50.0, DeepSWE 22.5, Terminal-Cyber 27.3, SciCode 42.5, Apex-TA 21.2, HLE-full 44.5, MCPMark 49.3, OpenAI ComputerUse 38.8) are producer claims; WELP Phase 10 classifies them against measured evidence only."
  }
}

# ---------- sources/snapshot_reference.json ----------
manifest = json.loads((WELP / "snapshot-freeze/manifest.json").read_text())
tree = subprocess.run(["git", "-C", str(WELP), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
dirty = subprocess.run(["git", "-C", str(WELP), "status", "--porcelain"], capture_output=True, text=True).stdout.strip()
snap = {
  "snapshot_id": manifest["snapshot_id"],
  "status": manifest["status"],
  "created_utc": manifest["created_utc"],
  "migration_type": manifest["migration_type"],
  "parent_snapshot": manifest["parent_snapshot"],
  "prior_snapshots": manifest["prior_snapshots"],
  "manifest_path": str(WELP / "snapshot-freeze/manifest.json"),
  "manifest_sha256": sha(WELP / "snapshot-freeze/manifest.json"),
  "welp_repo_head_at_freeze": tree,
  "welp_repo_dirty": bool(dirty),
  "file_count": int(subprocess.run(
      f"find {WELP} -type f -not -path '*/.git/*' -not -path '*__pycache__*' | wc -l",
      shell=True, capture_output=True, text=True).stdout.strip()),
  "tree_sha256": subprocess.run(
      f"find {WELP} -type f -not -path '*/.git/*' -not -path '*__pycache__*' -print0 | sort -z | xargs -0 cat | sha256sum",
      shell=True, capture_output=True, text=True).stdout.split()[0],
  "binding_note": "Campaign bound to this exact WELP protocol tree. Any protocol file change invalidates the binding and requires a new snapshot id."
}

# ---------- sources/dataset_inventory.json ----------
inv = {
  "recorded_utc": now,
  "policy": "All contract/task/scorer artifacts hash-pinned from the frozen WELP tree before use. No silent upstream updates.",
  "datasets": {
    "welp-practical-viability": {
      "path": str(WELP / "contracts/welp-practical-viability-0.1.3-draft.json"),
      "sha256": sha(WELP / "contracts/welp-practical-viability-0.1.3-draft.json"),
      "version_note": "filename 0.1.3-draft; internal version field 0.1.4-draft (canonical, matches welp-modules.json index)",
      "tasks": 30, "seeds": [42, 43, 44], "runs": 90,
      "corpora": "NONE — all task prompts inline in contract"
    },
    "welp-reliability": {
      "contract": str(WELP / "contracts/welp-reliability-0.1.0-draft.json"),
      "contract_sha256": sha(WELP / "contracts/welp-reliability-0.1.0-draft.json"),
      "task_source": str(ROOT / "wlep-development/overnight-hardening-2026-08-25/reliability/contracts/wlep-reliability-0.1.0-draft.json"),
      "task_source_sha256": sha(ROOT / "wlep-development/overnight-hardening-2026-08-25/reliability/contracts/wlep-reliability-0.1.0-draft.json"),
      "note": "welp contract is naming-only migration; 54 tasks x 7 domains unchanged; frozen_path per contract supersedes block",
      "tasks": 54, "seeds": [42, 43, 44], "runs": 162
    },
    "phase5-modules": {
      "index": str(WELP / "contracts/welp-modules.json"),
      "index_sha256": sha(WELP / "contracts/welp-modules.json"),
      "dev_tree": str(ROOT / "wlep-development/overnight-hardening-2026-08-25/capability-modules"),
      "modules_present": ["coding", "extraction-rag", "native-tools", "reasoning"],
      "status": "PENDING — Phase 5 applicability freeze selects modules + pins task/scorer hashes at that phase"
    }
  }
}

# ---------- summaries/toolchain_inventory.json ----------
def ver(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()

toolchain = {
  "schema": "welp-toolchain-inventory/0.1.0-draft",
  "generated_utc": now,
  "host": "wumbojetsii (Fedora Linux, kernel 7.1.10-200.fc44.x86_64, AMD Ryzen 7 9800X3D)",
  "gpu": "NVIDIA GeForce RTX 5070 (GB205, sm_120)",
  "driver": ver("nvidia-smi --query-gpu=driver_version --format=csv,noheader"),
  "cuda_toolkit": "CUDA 13.3 (/usr/local/cuda-13.3; llama-server built with GNU 15.3.1)",
  "policy": "LEAVE_IN_PLACE: runtime/toolchain sources are never modified by the campaign; only pinned commits + build dirs are referenced.",
  "tools": [
    {"tool": "llama.cpp", "purpose": "campaign serving runtime (llama-server)",
     "installed": True, "path": str(ROOT / "llama.cpp-sm120-upgrade"),
     "commit": "0d9ceae1e38291035605613ab41a8f5e693d6fcd",
     "version": "b10449-0d9ceae1e",
     "environment": {"build_dir": str(ROOT / "llama.cpp-sm120-upgrade/build-cuda-sm120-new"),
                     "binary": str(ROOT / "llama.cpp-sm120-upgrade/build-cuda-sm120-new/bin/llama-server"),
                     "binary_sha256": sha(ROOT / "llama.cpp-sm120-upgrade/build-cuda-sm120-new/bin/llama-server"),
                     "cmake": {"CMAKE_CUDA_ARCHITECTURES": "120", "GGML_CUDA": "ON"},
                     "built_with": "GNU 15.3.1, CUDA 13.3"},
     "compatible_status": "COMPATIBLE_ADMISSION_VERIFIED",
     "preferred": True,
     "notes": "admission: qwen35 arch loads, 33 layers -ngl 99, reasoning extraction + native tool_calls probes PASS; commit date 2026-08-15T20:00:18+02:00"},
    {"tool": "llama.cpp (stale trees)", "purpose": "documented exclusions",
     "installed": True, "path": str(ROOT / "llama.cpp"),
     "commit": "74ade52741203e5c8f81eaf06a96cb1cfe15f2a3",
     "compatible_status": "NOT_USED",
     "preferred": False,
     "notes": "single-runtime rule; llama.cpp-current also at 0d9ceae1e but not the campaign build dir"},
    {"tool": "python", "purpose": "runner + validators",
     "installed": True, "path": "/usr/bin/python3",
     "version": ver("python3 --version"),
     "compatible_status": "COMPATIBLE", "preferred": True,
     "notes": "jsonschema installed"},
    {"tool": "localmaxxing-cli", "purpose": "Phase 11 external publication",
     "installed": True, "path": "/usr/local/sbin/lmx",
     "version": "v0.1.33", "commit": "4a36be4871d0bf26960b2868e18771269df4dc8e",
     "environment": "system binary; saved CLI-native auth config",
     "compatible_status": "COMPATIBLE", "preferred": True,
     "notes": "lmx auth status PASS 2026-08-27 (provider: manual); no key material recorded in any campaign artifact"}
  ]
}

# ---------- summaries/environment_identity.json ----------
env = {
  "recorded_utc": now,
  "host": "wumbojetsii",
  "os": "Fedora Linux (kernel 7.1.10-200.fc44.x86_64, SMP PREEMPT_DYNAMIC Sun Aug 23 2026)",
  "cpu": "AMD Ryzen 7 9800X3D 8-Core",
  "gpu": ver("nvidia-smi --query-gpu=name,memory.total --format=csv,noheader"),
  "driver": toolchain["driver"],
  "cuda": toolchain["cuda_toolkit"],
  "python": ver("python3 --version"),
  "vram_policy": "single-model resident; no co-tenant GPUs during campaign runs",
  "profile_ref": str(CAMP / "hardware/wumbojetsii/profile.json") if (ROOT / "hardware/wumbojetsii/profile.json").exists() else str(ROOT / "hardware/wumbojetsii/profile.json"),
  "profile_sha256": sha(ROOT / "hardware/wumbojetsii/profile.json")
}

out = CAMP / "sources"; out.mkdir(exist_ok=True)
(CAMP / "summaries").mkdir(exist_ok=True)
(CAMP / "results").mkdir(exist_ok=True)
(CAMP / "toolchain").mkdir(exist_ok=True)

(out / "provenance.json").write_text(json.dumps(prov, indent=2) + "\n")
(out / "snapshot_reference.json").write_text(json.dumps(snap, indent=2) + "\n")
(out / "dataset_inventory.json").write_text(json.dumps(inv, indent=2) + "\n")
(CAMP / "summaries/toolchain_inventory.json").write_text(json.dumps(toolchain, indent=2) + "\n")
(CAMP / "summaries/environment_identity.json").write_text(json.dumps(env, indent=2) + "\n")

# ---------- protocol-snapshot/ copy ----------
import shutil
ps = CAMP / "protocol-snapshot"
if ps.exists(): shutil.rmtree(ps)
shutil.copytree(WELP, ps, ignore=shutil.ignore_patterns(".git", "__pycache__"))
copy_tree = subprocess.run(
    f"find {ps} -type f -print0 | sort -z | xargs -0 cat | sha256sum",
    shell=True, capture_output=True, text=True).stdout.split()[0]
assert copy_tree == snap["tree_sha256"], f"snapshot copy mismatch {copy_tree} != {snap['tree_sha256']}"
(ps / "SNAPSHOT-COPY-NOTE.md").write_text(
    "Campaign-local copy of welp/ frozen at " + now + "\n"
    "snapshot_id: " + snap["snapshot_id"] + "\n"
    "tree_sha256: " + snap["tree_sha256"] + "\n"
    "This copy is reference-only; the authoritative tree is <USER_HOME>/Projects/local-llm/welp.\n")

print("frozen:")
for f in ["sources/provenance.json", "sources/snapshot_reference.json", "sources/dataset_inventory.json",
          "summaries/toolchain_inventory.json", "summaries/environment_identity.json"]:
    print(" ", f, sha(CAMP / f)[:16])
print("snapshot tree sha256:", snap["tree_sha256"])
print("copy verified: OK")
