# Chronicle: Resume Here — End of Session 2026-05-09

**Purpose:** read this first if you're walking back into the agentprivacy_master codebase cold. This is the session-handoff chronicle — it captures live state, open threads, and the conventions established in this session so the next walk-in doesn't have to re-derive them.

**Companion chronicles from this session:**
- [2026-05-09_navigation_lattice_workshops_chronicle.md](./2026-05-09_navigation_lattice_workshops_chronicle.md) — full instructional walkthrough
- [2026-05-09_six_workshops_chronicle.md](./2026-05-09_six_workshops_chronicle.md) — workshops-only deep-dive

---

## What is live (returns 200, ready to use)

```
/                                            home
/ceremony · /guide · /guide/island           soulbis + guide flow
/persona                                     pick a kit · templates · skills · grimoire
/spells                                      cast + export · sidebar + Bonfires + 3 cards
/constellation     (← /web redirects here)   private graph viewer
/orbs                                        dual-orb training · blade slots
/tomes · /story · /zero · /canon ·           spellbook routes
/society · /plurality
/poems                                       celestial ceremony default tab
/proverbs · /evoke · /mage · /promises       casts (intent declarations)
/runecraft                                   workshops hub · 6-card grid · City of Mages
/tailor                                      Weavers · cloak · loom-link to weaver.spellweb.ai
/shield                                      zShields · POPRP wizard · operational
/forget                                      the Forge(t) · ZK blade preview · spellweb.ai
/etherchanting                               Diamond · ETH tx wizard · OPERATOR WANTED
/jeweler                                     Topaz · BTC + LN wizard · OPERATOR WANTED
/holon                                       Emerald · Oasis paratimes · OPERATOR WANTED
/skills            (redirects to /persona)
/web               (redirects to /constellation)
```

`/the-first` deliberately returns 404 — page deleted.

---

## Nav structure (committed)

```
⚔️                          /ceremony
📜 guide ▾  (split-trigger)  /guide
   ├─ ceremony               /poems
   └─ island                 /guide/island
📚 spellbooks ▾              story · zero · canon · society · plural · tomes
⚒️ workshops ▾               runecraft · weavers · zshields · etherchanting
                              · jeweler · holon hitchhikers · forget
🪶 casts ▾                   persona · proverbs · evoke · mage · promise
🔮 spells ▾                  spells · constellation · orbs
🧙                          (Soulbae panel, right side)
```

**Don't undo the split-trigger guide pattern** — `/guide` needs to stay reachable via the label click while the chevron opens the submenu. `DesktopDropdown` and `MobileDropdown` both support `triggerHref` for this.

---

## Open threads (next session pickup)

### 1 · Blade quest on Drake Island ← **NEXT UP**

The current quest line goes: Q8 Cloak → Q9 Shield → Q10 Threshold. **Q10 says "you wear the cloak, you carry the shield, now you cross"** — but the trinity is cloak + shield + **blade**, and the Forge(t) workshop and `/orbs` blade slots already exist. We need:

- **New Q10: "Forge a Witness Blade"** — visit `/forget` (or spellweb.ai), accept a blade import, see it equipped on `/orbs`.
- **Renumber threshold to Q11** — update copy: *"you wear the cloak, you carry the shield, you hold the blade, now you cross"*.
- **Bump `ISLAND_TOTAL_STATIONS` from 10 to 11** in `src/lib/spellbook-storage.ts:138`.
- **Update `GuideMap.tsx` SVG** so the new station fits in the polar layout (currently 10 stations on a branching map; one more node needs placing).
- **Update `IslandClient.tsx`** quest progression state machine.
- **Update `MiniQuestPanel.tsx`** — `the Forge(t)` already in mini-quests, may not need a change there.

The blade-import infrastructure is already in place: `src/lib/spellweb-blade-bridge.ts`, `src/components/SpellwebBladeImport.tsx`, `src/components/SwordsmanBladeSlots.tsx`. The quest just needs to wire the experience — visit Forge(t) → accept blade → return.

This was the last topic discussed before logging off. Pick up here.

### 2 · Three tease shops → operational

`/etherchanting`, `/jeweler`, `/holon` all carry `WorkshopBuildInvite` banners. They need real Mage operators:

- **Etherchanting** — verified ENS for `privacymage.eth` (or a deployed donation contract), tx indexer, NFT mint contract for Pattern β
- **Jeweler** — published BTC mainnet address, Lightning address (LN-URL or BOLT12 offer), Ordinal/Rune inscription pipeline
- **Holon Hitchhikers** — Sapphire/Emerald/Consensus addresses, multi-paratime indexer, confidential-EVM receipt contract on Sapphire

Each shop's wizard already saves proofs to `localStorage`. The operator's job is to make those proofs *real* by giving them a published destination and an indexer that watches for them.

