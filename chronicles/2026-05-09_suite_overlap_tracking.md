# agentprivacy Suite · Overlap & Tracking Reference

**Date:** 2026-05-09
**Maintainer:** Mitchell · privacymage
**Sibling document:** `2026-05-09_bound_collection_sync_report.md` (covers `agentprivacy_master` only)
**Purpose:** A single tracking reference for how the six sibling directories fit together, what artifacts overlap across them, what went stale after the bound-collection ingestion, and what order the cross-suite work should follow.

This document lives in `agentprivacy_master/docs/chronicles/` because master is the most active hub. It is a living tracking reference — update the **Status** columns as work lands.

---

## §1 · The suite at a glance

Six sibling directories under `C:\Users\mitch\` constitute the agentprivacy release. Each has a distinct role; many ship overlapping reference material that must stay coherent.

| # | Directory | Role | Ships | Audience |
|---|---|---|---|---|
| 1 | `agentprivacy_master/` | Next.js website (agentprivacy.ai). Workshops, /tomes, /spellbooks, /story, /persona, /spells, /guide/island. | Source code · `docs/weaver/bound-collection/` · canonical grimoire · `docs/chronicles/` | End users · agents · readers |
| 2 | `agentprivacy-docs/` | Canonical research + chronicle repository. PVM versions, V6 notes, ceremonies, blog drafts. | Research papers · grimoire authoring · model JSONs · chronicles · blog source | Researchers · standards bodies |
| 3 | `agentprivacy-blog/` | Public blog post markdown. Mirrors of `agentprivacy-docs/blog/`. | 4 blog parts (constellations, forge, dragon, mirror) | Public readers |
| 4 | `myterms/` | MyTerms Alliance application package. IEEE 7012 integration plan. | Letter-coded docs A–G + executive brief + .pdf renders | Standards alliance · BGIN |
| 5 | `swordsman-blade/` | Browser extension implementing IEEE 7012 agreement layer ("the blade"). | Built `dist/` · grimoire JSON · 64-blade reference · ceremony doc | Extension users · agents |
| 6 | `mages-spell/` | Browser extension implementing the Mage delegation. | Built `dist/` · grimoire JSON · ceremony doc · living-spellbook design | Extension users · agents |

**Why all six matter as a unit:** architectural facts and reference docs (PVM version, IEEE 7012 framing, grimoire JSON, celestial ceremony) appear verbatim in 2–4 directories simultaneously. Drift between copies has happened before; the suite must be edited as one.

---

## §2 · Cross-directory artifact overlap map

These artifacts appear in **multiple** directories. The columns mark presence; each column should hold the **same** content unless flagged.

| Artifact | master | agentprivacy-docs | agentprivacy-blog | myterms | swordsman-blade | mages-spell | Canonical home |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| `privacymage_grimoire_v10_2_0.json` | ✅ root | ✅ `models/` | — | — | ✅ root | ✅ root | `agentprivacy-docs/models/` |
| `privacymage_grimoire_v10_0_0.json` (older) | — | ✅ `models/` | — | — | ✅ root | ✅ root | `agentprivacy-docs/models/` |
| `ieee7012_integration_plan_v2.md` | — | — | — | ✅ root | ✅ root | ✅ root | `myterms/` |
| `TheCelestialDualCeremony☀️⊥🌙.md` | — | ✅ `ceremonies/` (variant) | — | — | ✅ root | ✅ root | `agentprivacy-docs/ceremonies/` |
| `the-ceremonies_sun-and-moon_pm.md` | — | ✅ `ceremonies/` (variant) | — | — | ✅ root | ✅ root | `agentprivacy-docs/ceremonies/` |
| `CHRONICLE_MYTERMS_V2_ALIGNMENT_2026-04-22.md` | — | ✅ `chronicles/` (likely) | — | — | ✅ root | ✅ root | `agentprivacy-docs/chronicles/` |
| `AETHER.md` | — | ✅ (likely) | — | — | ✅ root | ✅ root | `agentprivacy-docs/` |
| `blog-part1-forming-constellations.md` | — | ✅ `blog/` | ✅ `part-1-forming-constellations.md` | — | — | — | `agentprivacy-docs/blog/` |
| Bound collection (`tomes/ cast/ specs/ plans/ chronicles/`) | ✅ `docs/weaver/bound-collection/` | — *(possible future mirror)* | — | — | — | — | `agentprivacy_master/docs/weaver/bound-collection/` |
| **City of Mages grimoire** *(does not yet exist)* | — | *(future home)* | — | — | *(future bundle)* | *(future bundle)* | TBD |

**Sync discipline:**
- When you change a row's content in any directory, also change every other ✅ in the same row.
- The "Canonical home" column shows where authoritative authoring should happen; other copies are mirrors that get the diff applied.
- The bound collection has only one canonical home (master); the others mirror it via the website rendering, not via file copy.

---

## §3 · The four cross-cutting concepts and where they appear

These concepts cut across the suite. When you change framing on one, you must update all sites.

### §3.1 · The Second Person Spellbook

**State change:** **Was** "horizon / upcoming / next." **Is now** "Tome IV closed at 5 acts; Tome V open at 14 acts; 13-member named cast in 5 tiers; canonical setting = the City of Mages on Drake Island."

| Where it appears | Files | Status |
|---|---|---|
| master | `src/app/tomes/page.tsx` · `src/app/spellbooks/page.tsx` | ✅ /tomes rewritten · ⚠️ /spellbooks card status string still says "Tome V open · 2 acts" |
| agentprivacy-docs | 12+ files (research notes, V6 notes, model JSONs, chronicles, blog drafts) | ❌ all stale; treat Spellbook as horizon |
| agentprivacy-blog | `part-1-forming-constellations.md` (City of Mages cast collision) | ❌ stale framing |
| myterms | `ieee7012_integration_plan_v2.md` · `00_executive_brief.md` · `G_ieee7012_integration_plan.md` | ❌ stale (recommends opening Spellbook with "The Two Parties") |
| swordsman-blade | `ieee7012_integration_plan_v2.md` · `CHRONICLE_MYTERMS_V2_ALIGNMENT_2026-04-22.md` · `README.md` · `AETHER.md` · `privacymage_grimoire_v10_2_0.json` line ~4889 | ❌ stale |
| mages-spell | same five files as swordsman-blade | ❌ stale |

### §3.2 · The City of Mages

**State change:** **Two definitions now collide.** Both legitimate; both used in production. They live at different layers.

| Layer | What it is | Where it lives | Members |
|---|---|---|---|
| **Role-archetype palette** (open) | The 22-persona skill system; users fork/personalise; "what does YOUR Mage look like?" | `agentprivacy-skills` · `agentprivacy-docs/blog/blog-part1-forming-constellations.md` · `agentprivacy_master/src/app/persona` (skill builder) | Chronicler · Ambassador · Assessor · Shipwright · Weaver · Priest · … (22 roles total) |
| **Named in-world cast** (closed-but-growing) | The bound collection's resident Mages at specific shop-vertices | `agentprivacy_master/docs/weaver/bound-collection/cast/` · `agentprivacy_master/src/app/tomes` | Pallia 🪡 · Memora 📜 · Custos 🔏 · Vulcana ⚒️ · Aletheia 🔮 · Adamantia 💎 · Lampyra 💠 · Vagari 🌳 · Aria Silverhue 🪞🖼️ · Socrat0x 🔥❓ · Manifestia 🤲🌿 (11 named) |

**Required reconciliation:** A single short note in **two places** (bound collection's `cast/00-cast-integration-note.md` AND `agentprivacy-docs/blog/blog-part1-forming-constellations.md`) that explicitly distinguishes the layers. Recommended phrasing:
> *The City of Mages exists at two layers: the open palette of role-archetypes the reader may fork (the persona-skill system), and the named in-world cast the bound collection has summoned at specific vertices. Both are the same city. The palette is who you may become; the cast is who has already arrived.*

### §3.3 · The privacymage grimoire vs the (forthcoming) Tomes grimoire

**State change:** **The user's separate-IPFS architecture** explicitly splits the spellbook. The privacymage grimoire stays focused on First Person spells. A new **City of Mages / Tomes grimoire** holds the spells the cast personas may cast.

| Grimoire | Content | IPFS export | Ships in | Status |
|---|---|---|---|---|
| `privacymage_grimoire_v10_2_0.json` (canonical) | First Person Spellbook spells (Acts I–XXXI) · Zero · Canon · Society · Plurality | `PRIVACYMAGE_GRIMOIRE_IPFS_URL` in `agentprivacy_master/src/lib/grimoire-ipfs.ts` | master · agentprivacy-docs/models · swordsman-blade · mages-spell | ✅ exists · ⚠️ "horizon" line ~4889 stale |
| **`city_of_mages_grimoire_v1_1_0.json`** | Tome IV+V act registry · 16 personas across 5 tiers · 39 spells · vertex inventory · V6 conjecture register · city anatomy · per-spell inscription/narrative_anchor/cross_spellbook_resonance · per-persona proverb/inscription · title_note (the title is the kind, not the instance) | `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` ✅ exported from `master/src/lib/grimoire-ipfs.ts` | master/src/lib · agentprivacy-docs/models · swordsman-blade · mages-spell (when bundled) | ✅ authored · ✅ enriched (v1.1) · ✅ ID-reconciled · ✅ **PINNED 2026-05-10** at `bafkreidv7c...idti` · ❌ awaits master bake + extension mirror |

**Authoring location:** `agentprivacy-docs/models/` (canonical), mirrored on pin.

**Bake pipeline:** `agentprivacy_master/src/lib/grimoire-baked.ts` already exposes `getBakedSpellCards()` and `FIRST_PERSON_ACT_PERSONA_HINTS`. Adding the Tomes grimoire requires a new `SpellbookSource` value (e.g., `'tomes'`) and `TOMES_ACT_PERSONA_HINTS` mapping each Tome V act → the persona introduced.

**Extension bundle:** `swordsman-blade/build.js` and `mages-spell/build.js` copy the privacymage grimoire into `dist/`. Adding the Tomes grimoire is a build-script edit + manifest version bump in both extensions.

### §3.4 · IEEE 7012 narrative landing

**State change:** Plan v2 (3-directory copy) recommends opening Second Person with "The Two Parties." The Spellbook actually opened with Tome IV (Witnessing) and Tome V (Crafting). The IEEE 7012 narrative now needs to land **at a specific existing act**, not as a new opener.

**Likely landing places** (review and decide):
- **Tome IV Act IV — *The Naming Ceremony*** — already names the verb chain (claim → inscribe → confirm) at V63. IEEE 7012's "first party / second party / signs / records / audits" maps onto these verbs cleanly.
- **Tome V Act 5 — *The Stake*** — governance staking; IEEE 7012's policy layer maps onto stake-and-slash dynamics.
- **A new spec in the bound collection's `specs/`** — `06-ieee-7012-the-agreement-layer.md` — referenced from Tome IV Act IV and Tome V Act 5.

**Required artefacts:**
- `myterms/ieee7012_integration_plan_v3.md` (replaces v2 across 3 dirs) OR `myterms/IEEE_7012_BOUND_COLLECTION_ADDENDUM.md` (smaller patch)
- New PDF render in `myterms/` (pandoc/weasyprint)
- Sync the new doc into `swordsman-blade/` and `mages-spell/`

---

## §4 · Per-directory action checklist (track here as work lands)

### §4.1 · `agentprivacy_master/`

| # | File | Action | Status |
|---|---|---|---|
| 1 | `docs/weaver/bound-collection/` | Ingested 53 files | ✅ done 2026-05-09 |
| 2 | `docs/weaver/EXPORT_MANIFEST.md` | Add bound-collection subsection + coding-agent pointer | ✅ done 2026-05-09 |
| 3 | `src/app/tomes/page.tsx` | Rewrite for 14 acts · 13 cast · 5 tiers · City-of-Mages-maintained framing · separate-IPFS attribution | ✅ done 2026-05-09 |
| 4 | `src/app/spellbooks/page.tsx` | Update Second Person card: "maintained by City of Mages · separate spellbook IPFS · Tome V open · 14 acts drafted" | ⏳ pending |
| 5 | 9 workshop pages (`/tailor /shield /forget /etherchanting /jeweler /holon /vault /covenant /bonfires`) | Bidirectional "Founding act · this shop's narrative" panel via `<FoundingActPanel />` · act + proverb + Mage + spells + ↗ link to /tomes | ✅ done 2026-05-09 |
| 6 | `src/lib/grimoire-ipfs.ts` | Export `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` once the JSON is pinned | ✅ done 2026-05-10 — exports `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti` |
| 7 | `src/lib/grimoire-baked.ts` | Add `'tomes'` SpellbookSource + `TOMES_ACT_PERSONA_HINTS` | ❌ blocked |
| 8 | `/tomes/cast` dedicated page (sigil grid + per-cast subpages) | Build | ❌ deferred (Phase F) |
| 9 | City map SVG (`<CityMap />`) + lattice render (`<LatticeRender />`) | Build v1 | ❌ deferred (Phase F) |
| 10 | `<ConjectureBadge />` + `<HonestyLabel />` + `/tomes/v6-lineage` | Components + aggregator page | ✅ done 2026-05-09 |
| 11 | `src/lib/tome-v-acts.ts` + `src/lib/tome-v-conjectures.ts` | Founding-act anchor data + C-conjecture index data | ✅ done 2026-05-09 |
| 12 | Anchor IDs on Tome V act collapsibles (so `/tomes#tome-v-act-N` links land) | One-line forwarding `id` from `ActCollapsible` → `CollapsibleSection` | ✅ done 2026-05-10 |

