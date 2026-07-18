# 2026-07-16 · A3 session: branch (c) executed, the erosion clock placed in WP-07

**Role:** A3 formalist (First-Person direction of 2026-07-16 selected branch (c) of the L143 memo, conditional on verification).
**Verdict first:** both displays of the L143 candidate construction VERIFY, and the erosion leg is PLACED in WP-07 (`rehydrations/academic/linear_cap_paper.md`, now revision-draft-v3): Definition 3.9 (background side-information family {B_t}, Markov B_t → X → T) and Corollary 5.4b (the cap survives conditioning, I(T; X | B_t) ≤ Σ ε_i; the floor erodes through the residual entropy, P_e(t) ≥ (H(X | B_t) − Σ ε_i − 1)/log(|𝒳| − 1); informed deficit Σ ε_i < H(X | B_t); shelf life t*_inf = first crossing). ER-6's certified-bound semantics is undisturbed; the paper now carries two named clocks, certification (epistemic) and erosion (real), with the instruction that every downstream time-indexed reconstruction statement name which clock it runs on. Zero new citation keys. Checks re-run on the file: figures_fence / register_refs / tier_vocab / versions PASS, 0 em-dashes. Ledger L145.

## Mathematical record

- Notation change from the memo: the corpus variable is **B_t**, not Z_adv(t) (Z is taken in-paper by the interface messages Z_i). Erosion ratio **R_inf(t) = Σ ε_i / H(X | B_t)**.
- Display (i) needs ONLY the Markov hypothesis and Theorem 5.1: I(T; X | B_t) = I(T; X) − I(T; B_t) by the chain rule in two orders, since I(T; B_t | X) = 0.
- Display (ii) is Theorem 3.2 with Y := (T, B_t); the entropy bound H(X | T, B_t) ≥ H(X | B_t) − Σ ε_i follows from (i).
- Monotonicity: B_s measurable from B_t gives H(X | B_t) ≤ H(X | B_s); with certified budgets non-decreasing, the deficit set is an interval and t*_inf is the first crossing.
- Exact-Fano strictness under the informed deficit: I(T, B_t; X) = I(B_t; X) + I(T; X | B_t) < H(X), so P_e > 0.
- Fences placed with the result (GR-7/GR-8): the Markov hypothesis fails for a corpus containing transcript material, and conditioning can then increase leakage beyond the cap (corollary inapplicable); the background family is a declared model, symmetric to ER-6's declared decoder class; the empirical schedule of H(X | B_t) is not estimated; past t*_inf the floor is vacuous for every architecture (the corollary bounds what the transcript adds; it cannot prevent the world learning the source by other means); the normalised form's hypothesis H(X | B_t) ≥ log(|𝒳| − 1) itself expires.
- Open Problem 5.8 scope note added: a Grade-2 upgrade concerns the erasure guarantee's certification index and does not arrest the erosion clock.

## Edit inventory (all in linear_cap_paper.md)

Abstract (one sentence), contribution 4, section 2 time-varying-capacity paragraph, Remark 3.4 closing (two clocks), Definition 3.9 (end of §3.3), ER-6 semantics cross-reference, Corollary 5.4b + three-readings fence paragraph (after Cor 5.4), OP 5.8 scope note, §5.4 limits bullet, §6 "Two clocks, and the corpus model" paragraph, §7 framing sentence, frontmatter status (revision-draft-v3), traceability appendix row.

## Support files for the propagation process (same session)

- `plans/SOIL_PROPAGATION_EXECUTION_PACKET_2026-07-16.md`: self-contained packet for the corpus-propagation agent (ruling, formal object, canonical wording W1-W5, per-surface worklist with gates, false-positive fences, verification recipe). Indexed in `plans/INDEX.md`.
- `reviews/PHASE2_PHASE6_STAGED_DRAFTS_2026-07-16.md`: updated with the ruling + B_t notation note.
- `plans/DISPLAY_AND_DISTRIBUTION_UPDATE_PLAN_2026-07-16.md` (the display agent's plan): dated gate-status note added, **G-P1 OPEN** (items A5/A7/C2 unblocked), G-REG remains closed.

## Reversals

None mathematical. The memo's Z_adv notation was corrected to B_t before placement. No canon touched; register rows C82/C55 unmoved (G-REG closed); P4 not marked; nothing committed or pushed.

## Handoff

- **A9:** full P3 re-run on WP-07 (this session's check pass was a spot re-run, not the station).
- **A5:** targeted look at Definition 3.9 + Corollary 5.4b (new mathematical material post-review) before P4.
- **WP-14 revision loop (A12/A2/A3):** durability leg cites Corollary 5.4b; Assumption A3 replacement text is in the execution packet §3b; fixes the S2/Assumption-A3 split (L143 finding 2) in the same pass; M3 resolution path now concrete.
- **A1:** Phase-2 E2-C02/C04 re-pin per the staged drafts, branch-(c) wording, B_t notation; E2-C03 waits on the C82 register row (GR-1).
- **First Person:** G-REG dispositions (C82 re-word, C55 character change, figure batch, inscription supersession); P4 re-read of WP-07 revision-draft-v3; commits/pushes/deploys.
- **Propagation agent:** execute from the packet, corpus items §3c only, fences §4, verify per §5.
