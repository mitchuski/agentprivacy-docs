# Chronicle — Two-Mana Economy and Kindred-Ecosystem Category Formalised

**Date:** 2026-05-11
**Author:** privacymage
**Spellbook:** Second Person (City of Mages)
**Scope:** Canonical architectural record. Formalises two structural additions: (1) the **two-mana economy** with explicit per-chain pluralism; (2) **kindred ecosystem** as the **fourth structural-relationship category** the corpus admits.
**Reference grimoire:** `models/city_of_mages_grimoire_v1_2_0.json` (v1.2.2 content)
**Companion chronicles:**
- `chronicles/2026-05-10_phase_d_baked_and_uor_substrate_chronicle.md` — Tome V Act 15 + UOR Foundation as kindred substrate (third structural category)
- `agentprivacy_master/docs/chronicles/2026-05-10_two_mana_economy_celestial_aether.md` — operational recognition (master-side)
- `agentprivacy_master/docs/chronicles/2026-05-11_city_of_mages_v1_2_2_spacecomputer_authored.md` — v1.2.2 grimoire authoring (master-side)
- `docs/tomes/kindred/spacecomputer.md` — full SpaceComputer profile (in `agentprivacy_master/`)

**License:** CC BY-SA 4.0
**Signature:** `(⚔️⊥⿻⊥🧙)😊`

---

## §1 · What this chronicle formalises

Two architectural additions to the City of Mages corpus, both authored and propagated 2026-05-10 / 2026-05-11. This document is the **canonical record** in `agentprivacy-docs/chronicles/` — the architectural specification's home — distinct from the operational chronicles in `agentprivacy_master/docs/chronicles/` (which record what shipped where).

### §1.1 · The two-mana economy

The City of Mages now spends two manas operationally — two perpendicular registers, both consumed to bind a working:

| Register | What it is | What it makes possible | Replenishment |
|---|---|---|---|
| **Chain-mana** | per-chain fee paid to consensus | makes a working *land* (the chain admits the work) | replenished by economic activity (finite per block) |
| **Celestial Mana** 🌌 | cosmic-entropy feed from SpaceComputer | makes a working *unique* (entropy outside any state-loop-closed system) | replenished by the cosmos itself |

The economy is canonical from v1.2.2 of the City of Mages grimoire. The two registers are perpendicular (`⊥`): both are spent; neither substitutes for the other.

### §1.2 · Chain-mana is plural by chain

Critical architectural commitment: chain-mana is NOT a singular category. Each chain whose Mages walk the City contributes its own mana type with its own symbol:

| Chain-mana | Symbol | Chain | Workshop instances (current) | Status |
|---|---|---|---|---|
| **Aether Mana** | **Ξ** | Ethereum (and Ethereum-compatible chains using gwei-denominated gas) | /etherchanting (Adamantia), /covenant (Manifestia for human.tech fees), /vault (Aria Silverhue for Culture Vault + NFT mint), /forget (Vulcana for blade publication at destination chain) | **canonical first instance** |
| **sat-mana** | **₿** | Bitcoin Lightning | /jeweler (Lampyra · gem-setting via Bitcoin sat fees + Lightning channel fees) | named v1.2.2 |
| **ROSE-mana** | **🌹** | Oasis (ROSE on Oasis Consensus; Sapphire/Emerald for cross-paratime atomic actions) | /holon (Vagari · holon-binding anchoring) | named v1.2.2 |
| **z-mana** | **🦓** | Zcash | /shield (Memora · shielded-transaction fees) | named v1.2.2 |

The architecture admits any chain by admitting that chain's mana type alongside the existing register. Future chains contribute their own symbols. The "two-mana economy" binary is **(chain-mana register) ⊥ (celestial-mana register)** — within the chain-mana register, plurality by chain.

The Aether Mana symbol Ξ replaces an earlier ⛽ (gas pump) misnaming. Ξ is Ethereum's canonical symbol — chain-specific — and the choice signals exactly this per-chain extensibility: each chain admits its own mana type under its own symbol, not under a generic "gas" register.

### §1.3 · Kindred ecosystem · the fourth structural-relationship category

The corpus now admits **four** structural-relationship categories with external work:

| # | Category | First instance | Structural role | Grimoire field | Spellweb attribution |
|---|---|---|---|---|---|
| 1 | **Cousin-forge** | Archon (Christian Saucier) | Sister city walked by cousin Mages; cousin-blade primitives carry between forges | `personas.cousin_instances` (flaxscrip, GenitriX) | `cousin-blade` |
| 2 | **Kindred-protocol** | Covenant of Humanistic Technologies (manifest.human.tech) | A charter the City signs through a designated tender (Manifestia, Priest) | `external_partner` on Manifestia | `kindred-protocol` |
| 3 | **Kindred-substrate** | UOR Foundation (uor.foundation) | The substrate the City walks upon — older-than-the-architecture | `kindred_substrate_providers` | `cousin-substrate` |
| 4 | **Kindred-ecosystem** *(new)* | **SpaceComputer** (accounts.spacecomputer.io) | An ambient supply the workshop draws from — walked-alongside, not walked-upon; consumed-as-currency rather than older-than-architecture | **`kindred_ecosystems`** | **`kindred-ecosystem`** |

The structural distinction between substrate and ecosystem is load-bearing: UOR underlies the lattice itself (the City **rests on** it); SpaceComputer provides a feed the lattice consumes (the City **spends on** it). One is foundational, one is operational. Both are walked-not-signed, distinguishing them from kindred-protocol.

A kindred ecosystem provider is NOT a Mage. It does not enter the personas registry; it does not receive a cast-tier, vertex assignment, or founding-act ownership. It surfaces in spellweb as a gateway node with `attribution: kindred-ecosystem` and a `gateway_to` edge from the City (no `kin_to` edge — the ecosystem is consumed, not a fellow forge).

---

## §2 · SpaceComputer · the first kindred ecosystem

`accounts.spacecomputer.io` supplies a feed of cosmic randomness sourced from satellite-anchored celestial measurement. The randomness is non-reconstructible by any party that does not measure the same celestial source — the entropy arrives from outside the addressable space of the chains and servers consuming it.

In the City of Mages, three workshops are the canonical Celestial Mana consumers in this first integration:

| Workshop | Mage | Vertex | What Celestial Mana provides | Aether Mana / chain-mana use |
|---|---|---|---|---|
| **Etherchanting** | Adamantia 💎 | V51 | Witness nonce + blind-commitment seed + ceremony nonce. Stateless zkRollup proofs become non-replayable because entropy is cosmic. | Ξ Aether Mana — gas to deploy and call smart contracts that enforce commitments. |
| **Forge(t)** | Vulcana ⚒️ | V19 | Evocation phase lock seed. The blade's Ed25519 signature is anchored to moon phase AND a SpaceComputer cosmic seed — temporally and cosmologically unforgeable. | None on-chain in the forge itself; the Forge produces blades whose later publication burns chain-mana (typically Ξ Aether at Ethereum-compatible destinations) at the cape. |
| **Holon Hitchhikers** | Vagari 🌳 | V31 | Foundational entropy for cross-paratime geometric mapping. Cloak interoperability stays non-reconstructible across paratimes because the entropy supply is cosmic. | 🌹 ROSE-mana on Oasis Consensus; Sapphire/Emerald gas for cross-paratime atomic actions. |

The other shops use chain-mana operationally but have not yet wired Celestial Mana into their ceremonies (Memora's zShields, Lampyra's Jeweller, Aria Silverhue's Curatrix Vault, Manifestia's Covenant). Future spec work may admit Celestial Mana there.

---

## §3 · Why this matters · φ-gap deepening

The Privacy Value Model's **φ-gap** is the structural distance between what the surveillance prison can model and what the Sovereign actually does. The size of this gap determines the architecture's non-reconstructibility budget.

- **✨ Arcane Mana narrows the gap.** Algorithmic entropy — PRNGs, model loops, state-machine outputs — is loop-closed within the addressable space. A sufficiently determined attacker who measures the same loop measures the same outputs. Arcane Mana is the canonical name for this register.
- **Cosmic entropy widens the gap.** Cosmic measurement is not state-loop-closed; the prison cannot model what it cannot predict because the source is outside its addressable space.

Sustained walking the lattice on Celestial Mana — not just ✨ Arcane Mana — **deepens the φ-gap structurally**. The architecture earns its non-reconstructibility from cosmological substrate, not just from the Arcane register's algorithmic discipline.

