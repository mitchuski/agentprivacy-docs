# Chronicle — The City Key Economy: Charge, Stake, and the Workshop Trust Task

**Date:** 2026-05-28 (arc spans 2026-05-27 → 2026-05-28)
**Author:** privacymage
**Spellbook:** First Person (agentprivacy) ⊥ Soulbis (Swordsman keyring)
**Scope:** The arc that turned the City Key from a one-way export into a **round-trip economy** and reframed the workshop pages around a single ordered **trust task**. Covers: the canonical three-key model, the Charge loop (earning 🪢 VRC from soulbis runtime), VRC committed-staking (focus distribution), the Presence-vs-Artefact ontology, and the `WorkshopTrustTask` unification (design + status).
**Reference spec:** `star lattice/swordsmans-key.interop.md` (City Key wire format v1)
**Companion chronicles:**
- [2026-05-27_star_lattice_swordsman_key_integration_chronicle.md](2026-05-27_star_lattice_swordsman_key_integration_chronicle.md) (the plan + backward-compat)
- [2026-05-27_swordsman_key_producer_and_ceremony_surfacing_chronicle.md](2026-05-27_swordsman_key_producer_and_ceremony_surfacing_chronicle.md) (producer build · ceremony surfacing · §9 three-key rename · §10 /city rename)

**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · One-paragraph state

The City Key is now the centre of a closed mana loop. The bearer **exports** the 🗝️ City Key from `/city` (the renamed `/guide/achievements`), **walks the key path** on `soulbis.com/star` (which accrues a `trace` runtime), **charges** the returned key on `/city` to **earn 🪢 VRC mana**, then **commits** that mana into shops on the lattice to declare where their agents are focused — a distribution the City Key carries back out as `focus`. In parallel, each workshop page is being reframed around one ordered **trust task** whose ontology the user fixed: **Presence** (a root relationship document) is distinct from the **Artefact** (the trust-task flow), and Presence is the root that unlocks the task. The earning/charging/staking economy is shipped on the agentprivacy side; the `WorkshopTrustTask` wrapper that makes the per-shop task legible is designed and part-scaffolded.

---

## §2 · The three-key model (canonical)

Layered by where each key is minted and what it carries:

| Key | Minted on | Carries | → Destination | Status |
|---|---|---|---|---|
| **⚔️ Swordsman's Key** | agentprivacy `/ceremony` | ed25519 **identity** | spellweb (anchors blades) | shipped |
| **🧙 Mage's Key** | spellweb | DID-integrated credential | spellweb-internal | **future · unbuilt** |
| **🗝️ City Key** | agentprivacy `/city §2` | the **lattice** (palette · 64 descriptions · identity stamp · `lit` · `trace` · `focus`) | soulbis `/star` + `/lattice` | shipped |

The lattice-export format (historically "Swordsman's Key" in the interop spec) was renamed the **City Key**; "Swordsman's Key" is reserved for the identity export. Wire format stayed **v1** throughout — every change has been additive/optional, so old keys still parse.

---

## §3 · The City Key loop (earn)

```
/city: Export City Key → soulbis /star: walk the key path (accrues `trace`)
   → /city: ⚡ Charge City Key → reads soulbis runtime → earns 🪢 VRC mana
```

- **`lib/city-key-charge.ts`** — `parseCityKey()` + `chargeCityKey()`. Reads the key's `trace` (`{ laps, seconds, tourSeconds, savedAt }`), awards VRC via `addVrcMana()`, **dedups by `trace.savedAt`** (a given walk charges once). Award = **1 🪢 per succ lap (min 1) + 2 for a completed key-tour**. Keeps a charge ledger so the soulbis runtime behind a bearer's VRC stays inspectable.
- **`/city` headline block** — **⚡ Charge City Key** (file import) beside **🗝️ Export City Key**, a live **🪢 N VRC** readout, and status copy (`+5 🪢 charged from 4 laps + key-tour`, `already charged`, `no soulbis trace yet`).
- `CityKey.trace` added to the type (additive v1).

---

## §4 · VRC staking (commit · focus)

