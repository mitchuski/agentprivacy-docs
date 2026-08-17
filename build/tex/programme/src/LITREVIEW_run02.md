---
title: "WP-14 Literature Review — Adversarial Novelty Adjudication (Run 02)"
author: "The Privacy-is-Value Research Programme"
date: "2026-07-15"
---
# Lit-review runtime · run manifest

**Runtime:** `weis-litreview-runtime` (V6 pipeline workflow)
**Brief:** `chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md` (Matsuo venue+gap calls; C17; defects D2/D3/D4b in scope)
**Purpose:** produce a *defensible* novelty claim for WP-14 (WEIS 2027), not a summary. Mitchell runs the loop and owns all conjecture assignment; the runtime produces candidates and structure only (brief §2, §9).
**Run ID:** wf_ba400906-67b
**Date:** 2026-07-15
**Operator role:** A0 (orchestrator), extending A10 (prior-art scout) with an adversarial dual-seat loop.

---

## Seat configuration (D4b auditability, brief §5)

Seat separation is **structural, not prompt-only** (D3). Each seat is a distinct workflow `agent()` invocation with its own isolated context; no seat reads another seat's reasoning trace.

| Seat | Role | Isolation | Sees |
|---|---|---|---|
| extract:* | per-paper schema extraction (one per corpus item) | isolated invocation per paper | only its own paper hint + the PVM position + WebSearch |
| prove:* | PROVER — builds the case that the candidate is novel | isolated invocation | the candidate claim + corpus digest + WebSearch |
| refute:* | DELEGATOR — hunts covering prior art to destroy the claim | isolated invocation, **does not see the prover's argument** | the candidate claim + corpus digest + WebSearch |
| judge:* | JUDGE — rules VALIDATED / MIRAGE / BLOCKED | isolated invocation | the candidate claim + both seats' structured outputs |
| synthesise:* | assembles the four outputs | isolated invocation | the full corpus + all verdicts |

**D4b note (honest limit).** All seats run on the same underlying model. The separation this runtime enforces is *context isolation* (each seat forms its own search and reasoning with no shared trace), not distinct model weights. The delegator is given the full corpus and independent WebSearch capacity and is instructed to default to finding prior art; the adversariality is real but is seat-context-level, not weights-level. A run that returns all-VALIDATED is treated as a **failed** enforcement of D2/D3, not a success — MIRAGE is the expected, valuable verdict.

## Hardening constraints enforced

- **D2 (no absence-as-novelty):** the delegator must report absence as `not_found_in_corpus(n, range)` with web scope, never as `novel`; every contribution claim carries a verdict + the corpus tested + a confidence label.
- **D3 (structural isolation):** prover and delegator are separate invocations; the delegator never sees the prover's case.
- **D4b (seat separation auditable):** this manifest records the seat config; see the honest limit above.
- **C81 hold-back:** the Privacy Pools V2 constraint-reduction result does not enter the runtime or any output.

## Corpus (Tier A, challenge corpus)

20 items across five strands: propertization (6), data-as-labour (2), WEIS-native economics-of-privacy (7), privacy quantification (3), standards/PIA (2). Provenance-gated: each carries a DOI/URL and a `provenance_confidence`; `uncertain` items are flagged for first-person verification in `bibliography.md`.

## Outputs (this directory)

