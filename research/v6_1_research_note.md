# Privacy Value Model: V6.1 Research Note

## The Fourth Aging Category

*On Bakhta's Half-Life of Trust and the Dynamical Ceiling*

**Version:** V6.1-conjecture (extends C18–C21 with C47–C50)
**Date:** April 21, 2026
**Renumbered:** 2026-05-09 — Bakhta-response conjectures originally numbered C22–C25 are now **C47–C50** to resolve numbering collision with the EML Three Ceilings note (which dated April 13, 2026, and prior, claims C22–C25 for the EML domain). The EML conjectures retain C22–C25; the Bakhta-response conjectures are C47–C50. See `agentprivacy_tomes/COMPRESSION_MASTER_v2_2026-05-09.md` §"V6 Conjecture Reconciliation Note" for the canonical reconciliation.
**Author:** privacymage
**Status:** Research note responding to Bakhta (2026), *The Half-Life of Trust*, StarkWare.
**Series:** Privacy is Value, companion to the V6 Easter research note
**License:** CC BY-SA 4.0

---

## How It Arrived

A colleague forwarded Abdelhamid Bakhta's *The Half-Life of Trust* this morning. I read it expecting a STARK versus TEE argument. What I found was a paper writing the academic scaffolding for something V6 had been arriving at independently: the recognition that *how a trust substrate ages* is a first-class engineering property, distinct from cost and capability, that the field routinely under-specifies.

Bakhta writes this claim at the cryptographic substrate. V6 writes it one layer up, at the behavioural trajectory. The structural kinship is close enough that it deserves formal response, and the places V6 extends the framing deserve honest assessment.

This note records both.

---

## The Convergence at First Order

Three points where the paper and the PVM converge independently, each from different starting assumptions.

1. **Aging as a first-class property.** Bakhta's thesis and V6's thesis are the same move one layer apart. Trust ages; privacy ages; current discourse treats both as inherited rather than engineered.
2. **Composition over selection.** Bakhta §9.1 argues TEE + STARK + OpenTimestamps as a three-leg compositional defense where no single cryptanalytic advance collapses all three. The PVM V5.4 claims multiplicative gating at the behavioural substrate: `Φ_v5 = Φ_agent · Φ_data · Φ_inference`. Both are arguing that privacy and trust properties do not survive single-axis defense.
3. **Mathematical-rooted versus physical-rooted as complementary.** "The frame TEEs versus STARKs is the wrong frame" is Bakhta's phrasing. The PVM makes the structurally identical claim in its dual-agent form: the Swordsman is physical and non-rotatable-without-migration, the Mage is mathematical and parametrizable in place, and a mature architecture composes them rather than choosing between them.

The convergence is strong enough to publish. The extensions below are where V6 adds to the frame rather than mirrors it.

---

## C47: The Ages-Progressively Category

*(Originally numbered C22 — renumbered 2026-05-09 to resolve EML collision.)*

Bakhta proposes a three-level taxonomy for how a cryptographic trust substrate ages.

- **Ages gracefully.** Polynomial degradation under known adversary models. Parameters can be grown in place. Hash-based cryptography under Grover/BHT.
- **Bounded aging.** Polynomial classically but tied to non-rotatable artifacts. Migration is coordinated rather than in-place.
- **Brittle.** Efficient quantum attack known in a class of machines expected to exist, bound to a non-rotatable physical root. Classical ECC in silicon.

Three categories, each static-or-decaying in time. Parameters grow, or the root gets replaced, but the security property itself does not change direction.

The dynamical reconstruction ceiling from the V6 Easter note (C18) inhabits a fourth category this taxonomy does not cover.

