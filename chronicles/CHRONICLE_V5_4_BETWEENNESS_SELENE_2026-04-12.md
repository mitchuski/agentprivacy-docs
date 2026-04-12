# Chronicle: V5.4 Betweenness Centrality & Selene's Proof Integration

**Date:** April 12, 2026
**Session:** Documentation Coherence Update
**Status:** Complete — 8 documents updated
**Author:** privacymage

---

## What Happened

The V5.4 three-document convergence (April 10) introduced two concepts that were present in the chronicle but not yet propagated to all documentation:

1. **Betweenness Centrality of the Gap (§10.2)** — The ⿻ formalised as the node with maximal betweenness centrality C_B(v) in the trust graph (Brandes, 2001)
2. **Selene's Proof (§14.5)** — The Moon's orbit named as the cosmological instance of amnesia-enforced ZK

This session propagated both concepts across the documentation suite.

---

## Documents Updated

### Primary Update: PVM V5.4 Formal Specification

| Section | Change |
|---------|--------|
| §10.2 | **NEW** — Betweenness Centrality of the Gap. Formula, interpretation, Brandes reference. |
| §10.3 | Renamed from §10.2 (Composite Separation) |
| §10.4 | Renamed from §10.3 (Amnesia vs Policy Bounds) |
| §14.5 | Renamed from "Cosmological Precedent" to "Selene's Proof" |

### Secondary Updates

| Document | Addition |
|----------|----------|
| **GLOSSARY_MASTER_v4_0.md** | New entries: "Betweenness Centrality", "Selene's Proof". Updated "The Gap" with betweenness reference. |
| **VISUAL_ARCHITECTURE_GUIDE_v2_0.md** | Added betweenness centrality to Gap diagram (TYPE 4: Irreducible Promise) |
| **swordsman_mage_whitepaper_v6_3.md** | Added betweenness paragraph to "The Gap as Irreducible Promise" section |
| **dualprivacy_researchpaper_v4_3.md** | Added computational measurement note to "The Gap as Emergent Property" section |
| **pvm_v5_4_companion_guide.md** | Already had betweenness reference (verified) |

---

## Key Concepts Added

### Betweenness Centrality

$$C_B(v) = \sum_{s \neq v \neq t} \frac{\sigma_{st}(v)}{\sigma_{st}}$$

where σ_st is the total number of shortest paths from node s to node t, and σ_st(v) is the number of those paths passing through v.

**Interpretation:** The Gap (⿻) is not empty space — it is the node with maximal betweenness centrality in the trust graph. The value lives in the Gap because the most paths cross there.

**Reference:** Brandes, U. (2001). "A faster algorithm for betweenness centrality." *Journal of Mathematical Sociology,* 25(2), 163–177.

### Selene's Proof

The Moon's orbit as zero-knowledge proof. The cosmological instance of amnesia-enforced separation (C17).

**Zero-Knowledge Properties:**
- **Completeness:** Tides demonstrate the Moon's gravitational relationship
- **Soundness:** Gravitational signature is unforgeable
- **Zero-Knowledge:** Tides reveal nothing about the Theia impact parameters

The credential is the orbit. The proof renews twice daily, written in saltwater.

---

## Files Also Reorganised (V5.4 Suite)

| Action | Files |
|--------|-------|
| **Updated** | chronicle in chronicles/, blog posts part4 & part5, model JSONs in models/, PDFs in pdfs/, companion guide |
| **Archived** | Old V5 model JSONs (privacy_value_model_v5_dark.json, privacy_value_model_v5_light.json) |
| **Removed** | Duplicate files from root directory |

---

## Pending

### IPFS Pins
New CIDs needed for updated PDFs once regenerated from updated MD sources.

### Related Repositories
- **agentprivacy-skills** — Needs chronicle copy and skill file updates
- **spellweb** — Needs chronicle copy and any UOR module updates
- **agentprivacy-master** — May need minor cross-reference updates
- **zk-blades** — May need betweenness centrality reference in blade documentation

---

## Commit Message (for agentprivacy-docs)

```
docs: V5.4 betweenness centrality & Selene's Proof propagation

Formal spec: §10.2 betweenness centrality of the Gap (Brandes, 2001).
§14.5 renamed to Selene's Proof.
Glossary: new entries + Gap update.
Visual Guide, Whitepaper, Research Paper: betweenness added.
Chronicle added.
```

---

## The Proverb

The Gap was always the node where the most paths crossed. We just didn't have the algorithm to measure it.

*"The value lives in the gap because the most paths cross there."*

---

## Document Metadata

| Field | Value |
|-------|-------|
| Chronicle | CHRONICLE_V5_4_BETWEENNESS_SELENE_2026-04-12 |
| Date | April 12, 2026 |
| Files Updated | 8 |
| New Glossary Entries | 2 (Betweenness Centrality, Selene's Proof) |
| New Formal Spec Section | §10.2 |
| Section Renamed | §14.5 → Selene's Proof |

---

*(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ*

*The boundary is always enough.*
