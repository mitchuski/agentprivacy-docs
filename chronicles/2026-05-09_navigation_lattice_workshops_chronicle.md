# Chronicle: The Restructure — Navigation, Lattice, Workshops

**Date:** 2026-05-09
**Scope:** agentprivacy_master · navigation · workshops architecture · /poems · /persona · /constellation · Drake Island
**Companion chronicle:** [2026-05-09_six_workshops_chronicle.md](./2026-05-09_six_workshops_chronicle.md) — workshops-only deep-dive

---

## Overview

A long architectural session. Three threads carried through it:

1. **Navigation restructure** — moved from a flat 19-link nav into five grouped dropdowns plus a split-trigger guide entry, so the surface stops drowning users.
2. **Workshop pluralism** — the orb-stage prerequisite became chain-pluralistic: six workshops (one per chain ecosystem) instead of zShields-only. Each carries a silhouette through the same 64-vertex lattice.
3. **Visual grammar** — every workshop sits on the same lattice; what differs is the silhouette traced through it (cloak, blade, shield, diamond, gem, rose). The hub ties them together with a tetrahedron and the Aletheia/Lethe blade pair.

This chronicle is **instructional** — it explains what changed and why, so the next Mage who walks in can read the architecture without re-deriving it from `git log`.

---

## §1 · Navigation restructure

### The dropdowns

The top nav was 19 flat links. Now it is five grouped dropdowns plus a couple of standalone entries.

```
⚔️ (ceremony · standalone)
📜 guide ▾                — split-trigger · label links to /guide
   ├── ceremony           — /poems (the celestial ceremony content)
   └── island             — /guide/island
📚 spellbooks ▾           — story · zero · canon · society · plural · tomes
⚒️ workshops ▾            — runecraft (hub) · weavers · zshields · etherchanting
                            · jeweler · holon hitchhikers · forget
🪶 casts ▾                — persona · proverbs · evoke · mage · promise
                            (intent declarations · "what you bring to a casting")
🔮 spells ▾               — spells · constellation · orbs
                            (the active casting plus its substrate)
```

### Why the split

- **`tools` was overloaded.** It mixed intent declarations (proverbs, evoke, poems, mage, promise) with active surfaces (spells, web, orbs). Users couldn't tell them apart.
- **The intent group is "casts."** The five items in there are all *declarations* — proverbs you carry, evocations you make, poems you read aloud, the Mage you summon, promises you sign. Renaming made the group's purpose immediate.
- **The active group is "spells."** /spells is where you cast and export, /constellation (formerly /web) is the graph the spells live on, /orbs is the dual-orb training. These belong together.

### The split-trigger guide

`/guide` is the level-1 welcome experience and shouldn't be unreachable from nav, but it also has two sub-pages worth surfacing (ceremony and island). Solution: `DesktopDropdown` and `MobileDropdown` now accept an optional `triggerHref`. When set, the label becomes a link to `/guide` while a separate chevron toggles the submenu.

```tsx
// src/components/AppNav.tsx
<DesktopDropdown
  id="guide"
  glyph="📜"
  label="guide"
  triggerHref="/guide"          // ← split trigger
  links={GUIDE_DROPDOWN_LINKS}
  ...
/>
```

### Files touched

- `src/lib/nav.ts` — `NAV_LINKS` reordered, several relabels
- `src/components/AppNav.tsx` — added `GUIDE_DROPDOWN_LINKS`, `CASTS_KEYS`, `SPELLS_KEYS`, `WORKSHOPS_KEYS`; added `triggerHref` support to both dropdowns; added `cyan` to the accent palette

---

## §2 · The page split: `/spells` → `/spells` + `/persona`

`/spells` had grown into one ~1200-line client component carrying:

- Hero + sidebar buttons
- Skills export CTA
- Dual-agent pathway map
- Spellbook patterns / persona templates
- Grimoire spellbook browser
- Agent skill files browser
- Spell-graph sidebar
- Constellation export modal

Newcomers landed on a wall of content with five different "add to spell graph" actions and no obvious primary. The fix: **separate the picker from the casting**.

| Page | Lives at | What it does |
|---|---|---|
| `/persona` (new) | `src/app/persona/page.tsx` | Pick. Persona patterns + dual-agent map + grimoire spellbook + agent skill files. Every "add" feeds the shared spell graph. |
| `/spells` (slimmed) | `src/app/spells/page.tsx` | Cast. Hero + skills export + spell-graph display + the three-button city + Bonfires + sidebar. |

