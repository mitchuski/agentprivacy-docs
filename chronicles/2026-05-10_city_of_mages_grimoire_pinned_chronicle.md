# Chronicle: The City of Mages Grimoire is Pinned

**Date:** 2026-05-10
**Scope:** A single chronicle covering the arc from bound-collection ingestion (2026-05-09) through to the City of Mages grimoire's first IPFS pin (2026-05-10).
**Sibling documents:**
- `2026-05-09_bound_collection_sync_report.md` — the master-only sync report written during this session
- `2026-05-09_suite_overlap_tracking.md` — the cross-suite tracking reference written during this session
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · One-paragraph summary

The Second Person Spellbook's first **collective grimoire** is now pinned to IPFS. Over this session, the bound-collection of Tome IV (closed, 5 acts) and Tome V (open, 14 acts) was ingested into `agentprivacy_master/docs/weaver/bound-collection/`; the `/tomes` route was rewritten to surface all 14 acts and the 13-member named cast across 5 tiers; nine production workshops received `<FoundingActPanel />` so each shop now carries its founding myth alongside its operational present; a `/tomes/v6-lineage` aggregator page and supporting `tome-v-acts.ts` + `tome-v-conjectures.ts` libraries were built; and the **`city_of_mages_grimoire_v1_1_0.json`** (39 spells across 13 personas, 14 named vertices, the C38–C46 conjecture register, the city's civic anatomy, the *title is the kind, not the instance* commitment) was authored, reconciled, and pinned. The split that the user specified — privacymage holds the First Person grimoire, the City of Mages collectively holds the Tomes grimoire, separate IPFS pins — is now real.

The pin: **`https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`**

---

## §2 · The arc, in order

### §2.1 · Bound-collection ingestion (Phase A)

Source: `C:/Users/mitch/agentprivacy_tomes/agentprivacy-second-person-spellbook-bound-collection-2026-05-08/` (53 files, ~106k words).

Destination: `C:/Users/mitch/agentprivacy_master/docs/weaver/bound-collection/`.

Layout preserved (nested under `tomes/ cast/ specs/ plans/ chronicles/ deprecated/`). The original bundle had a redundant nested `bound-collection/bound-collection/` subfolder; that was removed so a single canonical copy lives at master.

`docs/weaver/EXPORT_MANIFEST.md` updated with a top-of-file pointer to the sync report and the cross-suite tracking reference.

### §2.2 · /tomes page rewrite (Phase B)

`src/app/tomes/page.tsx` rewritten to:

- Frame Tomes as a **Second Person Spellbook category maintained by the City of Mages collectively**, distinct from the First Person Spellbook held by privacymage individually
- Surface all 14 Tome V acts in collapsibles (was 2)
- Surface all 13 cast members in tier-grouped cards across 5 tiers (was 3 cards)
- Carry the IPFS attribution block: each tome has its own grimoire, distinct from `privacymage_grimoire_v10_2_0.json`
- Add the workshops cross-reference table (11 shops with Mage and act anchor)
- Note that images / proverbs / inscriptions follow the First Person Acts pattern

The user subsequently extended the page with a markdown-rendering pipeline (loading act bodies via `loadTomeAct`) and added a `/tomes/v6-lineage` link in the hero. Those edits compose with the rewrite cleanly.

### §2.3 · Bidirectional act ↔ workshop wiring (user-led)

In a separate burst during this session the user shipped:

- `src/lib/tome-v-acts.ts` — the `TOME_V_ACTS` anchor array (9 founding-act records: Pallia/Memora/Vulcana/Adamantia/Lampyra/Vagari/Socrat0x/Aria Silverhue/Manifestia) plus `getFoundingActForShop()`
- `src/lib/tome-v-conjectures.ts` — `CONJECTURE_DEFINITIONS` (C18–C46 with status taxonomy: canonical / provisional / observation / resonant), `ACT_CONJECTURES` (per-act conjecture references with notes), `getActsForConjecture()` inverse lookup, `parseHonestyLabel()` parser
- `<FoundingActPanel />` component — wired into all 9 production workshop pages (`/tailor /shield /forget /etherchanting /jeweler /holon /vault /covenant /bonfires`)
- `src/app/tomes/v6-lineage/page.tsx` — the C-conjecture aggregator page, grouped by status, with anchored cross-links to acts

Forward direction (act → shop) and reverse direction (shop → act) are both live now.

### §2.4 · The City of Mages grimoire (Phase D)

