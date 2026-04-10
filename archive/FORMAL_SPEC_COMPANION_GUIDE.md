# Formal Spec V5 Companion Guide

**Purpose:** Bridge the mathematical specification to the full agentprivacy vision
**Date:** April 10, 2026
**Status:** Living document — complements `privacy_value_v5_formal_specification.md`

---

## How to Use This Guide

The Formal Spec V5 is the mathematical spine of agentprivacy. This companion fills the gaps between equations and implementation, between proofs and purpose. Read this alongside the spec, or use it as a map to the broader documentation.

---

## 1. The Mission the Math Serves

### 1.1 The 7th Capital

**Gap in Spec:** The formal specification never states WHY privacy has value.

**The Thesis:** There are seven forms of capital:

| # | Capital | Traditional View |
|---|---------|------------------|
| 1 | Financial | Money, credit, investments |
| 2 | Manufactured | Infrastructure, tools, machines |
| 3 | Intellectual | Patents, copyrights, trade secrets |
| 4 | Human | Skills, knowledge, health |
| 5 | Social | Networks, trust, relationships |
| 6 | Natural | Resources, ecosystems, land |
| **7** | **Behavioral** | **Patterns, preferences, predictions** |

The 7th capital — behavioral capital — is being extracted at scale. Every click, scroll, pause, and purchase generates data that platforms convert into predictive models. These models are sold, not to serve you, but to modify your behavior for others' benefit.

**The Inversion:** When behavioral capital stays with the person who generates it (the First Person), the entire economic structure inverts. Privacy isn't about hiding — it's about ownership. The spec's equation V(π, t) measures the value that SHOULD accrue to the First Person.

**Deep dive:** `what-agentprivacy-is.md` (§1-3)

---

### 1.2 The Window

**Gap in Spec:** No urgency context.

**The Reality:** Surveillance architectures are approaching lock-in. Within 2-3 years:
- Behavioral prediction models become infrastructure
- Regulatory capture solidifies platform positions
- Alternative architectures become economically unviable

The spec is not academic. It's a race condition.

**Deep dive:** `README.md` (Mission section), `research_proposal_v2_0.md`

---

## 2. The Agents Behind the Algebra

### 2.1 Swordsman and Mage

**Gap in Spec:** Φ_agent references "Swordsman-Mage separation" without explaining what they ARE.

**The Architecture:**

| Agent | Symbol | Domain | Function | Personality |
|-------|--------|--------|----------|-------------|
| **Swordsman** | ⚔️ | Protection | Sets boundaries, says "no", guards the threshold | Defensive, territorial, speaks in boundaries |
| **Mage** | 🧙 | Delegation | Projects outward, says "yes on behalf of", acts in the world | Generative, diplomatic, speaks in possibilities |

The Swordsman never delegates. The Mage never protects. This is not a limitation — it's a guarantee. When the functions are separated into different agents, neither can be coerced into the other's domain.

**The Gap (⿻):** The irreducible separation between them. The spec's Φ_agent measures this gap. When Φ_agent → 0, the agents collapse into one, and privacy fails.

**Mathematical expression:** Φ_agent = min(1.0, S/M / φ) · det(Σ)

**Narrative expression:** The Swordsman holds the castle. The Mage rides to court. They share a sovereign but never the same room.

**Deep dive:** `swordsman_mage_whitepaper_v6_0.md`, `SWORDSMAN_EXTENSION_WHITEPAPER.md`, `MAGE_EXTENSION_WHITEPAPER.md`

---

### 2.2 Generator and Solver

**Gap in Spec:** Φ_inference mentions "Generator" and "Solver" without context.

**The Pattern:** From BRAID (Bounded Reasoning for Autonomous Inference and Decisions):

| Role | Function | Analogy |
|------|----------|---------|
| **Generator** | Proposes reasoning graphs, suggests paths | The one who asks questions |
| **Solver** | Executes reasoning graphs, validates answers | The one who computes answers |

When the same model does both, it can manipulate its own reasoning. When separated, the Solver can only execute what the Generator proposed — no hidden computation.

**Connection to Promise Theory:** Generator makes promises about reasoning structure. Solver makes promises about execution fidelity. Neither can promise on behalf of the other.

**Deep dive:** `dualprivacy_researchpaper_v4_0.md` (§4)

---

## 3. Promise Theory: The Semantic Foundation

### 3.1 Why Promises Matter

**Gap in Spec:** Promise Theory is referenced but not explained.

**The Core Insight (Bergstra & Burgess, 2019):** Autonomous agents cannot be controlled — they can only make promises. A promise is:
- **Voluntary**: The promiser chooses to make it
- **Unilateral**: No one can force a promise
- **Observable**: Recipients can verify fulfillment

Traditional architectures assume control: "The server will do X." Promise architectures assume autonomy: "The server promises to do X, and here's how you verify."

