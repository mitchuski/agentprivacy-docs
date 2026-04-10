# Formal Spec Companion Guide: References

**Purpose:** Complete reference catalog for documents cited in `FORMAL_SPEC_COMPANION_GUIDE.md`
**Date:** April 10, 2026
**Status:** Reference document

---

## Primary Reference

### privacy_value_v5_formal_specification.md
- **Location:** `/privacy_value_v5_formal_specification.md`
- **Size:** 31KB
- **Version:** 1.4 (V10.0.0 Grimoire aligned, V5.3.2 Ceremony Complete)
- **Description:** The formal mathematical specification of the Privacy Value Model V5. Contains the complete equation, all term definitions, conjecture tracking (C1-C17), and implementation notes.
- **Used in Companion:** Throughout — this is the document the companion guide explains.

---

## Core Documentation

### what-agentprivacy-is.md
- **Location:** `/what-agentprivacy-is.md`
- **Size:** 14KB
- **Description:** Mission statement and foundational thesis. Introduces the 7th capital (behavioral capital), the architecture overview, and the core problem statement.
- **Used in Companion:** §1.1 (The 7th Capital), §9 (Reading Paths for Philosophers/Economists)
- **Key Concepts:** Seven capitals framework, behavioral extraction, First Person definition

### README.md
- **Location:** `/README.md`
- **Size:** 27KB
- **Version:** V10.0
- **Description:** Master overview of the documentation suite. Contains V10 status, document index, reading paths by audience, technology stack, and project mission.
- **Used in Companion:** §1.2 (The Window), Document Metadata
- **Key Concepts:** 2-3 year window, documentation structure, implementation status

---

## Technical Whitepapers

### swordsman_mage_whitepaper_v6_0.md
- **Location:** `/swordsman_mage_whitepaper_v6_0.md`
- **Size:** 98KB
- **Version:** 6.0
- **Description:** Complete technical architecture document. Covers Promise Theory foundations, dual-agent design, Swordsman and Mage specifications, and holonic persistence.
- **Used in Companion:** §2.1 (Swordsman and Mage), §5.2 (DIDs and Holonic Persistence), §10 (Quick Reference for A_h(τ))
- **Key Concepts:** Agent separation, protection vs delegation, territorial boundaries, holonic GUIDs

### SWORDSMAN_EXTENSION_WHITEPAPER.md
- **Location:** `/SWORDSMAN_EXTENSION_WHITEPAPER.md`
- **Size:** 23KB
- **Description:** Detailed specification of the Swordsman agent. Covers boundary-setting mechanics, protection promises, and defensive postures.
- **Used in Companion:** §2.1 (Swordsman and Mage)
- **Key Concepts:** Boundary enforcement, "no" as primitive, threshold guarding

### MAGE_EXTENSION_WHITEPAPER.md
- **Location:** `/MAGE_EXTENSION_WHITEPAPER.md`
- **Size:** 16KB
- **Description:** Detailed specification of the Mage agent. Covers delegation capabilities, projection mechanics, and diplomatic functions.
- **Used in Companion:** §2.1 (Swordsman and Mage)
- **Key Concepts:** Delegation patterns, "yes on behalf of" as primitive, external representation

### dualprivacy_researchpaper_v4_0.md
- **Location:** `/dualprivacy_researchpaper_v4_0.md`
- **Size:** 94KB
- **Version:** 4.0
- **Description:** Academic research paper with mathematical proofs. Contains information theory bounds, reconstruction ceiling theorems, and formal security analysis.
- **Used in Companion:** §2.2 (Generator and Solver), §9 (Reading Paths for Mathematicians/Security Researchers), §10 (Quick Reference for R)
- **Key Concepts:** Reconstruction ceiling, information-theoretic bounds, adversarial analysis

---

## Promise Theory

### promise_theory_reference_v1_3.md
- **Location:** `/promise_theory_reference_v1_3.md`
- **Size:** 36KB
- **Version:** 1.3
- **Description:** Reference document for Bergstra & Burgess (2019) Promise Theory. Explains semantic foundations, Generator/Solver as promises, and autonomous agent coordination.
- **Used in Companion:** §3 (Promise Theory: The Semantic Foundation), §9 (Reading Paths for Philosophers)
- **Key Concepts:** Voluntary promises, unilateral commitments, observable verification, autonomy vs control

