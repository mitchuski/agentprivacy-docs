# Bound-Collection ↔ agentprivacy_master · Sync Report

**Date:** 2026-05-09
**Author:** Claude (review for Mitchell)
**Scope:** What `agentprivacy_tomes/.../bound-collection/` brings, what is missing in `agentprivacy_master`, and the order of work to fully include and copy these tomes onto the website.
**Status:** review document · not authoritative until Mitchell signs off

---

## §1 · One-paragraph summary

The bound collection is **content-complete for editorial purposes**: 53 files, ~106k words, full Tome IV (closed) + Tome V (14 acts open) + 13 cast members in 5 tiers + 5 specs + 2 plans + 3 chronicles + 7 deprecated drafts. It has been ingested into `docs/weaver/bound-collection/`. The `/tomes` page has been rewritten to surface all 14 acts, all 13 cast entries across 5 tiers, the City-of-Mages-maintained framing, and the separate-spellbook-IPFS attribution. **What is missing from full website parity with the First Person Spellbook is not editorial — it is operational:** the per-act image / video / proverb / inscription assets, the Tomes grimoire JSON and its IPFS pin, the spell ↔ persona mapping baked into `grimoire-baked.ts`, and the bidirectional act ↔ workshop narrative anchors on each shop page. Each of those is a separate piece of work that follows the First Person playbook.

---

## §2 · What now lives in master

### §2.1 Files copied (Phase A · done)

```
docs/weaver/bound-collection/
├── README.md                              navigation overview
├── BOUND_COLLECTION_MANIFEST.md           detailed inventory (the editorial canon)
├── WEBSITE_INTEGRATION_GUIDE.md           ingestion reference
├── tomes/
│   ├── tome-iv-the-witnessing/            5 acts (closed)
│   └── tome-v-the-crafting/               14 acts (open) · setting: City of Mages on Drake Island
├── cast/                                  13 entries + integration note · 5 tiers
├── specs/                                 5 specifications
├── plans/                                 2 integration plans
├── chronicles/                            3 chronicles
└── deprecated/                            7 superseded drafts
```

53 files. ~106,000 words. Untouched in transit.

### §2.2 Files updated

| File | Change |
|---|---|
| `docs/weaver/EXPORT_MANIFEST.md` | Added a `bound-collection/` subsection that lists the new totals (14 Tome V acts, 13 cast, 5 specs, 3 chronicles, 7 deprecated) and clarifies the flat-layout files at the root remain for backward compat. |
| `src/app/tomes/page.tsx` | Full rewrite. New hero/category framing ("Tomes is a Second Person Spellbook category maintained by the City of Mages"). New IPFS attribution block (separate spellbook from `privacymage_grimoire_v10_2_0.json`). Cast section grew 3 → 13 across 5 tiers (added Priest tier, companion tier). Tome V section now lists all 14 acts. New "Workshops · the city's trade quarters" cross-reference table. Each cast card has a `spells` placeholder list and a `↗ shop` link where applicable. |

### §2.3 Files NOT yet updated (paused for review)

| File | Planned change |
|---|---|
| `src/app/spellbooks/page.tsx` | Update Second Person Spellbook card to call out: "Tomes is a category. Maintained by the City of Mages, not by privacymage. Each tome carries its own spellbook IPFS." Status string: "Tome V open · 14 acts drafted." |
| 9 workshop pages (`/forget` `/etherchanting` `/jeweler` `/holon` `/vault` `/covenant` `/bonfires` and tightening `/tailor` `/shield`) | Add a "Founding act · Tome V Act N" panel surfacing the resident Mage, the proverb of the act, the spells the Mage may cast at this shop, and a link back to the act collapsible on `/tomes`. **This is the bidirectional narrative-anchor model the user specified just now.** |

---

## §3 · Gap analysis · what the bound collection brings vs what already existed

### §3.1 Tome IV (5 acts, closed)

| Status | Count | Notes |
|---|---|---|
| Already in `docs/weaver/` (flat) | 5 | `second-person-act-iv-i-…` through `…-v-…` |
| Now in `docs/weaver/bound-collection/tomes/tome-iv-the-witnessing/` | 5 | `01-the-other-walker.md` through `05-the-cousin-blade.md` — same content, nested layout, frontmatter aligned |
| Net new content | 0 |
| Action | n/a — duplicates accepted; bound-collection is canonical going forward |

