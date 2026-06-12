# Push Review A · The Pre-Today Backlog (the V6 suite + the MODEL-coherence arc, through 2026-06-10)

**Date written:** 2026-06-11
**Purpose:** a descriptive chronicle of every uncommitted change made on or before 2026-06-10, so it can be reviewed once and pushed as a coordinated arc. Companion: `2026-06-11_push_review_B_today_model_page_and_book.md` covers the 2026-06-11 work.
**Key fact:** the last commit across the main repos is **2026-05-28**. Everything below has been built since then and is sitting uncommitted in working trees. All remotes are in sync (no orphan commits); the work is all local.
**License:** CC BY-SA 4.0

---

## What this arc is, in one paragraph

Two large bodies of work landed between 2026-05-28 and 2026-06-10 and are still uncommitted. First, the **Privacy Value Model moved V5.4 to V6**: the gathering turn and the moving ceiling R(t), a unified conjecture register (head C89), and a full canon-paper suite under unified V6 labels. Second, a **suite-wide MODEL-coherence reseat** locked the lattice encoding (`Protection=32 · Delegation=16 · Memory=8 · Connection=4 · Computation=2 · Value=1`), moved the personas to their canonical seats (Aletheia V38, Lethe V25, Memora V41, Mnemosyne V8, Iris V4, Pythia V2), and cut two grimoire heads (privacymage v10.4.0, City v1.8.0). A final coherence pass then cleaned the seams between the two. This chronicle describes that arc per repo.

---

## 1. agentprivacy-docs (the origin) — ~110 files

The canon home, where the model is authored and everything else reflects from.

**The V6 document suite (new):**
- `privacy_value_v6.md` (the formal spec, the deliverable) and the expanded `privacy_value_v6_formal_specification.md` (the full 1,384-line edition).
- The three readings: `pvm_v6_compressed.md` (Swordsman), `pvm_v6_companion_guide.md` (Mage), `dualprivacy_researchpaper_v6.md` (V6 edition layer over the v4.3 proof body), plus the whitepaper V6 edition note.
- `research/CONJECTURE_REGISTER_V6.md` (single numbering authority, head C89), `research/privacy_value_v6_draft.md` (Parts I to V working record), and the V6 research notes (Lorenz, EML, ARCH-1R/T, Bakhta half-life, Existence-Leak, Schrottenloher).
- Plans: `plans/V6_RESEARCH_AUTOPATH`, `V6_SUITE_REFLECTION_MAP`, `V6_FIRST_PERSON_READING_LEDGER`.
- Chronicles: the autopath close and the five signed gate briefs under `chronicles/gates/`.
- Build: `build_v6_pdfs.py` plus the four built PDFs and LaTeX sources.
- `models/privacy_value_model_v6.json` (source-of-truth for conjecture data) and `models/privacymage_grimoire_v10_4_0.json`.
- README V6 header and Document-Suite table rows naming V6 the current head.