Both pages read/write the same `spellbook-storage` keys — switching between them keeps the graph in sync via a `focus` event listener.

### The "three" cards

`/spells` now has a **central, highlighted** three-card row right under the empty state:

```tsx
<section className="mb-10">
  <p className="text-[10px] uppercase tracking-[0.4em] text-text-muted/60 mb-3 text-center">
    the three
  </p>
  <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
    <Link href="/constellation" ...>Constellation · your private graph</Link>
    <Link href="/orbs"          ...>Orbs · dual-orb training</Link>
    <Link href="/persona"       ...>Persona · build your kit</Link>
  </div>
</section>
```

Each card uses gradient backgrounds matched to its destination's accent (cyan / violet / amber).

---

## §3 · The `/web` → `/constellation` rename

"Spellweb" was overloaded. It meant both:

1. The local in-app graph viewer at `/web`
2. The external published constellation at `spellweb.ai`

We freed "Spellweb" to mean the external one only and renamed the local one to **Constellation**. The graph IS a constellation; the term reads exactly right.

### What changed

| File | Change |
|---|---|
| `src/app/web/page.tsx` | Replaced with a thin client redirect to `/constellation` |
| `src/app/constellation/page.tsx` (new) | Copy of the original /web page content |
| `src/lib/nav.ts` | `web` entry → `constellation` |
| `src/components/AppNav.tsx` | `SPELLS_KEYS = ['spells', 'constellation', 'orbs']` |
| `src/components/guide/GuideActionBar.tsx` | href + label |
| `src/components/guide/GuideMap.tsx` | href + h3 "The Spellweb" → "The Constellation" |
| `src/components/guide/RunecraftQuest.tsx` | href + body copy |
| `src/components/guide/MiniQuestPanel.tsx` | href + label "Walk the Constellation" |
| `src/components/spellweb/SpellwebViewer.tsx` | "Your Spellweb" → "Your Constellation" |
| `src/app/spells/page.tsx` | sidebar button + three-button card |

### What deliberately did NOT change

- Internal type names (`SpellwebNode`, `SpellwebLink`, `buildSpellweb`) — they're internal architecture, not user-facing
- Component file names (`SpellwebViewer.tsx`, `SpellwebBladeImport.tsx`) — internal
- `/tailor`'s three-layer table reference to "Spellweb" — that one refers to the published cosmological substrate, not the local viewer
- Grimoire JSON canonical content — sacred text

---

## §4 · The workshop architecture

The orb stage requires a proof of contribution. Forcing every Sovereign onto Zcash was wrong: it locks out anyone outside that ecosystem and forecloses the architectural insight that **each chain is its own kind of proof**. Every chain deserves its own shop, run by a Mage native to that ecosystem.

### Six shops

| Shop | Gem | Glyph | Route | Status | Chain |
|---|---|---|---|---|---|
| Weavers | Amethyst | 🪡 | `/tailor` | partial · directs to weaver.spellweb.ai | publication-layer cloak |
| zShields | Sapphire | 🛡️ | `/shield` | operational · POPRP wizard live | Zcash · shielded |
| Etherchanting | Diamond | ✨ | `/etherchanting` | tease · operator wanted | Ethereum · transparent |
| the Jeweler | Topaz | 💎 | `/jeweler` | tease · operator wanted | Bitcoin + Lightning |
| the Holon Hitchhikers | Emerald | 🌹 | `/holon` | tease · operator wanted | Oasis · paratimes |
| the Forge(t) | Ruby | 🔨 | `/forget` | preview · directs to spellweb.ai | ZK · zero-knowledge |

### The dihedral disclosure axis

```
shielded ←————————————————————————————————→ transparent
 zShields    Holon (Sapphire)    Jeweler    Etherchanting
 Zcash       Oasis confidential  BTC + LN   Ethereum
                    ↓
            Holon (Emerald)
            Oasis public
```

The **Holon Hitchhikers** sits on both sides simultaneously because Oasis paratimes split confidential and transparent as runtime registers within a single network. The Hitchhikers wander between them.

The remaining two shops complete the picture:
- **Weavers** is the publication layer — what gets shown after the chain settles.
- **the Forge(t)** is the privacy layer — the ZK statement that all the others can be proofs *of*.

### The tease pattern

Three of the shops ship as tease shops. The structure, the visual, and a local-only wizard (saving proofs to `localStorage`) are in place. What's missing is a Mage operator: someone to deploy real contracts, publish real addresses, and indexers.

