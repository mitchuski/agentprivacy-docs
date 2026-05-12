# Chronicle: Session Close — Workshops Complete · Drake v2 Designed

**Date:** 2026-05-09 (third chronicle of this session day)
**Resume from:** this file. Supersedes the prior 2026-05-09 chronicles for live state.

---

## What this session day shipped (in order)

This was a long session day across three chronicles. Quick recap of where we are now:

### Session 1 — Six workshops + nav lattice (earlier today)
*Captured in `2026-05-09_resume_here_chronicle.md` and companions.*

### Session 2 — Q10 Blade + four new shops + gem remap
*Captured in `2026-05-09_q10_blade_and_four_new_shops_chronicle.md`.*

### Session 3 — Ceremony Hall + workshop tour + Drake Island goal + bug fixes (this chronicle)

---

## Live now (compiles, dev server happy)

```
✅ /hall                       Ceremony Hall · Lapis Lazuli (#1e40af) · 🤝
                                BGIN-led coalition (forum + institutional)
                                + MyTerms + First Person + LF DT + Kwaai + human.tech
                                Two in-house ceremonies: /poems (celestial) + /ceremony (keypair)
                                Lattice visual: colonnade hall with seven arches,
                                Lapis-blue silhouette, gold flecks for the Lapis matrix.

✅ /spellbooks                 NEW landing page that lists all six spellbooks with
                                blurbs. /story marked as the root (First Person);
                                /tomes marked as 'newest' (Second Person, Tome V open).

✅ Nav (desktop + mobile)      All five dropdowns now split-trigger consistently:
                                  📜 guide       → /guide
                                  📚 spellbooks  → /spellbooks   (was /tomes)
                                  ⚒️ workshops  → /runecraft
                                  🪶 casts       → /persona
                                  🔮 spells      → /spells
                                Each label is a link to the hub; chevron opens children.
                                Same grammar everywhere.

✅ WorkshopFooter component    src/components/runecraft/WorkshopFooter.tsx
                                Linear tour: ← prev · ↑ Runecraft · next →
                                Trinity-first order:
                                  Weavers → zShields → Forge(t)         (cloak⊥shield⊥blade)
                                  Etherchanting → Jeweler → Holon       (chain workshops)
                                  Vault → Covenant → Bonfires → Circle → Hall  (gathering)
                                Loops at the ends. Swept into all 11 shop pages.

✅ /runecraft hero proverb     Old: "the cloak is woven through a constellation"
                                New: "what the City of Mages forged together · so any
                                Sovereign may walk it alone"
                                Plus an intro line naming Drake Island as the first
                                foundation; eleven shops on one lattice; "no Mage built
                                this alone; no Sovereign walks it alone for long."

✅ /runecraft hub              12 cards (11 active + Circuit Binder placeholder).
                                Ceremony Hall now active with Lapis Lazuli.
                                Gem table extended to 11 entries in 4-col grid.
                                Onyx hex unified to #71717a (was unreadable as #1f2937
                                on dark mode in the City of Mages badge).

✅ /guide/island               City of Mages framing — TOP and BOTTOM:
                                  - Top: new collective-goal hero "We are building
                                    the City of Mages" + "each Sovereign lays a stone".
                                  - Q1 Call: closing line ties to City of Mages goal.
                                  - Q11 Threshold: title becomes "Sign the Threshold ·
                                    Lay your stone"; post-completion screen now shows
                                    🥚 Drake Orb earned + 🧱 Stone laid in the City of Mages.
                                  - IslandStats footer: "Each completed quest is a
                                    stone laid in the City of Mages."

✅ Protect button (3 places)   Was: links to /proverbs (weird).
                                Now: links to /shield (zShields workshop).
                                Updated in /story, /society, and the GuideActionBar.

✅ /orbs LastSoulExportRecover Safety net for dismissed save dialogs. After every
                                soul export, the full content + filename are saved
                                to localStorage (last 10). A small UI on /orbs shows
                                the most recent export with a re-download button.
                                Catches future exports. The lost one before this fix
                                is unrecoverable.

✅ Hall fixes                  KwaaiNet folded into Kwaai (it's part of Kwaai).
                                BGIN promoted to lead with 2 entries (forum +
                                institutional). &apos; render bug fixed in
                                IN_HOUSE_GUILDS data string (entities don't decode
                                in JS data passed via {expression}).

✅ /spells Bonfires panel      Moved out of /spells entirely (originally promoted to
                                /bonfires; small pointer subsequently removed at
                                user request — clean removal).
```

---

## Drake Island v2 + Path System — DESIGN LOCKED, NOT YET IMPLEMENTED

