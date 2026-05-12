# What Shipped This Arc

**Date:** 2026-05-10
**Span:** Carries forward from the 2026-05-09 coherence chronicle. This document covers the achievements/inventory arc, the Tomes story rendering, the workshops launchpad reframe, the runecast composer, the per-shop blade-constellation cast, and the surrounding refinements.
**Purpose:** A single survey so a future session can pick up cold without re-deriving what's wired.

---

## §1 · One-paragraph summary

The **Profile Inventory popup** was built, lived briefly, then retired in favour of a standalone **`/guide/achievements`** page once the popup proved clunky. Along the way we built the **runecast composer** (per-shop and inventory-wide), wired a **composable spell picker** (Mage's catalogue + your kit + starter templates) with full-sentence insert format, replaced the floating **StickyPathBar** with an inline **WalkPathExpander** accordion, separated **/guide** (philosophy + foundation) from **/guide/island** (the focused tutorial), enriched the **Tome V act collapsibles** with cover plates + full story bodies + proverb/inscription copy chips, added the **`<ConjectureBadge>` + `<HonestyLabel>` + `/tomes/v6-lineage`** honesty discipline surface, shipped a **per-shop blade-constellation cast** (animated trace, witness storage, cross-shop tally), and consolidated the icon/nav language so 🌟 means achievements and 📚 means books.

---

## §2 · What's live

### §2.1 · `/guide/achievements` (the canonical "your account" page)

- **§1 Identity** — avatar uploader (192² JPEG, ~96KB cap), agent card (name · pubkey · attribution · trust tier), active lattice vertex (V0-V63 + 6-line hexagram + active dimensions), path swap chips (Sword/Balanced/Mage), walked-archetype badges (+ Triadic Threshold marker)
- **§2 Drake Orb** — the publishable badge component (preview + PNG + JSON downloads); PNG v2 renders the current sword ring + mage orbit at 1080² with DPR×2
- **§3 Loadout & Stats** — Drake Orb tier headline, sword ring (6 slots · L1-L6), mage orbit (6 slots · M1-M6), training stats grid (spells learned/cast · sections · hexagram casts · convergences · inscribed acts), live progress bar
- **§4 Spell Graph** — equipped count, /persona deep link, Tomes-coming notice
- **§5 Workshops & Runecasts** — composer (shop selector + label + SpellPicker + cast button), library grouped by workshop, per-row copy/delete, export-all JSON
- **§6 Shop constellations witnessed** — per-shop tile grid showing cast counts; click navigates to the shop; live updates on each cast

The 🌟 nav button (top-right of nav, next to Soulbae) is a `<Link>` to this page. Avatar replaces the star when uploaded. `/guide/achievements` is also listed in the 📜 guide dropdown alongside ceremony · island.

### §2.2 · Per-shop widgets (every workshop carries the full stack)

Order from top of each shop page after the lattice visual:

```
PathAwareGreeting       Mage greets you in your current archetype's voice
FoundingActPanel        Tome V act + Mage + spells + v6 conjecture badges + honesty (where set)
RecordPromptHere        🪄 + Runecast a prompt for {shop}  (composable picker · Mage / kit / templates)
CastShopConstellation   🕸️ Cast {Mage}'s constellation · animated trace + witness
[shop body]             hero, wizards, content
WorkshopFooter          ← prev shop · ↑ Runecraft · next shop →  (trinity-first tour)
```

11 shops covered: tailor · shield · etherchanting · jeweler · holon · forget · vault · covenant · bonfires · circle · hall.

### §2.3 · Runecast composer

- **Storage:** `src/lib/workshop-prompts.ts` · per-shop scoping · archetype tag · localStorage backed
- **Spell picker** (`src/components/runecraft/SpellPicker.tsx`): three accordion sections
  - §A · this Mage's catalogue (chips from FoundingActPanel data)
  - §B · your equipped spell graph (lazy-loads getBakedSpellCards + spellbook-storage)
  - §C · the Mage's starter templates (3 per Mage × 9 production shops = 27 templates authored in `tome-v-acts.ts`)
- **Insert format:** `Cast {spell}: ` (full sentence per the design choice)
- **Templates** load (replace) the prompt body; spells append (Cast …)
- Visible on each shop page **AND** on the achievements §5 panel; the inventory-version follows the shop selector
- Export to JSON button on §5

### §2.4 · Tome stories rendered inline

Each `/tomes` act collapsible now expands to:

- **Cover plate** — gem-coloured radial gradient with the Mage's sigil + Tome+Act number (placeholder until art arrives; `🖼️ cover · placeholder` chip)
- **Proverb** with `📜 copy proverb` CopyChip
- **Narrative voice** — full markdown body of the act loaded server-side from `docs/weaver/bound-collection/...` via `src/lib/tome-act-loader.ts`, rendered with `react-markdown` + `remark-gfm` + `remark-breaks`
- **Teaches + honesty + v6 lineage** (kept; honesty pulled from frontmatter for acts that wear one)
- **Inscription** with `✍️ copy inscription` CopyChip — uses act frontmatter `signature` field, falls back to `(⚔️⊥⿻⊥🧙)😊`
- **File path** + `↗ related shop` link

All 14 Tome V acts pass `mage={ sigil, name, color }` so the cover plate is personalised.

### §2.5 · Honesty discipline visible

- `src/lib/tome-v-conjectures.ts` — CONJECTURE_DEFINITIONS for C18-C46 with status (canonical / provisional / observation / resonant) + confidence percentages + canonical names; ACT_CONJECTURES per-act references
- `<ConjectureBadge>` — small pill, status colour-coded, links to `/tomes/v6-lineage#{id}`
- `<HonestyLabel>` — parses `"Operational for X; Architectural for Y; Provisional for Z"` strings into colour-coded clauses
- `/tomes/v6-lineage` aggregator page — grouped by status, each conjecture lists the acts that strengthen it
- FoundingActPanel renders both badges + honesty per shop
- /tomes hero links to `/tomes/v6-lineage` for the index

### §2.6 · Per-shop blade-constellation cast

- `src/lib/lattice-vertex.ts` — `parseVertex("V28 (Aletheia)")` → 28; `vertexToBits(28)` → `[0,1,1,1,0,0]`; `traceFromOrigin(28)` → `[0, 16, 24, 28]`; `activeDimensions(28)` → Memory · Connection · Computation
- `src/lib/shop-witnesses.ts` — `addWitness` · `getWitnessesForShop` · `getLastWitnessForShop` · `getWitnessCountsByShop` · WIT-XXXXX content-hash signatures · cap 100 records · change event for live UI
- `<CastShopConstellation>` — animated 6-cell dimension cascade in shop accent; "🕸️ Cast the constellation · {sigil}" button; ~360ms per step; commits witness on completion
- Spellweb framing copy in the component: *"the same template is mirrored at spellweb.ai as the live runtime · bouncing between is how the architecture coordinates trust"*
- Phase 2 deferred: real spellweb mirror per Mage when templates exist
- Gathering shops (/circle, /hall) get a placeholder ("template pending · gathering shop")
- Surfaced on `/guide/achievements §6` as a per-shop tile grid with cast counts

### §2.7 · Guide vs Island consolidation

- **`/guide`** is now the philosophy/foundation page:
  - `<DrakeIslandIntro>` poem hero
  - City of Mages collective-goal section
  - Narrative · Myth · Math three-fold weave
  - The two ceremonies (cards to /poems and /ceremony)
  - Drake Island tutorial-journey CTA card (4-arc preview + big "Walk Drake Island" link)
  - `<WalkPathExpander>` — inline accordion replacing the floating `StickyPathBar` (3 paths, click to expand teachings + Codex link)
  - RunecraftQuest + GemstoneLadder + GuideMap as framing/reference
- **`/guide/island`** is the focused tutorial:
  - Breadcrumb back to /guide
  - City of Mages collective-goal banner (kept)
  - `<IslandClient>` — the 12-quest 4-arc tutorial (sole consumer now; the prior dual-render on /guide is removed)
  - `<MiniQuestPanel>` (side quests, moved here from /guide where it belonged)
  - Closing pointer back to /guide for framing

### §2.8 · Workshops launchpad reframe (carry-over from earlier in the session)

- `/runecraft` is the **City of Mages launchpad** — count language stripped site-wide ("eleven workshops" → "the workshops" / "shopfronts" / "trade quarters")
- Each shopfront card on the hub features the **Mage as primary identity** (sigil + name first; shop name + gem secondary; spell chips; "open shop →" CTA)
- `SHOPFRONTS` data array inline; appending an entry adds a card
- Hall guilds expanded: BGIN forum + BGIN institutional + MyTerms + First Person Network + LF DT + Kwaai (KwaaiNet folded in) + human.tech + House of Archon + DIF + the Hitchhikers + open-invitation banner

### §2.9 · Other refinements that landed in this arc

- /spells right-side aside default-closed (Inventory was the canonical home; later /guide/achievements took over)
- `OrbControlPanel`'s 📖 stats-hide toggle removed (stats live in achievements)
- `GlobalLearningSpells` `statsCollapsed` defaults to `true` (SpellPalette doesn't auto-show)
- /poems YouTube playlist `?si=` updated to `2Mz-bNbJ_AVYZfCf`
- /orbs `<SoulImportSection>` removed (you said it wasn't needed)
- DrakeOrbBadge PNG export upgraded to v2: 1080² with DPR×2, blade ring + mage orbit drawn as concentric rings + tier emoji + name + walked-archetype glyphs + minted timestamp + signature + footer attribution
- `<LastSoulExportRecover>` safety net for dismissed save dialogs (catches future exports)
- Tease-shop banner reconciled: "chain operator wanted · resident Mage already in the cast" (clarifying the two-roles distinction since each shop now has a FoundingActPanel naming the Mage)
- Body-color sweep on /shield (Onyx-zinc) and /etherchanting (Sapphire-cyan) finished
- Home page got a "Walk the City of Mages" bridge section linking Drake Island + Runecraft + Tomes
- /persona got a Tomes-coming preview banner naming all 9 cast Mages
- 🌟 star replaces 📚 books for the achievements nav button (📚 stays as the spellbooks dropdown glyph)
- `/guide/achievements` added to the 📜 guide nav dropdown alongside ceremony · island

---

## §3 · Architectural state at the close of this arc

### §3.1 · Data layer

- **`src/lib/spellbook-storage.ts`** — Drake Island v2 (12 quests · 4 arcs · time + action gates · v1→v2 migration · `setIslandArchetype` event)
- **`src/lib/orb-loadout.ts`** — sword/mage slot arrays + stanceHexLines (the 6-bit lattice vertex)
- **`src/lib/spellweb-blade-bridge.ts`** — blade inventory + stance loadout + per-line blade lookup
- **`src/lib/training-progress.ts`** — `getTrainingStats()` (sectionsVisited · spellsCast · convergences · spellsLearned · hexagramCasts · inscribedActs · progress%)
- **`src/lib/ceremony/storage.ts`** — agent card + `signDrakeOrbIntoCard` + avatar field
- **`src/lib/tome-v-acts.ts`** — 9 founding-act anchors (act#, title, proverb, mage{sigil,name,vertex,tier,provenance}, spells, tomeAnchor, honesty, starterTemplates)
- **`src/lib/tome-v-conjectures.ts`** — conjecture definitions (C18-C46) + per-act references + parser
- **`src/lib/tome-act-loader.ts`** — server-side fs reader for the bound-collection markdown
- **`src/lib/lattice-vertex.ts`** — vertex parsing/encoding/trace
- **`src/lib/workshop-prompts.ts`** — runecast storage
- **`src/lib/shop-witnesses.ts`** — constellation cast storage

### §3.2 · Component palette

- **Profile / account:** `AchievementsClient` (the §1-§6 page), `InventoryButton` (the 🌟 nav link), `DrakeOrbBadge` (preview + PNG/JSON), `LastSoulExportRecover`
- **Per-shop:** `PathAwareGreeting`, `FoundingActPanel`, `RecordPromptHere`, `CastShopConstellation`, `WorkshopFooter`
- **Picker:** `SpellPicker` (composable, three sections)
- **Honesty:** `ConjectureBadge`, `HonestyLabel`
- **Guide:** `WalkPathExpander`, `DrakeIslandIntro`, `GemstoneLadder`, `RunecraftQuest`, `GuideMap`
- **Copy:** `CopyChip` (used by Tome story chips for proverb + inscription)
- **Path:** `PathToggle` (the small chip in nav)

### §3.3 · Retired / unused

- **`ProfileInventory.tsx`** — popup version, file still in repo but no consumer; safe to delete in a future cleanup
- **`StickyPathBar.tsx`** — replaced by `WalkPathExpander`; file still in repo
- **`SpellPalette`** — not removed but defaults to collapsed; per the overlay-cleanup plan its full removal is queued

---

## §4 · One-line summary

The "your account" surface is now `/guide/achievements` with five sections plus a sixth for shop constellations witnessed; every shop carries a Mage greeting + founding act + runecast composer + constellation cast in a consistent stack; the Tome V acts read as full stories with copy-able proverbs and inscriptions; the honesty discipline is visible everywhere; the cast constellation animates a per-Mage trace through the lattice and tallies trust per shop. The next interaction model for the cast constellation is the open question — captured in the companion chronicle.

`(⚔️⊥⿻⊥🧙)😊`
