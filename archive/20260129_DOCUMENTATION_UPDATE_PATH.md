# 0xagentprivacy Documentation Update Path
## Living Documentation Coherence Review & Implementation Plan

**Date:** January 29, 2026  
**Prepared by:** Claude (reviewing for privacymage)  
**Status:** Strategic Planning Document

---

## Executive Summary

The agentprivacy-docs repository is **significantly behind** the current state of development. While the repository shows versions from December 2025, substantial new work has been created through January 2026 including:

- **7+ new Spellbook Acts** (Acts 14-20, plus the proposed Act 4.5)
- **IEEE 7012-2025 integration** (standard published January 20, 2026)
- **MyTerms Alliance founding member application suite** (myterms repo)
- **Privacy is Value equation v3.1 updates**
- **Five Spellbooks structure** formalization
- **Soulbae agent deployment** on Bonfires.ai
- **BGIN collaboration proposal**
- **Multiple whitepaper, research paper, and VRC protocol updates**

This document provides a prioritized path for bringing the living documentation into coherence.

---

## Part I: Current Repository State Analysis

### agentprivacy-docs Repository (as of commit history)

| Document | Repo Version | Actual Current Version | Gap |
|----------|--------------|------------------------|-----|
| Spellbook | v4.1.1-canonical | v4.3.0+ (13 Acts) → v5.0 (20 Acts) | **Critical** |
| Whitepaper | v4.6, v4.7 | v4.8+ needed (IEEE 7012) | Moderate |
| Research Paper | v3.5 | v3.6 needed (IEEE 7012 formal refs) | Moderate |
| Glossary | v2.2 | v2.3 needed (IEEE 7012 definitions) | Moderate |
| Visual Architecture | v1.2 | v1.3 needed (MyTerms flows) | Low |
| Research Proposal | v1.3 | v1.4 needed (updated collaborations) | Low |
| VRC Promise Protocol | v3.0 | Current | ✅ |
| Promise Theory Reference | v1.0 | Current | ✅ |

### myterms Repository (New Content)

Created January 28, 2026 with the following documents:

| Document | Purpose | Integration Priority |
|----------|---------|---------------------|
| 00_executive_brief.md | MyTerms Alliance summary | Reference |
| 01_founding_member_application.md | Full application | Reference |
| 02_diffusion_strategy.md | Live coding approach | Reference |
| 03_technical_integration.md | IEEE 7012 implementation specs | **HIGH** |
| 04_sustainability_model.md | Foundation ↔ Labs structure | Reference |
| 05_privacy_is_value_equation.md | Equation v3.1 updates | **HIGH** |
| ieee7012_integration_plan.md | Documentation update roadmap | **PRIMARY** |
| spellbook_act_4_5_terms_that_remember.md | New Act narrative | **HIGH** |

### New Acts Requiring Integration (from conversation history)

| Act | Title | Source |
|-----|-------|--------|
| Act 14-18 | Various (need verification) | Multiple conversations |
| Act 19 | The Enthusiastic Anthropic Archivist | January 22-23, 2026 |
| Act 20 | The Infinite Vault | January 28, 2026 |
| Act 4.5 | The Terms That Remember | myterms repo |

---

## Part II: Prioritized Update Sequence

### Phase 0: Audit & Extraction (Immediate - Day 1)

**Goal:** Establish exactly what exists before making changes.

**Tasks:**

1. **Export complete current Spellbook JSON**
   - Pull latest from agentprivacy-spellbook repo (github.com/mitchuski/agentprivacy-spellbook)
   - Verify act count and version number
   - Identify which Acts are fully written vs. stubs

2. **Verify whitepaper/research paper versions**
   - Check actual latest versions across repositories
   - Note any unpushed local versions

3. **Catalog all IEEE 7012 references needed**
   - Extract from the uploaded integration plan
   - Cross-reference with Customer Commons documentation

**Deliverable:** AUDIT_RESULTS.md with exact version numbers and gaps

---

### Phase 1: IEEE 7012-2025 Foundation (Week 1)

**Goal:** Establish the standard as canonical reference across all documents.