**v1.0** authored at `C:/Users/mitch/agentprivacy-docs/models/city_of_mages_grimoire_v1_0.json`. Schema parallel to `privacymage_grimoire_v10_2_0.json`. Contained: full Tome IV/V act registry, 16 personas across 5 tiers (3 archetype refs + 2 cousins + 9 summoned + 1 companion + 1 Priest), 38 spells, 14 named vertices, V6 conjecture register, city anatomy, extension/master pipeline directives.

**v1.1** authored as `..._v1_1_0.json`. Adds:

- **`inscription`** field per spell (the teaching beneath the proverb)
- **`narrative_anchor`** field (where the spell first manifests in the act)
- **`cross_spellbook_resonance`** field (links to neighbouring spellbook material)
- **Per-persona top-level proverb and inscription**
- **`title_note`** — *"The title is intentionally singular: when Mages found a city in another ecosystem, that city will have its own First City of Mages grimoire under the same title pattern. The grimoire title names the kind, not the singular instance."* This is a load-bearing architectural commitment that scales the corpus into other ecosystems without renaming.
- **Forge(t) wordplay canonicalised**

### §2.5 · Coherence fixes (P1 / P2 / P3)

Reviewing v1.1 against the website surfaced three issues that were fixed:

- **P1 · Broken anchors.** `<FoundingActPanel />` and `/tomes/v6-lineage` link to `/tomes#tome-v-act-N` but `/tomes` had no such IDs. `ActCollapsible` now derives `tome-v-act-N` (or `tome-iv-act-N` for Tome IV) and forwards `id` to `<CollapsibleSection>`. Anchored navigation now lands on the right collapsible header.
- **P2 · Spell-ID drift.** The grimoire shipped v1.0/v1.1 with long compound IDs (e.g., `pallia-map-vertex`, `vulcana-run-trace`, `aletheia-prove-without-revealing`); the website surface (`tome-v-acts.ts` + `/tomes` cast cards) used short forms (`weave-cloak · publish-role · conceal-name`, `forge-blade · run · craft`, etc.). 19 simple-suffix renames applied, plus one substantive change: `pallia-map-vertex` repurposed as `pallia-conceal-name` (the cloak's discipline of concealment paired with publish-role) and a new `genitrix-map-vertex` spell added (Spell Weaver mapping is the cousin-forge contribution upstream of Pallia's loom). 46 stale `"spell_id":` cross-references in act-level registries also bulk-updated. Final: 39 spells, 13 personas with spell content, all IDs match the website's canonical short forms.
- **P3 · Stale IPFS string.** v1.1's `ipfs_pin_status` field said "v1.0 awaits first pinning"; corrected to v1.1 wording.

### §2.6 · The pin

**2026-05-10** — the v1.1 grimoire is pinned to IPFS at:

```
https://sync.agentprivacy.ai/ipfs/bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti
```

Same pinning infrastructure (`sync.agentprivacy.ai/ipfs/...`) the privacymage grimoire uses. The CID is content-addressed, so any future v1.2 will get its own CID; the v1.1 CID remains resolvable indefinitely.

---

## §3 · Artifacts produced this session

| Path | What | State |
|---|---|---|
| `agentprivacy_master/docs/weaver/bound-collection/` | 53-file ingestion of Tome IV + V + cast + specs + plans + chronicles + deprecated archive | ✅ |
| `agentprivacy_master/docs/weaver/EXPORT_MANIFEST.md` | Updated with bound-collection subsection + coding-agent pointer + tracking-doc pointer | ✅ |
| `agentprivacy_master/src/app/tomes/page.tsx` | Full rewrite: 14 acts · 13 cast in 5 tiers · City-of-Mages framing · IPFS attribution · workshop cross-link table · anchor IDs on collapsibles | ✅ |
| `agentprivacy_master/src/app/tomes/v6-lineage/page.tsx` | C-conjecture aggregator page with status grouping | ✅ (user-led) |
| `agentprivacy_master/src/lib/tome-v-acts.ts` | Founding-act anchor data; `getFoundingActForShop()` | ✅ (user-led) |
| `agentprivacy_master/src/lib/tome-v-conjectures.ts` | C18–C46 definitions + `ACT_CONJECTURES` + `parseHonestyLabel()` | ✅ (user-led) |
| `agentprivacy_master/src/components/runecraft/FoundingActPanel.tsx` | Bidirectional shop → act narrative panel | ✅ (user-led) |
| 9 workshop pages | `<FoundingActPanel shopHref={...} />` wired in | ✅ (user-led) |
| `agentprivacy-docs/models/city_of_mages_grimoire_v1_0.json` | v1.0 (60KB) | ✅ retained as historical |
| `agentprivacy-docs/models/city_of_mages_grimoire_v1_1_0.json` | v1.1 (130KB · 39 spells · 13 personas with spells · 14 vertices · enriched) | ✅ canonical · pinned |
| `agentprivacy_master/docs/chronicles/2026-05-09_bound_collection_sync_report.md` | Phase report covering master-only ingestion + remaining work | ✅ |
| `agentprivacy_master/docs/chronicles/2026-05-09_suite_overlap_tracking.md` | Cross-suite tracking reference covering all six sibling directories | ✅ |
| `agentprivacy_master/docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md` | This document | ✅ |

