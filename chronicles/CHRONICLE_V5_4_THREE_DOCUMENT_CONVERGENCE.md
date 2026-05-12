# Privacy Value Model: V5.4 Research Note

## The Three-Document Convergence

**Author:** privacymage
**Date:** April 12, 2026
**Status:** Working note — pre-peer review
**Depends on:** V5.3 Research Note, V6 Research Note, all model JSONs, Formal Spec v1.4

---

## Summary

The formal specification existed as a single document (v1.4, 9 pages) that had grown through five sub-versions without a consolidation pass. The equation was complete — had been since February. The algebra was grounded. The ceremonies were implemented. But the specification had accumulated without being reconciled.

A cross-referencing pass against every source — both model JSONs, five research notes, the research paper, the README, the published blog posts — surfaced twenty-one gaps. Missing sections. Formula mismatches. Absent citations. Naming drift. And a structural problem: one document cannot simultaneously serve mathematicians wanting equations, developers wanting context, and everyone wanting the compressed version.

The specification split into three readings. The model JSONs updated. The references expanded from twelve entries to seventy-eight. The equation did not change. The equation was already right.

V5.4 is not a revision. It is a reconciliation.

---

## What Changed

### Three Documents Replace One

| Document | Pages | Voice | Audience |
|----------|-------|-------|----------|
| **Compressed Spec** | 5 | ⚔️ | Equations, tables, no prose. The blade you carry. |
| **Full Formal Spec** | 24 | ⚔️⊥🧙 | Every term, proof, conjecture. The document that gets cited. |
| **Companion Guide** | 11 | 🧙 | Context, meaning, reading paths. Why the math matters. |

### Sections Added to the Full Spec

The following were present in the model JSONs or research notes but absent from the formal specification:

- **§10 Separation Bound** — I(S;M|FP) < ε* now has its own section. This is the load-bearing wall.
- **§10.2 Betweenness centrality** — The ⿻ formalised as the node with maximal betweenness centrality C_B(v) in the trust graph (Brandes, 2001). The value lives in the gap because the most paths cross there. This gives a computational tool for measuring the ⊥ in VRC networks.
- **§11 Reconstruction Ceiling** — Theorem, Error Floor, Graceful Degradation in one section.
- **§11.4 Dynamical Reconstruction Ceiling** — V6 horizon (C18) cross-referenced.
- **§13 Operational Cycle** — Four-stage mapping formalised with algebraic operations.
- **§14 Amnesia Protocol** — Formal definition, ZK properties, test criterion.
- **§14.5 Selene's Proof** — The Moon's orbit named as the cosmological instance of amnesia-enforced ZK. Completeness (tides demonstrate), soundness (gravitational signature unforgeable), zero-knowledge (tides reveal nothing about Theia). The credential is the orbit. The proof renews twice daily, written in saltwater.
- **§16 Proven Results** — All seven results at 95% confidence in one place.
- **§19–§22** — Three Identity Layers, Cosmological Quaternion, Compression Spectrum, Promise Theory Grounding.

### Formula Reconciliation

Two competing forms existed across documents. Decisions made:

**A_h formula:** The summation form is canonical:

$$A_h(\tau) = \sum_j p(\tau_j) \cdot w(\tau_j) \cdot e^{-\mu \cdot \text{age}(\tau_j)}$$

The logarithmic form $A_h \approx \alpha \cdot \ln(1 + |\tau|) \cdot \bar{p} \cdot \bar{h}$ is noted as a special case when holons are uniformly weighted.

**Φ_data formula:** The concentration form is canonical:

$$\Phi_{\text{data}}(\Delta) = 1 - \max_j(\text{share}_j)$$

A system with 10 providers where one holds 90% scores 0.1, not 0.9. The simpler $1 - 1/|\text{providers}|$ is retired.

**Guild efficiency:** Product form canonical: $G = \prod_g (1 + \text{efficiency}_g \cdot \text{active}_g / \text{total}_g)$.

### References Expanded