- `gap_table.md` — corpus clustered on unit_of_analysis × economic_framing; the `system_property × market_pricing` cell called out.
- `contribution_claims.md` — CTR-shaped novelty candidates, each with verdict, residual novel core, corpus tested, confidence.
- `ctr_candidates.md` — conjecture-shaped residues (CTR-series only; assignment is the First Person's).
- `bibliography.md` — full citations with provenance, WEIS-submission ready.

*Generated artifacts; do not hand-edit. Fix the runtime inputs and rebuild.*

\newpage

# Gap table: the privacy-value corpus on unit-of-analysis x economic-framing

## Gap grid: unit_of_analysis x economic_framing

Corpus n = 20. Each cell lists the corpus items that land there. Short keys resolve to full citations in the bibliography.

| unit \ framing | none | cost_model | incentive_model | market_pricing |
|---|---|---|---|---|
| **subject_impact** | ISO/IEC 29134:2017; ISO/IEC 29100:2011 | (empty) | Delacroix-Lawrence 2019 | Laudon 1996; Samuelson 2000; Schwartz 2004; Purtova 2015/17; Prins 2006; Arrieta-Ibarra et al. 2018; Posner-Weyl 2018; Acquisti-John-Loewenstein 2013; Collis et al. 2022; Beresford-Kuebler-Preibusch 2012; Grossklags-Acquisti 2007 |
| **system_property** | Dwork 2006; Sweeney 2002; Smith 2009 | (empty) | Anderson 2001 | **(empty, 0 items)** |
| **both** | (empty) | (empty) | Acquisti-Taylor-Wagman 2016 | Spiekermann et al. 2015 |
| **unclear** | (empty) | (empty) | (empty) | (empty) |

Row/column totals: subject_impact = 14, system_property = 4, both = 2, unclear = 0. Column totals: none = 5, cost_model = 0, incentive_model = 3, market_pricing = 12.

## The load-bearing cell: {system_property x market_pricing}

**Exact membership count in the corpus: 0.**

No item in this 20-paper corpus both (a) takes the unit of measurement to be a property of the release mechanism or system, rather than the reported impact on a named subject, and (b) prices that property as a market quantity. The four system_property items either carry no economic framing at all (Dwork, Sweeney, Smith are formal leakage or indistinguishability bounds with `economic_framing = none`) or frame economics as incentive misalignment rather than pricing (Anderson, `incentive_model`). Conversely, every market_pricing item measures a subject-reported valuation, a legal entitlement of a named subject, or a market-position quantity attached to a subject, not a system property.

**What this means for the WEIS contribution claim.** This emptiness is a genuine structural feature of the assembled corpus, and it motivates the PVM position, but under discipline D2 it must be reported as `not_found_in_corpus(system_property x market_pricing, this 20-item corpus)` and NOT as "no prior work prices a system property." The adjudicated verdict on CTR-LR-02 is explicit that the literal in-corpus emptiness is a corpus-selection artefact: the external differential-privacy-markets strand (Ghosh-Roth 2011 and successors) does price the DP disclosure bound as a traded commodity and therefore occupies this cell outside the corpus window. Confidence that the cell is empty *within this corpus*: high (certain by inspection). Confidence that the cell is empty *in the field*: refuted (see CTR-LR-02 verdict). The defensible WEIS framing is therefore narrower than "we are first to price a system property": it is "we price a finite, adversary-relative, time-drifting reconstruction bound held as inalienable subject-owned capital," which is the residual that survives adjudication.

## Second grid: adversary_model coverage

| adversary_model | count | items |
|---|---|---|
| **explicit** | 2 | Dwork 2006; Smith 2009 |
| **implicit** | 7 | Samuelson 2000; Delacroix-Lawrence 2019; Acquisti-Taylor-Wagman 2016; Spiekermann et al. 2015; Anderson 2001; Sweeney 2002; ISO/IEC 29134:2017 |
| **absent** | 11 | Laudon 1996; Schwartz 2004; Purtova 2015/17; Prins 2006; Arrieta-Ibarra et al. 2018; Posner-Weyl 2018; Acquisti-John-Loewenstein 2013; Collis et al. 2022; Beresford-Kuebler-Preibusch 2012; Grossklags-Acquisti 2007; ISO/IEC 29100:2011 |

Reading: an explicit adversary appears only in the two pure formal-metric papers (Dwork, Smith), both of which have `economic_framing = none`. Every market_pricing item has an absent or (in two survey cases) merely implicit adversary. The intersection {explicit adversary} x {market_pricing} is also empty in the corpus. This reinforces the same gap from a different axis: adversary-relativity and pricing do not co-occur in any corpus item, which is exactly the join the PVM reconstruction bound R(t) attempts, and exactly the join that the CTR-LR-05 residual (adversary-relative drifting horizon carried into a capital valuation) is scoped to.

\newpage

# Contribution claims: adversarially adjudicated novelty candidates

## Novelty candidates: verdicts and surviving residues

Five novelty candidates were tested against the assembled corpus plus the adjudicators' web scope. **All five returned MIRAGE at the altitude stated.** None returned VALIDATED and none returned BLOCKED. This is the honest headline: the strongest form of each claim as written is anticipated. What survives in each case is a narrower residual novel core. The residues are ranked below by the adjudicated confidence that the residual itself survives, strongest first.

The verdict vocabulary: VALIDATED = the stated claim survives as novel; MIRAGE = the stated claim is anticipated but a narrower residue survives; BLOCKED = withheld (for example under an existence-leak hold). No claim here is VALIDATED, so every entry below is a MIRAGE-with-residue.

### 1. CTR-LR-02 (strongest surviving residue) â€” MIRAGE

**Claim as stated.** No prior work prices privacy as a market quantity attached to a system property (a reconstruction bound) rather than to subject-reported impact or to a technical metric with no market; the {system_property x market_pricing} cell is empty.

**Why it MIRAGE'd.** The differential-privacy-markets strand (Ghosh-Roth 2011 *Selling Privacy at Auction*, Li-Miklau-Roth-Suciu 2013/14, Fleischer-Lyu 2012, Cummings et al. 2015) already prices the DP disclosure bound epsilon, an adversary-independent system property, as a traded commodity with per-subject compensation and a formal equilibrium price. That occupies the asserted-empty cell and refutes the "no market" framing.

**Residual novel core (survives).** PVM is the first, against the surfaced corpus plus the DP-markets strand, to price a *finite, adversary-relative, time-drifting* reconstruction bound R(t), not a static adversary-independent DP or accuracy budget, held as inalienable subject-owned durable capital, with the observer-to-subject value gap decomposed as market-position rent rather than super-additive aggregation. It is the *joint* quadruple (drift + adversary-relativity + structural inalienability + rent decomposition) that is uncovered.

**Corpus tested against.** 20-item corpus (system_property tags: Anderson, Dwork, Sweeney, Smith; market_pricing tags: Laudon, Posner-Weyl, Acquisti et al.) plus external DP-markets strand.

**Confidence that the residual survives: high (86%).**

### 2. CTR-LR-03 â€” MIRAGE

**Claim as stated.** The subject-side near-zero surplus share is derived as the subgame-perfect equilibrium of a consent-interface bargaining game (notice-and-consent read as an ultimatum extensive form), and IEEE 7012 propose-and-respond inverts the proposer role to move that share off the floor.

**Why it MIRAGE'd.** Half A (near-zero responder share as the SPE of a one-shot ultimatum) is the standard Gueth 1982 / Stahl-Rubinstein result. Half B (IEEE 7012 / MyTerms inverting the proposer to shift bargaining power) is the MyTerms standard's own self-description. The bridge (reading the consent screen as the extensive form) is already published: privacy-law scholarship (Norton 2016; Richards-Hartzog 2025) maps notice-and-consent adhesion contracts onto take-it-or-leave-it structures with the firm as unilateral proposer. The composite was not found as one unit, but each half is separately covered and the join is routine.

**Residual novel core (survives).** Casting the empirically measured WTA/WTP floor and the MyTerms remedy as two evaluations of one preference-free SPE share function of proposer identity, with the subject-side share written as a structural venue-exclusion parameter s = h_X (the floor arising because the subject is excluded from the clearing venue, a structural rather than cognitive origin), and IEEE 7012 as the specific proposer permutation carrying h_X to an interior share.

**Corpus tested against.** 20-item corpus plus ultimatum/Rubinstein microeconomics, the WTA/WTP strand, the propertisation strand, notice-and-consent-as-adhesion privacy law, and the IEEE 7012 / MyTerms literature.

**Confidence that the residual survives: moderate (70%).**

### 3. CTR-LR-04 â€” MIRAGE

**Claim as stated.** The observer-to-subject value gap is market-position rent (atomisation discount + venue exclusion), not super-additive aggregation; returns-to-scale evidence rejects raw-record compounding; therefore redistribution requires pooling bargaining position, not replicating aggregation scale.

**Why it MIRAGE'd.** Each plank has corpus-adjacent prior art. The gap-as-structural-rent plank is anticipated by Bergemann-Bonatti-Gan 2022 (aggregator captures total information value via the social-data externality) and by the Posner-Weyl / Arrieta-Ibarra monopsony account. The flat-returns-to-scale plank is supplied by Bajari-Chernozhukov-Hortacsu-Suzuki 2019 and the "data is not the new oil" line. The pool-position plank is the standing data-union programme. The claim rests novelty on the joint move, but the join is closely anticipated by combining works already co-present.

**Residual novel core (survives).** The directed internal falsifier: using flat-N returns-to-scale evidence to deny a positive marginal product of an additional raw record, thereby showing that data-as-labour's "raise the wage toward marginal product via a labour cartel" remedy self-defeats (marginal product approximately zero), and re-specifying the redistributive object as venue-access/clearing-position rent rather than a wage. Stated as a directed correction to the labour-union / propertisation programme inside a reconstruction-bound / IEEE 7012 frame.

**Corpus tested against.** 20-item corpus plus data returns-to-scale, data-monopsony and data-union remedy literatures, social-data-externality surplus-capture work, and thin-market propertisation critiques.

**Confidence that the residual survives: moderate (70%).**

### 4. CTR-LR-01 â€” MIRAGE

**Claim as stated.** PIA measures impact to a named subject after the fact by survey/process (ISO/PIA); PVM instead bounds disclosure in advance and architecturally, with R a per-subject reconstruction bound and Phi the system property gating R; the unit of analysis shifts from subject-impact to system-property.

**Why it MIRAGE'd.** The system-property/reconstruction-bound structure is the founding form of quantitative information flow (Smith 2009 min-entropy vulnerability is a per-secret one-guess reconstruction bound) and differential privacy (Dwork 2006 epsilon is an ex-ante mechanism property; Dinur-Nissim 2003 the per-record reconstruction threshold). Separately, Wagner-Boiten 2018 already argues the PIA tradition should be replaced by quantified system-level metrics, the exact subject-survey-to-system-metric transition the claim names. Each half of the move is covered; what remains is re-contextualisation.

**Residual novel core (survives, thin).** A packaging move, not a new object: explicitly positioning a governance-facing, independently verifiable mechanism property Phi, held two-level-distinct from the per-subject reconstruction bound R it gates, as the single unit that a privacy impact-assessment or valuation instrument is conducted over. Genuinely un-verbatim only in the deliberate Phi/R governance-versus-quantity separation offered as the assessment unit.

**Corpus tested against.** 20-item corpus plus QIF (Smith 2009), DP (Dwork 2006), Dinur-Nissim 2003, Sweeney 2002, Wagner-Boiten 2018, and Balle-Cherubin-Hayes 2022 as the reconstruction-bound proxy.

**Confidence that the residual survives: moderate (68%).**

### 5. CTR-LR-05 â€” MIRAGE

**Claim as stated.** Behavioural-data-as-capital is durable only for a finite, adversary-relative horizon set by an information-theoretic reconstruction bound R(t) that drifts upward as adversary capability grows; the asset has a term, not perpetuity; no prior propertisation or valuation work indexes durability to a time-varying reconstruction bound.

**Why it MIRAGE'd.** The headline (a durability term set by an adversary-relative horizon that drifts upward) is substantially covered by Mosca's cryptographic shelf-life inequality (X + Y > Z) and the harvest-now-decrypt-later threat model, which already joins a drifting-adversary horizon to a required-protection term. That is exactly the convert-drift-into-a-maturity move the claim advertises as unclaimed.

**Residual novel core (survives).** Substituting an information-theoretic reconstruction bound in the Dinur-Nissim / QIF sense for Mosca's cryptographic break-time clock, and carrying that substituted clock into a subject-owned capital-asset valuation. Distinct from Mosca (which prices nothing and uses a crypto break-time) and from staleness/relevance-decay depreciation (which prices a term but on an endogenous fixed clock). A thin combination novelty, not the structural insight the claim advertised.

**Corpus tested against.** 20-item corpus plus Mosca inequality / cryptographic shelf-life / HNDL, Dinur-Nissim reconstruction and adversary-aware DP reconstruction bounds, data-value depreciation economics, and finite-horizon data-as-capital pricing.

**Confidence that the residual survives: moderate (66%).**

## What MIRAGE'd, and why that is a feature not a bug

All five candidates were knocked down from their stated altitude. This is the evidence that the prior-art search was adversarial rather than confirmatory. The pattern is consistent: in every case the *object* (a reconstruction bound; an ultimatum SPE; a structural rent; a system-property unit; a shrinking durability term) was already owned by named prior art, and the surviving novelty is a *specific composition or re-specification* layered on top of that object.

- CTR-LR-02: the market-priced system property is owned by Ghosh-Roth; only the drift + adversary-relativity + inalienability + rent quadruple survives.
- CTR-LR-03: the ultimatum floor and the proposer inversion are each owned; only the preference-free venue-exclusion parameterisation unifying them survives.
- CTR-LR-04: rent-framing, flat returns-to-scale, and pool-for-leverage are each owned; only the directed self-defeat falsifier of the data-as-labour remedy survives.
- CTR-LR-01: the reconstruction-bound object (QIF/DP) and the PIA-to-metric transition (Wagner-Boiten) are each owned; only the Phi/R governance separation as the assessment unit survives, and thinly.
- CTR-LR-05: the shrinking adversary-relative term is owned by Mosca; only the IT-bound-for-crypto-clock substitution inside a capital valuation survives.

The disciplined WEIS contribution is therefore the *conjunction* of these surviving residues within a single instrument, not any one of the headline claims taken alone. None of the residues should be written as "no prior work does X"; each is a candidate tested against a named corpus with a stated confidence, per D2.

\newpage

# CTR candidates: conjecture-shaped residues (assignment is the First Person's)

## Conjecture candidates (residues in CTR-series form)

Each surviving residual novel core is restated below as a testable conjecture with the measurement that would settle it. These are proposals only. **CTR-series ID assignment is the First Person's; the IDs below are placeholders in the CTR-LR-R series and carry no authority until the First Person ratifies them.** They are never to be promoted to C-series here. Every proposition is a candidate against a named corpus, not an absence claim.

### CTR-LR-R1 (residue of CTR-LR-02) â€” proposed

**Proposition.** Pricing a *finite, adversary-relative, time-drifting* reconstruction bound R(t) held as inalienable subject-owned capital, with the observer-to-subject gap decomposed as market-position rent, is not reducible to the differential-privacy-markets pricing of a static budget epsilon (Ghosh-Roth and successors).

**Measurement that would settle it.** Construct a mapping from a Ghosh-Roth-style auction on epsilon to the PVM pricing of R(t). If the mapping is total and value-preserving (the PVM price is recovered as a special case by freezing drift and adversary-relativity and removing the rent decomposition), the residue collapses and the conjecture is refuted. If any of the four features (drift, adversary-relativity, structural inalienability, rent-not-aggregation) has no image under the mapping, the residue stands for that feature. Confidence the residue stands under this test: high (86%), speculative.

### CTR-LR-R2 (residue of CTR-LR-03) â€” proposed

**Proposition.** The measured WTA/WTP floor and the IEEE 7012 remedy are two evaluations of one preference-free SPE share function s(proposer), where the floor equals a structural venue-exclusion parameter h_X (not a reservation-utility artefact), and IEEE 7012 is the specific proposer permutation carrying h_X to an interior share.

**Measurement that would settle it.** Specify s(proposer) with no preference primitives and fit it to two anchor points: the observed near-zero floor (firm-proposer arm) and any measured post-MyTerms share (subject-proposer arm). Settled affirmatively if a single preference-free parameter set reproduces both arms and if varying the reservation utility alone cannot reproduce the floor (isolating venue exclusion h_X as the driver). Refuted if the floor is fully explained by reservation utility without a venue-exclusion term. Confidence: moderate (70%), speculative.

### CTR-LR-R3 (residue of CTR-LR-04) â€” proposed

**Proposition.** Scale-replication data cooperatives fail to redistribute value because returns to raw-record scale are flat (marginal product of an additional record approximately zero), so the data-as-labour "wage toward marginal product via a cartel" remedy self-defeats, and only pooling venue/clearing-position rent redistributes.

**Measurement that would settle it.** Estimate the elasticity of downstream model or auction value with respect to N (records) holding the clearing venue fixed, versus its elasticity with respect to bargaining/venue access holding N fixed. Settled affirmatively if the N-elasticity is statistically indistinguishable from zero over the relevant range while the venue-access elasticity is strictly positive. Refuted if raw-record N carries a positive, exploitable marginal product that a cooperative could monetise as a wage. Confidence: moderate (70%), speculative.

### CTR-LR-R4 (residue of CTR-LR-01) â€” proposed

**Proposition.** A governance-facing, independently verifiable mechanism property Phi, held two-level-distinct from the per-subject reconstruction bound R it gates, can serve as the single unit over which a privacy impact-assessment or valuation instrument is conducted, and this two-level separation is not already carried by QIF/DP (which supply the object but not the instrument framing) nor by Wagner-Boiten (which supplies the instrument framing but not the Phi-gates-R unit).

**Measurement that would settle it.** Attempt to instantiate the PIA/valuation instrument using QIF/DP objects alone (no explicit Phi/R governance split) and, separately, using Wagner-Boiten metrics alone. Settled affirmatively if neither instantiation reproduces the auditability property that the explicit Phi/R separation provides (for example, a third-party attestation of Phi without disclosure of R). Refuted if either prior instrument already yields that attestation. This residue is thin; confidence: moderate (68%), speculative.

### CTR-LR-R5 (residue of CTR-LR-05) â€” proposed

**Proposition.** Substituting an information-theoretic reconstruction bound R(t) (Dinur-Nissim / QIF sense) for Mosca's cryptographic break-time clock, and carrying it into a subject-owned capital-asset valuation, yields a maturity/term that neither Mosca (prices nothing, crypto clock) nor staleness-decay depreciation (prices a term, fixed endogenous clock) produces.

**Measurement that would settle it.** Compute the durability term three ways for the same behavioural-data asset: (a) Mosca cryptographic shelf-life, (b) staleness-decay depreciation, (c) IT reconstruction bound R(t). Settled affirmatively if the R(t) term diverges materially from both (a) and (b) under a growing-adversary schedule (for example the term shortens with adversary compute in a way the fixed-clock model cannot express and the crypto-clock model expresses only for confidentiality, not valuation). Refuted if all three coincide up to relabelling. Confidence: moderate (66%), speculative.

**Note on scope.** None of the above is stated as "no prior work does X." Each is a candidate proposition bound to the corpus and web scope named in its parent verdict, with a confidence label, per discipline D2. Promotion, renumbering, or rejection is reserved to the First Person.

\newpage

# CTR-LR-02b: DP-refinements stress test of the R(t) residue (LM2 resolution)

## Verdict: distinction_holds_but_phrasing_wrong

**Residual after stress:** The R(t) residue survives the LM2 stress test, but sharpened and narrowed rather than left at its LR-02 form. Honest confidence: ~85% (essentially steady on the empty-cell fact, downgraded on its reach). The high-confidence, scope-bounded part is that within the surveyed DP-refinements strand no work indexes a fixed archive's per-subject reconstruction residual to adversary-capability growth along calendar time (CTR-LR-02b-ii/iii, high). What the stress test removes is the overreach: the claim can no longer be stated as 'categorically distinct' or grounded on 'static, adversary-independent' DP. The surviving form is (i) a CLOCK distinction (query/release-composition vs calendar-time adversary capability), (ii) restricted to the INFORMATIONAL-capability reading (accumulating linkage/side-prior corpus, not compute, which orthodox DP saturates), and (iii) explicitly current-formalization-contingent, since adversary-aware DP already carries capability as a static parameter and computational DP already gestures at the same erosion. Publishable as sharpened novelty in that narrowed informational form; not as an in-principle impossibility result.

## What differential privacy DOES do (do not understate)

Adaptive, RÃ©nyi, concentrated, Gaussian and composition DP do model an adversary: the guarantee is calibrated against a worst-case adversary of unbounded computation and arbitrary auxiliary knowledge, entering as a supremum (Mironov, 2017; Bun and Steinke, 2016; Dong, Roth and Su, 2022). They also carry a genuine temporal axis: privacy loss epsilon is accounted as it accumulates across composed mechanisms on a query/release-composition clock (Kairouz, Oh and Viswanath, 2015; Dwork, Rothblum and Vadhan, 2010), and continual-observation DP tracks a stream of T published outputs (Dwork, Naor, Pitassi and Rothblum, 2010). Adversary-aware refinements go further and parametrise which fixed adversary class the guarantee is calibrated against (Cummings et al., 2024; Swanberg et al., 2025).

## What differential privacy does NOT do (relative to R(t))

None of these index a fixed, never-re-queried archive's per-subject reconstruction residual to the adversary's informational capability (accumulating linkage corpus, side priors, informedness) growing along a calendar clock while nothing is re-released. Their temporal axis is added queries or releases (k, or stream-length T) against a held-fixed worst-case adversary, which is the inverse polarity to a frozen release aging, and where DP does run a wall clock (age-dependent and temporally-discounted DP; Valavi et al., 2022) the guarantee strengthens as data ages through relevance decay. Adversary capability therefore enters only as a static supremum or a fixed class parameter, never as a variable integrated along calendar time; the one caveat is that this exactness is proven for information-theoretic DP, with computational DP a separate, out-of-scope literature.

## Sub-claim adjudication

- **CTR-LR-02b-i: PARTIAL** (moderate-high) - DP composition and the information-theoretic DP family (RDP/zCDP/GDP/f-DP, advanced/optimal/continual-observation composition) provably run a query/release clock â€” free variable k, adversary held at worst-case sup_C â€” and therefore cannot express a fixed release's reconstruction residual rising with adversary capability over calendar time; R(t) is a distinct clock (free variable calendar-time t through a growing adversary C(t), single frozen release k=1), and no DP work in the searched corpus formalizes it. This distinctness is contingent-on-current-formalization, not categorical-in-principle: computational DP already recognizes (informally) that a fixed release's guarantee erodes as adversary compute grows over calendar time â€” the same mechanism, unformalized â€” and adversary-aware DP bounds (ATTAXONOMY / 2507.08158) already carry adversary capability C as an explicit static parameter, so a calendar-indexed C(t) is a natural, non-foreclosed bridge rather than a mathematical impossibility.

- **CTR-LR-02b-ii: HOLDS** (high) - Within the enumerated DP-refinements strand â€” all information-theoretic (RDP, zCDP/CDP, advanced/optimal/concurrent composition, continual-observation DP, f-DP/GDP, adversary-aware accounting) plus the time-aware DP families (temporal-correlation TPL/ConTPL/CSDP, age-dependent, temporally-discounted, everlasting) â€” no work indexes a fixed release's residual reconstruction/inference risk to adversary-CAPABILITY growth over calendar time. Each runs one of three non-R(t) clocks: (1) composition/query accounting with a fixed worst-case adversary, (2) release-stream length T of inverted polarity with a fixed adversary, or (3) a static adversary prior/baseline-success parameter with no time variable. The temporally-structured members (incl. Cao's TPL) run the stream clock against a fixed adversary; the wall-clock members (age-dependent, temporally-discounted) run relevance/age decay of the OPPOSITE polarity (guarantee strengthens as data ages). The structural reason is exact for this strand: every member is information-theoretic and robust to arbitrary auxiliary knowledge and unbounded compute, so adversary capability enters only as a supremum, never a calendar index. Out-of-scope caveat: computational DP and the crypto harvest-now-decrypt-later framing could in principle carry a capability-growth clock, but they are a different literature already excluded and do not formally index epsilon to calendar time.

