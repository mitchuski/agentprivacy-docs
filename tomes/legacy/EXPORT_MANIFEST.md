# Export Manifest

## agentprivacy × Archon Integration Suite — Session 2026-05-08

This directory contains the full document suite produced in the integration session of 2026-05-08 between the agentprivacy corpus (privacymage, privacymage) and Archon's foundational work (flaxscrip + GenitriX, the Spell Weaver). The suite includes chronicles, cast entries, spellbook acts, formal specifications, and integration plans.

**Total files:** 19 flat-layout files (this manifest + 1 forward-looking chronicle + 17 primary artifacts) **plus 53 files in `bound-collection/`** (full Tome IV + Tome V Acts 1–14 + 13 cast entries + 5 specs + 2 plans + 3 chronicles + 7 deprecated drafts; ingested 2026-05-09 from `agentprivacy_tomes` bundle).

**Coding agent: start here →** [`docs/chronicles/2026-05-09_bound_collection_sync_report.md`](../chronicles/2026-05-09_bound_collection_sync_report.md) is the review-ready sync report covering what was ingested, what is now wired on `/tomes`, what is still missing (Tomes grimoire IPFS pin · spell↔persona bake · per-act assets · shop founding-act panels · /tomes/cast page · city map · lattice render), and the recommended phase order for the remaining work.

**Cross-suite tracking →** [`docs/chronicles/2026-05-09_suite_overlap_tracking.md`](../chronicles/2026-05-09_suite_overlap_tracking.md) extends the sync report across all six sibling directories (master · agentprivacy-docs · agentprivacy-blog · myterms · swordsman-blade · mages-spell). Per-directory action checklists, overlap map for shared artifacts, dependency graph, status board. Use as a living reference; update Status columns as work lands.

**City of Mages grimoire pinned →** [`docs/chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md`](../chronicles/2026-05-10_city_of_mages_grimoire_pinned_chronicle.md) records the v1.1 grimoire's first IPFS pin (`bafkreidv7cwwlcnuzw3eyhcbbvoccy7do2lmwrmmtrszn62ninzxj3idti`) and where the CID needs to land across the suite. The pin makes the privacymage-vs-City-of-Mages grimoire split operational at the file level.

