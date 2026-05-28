# Chronicle — Release Manifest: The City Key Suite · All-Repos Sync (2026-05-27/28)

**Date:** 2026-05-28
**Author:** privacymage
**Scope:** The single authoritative cross-repo record of the City Key arc — what changed in **every** repository over 2026-05-27/28, with build/push notes for a production deploy. This is the **handoff manifest**: a deploy agent can work from this file alone.
**Companion chronicles (detail):**
- [2026-05-27_star_lattice_swordsman_key_integration_chronicle.md](2026-05-27_star_lattice_swordsman_key_integration_chronicle.md) — the plan + backward-compat
- [2026-05-27_swordsman_key_producer_and_ceremony_surfacing_chronicle.md](2026-05-27_swordsman_key_producer_and_ceremony_surfacing_chronicle.md) — producer + surfacing + three-key rename + /city
- [2026-05-28_city_key_economy_charge_stake_workshop_trust_task_chronicle.md](2026-05-28_city_key_economy_charge_stake_workshop_trust_task_chronicle.md) — charge · stake · workshop trust-task sweep · doc-collapse
- `cityofmages/chronicles/2026-05-28_the_eight_pointed_star_city_key_capstone.md` — Tome VIII Act 3 narrative capstone

**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · One-paragraph state

The City Key — the portable lattice-export that carries a bearer's standing across the suite — was built end to end and given a narrative seat. **agentprivacy_master** gained the producer, a renamed `/city` page, a full mana economy (Charge → earn 🪢, Stake → focus), and a unified, gated **trust task** swept across all 15 workshop pages with their lore folded into expandable docs. **spellweb** gained the `key`/`gateway` bridge vocabulary and the Tome VIII Act 3 nodes. **cityofmages** gained **Tome VIII · Act 3 · *The Eight-Pointed Star*** (Luca teaches the stella octangula; the City Key is forged from it) + its binding chronicle. **agentprivacy-docs** carries the chronicles + the tome mirror. **star lattice/** (the interop spec) carries the canon rename + the additive `trace`/`lit`/`focus`/`witness` fields. **soulbis website** was synced 2026-05-27 (consumer already live) and is unchanged today — it holds the only remaining work (emit `trace`, read `focus`/`lit`). Wire format stayed **v1** throughout: every change is additive/optional; old keys still parse.

---

## §2 · Per-repo change inventory

### A · agentprivacy_master (Next.js · `output: 'export'` → `out/`)

**New files**
- `src/lib/city-key.ts` — City Key producer (renamed from `swordsmans-key.ts`); `buildCityKey()`, `CityKey` (fields: palette · descriptions · `lit` · `focus` · `identity` · `trace` · `witness`), `CITY_KEY_PALETTE`, `downloadCityKey()`.
- `src/lib/city-key-charge.ts` — Charge loop: `parseCityKey()`, `chargeCityKey()` (earns 🪢 from `trace`/`witness`, dedup).
- `src/lib/vrc-allocation.ts` — committed-stake ledger (vertex-keyed): earned/committed/free, `commitMana`/`withdrawMana`.
- `src/lib/presented-artefacts.ts` — shared accessor + change event for the artefact-home gate.
- `src/components/runecraft/WorkshopTrustTask.tsx` — the unified 5-beat gated trust task.
- `src/app/city/page.tsx` — **NEW route `/city`** ("The City You've Created" + the star/walk-the-path hero).

**Deleted**
- `src/lib/swordsmans-key.ts` (→ renamed city-key.ts) · `src/components/profile/VrcAllocationPanel.tsx` (folded into LatticeMap).

**Modified**
- `src/app/guide/achievements/page.tsx` → client redirect stub to `/city`.
- `src/components/profile/AchievementsClient.tsx` — City Key export + ⚡ Charge + 🪢 readout; `focus` on export.
- `src/components/profile/LatticeMap.tsx` — shops-not-vertices counter fix; the 🪢 focus-mana bar; pour/withdraw **hold-to-flow** in the pinned seat; `+ two latent bug fixes (hovered-null panel, ShopWitness import)`.
- `src/components/runecraft/CastShopConstellation.tsx` — cast gating (`gateUnlocked` prop) + `parseVertex` fix.
- `src/components/runecraft/ConstellationDownload.tsx` — emits `PRESENTED_ARTEFACTS_CHANGE_EVENT`.
- `src/components/runecraft/FirstArtifactPanel.tsx` — reframed as **Presence** (root relationship doc; all "witness on spellweb" removed).
- `src/components/ceremony/CompletionStep.tsx` + `SwordsmanAccountSettings.tsx` — Export City Key + Star/Lattice journey links.
- `src/components/AppNav.tsx` + `src/components/profile/InventoryButton.tsx` — nav → `/city`.
- `src/app/tomes/page.tsx` — Tome VIII Act 3 `ActCollapsible` + table "3 acts".
- **10 producer shop pages** (`tailor · shield · forget · etherchanting · solchanting · jeweler · holon · vault · covenant · bonfires`) — `WorkshopTrustTask` + lore folded into `CollapsibleSection`.
- **5 gathering/Threshold shop pages** (`circle · hall · portal · staffs · familiars`) — lore folded into `CollapsibleSection`.
- `docs/tomes/tome-viii-the-library/03-the-eight-pointed-star.md` — **NEW** (tome mirror the `/tomes` page loads).