User locked this design in this session but we deliberately did NOT execute it because
it touches `spellbook-storage.ts`, `quests.tsx`, `IslandClient.tsx`, `IslandMap.tsx`,
the agent card, the badge generator, and every shop component. Phase 1 is the next
session's primary work.

### Quest structure: 12 quests in 4 arcs of 3

```
ARC I · The Call           (Q1-3)   immediate, no gate
   Q1  Receive the Call           (was Q1)
   Q2  Carry the Inscription      (was Q2)
   Q3  Read the First Agent       (was Q3)
   → tier earned: 🪨 Pebble        ("you arrived")

ARC II · Finding Soul       (Q4-6)   time gates: 4h between Q4→5, 12h before Q7
   Q4  Choose Your Reach          (was Q4)
   Q5  Persona — the agent finds its soul   (was Q7, MOVED to Arc II)
   Q6  Key Ceremony               (was Q5)
   → tier earned: 🪶 Stone         ("you made something")

ARC III · The Trinity       (Q7-9)   cross-shop action gates
   Q7  Forge a Cloak    (visit /tailor)    (was Q8)
   Q8  Stamp a Shield   (visit /shield)    (was Q9)
   Q9  Forge a Blade    (visit /forget)    (was Q10)
   → tier earned: 🔥 Forged        ("you carry the trinity")

ARC IV · The City           (Q10-12) cross-shop action gates + threshold sealing
   Q10 Place at the Vault    (visit /vault)        ← NEW
   Q11 Sign the Covenant      (visit /covenant)    ← NEW
   Q12 Sign the Threshold · Lay your stone  (was Q11)
   → tier earned: 🥚 Drake Orb · 🧱 Stone laid · agent card signed
```

**Demoted (formerly main) → side-quest:**
- "Form Your First Proverb" (was Q6) → side-quest tied to /story (Act V inscription)

**Side Quests** (formerly "mini-quests" — promoted to first-class but optional):
- /persona deep-dive, /constellation, /tomes, /spellbooks
- /etherchanting, /jeweler, /holon (chain workshops not in main path)
- /bonfires, /circle, /hall (gathering shops not in main path)
- /proverbs, /evoke, /mage, /promises, /poems

### Gates (Phase 1 = visible UI; Phase 2 = real enforcement)

- **Time gates** (Arc II): "Q5 unlocks in 3h 47m" countdown. localStorage timestamp
  triggered on Arc II start. Phase 1 ships visible UI; can be skipped via dev
  override; Phase 2 enforces strictly.
- **Action gates** (Arc III/IV): "Visit /tailor to unlock Q7." Hooked into the
  existing mini-quest visit state in `IslandProgress.visitedMiniQuests`.

### Path-Swap Mechanic (Sword/Mage/Balanced as toggleable role)