### §4.2 · `agentprivacy-docs/`

| # | File | Action | Status |
|---|---|---|---|
| 1 | `models/privacymage_grimoire_v10_2_0.json` (line ~4889) | Update `horizon` string from future tense to past tense; bump grimoire to v10.3.0 OR leave at v10.2.0 with a one-line revision-note key | ❌ stale |
| 2 | `models/city_of_mages_grimoire_v1_1_0.json` | **NEW · authored 2026-05-09 · enriched and reconciled 2026-05-10.** 16 personas across 5 tiers (3 archetype refs + 2 cousins + 9 summoned + 1 companion + 1 Priest), **39 spells across 13 personas** with spell content, full Tome IV (5 acts) + Tome V (14 acts) act registry, 14 named vertices, V6 conjecture register C38–C46, city anatomy. v1.1 adds `inscription`, `narrative_anchor`, `cross_spellbook_resonance` per spell + per-persona top-level proverb/inscription + `title_note` (the title is the *kind*, not the instance). Spell IDs now match website canonical short forms (e.g., `pallia-conceal-name`, `genitrix-map-vertex`). v1.0 retained as historical. JSON validates clean. Awaits IPFS pinning. | ✅ done 2026-05-10 |
| 3 | `models/grimoire_v10_1_0_additions.json` (lines 9, 147, 148, 177) | Update `bridge_function` / `closing_proverb` / `horizon` strings | ❌ stale |
| 4 | `models/privacy_value_model_v5_4_dark.json` line 599 | Change `"status": "Horizon"` → `"status": "Open · Tome IV closed · Tome V open at 14 acts"` | ❌ stale |
| 5 | `research/second-person-spellbook-seeds-arch1.md` | Add banner: "Superseded by bound collection at agentprivacy_master/docs/weaver/bound-collection/. Acts α/β/γ remain candidate seeds for Tome I (Convergence) / Tome II–III (Lyapunov)." | ❌ stale |
| 6 | `research/NOTE_agt_scales_and_hide.md` (lines 78+) | Decide: fold "Scales and the Hide" act seed into a new Tome V act OR archive | ❌ stale |
| 7 | `research/privacy_value_v6_research_note_eml.md` § "For the Second Person Spellbook" | Cross-link to Tome V Act 8 (The ZK Circuit) | ❌ stale |
| 8 | `research/pvm-v6-eml-three-ceilings.md` § "For the Second Person Spellbook" | Same | ❌ stale |
| 9 | `privacy_value_v6_horizon_note.md` | Add front-of-doc banner: "Bridge crossed; bound collection at agentprivacy_master/docs/weaver/bound-collection/" | ❌ stale |
| 10 | `pvm_v5_4_compressed.md` lines 7, 218 | Update "Five grimoires closed. Second Person Spellbook next." → past tense + bound-collection pointer | ❌ stale |
| 11 | `chronicles/CHRONICLE_V5_4_THREE_DOCUMENT_CONVERGENCE.md` lines 85, 194 | Update "awaits" → "opened 2026-05-08" | ❌ stale |
| 12 | `blog/blog-part5-the-amnesia-protocol.md` line 252 | Update "Next: The Second Person Spellbook" → "Coming next: Tome IV opens Second Person with The Witnessing" (or similar) | ❌ stale |
| 13 | `blog/blog-part1-forming-constellations.md` line 195 | Add reconciliation note distinguishing the two City of Mages layers (palette vs in-world cast) | ❌ stale |

