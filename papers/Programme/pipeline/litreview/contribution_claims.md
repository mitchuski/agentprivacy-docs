---
artefact: litreview-runtime-output
runtime: weis-litreview-runtime
run_id: wf_ba400906-67b
brief: chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md
target: WP-14 (weis_seventh_capital, WEIS 2027)
date: 2026-07-15
register: standards
generated: true
note: "Generated artifact. Do not hand-edit; fix the runtime inputs and rebuild. Verdict spread: 0 VALIDATED / 5 MIRAGE / 0 BLOCKED across 5 candidates, 20-item corpus. CTR-series IDs are candidates only; assignment is the First Person's."
---

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