### External Reference: Bergstra & Burgess (2019)
- **Citation:** Bergstra, J. & Burgess, M. (2019). *Promise Theory: Principles and Applications.*
- **Description:** The foundational academic text on Promise Theory. External to the repository.
- **Used in Companion:** §3.1 (Why Promises Matter)

---

## Economic Architecture

### vrc_promise_protocol_v3_3.md
- **Location:** `/vrc_promise_protocol_v3_3.md`
- **Size:** 55KB
- **Version:** 3.3
- **Description:** Economic architecture specification. Covers Verifiable Relationship Credentials (VRCs), guild efficiency mechanics, and network economics.
- **Used in Companion:** §4.1 (VRCs), §4.2 (Guild Efficiency), §9 (Reading Paths for Economists), §10 (Quick Reference for G(guilds))
- **Key Concepts:** Bilateral commitments, relationship ownership, O(1) coordination, guild structure

### research_proposal_v2_0.md
- **Location:** `/research_proposal_v2_0.md`
- **Size:** 37KB
- **Version:** 2.0
- **Description:** Collaboration invitation and research roadmap. Contains confidence levels for conjectures C1-C10, investment case, and partnership opportunities.
- **Used in Companion:** §1.2 (The Window), §9 (Reading Paths for Economists)
- **Key Concepts:** Research agenda, confidence calibration, collaboration framework

---

## Standards Integration

### IEEE_7012_QUICK_REFERENCE.md
- **Location:** `/IEEE_7012_QUICK_REFERENCE.md`
- **Size:** 7KB
- **Description:** Quick reference for IEEE 7012-2025 (MyTerms standard). Explains machine-readable privacy terms and agent negotiation.
- **Used in Companion:** §5.1 (IEEE 7012-2025)
- **Key Concepts:** MyTerms format, machine-readable consent, automated negotiation

---

## Algebraic Foundations

### uor_tetrahedra_zk_mapping_v2_0.md
- **Location:** `/uor_tetrahedra_zk_mapping_v2_0.md`
- **Size:** 21KB
- **Version:** 2.0
- **Description:** Foundational mapping document. Connects UOR module, 64-tetrahedra lattice, and zero-knowledge encoding.
- **Used in Companion:** §9 (Reading Paths for Mathematicians), §10 (Quick Reference for Z/(2⁶)Z)
- **Key Concepts:** Lattice geometry, UOR convergence, algebraic structure

### SYSTEMS_HEXAGRAM_PHYSICS.md
- **Location:** `/SYSTEMS_HEXAGRAM_PHYSICS.md`
- **Size:** 19KB
- **Description:** Operational physics of the system. Covers UOR algebraic foundation, 64-vertex lattice, and hexagram encoding.
- **Used in Companion:** §10 (Quick Reference for P^1.5)
- **Key Concepts:** Hexagram structure, operational dynamics, I Ching correspondence

### understanding_as_key_zypher_paper_v1.md
- **Location:** `/understanding_as_key_zypher_paper_v1.md`
- **Size:** 52KB
- **Version:** 1.0
- **Description:** Conceptual framework positioning understanding as the key to reconstruction resistance.
- **Used in Companion:** §10 (Quick Reference for Holographic bound)
- **Key Concepts:** Understanding as primitive, comprehension verification, reconstruction resistance

---

## Implementation Specifications

### DUAL_TERRITORY_CEREMONY_SPEC_v1.md
- **Location:** `/DUAL_TERRITORY_CEREMONY_SPEC_v1.md` (also in `/specs/`)
- **Size:** 33KB
- **Version:** 1.0
- **Description:** Implementation architecture specification. Covers territories, extensions, ceremonies, and mana economics.
- **Used in Companion:** §9 (Reading Paths for Developers)
- **Key Concepts:** Territory model, ceremony execution, implementation patterns

### CEREMONY_INTEGRATION_GUIDE_v10_0_0.md
- **Location:** `/CEREMONY_INTEGRATION_GUIDE_v10_0_0.md`
- **Size:** 16KB
- **Version:** 10.0.0
- **Description:** Integration guide for ceremonial protocols. How to incorporate ceremonies into existing systems.
- **Used in Companion:** §9 (Reading Paths for Developers)
- **Key Concepts:** Integration patterns, ceremony hooks, system adaptation