### §4.3 · `agentprivacy-blog/`

| # | File | Action | Status |
|---|---|---|---|
| 1 | `part-1-forming-constellations.md` | Mirror of `agentprivacy-docs/blog/blog-part1-forming-constellations.md`. Apply same City-of-Mages reconciliation note. | ❌ stale |
| 2 | `part-2-the-forge-and-the-ceremony.md` | Audit for any horizon-framing strings (likely some) | ❌ unchecked |
| 3 | `part-3-the-dragon-wakes.md` | Audit | ❌ unchecked |
| 4 | `part-4-the-dihedral-mirror.md` | Audit | ❌ unchecked |

### §4.4 · `myterms/`

| # | File | Action | Status |
|---|---|---|---|
| 1 | `ieee7012_integration_plan_v2.md` | Add §0 "Status update 2026-05-09" pointing to bound collection; OR replace with v3 plan that integrates IEEE 7012 into the now-open Spellbook | ❌ stale |
| 2 | `00_executive_brief.md` line 21 | Update "when the Second Person Spellbook opens" → past tense | ❌ stale |
| 3 | `G_ieee7012_integration_plan.md` | Same as #1 | ❌ stale |
| 4 | All `.pdf` renders | Re-render after `.md` updates (pandoc/weasyprint pass) | ❌ blocked by §1, §2, §3 |