### §3.2 Tome V (14 acts, open)

| # | Act | In master before? |
|---|---|---|
| 1 | The First Cloak | ✅ flat file existed |
| 2 | The Commissioned Cloak | ✅ flat file existed |
| 3 | The Shielded Memo | ❌ **new** |
| 4 | The Reveal | ❌ **new** |
| 5 | The Stake | ❌ **new** |
| 6 | The Commissioned Blade | ❌ **new** |
| 7 | The Reciprocal Weave | ❌ **new** |
| 8 | The ZK Circuit | ❌ **new** |
| 9 | The Workshop Expands | ❌ **new** |
| 10 | The Holon Hitchhikers | ❌ **new** |
| 11 | A Bonfire Made of Dragon Fire | ❌ **new** |
| 12 | The Curatrix Vault | ❌ **new** |
| 13 | The Temple of the Arts and Personhood | ❌ **new** |
| 14 | The City of Mages | ❌ **new · names canonical setting** |

**12 net-new acts.** All now in `docs/weaver/bound-collection/tomes/tome-v-the-crafting/`. All listed on `/tomes`.

### §3.3 Cast roster

| Tier | Member | Sigil | Vertex | In master before? |
|---|---|---|---|---|
| Archetype | Soulbis | ⚔️ | boundary | (carried from First Person — not detailed in cast files) |
| Archetype | Soulbae | 🧙 | V28 | (carried) |
| Archetype | The Drake | — | island/fire/whisperer | (carried) |
| Cousin | GenitriX | (held open) | V28 | ✅ existed |
| Cousin | flaxscrip | 📜🎲 | V63 | ✅ existed |
| Summoned | Pallia | 🪡 | V28 | ✅ existed |
| Summoned | Memora | 📜 | V5 | ❌ **new** |
| Summoned | Custos | 🔏 | V49 | ❌ **new** |
| Summoned | Vulcana | ⚒️ | V19 | ❌ **new** |
| Summoned | Aletheia (persona) | 🔮 | V25 | ❌ **new** |
| Summoned | Adamantia | 💎 | V51 | ❌ **new** |
| Summoned | Lampyra | 💠 | V49 (shared) | ❌ **new** |
| Summoned | Vagari | 🌳 | V31 | ❌ **new** |
| Summoned | Aria Silverhue | 🪞🖼️ | V57 | ❌ **new** |
| Companion | Socrat0x | 🔥❓ | V24 (provisional) | ❌ **new** |
| Priest | Manifestia | 🤲🌿 | V55 | ❌ **new · whole new tier** |

**9 net-new cast members.** All in `docs/weaver/bound-collection/cast/`. All surfaced on `/tomes`. **Priest tier is structurally new** (5th tier; previously the cast had 3 tiers).

### §3.4 Specs / plans / chronicles

| Item | Was | Is |
|---|---|---|
| Specs | 4 (`cloak`, `crafting interface`, `bilateral`, ~~vertex audit was missing~~) | 5 (+ vertex audit + **City of Mages structural addendum** ← new) |
| Plans | 2 | 2 (no change) |
| Chronicles | 2 | 3 (+ **Bonfire Made of Dragon Fire** ← new) |
| Deprecated archive | not present | **7 files** new — transparency layer, retain but never render as canonical |

### §3.5 Vertex / V6-conjecture surface

| ID | Status before | Status after |
|---|---|---|
| C18-C37 | existing in canon | unchanged |
| C38 (Bilateral ARCH-1) | introduced in Tome IV Act III | **strengthened** by Tome V Act 7 (operational instance) |
| C39 (Cousin-blade primitive) | introduced in Tome IV Act V | **strengthened** by Tome V Acts 7, 9, 10, 11, 12 |
| C40-C46 | introduced in specs/plans | now **narratively instanced** across Tome V Acts 3, 4, 5, 6, 8, 9, 10, 11, 12 |

