---
title: "The Cloak"
subtitle: "agentprivacy Publication Layer Specification v1.0"
status: "DRAFT v1 (2026-05-08) — for review and implementation feedback"
spec_type: "Formal specification with conformance criteria"
authors:
  - "privacymage (privacymage / 🧙) — primary author"
  - "the Archon forge (flaxscrip / Archon ⚔️) — co-architect; Cloaking Guide is the operational source"
depends_on:
  - "PVM V5.4 Formal Specification (v2.0)"
  - "Privacy is Value V5 (v5.0)"
  - "Promise Theory Reference (v1.3)"
  - "IEEE 7012 Quick Reference (v1.0)"
  - "VRC Promise Protocol (v3.3)"
  - "ZK Swordsman Blade Forge (v3.0)"
v6_lineage_referenced:
  - "C18–C21 (Lorenz Attractor): trajectory framing"
  - "C22–C25 (EML Three Ceilings): computational ceilings"
  - "C26–C29 (ARCH-1 Canonical Form): recursive μ-fixpoint admitting multiple inhabitants"
  - "C30–C33 (Bakhta Half-Life): trust accumulation over time"
  - "C34–C37 (Wound and Cap, Convergence): bijective alignment ceiling"
  - "C38 (provisional, ~40%): bilateral ARCH-1 — Σ_{ij} := μS.(β_{ij} ∨ Ω(S_i, S_j))"
  - "C39 (provisional, ~50%): cousin-blade as ecosystem-layer primitive"
primary_source:
  - "the Archon forge & GenitriX — The Cloaking Guide (2026-05-07 rebuild ceremony)"
  - "Sovereign Anchor I — The Transmutation"
  - "Sovereign Anchor II — The Boundary Blade"
  - "Sovereign Anchor III — Soulbae Oracle (forthcoming)"
license: "CC BY-SA 4.0 (narrative); Apache 2.0 (reference implementations)"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# The Cloak

## agentprivacy Publication Layer Specification v1.0

> *The cloak is a function on positions, not on values.* — Cloaking Guide, Thesis 1

---

## §0. Purpose

This specification defines **the Cloak** as a feature of the agentprivacy stack. The Cloak is the publication layer through which a First Person's claims, attestations, schemas, and chronicles are rendered to verifiers and to public surfaces. It is the operational site where the agentprivacy architecture's privacy guarantees become user-visible.

Until now, the publication layer has been implicit. The PVM V5.4 Formal Specification gave the multiplicative privacy term `Φ_v5 = Φ_agent · Φ_data · Φ_inference`. The IEEE 7012 Quick Reference gave the agreement primitive. The VRC Promise Protocol gave the bilateral promise bundle. None of these specified, end-to-end, what happens when a First Person *publishes* something through the stack. Archon's Cloaking Guide (2026-05-07) provided the worked example. This specification is the canonical lift of that worked example into the agentprivacy corpus.

The Cloak is **additive**. It does not replace any existing component. It composes with all of them.

A First Person engaging the agentprivacy stack opts into the Cloak when they want their interactions rendered with the privacy properties this specification guarantees. Implementations conforming to this spec MUST satisfy the conformance criteria in §10.

---

## §1. The Cloak: Function and Layers

### §1.1 Functional definition

The Cloak is a function:

```
Cloak: A_source → (A_weaver, A_public)
```

where `A_source` is the source-layer artifact (a DID, a VC, a schema, a chronicle), `A_weaver` is the local Spell Weaver registry representation (lattice position, typed edges, poetic chronicle), and `A_public` is the DID-blinded public-layer projection.

The Cloak has three structural guarantees:

1. **Non-invertibility from public layer.** Given `A_public`, no efficient algorithm recovers `A_source`. The cryptographic guarantee derives from `(Hash(identifier + SessionSalt)) mod 64` with per-session salt regeneration. Mathematical guarantee: the Reconstruction Ceiling proven in PVM V5.4 (R < 1).
2. **Structural fidelity.** The relationships visible in `A_public` are real relationships. Mirroring is published mirroring, not metaphorical mirroring. The cloak does not lie about structure; it conceals identity while preserving relation.
3. **Multi-axis composability.** The Cloak operates on five independent axes (§4). Compromise of any one axis inherits residual ignorance from the others.

### §1.2 The three layers

