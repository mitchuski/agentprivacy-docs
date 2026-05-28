# Proposal — Track `/star` and `/lattice` as Gateway Nodes in Spellweb

**Date:** 2026-05-28
**Author:** privacymage
**Status:** PROPOSAL · ready to apply (drop-in node/edge specs below)
**Scope:** Add the two soulbis lattice surfaces — `soulbis.com/star` (manifold) and `soulbis.com/lattice` (codex) — as first-class `gateway` nodes in the spellweb knowledge graph, so the City Key bridge has visible endpoints to track.
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

**Builds on:**
- `chronicles/2026-05-27_star_lattice_swordsman_key_integration_chronicle.md` — §5 *Spellweb updates* named this work; this proposal is the concrete node/edge spec that §5 deferred.
- `spellweb/src/types/graph.ts` — the `key` NodeType and the `keys_to` / `synced_with` EdgeTypes (shipped 2026-05-27).

---

## §1 · Why this exists

The 2026-05-27 integration shipped the **vocabulary** for the City Key bridge — the `key` NodeType, the `keys_to` and `synced_with` EdgeTypes, plus the `key` node visual (🗝️) and the two edge styles in `theme.ts`. What it did **not** ship is the **node instances**: there is still no node in `src/data/nodes.ts` that represents `soulbis.com/star` or `soulbis.com/lattice`, and no edge in `src/data/edges.ts` that wires them in. So the graph carries the *capacity* to describe the bridge but not the bridge itself.

This proposal closes that gap. After it lands, a viewer of spellweb.ai can see the two soulbis surfaces as tracked nodes — where the City Key is carried, how the two surfaces relate, and how they attach to the City of Mages — instead of the bridge being documented only in prose.

The pipeline is **hand-curated**, not generated: `nodes.ts` / `edges.ts` are authored by hand (see their file headers; `update_nodes_v54.py` is a per-node patch script, not a generator). So "include it in agentprivacy-docs and have it appear in spellweb" means: *this doc is the source of truth for the change, and a maintainer applies the blocks in §3–§4 verbatim to both spellweb trees.* No build step reads this file.

---

## §2 · What we are adding (and what we are not)

**Adding:** two `gateway` node instances + the edges that anchor them.

**Not adding:** a canonical `key` node instance. A City Key is **per-bearer and runtime** — like the `artefact` deviation nodes, a `key` node is created at import/export time from the bearer's own key, not authored into the canonical `NODES` list. The canonical graph gets the *endpoints* (the two gateways); the `key` carrier and its `keys_to` / `synced_with` edges are minted at runtime when a bearer loads a key. This proposal therefore only touches `nodes.ts` (two nodes) and `edges.ts` (the anchoring edges); it leaves the runtime key-node path to the import flow.

**Is `gateway` the correct type?** Yes — it is the *already-committed* decision, not a fresh pick: the shipped `graph.ts` comment on the `key` type states verbatim that *"the soulbis pages are `gateway` nodes it `synced_with`,"* and the 2026-05-27 chronicle §5 named `gateway` for exactly these two surfaces. The only caveat is semantic: `gateway`'s stated purpose is "sister cities & upstream cousin-substrate forges (Archon, UOR…)," whereas the soulbis surfaces are **first-party** (soulbis is the Swordsman keyring of this same suite). We resolve this by (a) marking them `attribution: "agentprivacy"` so they read as first-party, not cousin, and (b) broadening the type's doc comment to "external surfaces this corpus links to — sister cities, cousin-substrate forges, and first-party companion surfaces." The alternative — a dedicated `surface`/`lattice_view` NodeType — is *cleaner* semantically but materially bigger: it touches the `NodeType` union, `Theme.nodes`, `TypeFilterState`, the `Record<NodeType,…>` maps in `MobileSpell.tsx` + `SpellWeb.tsx`, and `theme.ts` visuals, and it contradicts an already-shipped decision. **Recommendation: keep `gateway`** (Decision D1 below).

---

## §3 · Node specs (apply to `src/data/nodes.ts`)

