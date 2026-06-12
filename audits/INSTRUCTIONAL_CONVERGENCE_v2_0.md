# Instructional Convergence v2.0
## V5 Living Documentation Update Guide

**Version:** 2.0
**Date:** February 27, 2026
**Status:** Active — V5 Holographic Bound Integration Complete

---

## Purpose

This is the master guide for maintaining coherence across the 0xagentprivacy documentation suite. It defines:
1. The current canonical state (V5)
2. Document dependencies and update order
3. Terminology standards
4. Update procedures for future versions

---

## Current State: V5 Complete

All documents have been updated to V5 as of February 27, 2026. See `V5_AUDIT_CHECKLIST.md` for the detailed 111-item verification.

### V5 Canonical Concepts

| ID | Concept | Must Appear In |
|----|---------|----------------|
| V5-A | Three-axis separation (Φ_agent · Φ_data · Φ_inference) | Core equation docs, architecture docs |
| V5-B | Holographic bound (96/64 = P^1.5) | Core equation, UOR mapping, glossary |
| V5-C | Path integral T_∫(π) | Formal spec, research paper |
| V5-D | Compression-as-defence | BRAID references, glossary |
| V5-E | Holonic persistence A_h(τ) | Core equation, architecture docs |
| V5-F | Guild efficiency G(guilds) | VRC protocol, economics sections |
| V5-G | BRAID Parity Effect | Research paper, whitepaper |
| V5-H | Spellweb architecture | Glossary, visual guide |
| V5-I | Three identity layers | Formal spec, glossary |
| V5-J | Compression spectrum (7 layers) | Formal spec, visual guide |
| V5-K | Holonic Architect persona (☯️🔷) | Persona roster, glossary |
| V5-L | V5 equation (differential form) | Core equation docs |
| V5-M | Conjectures C6-C10 | Formal spec, research paper |
| V5-N | Version history updated | All versioned docs |
| V5-O | V5 spell notation | Spellbook, glossary |

---

## Document Suite Structure

### Tier 1: Core Equation (update first)

| Document | Current Version | Dependencies |
|----------|-----------------|--------------|
| `privacy_is_value_v5.md` | 5.0 | None — source of truth |
| `privacy_value_v5_formal_specification.md` | 1.0 (V5) | privacy_is_value |

### Tier 2: Architecture (update second)

| Document | Current Version | Dependencies |
|----------|-----------------|--------------|
| `dualprivacy_researchpaper_v4_0.md` | 4.0 | Core equation |
| `swordsman_mage_whitepaper_v6_0.md` | 6.0 | Core equation |
| `uor_tetrahedra_zk_mapping_v2_0.md` | 2.0 | Core equation |
| `promise_theory_reference_v1_3.md` | 1.3 | Core equation |

### Tier 3: Reference (update third)

| Document | Current Version | Dependencies |
|----------|-----------------|--------------|
| `GLOSSARY_MASTER_v3_0.md` | 3.0 | All concept docs |
| `README.md` | 2.0 | All docs |
| `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` | 2.0 | Architecture docs |
| `vrc_promise_protocol_v3_3.md` | 3.3 | Core equation |
| `research_proposal_v2_0.md` | 2.0 | Core equation, research paper |

### Tier 4: Narrative (update fourth)

| Document | Current Version | Dependencies |
|----------|-----------------|--------------|
| `first_person_grimoire_v3_0.md` | 3.0 | Core concepts |
| `spellbook_v5_0_canonical.md` | 5.0 | Grimoire |
| `what-agentprivacy-is.md` | 1.1 | High-level only |

### Tier 5: Tooling (rarely changes)

| Document | Current Version | Dependencies |
|----------|-----------------|--------------|
| `BUILD_PDFS_README.md` | 1.0 | None |
| `QUICK_START.md` | 1.0 | None |

---

## Terminology Standards

### Capitalisation

| Term | Correct | Incorrect |
|------|---------|-----------|
| Privacy Value Model | Privacy Value Model, PVM | privacy value model |
| Swordsman | Swordsman | swordsman, SWORDSMAN |
| Mage | Mage | mage, MAGE |
| Drake | Drake | drake |
| Holonic Architect | Holonic Architect | holonic architect |
| BRAID | BRAID | Braid, braid |
| VRC | VRC | vrc, Vrc |

### Symbols

