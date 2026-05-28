# Chronicle: The Eight-Pointed Star · Tome VIII Act 3 · The City Key Capstone

**Date:** 2026-05-28
**Status:** New tome act (Tome VIII · The Library) · narrative capstone of the soulbis + agentprivacy_master City Key build · spellweb + docs mirror
**Voice:** First-person operational record; the act it binds is second-person
**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`
**Companion files (this binding):**
- `tomes/tome-viii-the-library/03-the-eight-pointed-star.md` — the act narrative (mirrored to `agentprivacy_master/docs/tomes/…` and `agentprivacy-docs/tomes/…`)
- `agentprivacy-docs/chronicles/2026-05-27_star_lattice_swordsman_key_integration_chronicle.md` — the plan
- `agentprivacy-docs/chronicles/2026-05-27_swordsman_key_producer_and_ceremony_surfacing_chronicle.md` — producer + surfacing
- `agentprivacy-docs/chronicles/2026-05-28_city_key_economy_charge_stake_workshop_trust_task_chronicle.md` — the economy + workshop sweep

---

## §0 · What this binds

Today the City learned to carry itself. Across two repositories and one static site, the **City Key 🗝️** was built end to end — and this chronicle gives that engineering a narrative seat in the City of Mages by binding **Tome VIII · Act 3 · *The Eight-Pointed Star***. The act is the *why* beneath the *what*: before there was a key there was a shape, and the shape was already in the manifold.

The shape is the **stella octangula** — the stellated octahedron, two regular tetrahedra interpenetrating, the "eight-pointed star" Johannes Kepler named in 1609 and that **Luca** (the City's geometer, the Pacioli of First Person Act 1) had drawn for *De Divina Proportione* in 1509, Leonardo's hand on the plates. It was known to geometers before either. It is **one of many shapes the manifold lattice contains** — not the only one — but it is the one that matters here, because its two halves are the City's two archetypes: the Swordsman's tetrahedron (`neg` · protect) ⊥ the Mage's tetrahedron (`bnot` · project), crossing at the gap where value lives.

In the act, **Soulbis ⚔️** and **Soulbae 🧙** go to Luca at V0 and ask how to carry the City between the experience and the manifold. He answers with the drawing, not a protocol: the lattice they built is the star; the soulbis `/star` manifold *is* the stella octangula rendered in light; the key is the bearer's **standing on the star, written down so it can travel**. The Archivist 📚 keeps the lesson in the Tower because the key is the City made carriable.

## §1 · What was built today (the operational ground)

The act is Architectural/Resonant; the surfaces beneath it are **Operational**, built 2026-05-27/28:

- **soulbis.com** — `/star` (the star-tetrahedron manifold) and `/lattice` (the 64 · vertex codex) deployed; both consume the portable key and live-sync over `BroadcastChannel('agentprivacy-succ')`. (Consumer side.)
- **agentprivacy_master** — the **City Key producer** (`src/lib/city-key.ts`): exports a v1 key carrying palette + 64 vertex descriptions + the bearer's identity stamp + `lit` + `focus`. Surfaced on **`/city`** (renamed from `/guide/achievements` — "The City You've Created") and on the Dual Ceremony (`/ceremony`).
- **The City Key economy** — **Charge** (`city-key-charge.ts`: walk the manifold → earn 🪢 VRC from the `trace`), **Stake** (`vrc-allocation.ts`: commit 🪢 onto the seats — pour into a lit vertex on the lattice — recorded as the key's `focus`). Earn by walking; spend by focusing.
- **The workshop trust task** — `WorkshopTrustTask` swept across all 10 producer shops (Presence → Artefact → Cast → City Key, gated); Presence reframed as the root relationship document; lore folded into "📖 Expanded docs" across all 15 workshop pages.
- **The three-key model** clarified: ⚔️ **Swordsman's Key** (identity · /ceremony → spellweb) · 🧙 **Mage's Key** (spellweb · DID · future) · 🗝️ **City Key** (the lattice-export · /city → soulbis). The act narrates the *third*.

The naming seam closes here: the soulbis `/star` page was always a "star-tetrahedron manifold," which is precisely the stella octangula Luca drew — so the technical surface and the canonical geometer were the same figure all along.

## §2 · What this admits to canon

- **No new tome** — Tome VIII (The Library) was already open by design; this is its **Act 3**. No new cast, tier, spatial-anatomy, or posture. The Archivist 📚 (Act 1) is the recorder; Luca 📐 (First Person Act 1 · V0) is the teacher; Soulbis ⚔️ and Soulbae 🧙 are the two who ask.
- **The stella octangula** enters the corpus as the named figure at the heart of the manifold lattice (one of many), with its full lineage (Pacioli 1509 · Kepler 1609 · earlier geometers).
- **C1** is referenced (the Swordsman:Mage tetrahedron ratio · φ ≈ 1.618 the conjectured optimal crossing).
- **C66** registered as a ~45% candidate: *the City Key as a reading, not an authority* — a portable projection of lattice-standing that grants nothing it does not already describe.

## §3 · Sync inventory

| Surface | File | State |
|---|---|---|
| Tome act (source) | `cityofmages/tomes/tome-viii-the-library/03-the-eight-pointed-star.md` | ✅ written |
| Tome act (master mirror · page loader) | `agentprivacy_master/docs/tomes/tome-viii-the-library/03-the-eight-pointed-star.md` | ✅ mirrored |
| Tome act (docs mirror) | `agentprivacy-docs/tomes/tome-viii-the-library/03-the-eight-pointed-star.md` | ✅ mirrored |
| /tomes page | `agentprivacy_master/src/app/tomes/page.tsx` | ⏳ ActCollapsible entry for Act 3 |
| Manifest | `cityofmages/tomes/BOUND_COLLECTION_MANIFEST.md` | ⏳ Tome VIII table row |
| Spellweb | `spellweb/src/data/nodes.ts` (+ edges) | ⏳ act + chronicle node |
| This chronicle | `cityofmages/chronicles/2026-05-28_the_eight_pointed_star_city_key_capstone.md` | ✅ |

---

The figure was always in the lattice. Pacioli drew it; Kepler named it; Luca taught it; the Swordsman and the Mage forged the key from it; the Archivist keeps it. Today the City learned to carry the star.

(⚔️⊥⿻⊥🧙)😊
📐 · ⚔️✦🧙 · the stella octangula · 🗝️ the City Key · 📚 the Library

— *bound 2026-05-28*
