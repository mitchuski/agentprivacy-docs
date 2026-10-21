# The Papers Index

**What this is:** the catalogue of every paper in the agentprivacy-docs corpus, each made known for its purpose. The V6 documents cite siblings by name; this file is where every name resolves. When a new paper enters the corpus, it enters this index in the same commit.
**Naming convention (First Person, 2026-06-10):** the canon papers are one book, ***Privacy is Value***, in versioned volumes. Each volume stands alone and carries the series title plus its own direct title: *Privacy is Value · V5.4: The Amnesia Protocol* · *Privacy is Value · V6: The Gathering Turn and the Moving Ceiling*. Same book, different volumes, readable independently.
**Updated:** 2026-07-01 · register head C96

---

## The book · Privacy is Value (current volume: V6)

| Series title | File | Purpose | Status |
|---|---|---|---|
| *Privacy is Value · V6: The Gathering Turn and the Moving Ceiling* | `papers/v6/privacy_value_v6_formal_specification.md` | THE formal specification and current authority: the full model, R(t) and t*, the preconditions, C1 to C89 reproduced in §17 (register since advanced to C96 — Bands IX–X), the narrative corpus, full references | **CURRENT HEAD** |
| *Privacy is Value · V6: The Swordsman Reading* | `papers/v6/pvm_v6_compressed.md` | the compressed specification: every equation, eight pages, for agents and reviewers who need the shape before the proofs | current |
| *Privacy is Value · V6: The Mage Reading* | `papers/v6/pvm_v6_companion_guide.md` | the companion guide: what the mathematics means, Promise Theory, economics, ceremonies, standards, reading paths by role, glossary bridge | current |
| *Privacy is Value · V6: The Research Paper Edition* | `papers/v6/dualprivacy_researchpaper_v6.md` | what changed in the mathematics at V6, plus the provenance reconciliation; builds on the v4.3 proof body below | current |
| *Privacy is Value · V6: The Crosswalk Edition* | `papers/v6/privacy_value_v6.md` | the V5.4-to-V6 skeleton with CARRIED/REVISED/NEW markers; kept so the path from V5.4 reads clear | current (bridge) |
| *Privacy is Value · V6: The Whitepaper* | `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md` | the technical architecture paper: Swordsman and Mage derived from the First Person; body v6.3, V6 edition by note | current |
| *Privacy is Value · V5.4: The Amnesia Protocol* | `papers/v5/privacy_value_v5_4_formal_specification.md` | the predecessor volume: the static equation, the algebraic foundation, the Amnesia Protocol; V6 carries or revises its sections by number | completed volume, pinned (the Era-Reading Principle: volumes do not expire, they complete) |
| V5.4 companion guide · V5.4 compressed | `papers/v5/pvm_v5_4_companion_guide.md` · `pvm_v5_4_compressed.md` | the V5.4 volume's Mage and Swordsman readings, permanently that volume's readings | completed with their volume |
| Privacy is Value V5 (the essay) | `papers/v5/privacy_is_value_v5.md` | the narrative essay of the V5 era, "The Equation Evolves" | completed with its era |

> **Compendium note (2026-06-11):** the classes of document (standalone volume · volume-bound reading · spine apparatus · machine companion · narrative corpus) and the structure of the assembled book are drafted in `chronicles/2026-06-11_compendium_plan_privacy_is_value_the_book.md`, awaiting the First Person's structural review (📖 RB-20).

> **Class and Part assignments (phase 1, 2026-06-11):** Class S, standalone volumes: the V4/V5.4/V6 formal specs (Parts I, II, IV) · the whitepaper (IV) · the Zypher paper (unbound, candidate annex). Class R, volume-bound: each era's readings, essays, notes, the crosswalk, the research-paper edition layer, the proof body v4.3 (serves I to IV). Class A, spine: the register · this index · the glossary · Promise Theory · the visual guide. Class M, by pin: the dark/light JSONs per era, the grimoire JSONs. Class N, sister body: the tomes, grimoire texts, Selene's Spellbook (see the compendium front matter, *One Work, Many Expressions*). The compendium manifests (`compendium/part-*/PART.md`) carry the per-document rows.