- **CTR-LR-02b-iii: PARTIAL** (high) - Over the DP-refinements/DP-markets strand (~40 works surveyed), the joint cell C = A x B x C is empty and no member co-occupies even two of its three axes, where A = an information-theoretic per-subject reconstruction bound on a FIXED (non-growing) archive; B = a Mosca-STRUCTURED calendar-time clock along which the adversary's AUXILIARY/INFORMATIONAL capability (linkage corpus, side priors, informedness â€” NOT computational power, which axis A renders inert and which unbounded-adversary DP already saturates) grows, so the frozen archive's per-subject reconstruction residual rises monotonically with t though nothing is re-released â€” explicitly neither a crypto break-time nor a DP composition/continual-release budget; and C = the residual held and priced as inalienable subject-owned CAPITAL (a stock) rather than a per-query privacy-loss FLOW. The clock distinction is real and exact against every surveyed clock; the contribution survives as novelty only in this narrower, informational-capability form.

## Applied to the draft

- S1 fix: The differential-privacy budget is not adversary-independent; it is calibrated against a worst-case adversary of unbounded computation and arbitrary auxiliary knowledge, which enters the guarantee as a supremum (Mironov, 2017; Bun and Steinke, 2016; Dong, Roth and Su, 2022). What that literature holds fixed is not the adversary but the clock: privacy loss is accounted along a query/release-composition axis, with epsilon degrading as mechanisms are composed (Kairouz, Oh and Viswanath, 2015; Dwork, Rothblum and Vadhan, 2010) or as a stream of T outputs is published under continual observation (Dwork, Naor, Pitassi and Rothblum, 2010), the adversary's capability being held at that worst-case supremum throughout. [Placement: replaces the S1 sentence that currently characterises the DP-markets budget as 'static, adversary-independent', i.e. the positioning sentence that opens the DP-refinements comparison.]