The active verb on top of accrual: distribute earned mana into shops. **Committed-stake** model (user's call), reconciled with the monotonic-earned canon:

```
earned    = getVrcMana()          · cumulative, never decreases
committed = Σ allocations          · staked into shops
free      = max(0, earned − committed)
```

- **`lib/vrc-allocation.ts`** — **vertex-keyed** (matches the City Key `focus` shape directly, no shop→vertex map). `commitMana(vertex)` draws from free; `withdrawMana(vertex)` returns it; earned is never touched. Stored at `agentprivacy:vrc-allocations-v2` (vertex "0".."63" → amount).
- **Integrated into the lattice (not a separate clicky panel)** — after a first cut shipped a per-shop +/− stepper panel (`VrcAllocationPanel`, since removed for being "too clicky"), allocation now lives in `LatticeMap`: a **🪢 focus-mana bar** in the lattice card (free/committed/earned + a committed-vs-free bar), and a **pour 🪢 / − withdraw** control inside the pinned-seat panel — you click a lit seat (one you hold in your City Key) and pour focus into it. Un-clicky and in the flow of the lattice.
- **City Key `focus`** — on export, `focus = getAllocations()` directly (already vertex-keyed). *"The City Key knows where you're focusing your agents."* soulbis can render `focus` as vertex intensity. Added to `CityKey` type + `buildCityKey` (additive v1).
- *Note:* earning still depends on the soulbis `trace` (unbuilt consumer-side), so the free pool is 0 until Charge has something to award — the mana bar now states this ("Earn 🪢 by charging your City Key").

---

## §5 · The workshop trust task — Presence vs Artefact

The key ontological fix from the user: **Proof of Presence ≠ the Artefact.**
- **Presence** = a **root relationship document** (a template with instructions for *how you relate to this workshop*), filled in. It is the foundation, and it **unlocks** the task.
- **Artefact** = the **trust-task flow** itself (and its output).

The chosen ordering — *Presence is the root → unlocks the task*:

```
0 · PRESENCE      fill the root 'how I relate' doc        → unlocks
1 · DISCOVER      download the artefact template
2 · TRACE         create the artefact on spellweb
3 · BRING HOME    present the forged artefact.md back
4 · CAST → City Key   witness the constellation → adds the vertex to the City Key
```

Three existing storage signals map exactly onto these steps:

| Step | Component | Signal |
|---|---|---|
| 0 · Presence | `FirstArtifactPanel` | `ArtifactPresence` (`agentprivacy:artifact-presences`, shopHref-keyed) |
| 1–3 · Artefact | `ConstellationDownload` | presented-artefacts (`agentprivacy:presented-artefacts`, workshop-keyed) |
| 4 · Cast | `CastShopConstellation` | `ShopWitness` → feeds City Key `lit` |

**Corrected gate chain:** Presence unlocks the artefact task; **bringing the artefact home** unlocks the cast. (An earlier interim build gated the cast on Presence — to be re-pointed in the wrapper.)

Also fixed this arc: the `/city §2` "first artifacts · N / 11 shops" counter was counting distinct *vertices* (so V51-sharing shops collapsed); now counts *shops* (`firstArtifactShops.size`).

---

## §6 · Workshop UX unification — the `WorkshopTrustTask` wrapper (design · status)

Each shop page stacks ~20 components and the trust loop is scattered and out of order. The unification keeps everything but tiers each page:

- **A · Arrival** (banner, hero, lattice visual, greeting)
- **B · The Trust Task** — a `WorkshopTrustTask` wrapper rendering the five beats contiguously, gated, with one header + progress strip (Presence → discover/trace/home → cast → City Key)
- **C · Practice** (record prompt, pattern library, operational-tool CTA)
- **D · Lore & reference** (collapsible: founding act, cousins, spec §§, gaps)

**Status — pilot SHIPPED on `/tailor` (Weavers):**
- ✅ `lib/presented-artefacts.ts` — shared read-accessor + `PRESENTED_ARTEFACTS_CHANGE_EVENT` + `workshopIdForShopHref()`.
- ✅ `ConstellationDownload` emits `PRESENTED_ARTEFACTS_CHANGE_EVENT` on present/remove (so the cast gate reacts to "artefact brought home").
- ✅ `CastShopConstellation` gate re-pointed: optional `gateUnlocked`/`gateHint` props let the wrapper drive the gate (artefact-home); standalone pages fall back to the presence gate until swept. (Also fixed the latent `parseVertex(string|null)` type error.)
- ✅ `WorkshopTrustTask` component built — renders the five beats contiguously with a header + a ✓-progress strip; Presence (FirstArtifactPanel) → [gate: presence] → Artefact (ConstellationDownload) → [gate: artefact-home] → Cast (CastShopConstellation, `gateUnlocked` fed). Piloted on `/tailor` (replaced the three scattered usages; FoundingAct + RecordPrompt remain in the Practice tier). `tsc` clean; `/tailor` 200.
- ✅ **Swept to all producer shops (2026-05-28):** shield · forget · etherchanting · solchanting · jeweler · holon · vault · covenant · bonfires now use `<WorkshopTrustTask>` (via a one-off `sweep_trust.mjs` that swapped the scattered FirstArtifactPanel + ConstellationDownload + CastShopConstellation for the wrapper and fixed imports). All 9 + tailor compile; every route 200. Gathering/Threshold shops (circle · hall · portal · staffs · familiars) intentionally untouched — no first-artefact/Presence, so the wrapper doesn't fit.
- ✅ **Expanded-docs collapse — DONE across all 10 producer shops (2026-05-28):** each page's verbose lore (the §-sections / "Who …" blocks) is now wrapped in a collapsed `CollapsibleSection` ("📖 Expanded docs · {shop}"), folded by default, with the CTAs + WorkshopFooter left visible — so every shop leads with the trust task and tucks the reference lore away (tomes-style). Tailor done by hand; the other 8 regular pages via `wrap_lore.mjs` (anchored on each page's unique §1/"Who" comment → before `{/* CTAs */}`, adding the `CollapsibleSection` import where missing — vault/covenant/bonfires); solchanting wrapped by hand (irregular: no §-comments, lore = "mana/stance" → "Tome VII opens" before the footer). All 10 compile; every route 200. Shared trust components (FirstArtifactPanel · WorkshopTrustTask) were also trimmed, so the always-visible text is leaner everywhere.
- ✅ **Gathering/Threshold shops folded too (2026-05-28):** circle · hall · portal · staffs · familiars now also wrap their lore in a collapsed "📖 Expanded docs · {room}" `CollapsibleSection` — keeping each room's ceremony/interaction (and the bottom District/vertex block) visible, folding the deeper lore. circle/hall/portal/familiars via `wrap_lore2.mjs`; staffs by hand (client component · 8-space indent · keeps the always-visible aspect toggle + aspect panel, folds "four spells" onward). **Expanded-docs collapse now covers all 15 workshop pages.** All compile; every route 200.
- ⏳ Remaining polish: optional lattice glow for `focus`; consider committed-mana deepening a shop's relationship.

