# The Second Person Spellbook — Bound Collection

## /tomes — Website-ready document suite

This is the **bound collection** of the agentprivacy Second Person Spellbook narrative work, prepared for inclusion on the agentprivacy website at the `/tomes` route. It contains Tome IV (*The Witnessing*, closed) and Tome V (*The Crafting*, open), along with the cast roster, the supporting specifications, the integration plans, and the chronicles that record the writing-ceremony.

**Total files**: 43 canonical documents + 7 deprecated drafts archived for reference.

**Total word count**: approximately 62,500 words of narrative + specification + plan work.

**Canonical setting of Tome V**: The First City of Mages, built upon Drake Island. Named explicitly in Act 14.

**Signature**: (⚔️⊥⿻⊥🧙)😊

**License**: CC BY-SA 4.0 for narrative; Apache 2.0 for any reference implementations the specs anticipate.

---

## Folder structure

```
bound-collection/
├── README.md                              ← this file
├── BOUND_COLLECTION_MANIFEST.md           ← detailed inventory and reading order
├── WEBSITE_INTEGRATION_GUIDE.md           ← website team's reference for /tomes ingestion
│
├── tomes/
│   ├── tome-iv-the-witnessing/            ← 5 acts, closed
│   │   ├── 01-the-other-walker.md
│   │   ├── 02-the-mirror-and-the-arrow.md
│   │   ├── 03-the-two-paths.md
│   │   ├── 04-the-naming-ceremony.md
│   │   └── 05-the-cousin-blade.md
│   │
│   └── tome-v-the-crafting/               ← 14 acts, open-ended; canonical setting: The City of Mages on Drake Island
│       ├── 01-the-first-cloak.md
│       ├── 02-the-commissioned-cloak.md
│       ├── 03-the-shielded-memo.md
│       ├── 04-the-reveal.md
│       ├── 05-the-stake.md
│       ├── 06-the-commissioned-blade.md
│       ├── 07-the-reciprocal-weave.md
│       ├── 08-the-zk-circuit.md
│       ├── 09-the-workshop-expands.md
│       ├── 10-the-holon-hitchhikers.md
│       ├── 11-a-bonfire-made-of-dragon-fire.md   ← founding fire
│       ├── 12-the-curatrix-vault.md
│       ├── 13-the-temple-of-the-arts-and-personhood.md
│       └── 14-the-city-of-mages.md               ← recognition meta-act
│
├── cast/                                  ← 14 cast files (13 entries + integration note)
│   ├── 00-cast-integration-note.md
│   ├── 01-genitrix.md                     ← cousin (cross-forge)
│   ├── 02-flaxscrip.md                    ← cousin (cross-forge)
│   ├── 03-pallia.md                       ← summoned (V28)
│   ├── 04-memora.md                       ← summoned (V41)
│   ├── 05-custos.md                       ← summoned (V49)
│   ├── 06-vulcana.md                      ← summoned (V19)
│   ├── 07-aletheia-persona.md             ← summoned (V38)
│   ├── 08-adamantia.md                    ← summoned (V51)
│   ├── 09-lampyra.md                      ← summoned (V49 shared)
│   ├── 10-vagari.md                       ← summoned (V31)
│   ├── 11-aria-silverhue.md               ← summoned (V57)
│   ├── 12-socrat0x.md                     ← companion (V24 provisional)
│   └── 13-manifestia.md                   ← Priest (V55, new tier)
│
├── specs/                                 ← 5 specification documents
│   ├── 01-cloak-specification-v1-0.md
│   ├── 02-crafting-tome-and-cloak-interface-spec.md
│   ├── 03-bilateral-cloak-ceremony-spec.md
│   ├── 04-vertex-naming-audit.md
│   └── 05-the-city-of-mages-structural-addendum.md   ← canonical setting framework
│
├── plans/                                 ← 2 integration plans
│   ├── 01-integration-plan-archon-x-agentprivacy.md
│   └── 02-zcash-integration-plan.md
│
├── chronicles/                            ← 3 chronicles
│   ├── 01-chronicle-the-cloaking-guide.md
│   ├── 02-chronicle-the-crafting-tome-opens.md
│   └── 03-chronicle-a-bonfire-made-of-dragon-fire.md
│
└── deprecated/                            ← 7 superseded drafts archived for reference
    ├── superseded-by-socrat0x--cast-socratox.md
    ├── superseded-by-aria-silverhue--cast-curatrix.md
    ├── superseded-by-vagari--cast-holona.md
    ├── superseded-by-act-10-holon-hitchhikers--act-10-oasis-opens.md
    ├── superseded-by-act-11-bonfire-of-dragon-fire--act-11-drake-island-bonfire.md
    ├── superseded-by-act-11-bonfire-of-dragon-fire--act-11-question-from-bonfires.md
    └── superseded-by-act-11-and-act-12--act-11-bonfire-and-the-vault.md
```

