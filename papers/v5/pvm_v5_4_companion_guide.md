# Privacy Value Model: Companion Guide

**The Mage's Reading**

**Version:** 2.0 (aligned to PVM V5.4 Formal Specification v2.0)
**Date:** April 10, 2026
**Author:** privacymage
**Contact:** mage@agentprivacy.ai
**License:** CC BY-SA 4.0
**Purpose:** Bridge the mathematical specification to the full agentprivacy vision

---

## How to Read These Documents

The formal specification and this companion are two readings of the same work.

The **Formal Specification** (⚔️ Swordsman reading) presents the mathematics: equations, proofs, bounds, conjectures with explicit confidence levels. It answers WHAT the model is. It draws boundaries.

This **Companion Guide** (🧙 Mage reading) presents the context: motivation, implementation, narrative, standards, economics. It answers WHY the model matters. It projects outward.

Neither is complete without the other. The gap between them — the ⊥ — is where understanding lives.

| If you want... | Start with... |
|----------------|---------------|
| The equations | Formal Spec §1–§11 |
| The algebra | Formal Spec §12 |
| The ceremonies | Formal Spec §13–§15, then this guide §6 |
| The economic case | This guide §4 |
| The narrative | This guide §7 |
| The standards | This guide §5 |
| The agents explained | This guide §2 |

---

## 1. The Mission the Math Serves

### 1.1 The 7th Capital

**Formal Spec gap:** The specification never states WHY privacy has value.

**The Thesis:** There are seven forms of capital:

| # | Capital | Traditional View |
|---|---------|------------------|
| 1 | Financial | Money, credit, investments |
| 2 | Manufactured | Infrastructure, tools, machines |
| 3 | Intellectual | Patents, copyrights, trade secrets |
| 4 | Human | Skills, knowledge, health |
| 5 | Social | Networks, trust, relationships |
| 6 | Natural | Resources, ecosystems, land |
| **7** | **Behavioural** | **Patterns, preferences, predictions** |

Behavioural capital is being extracted at scale. Every click, scroll, pause, and purchase generates data that platforms convert into predictive models sold not to serve you but to modify your behaviour for others' benefit.

**The Inversion:** When behavioural capital stays with the person who generates it (the First Person), the entire economic structure inverts. Privacy isn't about hiding — it's about ownership. The spec's equation $V(\pi, t)$ measures the value that SHOULD accrue to the First Person.

The spec's multiplicative gating (§1.3) formalises this: if any single axis of privacy collapses, the ENTIRE value collapses. There are no partial victories.

**Deep dive:** `what-agentprivacy-is.md`

### 1.2 The Window

**Formal Spec gap:** No urgency context.

Surveillance architectures are approaching lock-in. Within 2–3 years, behavioural prediction models become infrastructure, regulatory capture solidifies platform positions, and alternative architectures become economically unviable.

Promise Theory insight: surveillance systems use the *attack pattern* — imposing data extraction without prior consent. Privacy infrastructure must establish the *invitation pattern* — acceptance relationships before specific proposals. This architectural choice cannot be retrofitted.

The spec is not academic. It's a race condition.

**Deep dive:** `README.md` (Critical Window), `research_proposal_v2_0.md`

---

## 2. The Agents Behind the Algebra

### 2.1 Swordsman and Mage

**Formal Spec reference:** §4.2 (Φ_agent), §12.2 (neg/bnot), §13 (operational cycle), §14 (amnesia)

| Agent | Symbol | Domain | Function | Operation |
|-------|--------|--------|----------|-----------|
| **Swordsman** | ⚔️ | Protection | Sets boundaries, says "no", guards the threshold | neg(x) = 64 − x |
| **Mage** | 🧙 | Delegation | Projects outward, acts in the world on your behalf | bnot(x) = 63 − x |
| **First Person** | 😊 | Sovereignty | Authorises both, owns the path | succ(x) = neg(bnot(x)) |

The Swordsman never delegates. The Mage never protects. This is the guarantee — when the functions are separated into different agents, neither can be coerced into the other's domain.

**The Gap (⿻):** The irreducible separation between them. The spec's Φ_agent measures this gap. When Φ_agent → 0, the agents collapse into one, and privacy fails. The dihedral group D₆₄ (§12.5) gives this algebraic structure — two involutions that must remain independent for the full group to be accessible.

**The Amnesia Protocol (§14):** The Swordsman and Mage don't just operate separately — they are structurally unable to recover shared origin. This is not a policy ("don't share data"). It is topology ("cannot share memory"). Extension process boundaries enforce this: separate processes = separate memory = structural amnesia.

