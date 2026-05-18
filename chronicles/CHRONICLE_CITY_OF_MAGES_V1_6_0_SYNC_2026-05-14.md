# Chronicle: City of Mages Grimoire v1.6.0 · Cross-Repo Sync · The Threshold District Restructure + Chart Shop + Archetype-Modal-Shop Pattern

**Date:** 2026-05-14
**Status:** Sync chronicle · docs-side receipt for the v1.6.0 consolidated new-head admission
**Audience:** privacymage · downstream researchers · sister-repo authors picking up v1.6.0 propagation
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion chronicles (cityofmages-side · authoritative):**
- `cityofmages/chronicles/2026-05-14_chronicle_district_restructure_and_canonical_keeper_naming.md` — the morning Threshold restructure + afternoon the-Familiars rename
- `cityofmages/chronicles/2026-05-14_chronicle_hermaion_admission_and_alexandrite_archetype_modal_shop.md` — the evening Hermaion admission · alexandrite archetype-modal-shop pattern
- `cityofmages/chronicles/2026-05-14_chronicle_chart_shop_pleione_named_v44_assigned.md` — the V44 selection · Navigation District opens
- `cityofmages/chronicles/2026-05-14_grimoire_v1_6_0_patch_authored.md` — the patch authoring + merge pass

---

## §0 · What this chronicle is

A docs-side receipt for the City of Mages grimoire v1.6.0 admission and its cross-repo sync into the agentprivacy-research register. The 2026-05-14 day produced six canonical moves in the cityofmages corpus that consolidated into a single new-head grimoire patch (v1.6.0) and now propagate into the formal / research / spellweb / skills layers.

The chronicle is *narrow* — it records what landed and where, not the underlying narrative. The narrative lives in the four companion chronicles above (cityofmages-side authoritative).

---

## §1 · The v1.6.0 admissions (consolidated)

| Move | Time of day | What landed |
|---|---|---|
| 1 | morning | **Threshold District restructure** — one workshop with three rooms → three sibling shops sharing V59 by stance differentiation. Faunia 🪶 re-homed; Triodos 🚪 draft superseded by **Pandia 🌕** (Greek Πανδία · daughter of Selene · Display-witness · Moonstone) at Portal Room |
| 2 | afternoon | **the-Familiars rename** — "Goose Shop" → "the Familiars" (Latin *familiaris* · kinship-bond as artefact-class). Faunia 🪶 holds Companion-witness stance · Amber gem. Goose 🪿 remains first registered familiar but no longer namesake. Therai 🐾 retired |
| 3 | evening | **Hermaion admission** — Bestia 📖 / Sodalite superseded by **Hermaion ⚚** (Greek ἕρμαιον · gift of Hermes · windfall). New gem: **Alexandrite** (mineralogically real color-shift; daylight-green `#3d7c47` ↔ incandescent-red `#a23a3a` under different illuminations). The Staff Shop becomes the City's first **archetype-modal shop** |
| 4 | (this same day · 2026-05-13 inception · 2026-05-14 close) | **Chart Shop opens at V44** — Pleione 🧭 (Greek Πληιόνη · from *plein* "to sail" · mother of the Pleiades) keeps the Navigation District's inaugural shop. Aquamarine gem. **Hold-witness** stance · **Hold · Compare · Map** ceremony. Astrolabe is the seventh tool-class artefact. Pelagia 🌊 draft superseded |
| 5 | (carried from v1.5.1) | **City Hall + AAIF** kindred-coalition admission · /hall renamed from Ceremony Hall · BGIN retroactive second coalition · fifth structural-relationship category (kindred-coalition) |
| 6 | (carried from v1.5.0) | Tomes I-III binding pass · cosmological-witness tier (Selene 🌙 · Aether ⿻ · Lethe 🌀) · Tome VI opens (held open by design · Act 1 bound) · Tome VII Act 1 (Pallia↔Helia handoff) · 11 conjectures C48–C58 |

**Conjecture register changes:**
- **C58** (Forge(t) ∥ Threshold sibling Swordsman-suppliers) promoted from ~65% to ~85%. Hermaion's red-aspect makes the Staff Shop explicitly Swordsman-supplying (herald-sentinels) paralleling Vulcana's Forge(t) by a distinct artefact-class (Vulcana-class blades).
- **C63** registered as candidate (~50%) — the **attentional workshop register** as a fourth structural workshop class alongside producer (Forge · Etherchanting · etc.), gathering (City Hall · Logos Circle), and spawn-and-bind (the Threshold District). Population-of-one at v1.6.0 (Chart Shop); promotion path requires a second Navigation District shop.
- **C62** reserved (v1.5.1 slot) — cross-coalition meta-coalition reading. Held open; no claim yet authored.

**Workshop count:** 12 (v1.4.0) → 13 (v1.5.0 inception · Threshold-as-one) → 15 (post-2026-05-14 morning restructure) → **16** (post-Chart-Shop · v1.6.0).