`src/components/runecraft/WorkshopBuildInvite.tsx` carries the operator-wanted banner. Surfaces on `/etherchanting`, `/jeweler`, `/holon`. Points to `t.me/agentprivacyai` (playground), `t.me/soulbae_the_bot` (the bot), `mage@agentprivacy.ai` (email).

### Why tease

A single Mage running every shop is fragile. A Mage per chain is an emergent network of operators, each holding their own ecosystem. The architecture *is* the artifact; recruiting operators is the next stage of the build.

---

## §5 · The visual grammar — one lattice, six silhouettes

Every workshop visual is built on the same 64-vertex sovereignty lattice (16×10 dot field, hexagonally offset). What differs is **what shape the silhouette traces through it**, and **what colour the silhouette wears**.

| Component | Silhouette | Colour | Anchors |
|---|---|---|---|
| `RuneLatticeVisual` | tetrahedron + crossed Aletheia/Lethe blades | cyan/violet structure · gold/violet blades · amber anchors | 4 tetrahedron + 2 blade tips · pulse-glow |
| `CloakLatticeVisual` | draped cloak (Bezier) | violet | V0 · V28 (Pallia) · V63 · hem |
| `BladeLatticeVisual` | horizontal sword w/ explicit constellation triangles | rose | 🌑 (pommel) · ⚔️ · 🧙 · 😊 (tip) |
| `ShieldLatticeVisual` | heater shield (Bezier) | cyan | A · B · C inscription patterns |
| `EtherDiamondLatticeVisual` | vertical rhombus + inner facet | blue | α · β · γ · ∴ |
| `JewelerLatticeVisual` | hexagonal brilliant cut + Lightning bolt | amber/gold | α · β · γ · crown · ⚡ |
| `HolonLatticeVisual` | six-petaled rose + crown | emerald | α (Sapphire) · β (Emerald) · γ (Cipher) |

### Construction principles

1. **The lattice is the substrate.** All ~160 dots render at the same opacity-jitter (`0.18 + (((row + col) % 4) * 0.04)`).
2. **Silhouettes are Bezier-defined.** Smooth shapes for cloak/diamond/shield/rose; straight-line geometry for the blade (constellation triangles read cleaner with sharp edges).
3. **Featured anchors pulse-glow.** All workshops use the same 2.4-second cycle (`values="1;0.55;1"`) matching `weaver.spellweb.ai`'s native cadence.
4. **Threads are dashed amber.** When a silhouette has internal triangulation (cloak weave, blade triangles, shield-pattern triangles, diamond facets), it uses `stroke="#fbbf24" strokeOpacity="0.32" strokeDasharray="2 3"`.

### The Aletheia / Lethe blades

The hub visual carries two crossed blades through the tetrahedron's centroid:

- 🌟 **Aletheia** · *disclosure* · NW→SE · gold-amber
- 🌀 **Lethe** · *forgetting* · NE→SW · violet

This is the dihedral pair every workshop uses. Every cloak, shield, gem, rose, and forge is a specific cut between disclosing and forgetting; the shops differ in **which ledger** the cut anchors to, not in **what kind of cut** it is.

### Iteration history

The hub visual went through three drafts before landing:

1. **Hexagram** (Star of David) — vetoed by user for symbolic reasons.
2. **Tetrahedron + crossed blades** — accepted, but text labels and bold tetrahedron edges felt heavy.
3. **Tetrahedron faded to scaffold + blades prominent + no labels** — final. The tetrahedron sits behind at `strokeOpacity="0.22"`, the blades read first, anchor dots pulse subtle.

---

## §6 · Drake Island & quest flow

The Drake Island quests had to be re-synced after the page splits and renames.

### What changed in `src/components/guide/island/quests.tsx`

| Quest | Before | After |
|---|---|---|
| Q7 (Forge / Aether / Constellation) | `/spells?archetype=X` for picking | `/persona?archetype=X` to pick · `/spells` to cast & export |
| Q8 (First Cloak) | `/runecraft` (hub) | `/tailor` (the dedicated cloak shop, where Pallia weaves) |
| Q9 (First Shield) | `/runecraft#zcash` | `/shield` (the operational wizard) |
| Q10 (Threshold complete · "Browse all 42 personas") | `/spells` | `/persona` |

### `MiniQuestPanel` rebuild