The cosmological precedent: the Moon cannot recover the Theia impact from its geological state. The tides prove the relationship without disclosing the origin. This is **Selene's Proof** — zero-knowledge by physics, not by policy.

**Betweenness centrality (⿻):** The Gap is not empty — it is the node with highest betweenness centrality in the trust graph (Brandes, 2001). The value lives in the gap because the most paths cross there.

**Deep dive:** `swordsman_mage_whitepaper_v6_0.md`, extension whitepapers

### 2.2 Generator and Solver

**Formal Spec reference:** §4.4 (Φ_inference)

From BRAID (Bounded Reasoning for Autonomous Inference and Decisions):

| Role | Function | Promise |
|------|----------|---------|
| **Generator** | Proposes reasoning graphs, suggests paths | "I will structure the question fairly" |
| **Solver** | Executes reasoning graphs, validates answers | "I will compute the answer honestly" |

When the same model does both, it can manipulate its own reasoning. When separated, the Solver can only execute what the Generator proposed. The spec's Φ_inference = 1 − I(model ; executor) measures this separation.

**Deep dive:** `dualprivacy_researchpaper_v4_0.md` (§4)

---

## 3. Promise Theory: The Semantic Foundation

### 3.1 Why Promises Matter

**Formal Spec reference:** §22

Promise Theory (Bergstra & Burgess, 2019) provides the semantic foundation. A promise is voluntary, unilateral, and observable. Traditional architectures assume control: "The server WILL do X." Promise architectures assume autonomy: "The server PROMISES to do X, and here's how you verify."

The autonomy axiom — *an agent can only make promises about its own behaviour* — formally explains why single agents fail at the privacy-delegation paradox. Attempting to promise both protection and delegation exceeds autonomous capability.

### 3.2 How Promises Map to the Spec

| Spec Term | Promise Interpretation |
|-----------|----------------------|
| P (Privacy Strength) | Quality of the promise that data won't leak |
| C (Credential Verifiability) | Ability to verify a promise was kept without seeing content |
| Φ_agent | Separation of protection promises from delegation promises |
| Φ_data | No single provider can break the data promise alone |
| Φ_inference | Reasoning promises kept separate from execution promises |
| VRC | Bilateral promise bundle between two First Persons |
| T_∫(π) | Accumulated value of promises kept along a path |
| R(d, c, ρ) | How hard it is to break the promise retrospectively |
| The Gap (⿻) | Irreducible promise of the superagent — owned by neither agent |

**Deep dive:** `promise_theory_reference_v1_4.md`

---

## 4. Economic Architecture: VRCs and Guilds

### 4.1 Verifiable Relationship Credentials (VRCs)

**Formal Spec reference:** §19 (Three Identity Layers)

A VRC is a bilateral commitment between two First Persons — cryptographically verifiable without revealing relationship content, relationship-scoped (dies when the relationship ends).

| Old Model | VRC Model |
|-----------|-----------|
| Platform owns the social graph | First Persons own their edges |
| Relationships are platform assets | Relationships are bilateral property |
| Exit means losing connections | Exit means taking your edges with you |

No platform can hold relationships hostage. Switching costs collapse to zero. Network effects accrue to people, not platforms.

**Economic parameters:**

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Ceremony | 1 ZEC (~$500) | One-time genesis of agent pair |
| Signal | 0.01 ZEC (~$5) | Ongoing proof of comprehension |
| Fee split | 61.8% transparent / 38.2% shielded | φ-derived constant |

**Deep dive:** `vrc_promise_protocol_v3_3.md`

### 4.2 Guild Efficiency

**Formal Spec reference:** §6

A guild is a group of agents sharing a reasoning library (shared-parent pattern). Members coordinate at O(1) cost instead of O(N²). The spec's G(guilds) = 1 + guild_efficiency captures the multiplier.

**Trust Tier Progression:**

| Tier | Signals | Capabilities | Trust Value |
|------|---------|-------------|-------------|
| Blade 🗡️ | 0–50 | Basic participation, learning | 0.0–0.2 |
| Light 🛡️ | 50–150 | Multi-site coordination | 0.2–0.5 |
| Heavy ⚔️ | 150–500 | Template creation, governance | 0.5–0.8 |
| Dragon 🐉 | 500+ | Guardian eligibility, unlimited VRCs | 0.8–1.0 |

**Deep dive:** `vrc_promise_protocol_v3_3.md` (§3)

---

## 5. Standards Integration

### 5.1 IEEE 7012-2025 (MyTerms)