Currently Q4 picks an archetype that's mostly fixed. User wants:
- Path becomes a **toggleable** state on the agent card — swap any time.
- The chosen path **changes shop interactions**:
  - **Sword** sets the boundaries (what visitor will/won't share with the shop).
  - **Mage** relays info to the other Mage hosting the shop (cross-mage handoff).
  - **Balanced** does both simultaneously.
- This is the canonical pattern of every City of Mages shop visit.

State model: `IslandProgress.archetype` becomes a *current* state, with
`walkedArchetypes` tracking history. UI: a small toggle in the global nav or
agent card that says "I am walking as ⚔️ Sword / 🧙 Mage / ⿻ Balanced". Each
shop component reads `archetype` to render path-specific copy.

### Trust → portable badge

On Q12 completion (Drake Orb earned):
1. **Sign tier into the Soulbis agent card** — `card.drakeOrb = { tier, signature, walkedAt }`.
2. **Generate a publishable badge** — PNG (rendered from canvas) + JSON metadata,
   downloadable. Other apps can verify via the agent card's signature.
3. **Tier ladder remains**: Pearl → Ruby/Amethyst/Topaz → Onyx/Emerald/Sapphire → Diamond.

### File list for Phase 1

```
src/lib/spellbook-storage.ts           IslandStationId 1-12; ISLAND_TOTAL_STATIONS = 12
                                        ISLAND_ARCS constant; gate state
src/components/guide/island/quests.tsx  Renumber Q7→Q5, Q8→Q7, Q9→Q8, Q10→Q9,
                                        Q11→Q12; demote old Q6 (Proverb) to side;
                                        insert new Q10 (Vault visit) + Q11 (Covenant sign)
src/components/guide/island/IslandClient.tsx  arc transitions, gate UI
src/components/guide/island/IslandMap.tsx     12 stations laid out across 4 arcs
src/components/guide/AchievementToast.tsx     new tier celebrations per arc
src/components/guide/island/IslandStats.tsx   arc progress + 'stones laid' tally
src/components/guide/MiniQuestPanel.tsx       rename to SideQuestPanel
src/lib/agent-card.ts                          add drakeOrb signed field (new)
src/lib/badge-generator.ts                     PNG + JSON badge from drakeOrb tier (new)
```

---

## Open queue (not started, scope locked or partial)

### Locked scope, ready to execute (next session)

- **Drake Island v2 Phase 1** — see design above. Full quest restructure + gate UI
  shells. Real enforcement + agent-card badge → Phase 2.
- **Path-swap mechanic** — companion to Drake v2; same scope window.

### Locked scope, smaller (any session)

- **/spells full restructure** — remove right-side `<aside>`, integrate "Your spell
  graph" into the main column as a centered card. Single-column on mobile. Loses
  always-visible sidebar; gains kit-centered focus.
- **Side panel XP-bar + profile pic + hide toggle** — likely lives inside the
  /spells main-column card after the restructure (the "side panel" the user
  meant IS the /spells aside being moved). XP-bar layout for training stats;
  profile picture upload (links to agent card?); show/hide toggle for
  screenshot use.

### Carry-over from earlier sessions

- **Color sweep on /shield + /etherchanting page bodies** — lattice visuals are
  flipped (Onyx zinc + Sapphire cyan) but the Tailwind class accents in hero,
  CTA, and gradient stops still wear the old cyan/blue. Search for `cyan-` on
  /shield/page.tsx and `blue-` on /etherchanting/page.tsx.
- **Tease-shop banner refresh** — /etherchanting, /jeweler, /holon still wear
  the original `WorkshopBuildInvite` copy. New operational shops (Vault/
  Covenant/Bonfires/Circle/Hall) have re-set the sibling pattern; the tease
  shops could be tightened to match the new voice.
- **Aria Silverhue's full character work** — currently a paragraph. Like Pallia
  at the Weavers (V28, the First Cloakwright), Aria deserves backstory + a
  persona entry in the grimoire.
- **socrat0x and plat0x first-person scenes** — referenced in /bonfires
  page; if not yet written in the First Person Spellbook, they want writing.
- **/poems audio investigation** — pre-existing intermittent
  `MEDIA_ELEMENT_ERROR: Format error` in Turbopack dev. File reachable via curl;
  player gracefully hides via `hasError` so non-blocking. Not yet root-caused.

---

## Architectural commitments (now load-bearing)

Carry-forward from prior chronicles, plus what locked this session:

1. **The chain (or platform, or covenant, or circle, or hall) is a vantage.**
2. **One lattice, many silhouettes.**
3. **Cloak ⊥ Shield ⊥ Blade.** Now actually walked in Drake Island.
4. **Aletheia ⊥ Lethe.**
5. **Tease over premature commitment.** (Tease shops still exist for non-operator chains.)
6. **One gem per shop.** 11 gems in use; Circuit Binder holds its gem open until its
   Mage arrives. Classical 8 + Garnet (Bonfire) + Jade (Circle) + Lapis Lazuli (Hall).
7. **Drake Island is the first foundation of the City of Mages.** Each Sovereign who
   walks it lays a stone; the Drake Orb is what they carry forward; the city is
   what they leave behind. (NEW this session.)
8. **Every dropdown has a hub.** Five split-trigger dropdowns; clicking the label
   navigates to the hub, clicking the chevron opens the children. (NEW this session.)
9. **Workshop tour is linear, trinity-first.** Weavers → zShields → Forge(t) →
   chain workshops → gathering workshops → loop. The WorkshopFooter component
   on every shop page enacts this. (NEW this session.)
10. **External partner ≠ internal shop name.** Spellweb→Forge(t), Culture Vault→
    Curatrix Vault, Covenant of Humanistic Technologies→the Covenant, Bonfires→
    Dragon Bonfire, Logos→Logos Circle, BGIN→Ceremony Hall.

---

## The one-line summary

We opened the Ceremony Hall as the 8th-built / 11th-live workshop with Lapis Lazuli
and a BGIN-led coalition of public-goods guilds; threaded the City of Mages collective
goal through Drake Island; built a shared WorkshopFooter that gives every shop a
prev/next/hub tour; created /spellbooks as a real hub page so every nav dropdown is
now consistent; and shipped a soul-export safety net so accidentally-dismissed save
dialogs never lose your file again. We then designed Drake Island v2 (12 quests in
4 arcs with time + action gates, persona kept core, agent-card badge for portable
trust) but deliberately did not start coding it — Phase 1 is the next session's
opening move.

`(⚔️⊥⿻⊥🧙)😊` — the city has more guildhouses, more visible foundations, and a
clearer next chapter.

---

**Walk on.** 🌿