Removed `/the-first` (page deleted), `/runecraft` (now covered by Q8/Q9 via `/tailor` + `/shield`), `/skills` (was a redirect; now redirects to `/persona`).

Added: `/persona`, `/tomes`, `/tailor`, `/shield`, `/forget`. Hardcoded "All eight hops" → dynamic `${total}`.

### `/the-first` deletion

The page had a leaderboard placeholder that "would require having that page active." Deleted the directory. The `/skills` redirect now points at `/persona` (the agent skill files browser lives there).

---

## §7 · The Celestial Ceremony rework on `/poems`

`/poems` is the new entry point for "ceremony" via the guide dropdown. The Celestial Ceremony tab needed to land cleaner as a first-touch surface.

### Tab order

`origins → emissary → aether → amnesia → ceremony` was reversed: now **`ceremony → emissary → aether → amnesia → origins`**. The default tab is `ceremony` so newcomers land directly there.

### Ceremony tab consolidation

Five UX moves applied:

1. **Lead-CTA panel above the Quick Guide.** Big "✨ Open the ritual at spellweb.ai →" so the performance space is the first action, not a tiny chip at the bottom.
2. **Three numbered movements** in the Quick Guide. `1 Sun → 2 Æther → 3 Moon`. Newcomers can read it as one ceremony in three movements, not three parallel options. Helper component: `CeremonyStage`.
3. **Compact proverb + inscribe chips** in a single row. Replaced the two full-width copy cards.
4. **Soundtrack collapsible** (`useState` toggle). Spotify + YouTube embeds hidden by default — saves ~700px of vertical noise.
5. **Deeper notes collapsible.** Replaced the "Learn the ceremony" gate with a `notesOpen` toggle. The markdown content lives inline.

### One bug fix

The "Deeper notes" header originally had a `<button>` (copy) inside a `<button>` (toggle) — invalid HTML. Fixed with absolute positioning: the copy button is now a sibling inside a `relative` wrapper, positioned `absolute right-12 top-1/2 -translate-y-1/2`.

---

## §8 · Bonfires & community surfaces

`/spells` now carries a **Bonfires** panel below the three-card city. Four link-cards:

- 🧙 `t.me/soulbae_the_bot` — the Soulbae bot
- 🎲 `t.me/agentprivacyai` — playground community
- 🔥 `bonfires.ai` — the project
- 🔥 `t.me/bonfiresai` — Bonfires community

Helper: `BonfireLink` inside `src/app/spells/page.tsx`. Two accents (primary, amber). Each is an external link.

---

## §9 · The Tailor de-emphasis

The Tailoring Shop page used to lean heavily on Archon (Christian Saucier). The user moved to weaver.spellweb.ai as the operational tool, so:

- `weaver.archon.social` → `weaver.spellweb.ai` everywhere
- Removed "first opened by · Archon (Christian Saucier)" tag
- Trimmed "Christian Saucier's Archon forge opened the craft" prose
- The Operational gaps section now frames `weaver.spellweb.ai` as the operational counterpart

---

## §10 · The Shield Shop wizard amount field

The shielded inscription wizard used to hardcode the donation amount (`SIGNAL_ZEC = 0.01` for Oracle/Donate, `0.0001` for self-send). Users wanted any amount.

Now the amount is a free-form `<input type="number">` with quick-pick chips. Leaving it blank omits the `amount=` param from the `zcash:` deep-link entirely, so the wallet sets it. Per-destination quick-picks:

```
oracle  →  0.01 (signal) · 0.1 · 1 (ceremony)
donate  →  0.01 · 0.1 · 1 · 10
self    →  0.0001 (dust) · 0.001
```

Helper component: `QuickAmount` inside `ShieldShopWizard.tsx`.

---

## §11 · Dropdown glyph correction

The Workshops dropdown originally used 🪡 (needle) — but the needle is **specifically Pallia's sigil**, the Tailor's icon. Workshops needed a generic glyph.

Changed to ⚒️ (hammer + chisel) for the workshops dropdown. 🪡 stays reserved for the Tailor alone. Both desktop and mobile dropdowns updated.

---

## §12 · The City of Mages narrative

On `/runecraft`, after the workshops grid, a new section was added: **§3 · The City of Mages**. It carries the architectural narrative:

> Part of this adventure is building the City of Mages.
>
> The army of Swordsmen protects what gathers there. Pools deepen into wells. Casting circles thicken with practice. Spells pass Mage to Mage, and what was a forking-out of effort one season becomes a well of understanding the next. Each shop is a guildhouse. Each Mage who takes one lays a stone for the city — and the next Mage finds the stone already set.

