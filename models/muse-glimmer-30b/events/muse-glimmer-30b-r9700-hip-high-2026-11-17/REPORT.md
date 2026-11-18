# Muse Glimmer 30B: accepted WELP scientific findings

**HUMAN_ACCEPTED scope: Model/Core baseline and Advanced Tool Use.** Both are independent results for this deployment. Neither establishes autonomous Agentic readiness or production readiness.

## Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **51 PASS, 4 FAIL, 4 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. All 15 instruction-following probes, all six reasoning probes, and all three basic-tool probes passed. The reviewed Git-safety response advised coordination but made substantive technical overclaims: a changed commit ID alone does not imply a non-fast-forward update, and the consequences for later fetch/pull were overstated.

Both 3K controlled context checks and both Multi-Document checks passed. All four Family A checks at 4K and 8K exhausted the 4,096-token completion budget with no visible answer. These are budget-limited findings, not incorrect answers; the pattern does not establish a monotonic context limit, a useful 16K default, or advertised maximum-context performance.

**SCI-01:** Q02 originally passed under the corrected frozen key order. No historical erratum or replacement score applies. **SCI-02:** the original strict-extraction FAIL reflects an exact check on ambiguous wording, not a general instruction-following finding. **SCI-03:** the Xid response referred to an old journal without attributing the event to the current run; its wording missed the frozen lexical requirement. The systemd response rejected the premise that active implies serving, but a conditional formulation triggered the frozen assertion guard. Both original FAILs are retained; neither is a semantic regrade.

## Advanced Tool Use (tool-use-advanced/1)

**3 PASS out of 3.** In the frozen simulator the native ATEM interface executed a multi-tool selection chain using returned identifiers; restricted diagnosis to the permitted read-only tools; and recovered from a tool deprecation using the observed feedback. These verify bounded tool execution in the simulator, not live operational access or general autonomous Agentic readiness.

## Identity and deployment

- Event: `muse-glimmer-30b-r9700-hip-high-2026-11-17`. Profile: `muse-glimmer-30b-r9700-hip-not-configurable-2026-11-17`, revision `3150011b557095fe496cb98af82c7b049c101074aee762fe47016506d037e927`.
- Tested [GGUF artifact](https://huggingface.co/meta-models/Muse-Glimmer-30B-GGUF/tree/b44f1072cf75e918a1b82a3a17b45c4389b076e7): text-only Q4_K_M, 16,756,683,904 bytes, SHA-256 `4cc57c0f51040a226e5a72cc47b7613f7772950e460a665f7083de89f183f60e`.
- AMD Radeon AI PRO R9700, HIP, llama.cpp `b11311-f7b384c1e5c5b2c5b321a4a7cefea04b15b54cb7` (flash attention off), native always-on ATEM high effort, no drafter or perception encoder, 16,384 tokens configured.
- Accepted baseline manifest SHA-256 `83c4f9908c63d0d3e45aad0f627ed7751af826ee307e79a81d1f8d59927788b1`; accepted Advanced Tool Use manifest SHA-256 `176b6ebc69dd492f7c0e4cf4eb0a7fd28686a18bdce603411befdaa6a3a7e004`, owner acceptance 2026-11-18 UTC.

The accompanying structured export, `website-publication.json`, retains all identity-level outcomes, workload measurements, exact deployment conditions, and acceptance bindings. Original local evidence governs scientific conflicts.
