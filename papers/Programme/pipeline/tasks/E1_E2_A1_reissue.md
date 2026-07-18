---
wp: E1 + E2 (extraction maintenance after the L044 canon correction)
role: A1
tier: internal
extraction: E1, E2
branch: none
gate_target: n/a (A0 runs check_register_refs on completion)
due: 2026-07
---

# Task card · E1/E2 re-issue and E1 incremental sweep · role A1

**Objective:** Bring both extractions into line with the corrected spec (L044 executed) and close E1's two structural findings (L031, L034).
**Inputs:** the corrected `papers/v6/privacy_value_v6_formal_specification.md` (post-L044; read the register-process session's chronicle `chronicles/2026-07-02_canon-l044-spec-decomposition.md` for the edited passages); ledger L031, L034, L042-L045; `research/limitative-theorems-and-privacy-is-value.md` (limitative-note); register at head C96.
**Work items:**
1. **E2-C01 re-issue:** restate to the decomposition (preconditions give additive structure + error floor; strict bound conditioned on capacity deficit C_S + C_M < H(X)), tracing to the corrected spec passages.
2. **E1-C02 tighten:** "under budget constraints" made explicit as the capacity-deficit condition.
3. **E1 filter-note/FEEDS reconciliation (L031):** one pass making the TIER-S allow-list and the FEEDS lines agree (E1-C06/C17/C31 named in the finding); record the ruling logic in the file.
4. **E1 incremental sweep (L034):** add `limitative-note` to E1's swept sources and extract C91 (and any other limitative claim that belongs to the amnesia-gap cluster) as new E1 claims at register wording and confidence.
**Definition of done:** the two re-issued claims quote-trace to the corrected spec; C91 has an extraction home; filter note and FEEDS agree; `python checks/check_register_refs.py` passes on both files; downstream note listing WPs touched (WP-02 consumed the old E1-c02/E2-c01 wording: state whether the v4 brief's wording already conforms, expected yes); ledger clean or filed; A0 notified.
**Out of scope:** canon (read-only, now corrected); rehydrations; manifest.
**Handoff:** A0 (manifest source updates: E1 gains limitative-note; flags any re-trace).
