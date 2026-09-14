### Identity and scope

- Profile: `gemma-4-12b-llamacpp-qat-q4-0` — llama.cpp official QAT Q4_0 (google GGUF, UD-Q4_K_XL packaging)
- Evidence maturity: **PRACTICAL_USE**
- Evidence scope: practical-use
- Hardware: WumboJetsII (RTX 5070 12GB)

Gemma 4 12B IT QAT UD-Q4_K_XL scored 259.2/300 (4.32 avg, 73.45 tok/s) vs UD-Q5_K_XL 254.0/300 (4.23); QAT Q4 selected as best overall practical variant. Shared report also tested Gemmable 4 12B MTP Q4_K_M (119.8/300) on the same suite — that model carries its own Evaluation page.

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.

Shared comparison: `practical-use-comparison-2026-06-21` — one immutable shared report; related model pages list
this event with their own measured entries.
