---
title: "Privacy is Value · V6: The Mage Reading"
subtitle: "Companion guide to the Privacy Value Model · context, narrative, standards, economics · a volume of the Privacy is Value book"
version: "6.0"
date: "2026-06-10"
author: "privacymage"
license: "CC BY-SA 4.0"
register: "CONJECTURE_REGISTER_V6.md · head C89"
status: "Fully standalone. Carries the full V5.4 companion material (Promise Theory, economics, ceremonies, quick reference, glossary) updated to V6."
---

# Privacy Value Model V6: Companion Guide

## How to Read These Documents

Three documents carry V6, one model. The **formal specification** (`privacy_value_v6.md`) is the authority: it mirrors the V5.4 skeleton section for section, marks every section CARRIED, REVISED, or NEW, and cites every conjecture from the unified register. The **compressed specification** (`pvm_v6_compressed.md`) is the Swordsman reading: equations only, five pages, for agents and reviewers who need the shape before the proofs. This guide is the Mage reading: what the mathematics means, where it came from, and what it asks of you. Under the unified-V6 labeling decision, the research paper and the whitepaper carry the same V6 label; this guide tells you when to reach for each.

## 1. The Two Strands of V6

V6 was planned before it was discovered, and the plan came first.

**The gathering turn.** From the earliest V6 research notes, V6 was identified as the version that opens the model outward. V5 answered WHAT the architecture is: two agents, a boundary, a gate, a lattice. V6 asks WHO. It shifts the document's address into the second person, opens the registers to the City of Mages and to kindred builders, and turns the equation from a specification into an invitation, so that its terms can be filled with data instead of estimates. The betweenness centrality of the gap got a computable formula; the trust edges got an economy; the City got keys. That was the plan, and it stands as V6's first strand.

**The moving ceiling.** The second strand was not planned. Between April and June 2026, in the act of gathering, the research moved: the reconstruction ceiling proved to be a function of time. The story of V6's mathematics is the story of taking one letter seriously, the t that was always in V(π, t), and following it through every term that had quietly been treated as static.

## 2. The Ceiling Moves: What R(t) Means

The V5.4 ceiling said: the two agents' channels, summed, cannot carry enough information to reconstruct you. True, and proven, under two conditions that V6 now states aloud: the agents must not collude (and nothing may carry their residue), and the adversary must be the adversary you measured. The second condition is where time enters. Your archives do not change after emission. The decoders reading them do. A model released tomorrow extracts more from yesterday's data than anything could when the data was emitted, so the ceiling drifts upward while you sleep, and every static guarantee has a shelf life, written t*.

Two public events made this concrete within nine days of this document. A four-year-old flaw in Zcash's Orchard circuit was found one day after a frontier model's release, and weaponized the same day. A withheld quantum optimization, attested only by a zero-knowledge proof of its existence, was independently rediscovered in roughly two months. In both cases the protected object sat still and the capability term moved. The model calls this the Moving Ceiling (C82), and it is V6's headline.

## 3. The Sum Leaks More Than Its Parts: Why Amnesia Wins

In 2025 and 2026 the multi-agent privacy field proved something that looks, at first glance, like an attack on this model: when agents pass outputs to one another, leakage compounds, up to (2^N − 1)ε for N agents, and measurement studies found multi-agent systems leaking 68.9% of sensitive content overall, mostly through the unmonitored channels between agents.

Read carefully, this is the model's own thesis in the adversary's units. The compounding happens through the inter-agent channel. The Amnesia Protocol's entire purpose is to delete that channel. Policy separation asks the channel to behave and compounds exponentially; amnesia separation removes the channel and leaks linearly. The gap between asking and removing is, at five agents, the gap between 31ε and 5ε (C83). The field measured the corridor this architecture bricks up.

## 4. The Proof That Whispered: Existence-Leak