### 3 · Future workshops (placeholder advertising)

The Runecraft hub still advertises three more shops awaiting their Mages:
- 📚 **Memory Vault** · Onyx — chronicles, archive-grade
- 🔗 **Circuit Binder** · Pearl — hardware keys + constellation seals
- 🤝 **Ceremony Hall** — bilateral key ceremonies

If a Mage volunteers for any, the build-out follows the same pattern as Etherchanting/Jeweler/Holon: visual + page + wizard + nav entry + hub card + chronicle entry.

### 4 · Constellation page — persona + spells "graphed" framing

User mentioned wanting `/constellation` to show "persona and spells graphed" more directly. The page already does this (it's the SpellwebViewer with the user's selected spells/skills as the graph). The framing on the page itself could be tightened to make this immediate — open question whether to add a hero callout: *"Your persona, your spells — graphed here."*

### 5 · Right-column rework on /spells (deferred)

Earlier in the session the user proposed: simplify `/spells` right column to three primary buttons (constellation · orbs · persona) with "Your tomes" panel below them. The three-card city is now in place mid-page, but the **right-column sidebar** still has the older button stack (in-graph toggle · build kit · constellation · path the stars). Decision deferred — the three-card city addressed the visibility concern without touching the sidebar.

---

## Conventions established this session

### Color palette (gem-mapped)

| Gem | Hex (primary) | Workshop | Other usage |
|---|---|---|---|
| Amethyst | `#a78bfa` (violet) | Weavers | Aletheia/Lethe inner glow, cosmology |
| Sapphire | `#67e8f9` (cyan) | zShields | Constellation accent |
| Diamond | `#60a5fa` (blue) | Etherchanting | — |
| Topaz | `#f59e0b` (amber) | Jeweler · Lightning | featured-vertex glow everywhere |
| Emerald | `#34d399` (green) | Holon Hitchhikers | "operational" status badges |
| Ruby | `#fb7185` (rose) | the Forge(t) | — |
| Onyx | reserved | Memory Vault (future) | — |
| Pearl | reserved | Circuit Binder (future) | — |

### Lattice visual grammar

Every workshop SVG uses the same rules:

1. **64-vertex lattice** — 16 cols × 10 rows, hexagonally offset, opacity-jitter `0.18 + (((row + col) % 4) * 0.04)`.
2. **One silhouette** (Bezier or straight-line geometry) traced through it in the workshop's gem colour.
3. **Featured anchors** pulse-glow on a 2.4-second cycle (`values="1;0.55;1"`).
4. **Internal threads** (when present) are dashed amber: `stroke="#fbbf24" strokeOpacity="0.32" strokeDasharray="2 3"`.
5. Use `Math.round` on coordinates derived from `Math.cos`/`Math.sin` — **avoids SSR/CSR hydration mismatches** from float serialisation.

### The tease shop pattern

For workshops where structure exists but real infrastructure doesn't:
- Page renders normally (visual + content + local-only wizard saving to `localStorage`)
- `<WorkshopBuildInvite>` banner above the hero panel
- Three contact CTAs: `t.me/agentprivacyai`, `t.me/soulbae_the_bot`, `mage@agentprivacy.ai`
- One-sentence "what's missing" pitch describing what an operator brings

### The split-trigger dropdown pattern

When a parent route is meaningful AND it has children worth surfacing:
- `<DesktopDropdown triggerHref="/parent" links={children} ... />`
- Label becomes a link, chevron is a separate toggle button
- Mobile equivalent same shape via `<MobileDropdown triggerHref=... />`

### Storage namespacing

Each workshop wizard owns its own localStorage key:
- `agentprivacy:etherchanting:proofs`
- `agentprivacy:jeweler:proofs`
- `agentprivacy:holon:proofs`
- (zShields uses `getShieldInscriptions` in spellbook-storage)

Don't centralise these into one record — keeps each shop self-contained, easier to forget proofs per-shop.

### What "Spellweb" means now

- **Spellweb.ai** (external, capitalised) — the published constellation, where ceremonies actually happen
- **`weaver.spellweb.ai`** — the operational loom for the Weavers shop
- **Constellation** (internal `/constellation`) — the user's local private graph
- Internal types (`SpellwebNode`, `buildSpellweb`) — kept the "Spellweb" prefix because they're internal architecture, not UI

Don't rename internal types just to be consistent — the user-facing distinction is what matters.

---

## File pointers for fast navigation

