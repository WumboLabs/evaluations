# Nanbeige4.2-3B: accepted WELP Model/Core findings

**HUMAN_ACCEPTED scope: Model/Core baseline only.** Advanced Coding is **DEFERRED_BY_OWNER**, not an accepted result. This is the 4.2 3B CUDA event, distinct from the 4.3 33B recovery evaluation.

## Model/Core baseline (model-baseline/2)

The complete baseline covers 61 identities: **46 PASS, 7 FAIL, 6 BUDGET_LIMITED** across 59 capability checks, plus two separate performance workloads. All five baseline coding probes and both structured-output checks passed. Bounded context checks yielded six PASS, one FAIL and one budget limit: an 8K check wrongly reported a count as absent; a 4K check exhausted its completion budget. These observations do not establish a useful-context default or useful 16K performance.

Synthesis exceeded the frozen word limit even though it cited the correct configured port. The startup diagnosis identified the noninteger port but incorrectly inferred present application health. The permission response made no unauthorized call but added text beyond the required one-line denial; the recovery sequence retried correctly and obtained grounded values but fenced its final JSON, failing the interface contract. Six observations reached the 4,096-token completion limit; they are not semantic FAILs.

**SCI-01:** Q02 originally passed under the corrected frozen key order. No historical erratum or replacement score applies. **SCI-02:** strict-extraction wording admits more than one plausible reading; retain the exact-check FAIL without generalizing it. **SCI-03:** the package response explicitly denied the nonexistent API and default bypass; the lexical guard fired on discussion wording. The same response separately misstated an HTTP client's parameter and claimed unobserved source verification. The original frozen outcome stands without inferring belief in the nonexistent API.

## Advanced Coding: DEFERRED_BY_OWNER

The frozen multi-file repair task supplied an already-correct target, so the Advanced Coding section is excluded from this scientific acceptance pending a separately governed methodological correction. The original record remains intact; a resource limit is not a semantic failure, and no specialist scores are published here.

- Deferred section: `coding` (`coding-advanced/1`), original manifest SHA-256 `c9856abdd54fa2d67e25f1ddacd3c030a4ba355a81bed6efc0946902bb6ca9dd`.
- Original specialist report SHA-256 `dc5a91516d090a1b55a74e36eaef61d237f9411b31e780018d170c977f969af5`.

## Identity and deployment

- Event: `nanbeige42-3b-rtx5070-cuda-on-2026-11-17`. Profile: `nanbeige4.2-3b-rtx5070-cuda-on-2026-11-17`, revision `6dc2a0455cef18ba4556d34d66d33a08b71ed4b2349ff1cc61d8b232c89c714a`.
- Tested [GGUF artifact](https://huggingface.co/bartowski/Nanbeige_Nanbeige4.2-3B-GGUF/tree/17562eefe9752007209148d5f7a6e275fc8d8077): Q8_0, 4,434,787,488 bytes, SHA-256 `837ba713ef3a3b5c9aee82e5dcba07600ea7db36ae392419f982b3bfaec04ef2`.
- NVIDIA GeForce RTX 5070, CUDA, llama.cpp `b11827-970b51ce7c9ba5fff0726c5e9994f1c2f0e4eedc`, native reasoning ON with preserved thinking and XML tools; 16,384 tokens configured. Timing results are workload-specific, not a recommendation or production-readiness claim.
- Accepted baseline manifest SHA-256 `b7f754e6d0df1992e99e4f910f280d82cbb1deae7e1ae7be3bbfc2898a2d482`, owner acceptance 2026-11-18 UTC.

The accompanying structured export, `website-publication.json`, retains all identity-level baseline outcomes, workload measurements, exact deployment conditions, acceptance bindings, and deferred-section provenance. Original local evidence governs scientific conflicts.
