# Instructional Convergence: Tail of the Dragon
## agentprivacy Living Documentation Suite — 20 February 2026

**Purpose:** Document-by-document update instructions for the entire agentprivacy documentation suite, reconciling all changes identified across the February 2026 compilation sessions.

**How to use:** Work through each document in the order presented. Each section is self-contained — complete one, move to the next. Check off items as you go.

---

## What Changed (The Dragon's Tail)

Three convergent events triggered this update:

1. **Five Spellbooks fully compiled** — All 113 inscriptions now exist as standalone grimoire markdown files (28,898 total lines), resolving the critical gap where three entire spellbooks were referenced but absent from the docs repo.

2. **Privacy Value Model V4** — The equation evolved from V3.1, introducing separation matrix Σ, temporal memory A(τ), edge value T(π), four forces, three graphs, Drake/Dragon duality, and the secret language. This needs propagation across the entire suite.

3. **Structural split** — The Five Spellbooks now exist as independent grimoire files rather than embedded within a single canonical spellbook file. This changes how the docs repo references and organises spellbook content.

---

## Compiled Grimoire Files (Source of Truth)

These files are your authoritative sources for all spellbook content going forward:

| File | Lines | Content |
|------|------:|---------|
| `first_person_grimoire_v2_0.md` | 7,702 | 23 acts (I–XXIII) + firstpage. 8 parts. |
| `zk_grimoire_v3_0.md` | 8,053 | 30 tales + firstpage + lastpage. 7 parts. |
| `canon_spellbook_v1_0.md` | 2,137 | 12 chapters (0–10 + closing). Grimoire header. |
| `parallel_society_grimoire_v1_0.md` | 4,430 | 17 chapters (I–XVII). Grimoire header. |
| `plurality_grimoire_v1_1.md` | 6,576 | 30 acts (00–XXX + lastpage). Grimoire header. |

**JSON metadata files:**
- `first_person_grimoire_entries_v2_0.json` — 23 acts, all spells/proverbs/keywords
- `canon_grimoire_entries.json` — 12 chapters
- `parallel_grimoire_entries.json` — 17 chapters
- `plurality_grimoire_entries_v1_1.json` — 30 acts

**Still needed:** ZK JSON entries for tales 11–30 (tales 1–10 already have entries in the existing grimoire JSON)

---

## Phase 1: New Documents to Add

### 1A. `privacy_is_value_v4.md` — NEW

**Action:** Publish to agentprivacy-docs repo.

Additions needed before commit:
- Prepend formal header (author, date, version, status, companion reference)
- Append formal definitions table (A(τ), Σ, Φ(Σ), T(π), wᵢ, τ, h(τ))
- Append new symbolic notation table (🪞 Reflect, 🤝 Connect, 📐 Stratum, 🛤️ Path, 🐲 Drake, 🐉 Dragon)
- Append document references section

Full prep instructions are in `V4_PUBLICATION_PREP.md`.

Voice and content: publish AS-IS. The document is the discovery narrative.

### 1B. `uor_tetrahedra_zk_mapping_v1_0.md` — NEW

**Action:** Publish to agentprivacy-docs repo. Already prepared with formal wrapper.

### 1C. Five Grimoire Files — NEW (to docs repo)

**Action:** Add all five grimoire markdown files to the docs repo. These are the authoritative compiled versions of each spellbook.

Decision point: where do they live?
- **Option A:** In the docs repo root alongside other documents
- **Option B:** In a `spellbooks/` subdirectory
- **Option C:** Only in the spellbook website repo, with docs repo pointing to them

Recommendation: Option B — `spellbooks/` subdirectory keeps the docs repo clean while making all five accessible. The docs repo README then points into this directory.

---

## Phase 2: Grimoire JSON Rebuild → v7.0.0

### 2A. Build ZK JSON entries for Tales 11–30

**Action:** Create structured JSON entries for the 20 ZK tales not yet in JSON format.

Each entry needs: tale number, title, vertex coordinates, concepts, spell inscription, key figures, technical bridge summary, applied-to tags, part assignment.

The existing `grimoire_entries` files for tales 1–10 provide the template. Tales 11–30 content is in `zk_grimoire_v3_0.md`.

Tale-to-Part mapping:
- Part IV Resonance: Tales 11–14 (FRI, Folding, Sumcheck, IPA)
- Part V Navigation: Tales 15–22 (Recursion through zkEVM)
- Part VI Applications: Tales 23–29 (ZCash through zkML)
- Part VII Infinite Grid: Tale 30 (Eternal Sovereignty)