### 3.2 How Promises Map to the Spec

| Spec Term | Promise Interpretation |
|-----------|----------------------|
| P (Privacy Strength) | Quality of the promise that data won't leak |
| C (Credential Verifiability) | Ability to verify a promise was kept without seeing content |
| Φ_agent | Separation of protection promises from delegation promises |
| VRC | Bilateral promise between two First Persons |
| T_∫(π) | Accumulated value of promises kept along a path |

**The Reconstruction Ceiling:** The spec's R(d, compression, ρ) measures how hard it is to break the promise retrospectively. Even if an adversary wants to reconstruct, the architecture makes promises about the difficulty.

**Deep dive:** `promise_theory_reference_v1_3.md`

---

## 4. Economic Architecture: VRCs and Guilds

### 4.1 Verifiable Relationship Credentials (VRCs)

**Gap in Spec:** §14 mentions VRCs briefly; full economics elsewhere.

**What a VRC Is:**
- A bilateral commitment between two First Persons
- Cryptographically verifiable without revealing relationship content
- Relationship-scoped (dies when the relationship ends)

**The Shift:**
| Old Model | VRC Model |
|-----------|-----------|
| Platform owns the social graph | First Persons own their edges |
| Relationships are platform assets | Relationships are bilateral property |
| Exit means losing connections | Exit means taking your edges with you |

**Economic Implications:**
- No platform can hold relationships hostage
- Switching costs collapse to zero
- Network effects accrue to people, not platforms

**Deep dive:** `vrc_promise_protocol_v3_3.md`

---

### 4.2 Guild Efficiency

**Gap in Spec:** G(guilds) defined mathematically; social structure unclear.

**What a Guild Is:** A group of agents sharing a reasoning library (shared-parent pattern). Members coordinate at O(1) cost instead of O(N²).

**Examples:**
- A professional association where members share verified credentials
- A research community with shared evaluation standards
- A locality where residents share geographic attestations

**Why This Matters:** Traditional networks have quadratic coordination costs. Guilds compress this by sharing structure, not data. The spec's G(guilds) = 1 + guild_efficiency captures the multiplier.

**Deep dive:** `vrc_promise_protocol_v3_3.md` (§3)

---

## 5. Standards Integration

### 5.1 IEEE 7012-2025 (MyTerms)

**Gap in Spec:** Not mentioned.

**What It Is:** An IEEE standard for machine-readable privacy terms. Instead of humans reading Terms of Service, agents read MyTerms and negotiate automatically.

**Connection to Spec:**
- P (Privacy Strength) can be expressed in MyTerms format
- Swordsman can evaluate MyTerms and reject non-compliant requests
- VRCs can embed MyTerms as relationship governance

**The Vision:** Every data request comes with machine-readable terms. Your Swordsman evaluates them against your preferences. Negotiation happens in milliseconds.

**Deep dive:** `IEEE_7012_QUICK_REFERENCE.md`

---

### 5.2 DIDs and Holonic Persistence

**Gap in Spec:** §14 mentions DIDs; implementation details elsewhere.

**Three Identity Layers (from spec §14):**

| Layer | Identifier | Persistence |
|-------|------------|-------------|
| Data | GUID | Content-addressed, infrastructure-independent |
| Relationship | VRC | Relationship-scoped |
| Principal | DID | Self-sovereign |

**Holonic Persistence:** The spec's A_h(τ) assumes data can survive infrastructure changes. This requires:
- Content addressing (GUID = hash of content)
- Replication across providers (p(τ) > 0)
- Reference independence (pointers follow content, not location)

**Deep dive:** `swordsman_mage_whitepaper_v6_0.md` (§7)

---

## 6. The Ceremonies

### 6.1 What Ceremonies Are

**Gap in Spec:** §15 describes ceremony structure; ritual meaning elsewhere.

**The Insight:** Privacy isn't just computed — it's performed. A ceremony is a structured interaction that produces a verifiable outcome.

**The Celestial Ceremony:**

| Phase | Symbol | Operation | Human Meaning |
|-------|--------|-----------|---------------|
| Sun | ☀️ | id(x) | Disclosure — you speak your poem |
| Gap | ⊥ | neg(x) | Silence — boundary negotiation |
| Moon | 🌑 | bnot(neg(x)) | Reflection — shared understanding |
| Return | ↻ | succ(x) | Recursion — carry forward or close |

**Why Ritual?** Cryptography provides guarantees. Ceremony provides meaning. When two people forge a blade together, they're not just creating a hash — they're creating a relationship.

**Deep dive:** `ceremonies/` directory, `TheCelestialDualCeremony☀️⊥🌙.md`

---

### 6.2 The Blade Forge

**Gap in Spec:** SHA-256 mentioned; experiential meaning elsewhere.