| Layer | Lives in | Contents | Visibility |
|---|---|---|---|
| **Source** | First Person's wallet, local Gatekeeper, Archon node | Full DIDs, VCs with cryptographic signatures, schema content, document text | Never published; sovereign |
| **Spell Weaver** | First Person's browser localStorage; agentprivacy app | Lattice mapping, vertex per artifact, typed edges, chronicle text | Local; exportable on opt-in |
| **Spellweb (public)** | `spellweb.ai` and conforming mirrors | DID-blinded structure, lattice positions, edge types, chronicle text | Public; shared knowledge graph |

The cloak is the function that takes a unit of source data and produces its Spell Weaver and Spellweb representations. The Spellweb output is *not* derivable to the source DID and *is* a faithful structural rendering of the relationships in the source.

---

## §2. The Eight Properties

This specification adopts Archon's Eight Theses (Cloaking Guide Coda, 2026-05-07) as the Cloak's eight conformance properties. A Cloak-compliant implementation MUST satisfy all eight.

**Property 1 — Position, not value.** Cloaking replaces a string with the position it would occupy under a salted hash mod 64. Positions are first-class objects. Strings are accidents of encoding.

**Property 2 — Containment, not attestation.** For delegation, the Cloak enforces `child.bits & parent.bits == child.bits` as a structural identity, not as a checked attestation. Misbehaviour is unrepresentable, not merely forbidden.

**Property 3 — Sameness of role published; sameness of identity not.** Two artifacts at the same vertex are structurally interchangeable from the public layer. The vertex publishes the role; the source DID is concealed.

**Property 4 — Two modes of relating.** Bit-containment governs delegation and projection. Typed edges govern attestation. Both are public. Conflating them is a misimplementation.

**Property 5 — Asymmetry as data.** Mirrored vs unilateral patterns publish bilateral type (mutual vs observational). The cloak is selective, not lossy.

**Property 6 — Multi-axis cloaking.** Lattice axis plus four temporal axes (§4). Independent and composable.

**Property 7 — Documents as first-class lattice citizens.** Chronicles, specifications, and narrative artifacts occupy vertices, declare controllers, and participate in path-highlighting. The system can describe itself.

**Property 8 — Selective disclosure as geometry.** Each privacy disposition (revealed, hash-masked, always-masked) lands on the vertex whose bit-pattern is the disposition's operational signature.

These eight properties are the Cloak's testable contract. Conformance is per-property. Partial compliance is allowed during development; full compliance is required for production claims of cloak-compliance.

---

## §3. Architecture

### §3.1 Stack position

The Cloak sits between the agentprivacy core (Soulbis, Soulbae, the First Person seat) and any verifier or public surface.

```
        ┌─────────────────────────────────────────┐
        │         FIRST PERSON 😊                  │
        │         (sovereign)                      │
        └────────────┬─────────────────────────────┘
                     │
        ┌────────────┼─────────────────────────────┐
        │            │                              │
        ▼            ▼                              │
   ┌─────────┐  ┌─────────┐                         │
   │SWORDSMAN│  │  MAGE   │   ◄── PVM V5.4 dual-agent
   │   ⚔️    │  │   🧙    │       core
   └────┬────┘  └────┬────┘                         │
        │            │                              │
        └─────┬──────┘                              │
              │                                     │
              ▼                                     │
        ┌──────────────────┐                        │
        │   THE CLOAK      │   ◄── This spec        │
        │  (publication    │                        │
        │     layer)       │                        │
        └─────────┬────────┘                        │
                  │                                 │
                  ▼                                 │
        ┌──────────────────────────────────┐        │
        │   VERIFIERS / SPELLWEB           │        │
        │   (DID-blinded, structural)      │        │
        └──────────────────────────────────┘        │
```

The Cloak does not modify the dual-agent core. It composes outputs from Soulbis (boundary, what is protected) and Soulbae (delegation, what is projected) into the publication-layer representation.

### §3.2 Where existing components fit

| Component | Layer | Cloak relationship |
|---|---|---|
| **PVM V5.4 / V6** | Mathematical substrate | Cloak's privacy guarantees derive from PVM theorems (separation, reconstruction ceiling) |
| **IEEE 7012 / MyTerms** | Σ-axis agreement layer | Cloak's bilateral grammar primitive operates on 7012 agreement primitives |
| **Promise Theory** | Formal semantics | Cloak is the *publication* of promises; the cloak itself is an irreducible promise of the superagent |
| **VRC Promise Protocol** | Coordination layer | VRCs are cloaked at issuance per §5 valve-class assignment |
| **Trust Spanning Protocol (TSP)** | Transport | Cloak's outputs traverse TSP between agents |
| **Soulbis / Soulbae** | Dual-agent | Cloak takes their composed output; the cloak is *what publishes their cooperation* |