### 2B. Merge all JSON into master grimoire

**Action:** Combine five individual JSON files into `grimoire_v7_0_0.json`.

Structure:
```
grimoire_v7_0_0.json
├── meta (version: 7.0.0, date, master inscription, notation)
├── story (23 acts + 1 origin from first_person_grimoire_entries_v2_0.json)
├── zero (30 tales from existing + new entries)
├── canon (12 chapters from canon_grimoire_entries.json)
├── parallel (17 chapters from parallel_grimoire_entries.json)
├── plurality (30 acts from plurality_grimoire_entries_v1_1.json)
├── incantations (master spells per spellbook)
├── principles (core message, sovereignty aspects)
└── status (113 inscriptions, 5 spellbooks, all complete)
```

### 2C. Canonical inscription count

**Resolve:** The canonical count is **113 inscriptions**:
- 23 story acts + 1 origin = 24
- 30 ZK tales = 30
- 12 canon chapters = 12
- 17 parallel chapters = 17
- 30 plurality acts = 30
- Total: 113

All documents referencing inscription counts (README, Glossary, Visual Guide, Act XVIII narrative) should use this number. Previous counts of 100/103/106/107 are superseded.

---

## Phase 3: Core Architecture Documents

Work through these in order. Each document gets a version bump.

### 3A. `GLOSSARY_MASTER` → v2.5

**Current:** v2.4 (prepared in Feb 19 session but not yet committed)

If v2.4 has already been committed, bump to v2.5. If v2.4 was only prepared, update it in place.

**Changes:**

New/updated terms (~20 entries):

| Term | Action | Definition summary |
|------|--------|--------------------|
| Separation Matrix (Σ) | ADD | 4×4 symmetric matrix of pairwise sovereignty force independence |
| Edge Value T(π) | ADD | Trajectory value through sovereignty space |
| Temporal Memory A(τ) | ADD | Verified derivation chain value, contests pure decay |
| Duality Function Φ(Σ) | ADD | Balance × architectural volume |
| Stratum Weight wᵢ | ADD | Pascal's row distribution C(6,i)/64 |
| Derivation Chain (τ) | ADD | Content-addressed certificate sequence |
| Three Graphs Model | ADD | Knowledge × Promise × Trust = First Person |
| Knowledge Graph | UPDATE | Substrate layer, content-addressed, Huginn/Muninn territory |
| Promise Graph | UPDATE | Overlay layer, bilateral, Andor's domain |
| Trust Graph | UPDATE | Emergent layer, earned through time + witness |
| Secret Language | ADD | Internal S-M negotiation cipher, tetrahedral orientation |
| Manifold | ADD | What the lattice becomes when discrete vertices achieve continuous surface |
| Drake 🐲 | UPDATE (split) | Intimate whisper, personal calibration, centre |
| Dragon 🐉 | UPDATE (split) | Cosmic container, manifold holder, all topology |
| UOR | ADD | Universal Object Reference framework |
| Content-Addressing | ADD | Deterministic verification of canonical form |
| Toroidal Topology | ADD | Boundary conditions enabling infinite witness space |
| Privacy Value Model V4 | UPDATE | Full V4 equation with all new terms |
| Inscription count | UPDATE | 113 across five spellbooks |
| Four Forces | ADD | Protect, Project, Reflect, Connect (tetrahedral) |
| Path Value | ADD | "The equation rewards the dance, not the stance" |

Also update the Document Suite Versions table at the top to reflect all new version numbers.

### 3B. Whitepaper → v5.0