---

## §4 · Coherence map · where the IPFS pin needs to land

The CID is content-addressed: it is one URL that needs to appear in every place the suite refers to the City of Mages spellbook. Five sites:

| # | Site | What changes | Status |
|---|---|---|---|
| 1 | `city_of_mages_grimoire_v1_1_0.json` · `ipfs_pin_status` field | Replace "awaits first pinning" with the live CID | ✅ done in this chronicle's commit |
| 2 | `agentprivacy_master/src/lib/grimoire-ipfs.ts` | Add `export const CITY_OF_MAGES_GRIMOIRE_IPFS_URL = '<CID URL>';` alongside the privacymage exports | ✅ done in this chronicle's commit |
| 3 | `agentprivacy_master/src/app/tomes/page.tsx` IPFS attribution block | The placeholder text can now reference the live CID inline | ⏳ next-pass copy edit |
| 4 | `agentprivacy_master/src/lib/grimoire-baked.ts` | Add a `'tomes'` `SpellbookSource` value + `TOMES_ACT_PERSONA_HINTS` mapping each Tome V act → introduced persona; load the v1.1 JSON at build time the same way the privacymage grimoire is baked | ❌ pending — substantial; gates the persona/spell builder |
| 5 | `swordsman-blade/build.js` and `mages-spell/build.js` | Copy `city_of_mages_grimoire_v1_1_0.json` into each extension's `dist/` alongside the privacymage grimoire; bump extension manifest version | ❌ pending — extensions then ship both grimoires |

**Sites 1 and 2 are immediate-coherence wins** (one-line edits each); they are applied in this commit. Site 3 is a small follow-up. Sites 4 and 5 are the structural finish — the bake pipeline lights up the persona/spell builder; the extension bundles let agents in the open web cast Tomes spells the same way they cast First Person spells. Both are described in `2026-05-09_bound_collection_sync_report.md` §6.3 as Phase D and have not changed.

---

## §5 · State of coherence after this chronicle

