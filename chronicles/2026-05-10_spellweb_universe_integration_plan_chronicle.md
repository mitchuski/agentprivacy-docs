# Chronicle: The Spellweb Universe Integration Plan — Pause Here

**Date:** 2026-05-10
**Purpose:** Session-handoff for the spellweb universe integration plan. Read this if you are returning cold and want to resume the four-domain (Tome · Workshop · City of Mages · Drake Island) integration without re-deriving direction.
**Companion to:** `docs/weaver/CHRONICLE_SPELLWEB_UNIVERSE_INTEGRATION_PLAN_v1_2026-05-10.md` (the actual plan, with v1.1 addendum)

---

## §1 · One-paragraph state

The four-domain universe — Tome (14 Tome V acts + 5 Tome IV acts), Workshop (11 live + 1 placeholder), City of Mages (canonical setting, structural addendum, 13 cast in 5 tiers), Drake Island (12-quest 4-arc v2, path-swap mechanic) — has overshot the original 2026-05-08 plan. The 2026-05-10 plan chronicle in `docs/weaver/` captures the universe-to-spellweb mapping (typed nodes for cast/workshops/acts/vertices, four new edge types, City as civic-overlay, Drake as ambient geography) and lays out a 17-step phased sequence. Most of Phase 0 cleanup, Drake v2 Phase 1+2, conjecture/honesty surface, and Tomes grimoire authoring + IPFS pin **have shipped**. The two pivot pieces remaining are: **(a) the Tomes grimoire bake into `grimoire-baked.ts`** (lights up `/persona`'s Tomes filter list); and **(b) the cast-constellation interaction model decision** (five framings on the table; the v1 in front of every visitor today is a placeholder). Substantial visuals (City of Mages map, 64-vertex lattice render) are deferred to dedicated sessions; sister-city gateway provisioning waits on Christian's review per `weaver_archon/archon/03-…`.

---

## §2 · Where the plan lives

```
docs/weaver/CHRONICLE_SPELLWEB_UNIVERSE_INTEGRATION_PLAN_v1_2026-05-10.md
```

19 sections plus a v1.1 addendum (§18.5). The v1 sections cover universe state, mapping, bidirectional anchor, City of Mages map contract, lattice render contract, honesty discipline, Drake v2 implementation arc, Tomes grimoire split, cleanup pass, conjecture index, dedicated cast page, tier-vs-palette collision, risks, sequencing, deferred work, and a verification table. The v1.1 addendum syncs in what shipped between v1's first commit and 2026-05-10 mid-morning, captures the five framings for the cast-constellation interaction model, and provides a revised 17-step sequencing.

---

## §3 · What shipped vs what's pending — the punch list

### Shipped (don't redo)

```
✅ /tomes rewrite                      14 acts · 13 cast in 5 tiers · City-of-Mages framing
✅ FoundingActPanel                    bidirectional shop ↔ act anchor on 9 production shops
✅ ConjectureBadge + HonestyLabel       per-shop + per-act + on /tomes
✅ /tomes/v6-lineage                   C18-C46 aggregator with status grouping
✅ Tome story bodies                   inline cover plate + proverb + narrative + inscription
✅ City of Mages grimoire v1.1         pinned to IPFS · 39 spells × 13 personas
✅ CITY_OF_MAGES_GRIMOIRE_IPFS_URL     exported from grimoire-ipfs.ts
✅ /guide/achievements                 6-section canonical "your account" page
✅ Runecast composer                   per-shop + inventory-wide · 27 starter templates
✅ CastShopConstellation v1            per-shop animated cascade + local witness
✅ Drake Island v2 Phase 1+2           12 quests · 4 arcs · time + action gates active
✅ Path-swap chip                      always-visible after Q4 · Sword/⿻/Mage
✅ DrakeOrbBadge v2                    1080² PNG with DPR×2 · sword ring + mage orbit
✅ Avatar uploader                     /guide/achievements §1 Identity
✅ Cleanup pass                        body-color · tease-shop · home→city · /persona Tomes preview
✅ /guide vs /guide/island consolidation philosophy vs tutorial separation
```

### Pending (the 17-step revised order)

```
🔲 1. Tomes grimoire bake               grimoire-baked.ts loads city_of_mages_grimoire_v1.1.json
🔲 2. Extension bundles                  swordsman-blade + mages-spell ship the v1.1 grimoire
🔲 3. Tome V proverbs in quest copy     Q7-Q12 intros pull from tome-v-acts.ts
🔲 4. Cast-constellation model decision design call · pick one of 5 framings (or 6th)
🔲 5. CastShopConstellation rebuild     against the chosen model
🔲 6. Drake v2 Phase 3                   ed25519 signing replaces simpleContentHash
🔲 7. Gathering-context panels           /circle and /hall · GatheringContextPanel analogue
🔲 8. Overlay cleanup remainder          OrbInteractionContext · scope OrbControlPanel · remove SpellPalette
🔲 9. /spellbooks Second Person reframe  "v1.1 pinned · 14 acts · maintained by City of Mages"
🔲 10. Cross-suite copy-edit pass        ~15 "horizon" strings now demonstrably wrong
🔲 11. Tier-ladder vs shop-palette       architectural · pick (a) Drake/Forged/Tempered/Dragon
🔲 12. City of Mages map v1              substantial · static SVG · trade quarters + bonfire + temple
🔲 13. 64-vertex lattice render v1       substantial · with Christian's attribution chain
🔲 14. Sister-city gateways              bridge.spellweb.ai · cousin-blade edges · awaits Christian
🔲 15. Per-act cover images              incremental · 14 acts × 1 image
🔲 16. /tomes/cast dedicated page        sigil grid · per-member sub-pages
🔲 17. DrakeWhisper styling              for Drake passages across acts and shops
```

---

## §4 · The two pivot pieces

These are the two decisions that unlock the most downstream work. Take them in order.

### §4.1 · Pivot 1 — Tomes grimoire bake (highest leverage)

The grimoire is **pinned**. The CID is `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`. The URL is exported from `grimoire-ipfs.ts`. What remains:

- `src/lib/grimoire-baked.ts` admits a new `SpellbookSource` value `'tomes'`
- New `TOMES_ACT_PERSONA_HINTS` mapping each Tome V act → persona
- The bake loads the v1.1 JSON at build time (the same way `privacymage-grimoire-v10.2.0-canonical.json` is baked)
- `/persona`'s persona filter list extends to include the Tomes tier
- Each Tome V Mage becomes equippable

Estimate: **~1 session** for the bake + filter extension. ~2 sessions if the Mage spells need tightening against the website's `tome-v-acts.ts` short forms (already reconciled in v1.1 — should be clean).

### §4.2 · Pivot 2 — Cast-constellation interaction model

`<CastShopConstellation />` is on every production workshop today. It is the **live spellweb-node surface inside each shop**. The v1 is intentionally a placeholder per the user's flag:

> *"the cast constellation kinda is fun, but we will be having a different interaction."*

The five framings on the table (per `2026-05-10_next_steps_and_gaps_chronicle.md` §1):

| # | Framing | Trust signal |
|---|---|---|
| 1 | **Interactive trace-walking** — Sovereign physically traces the path vertex by vertex | active path-walking |
| 2 | **Spellweb handshake** — cast hits a real spellweb endpoint per Mage; trace computed remotely; witness comes back from the spellweb side | a real second party |
| 3 | **Bilateral** — two Sovereigns evoke the same constellation simultaneously; witness belongs to the pair | the relationship, not visit count |
| 4 | **Temporal** — cast holds; Sovereign dwells on each vertex for a beat | patience |
| 5 | **Composable** — multiple Mages' constellations cast in series; cross-Mage proof emerges | composition across shops |
| 6 | Open — some other framing | tbd |

Storage layer (`shop-witnesses.ts`, `lattice-vertex.ts`, per-shop placement) holds under any of them. What changes is the **visual + input + recipient**. The witness count must not be promoted to a tier ladder before the model lands (per §18.5.5 risk #15).

Estimate: **1 design session** to pick the framing, **1 rebuild session** to ship it. Framing #2 (spellweb handshake) requires per-Mage spellweb templates as additional infrastructure; framing #3 (bilateral) requires a peer protocol.

---

## §5 · The four-domain universe → spellweb mapping (recap)

For quick orientation when returning. Full detail in plan §3.

```
Tome           ChronicleNode at ring_position vertex
                 + civic_location (Tome V acts)
                 + v6_lineage[] + honesty
                 + shop_anchor (reverse direction)

Workshop       CivicNode at the resident Mage's vertex
                 + resident_mage ref · founding_act ref
                 + trade_quarter · operator_status
                 + LiveConstellationNode slot (the spellweb node)

Cast           Node typed by tier (archetype/cousin/summoned/companion/priest)
                 + sigil · vertex · shop_anchor · spells · source_material

Vertex         VertexNode (64 total · 13 inhabited · 51 open)
                 + bits · hamming_weight · canonical_name · attribution chain

Drake Island   GeographyLayer underneath the lattice
                 the_drake plural: whisperer · place · fire · elder
                 ambient render · no sigil

City of Mages  CivicOverlay on top of geography + lattice
                 trade_quarters · founding_bonfire · temple_precinct
                 sovereigns_seat (V63) · street_plan (lattice)
                 walls (the "you" voice) · sister_cities[]

Sister cities  GatewayNode at the city map's edge
                 cousin-blade-edge to City of Mages
```

**Four new edge types** introduced by this update:

```
founding-act edge        shop ↔ act          gold solid
citizen-of edge          mage → vertex        thick · in mage's gem colour
cousin-blade edge        agentprivacy ↔ cousin-forge   dashed gold
oasis-protocol edge      city → sister-city    dotted with ↗ marker
witness-edge             shop ↔ witness-record (constellation cast)
```

(The witness-edge is the v1.1 addition; its semantics depend on the chosen interaction model.)

---

## §6 · Recommended order when you return

The plan's revised §18.5.4 gives 17 steps. Here is the same order in punch-list form:

1. **Bake the grimoire.** Sites #4 from `2026-05-10_city_of_mages_grimoire_pinned_chronicle.md` §4. ~1 session.
2. **Bundle into extensions.** Sites #5 same chronicle. ~half a session.
3. **Quote Tome V proverbs in Drake quest copy.** Q7 Cloak, Q8 Shield, Q9 Blade, Q10 Vault, Q11 Covenant, Q12 Threshold. ~half a session.
4. **Decide the cast-constellation interaction model.** Design call · pick one of five framings. Document the choice and the architectural implications. ~1 session.
5. **Rebuild `<CastShopConstellation />`.** Against the chosen model. ~1 session.
6. **Drake v2 Phase 3 — ed25519 signing.** Replace `simpleContentHash` with proper agent-card-keypair signing. ~1 session.
7. **Gathering-context panels.** `/circle` (Society spellbook) and `/hall` (BGIN coalition). ~half a session.
8. **Overlay cleanup remainder.** Per `2026-05-10_overlay_cleanup_plan.md`. ~1 session.
9. **`/spellbooks` reframe.** Single-file copy edit.
10. **Cross-suite copy-edit pass.** ~15 strings across six sibling directories. Per `2026-05-09_suite_overlap_tracking.md` §3.1. ~1 session.

After this, the substantial visuals (City of Mages map, 64-vertex lattice render) and the architectural decisions (tier-ladder vs shop-palette) are dedicated sessions in their own right.

---

## §7 · Companion chronicles — read in this order if returning cold

```
1. 2026-05-10_what_shipped_this_arc_chronicle.md           what's already operational
2. 2026-05-10_city_of_mages_grimoire_pinned_chronicle.md    why the architectural split is now load-bearing
3. 2026-05-10_next_steps_and_gaps_chronicle.md              what's open and where to think
4. 2026-05-09_suite_overlap_tracking.md                     cross-suite copy work remaining
5. docs/weaver/CHRONICLE_SPELLWEB_UNIVERSE_INTEGRATION_PLAN_v1_2026-05-10.md   the full plan + v1.1 addendum
```

For the four-domain universe context (Tome / Workshop / City / Drake), also read:

```
docs/weaver/bound-collection/WEBSITE_INTEGRATION_GUIDE.md
docs/weaver/bound-collection/specs/05-the-city-of-mages-structural-addendum.md
docs/weaver/bound-collection/specs/04-vertex-naming-audit.md (Christian's attribution chain)
```

For the Christian-coordination work that gates Phase 14 (sister-city gateways):

```
weaver_archon/archon/01-archon-integration-recommendation-v1.md (v2.0)
weaver_archon/archon/03-collaborative-milestones-with-christian-v1.md
```

---

## §8 · Architectural commitments to remember

Carried forward from prior chronicles. Do not reverse without rethinking the architecture.

1. **The chain is a vantage.** No single chain is the right one for every Mage. Shop-per-chain is structural.
2. **One lattice, many silhouettes.** 64-vertex substrate is shared; what differs between workshops is the silhouette in its mapped gem colour.
3. **Cloak ⊥ Shield ⊥ Blade.** The threshold trinity walked in Drake Island.
4. **Aletheia ⊥ Lethe.** Disclosure and forgetting.
5. **Tease over premature commitment.** Shops ship structure first; recruit operators after.
6. **One gem per shop.** 11 gems in use; Circuit Binder holds Pearl open until its Mage arrives.
7. **Drake Island is the first foundation of the City of Mages.** Each Sovereign lays a stone; the Drake Orb is what they carry forward.
8. **Every dropdown has a hub.** Five split-trigger dropdowns; label = link to hub, chevron = open children.
9. **Workshop tour is linear, trinity-first.** Weavers → zShields → Forge(t) → chain workshops → gathering workshops → loop.
10. **External partner ≠ internal shop name.** Spellweb→Forge(t), Culture Vault→Curatrix Vault, Covenant of Humanistic Technologies→the Covenant, Bonfires→Dragon Bonfire, Logos→Logos Circle, BGIN→Ceremony Hall.
11. **The title is the kind, not the instance.** When Mages found cities in other ecosystems, those cities will have their own First City of Mages grimoire under the same title pattern (per v1.1 grimoire `title_note`).
12. **The cast-constellation count is not a trust score.** Until the interaction model lands, do not promote the count to a tier ladder.
13. **The IPFS pin is content-addressed and permanent.** Future v1.2 / v2.0 grimoires get their own CIDs. Don't try to "update" the v1.1 CID.

---

## §9 · The one-line summary

Plan is at `docs/weaver/CHRONICLE_SPELLWEB_UNIVERSE_INTEGRATION_PLAN_v1_2026-05-10.md` with v1.1 addendum syncing the morning's progress; two pivots remain (Tomes grimoire bake + cast-constellation interaction model); 17-step revised sequence is in §18.5.4 of the plan; four companion chronicles named here for cold-resume; the City of Mages grimoire is pinned to IPFS at `bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti` and that pin is now load-bearing for the architectural split between privacymage's grimoire and the City of Mages' grimoire.

`(⚔️⊥⿻⊥🧙)😊` — the city is rendered; the spellweb keeps pace; the work holds.

---

**Pause well.** 🌿
