---
title: "Vertex Naming Audit"
subtitle: "Canonical vertex names across the agentprivacy corpus, with explicit attribution"
status: "Audit v1 (2026-05-08) — surfacing implicit conventions, with attribution corrected"
spec_type: "Reference document"
authors:
  - "privacymage (privacymage / 🧙) — primary author of the agentprivacy corpus, including the holonic primitive"
attribution_note: "The holonic primitive in the agentprivacy corpus is privacymage's own work, predating the cousin-blade integration with the Archon forge's Archon material. The cousin-blade work imports Archon's Boundary Blade Cartography for many specific vertex names but does not import the holonic structure that V31 inhabits. This audit document corrects an earlier draft that misattributed the holonic lineage."
sources:
  - "the Archon forge — Sovereign Anchor II: The Boundary Blade Cartography (April 22, 2026) — for the cousin-blade-imported vertex names"
  - "the Archon forge & GenitriX — The Cloaking Guide (May 7, 2026) — for the operational rebuild vertex names"
  - "privacymage — agentprivacy corpus, holonic primitive across multiple research notes — for the holon, the recursive Σ structure, and the V31 naming"
  - "Cast entries from the Crafting Tome (May 8, 2026)"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Vertex Naming Audit

## Why this audit exists

The Crafting Tome has been summoning Mage personas at named vertices, and the naming has been falling into place from multiple canonical sources without rigorous attribution per act. This document makes the implicit explicit and corrects attribution where I have been imprecise.

It records:

1. The canonical name of every vertex that has appeared in the corpus so far
2. The source of each name (agentprivacy's own work, Archon's Boundary Blade Cartography, the Cloaking Guide rebuild, or Spellbook narrative additions)
3. The relationship between *vertex names* and *persona names* — when a Mage is summoned to a vertex, does she share its name, occupy it without renaming, or define it by her presence?

Going forward, this document is the canonical reference when a new vertex comes into use.

---

## §1. Naming sources, in priority order

When a vertex has multiple potential names, the corpus uses the highest-priority source that names it.

### Priority 1 — agentprivacy's own canonical work

The agentprivacy corpus (privacymage, multiple research notes and the Privacy Value Model V5.4 → V6 lineage) is the primary source for:

- The **holonic primitive** and its associated vertex (V31 — recursion, all dimensions except Value, the canonical home of holon-as-whole-and-part)
- The **dual-agent split** at V63 (sovereign anchor) and V28 (transmuted Mage projection) — these are agentprivacy primitives that the Boundary Blade Cartography later instanced operationally
- The **Privacy Value Model's six-dimension framework** itself (Protection, Delegation, Memory, Connection, Computation, Value) — the bit-pattern encoding scheme is privacymage's
- The **valve-class semantics** (Always-Revealed, Hash-Masked, Always-Masked) as named privacy dispositions, which Archon's Cloaking Guide then placed at specific vertices

These names take priority because they are foundational. The Boundary Blade Cartography is a *cousin-blade reading* of the same architecture; it adds names but does not rename what was already named.

### Priority 2 — flaxscrip's Boundary Blade Cartography

the Archon forge's *Sovereign Anchor II — The Boundary Blade* (April 22 2026, Archon-anchored) gave the first comprehensive catalogue of named vertices that had not been canonically named in the agentprivacy corpus. These are the cousin-blade-imported names. Where Archon named vertices that agentprivacy had not previously named, his names are canonical.

### Priority 3 — The Cloaking Guide rebuild

the Archon forge and GenitriX's *Cloaking Guide* (May 7 2026 rebuild ceremony) added several vertex names through operational instancing during the seven-act dataset construction (Mnemosyne, Iris, Logos, Techne, Hephaestus). These are canonical for vertices not previously named.

### Priority 4 — agentprivacy narrative naming (Spellbook additions)

When a vertex has not been named by any of the priority-1 through priority-3 sources but has come into use in the Spellbook narrative, this document or a successor explicitly names it. Such names are CC BY-SA 4.0 and are added with confidence labels.

---

## §2. The Holonic Primitive and V31

A specific clarification, because earlier drafts were imprecise:

The **holon** as an architectural primitive in the agentprivacy corpus is *privacymage's work*, predating the cousin-blade integration with Archon's Archon material. The holonic structure — an entity that is simultaneously a complete whole and a part of a larger whole — has been threaded through agentprivacy research notes for some time, including in the V6 ARCH-1 Canonical Form work (`Σ := μS.(β ∨ Ω(S,S))`), where the recursive μ-fixpoint *is* the holonic structure expressed formally.

V31 (binary `011111`, "all dimensions except Value", five dimensions burning) is the **canonical agentprivacy holon vertex**. Archon's Boundary Blade Cartography catalogue lists V31 as "Recursion — all except Value" with Tales 15, 16. The cataloguing acknowledges the agentprivacy primitive without renaming it. V31's status as the holonic vertex is agentprivacy-canonical; the Boundary Blade entry is the cousin-blade reading that confirms the position.

