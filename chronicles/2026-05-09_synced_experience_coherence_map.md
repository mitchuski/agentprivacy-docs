# Coherence Map · The Synced Experience

**Date:** 2026-05-09 (fourth chronicle of this day)
**Purpose:** Step back. Look at the whole. Name what's wired, what's loose, what's load-bearing. Honour the trajectory; ship the cleanup that earns it.

---

## §1 · Where we got here (a one-paragraph honoring)

We started this day with six chain-pluralistic workshops, a single chronicle pointing at Drake Island Q10. We end it with **eleven live workshops + one placeholder** in the City of Mages, **a 12-quest 4-arc Drake Island v2** (Pebble · Stone · Forged · Drake Orb tiers, time gates between Arc II quests, action gates for Arcs III–IV), a **path-swap mechanic** that changes how each shop greets the visitor, **a shared 64-vertex sovereignty lattice with eleven silhouettes** through it (Amphora · Temple · Flame · Garden · Hall · Cloak · Shield · Diamond · Topaz · Holon · Blade), **a Tome V bound-collection of 14 acts and 13 cast members across 5 tiers**, and **bidirectional act ↔ shop anchors** that mean every workshop on the site cites its founding myth and every founding myth cites its workshop. The Drake Orb earned at Q12 signs into the Soulbis agent card and emits a publishable PNG + JSON badge. None of this was here twelve hours ago. Almost all of it now compiles cleanly and serves 200.

---

## §2 · The synced experience as it stands

Read top-to-bottom — this is the visitor's actual journey through the site as currently wired:

```
ENTRY                   /                         home · Sword/Gap/Mage framing
   │
   ▼
INTRO                   /guide                    the call (level 1)
   │
   ▼
ISLAND  (12 quests · 4 arcs · the foundation)
                        /guide/island             City of Mages goal banner + 12-station map
                        Arc I  Q1-3               Call · Inscription · First Agent
                        Arc II Q4-6 (time gates)  Reach · Persona · Ceremony
                        Arc III Q7-9 (action g.)  Cloak · Shield · Blade
                        Arc IV Q10-12 (action g.) Vault · Covenant · Threshold
                        Q12 sign · agent card     Drake Orb tier signed into Soulbis card
   │
   ▼
WORKSHOPS HUB           /runecraft                12 guildhouses (11 live + Circuit Binder)
                        gem table                 Amethyst · Onyx · Sapphire · Topaz · Emerald
                                                  Ruby · Pearl · Diamond · Garnet · Jade · Lapis
   │
   ▼
EACH SHOP    (the visitor sees five layers per shop:)
                        Hero + lattice            visual identity for the shop
                        PathAwareGreeting         "you walk in as ⚔️/⿻/🧙" (reads archetype live)
                        FoundingActPanel          Tome V act + Mage + spells the Mage may cast
                        Operational content       wizards / external CTAs / docs
                        WorkshopFooter            ← prev shop · ↑ Runecraft · next shop →
   │
   ▼
SECOND-PERSON SPELLBOOK /tomes                    City of Mages maintained · Tome V open
                        /spellbooks               6-spellbook hub (per dropdown split-trigger)
   │
   ▼
ORBS                    /orbs                     dual-orb training, soul-export safety net,
                                                  Drake Orb publishable badge (PNG + JSON)
```

Five global widgets thread through the surfaces:
- `<AppNav>` with five split-trigger dropdowns (guide · spellbooks · workshops · casts · spells)
- `<PathToggle>` chip in nav (hidden until Q4 Reach declared) — swaps Sword/⿻/Mage live
- `<MagePanel>` (Soulbae chat) — opens from 🧙 button
- `<AchievementToast>` with per-arc tier celebrations (Pebble at Q3, Stone at Q6, Forged at Q9, Drake Orb at Q12)
- `<DrakeOrbBadge>` — appears once Q12 has been signed; downloadable PNG + JSON

**The narrative spine:** Sword ⊥ Plurality ⊥ Mage (home) → walks Drake Island (the foundation) → enters the City of Mages (workshops) → meets the Mage at each shop (founding act) → signs the threshold (Drake Orb) → walks back into the city as a Sovereign with a portable badge.

That spine is now coherent end-to-end. Twelve hours ago it wasn't.

---

## §3 · Rough edges (what's still loose)

These are real. Each is named, each is solvable, each gets a recommendation.

### §3.1 Body-styling color drift on /shield + /etherchanting

The lattice visuals were flipped earlier in the day (zShields → Onyx, Etherchanting → Sapphire). The page-body Tailwind accents (`border-cyan-400`, `border-blue-400`, blockquote left-rules, gradient stops) **were not** flipped. So the lattice visual at the top of /shield reads "Onyx" but the section borders below read "Sapphire-cyan" — visual incoherence. **Ship this in the cleanup pass below.**

