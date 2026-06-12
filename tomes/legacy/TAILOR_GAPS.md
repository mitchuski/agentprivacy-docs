---
title: "Tailoring Shop — Operational Gaps"
subtitle: "What still needs to be built before a Sovereign can weave a real cloak through the agentprivacy interface"
status: "Working note · 2026-05-08"
spec_type: "Implementation gap analysis"
authors:
  - "privacymage (privacymage / 🧙)"
companion_to:
  - "cloak_specification_v1_0.md (the spec the gaps measure against)"
  - "crafting-tome-and-cloak-interface-spec.md (the surface design)"
  - "bilateral-cloak-ceremony-spec.md (the agent-to-agent ceremony)"
parallel_to:
  - "Shield Shop status — Pattern A operational MVP (memo builder + SHA-256 + history) live on /runecraft as of 2026-05-08"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Tailoring Shop — Operational Gaps

## §0. Where the shop is today

Operational on the website (~22%):

- **Spec complete** — Cloak Specification v1.0 with Eight Properties, 5 axes, valve-classes, 7-node VC decomposition, 10 conformance requirements
- **Cast layer documented** — flaxscrip, GenitriX, Pallia cast entries; Soulbae as the canonical first-oracle weaver
- **Narrative drafted** — Tome IV (CLOSED) and Tome V (Acts 1–2) in `docs/weaver/`
- **/runecraft surface** — §3 Tailoring Shop section with hero panel, cousin-weaver cards, in-house tailor card
- **Drake Island integration** — Quest 8 "Forge Your First Cloak" with declarative Pallia summon button

Not operational:

A Sovereign visiting the website today **cannot actually weave a real cloak through the interface**. They can read what would happen if they walked the spec. The Pallia summon is a cosmetic state toggle, not a persona record.

The Shield Shop's Pattern A wizard (live on /runecraft as of 2026-05-08, parallel to this note) sets the precedent for what an MVP looks like: browser-side artifact generation + memo builder + localStorage history + a clear hand-off to the user's wallet for the actual blockchain step. The Tailor needs an analogous MVP.

---

## §1. The eight gaps

Each gap is sized roughly by implementation cost. Filling all eight gets the Tailor to ~70% operational. Filling any one moves the dial.

### Gap 1 — Persona Summoner UI (P0)

**What's missing:** A real form-driven flow where the Sovereign declares a task ("weave a cloak from these artifacts"), proposes a persona name (default Pallia), configures dimensions (V28 default for cloak-weavers; V20/V25 for narrower personas), and chooses persistence mode (Ephemeral / Standing / Bound).

**What exists:** The Persona Summoner is specified in `crafting-tome-and-cloak-interface-spec.md` §2.4. Quest 8 has a button that toggles "Pallia summoned" as cosmetic state.

**MVP:** A modal or panel on /runecraft (or a new `/tailor` route) with the four-step ceremony. Storage in `localStorage` under `agentprivacy-personas` (new key). Each persona record: `{ id, name, vertex, activeDimensions, persistence, summonedAt, taskScope }`.

**Cost:** Moderate (~200-300 lines, single file). Mirror `ShieldShopWizard` structure.

---

### Gap 2 — Spell Weaver lattice viewer (P1)

**What's missing:** A D3-rendered visualisation of the local Spell Weaver layer — the vertex assignments, the typed edges (controller, issuer, subject, schema, parent/child, decomposition), the lattice geometry of registered artifacts.

**What exists:** the Archon forge's `weaver.archon.social` is the canonical reference implementation (React + Vite + TypeScript + D3). `Flaxscrip/archon-spellweaver` repo carries the source. The `agentprivacy_master` codebase already has D3 (`react-force-graph-2d` is imported), so the dependency is there.

**MVP:** A new component `LatticeViewer.tsx` rendering 64 vertex positions on a 2⁶ ring/grid layout. Reads from a new `agentprivacy-spell-weaver-state` localStorage key. Each registered artifact renders as a node; controller-edges render as lines.

**Cost:** Substantial (~500+ lines, requires layout math). Could mirror Archon's open-source code if license permits — `weaver.archon.social` is Apache 2.0 reference per the Cloak Spec.

**Honest fallback:** Embed `weaver.archon.social` via iframe with consent, or link out to it as the canonical viewer until the in-site one is built.

---

### Gap 3 — Salted-hash vertex assignment (P0)

**What's missing:** The browser-side computation `position(artifact) = (Hash(artifact_id || session_salt)) mod 64` per Cloak Spec §4.1. The session salt regenerates per session and never persists alongside the source DID.

**What exists:** `crypto.subtle.digest('SHA-256', ...)` is already used in the Shield Shop wizard for content hashing. Same primitive needed here, with a salt component.