Append to the **Gateways** block (after `gateway-aaif`, ~line 1444 in standalone spellweb), and bump the block's count comment from `(4)` to `(6)`:

```ts
  // ── soulbis lattice surfaces (2 · the City Key bridge endpoints · 2026-05-28) ──
  // First-party Swordsman-keyring surfaces (NOT cousin forges): the two soulbis
  // renderings of the 64-vertex lattice that import/export the City Key. See
  // chronicles/2026-05-27_star_lattice_swordsman_key_integration_chronicle.md.
  { id: "gateway-soulbis-star", type: "gateway", label: "soulbis · /star (manifold)", emoji: "✦", domain: "shared", layer: "knowledge", desc: "First-party Swordsman-keyring surface. The 3D star-tetrahedron manifold (Vite + Three.js) rendering the 64-vertex ℤ/64ℤ sovereignty lattice on soulbis.com. Imports a City Key (palette + 64 vertex descriptions) and shows each description in its inspector as the succ run lights the vertex. Live-syncs with /lattice over BroadcastChannel('agentprivacy-succ'). Consumer endpoint for the City Key exported from agentprivacy /guide/achievements.", href: "https://soulbis.com/star", attribution: "agentprivacy" },
  { id: "gateway-soulbis-lattice", type: "gateway", label: "soulbis · /lattice (codex)", emoji: "⬢", domain: "shared", layer: "knowledge", desc: "First-party Swordsman-keyring surface. The self-contained 64-cell vertex codex on soulbis.com, keyed by stratum (Pascal rows 0–6). Imports a City Key and flags described cells in its panel; rebroadcasts the key over BroadcastChannel('agentprivacy-succ') so one import lights both surfaces. The textual/codex twin of /star — same 64 vertices, same 96 holographic edges, same moon-phase stratum lighting.", href: "https://soulbis.com/lattice", attribution: "agentprivacy" },
```

Field choices follow the existing `gateway-archon` / `gateway-uor-foundation` pattern exactly (`type`, `domain`, `layer`, `desc`, `href`, `attribution`). `layer: "knowledge"` (these render the lattice geometry/codex; matches `gateway-uor-foundation`). Emojis `✦` (star) and `⬢` (hex/lattice) mirror the icons the agentprivacy CompletionStep already uses for these two destinations.

---

## §4 · Edge specs (apply to `src/data/edges.ts`)

Add near the civic/gateway edges:

```ts
  // ── soulbis lattice surfaces · City Key bridge (2026-05-28) ──
  // The City of Mages opens onto both surfaces; the two surfaces are sibling
  // renderings that live-sync the same lattice.
  { source: "civic-city-of-mages", target: "gateway-soulbis-star",    type: "gateway_to" },
  { source: "civic-city-of-mages", target: "gateway-soulbis-lattice", type: "gateway_to" },
  { source: "gateway-soulbis-star", target: "gateway-soulbis-lattice", type: "kin_to" },
```

**Verified house style (2026-05-28, `edges.ts:1946–1965`):** every existing gateway is anchored from the City with **both** a `gateway_to` and a `kin_to` edge (`civic-city-of-mages → gateway-archon`, `→ gateway-uor-foundation`, etc.). There are **no** gateway↔gateway edges today, and **no** `gateway-soulbis-*` edges exist — confirming this is a net-new addition.

Rationale for the chosen set:
- `gateway_to` (city → surface) matches its defined use and ties both nodes into the giant component via `civic-city-of-mages`, so the orphan audit (`scripts/audit-orphans.mjs`) stays clean.
- We **omit** the city→soulbis `kin_to` that the cousin gateways carry: `kin_to` means *mutual lateral kinship — cousin-cast / sister-city / cousin-substrate*, and the soulbis surfaces are **first-party**, not cousins. Using it city→soulbis would mislabel them as an external ecosystem.
- `kin_to` (star ↔ lattice) is the one place kinship genuinely applies — the two surfaces are sibling renderings of one lattice that live-sync over BroadcastChannel. This is a new *gateway↔gateway* shape (none exist yet); it is the most honest available edge for "two views of the same thing."
- We deliberately **do not** use `synced_with` here — per `graph.ts`, `synced_with` is reserved for *key → gateway* (a City Key carried to a surface), a **runtime** edge minted on import, not a canonical star↔lattice edge.

