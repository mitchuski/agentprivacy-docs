# Next Steps · Gaps · Where the Thinking Pauses

**Date:** 2026-05-10
**Companion to:** `2026-05-10_what_shipped_this_arc_chronicle.md`
**Purpose:** Capture what's next, what's missing, and where the user paused to think — so the work picks up cleanly without re-deriving direction.

---

## §1 · The "different interaction" you flagged for the cast constellation

You said: *"the cast constellation kinda is fun, but we will be having a different interaction."*

The v1 we shipped is a **6-cell dimension cascade** that lights Memory · Connection · Computation (or whichever bits the Mage's vertex carries) in sequence on click, then commits a witness record. It's playful but it's a single button → one short animation → counter goes up. Trust accumulates by tap count. That's not what's wanted longer-term.

What's not yet articulated (and what to think about during the pause):

- **Is it interactive trace-walking?** The Sovereign physically traces the path through the lattice (drag, click vertex by vertex, swipe) rather than watching a cascade.
- **Is it a spellweb handshake?** The cast hits a real spellweb endpoint per Mage; the trace is computed remotely and witnessed back in the shop. The "bouncing between" you described becomes literal traffic.
- **Is it bilateral?** Two Sovereigns evoke the same constellation simultaneously and the witness belongs to the pair, not the individual. Trust accrues to the relationship rather than the visit count.
- **Is it temporal?** The cast holds — you have to dwell on each vertex for a beat (mirroring the keypair-ceremony pacing) before the trace completes. Trust is patience.
- **Is it composable?** Multiple Mages' constellations can be cast in series and a cross-Mage proof emerges from the combined trace.

The v1 component (`src/components/runecraft/CastShopConstellation.tsx`) is structured so the **storage**, **trace data**, and **witness signature** stay correct under any of these interaction models. What changes is the visual + the input. So the next session can keep `shop-witnesses.ts` + `lattice-vertex.ts` + the per-shop placement and rebuild the interactive surface.

**Recommendation when you return:** decide which of the five framings (or a sixth) fits the architecture's coordination story, then rebuild the visual + input. The witness ledger and per-shop placement don't need to change.

---

## §2 · Gaps in the cast-constellation v1 (worth naming)

- **No spellweb handshake.** The component frames the spellweb mirror as Phase 2; the actual mirror doesn't exist yet because per-Mage spellweb templates aren't set up. Today's witness is local-only.
- **Animation is uniform across all shops.** Each Mage walks the same dimension-cascade pattern; the visual doesn't yet express what makes Vulcana's blade different from Pallia's beyond the bits that light up.
- **Witness has no recipient.** A real witness has a witnesser. Today's witness is the Sovereign's local localStorage record of having pressed the button. There's no peer, no shop-side acknowledgement, no chain anchor.
- **No re-cast cooldown / pacing.** You can cast 100 times in 30 seconds and rack up 100 witnesses. Trust shouldn't be that easy to manufacture.
- **No cross-shop composition.** Each shop's constellation stands alone. The lattice's whole point is that vertices compose; the witnesses don't yet.
- **No export of the constellation cast itself.** Drake Orb has a publishable PNG + JSON; the constellations don't.

---

## §3 · Other open work in priority order

### §3.1 · Tomes grimoire authoring (highest leverage)

Per the 2026-05-09 sync report, this is the most-leveraged pending piece. Status: **not started**.

- Author the `tomes` grimoire JSON: ~27 spells × 9 personas (3 spells per Mage × the 9 founding-act Mages)
- Pin to IPFS via the existing `sync.agentprivacy.ai/ipfs/...` infrastructure
- Export `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` from `src/lib/grimoire-ipfs.ts`
- Bake into `src/lib/grimoire-baked.ts` with a new `SpellbookSource` value (e.g. `'tomes'`)
- Add `TOMES_ACT_PERSONA_HINTS` mapping each act to its persona
- /persona's persona filter list extends to include the Tomes tier
- Estimated: ~2 sessions of authoring + one of integration

The starter templates already authored in `src/lib/tome-v-acts.ts` are a head-start on the spell vocabulary — the spell names there (weave-cloak · publish-role · conceal-name · …) become the spell IDs in the grimoire.

### §3.2 · Drake Island Phase 3 — real gate enforcement

Phase 1 (visible-but-skippable gates) is live. Phase 3 makes the time gates and action gates **actually block** progression.

- Enforce Q5 Persona time-gate (4h after Q4 Reach)
- Enforce Q6 Ceremony time-gate (12h after Q5)
- Enforce Q7-Q12 cross-shop action gates (require `visitedMiniQuests` to include the right route)
- Drake Orb signature upgrade from content-hash (`simpleContentHash`) to ed25519 against the agent card keypair
- Storage already has `getStationLockStatus`; just needs `IslandClient` to switch from "show banner" to "block".

### §3.3 · Drake Island Q copy quotes Tome V proverbs

Small, lovely. Each Drake Island Q (especially Q7 Cloak, Q8 Shield, Q9 Blade, Q10 Vault, Q11 Covenant, Q12 Threshold) maps 1:1 to a Tome V act. Quoting the act's proverb in the quest intro makes the bidirectional anchor visible **during** the journey, not just on the shop page after.

Data is already in `tome-v-acts.ts`; just needs quest copy edits in `quests.tsx`.

### §3.4 · Overlay cleanup pass (planned in 2026-05-09 chronicle)

The 2026-05-09 overlay-cleanup-plan chronicle named this work. Today's state:
- 📖 stats-hide toggle removed from `OrbControlPanel` (done)
- `SpellPalette` defaults to collapsed (done)
- **Still pending:** lift orb-selection state to a Context so Inventory tiles become click-to-arm (now applies to /guide/achievements §3 tiles)
- **Still pending:** scope `OrbControlPanel` global render to training surfaces only (/orbs, /persona, /spells, /guide/island)
- **Still pending:** remove `SpellPalette` from `GlobalLearningSpells` entirely

### §3.5 · Tier-ladder vs shop-palette gem-name overlap (architectural)

The Drake Orb tier ladder uses gem names (Pearl · Onyx · Diamond · etc.) that ALSO name workshops. Three resolutions sketched in the 2026-05-09 coherence chronicle §3.5:
- (a) Rename tier-ladder to non-gem labels (Drake/Forged/Tempered/Dragon)
- (b) Prefix-distinguish "tier-Pearl" from "shop-Pearl"
- (c) Accept the duality and document the rule

Pick one in a dedicated architectural session.

### §3.6 · Per-act assets

Cover plates on `/tomes` use gem-coloured gradient placeholders with the Mage's sigil. Real cover images per act (and optionally story videos) are open-ended contribution work.

### §3.7 · Substantial visuals (Phase F per the sync report)

- `City of Mages map` — static SVG v1 with the trade quarters + bonfire + temple + sovereign's seat
- `Lattice render` — the 64-vertex Hamming graph with the 13 inhabited vertices labelled (Christian's V19/V25/V49/V51/V57/V63 attribution travels via `specs/04-vertex-naming-audit.md`)
- `/tomes/cast` dedicated page — sigil grid with per-member sub-pages

Substantial design + implementation. Dedicated session each.

### §3.8 · Smaller carry-overs

- **/poems audio** — `MEDIA_ELEMENT_ERROR: Format error` on localhost; cloud file is reachable via curl. Likely Turbopack dev / range-request quirk. Not yet root-caused. Player gracefully hides on error.
- **`ProfileInventory.tsx`** — popup version no longer wired; can be deleted in a cleanup pass
- **`StickyPathBar.tsx`** — replaced by `WalkPathExpander`; can be deleted in a cleanup pass
- **Profile picture upgrade** — currently 192² JPEG data URL on localStorage; could use a content-addressed store + IPFS pin for portability

---

## §4 · Gaps in the architecture that aren't bugs

These aren't tasks; they're things to keep in mind when the design moves forward.

### §4.1 · The witness has no recipient

Today every "witness" event in the codebase (constellation cast, Drake Orb signing, runecast saving) is self-witnessing — the Sovereign records that they did the thing in their own localStorage. The architecture's deeper claim is that a witness needs a *witnesser*. The cast-constellation rework is the natural place to introduce a real second party (peer, shop-side endpoint, or chain anchor).

### §4.2 · Trust accrues to taps, not to acts

A counter that goes up by 1 per click rewards repetition, not commitment. The runecasts library doesn't have this problem (each runecast is a saved artifact); the constellation casts do. The cooldown/pacing/two-party question in §1 above is how to fix this.

### §4.3 · The Mages don't yet differ on the spellweb side

Pallia's spellweb template doesn't exist. Memora's doesn't. Vulcana's doesn't. The agentprivacy site treats each Mage as distinct (gem, sigil, vertex, founding act, spells, starter templates) but the spellweb has no per-Mage runtime to handshake with. Until that exists, the "bouncing between" remains rhetorical.

### §4.4 · The achievements page is the account, but it's not the agent

`/guide/achievements` shows everything *about* the Sovereign but it doesn't *act*. The Soulbis chat panel (`<MagePanel>`) is closer to an agent surface but it's a different conversation. Worth thinking about whether the "your account" page should be more agentic (chat, propose actions) or stay as a clean dashboard.

### §4.5 · The Hall's open invitation isn't yet a flow

The Ceremony Hall has an "open invitation · become a guild in residence" banner pointing to telegram + email. There's no in-page flow for a new guild to introduce itself, no `/hall/apply` form, no triage. Today: someone reaches out via the listed channels and it gets handled manually. Worth thinking about whether a lightweight intake flow makes sense.

---

## §5 · Recommended order when you return

Suggested but not committed; you'll know better after the pause.

1. **Decide the cast-constellation interaction model** (§1) — design call before rebuild
2. **Phase D · Tomes grimoire** (§3.1) — highest leverage
3. **Drake Island Q copy quotes Tome V proverbs** (§3.3) — small, satisfying, completes the bidirectional anchor inside the journey
4. **Drake Island Phase 3 enforcement + ed25519 signing** (§3.2) — substantial but the data layer is ready
5. **Overlay cleanup pass** (§3.4) — cleans the page-level noise
6. **Tier-ladder vs shop-palette resolution** (§3.5) — architectural session
7. **City of Mages map + lattice render** (§3.7) — substantial visual session

Phase E (per-act assets · §3.6) can land any time as contributions arrive.

---

## §6 · One-line summary

The cast-constellation v1 is a fun click-to-cascade with local witnesses, but the next interaction model is open — pick one of the five framings (or a sixth) when you return. Beyond that, Phase D (Tomes grimoire) is the highest-leverage pending work, with Drake Island Phase 3 + the architectural tier-ladder resolution waiting in the wings.

`(⚔️⊥⿻⊥🧙)😊` — pause well; the work holds.