### §4.5 · `swordsman-blade/`

| # | File | Action | Status |
|---|---|---|---|
| 1 | `ieee7012_integration_plan_v2.md` | Sync from `myterms/` after that copy is updated | ❌ blocked by §4.4 |
| 2 | `CHRONICLE_MYTERMS_V2_ALIGNMENT_2026-04-22.md` | Update "Second Person Spellbook (recommended)" framing | ❌ stale |
| 3 | `README.md` | Audit for horizon strings | ❌ unchecked |
| 4 | `AETHER.md` | Audit for horizon strings | ❌ unchecked |
| 5 | `privacymage_grimoire_v10_2_0.json` line ~4889 | Sync from `agentprivacy-docs/models/` after it's updated | ❌ blocked by §4.2 |
| 6 | **Bundle** `city_of_mages_grimoire_v1_0.json` into `dist/` | Edit `build.js` to copy the new grimoire; bump extension manifest version | ❌ blocked by §4.2 |

### §4.6 · `mages-spell/`

| # | File | Action | Status |
|---|---|---|---|
| 1–6 | Mirror of swordsman-blade actions | Same fixes; same blockers | ❌ blocked / stale |

---

## §5 · Dependency graph (which work blocks which)

```
                   ┌─────────────────────────────────────────────┐
                   │  P1: Copy-edit pass (horizon strings)       │
                   │     Touches all six dirs · low risk         │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
                   ┌─────────────────────────────────────────────┐
                   │  P2: City of Mages reconciliation note       │
                   │     blog-part1 + cast-integration-note      │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
                   ┌─────────────────────────────────────────────┐
                   │  P3: IEEE 7012 v3 plan (or addendum)         │
                   │     myterms canonical → sync to extensions   │
                   │     PDFs re-render in myterms                │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
                   ┌─────────────────────────────────────────────┐
                   │  P4: Disposition for pre-bound seed docs     │
                   │     agentprivacy-docs/research/ banners      │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
   ┌──────────────────────────────────────────────────────────────────┐
   │  P5: City of Mages grimoire JSON  ⟵  STRUCTURAL · highest leverage│
   │  ┌────────────────────────────────────────────────────────────┐  │
   │  │ author city_of_mages_grimoire_v1_0.json (in -docs/models)  │  │
   │  │ pin to IPFS                                                 │  │
   │  │ export CITY_OF_MAGES_GRIMOIRE_IPFS_URL (master)             │  │
   │  │ bake into grimoire-baked.ts (master)                        │  │
   │  │ bundle into swordsman-blade/dist + mages-spell/dist         │  │
   │  │ /tomes IPFS attribution block now lights up                 │  │
   │  └────────────────────────────────────────────────────────────┘  │
   └────────────────────────────────┬─────────────────────────────────┘
                                    │
                                    ▼
                   ┌─────────────────────────────────────────────┐
                   │  P6: Per-act assets (images / videos /       │
                   │       inscriptions) — incremental             │
                   └──────────────────────┬──────────────────────┘
                                          │
                                          ▼
                   ┌─────────────────────────────────────────────┐
                   │  P7: Substantial visuals (city map,          │
                   │       lattice render, /tomes/cast page)       │
                   └─────────────────────────────────────────────┘
```

