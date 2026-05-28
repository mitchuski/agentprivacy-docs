# Chronicle — Star Lattice & the Swordsman's Key: Suite Integration

**Date:** 2026-05-27
**Author:** privacymage
**Spellbook:** First Person (agentprivacy) ⊥ Soulbis (Swordsman keyring)
**Scope:** Architectural record of how the **star lattice** (`soulbis.com/star` + `/lattice`) and the **Swordsman's Key** interchange format thread through the whole agentprivacy suite. Documents the producer/consumer seam, names the new **export type** owed by `/guide/achievements`, and specifies the spellweb-graph vocabulary the bridge needs.
**Reference spec:** `star lattice/swordsmans-key.interop.md` (Key format v1, consumer contract)
**Companion chronicles:**
- `soulbis website/CHRONICLE_SWORDSMAN_KEY_2026-05-27.md` (soulbis-side sync, redesign sketch)
- `chronicles/2026-05-09_navigation_lattice_workshops_chronicle.md` (the 64-vertex lattice unification)
- `chronicles/moon-phase-notation.md` (stratum = popcount, 🌑0→🌕6)

**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · One-paragraph state

The star lattice is the 64-vertex `ℤ/64ℤ` sovereignty structure of PVM V5.4, rendered on `soulbis.com` two ways — `/star` (a 3D Vite + Three.js star-tetrahedron manifold) and `/lattice` (a self-contained 64-cell vertex codex). Both pages already **import and export** the **Swordsman's Key**, a portable JSON (`{ name, version:1, palette{cool,warm,sword,mage}, descriptions{"0".."63"} }`) that carries the gem palette and 64 per-vertex descriptions between origins, and they live-sync over `BroadcastChannel('agentprivacy-succ')`. The agentprivacy side already renders the **identical lattice** inside `/guide/achievements` (`src/lib/spellweb/lattice-mode.ts` + `LatticeMap.tsx`): same Pascal-row layout, same `popcount` stratum, same 96 Hamming-1 edges, the same `PERSONA_VERTEX` / `SHOP_VERTEX` / `VERTEX_SIGIL` maps, and a `deriveLitVertices()` lighting rule. **The consumer is built; the producer is not.** The single missing piece is an **export type on the achievements tab** that serialises the user's achievement state into a `swordsmans-key.json` the soulbis pages already know how to read.

---

## §2 · The overlap, precisely

Both surfaces are the *same* lattice, independently implemented:

| Concept | star lattice (`soulbis.com`) | agentprivacy_master (`/guide/achievements`) |
|---|---|---|
| Vertices | 64 (`ℤ/64ℤ`), 6-bit address | 64, `vertexToGraphCoord(v)` over Pascal rows |
| Stratum | `popcount(x)`, 0→6 | `stratum(v)`, identical |
| Edges | 96 holographic (∂M, 96/64 = P^1.5) | 96 Hamming-1 (`v ^ (1<<i)`), identical |
| ⚔️ Swordsman | `neg(x) = (64−x) mod 64` (protect) | same canon |
| 🧙 Mage | `bnot(x) = 63−x` (project/antipode) | same canon |
| succ | `neg∘bnot = (x+1) mod 64` | same canon |
| Cast → vertex | descriptions keyed `"0".."63"` | `PERSONA_VERTEX`, `SHOP_VERTEX`, `VERTEX_SIGIL` |
| Lighting | imported descriptions flag cells | `deriveLitVertices()` (visited / witnessed / ceremony→V25 / Drake Orb→V63) |

The **Swordsman's Key** is the bridge between them — by design it "replaces a cross-site live link: produce it on one side, import it on the other" (interop spec §intro). Cross-origin live linking is impossible (localStorage and BroadcastChannel are per-origin), so the Key is the portable carrier.

**Consumer contract (already shipped on soulbis):**
- Import parses JSON → applies `palette` (gradient + gem glows) → writes `descriptions` onto nodes; `/star` shows each description in its inspector as the succ run hits the vertex, `/lattice` flags described cells in its panel.
- Export serialises current palette + descriptions back to `swordsmans-key.json` (round-trips cleanly).
- On import, the Key is rebroadcast over `BroadcastChannel('agentprivacy-succ')` so loading once lights both pages.