- S2 fix: R(t) runs a different clock. It indexes a single fixed release, never re-queried, whose per-subject reconstruction residual rises as the adversary's informational capability, namely its accumulating linkage corpus and side priors rather than its computational power (which differential privacy already saturates), grows along calendar time. No work in the surveyed DP-refinements strand runs this clock: composition and its RÃ©nyi, concentrated, Gaussian and continual-observation refinements all move along added queries or releases against a fixed worst-case adversary, and the wall-clock DP families, being age-dependent and temporally-discounted DP together with the data-value decay of Valavi et al. (2022), run relevance decay of the opposite polarity in which the guarantee strengthens as data ages. We state this as a clock distinction and not a categorical barrier: adversary-aware DP already carries adversary capability as an explicit static parameter (Cummings et al., 2024; Swanberg et al., 2025) and computational DP already informally recognises that a fixed release erodes as adversary compute grows, so a calendar-indexed capability clock is a natural but as-yet-unformalised extension rather than a mathematical impossibility. [Placement: replaces the S2 sentence that restates 'static, adversary-independent' as the ground for the R(t) distinction, i.e. the contrast sentence that asserts R(t)'s novelty against the strand.]

## Ledger paragraph

LM2 resolved as distinction_holds_but_phrasing_wrong. The DP referee is right that adaptive/RÃ©nyi/concentrated/Gaussian/composition/continual-observation DP model adversaries (a worst-case, unbounded-compute, arbitrary-auxiliary-knowledge adversary entering as a supremum) and carry a temporal axis (privacy loss accounted along query/release composition, or a stream of T releases under continual observation), and adversary-aware DP even parametrises the fixed adversary class; so 'static, adversary-independent' is a genuine mischaracterisation and must be replaced. But the R(t) distinction does not collapse (adjudicated CTR-LR-02b-i PARTIAL, -ii HOLDS, -iii PARTIAL): every strand member runs one of three non-R(t) clocks (composition/query accounting against a fixed worst-case adversary; release-stream length T of inverted polarity; or a static adversary-class parameter with no time variable), and the wall-clock DP families (age-dependent, temporally-discounted, Valavi et al. 2022) run relevance decay of the OPPOSITE polarity in which the guarantee strengthens as data ages. The residue is re-stated as a CLOCK distinction (query/release-composition vs calendar-time adversary capability) and narrowed to the informational-capability reading forced by CTR-LR-02b-iii (accumulating linkage/side priors, not compute, which DP already saturates). Two honesty constraints are carried into the prose: the distinction is current-formalization-contingent, not categorical (computational DP and adversary-aware bounds are non-foreclosed bridges), and every negative claim is scoped to the surveyed DP-refinements strand per D2. S1/S2 drop-in replacements written engaging Mironov 2017, Bun-Steinke 2016, Dong-Roth-Su 2022, Kairouz-Oh-Viswanath 2015, Dwork-Rothblum-Vadhan 2010, Dwork-Naor-Pitassi-Rothblum 2010, Cummings et al. 2024, Swanberg et al. 2025 and Valavi et al. 2022 by author-year. Residual after stress: ~85%, sharper but narrower than the 86% LR-02 figure.

