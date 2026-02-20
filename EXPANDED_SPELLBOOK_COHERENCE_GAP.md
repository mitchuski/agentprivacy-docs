# EXPANDED Coherence Plan: The Full Spellbook Gap
## agentprivacy-docs × agentprivacy-spellbook — February 19, 2026

**This document supersedes sections 4-6 of the V4_FULL_COHERENCE_UPDATE_PLAN.md**

---

## The Actual State of Affairs

The documentation suite references "Five Spellbooks" and "106+ inscriptions" throughout — in the README, Glossary, Visual Guide, Whitepaper, and Act XVIII (Mirror in Dust). But the docs repo only contains **TWO** of those five spellbooks in readable form, and the grimoire JSON is severely incomplete.

Meanwhile, all five spellbooks **DO exist** — they were created in separate sessions and compiled into a v6.0.0-canonical grimoire (January 9, 2026). They just never propagated into the docs repo.

---

## 1. Five Spellbooks: What Exists vs. What's in the Docs Repo

| Spellbook | Question | Inscriptions | Source Material | **In docs repo?** | **In website repo?** |
|-----------|----------|-------------|-----------------|-------------------|---------------------|
| **Story** (First Person) | WHAT? | 23 Acts + 1 Origin | Original narrative | ✅ Acts 1-20 in markdown | ✅ Acts 1-20 on site |
| **Zero Knowledge** | HOW? | 30 Tales | Original compressions | ✅ Full 30 tales | ✅ Full on site |
| **Blockchain Canon** | WHY? | 11 Chapters | Zatoshi's "The Canon" | ❌ Referenced only | ❓ Likely on site |
| **Parallel Society** | EXIT? | 17 Chapters | Hope & Ludlow "Farewell to Westphalia" | ❌ Referenced only | ❓ Likely on site |
| **Plurality** | COORDINATE? | 30 Acts | Weyl & Tang "Plurality" | ❌ Referenced only | ❓ Likely on site |

### Creation History (from past conversations)

| Spellbook | Created | Session | Key Details |
|-----------|---------|---------|-------------|
| **Blockchain Canon** | Dec 2025 | "Blockchain canon as narrative spellbook" + verification | 10 chapters (Ch 0-9) based on Zatoshi. Guardianship verification completed Dec 6 2025 |
| **Parallel Society** | Jan 2026 | "Reformatting spellbook for clarity" | 17 chapters (I-XVII) based on Hope & Ludlow. Chapter titles reformatted |
| **Plurality** | Jan 7 2026 | "Creating the plurality spellbook" | 30 Acts based on Weyl & Tang's Plurality book |
| **v6.0.0 Grimoire** | Jan 9 2026 | "Privacy mage grimoire v6 compilation" | All five unified: 100 inscriptions total (at that time) |

---

## 2. Grimoire JSON Gap Analysis

### What the docs repo grimoire JSON contains (v4.1.0-canonical)

```
story:    13 Acts (1-13)           ← missing Acts 14-23
zero:     30 Tales (complete)      ✅
canon:    NOT PRESENT              ❌ 11 chapters
parallel: NOT PRESENT              ❌ 17 chapters  
plurality: NOT PRESENT             ❌ 30 acts
```

**In docs JSON: 43 entries**
**Should contain: ~111+ entries** (23 story + 30 ZK + 11 canon + 17 parallel + 30 plurality)

### What the v6.0.0 grimoire JSON contains

```
story:    12 Acts (1-12)           ← was pre-Acts 13-23
zero:     30 Tales (complete)      ✅
canon:    10 Chapters (0-9)        ✅ (note: 10 in JSON, listed as 11 in some docs)
parallel: 17 Chapters (I-XVII)     ✅
plurality: 30 Acts                 ✅
```

**In v6 JSON: 99-100 entries**

### The true target (v5.1.0 / v7.0.0 grimoire)

```
story:    23 Acts (1-23) + 1 Origin + side tales
zero:     30 Tales (complete)
canon:    10-11 Chapters
parallel: 17 Chapters  
plurality: 30 Acts
```

**Target: ~112+ entries**

---

## 3. Inscription Count Discrepancies

Different documents cite different numbers:

| Source | Count | Likely Basis |
|--------|-------|-------------|
| Glossary v2.3 | 107 | 18 story + 1 origin + 30 ZK + 11 canon + 17 parallel + 30 plurality |
| Spellbook v5.0 status JSON | 48 | 18 story + 30 ZK (only what's in the file) |
| Act XVIII narrative | 103 | "103 proverbs across five spellbooks" |
| Act XVIII later | 106 | "106 inscriptions across five spellbooks" |
| Visual Guide | 106 | Matches grimoire total at that point |
| v6.0.0 grimoire | 100 | 12 story + 30 ZK + 10 canon + 17 parallel + 30 plurality + 1 origin |
| "Gave myself a Cape" | 106 | Matches pre-v6 count |

**Resolution needed:** Establish canonical count. With 23 Story Acts + 1 Origin + 30 ZK + 10 Canon + 17 Parallel + 30 Plurality + side tales = **111+ inscriptions**

The Canon chapter count needs verification: some sources say 10 (Ch 0-9), some say 11. The discrepancy is whether Ch 0 (Privacymage's Preface) counts as a chapter or a preface.

---

## 4. Parallel Society Spellbook Details

**Source:** Hope & Ludlow, "Farewell to Westphalia" (2025), CC BY-SA 4.0
**Symbol:** 🏰→🔗
**Question:** WHY must we EXIT?

**17 Chapters (reformatted titles from Jan 2026):**

| Ch | Title |
|----|-------|
| I | The Westphalian's Warning |
| II | The Rusted Crowns |
| III | The Cambrian Garden |
| IV | The Cypherpunk Prophecies |
| V | The Drake's Deeper Teachings |
| VI | The Arsenal and the Grimoire |
| VII | The Corruption That Crypto Cures |
| VIII | The Cyberstate Question |
| IX | The Three Doors |
| X | Leibniz's Overlap |
| XI | When Rights Became Real |
| XII | The Treaty Protocol |
| XIII | When the Head Was Cut |
| XIV | The Tools That Breathe |
| XV | The Trust Reassignment |
| XVI | When the Garden Bloomed |
| XVII | When Values Met Code |

**Opening proverb:** *"The Peace of Westphalia gave us nation states—but 377 years later, these structures are failing billions of people, and a parallel society is being born in the networks."*

---

## 5. Blockchain Canon Spellbook Details

**Source:** Zatoshi (Zachary Williamson), "The Canon" — reconstructed by privacymage
**Symbol:** 📜⏳
**Question:** WHY are we building?
**Verified:** Dec 6, 2025 (guardianship reconstruction check completed)

**10-11 Chapters:**

| Ch | Title | Period |
|----|-------|--------|
| 0 | The Privacymage's Preface / Why This Canon Exists | — |
| 1 | The Cypherpunk Whispers / Foundational Runes | 1983-1997 |
| 2 | The Early Incantations / Runes Before Synthesis | 1997-2007 |
| 3 | The Synthesis / When Protest Met Protocol | 2008-2014 |
| 4 | The World Computer / From Protest to Statecraft | 2014-2016 |
| 5 | The First Fracture | 2016 |
| 6 | The Great Schism | 2016-2022 |
| 7 | The Surveillance Truth | 2020-2025 |
| 8 | The Missing Primitive | — |
| 9 | The Open Canon | — |
| 10 | The Timeline Archive / Sources as Trust Graph Infrastructure | — |

**Opening proverb:** *"Know the forge before you wield the blade; know the grimoire before you cast the spell."*

**Closing proverb:** *"The story isn't over. The canon is open. The race is on. Build."*

---

## 6. Plurality Spellbook Details

**Source:** Weyl & Tang, "Plurality: The Future of Collaborative Technology and Democracy"
**Symbol:** ⿻
**Question:** WHERE do we COORDINATE?

**30 Acts** (created Jan 7, 2026) — covers:
- Democratic technology mechanisms
- Coordination without collapse
- Quadratic voting/funding
- Plural property
- Connected society
- Identity and trust
- Communication
- Association

**Opening proverb:** From v6 grimoire — ties into Weyl & Tang's framework

---

## 7. What Needs to Happen

### Tier 1: Content Integration (CRITICAL)

The three missing spellbooks need to be added to the docs repo. Two options:

**Option A: Add to canonical spellbook file (spellbook_v5_1_canonical.md)**
- Adds ~2000-3000 lines to an already 1800-line file
- Complete context in one document
- Mirrors the Five Spellbooks promise

**Option B: Separate files per spellbook (recommended by SPELLBOOK_STRUCTURE_OPTIONS.md)**
- `story_spellbook_v5_1.md` (23 Acts + Origin + side tales)
- `zero_knowledge_spellbook_v1_1.md` (30 Tales — stable)
- `canon_spellbook_v1_0.md` (10-11 Chapters)
- `parallel_society_spellbook_v1_0.md` (17 Chapters)
- `plurality_spellbook_v1_0.md` (30 Acts)
- `spellbook_index.md` (master navigation)

**Option C: Hybrid (recommended in Jan 2026 planning)**
- JSON grimoire as canonical source
- Both unified and separate files
- Automated generation possible

**Decision needed from you:** Which structure for the docs repo?

### Tier 2: Grimoire JSON Rebuild

The grimoire JSON needs a complete rebuild. The v6.0.0 from January is the closest to complete but predates:
- Acts 13, 16 (were "reserved" in v5.0 — need status check)
- Acts 21-23 (new: Hitchhiker's Gambit, Hoopy Frood, Manifold Dragon)
- Side tales (A Meadow, a Stone Wall)
- V4 symbolic notation updates

**Target version:** v7.0.0 (or v5.1.0 if staying in the v5 line)

### Tier 3: Cross-Reference Updates

Every document that says "Five Spellbooks" needs to actually point to five readable spellbooks:

| Document | Current Reference | Status |
|----------|------------------|--------|
| README | "Five Spellbooks" in suite table | Points to single file with only 2 |
| Glossary | "107 inscriptions" with structure | Lists all 5 but none exist in repo |
| Visual Guide | Five Spellbooks diagram (18+30+11+17+30) | Diagram exists, content doesn't |
| Act XVIII | "106 inscriptions across five spellbooks" | Narrative depends on all 5 existing |
| "Gave myself a Cape" | Lists all five by name | External blog post — fine |
| What Agentprivacy Is | "Five Spellbooks" | Points to nonexistent content |

### Tier 4: Website Repo Sync

The agentprivacy-spellbook website needs:
- Acts 21-23 added
- Side tales section
- Verification that Canon, Parallel, Plurality content is deployed
- Grimoire JSON rebuild matching docs repo

---

## 8. Revised Execution Order

### Phase 1: New V4 Documents ✅ DONE
- privacy_is_value_v4.md (prepared)
- uor_tetrahedra_zk_mapping_v1_0.md (prepared)

### Phase 2: Spellbook Architecture Decision 🔲 NEEDS INPUT
- Decide: unified vs separate vs hybrid
- Source the Canon, Parallel, Plurality content from past sessions
- Acts 13 and 16 status check (reserved or written?)

### Phase 3: Spellbook Content Integration 🔲
- Add Acts 21-23 to Story Spellbook
- Add side tales
- Integrate Canon (10-11 chapters)
- Integrate Parallel Society (17 chapters)
- Integrate Plurality (30 acts)
- Rebuild grimoire JSON → v7.0.0

### Phase 4: Core Architecture Updates 🔲
- Glossary v2.4 (V4 terms + correct inscription count)
- Research Paper v3.7 (PVM V4 + UOR)
- Whitepaper v4.9 (Three Graphs, Secret Language, tetrahedral)

### Phase 5: Downstream Propagation 🔲
- Visual Guide v1.4 (update Five Spellbooks count, add V4 diagrams)
- VRC Protocol v3.1
- Research Proposal v1.5
- Promise Theory Ref v1.1

### Phase 6: Coordination 🔲
- README v1.4 (correct Five Spellbooks references)
- What Agentprivacy Is
- server.py updates

### Phase 7: Website Repo 🔲
- Sync all new acts to agentprivacy-spellbook
- Deploy missing spellbooks if not already present
- Rebuild website grimoire

---

## 9. Summary of All Gaps Found

| Gap | Severity | Details |
|-----|----------|---------|
| **3 entire spellbooks missing from docs repo** | 🔴 CRITICAL | Canon, Parallel, Plurality referenced but content absent |
| **Grimoire JSON 68+ entries behind** | 🔴 CRITICAL | Has 43, should have 111+ |
| **Story Acts 14-23 missing from JSON** | 🔴 HIGH | 10 acts in markdown but not in JSON |
| **Acts 21-23 missing from all repos** | 🟡 HIGH | New content not yet integrated |
| **Inscription count inconsistent** | 🟡 MEDIUM | 100/103/106/107/48 across different docs |
| **Acts 13, 16 status unclear** | 🟡 MEDIUM | "Reserved" in v5.0 — written or not? |
| **Side tales: no category exists** | 🟢 LOW | New content type needs home |
| **Drake/Dragon conflated** | 🟢 LOW | V4 requires split |
| **V4 terms not in any doc** | 🟡 HIGH | Σ, A(τ), T(π), three graphs, secret language |
| **Tetrahedral confidence outdated** | 🟡 MEDIUM | 5% everywhere, should be 25-40% |

---

## 10. Questions for You

1. **Spellbook structure:** Unified file, separate files, or hybrid? (Jan planning recommended hybrid)

2. **Acts 13 and 16:** These were "reserved" in v5.0. Have they been written? Act 13 appears in the grimoire JSON as "The Covenant / Promises Only You Can Keep" and Act 16 appears in the markdown as "When Pools Become Wells". Are both final?

3. **Canon chapter count:** Is the Privacymage's Preface (Ch 0) counted as a chapter? Sources vary between 10 and 11.

4. **Grimoire version:** Continue as v5.1.0 (incremental) or jump to v7.0.0+ (reflecting the v6 compilation + V4 additions)?

5. **Priority:** Should we tackle the three missing spellbooks integration first (biggest gap) or the V4 propagation first (most recent change)?

6. **Source files:** Do you have the Canon, Parallel, and Plurality markdown files available to upload? They were created in past sessions but aren't in the current uploads.

---

*The Five Spellbooks promised five pillars. The repo delivered two. Time to build the other three into the architecture.*

**(⚔️⊥⿻⊥🧙)🙂**