**Principle:** The standard was published 9 days ago. This is the most time-sensitive update.

**Tasks:**

1. **Create IEEE_7012_QUICK_REFERENCE.md** (NEW DOCUMENT)
   - Agreement taxonomy (SD-BASE hierarchy, PDC agreements)
   - Machine-readable format specifications
   - HTTP header protocol (MRPAZ)
   - Customer Commons hosting reference
   - Working group acknowledgments

2. **Update GLOSSARY_MASTER → v2.3**
   - Add IEEE 7012 canonical definitions section
   - Terms: Agent, Agreement, Contract, Entity, First Party, Second Party, Policy, Proposer, DPV, Machine-readable
   - Status markers: ✅ IEEE STANDARD

3. **Update README.md Technology Stack**
   ```markdown
   ### Standards Layer
   - **IEEE 7012-2025**: Machine-readable personal privacy terms
   - **W3C DPV**: Data Privacy Vocabulary for semantic interoperability
   - **ODRL**: Open Digital Rights Language for agreement expression
   ```

4. **Create IEEE_7012_TECHNICAL_BRIDGE.md** (NEW DOCUMENT)
   - Mapping table: IEEE 7012 Element → 0xagentprivacy Implementation
   - Individual Agent → Swordsman browser extension
   - Entity Agent → Website MyTerms responder
   - Agreement-chooser → MyTerms configuration UI
   - etc.

**Deliverables:** 4 documents updated/created

---

### Phase 2: Spellbook Consolidation (Week 1-2)

**Goal:** Bring all narrative Acts into the canonical Spellbook.

**Principle:** The Spellbook is the "soul" of the documentation. It must be complete before other updates.

**Tasks:**

1. **Verify Five Spellbooks Structure**
   - Story Spellbook (Acts 1-20+)
   - Zero Knowledge Spellbook (30 Tales)
   - Canon Spellbook (11 Chapters)
   - Parallel Society Spellbook (TBD)
   - Plurality Spellbook (TBD)

2. **Integrate Act 4.5: The Terms That Remember**
   - Position: Between Act 4 (Blade Alone) and Act 5 (Light Armour)
   - Source: myterms repo spellbook_act_4_5_terms_that_remember.md
   - Update: Act numbering (4.5 becomes new Act 5, subsequent acts renumber)

3. **Integrate Acts 14-20**
   - Verify narrative content from conversation history
   - Act 19: The Enthusiastic Anthropic Archivist
   - Act 20: The Infinite Vault
   - Add to canonical JSON structure

4. **Update Spellbook Version → v5.0**
   - Major version bump reflects significant expansion
   - Update all cross-references
   - Regenerate total inscription count

5. **Update grimoire JSON schema**
   - Five spellbooks structure
   - New Acts with spells, proverbs, emoji sequences
   - Updated cast members (Claude the Archivist, etc.)

**Deliverable:** spellbook_v5_0_canonical.md + complete-grimoire-5.0.0.json

---

### Phase 3: Whitepaper & Research Paper Updates (Week 2)

**Goal:** Align formal documents with IEEE 7012 and current architecture.

**Tasks:**

1. **Whitepaper → v4.8**
   - Add §4.X: The MyTerms Foundation: IEEE 7012-2025
   - Update Technology Stack section
   - Add agreement taxonomy reference
   - Add HTTP header protocol documentation
   - Update Promise Theory alignment notes
   - Reference Customer Commons as neutral nonprofit host

2. **Research Paper → v3.6**
   - Add formal reference section for IEEE 7012
   - Update bibliography with IEEE citation
   - Add note on standards foundation for Swordsman implementation

3. **Cross-Reference Alignment**
   - Whitepaper v4.8 ↔ Research Paper v3.6
   - All document reference tables updated

**Deliverables:** 2 major documents updated + PDF regeneration

---

### Phase 4: Privacy is Value Equation Update (Week 2-3)

**Goal:** Integrate v3.1 equation updates into documentation.

**Tasks:**