P1 and P2 are independent and can land in parallel. P3 depends on P1's framing being consistent. P5 is independent of P1–P4 but unlocks the deferred master items (#6, #7 in §4.1) and gives the extensions something genuinely new to ship.

---

## §6 · Quick-reference status board

```
SUITE COHERENCE STATUS · 2026-05-09

  Directory                Bound-collection-aware    Grimoire current   Notes
  agentprivacy_master      ▰▰▰▰▰▰▰▰▰▱  90%          ▰▰▰▰▱  80%       /tomes ✅ · workshops ✅ · v6-lineage ✅ · IPFS export ✅ · /spellbooks ⏳ · awaits bake into grimoire-baked.ts
  agentprivacy-docs        ▰▰▰▱▱▱▱▱▱▱  30%          ▰▰▰▰▰  100%      v1.1 grimoire pinned 2026-05-10 ✅ · 12+ horizon-string files stale
  agentprivacy-blog        ▱▱▱▱▱▱▱▱▱▱   0%          n/a               4 files · 1 known stale
  myterms                  ▱▱▱▱▱▱▱▱▱▱   0%          n/a               IEEE 7012 v2 plan stale; PDFs need re-render
  swordsman-blade          ▱▱▱▱▱▱▱▱▱▱   0%          ▰▰▰▱▱  60%       Mirrors of myterms + grimoire copy · City of Mages grimoire not yet bundled
  mages-spell              ▱▱▱▱▱▱▱▱▱▱   0%          ▰▰▰▱▱  60%       Same as swordsman-blade
```