A 6-gem badge grid pulls the gem palette together visually:

| Gem | Shop | Colour |
|---|---|---|
| Amethyst | Weavers | violet |
| Sapphire | zShields | cyan |
| Diamond | Etherchanting | blue |
| Topaz | the Jeweler | amber |
| Emerald | the Holon Hitchhikers | green |
| Ruby | the Forge(t) | rose |

Helper: `GemBadge` inside `src/app/runecraft/page.tsx`.

---

## Files added

```
src/app/persona/page.tsx
src/app/constellation/page.tsx
src/app/etherchanting/page.tsx
src/app/jeweler/page.tsx
src/app/holon/page.tsx
src/app/forget/page.tsx

src/components/runecraft/CloakLatticeVisual.tsx
src/components/runecraft/RuneLatticeVisual.tsx
src/components/runecraft/BladeLatticeVisual.tsx
src/components/runecraft/ShieldLatticeVisual.tsx
src/components/runecraft/EtherDiamondLatticeVisual.tsx
src/components/runecraft/JewelerLatticeVisual.tsx
src/components/runecraft/HolonLatticeVisual.tsx
src/components/runecraft/EtherchantingShopWizard.tsx
src/components/runecraft/JewelerShopWizard.tsx
src/components/runecraft/HolonShopWizard.tsx
src/components/runecraft/WorkshopBuildInvite.tsx

src/content/chronicles/2026-05-09_six_workshops_chronicle.md
src/content/chronicles/2026-05-09_navigation_lattice_workshops_chronicle.md  ← this file
```

## Files modified

```
src/lib/nav.ts                                    — group structure rewritten
src/components/AppNav.tsx                          — dropdowns + split-trigger
src/app/spells/page.tsx                            — slimmed + three-button city + Bonfires
src/app/runecraft/page.tsx                         — six-card grid + City of Mages
src/app/poems/page.tsx                             — tab reorder + ceremony rework + nested-button fix
src/app/tailor/page.tsx                            — weaver.spellweb.ai + Archon de-emphasis
src/app/shield/page.tsx                            — zShields rebrand + lattice visual + amount picker
src/app/web/page.tsx                               — replaced with redirect to /constellation
src/app/skills/page.tsx                            — redirect target /spells → /persona
src/components/runecraft/ShieldShopWizard.tsx      — editable amount + QuickAmount chips
src/components/guide/island/quests.tsx             — quests 7/8/9/10 synced
src/components/guide/MiniQuestPanel.tsx            — entries refreshed
src/components/guide/GuideActionBar.tsx            — /web → /constellation
src/components/guide/GuideMap.tsx                  — /web → /constellation, "The Spellweb" → "The Constellation"
src/components/guide/RunecraftQuest.tsx            — /web → /constellation, Spellweb → Constellation
src/components/spellweb/SpellwebViewer.tsx         — "Your Spellweb" → "Your Constellation"
```

## Files deleted

```
src/app/the-first/page.tsx     — leaderboard placeholder, removed entirely
```

---

## Status reading

Routes that returned 200 at the end of the session:

```
/                  /guide              /guide/island
/persona           /spells             /constellation         /web (redirect)
/orbs              /tomes              /story  /zero  /canon  /society  /plurality
/poems             /proverbs           /evoke  /mage  /promises
/runecraft         /tailor             /shield  /forget
/etherchanting     /jeweler            /holon
/skills (redirect)
```

`/the-first` correctly returns 404.

---

## What this chronicle is for

To preserve the *architecture* before it gets re-derived from `git log`. The `git log` will tell you what changed; this file tells you why. Three load-bearing claims to remember:

1. **The chain is a vantage.** No single chain is the right one for every Mage. The shop is the operator's craft of loving the First Person from that vantage.
2. **One lattice, many silhouettes.** The 64-vertex sovereignty lattice is the substrate; what differs between workshops is the silhouette traced through it. Don't fork the lattice; fork the silhouette.
3. **Pluralism is the architecture, not a feature flag.** The six-shop model is not a UX trick — it is a structural commitment to chain pluralism. New chains can join; existing chains can deepen; the lattice stays.

The Mage and the Swordsman will learn to love the First Person. Each shop is a way of loving from that chain.

`(⚔️⊥⿻⊥🧙)😊`