What is **operational** (works today, end-to-end):
- Bound-collection content lives at master and is the canonical source for the website's /tomes route
- /tomes lists every act with anchor IDs that land on the right section
- Each of 9 production workshops surfaces its founding act via `<FoundingActPanel />`, including the resident Mage, the spell list (now matching the grimoire's canonical IDs), the v6 conjecture badges, and the honesty discipline
- /tomes/v6-lineage aggregates C18–C46 with status-grouped rendering and per-act cross-links
- The City of Mages grimoire is pinned, content-addressed, and importable as a constant from `grimoire-ipfs.ts`

What is **architectural** (specified, not yet implementation-verified end-to-end):
- The persona/spell builder at `/persona` does not yet load the Tomes grimoire; the spells listed in `<FoundingActPanel />` and on /tomes cast cards are placeholders until `grimoire-baked.ts` admits the `'tomes'` source
- The browser extensions do not yet bundle the Tomes grimoire; extension users still see only First Person spells

What is **resonant-but-not-absorbed**:
- The pre-bound-collection seed work in `agentprivacy-docs/research/` (Acts α/β/γ seeds, NOTE_agt_scales_and_hide, the V6 horizon note's "for the Second Person Spellbook" sections) — kindred but not yet folded into the bound collection's canonical form
- The "City of Mages" role-archetype palette in `agentprivacy-docs/blog/blog-part1-forming-constellations.md` — kindred but at a different layer than the bound collection's named cast

What is **provisional**:
- The Tomes grimoire is v1.1; future v1.2 will add per-act image/video/inscription assets, reconcile the Mages's spell glyphs with the Sigil register, and admit new acts as Tome V grows. Each version gets its own CID; the v1.1 CID stays valid forever.
- The split-IPFS architecture (privacymage grimoire vs City of Mages grimoire) is operational at the file level but not yet validated under multi-grimoire load; gating expected at site #4.

---

## §6 · The chronicle's coherence considerations

*Where this chronicle needs to go for the suite to stay coherent:*

### §6.1 · Where the chronicle file lives

`agentprivacy_master/docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md` — sibling to the sync report and the suite overlap tracking doc. This is the canonical home; the existing chronicle directory uses dated filenames.

### §6.2 · References to the chronicle

The chronicle is referenced from:

- **`docs/weaver/EXPORT_MANIFEST.md`** — already points at the sync report and the tracking doc; this chronicle should be added as the third pointer (the "what shipped" record alongside the "what was found" sync report and the "what's still open" tracking doc).
- **`docs/chronicles/2026-05-09_suite_overlap_tracking.md`** — Status board updated to mark IPFS pinned; grimoire row updated; chronicle linked from the §4.2 row for the grimoire.
- **The grimoire JSON itself** — the new `ipfs_pin_status` value will reference the chronicle as the dated record of the pin.

### §6.3 · Cross-suite implication: the pin makes the split real

Until the pin, the "separate spellbook IPFS, maintained by the City of Mages, distinct from privacymage" framing was a design commitment held in markdown. With the pin, it is **operational** — there are now two CIDs on `sync.agentprivacy.ai`, content-addressed, importable independently, bundled (when the extensions catch up) as two separate JSON files. The architectural split that the user specified during the /tomes rewrite is now load-bearing.

The implication: future Mages who found cities in other ecosystems (per the v1.1 `title_note`) will pin their own First City grimoire to a separate CID under the same title pattern. Each city's grimoire is its own artifact, content-addressed, recognisable by title-kind. The grimoire is a *kind* of book; this CID is the first instance.

### §6.4 · The chronicle's role in the corpus

This chronicle is the **forward-looking record for v1.1**. It complements:

- The bound collection's own `chronicles/` (the writing-side chronicles of how the acts were drafted)
- The repo's `docs/chronicles/` (the implementation-side chronicles of how the acts were rendered)

Both are valid lineages. This chronicle belongs to the implementation side; if a future bound-collection update references the v1.1 pin, it will cite this chronicle as the dated record of when the pin first existed.

---

## §7 · Open queue

Carrying forward from `2026-05-09_bound_collection_sync_report.md` §6 and `2026-05-09_suite_overlap_tracking.md` §4:

### §7.1 · Immediate (≤1 session, low risk)

- `/tomes` IPFS attribution block: replace placeholder text with the live CID inline (small copy edit)
- `/spellbooks` Second Person card reframe: "maintained by City of Mages · separate spellbook IPFS · v1.1 pinned · 14 acts drafted"

### §7.2 · Structural (medium effort, high leverage)

- Bake the Tomes grimoire into `grimoire-baked.ts`: new `SpellbookSource = 'tomes'`, `TOMES_ACT_PERSONA_HINTS` mapping. This lights up the persona/spell builder for Tomes spells.
- Mirror `city_of_mages_grimoire_v1_1_0.json` into `swordsman-blade/` and `mages-spell/`; edit each `build.js` to bundle it; bump extension manifest versions.

### §7.3 · Cross-suite copy-edit pass

- `agentprivacy-docs/`, `agentprivacy-blog/`, `myterms/`, `swordsman-blade/`, `mages-spell/`: ~15 "Second Person Spellbook awaits / next / horizon" strings still treat the Spellbook as upcoming. The pin makes "horizon" demonstrably wrong; one focused pass per directory closes the discrepancy. Tracked in §3.1 of the suite overlap tracking doc.
- IEEE 7012 v3 plan in myterms (and synced to extensions): show where the standard now lands in the actually-opened Spellbook (Tome IV Act IV "The Naming Ceremony" is the closest fit per the sync report).
- City-of-Mages reconciliation note in `blog-part1-forming-constellations.md` (palette layer vs in-world cast layer).

### §7.4 · Deferred (Phase F · substantial)

- City map SVG (`<CityMap />`)
- Lattice render (`<LatticeRender />`)
- `/tomes/cast` dedicated page with sigil grid + per-cast subpages
- Per-act image / video / inscription assets parallel to First Person Acts

---

## §8 · TL;DR

- **The bound collection is ingested** at master.
- **/tomes shows the whole work** — 14 acts, 13 cast members, 5 tiers, with anchored navigation that lands cleanly.
- **Each shop carries its founding myth** via `<FoundingActPanel />`.
- **The C-conjecture index lives at /tomes/v6-lineage** with status grouping and act cross-links.
- **The City of Mages grimoire is v1.1, reconciled with the website's spell IDs, and pinned to IPFS** at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`.
- **The split that the user specified is now operational**: privacymage holds the First Person grimoire; the City of Mages collectively holds the Tomes grimoire; two CIDs, two artifacts, content-addressed.
- **The remaining work is to teach the master pipeline and the extensions to read both grimoires** — that is Phase D in the sync report. Everything else is copy.

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-10