---

## §3 · The new export type (the producer — to build)

`/guide/achievements` already holds every input the Key needs. The integration adds **one new export type** alongside the page's existing exporters (`lib/workshop-prompts.ts` → `agentprivacy.workshop-prompts` JSON; `my_spellbook.md`; `*.soul.md`).

**Producer plan:**
1. New helper `src/lib/swordsmans-key.ts` exporting `buildSwordsmansKey(state): SwordsmanKey`.
2. `descriptions{"0".."63"}` — for each **inhabited** vertex emit cast/shop name + sigil + stratum reading (e.g. `"28": "🪡 Pallia · the Tailor · s2 — woven concealment"`); for **lit-but-uninhabited** vertices emit the achievement that lit it; leave the rest sparse (spec permits fallback to the derived reading).
3. `palette{cool,warm,sword,mage}` as `#rrggbb`. **OPEN DECISION — flag, do not silently choose:** soulbis preset default is `sword:#9fe8ff / mage:#ffc070`, but soulbis-site design canon is coral = Swordsman / cyan = Mage. Palette reconciliation is unresolved (see soulbis chronicle). Until decided, emit the soulbis "artificial" preset so round-trip is loss-free.
4. Stamp `name:"agentprivacy · achievements key"`, `version:1`; reuse the existing Blob → object-URL → click download pattern.
5. UI: "↓ Swordsman's Key" button in **§2 The Lattice** of `AchievementsClient.tsx`.

**Keying:** emit **vertex keys** (one-to-one), not stratum form — agentprivacy knows each cast's exact vertex, so no `"s0".."s6"` expansion is needed by the importer.

**Reserved, backward-compatible (later):** the optional `geometry{coreScale,smRatio}` block, where `smRatio = φ ≈ 1.618` is the conjectured optimal protect:project ratio (canon C1); and an ed25519 sign/verify phase for the redesign where soulbis becomes the **Swordsman keyring** (`/key` to verify/carry the Agent Card; forge stays Mage-side on `/ceremony`).

---

## §4 · Sync path (no consumer changes)

```
/guide/achievements  ──build──▶  swordsmans-key.json  ──import──▶  /star  ⇄(BroadcastChannel)⇄  /lattice
       (producer: NEW)                (Key v1)              (consumers: SHIPPED)
```

Once the producer ships, the loop closes with zero changes to the soulbis pages: download from achievements → import on `/star` or `/lattice` → both light up. A Key exported from soulbis is also valid input back into agentprivacy (round-trip).

---

## §5 · Spellweb updates

Spellweb's `lattice` layout mode already pins nodes to these same vertices, so the geometric ground is shared. To make the Key and the cross-site bridge **first-class graph objects**:

- **NodeType:** add `key` (an imported/exported Swordsman's Key as a node), or reuse `artefact` with a `keyKind` field.
- **NodeType `gateway`** (already exists): add gateway nodes `soulbis.com/star` and `soulbis.com/lattice`.
- **EdgeTypes:** add `keys_to` (Key node → the vertices it describes) and `synced_with` / reuse `gateway_to` (Key ⇄ soulbis gateways).
- Apply to **both** the in-master spellweb (`agentprivacy_master/src/...`) and the standalone `spellweb/` repo (`src/types/graph.ts` NodeType/EdgeType unions), following the established 2026-05-14 pattern of admitting EdgeTypes + node fields together.

---

## §6 · Punch list

| Item | Where | Status |
|---|---|---|
| Swordsman's Key consumer (import/export, BroadcastChannel) | `soulbis.com/star`, `/lattice` | ✅ shipped |
| Lattice render parity (64 / popcount / 96 edges / cast maps) | `lib/spellweb/lattice-mode.ts`, `LatticeMap.tsx` | ✅ shipped |
| `buildSwordsmansKey()` helper | `agentprivacy_master/src/lib/swordsmans-key.ts` | ✅ built (2026-05-27) |
| "↓ Swordsman's Key" export button | `AchievementsClient.tsx` §2 | ✅ built (2026-05-27) |
| Latent `drakeOrbTier`→`drakeOrb` fix (V63 lighting) | `AchievementsClient.tsx` | ✅ fixed (2026-05-27) |
| Spellweb `key` node + `keys_to`/`synced_with` edges | `spellweb/src/types/graph.ts` + `theme.ts` + maps | ✅ built (2026-05-27) · typecheck 0 errors |
| Palette reconciliation decision | soulbis ⊥ agentprivacy canon | ⛔ open (shipped with soulbis preset default) |
| ed25519 verify phase + `geometry{smRatio:φ}` | Key v2 (reserved) | 🔮 future |

---

## §8 · What shipped 2026-05-27 (the external-repo build)

The soulbis repo was **not touched** (its consumer is already correct). Work landed in the two external repos:

**agentprivacy_master (producer):**
- New `src/lib/swordsmans-key.ts` — `buildSwordsmansKey(opts)` emits strict **v1** `{ name, version:1, palette, descriptions{"0".."63"} }`. Vertex-keyed (one-to-one). Annotations sourced from `FIRST_ARTIFACTS` (shop → vertex → Mage → artefact) + special seats V0/V25/V63 + derived stratum readings for the rest; lit vertices flagged `✦ lit by your achievements.` Palette defaults to the soulbis `artificial` preset (`#1f54d6 / #ff4533 / #9fe8ff / #ffc070`) so round-trip is exact; overridable.
- `AchievementsClient.tsx` §2: a "↓ Swordsman's Key" button + a one-line caption pointing at `soulbis.com/star` and `/lattice`.
- Fixed a latent bug: the lattice's Drake-Orb lighting read `card.drakeOrbTier` (nonexistent → V63 never lit). Corrected to `card.drakeOrb` in both the display path and the new export, so the rendered lattice and the exported Key agree.

**spellweb (graph vocabulary):**
- `NodeType` gained `key`; `EdgeType` gained `keys_to` (key → vertices it describes) and `synced_with` (key → soulbis gateway). `Theme.nodes` + `TypeFilterState` extended; `theme.ts` got the `key` node visual (🗝️ sword-cyan) + the two edge styles; the three `Record<NodeType,…>` maps in `MobileSpell.tsx` and the filter state in `SpellWeb.tsx` got their `key` entries. `tsc --noEmit` → **0 errors**.
- Note: spellweb's existing `SwordsmanImport` component is a **different** object — the *Swordsman identity link* (`publicKeyHex` / `participantId` from `/ceremony`), not the *Swordsman's Key* (palette + descriptions). Same name, different payloads, no collision.

## §9 · Backward compatibility of existing keys

**Old keys do not break.** Verified against the reference `swordsmans-key.sample.json` (a full 64-vertex v1 key):

- **No schema version bump.** The producer emits `version: 1` — the same version every existing key and consumer already uses.
- **No field renamed or removed.** Output is exactly `{ name, version, palette{cool,warm,sword,mage}, descriptions }` — the identical shape the sample carries and the soulbis pages parse.
- **Additive-only forward plan.** The reserved `geometry{coreScale,smRatio}` block is optional; the spec's extensibility clause says consumers ignore unknown fields, so adding it later stays backward-compatible.
- **Round-trip preserved.** A key exported here imports unchanged into `/star` and `/lattice`; a key exported from soulbis re-imports here unchanged (palette default matches the consumer's own default preset). The only field whose *content* differs from the sample is `descriptions` text — which is exactly what the sample's `[REPLACE with the /achievements text]` placeholders asked the producer to fill.

Conclusion: the changes are a **strict superset-compatible v1 producer**; nothing about old keys breaks.

---

## §7 · Conjecture touchpoints

- **C1** (φ ≈ 1.618 protect:project): the reserved `geometry.smRatio` field is where each intelligence preset can carry its own Swordsman:Mage balance.
- **P^1.5** (∂M = 96/64 = 1.5): the lattice's 96 holographic edges already encode the Privacy Exponent; both surfaces draw it identically.
- **Moon-phase notation:** stratum = popcount = 🌑0→🌕6 (6 sovereignty dimensions); the Key's per-vertex descriptions are the textual face of the same encoding.