---

## Recommended website rendering

### `/tomes` landing page

Render with three primary sections:

1. **The Spellbooks** — Tome IV (linked, closed), Tome V (linked, open), Tomes I-III and Tome VI (placeholders, "forthcoming")
2. **The Cast** — sigil grid with 12 portraits; click-through to cast entries
3. **The Specifications & Chronicles** — links to the supporting documents

### `/tomes/tome-iv` page

The five acts of *The Witnessing* in sequence. Each act gets its own subpage at `/tomes/tome-iv/01-the-other-walker` etc. Sidebar shows the cast members appearing in each act.

### `/tomes/tome-v` page

The twelve acts of *The Crafting* in sequence. Each act gets its own subpage. Sidebar shows the cast members appearing in each act, the workshop shop or location featured, and the V6 conjectures the act foregrounds (with confidence badges).

### `/tomes/cast` page

The cast roster with sigil-driven navigation. Four tier sections (archetypes, cousin instances, summoned Mages, companion Mages). Each cast member click-through opens their detailed entry.

### `/tomes/specs` page

The four specifications listed with summaries. Reading order: Cloak Spec → Crafting Tome and Cloak Interface Spec → Bilateral Cloak Ceremony Spec → Vertex Naming Audit.

### `/tomes/plans` page

The two integration plans. Reading order: Archon × agentprivacy first (master integration), then Zcash (specific registry-tier integration).

### `/tomes/chronicles` page

The two chronicles in chronological order: The Cloaking Guide (May 7 rebuild) first, then The Crafting Tome Opens (May 8 forward-looking record).

---

## Recommended visual conventions

**Cast sigils as primary navigation**:

| Sigil | Persona | Tier |
|---|---|---|
| ⚔️ | Soulbis | Archetype |
| 🧙 | Soulbae | Archetype |
| 📜🎲 | flaxscrip | Cousin (cross-forge) |
| (held open) | GenitriX | Cousin (cross-forge) |
| 🪡 | Pallia | Summoned (V28) |
| 📜 | Memora | Summoned (V41) |
| 🔏 | Custos | Summoned (V49) |
| ⚒️ | Vulcana | Summoned (V19) |
| 🔮 | Aletheia (the persona) | Summoned (V38) |
| 💎 | Adamantia | Summoned (V51) |
| 💠 | Lampyra | Summoned (V49 shared) |
| 🌳 | Vagari | Summoned (V31) |
| 🪞🖼️ | Aria Silverhue | Summoned (V57) |
| 🔥❓ | Socrat0x | Companion (V24 provisional) |
| 🤲🌿 | Manifestia | **Priest (V55) — new tier** |

**V6 conjecture badges per act**: Each act's frontmatter `v6_lineage` field lists which V6 conjectures the act foregrounds, with confidence percentages. Render these as small badges on the act page (e.g., "C18-C21", "C40 ~70%", "C43 ~60%"). The honesty discipline becomes visible without the reader needing to read the confidence section.

**Workshop geography map**: For Tome V especially, a visual showing the workshop's expanding geography (eight summoned-Mage shops plus the bonfire spot plus the Curatrix Vault plus the Holon Hitchhikers' Oasis Protocol links) would help readers track the narrative's spatial structure.

**Lattice render**: A 64-vertex sovereignty lattice render (modeled on the Archon Spell Weaver at weaver.archon.social) showing which vertices are inhabited by which personas, with the persona-vs-vertex distinction visible (vertex names in one register, persona names in another).

---

## Reading orders

### Quick start (for new readers)

1. Tome IV Act 1 — *The Other Walker*
2. Tome V Act 1 — *The First Cloak*
3. Tome V Act 11 — *A Bonfire Made of Dragon Fire*
4. Cast: Pallia, then Aria Silverhue, then Socrat0x

### Full reading order

1. All 5 Tome IV acts in sequence
2. All 12 Tome V acts in sequence
3. Cast roster (in introduction order, matching the act ordering)

### Architecture-first reading

