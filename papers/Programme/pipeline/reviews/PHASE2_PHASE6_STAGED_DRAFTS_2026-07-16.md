# Staged drafts: Phase-2 (E2 re-pin) and Phase-6-pipeline (soil framing), branch-conditional on the Phase-1 ruling

**Date:** 2026-07-16
**Status:** STAGED, NOT APPLIED. Nothing below is executed until Phase 1 of `plans/SOIL_PROPAGATION_PLAN_2026-07-16.md` is ruled (memo: `PHASE1_DECISION_MEMO_WP07_RT_2026-07-16.md`, ledger L143). Branch (a) is closed per L143; drafts are given for branches (b) and (c).

**UPDATE 2026-07-16 (L145): Phase 1 RULED branch (c) and executed.** WP-07 now carries Definition 3.9 + Corollary 5.4b. Use the BRANCH (c) variants below, with one notation change: read `Z_adv(t)` as **B_t** (background side information; Z was taken in-paper by the interface messages) and `R_adv(t)` as **R_inf(t) = Σ ε_i / H(X | B_t)**. The erosion clock is now citable, so drop every "no theorem behind it" label from the (c) wording. Consolidated wording + the full corpus worklist: `plans/SOIL_PROPAGATION_EXECUTION_PACKET_2026-07-16.md`.
**Discipline:** E2 is a regenerable pipeline extraction (A1's), safe once the gate opens, EXCEPT where noted: E2-C03 quote-mirrors register conjecture C82, and per GR-1 the extraction cannot move ahead of the register row. That dependency is marked below. Rehydration sweeps (checklist items A4-A7) follow the applied wording; they are listed, not drafted, to avoid hand-patching generated artifacts (GR-6).

---

## 1. Phase 2: the E2 re-pin (single source of the moving-ceiling chain)

### E2-C02 (design-assumption definition; safe for A1 once ruled)

**Current:** R(t) = (C_S(t) + C_M(t))/H(X), where H(X) is fixed by the source and C_S(t), C_M(t) are effective capacities against the strongest adversary class available at time t. Shelf life t* = sup{t : R(t) < 1}.

**Branch (b) draft (certification clock kept, honestly labelled):**
> R(t) = (C_S(t) + C_M(t))/H(X), where H(X) is fixed by the source and C_S(t), C_M(t) are certified effective capacities against the strongest decoder class available at time t, under the certified-bound semantics of WP-07 ER-6: what is non-decreasing in t is the certified value, not the transcript's information. Shelf life t* = sup{t : R(t) < 1}. The distinct reading of the drift as adversary-informational-capability erosion (accumulating linkage corpus and side priors against the fixed archive) is a register conjecture with no theorem behind it, and no artifact may present it as proven.

**Branch (c) draft (denominator object; requires the WP-07 corollary to exist first):**
> Two clocks are defined and must not be conflated. The certification clock is R_cert(t) = (C_S(t) + C_M(t))/H(X), capacities carrying WP-07 ER-6's certified-bound semantics. The erosion clock is R_adv(t) = (C_S + C_M)/H(X | Z_adv(t)), where Z_adv(t) is the adversary's calendar-indexed side information (accumulating linkage corpus and side priors), Markov Z_adv(t) -- X -- T, budgets fixed: H(X | Z_adv(t)) is non-increasing in t, so R_adv(t) is non-decreasing with nothing added to the archive and no weakening of any certificate. Shelf life t*_adv = sup{t : R_adv(t) < 1} (equivalently C_S + C_M < H(X | Z_adv(t)), the deficit condition evaluated against the corpus). The moving-ceiling economics cite the erosion clock; conformance and audit statements cite the certification clock.

### E2-C03 (REGISTER-GATED: mirrors conjecture C82; the register row moves first, GR-1)

**Current:** Frontier capability growth raises C_S(t) + C_M(t) against fixed archives without raising H(X); R(t) drifts upward; the drift is coupled to frontier-model release, not to any action of the subject.

**Proposed C82 re-wording for the register process (both branches; branch (c) shown, branch (b) identical with the "posited, not proven" label from C02(b) appended):**
> Adversary informational capability grows against fixed archives: the linkage corpus and side priors accumulate along calendar time, shrinking H(X | Z_adv(t)) while nothing is added to the archive and no action of the subject is involved. R_adv(t) drifts upward on a schedule. Frontier-model releases enter only informationally (better extraction of linkage from existing corpora), never as compute against the information-theoretic guarantee, which is compute-saturated.

### E2-C04 (design-assumption, formalisation obligation for A3; safe once ruled)

**Branch (b):** unchanged (ordered decoder classes {D_t} formalise what the CERTIFICATE is relative to).
**Branch (c) draft:** the obligation splits: (i) ordered decoder classes {D_t} for the certification clock, as now; (ii) a filtration {Z_adv(t)} (Z_adv(s) measurable from Z_adv(t) for s <= t) for the erosion clock; monotonicity of R_adv(t) follows from the filtration, empirical content is the rate of decrease of H(X | Z_adv(t)).

### Instances (both branches; SOURCES additions proposed to A0, not cited around the registry)

The two canonical instances (E2-C05 Zcash flaw, E2-C07 Shor spacetime-volume) are compute/cryptanalytic events and now sit off-analogy for the informational clock. Proposed supplementary instance class for A0/A4 verification and SOURCES.md registration before any claim is written:
- Long-range familial-search identification of genomic archives (Erlich et al. 2018, Science 362(6415)): a fixed DNA archive whose identifiability rose year over year purely because the third-party genealogy corpus grew. This is the informational-erosion clock in the wild: archive fixed, certificates untouched, H(X | corpus) falling on a calendar.
- Classic linkage re-identification (Sweeney 2000 k-anonymity motivation; Narayanan and Shmatikov 2008 Netflix) as the mechanism's antecedents.

### Sweep list after the extraction moves (checklist A4-A7; regenerate, do not hand-patch)

`moving_ceiling_sok.md` Def 2 (:230) and section 5.4; `the_moving_ceiling.md` (WP-01) :65/77/93/123 (reserve "compounds" for reputation); `enforceable_by_architecture.md` (WP-02) :128/348 (Mosca/HNDL stays analogy, not mechanism); `wp14_P1_derivation.md` :390/283. Plus the WP-14 revision-loop fix of its internal S2/Assumption-A3 split (L143 finding 2), in the ruled branch's vocabulary.

---

## 2. Phase-6-pipeline: the soil figure into the WEIS-cluster framing (A0, once Phase 1 sets the wording)

Target surfaces (checklist A8/A9): `extractions/E4-seventh-capital.md` E4-C01 framing note; WEIS cluster framing sections (skeleton, M2 note, valuation notes). The figure enters as framing prose, never as a claim with a confidence number (GR-2, tier A).

**Staged framing paragraph, branch (c) variant:**
> The economic character of the stock is land-like. It yields rent by position, not value by aggregation: the marginal product of one additional raw record is approximately zero, and the observer-to-subject gap decomposes as atomisation discount, market-position rent, and lifetime accumulation. Its exposure erodes on a calendar: the archive is fixed, and what grows is the adversary's side information, so the residual uncertainty H(X | Z_adv(t)) falls the way soil loses cover to weather, with nothing added to the plot. And it is leased, never conveyed: a scoped disclosure transfers a season's harvest, not the land, because the observing side cannot reconstruct the underlying record from it for the term the erosion clock permits. The one quantity that genuinely accumulates is the cultivated fertility of the relationship, the reputational stock, and that is a conjecture, not a measured aggregation of records.

**Branch (b) variant:** identical, with the erosion sentence replaced by:
> Its exposure is conjectured to erode on a calendar: the archive is fixed, and the register carries as a conjecture, not a theorem, that the adversary's accumulating side information shrinks the residual uncertainty about it the way soil loses cover to weather.

Honesty guard carried from the ruling note: the fertility sentence must never re-import the refuted aggregation intuition; reputation accumulates, raw soil does not.

---

Nothing above is applied. E2 edits are A1's on the open gate; the C82 row and every canon surface are the First Person's (GR-10). P4 is not marked.