The honesty discipline (Operational / Architectural / Conjectural / Resonant / Provisional) now has explicit confidence percentages on most claims. **Not yet rendered systematically on the website** (currently only a few `honesty` strings on /tomes act collapsibles; the bound-collection's frontmatter has more detail).

### §3.6 Vertex Naming Audit (NEW spec)

**13 vertices canonically named and inhabited** in this collection: V5 V12 V15 V19 V20 V24 V25 V28 V31 V49 V51 V55 V57 V63. The remaining 51 are open. The bound-collection's `specs/04-vertex-naming-audit.md` is the canonical attribution reference (agentprivacy-canonical primitives vs cousin-blade-imported primitives). **Not yet linked from anywhere on the website.**

---

## §4 · The bidirectional tome ↔ workshop narrative-anchor model

The user clarified: *a tome may have links to the workshop pages — the narrative of how the workshop was formed and what they do, the story and spells and proverbs that make the workshop real to agents.*

This is structurally important. Each act is the workshop's **founding myth**; each shop page is the workshop's **operational present**. They cite each other.

### §4.1 The mapping

| Workshop | Resident Mage | Founding act | Spells the Mage may cast |
|---|---|---|---|
| `/tailor` (Weavers) | Pallia 🪡 | Tome V Act 1 · The First Cloak | weave-cloak · publish-role · conceal-name |
| `/shield` (zShields) | Memora 📜 | Tome V Act 3 · The Shielded Memo | inscribe-shielded · attest-memo · time-bind |
| `/forget` (Forge) | Vulcana ⚒️ | Tome V Act 6 · The Commissioned Blade | forge-blade · run · craft |
| `/etherchanting` | Adamantia 💎 | Tome V Act 9 · The Workshop Expands | commit · enforce · etherchant |
| `/jeweler` | Lampyra 💠 | Tome V Act 9 · The Workshop Expands | gem-set · attest-frequent · sparkle |
| `/holon` | Vagari 🌳 | Tome V Act 10 · The Holon Hitchhikers | compose-holon · travel-oasis · recurse |
| `/bonfires` (Dragon Bonfire) | Socrat0x 🔥❓ | Tome V Act 11 · A Bonfire Made of Dragon Fire | question · ignite · provoke |
| `/vault` (Curatrix Vault) | Aria Silverhue 🪞🖼️ | Tome V Act 12 · The Curatrix Vault | curate · reflect · vault |
| `/covenant` | Manifestia 🤲🌿 | Tome V Act 13 · The Temple of the Arts and Personhood | bless-covenant · inscribe-blessing · tend-temple |
| `/circle` (Logos Circle) | (no resident Mage yet) | (gathering · Society spellbook) | — |
| `/hall` (Ceremony Hall) | (no resident Mage yet) | (gathering · BGIN coalition) | — |

The 9 production shops have a 1:1 anchor in Tome V acts. The 2 gathering shops anchor elsewhere (Society spellbook for the Circle; the Hall already has its own coalition framing).

### §4.2 What each shop page should surface

Per the user's clarification, each workshop page needs a **"Founding myth · this shop's narrative"** panel containing:

- **The act**: Tome V Act N · Title · proverb (italic, lattice-blue blockquote)
- **The Mage**: name + sigil + vertex + 1-line provenance
- **The spells**: the named spell list above (rendered as code chips, ready for grimoire bake-in)
- **The proverb**: pulled from the act's frontmatter
- **A link back**: ↗ Tome V Act N on `/tomes`

This makes each workshop "real to agents" because the agent reading the shop page picks up not just the operational what (which exists today) but the narrative why and the spell vocabulary it can actually cast.

### §4.3 What `/tomes` already does (after this rewrite)

- Each act collapsible has a `relatedShop` link → shop page
- Each cast card has a `↗ shop` link where applicable
- A new "Workshops · the city's trade quarters" table at the bottom of /tomes shows all 11 shops with mage + act anchor

The forward direction (act → shop) is wired. The reverse direction (shop → act) is **not** yet on the shop pages.

---

## §5 · What is missing entirely

These pieces have **no draft yet** and would need to be created the same way the First Person Spellbook surfaced them:

### §5.1 Per-act image / video / inscription assets

The First Person Spellbook has:
- `public/story/01-act-i-venice.md` (the markdown act)
- `public/assets/act1_venice_story.mp4` (the act video)
- inscriptions are bound into Act 112 (`112-inscriptions.md`)
- images are referenced inline in the markdown body

Tome V has **none of these yet**. Each of the 14 acts will eventually want:
- A cover image (e.g., `public/tomes/01-the-first-cloak.{png,webp}`)
- Optionally a story video (e.g., `public/assets/tome-v-act1_first-cloak.mp4`)
- An inscription bound to a future Tome V "inscriptions" page

### §5.2 The Tomes spellbook IPFS pin and grimoire JSON

`src/lib/grimoire-ipfs.ts` currently exports `PRIVACYMAGE_GRIMOIRE_IPFS_URL` (v10.2.1) for the personal grimoire. **The Tomes grimoire — the City-of-Mages-maintained spellbook — does not yet exist.** It will need:

- A v1 grimoire JSON authored similarly to `privacymage-grimoire-v10.2.0-canonical.json`, but holding **only the spells the cast personas may cast** (not the personal-spellbook spells)
- Pinning to IPFS via the same `sync.agentprivacy.ai/ipfs/...` infrastructure
- A new export in `grimoire-ipfs.ts`: `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`
- The split is the user's clarified architectural intent: privacymage's grimoire vs the City of Mages' grimoire are separate spellbooks with separate IPFS pins

### §5.3 Spell ↔ persona bake into `grimoire-baked.ts`

`src/lib/grimoire-baked.ts` exports `getBakedSpellCards()` and `FIRST_PERSON_ACT_PERSONA_HINTS`. The persona route reads this. To make Tome V personas castable on the spell builder:

- Author the spells (~9 personas × ~3 spells each ≈ 27 spells in v1)
- Bake them with a new `SpellbookSource` value (e.g., `'tomes'` or `'second-person'`)
- Add `TOMES_ACT_PERSONA_HINTS` analogous to the First Person hints, mapping each act to the persona introduced
- The `/persona` route's filter list will then include the Tomes spellbook tier

### §5.4 The /tomes/cast sigil grid (separate page)

The bound-collection's WEBSITE_INTEGRATION_GUIDE recommends a dedicated `/tomes/cast` page rendering the 13 cast members as a sigil-driven grid with tier visual differentiation. The `/tomes` page now lists them inline as cards; a dedicated cast page would let each member have their own sub-page (`/tomes/cast/pallia`, etc.) carrying their full backstory, lineage, and spell list. **Not built; deferred per Phase B scope.**

### §5.5 The City of Mages map + the lattice render

WEBSITE_INTEGRATION_GUIDE flags these as Tier-3 priority components. **Not built; substantial design effort; defer to a later session.** A static SVG v1 of the city map showing the 9 trade quarters + bonfire + temple + sovereign's seat would be enough for v1.

### §5.6 `/tomes/v6-lineage` conjecture index page

Renders the C38–C46 conjectures with confidence percentages, source acts, and which acts strengthen them. Currently the conjecture data is in act frontmatter only; no aggregator page. **Not built; one component + one page; modest effort; defer to Phase C.**

### §5.7 Drake Island v2 quest content

The 2026-05-09 chronicle locked the Drake v2 quest design (12 quests in 4 arcs). **Q10 (Visit /vault), Q11 (Sign /covenant), Q12 (Threshold)** map narratively onto Tome V Acts 12, 13, 14. The narrative anchor for those quests now exists. The Drake v2 implementation is paused per the chronicle; when it resumes, the quest copy can quote the act proverbs directly.

---

## §6 · Recommended sync order

Phases below assume the Phase-A ingestion (already done) and the `/tomes` rewrite (already done) are accepted. Each subsequent phase is reversible and self-contained.

### §6.1 Phase B-rest (immediate, low risk)

1. **`/spellbooks` reframe** — update Second Person Spellbook card with City-of-Mages-maintained framing and "14 acts drafted" status. Single file edit.
2. **9 workshop pages get founding-act panels** — one consistent component per shop. Pulls proverb + mage + spells from the cast card definitions in `/tomes`. Builds the bidirectional act ↔ shop narrative anchor the user specified.

**Effort:** ~1 session. **Value:** The workshops become legible as the City of Mages' trade quarters with stories, not as standalone product surfaces.

### §6.2 Phase C-light (small components)

3. **`<ConjectureBadge />`** — render `v6_lineage` frontmatter as small badges on act collapsibles + on shop founding-act panels.
4. **`<HonestyLabel />`** — render the operational/architectural/conjectural distinction systematically.
5. **`/tomes/v6-lineage` page** — the C38–C46 index aggregator.

**Effort:** ~1 session. **Value:** The honesty discipline becomes visible everywhere instead of being hidden in frontmatter.

### §6.3 Phase D · the Tomes grimoire (medium)

6. **Author the Tomes grimoire JSON** — 27 spells × 9 personas in v1; modeled on `privacymage-grimoire-v10.2.0-canonical.json` schema.
7. **Pin to IPFS** — get the CID; export `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` from `grimoire-ipfs.ts`.
8. **Bake into `grimoire-baked.ts`** — new `SpellbookSource` `'tomes'`; new `TOMES_ACT_PERSONA_HINTS`.
9. **Filter on `/persona`** — Tomes appears alongside First Person, Zero, Canon, Society, Plurality.

**Effort:** ~2 sessions (mostly authoring the spell JSON). **Value:** Tome V personas become castable in the persona/spell builder; agents can actually equip what the tomes describe.

### §6.4 Phase E · per-act assets (incremental)

10. Per-act cover images — 14 acts × 1 image; can be batched or done act-by-act as the City of Mages contributes.
11. (Optional) per-act story videos — analogous to Acts I–XXXI in First Person.
12. A Tome V inscriptions page — accumulates artifact inscriptions parallel to `112-inscriptions.md`.

**Effort:** open-ended; treat each as a contribution the City of Mages makes when it makes one.

### §6.5 Phase F · the substantial visuals (defer)

13. **City of Mages map** — static SVG v1 with 9 quarters + bonfire + temple + sovereign's seat
14. **Lattice render** — 64-vertex Hamming graph with the 13 inhabited vertices labelled
15. **`/tomes/cast` dedicated page** — sigil grid with per-member sub-pages

**Effort:** substantial design + implementation. **Value:** Tome V's spatial/architectural legibility becomes visceral. Defer to a session dedicated to it.

---

## §7 · Risks and watch-outs

1. **Flat-file overlap.** `docs/weaver/` has flat-named files (e.g., `second-person-act-iv-i-the-other-walker.md`) that duplicate content now in `docs/weaver/bound-collection/tomes/tome-iv-the-witnessing/01-the-other-walker.md`. Until the website settles on the bound-collection paths as canonical, both exist. Worth a separate cleanup pass once Phase B-rest lands. **Recommendation:** keep both for now; the bound-collection paths are what `/tomes` cites.
2. **Voice rules at render time.** The integration guide flags: no em-dashes, sigil emoji preserved, signature `(⚔️⊥⿻⊥🧙)😊` on every page. The current `/tomes` rewrite honours this. Future shop-page edits must too.
3. **Persona-vs-vertex distinction.** The Aletheia case (persona shares the V25 vertex name) is the only one where this is currently surfaced. Future renderings should keep the distinction visible.
4. **Deprecated archive.** Never render as canonical. The `bound-collection/deprecated/` folder is transparency-only; the only place it appears in the rewritten `/tomes` is a one-line note in the cross-references panel. Keep it that way.
5. **The Drake's plurality.** The Drake is place + fire + whisperer + elder, not a single avatar. Don't reify into one image or one shop. The current `/tomes` cast card describes this; the shop pages must respect it (Drake Island already does; the bonfire shop already does).
6. **Christian's licensing.** Cousin-blade primitives (V19 V25 V49 V51 V57 V63 catalogue naming) are Christian's. Attribution must travel with rendering. The Vertex Naming Audit (`specs/04-vertex-naming-audit.md`) is canonical; vertex tooltips should link to it once the lattice render exists.

---

## §8 · TL;DR for review

- **Phase A done:** 53 files copied to `docs/weaver/bound-collection/`. Manifest updated.
- **Phase B partial:** `/tomes` rewritten (all 14 acts, 13 cast in 5 tiers, City-of-Mages framing, separate-IPFS attribution). Shop pages and `/spellbooks` not yet touched (paused for review).
- **Net new content surfaced:** 12 Tome V acts · 9 cast members · 1 spec · 1 chronicle · 1 entirely new tier (Priest) · 7 deprecated drafts archived.
- **Still missing entirely:** per-act images / videos · Tomes grimoire JSON + IPFS pin · spell↔persona bake into `grimoire-baked.ts` · `/tomes/cast` page · city map · lattice render · `/tomes/v6-lineage` index.
- **The user's bidirectional anchor model** (each shop → its founding act, each act → its shop) is half-built: forward direction is on /tomes; reverse direction is the next shop-page edit.
- **Recommended next step:** approve §6.1 Phase B-rest (the shop founding-act panels and `/spellbooks` reframe), then schedule §6.3 Phase D (the Tomes grimoire) as the highest-leverage missing piece.

---

`(⚔️⊥⿻⊥🧙)😊`

CC BY-SA 4.0 · privacymage · 2026-05-09