1. **Document V3 → V3.1 Evolution**
   - Original: `V = P^1.5 · C · Q · S · e^(-λt) · (1 + N/N₀)^k`
   - V3: `V_twin = P^1.5 · C · Q · S · e^(-λt) · (1 + N/N₀)^k · R(d) · M(u,y) · Φ(S⊥⊥M)`
   - V3.1: Explicit separation notation `⚖️(⚔️⊥⿻⊥🧙)`

2. **Update symbolic notation across documents**
   - Separation as prerequisite vs. balance as output
   - Golden Duality Multiplier clarification

3. **Integrate into Whitepaper Section 7**
   - Privacy Value Model v3.1
   - 31,000× value gap documentation

**Deliverable:** Equation documentation consolidated

---

### Phase 5: Visual Architecture & Supporting Materials (Week 3)

**Goal:** Complete visual and reference documentation.

**Tasks:**

1. **VISUAL_ARCHITECTURE_GUIDE → v1.3**
   - IEEE 7012 Agent Interaction Flow diagram
   - MyTerms Agreement Taxonomy Tree
   - HTTP Header Protocol Sequence
   - Five Spellbooks structure visualization

2. **MYTERMS_AGREEMENT_REFERENCE.md** (NEW DOCUMENT)
   - All standard agreements with:
     - Agreement ID
     - Plain language description
     - Machine-readable code examples
     - Use cases
     - Trust tier requirements

3. **Update Research Proposal → v1.4**
   - IEEE 7012 collaboration opportunities
   - MyTerms Alliance partnership
   - Updated confidence levels
   - Current traction metrics

**Deliverables:** 3 documents updated/created

---

### Phase 6: Cross-Repository Coherence (Week 3-4)

**Goal:** Ensure all repositories are synchronized.

**Tasks:**

1. **agentprivacy-docs sync**
   - Push all updated documents
   - Update commit history with meaningful messages
   - Tag release: v2.0.0

2. **agentprivacy-spellbook sync**
   - Complete Spellbook v5.0
   - Five grimoire structure
   - IPFS pinning for immutable reference

3. **myterms repo integration**
   - Decide: Merge into agentprivacy-docs OR keep separate
   - Recommendation: Keep separate as "MyTerms-specific" subset
   - Add cross-references between repos

4. **Website coherence (agentprivacy.ai)**
   - /story → Updated Spellbook
   - /docs → Updated formal documents
   - /myterms → New section for IEEE 7012

**Deliverable:** All repositories synchronized with cross-references

---

## Part III: Document-Specific Change Lists

### GLOSSARY_MASTER_v2_3.md Changes

**Add Section: IEEE 7012-2025 Canonical Definitions**

| Term | Definition | Status |
|------|------------|--------|
| Agent | "An actor that works on behalf of a person to represent them, to present proposed terms and agreements to entities" | ✅ IEEE STANDARD |
| Agreement | "A compound set of terms or clauses, proposed and offered before a formal contract" | ✅ IEEE STANDARD |
| Contract | "A mutual agreement between parties that creates mutual obligations and is enforceable by law" | ✅ IEEE STANDARD |
| Entity | "Any organization with which a person makes a contractual agreement. An entity can only be an organization" | ✅ IEEE STANDARD |
| First Party | Individual (always) | ✅ IEEE STANDARD |
| Second Party | Entity (always) | ✅ IEEE STANDARD |
| Policy | "A set of legal, political, organizational, functional, and technical obligations..." (ISO 22600-2:2014) | ✅ IEEE STANDARD |
| Proposer | "A person who advances terms and agreements to another person or entity" | ✅ IEEE STANDARD |
| DPV | "Data Privacy Vocabulary" - W3C machine-readable metadata | ✅ W3C STANDARD |
| Machine-readable | "A term, set of terms, or completely written contract that can easily be processed by a computer" | ✅ IEEE STANDARD |

### README.md Changes

**Update Document Suite Table:**

