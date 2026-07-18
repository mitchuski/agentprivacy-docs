# 2026-07-16 · Erosion leg reviewed (A9 GREEN, A5 MINOR discharged); WP-14 and E2 revised to consume it

**Role:** A0 orchestrator for the loop; A9 and A5 run as delegated review agents; the fixes applied as A3; the WP-14 integration as A2/A12-class revision-loop work; the E2 re-issue as A1-class maintenance. Ledger L146.
**Verdict first:** the L145 erosion leg survives adversarial review with no mathematical defect (A5: "no proof step is wrong"; A9: GREEN across all six consistency checks with the 5.4b proofs independently re-verified), and the two research surfaces the ruling unblocked now consume it: WP-14 is draft-v4 with its durability leg on the two-clock form and the M3 metric-agreement half of the submission gate discharged, and E2-C02/C04 are re-issued so the moving-ceiling chain has its corrected source definition.

## Review stations

- **A9 (full-file consistency):** GREEN. Cross-references, numbering, notation inventory, GR-7/GR-4 discipline, frontmatter-vs-body, traceability row: all pass. Two cosmetic notes applied (Remark 3.4 "a time-indexed quantity"; 𝔄_tr(t) now used at 5.4b(ii)); the imported-Theorem-4.1 number coincidence stays deferred to A8 port.
- **A5 (targeted adversarial, erosion leg only):** MINOR. Independently verified all three parts of Corollary 5.4b including edge cases (trivial B_t recovers Corollary 5.4; the normalised form's guard; the non-Markov counterexample T = X ⊕ K, B = K confirming the fence is necessary and present). Four MINORs + two NOTEs, all prose-precision, all discharged same day:
  1. §5.3 preamble re-scoped: Grade-2 erasure's upgrade carries "no certification index" (not "no time index"), with the 5.4b contrast added. This was the one pre-existing sentence the new material made overclaiming.
  2. GR-8 weakening: "genuinely falls" → non-increase plus any-fall-is-genuine (Definition 3.9 admits a constant family); §7 sentence aligned.
  3. "The drift here is real" qualified to the model's sense: what moves is the modelled quantity itself, not a certificate of a fixed quantity.
  4. One-calendar clause added at Definition 3.9: two clocks are two quantities drifting on one calendar, not two time axes.
  5. Markov-violation examples widened ("for instance"; backgrounds correlated with invocation-internal randomness also violate; displayed condition exact).
  6. Portability remark added: the corollary uses only Theorem 5.1's conclusion, so it applies to any composition carrying a certified transcript cap.
- Checks re-run after fixes: figures_fence / register_refs / tier_vocab / versions PASS; 0 em-dashes.

## WP-14 → draft-v4 (durability leg on the two-clock form)

Abstract, S1 clock paragraph, and S3 inalienability passage re-typed from "frontier/adversary capability grows" to background-information accumulation. S2 gains the companion-proof sentence (cap survives conditioning; floor erodes through the record's residual entropy; the protection does not leak more, it matters less). Assumption A3 rewritten to the two-deficit form: informed deficit $C_S + C_M < H(X \mid B_t)$, ratio $R(t) = (C_S + C_M)/H(X \mid B_t)$, drift moved from numerator to denominator, discharging the L143-finding-2 internal split. S6 limits block re-typed; submission gate updated to the resolved form: citability remains the gate, the metric-agreement half is discharged. Trace comment updated. Checks: register_refs/tier_vocab/versions PASS; figures_fence flags only the two pre-existing strip-at-release trace comments (benign, L138-era pattern); 0 em-dashes; 12,520 words. Still open: LM3 hedge, A4 full P2 pass, alphabetical reference interleave.

## E2 re-issue (the moving-ceiling chain's source definition)

`soil-note` registered in SOURCES.md. E2-C02 re-issued to the two-clock definition (R_cert per ER-6 certified-bound semantics; R_inf(t) = (C_S + C_M)/H(X | B_t) per Definition 3.9 + Corollary 5.4b). E2-C04 re-issued: the formalisation obligation splits; the erosion half is DISCHARGED by Definition 3.9; the certification half (ordered decoder classes, QIF/Bayes-capacity grounding) stays open with A3. E2-C03 deliberately NOT re-worded (GR-1: it mirrors register C82; annotation routes to the staged register re-word; the frontier-capability wording now survives only there, pending the row). FEEDS widened with WP-14 (consumption verified). The Erlich et al. 2018 linkage instance stays a proposal routed to A4; it is cited nowhere. Checks PASS; the file's one em-dash is pre-existing in E2-C06's older claim line and was not touched.

## Reversals

None. No canon touched (spec/whitepaper/register rows unmoved; E2-C03's register-mirrored wording preserved per GR-1). P4 not marked. Nothing committed or pushed.

## Handoff

- **A0:** schedule the evolution-3 inheritor sweep now that the source definition is fixed (checklist A4-A7: `moving_ceiling_sok.md` Def 2, `the_moving_ceiling.md`, `enforceable_by_architecture.md`, `wp14_P1_derivation.md`), in E2-C02's new vocabulary.
- **A4:** WP-14 full P2 inline-cite pass; verify Erlich et al. 2018 (+ Sweeney, Narayanan-Shmatikov) before any linkage-instance claim enters E2.
- **A5 (optional, cheap):** economist spot-review of WP-14 draft-v4's revised durability material.
- **First Person:** C82 register re-word (E2-C03 and the master mirror follow it); the other G-REG dispositions; P4 reads of WP-07 rev-draft-v3 and, when the loop closes, WP-14; commits/pushes.
- **Propagation agent:** unchanged; the execution packet stands (its W1-W5 wording is consistent with everything landed this session).