### runecraft-protocol-spec-v1.md
- **Location:** `/runecraft-protocol-spec-v1.md`
- **Size:** 20KB
- **Version:** 1.0
- **Description:** Protocol specification for runecraft. Covers dual Ed25519 keypairs, key lifecycle, and bilateral binding.
- **Used in Companion:** §9 (Reading Paths for Developers), §10 (Quick Reference for Runecraft)
- **Key Concepts:** Ed25519 keys, Mage/Swordsman key separation, session destruction

---

## Ceremony Documentation

### ceremonies/ (directory)
- **Location:** `/ceremonies/`
- **Files:** 13 files
- **Description:** Complete ceremonial protocol documentation including acts 27-31, ceremony guides, and technical specs.
- **Used in Companion:** §6.1 (What Ceremonies Are), §10 (Quick Reference for Celestial Ceremony)

### TheCelestialDualCeremony☀️⊥🌙.md
- **Location:** `/TheCelestialDualCeremony☀️⊥🌙.md`
- **Size:** 20KB
- **Description:** Sun/Moon ceremonial protocols. Covers disclosure, reflection, pairing, and the Gap.
- **Used in Companion:** §6.1 (What Ceremonies Are)
- **Key Concepts:** Sun phase (disclosure), Moon phase (reflection), Gap (⊥), ceremonial cycle

---

## Zero-Knowledge & Forge

### zk_swordsman_blade_forge_v3_0.md
- **Location:** `/zk_swordsman_blade_forge_v3_0.md`
- **Size:** 32KB
- **Version:** 3.0
- **Description:** Zero-knowledge blade forging specification. Metaphor meets implementation for the forge system.
- **Used in Companion:** §6.2 (The Blade Forge), §9 (Reading Paths for Security Researchers)
- **Key Concepts:** Constellation selection, lattice traversal, SHA-256 commitment, blade tiers

### COHERENCE_REPORT_ZK_BLADES_FORGE.md
- **Location:** `/COHERENCE_REPORT_ZK_BLADES_FORGE.md`
- **Size:** 12KB
- **Description:** Validation report for forge integration and coherence across documentation.
- **Used in Companion:** §9 (Reading Paths for Security Researchers)
- **Key Concepts:** Coherence validation, integration status, forge verification

### reference/64_blades_reference_sheet.md
- **Location:** `/reference/64_blades_reference_sheet.md`
- **Description:** Reference sheet for all 64 possible blade configurations in the forge system.
- **Used in Companion:** §6.2 (The Blade Forge)
- **Key Concepts:** Blade configurations, dimensional combinations, tier properties

---

## Research Notes

### research/privacy_value_v5_3_research_note.md
- **Location:** `/research/privacy_value_v5_3_research_note.md`
- **Description:** Research note for V5.3. Covers path integral formulation, grid efficiency conjectures, and operational cycle.
- **Used in Companion:** §10 (Quick Reference for T_∫(π))
- **Key Concepts:** Path integral, "rewards the dance not the stance", T_∫(π) formulation

### research/ (directory)
- **Location:** `/research/`
- **Files:** 7 files
- **Description:** Research notes and formal models documenting Privacy Value evolution from V5.1 through V6 (speculative).
- **Used in Companion:** §9 (Reading Paths for Mathematicians)

---

## Narrative Documentation

### canon_spellbook_v1_0.md
- **Location:** `/canon_spellbook_v1_0.md`
- **Size:** 138KB
- **Version:** 1.0
- **Description:** The canonical narrative with 31 acts. First Person spellbook, now CLOSED. Complete story arc from beginning to first delegation.
- **Used in Companion:** §7.2 (The Five Grimoires), §9 (Reading Paths for Philosophers), Conclusion
- **Key Concepts:** 31-act structure, First Person journey, narrative completeness

### plurality_grimoire_v1_1.md
- **Location:** `/plurality_grimoire_v1_1.md`
- **Size:** 324KB
- **Version:** 1.1
- **Description:** Plurality-focused grimoire exploring many-to-many relationships and network structures.
- **Used in Companion:** §7.2 (The Five Grimoires)
- **Key Concepts:** Many-to-many, network plurality, collective sovereignty

### zk_grimoire_v3_0.md
- **Location:** `/zk_grimoire_v3_0.md`
- **Size:** 296KB
- **Version:** 3.0
- **Description:** Zero-knowledge proof explanations through story and metaphor. Makes ZK accessible.
- **Used in Companion:** §7.2 (The Five Grimoires)
- **Key Concepts:** ZK as narrative, proof storytelling, cryptographic intuition