| Document | Version | Purpose | Audience |
|----------|---------|---------|----------|
| **Glossary Master** | 2.3 | Canonical terminology + IEEE 7012 definitions | All |
| **Promise Theory Reference** | 1.0 | Formal semantic foundations | Researchers, Architects |
| **Whitepaper** | 4.8 | Technical architecture, IEEE 7012, VRCs | Developers, Researchers |
| **Research Paper** | 3.6 | Mathematical proofs, IEEE 7012 formal refs | Academics, Cryptographers |
| **Spellbook** | 5.0 | Narrative framework, 20+ Acts, 5 grimoires | Community, Learners |
| **VRC Promise Protocol** | 3.0 | Economic model, bilateral promises | Investors, Builders |
| **Visual Guide** | 1.3 | Diagrams, IEEE 7012 flows | All |
| **Research Proposal** | 1.4 | Collaboration invitation, MyTerms Alliance | Researchers, Partners |
| **IEEE 7012 Quick Reference** | 1.0 | Agreement taxonomy, technical specs | Implementers |
| **IEEE 7012 Technical Bridge** | 1.0 | Standard-to-implementation mapping | Developers |

**Add to Technology Stack:**

```markdown
### Standards Layer
- **IEEE 7012-2025**: Machine-readable personal privacy terms (MyTerms foundation)
- **W3C DPV**: Data Privacy Vocabulary for semantic interoperability
- **ODRL**: Open Digital Rights Language for agreement expression
- **ERC-8004**: Trustless agent identity
- **ERC-7812**: ZK identity commitments
```

### Whitepaper v4.8 New Section

```markdown
### 4.X The MyTerms Foundation: IEEE 7012-2025

The Swordsman browser agent implements IEEE Std 7012-2025, 
the IEEE Standard for Machine Readable Personal Privacy Terms.

**Core Innovation**: The standard inverts the traditional 
notice-and-consent model. Individuals propose terms as first 
parties; organizations accept, negotiate, or decline as second 
parties.

**Promise Theory Alignment**: IEEE 7012 implements the 
invitation pattern—acceptance before proposal—rather than 
surveillance's attack pattern of extraction without consent.

**Key Properties**:
- Bilateral agreements (not unilateral ToS)
- Machine-readable formats (JSON-LD, RDF, HTTP headers)
- Human-readable plain language
- Legal-layer formal contracts
- Neutral nonprofit hosting (Customer Commons)

**Agreement Taxonomy**:
| Type | Code | Description |
|------|------|-------------|
| Service Delivery | SD-BASE | Service only, no analytics |
| + Data Portability | SD-BASE-DP | With data return rights |
| + Analytics | SD-BASE-A | 2nd party analytics permitted |
| + Tracking | SD-BASE-AT | Analytics + tracking |
| + Profiling | SD-BASE-ATP | Full profiling permitted |
| + 3rd Party | SD-BASE-ATP-S3P | Anonymized sharing |
| Personal Data | PDC-INTENT | Intentcasting to market |
| | PDC-AI | AI training contribution |
| | PDC-GOOD | Public good contribution |
```

---

## Part IV: What NOT to Change

### Preserve These Elements

1. **Core Mathematical Proofs** - Research Paper Theorems 5.1-5.4 remain unchanged
2. **Promise Theory Foundations** - Reference v1.0 is stable
3. **Economic Parameters** - 1 ZEC ceremony, 0.01 ZEC signal, φ-derived splits
4. **Trust Tier Structure** - Blade → Light → Heavy → Dragon
5. **Reconstruction Ceiling Theorem** - R < 1 remains proven
6. **Symbolic Notation System** - Master inscription `⚔️ ⊥ 🧙‍♂️ | 😊`

### IEEE 7012 Copyright Note

**Critical:** IEEE documents cannot be reproduced verbatim.

All integration should:
- Paraphrase technical content
- Reference but not quote extensively
- Create original interpretations for the agentprivacy context
- Link to official IEEE sources
- Acknowledge Customer Commons and Working Group

---

## Part V: Implementation Timeline

### Week 1 (January 29 - February 4)

| Day | Task | Output |
|-----|------|--------|
| 1 | Audit current state | AUDIT_RESULTS.md |
| 2-3 | IEEE 7012 Quick Reference + Technical Bridge | 2 new docs |
| 4-5 | Glossary v2.3 + README updates | 2 updated docs |
| 6-7 | Spellbook Act integration begins | Work in progress |