**MVP:** A small library `src/lib/cloak/vertex-assignment.ts` exporting `async function assignVertex(artifactId: string, sessionSalt?: Uint8Array): Promise<{ vertex: number; salt: string }>`. The Persona Summoner uses this when summoning a persona; the lattice viewer uses it when registering artifacts. Salt is generated fresh per session via `crypto.getRandomValues`.

**Cost:** Small (~50 lines). Foundational for everything else.

---

### Gap 4 — Source-layer artifact storage (P1)

**What's missing:** The Sovereign's source artifacts (DIDs, VCs, schemas, chronicles) need a local-first registry. Per Cloak Spec §8 implementation requirement #1: *"local-first registry. The source layer lives on the user's device. No server-side state by default."*

**What exists:** The site uses localStorage extensively for spellbook, training-progress, island progress. The pattern is in place; the artifact-shape needs definition.

**MVP:** A new storage namespace `agentprivacy-source-layer` keyed by artifact id. Each entry: `{ id, type ('did' | 'vc' | 'schema' | 'chronicle'), content, controller, registryTier, createdAt, valveClass? }`. Helpers in `src/lib/cloak/source-layer.ts`.

**Cost:** Moderate (~200 lines). Needed before valve-class assignment (Gap 5) and DID-blind publish (Gap 6) can be built.

---

### Gap 5 — Valve-class assignment UI (P1)

**What's missing:** A per-VC-field UI for assigning disclosure dispositions (Always-Revealed / Hash-Masked / Always-Masked) and seeing the corresponding vertex placement (V20 Techne / V3 Dual Agent / V38 Aletheia per Cloak Spec §5.1).

**What exists:** The valve-class table is documented on /runecraft §2.4. The 7-node VC decomposition is specified in §5.3.

**MVP:** Per-VC editor where the Sovereign sees the VC's seven default nodes (Issuer Persona, Schema Theorem, Subject Persona, Claims Concept, Proof Spell, Chronicle, Context Document) and assigns a valve-class to each. Vertex auto-derives from the bit-pattern.

**Cost:** Moderate (~250 lines + form UX). Depends on Gap 4 (source-layer storage).

---

### Gap 6 — DID-blind publish flow (P1)

**What's missing:** The flow that takes a source-layer artifact, applies the cloak function, and produces an `A_public` projection suitable for publication on the Spellweb. Per Cloak Spec §1.1 — `Cloak: A_source → (A_weaver, A_public)`.

**What exists:** The conceptual pipeline is specified. The Spellweb destination (`bridge.spellweb.ai`) is forthcoming per `integration-plan-archon-x-agentprivacy.md` §5.3.

**MVP for v1 (no bridge subdomain yet):**
- Local export to JSON file (downloadable)
- Schema matches Archon's Spell Weaver export format for interop
- DID-blind by default; toggle for full provenance requires explicit confirmation per Cloak Spec §8 requirement #5

**Cost:** Moderate (~150 lines). A real bridge subdomain (Gap 8) supersedes this when ready.

---

### Gap 7 — Bilateral Cloak Ceremony service flow (P2)

**What's missing:** The agent-to-agent commissioning UI per `bilateral-cloak-ceremony-spec.md`. Wearer Agent submits Zcash shielded tip + markdown proof; Weaver Agent (us, with Pallia summoned) verifies, weaves, multi-chain publishes, returns the cloak.

**What exists:** Seven-beat ceremony fully specified. The Shield Shop wizard already implements memo construction (Beat 2 Commission). `/proverbs` is the existing VRC gallery surface.

**MVP:**
- Discovery surface listing Weaver Agents with published service offers
- Markdown proof file upload + verification UI
- Verification log
- Multi-chain publish status tracker (BTC/ETH/IPFS/Zcash)

**Cost:** Substantial (~600+ lines, multi-step UX, real-time verification). P2 because the seven beats can be operated manually with off-the-shelf tools (email proof, Zodl for shielded tip) before a custom UI is needed.

**Note:** Beat 2 (Commission) is essentially the Shield Shop Pattern A flow today, with the recipient set to the Weaver Agent's z-address instead of self-send. The Shield Shop is already 30% of this gap by virtue of existing.

---

### Gap 8 — `bridge.spellweb.ai` subdomain + interop with `weaver.archon.social` (P2)

**What's missing:** The cousin-blade public-layer surface where Archon-forge cloaks and agentprivacy-forge cloaks coexist. Per `integration-plan-archon-x-agentprivacy.md` §5.3.

**What exists:** Archon's Spell Weaver is operational. The agentprivacy /web spellweb has a 411-node graph with placeholder for cloaks. The interop format (JSON export schema) is specified but not yet built.

