# Chronicle · A0 · WP-14 WEIS 2027 arc close-out

**Session:** 2026-07-14 / 2026-07-15
**Role:** A0 (orchestrator), running the pipeline as multi-agent workflows against `papers/Programme/pipeline/`.
**Scope:** WP-14 (`weis-seventh-capital`, tier A, thrust T3), from a cold start (E4 unbuilt) to an accept-class draft.

---

## Verdict

WP-14 stands at **accept-class**. A5 economist-referee **review-2 = MINOR revision** (ledger **L136**), 5 of 6 majors discharged in the artifact; the sixth (M3) is partial and gated on an external dependency, not a defect in this paper. The single remaining blocker to an actual WEIS 2027 submission is **WP-07** (the imported information-theoretic guarantee must be a real, citable companion). The valuation was rebuilt on external evidence across three adversarial passes; two canon-level findings surfaced and are on the ledger awaiting the register process. Nothing was committed, pushed, or submitted. **P4 remains the First Person's** and was not simulated.

## Path taken (five workflow runs)

1. **Run 1 — chain A1→A12→A2→A5.** Built E4 (12 claims, the GR-9 blocker), the WEIS skeleton, the first-pass tier-A draft, and A5 review-1 = MAJOR revision, 0 blocking (**L131**). Manifest: E4 → built; WP-14 → draft/gate P1.
2. **A10 prior-art scout** (parallel Agent, not a workflow). `rehydrations/academic/weis_prior_art_map.md`: 9 verified WEIS-native / adjacent entries, the must-engage shortlist, and the empirical-number shortlist. Independently corroborated review-1's novelty gap (M2) and figure gap (M4).
3. **Run 2 — empirical valuation rebuild.** `weis_valuation_methodology_v2_empirical.md` + `weis_seventh_capital_S5_patch.md`. The retired canonical figures (678x/31,000x) do not survive (**L130**, CANON-LEVEL). The rebuild's own "convergence" claim was **refuted** by the commensurability lens (observer gross-revenue flow vs subject reservation-value stock are non-commensurable; the overlap was an annualisation-knob artifact) → per-category ranges are the honest deliverable (**L132**, CANON-LEVEL).
4. **Run 3 — wedge tightening.** Data-attributable capture separated from gross ARPU via the targeting-premium fraction x ∈ [0.04, 0.52], central [0.2, 0.4] → observer capture ~$8.92–$17.84/yr (data-attributable) vs ~$44.60 gross. The single "super-additive aggregation wedge (10^1–10^5)" was found to be a **category error** and split into w_model (~10^0, saturating, super-additivity rejected by Bajari/Varian/Neumann) and w_gap (10^4–10^5, reclassified as **market-position RENT**, not aggregation value) (**L133**, **L134**, CANON-LEVEL). Magnitude did not become point-identified; the categorisation did.
5. **Run 4 — revision loop (with a reversal).** A3 derived Proposition P1 in full; A12 answered the propertization literature + integrated the rent finding + retitled (M5); A4 added 19 verified references. **A2 integration crashed on a transient API drop and wrote nothing**; the A5 pass that ran therefore reviewed the un-revised draft and was logged as a process entry (**L135**). Retry workflow re-ran integration (against the on-disk side files) + a proper review-2: revised draft written (9,925 words, retitled), **review-2 = MINOR/accept-class (L136)**, superseding L135.

## Reversals and corrections on the record

- The Run-2 convergence framing was asserted then refuted within the same run; the honest per-category form is what survives (L132).
- "Super-additive" was dropped entirely from the wedge; the canon figures it descended from do not survive at tier A (L130/L134). These are GR-10 escalations, **not** resolutions — the register process decides the canon surfaces.
- A2's first integration attempt failed (infrastructure, not quality); the substance was intact in side files and merged on retry. L135 (process) is superseded by L136.
- M3's "term structure" over-claim was retracted to "a finite, adversary-relative horizon"; the durability leg is honestly flagged as reverting to an open problem if WP-07 is not citable at submission.

## State at close

- **Manifest:** E4 = built; WP-14 = revised / gate P1 (review-2 accept-class; P2 cite-verify + P3 trace-strip pending).
- **P3 checks (via `py`, not `python3`):** register_refs / tier_vocab / versions PASS; figures_fence "fails" only on strip-at-release trace comments (lines 40, 617) — green at release.
- **Ledger:** L130–L136 all WP-14. Three CANON-LEVEL escalations (L130, L132, L134) await the register process.

## Artifacts (all under `rehydrations/academic/` unless noted)

- `weis_seventh_capital.md` — the revised draft (draft-v2, accept-class)
- `weis_seventh_capital_firstpass_2026-07-14.md` — preserved first pass (lineage)
- `weis_valuation_methodology_v2_empirical.md` — the real-numbers valuation (tier internal, evidence-bearing)
- `weis_seventh_capital_S5_patch.md` — §5.1/5.2 replacement (folded into the draft)
- `wp14_P1_derivation.md` — A3's full Proposition P1 derivation
- `wp14_M2_rent_reframe_note.md` — A12's propertization answer + rent integration + M5
- `weis_prior_art_map.md` — A10's WEIS prior-art map
- `../../extractions/E4-seventh-capital.md` — the extraction
- `../../reviews/pc_reviews/WP-14_A5_economist_2026-07-14.md` (review-1) and `..._review2_2026-07-15.md` (review-2)
- `../../templates/submission/references/pv_v6.bib` — +19 verified references

## Handoff (when this is picked back up)

1. **Critical path = WP-07.** The durability leg needs the information-theoretic separation guarantee as a real, citable companion (chain A3→A11→A5, extraction E2 already built). Until then the paper is accept-class-conditional, not submittable. This is the next run if the loop continues.
2. **WP-14 polish (mechanical):** A4 verify the draft's inline citations against the bib (P2); strip the trace comments at release (P3 figures-fence closes); prepare an anonymised build **if** the 2027 CFP is double-anonymous — A13 re-checks the WEIS 2027 CFP on **2026-11-01** (deadlines.md).
3. **Register process (First Person):** the three CANON-LEVEL escalations (678x/31,000x non-survival; the IIRC six-capital enumeration correction; the convergence-framing and super-additive-wedge corrections) are on the ledger for the register to rule on. Rehydration agents do not resolve canon (GR-10).
4. **P4 is the door only the First Person holds.** No gate past P3 was marked, simulated, or assumed.

the extraction is built. the valuation is real. the mechanism is proven. the guarantee it leans on is the next thing to make citable.