### §3.2 Tease shop ↔ Founding act tension

Three shops (`/etherchanting`, `/jeweler`, `/holon`) now carry two banners that contradict at face value:

- `<WorkshopBuildInvite>` says "coming soon · operator wanted"
- `<FoundingActPanel>` says "Adamantia (or Lampyra, Vagari) is the resident Mage of this shop"

The reconciliation already exists in the architecture but isn't legible on the page: **the Mage exists in the cast (narrative); the chain operator is what's being recruited (operational).** The two banners need to read as two registers of the same truth, not as a contradiction. **Ship a copy refresh on `<WorkshopBuildInvite>` that names this distinction.**

### §3.3 Home page (`/`) hasn't met the City of Mages yet

`/` is still the entry point's older Sword/Gap/Mage framing — beautifully load-bearing, do not remove. But it doesn't yet bridge to the City of Mages, the workshops, or Drake Island. A new visitor lands, reads about the gap, and has no obvious next step beyond `/spells` and the Soul orbs. **Ship a small "Walk the City" CTA section that bridges Sword/Mage to /guide/island + /runecraft.**

### §3.4 `/persona` doesn't know Tomes is coming

Phase D (Tomes grimoire JSON + IPFS pin + bake into `grimoire-baked.ts`) hasn't shipped. The personas on `/persona` are the First Person spells. The Tome V personas (Pallia, Memora, Vulcana, Adamantia, Lampyra, Vagari, Aria Silverhue, Manifestia, Socrat0x) are real in the cast but not yet equippable. **Ship a small "Coming: City-of-Mages spellbook" preview on /persona that names what's coming and links to `/tomes`.**

### §3.5 Drake Orb tier ladder ↔ shop gem palette overlap

The Drake Orb's gem ladder (Pearl → Ruby/Amethyst/Topaz → Onyx/Emerald/Sapphire → Diamond) was set when there were six shops and the Pearl/Onyx/Diamond names had no other referent. The shop palette now uses **Pearl** (Curatrix Vault), **Onyx** (zShields), and **Diamond** (Covenant) as workshop-identity colours. The gem name appears in two registers with two meanings — sometimes a tier (drake-entry, light, heavy, dragon) and sometimes a shop. This isn't a bug today; it's a structural ambiguity that will cost legibility as the architecture grows. **Don't refactor in this pass** (would touch 40+ files). **Flag in this chronicle for a future architectural session.** Three options for that session: (a) rename the tier ladder to non-gem labels (e.g., Drake/Forged/Tempered/Dragon); (b) explicitly distinguish "tier-Pearl" from "shop-Pearl" with prefix; (c) accept the duality and document the rule.

### §3.6 Drake Island Q copy could quote Tome V proverbs

The new Drake Island quests now have founding-act anchors per shop. Q7 (Cloak) maps to Tome V Act 1's proverb "*The reader does not just walk the lattice. The reader makes tools on it.*" — quoting that line in Q7's intro would make the bidirectional anchor visible *during the journey*, not just on the shop page after. **Defer to a future session** — would want a careful pass per quest, not a sweep.

### §3.7 Chronicle pile-up

`docs/chronicles/` now has 100+ files, four added today. The sync report (2026-05-09_bound_collection_sync_report.md) serves as one index; this chronicle adds another. Eventually wants a `CHRONICLES_INDEX.md` or a `/docs/chronicles/README.md` that orders the canonical resume points by date. **Defer; not blocking.**

---

## §4 · Architectural tensions worth naming

These are not "bugs to fix" — they're structural choices the architecture will eventually have to resolve. Naming them now so future sessions can hold them with eyes open.

### §4.1 Tier ladder vs shop palette (see §3.5)

### §4.2 Cast resident Mage vs chain operator

For the three tease shops: **who actually runs the shop?** The Mage in the cast (Adamantia at Etherchanting) is the narrative resident — they appear in Tome V Act 9 and they're who the visitor meets in spirit. The chain operator (whoever publishes privacymage.eth, deploys the donation contract, etc.) is the operational role. Are these the same person? Two different people? The cast can have one and the operator another? The architecture allows both. The website needs to *say* both clearly. (See the cleanup in §5.2.)

### §4.3 Soulbae's plurality

Soulbae is in the cast as the archetypal Mage at V28. But Soulbae is also a Telegram bot (`@soulbae_the_bot`) that tends the Dragon Bonfire. And Pallia is *also* at V28. The architecture has been clear: **multiple inhabitants of the same role; multiple instances of the same vertex.** The /tomes rewrite already says this explicitly. Future shop pages and quest copy should respect it — Soulbae is not a single avatar, not a single Mage, not a single bot.