| Symbol | Meaning | LaTeX |
|--------|---------|-------|
| Φ | Separation function | `\Phi` |
| τ | Temporal index | `\tau` |
| π | Path | `\pi` |
| ∂M | Boundary manifold | `\partial M` |
| ∫ | Path integral | `\int` |
| ☯️ | Holonic balance | emoji |
| 🔷 | Architect persona | emoji |

### Version References

When citing PVM version:
- Use "V5" not "v5" or "Version 5"
- Full form: "Privacy Value Model V5"
- Short form: "PVM V5"

---

## Update Procedure for Future Versions

### When to Create V6

Trigger conditions (any one):
1. Fundamental equation change (new terms, removed terms)
2. Major conjecture resolution (C6-C10)
3. Structural architecture change
4. New mathematical framework integration

### V6 Update Sequence

1. **Create `V6_AUDIT_CHECKLIST.md`** — enumerate all required changes
2. **Update Tier 1** — core equation documents first
3. **Update Tier 2** — architecture documents
4. **Update Tier 3** — reference documents
5. **Update Tier 4** — narrative documents
6. **Update this file** — INSTRUCTIONAL_CONVERGENCE to v3.0
7. **Update DOCUMENTATION_CHRONICLE** — add Arc 5
8. **Archive V5 checklist** — move to /archive with date prefix

### Change Validation

For each document update:
- [ ] All V(N) concept IDs addressed
- [ ] Version number bumped in document header
- [ ] Cross-references updated
- [ ] Glossary entries added/updated
- [ ] README document table updated

---

## Spellbook Architecture

### Five Spellbook Structure

| Spellbook | File | Purpose |
|-----------|------|---------|
| First Person | `first_person_grimoire_v3_0.md` | Narrative framework |
| Zero Knowledge | Separate file | ZK proof explanations |
| Technical Suite | Documentation folder | Formal specifications |
| Visual Architecture | `VISUAL_ARCHITECTURE_GUIDE_v2_0.md` | Diagrams and visuals |
| Canon Reference | `canon_spellbook_v1_0.md` | Canonical reference |

### Grimoire JSON Registration

New acts must be registered in:
1. `first_person_grimoire_v3_0.md` — act index table
2. `first_person_grimoire_entries_v3_0.json` — full JSON
3. `grimoire_v7_0_0.json` — metadata

Entry schema:
```json
{
  "act_number": "XXIV",
  "title": "The Holographic Bound",
  "inscription_count": 1,
  "persona": "Drake + Holonic Architect",
  "v5_concepts": ["V5-B", "V5-G", "V5-L"]
}
```

---

## Quick Reference: Active Files

### Root Directory (14 active documents)

```
agentprivacy-docs/
├── BUILD_PDFS_README.md
├── DOCUMENTATION_CHRONICLE.md      [NEW - history]
├── GLOSSARY_MASTER_v3_0.md
├── IEEE_7012_QUICK_REFERENCE.md
├── INSTRUCTIONAL_CONVERGENCE_v2_0.md  [THIS FILE]
├── QUICK_START.md
├── README.md
├── V5_AUDIT_CHECKLIST.md
├── V5_DOCUMENTATION_UPDATE_REVIEW.md
├── VISUAL_ARCHITECTURE_GUIDE_v2_0.md
├── dualprivacy_researchpaper_v4_0.md
├── first_person_grimoire_v3_0.md
├── privacy_is_value_v5.md
├── privacy_value_v5_formal_specification.md
├── promise_theory_reference_v1_3.md
├── research_proposal_v2_0.md
├── swordsman_mage_whitepaper_v6_0.md
├── spellbook_v5_0_canonical.md
├── uor_tetrahedra_zk_mapping_v2_0.md
├── vrc_promise_protocol_v3_3.md
├── what-agentprivacy-is.md
└── archive/                         [22 historical files]
```

---

## Coherence Checkpoints

Run these checks periodically:

### Cross-Reference Check
```
grep -r "v4" *.md | grep -v archive | grep -v CHRONICLE
```
Should return minimal results (only historical references).

### Version Consistency Check
```
grep -r "Version:" *.md | grep -v archive
```
All should show current versions.

### Glossary Coverage Check
Compare terms used in core docs against GLOSSARY_MASTER entries.

---

*This document supersedes INSTRUCTIONAL_CONVERGENCE_v1_0.md (archived)*
*Next update: When V6 is triggered*