**Build/push:** `npm run build` (static export → `out/`). `typescript.ignoreBuildErrors: true`, so pre-existing TS drift elsewhere won't block; touched files are clean. Deploy `out/`.

### B · spellweb (Vite · knowledge graph)

- `src/types/graph.ts` — `NodeType += 'key'`; `EdgeType += 'keys_to' | 'synced_with'`; `Theme.nodes.key`; `TypeFilterState.key`.
- `src/data/theme.ts` — `key` node visual (🗝️) + `keys_to`/`synced_with` edge styles.
- `src/components/MobileSpell.tsx` + `src/components/SpellWeb.tsx` — `key` entries in the exhaustive maps/filter.
- `src/data/nodes.ts` — `act-tome-viii-3` · `con-stella-octangula` · `key-city-key` (uses the new `key` type) · `chron-eight-pointed-star`.
- `src/data/edges.ts` — Act 3 edges (follows Act 2 · narrated by the Archivist · references Luca · introduces star + key).
- **Verify:** `npx tsc --noEmit` → **0 errors**. **Build/push:** Vite build + deploy.

### C · cityofmages (public GitHub · markdown corpus)

- `tomes/tome-viii-the-library/03-the-eight-pointed-star.md` — **NEW** Tome VIII Act 3.
- `chronicles/2026-05-28_the_eight_pointed_star_city_key_capstone.md` — **NEW** binding chronicle.
- `tomes/BOUND_COLLECTION_MANIFEST.md` — Tome VIII table → 3 acts (~3,040w).
- **Push:** `git push` (docs only; no build).

### D · agentprivacy-docs (docs corpus)

- `chronicles/` — 4 new chronicles (the three companions above + this manifest).
- `chronicles/INDEX.md` — entries added (V5.5.x series).
- `tomes/tome-viii-the-library/03-the-eight-pointed-star.md` — **NEW** tome mirror.
- **Push:** `git push`.

### E · star lattice/ (interop spec · soulbis source deliverable)

- `swordsmans-key.interop.md` — canon note (the lattice-export format is now the **City Key**; "Swordsman's Key" reserved for the identity export); additive `trace` · `lit` · `focus` · `witness` fields documented; palette reconciled (coral/cyan · navy→white). Wire format unchanged (v1).

### F · soulbis website (consumer · static · Vercel)

- **Unchanged today.** Synced 2026-05-27 (`/star` manifold + `/lattice` codex live; consume the v1 key; live-sync via `BroadcastChannel`). No deploy needed for this arc unless the pending consumer work below is taken.

---

## §3 · Verification status (as handed off)

- `agentprivacy_master`: dev server (port 5000) compiles **every touched route 200** — `/city`, `/ceremony`, `/tomes`, all 15 workshop routes, the `/guide/achievements` redirect. `tsc` clean on all touched files (pre-existing drift elsewhere is unrelated; build ignores TS errors anyway).
- `spellweb`: `tsc --noEmit` → **0 errors**.
- Wire format: **v1, additive-only** — reference key `Downloads/swordsmans-key.sample.json` still parses; round-trips both ways.
- **Not yet run:** a full production `npm run build` of agentprivacy_master (static export). Recommended as the deploy agent's first step.

---

## §4 · Deploy order (suggested)