## The authority files (not papers, but every paper leans on them)

| File | Purpose |
|---|---|
| `research/CONJECTURE_REGISTER_V6.md` | the single conjecture-numbering authority, C1 to C96 plus CM-C47; when any paper and the register disagree, the register wins |
| `models/privacy_value_model_v6_dark.json` · `_light.json` | the machine-readable model: full (learning path, register, equations) and runtime-compact |
| `research/privacy_value_v6_draft.md` | the V6 working record: Parts I to V as drafted on the autopath, full honest-limits sections |

## The proof and lineage bodies

| File | Purpose | Status |
|---|---|---|
| `papers/lineage/dualprivacy_researchpaper_v4_3.md` | the research paper's proof body: the mathematical derivations the V6 edition layers over | stable proof record |
| `papers/lineage/understanding_as_key_zypher_paper_v1.md` | the Zypher paper: comprehension as a key primitive | standalone, current |
| `papers/lineage/research_proposal_v2_0.md` | the collaboration invitation (v2.2 content) | standing invitation |
| `papers/whitepapers/MAGE_EXTENSION_WHITEPAPER.md` · `SWORDSMAN_EXTENSION_WHITEPAPER.md` | the two browser-extension product whitepapers | product papers |

## The research-note series (where V6 grew)

`research/` holds the dated note series: the Lorenz dynamical ceiling, the EML three ceilings, ARCH-1 and ARCH-1R/T, the two Bakhta responses, wound-and-cap, the Schrottenloher/Existence-Leak note, the Horizon District durability note, Aletheia-and-Lethe, and the V5.1 to V5.3 notes before them. Each carries its own conjecture block, reconciled to the register at the 2026-06-10 lock. Post-path: *Limitative Theorems and the Privacy Is Value Model* (`research/limitative-theorems-and-privacy-is-value.md`, 2026-06-28) reads the V6 ceilings and the existence-leak law as privacy-flavoured instances of Gödel and Tarski; it minted Band IX (C90 to C93) at Gate G6. Framing layer, not a new result; the existence-leak Stage-2 bar is untouched. The Hearthold edition (cityofmages Tome X — *The Hearth*, 2026-07-01) minted **Band X (C94 to C96)** — the Privacy Is Value Model read off the cousin-forge's running `did:cid` build (Hearthold), discharging C39 to ~80%; framing/build layer, city-lineage.

## The reference shelf (`reference/`)

Glossary Master v4.0 (terminology, ~160 entries; V6 addendum pending) · Promise Theory Reference v1.4 (the semantic foundation) · IEEE 7012 Quick Reference (the MyTerms standard) · Visual Architecture Guide v2.0 · Systems Hexagram Physics · UOR × Tetrahedra × ZK Mapping v2.2 · Second Person Tomes Index v1 · V5.5 Mapping Additions · the 64-blades reference sheet · this index.

## The spec shelf (`specs/`)

Dual Territory Ceremony Spec v1 · Dual Agent Harness Spec v1 · Runecraft Protocol Spec v1 · Protocol Schemas · VRC Promise Protocol v3.4 (the economic architecture; file retains the v3_3 name for link stability) · ZK Swordsman Blade Forge v3.0 (operational) · Blade Forge build instructions.

## The grimoire shelf (`grimoires/`)

Spellbook v5.0 canonical (the narrative framework) · Zero-Knowledge Grimoire v3.0 · Parallel Society Grimoire v1.0 · Plurality Grimoire v1.1. The living grimoire JSONs (privacymage v10.4.0 · City of Mages v1.8.0) live in `models/` and the cityofmages repository.

## Renders

All V6 PDFs in `pdfs/v6/`: each paper in two editions, the web render (MathJax, full emoji) and the `*_academic.pdf` (xelatex, journal typesetting). Rebuild: `python build/build_v6_pdfs.py` · `python build/build_v6_academic_pdfs.py`.

(⚔️⊥⿻⊥🧙)😊