**Formal Spec gap:** Not mentioned in the spec (correctly — it's implementation, not mathematics).

IEEE 7012-2025 provides machine-readable privacy terms. Instead of humans reading Terms of Service, agents read MyTerms and negotiate automatically. The Swordsman evaluates MyTerms against your preferences. Negotiation happens in milliseconds.

### 5.2 Identity Stack

**Formal Spec reference:** §19 (Three Identity Layers)

| Layer | Spec Symbol | Standard | Implementation |
|-------|-------------|----------|---------------|
| Data | GUID | Content addressing | SHA-256 hash of content |
| Relationship | VRC | W3C VCs / DIDs | Bilateral promise bundles |
| Principal | DID | W3C DID | Self-sovereign identity |

Additional standards: ERC-8004 (trustless agent identity), ERC-7812 (ZK identity commitments), Trust Spanning Protocol (TSP) for agent-to-agent messaging.

### 5.3 Post-Quantum Context

**Formal Spec reference:** §16 (Proven Results — ring algebra), references

The stored-secret model (2D algebraic space, e.g. secp256k1) is vulnerable to quantum attack. The behavioural manifold proof (6D sovereignty space) has no secret to solve — only a path to walk. Canonical post-quantum recommendation: ML-KEM (Kyber) for key encapsulation, ML-DSA (Dilithium) for signatures. Hybrid constructions (Kyber512-X25519) as transitional.

The bilateral witness ceremony (C13, 65% confidence) is a candidate quantum-resistant primitive: proof of comprehension, not possession.

**Deep dive:** Google Quantum AI (Babbush et al., 2026), `understanding_as_key_zypher_paper_v1.md`

---

## 6. The Ceremonies

### 6.1 What Ceremonies Are

**Formal Spec reference:** §13 (operational cycle), §15 (ceremony implementation)

Privacy isn't just computed — it's performed. A ceremony is a structured interaction that produces a verifiable outcome. The Celestial Ceremony maps the operational cycle (§13) to two people:

| Phase | Symbol | Spec Operation | Human Meaning |
|-------|--------|----------------|---------------|
| Sun | ☀️ | id(x) | Disclosure — you speak your poem |
| Gap | ⊥ | neg(x) | Silence — boundary negotiation |
| Moon | 🌑 | bnot(neg(x)) | Reflection — shared understanding |
| Return | ↻ | succ(x) | Recursion — carry forward or close |

Cryptography provides guarantees. Ceremony provides meaning.

### 6.2 The Blade Forge

**Formal Spec reference:** §15.3 (forge cryptography), §15.5 (moon phases), §15.6 (tier classification)

Forging a blade:
1. Select a constellation (six sovereignty dimensions → spectrum)
2. Walk the nodes (traverse the lattice → accumulate laps)
3. Create the hash (SHA-256 commitment → content addressing)
4. Sign with your key (Ed25519 binding → identity)

The spec's behavioural density ρ (§5.3) captures why two blades with identical constellations but different lap counts have qualitatively different reconstruction resistance. The Universe Blade (62 laps, 2,170s) vs Hitchhiker's Blade (13 laps, 433s) — same hash position, different proof depth.

**Deep dive:** `zk_swordsman_blade_forge_v3_0.md`

---

## 7. The Narrative Layer

### 7.1 Three Expressions, One Architecture

Every concept has three simultaneous expressions:

| Expression | Document Type | Purpose |
|------------|--------------|---------|
| **Mathematical** | Formal Spec | Verification — can it be proven? |
| **Architectural** | Whitepapers | Implementation — can it be built? |
| **Narrative** | Grimoires + Blog | Transmission — can it be understood? |

The grimoires tell the same truths in story form. The math proves what the stories teach. The whitepapers show what the math demands.

### 7.2 The Five Grimoires

| Grimoire | Focus | Entry Point |
|----------|-------|-------------|
| **The First Person Spellbook** | The complete 31-act journey (CLOSED) | First-time readers |
| **The Zero Knowledge Spellbook** | ZK proofs as narrative — cryptography as story | Cryptographers seeking intuition |
| **The Canon Spellbook** | Canonical formulations, axioms, principles | Researchers, architects |
| **The Parallel Society Spellbook** | Alternative social structures, governance | Political theorists |
| **The Plurality Spellbook** | Many-to-many relationships, ⿻ overlap | Network thinkers |

The **PrivacyMage JSON** (v10.0.0) is the grimoire as compression — the entire architecture encoded as structured data. Not a sixth grimoire but the grimoire's holographic boundary: the surface that encodes the volume.

### 7.3 The Blog Series: Privacy is Value V5

| Part | Title | Spec Connection |
|------|-------|-----------------|
| 0 | The Myth Before the Math | Why the equation exists |
| 1 | Forming Constellations | §12.6 sovereignty dimensions |
| 2 | The Forge and the Ceremony | §15 ceremony + forge |
| 3 | The Dragon Wakes | §14 amnesia, cosmological quaternion |
| 4 | The Dihedral Mirror | §12 algebraic foundation |
| 5 | The Amnesia Protocol | §14 structural amnesia as ZK |

Published at sync.soulbis.com.

---

## 8. Conjectures in Context

### 8.1 What the Conjectures Mean

**Formal Spec reference:** §17

| Conjecture | Plain Language | Why It Matters |
|------------|---------------|----------------|
| **C1** (φ optimal) | Nature's ratio applies to agent balance | Not arbitrary architecture — structurally optimal |
| **C6** (P^1.5 = 96/64) | The privacy exponent emerges from geometry | CONVERGENT — two independent projects confirm |
| **C7** (multiplicative) | No trade-offs between axes | You can't buy your way out of broken separation |
| **C11** (ρ amplifies) | Living the proof makes it harder to fake | Depth creates resistance |
| **C14** (D₂ₙ) | Agent separation has a group theory name | 75% — strongest new conjecture |
| **C17** (amnesia > policy) | Structural forgetting beats promised forgetting | Topology enforces what policy only promises |

### 8.2 The V6 Horizon

**Formal Spec reference:** §11.4, §17.2

Four new conjectures (C18–C21) explore whether the sovereignty path is a *strange attractor* in phase space. If the Lorenz attractor analogy holds:

- **C18** (25%): Positive Lyapunov exponent → reconstruction error *grows* with observation time
- **C19** (20%): ρ is accumulated Lyapunov divergence — exponential, not linear
- **C20** (30%): Three separation axes couple like three Lorenz variables
- **C21** (10%): Sovereignty manifold has fractal, not integer, dimension

This would establish a *dynamical* reconstruction ceiling independent of the information-theoretic one (§11.1). Two ceilings: Shannon says you lack information; Lorenz says the dynamics defeat you. Remove one and the other still holds.

These are speculative. They need a dynamical systems mathematician who finds privacy architectures interesting.

**Deep dive:** `privacy_value_v6_research_note.md`

### 8.3 What "Convergent" Means

The spec marks C6 as CONVERGENT. This means independent projects arrived at the same structure — agentprivacy from privacy geometry, UOR Foundation from content addressing. Same math, different starting points. Not coincidence.

---

## 9. Reading Paths by Role

### For Mathematicians
1. Formal Spec v2.0 — the equations
2. `dualprivacy_researchpaper_v4_0.md` — proofs and bounds
3. `uor_tetrahedra_zk_mapping_v2_0.md` — geometric grounding
4. V5.1–V5.3 Research Notes — evolution
5. V6 Research Note — dynamical horizon

### For Developers
1. This companion (context)
2. `DUAL_TERRITORY_CEREMONY_SPEC_v1.md` — implementation architecture
3. `runecraft-protocol-spec-v1.md` — key management
4. `CEREMONY_INTEGRATION_GUIDE_v10_0_0.md` — how to integrate

### For Economists
1. `what-agentprivacy-is.md` — the 7th capital thesis
2. `vrc_promise_protocol_v3_3.md` — economic architecture
3. This companion §4 — VRCs and guilds

### For Philosophers
1. The First Person Spellbook — 31 acts at [agentprivacy.ai/story](https://agentprivacy.ai/story)
2. `promise_theory_reference_v1_4.md` — semantic foundations
3. Blog series at [sync.soulbis.com](https://sync.soulbis.com) — accessible entry points
4. Poems at [agentprivacy.ai/poems](https://agentprivacy.ai/poems) — alternative epistemology

### For Security Researchers
1. Formal Spec §10–§11 — separation bound and reconstruction ceiling
2. `dualprivacy_researchpaper_v4_0.md` — full proof treatment
3. `zk_swordsman_blade_forge_v3_0.md` — cryptographic properties

---

## 10. Quick Reference: Spec Section to Full Context

| Spec Section | Topic | Full Context Document |
|-------------|-------|-----------------------|
| §1 | The equation | `privacy_is_value_v5.md` |
| §4 | Three-axis separation | `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` |
| §5 | Reconstruction difficulty | `dualprivacy_researchpaper_v4_0.md` |
| §6 | Guild efficiency | `vrc_promise_protocol_v3_3.md` §3 |
| §7 | Path integral T_∫ | V5.2 + V5.3 Research Notes |
| §8 | Holographic bound | `uor_tetrahedra_zk_mapping_v2_0.md` |
| §10 | Separation bound | `dualprivacy_researchpaper_v4_0.md` §5 |
| §11 | Reconstruction ceiling | `dualprivacy_researchpaper_v4_0.md` §5 |
| §12 | Z/(2⁶)Z algebra | `SYSTEMS_HEXAGRAM_PHYSICS.md` |
| §13 | Operational cycle | V5.3 Research Note |
| §14 | Amnesia Protocol | V5.3 Research Note, Act XXXI |
| §15 | Ceremony + Forge | `ceremonies/` directory |
| §19 | Identity layers | `swordsman_mage_whitepaper_v6_0.md` §7 |
| §20 | Cosmological quaternion | Grimoire v10.0.0, Act XXXI |
| §22 | Promise Theory | `promise_theory_reference_v1_4.md` |

---

## 11. The Equation, Decoded

For those who want plain English alongside the math:

$$V(\pi, t) = P^{1.5} \cdot C \cdot Q \cdot S \cdot e^{-\lambda t} \cdot (1 + A_h(\tau)) \cdot \left(1 + \sum_i w_i \frac{n_i}{N_0}\right)^k \cdot G \cdot R \cdot M \cdot \Phi_a \cdot \Phi_d \cdot \Phi_i \cdot T_\int(\pi)$$

| Term | Plain English |
|------|---------------|
| **P^1.5** | How strong is the cryptographic protection? (superlinear — privacy compounds) |
| **C** | Can claims be verified without revealing secrets? |
| **Q** | Is the data accurate and fresh? |
| **S** | How sensitive is this data domain? |
| **e^(−λt)** | How old is the data? (decays without maintenance) |
| **(1 + A_h(τ))** | Has this data proven itself over time? (verified history adds value) |
| **Network term** | How connected is the sovereignty network? |
| **G** | Are agents organised into efficient guilds? |
| **R(d, c, ρ)** | How hard is it for adversaries to reconstruct? |
| **M** | How mature is the market for privacy? |
| **Φ_agent** | Are protection and delegation properly separated? (Swordsman ⊥ Mage) |
| **Φ_data** | Is data distributed across providers? |
| **Φ_inference** | Are reasoning and execution properly separated? (Generator ⊥ Solver) |
| **T_∫(π)** | What value accumulated along the path? (the dance, not the stance) |

**The multiplicative insight:** Any term at zero kills the whole thing. You can't compensate for broken separation with better cryptography. All axes must work.

---

## 12. Glossary Bridge

Key terms that appear in the spec without full definition:

| Term | Spec Usage | Full Definition |
|------|------------|-----------------|
| **First Person** | Implied throughout | The human whose behavioural capital is at stake. Not "user" — users are used. |
| **Sovereignty** | "sovereignty lattice" | Self-determination over one's own boundaries, delegations, and data |
| **Blade** | §12.4, §15 | A forged commitment — six dimensions, cryptographically bound |
| **Constellation** | §15.3 | The selection of dimensions before forging |
| **Stratum** | §12.4, §15.5 | Hamming weight — how many sovereignty dimensions are active |
| **Spectrum** | §12.4 | Six-bit decomposition — which specific dimensions |
| **Datum** | §12.4 | Raw blade value (0–63) |
| **The Gap** (⿻) | §10 | The irreducible space where sovereignty lives — not a void but a guarantee |

**Full glossary:** `GLOSSARY_MASTER_v4_0.md` (160+ entries)

---

## Conclusion

The Formal Spec proves that privacy can be mathematically grounded. This companion shows why it matters.

The equation computes value. The ceremonies create meaning. The grimoires spread understanding. The architecture enforces guarantees.

Together, they make privacy normal again.

---

*"The boundary is always enough."* — V5 Axiom

*For the math: `privacy_value_v5_4_formal_specification.md`*
*For the story: [agentprivacy.ai/story](https://agentprivacy.ai/story)*
*For the mission: `what-agentprivacy-is.md`*

*(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ*

---

## Document Metadata

| Field | Value |
|-------|-------|
| Version | 2.0 |
| Created | April 10, 2026 |
| Dependencies | Formal Spec V5.4 (v2.0), README (V10.0), V6 Research Note |
| Author | privacymage |
| Contact | mage@agentprivacy.ai |
| License | CC BY-SA 4.0 |