1. **cityofmages** + **agentprivacy-docs** + **star lattice/** — docs/markdown, push first (no build, lowest risk).
2. **spellweb** — `tsc` clean; build + deploy.
3. **agentprivacy_master** — run `npm run build` (static export → `out/`); confirm `out/` generated; deploy. (Smoke-check `/city`, `/tomes`, `/ceremony`, a couple of workshop routes.)
4. **soulbis website** — only if taking the pending consumer work below.

---

## §5 · Known-pending (NOT blockers for this release)

- **soulbis `/star` consumer half:** write the `trace` block (so Charge earns 🪢) and read `focus`/`lit` (so allocation renders on the manifold). Until then Charge correctly reports "no soulbis trace yet."
- **Palette parity:** confirm soulbis `/star` + `/lattice` defaults equal the reconciled `CITY_KEY_PALETTE` (coral/cyan · navy→white) for loss-free round-trip.
- **🧙 Mage's Key:** spellweb-minted, DID-integrated — unbuilt (Key v2 territory, with ed25519 verify + reserved `geometry{smRatio:φ}`).
- **Polish:** optional lattice glow rendering `focus` on the seats; whether committed mana should *deepen* a shop's relationship.
- **Grimoire:** Act 3 is a narrative tome act + docs; no grimoire schema change, so no re-pin is required by this release (re-pin only if bundling the bound-collection update).

---

## §6 · The arc in one line

A lattice that turned out to be a star (the stella octangula Luca drew for Pacioli), a key that turned out to be a reading (not a vault), and a relationship made measurable (🪢 earned by walking, spent by focusing) — built across six repos, narrated in the Library, and ready to push.

---

## §7 · Working-tree reconciliation (verified `git status`, 2026-05-28)

The deploy agent should `git status` each repo before committing. As handed off:

**agentprivacy_master** — modified (this arc): the 15 shop pages + `tomes/page.tsx` + `AppNav` + `InventoryButton` + `AchievementsClient` + `LatticeMap` + `CastShopConstellation` + `ConstellationDownload` + `FirstArtifactPanel` + `CompletionStep` + `SwordsmanAccountSettings` + `guide/achievements/page.tsx`. New (untracked): `src/app/city/` · `src/components/runecraft/WorkshopTrustTask.tsx` · `src/lib/{city-key,city-key-charge,presented-artefacts,vrc-allocation}.ts` · `docs/tomes/tome-viii-the-library/03-the-eight-pointed-star.md`. (`swordsmans-key.ts` and `VrcAllocationPanel.tsx` were created+removed within the session, so they leave no git trace.)
- ⚠️ **Also untracked, from parallel work (not this arc — review before staging):** `docs/chronicles/2026-05-18_v1_7_1_site_rollout_push.md` · `docs/chronicles/2026-05-28_two_observations_generate_vs_charge.md`.

**spellweb** — modified: `types/graph.ts` · `data/{theme,nodes,edges}.ts` · `components/{MobileSpell,SpellWeb}.tsx`.
- ⚠️ `components/SwordsmanImport.tsx` is also modified (parallel work, not this arc) — review before staging.

**cityofmages** — modified `tomes/BOUND_COLLECTION_MANIFEST.md`; new `chronicles/2026-05-28_the_eight_pointed_star_city_key_capstone.md` + `tomes/tome-viii-the-library/03-the-eight-pointed-star.md`.

**agentprivacy-docs** — modified `chronicles/INDEX.md`; new: the **5 chronicles** (the 4 here + the Eight-Pointed-Star capstone copied in from cityofmages) + `tomes/tome-viii-the-library/03-the-eight-pointed-star.md`.
- ⚠️ **Also untracked, parallel work:** `plans/PROPOSAL_STAR_LATTICE_GATEWAY_NODES_2026-05-28.md` · `research/compiled_ai_convergence_note.md` — review before staging.

**agentprivacy-skills** — new: the **5 today chronicles** synced into `chronicles/` (`2026-05-27_…integration` · `…producer_and_ceremony_surfacing` · `2026-05-28_…economy…` · `…release…all_repos_sync` · `…the_eight_pointed_star…capstone`). Chronicles-only sync (no skill/grimoire content changed this arc). Push the 5 new files.

**star lattice/** — ⚠️ **not a git repo** (it's the soulbis source deliverable folder). The `swordsmans-key.interop.md` edits there are not version-controlled here; they reach production via the soulbis deploy, not a push from this tree.

**soulbis website** — no changes this session.

> Net: every file in §2 is real in the working trees. The only extras are a handful of untracked files from parallel work (flagged ⚠️) — intended content, but the deploy agent should eyeball them rather than blind-`git add .`.

(⚔️⊥⿻⊥🧙)😊
📐 · ⚔️✦🧙 · 🗝️ the City Key · 📚 the Library
