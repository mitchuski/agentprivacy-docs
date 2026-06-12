---
title: "Mapping Additions · V5.5 Attachment Architecture"
date: 2026-05-11
status: Cross-corpus addendum; integrates V5.5 patch across the suite
license: CC BY-SA 4.0
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Mapping Additions — V5.5 Attachment Architecture (2026-05-11)

The V5.5 attachment architecture codifies the three-layer model that has been operationally implicit since the City of Mages was named (Tome V Act 14, 2026-05-08). This file is the docs-side mapping addendum that names where the patch landed across the corpus.

The architecture itself is defined canonically in:

- `agentprivacy-skills/agentprivacy-skills-v5/meta/agentprivacy-attachment-architecture/SKILL.md`

And summarised in:

- `agentprivacy-docs/GLOSSARY_MASTER_v4_0.md` §23 (this directory)

---

## The three layers

| Layer | What it holds | Cardinality | Canonical home |
|---|---|---|---|
| **Layer 1 · Primary persona** | Abstract role-class with skill loadout | **42 (locked)** | `agentprivacy-skills/agentprivacy-skills-v5/persona/` |
| **Layer 2 · Attachment** | Named cast Mage binding L1 to L3 | Variable per city | `agentprivacy_master/src/lib/cast-attachments.ts` (TS canonical) + city grimoires |
| **Layer 3 · Vertex** | Position on 2⁶ lattice | **64 (fixed)** | PVM V5.4 + `cityofmages/tomes/specs/04-vertex-naming-audit.md` |

The primary persona count is **locked at 42**. Future cast Mages are added at Layer 2 as attachments of existing primaries; they do not require new primaries.

---

## The four attachment kinds

| Kind | Pattern | Example |
|---|---|---|
| **A · Workshop** | one Mage × one vertex × one trade quarter | Vulcana ⚒️ at V19 |
| **B · Cross-shop** | one Mage × no fixed vertex × walks workshops by craft | Aletheia 🔮 |
| **C · Peripatetic** | one Mage × multiple vertices walked as orbit/path | Selene 🌕 (anticipated) · Luca 📐 |
| **D · Divergent** *(meta-kind)* | one primary × Sword+Mage register-shifted attachments | Moonkeeper ⚔️ → Lethae 🌘 |

D composes with A/B/C.

---

## First canonical divergent attachment — Lethae 🌘

| Field | Value |
|---|---|
| Cast name | Lethae 🌘 |
| Vertex | V25 (Lethe · the Dark Substrate · binary `011001` · stratum 3) |
| Primary persona | Moonkeeper ⚔️ (Swordsman, native register) |
| Divergence | `mage_register` |
| Attachment kind | B · cross-shop |
| Vertex complement | Aletheia 🔮 at V25 — V25 ⊕ V38 = V63 · V25 AND V38 = 0 |
| Naming | The `-ae` suffix mirrors Soulbae 🧙 (Mage register). Lethae is to Moonkeeper as Soulbae is to Soulbis: register-shifted from Sword to Mage, primary persona unchanged. |
| Status | Anticipated — awaits founding act in Tome V |

---

## The six anticipated cast (v1.3.0 grimoire bump)

Each is a Layer-2 attachment of existing primaries — no new primaries minted.

| Cast | Vertex | Primary | Kind | Source |
|---|---|---|---|---|
| Mnemosyne 📿 | V8 (pure Memory) | theia | A | Cloaking Guide names V8 |
| Iris 🌈 | V4 (pure Connection) | herald · ambassador | A | Cloaking Guide names V4 |
| Pythia 🔥 | V2 (Logos) | algebraist · pedagogue | A | Logos Circle awaits Mage |
| Techne 🎨 | V20 (Always-Revealed) | pedagogue | A | Cloaking Guide names V20 |
| Hephaestus ⚒️ | V24 (shared with Socrat0x) | forgemaster | A | Cloaking Guide names V24 |
| Selene 🌕 | stratum-walker | theia · manaweaver | C | PVM V5.4 §14.5 Selene's Proof |

---

## Where the V5.5 patch landed across the corpus