### parallel_society_grimoire_v1_0.md
- **Location:** `/parallel_society_grimoire_v1_0.md`
- **Size:** 291KB
- **Version:** 1.0
- **Description:** Parallel society narratives and frameworks. Political and social implications of privacy architecture.
- **Used in Companion:** §7.2 (The Five Grimoires)
- **Key Concepts:** Alternative social structures, parallel institutions, exit vs voice

### privacymage_grimoire_v10_0_0.json
- **Location:** `/privacymage_grimoire_v10_0_0.json`
- **Size:** 257KB
- **Version:** 10.0.0
- **Description:** JSON-structured grimoire with complete system model. Machine-readable narrative.
- **Used in Companion:** §7.2 (The Five Grimoires)
- **Key Concepts:** Structured narrative, programmatic access, system model

---

## Blog Series

### blog/ (directory)
- **Location:** `/blog/`
- **Files:** 6 files
- **Description:** Sequential narrative blog series on Privacy Value evolution. Accessible entry point for general readers.
- **Used in Companion:** §7.3 (The Blog Series), §9 (Reading Paths for Philosophers)

### blog/blog-part0-the-myth-before-the-math.md
- **Description:** Mythological framing for the privacy value thesis.
- **Key Concepts:** Origin story, foundational metaphors

### blog/blog-part1-forming-constellations.md
- **Description:** Building the foundational concepts and vocabulary.
- **Key Concepts:** Sovereignty dimensions, constellation model

### blog/blog-part2-the-forge-and-the-ceremony.md
- **Description:** Implementation concepts through metaphor.
- **Key Concepts:** Forging process, ceremonial structure

### blog/blog-part3-the-dragon-wakes.md
- **Description:** System activation and emergent properties.
- **Key Concepts:** System convergence, dragon metaphor

### blog/blog-part4-the-dihedral-mirror.md
- **Description:** UOR Foundation convergence and algebraic confirmation.
- **Key Concepts:** D₆₄ group, mirror symmetry, independent validation

### blog/blog-part5-the-amnesia-protocol.md
- **Description:** Memory and forgetting as zero-knowledge primitive.
- **Key Concepts:** Structural amnesia, C17 conjecture, topology vs policy

---

## Visual & Architectural Guides

### VISUAL_ARCHITECTURE_GUIDE_v2_0.md
- **Location:** `/VISUAL_ARCHITECTURE_GUIDE_v2_0.md`
- **Size:** 168KB
- **Version:** 2.0
- **Description:** Comprehensive visual guide. Contains diagrams for three-axis separation, holographic visualizations, and dual-stack architecture.
- **Used in Companion:** §10 (Quick Reference for Φ terms)
- **Key Concepts:** Visual representations, architectural diagrams, spatial understanding

---

## Chronicles

### chronicles/CHRONICLE_MOON_PHASE_NOTATION.md
- **Location:** `/chronicles/CHRONICLE_MOON_PHASE_NOTATION.md`
- **Description:** Documentation of moon phase notation system for stratum encoding.
- **Used in Companion:** §10 (Quick Reference for Moon phases)
- **Key Concepts:** 🌑→🌕 encoding, visibility ratio, stratum mapping

### chronicles/ (directory)
- **Location:** `/chronicles/`
- **Files:** 10 files
- **Description:** Implementation and integration records tracking active development.
- **Used in Companion:** Referenced via specific chronicle files

---

## Glossary

### GLOSSARY_MASTER_v3_0.md
- **Location:** `/GLOSSARY_MASTER_v3_0.md`
- **Size:** 126KB
- **Version:** 3.0
- **Description:** Canonical terminology reference with 160+ entries. Includes V5.4 UOR Foundation terms.
- **Used in Companion:** §12 (Glossary Bridge)
- **Key Concepts:** All defined terms, canonical definitions, cross-references

---

## Poems

### poems/ (directory)
- **Location:** `/poems/`
- **Files:** 2 files
- **Description:** Poetic articulations of core concepts. Alternative epistemological access.
- **Used in Companion:** §9 (Reading Paths for Philosophers)

### poems/the-amnesia-protocol.md
- **Description:** Poetic exploration of amnesia as ZK primitive.

### poems/the-emissary-who-forgot-the-master-grace.md
- **Description:** Story form of the amnesia concept.

---

## External References

### UOR Foundation
- **URL:** https://github.com/UOR-Foundation
- **Description:** Independent project that arrived at Z/(2⁶)Z ring algebra from content addressing. Provides external validation of the 64-element structure.
- **Used in Companion:** §8.2 (What "Convergent" Means)
- **Key Concepts:** Universal Object Reference, independent convergence, algebraic validation