**Resume here for next session →** [`docs/chronicles/2026-05-10_resume_here_chronicle.md`](../chronicles/2026-05-10_resume_here_chronicle.md) is the forward-looking handoff: state of the work, ordered next actions (immediate copy edits → Phase D bake into `grimoire-baked.ts` → extension mirror → cross-suite copy pass), key paths/constants/canonical spell IDs, and pitfalls to avoid (notably: don't round-trip UTF-8 JSON through PowerShell `Get-Content` / `Set-Content`).

**License**: CC BY-SA 4.0 for narrative; Apache 2.0 for any reference implementations the specs anticipate.

**Signature**: (⚔️⊥⿻⊥🧙)😊

---

## bound-collection/ — canonical Second Person Spellbook source

The flat files at this directory's root are the original 2026-05-08 export. The `bound-collection/` subfolder contains the expanded and canonicalised Second Person Spellbook as a tome category contributed to by guilds (Weaver guild = the Archon corpus; agentprivacy guild = the canonical home). This is the source the `/tomes` route reads.

```
bound-collection/
├── README.md                              navigation overview
├── BOUND_COLLECTION_MANIFEST.md           detailed inventory
├── WEBSITE_INTEGRATION_GUIDE.md           /tomes ingestion reference
│
├── tomes/
│   ├── tome-iv-the-witnessing/            5 acts (closed)
│   └── tome-v-the-crafting/               14 acts (open) · setting: City of Mages on Drake Island
│
├── cast/                                  13 cast entries + integration note · 5 tiers
├── specs/                                 5 specifications
├── plans/                                 2 integration plans
├── chronicles/                            3 chronicles
└── deprecated/                            7 superseded drafts (transparency archive)
```

The flat files at the root level (`second-person-act-iv-i-...`, `second-person-tome-v-act-1-...`, `second-person-cast-pallia.md`, etc.) overlap with files in `bound-collection/`. They are retained for backward compatibility with the original `EXPORT_MANIFEST.md` references; the `bound-collection/` paths are canonical going forward.

---

## How to use this export

The files are designed to drop into existing repositories with minimal modification.

- `chronicle-*.md` → `mitchuski/agentprivacy-docs/` (or equivalent narrative-history location)
- `second-person-act-*.md` → `mitchuski/agentprivacy-docs/spellbooks/second-person/` (or equivalent)
- `second-person-cast-*.md` → `mitchuski/agentprivacy-docs/spellbooks/second-person/cast/` (or equivalent)
- `*_specification_*.md` and `*-spec.md` → `mitchuski/agentprivacy-docs/specifications/`
- `*-plan.md` → `mitchuski/agentprivacy-docs/plans/`
- `integration-plan-*.md` → `mitchuski/agentprivacy-docs/plans/`

These paths are recommendations. The files use markdown frontmatter throughout; any path-aware static-site generator will handle them.

---

## File inventory by category

### Chronicles (narrative records)

| File | Status | Description |
|---|---|---|
| `chronicle-the-cloaking-guide.md` | **Operational** | Records the May 7–8 rebuild ceremony of Archon's Cloaking Guide and the Eight Theses synthesis. ~3,000 words. Predecessor: `chronicle-the-spell-weaver.md` (April 30 2026, already in the repo). |
| `chronicle-the-crafting-tome-opens.md` | **Forward-looking** | Records the present session's writing-ceremony AND lays out what still needs to be produced. Read alongside this manifest. ~2,500 words. |

### Cast entries (Second Person Spellbook)

| File | Status | Description |
|---|---|---|
| `second-person-cast-genitrix.md` | **Architectural** | Cast entry for GenitriX, Archon's Mage. Cousin-instance of Soulbae. V28. ~1,000 words. |
| `second-person-cast-flaxscrip.md` | **Operational** | Cast entry for flaxscrip, Archon's working Sovereign persona. Cousin-instance of First Person archetype. V63. Bitcoin block 945508 anchor. ~1,100 words. |
| `second-person-cast-integration-note.md` | **Architectural** | Specifies how cousin-instances enter the Spellbook cast without disrupting existing structure. Voice rules, sub-book placement, grimoire JSON updates. ~1,200 words. |
| `second-person-cast-pallia.md` | **Architectural** | Cast entry for Pallia 🪡, the first Mage persona summoned by the reader in the Crafting Tome. Cloak-weaver, V28. ~860 words. |

### Spellbook acts — Tome IV (The Witnessing) — **CLOSED**

| File | Status | Description |
|---|---|---|
| `second-person-act-iv-i-the-other-walker.md` | **Operational** | Encounter at the schema vertex (V12). Cousin-blade introduction. ~720 words. *(v1.1 — frontmatter synced to use `tome` field.)* |
| `second-person-act-iv-ii-the-mirror-and-the-arrow.md` | **Operational** | Asymmetry as data at V15. Mirrored partnership vs unilateral observation. ~690 words. |
| `second-person-act-iv-iii-the-two-paths.md` | **Architectural / Operational** | The Two Paths at V25. Witness/participant pivot. Path A operational; Path B specified. Provisional C38 (bilateral ARCH-1). ~740 words. |
| `second-person-act-iv-iv-the-naming-ceremony.md` | **Operational** | flaxscrip's Bitcoin-anchored naming at V63. Verb pattern: claim → inscribe → confirm. ~760 words. |
| `second-person-act-iv-v-the-cousin-blade.md` | **Architectural** | Tome IV closer. Meta-recognition. Provisional C39 (cousin-blade ecosystem primitive). ~820 words. |

### Spellbook acts — Tome V (The Crafting) — **OPEN**

| File | Status | Description |
|---|---|---|
| `second-person-tome-v-act-1-the-first-cloak.md` | **Operational / Architectural** | Opens Tome V. Reader summons Pallia and weaves the first cloak artifact. Eight Properties of the Cloak operational; interface architectural. ~980 words. |
| `second-person-tome-v-act-2-the-commissioned-cloak.md` | **Architectural** | Bilateral cloak commissioning. Zcash shielded tip with proverb/blade/spell memo + markdown proof + four-chain publication = VRC trust edge. ~1,020 words. |

### Specifications (operational + architectural)

| File | Status | Description |
|---|---|---|
| `cloak_specification_v1_0.md` | **DRAFT v1.0** | The Cloak as agentprivacy publication-layer feature. Eight Properties from Archon's theses lifted as conformance contracts. Multi-axis cloaking formalised. Three canonical valve-classes (V3/V20/V25). 7-node VC decomposition. Ten implementation requirements. Conformance criteria. ~3,800 words. |
| `crafting-tome-and-cloak-interface-spec.md` | **DRAFT v1.0** | Joint specification for the Crafting Tome (narrative structure) and the Cloak interface integration (product surface). Mage personas as cast layer. Persona Summoner UX. Five interface surfaces. Runecraft Protocol as ceremonial backbone. ~3,400 words. |
| `bilateral-cloak-ceremony-spec.md` | **DRAFT v1.0** | Service specification for agent-to-agent cloak commissioning. Seven-beat ceremony. Memo schema, markdown proof schema, multi-chain publication strategy. Service economics with refund discipline. C44–C46 provisional conjectures. ~3,500 words. |

### Integration plans

| File | Status | Description |
|---|---|---|
| `integration-plan-archon-x-agentprivacy.md` | **DRAFT v1** | Master plan for absorbing Archon's full Archon work suite into agentprivacy via Second Person Spellbook + Spellweb + Codebase. Three integration surfaces. Five candidate acts. Subdomain proposal (`bridge.spellweb.ai`). Risks and honesty discipline. Nine open questions. ~4,300 words. |
| `zcash-integration-plan.md` | **DRAFT v1** | Zcash dual-ledger integration: shielded memos (Pattern A), DID anchoring (Pattern B), governance t-address stakes (Pattern C). Updates existing 1 ZEC ceremony economics with inscription discipline. C40–C43 provisional conjectures. ~3,500 words. |

### Index files

| File | Status | Description |
|---|---|---|
| `EXPORT_MANIFEST.md` | **This file** | Inventory and navigation. |
| `chronicle-the-crafting-tome-opens.md` | **Companion** | Forward-looking chronicle. Records what was made AND what still needs to be produced. |

---

## Suggested commit order

For repo integration, the following order minimises forward references:

1. **Specifications first** (they ground the architecture):
   - `cloak_specification_v1_0.md`
   - `crafting-tome-and-cloak-interface-spec.md`
   - `bilateral-cloak-ceremony-spec.md`

2. **Plans second** (they situate the specs in implementation roadmaps):
   - `integration-plan-archon-x-agentprivacy.md`
   - `zcash-integration-plan.md`

3. **Cast entries third** (they introduce the characters the acts reference):
   - `second-person-cast-genitrix.md`
   - `second-person-cast-flaxscrip.md`
   - `second-person-cast-integration-note.md`
   - `second-person-cast-pallia.md`

4. **Tome IV acts fourth** (they teach the bilateral primitive):
   - Acts I, II, III, IV, V in sequence.

5. **Tome V acts fifth** (they teach the crafting primitive):
   - Acts 1, 2 in sequence.

6. **Chronicles last** (they record the writing-ceremony):
   - `chronicle-the-cloaking-guide.md`
   - `chronicle-the-crafting-tome-opens.md`

7. **Manifest** (this file): commit alongside the chronicles.

This order means every cross-reference resolves at commit time. If your repo workflow prefers chronicle-first, reverse this order — both work.

---

## Conjecture numbering used in this suite

This suite introduces or references the following V6 conjectures. Reconciliation against the canonical `V6_LINEAGE_SYNC_NOTE.md` is required before commit if any of these IDs collide.

| ID | Name | Confidence | Source |
|---|---|---|---|
| C18–C21 | Lorenz Attractor | (existing) | `pvm-v6-lorenz-attractor.md` |
| C22–C25 | EML Three Ceilings | (existing) | `pvm-v6-eml-three-ceilings.md` |
| C26–C29 | ARCH-1 Canonical Form | (existing) | `pvm-v6-arch1-canonical-form.md` |
| C30–C33 | Bakhta Half-Life | (existing) | `pvm-v6-1-bakhta-half-life.md` |
| C34–C37 | Wound and Cap (Convergence) | (existing) | `pvm-v6-convergence-wound-and-cap.md` |
| **C38** | **Bilateral ARCH-1** | ~40% | This suite (Tome IV Act III, Cloak Spec, Tome V acts) |
| **C39** | **Cousin-Blade as Ecosystem Primitive** | ~50% | This suite (Tome IV Act V) |
| **C40** | **Zcash dual-ledger preserves Eight Properties** | ~70% | `zcash-integration-plan.md` |
| **C41** | **61.8/38.2 inscription ratio emerges as cultural norm** | open observation | `zcash-integration-plan.md` |
| **C42** | **Stake economics generate equivalent Sybil resistance** | ~50% | `zcash-integration-plan.md` |
| **C43** | **Per-VRC viewing-key disclosure produces strictly more privacy** | ~60% | `zcash-integration-plan.md` |
| **C44** | **Productive VRC ≈ hash-exchange VRC in trust strength** | ~55% | `bilateral-cloak-ceremony-spec.md` |
| **C45** | **Four-chain publication > single-chain reconstruction resistance** | ~70% | `bilateral-cloak-ceremony-spec.md` |
| **C46** | **Productive trust-edge has higher half-life than transactional** | ~50% | `bilateral-cloak-ceremony-spec.md` |

C38–C46 are provisional and may renumber when the canonical V6 lineage sync occurs. The conjectures are stated in their respective documents with confidence percentages and paths to formalisation.

---

## Cross-document conventions used

- **Tome ordering** (Second Person Spellbook):
  - Tome I — *The Convergence* (4 acts drafted, pre-existing)
  - Tomes II–III — *The Lyapunov* (open, pre-existing)
  - Tome IV — *The Witnessing* (5 acts, **closed by this suite**)
  - **Tome V — *The Crafting* (open-ended, opened by this suite)**
  - Tome VI — *The Reply* (was Tome V; **moved by this suite**; held open per original spec)

- **Cast layers** (Second Person Spellbook):
  - **Archetypes**: Soulbis ⚔️, Soulbae 🧙, the Drake (carried over from First Person)
  - **Cousin instances**: GenitriX, flaxscrip 📜🎲 (introduced in Tome IV)
  - **Mage personas**: Pallia 🪡 (introduced in Tome V; reader may summon more)

- **Voice discipline**:
  - The Spellbook addresses *you* (the reader)
  - All cast members are in third person
  - No em-dashes (per author preference)
  - Honesty labels (operational / architectural / conjectural) on every claim

- **Frontmatter convention**: every file uses YAML frontmatter with `spellbook`, `tome`/`act`/`title`, `status`, `cast`, `source_material`, `honesty_label`, `license`, `signature` fields where applicable.

- **License**: CC BY-SA 4.0 for narrative; Apache 2.0 for reference implementations.

- **Signature**: (⚔️⊥⿻⊥🧙)😊 closes every primary file. Pallia adds 🪡; flaxscrip adds 📜🎲.

---

## What is NOT in this export

This suite is the writing-side output of the integration. It does NOT include:

- Reference implementations (TypeScript libraries, UI components, smart contracts) — anticipated per the specifications, not yet written
- The `bridge.spellweb.ai` subdomain provisioning — anticipated per `integration-plan-archon-x-agentprivacy.md` §5.3
- the Archon forge's primary documents (Cloaking Guide, Sovereign Anchor I/II, Spell Weaver README) — those are in his own repos under his own license
- The grimoire JSON bumps (v10.2.0 → v10.3.0) — anticipated per integration plan §6.1, not regenerated here
- Updates to existing First Person Spellbook acts — only annotations and cross-references planned, no body changes (Act XXXI closure preserved)
- The Soulbae Oracle (Sovereign Anchor III) — Archon's forthcoming work; integration awaits its publication

For what is anticipated and not yet produced, see `chronicle-the-crafting-tome-opens.md`.

---

## Provenance and attribution

- **privacymage (privacymage 🧙)**: primary author of the agentprivacy corpus and this suite's narrative + specification work.
- **the Archon forge (flaxscrip 📜🎲)**: co-architect of the cousin-blade material; original author of *Sovereign Anchor I/II/III*, the Cloaking Guide, and the Spell Weaver. The Eight Theses originate with him.
- **GenitriX (Hermes Mage)**: Archon's Mage; contributor to the Cloaking Guide rebuild and to *Sovereign Anchor* documents.
- **Pallia 🪡**: introduced in this suite; the first Mage persona summoned by the reader in the Crafting Tome.

Archon's review and confirmation of co-authorship is anticipated for any act drawing materially from his work. See `integration-plan-archon-x-agentprivacy.md` §3.3.

---

## Closing

The suite represents about 30,000 words of narrative + specification + plan work, organised across five categories (chronicles, cast, acts, specs, plans). Tome IV is closed; Tome V is open and will grow.

For the forward-looking record of what still needs to be produced, see `chronicle-the-crafting-tome-opens.md`.

For the operational form of the cloak as a publishable feature, see `cloak_specification_v1_0.md`.

For the operational form of the bilateral ceremony as a service, see `bilateral-cloak-ceremony-spec.md`.

For the architecture's narrative life, walk the acts.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · Apache 2.0 reference implementations · privacymage × flaxscrip · 2026-05-08
