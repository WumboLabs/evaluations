### Identity and scope

- Profile: `qwen38-27b-llamacpp-ud-q2-k-xl` — Historical llama.cpp (Unsloth UD-Q2_K_XL GGUF)
- Evidence maturity: **PROFILE_OPTIMIZATION**
- Evidence scope: performance, serving-profile
- Hardware: WumboJetsII (RTX 5070 12GB)

llama.cpp-era quant/variant showdown evidence (unsloth v3-final UD-IQ1_S/IQ2_XXS/IQ2_M ladder, community variants AtomicChat/XYZ Q3 smokes, 16k practical-use selection, 196k context-retrieval probe) that informed the historical llama.cpp profile before the ExLlamaV3 H1 promotion. Long-form context completion is separately represented (context-envelope-completion-2026-09-12).

This event is a bounded public-safe summary derived from retained WumboLabs evidence.
It is not a WELP characterization, a universal model ranking, or a production-readiness
proof. Values are attributed to the tested artifact, runtime, hardware, suite, and settings.
### Historical lane note

These showdown runs belong to the historical llama.cpp lane. The current canonical serving
profile for this model is the ExLlamaV3 H1 surface, represented by its own events above.