\newpage

# Bibliography: challenge corpus with provenance

## Bibliography (WEIS-submission ready)

Grouped by strand. Every item below carries `provenance_confidence = verified_from_search`. **No item is flagged `uncertain`; no first-person provenance verification is outstanding for this corpus.** Standards items list both the cited edition and its known revision for the First Person to select the citation edition at submission.

### Strand A â€” Propertisation and property rights in personal data (legal)

1. Kenneth C. Laudon, "Markets and Privacy," *Communications of the ACM*, Vol. 39, No. 9 (September 1996), pp. 92-104. https://doi.org/10.1145/234215.234476 (verified_from_search)
2. Pamela Samuelson, "Privacy As Intellectual Property?", 52 *Stanford Law Review* 1125-1173 (2000). https://www.jstor.org/stable/1229511 (verified_from_search)
3. Paul M. Schwartz, "Property, Privacy, and Personal Data," 117 *Harvard Law Review* 2056 (2004). https://papers.ssrn.com/sol3/papers.cfm?abstract_id=721642 (verified_from_search)
4. Nadezhda Purtova, "The illusion of personal data as no one's property," *Law, Innovation and Technology* 7(1) (2015): 83-111; see also N. Purtova, *Property Rights in Personal Data: A European Perspective* (Kluwer Law International, 2011/2012) and "Do Property Rights in Personal Data Make Sense after the Big Data Turn? Individual Control and Transparency" (2017). https://doi.org/10.1080/17579961.2015.1052646 (verified_from_search)
5. J.E.J. (Corien) Prins, "Property and Privacy: European Perspectives and the Commodification of our Identity," in L. Guibault and P.B. Hugenholtz (eds), *The Future of the Public Domain: Identifying the Commons in Information Law* (Information Law Series No. 16, pp. 223-257), Kluwer Law International, 2006. https://papers.ssrn.com/sol3/papers.cfm?abstract_id=929668 (verified_from_search)