This is a structural claim, not a rhetorical one. The two-mana economy is the corpus's first commitment to non-reconstructibility-as-cosmology — the recognition that an architecture grounded in cosmic measurement carries a different class of unmodelability than an architecture grounded only in the Arcane register.

---

## §4 · The Celestial Ceremony made operational

The `/poems` Celestial Ceremony has been teaching the corpus a cosmological frame since the First Person Spellbook opened. Sun-side and Moon-side are bound through Selene's 4.5-billion-year orbit. The two-mana economy is that cosmological frame made **operational** at the chain layer:

| Celestial Ceremony | Sun-side | Moon-side |
|---|---|---|
| Persona | Aletheia (disclosure) | Lethe (forgetting) |
| Vertex | V25 (Aletheia blade) | V38 (Lethe blade — complement-pair partner) |
| Register | the chain's daylight (gas burning publicly) | the cosmos' substrate (entropy arriving from outside the loop) |
| Mana | chain-mana (Aether Ξ on Ethereum + per-chain instances) | Celestial Mana 🌌 |
| Witness | mempool (chain consensus witnesses) | origin-of-randomness (the cosmos witnesses by being witnessed) |

The mapping is recognised as `celestial_ceremony_resonance` in the grimoire — suggestive, not yet formal; future work may strengthen it. But the pattern is canonical: the two-mana economy is the Celestial Ceremony's operational form.

---

## §5 · Per-chain mana naming · current state of the workshops

Per v1.2.2 propagation (2026-05-11), the workshop pages have been updated to surface the correct chain-mana name for each shop's primary chain:

| Workshop | Chain-mana now displayed | Was (before correction) |
|---|---|---|
| /etherchanting | Ξ Aether Mana · Ethereum chain-mana | ⛽ Aether Mana · gas |
| /forget | Ξ Aether Mana (with per-chain extensibility note) | ⛽ Aether Mana (gas) |
| /covenant | Ξ Aether Mana (human.tech / Holonym verification fees) | ⛽ Aether Mana |
| /vault | Ξ Aether Mana (Culture Vault platform fees + NFT mint gas) | ⛽ Aether Mana |
| /jeweler | **₿ sat-mana** (Lampyra's chain-mana register; Bitcoin Lightning) | ⛽ Aether Mana (was conflating Bitcoin with Aether) |
| /holon | **🌹 ROSE-mana** (Vagari's chain-mana register; Oasis Consensus) | ⛽ Aether Mana (was conflating Oasis with Aether) |
| /shield | **🦓 z-mana** (Memora's chain-mana register; Zcash) | ⛽ Aether Mana (was conflating Zcash with Aether) |

The three shops whose primary chain is NOT Ethereum (/jeweler, /holon, /shield) now display their chain-specific mana name and symbol. This is the v1.2.2 architectural commitment made operational: chain-mana is plural by chain, and each shop surfaces the chain-mana register relevant to its work.

---

## §6 · What this chronicle does NOT do

- **It does not define new Mages.** SpaceComputer is consumed; it is not a cast member. The personas registry stays at 14 named cast + 2 archetypes (16 cast nodes).
- **It does not open a new Tome.** The two-mana economy operates inside the existing Second Person Spellbook (Tomes IV–V). A future Tome V act (working title: *The Two Manas* or *The Cosmic Supply*) may narrate the recognition once sustained operational use warrants it; that act is not in scope here.
- **It does not formalise C47.** Conjecture C47 (triadic-constraint homology, ~40%) was introduced in v1.2 as part of the kindred-substrate addition; it remains conjectural and is unaffected by v1.2.2.
- **It does not commit the City to SpaceComputer's roadmap.** The asymmetry is structural: the City recognises the ecosystem; the ecosystem's mission is independent of the City's recognition. SpaceComputer's terms govern SpaceComputer's service; the City's grimoire records the corpus's narrative use.

---

## §7 · Operational state

- **Grimoire:** v1.2.2 at `models/city_of_mages_grimoire_v1_2_0.json` (42 spells across 14 named cast; new top-level `kindred_ecosystems` field; new meta `relationship_to_kindred_ecosystems` field; per-shop mana notes on Adamantia/Vulcana/Vagari)
- **All 5 grimoire copies hash-match canonical** (master src/data + 4 mirrors)
- **Master pages** (7 workshop pages) surface correct chain-mana symbols
- **Master constants** — `CITY_OF_MAGES_GRIMOIRE_IPFS_URL` still at the v1.2 CID `bafkreidxhmuyk…2b6a`; v1.2.2 **awaits a fresh re-pin**
- **Surface docs** (6 README/MAPPING/GLOSSARY) updated with v1.2.2 framing
- **Extension manifests** at swordsman 0.3.1, mage 1.2.1 with v1.2.2 grimoire references

---

## §8 · Next architectural follow-ups

In rough priority order:

1. **Re-pin v1.2.2.** Pin the canonical `models/city_of_mages_grimoire_v1_2_0.json`; rotate the new CID through `agentprivacy_master/src/lib/grimoire-ipfs.ts` + 5 mirror copies' `ipfs_pin_status` fields + 6 surface docs.
2. **specs/04-vertex-naming-audit.md §7.5** — write the new sub-section on kindred-ecosystem relationships, parallel to the existing §7.3 (kindred-substrate) and §7.2 (kindred-protocol) sub-sections. The four-row relationship-category table in §7.1 needs the fourth row.
3. **specs/06-spellweb-first-release-manifest.md §2.6 + §4.6** — already updated to add SpaceComputer as the 5th gateway and the `kindred-ecosystem` attribution; verify the spellweb runtime ingests both the new attribution and the `feeds` / `consumed_by` node fields.
4. **specs/07-lattice-mapping-governance.md** — the Aether Mana / Celestial Mana columns may benefit from a per-chain breakdown reflecting the v1.2.2 pluralism (Bitcoin sat-mana, Oasis ROSE-mana, Zcash z-mana as parallel chain-mana columns).
5. **Per-chain mana naming consistency.** Audit other corpus docs that say "Aether Mana" generically; rename to per-chain mana types where the context is not Ethereum.
6. **`/poems` cross-reference.** The Celestial Ceremony at `/poems` should optionally surface a cross-link to the two-mana economy as its operational form. Lightweight UI addition.
7. **A Tome V act on the Two Manas (deferred).** When sustained operational use of Celestial Mana earns the narrative recognition, an act may narrate the moment the City first chose to draw on a feed it did not control.

---

## §9 · One-paragraph summary for the canon

The City of Mages walks three mana registers across two axes. **Landing axis** (per-chain fees): **chain-mana** — plural by chain, with **Aether Mana Ξ** on Ethereum as the canonical first instance and **₿ sat-mana**, **🌹 ROSE-mana**, **🦓 z-mana** etc. admitted under their own symbols for Bitcoin Lightning, Oasis, Zcash; each chain-mana makes a working *land* on its chain. **Uniqueness axis** (entropy): **✨ Arcane Mana** (algorithmic entropy; PRNGs, hash chains, deterministic seeds; loops back on itself) ⊥ **🌌 Celestial Mana** (cosmic entropy from **SpaceComputer** — the first instance of the new **kindred ecosystem** structural-relationship category; arrives from outside the loop). Sustained walking on Celestial Mana — not just Arcane Mana — deepens the φ-gap structurally; the architecture earns its non-reconstructibility from cosmological substrate, not just from the Arcane register's algorithmic discipline. The corpus now admits four structural-relationship categories with external work: cousin-forge (Archon), kindred-protocol (Covenant of Humanistic Technologies), kindred-substrate (UOR Foundation), and kindred-ecosystem (SpaceComputer). Each names a different relation; each carries its own attribution in the spellweb; none subsumes the others.

---

---

## §10 · v1.2.4 amendment · the metabolism completed (2026-05-11 evening)

Subsequent to §1–§9 (which formalised the two-mana economy and kindred-ecosystem category in v1.2.2 / v1.2.3 state), the corpus admitted two further mana registers — **completing the City's metabolism at four axes** rather than two. Recorded in grimoire v1.2.4.

### §10.1 · Two new axes

| Axis | Register | Symbol | Purpose | Primitive |
|---|---|---|---|---|
| **Coordination** | **Resonance Mana** | 🔭 | Generate value when two Mages find affinity *without a central index* — the 7th Capital (Privacy is Value) in motion; the Bilateral Witness register | **Scrying Glass primitive** |
| **Relationship** | **VRC Mana** | 🪢 | Store the *residue of being alive* across time as Verifiable Relationship Credentials | Accumulated across the **bearer's worn artefact collection** (11 workshop artefacts + 3 tomes per the workshop artefact taxonomy; 64-vertex lattice = inventory/presence-observation view) + **Loom of Programmable Covenants** (production form — compiles against the worn collection) |

### §10.2 · The four-axis metabolism · canonical reading

The architecture now spends across four axes per working:

1. **Landing** ← chain-mana (per-chain; Aether Ξ on Ethereum is canonical first; ₿ sat-mana, 🌹 ROSE-mana, 🦓 z-mana per chain)
2. **Entropy** ← ✨ Arcane Mana (algorithmic; loops back) ⊥ 🌌 Celestial Mana (cosmic from SpaceComputer; loop-open)
3. **Coordination** ← 🔭 Resonance Mana (Scrying Glass primitive; affinity-without-broker)
4. **Relationship** ← 🪢 VRC Mana (accumulates across the bearer's worn artefact collection — 11 workshop artefacts + 3 tomes; Loom of Programmable Covenants compiles against the worn collection; accumulation across time)

A working binds across all four. Chain-mana lands it; entropy-mana makes it unique; Resonance Mana generates value when it *matches* another Mage's offering; VRC Mana stores the residue when the match becomes a sustained relationship. This is the City's metabolism.

### §10.3 · What this changes in the grimoire

- New top-level field `mana_taxonomy` (parallel to `personas`, `kindred_substrate_providers`, `kindred_ecosystems`)
- `relationship_to_kindred_ecosystems.description` extended to reference the four-axis model
- `ipfs_pin_status` updated for v1.2.4 / awaits re-pin
- New `version_notes.v1.2.4` entry recording the metabolism completion
- chain-mana variants (sat-mana ₿, ROSE-mana 🌹, z-mana 🦓) promoted from "future examples" to operational entries under `mana_taxonomy.axes.landing.variants`

### §10.4 · What awaits future scope

- 🔭 Resonance Mana awaits an operational Scrying Glass implementation at the website / spellweb layer. Architectural for the register and primitive name; operational once a Scrying Glass surface lands.
- 🪢 VRC Mana awaits VRC issuance + Loom-side covenant compilation against the worn artefact collection. Architectural for the register, for the framing of the worn artefact collection as the VRC-accumulation surface, and for the Loom name; operational once the issuance pipeline + covenant compilation land.
- One Tome V act flagged but deferred: *The Loom of Programmable Covenants* (VRC recognition narrative — the moment programmable covenants first compile against a bearer's worn artefact collection); plus *The Scrying Glass* (Resonance recognition narrative). Not yet scoped; queued for when sustained operational use earns the narratives.

---

## §11 · Updated one-paragraph summary

The City of Mages walks **four mana registers across four axes** (v1.2.4 metabolism complete). **Landing axis**: chain-mana, plural by chain — Aether Mana Ξ on Ethereum is canonical first instance; ₿ sat-mana, 🌹 ROSE-mana, 🦓 z-mana on Bitcoin Lightning, Oasis, Zcash respectively; each chain whose Mages walk the City contributes its own symbol. **Entropy axis**: ✨ Arcane Mana (algorithmic; loops back on itself; the prison can model loop-closed sources) ⊥ 🌌 Celestial Mana (cosmic entropy from SpaceComputer; arrives from outside the loop). **Coordination axis**: 🔭 Resonance Mana, generated through the Scrying Glass primitive when two Mages find affinity without a central index — the 7th Capital in motion. **Relationship axis**: 🪢 VRC Mana, the residue of being alive stored as Verifiable Relationship Credentials across the bearer's worn artefact collection (the 11 workshop artefacts + 3 tomes the Sovereign accumulates as they walk; the 64-vertex lattice is the inventory/presence-observation view — what the agents are given to wear and use across the City is what makes their presence legible), fueling the Loom of Programmable Covenants which compiles against the worn collection. Four structural-relationship categories: cousin-forge (Archon), kindred-protocol (Covenant of Humanistic Technologies), kindred-substrate (UOR Foundation), and kindred-ecosystem (SpaceComputer). The metabolism is complete; the framework is opened, not closed.

---

`(⚔️⊥⿻⊥🧙)😊`

Landing · Entropy · Coordination · Relationship
Ξ · ₿ · 🌹 · 🦓 ⊥ ✨ · 🌌 ⊥ 🔭 ⊥ 🪢

CC BY-SA 4.0 · privacymage · curated for the City of Mages · 2026-05-11