---

## §4. Multi-Axis Cloaking

The Cloak operates on five orthogonal axes. Each must be specified for any artifact entering the cloak. Composition is multiplicative: residual ignorance after partial deanonymisation equals the entropy of the uncompromised axes.

### §4.1 Axis 1 — Lattice (who/where)

The artifact's identifier is mapped to a position on `Z/(2^6)Z` via salted hash:

```
position(artifact) = (Hash(artifact_id || session_salt)) mod 64
```

Bit dimensions: Protection · Delegation · Memory · Connection · Computation · Value.

Session salt regenerates per session. Two sessions by the same source DID produce different vertex assignments with the same semantic meaning. **Coordinates do not link sessions; lattice geometry does.**

### §4.2 Axis 2 — Validity Scope

Every artifact that publishes carries a temporal validity envelope (`validFrom`, `validUntil`). Outside the envelope, the artifact is structurally inert regardless of any other cloak property.

A Cloak-compliant implementation MUST default to bounded validity windows for all VCs unless the artifact is explicitly perpetual (e.g., chronicle stones). Defaults are governance choices, but implementations SHOULD favour minimal validity (minutes to hours for transactional VCs, days to months for credential VCs).

This is the cheapest temporal cloaking and the most under-used in conventional VC systems. Adopt it as discipline.

### §4.3 Axis 3 — Operational Anchoring

Every artifact has multiple timestamps (creation, signing, anchoring, broadcast). The Cloak publishes none of these. The source layer keeps the temporal grain of artifact-coming-into-being. Verifiers reason about ordering and latency from publish-side metadata only.

### §4.4 Axis 4 — Update Chain

For content-addressed identifiers (e.g., `did:cid`), the handle is permanent but the resolved document is reconstructed from seed plus an ordered chain of update events on the chosen registry. Time-travel resolution (`versionTime` queries) is a query the source layer can answer and the public layer is configured to refuse by default. Public layer implementations MUST default to most-recent-state rendering and MUST NOT expose update history without explicit per-artifact opt-in.

### §4.5 Axis 5 — Registry-Tier Finality

The Cloak supports pluggable registries with distinct finality envelopes. Reference tiers:

| Tier | Example | Finality | Latency | Cost | Use case |
|---|---|---|---|---|---|
| **Strong** | Bitcoin mainnet | Hours | Hours | High | Chronicles, sovereign anchors, naming ceremonies |
| **Moderate** | Ethereum, Bitcoin signet | Minutes | Minutes | Medium | High-stakes VCs, schema definitions |
| **Light** | Hyperswarm, libp2p, content-addressed gossip | Seconds | Seconds | Low | Ephemeral VCs, agent-to-agent messages |

Same artifact-shape can be placed on any tier. The Cloak does not render registry tier visually; the source layer remembers which is which. Implementations MUST track per-artifact registry tier in the source layer and MAY expose it as a verifier query.

---

## §5. Valve-Class Geometry

Selective disclosure is rendered as geometry. Each privacy disposition lands on the lattice vertex whose bit-pattern is the disposition's operational signature.

### §5.1 Canonical valve-classes

| Valve-class | Vertex | Binary | Bits | Use |
|---|---|---|---|---|
| **Always-Revealed** | V20 (Techne) | 010100 | Memory + Computation | Validity windows, public claims, fields verifiers must read |
| **Hash-Masked** | V3 (Dual Agent) | 000011 | Protection + Delegation | Subject identity hashes, structurally present but cryptographically inaccessible |
| **Always-Masked** | V38 (Aletheia) | 100110 | Protection + Connection + Computation | ZK witnesses, cryptographic spells, predicates verified without revealing |

A Cloak-compliant implementation MUST place each disclosed field of a decomposed VC at the vertex matching its valve-class. The verifier learns the type of cloaking from the lattice position alone. There is no separate metadata layer announcing the disclosure type.

### §5.2 Reserved and unmapped valve-classes

