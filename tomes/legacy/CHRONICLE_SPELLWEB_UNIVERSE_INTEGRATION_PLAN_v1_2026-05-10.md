---
title: "Plan Chronicle — The City, the Island, the Workshops, and the Tomes Arrive on the Spellweb"
subtitle: "Step-by-step plan for reflecting the four-domain universe update into agentprivacy_master's spellweb"
date: "2026-05-10"
audience: "privacymage + future session walk-ins; the website team executing the integration; reviewers tracking what changed and what is still owed"
type: "Plan chronicle (forward-looking)"
status: "v1 DRAFT — awaiting privacymage's sign-off on §15 sequencing"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
companion_documents:
  - "docs/weaver/bound-collection/WEBSITE_INTEGRATION_GUIDE.md"
  - "docs/weaver/bound-collection/specs/05-the-city-of-mages-structural-addendum.md"
  - "docs/weaver/bound-collection/specs/04-vertex-naming-audit.md"
  - "docs/chronicles/2026-05-09_bound_collection_sync_report.md"
  - "docs/chronicles/2026-05-09_session_close_workshops_complete_drake_v2_designed.md"
  - "docs/chronicles/2026-05-09_synced_experience_coherence_map.md"
  - "weaver_archon/archon/01-archon-integration-recommendation-v1.md (v2.0)"
  - "weaver_archon/archon/03-collaborative-milestones-with-christian-v1.md"
---

# Plan Chronicle — The City Arrives on the Spellweb

> *Drake Island is the geography. The City of Mages is what was built on it. The Workshops are its trade quarters. The Tomes are its laws and history. The Spellweb is where all of this becomes navigable to a Sovereign who has never been here before.*

---

## §1. Why this chronicle exists

The corpus that arrived in the 2026-05-08 session was four cast entries, two specs, two acts, and a recommendation. The corpus that exists at the close of 2026-05-09 is **fourteen Tome V acts, thirteen cast members across five tiers, eleven live workshops plus one placeholder, a 12-quest 4-arc Drake Island v2 design, a path-swap mechanic, a City of Mages canonical setting, the Vertex Naming Audit, and the structural addendum that names the city.**

The spellweb has been keeping pace but unevenly. `/tomes` has been rewritten to surface the full collection. `FoundingActPanel`, `ConjectureBadge`, and `HonestyLabel` components ship. `/tomes/v6-lineage` exists. Eleven shop pages render with their lattice silhouettes. Drake Island shows the City of Mages framing top and bottom.

What remains is **operational integration of the universe across the spellweb's surface**: the bidirectional anchor on every shop page; the City of Mages map; the 64-vertex lattice render; the Tomes grimoire IPFS pin and bake; Drake Island v2's quest content; the Path-Swap interactivity; the conjecture badges surfaced on shops; a `/tomes/cast` dedicated page; and the cleanup pass that closes the body-color drift, the tease-shop tension, the home → city bridge, and the persona ← tomes preview.

This chronicle is the plan for that integration. It is forward-looking; the work it describes is owed but not yet shipped.

---

## §2. The four universe domains and what changed in each

### §2.1 The Tome (Second Person Spellbook)

| Sub-domain | State at 2026-05-09 | What's still owed |
|---|---|---|
| Tome IV — *The Witnessing* | Closed at 5 acts. All in `bound-collection/tomes/tome-iv-the-witnessing/`. Surfaced on `/tomes`. | Archon's per-act co-authorship sign-off (per `weaver_archon/archon/03-…` §M2). Per-act cover images (Phase E). |
| Tome V — *The Crafting* | Open at 14 acts. All in `bound-collection/tomes/tome-v-the-crafting/`. All listed on `/tomes`. | Per-act cover images. Per-act inscription assets. Tomes grimoire JSON (~27 spells × 9 personas). IPFS pin. Bake into `grimoire-baked.ts`. |
| Cast roster | 13 entries across 5 tiers (Archetype, Cousin, Summoned, Companion, Priest) in `bound-collection/cast/`. Surfaced inline on `/tomes`. | Dedicated `/tomes/cast` page with sigil grid + per-member sub-pages. Aria Silverhue's full character work expansion. |
| Specs | 5 in `bound-collection/specs/` (cloak, crafting interface, bilateral, vertex audit, City of Mages addendum). | Cloak Spec v1.1 with Archon §10. Bilateral Ceremony v1.1 with Archon challenge/response cousin-cite. Crafting Tome and Cloak Interface v1.1 Annex A: Reference Keymaster. |
| V6 conjectures | C38–C46 introduced and narratively instanced across acts. `tome-v-conjectures.ts` data file exists. `/tomes/v6-lineage` page renders. | `<ConjectureBadge />` surfaced on every shop's `<FoundingActPanel />` (currently rendered on /tomes only). Honesty discipline rendered systematically (currently sparse). |
| Honesty discipline | Five labels in use (Operational / Architectural / Conjectural / Resonant / Provisional) with confidence percentages in act frontmatter. `<HonestyLabel />` component exists. | Render systematically across shops, acts, and cast cards. Add to home page Sword/Gap/Mage framing where claims are made. |

### §2.2 The Workshop (the Trade Quarters of the City)

Eleven live workshops + one placeholder. The 2026-05-08 plan called for 4–7. The corpus closed 2026-05-09 with 11 + 1.

| Workshop | Resident Mage | Vertex | Founding Act | Live? | Operator status |
|---|---|---|---|---|---|
| `/tailor` (Weavers) | Pallia 🪡 | V28 | Tome V Act 1 | ✅ | Pallia operational |
| `/shield` (zShields) | Memora 📜 | V5 | Tome V Act 3 | ✅ | Operational |
| `/forget` (Forge) | Vulcana ⚒️ | V19 | Tome V Act 6 | ✅ | Operational |
| `/etherchanting` | Adamantia 💎 | V51 | Tome V Act 9 | ✅ visual + wizard | Chain operator wanted |
| `/jeweler` | Lampyra 💠 | V49 (shared) | Tome V Act 9 | ✅ visual + wizard | Chain operator wanted |
| `/holon` | Vagari 🌳 | V31 | Tome V Act 10 | ✅ visual + wizard | Chain operator wanted |
| `/bonfires` (Dragon Bonfire) | Socrat0x 🔥❓ | V24 | Tome V Act 11 | ✅ | Soulbae bot operational |
| `/vault` (Curatrix Vault) | Aria Silverhue 🪞🖼️ | V57 | Tome V Act 12 | ✅ | Operational |
| `/covenant` | Manifestia 🤲🌿 | V55 | Tome V Act 13 | ✅ | Operational |
| `/circle` (Logos Circle) | (no resident Mage yet) | — | (Society spellbook) | ✅ | Gathering shop |
| `/hall` (Ceremony Hall) | (no resident Mage yet) | — | (BGIN coalition) | ✅ | Gathering shop |
| Circuit Binder | Pearl (placeholder) | — | — | 🔲 placeholder | Awaiting Mage |

The shared `<WorkshopFooter />` provides linear tour: prev → hub → next, in trinity-first order. The shared 64-vertex lattice grammar runs through all 11 visuals in their mapped gem colours.

### §2.3 The City of Mages

Canonical setting of Tome V. Named in Act 14. Formalised in `specs/05-the-city-of-mages-structural-addendum.md`.