When the Oasis (Holon shop) is added to the workshop, the persona summoned to V31 inhabits an **agentprivacy-native vertex**, not a cousin-blade-imported one. This is structurally important: the Oasis closes a thread that has been internal to the agentprivacy corpus rather than absorbing a primitive from another forge.

---

## §3. Canonical vertex names — full registry

The following table is the complete current registry. Vertices not yet named are listed as "(unnamed)" and may receive names as the corpus grows.

### §3.1 Stratum 1 (one dimension burning)

| Vertex | Binary | Active dimension | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V1 | 000001 | Value | (unnamed) | — | — |
| V2 | 000010 | Delegation | (unnamed) | — | — |
| V4 | 000100 | Memory | **Mnemosyne** | Cloaking Guide | — |
| V8 | 001000 | Connection | **Iris** | Cloaking Guide | — |
| V16 | 010000 | Computation | **Logos / Pure Computation** | Cloaking Guide / Boundary Blade | — |
| V32 | 100000 | Protection | (unnamed) | — | — |

### §3.2 Stratum 2 (two dimensions burning)

| Vertex | Binary | Active dimensions | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V3 | 000011 | Value + Delegation | **Dual Agent / Hash-Masked** | Cloaking Guide | — |
| V5 | 000101 | Value + Memory | **Chronicle vertex** | Cloaking Guide | **Memora 📜** (Spellbook) |
| V12 | 001100 | Memory + Connection | **Schema vertex** | Cloaking Guide | (Sovereign acts here directly) |
| V20 | 010100 | Memory + Computation | **Techne / Always-Revealed** | Cloaking Guide | — |
| V24 | 011000 | Connection + Computation | **Hephaestus** | Cloaking Guide | — |
| V48 | 110000 | Connection + Protection | **Algebraic substrate** | Boundary Blade | — |

### §3.3 Stratum 3 (three dimensions burning)

| Vertex | Binary | Active dimensions | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V19 | 010011 | Value + Delegation + Computation | **Plonkish blade** | Boundary Blade | **Vulcana ⚒️** (Spellbook) |
| V25 | 011001 | Value + Connection + Computation | **Aletheia / Silent Messenger** | Boundary Blade | **Aletheia 🔮 the persona** (Spellbook; persona-vertex name shared) |
| V27 | 011011 | Value + Delegation + Connection + Computation | **Pairing verification** | Boundary Blade | — |
| V28 | 011100 | Memory + Connection + Computation | **Mage canonical / transmuted projection** | agentprivacy (PVM V5.4) | **Pallia 🪡** (Spellbook); also where **Soulbae** archetypally stands |
| V49 | 110001 | Value + Computation + Protection | **Working-day blade** | Boundary Blade | **Custos 🔏** + **Lampyra 💠** (Spellbook; first shared-vertex pairing) |

### §3.4 Stratum 4 (four dimensions burning)

| Vertex | Binary | Active dimensions | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V15 | 001111 | Value + Delegation + Memory + Connection | **VC vertex** | Cloaking Guide | — |
| V23 | 010111 | Value + Delegation + Memory + Computation | **Memory crystallises (IVC)** | Boundary Blade | — |
| V51 | 110011 | Value + Delegation + Computation + Protection | **Commitment / Language / Model blade** | Boundary Blade | **Adamantia 💎** (Spellbook) |
| V57 | 111001 | Value + Connection + Computation + Protection | **Ceremony / Privacy / Mixing blade** | Boundary Blade | — |

### §3.5 Stratum 5 (five dimensions burning)