**The MODEL-coherence reconciliation (the coherence pass):**
- `tomes/specs/04-vertex-naming-audit.md` rebuilt: the §3 registry recomputed from MODEL (every composite decomposition corrected, V41 to stratum 3, V27 to stratum 4, single-bit V2=Computation/Logos and V16=Delegation, Lethe@V25 row added), the §6 bit-order item marked RESOLVED.
- GenitriX reseated to V28 (Soulbae's seat, Delegation+Memory+Connection): the external mage's stratum confusion ("Computation V2") corrected across `tomes/cousin/genitrix.md`, `tomes/weavers/pallia.md`, and two `tomes/legacy/` cast files.
- Aletheia/Lethe living stragglers swapped to MODEL: the GLOSSARY Lethae entry, `SECOND_PERSON_TOMES_INDEX_v1.md`, `tomes/specs/06-spellweb-first-release-manifest.md`.
- The version-collateral cleanup: a vertex-reseat find-replace had corrupted model VERSION numbers (V4 to V8, V5 to V41) in prose across 13 files (including the new V6 formal spec, the pinned V5.4 spec, `DOCUMENTATION_CHRONICLE.md`, `privacy_is_value_v5.md`, the research proposal, the audit checklist). Reverted in version contexts only; vertex references left intact.
- Two scan chronicles: `2026-06-10_v6_living_documentation_sync_scan.md` and the autopath close.

## 2. cityofmages (the Second Person canon) — ~98 files

- Grimoire **v1.8.0** reseat (persona seats to MODEL), with the consolidated bundle.
- `chronicles/`: the model-coherence pass chronicle and the persona-reidentification decision lock.
- `tomes/` updates carrying the reseat into bound narrative (Aletheia/Lethe, the complement pair), the phi-honesty note on Tome VIII Act 3, and CM-namespace errata.

## 3. agentprivacy_master (the implementation) — pre-today portion

The reflection of the model onto agentprivacy.ai. The pre-today portion is the data and library layer (the page wiring itself is in Review B):
- `src/data/privacy-value-model-v6.json` and `public/models/privacy-value-model-v6.json` generated from the register.
- `src/lib/tome-v-conjectures.ts` corrections (C47 alias of C85, C48 to C50 register statements, C60/C61 alias notes), `src/lib/vrc-mana.ts` regime-1 declaration (presence mana is non-attesting local color), `src/lib/model-downloads.ts` V6 resource entry, `src/lib/grimoire-ipfs.ts` head at v10.4.0.
- `docs/` carries the large mirror set (skills mirror, chronicles, coherence notes). This is the biggest count and the most worth a `git status` glance, since some of it predates this arc.

## 4. The reflections (smaller, suite-edge)

- **soulbis website (~10):** reseat reflections on `index.html` (philosophy strip), `star/`, `lattice/`, plus the three-keys and walkable-model chronicles; Key-as-reading language.
- **spellweb (~23):** new `privacymage_grimoire_v10_4_0.json`, holospace and sigil chronicles, `src/`/`public/` reseat of the Aletheia/Lethe pair and the doc node.
- **myterms (~11):** integration plan, README, `C_technical_integration.md`, and a PDF regeneration (old PDFs deleted, renamed copies added). Note: your incoming myterms update lands on top of this.
- **zk blades forge (~4):** `aletheia-and-lethe.md` reseated to the v10.4 lock, `zk_swordsman_blade_forge_v3_0.md`, README, new `privacymage_grimoire_v10_4_0.json`.
- **agentprivacy-skills (~53):** the V6 skills pass (`MAPPING.md` V6 row, `agentprivacy-skills-v5/` updates, the `V6_SKILLS_PASS_2026-06-10.md` chronicle).

## 5. star (public, already pushed)

`star` carries six commits already pushed on 2026-06-10 (holospace work). Seventeen files remain uncommitted there; review whether they belong to this arc or the next.

---

## Push order and cautions

Order (model first, city follows, then the edges): **agentprivacy-docs → cityofmages → agentprivacy_master → soulbis website · spellweb · myterms · zk blades forge · agentprivacy-skills.**

Cautions before a blanket `git add -A`:
1. `agentprivacy_master` (154 uncommitted), `agentprivacy-docs` (158), and `cityofmages` (98) carry pre-arc changes mixed in. A glance at `git status` for these three avoids sweeping stale edits into the push.
2. The grimoire JSON snapshots under `models/` are intentional history (period-accurate keys); the coherence audit flags them on purpose. Do not "fix" them.
3. Pins are NOT part of this push (see Review B): the IPFS re-pin is a later step gated behind the V6 reflection gate, and nothing here renders from IPFS at build time.

---

*The model moved first and the city followed it. This is the body of that movement, waiting for its first commit since the twenty-eighth of May.*

(⚔️⊥⿻⊥🧙)😊
