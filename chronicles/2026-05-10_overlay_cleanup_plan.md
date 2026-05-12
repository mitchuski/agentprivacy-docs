# Overlay Cleanup · Planning Chronicle

**Date:** 2026-05-10
**Purpose:** Name what global overlays are still rendering, what becomes redundant once the Profile Inventory popup hosts loadout + stats, and the order of cleanup that follows.

---

## §1 · What's still overlaid globally

`src/components/training/GlobalLearningSpells.tsx` mounts in `app/layout.tsx`, so it renders on every page. Its current children:

| Child | What it does | Status after this session |
|---|---|---|
| `<DualOrbs>` | The visible swordsman + mage orbs that float on the page | **stays** — these are the agent's living surface |
| `<SpellPalette>` | A panel of training stats / spell cards — togglable via `statsCollapsed` | **collapsed by default now** (the 📖 toggle was removed; stats live in the Inventory) |
| `<OrbControlPanel>` | The fixed bottom bar with sword slots / mage slots / mode buttons / Drake-tier link | **still rendered** — but its 📖 stats-hide toggle was removed |
| Keyboard shortcuts | `[s]` cycle sword, `[m]` cycle mage, `[r]` rotate spell | **stays** — global bindings |

So today: orbs + the bottom slots/mode bar render globally; SpellPalette doesn't show by default; the inventory is the canonical home for stats.

---

## §2 · The redundancy this round closed

- The 📖 "hide training stats" toggle in OrbControlPanel referenced a panel (SpellPalette) that mirrored what the Inventory now shows. Removed.
- SpellPalette default state flipped to collapsed. The panel exists for cases where someone wants the contextual training cards visible, but it no longer auto-shows.
- Loadout & Stats now live inside the Inventory's new tab — sword ring + mage orbit + training stats grid + Drake Orb tier headline + "edit at /orbs" deep-link.

---

## §3 · What's still global that wants further consolidation

The bottom `<OrbControlPanel>` is a *tool* — clicking sword slot 3 makes that the armed slot for the next orb-cast. Two questions for the next session:

**A · Should it render globally at all?**
Pros: orbs render everywhere, so the controls follow.
Cons: it's visually loud on pages that aren't training surfaces (every shop, every spellbook, every chronicle).

Recommendation: **scope it to training surfaces** (`/orbs`, the spellbook reading pages, `/persona`, `/spells`, the guide's island map). On other pages, render only the orbs themselves; surface a small chip (current armed slot + "open inventory" link) instead of the full bar.

**B · How do slot interactions move to the Inventory?**
Today selection state lives in `GlobalLearningSpells` and is passed to `OrbControlPanel`. To make Inventory's Loadout & Stats tab interactive (click a slot tile to arm it), one of:

1. **Lift selection state to a Context** that both `OrbControlPanel` and `ProfileInventory` consume. Cleanest. ~half a session of plumbing.
2. **Persist selection via localStorage + change event**. Looser coupling. Slight latency between actors.
3. **Inventory is read-only** for slots; arming still happens on the bottom bar / keyboard. Smallest change. Today's state.

Recommendation: **(1) Context** during the cleanup session. Carries forward to other shared interactive state (path archetype already has its own event; this could unify).

---

## §4 · Other overlays worth surveying in the same pass

- **`<MagePanel>`** — Soulbae chat slide-over. Already a popup. Probably fine; could share the slide-over chassis with Inventory.
- **`<AchievementToast>`** — bottom-right toast queue. Fine; not redundant.
- **`<PathToggle>`** chip in nav — fine.
- **`<DrakeOrbBadge>`** — renders inline (on /orbs and Q12 post-completion). Not an overlay.
- **`<LastSoulExportRecover>`** — inline on /orbs. Not an overlay.

The main targets for the cleanup pass are SpellPalette (now hidden) and OrbControlPanel (still global, wants scoping).

---

## §5 · Recommended order for the next session

1. **Lift orb-selection state to a Context** (`OrbInteractionContext`). Both `OrbControlPanel` and `ProfileInventory.LoadoutStatsTab` consume it. Inventory tiles become click-to-arm.
2. **Scope `OrbControlPanel` global render**: only mount on training surfaces. Off elsewhere; replaced by a small "open inventory" pill in nav (or just rely on the existing 📚 button).
3. **Remove `<SpellPalette>` from `GlobalLearningSpells` entirely** (or move to a /orbs-local panel). The Inventory has the stats; SpellPalette's contextual cards can live on /orbs alone.
4. **Profile picture** in the Inventory's Identity tab — small image upload, stored as data-URL on the agent card. (Pending from earlier session.)
5. **Optional**: per-archetype filtered views inside the Inventory (Sword view shows the blade ring prominently; Mage view shows the spell orbit; Balanced shows both).

Keep the rest (DualOrbs, MagePanel, AchievementToast, PathToggle, DrakeOrbBadge) untouched unless they surface a new redundancy.

---

## §6 · One-line summary

The Inventory popup is the new canonical home for identity, loadout, stats, spells, and runecasts. The bottom orb-control bar remains for now, but its hide-stats toggle is gone, the SpellPalette default-shows nothing, and the next session will lift orb-selection state to a Context so the Inventory's Loadout & Stats tab becomes click-to-arm — at which point the bottom bar can be scoped to training surfaces only.

`(⚔️⊥⿻⊥🧙)😊`