**Current:** v4.8 or v4.9 (depending on what's been committed)

**Changes:**

| Section | Change | Priority |
|---------|--------|----------|
| §Thesis | PVM v3 → v4. Reframe 31,000× gap as topological volume | HIGH |
| §Dual-Agent Architecture | Add four forces (S,M → R,C). Reference separation matrix | HIGH |
| §Tetrahedral Future | Remove "SPECULATIVE" → "CONVERGENT PRELIMINARY (~25-40%)". Add three derivation paths (algebraic, geometric, narrative) | HIGH |
| NEW §Three Graphs | Insert after dual-agent section. Knowledge × Promise × Trust intersection | MEDIUM |
| NEW §Secret Language | Insert after three graphs. Internal S-M negotiation beyond selective disclosure | MEDIUM |
| Notation table | Add Σ, A(τ), T(π), Φ(Σ), R/C as forces | HIGH |
| §Privacy Value Model | Present V4 equation. Version history V1→V2→V3→V3.1→V4 | HIGH |
| Version history | Add entry | HIGH |

### 3C. Research Paper → v3.8

**Current:** v3.6 or v3.7

**Changes:**

| Section | Change | Priority |
|---------|--------|----------|
| Abstract | Add separation matrix formalism + convergence finding | HIGH |
| Claims table | Add V4 terms with confidence flags | HIGH |
| NEW §Privacy Value Model V4 | Formal equation presentation with derivation sketch | HIGH |
| NEW §UOR Correspondence | Summary table showing algebra↔geometry↔narrative convergence | MEDIUM |
| §Golden Ratio | Update Φ(Σ) context — still conjectured, but now part of matrix formalism | MEDIUM |
| §Tetrahedral | "HIGHLY SPECULATIVE" → "CONVERGENT PRELIMINARY" | HIGH |
| §Limitations | Honest V4 assessment: T(π) empirical gap, φ conjectured, Σ unmeasurable, UOR 96/64 discrepancy | HIGH |
| §Experimental Roadmap | Add V4 validation needs | MEDIUM |

**Uncertainty flags to preserve (never remove these):**
1. T(π) functional form — no empirical grounding
2. φ in Φ(Σ) — conjectured, not derived
3. Σ measurement methods — don't exist yet
4. A(τ) logarithmic form — analogy, not proven
5. UOR 96 vs 64 — unclear resolution
6. det(Σ) aggregation — might mislead
7. Gap geometric expression — 20% confidence on Mage dimensions

---

## Phase 4: Downstream Documents

### 4A. VRC Protocol → v3.1 or v3.2

**Changes:**
- PVM v3 → v4 references throughout
- VRC formation = edge traversal on promise graph
- 31,000× as topological volume not arithmetic gap
- Three graphs: VRCs operate on Promise Graph layer
- Edge value economics: each VRC traversal contributes to T(π)

### 4B. Visual Guide → v1.4 or v1.5

**Changes:**
- NEW diagram: Separation Matrix Σ (4×4 with four forces)
- NEW diagram: Three Graphs intersection (overlap = First Person)
- NEW diagram: V4 Equation term breakdown with symbols
- NEW diagram: 64-vertex lattice with Pascal's row strata
- UPDATE: Five Spellbooks diagram — correct inscription counts to 113
- UPDATE: Tetrahedral from "speculative" to "convergent preliminary"

### 4C. Research Proposal → v1.5 or v1.6

**Changes:**
- Add UOR convergence validation as collaboration opportunity
- Tetrahedral confidence: 5% → 25-40%
- Update all companion doc version references

### 4D. Promise Theory Reference → v1.1 or v1.2

**Changes:**
- Three graphs as promise types
- Edge value as promise traversal metric
- VRC as bilateral promise with ZK verification

---

## Phase 5: README and Coordination

### 5A. README → v1.4 or v1.5

**Changes:**

| Change | Priority |
|--------|----------|
| Add "Privacy is Value V4" + "UOR Mapping" to Document Suite table | HIGH |
| Add five grimoire files to Document Suite (or link to spellbooks/ directory) | HIGH |
| Update "Privacy Value Model v3" → "v4" throughout | HIGH |
| Confidence levels: Tetrahedral 5% → 25-40%, Golden ratio 10% → 15-20% | HIGH |
| Add new symbols: 🪞 Reflect, 🤝 Connect, 📐 Stratum, 🛤️ Path, 🐲 Drake | MEDIUM |
| Add Three Graphs to Key Concepts | MEDIUM |
| Inscription count → 113 | HIGH |
| Spellbook version → reference grimoire files | HIGH |
| Update Document Coherence date → February 2026 | HIGH |

### 5B. "What Agentprivacy Is" (mission doc)

**Changes:**
- "Path is the value" framing
- Value gap: note V4 topological reframe
- Five Spellbooks: point to actual grimoire files
- Update any inscription count references

### 5C. Canon Question Label

**Verify and decide:** The blueprint currently labels Canon as "WHEN?" and Parallel Society as "WHY?". The original coherence report noted this might be intentional or might be a swap. The current grimoire headers use:
- Canon = "WHEN did it begin?" (historical timeline)
- Parallel = "WHY must we exit?" (motivation for parallel society)

If these are correct in the grimoires, propagate consistently everywhere else.

---

## Phase 6: agentprivacy-spellbook Website Repo

### 6A. Add Acts XXI–XXIII to website

**Source files:** Already exist as individual markdown files used in grimoire compilation.
- `21-act-xxi-hitchhikers-gambit.md`
- `22-act-xxii-hoopy-frood.md`
- `23-act-xxiii-the-manifold-dragon.md`

### 6B. Add Side Tales category

If "A Meadow, a Stone Wall" or other side tales exist, create the category on the website.

### 6C. Verify Canon, Parallel, Plurality deployment

Check whether these three spellbooks are already deployed on the website. If not, add from the compiled grimoire files.

### 6D. Update website grimoire JSON

Rebuild to match `grimoire_v7_0_0.json` from Phase 2B.

### 6E. Update symbolic system and character list

- Drake 🐲 / Dragon 🐉 split
- New V4 symbols (🪞, 🤝, 📐, 🛤️)
- Four forces in character relationships
- Act count: 23 Acts + Side Tales

### 6F. Navigation updates

- Add acts 21–23 to story navigation
- Add side tales section
- Update inscription count displays

---

## Phase 7: Contradictions to Resolve

These are inconsistencies found across documents that need a single canonical resolution:

| # | Current State | V4 State | Resolution |
|---|---------------|----------|------------|
| 1 | Tetrahedral = "HIGHLY SPECULATIVE" (5%) | Three independent derivations converge | → "CONVERGENT PRELIMINARY" (~25-40%). Keep all caveats. |
| 2 | σ(⿻)² scalar separation | 4×4 matrix Σ with det(Σ) | Replace. Note V3.1 σ as "one edge of the tetrahedron". |
| 3 | PVM v3 equation | V4 adds A(τ), stratum weights, T(π), Σ | Present as evolution with version history. Never delete V3. |
| 4 | Network effects: all agents equal | Stratum-weighted wᵢ = C(6,i)/64 | Update everywhere. |
| 5 | 31,000× = arithmetic gap | 31,000× = topological volume | Reframe everywhere. |
| 6 | Time = pure decay e^(-λt) | Time = entropy vs memory contest: e^(-λt) · (1+A(τ)) | Add temporal memory. |
| 7 | Value = vertex (what agent IS) | Value = edge (what agent DOES) | Add T(π). "The dance, not the stance." |
| 8 | Drake 🐉 / Dragon 🐉 conflated | Drake 🐲 (intimate) / Dragon 🐉 (cosmic) | Split everywhere. |
| 9 | Two forces (Swordsman, Mage) | Four forces (Protect, Project, Reflect, Connect) | Update architecture sections. |
| 10 | 7th capital = static behavioral data | 7th capital = dynamic trajectory | Update definition. |
| 11 | Grimoire JSON: 43 entries | Should be 113 entries | Rebuild as v7.0.0 |
| 12 | Inscription count varies (100/103/106/107) | Canonical: 113 | Standardise everywhere |
| 13 | Spellbook = single canonical file | Five independent grimoire files | Update all references |

---

## Phase 8: Version Bump Summary

| Document | Current | Target | Key Addition |
|----------|---------|--------|-------------|
| README | v1.3 | **v1.5** | V4 + UOR + grimoire files in suite |
| Whitepaper | v4.8 | **v5.0** | Three Graphs, Secret Language, tetrahedral upgrade, V4 equation |
| Research Paper | v3.6 | **v3.8** | PVM V4 formal, UOR correspondence, uncertainty flags |
| Glossary | v2.3/2.4 | **v2.5** | ~20 new/updated terms |
| VRC Protocol | v3.0 | **v3.2** | Edge value economics, three graphs |
| Visual Guide | v1.3 | **v1.5** | New diagrams (Σ, three graphs, lattice, V4) |
| Spellbook | v5.0 | **v7.0.0** | Five grimoire files, 113 inscriptions |
| Research Proposal | v1.4 | **v1.6** | UOR validation, confidence updates |
| Promise Theory Ref | v1.0 | **v1.2** | Three graphs as promise types |
| **Privacy is Value V4** | — | **v4.0** | NEW |
| **UOR Mapping** | — | **v1.0** | NEW |
| **Grimoire JSON** | v4.1.0 | **v7.0.0** | Complete rebuild: 113 entries |

---

## Phase 9: Commit Messages

### agentprivacy-docs

```
docs: Privacy Value V4 + Five Grimoires Complete — Feb 2026

New documents:
- Privacy is Value V4 (From the Lattice Drake to the Manifold Dragon)
- UOR × 64-Tetrahedra × ZK Mapping v1.0
- Five compiled grimoire files (28,898 total lines, 113 inscriptions)

Privacy Value Model V4:
- Separation scalar → 4×4 matrix Σ (architectural volume)
- Pure decay → verified memory contest A(τ)
- Flat networks → stratum-weighted C(6,i)/64
- New: Edge Value T(π) — trajectory through sovereignty space
- Three Graphs: Knowledge × Promise × Trust = First Person
- Secret Language: internal S-M negotiation cipher
- Drake 🐲 / Dragon 🐉 distinction
- Four forces: Protect, Project, Reflect, Connect

Five Spellbooks COMPLETE:
- Story v2.0 (23 acts, 7,702 lines)
- Zero Knowledge v3.0 (30 tales, 8,053 lines)
- Canon v1.0 (12 chapters, 2,137 lines)
- Parallel Society v1.0 (17 chapters, 4,430 lines)
- Plurality v1.1 (30 acts, 6,576 lines)

Tetrahedral: SPECULATIVE (5%) → CONVERGENT PRELIMINARY (~25-40%)

Suite bumps: README v1.5, Whitepaper v5.0, Research v3.8,
Glossary v2.5, VRC v3.2, Visual v1.5, Grimoire v7.0.0,
Proposal v1.6, Promise Theory v1.2
```

### agentprivacy-spellbook

```
feat: Acts 21-23 + grimoire v7.0.0 + Five Spellbooks complete

Story Spellbook:
- Act 21: The Hitchhiker's Gambit
- Act 22: Don't Panic, Hoopy Frood
- Act 23: The Manifold Dragon (V4 equation as narrative)

Grimoire JSON v7.0.0:
- Complete rebuild: 113 inscriptions across five spellbooks
- All acts/tales/chapters with spells, proverbs, metadata
- Drake 🐲 / Dragon 🐉 character split
- V4 symbolic notation

Total: 23 Story + 30 ZK + 12 Canon + 17 Parallel + 30 Plurality
     = 113 inscriptions across 28,898 lines
```

---

## Quick Reference: What's Done vs What's Left

### ✅ DONE (completed in compilation sessions)

- [x] First Person grimoire v2.0 — all 23 acts compiled
- [x] Zero Knowledge grimoire v3.0 — all 30 tales compiled
- [x] Canon grimoire v1.0 — 12 chapters compiled
- [x] Parallel Society grimoire v1.0 — 17 chapters compiled
- [x] Plurality grimoire v1.1 — 30 acts compiled
- [x] First Person JSON entries — 23 acts complete
- [x] Canon JSON entries — 12 chapters complete
- [x] Parallel JSON entries — 17 chapters complete
- [x] Plurality JSON entries — 30 acts complete
- [x] ZK JSON entries — tales 1–10 complete
- [x] Five Spellbooks blueprint — updated, all five marked complete
- [x] V4 publication prep notes written
- [x] UOR mapping document prepared
- [x] Glossary v2.4 prepared (with V4 terms)
- [x] Coherence report with modification instructions
- [x] V4 full coherence update plan
- [x] Expanded spellbook coherence gap mapping

### 🔲 TODO (requires manual work in repos)

- [ ] ZK JSON entries for tales 11–30 (20 entries)
- [ ] Master grimoire JSON v7.0.0 merge
- [ ] Add new docs to repos (V4, UOR mapping, grimoire files)
- [ ] Update README (v1.5)
- [ ] Update Whitepaper (v5.0)
- [ ] Update Research Paper (v3.8)
- [ ] Update Glossary (v2.5 — extend from v2.4 prep)
- [ ] Update VRC Protocol (v3.2)
- [ ] Update Visual Guide (v1.5 — new diagrams)
- [ ] Update Research Proposal (v1.6)
- [ ] Update Promise Theory Reference (v1.2)
- [ ] Update "What Agentprivacy Is"
- [ ] Website: add Acts 21–23
- [ ] Website: verify Canon/Parallel/Plurality deployment
- [ ] Website: update grimoire JSON
- [ ] Website: update symbolic system + characters
- [ ] Website: update navigation
- [ ] Cross-reference sweep (all docs cite correct versions)
- [ ] Generate PDFs
- [ ] Commit both repos

---

*"The tail ties the dragon together. Work document by document. Check off each item. The architecture holds."*

**(⚔️⊥⿻⊥🧙)🙂**