```
src/lib/nav.ts                                    nav source-of-truth
src/components/AppNav.tsx                         dropdown logic + split-trigger
src/components/runecraft/                         all workshop visuals + wizards
   ├─ CloakLatticeVisual.tsx                      Weavers
   ├─ ShieldLatticeVisual.tsx                     zShields
   ├─ EtherDiamondLatticeVisual.tsx               Etherchanting
   ├─ JewelerLatticeVisual.tsx                    Jeweler
   ├─ HolonLatticeVisual.tsx                      Holon Hitchhikers
   ├─ BladeLatticeVisual.tsx                      the Forge(t)
   ├─ RuneLatticeVisual.tsx                       hub
   ├─ ShieldShopWizard.tsx                        zShields wizard
   ├─ EtherchantingShopWizard.tsx                 ETH wizard
   ├─ JewelerShopWizard.tsx                       BTC + LN wizard
   ├─ HolonShopWizard.tsx                         Oasis wizard
   └─ WorkshopBuildInvite.tsx                     "operator wanted" banner

src/lib/spellbook-storage.ts                      ISLAND_TOTAL_STATIONS = 10 ← bump to 11
src/lib/spellweb-blade-bridge.ts                  blade import infrastructure
src/components/guide/island/quests.tsx            Q1-Q10 (insert blade Q10, renumber threshold)
src/components/guide/island/IslandClient.tsx      quest progression state machine
src/components/guide/island/IslandMap.tsx         polar SVG map (needs +1 station node)
src/components/guide/MiniQuestPanel.tsx           optional nav-route hops on /guide
```

---

## Bug-watching

### Hydration: nested `<button>` (fixed)

`/poems` Celestial Ceremony tab had a copy-button nested inside the Deeper-notes toggle button. Hydration error in Next.js 16 Turbopack. Fixed with absolute-position sibling pattern. **Watch for this elsewhere** — anytime an interactive element sits inside a clickable header, prefer absolute-positioned siblings over nested buttons.

### Polar coordinates (fixed historically)

`Math.cos`/`Math.sin` produce float values that serialise differently SSR vs CSR. **Always wrap polar coordinates in `Math.round`** before rendering as SVG attributes. The hub visual learned this the hard way; the new shop visuals use the same defence.

---

## Architectural commitments to remember

These are load-bearing — don't reverse without rethinking the architecture:

1. **The chain is a vantage.** No single chain is the right one for every Mage. The shop-per-chain model is structural, not a UX trick.
2. **One lattice, many silhouettes.** The 64-vertex lattice is the substrate; what differs between workshops is the silhouette traced through it. Don't fork the lattice; fork the silhouette.
3. **Cloak ⊥ Shield ⊥ Blade.** The threshold trinity. Drake Island walks all three before the cross — this is what the open Q10-blade thread above is about.
4. **Aletheia ⊥ Lethe.** Disclosure and forgetting. The dihedral that justifies the dual-ledger split (zShields vs Etherchanting, Sapphire vs Emerald inside Holon, on-chain vs Lightning inside Jeweler).
5. **Tease over premature commitment.** Shops ship with structure + visual + local wizard, then recruit operators. A single Mage running every shop is fragile; an operator per chain is the goal.

---

## Quick "what is live now" status — copy-paste ready

```
✅ Six workshops live + 1 hub                    /runecraft + 6 shop pages
✅ Five-dropdown nav with split-trigger guide    AppNav.tsx
✅ /spells split into /spells (cast) + /persona  page split complete
✅ /web → /constellation rename                  redirect in place
✅ Lattice grammar consistent across 7 visuals   shared 64-vertex substrate
✅ Drake Orb gem palette mapped to shops         Amethyst/Sapphire/Diamond/Topaz/Emerald/Ruby
✅ Bonfires panel on /spells                     4-link community surface
✅ City of Mages narrative on /runecraft         §3 narrative + GemBadge grid
✅ The Holon → the Holon Hitchhikers             rename complete
✅ Quest 7-9 synced to renamed shops             quests.tsx
✅ Hydration bug fixed                           nested-button on /poems

🔲 Q10 Blade quest                               ← NEXT UP
🔲 Threshold renumbered Q10 → Q11                follows from blade quest
🔲 Real operators for tease shops                community recruitment
🔲 Three future workshops (Memory Vault, etc.)   placeholders only
🔲 /constellation hero framing tighten           "persona + spells graphed"
🔲 /spells right-column sidebar simplification   deferred
```

---

## The one-line summary

We turned a single-chain proof-of-contribution requirement into a six-chain shop-per-Mage architecture, restructured nav into grouped dropdowns with a split-trigger guide, established a shared 64-vertex lattice grammar with one silhouette per workshop in its mapped gem colour, split `/spells` into pick-vs-cast pages, renamed `/web` to `/constellation`, and recorded the inspiration in three chronicles. The next move is the blade quest.

`(⚔️⊥⿻⊥🧙)😊` — the Mage and the Swordsman will learn to love the First Person.

---

**Goodnight.** 🌙