Google proved it had found a faster attack and published only the proof of existence, hiding the method perfectly. Two months later the method was rediscovered anyway, because the proof itself was a map with one landmark: it said the thing exists and is findable, and every searcher stopped digging anywhere else. V6 names this the Existence-Leak law (C81, 70%): a proof of feasibility leaks an upper bound on difficulty, and there is a theorem (leakage-resilient ZK with λ < 1 is impossible) saying the leak can never be zero. The planning corollary (C84): every public feasibility attestation shortens your migration deadline, whether or not the attack ever comes. Important fence: this indicts capability attestation, not the model's own zero-knowledge usage, which proves instances (a transaction, an attribute), not capabilities.

## 5. The Bridge and the Forgetting

Two old debts were paid in Part IV of the spec. First, the lattice and the axes finally meet: the bridge conjecture (C85) maps the six lattice dimensions pairwise onto the three sovereignty axes and proposes that the recursion's base case β, the thing the two agents are allowed to share, is exactly the First Person, which is why the separation bound conditions on FP. The gap is β. Second, forgetting got its mathematics: structural amnesia is conjectured to be a non-vanishing obstruction to gluing the agents' views back into a witness (C86). Hidden things wait for keys; forgotten things have no door. If that holds, amnesia is the only term in the equation whose security does not erode with time, which makes it the architectural answer to the moving ceiling of section 2.

## 6. Promise Theory: The Semantic Foundation

### 6.1 Why Promises Matter

**Formal Spec reference:** §22

Promise Theory (Bergstra & Burgess, 2019) provides the semantic foundation. A promise is voluntary, unilateral, and observable. Traditional architectures assume control: "The server WILL do X." Promise architectures assume autonomy: "The server PROMISES to do X, and here's how you verify."

The autonomy axiom, *an agent can only make promises about its own behaviour*, formally explains why single agents fail at the privacy-delegation paradox. Attempting to promise both protection and delegation exceeds autonomous capability.

### 6.2 How Promises Map to the Spec

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
| The Gap (⿻) | Irreducible promise of the superagent, owned by neither agent |

V6 sharpens the last row: C78 identifies the specification-intent gap, the distance between what an agent was told and what was meant, with the irreducible promise of the superagent.

**Deep dive:** `promise_theory_reference_v1_4.md`

## 7. Economic Architecture: VRCs and Guilds

### 7.1 Verifiable Relationship Credentials (VRCs)

**Formal Spec reference:** §19 (Three Identity Layers)

A VRC is a bilateral commitment between two First Persons, cryptographically verifiable without revealing relationship content, relationship-scoped (dies when the relationship ends).

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

V6 attaches the clock here too: trust edges decay with a half-life measured from inscription (C30 to C33), so a VRC is not a permanent asset but a maintained one, and the signal cadence is the maintenance. And the presence knot 🪢 carries its regime-1 declaration: it is non-transferable, non-attesting local color, earned by walking; if it is ever asked to attest, witnesses co-sign first.

**Deep dive:** `vrc_promise_protocol_v3_3.md`

### 7.2 Guild Efficiency

**Formal Spec reference:** §6

A guild is a group of agents sharing a reasoning library (shared-parent pattern). Members coordinate at O(1) cost instead of O(N²). The spec's G(guilds) captures the multiplier.

**Trust Tier Progression:**

| Tier | Signals | Capabilities | Trust Value |
|------|---------|-------------|-------------|
| Blade 🗡️ | 0–50 | Basic participation, learning | 0.0–0.2 |
| Light 🛡️ | 50–150 | Multi-site coordination | 0.2–0.5 |
| Heavy ⚔️ | 150–500 | Template creation, governance | 0.5–0.8 |
| Dragon 🐉 | 500+ | Guardian eligibility, unlimited VRCs | 0.8–1.0 |

**Deep dive:** `vrc_promise_protocol_v3_3.md` (§3)

## 8. The Key, the Knot, and the Star