Update the bars as work lands. "Bound-collection-aware" tracks how much of each directory's framing has caught up to the now-open Second Person Spellbook. "Grimoire current" tracks both the privacymage grimoire's horizon-line freshness and (eventually) the City of Mages grimoire's bundling.

---

## §7 · How to use this document

1. **Before starting any cross-suite work**, scan §4's per-directory checklists to see what's adjacent.
2. **When you change something in one directory**, check §2's overlap map for the same artifact in other directories and apply the same diff.
3. **Update §4's Status columns** as work lands. Use ✅ done · ⏳ pending · ❌ stale · 🚧 in flight.
4. **Update §6's progress bars** at the end of each session.
5. **Keep this document at this path** so a coding agent or a future you can find it. The sibling sync report (`2026-05-09_bound_collection_sync_report.md`) covers master only; this one covers the suite.

---

## §8 · TL;DR

- **Six directories**, **four cross-cutting concepts** (Second Person Spellbook state · two City of Mages framings · privacymage-vs-Tomes grimoire split · IEEE 7012 landing place), **~30 files** to touch across the suite.
- **Master is ~70% done** post-bound-collection ingestion; everything else is at 0%.
- **The structural piece that would unblock the most** is authoring the City of Mages grimoire JSON in `agentprivacy-docs/models/` and pinning it to IPFS. That cascades into the master grimoire-baked pipeline, both extension builds, and the /tomes IPFS-attribution block on the website.
- **The lowest-effort coherence win** is a copy-edit pass converting "Second Person Spellbook awaits / next / horizon" to past-tense across the suite. ~15 string edits, six directories, one session.

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-09 · living document