### Strand B â€” Data-as-labour and market-structure remedies

6. Imanol Arrieta-Ibarra, Leonard Goff, Diego Jimenez-Hernandez, Jaron Lanier, and E. Glen Weyl, "Should We Treat Data as Labor? Moving beyond 'Free'," *AEA Papers and Proceedings* 108 (2018): 38-42. https://doi.org/10.1257/pandp.20181003 (verified_from_search)
7. Eric A. Posner and E. Glen Weyl, "Data as Labor: Valuing Contributions to the Digital Economy," Chapter 5 in *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*, pp. 205-249, Princeton University Press, 2018. https://doi.org/10.1515/9780691196978-009 (verified_from_search)
8. Sylvie Delacroix and Neil D. Lawrence, "Bottom-up data Trusts: disturbing the 'one size fits all' approach to data governance," *International Data Privacy Law* 9(4) (2019): 236-252. https://doi.org/10.1093/idpl/ipz014 (verified_from_search)

### Strand C â€” Empirical valuation of privacy (WTA/WTP, market surveys)

9. Alessandro Acquisti, Curtis Taylor, and Liad Wagman, "The Economics of Privacy," *Journal of Economic Literature* 54(2) (2016): 442-492. https://doi.org/10.1257/jel.54.2.442 (verified_from_search)
10. Alessandro Acquisti, Leslie K. John, and George Loewenstein, "What Is Privacy Worth?", *The Journal of Legal Studies* 42(2) (2013): 249-274. https://doi.org/10.1086/671754 (verified_from_search)
11. Avinash Collis, Alex Moehring, Ananya Sen, and Alessandro Acquisti, "Information Frictions and Heterogeneity in Valuations of Personal Data," 21st Workshop on the Economics of Information Security (WEIS 2022). Median WTA to share entirety of Facebook data = $750 (YouGov nationally representative sample); $1,000 (Data Dividend Project sample); bimodal distribution clustered below $250 and above $10,000. https://weis2022.econinfosec.org/wp-content/uploads/sites/10/2022/06/weis22-collis.pdf (verified_from_search)
12. Alastair R. Beresford, Dorothea Kuebler, and Soeren Preibusch, "Unwillingness to pay for privacy: A field experiment," *Economics Letters* 117(1) (2012): 25-27. https://doi.org/10.1016/j.econlet.2012.04.077 (verified_from_search)
13. Jens Grossklags and Alessandro Acquisti, "When 25 Cents is Too Much: An Experiment on Willingness-To-Sell and Willingness-To-Protect Personal Information," Sixth Workshop on the Economics of Information Security (WEIS 2007), Carnegie Mellon University, June 2007. https://econinfosec.org/archive/weis2007/papers/66.pdf (verified_from_search)
14. Sarah Spiekermann, Alessandro Acquisti, Rainer Boehme, and Kai-Lung Hui, "The challenges of personal data markets and privacy," *Electronic Markets* 25(2) (2015): 161-167. https://doi.org/10.1007/s12525-015-0191-0 (verified_from_search)