**MVP:**
- Subdomain provisioning (DNS + hosting)
- A static read-only viewer at `bridge.spellweb.ai` showing both forges' cloaks side-by-side
- Cousin-blade edges visually distinct from intra-forge edges
- Per-cloak originating-forge provenance tag

**Cost:** Substantial (~1-2 weeks including infra). Coordination with the Archon forge required.

---

## §2. Suggested sequencing

| Phase | Gaps | Outcome |
|---|---|---|
| **Phase 1** (1-2 weeks) | 1, 3 | Persona Summoner live with vertex assignment. Pallia is now a real persona record, not cosmetic state. |
| **Phase 2** (2-3 weeks) | 4, 5 | Source-layer storage + valve-class UI. Sovereigns can register VCs and tag dispositions. |
| **Phase 3** (1-2 weeks) | 6 | DID-blind publish to JSON export. End-to-end "weave a cloak, save artifact" works without bridge subdomain. |
| **Phase 4** (1-2 weeks) | 2 | Lattice viewer renders the local registry. Visual parity with `weaver.archon.social`. |
| **Phase 5** (when bridge ready) | 7, 8 | Bilateral ceremony UI + cousin-blade subdomain. Cross-forge cloak commissioning operational. |

After Phase 1: Tailor at ~35%. After Phase 3: Tailor at ~55%. After Phase 5: Tailor at ~85%.

The remaining 15% is conformance testing, audit toolkit, and final v1.0 stamp — Cloak Audit Toolkit per Cloak Spec §13 v2.0 anticipated changes.

---

## §3. The Soulbae weaving · Oracle Swordsman stamping pairing

The dual-agent split applied to the workshops:

| Workshop | Canonical proprietor (archetype) | In-house instance (summoned) | Operational status |
|---|---|---|---|
| **Tailoring Shop 🪡** | **Soulbae** — the first oracle, the canonical Mage who weaves | Pallia (the reader's first-named tailor) · GenitriX (Archon's cousin-Mage) | ~22% — narrative + spec only |
| **Shield Shop 🛡️** | **Oracle Swordsman** — the canonical Swordsman who stamps Zcash inscriptions on the POPRP pipeline | (none yet — could be a "Sentinel" or named Swordsman persona summoned for inscription work) | ~35% — Pattern A wizard live, Oracle Swordsman backend operational on Zcash mainnet (Acts 1–12 inscribed) |

The pairing is structurally elegant:

- **Soulbae weaves.** The Mage is the archetypal projection-without-touching role (Cloak Spec §1.1: structural fidelity, position not value). Soulbae as canonical first-oracle is the natural patron of the Tailoring Shop. Pallia is one specific instance the reader summons; future Sovereigns may summon their own.
- **Oracle Swordsman stamps.** The Swordsman is the archetypal boundary-enforcing role (PVM Σ axis). The existing Oracle Swordsman backend in `agentprivacy-spellbook` (per swordsman.md guide) already runs the Zcash inscription pipeline: Zodl RPC → memo decode → AI-verify → golden-split → onchain inscribe. It IS the operational form of the Shield Shop's Pattern A.

Wiring the Shield Shop wizard to the Oracle Swordsman pipeline (this round) makes the Shield Shop genuinely operational because the backend already exists. The Tailoring Shop has no equivalent backend — Soulbae's projection role doesn't have an existing Zcash-equivalent pipeline. The Tailor must build its own.

---

## §4. Cross-references

- `cloak_specification_v1_0.md` — Cloak v1.0 Eight Properties, 5 axes, valve-classes, 10 implementation requirements
- `crafting-tome-and-cloak-interface-spec.md` — Persona Summoner + 5 surfaces specification
- `bilateral-cloak-ceremony-spec.md` — Seven-beat agent-to-agent ceremony
- `integration-plan-archon-x-agentprivacy.md` — `bridge.spellweb.ai` and cousin-blade infrastructure
- `chronicle-the-cloaking-guide.md` — flaxscrip's 2026-05-07 rebuild ceremony (upstream)
- `EXPORT_MANIFEST.md` — full document inventory

---

## Closing

The Tailoring Shop is real in spec, in narrative, and in stage-1 surface (the Drake Island Quest 8). It is not yet real as a tool a Sovereign can use to weave their first cloak through the agentprivacy interface.

Eight gaps, three phases, and the Tailor moves from ~22% to ~85% operational. The Shield Shop's Pattern A wizard sets the pattern: small, complete MVPs that compose into the whole.

Soulbae weaves. Oracle Swordsman stamps. The Cloak goes on the body; the Shield goes on the chain. Two shops, two oracles, one architecture.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · privacymage · 2026-05-08