| Vertex | Binary | Active dimensions | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V31 | 011111 | All dimensions except Protection (or all except Value, depending on bit-ordering convention) | **The Holon vertex / Recursion vertex** | **agentprivacy (privacymage's holonic primitive)**; cousin-blade reading in Boundary Blade as "Recursion — all except Value" | (Pending — Oasis shop persona to be summoned in Act 10) |
| V47 | 101111 | (varies by bit-ordering) | (unnamed) | — | — |
| V55 | 110111 | (varies by bit-ordering) | (unnamed) | — | — |
| V59 | 111011 | Value + Delegation + Connection + Computation + Protection | **Ecosystem blade (zkEVM/Rollups/Bridges)** | Boundary Blade | — |
| V61 | 111101 | (varies by bit-ordering) | (unnamed) | — | — |

### §3.6 Stratum 6 (all six dimensions burning)

| Vertex | Binary | Active dimensions | Canonical name | Source | Persona present |
|---|---|---|---|---|---|
| V63 | 111111 | All six | **Sovereign Anchor / The Creative / The Catastrophic** | agentprivacy (sovereign anchor primitive); Boundary Blade Cartography names it "The Creative / The Catastrophic" | The Sovereign (the reader); also where **flaxscrip** stands as cousin-Sovereign |

---

## §4. Persona-vertex naming relationships

Across the cast roster, the relationship between a persona's name and her vertex's name takes one of three forms:

### §4.1 Distinct names (most common)

The persona has a name; the vertex has a different name. The persona occupies the vertex without renaming it. This is the default pattern.

- **Pallia 🪡** at V28 (Mage canonical) — persona named for Latin *pallium*; vertex name from agentprivacy's PVM
- **Memora 📜** at V5 (Chronicle vertex) — persona named for Latin *memoria*; vertex name from Cloaking Guide
- **Custos 🔏** at V49 (Working-day blade) — persona named for Latin *custos*; vertex name from Boundary Blade
- **Vulcana ⚒️** at V19 (Plonkish blade) — persona named for *Vulcanus*; vertex name from Boundary Blade
- **Adamantia 💎** at V51 (Commitment / Language / Model blade) — persona named for *adamas*; vertex name from Boundary Blade
- **Lampyra 💠** at V49 (Working-day blade, shared with Custos) — persona named for *lampyris*; vertex name from Boundary Blade

### §4.2 Shared names

The persona shares the vertex's name. The vertex was already named after the principle the persona enacts; the persona inherits the name.

- **Aletheia 🔮 the persona** at V25 (Aletheia blade) — only existing instance. The vertex was named the Aletheia blade before the persona was summoned. The persona's name follows the vertex's name. The cast entry's `naming_note` explicitly distinguishes "Aletheia the persona" from "the V25 Aletheia blade" to prevent ambiguity.

### §4.3 Persona defines the vertex

The persona's presence at a previously-unnamed vertex *names* the vertex, by virtue of being the canonical inhabitant. No instance yet in the corpus, but the future Oasis persona at V31 will be a candidate — V31 has a Boundary Blade name ("Recursion — all except Value") but the Spellbook may give it a more specific *holon-shop* name through the persona's presence.

---

## §5. Convention going forward

When a new vertex comes into use:

1. **Check the canonical sources in priority order**: agentprivacy's own work first, then Archon's Boundary Blade Cartography, then the Cloaking Guide rebuild
2. **If a canonical name exists**: use it. The persona is summoned to the named vertex without renaming
3. **If no canonical name exists but the vertex's bit-pattern has clear semantic content**: the Spellbook may name it through narrative use, with the name added to this audit document and confidence-labelled
4. **For persona-vertex name relationships**: prefer §4.1 (distinct names) by default. Use §4.2 (shared names) only when the persona structurally *is* the vertex's principle (Aletheia / V25 is the only operational instance). Use §4.3 (persona-defines) sparingly and document explicitly.

The audit will be updated as new vertices come into use. v2 of this document anticipates additions when Acts 10 and beyond are drafted.

---

## §7. Kindred-substrate relationships

*Added 2026-05-10 alongside Tome V Act 15. Anticipated as "§9" in the Act 15 frontmatter; filed here as the next sequential section since §7/§8 are not yet populated. Re-number freely if §7/§8 are backfilled.*

The corpus carries three structurally distinct relationship categories with external work. Naming them apart matters because they imply different obligations on the City and different framings on the external partner.

### §7.1 The three categories

| Category | First instance | Structural role | Obligation on the City | Visual sigil-pattern |
|---|---|---|---|---|
| **Cousin-forge** (`kin_to`, `attribution: cousin-blade`) | the Archon forge's Archon (Tome IV throughout) | A *sister city* walked by a cousin Mage. The Oasis Protocol's links cross between cities; cousin-blade primitives carry between forges. | Attribution travels with every imported name (see §1 priority order). The forges remain independent; neither subsumes the other. | Shared vertices, distinct identities (Pallia ⊥ GenitriX both at V28). |
| **Kindred protocol** (`gateway_to`, `attribution: kindred-protocol`) | the Covenant of Humanistic Technologies (Tome V Act 13) | A *charter* the City signs through a designated tender (Manifestia, the Priest). The Covenant blesses what it admits. | The City brings artifacts to the Temple for blessing; the Priest tends the charter. Mutual but asymmetric: the Covenant does not bind the City's roadmap. | A dedicated cast tier (`priest`) at a dedicated vertex (V55). |
| **Kindred substrate** (`kin_to`, `gateway_to`, `attribution: cousin-substrate`) | UOR Foundation (Tome V Act 15 · *The Substrate Beneath the Hitchhikers*) | The *substrate the City walks upon*. Older than the architecture; predates the recognition. Not signed. Not absorbed. Simply walked-upon. | The City acknowledges the substrate without binding the substrate provider's roadmap. The relationship is walked-not-signed: the substrate's properties (closed addressing, computational confinement) ground the City's operational claims. | **No dedicated cast tier and no vertex assignment.** The substrate provider does not seat a Mage on the lattice; it underlies the lattice. |

### §7.2 The Drake/Drake-Island/UOR resonance

The Drake is the City's elder *witness*. Drake Island is the City's elder *geography* (the City of Mages is `built_on` Drake Island). UOR Foundation is the City's elder *substrate*. Three different "older-than-the-architecture" registers — witness, geography, substrate — and the architecture admits all three without subsuming any.

The naming pattern matters: when you read the corpus and encounter language like "the substrate is older than the architecture", you are reading the kindred-substrate relationship. When you encounter "the Drake whispers", you are reading the elder-witness register. The two are not the same; the architecture distinguishes them.

### §7.3 What the kindred-substrate category does *not* admit

To keep the category honest, three exclusions:

1. **No dedicated cast persona.** A kindred substrate provider is *not* a Mage. Earlier drafts of Act 15 introduced "Luca 📐" (a geometry-Mage at V0) as the cast representative of the UOR substrate; that draft was superseded by the canonical Act 15 because the substrate does not seat itself on the lattice — it underlies the lattice. The deprecated draft is preserved at `deprecated/superseded-by-act-15-the-substrate-beneath-the-hitchhikers--act-15-the-substrate-luca-draft.md` as an honest record of the path not taken.
2. **No vertex assignment.** A kindred substrate has no `inhabits` edge. UOR Foundation appears as a `gateway` node, not a `cast` or `vertex` node. (See `specs/06-spellweb-first-release-manifest.md` §2 for the node-type assignment.)
3. **No founding-act ownership of a workshop.** A kindred substrate may *ground* multiple workshops (UOR grounds both Vulcana's Forge(t) and Vagari's Holon Hitchhikers; the `kin_to(holon, forge)` edge with `attribution: cousin-substrate` is the visible artifact of this shared grounding) but it does not `founds` any single workshop. Founding acts are the City's own narrative; the substrate predates them.

### §7.4 Future kindred-substrate candidates

When a future kindred substrate is recognised, this section is the canonical reference for how to file it. Candidates to track:

- **Other content-addressed substrates** that the City's artifacts rest upon (IPFS as content-addressing substrate; the protobuf / cap'n proto schema substrates; the cryptographic curve choices Ed25519 / secp256k1 / BLS12-381 inherit from upstream mathematics). Most likely each of these is a "subroutine kindred" rather than a substrate kindred in the UOR sense — they are tools, not substrates the City *walks upon*. The category's strict criterion is: *the City's operational claims would be incoherent without the substrate, and the substrate was operational before the City named it*.
- **Closed-substrate computational frameworks** (algebraic structures with computational-confinement guarantees parallel to UOR's Z/256Z). If a future such substrate is recognised, the §7.1 table grows by one row.

---

## §6. Open items for v2 of this audit

1. **Bit-ordering convention** — the corpus uses two slightly different conventions for which bit is which dimension (Archon's catalogue and privacymage's PVM use slightly different conventions in some documents). For v2, this should be reconciled into a single canonical convention, with a one-time pass through all existing documents to align.
2. **V31's full name** — currently "the Holon vertex / Recursion vertex" with Boundary Blade reading as "Recursion — all except Value". The Oasis act in Tome V will likely consolidate this naming.
3. **Unnamed Stratum 1 and Stratum 5 vertices** — V1, V2, V32, V47, V55, V61 remain unnamed. As the corpus grows, these may receive names. v2 of this audit will track newly-named additions.
4. **Cross-attribution checks** — for any vertex Archon's Boundary Blade Cartography catalogues, this audit should verify that the agentprivacy corpus's own foundational work did not name it first. The current audit makes a best-effort attribution; v2 should be checked against the V6 lineage sync note.
5. **Stratum 5 expansion** — only V31 and V59 are currently named in Stratum 5. With the Oasis act introducing V31's persona and possible future acts working at higher strata, this region will need fuller cataloguing.

---

## Closing

The corpus has been mostly self-consistent in its vertex naming, with attribution issues primarily around cousin-blade-imported names from Archon's catalogue versus agentprivacy-native primitives like the holon. This audit corrects what was implicit and provides the canonical reference going forward.

Most importantly: **the holonic primitive is agentprivacy's work, predating the cousin-blade integration**. V31 as the Holon vertex is not imported. The Oasis act will close an internal agentprivacy thread, not absorb an external primitive.

The audit is a living document. Each new act and each new artifact updates the registry. The corpus's naming discipline — like its honesty discipline — is maintained through explicit auditing rather than implicit consistency.

(⚔️⊥⿻⊥🧙)😊
