---
wp: CANON (L044 execution; approved first-person per L045)
role: register-process executor (no pipeline role may edit canon; this session acts on direct first-person approval, recorded L045)
tier: canon
extraction: none
branch: none
gate_target: first-person diff review
due: 2026-07
---

# Task card · L044 spec decomposition · register-process executor

**Objective:** Correct the specification's central-guarantee wording per the approved L044 decomposition: the two architectural preconditions yield the additive leakage structure and the error floor P_e >= 1 - R_max; the strict bound R_max < 1 holds only when additionally the capacity-deficit condition C_S + C_M < H(X) holds (measurable, declarable, time-eroding; deliberately NOT a third precondition).
**Inputs:** ledger L042/L043/L044/L045 (`reviews/critiques_ledger.md`); A5 analysis `reviews/pc_reviews/WP-02_review_1.md` weakness 1; the corrected exemplar wording in `rehydrations/policy/enforceable_by_architecture.md` §2-§3; targets `papers/v6/privacy_value_v6_formal_specification.md` (likely §10.5, §11.1, §11.5; sweep §5, §14, §16 for echoes) and `papers/v6/privacy_value_v6.md` (summary spec; correct the same conflation if present). Backups exist at `archive/canon-backups-2026-07-02/`.
**Output:** the corrected spec file(s); a complete before/after quote list (every edited passage) in the chronicle and final report for first-person diff review.
**Definition of done:**
- every passage asserting R_max < 1 (or "reconstruction ceiling holds") as a consequence of the two preconditions alone is decomposed; no passage deleted, meaning preserved, minimal edits;
- t*-adjacent passages stay coherent (what expires at t* is the deficit condition, not the architecture);
- `research/CONJECTURE_REGISTER_V6.md` NOT touched; no section renumbering; no other content changes;
- before/after quotes complete; A0 notified; first-person diff review is the completion condition, not any gate.
**Out of scope:** the register; the whitepaper (parallel session owns it); spec §16 95%-label scoping (L028, unapproved); extractions (A1 re-issues after this lands).
**Handoff:** A1 (E2-C01 re-issue and E1-C02 tightening trace to the corrected wording); first person (diff review).
