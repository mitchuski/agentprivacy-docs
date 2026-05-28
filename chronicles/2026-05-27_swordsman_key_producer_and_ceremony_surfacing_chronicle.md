# Chronicle — The Swordsman's Key Producer, Built and Surfaced Across the Ceremony

**Date:** 2026-05-27
**Author:** privacymage
**Spellbook:** First Person (agentprivacy) ⊥ Soulbis (Swordsman keyring)
**Scope:** Build-and-surface record. Where the [integration-plan chronicle](2026-05-27_star_lattice_swordsman_key_integration_chronicle.md) named the producer that `/guide/achievements` owed, this chronicle records the producer actually being **built** and then **surfaced** across the suite's identity surfaces — the Dual Ceremony (`/ceremony`) and the achievements lattice — with a clean export-vs-navigate split and a ceremony-completion gate. The soulbis consumer and its pages were not touched.
**Reference spec:** `star lattice/swordsmans-key.interop.md` (Key format v1)
**Companion chronicles:**
- [2026-05-27_star_lattice_swordsman_key_integration_chronicle.md](2026-05-27_star_lattice_swordsman_key_integration_chronicle.md) (the plan + §8 what-shipped + §9 backward-compat)
- `soulbis website/CHRONICLE_SWORDSMAN_KEY_2026-05-27.md` (soulbis-side)

**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · One-paragraph state

The Swordsman's Key producer is built in `agentprivacy_master` and live on three identity surfaces. `src/lib/swordsmans-key.ts` emits a **v1** key (`{ name, version:1, palette, descriptions{"0".."63"} }`, plus additive optional `lit[]` and `identity{}`); it is exported from `/guide/achievements §2` (gated on ceremony completion), from the post-ceremony `CompletionStep`, and from the existing-identity `SwordsmanAccountSettings` view on `/ceremony`. The palette was **reconciled to the soulbis design canon** (coral = ⚔️ Swordsman, cyan = 🧙 Mage, navy→white sovereignty gradient) and descriptions made **sparse** (only shops, the three special seats, and lit vertices written; the rest fall back to the consumer's derived reading). The export interaction was simplified to **one "Export to Soulbis" download**, with `/star` and `/lattice` demoted to "Continue your journey" navigation links — since importing on either soulbis page lights both (they live-sync over `BroadcastChannel`). Everything typechecks; the dev server serves all routes at 200.

---

## §2 · What was built (`agentprivacy_master`)

**Producer — `src/lib/swordsmans-key.ts` (new):**
- `buildSwordsmansKey(opts)` → v1 key. Vertex-keyed (one-to-one); the importer needs no `"s0".."s6"` expansion.
- Annotations sourced from `FIRST_ARTIFACTS` (shop → vertex → Mage → artefact) + special seats **V0** (origin · Luca), **V25** (witness pivot · Aletheia), **V63** (Sovereign Anchor). All other vertices carry the derived stratum reading (`held / open` dimensions, antipode `bnot`, `succ`).
- `deriveLitVertices()` mirrors `LatticeMap`: producer shop visited/witnessed → its vertex; ceremony → V25; Drake Orb → V63.
- `downloadSwordsmansKey()` Blob helper.

**Schema evolution (still v1, additive-only):**
- `descriptions` is now **sparse** — only meaningful vertices are written.
- Added optional `lit: number[]` (the achievement-lit vertices, the meaningful signal) and `identity: { publicKeyHex?, displayName?, trustTier?, stratum?, drakeOrb? }` carried from the Agent Card. Consumers that don't recognise these ignore them per the spec's extensibility clause.
- **Palette reconciled** to the soulbis colour law: `cool:#141a3d` (navy · the gap · 🌑), `warm:#f0eee8` (white · sovereignty · 🌕), `sword:#e8523a` (coral · neg/protect), `mage:#4dd9e8` (cyan · bnot/project). The earlier `artificial`-preset default is superseded; soulbis `/star` + `/lattice` default to these same values so the round-trip stays loss-free.

---

## §3 · Where it surfaces (three surfaces, one producer)