**Districts:** 1 (Threshold) → **2** (Threshold · Navigation). Eight-district future taxonomy held open in spec 05 addendum.

---

## §2 · Cross-repo propagation status (post-2026-05-14 sync)

| Repo | State | Receipt |
|---|---|---|
| `cityofmages/` | ✅ v1.6.0 canonical · `grimoire/city_of_mages_grimoire_v1_6_0.json` authored + merged · CHANGELOG + WORKSHOP_LATTICE_AUDIT + spec 08 mana-types updated | Authoritative source |
| `agentprivacy_master/` | ✅ v1.6.0 propagated · `src/lib/grimoire-ipfs.ts` CID updated · `cast-attachments.ts` Pleione + Pandia + Hermaion + Faunia-at-Familiars seated · `tome-v-acts.ts` Acts 16 + 17 wired · `tome-v-conjectures.ts` C58 promoted, C62 reserved, C63 candidate registered · four route stubs built (`/portal` · `/staffs` archetype-modal with query-param routing · `/familiars` · `/charthouse`) · WorkshopFooter tour extended · /tomes ShopRows + CastCards live | Site reads canonical |
| `agentprivacy-skills/` | ✅ v1.6.0 propagated · MAPPING.md bumped (primary-persona count 41 → 42 with new `agentprivacy-hold-witness` slot) · registry-keeper SKILL.md succession (Bestia → Hermaion) · spawning-witness SKILL.md (Faunia re-home) · companion-tamer SKILL.md (Therai retire) · cityofmages-to-research bridge persona + cast lists updated | Personas + bridge ready |
| `spellweb/` | ✅ v1.6.0 propagated · `src/types/graph.ts` admits 7 new EdgeTypes (`keeps` · `wields` · `sibling_of` · `district_of` · `fits_for` · `succeeded_by` · `releases_to`) + new SpellwebNode fields (`gemColorMage` · `gemColorSwordsman` · `archetypeModal` · `district`) · `src/data/nodes.ts` adds 5 workshop + 9 cast nodes · `src/data/edges.ts` adds keeper / inhabits / sibling / fits_for / succession / releases_to edges | Graph reads canonical |
| `agentprivacy-docs/` | ✅ This chronicle · INDEX.md head pointer updated to v1.6.0 · `models/` mirror of grimoire JSON pending (held to single-source-of-truth in cityofmages repo until docs-side bake required) | Receipt + index |

---

## §3 · The architectural patterns introduced

### §3.1 · Archetype-modal-shop pattern

