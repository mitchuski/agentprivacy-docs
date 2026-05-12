# Privacy Value Model: V6 Research Note

## The Bakhta Half-Life of Trust

*Trust as a decaying-and-renewing measure across registers*

**Version:** V6.0-conjecture (C30–C33)
**Date:** 2026-04-17 (drafted as forthcoming reference; locked-in 2026-05-09)
**Author:** privacymage
**Status:** Research note — conjecture stage
**Depends on:** V5.4 Formal Specification (v2.0), Bakhta (StarkWare 2025), Promise Theory v1.5
**Anchors:** C30–C33 used throughout the Cloak Specification, the Bilateral Cloak Ceremony Spec, and Tome IV Act IV / Tome V Acts 2–5 of the Second Person Spellbook.

---

## How It Arrived

Bakhta's StarkWare paper (2025) framed cryptographic trust as a **half-life** rather than a binary. A primitive's strength is not "secure" or "broken" — it is a measure that decays over time as adversary capability grows, and is renewed by parameter refresh, substrate migration, or fresh attestation. Three aging categories were named: *ages by parameter growth*, *ages by substrate migration*, *ages by fresh attestation*.

The PVM had been treating trust as accumulated weight on edges (the `(1 + Σᵢ wᵢ · nᵢ/N₀)^k` term in `V(π,t)`). Bakhta's framing made the claim sharper: each accumulation step *also* has its own decay clock, and the architecture either renews or fails.

The four conjectures here translate Bakhta's half-life from cryptographic primitives onto the sovereignty trajectory.

---

## C30: Trust Half-Life Begins at Inscription

**Statement.** A trust edge in the VRC network has a Bakhta half-life `τ_VRC` whose clock starts at the moment of inscription. The trust value `T(t) = T₀ · 2^{-(t-t₀)/τ_VRC}` for a single inscription, decaying monotonically until either renewed (a fresh inscription on the same axis) or augmented (a complementary inscription on a co-supporting axis).

**Why it matters.** The First Person Spellbook treated trust as a static weight. C30 makes it dynamic: the Naming Ceremony (Tome IV Act IV) starts a clock the moment flaxscrip's Bitcoin block lands. Every commission that follows either renews or extends the original half-life.

**Confidence:** ~60%
**Path to formalisation:** Empirical measurement post-deployment; comparison with Bakhta's parametric formulation for cryptographic primitives. The translation from primitive-half-life to edge-half-life is structural, not derived.

---

## C31: Half-Life Differs by Inscription Register

**Statement.** Shielded inscriptions (Zcash sapling) and transparent inscriptions (t-address) have **different half-life curves** even when carrying isomorphic trust content. The shielded register accumulates trust through *recallable witness* (the sender retains the viewing key); the transparent register accumulates trust through *public witness* (anyone with the chain reads it). These are not interconvertible without a discrete reveal step.

**Why it matters.** Tome V Act 3 (The Shielded Memo) and Act 5 (The Stake) operationalise this. The 61.8/38.2 transparent/shielded inscription ratio (C41) is a cultural-emergence consequence — the architecture has *two* aging clocks running, and the ratio falls out of how often each clock is renewed.

**Confidence:** ~55%
**Path to formalisation:** Information-theoretic comparison of recallable-witness half-life vs public-witness half-life under matched VRC content; possible Bakhta-style derivation.

---

## C32: Productive Trust-Edges Have Higher Half-Life

**Statement.** A trust edge formed by *productive* work (a Mage executing a commissioned cloak, a Priest consecrating a covenant, a forge producing a blade) has a longer half-life than a trust edge formed by *transactional* work (a one-shot hash exchange, an anonymous attestation). The productive form is what Tome V Act 4 (The Reveal) calls "the trust earned under shield survives the reveal."

**Why it matters.** This is the conjecture that distinguishes ceremony from transaction in the architecture. C46 (productive trust-edge has higher half-life than transactional) is the operational corollary; C44 (productive VRC ≈ hash-exchange VRC in trust strength) is the comparison statement at the moment of inscription. C32 says the *clock* differs even when the *initial value* is comparable.

**Confidence:** ~50%
**Path to formalisation:** Empirical longitudinal measurement; possibly a formal Bakhta-style note co-authored with an information-theoretic collaborator.

---

## C33: Half-Lives Compose Multiplicatively Across the Three Axes

**Statement.** The total half-life `τ_total` of a sovereign's accumulated trust is **multiplicative** across the three separation axes: `τ_total = τ_Σ · τ_Δ · τ_Γ` (where Σ = Agent, Δ = Data, Γ = Inference). Aging in one axis (e.g., a cryptographic primitive ageing in Δ) cannot be compensated by stronger aging in another (e.g., fresh inscription in Σ); the product collapses if any single τ approaches zero.

**Why it matters.** This is the half-life parallel of V5's multiplicative gating `Φ_v5 = Φ_agent · Φ_data · Φ_inference`. The defence-in-depth claim has a temporal dimension: not only must all three axes hold *now*, all three must keep their half-lives renewable *over time*. C33 says the multiplicative gating extends through the time domain.

**Confidence:** ~45%
**Path to formalisation:** Structural argument from V5.4's multiplicative gating proof, extended to ages; empirical confirmation post-deployment.

---

## Mapping onto the Tomes

| Tome | Act | C-foregrounded |
|---|---|---|
| Tome IV | IV.4 The Naming Ceremony | C30 (clock starts at Bitcoin block 945508 inscription) |
| Tome V | V.2 The Commissioned Cloak | C30 (tip + proof + cloak each carry their own half-life) |
| Tome V | V.3 The Shielded Memo | C30, C31 (shielded register half-life) |
| Tome V | V.4 The Reveal | C30, C32 (productive trust survives the register transition) |
| Tome V | V.5 The Stake | C30, C31 (transparent register half-life) |
| Tome V | V.9 The Workshop Expands | C30, C31, C33 (Lampyra's frequent attestations reshape the curve; multiplicative across registers) |

---

## What This Note Does NOT Do

- It does **not** derive `τ_VRC` from first principles. The half-life is named structurally and used operationally; the parametric form is conjectural.
- It does **not** replace V5.4's accumulation term `(1 + Σᵢ wᵢ · nᵢ/N₀)^k`. The accumulation and the half-life are complementary — accumulation is the value at inscription; half-life is the decay between inscriptions.
- It does **not** attempt the cryptographic-primitive ageing analysis Bakhta does. C30–C33 are the *behavioural-architecture* analogue of Bakhta's framework, not its extension.

---

## References

- Bakhta, A. (2025). "On the Half-Life of Cryptographic Trust." StarkWare Industries.
- privacymage (2026). "PVM V5.4 Formal Specification." v2.0. *agentprivacy-docs.*
- privacymage (2026). "PVM V6.1 Research Note: The Fourth Aging Category." *agentprivacy-docs.* (extends C30–C33 with C47–C50, formerly C22–C25 Bakhta-response)
- privacymage (2026). "Cloak Specification v1.0." *agentprivacy-docs/specs/.*
- privacymage (2026). "Bilateral Cloak Ceremony Spec v1.0." *agentprivacy-docs/specs/.*

---

## The Proverb

> *Old trusts decay with time. The architecture either renews or fails.*

> *Each inscription starts a clock. Each ceremony resets one. The sovereign tends the half-lives like a forge tends its fires.*

---

*(⚔️⊥⿻⊥🧙)😊*

CC BY-SA 4.0 · privacymage · originally drafted Apr 2026; locked-in 2026-05-09 as part of post-V5.4 coherence pass