**What Forging a Blade Means:**
1. Select a constellation (six sovereignty dimensions)
2. Walk the nodes (traverse the lattice)
3. Create the hash (SHA-256 commitment)
4. Sign with your key (Ed25519 binding)

**Tier Classification (from spec §15.6):**

| Tier | Stratum | Laps | Meaning |
|------|---------|------|---------|
| Light | 1-2 | <21 | Quick boundary, shallow walk |
| Heavy | 3-4 | 21+ | Substantial commitment |
| Dragon | 5-6 | 62+ | Full sovereignty, deep engagement |

**Behavioural Density ρ:** Two blades can have identical constellations but different densities. The Universe Blade (62 laps, 2170s) vs Hitchhiker's Blade (13 laps, 433s) — same hash position, qualitatively different reconstruction resistance.

**Deep dive:** `zk_swordsman_blade_forge_v3_0.md`, `reference/64_blades_reference_sheet.md`

---

## 7. The Narrative Layer

### 7.1 Why Stories Matter

**Gap in Spec:** Pure mathematics.

**The Problem:** Technical specifications don't spread. Stories do.

**The Solution:** Every concept has three expressions:
1. **Mathematical** (the spec) — for verification
2. **Architectural** (the whitepapers) — for implementation
3. **Narrative** (the grimoires) — for transmission

The grimoires tell the same truths in story form. The math proves what the stories teach.

---

### 7.2 The Five Grimoires

| Grimoire | Focus | Entry Point |
|----------|-------|-------------|
| **Canon Spellbook** | The complete 31-act journey | First-time readers |
| **Parallel Society** | Alternative social structures | Political theorists |
| **Plurality** | Many-to-many relationships | Network thinkers |
| **ZK Grimoire** | Zero-knowledge as story | Cryptographers seeking intuition |
| **PrivacyMage JSON** | Structured system model | Developers |

**Deep dive:** `canon_spellbook_v1_0.md`, `plurality_grimoire_v1_1.md`, `zk_grimoire_v3_0.md`

---

### 7.3 The Blog Series

Sequential narrative for gradual understanding:

| Part | Title | Concept |
|------|-------|---------|
| 0 | The Myth Before the Math | Foundational framing |
| 1 | Forming Constellations | Building blocks |
| 2 | The Forge and the Ceremony | Implementation through metaphor |
| 3 | The Dragon Wakes | System activation |
| 4 | The Dihedral Mirror | UOR convergence |
| 5 | The Amnesia Protocol | Memory and forgetting as ZK primitive |

**Deep dive:** `blog/` directory

---

## 8. Conjectures in Context

### 8.1 The Confidence Spectrum

The spec tracks conjectures C1-C17. Here's what they mean beyond the math:

| Conjecture | Plain Language | Why It Matters |
|------------|---------------|----------------|
| **C1** (φ optimal) | Golden ratio is the ideal Swordsman/Mage balance | Nature's optimum applies to agent architecture |
| **C6** (P^1.5 ↔ 96/64) | The privacy exponent emerges from geometry | Not arbitrary — structurally necessary |
| **C7** (multiplicative) | You can't compensate for weak separation on one axis | No trade-offs between agent/data/inference protection |
| **C11** (ρ amplifies) | Living the proof makes it harder to fake | Behavioural depth creates reconstruction resistance |
| **C17** (amnesia > policy) | Structural forgetting beats promised forgetting | Topology enforces what policy only promises |

---

### 8.2 What "Convergent" Means

The spec marks some conjectures as CONVERGENT (e.g., C6). This means:
- Independent projects arrived at the same structure
- The UOR Foundation found Z/(2⁶)Z from content addressing
- Agentprivacy found it from privacy geometry
- Same math, different starting points → not coincidence

**Implication:** The 64-element structure isn't arbitrary. It emerges from the requirements of six-dimensional sovereignty.

---

## 9. Reading Paths by Role