---

## §7 · Files touched this arc

**agentprivacy_master**
- `src/lib/city-key.ts` (renamed from `swordsmans-key.ts`) — `buildCityKey` · `CityKey` (+ `trace`, `focus`) · `CITY_KEY_PALETTE` (reconciled coral/cyan · navy→white).
- `src/lib/city-key-charge.ts` — Charge loop (NEW).
- `src/lib/vrc-allocation.ts` — committed-stake ledger (NEW).
- `src/lib/presented-artefacts.ts` — shared presented-artefacts accessor (NEW).
- `src/components/profile/VrcAllocationPanel.tsx` — staking UI (NEW).
- `src/components/profile/AchievementsClient.tsx` — City Key headline (export · charge · VRC readout) · `focus` on export · VrcAllocationPanel in §2.
- `src/components/profile/LatticeMap.tsx` — counter shops-not-vertices.
- `src/components/runecraft/CastShopConstellation.tsx` — cast gating (interim presence gate; → artefact-home pending).
- `src/components/runecraft/ConstellationDownload.tsx` — emits presented-artefacts change.
- `src/app/city/page.tsx` (NEW · renamed route) + `src/app/guide/achievements/page.tsx` (client redirect stub); AppNav · InventoryButton · FirstArtifactPanel link updates.
- `src/components/ceremony/CompletionStep.tsx` · `SwordsmanAccountSettings.tsx` — City Key export + Star/Lattice journey links.

**spellweb** — `key` NodeType + `keys_to`/`synced_with` EdgeTypes + theme visual (City Key).
**star lattice** — `swordsmans-key.interop.md` canon note + `trace`/`lit`/`focus` fields + palette reconciliation.

---

## §8 · Shipped vs queued vs soulbis-dependencies

**Shipped & verified** (`tsc` clean on touched files; `/city`, `/ceremony`, `/tailor` all 200): three-key rename · `/city` route + hero · City Key producer · Charge loop · VRC staking + `focus` · counter fix · `presented-artefacts` accessor + ConstellationDownload event · cast gate re-pointed to artefact-home · **`WorkshopTrustTask` wrapper piloted on `/tailor`**.

**Queued:** sweep `WorkshopTrustTask` across the other 10 shops + full A/B/C/D page tiering; optional lattice glow for `focus`; whether committed mana should *deepen* a shop's relationship (unlocks).

**Soulbis-side (consumer half · not built here):** `/star` must write the `trace` block (so Charge awards mana) and read `focus`/`lit` (to render). Until then Charge correctly reports "no soulbis trace yet."

---

## §9 · Canon touchpoints

- **VRC monotonic** (`vrc-mana.ts`): earned never decreases — the committed/free split preserves this; staking points mana without spending the earned total.
- **Moon-phase stratum**: `identity.stratum` = popcount of the tier; the key's per-vertex readings echo 🌑0→🌕6.
- **C1 (φ ≈ 1.618 protect:project)** and the reserved `geometry{smRatio}` block remain Key-v2 territory alongside the Mage's Key + ed25519 verify.