**Runtime edges (no change needed here, documented for completeness):** when a bearer imports/exports a City Key, the import flow may mint a runtime `key` node with `keys_to` edges to the vertices it describes and `synced_with` edges to these two gateways — exactly as `artefact` deviation nodes are minted from forged blades today.

---

## §5 · Apply to BOTH spellweb trees

Per the established 2026-05-14 pattern (admit nodes + edges together across both copies):
1. **Standalone `spellweb/`** — `src/data/nodes.ts` (§3) + `src/data/edges.ts` (§4). The NodeType/EdgeType unions and `theme.ts` visuals already exist, so no type changes are needed.
2. **In-master `agentprivacy_master/src/...`** — mirror the same two nodes + three edges into the in-master spellweb data if/when its graph data is kept in sync (confirm whether master re-uses the standalone data or carries its own copy before duplicating).

**Gate:** `npm run build` (which runs `tsc`) in `spellweb/` after applying — expect 0 errors (additive data only). Optionally run `scripts/audit-orphans.mjs` to confirm the two new nodes are reachable.

---

## §6 · Open decisions (flag, don't silently choose)

- **D1 · Attribution.** Proposed `attribution: "agentprivacy"` (soulbis is first-party, the Swordsman keyring of this suite). Alternative: introduce a new `Attribution` value if first-party external *surfaces* should be visually distinct from the core corpus. Recommend `agentprivacy` for now — no type change, accurate ownership.
- **D2 · Layer.** Proposed `knowledge` (geometric surfaces, matches UOR). Alternative `narrative` if they should group with the sister-city gateways in the layer filter. Recommend `knowledge`.
- **D3 · star↔lattice edge.** Proposed `kin_to`. Alternative: broaden `synced_with` to also cover gateway↔gateway BroadcastChannel sync and use it here. Recommend `kin_to` to keep `synced_with` meaning exactly *key→gateway*.
- **D4 · `key` node.** Proposed: keep it runtime-only (per-bearer), not canonical. Revisit only if a canonical "sample key" node is wanted for documentation.

---

## §6b · The guild-quarter pattern (why `quarter_of`, forward-looking)

`quarter_of` is deliberate, not a placeholder. The soulbis Star/Lattice are **the root's quarter** of the City — the first instance of a generalizable pattern, not a one-off. The intended shape:

- **`keeps`** (guild → its surfaces): each guild keeps its own lattice surfaces. Soulbis ⚔️ keeps `/star` + `/lattice` today.
- **`quarter_of`** (surfaces → City): those surfaces are a quarter *of* the City of Mages, not a sister city outside it.

Today the soulbis quarter looks lopsided because the root (Soulbis) is the only fully-built guild. As the City grows, other guilds are expected to mirror it with their own quarters and surfaces — **Archon next**: `gateway-archon` would gain parallel lattice surfaces kept by `cast-genitrix` / `cast-flaxscrip`, each `quarter_of` the same City. The `keeps` + `quarter_of` pair is the template every future guild-quarter reuses; the structure anticipates the symmetry before the symmetry exists.

## §7 · Checklist

| Item | Where | Status |
|---|---|---|
| `gateway-soulbis-star` + `gateway-soulbis-lattice` nodes | `spellweb/src/data/nodes.ts` | ☐ to apply |
| `gateway_to` ×2 + `kin_to` ×1 edges | `spellweb/src/data/edges.ts` | ☐ to apply |
| Mirror into in-master spellweb data (if separate copy) | `agentprivacy_master/src/...` | ☐ confirm + apply |
| `npm run build` (tsc) gate | `spellweb/` | ☐ 0 errors expected |
| Orphan audit | `scripts/audit-orphans.mjs` | ☐ both reachable |
| Index this proposal | `plans/INDEX.md` | ☐ add one-liner |

---

*The graph carried the word for the bridge before it carried the bridge. This lays the two stones the City Key already knew how to stand on.*