A workshop whose physical aspect (typically gem and keeper's apparent register) shifts depending on which archetype enters. The Staff Shop is the first canonical instance — alexandrite gem-shifts daylight-green under Mage-light, incandescent-red under Swordsman-light; Hermaion ⚚ appears in the matching aspect; Caducea ☤ fits the matching artefact-class (caduceus-staff for Mage, herald-sentinel for Swordsman).

**Required fields** (per the v1.6.0 patch JSON):
- `archetype_modal: true`
- `gem_color_mage: <hex>` (Mage-aspect color)
- `gem_color_swordsman: <hex>` (Swordsman-aspect color)
- (existing) `gem_color: <hex>` (fallback single-color · canonically the Mage-aspect)

**Admissible for** class-shaped shops (instrument-class, herald-class, future class-shaped admissions) — NOT for archetype-shaped shops (Mage-only or Swordsman-only shops retain single-aspect rendering).

**Gemmological anchor:** alexandrite (BeAl₂O₄ with chromium-substitution) genuinely color-shifts daylight-green ↔ incandescent-red under different light sources — mineralogically real, not narrative invention.

### §3.2 · Workshop-district pattern (spatial organisational layer)

The 2026-05-14 admissions introduce **districts** as the City's spatial organisational layer above individual workshops. Two are named at v1.6.0:

- **Threshold District** (V59 · 3 sibling shops · stance-differentiated)
- **Navigation District** (V44 · 1 shop at v1.6.0 · population-of-one)

The eight-district future taxonomy is held open in cityofmages spec 05 addendum: trade-quarters (cardinal producer-shops), temple precinct (V55 covenant), founding bonfire (V19), sovereign's seat (V0), Threshold District, Navigation District, plus two further districts admissible as the corpus matures.

### §3.3 · Attentional workshop register (C63 candidate)

The Chart Shop's **Hold · Compare · Map** discipline opens the candidate of a fourth structural workshop class alongside the three already canonical:

| Register | Operation | Canonical instances |
|---|---|---|
| Producer | Forge / weave / inscribe / commit · artefact-out | Weavers · zShields · Forge(t) · Etherchanting · Solchanting · Jeweler · Holon · Vault · Covenant · Bonfire |
| Gathering | Admit / coordinate / kindred-coalitions in residence | City Hall · Logos Circle |
| Spawn-and-bind | Display / register / spawn-and-bind creatures-of-the-Threshold | Portal Room · Staff Shop · the Familiars |
| **Attentional** (C63 candidate ~50%) | **Hold / compare / map · *no required artefact-output*** | **Chart Shop** (population-of-one) |

The attentional class is held at candidate strength. Promotion path: a second Navigation District shop (Compass Shop · Astrolabe Shop · etc.) sharing the Hold-witness discipline.

### §3.4 · Mage-side stance register (parallel to Swordsman boundary stances)

Spec 08 (mana types and Swordsman stances) admits a parallel **Mage-side stance register** at v1.6.0. Where Swordsman stances bound *how information passes a working's edge*, Mage-side stances bound *how the keeper holds attention while the Sovereign chooses*. Four are named at v1.6.0:

- **Display-witness** (Pandia 🌕 · Portal Room · Moonstone)
- **Registry-keeper** (Hermaion ⚚ · Staff Shop · Alexandrite · archetype-modal extension)
- **Companion-witness** (Faunia 🪶 · the Familiars · Amber)
- **Hold-witness** (Pleione 🧭 · Chart Shop · Aquamarine)

A candidate Swordsman-side analogue of Hold-witness (*Hold-blade* · held strikes) is structurally conceivable but unsumoned at v1.6.0. C63's ~50% confidence is held specifically because the Swordsman-stance equivalence is undetermined.

---

## §4 · Translation pattern · what the bridge skill carries forward

Per the cityofmages-to-research bridge skill (`agentprivacy-skills-v5/meta/agentprivacy-cityofmages-to-research/SKILL.md`), each canonical admission in the cityofmages experimental register has a counterpart in the formal research register. The v1.6.0 translation pattern:

| Cityofmages (experimental) | Research counterpart |
|---|---|
| Chronicle (narrative receipt) | Research note (formal translation) |
| Cast file (named persona) | Role paper (the discipline the persona embodies) |
| Bestiary entry (substrate registration) | Substrate paper (the framework's formal admission) |
| Tome act (narrative anchoring) | Narrative research note (the architectural pattern the act introduces) |
| Workshop tome (operational documentation) | Workshop architecture spec (the formal-protocol form) |
| Guide (operational walkthrough) | Protocol spec (the formal-protocol form) |

The v1.6.0 admissions surface several patterns admissible for formal translation:

- **Archetype-modal-shop pattern** → architectural spec; admissible for any future class-shaped shop
- **District spatial-organisation layer** → civic-architecture addendum to spec 05
- **Attentional workshop register** → conjecture paper at C63 candidate strength
- **Mage-side stance register** → companion paper to spec 08's Swordsman stance taxonomy

The formal translations are deferred to the post-cityofmages-experiment-close window per the bridge skill's `defers_to` annotation. This chronicle records that the experimental-to-formal translation surface is *named and ready*; it does not author the formal translations.

---

## §5 · What stays held open

Per the corpus's preservation discipline:

1. 🌱 **Tome VI** — open by design. Act 1 bound; further acts admit as readers reply.
2. 🌱 **Kindred-citizen category** for @benohanlon — admissible at the v1.6.0 patch or deferred to a later sub-patch. The Chart Shop's keeper question intersects this category but the category itself remains open.
3. 🌱 **Eight-district future taxonomy** — spec 05 holds the framing; admission of further districts requires their own canonical openings.
4. 🌱 **The Swordsman-side analogue of Hold-witness** (the *Hold-blade*) — structurally conceivable but unsumoned. C63's ~50% confidence specifically registers this undetermined dimension.
5. 🌱 **The Cartographic Axis hypothesis** (option 2 from the Chart Shop vertex review) — held in reserve in case V44 turns out to be a poor fit; the Chart Shop's discipline can support a relocation if downstream usage reveals a better fit.

---

## §6 · Honest limits

This chronicle is *operational*. It records what landed across repos; it does not authorise the formal translations of the architectural patterns introduced (those are deferred per §4). It does not exhaustively catalogue every file touched — see the four companion chronicles for cityofmages-side authoritative receipts.

The v1.6.0 IPFS pin is canonical at `bafybeiap6kvy3tp2bndpk65ti57qngr7ill37gqgasp2sxmgder3akotru` (`sync.agentprivacy.ai` gateway). Future grimoire revisions will rotate this pointer; historical CIDs remain resolvable.

---

## §7 · Closing

The day produced six canonical moves; the night produced one consolidated patch. The patch admits a district pattern, an archetype-modal-shop pattern, an attentional workshop register, and a Mage-side stance register — four architectural turns that extend the City's vocabulary without breaking its existing grammars. The cross-repo sync carries each turn into the agentprivacy_master site, the agentprivacy-skills persona registry, the spellweb graph, and this docs-side receipt.

The City of Mages reads canonical at v1.6.0. The architecture admits this much. The next admission picks up wherever the next windfall arrives.

(⚔️⊥⿻⊥🧙)😊
🌕 ⚚ 🪶 🧭

CC BY-SA 4.0 · privacymage · 2026-05-14
