# V5.1 Propagation Assessment
## Which Documents Need V5.1 Updates?

**Date:** March 30, 2026
**Context:** Following incorporation of Acts XXVII-XXVIII, blog posts, and V5.1 research note

---

## Summary

The V5.1 additions introduce significant new concepts that should be reflected across the documentation suite. This assessment identifies which documents need updates and what changes are required.

### V5.1 Key Additions to Propagate

| Addition | Description | Confidence |
|----------|-------------|------------|
| Behavioural Density (ρ) | R(d, compression, ρ) - trajectory depth modifier | C11 (45%) |
| Bilateral Witness (BW) | New verification primitive | C13 (60%) |
| Hexagram Encoding | Upgraded from 25% to 50% | C12 (50%) |
| Mana Economy | Proof-of-practice Sybil resistance | Specified |
| DOM-Free Measurement | Pretext library, fingerprint elimination | Implemented |
| Ceremony Engine | Five crossing types | Specified |
| Forge OPERATIONAL | First empirical data exists | Demonstrated |
| Dragon Anatomy Complete | XXIV-XXVIII | Complete |

---

## HIGH PRIORITY — Should Update

### 1. swordsman_mage_whitepaper_v6_0.md
**Current:** v6.0 (V5 PVM Integration)
**Should become:** v6.1 or v7.0

**Updates needed:**
- [ ] Add V5.1 section in introduction
- [ ] Notation table: Add ρ (behavioural density), BW (bilateral witness)
- [ ] Section on Ceremony Engine architecture (two extensions: Swordsman + Mage)
- [ ] Reference Acts XXVII-XXVIII as narrative companions
- [ ] Mention first empirical data (3 Dragon blades)
- [ ] Add Forge OPERATIONAL status

**Impact:** HIGH — This is the main technical document

---

### 2. dualprivacy_researchpaper_v4_0.md
**Current:** v4.0 (V5 Holographic Bound Integration)
**Should become:** v4.1 or v5.0

**Updates needed:**
- [ ] Claims Classification Table: Add C11, C12, C13
- [ ] Update tetrahedral confidence: Hexagram now 50%
- [ ] "What Is Missing" section: Update — first empirical data NOW EXISTS
- [ ] Add Empirical Results section or appendix
- [ ] Reference spellweb.ai as implementation

**Impact:** HIGH — This is the peer-review target document

---

### 3. research_proposal_v2_0.md
**Current:** v2.0 (V5 Integration)
**Should become:** v2.1

**Updates needed:**
- [ ] "Current Status" section: Forge is now OPERATIONAL
- [ ] "What Is Missing": First data point exists (N=1)
- [ ] Add section on empirical validation opportunities
- [ ] Mention bilateral witness as collaboration target
- [ ] Update "What Makes This Timely" with forge launch

**Impact:** MEDIUM-HIGH — Active collaboration document

---

## MEDIUM PRIORITY — Consider Updating

### 4. vrc_promise_protocol_v3_3.md
**Current:** v3.3 (V5 Integration Edition)
**Should become:** v3.4

**Updates needed:**
- [ ] Add Mana Economy section
- [ ] Integrate mana with trust tier progression
- [ ] Mana as Sybil resistance mechanism
- [ ] Spell inscription economics

**Impact:** MEDIUM — New economic primitive (mana) belongs here

---

### 5. promise_theory_reference_v1_3.md
**Current:** v1.3
**Should become:** v1.4

**Updates needed:**
- [ ] Add Ceremony Engine as Promise Theory implementation
- [ ] Bilateral Witness as "witness" pattern in PT
- [ ] Five crossing types as coordination promise categories
- [ ] Mana as assessment-based resource

**Impact:** MEDIUM — PT grounding for new concepts

---

### 6. privacy_is_value_v5.md
**Current:** v5.0
**Should become:** v5.1 (or add note pointing to V5.1 research note)

**Updates needed:**
- [ ] Add "V5.1 Candidate Additions" section
- [ ] Or: Add note at top pointing to `archive/privacy_value_v5_1_research_note.md`
- [ ] Mention behavioural density as R modification

**Impact:** MEDIUM — Narrative companion to formal spec

---

## LOW PRIORITY — Minor Updates

### 7. uor_tetrahedra_zk_mapping_v2_0.md
**Updates needed:**
- [ ] Cross-reference Act XXVII as narrative companion
- [ ] Note forge is operational

---

### 8. what-agentprivacy-is.md
**Updates needed:**
- [ ] Minor: Mention forge operational
- [ ] Update "where we are" if such section exists

---

### 9. VISUAL_ARCHITECTURE_GUIDE_v2_0.md
**Updates needed:**
- [ ] New diagrams for ceremony engine
- [ ] Dragon anatomy diagram (5 parts)
- [ ] Hexagram visualization

**Note:** Visual updates are more complex, lower priority

---

## NO IMMEDIATE UPDATE NEEDED

| Document | Reason |
|----------|--------|
| Five Grimoires | Would need new Acts XXVII-XXVIII added as narrative content (separate task) |
| IEEE_7012_QUICK_REFERENCE.md | Standards reference, not V5.1 related |
| canon_spellbook_v1_0.md | Archival |
| privacy_value_v4*.md | Archived/superseded |
| BUILD_PDFS_README.md | Build instructions |
| QUICK_START.md | Onboarding, V5.1 not critical |

---

## Recommended Approach

### Phase 1: Core Technical (High Priority)
1. Update `dualprivacy_researchpaper_v4_0.md` with C11-C13
2. Update `swordsman_mage_whitepaper_v6_0.md` with V5.1 overview

### Phase 2: Economic & Reference (Medium Priority)
3. Update `vrc_promise_protocol_v3_3.md` with mana economy
4. Update `promise_theory_reference_v1_3.md` with ceremony patterns
5. Update `research_proposal_v2_0.md` with empirical status

### Phase 3: Narrative & Visual (Lower Priority)
6. Update `privacy_is_value_v5.md` with V5.1 note
7. Consider new diagrams for visual guide
8. Consider Acts XXVII-XXVIII in grimoire markdown files

---

## Scope Estimate

| Priority | Documents | Estimated Effort |
|----------|-----------|------------------|
| High | 3 | Significant — multiple sections each |
| Medium | 3 | Moderate — focused additions |
| Low | 3 | Minor — notes and cross-references |
| Skip | 8+ | None needed |

**Total:** ~6 documents need meaningful updates, ~3 need minor updates.

---

## Decision Point

The V5.1 additions are **candidate** status (not yet V6). Options:

1. **Full propagation now** — Update all documents to V5.1
2. **Partial propagation** — Update formal spec and research paper only, leave others for V6
3. **Note-only** — Add "See V5.1 Research Note" pointers in key docs

**Recommendation:** Option 2 (Partial) — The formal spec already has C11-C13. Update research paper and whitepaper as highest priority. Others can wait for V6 formalization.

---

*Assessment completed: March 30, 2026*