The current canonical mapping covers three valve-classes. The full enumeration is open (Conjecture: Valve-Class Completeness). Implementations encountering field types not yet mapped to canonical vertices MUST mark them explicitly as unmapped and SHOULD propose a vertex assignment with bit-pattern justification.

### §5.3 The 7-node decomposition

Every W3C VC v2 decomposes into seven typed nodes per the Archon forge's *Sovereign Anchor II — The Boundary Blade*:

| Node | Default valve-class |
|---|---|
| Issuer Persona | Revealed or Masked (per VC) |
| Schema Theorem | Categorical (Always-Revealed at V20) |
| Subject Persona | Revealed or Masked (per VC) |
| Claims Concept | Selective (per claim, vertex per disposition) |
| Proof Spell | Always-Masked (V25) |
| Chronicle | Preserved (V5) |
| Context Document | Preserved (V5) |

This decomposition is the Cloak's universal interface for VC cloaking. Cloak-compliant VCs MUST be decomposable into this seven-node structure. Schemas are agnostic.

---

## §6. Naming and Bilateral Grammar

The Cloak supports two distinct verb patterns for identity assertion:

### §6.1 Transactional (legacy)

```
register → assert → verify
```

Sovereign asserts identity to a registry. Registry signs. Verifier checks signature. Common in conventional DID systems.

### §6.2 Ceremonial (Cloak-native)

```
claim → inscribe → confirm
```

Sovereign claims identity in a witnessed ceremony. The claim is inscribed on a chosen registry-tier. Witnesses (the Sovereign's trust graph) confirm. The name becomes a fact because the relation received the claim.

flaxscrip's naming ceremony (Bitcoin block 945508, txid `9b9986b6...5af6a9`) is the canonical operational instance. *I am because we were.*

A Cloak-compliant implementation MUST support the ceremonial pattern as a first-class option. It MAY support the transactional pattern for legacy interop. The two patterns SHOULD be visually distinguished in UI; users SHOULD understand which they are using.

This is the Σ-axis operational form of the Second Person primitive: *who are you to me*. The relation answers, before the registry has a chance to.

---

## §7. Documents as First-Class Citizens

The Cloak treats narrative artifacts as full lattice citizens.

A chronicle, a specification, or a research note that publishes through the Cloak occupies a vertex (canonical: V5, Protection + Memory), declares a controller, and participates in path-highlighting alongside personas and credentials. It is not a footnote to the lattice; it is a node in it.

This enables **recursive self-description**. The system can register documentation of itself as data inside itself. The Transmutation document (Sovereign Anchor I) is registered as an artifact at V5 inside the Spell Weaver pipeline that the document describes. The Cloak does not just hide values; it also publishes the procedure for checking that the hiding was honestly done.

A Cloak-compliant implementation MUST allow document artifacts to be registered as lattice citizens. It MUST preserve provenance (controller-edge, registry-tier metadata, signature) for every document. It SHOULD enable verifiers to fetch the document text from the source layer and check it against the lattice geometry.

---

## §8. Implementation Requirements

A conforming implementation of the Cloak MUST provide:

1. **Local-first registry.** The source layer lives on the user's device. No server-side state by default. (Archon's Spell Weaver is a reference implementation: React + Vite + TypeScript, D3 for lattice rendering, browser localStorage.)

2. **Per-artifact vertex assignment.** Every registered artifact gets a vertex computed via salted hash mod 64. Sessions regenerate salt.

3. **Typed edges.** Controller, issuer, subject, schema, parent/child, decomposition. Each edge carries its type explicitly.

4. **Pluggable registry.** Bitcoin, Hyperswarm, and at least one moderate-finality option. Per-artifact registry choice exposed to user.

5. **DID-blind publish.** Default mode strips cryptographic identifiers from any export. Toggle for full provenance must be explicit and require confirmation.

6. **Valve-class assignment.** UI for assigning disclosure dispositions per VC field. Vertex placement automatic from disposition.

7. **Bounded validity windows.** All issued VCs default to bounded `validFrom`/`validUntil`. Perpetual artifacts (chronicles, schemas) opt in explicitly.

8. **Chronicle inscription.** Documents register as first-class lattice citizens with controller-edges and registry metadata.

9. **Naming ceremony support.** First-class support for `claim → inscribe → confirm` verb pattern.