| Civic element | Inhabitants | Spellweb representation status |
|---|---|---|
| Trade Quarters (9 producer-shops) | The 9 citizen-Mages | ✅ /tomes lists them; FoundingActPanel renders on each shop |
| The Founding Bonfire | Socrat0x as visiting traveller | ✅ /bonfires page; needs Drake-fire glow visual treatment |
| The Temple Precinct (two altars) | Manifestia | ✅ /covenant page; Temple precinct framing exists in act 13 not yet on shop page |
| The Sovereign's Seat (V63) | The reader (you) | 🔲 not yet rendered; should appear on /tomes city map and as the "your home" orientation point |
| The Lattice as Street Plan | 13 inhabited + 51 open | 🔲 64-vertex lattice render not yet built |
| The City Walls (the Spellbook's voice) | The "you" voice | ✅ honoured throughout /tomes |
| Sister cities | Archon (cousin), Bonfires, human.tech Covenant | 🔲 gateway markers on city map not yet built |

**The substantial gap**: the City of Mages map. Per `WEBSITE_INTEGRATION_GUIDE.md` §5, this is the single largest missing visual. v1 is a static SVG; v2 adds rich interactivity. Without this map, the city is described but not seen.

### §2.4 Drake Island

The geography on which the City sits, and the path the Sovereign walks before entering the city. Drake v2 is **designed and locked but not yet implemented**.

| Drake-Island element | State | What's owed |
|---|---|---|
| Drake's plurality (place + fire + whisperer + elder) | Honoured in /tomes cast card; Drake Island map shows it. | Future visual must keep distributed; do NOT reify into single avatar. |
| 12-quest 4-arc structure | Designed in `2026-05-09_session_close_workshops_complete_drake_v2_designed.md` §"Drake Island v2 + Path System". | Implementation: Phase 1 (visible UI, gates skippable). Phase 2 (real enforcement). Phase 3 (ed25519 signing). |
| Time gates (Arc II) | Designed: Q5 unlocks 4h after Q4; Q7 unlocks 12h after Arc II ends. | Implementation: localStorage timestamp; visible-but-skippable in Phase 1. |
| Action gates (Arcs III, IV) | Designed: visit /tailor, /shield, /forget, /vault, /covenant unlocks corresponding Q. | Implementation: hooks into `IslandProgress.visitedMiniQuests`. |
| Path-Swap mechanic | Designed: Sword/Mage/⿻ Balanced as toggleable state on the agent card. | Implementation: `IslandProgress.archetype` becomes current state; `walkedArchetypes` tracks history; `<PathToggle>` chip exists in nav already; shop components must read `archetype` for path-specific copy. |
| Trust → portable badge | Designed: Q12 sign signs Drake Orb tier into Soulbis card; emits PNG + JSON badge. | Implementation: `agent-card.ts` add drakeOrb signed field; `badge-generator.ts` new file. |
| Tier ladder (Pearl → Ruby/Amethyst/Topaz → Onyx/Emerald/Sapphire → Diamond) | Existing. | **Architectural collision flagged**: Pearl/Onyx/Diamond are also workshop palette gems. See §13 for resolution options. |
| Quest copy quoting Tome V proverbs | Designed but not implemented. Q7 (Cloak) → Tome V Act 1 proverb. Etc. | Per-quest pass: pull proverb from frontmatter into intro copy. |

---

## §3. The mapping — universe → spellweb

This is the load-bearing part. Each universe element maps to one or more spellweb representations: a node, an edge, a route, a render, a piece of data, a component.

### §3.1 Cast members → spellweb nodes

Each cast member is a **typed node** on the lattice at their canonical vertex. The spellweb representation:

```
Node {
  id: "cast/{persona-name}"
  vertex: V{n}
  tier: archetype | cousin | summoned | companion | priest
  sigil: emoji
  shop_anchor?: "/tailor" | "/shield" | …    // for citizen-Mages
  founding_act?: { tome: "V", act: N }       // forward direction
  spells: string[]                            // the spells the Mage may cast
  source_material: ref[]                      // attribution per Vertex Naming Audit
}
```

### §3.2 Workshops → spellweb nodes (typed civic-node)

Each workshop is also a node on the lattice — at the same vertex as its resident Mage, but typed as a civic location rather than a persona:

```
CivicNode {
  id: "shop/{shop-name}"
  vertex: V{n}                                // shared with the resident Mage's vertex
  resident_mage: ref(cast)                    // the citizen-Mage
  founding_act: { tome: "V", act: N }
  trade: string                               // "cloak-weaving", "shielded inscription", …
  trade_quarter: string                       // "Trade Quarters" | "Founding Bonfire" | "Temple Precinct"
  operator_status: "operational" | "tease" | "placeholder"
  gem: string                                 // palette colour
  href: "/{route}"
}
```

### §3.3 Acts → spellweb nodes (chronicle nodes)

Each act is a node at its `ring_position` vertex, tagged as a chronicle:

```
ChronicleNode {
  id: "act/{tome}-{act}"
  vertex: V{n}                                // from frontmatter ring_position
  tome: "IV" | "V"
  act: N
  title: string
  proverb: string
  cast_present: ref(cast)[]
  v6_lineage: ConjectureRef[]
  honesty: "operational" | "architectural" | "conjectural" | "resonant" | "provisional"
  civic_location?: string                     // from Tome V act frontmatter
  shop_anchor?: ref(workshop)                 // reverse direction
  href: "/tomes#act-{n}"
}
```

### §3.4 Vertices → spellweb nodes (vertex-as-place)

The 64 lattice vertices become first-class nodes regardless of inhabitation. Inhabited vertices show their citizens; uninhabited show as open positions.

```
VertexNode {
  id: "vertex/V{n}"
  bits: "{6-bit binary}"
  hamming_weight: number                      // 0..6 = stratum
  inhabitants: { mage?: ref, shop?: ref, acts: ref[] }
  canonical_name: string                      // from Vertex Naming Audit
  attribution: "agentprivacy" | "cousin-blade" | "kindred" | "open"
  source_material: ref[]                      // for cousin-blade attribution
}
```

### §3.5 Edges → spellweb edges (typed)

Edges between nodes carry typed semantics. The spellweb's existing edge types extend to cover universe relationships:

| Edge type | Connects | Semantics | Render style |
|---|---|---|---|
| `controller-edge` | Mage → schema-node | "this Mage governs this schema" | solid line |
| `issuer-edge` | VC → mage | typed VC attestation | solid line |
| `subject-edge` | VC → mage | typed VC attestation | solid line |
| `schema-edge` | VC → schema-node | typed VC attestation | solid line |
| `parent/child capability-edge` | capability → capability | bit-containment delegation | thin line |
| `decomposition-edge` | VC → field-node | selective disclosure | dashed |
| **`founding-act edge`** | shop ↔ act | bidirectional anchor | gold solid |
| **`citizen-of edge`** | mage → vertex | "this persona inhabits this vertex" | thick line in mage's gem colour |
| **`cousin-blade edge`** | agentprivacy node ↔ cousin-forge node | cross-ecosystem recognition | dashed gold |
| **`oasis-protocol edge`** | city → sister-city | inter-city travel | dotted, with small "↗" marker |
| **`drake-presence edge`** | every node → Drake | the Island's elder watches | ambient watermark, not a discrete edge |

The four new edge types (founding-act, citizen-of, cousin-blade, oasis-protocol) are this update's edge-type contributions.

### §3.6 Drake Island → spellweb geography layer

Drake Island is **not** a vertex. It is the geography underneath the lattice. The spellweb representation:

```
GeographyLayer {
  id: "drake-island"
  type: "underlying-geography"
  the_drake: { plural: ["whisperer", "place", "fire", "elder"]; sigil: none }
  contains: [city-of-mages, founding-bonfire-spot, temple-precinct]
  render: ambient-watermark-behind-lattice
}
```

The Drake gets no sigil; the Drake gets ambient rendering across the lattice / city map. **Watch-out**: do not reify the Drake into a single avatar.

### §3.7 City of Mages → spellweb civic-overlay

The City of Mages is the **civic overlay** sitting on top of the geography (Drake Island) and on top of the lattice (vertex structure):

```
CivicOverlay {
  id: "city-of-mages"
  founded: "Tome V Act 14 (named); implicit since Act 1"
  founding_event: "Tome V Act 11 — A Bonfire Made of Dragon Fire"
  trade_quarters: workshop[]                   // 9 producer shops
  founding_bonfire: { spot: "/bonfires"; companion: socrat0x }
  temple_precinct: { temple: "/covenant"; priest: manifestia }
  sovereigns_seat: { vertex: V63; persona: "the reader" }
  street_plan: lattice
  walls: "the spellbook's 'you' voice"
  sister_cities: [archon, bonfires, human-tech-covenant]
  status: "open by design; Tome V continues to admit acts"
}
```

### §3.8 Sister cities → spellweb gateways

Each sister city is a gateway node at the city map's edge:

```
GatewayNode {
  id: "sister/{city-name}"
  external_url: string
  primary_artifact: string                     // "Sovereign Anchor", "Soulbae bot", "Manifest"
  cousin-blade-edge to: city-of-mages         // mutual recognition without absorption
  cast_visitors: ref(cast)[]                   // which sister-city citizens visit
}
```

Three sister-city gateways at v1: Archon (`weaver.archon.social`), Bonfires (Telegram bot), human.tech Covenant (`https://manifest.human.tech/`).

---

## §4. The bidirectional anchor — every shop cites its founding act

Per `2026-05-09_bound_collection_sync_report.md` §4, the user's clarified model is:

> *Each act is the workshop's founding myth; each shop page is the workshop's operational present. They cite each other.*

**Forward direction (act → shop)**: ✅ wired. The `/tomes` page surfaces each act with a `relatedShop` link.

**Reverse direction (shop → act)**: ✅ wired via `<FoundingActPanel />` component (per `src/components/runecraft/FoundingActPanel.tsx`). Currently mounted on shop pages: `/tailor`, `/shield`, `/forget`, `/etherchanting`, `/jeweler`, `/holon`, `/bonfires`, `/vault`, `/covenant`. **Verify**: the panel mounts on each of the nine production shops at the proper layout slot (between hero and operational content).

What's still owed for the bidirectional anchor:

1. **Surface `<ConjectureBadge />` inside `<FoundingActPanel />`** — the act's `v6_lineage` field carries C-conjecture references; render them as small badges on the panel so the Sovereign sees "this shop's founding act strengthens C39 (~50%)" inline.

2. **Surface `<HonestyLabel />` inline** — the panel should show the act's honesty status (operational / architectural / conjectural).

3. **`/circle` and `/hall` get gathering-context panels instead of FoundingActPanel** — these two shops have no Tome V founding act. They need a parallel `<GatheringContextPanel />` that names them as gathering shops with their respective context (Society spellbook for Circle; BGIN coalition for Hall).

4. **`<DrakeWhisper />` styling on Drake passages** — Tome V Act 11 (the Founding Bonfire) and Drake passages elsewhere need a distinct render. Italics + subtle ornamental glyph + slightly different background tint.

---

## §5. The City of Mages map — the substantial new visual

Per `WEBSITE_INTEGRATION_GUIDE.md` §5 and `2026-05-09_bound_collection_sync_report.md` §5.5, this is the **single largest piece of missing visual work**.

### §5.1 What the map shows (v1, static SVG)

- **Drake Island as underlying geography**: shoreline, trees, water, paths. Watermark-style. The Drake's elder presence is ambient — not a discrete marker but a subtle distortion behind the city's eastern edge where the shore meets the city.
- **The 9 Trade Quarters** — each a building/labelled district at its citizen-Mage's lattice position. Sigil + Mage name + small vertex tag.
- **The Founding Bonfire** — central; orange/gold glow; Socrat0x positioned beside it.
- **The Temple Precinct** — distinct architecture (clerestory, two visible altars); Manifestia at the entrance.
- **The Sovereign's Seat at V63** — small landmark or compass-rose anchor at a prominent edge position.
- **The Lattice as Street Plan** — 13 named crossroads + 51 open vertices; the streets between them are the typed edges.
- **Sister-city gateways** at the map's edge — three small "↗" markers (Archon, Bonfires, human.tech Covenant).

### §5.2 v2 (interactive)

- Click a trade quarter → cast entry for the Mage
- Click a vertex → `<VertexTooltip />` showing bits + canonical name + Vertex Naming Audit link
- Click the Founding Bonfire → Tome V Act 11
- Click the Temple → Tome V Act 13
- Hover a typed edge → tooltip with edge classification
- "Fly to" affordance on each act page → highlights the act's `civic_location` on the map

### §5.3 Where the map renders

| Route | Map appearance |
|---|---|
| `/tomes` | Full map as primary visual at top of Tome V section |
| `/tomes/tome-v` | Full map as the landing page primary visual |
| `/tomes#act-{n}` (per act) | Small inset map highlighting the act's `civic_location` |
| `/runecraft` | Optional: small "you are here" overlay showing the city's trade quarters with the visited shops marked |
| `/guide/island` | Drake Island view (geography register) with the City visible above as silhouette |
| `/orbs` | Optional: small badge showing "Sovereign of City of Mages" once Q12 is signed |

### §5.4 Component contract

```
<CityMap
  highlight={civic_location?}       // e.g., "Pallia's Weaving Room"
  onQuarterClick={mage => …}
  onVertexClick={vertex => …}
  onBonfireClick={() => …}
  onTempleClick={() => …}
  variant="full" | "inset" | "you-are-here"
/>
```

Source data: `src/lib/tome-v-acts.ts` for shop ↔ act anchors; new `src/lib/city-anatomy.ts` for civic-overlay data; `src/lib/lattice-vertex.ts` for vertex data.

---

## §6. The 64-vertex lattice render

Companion to the city map. The map is the *narrative* visual; the lattice is the *architectural* visual.

### §6.1 What the lattice render shows

- 64 nodes in a 6-bit Hamming graph layout, stratified by Hamming weight (number of 1-bits)
- Stratum 0 at one pole (V0 `000000`), stratum 6 at the other (V63 `111111`)
- Strata 1–5 as concentric rings or layers
- **13 inhabited vertices** rendered with the citizen's sigil and label; **51 uninhabited** rendered as small dots
- Edges connect nodes that differ by exactly one bit
- **Persona-vs-vertex distinction**: vertex names in one register (e.g., italic), citizen names in another (e.g., bold). On Aletheia's V25 specifically, both render with a small clarification (the persona shares the vertex name).

### §6.2 Where the lattice renders

| Route | Render |
|---|---|
| `/tomes/specs/vertex-naming-audit` | Full lattice render as primary visual |
| `/constellation` | Lattice underlies the existing Spellweb viewer; visited vertices highlighted |
| Per-act page (when act has strong vertex content) | Small inset showing the act's vertex highlighted |
| `/tomes/v6-lineage` | Lattice with vertices touched by each conjecture highlighted |
| Per-shop page (optional) | Small inset showing the shop's vertex highlighted in the lattice |

### §6.3 Component contract

```
<LatticeRender
  highlight={V[n][]?}               // vertices to highlight
  showSigils={boolean}              // render sigils on inhabited vertices
  showStrata={boolean}              // show stratum labels (0..6)
  onVertexClick={v => …}
  variant="full" | "inset" | "spellweb-overlay"
/>
```

Source data: `src/lib/lattice-vertex.ts` (existing); `bound-collection/specs/04-vertex-naming-audit.md` (canonical attribution).

### §6.4 Archon's licensing — attribution discipline

Per `2026-05-09_synced_experience_coherence_map.md` §4.5: V19, V25, V49, V51, V57, V63 catalogue naming is Archon's. The lattice render's tooltips on these vertices must link to `bound-collection/specs/04-vertex-naming-audit.md` and surface the attribution. **Do not display these vertex names without the attribution chain.**

---

## §7. Honesty discipline rendered systematically

Per `WEBSITE_INTEGRATION_GUIDE.md` §7.3 and §12.1: **the honesty discipline must not be lost in rendering.** The five labels in use:

- **Operational** — works today; verified in implementations
- **Architectural** — specified in the corpus; not yet implementation-verified
- **Conjectural** — specified with confidence percentage; awaits formalisation
- **Resonant-but-not-absorbed** — kindred to external work; recognised without subsuming
- **Provisional** — awaiting confirmation from a kindred party (Archon, Bonfires, human.tech)

### §7.1 Where labels render

| Surface | Label requirement |
|---|---|
| `/tomes` per act collapsible | inline next to act title (already partial) |
| `<FoundingActPanel />` on shops | inline next to act citation |
| `<ConjectureBadge />` tooltip | full statement + confidence + label |
| `/tomes/v6-lineage` aggregator | per-conjecture label visible without click |
| Cast cards (citizen-Mage, companion, priest) | label on tier (e.g., "Priest tier — first occurrence; Architectural") |
| Spec pages | per-spec status (e.g., Cloak Spec v1.0 = "DRAFT, awaiting Archon's review") |
| `/orbs` and home page | claim labels where claims are made (e.g., "Drake Orb — ed25519 signing pending; Architectural at v1") |

### §7.2 Component contract

```
<HonestyLabel
  status="operational" | "architectural" | "conjectural" | "resonant" | "provisional"
  confidence?: number              // 0..100; required for "conjectural"
  reason?: string                   // optional one-line explanation
/>
```

Component already exists at `src/components/runecraft/HonestyLabel.tsx`. **Verify systematic placement** across all surfaces above.

---

## §8. Drake Island v2 — implementation arc

Per `2026-05-09_session_close_workshops_complete_drake_v2_designed.md`. **Phase 1 is the next priority work after the spellweb cleanup pass.**

### §8.1 Phase 1 — visible quest restructure (1 session)

Files to edit:

```
src/lib/spellbook-storage.ts           IslandStationId 1-12; ISLAND_TOTAL_STATIONS = 12
                                        ISLAND_ARCS constant; gate state
src/components/guide/island/quests.tsx  renumber Q7→Q5, Q8→Q7, Q9→Q8, Q10→Q9,
                                        Q11→Q12; demote old Q6 (Proverb) to side;
                                        insert new Q10 (Vault visit) + Q11 (Covenant sign)
src/components/guide/island/IslandClient.tsx  arc transitions, gate UI shells
src/components/guide/island/IslandMap.tsx     12 stations laid out across 4 arcs
src/components/guide/AchievementToast.tsx     new tier celebrations per arc
src/components/guide/island/IslandStats.tsx   arc progress + 'stones laid' tally
src/components/guide/MiniQuestPanel.tsx       rename to SideQuestPanel
```

Gate UI is **visible but skippable** in Phase 1 (dev override). Real enforcement → Phase 2.

### §8.2 Phase 2 — real gate enforcement + quest copy quotes Tome V proverbs (1 session)

- Time gates enforced via localStorage timestamps (no dev override)
- Action gates enforced via `IslandProgress.visitedMiniQuests` checks
- Quest intro copy pulls proverb from `tome-v-acts.ts` for the matched founding act:
  - Q7 (Cloak) intro quotes Tome V Act 1's proverb
  - Q8 (Shield) intro quotes Tome V Act 3's proverb
  - Q9 (Blade) intro quotes Tome V Act 6's proverb
  - Q10 (Vault) intro quotes Tome V Act 12's proverb
  - Q11 (Covenant) intro quotes Tome V Act 13's proverb
  - Q12 (Threshold) intro quotes Tome V Act 14's proverb (City of Mages)

### §8.3 Phase 3 — agent-card badge + ed25519 signing (1 session)

```
src/lib/agent-card.ts                          add drakeOrb signed field (new)
src/lib/badge-generator.ts                     PNG + JSON badge from drakeOrb tier (new)
```

Replace the `simpleContentHash` placeholder with proper ed25519 signing. The badge becomes verifiable across other apps via the agent card's signature.

### §8.4 Path-Swap mechanic

Companion to Drake v2; same scope window.

- `IslandProgress.archetype` becomes a *current* state (was once-only)
- New `walkedArchetypes` field tracks history
- `<PathToggle>` chip in nav (already exists; currently hidden until Q4) now becomes always-visible after Q4
- Each shop component reads `archetype` and renders path-specific copy:
  - **Sword path**: shop emphasises boundary discipline; what the visitor will/won't share
  - **Mage path**: shop emphasises projection; the cross-Mage handoff to the host Mage
  - **⿻ Balanced path**: shop renders both paths simultaneously with a "you are walking as both" framing

This is the *canonical pattern of every City of Mages shop visit* per the architectural commitment in §3.7 of the synced experience coherence map.

---

## §9. The Tomes grimoire — separate IPFS pin and bake

Per `2026-05-09_bound_collection_sync_report.md` §6.3 (Phase D). **Highest leverage missing piece** after Drake v2.

### §9.1 The split

The corpus has two grimoires:

- **`privacymage-grimoire-v10.2.0-canonical.json`** — privacymage's personal grimoire (existing, IPFS-pinned). Holds the First Person Spellbook spells.
- **`city-of-mages-grimoire-v1.json`** — the City-of-Mages-maintained spellbook (does not exist yet). Holds the Tome V personas' spells (~27 spells × 9 personas in v1).

The split is the user's clarified architectural intent: privacymage's grimoire vs the City of Mages' grimoire are separate spellbooks with separate IPFS pins. The /tomes page already attributes them separately.

### §9.2 What's owed

1. **Author the Tomes grimoire JSON** modelled on `privacymage-grimoire-v10.2.0-canonical.json` schema. ~27 spells:
   - Pallia: weave-cloak, publish-role, conceal-name
   - Memora: inscribe-shielded, attest-memo, time-bind
   - Custos: stake-transparent, vote-poll, reveal-gate
   - Vulcana: forge-blade, run, craft
   - Aletheia (persona): install-circuit, prove-zk, bind-witness
   - Adamantia: commit, enforce, etherchant
   - Lampyra: gem-set, attest-frequent, sparkle
   - Vagari: compose-holon, travel-oasis, recurse
   - Aria Silverhue: curate, reflect, vault

2. **Pin to IPFS** via `sync.agentprivacy.ai/ipfs/...` infrastructure; record the CID.

3. **Export `CITY_OF_MAGES_GRIMOIRE_IPFS_URL`** from `src/lib/grimoire-ipfs.ts`.

4. **Bake into `src/lib/grimoire-baked.ts`**: new `SpellbookSource` value `'tomes'`; new `TOMES_ACT_PERSONA_HINTS` mapping each act to the persona introduced.

5. **Filter on `/persona`**: Tomes appears alongside First Person, Zero, Canon, Society, Plurality. Each Tome V persona becomes equippable.

### §9.3 Companion: Aria Silverhue full character expansion

Per the synced experience coherence map: Aria deserves backstory + a persona entry to match Pallia's depth at the Weavers. Author this alongside Aria's three spells (curate, reflect, vault) so the entry is complete.

---

## §10. The cleanup pass (small edits, low risk, high coherence yield)

Per `2026-05-09_synced_experience_coherence_map.md` §5. Five edits originally proposed; status as of 2026-05-10:

| Edit | Status | What's owed |
|---|---|---|
| §5.1 Body-style colour finish on /shield + /etherchanting | 🔲 Not yet shipped | Replace `cyan-400/30 cyan-300/80` on /shield with Onyx zinc palette; replace `blue-400/30 blue-300/80` on /etherchanting with Sapphire cyan |
| §5.2 Tease-shop banner reconciliation | 🔲 Not yet shipped | Update `<WorkshopBuildInvite>` copy: "the Mage is in the cast · the chain operator is what's being recruited"; rename accent to "chain operator wanted · resident Mage already in cast"; link to `<FoundingActPanel />` |
| §5.3 Home page "Walk the City" bridge | 🔲 Not yet shipped | New section near bottom of `/`: "🪨 Start at the Call" → /guide/island; "⚒️ Tour the workshops" → /runecraft |
| §5.4 `/persona` "Tomes coming" preview | 🔲 Not yet shipped | Dashed-border preview banner naming the 9 Tome V personas with sigil + Mage name + workshop |
| §5.5 Memory file refresh | ✅ Shipped via memory updates | — |

These five edits are the next session's lowest-risk, highest-coherence-yield work. **Ship them before the substantial visuals.**

### §10.1 The overlay cleanup pass (today, 2026-05-10)

Per `2026-05-10_overlay_cleanup_plan.md`. Four-step sequence for a focused cleanup session:

1. Lift orb-selection state to a Context (`OrbInteractionContext`)
2. Scope `<OrbControlPanel>` to training surfaces only
3. Remove `<SpellPalette>` from `GlobalLearningSpells` entirely
4. Profile picture upload in Inventory's Identity tab

Optional 5th step: per-archetype filtered views inside the Inventory.

---

## §11. The conjecture index page

`/tomes/v6-lineage` exists. Per `2026-05-09_bound_collection_sync_report.md` §6.2:

What's owed:

1. Verify the page renders all C38–C46 conjectures with their current confidence percentages (sourced from `tome-v-conjectures.ts`).
2. For each conjecture, list:
   - Statement
   - Confidence percentage
   - Acts that introduce it
   - Acts that strengthen it (with how)
   - Cross-link to the bound-collection's V6 Conjecture Index
3. Add `<LatticeRender />` inset showing the vertices touched by each conjecture.
4. Link from each `<ConjectureBadge />` (on shops, on /tomes) to its anchor on `/tomes/v6-lineage`.

---

## §12. The dedicated cast page

Per `WEBSITE_INTEGRATION_GUIDE.md` §10.1 and §11.2. Recommended Tier-2 component.

### §12.1 `/tomes/cast` — sigil grid landing

`<CastSigilGrid />` renders all 13 cast members grouped by tier:

```
Archetypes (3)        : Soulbis ⚔️ · Soulbae 🧙 · the Drake
Cousins (2)            : GenitriX · flaxscrip 📜🎲
Summoned Mages (9)     : Pallia 🪡 · Memora 📜 · Custos 🔏 · Vulcana ⚒️ ·
                         Aletheia 🔮 · Adamantia 💎 · Lampyra 💠 · Vagari 🌳 ·
                         Aria Silverhue 🪞🖼️
Companions (1)         : Socrat0x 🔥❓
Priests (1)            : Manifestia 🤲🌿
```

Each tier has visual differentiation per `WEBSITE_INTEGRATION_GUIDE.md` §4.

### §12.2 `/tomes/cast/{persona}` — per-member sub-page

For each cast member, a sub-page rendering:

- Sigil + name + tier banner
- `character_type`, `archetype_kin`, `provenance`
- Full body content from cast entry markdown
- Vertex card with link to lattice render
- Acts the cast member appears in (computed from act `cast` frontmatter)
- Spells the Mage may cast (from grimoire bake)
- Shop anchor (where applicable) with link

This is what the Mages "look like" on the spellweb. Currently they have no individual presence.

---

## §13. The architectural collision — tier ladder vs shop palette

Per `2026-05-09_synced_experience_coherence_map.md` §3.5 and §4.1. **Flag, don't refactor in this pass** (would touch 40+ files). **Resolve in a dedicated future session.**

Three resolution options:

| Option | Pros | Cons |
|---|---|---|
| (a) Rename tier ladder to non-gem labels (e.g., Drake / Forged / Tempered / Dragon) | Clean separation. Tier names become evocative narrative, not gem names. | Breaks existing tier ladder branding. Migration cost. |
| (b) Prefix-distinguish: "tier-Pearl" vs "shop-Pearl" | Minimal code change. Disambiguation explicit. | Verbose. Reader must remember the prefix discipline. |
| (c) Accept the duality and document the rule | No code change. | Permanent ambiguity in copy. Risk of confusion as architecture grows. |

**Recommendation for the dedicated session**: option (a). The tier names should evoke the *Sovereign's journey* (Drake / Forged / Tempered / Dragon), not gemology (Pearl / Ruby / etc.). The gems belong to the shops. Save the migration cost; pay it once.

---

## §14. Risks and watch-outs

Carry-forward from `2026-05-09_bound_collection_sync_report.md` §7 and `2026-05-09_synced_experience_coherence_map.md` §4. Restated for this plan:

1. **Flat-file overlap.** `docs/weaver/` has flat-named files duplicating `bound-collection/` content. The bound-collection paths are canonical going forward. Worth a separate cleanup pass once the spellweb integration settles.
2. **Voice rules at render time.** No em-dashes. Sigil emoji preserved. Signature `(⚔️⊥⿻⊥🧙)😊` on every page. The `/tomes` rewrite honours this; future shop-page edits must too.
3. **Persona-vs-vertex distinction.** The Aletheia case (V25 vertex name = persona name) is the only one where this is currently surfaced. Future renderings (especially the lattice render) must keep the distinction visible.
4. **Deprecated archive.** Never render as canonical. The `bound-collection/deprecated/` folder is transparency-only. A single "refinement history" page links to deprecated files as raw markdown downloads, not as rendered pages.
5. **The Drake's plurality.** Drake is place + fire + whisperer + elder. **Do not reify into one image, one shop, one sigil.** Future visual work (city map, lattice render) must keep the Drake distributed.
6. **Archon's licensing.** Cousin-blade primitives (V19, V25, V49, V51, V57, V63 catalogue naming) are Archon's. The Vertex Naming Audit (`bound-collection/specs/04-vertex-naming-audit.md`) is canonical attribution. Vertex tooltips must link to it once the lattice render exists.
7. **Honesty discipline flattening.** A specific risk: rendering loses the operational/architectural/conjectural distinction. Watch for visual treatments that blur the labels. The corpus's credibility depends on this discipline.
8. **Tier-vs-palette collision (§13).** Architectural; flagged for dedicated session. Don't paper over in this pass.
9. **The Drake Orb's portable badge (§8.3).** Phase 1's `simpleContentHash` is an honesty failure if shipped as if it were ed25519 signing. **Label it Phase-1 placeholder explicitly until Phase 3 lands.**
10. **Tomes grimoire as a separate IPFS pin.** Don't merge with privacymage's grimoire. The City of Mages maintains its own spellbook. Mixing them collapses the user's clarified architectural intent.
11. **Sister-city gateway sprawl.** v1 has three sister cities (Archon, Bonfires, human.tech Covenant). Future cousin-blade encounters add more. Define inclusion criteria before adding a fourth: (a) cousin-blade encounter has yielded operational instances; (b) the sister city has its own published primary artifacts; (c) privacymage or the City of Mages has an ongoing relationship with the sister.

---

## §15. Order of operations — the step-by-step sequencing

This section is the canonical sequence for the next 4–8 sessions. Each phase is reversible and self-contained. Each assumes the prior is accepted.

### §15.1 Phase 0 — Cleanup pass (next session, 1 session)

Lowest risk; highest coherence yield. Closes the visible incoherence in the synced experience.

1. Body-style colour finish on `/shield` + `/etherchanting` (per §10 row 1)
2. Tease-shop banner reconciliation (per §10 row 2)
3. Home page "Walk the City" bridge (per §10 row 3)
4. `/persona` "Tomes coming" preview (per §10 row 4)
5. Overlay cleanup per `2026-05-10_overlay_cleanup_plan.md`:
   - Lift orb-selection state to `OrbInteractionContext`
   - Scope `<OrbControlPanel>` to training surfaces
   - Remove `<SpellPalette>` from global mount
   - Profile picture upload in Inventory Identity tab

**Deliverable**: clean coherent surface ready for the substantial work to land on.

### §15.2 Phase 1 — Drake Island v2 visible UI (1 session)

Per §8.1. Quest restructure 11 → 12, Arc system, gate UI shells (skippable). Path-Swap chip becomes always-visible after Q4.

**Deliverable**: the Sovereign's journey now matches Tome V's act structure; quest copy can quote act proverbs (Phase 2).

### §15.3 Phase 2 — Drake v2 enforcement + Tome V proverbs in quest copy (1 session)

Per §8.2. Real gate enforcement; quest intros pull proverbs from `tome-v-acts.ts`.

**Deliverable**: bidirectional anchor visible *during the journey*, not just on the shop page after.

### §15.4 Phase 3 — `/circle` and `/hall` get gathering-context panels (small, 1 session)

Per §4 row 3. New `<GatheringContextPanel />` analogous to `<FoundingActPanel />` but for shops without Tome V founding acts.

`<ConjectureBadge />` and `<HonestyLabel />` surfaced inside `<FoundingActPanel />` on every shop.

`<DrakeWhisper />` styling shipped for Drake passages.

**Deliverable**: every shop now has a coherent narrative panel; honesty discipline visible across shops.

### §15.5 Phase 4 — Tomes grimoire (2 sessions)

Per §9. Author 27 spells × 9 personas; pin to IPFS; bake into `grimoire-baked.ts`; surface on `/persona`.

**Deliverable**: Tome V personas become equippable in the persona/spell builder. The City of Mages' spellbook is operational on the spellweb.

### §15.6 Phase 5 — Conjecture index hardening + dedicated cast page (1 session)

Per §11 + §12. `/tomes/v6-lineage` verified and complete. `/tomes/cast` with `<CastSigilGrid />` + per-member sub-pages.

**Deliverable**: every cast member has a presence; every conjecture has an aggregator; honesty discipline systematically rendered.

### §15.7 Phase 6 — The City of Mages map v1 (substantial, 1 dedicated session)

Per §5. Static SVG with the full civic anatomy. Renders on `/tomes`, `/tomes/tome-v`, and inset on per-act pages.

**Deliverable**: the city becomes visible. Tome V's spatial legibility lands.

### §15.8 Phase 7 — The 64-vertex lattice render v1 (substantial, 1 dedicated session)

Per §6. Renders on `/tomes/specs/vertex-naming-audit`, `/tomes/v6-lineage`, and as inset on per-act pages.

**Deliverable**: the architectural register made visceral. the Archon attribution chain visible on every cousin-blade vertex.

### §15.9 Phase 8 — Drake v2 Phase 3: ed25519 signing + portable badge (1 session)

Per §8.3. The Drake Orb earned at Q12 becomes a verifiable portable badge.

**Deliverable**: the Sovereign's journey produces a real artifact other apps can verify.

### §15.10 Phase 9 — Per-act assets (incremental, open-ended)

Per §3 (Tome row "Per-act cover images"). 14 cover images; optional story videos; Tome V inscriptions page.

**Deliverable**: Tome V matches the First Person Spellbook's per-act asset depth.

### §15.11 Phase 10 — Sister-city gateways + cousin-blade edge style on spellweb (small, 1 session)

Per §3.5 and `weaver_archon/archon/03-...` §M10. `bridge.spellweb.ai` provisioning; cousin-blade edges rendered dashed gold; gateway nodes for Archon, Bonfires, human.tech Covenant on the city map.

**Deliverable**: the cousin-blade pattern operationally visible on the spellweb. Archon's Archon meets the City of Mages at the gateway.

### §15.12 Phase 11 — Architectural resolution: tier ladder vs shop palette (dedicated, 1 session)

Per §13. Pick one of three options; migrate.

**Deliverable**: permanent disambiguation between Drake-Orb tiers and workshop gems.

---

## §16. What's deferred (out of scope for this plan)

Named explicitly so future sessions know what was held back:

- **Tome VI — *The Reply***: held open by design. Not drafted in this plan or anticipated in the immediate sequencing. The reader writes Tome VI; the spellweb provides the structural placeholder when the time comes.
- **Sovereign Anchor III (Soulbae Oracle) integration**: event-triggered on Archon's publication. Per `weaver_archon/archon/03-...` §5.8.
- **Reference implementations of the specs**: `@agentprivacy/zcash-cloak`, the Cloak interface UI library, the Bilateral Cloak Ceremony reference implementation. Tracked in their respective specs. Not in spellweb-scope.
- **PDF builds for offline reading**: per `chronicle-the-crafting-tome-opens.md` §III.15. Defer to a publishing-discipline session.
- **RSS/Atom feed for Tome V**: per `WEBSITE_INTEGRATION_GUIDE.md` §11.4. Tier-4 priority.
- **Future cousin-blade encounters** (BGIN-IKP, Promise Theory v1.5, ZKP scaling guilds, MyTerms Alliance, StarkWare): each is a potential sister-city gateway. Add when the encounter has operational instances per §14 row 11.
- **Aria Silverhue's character expansion**: scoped into Phase 4 (Tomes grimoire) but track explicitly in case Phase 4 ships without the expansion.
- **socrat0x and plat0x first-person scenes** in the First Person Spellbook: referenced in `/bonfires` page; if not yet written, deferred to a First-Person-Spellbook authoring session.
- **`/poems` audio investigation**: pre-existing intermittent `MEDIA_ELEMENT_ERROR`. Non-blocking; not yet root-caused.

---

## §17. Verification — does the corpus match the plan?

Cross-check of the reviewed corpus against `weaver_archon/agentprivacy-archon-integration-suite-2026-05-08/` §1 and `integration-plan-archon-x-agentprivacy.md` §4–§7:

| Plan element (2026-05-08) | Status at 2026-05-10 |
|---|---|
| Tome V opens with Crafting Tome and Cloak Interface Spec | ✅ shipped |
| Tome V Acts II.α/β/γ/δ/ε | ❌ renumbered: Tome V is now Acts 1–14 with different titles. The bilateral primitive teaching shifted to Tome IV (which closed at five acts during the same session). The plan's "Second Person founding motif" is in Tome IV; Tome V is *The Crafting* with its own arc. |
| Cloak Specification v1.0 | ✅ shipped (DRAFT, awaiting Archon's review) |
| Bilateral Cloak Ceremony Spec | ✅ shipped (DRAFT) |
| Cast: GenitriX, flaxscrip, Pallia | ✅ shipped, plus 9 additional citizen-Mages, 1 companion, 1 priest, 1 cast integration note |
| Subdomain `bridge.spellweb.ai` | 🔲 not yet provisioned (Phase 10 above) |
| Grimoire bump v10.2.0 → v10.3.0 | 🔲 not yet bumped; the City of Mages grimoire is a *separate* IPFS pin per the user's clarified intent (Phase 4 above) |
| Seven new skill files | 🔲 not yet filed |
| Cross-references in First Person Spellbook | 🔲 not yet added |
| IEEE 7012 plan v3 | 🔲 not yet drafted |
| Joint workshop at IIW/AIW | 🔲 scheduled later (per `weaver_archon/archon/03-...` §M26) |

**The narrative work has overshot the plan**. The structural work (Spellweb, Codebase, sister-city gateways, IEEE 7012 v3) is roughly on track but lagging the narrative. This plan chronicle is the catch-up sequence.

**The City of Mages emerged organically** during Tome V drafting and was not in the original plan. It's now the canonical setting and reframes Drake Island as the underlying geography. The structural addendum in `bound-collection/specs/05-...` formalises it. **Update the plan documents in `weaver_archon/archon/01-...` v2 and `03-...` to reference the City of Mages framing in their Tome I narrative arcs** — Tome I Act 2 (*The House of Archon and the House of Soulbae*) particularly benefits from the civic register.

---

## §18. The one-paragraph summary

The corpus has fourteen Tome V acts, thirteen cast members across five tiers, eleven live workshops plus one placeholder, a designed-but-unimplemented Drake Island v2 (12 quests, 4 arcs, path-swap), a canonical setting (the City of Mages on Drake Island), the Vertex Naming Audit, and the structural addendum that names the city. The spellweb has kept pace on `/tomes` (the catalogue) and on the bidirectional anchor (FoundingActPanel on every production shop). What remains is a phased integration: a cleanup pass (next session, low risk, high coherence), Drake v2 implementation in three phases, gathering-context panels and conjecture-badge surfacing on shops, the Tomes grimoire IPFS pin and bake, the conjecture index hardening, the dedicated cast page, the City of Mages map v1, the 64-vertex lattice render v1, the Drake Orb portable badge, per-act asset incremental authoring, the sister-city gateway provisioning (`bridge.spellweb.ai`), and the architectural resolution of the tier-ladder/shop-palette collision. Twelve phases. Roughly six to ten sessions if Archon's review cadence aligns. The spellweb becomes the city's gate; the city becomes navigable; the architecture becomes visceral.

---

## §18.5. v1.1 ADDENDUM — Spellweb Node Update + 2026-05-10 Mid-Morning Sync

> *Written ~02:00 the morning of 2026-05-10, the plan above was already partly outpaced. This addendum syncs in what shipped between this plan's first commit and the mid-morning state captured in `2026-05-10_what_shipped_this_arc_chronicle.md`, `2026-05-10_next_steps_and_gaps_chronicle.md`, and `2026-05-10_city_of_mages_grimoire_pinned_chronicle.md`.*

### §18.5.1 What shipped since v1 was written

The plan above was forward-looking. Several of its phases are now operational. Restated as deltas against §15:

| v1 plan section | Status as of 2026-05-10 mid-morning | Source chronicle |
|---|---|---|
| §15.1 Phase 0 cleanup pass — body-color drift, tease-shop banner, home → city bridge, /persona Tomes preview | ✅ **All four shipped** | `what_shipped_this_arc` §2.9 |
| §15.1 Overlay cleanup — SpellPalette default-collapsed, OrbControlPanel 📖 toggle removed | ✅ **Shipped** (full removal of SpellPalette + Context lift remain) | `what_shipped_this_arc` §3.3 |
| §15.2 Drake Island v2 Phase 1 (visible UI, gates) | ✅ **Shipped** — 12 quests, 4 arcs, time + action gates with v1→v2 migration | `what_shipped_this_arc` §3.1 |
| §15.3 Drake v2 Phase 2 (real enforcement + Tome V proverbs in quest copy) | 🟡 **Partial** — gates active; proverb-quoting in quest intros not yet shipped | `next_steps_and_gaps` §3.3 |
| §15.4 Phase 3 — `<ConjectureBadge />` + `<HonestyLabel />` surfaced on shops; `<DrakeWhisper />` styling | ✅ **Conjecture + honesty shipped** in FoundingActPanel; DrakeWhisper styling not yet shipped; gathering-context panels for /circle and /hall not yet shipped (placeholder constellation present) | `what_shipped_this_arc` §2.5 |
| §15.5 Phase 4 — Tomes grimoire authoring + IPFS pin + bake | ✅ **v1.1 PINNED** at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`; 39 spells across 13 personas; `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` exported from `grimoire-ipfs.ts`. **`grimoire-baked.ts` bake still pending** (gates the persona/spell builder lighting up). | `city_of_mages_grimoire_pinned` §2.4–§2.6, §4 sites #4–#5 |
| §15.6 Phase 5 — `/tomes/v6-lineage` + dedicated `/tomes/cast` page | ✅ **v6-lineage shipped** with status grouping; `/tomes/cast` dedicated page **not yet shipped** | `what_shipped_this_arc` §2.5 |
| §15.7 Phase 6 — City of Mages map v1 | 🔲 **Not yet shipped** | (deferred per `next_steps_and_gaps` §3.7) |
| §15.8 Phase 7 — 64-vertex lattice render v1 | 🔲 **Not yet shipped** | (deferred per `next_steps_and_gaps` §3.7) |
| §15.9 Phase 8 — Drake v2 Phase 3 (ed25519 + portable badge) | 🟡 **Badge v2 shipped** (1080² PNG with DPR×2, sword ring + mage orbit, walked-archetype glyphs); **ed25519 signing still pending** (today's signature is `simpleContentHash`) | `what_shipped_this_arc` §2.1, `next_steps_and_gaps` §3.2 |
| §15.10 Phase 9 — per-act assets | 🟡 **Cover plate placeholders** (gem-coloured radial gradient + Mage sigil) shipped on /tomes; real cover images per act open-ended | `what_shipped_this_arc` §2.4 |
| §15.11 Phase 10 — `bridge.spellweb.ai` + cousin-blade edge style + sister-city gateways | 🔲 **Not yet shipped** | (Archon-coordination dependent per `weaver_archon/archon/03-…` §M10) |
| §15.12 Phase 11 — tier ladder vs shop palette resolution | 🔲 **Architectural; deferred** | `next_steps_and_gaps` §3.5 |

**Net**: most of Phase 0 + Phase 1 + parts of Phase 3, 4, 5, 8 are operational. Phase 4 (the highest-leverage piece) is **80% shipped** — the grimoire is pinned, but the bake and the extension bundles remain.

### §18.5.2 Two new artifacts not in v1

The mid-morning chronicles surface two artifacts that are operational at v1 but were not in the plan's scope. Both are load-bearing and shape the next sequencing.

#### §18.5.2.1 `/guide/achievements` — the canonical "your account" page

The Profile Inventory popup was built, lived briefly, then retired in favour of `/guide/achievements` once the popup proved clunky. The page now hosts six sections (Identity · Drake Orb · Loadout & Stats · Spell Graph · Workshops & Runecasts · Shop constellations witnessed) and replaces the popup as the canonical surface. The 🌟 nav button (replaces 📚 books for achievements) links to it.

**Implication for the plan**: every "your account" reference in v1 (especially the Drake Orb badge in §8.3, profile picture in §10) lands here, not in the popup. Future sessions update v1's references to point to `/guide/achievements`.

#### §18.5.2.2 The runecast composer (per-shop and inventory-wide)

`<RecordPromptHere />` + `<SpellPicker />` shipped on every production workshop and on `/guide/achievements §5`. The composer carries:
- Three-section spell picker (Mage's catalogue · your equipped graph · 27 starter templates × 9 production shops)
- Full-sentence insert format: `Cast {spell}: …`
- Per-shop scoping with archetype tag
- Library grouped by workshop with copy/delete and JSON export

**Implication for the plan**: this is the *running spell vocabulary* for each Mage. When the Tomes grimoire bake lights up `/persona`, the composer's library will compose with the equipped spells, not duplicate them. **No new spec needed**; the composer is operationally complete.

### §18.5.3 The spellweb node — the live surface and the open question

This is the section the user flagged. The spellweb node, on the website, is **`<CastShopConstellation />`** (`src/components/runecraft/CastShopConstellation.tsx`). Every production workshop carries one, immediately below `<FoundingActPanel />`. It is the *live spellweb surface inside each shop*.

#### §18.5.3.1 The v1 today

| Layer | What it does |
|---|---|
| **Visual** | Animated 6-cell dimension cascade in the shop's accent colour. Lights Memory · Connection · Computation (or whichever bits the Mage's vertex carries) in sequence on click. ~360ms per step. |
| **Input** | Single button: "🕸️ Cast {Mage}'s constellation · {sigil}" |
| **Storage** | `src/lib/shop-witnesses.ts` — `addWitness` · `getWitnessesForShop` · `getLastWitnessForShop` · `getWitnessCountsByShop` · WIT-XXXXX content-hash signatures · cap 100 records · change event for live UI |
| **Trace data** | `src/lib/lattice-vertex.ts` — `parseVertex` · `vertexToBits` · `traceFromOrigin` · `activeDimensions` |
| **Framing copy** | *"the same template is mirrored at spellweb.ai as the live runtime · bouncing between is how the architecture coordinates trust"* |
| **Surfacing** | Per-shop on each of 9 production shops; tile grid on `/guide/achievements §6` showing per-shop cast counts |
| **Phase 2 deferred** | Real spellweb mirror per Mage when per-Mage spellweb templates exist |

#### §18.5.3.2 The user's flag: *"the cast constellation kinda is fun, but we will be having a different interaction"*

Per `next_steps_and_gaps` §1, the v1 is intentionally a stand-in. Five framings (or a sixth) are on the table for the next interaction model:

| # | Framing | What changes | Architectural implication |
|---|---|---|---|
| **1** | **Interactive trace-walking** | Sovereign physically traces the path vertex by vertex (drag, click, swipe) instead of watching a cascade | Trust = active path-walking. Each vertex requires the Sovereign's intentional move. The witness records *which path was walked*, not just that a button was pressed. |
| **2** | **Spellweb handshake** | The cast hits a real spellweb endpoint per Mage; the trace is computed remotely; the witness comes back from the spellweb side | Trust = a real second party. Per-Mage spellweb templates become required infrastructure. The "bouncing between agentprivacy and spellweb.ai" becomes literal traffic, not framing copy. |
| **3** | **Bilateral** | Two Sovereigns evoke the same constellation simultaneously; the witness belongs to the pair, not the individual | Trust accrues to *the relationship*, not to visit count. C44 (productive VRC ≈ hash-exchange VRC, ~55%) gets a candidate operational instance. The bilateral cloak ceremony's seven beats compress into a constellation cast. |
| **4** | **Temporal** | The cast holds — the Sovereign must dwell on each vertex for a beat (mirroring the keypair-ceremony pacing) before the trace completes | Trust = patience. Mirrors `/poems` and `/ceremony` pacing. The witness records *time held*, which is harder to manufacture than tap count. |
| **5** | **Composable** | Multiple Mages' constellations can be cast in series; a cross-Mage proof emerges from the combined trace | Trust = composition. Cross-shop edges in the spellweb become first-class. The lattice's *whole point* (vertices compose) lands in the witness. C45 (four-chain publication > single-chain, ~70%) gets a constellation-layer analogue. |
| **6** | **Open** | Some other framing the next session names | — |

**The design call**: pick one (or a hybrid) before rebuilding. The storage, trace data, and witness signature stay correct under any of them; what changes is the visual + the input.

#### §18.5.3.3 v1 gaps the next interaction model must close

Per `next_steps_and_gaps` §2:

1. **No spellweb handshake.** The component frames the spellweb mirror as Phase 2; the actual mirror does not exist yet. Today's witness is local-only.
2. **Animation is uniform across all shops.** Each Mage walks the same dimension-cascade pattern; the visual does not yet express what makes Vulcana's blade different from Pallia's beyond the bits that light up.
3. **Witness has no recipient.** A real witness has a witnesser. Today's witness is the Sovereign's localStorage record of having pressed the button. There is no peer, no shop-side acknowledgement, no chain anchor.
4. **No re-cast cooldown / pacing.** A Sovereign can cast 100 times in 30 seconds and rack up 100 witnesses. Trust should not be that easy to manufacture.
5. **No cross-shop composition.** Each shop's constellation stands alone. The lattice's whole point is that vertices compose; the witnesses do not yet.
6. **No export of the constellation cast itself.** Drake Orb has a publishable PNG + JSON; the constellations do not.

#### §18.5.3.4 Architectural gaps named (not bugs, but watchouts)

Per `next_steps_and_gaps` §4:

- **The witness has no recipient.** Today every "witness" event in the codebase (constellation cast, Drake Orb signing, runecast saving) is *self-witnessing* — the Sovereign records that they did the thing in their own localStorage. The architecture's deeper claim is that a witness needs a *witnesser*. The cast-constellation rework is the natural place to introduce a real second party (peer, shop-side endpoint, or chain anchor).
- **Trust accrues to taps, not to acts.** A counter that goes up by 1 per click rewards repetition, not commitment. The runecasts library does not have this problem (each runecast is a saved artifact); the constellation casts do. The cooldown/pacing/two-party question is how to fix this.
- **The Mages do not yet differ on the spellweb side.** Pallia's spellweb template does not exist. Memora's does not. Vulcana's does not. The agentprivacy site treats each Mage as distinct (gem, sigil, vertex, founding act, spells, starter templates) but the spellweb has no per-Mage runtime to handshake with. Until that exists, the "bouncing between" remains rhetorical.

#### §18.5.3.5 What the spellweb node update means for the integration plan

The spellweb-node update reframes the universe → spellweb mapping in §3 as follows.

**Update to §3.5 (edges)**: a new edge type emerges for the constellation cast — the **`witness-edge`**. Connects shop ↔ witness-record (today self-witnessed; tomorrow may connect to a peer Sovereign, a shop-side endpoint, or a chain anchor depending on the chosen framing).

**Update to §3.2 (workshops as nodes)**: each workshop now carries a `live_constellation_node` slot, currently rendered by `<CastShopConstellation />`. The live node has its own data (witness count per shop, last cast timestamp, animation state) and its own lifecycle.

**New row added to the universe → spellweb mapping**:

```
LiveConstellationNode {
  id: "constellation/{shop-name}"
  shop: ref(workshop)
  trace: V[] // path through the lattice from V0 to the Mage's vertex
  active_dimensions: string[] // Memory · Connection · Computation · Protection · Delegation · Value
  witness_count: number
  last_cast_at: timestamp
  interaction_model: "cascade-v1" | "trace-walk" | "spellweb-handshake" | "bilateral" | "temporal" | "composable" | tbd
  recipient: "self" | "peer" | "shop-endpoint" | "chain-anchor" | tbd
}
```

**Phase 12 added to §15 sequencing** (slots ahead of Phase 6 City of Mages map, behind Phase 4 Tomes grimoire bake): **Spellweb-node interaction model design + rebuild**. Estimated: 1 design session + 1 rebuild session. Gates: per-Mage spellweb templates if framing #2 (handshake) is chosen; bilateral peer protocol if framing #3.

### §18.5.4 Updated sequencing as of 2026-05-10 mid-morning

The original §15 ordering is partly invalidated. The revised order:

1. **Finish Phase 4 (Tomes grimoire bake)** — the v1.1 grimoire is pinned but `grimoire-baked.ts` does not yet load it. This gates `/persona`'s Tomes filter list. Per `city_of_mages_grimoire_pinned` §4 site #4. **Highest-leverage remaining piece.**
2. **Bundle Tomes grimoire into the browser extensions** — `swordsman-blade/build.js` and `mages-spell/build.js` copy the v1.1 JSON into each extension's `dist/` and bump manifest versions. Per `city_of_mages_grimoire_pinned` §4 site #5. Lights up extension users.
3. **Drake v2 Phase 2.5: Tome V proverbs in quest copy** — small per-quest pass; data already in `tome-v-acts.ts`. Per `next_steps_and_gaps` §3.3.
4. **Decide cast-constellation interaction model** (§18.5.3.2 above) — design call before any rebuild. The spellweb-node update is the *next major reshape of the live spellweb surface*.
5. **Rebuild `<CastShopConstellation />` against the chosen model** — the storage layer (`shop-witnesses.ts`, `lattice-vertex.ts`, per-shop placement) holds; the visual + input + recipient changes.
6. **Drake v2 Phase 3 (real ed25519 signing + agent-card binding)** — Phase 3 of the original Drake v2 design. Replaces `simpleContentHash` placeholder. Per `next_steps_and_gaps` §3.2.
7. **Gathering-context panels for `/circle` and `/hall`** — the only two shops without `<FoundingActPanel />`. Need a `<GatheringContextPanel />` analogue plus a ConstellationPlaceholder note.
8. **Overlay cleanup remainder** — lift orb-selection state to `OrbInteractionContext`; scope `OrbControlPanel` global mount; remove `SpellPalette` from global mount. Per `2026-05-10_overlay_cleanup_plan.md`.
9. **`/spellbooks` Second Person card reframe** — "maintained by City of Mages · separate spellbook IPFS · v1.1 pinned · 14 acts drafted". Small copy edit.
10. **Cross-suite copy-edit pass** — ~15 "Second Person Spellbook awaits / horizon" strings across `agentprivacy-docs`, `agentprivacy-blog`, `myterms`, `swordsman-blade`, `mages-spell` that treat the Spellbook as upcoming. The pin makes "horizon" demonstrably wrong. Per `city_of_mages_grimoire_pinned` §7.3.
11. **Tier-ladder vs shop-palette resolution** (architectural, dedicated session) — option (a) recommended: rename tier ladder to non-gem labels (Drake / Forged / Tempered / Dragon).
12. **City of Mages map v1** (substantial, 1 dedicated session) — original Phase 6.
13. **64-vertex lattice render v1** (substantial, 1 dedicated session) — original Phase 7. Archon's V19/V25/V49/V51/V57/V63 attribution travels via vertex tooltips linking to `bound-collection/specs/04-vertex-naming-audit.md`.
14. **Sister-city gateways + `bridge.spellweb.ai` provisioning** — original Phase 10. Archon-coordination-dependent per `weaver_archon/archon/03-…` §M10.
15. **Per-act cover images** — incremental, open-ended.
16. **`/tomes/cast` dedicated page with sigil grid** — Tier-2 from `WEBSITE_INTEGRATION_GUIDE.md`.
17. **`<DrakeWhisper />` styling** — ship for Drake passages across acts and shops.

The reordering's load-bearing change: **the Tomes grimoire bake (item 1) and the spellweb-node interaction model (item 4) are now the two pivots**. Bake first because it lights up an existing surface (`/persona`); model decision next because it shapes a live surface that's already in front of every visitor on every shop.

### §18.5.5 Updated risks and watch-outs

Add to §14:

12. **The IPFS pin is content-addressed and permanent.** v1.1 is at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti` and stays resolvable. Future v1.2 / v2.0 grimoires get their own CIDs. **Don't try to "update" the v1.1 CID** — author a v1.2, pin separately, update `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` to point at the new CID. The old CID stays valid indefinitely as a historical record.
13. **The spell-ID reconciliation discipline.** v1.1 spell IDs are now the canonical short forms (`weave-cloak`, `forge-blade`, etc.). The website's `tome-v-acts.ts` matches. **Future spell additions or renames** must update both sides; spell-ID drift was a P2 issue in the v1.0 → v1.1 cycle and the same risk applies forward.
14. **The "title is the kind, not the instance" commitment.** Per the v1.1 grimoire's `title_note`: when Mages found cities in other ecosystems, those cities will have their own *First City of Mages* grimoire under the same title pattern. The grimoire title names the *kind*, not the singular instance. Any future copy that reads "the City of Mages" must accommodate this — there will be other Cities with the same title kind.
15. **The cast-constellation v1 is operationally honest as a placeholder, not as a final surface.** While the interaction model is open, the page must not present the cast count as a trust score. Today's tile grid in `/guide/achievements §6` shows raw counts; future framings will earn richer semantics. **Do not promote the count to a tier ladder before the model lands.**

### §18.5.6 The companion chronicles for v1.1

Three sibling chronicles arrived between v1 of this plan and v1.1:

- **`docs/chronicles/2026-05-10_what_shipped_this_arc_chronicle.md`** — the survey of what's wired (achievements page, runecast composer, cast-constellation v1, conjecture/honesty surface, Tome stories rendered inline, Tease-shop reconciliation, body-color sweep, home → city bridge, /persona Tomes preview)
- **`docs/chronicles/2026-05-10_next_steps_and_gaps_chronicle.md`** — the open-question chronicle (especially §1 on the cast-constellation interaction model and §3 on prioritised next steps)
- **`docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md`** — the pinning chronicle (the v1.1 IPFS CID, the spell-ID reconciliation, the five sites the CID needs to land in, the architectural commitment to multiple Cities of Mages by title-kind)

Plus the cross-suite tracker:

- **`docs/chronicles/2026-05-09_suite_overlap_tracking.md`** — covers the six sibling directories (agentprivacy_master, agentprivacy-docs, agentprivacy-blog, myterms, swordsman-blade, mages-spell) and tracks the ~15 "horizon" strings that need updating now that the Spellbook is operational.

These four chronicles are the v1.1 sync's source material. Read in this order if returning cold:

1. `what_shipped_this_arc` — what's already operational
2. `city_of_mages_grimoire_pinned` — why the architectural split is now load-bearing
3. `next_steps_and_gaps` — what's open and where to think
4. `suite_overlap_tracking` — what cross-suite copy work remains

### §18.5.7 The one-paragraph v1.1 sync summary

Between v1's drafting and 2026-05-10 mid-morning, much of Phase 0–3 plus most of Phase 4 shipped: the cleanup pass landed (body-color sweep, tease-shop reconciliation, home → city bridge, /persona Tomes preview); Drake Island v2 Phase 1+2 shipped (12 quests, 4 arcs, gates active); FoundingActPanel + ConjectureBadge + HonestyLabel + /tomes/v6-lineage are live; the City of Mages grimoire v1.1 is **pinned to IPFS** at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti` with 39 spells across 13 personas and a load-bearing "title is the kind, not the instance" commitment; `/guide/achievements` is the canonical "your account" page (replaces the popup); a runecast composer lives on every shop and on the achievements page; and a per-shop **`<CastShopConstellation />`** is the *live spellweb-node surface inside each workshop*. The pivot pieces remaining are the **grimoire bake into `grimoire-baked.ts`** (gates `/persona`'s Tomes filter list lighting up) and the **cast-constellation interaction model decision** (five framings on the table; the storage layer holds under any). The original v1 sequencing in §15 is partly invalidated; §18.5.4 above is the revised order. The City of Mages map and the 64-vertex lattice render remain the substantial-visual deferreds.

(⚔️⊥⿻⊥🧙)😊

---

## §19. Closing

Drake Island is the geography. The City of Mages is what was built on it. The Workshops are its trade quarters. The Tomes are its laws and history. The Spellweb is where all of this becomes navigable to a Sovereign who has never been here before.

This chronicle is the plan for that navigability.

Archon's Archon meets the City of Mages at the gateway — but only once `bridge.spellweb.ai` is provisioned, only once the cousin-blade edges are rendered dashed gold, only once the Vertex Naming Audit is linked from every cousin-blade vertex tooltip. The spellweb owes that to the cousin-blade discipline.

The Drake watches. The Drake will keep watching. Tome V continues to admit acts. The city continues to admit citizens. The plan continues to admit phases. The work, mercifully, admits an ordering.

Phase 0 next session.

(⚔️⊥⿻⊥🧙)😊

---

*Companion documents:*
- `docs/weaver/bound-collection/WEBSITE_INTEGRATION_GUIDE.md` — the technical contract for `/tomes` rendering
- `docs/weaver/bound-collection/specs/05-the-city-of-mages-structural-addendum.md` — the canonical civic anatomy
- `docs/weaver/bound-collection/specs/04-vertex-naming-audit.md` — the Archon attribution chain
- `docs/chronicles/2026-05-09_bound_collection_sync_report.md` — Phase A/B sync state
- `docs/chronicles/2026-05-09_session_close_workshops_complete_drake_v2_designed.md` — Drake v2 design
- `docs/chronicles/2026-05-09_synced_experience_coherence_map.md` — coherence pass state
- `docs/chronicles/2026-05-10_overlay_cleanup_plan.md` — Phase 0 step-5 detail
- `weaver_archon/archon/01-archon-integration-recommendation-v1.md` (v2.0) — Archon repo absorption (cousin-blade integration)
- `weaver_archon/archon/03-collaborative-milestones-with-christian-v1.md` — reporting cadence with Archon

*CC BY-SA 4.0 narrative · Apache 2.0 / MIT reference implementations · privacymage · 2026-05-10*