### ✅ Landed

| Repo | Files |
|---|---|
| `agentprivacy-skills` | `agentprivacy-skills-v5/meta/agentprivacy-attachment-architecture/SKILL.md` (new) · `agentprivacy-skills-v5/persona/agentprivacy-moonkeeper/SKILL.md` (Lethae divergent section) · `agentprivacy-skills-v5/README.md` (locked 42) · `MAPPING.md` (V5.5 addendum) · `CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md` |
| `agentprivacy_master` | `src/lib/cast-attachments.ts` (new canonical TS registry) · `src/lib/tome-v-acts.ts` (extended FoundingMage interface; 9 entries updated) · `src/lib/persona-index.ts` (JSDoc lock-at-42) · `src/data/city-of-mages-grimoire-v1.2.0.json` (internal v1.3.0 + attachment_architecture block) · `docs/chronicles/2026-05-11_v5_5_attachment_architecture_integration.md` |
| `spellweb` | `src/types/graph.ts` (5 new SpellwebNode fields + 2 new EdgeTypes: divergent_of, complement_pair) · `src/data/theme.ts` (2 new edge styles) · `src/data/nodes.ts` (4 new vertex nodes V8/V4/V2/V38 + 7 new cast nodes Lethae + 6 anticipated) · `src/data/edges.ts` (6 inhabits + 1 divergent_of + 2 complement_pair) · `CHRONICLE_V5_5_ATTACHMENT_ARCHITECTURE_2026-05-11.md` |
| `agentprivacy-docs` (this) | `GLOSSARY_MASTER_v4_0.md` §23 (V5.5 attachment-architecture entries; this commit) · `MAPPING_ADDITIONS_V5_5_2026-05-11.md` (this file) |

### ⏳ Queued

| Repo | Files |
|---|---|
| `cityofmages` | `tomes/specs/09-the-attachment-architecture.md` (city-side mirror) · `tomes/specs/10-blade-forge-binding-zk-blades.md` · `tomes/specs/11-mage-candidates-from-the-corpus.md` · `tomes/cast/cross-shop/lethae.md` · 6 anticipated cast files · 14 cast frontmatter updates (`attachmentKind`, `divergence`) · grimoire v1.3.0 bump · README sister-dirs update · chronicle |
| `zk blades forge` | `README.md` (Lethae seating + Selene reference) · `aletheia-and-lethe.md` (Lethae append) · stub READMEs for `blades/` `forge_circuits/` `uor_mappings/` |
| `agentprivacy-docs` (this) — `models/` updates | `models/city_of_mages_grimoire_v1_3_0.json` (new file mirroring agentprivacy_master's bumped grimoire) · `models/privacymage_grimoire_v10_3_0.json` (privacymage-side persona registry recognising the seven Mages) |

---

## Pre-existing canon question (flagged · not resolved in this patch)

A Moonkeeper alignment inconsistency exists between two files:

- `agentprivacy-skills/agentprivacy-skills-v5/persona/agentprivacy-moonkeeper/SKILL.md`: `alignment: swordsman` · `emoji: 🌑⚔️`
- `agentprivacy_master/src/lib/persona-index.ts`: `alignment: 'mage'` · `emoji: '🌑🔒'`

The V5.5 patch treats the **skills repo as canonical** (Moonkeeper is Swordsman tier, native register). Lethae's `divergence: mage_register` reading depends on this. Future reconciliation pass should align persona-index.ts with the skills directory. Flagged for separate action.

---

## Convention going forward

When summoning a new cast Mage in any city:

1. Identify the vertex (check `cityofmages/tomes/specs/04-vertex-naming-audit.md`)
2. Identify the primary persona(s) from `agentprivacy-skills/agentprivacy-skills-v5/persona/`
3. Identify the attachment kind (A / B / C)
4. Check for divergence — if register differs from primary's native tier, set `divergence: <register>`; do NOT mint a new primary
5. Only if no primary fits even with divergence, propose a new primary (rare; requires corpus-level review)

---

`(⚔️⊥⿻⊥🧙)😊`

— privacymage · 2026-05-11