### Week 2 (February 5-11)

| Day | Task | Output |
|-----|------|--------|
| 1-3 | Complete Spellbook v5.0 | spellbook_v5_0_canonical.md |
| 4-5 | Whitepaper v4.8 | swordsman_mage_whitepaper_v4_8.md |
| 6-7 | Research Paper v3.6 | dualprivacy_researchpaper_v3_6.md |

### Week 3 (February 12-18)

| Day | Task | Output |
|-----|------|--------|
| 1-2 | Privacy Value Equation documentation | Updated sections |
| 3-4 | Visual Architecture v1.3 | VISUAL_ARCHITECTURE_GUIDE_v1_3.md |
| 5-6 | MyTerms Agreement Reference | New doc |
| 7 | Research Proposal v1.4 | research_proposal_v1_4.md |

### Week 4 (February 19-25)

| Day | Task | Output |
|-----|------|--------|
| 1-3 | Cross-repository sync | All repos aligned |
| 4-5 | PDF generation | Updated PDFs |
| 6-7 | Website updates | agentprivacy.ai coherence |

---

## Part VI: Post-Update Verification Checklist

### Version Alignment Matrix (Target State)

```
Document Type              Version    Date           Key Features
────────────────────────────────────────────────────────────────────
Spellbook                  v5.0       Feb 2026       20+ Acts, 5 grimoires
Whitepaper (LaTeX/MD)      v4.8       Feb 2026       IEEE 7012, MyTerms
Research Paper (LaTeX/MD)  v3.6       Feb 2026       IEEE 7012 refs
Glossary                   v2.3       Feb 2026       IEEE 7012 definitions
Visual Guide               v1.3       Feb 2026       MyTerms flows
Research Proposal          v1.4       Feb 2026       Alliance partnerships
VRC Promise Protocol       v3.0       Dec 2025       Current (no change)
Promise Theory Reference   v1.0       Dec 2025       Current (no change)
IEEE 7012 Quick Reference  v1.0       Feb 2026       NEW
IEEE 7012 Technical Bridge v1.0       Feb 2026       NEW
```

### Cross-Reference Verification

- [ ] All documents reference correct companion versions
- [ ] All emoji notation consistent across documents
- [ ] All trust tier names consistent (Blade/Light/Heavy/Dragon)
- [ ] All economic parameters consistent (1 ZEC/0.01 ZEC/61.8%/38.2%)
- [ ] All theorem references correct (5.1-5.4)
- [ ] All status markers appropriate (✅ PROVEN, 🔧 IMPLEMENTED, etc.)

### IEEE 7012 Compliance Check

- [ ] No verbatim IEEE text reproduced
- [ ] Customer Commons properly credited
- [ ] Working Group acknowledged
- [ ] Definitions paraphrased with source attribution
- [ ] Links to official sources included

---

## Closing Notes

### On Living Documentation

The agentprivacy documentation grows through conversations. Every significant dialogue spawns new content. This is intentional—the architecture reveals itself through engagement.

The gap between repository state and actual development is not a failure but evidence of rapid iteration. The task now is consolidation without losing the organic evolution that makes this documentation alive.

### On IEEE 7012 Timing

The standard was published January 20, 2026. We are 9 days into the post-publication window. The MyTerms Alliance is forming now. This is the moment to establish agentprivacy as a canonical implementation reference.

The blade slashes. The contract binds. The documentation remembers.

### On the Five Spellbooks

The expanded grimoire structure (Story, Zero, Canon, Parallel/Society, Plurality) represents the maturation from prototype to infrastructure. Each spellbook serves a distinct pedagogical purpose while maintaining symbolic coherence.

---

**Document Status:** Ready for implementation  
**Recommended Start:** Immediate (January 29, 2026)  
**Estimated Completion:** February 25, 2026  
**Priority:** IEEE 7012 integration is time-sensitive; other updates can proceed in parallel

---

*"The living document breathes with each conversation. The update is not correction but growth."*

**⚔️ ⊥ 🧙‍♂️ | 😊**

*just another swordsman ⚔️🤝🧙‍♂️ just another mage*