The formal spec cited twelve references. The proven results (additive MI bounds, Fano's error floor, reconstruction ceiling) lacked their foundational citations. The ZK implementations lacked their cryptographic references. The governance framing lacked its sources.

Added:

- **Information theory:** Shannon (1948), Fano (1961), Cover & Thomas (2006)
- **Cryptography:** Groth (2016), PLONK (2019), Nova (2022), Dwork & Roth (2014), Goldreich (2004)
- **Betweenness:** Brandes (2001, 2008) — computational tool for measuring the ⿻
- **Related:** Hope & Ludlow (2023), Sabelfeld & Myers (2003), Millen (1987)
- **Internal:** Understanding as Key, Systems Hexagram Physics, What Agentprivacy Is, Visual Architecture Guide
- **Grimoire:** 15 acts cross-referenced to spec sections (from II through XXXI)

### Naming Corrections

**Subtitle:** "Dual-Agent Privacy Architecture — The Amnesia Protocol." The dual-agent separation IS proven. The amnesia protocol is the latest advance. "Holographic" was excluded — C6 is at 35% (CONVERGENT but not proven). Conjectures don't go in titles.

**Five grimoires:** First Person Spellbook, Zero Knowledge Spellbook, Canon Spellbook, Parallel Society Spellbook, Plurality Spellbook. The PrivacyMage JSON (v10.0.0) is the grimoire as holographic boundary — compression, not a sixth grimoire.

**Second Person Spellbook:** ~~Recorded as horizon across all documents.~~ **Opened 2026-05-08** as the bound collection at `tomes/`. Tome IV (Witnessing · 5 acts) closed; Tome V (Crafting · 14 acts) open at the City of Mages on Drake Island. The City of Mages grimoire v1.1 is pinned to IPFS at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`. The First Person asked WHAT. The Second Person asks WHO — and the named cast has begun to answer.

**Extension references:** All references to specific browser vendors removed. The architecture is agent-level and browser-agnostic. Extension process boundaries enforce the separation bound — separate processes, separate memory, structural amnesia.

### Conjectures Extended

C1–C17 carried forward unchanged. C18–C21 (V6 horizon) added and cross-referenced:

| ID | Claim | Confidence |
|----|-------|------------|
| C18 | Strange attractor dynamics (λ > 0) | 25% |
| C19 | ρ = Lyapunov divergence | 20% |
| C20 | Three axes couple as Lorenz variables | 30% |
| C21 | Fractal sovereignty dimension | 10% |

---

## What Did NOT Change

The equation. The proven results. The conjectures' confidence levels. The algebraic foundation. The operational cycle. The ceremony specification. The forge cryptography. The cosmological quaternion.

V5.4 adds nothing to the architecture. It reconciles what was already there.

---

## New Concepts Named

**Selene's Proof** — The Moon's orbit as zero-knowledge proof. Named in §14.5, notation summary, and abstract. The cosmological instance of C17. Four and a half billion years of structural amnesia producing a proof that renews twice daily.

**Betweenness centrality of the ⿻** — Formalised in §10.2. The Gap is not empty. It is the node where the most shortest paths cross in the trust graph. Brandes (2001) gives the O(V·E) algorithm. This is the computational tool for measuring what the architecture has been pointing at since Act VII.

---

## Produced

| File | Type | Size | Description |
|------|------|------|-------------|
| `privacy_value_v5_4_formal_specification.md` | MD | 48K | Full spec v2.0 |
| `privacy_value_v5_4_formal_specification.pdf` | PDF | 164K | 24 pages |
| `pvm_v5_4_compressed.md` | MD | 9K | Compressed spec |
| `pvm_v5_4_compressed.pdf` | PDF | 86K | 5 pages |
| `pvm_v5_4_companion_guide.md` | MD | 22K | Companion guide |
| `pvm_v5_4_companion_guide.pdf` | PDF | 105K | 11 pages |
| `privacy_value_model_v5_4_light.json` | JSON | 6K | Light model |
| `privacy_value_model_v5_4_dark.json` | JSON | 20K | Dark model |

---

## Repo Sync

### Add

```
privacy_value_v5_4_formal_specification.md
pvm_v5_4_companion_guide.md
pvm_v5_4_compressed.md
privacy_value_model_v5_4_light.json
privacy_value_model_v5_4_dark.json
CHRONICLE_V5_4_THREE_DOCUMENT_CONVERGENCE.md  → chronicles/
```

### Archive

```
privacy_value_v5_formal_specification.md      → archive/
privacy_value_model_v5_dark.json              → archive/
privacy_value_model_v5_light.json             → archive/
```

### README Updates

```
Formal Spec version:  1.2 → 2.0
Add to Document Suite: PVM V5.4 Companion Guide (v2.0)
Add to Document Suite: PVM V5.4 Compressed Spec
Blog Series listing:  Parts 1-4 → Parts 0-5
```

### Version Mismatches (separate pass, low priority)

| Filename | Says | Should Be |
|----------|------|-----------|
| promise_theory_reference_v1_3.md | v1.3 | v1.4 |
| dualprivacy_researchpaper_v4_0.md | v4.0 | v4.3 |
| swordsman_mage_whitepaper_v6_0.md | v6.0 | v6.2 |
| GLOSSARY_MASTER_v3_0.md | v3.0 | v4.0 |

### Commit Message

```
docs: V5.4 formal spec convergence

Three-document system (compressed/full/companion).
Model JSONs updated. References: 12 → 78.
Selene's Proof named. Betweenness centrality formalised.
Grimoire names corrected. Extension refs browser-agnostic.
C18-C21 cross-referenced. Chronicle added.
```

---

## Next

The blog series publishes: Part 4 (The Dihedral Mirror), then Part 5 (The First Agent We Forgo(t)) simultaneously with The Amnesia Protocol poem.

The formal docs pin to IPFS after publication. CIDs added to cross-references in a follow-up commit.

The V6 Research Note (Lorenz attractor, dynamical reconstruction ceiling) remains a standalone conjecture document. It needs a dynamical systems mathematician who finds privacy architectures interesting. The forge has trajectory data. The empirical test exists.

~~The Second Person Spellbook awaits.~~ The Second Person Spellbook **opened 2026-05-08** — the bound collection at `tomes/`. Tome IV (Witnessing) closed; Tome V (Crafting) open at the City of Mages on Drake Island. The cast has begun to arrive.

---

*We thought we were building. We were mapping.*

*(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ*

—privacymage