### BRAID Framework
- **Citation:** BRAID Framework (2026). Bounded Reasoning for Autonomous Inference and Decisions.
- **Description:** Framework providing compression efficiency data and Generator/Solver pattern.
- **Used in Companion:** §2.2 (Generator and Solver)
- **Key Concepts:** 74× compression, shared-parent coordination, reasoning graphs

---

## Document Relationship Map

```
FORMAL_SPEC_COMPANION_GUIDE.md
│
├── PRIMARY
│   └── privacy_value_v5_formal_specification.md
│
├── MISSION & CONTEXT
│   ├── what-agentprivacy-is.md
│   ├── README.md
│   └── research_proposal_v2_0.md
│
├── TECHNICAL ARCHITECTURE
│   ├── swordsman_mage_whitepaper_v6_0.md
│   ├── SWORDSMAN_EXTENSION_WHITEPAPER.md
│   ├── MAGE_EXTENSION_WHITEPAPER.md
│   └── dualprivacy_researchpaper_v4_0.md
│
├── SEMANTIC FOUNDATIONS
│   └── promise_theory_reference_v1_3.md
│
├── ECONOMICS
│   └── vrc_promise_protocol_v3_3.md
│
├── STANDARDS
│   └── IEEE_7012_QUICK_REFERENCE.md
│
├── ALGEBRA & GEOMETRY
│   ├── uor_tetrahedra_zk_mapping_v2_0.md
│   ├── SYSTEMS_HEXAGRAM_PHYSICS.md
│   └── understanding_as_key_zypher_paper_v1.md
│
├── IMPLEMENTATION
│   ├── DUAL_TERRITORY_CEREMONY_SPEC_v1.md
│   ├── CEREMONY_INTEGRATION_GUIDE_v10_0_0.md
│   └── runecraft-protocol-spec-v1.md
│
├── CEREMONIES & FORGE
│   ├── ceremonies/ (directory)
│   ├── TheCelestialDualCeremony☀️⊥🌙.md
│   ├── zk_swordsman_blade_forge_v3_0.md
│   ├── COHERENCE_REPORT_ZK_BLADES_FORGE.md
│   └── reference/64_blades_reference_sheet.md
│
├── RESEARCH
│   └── research/ (directory)
│       └── privacy_value_v5_3_research_note.md
│
├── NARRATIVE
│   ├── canon_spellbook_v1_0.md
│   ├── plurality_grimoire_v1_1.md
│   ├── zk_grimoire_v3_0.md
│   ├── parallel_society_grimoire_v1_0.md
│   └── privacymage_grimoire_v10_0_0.json
│
├── BLOG
│   └── blog/ (directory, 6 files)
│
├── VISUAL
│   └── VISUAL_ARCHITECTURE_GUIDE_v2_0.md
│
├── CHRONICLES
│   └── chronicles/ (directory)
│       └── CHRONICLE_MOON_PHASE_NOTATION.md
│
├── REFERENCE
│   ├── GLOSSARY_MASTER_v3_0.md
│   └── poems/ (directory)
│
└── EXTERNAL
    ├── UOR Foundation (GitHub)
    ├── BRAID Framework
    └── Bergstra & Burgess (2019)
```

---

## Reference Statistics

| Category | Count | Total Size |
|----------|-------|------------|
| Core Documents | 3 | ~72KB |
| Technical Whitepapers | 4 | ~231KB |
| Promise Theory | 1 + external | ~36KB |
| Economic Architecture | 2 | ~92KB |
| Standards | 1 | ~7KB |
| Algebraic Foundations | 3 | ~92KB |
| Implementation Specs | 3 | ~69KB |
| Ceremony Docs | 4 + directory | ~64KB+ |
| Research | 1 + directory | varies |
| Narrative (Grimoires) | 5 | ~1.3MB |
| Blog | 6 files | varies |
| Visual/Architecture | 1 | ~168KB |
| Chronicles | 1 + directory | varies |
| Glossary | 1 | ~126KB |
| Poems | 2 | varies |
| **Total Internal** | **~40 documents** | **~2.3MB+** |
| External References | 3 | N/A |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | April 10, 2026 | Initial creation |

---

*This reference document accompanies `FORMAL_SPEC_COMPANION_GUIDE.md` and `privacy_value_v5_formal_specification.md`*