### Strand D â€” Security economics (incentive framing)

15. Ross Anderson, "Why Information Security is Hard - An Economic Perspective," *Proceedings of the 17th Annual Computer Security Applications Conference (ACSAC 2001)*, New Orleans, LA, 10-14 December 2001, pp. 358-365, IEEE Computer Society. https://doi.org/10.1109/ACSAC.2001.991552 (draws on G. Akerlof, "The Market for Lemons," *QJE* 84(3) (1970): 488-500). (verified_from_search)

### Strand E â€” Formal privacy metrics and system properties

16. Cynthia Dwork, "Differential Privacy," in *Automata, Languages and Programming (ICALP 2006)*, Part II, LNCS vol. 4052, pp. 1-12, Springer, 2006. https://doi.org/10.1007/11787006_1 (verified_from_search)
17. Latanya Sweeney, "k-Anonymity: A Model for Protecting Privacy," *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems* 10(5) (2002): 557-570. https://doi.org/10.1142/S0218488502001648 (verified_from_search)
18. Geoffrey Smith, "On the Foundations of Quantitative Information Flow," in *Foundations of Software Science and Computational Structures (FOSSACS 2009)*, LNCS vol. 5504, pp. 288-302, Springer, 2009. https://doi.org/10.1007/978-3-642-00596-1_21 (verified_from_search)