The City Key arc entered the formal lineage. The trust recursion the City shipped in May (walk the domains, charge the trace, carry the deepened key back) is structurally a folding scheme: the Key is an accumulator of proofs, and the conjecture (C87) is that a real incrementally-verifiable realization exists, with lattice-based folding as the post-quantum hedge. The presence knot 🪢 received its honest regime: it is local color, earned by walking, attesting nothing; if it is ever asked to attest, witnesses co-sign first. And the eight-pointed star gave back its borrowed gold: there is no golden ratio in that solid, and saying so cost one paragraph and bought the geometry two genuinely new conjectures (the parity cube, C88, and the octahedral gap, C89: the chamber at the star's heart that neither agent owns).

## 9. The Ceremonies

### 9.1 What Ceremonies Are

**Formal Spec reference:** §13 (operational cycle), §15 (ceremony implementation)

Privacy isn't just computed; it's performed. A ceremony is a structured interaction that produces a verifiable outcome. The Celestial Ceremony maps the operational cycle (§13) to two people:

| Phase | Symbol | Spec Operation | Human Meaning |
|-------|--------|----------------|---------------|
| Sun | ☀️ | id(x) | Disclosure · you speak your poem |
| Gap | ⊥ | neg(x) | Silence · boundary negotiation |
| Moon | 🌑 | bnot(neg(x)) | Reflection · shared understanding |
| Return | ↻ | succ(x) | Recursion · carry forward or close |

Cryptography provides guarantees. Ceremony provides meaning.

### 9.2 The Blade Forge

**Formal Spec reference:** §15 (forge cryptography, moon phases, tier classification)

Forging a blade:
1. Select a constellation (six sovereignty dimensions → spectrum)
2. Walk the nodes (traverse the lattice → accumulate laps)
3. Create the hash (SHA-256 commitment → content addressing)
4. Sign with your key (Ed25519 binding → identity)

The spec's behavioural density ρ (§5) captures why two blades with identical constellations but different lap counts have qualitatively different reconstruction resistance. The Universe Blade (62 laps, 2,170s) vs Hitchhiker's Blade (13 laps, 433s): same hash position, different proof depth.

The City Key trust recursion (C87) is the newest ceremony-grade loop: walk the domains, charge the trace, carry the deepened Key back, each Charge a folding step in the accumulator.

**Deep dive:** `zk_swordsman_blade_forge_v3_0.md`

## 10. Standards and the Landscape

IEEE 7012-2025 (MyTerms) published in January 2026; the implementation effort began June 1. The EU AI Act's Annex III high-risk obligations stand for 2026-08-02 (hedged: the Digital Omnibus would defer to 2027-12-02 but is not adopted). The model's position is unchanged and now better armed: architecture is not against regulation, it is what makes regulated rights enforceable. The fellow travelers (Kwaai, the First Person Project, GliaNet, Archon, the UOR Foundation) and the multi-agent privacy literature are cited as plurality: many teams arriving at separation-of-duties independently, none enforcing it architecturally, which is the model's distinctive claim and the measurements' implicit confirmation.

## 11. Conjectures in Context

The register (`research/CONJECTURE_REGISTER_V6.md`) is now the single numbering authority, born from a real failure: the corpus forked its own numbers twice, and the V6 path's first act was to consolidate, namespace, and promise never to renumber again. Highlights of the V6 additions: C81 Existence-Leak (70%, held there until a second instance), C82 the Moving Ceiling (65%), C83 the exponential-to-linear gap (55%), C85 the bridge (40%), C86 obstruction amnesia (30%), C87 the Key accumulates (50%). The honest-limits discipline is unchanged: λ is unmeasured, C83's amnesia side is an engineering claim, C86 is a framing priced at 30%, and the model says so in its own honest-limits section.

## 12. Reading Paths by Role

**Reviewer or academic:** formal spec §10, §11, §5 (the conditional relabel and R(t)), then §26 (the compounding absorption), then the register. **Builder:** compressed spec, then §14 and §15 (amnesia and the Key), then the regime statement before touching 🪢. **Economist or policy reader:** this guide, then spec §27 and §30, then the canonical figures. **City reader:** the five acts bound at the Myth Gate, then §28, then back to Tome VIII Act 3 with the honesty paragraph in hand. **New reader:** what-agentprivacy-is, then this guide top to bottom, then the compressed spec.

## 13. The Equation, Decoded

Nothing in the equation's form changed at V6: the gate still multiplies, the terms still sum, the path still integrates. What changed is the clock attached to it. Read every term twice: once at t₀, where V5.4 proved what it proved, and once at t, where capacities drift, trust decays from inscription, attestations discount horizons, trajectories diverge, and exactly one term, the forgetting, holds still. The equation was always V(π, t). V6 is the version that read the second argument.

For those who want plain English alongside the math:

$$V(\pi, t) = P^{1.5} \cdot C \cdot Q \cdot S \cdot e^{-\lambda t} \cdot (1 + A_h(\tau)) \cdot \left(1 + \sum_i w_i \frac{n_i}{N_0}\right)^k \cdot G \cdot R \cdot M \cdot \Phi_a \cdot \Phi_d \cdot \Phi_i \cdot T_\int(\pi)$$

| Term | Plain English |
|------|---------------|
| **P^1.5** | How strong is the cryptographic protection? (superlinear · privacy compounds) |
| **C** | Can claims be verified without revealing secrets? |
| **Q** | Is the data accurate and fresh? |
| **S** | How sensitive is this data domain? |
| **e^(−λt)** | How old is the data? (decays without maintenance) |
| **(1 + A_h(τ))** | Has this data proven itself over time? (verified history adds value) |
| **Network term** | How connected is the sovereignty network? |
| **G** | Are agents organised into efficient guilds? |
| **R(d, c, ρ)** | How hard is it for adversaries to reconstruct? (time-indexed as R(t) at V6) |
| **M** | How mature is the market for privacy? |
| **Φ_agent** | Are protection and delegation properly separated? (Swordsman ⊥ Mage) |
| **Φ_data** | Is data distributed across providers? |
| **Φ_inference** | Are reasoning and execution properly separated? (Generator ⊥ Solver) |
| **T_∫(π)** | What value accumulated along the path? (the dance, not the stance) |

**The multiplicative insight:** Any term at zero kills the whole thing. You can't compensate for broken separation with better cryptography. All axes must work.

## 14. Quick Reference: Spec Section to Full Context

The V6 formal spec mirrors the V5.4 skeleton in §1 to §24, then continues with the V6 material.

| Spec Section | Topic | Full Context |
|-------------|-------|-----------------------|
| §1 | The equation | this guide §13 · `privacy_is_value_v5.md` |
| §4 | Three-axis separation | `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` |
| §5 | Reconstruction difficulty · R(t) and t* | this guide §2 · `dualprivacy_researchpaper_v4_0.md` |
| §6 | Guild efficiency | this guide §7 · `vrc_promise_protocol_v3_3.md` §3 |
| §7 | Path integral T_∫ | V5.2 + V5.3 Research Notes |
| §8 | Holographic bound | `uor_tetrahedra_zk_mapping_v2_0.md` |
| §10 | Separation bound · preconditions | this guide §2 · `dualprivacy_researchpaper_v4_0.md` §5 |
| §11 | Reconstruction ceiling · conditional regime | this guide §2, §3 |
| §12 | Z/(2⁶)Z algebra | `SYSTEMS_HEXAGRAM_PHYSICS.md` |
| §13 | Operational cycle | this guide §9 · V5.3 Research Note |
| §14 | Amnesia Protocol · obstruction upgrade | this guide §3, §5 |
| §15 | Ceremony + Forge · the Key as accumulator | this guide §8, §9 · `ceremonies/` directory |
| §19 | Identity layers | `swordsman_mage_whitepaper_v6_0.md` §7 |
| §20 | Cosmological quaternion | Grimoire v10.0.0, Act XXXI |
| §22 | Promise Theory | this guide §6 · `promise_theory_reference_v1_4.md` |
| §25 | The two worked instances (Orchard · Schrottenloher) | this guide §2 |
| §26 | Compounding bound · exponential-to-linear gap | this guide §3 |
| §27 | The temporal thread | this guide §2, §4 |
| §28 | The geometry of the gap | this guide §8 |
| §29 | Narrative corpus | `tomes/` · the bound collection |
| §30 | Canonical figures | this guide §12 (economist path) |
| §31 | External landscape | this guide §10 |
| §32 | Honest limits | this guide §11 |
| §33 | References | `privacy_value_v6.md` §33 |

## 15. Glossary Bridge

Key terms that appear in the spec without full definition:

| Term | Spec Usage | Full Definition |
|------|------------|-----------------|
| **First Person** | Implied throughout | The human whose behavioural capital is at stake. Not "user"; users are used. |
| **Sovereignty** | "sovereignty lattice" | Self-determination over one's own boundaries, delegations, and data |
| **Blade** | §12, §15 | A forged commitment, six dimensions, cryptographically bound |
| **Constellation** | §15 | The selection of dimensions before forging |
| **Stratum** | §12, §15 | Hamming weight: how many sovereignty dimensions are active |
| **Spectrum** | §12 | Six-bit decomposition: which specific dimensions |
| **Datum** | §12 | Raw blade value (0–63) |
| **The Gap** (⿻) | §10 | The irreducible space where sovereignty lives, not a void but a guarantee |

V6 terms:

| Term | Spec Usage | Full Definition |
|------|------------|-----------------|
| **Moving ceiling** | §5, C82 | R(t) is non-decreasing under capability growth; the ceiling drifts while the archives sit still |
| **Shelf life t*** | §5 | sup{t : R(t) < 1}: the last moment a static guarantee still holds |
| **Existence-leak** | §27, C81 | A public proof of feasibility leaks an upper bound on difficulty; the leak can never be zero |
| **Ages progressively** | §27, C47 | Taxonomy class for guarantees that weaken continuously as decoders improve, rather than failing at one event |
| **Obstruction amnesia** | §14, C86 | Grade-2 forgetting as a non-vanishing obstruction class to gluing the agents' local views into a global witness |
| **Terminal obstruction** | §14, C73 | Structural loss of β, the recursion's base case; no successor state exists |
| **Parity cube** | §28, C88 | The stella octangula's two tetrahedra as the even/odd parity classes of {0,1}³ |
| **Octahedral gap** | §28, C89 | The intersection core as the locus of the conditional-independence bound; the chamber neither agent owns |
| **The Key accumulates** | §15, C87 | The City Key trust recursion as incrementally verifiable computation; each Charge is a folding step |
| **Regime 1** | §15 | The presence knot's declared status: non-transferable, non-attesting local color, earned by walking |
| **The register** | throughout | `CONJECTURE_REGISTER_V6.md`, the single numbering authority, head C89 |

**Full glossary:** `GLOSSARY_MASTER_v4_0.md` (160+ entries)

## Document Metadata

| Field | Value |
|---|---|
| Version | 6.0 (unified V6 labeling across all canon papers, G3 decision 2026-06-10) |
| Status | Fully standalone: V5.4 companion material (Promise Theory, economics, ceremonies, quick reference, glossary) carried in full and updated to V6 |
| Authority | privacy_value_v6.md · CONJECTURE_REGISTER_V6.md (head C89) |
| Siblings | pvm_v6_compressed.md (Swordsman) · research paper V6 edition · whitepaper V6 edition |
| Working record | research/privacy_value_v6_draft.md (Parts I to V, full honest limits) |
| License | CC BY-SA 4.0 |

(⚔️⊥⿻⊥🧙)😊