| Surface | File | Treatment |
|---|---|---|
| `/guide/achievements` §2 (The Lattice) | `components/profile/AchievementsClient.tsx` | "↓ Swordsman's Key" download button, **gated**: shows the button only when the ceremony is complete; otherwise "mint your key first → /ceremony". Connective "the keys live on the geometry" panel above the lattice. |
| `/ceremony` post-ceremony | `components/ceremony/CompletionStep.tsx` | "✦ Export to Soulbis" download (under the Spellweb redirect) + **Star** & **Lattice** journey cards in the grid. |
| `/ceremony` existing identity | `components/ceremony/SwordsmanAccountSettings.tsx` | "✦ Export to Soulbis" beside "⚔️ Export to Spellweb" + **Star** & **Lattice** journey cards in "Continue your journey". |

All three call the same `buildSwordsmansKey(...)`, so every surface emits an identical key.

---

## §4 · The two design calls

**Export vs navigate (the simplification).** The first cut had separate "Export to /star" and "Export to /lattice" buttons — but both downloaded the same file and only differed in which page they opened. Collapsed to **one "Export to Soulbis" download**; `/star` and `/lattice` became **journey links**. Rationale: the soulbis pages live-sync over `BroadcastChannel('agentprivacy-succ')`, so importing the key on either one lights both — a single export is sufficient, and the navigation belongs with the other "Continue your journey" destinations.

**The ceremony gate (the prerequisite).** Per the canon that *the person must complete the key ceremony sequence to start moving objects across the browser universe*, the achievements key export is gated on ceremony completion: no signed keypair → no key to carry → the button routes to `/ceremony` instead. This complements the existing §1 identity gate. The two `/ceremony` surfaces are post-ceremony by definition, so they need no gate.