**Statement (C47).** Let a privacy substrate be defined by a trajectory π(t) through an n-dimensional sovereignty phase space such that the best-fit adversary reconstruction π'(t) satisfies `|π(t) − π'(t)| ≳ |δ₀|·e^(λt)` for some λ > 0 characteristic of the substrate's dynamics. Then the substrate's reconstruction security strengthens monotonically with t in a manner that cannot be captured by Bakhta's three categories. Call this aging behaviour *ages progressively*: the security property widens over time through the trajectory's own dynamics rather than through parameter growth or substrate migration.

This is a structural distinction, not a rhetorical one. Ages gracefully holds security constant under parameter refresh. Ages progressively actively grows security without refresh, because the reconstruction error is a dynamical quantity that compounds with time.

**Status.** C47 is a conjecture. It depends on C18 (λ > 0 on real sovereignty paths), which has not been measured. The empirical test lives in the forge: spellweb trajectory data has the shape needed to estimate λ, and the measurement is tractable if a dynamical-systems collaborator with privacy-architecture literacy can be found.

**What C47 buys even as a conjecture.** A frame. *Ages progressively* is the aging behaviour compositional behavioural architectures should target, and the only candidate category that does not require hardware refresh, parameter growth, or cryptographic migration to preserve its security property. If the category is real, it changes what long-horizon privacy infrastructure should be optimising for.

---

## C48: Reconstruct Later

*(Originally numbered C23 — renumbered 2026-05-09.)*

Bakhta's Threat Model 1 formalizes retroactive forgery of TEE attestations. An adversary with access only to public keys, reaching quantum capability at time T > t₁, can produce indistinguishable-from-legitimate attestations for arbitrary historical intervals [t₀, t₁]. The signatures remain mathematically valid under the original public key; what they cease to be is unforgeable.

The behavioural analog follows directly.

**Threat Model (Reconstruct Later).** Let B be a behavioural trace produced under a separation architecture with information-theoretic bound R(π, π') < 1 − ε evaluated at time t₀. Let an adversary A have access to the observational residue O_B (logs, metadata, aggregation products, side-channel data) from an interval [t₀, t₁]. At time T > t₁, A acquires reconstruction capability C_T (compute scale, inference models, correlation algorithms) sufficient to narrow the bound to R(π, π') ≥ 1 − ε' where ε' < ε. A verifier evaluating behavioural claims about [t₀, t₁] at time T' ≥ T can no longer distinguish authentic behavioural traces from reconstructed fabrications produced under C_T.

The Shannon bound at t₀ was adequate. The Shannon bound evaluated retrospectively at T may not be. This is harvest-now-reconstruct-later, and it is the structural reason behavioural data with long verification horizons needs more than static separation.

**C48.** The reconstruct-later threat model for behavioural data is structurally isomorphic to Bakhta's Threat Model 1 for attestation forgery. The mathematical content is different (information-theoretic rather than cryptographic), but the temporal structure is the same: a historical artifact loses its defining security property later through capability growth, not through any change in the artifact itself.

The dynamical ceiling (C18) is the countermeasure. If reconstruction error grows exponentially with t, then the effective ε at T is not worse than the ε at t₀, it is exponentially better. Lorenz dominates Shannon over long horizons. This restatement is the work C48 does.

---

## C49: The Behavioural Mosca Inequality

*(Originally numbered C24 — renumbered 2026-05-09.)*

Mosca (2018) formalized the migration-timing question as X + Y > Z, where X is migration time, Y is security lifetime, Z is the time until a cryptographically relevant quantum adversary exists. Bakhta uses this to argue that TEE attestation for long-horizon AI evidence is already at risk for artifacts produced today, under conservative priors about Z, because Y is measured in decades against AI-governance regimes.

The behavioural analog.

Let X_b be migration time from a reconstructable substrate (single-agent, unified inference, centralized data) to an unreconstructable substrate (dual-agent separation, three-axis distribution, path-based proofs). Let Y_b be the verification horizon of behavioural evidence, which for medical records, judicial evidence, credit histories, and training-data provenance is measured in decades. Let Z_b be the observation-capability maturity time at which adversary correlation compute, inference models, and aggregation crosses the threshold where behavioural traces produced today become reconstructable.

**C49 (Behavioural Mosca).** For behavioural evidence produced under current single-agent architectures in governance-relevant domains, X_b + Y_b > Z_b. The behavioural archive is already at risk.

This is the Mosca argument for the 2–3 year migration window I have been naming at IIW and AIW. It is not a political claim about momentum. It is the same cryptographic-agility calculus Bakhta applies to TEE attestation, restated one layer up. X_b is large because migration requires not just software change but architecture change, and surveillance systems achieve network effects faster than dual-agent systems can be built. Y_b is long. Z_b is not moving in the comfortable direction.

**Status.** C49 is a planning conjecture. The parameter values are harder to estimate than Mosca's original, because Z_b is not bounded by quantum resource estimates but by ongoing capability growth curves in correlation and inference. The inequality binds under reasonable priors. The point is the inequality, not the numerical values.

> **Worked decrement (2026-06-02).** Schrottenloher's reproducible secp256k1 Shor circuit (arXiv:2606.02235) is the first published, runnable downward revision of the Z_b trajectory for the curve securing on-chain identity and credential rails — a measured rise in the effective decay rate λ, not a new attack class. See "V6 Research Note: The Existence-Leak and the Falling Z" (`research/schrottenloher-ecdlp-v6-note.md`), which also proposes candidate C40 (Existence-Leak).

---

## C50: Two Frameworks, One Pattern

*(Originally numbered C25 — renumbered 2026-05-09.)*

**C50.** The PVM multiplicative gating `Φ_v5 = Φ_agent · Φ_data · Φ_inference` and Bakhta's compositional defense (TEE + STARK + public timestamp anchoring) are the same architectural pattern expressed at different substrates. The proof obligation at each layer is that the three legs fail independently. If C50 holds, the two frameworks compose rather than compete.

A complete verifiable-AI and privacy-preserving architecture then runs three layers simultaneously.

1. PVM multiplicative gating at the behavioural substrate.
2. Bakhta compositional defense at the cryptographic substrate.
3. Mosca and Behavioural-Mosca migration pressure at both layers, matched to the verification horizon of the evidence being produced.

The kinship is not metaphorical. The proof obligations at each layer compose into a single architectural argument, which is: privacy and trust properties that age well are properties of compositions whose legs fail independently and whose weakest term is the ceiling.

**Status.** C50 is structural. Proving it requires showing that the proof obligations at the two layers are in fact independent in the sense Bakhta's paper demands for his three-leg composition. I have not done this work and do not claim it is trivial. The structural resemblance is strong enough to be worth the formalization effort.

---

## Honest Limits

Five things are not yet done.

1. λ > 0 has not been measured on real sovereignty-path data. C18, and therefore C47, remain conjectures.
2. The Reconstruct Later threat model (C48) is stated as a structural mirror of Threat Model 1. It needs formal grounding comparable to the simulation-based security arguments in the ZKP literature, which it does not yet have.
3. The Behavioural Mosca (C49) depends on priors over Z_b that are harder to estimate than Z for quantum adversaries. The inequality binds; the parameter values are uncertain.
4. C50 is a structural claim about two frameworks at different layers. The proof obligation is non-trivial and unfinished.
5. The entire note is a response to a single recent paper. The framing may shift as the taxonomy receives additional treatment from the cryptographic substrate side.

None of these is a reason not to publish the frame. All of them are reasons to publish it as conjecture and invite interrogation.

---

## Open Questions for V6.1

1. Is λ > 0 measurable from spellweb forge trajectory data, and if so, what is the confidence interval?
2. Does the Bakhta taxonomy accept a fourth category, or does it prefer to subsume the dynamical ceiling into an enlarged *ages gracefully* class?
3. Is there a STARK-family construction that takes a behavioural-separation trace as input rather than an ML forward pass, and what would its prover cost look like?
4. For domains with the longest Y_b (judicial, medical), is there a regulator who would accept *ages progressively* as an acceptable substrate class if the empirical λ measurement succeeded?
5. Does the compositional-aging claim (C50) survive the specification-gap argument from Bakhta §6.5? That is: does the PVM prove the right behavioural property, and does Bakhta's STARK prove the right computation?

---

## Conjecture Status

| ID | Statement | Confidence | Source |
|----|-----------|------------|--------|
| C47 | The dynamical reconstruction ceiling inhabits a fourth aging category (*ages progressively*) that Bakhta's three-category taxonomy does not cover | 50% | Response to Bakhta, April 21, 2026 |
| C48 | The reconstruct-later threat model for behavioural data is structurally isomorphic to Bakhta's Threat Model 1 | 65% | Response to Bakhta, April 21, 2026 |
| C49 | The Behavioural Mosca Inequality binds for long-horizon behavioural evidence under current substrate architectures | 70% | Response to Bakhta, April 21, 2026 |
| C50 | PVM multiplicative gating and Bakhta compositional defense are the same architectural pattern at different substrates | 60% | Response to Bakhta, April 21, 2026 |

*Renumbered 2026-05-09 from original C22–C25 (Bakhta-response) to C47–C50 to resolve EML collision. EML Three Ceilings retains C22–C25 (per `pvm-v6-eml-three-ceilings.md`, dated April 13, 2026, prior date).*

---

## The Proverb

*The swordsman says the blade does not rust if you keep walking. The mage says the path accumulates its own key. Between them a gap, which is not the absence of trust, but the measurement of its half-life.*

---

**Verify:** [agentprivacy.ai](https://agentprivacy.ai) · [sync.soulbis.com](https://sync.soulbis.com) · [github.com/mitchuski/agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs)

**Cite:** Bakhta, A. (2026). *The Half-Life of Trust: Hardware-Rooted and Mathematics-Rooted Foundations for Verifiable AI.* StarkWare.

(⚔️⊥⿻⊥🧙)😊