### Strand F â€” Standards (process and framework)

19. ISO/IEC 29134:2017, *Information technology - Security techniques - Guidelines for privacy impact assessment*, 1st ed., ISO/IEC, Geneva, 2017 (revised by ISO/IEC 29134:2023). https://www.iso.org/standard/62289.html (verified_from_search). First-person note: select 2017 or 2023 edition at submission.
20. ISO/IEC 29100:2011, *Information technology - Security techniques - Privacy framework*, ISO/IEC (second edition ISO/IEC 29100:2024). https://www.iso.org/standard/45123.html (verified_from_search). First-person note: select 2011 or 2024 edition at submission.

### External works cited in adjudication (not in the 20-item corpus, listed for the reference apparatus)

These were surfaced by the adjudicators' web scope and are load-bearing for the MIRAGE verdicts; the First Person may wish to cite them in the related-work section. Provenance: adjudicator web scope, July 2026, not independently re-verified here (flag for first-person verification before citation).

- Arpita Ghosh and Aaron Roth, "Selling Privacy at Auction," EC 2011 (DP-markets strand; occupant of the {system_property x market_pricing} cell). Verification pending.
- Dinesh Bergemann, Alessandro Bonatti, and Tan Gan, "The Economics of Social Data," RAND Journal of Economics, 2022 (aggregator surplus capture, social-data externality). Verification pending.
- Patrick Bajari, Victor Chernozhukov, Ali Hortacsu, and Junichi Suzuki, "The Impact of Big Data on Firm Performance," AEA P&P, 2019 (flat returns-to-scale evidence). Verification pending.
- Ben Wagner and Eerke Boiten, "Privacy Risk Assessment: From Art to Science, By Metrics," DPM 2018 (PIA-to-metric transition). Verification pending.
- Irit Dinur and Kobbi Nissim, "Revealing Information while Preserving Privacy," PODS 2003 (per-record reconstruction threshold). Verification pending.
- Michele Mosca, cryptographic shelf-life inequality (X + Y > Z) and harvest-now-decrypt-later threat model (IEEE S&P 2018; FEDS 2025-093). Verification pending.
- IEEE 7012 / Customer Terms (MyTerms), ProjectVRM / Doc Searls, myterms.info (proposer-inversion standard). Verification pending.