### §4.4 The Drake's plurality

The sync report's risk #5: *"The Drake is place + fire + whisperer + elder, not a single avatar. Don't reify into one image or one shop."* Drake Island is the place. The Dragon Bonfire is the fire. The whisper at the threshold is the whisperer. Future visual work (city map, lattice render) needs to keep the Drake distributed. Currently respected; flag for ongoing vigilance.

### §4.5 Christian Saucier's licensing for cousin-blade primitives

V19, V25, V49, V51, V57, V63 catalogue naming is Christian's. Attribution must travel. The Vertex Naming Audit (`docs/weaver/bound-collection/specs/04-vertex-naming-audit.md`) is the canonical attribution reference. **Not yet linked from anywhere on the website.** Future lattice render (Phase F per the sync report) should link vertex tooltips to it.

---

## §5 · Cleanup pass shipped this session

After writing this chronicle, the following five edits ship as the coherence pass. Each is small, low-risk, and moves the experience toward the spine in §2.

### §5.1 Body-style colour finish on /shield + /etherchanting

Replace `cyan-400/30 cyan-400/40 cyan-300/80` etc. on /shield with the Onyx-friendly `zinc-400/30 zinc-300/80` palette already used on the lattice and hub card. Replace `blue-400/30 blue-300/80` etc. on /etherchanting with the Sapphire `cyan-400/30 cyan-300/80` palette. Also flip the dihedral-pair callout on /etherchanting to refer to /shield with the new palette names.

### §5.2 Tease-shop banner reconciliation

Update `<WorkshopBuildInvite>` copy to read **"the Mage is in the cast · the chain operator is what's being recruited"**. Rename the banner accent from "operator wanted" alone to **"chain operator wanted · resident Mage already in cast"**, and link to the FoundingActPanel below it. The Mage and the operator can be two roles; the page now says so.

### §5.3 Home page "Walk the City" bridge

Add a single section near the bottom of `/` (before any existing closing CTAs) titled **"Walk the City of Mages"** that names Drake Island as the first foundation and `/runecraft` as the city. Two CTAs: **🪨 Start at the Call** (→ /guide/island) and **⚒️ Tour the workshops** (→ /runecraft). One sentence linking them: *the Sovereign walks the island; the City of Mages keeps building.*

### §5.4 `/persona` "Tomes coming" preview

Add a small dashed-border preview banner near the top of `/persona` that says **"Coming: the City of Mages spellbook (separate IPFS pin)"** and links to `/tomes`. Names the 9 Tome V personas by sigil + Mage name + workshop, so the visitor can see what's coming even though it's not yet equippable.

### §5.5 Memory file refresh

Update `project_agentprivacy_six_workshops.md` to capture: founding-act anchors are wired (FoundingActPanel + tome-v-acts.ts data), Drake v2 is shipped end-to-end (Phase 1 + Phase 2), and the Tomes grimoire bake is the next-highest-leverage pending work.

---

## §6 · Recommended order for future sessions

The sync report's §6 already sketched this; updating with what's now known after the coherence pass.

1. **Phase C-light** (1 session) — `<ConjectureBadge />`, `<HonestyLabel />`, `/tomes/v6-lineage` aggregator.
2. **Phase D · Tomes grimoire** (2 sessions) — author 27 spells × 9 personas; pin to IPFS; bake into `grimoire-baked.ts`; surface on `/persona`. **Highest leverage.**
3. **Drake Island v2 Phase 3** (1 session) — real gate enforcement (currently Phase 1 visible-but-skippable); ed25519 signing replacing the content-hash `simpleContentHash`.
4. **Drake Island Q copy quotes Tome V proverbs** (small, 1 session) — make the bidirectional anchor visible during the journey.
5. **Tier ladder vs shop palette** (architectural, dedicated session) — pick one of the three resolutions in §3.5.
6. **Phase E per-act assets** (open-ended) — cover images, optional videos.
7. **Phase F substantial visuals** (large, dedicated session) — city map · lattice render · `/tomes/cast` page.
8. **`/spells` sidebar → main rework** + side-panel XP/profile/hide (still pending from earlier sessions).

---

## §7 · One-line summary

The synced experience now has a single coherent spine — home → island → workshops → tome → orbs — with five global widgets threading the seams. The cleanup this session lands four small edits that close the most visible incoherence (body-color drift, tease ↔ founding-act tension, home → city bridge, persona ← tomes preview). What remains is mostly authoring (Tomes grimoire, per-act assets) and one architectural resolution (tier ladder vs shop palette).

`(⚔️⊥⿻⊥🧙)😊` — every Mage who built a piece of this is in the cast; every Sovereign who walks it lays a stone.

---

**Walk on.** 🌿