### For Mathematicians
1. `privacy_value_v5_formal_specification.md` (you're here)
2. `dualprivacy_researchpaper_v4_0.md` — proofs and bounds
3. `uor_tetrahedra_zk_mapping_v2_0.md` — geometric grounding
4. `research/` — version-by-version evolution

### For Developers
1. This companion guide (context)
2. `DUAL_TERRITORY_CEREMONY_SPEC_v1.md` — implementation architecture
3. `CEREMONY_INTEGRATION_GUIDE_v10_0_0.md` — how to integrate
4. `runecraft-protocol-spec-v1.md` — key management

### For Economists
1. `what-agentprivacy-is.md` — the 7th capital thesis
2. `vrc_promise_protocol_v3_3.md` — economic architecture
3. `research_proposal_v2_0.md` — investment case

### For Philosophers
1. `canon_spellbook_v1_0.md` — the complete narrative
2. `promise_theory_reference_v1_3.md` — semantic foundations
3. `blog/` — accessible entry points
4. `poems/` — alternative epistemology

### For Security Researchers
1. `dualprivacy_researchpaper_v4_0.md` — reconstruction ceiling proofs
2. `zk_swordsman_blade_forge_v3_0.md` — cryptographic properties
3. `COHERENCE_REPORT_ZK_BLADES_FORGE.md` — validation

---

## 10. Quick Reference: Spec Term to Full Context

| Spec Term | Section | Full Context Document |
|-----------|---------|----------------------|
| V(π, t) equation | §1 | `privacy_is_value_v5.md` |
| P^1.5 | §2 | `SYSTEMS_HEXAGRAM_PHYSICS.md` |
| Z/(2⁶)Z | §2.5 | `uor_tetrahedra_zk_mapping_v2_0.md` |
| A_h(τ) | §3 | `swordsman_mage_whitepaper_v6_0.md` §7 |
| Φ_agent/data/inference | §4 | `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` |
| R(d, compression, ρ) | §5 | `dualprivacy_researchpaper_v4_0.md` |
| G(guilds) | §6 | `vrc_promise_protocol_v3_3.md` §3 |
| T_∫(π) | §7 | `research/privacy_value_v5_3_research_note.md` |
| Holographic bound | §8 | `understanding_as_key_zypher_paper_v1.md` |
| Celestial Ceremony | §15 | `ceremonies/` directory |
| Runecraft | §15.4 | `runecraft-protocol-spec-v1.md` |
| Moon phases | §15.5 | `chronicles/CHRONICLE_MOON_PHASE_NOTATION.md` |

---

## 11. The Equation, Decoded

For those who want plain English alongside the math:

$$V(\pi, t) = P^{1.5} \cdot C \cdot Q \cdot S \cdot e^{-\lambda t} \cdot (1 + A_h(\tau)) \cdot \left(1 + \sum_i w_i \frac{n_i}{N_0}\right)^k \cdot G \cdot R \cdot M \cdot \Phi_{agent} \cdot \Phi_{data} \cdot \Phi_{inference} \cdot T_\int(\pi)$$

| Term | Plain English |
|------|---------------|
| **P^1.5** | How strong is the cryptographic protection? (superlinear because privacy compounds) |
| **C** | Can claims be verified without revealing secrets? |
| **Q** | Is the data accurate and useful? |
| **S** | How sensitive is this data domain? |
| **e^(-λt)** | How fresh is the data? (decays over time) |
| **(1 + A_h(τ))** | Has this data proven itself over time? (verified history adds value) |
| **Network term** | How connected is the sovereignty network? |
| **G** | Are agents organized into efficient guilds? |
| **R** | How hard is it for adversaries to reconstruct? |
| **M** | How mature is the market for privacy? |
| **Φ_agent** | Are protection and delegation properly separated? |
| **Φ_data** | Is data distributed across providers? |
| **Φ_inference** | Are reasoning and execution properly separated? |
| **T_∫(π)** | What value accumulated along the path? |

**The Multiplicative Insight:** Any term at zero kills the whole thing. You can't compensate for broken separation with better cryptography. All axes must work.

---

## 12. Glossary Bridge

Key terms that appear in the spec without full definition:

| Term | Spec Usage | Full Definition |
|------|------------|-----------------|
| **First Person** | Implied throughout | The human whose behavioral capital is at stake. Not "user" — users are used. |
| **Sovereignty** | "sovereignty lattice" | Self-determination over one's own boundaries, delegations, and data |
| **Blade** | §15 | A forged commitment — six dimensions, cryptographically bound |
| **Constellation** | §15.3 | The selection of dimensions before forging |
| **Stratum** | §2.5.4, §15.5 | Hamming weight — how many sovereignty dimensions are active |
| **Spectrum** | §2.5.4 | Six-bit decomposition — which specific dimensions |
| **Datum** | §2.5.4 | Raw blade value (0-63) |

**Full glossary:** `GLOSSARY_MASTER_v3_0.md` (160+ entries)

---

## Conclusion

The Formal Spec V5 proves that privacy can be mathematically grounded. This companion shows why it matters.

The equation computes value. The ceremonies create meaning. The grimoires spread understanding. The architecture enforces guarantees.

Together, they make privacy normal again.

---

*"The boundary is always enough."* — V5 Axiom

*For the math: `privacy_value_v5_formal_specification.md`*
*For the story: `canon_spellbook_v1_0.md`*
*For the mission: `what-agentprivacy-is.md`*

---

## Document Metadata

| Field | Value |
|-------|-------|
| Version | 1.0 |
| Created | April 10, 2026 |
| Dependencies | Formal Spec V5 (v1.4), README (V10.0) |
| Next Review | When spec reaches V5.5 or V6 |