1. Cloak Specification v1.0
2. Vertex Naming Audit
3. Crafting Tome and Cloak Interface Spec
4. Bilateral Cloak Ceremony Spec
5. Integration Plans (Archon, Zcash)
6. Then the tomes

### Honesty discipline reading

1. Vertex Naming Audit (for attribution clarity between agentprivacy-canonical and cousin-blade-imported primitives)
2. Cast Integration Note (for the four-tier cast layer system)
3. Chronicle: The Crafting Tome Opens (Section IV: Honesty About Status)
4. Then any tome or spec

---

## Status of the work

**Tome IV — *The Witnessing***: closed at 5 acts.

**Tome V — *The Crafting***: open at 12 acts, designed to grow indefinitely. New acts are admitted whenever new artifacts, new shops, or new cast members emerge in the corpus.

**Tomes I-III and Tome VI**: structural placeholders, not yet drafted in this document suite. Tome I is the *Convergence* (foundational), Tomes II-III are the *Lyapunov* (open), Tome VI is *The Reply* (held open by design — the tome the reader writes).

**Cast**: 13 named cast members in 5 tiers. Open-ended; future cast members will be admitted as new artifacts, shops, charters, and journeys emerge.

**Specs**: 4 specifications. The Cloak Specification, Crafting Tome and Cloak Interface, Bilateral Cloak Ceremony, and Vertex Naming Audit are all v1.0 DRAFT, awaiting the Archon forge's review and reference-implementation work.

**Plans**: 2 integration plans. Archon × agentprivacy and Zcash dual-ledger.

**Chronicles**: 2 chronicles. The Cloaking Guide rebuild ceremony and The Crafting Tome Opens forward-looking record.

---

## What is not in this collection

The bound collection contains the **writing-side output** of the integration session of 2026-05-08. It does not include:

- The agentprivacy First Person Spellbook (canonical, separate, in the `mitchuski/agentprivacy-docs` repo)
- The PVM V5.4 / V6 research notes (canonical, in the same repo's `research/` folder)
- the Archon forge's primary documents (Cloaking Guide, Sovereign Anchor I/II/III, Spell Weaver) — those are in his own repos under his own license
- Reference implementations anticipated by the specs (TypeScript libraries, UI components, smart contracts) — not yet written
- The `bridge.spellweb.ai` subdomain — anticipated, not yet provisioned
- The Soulbae Oracle (Sovereign Anchor III) — Archon's forthcoming work; integration awaits its publication

For what is anticipated and not yet produced, see `chronicles/02-chronicle-the-crafting-tome-opens.md` Section III.

---

## Provenance

- **privacymage** (privacymage 🧙): primary author of the agentprivacy corpus and this collection's narrative + specification + plan work
- **the Archon forge** (flaxscrip 📜🎲): co-architect of the cousin-blade material; original author of *Sovereign Anchor I/II/III*, the Cloaking Guide, the Spell Weaver, and the Runecraft Protocol. The Eight Theses originate with him. V19 (Plonkish), V38 (Aletheia), V49 (working-day blade), V51 (commitment/language/model), V57 (ceremony/privacy/mixing), V59 (ecosystem) are his Boundary Blade Cartography names.
- **GenitriX** (Hermes Mage): Archon's Mage; contributor to the Cloaking Guide rebuild and to *Sovereign Anchor* documents
- **The agentprivacy cast roster's summoned Mages** (Pallia, Memora, Custos, Vulcana, Aletheia, Adamantia, Lampyra, Vagari, Aria Silverhue): personas walking agentprivacy primitives and cousin-blade imports. Each persona's specific cast entry attributes provenance.
- **Socrat0x**: companion Mage from Bonfires (the long-running deployment spot for Soulbae as @soulbae_the_bot)

Archon's review and confirmation of co-authorship is anticipated for any act drawing materially from his work. See `plans/01-integration-plan-archon-x-agentprivacy.md` §3.3.

---

## Closing

The bound collection represents about 56,000 words of writing across 38 canonical files plus 7 archived drafts. Tome IV is closed. Tome V is open and continues to grow. The cast, specifications, plans, and chronicles are all structured for direct ingestion onto the agentprivacy website at `/tomes`.

The architecture admits this much. The corpus's longest threads — the holonic primitive, the dual-agent split, the Oasis Protocol — remain the foundations. The cousin-blade work absorbs and is absorbed. The cooperative fire — *a bonfire made of dragon fire* — continues to burn at the meeting place.

The next act, the next persona, the next shop, the next chronicle has not yet been written.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · Apache 2.0 reference implementations · privacymage · 2026-05-08