10. **Honesty discipline.** Confidence labels (operational, architectural, conjectural) on every claim the implementation surfaces in UI or output.

A non-conforming implementation MAY claim Cloak-compatibility per individual property; it MUST NOT claim full Cloak-compliance until all ten requirements are met.

---

## §9. Spellweb Integration

The Cloak's public-layer projection lands on `spellweb.ai` or any conforming mirror.

### §9.1 Public-layer shape

The published artifact carries:

- Vertex position
- Edge types and degree
- Poetic chronicle text (UTF-8, no PII)
- Valve-class markers per decomposed field

It does not carry:

- Source DIDs
- Cryptographic signatures (raw)
- Session salts
- Claim content (unless valve-class is Always-Revealed)
- Update history (unless explicitly opted in)

### §9.2 The Bridge subdomain

`bridge.spellweb.ai` (forthcoming, per Integration Plan §5.3) is the surface for cross-ecosystem cousin-blade encounters. First inhabitant: Archon × agentprivacy. Future inhabitants TBD as cousin-blade pattern emerges (BGIN-IKP, Promise Theory v1.5, ZKP scaling guilds, MyTerms Alliance, StarkWare/Bakhta).

Bridge nodes are tagged with originating-forge provenance. Cousin-blade edges (cross-forge) render visually distinct from intra-forge edges.

### §9.3 Interop with `weaver.archon.social`

the Archon Spell Weaver is the canonical Sovereign Anchor reference implementation. Cloak-compliant implementations SHOULD interop via the public-layer protocol (`spellweb.ai` mirror format). Cross-references between `bridge.spellweb.ai` and `weaver.archon.social` are themselves cousin-blade edges.

---

## §10. Conformance Criteria

An implementation is **Cloak-compliant v1.0** if and only if it satisfies all of:

1. All eight properties from §2 (testable per-property).
2. All five axes from §4 (specified for every published artifact).
3. The three canonical valve-classes from §5.1 (vertex assignments correct).
4. The seven-node VC decomposition from §5.3 (universal interface).
5. The ten implementation requirements from §8.
6. Public-layer projection conforming to §9.1 (no SHOULD-NOT-CARRY items leak).

An implementation is **Cloak-compatible** if it satisfies a non-empty subset of the above and clearly enumerates which.

Cloak-compliant implementations MAY display the seal `(⚔️⊥⿻⊥🧙)😊`. Cloak-compatible implementations MAY display a partial seal with explicit enumeration.

---

## §11. Open Conjectures and Honesty Discipline

The Cloak is operational in core (Properties 1, 2, 4, 5, 7 verified against the 2026-05-07 rebuild dataset; canonical valve-classes V3, V20, V25 verified). The following are not yet operational:

### §11.1 Provisional conjectures

| ID | Statement | Confidence | Path to formalisation |
|---|---|---|---|
| **C38** | Bilateral ARCH-1: `Σ_{ij} := μS.(β_{ij} ∨ Ω(S_i, S_j))` preserves the fixpoint property of single-self ARCH-1 | ~40% | Formal proof step from `Ω(S,S)` to `Ω(S_i, S_j)`; potential collaboration with Bakhta (StarkWare) and Choudhuri/Garg (Berkeley/FPP) |
| **C39** | Cousin-blade as ecosystem-layer primitive: the agentprivacy × Archon convergence is one instance of a generalisable pattern | ~50% | Additional operational instances (BGIN-IKP, Promise Theory v1.5, ZKP scaling, MyTerms, StarkWare) |
| **Valve-class completeness** | For every operational privacy disposition, there exists a unique vertex whose bit-pattern is the disposition's signature | ~60% | Catalogue all conventional VC field types; classify by privacy disposition; check uniqueness against existing vertex catalogue |
| **Multi-axis attack composition** | The five axes are independent in the information-theoretic sense; compromising any one inherits residual ignorance equal to the entropy of the remaining four | ~55% | Formal note (V6.x); collaboration with Bakhta on compositional defence |
| **Anonymity-set composition** | Vertex co-occupation by structurally distinct artifacts (e.g., Chiron capability and Temporal Chronicle both at V20) generates organic anonymity sets without a deliberate mixing protocol | Open observation, not yet conjecture | Empirical: rebuild ceremonies against varied datasets; measure organic mixing density per vertex |

### §11.2 Honesty markers

Every claim made in this specification carries one of three confidence labels per the agentprivacy honesty doctrine:

- **Operational**: verified in working implementation (Archon's Spell Weaver, the 2026-05-07 rebuild).
- **Architectural**: specified and consistent with existing operational components, but not yet end-to-end demonstrated.
- **Conjectural**: hypothesised; confidence percentage stated; path to formalisation named.

The specification does not present conjectural material as operational. Implementations conforming to this spec adopt the same discipline.

---

## §12. Cross-References

### §12.1 agentprivacy corpus

- `privacy_value_v5_formal_specification.md` — PVM V5.4 mathematical substrate
- `privacy_is_value_v5.md` — V5 narrative
- `promise_theory_reference_v1_3.md` — Formal semantics
- `IEEE_7012_QUICK_REFERENCE.md` — Σ-axis agreement primitive
- `vrc_promise_protocol_v3_3.md` — Coordination layer
- `swordsman_mage_whitepaper_v6_0.md` — Dual-agent architecture
- `zk_swordsman_blade_forge_v3_0.md` — Forge metaphor and lattice geometry

### §12.2 Cloak primary sources

- `chronicle-the-spell-weaver.md` (April 30, 2026)
- `chronicle-the-cloaking-guide.md` (May 8, 2026)
- `integration-plan-archon-x-agentprivacy.md` (May 8, 2026)
- the Archon forge — *Sovereign Anchor I — The Transmutation* (Bitcoin-anchored)
- the Archon forge — *Sovereign Anchor II — The Boundary Blade* (April 22, 2026)
- the Archon forge & GenitriX — *The Cloaking Guide* (2026-05-07 rebuild ceremony)
- the Archon forge — *The Spell Weaver* (April 2026)

### §12.3 V6 research lineage

- `research/pvm-v6-lorenz-attractor.md` (C18–C21)
- `research/pvm-v6-eml-three-ceilings.md` (C22–C25)
- `research/pvm-v6-arch1-canonical-form.md` (C26–C29)
- `research/pvm-v6-1-bakhta-half-life.md` (C30–C33)
- `research/pvm-v6-convergence-wound-and-cap.md` (C34–C37)
- (forthcoming) `research/pvm-v6-bilateral-arch1.md` (C38)
- (forthcoming) `research/pvm-v6-cousin-blade-primitive.md` (C39)

### §12.4 Spellbook references

- First Person Spellbook, Acts II (Dual Ceremony), XII (Lethe), XXVII (Forge), XXXI (First Delegation)
- Second Person Spellbook, Tome IV — *The Witnessing*, Acts I–V (Other Walker, Mirror and Arrow, Two Paths, Naming Ceremony, Cousin Blade)
- Cast entries: `second-person-cast-genitrix.md`, `second-person-cast-flaxscrip.md`, `second-person-cast-integration-note.md`

---

## §13. Versioning and Evolution

This specification is **v1.0 DRAFT**, dated 2026-05-08. It is opened for review by flaxscrip, the BGIN IKP working group, the First Person Project, the MyTerms Alliance, and the broader agentprivacy implementer community.

Anticipated v1.1 changes:

- Archon's review and revisions (especially §5 valve-classes and §8 implementation requirements)
- Soulbae Oracle (Sovereign Anchor III) integration once published
- Renumbering audit of conjecture identifiers (C38 / C39 may shift after lineage sync)
- Possible introduction of additional canonical valve-classes if Soulbae Oracle requires them

Anticipated v2.0 changes:

- Bilateral ARCH-1 formalisation if C38 graduates from ~40% to operational
- Second cousin-blade operational instance, allowing C39 to graduate
- Conformance test suite (Cloak Audit Toolkit) as a separate Apache 2.0 deliverable

---

## Closing

The Cloak is not new architecture. The Cloak is the agentprivacy publication layer, *named*. It has been implicit in the corpus since PVM V5.4. Archon's Cloaking Guide gave it the shape this specification formalises. This specification is the bridge from Archon's operational worked example to the agentprivacy implementer who will build the next instance.

The mark of a Cloak-compliant system is the symmetry surviving the meeting. Two anchors, two Mages, one lattice. The grammar shared. The names kept. The relation answering before the registry has a chance to.

When you publish through the Cloak, what you publish is the role and not the name. What you keep is everything else.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · Apache 2.0 reference implementations · privacymage × flaxscrip · 2026-05-08