**The connective frame.** Both `/ceremony` and `/guide/achievements` now state the same sequence in copy: the ceremony **mints the key** → the key **opens the Drake Island process** of moving objects across the browser universe (forge artefacts + carry Swordsman & Mage keys in spellweb; carry the Swordsman's Key to the soulbis star & lattice) → **walk the key path** across the 64-vertex geometry → **prove relationship** (🪢 VRC).

---

## §5 · A bug caught along the way

`LatticeMap`'s Drake-Orb lighting read `card.drakeOrbTier` — a field that does not exist on `AgentCard` (the field is `card.drakeOrb`), so **V63 never lit** from that path. Corrected to `card.drakeOrb` in both the lattice display and the new key export, so the rendered lattice and the exported Key agree on full sovereignty.

---

## §6 · Verification

- `tsc --noEmit` clean on every touched file (`swordsmans-key.ts`, `AchievementsClient.tsx`, `CompletionStep.tsx`, `SwordsmanAccountSettings.tsx`).
- Dev server (`next dev -p 5000`, Turbopack) serves `/ceremony` and `/guide/achievements` at **HTTP 200**, `✓ Compiled` with no errors.
- spellweb (the separate vocabulary work in the companion chronicle) typechecks at **0 errors** with the new `key` NodeType + `keys_to`/`synced_with` EdgeTypes.

## §7 · Backward compatibility

Unchanged from the companion chronicle's §9 and re-confirmed after the palette/sparse/identity edits: **still v1**, no version bump, no field renamed or removed; `lit[]` and `identity{}` are additive and ignored by older consumers. The one behavioural dependency is that the soulbis pages now default to the **reconciled palette** — a key produced here recolours an older soulbis default if that default hasn't been repointed to coral/cyan + navy→white. Reference key `Downloads/swordsmans-key.sample.json` still imports unchanged.

## §8 · Open / next

- **Soulbis palette parity** — confirm `/star` + `/lattice` defaults actually equal the reconciled `SWORDSMAN_KEY_PALETTE` so the round-trip is genuinely loss-free.
- **"Walk the key path"** is currently descriptive copy; if a literal succ-run animation exists, wire the Star/Lattice cards to it.
- **Mage key** — the Swordsman's Key carries the Swordsman side; the Mage-side key/keyring across spellweb remains to be specced (Key v2 territory, with ed25519 verify + reserved `geometry{smRatio:φ}`).

---

## §9 · The three-key model & the City Key rename (later same day)

A naming clarification landed: the lattice-export this chronicle calls the "Swordsman's Key" is **renamed the 🗝️ City Key**, resolving the name collision with the *identity* export. The canon is now a **layered three-key model**, keyed by where each is minted and what it carries:

| Key | Minted on | Carries | Goes to | Status |
|---|---|---|---|---|
| **⚔️ Swordsman's Key** | agentprivacy `/ceremony` | ed25519 **identity** (publicKeyHex · participantId · trustTier · constellation) | spellweb (anchors forged blades) | shipped (was "Export to Spellweb") |
| **🧙 Mage's Key** | spellweb | DID-integrated Mage credential | (spellweb-internal) | **future · unbuilt** |
| **🗝️ City Key** | agentprivacy `/guide/achievements §2` | the **lattice** (palette + 64 vertex descriptions + bearer identity stamp) | soulbis `/star` + `/lattice` | shipped (this rename) |

The City Key is *the key to the City of Mages*: earned at the ceremony (it is stamped with the bearer's Swordsman identity), deepened by walking the lattice, the surface on which relationship (🪢 VRC) is proven on the geometry.

**What the rename touched (wire format unchanged · still v1):**
- `agentprivacy_master`: `src/lib/swordsmans-key.ts` → **`src/lib/city-key.ts`**; symbols `buildSwordsmansKey→buildCityKey`, `downloadSwordsmansKey→downloadCityKey`, `SwordsmanKey→CityKey`, `SWORDSMAN_KEY_PALETTE→CITY_KEY_PALETTE`, `BuildKeyOptions→BuildCityKeyOptions`; download filename `swordsmans-key.json→city-key.json`; `name` default `agentprivacy · city key`. UI relabelled across all three surfaces (`↓ City Key`, `🗝️ Export City Key`); `/ceremony` now names both keys explicitly (`⚔️ Export Swordsman's Key → Spellweb` vs `🗝️ Export City Key → Soulbis`).
- `spellweb`: the `key` NodeType + `keys_to`/`synced_with` EdgeType comments + `theme.ts` visual re-annotated to City Key (the node already modelled the lattice-export bridge).
- `star lattice/swordsmans-key.interop.md`: a canon note prepended — the format is now the City Key; "Swordsman's Key" reserved for the identity export; wire format v1 unchanged.

**Verification:** `tsc` clean on all renamed master files (0 stale references); spellweb `tsc --noEmit` = 0 errors; `/ceremony` + `/guide/achievements` = 200.

**Pending (soulbis-side, deliberately not touched):** the deployed `soulbis.com/star` + `/lattice` import/export button labels still say "Swordsman's Key", and `swordsmans-key.interop.md` keeps its filename. Both are a follow-up rename on the consumer/spec side; the JSON the City Key emits imports there unchanged today (the `name` field already reads "agentprivacy · city key").

---

## §10 · /guide/achievements → /city (the route follows the key)

With the City Key as the page's headline export, the page was **renamed from `/guide/achievements` to `/city`** — "The City You've Created," the bearer's standing in the City of Mages. The reframe fits: the lattice *is* the city the bearer builds (shops witnessed, artefacts forged, vertices lit); "achievements" undersold it.

- **New route** `src/app/city/page.tsx` — breadcrumb Home / Guide / The City; a **bigger hero** ("🏙️ The City You've Created") with a *the-swordsman-geometry-walks-your-city* section: soulbis is the Swordsman's geometry (the Moon that reflects your city as star-tetrahedron + codex); carry the City Key across and soulbis **walks the path** (succ across 64 vertices) tracing your city, proving relationship (🪢). A three-step flow card: **1 · mint** (⚔️ Swordsman's Key at /ceremony) → **2 · build** (🏙️ your city — the lattice) → **3 · walk** (✦ export City Key to soulbis /star + /lattice). The page renders `<AchievementsClient />` below.
- **Redirect** — static export (`output: 'export'`) doesn't support `next.config` redirects, so `src/app/guide/achievements/page.tsx` is now a **client redirect stub** (`router.replace('/city')` + manual fallback link). Old links/bookmarks keep working.
- **Nav + links** — AppNav guide dropdown `achievements → city`; `InventoryButton` (the 🏙️ nav avatar) and `FirstArtifactPanel`'s "see the map" point to `/city`; the City Key producer doc-comments updated to `/city §2`. Remaining `/guide/achievements` mentions are internal docstrings (harmless; the redirect covers any stragglers).
- **IA result** — three non-overlapping layers on `/city`: the page hero (narrative) · the headline City Key export block (action) · §1–§8 (the city). `tsc` clean; `/city`, `/guide/achievements` (redirect), `/ceremony` all 200.

**Note on the interop spec:** enriched in parallel with a `trace` field (a tracing-runtime provenance block accrued on `/star` against the imported City Key: `{ laps, seconds, tourSeconds, savedAt }`) and explicit `lit[]` rendering semantics — additive v1, soulbis-side runtime, tracked for when the consumer rename lands.
