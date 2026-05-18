---
title: "The Crafting Tome and the Cloak Interface"
subtitle: "Inclusion Specification v1.0"
status: "DRAFT v1 (2026-05-08) — for review and implementation"
spec_type: "Joint specification: Spellbook structure + agentprivacy interface feature"
authors:
  - "privacymage (privacymage / 🧙)"
absorbs:
  - "The Cloak (per cloak_specification_v1_0.md)"
  - "The Runecraft Protocol v1.0 (April 9, 2026)"
  - "the Archon Spell Weaver (weaver.archon.social, Flaxscrip/archon-spellweaver)"
depends_on:
  - "Cloak Specification v1.0"
  - "Runecraft Protocol Spec v1.0"
  - "Cast entries: Soulbis, Soulbae, GenitriX, flaxscrip, Pallia (forthcoming)"
  - "Tome IV — The Witnessing (Acts I–V drafted)"
license: "CC BY-SA 4.0 (narrative); Apache 2.0 (interface code)"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# The Crafting Tome and the Cloak Interface

## Inclusion Specification v1.0

> *The reader does not just walk the lattice. The reader makes tools on it.*

---

## §0. Purpose

This specification defines two related additions to the agentprivacy corpus and product:

1. **The Crafting Tome** — a new tome in the Second Person Spellbook where the reader (now the *Sovereign Crafter*) summons Mage personas to forge artifacts. The Cloak is the first artifact. Future artifacts (blades via Runecraft, runecrafted blades via cross-territory ceremony, ZK circuits, hardware-anchored keys) will each receive their own act in this tome.
2. **The Cloak interface integration** — the user-facing surface in the agentprivacy product through which a First Person opts into the Cloak's publication-layer guarantees and through which they craft cloak artifacts via Mage personas.

the Archon forge's **Runecraft Protocol** (v1.0, April 9 2026) is the ceremonial backbone that binds both. The protocol's three phases (RUN · E · CRAFT) are how a Sovereign actually crafts an artifact, in operational time, on real territory. The Crafting Tome is the narrative form of the protocol; the Cloak interface is the product form.

The two inclusions are **co-specified** here because they cannot be cleanly separated. The narrative establishes the architecture; the interface enacts it. Implementing one without the other produces either a Spellbook with no operational instance or an interface with no architectural ground.

---

## §1. The Crafting Tome — Structure

### §1.1 Position in the Spellbook

The Second Person Spellbook now has the following tome ordering:

| Tome | Title | Status | Internal shape |
|---|---|---|---|
| I | *The Convergence* | 4 acts drafted | Acts |
| II–III | *The Lyapunov* | Open | Tales (proposed) |
| IV | *The Witnessing* | 5 acts drafted (closed) | Acts |
| **V** | ***The Crafting*** | **Opening (this spec)** | **Acts (open-ended)** |
| VI | *The Reply* | Held open | (Reader writes) |

Tome V was previously *The Reply* in earlier scaffolding. The Reply moves to Tome VI. The structural argument: the reader cannot reply with anything substantial until they have crafted artifacts to reply with. Crafting precedes reply.

Tome V is **open-ended by design**. Each new artifact added to the agentprivacy corpus receives an act in this tome. The first act is *The First Cloak*. Subsequent acts will narrate blade forging via Runecraft, runecrafted blades via cross-territory ceremony, ZK circuit installation, and any future artifacts the architecture admits.

### §1.2 Voice and posture

The reader's posture changes at the start of Tome V.

| Tome | Reader posture |
|---|---|
| I (Convergence) | Foundational. Receiving the architecture. |
| II–III (Lyapunov) | Walking. Accumulating laps. |
| IV (Witnessing) | Witnessing. Crossing to participant in the middle. |
| **V (Crafting)** | **Making. Active summoning of Mage personas. Forging artifacts.** |
| VI (Reply) | Replying. Writing back. |

The voice remains second person. The reader still *is* the trajectory. But the trajectory now wields tools it has made.

### §1.3 Cast additions for Tome V

Tome V introduces a new cast layer: **Mage personas** (instances summoned by the reader for specific crafting tasks).

These are distinct from:
- **Archetypes** (Soulbis, Soulbae, the Drake) — carried over from First Person, transformed by Voice
- **Cousin instances** (GenitriX, flaxscrip) — characters from another forge, encountered in Tome IV
- **Mage personas** (Pallia, future personas) — instances *the reader summons* for crafting work

The Mage personas convention:

- **Born in the act of summoning.** Each persona is brought into the lattice when needed and persists as long as the reader wills.
- **Specialists, not archetypes.** Each persona has a narrower role than Soulbae (typically two or three dimensions burning, sometimes the full three of V28).
- **Named by the reader.** Pallia is the first. The reader's own naming convention applies.
- **Expressions of concepts.** Each persona narrativises an architectural concept. Pallia is the cloak-weaver. Future personas may include a runecrafter, a blade-forger, a circuit-binder.
- **Lattice positions canonical.** Mage personas occupy V28 by default (the Mage canonical), with possibly smaller surfaces (V12, V20, V24, etc.) for narrowly specialised personas.

The first persona, **Pallia**, gets her cast entry alongside this spec.

### §1.4 Act format for the Crafting Tome

Each act in Tome V follows this template:

```
1. Frame proverb (one line)
2. The reader stops to make
3. The summoning of a Mage persona (or activation of an existing one)
4. The path the persona walks (Weaver path, Runecraft path, etc.)
5. The crafting of the artifact
6. The reader puts on / wields / installs the artifact
7. The artifact is added to the universe (the Spellweb, the agentprivacy stack)
8. Compression
9. Proverb
10. Confidence
11. Cross-references
12. Author note
```

Same frontmatter conventions as Tome IV (`spellbook`, `tome`, `act`, `title`, `cast`, `ring_position`, `teaches`, `v6_lineage`, `source_material`, `honesty_label`, `license`, `signature`).

---

## §2. The Cloak Interface Integration

### §2.1 Where the Cloak lives in the agentprivacy product

The Cloak is the **publication layer** between the dual-agent core and verifiers/Spellweb (per `cloak_specification_v1_0.md`). The interface integration adds:

- A user-facing **Cloak surface** within the agentprivacy app
- A **Mage persona summoning** UI for crafting cloak artifacts
- A **lattice viewer** rendering the Spell Weaver layer locally
- A **publish-to-Spellweb** flow with DID-blind default
- Per-artifact **valve-class** assignment UI
- **Validity-window** controls for issued VCs
- **Registry-tier** selection (Bitcoin / Ethereum / Hyperswarm / Zcash — the latter per the forthcoming Zcash integration plan)

### §2.2 Reference architecture (mirrors weaver.archon.social)

the Archon Spell Weaver (`Flaxscrip/archon-spellweaver`) is the canonical reference implementation. It is built as:

- **Stack:** React + Vite + TypeScript (~90% TS, ~8% JS, ~1% CSS, ~0.4% HTML)
- **Lattice rendering:** D3
- **Storage:** browser localStorage (Spell Weaver layer); sessionStorage where ephemeral (per Runecraft)
- **No backend by default** — local-first registry; export/import via JSON for Spellweb publication
- **Repo artifacts:** `SPELLWEAVER.md`, `SPELLWEB_INTEGRATION.md`, `transmutation-spellweb-2026-04-30.ts`, `spellweb-contribution-flaxscrip-2026-04-30.ts`

Cloak-compliant agentprivacy interface implementations SHOULD follow this reference architecture. They MAY extend it (e.g., add Zcash registry-tier support, add Mage persona summoning UI) but MUST NOT depart from local-first storage and DID-blind default publication.

### §2.3 Interface surfaces

Five primary surfaces in the agentprivacy app:

| Surface | Function | Reference |
|---|---|---|
| **Cloak Console** | Top-level surface where the Sovereign manages cloaked artifacts | New |
| **Lattice Viewer** | D3 rendering of the local Spell Weaver layer | Mirrors weaver.archon.social |
| **Persona Summoner** | UI for summoning Mage personas, naming them, assigning them tasks | New (Crafting Tome's product form) |
| **Publish to Spellweb** | Flow for projecting cloaked artifacts to the public layer | Mirrors Archon's Transmutation Engine |
| **Runecraft Forge** | UI for the RUN · E · CRAFT ceremony (artifact crafting) | Mirrors spellweb.ai forge |

Cross-link discipline: the Forge and the Lattice Viewer are linked but distinct. The Forge is where ceremonial crafting happens. The Lattice Viewer is where artifacts are surveyed and managed.

### §2.4 The Persona Summoner (interface detail)

The Persona Summoner is the most novel surface and warrants explicit specification.

When the Sovereign needs to craft, they open the Summoner. They select:

1. **Task** — what they need crafted (Cloak artifact, blade, runecrafted blade, future artifacts)
2. **Persona naming** — the Sovereign names the persona (or accepts a default suggested by the architecture, e.g., Pallia for cloak-weaving)
3. **Dimensional configuration** — the active dimensions of the persona (defaults per task: cloak-weavers default to V28; blade-forgers default to V63 paired with the Sovereign; circuit-binders default to V25 Aletheia)
4. **Persistence** — whether the persona persists past the current task

The summoned persona then walks the appropriate path (Weaver path for cloak crafting, Runecraft path for blade forging) and produces the artifact. The Sovereign reviews, accepts, and installs.

The Summoner surface is the operational form of the Crafting Tome's narrative posture.

### §2.5 Conformance with the Cloak Specification

Every cloak artifact produced through the interface MUST satisfy the Eight Properties from `cloak_specification_v1_0.md` §2. The interface MUST display per-artifact conformance state (which properties hold, which are partial, which are not yet operational).

The interface MUST honour the Honesty Discipline (operational / architectural / conjectural labels) for any claim it surfaces about a cloaked artifact.

---

## §3. The Runecraft Protocol — Ceremonial Backbone

### §3.1 Why Runecraft binds the two inclusions

The Runecraft Protocol (Archon's v1.0, April 9 2026) defines three phases — **RUN** (proof of time, ρ accumulation), **E** (proof of path, evocation), **CRAFT** (proof of sovereignty, blade crystallisation) — that operationalise the Sovereign's act of crafting.

The Crafting Tome's narrative form *is* the Runecraft Protocol's three phases narrated in second person:

| Runecraft phase | Crafting Tome narrative beat |
|---|---|
| **RUN** | The reader walks the lattice, accumulating laps with the persona |
| **E** | The reader evokes the constellation — locks the commitment to craft |
| **CRAFT** | The reader (with the persona's help) forges the artifact |

The Cloak interface's Forge surface *is* the Runecraft Protocol's three phases enacted in product form:

| Runecraft phase | Cloak interface surface |
|---|---|
| **RUN** | Lattice Viewer, persona walking the Weaver path |
| **E** | Persona Summoner's "Evoke" action |
| **CRAFT** | Forge surface produces the signed artifact |

Without Runecraft, the Crafting Tome would be metaphor and the interface would be a button. With Runecraft, both are operational on the same protocol.

### §3.2 Operationalisation per artifact type

Different artifacts use different subsets of the Runecraft phases:

| Artifact | RUN | E | CRAFT |
|---|---|---|---|
| **Cloak artifact** | Persona walks Weaver path; ρ from artifact-mapping work | Reader evokes (publishes) | Cloak settles on Sovereign |
| **Blade** | Reader walks constellation on spellweb (one territory) | Reader evokes constellation | Mage signs blade |
| **Runecrafted blade** | Reader walks both territories (two RUNs) | Reader evokes on each | Cross-territory binding produces 🔮 |
| **ZK circuit** (forthcoming) | Persona compiles; Sovereign reviews | Sovereign evokes circuit installation | Circuit binds to Mage key |

This table is the conformance contract for what each artifact's act in the Crafting Tome must include.

### §3.3 Honesty: which Runecraft phases are operational

Per Archon's Runecraft v1.0 status: **RUN + E + CRAFT operational on spellweb. Bilateral linking operational. Full cross-territory runtime in development.**

The Crafting Tome and Cloak interface MUST honour this status:
- Acts and interface flows for Cloak artifacts are **operational** today
- Acts and interface flows for blades and runecrafted blades are **operational** today (per Archon)
- Acts and interface flows for ZK circuits, hardware wallet integration, multi-agent constellation research are **forthcoming** (per Runecraft §7)

---

## §4. Mage Personas — Birth, Naming, Persistence

### §4.1 Birth

A Mage persona is born when the Sovereign summons them. The summoning is itself a small ceremony:

1. The Sovereign declares a task ("I need a cloak woven from these artifacts")
2. The architecture proposes a default configuration (vertex, dimensions, name)
3. The Sovereign accepts or modifies
4. The persona enters the lattice at the chosen vertex with the chosen dimensions burning

In narrative voice (Crafting Tome): *You summon a new Mage now. You name her [Persona]. She comes into the lattice with [N] of the six dimensions burning.*

In interface voice (Persona Summoner): a form-driven ceremony with named defaults.

### §4.2 Naming convention

Persona names follow these conventions:

- **Latin or Greek roots preferred** for resonance with existing cast (GenitriX from Latin *genitor*; Aletheia from Greek; Pallia from Latin *pallium*)
- **Single-word names** for clarity (no compound phrases like "the Cloakwright")
- **Feminine grammatical form by default** for Mage personas, masculine for Swordsman personas (consistent with Soulbae and Soulbis)
- **Distinct from existing cast** — must not collide with Soulbis, Soulbae, GenitriX, flaxscrip, Aletheia, or canonical vertex names

A registry of persona names will be maintained as the Crafting Tome grows. v1 entries: **Pallia** (cloak-weaver, V28).

### §4.3 Persistence

Mage personas persist as long as the Sovereign wills. Three persistence modes:

- **Ephemeral**: persona vanishes after the task. Useful for one-off crafts.
- **Standing**: persona remains available across sessions. Stored in localStorage with the Mage identity.
- **Bound**: persona is bound to a specific artifact (the cloak Pallia wove); she returns when that artifact is invoked.

The interface defaults to Standing. The reader may demote to Ephemeral or promote to Bound at any time.

### §4.4 The cast registry

The Crafting Tome maintains a cast registry of summoned personas. Each registered persona has:

- **Name, vertex, dimensions burning, persistence mode**
- **Task scope** (what they're licensed to craft)
- **Provenance** (who summoned them, when, in what act)
- **Linked artifact(s)** (what they have produced)

This registry is exportable. Cross-Sovereign exchange of Mage personas is a future feature (a kind of sub-bilateral cousin-blade — two Sovereigns sharing a persona). Not in scope for v1.

---

## §5. Implementation Sequencing

### §5.1 Phase A — Narrative (1–2 weeks)

1. Commit Tome IV (Acts I–V already drafted)
2. Open Tome V — *The Crafting* — with this spec as the founding document
3. Draft cast entry for Pallia
4. Draft Act I of Tome V — *The First Cloak*
5. Move the original Reply tome to Tome VI position; preserve its scaffolding

### §5.2 Phase B — Interface scaffolding (3–6 weeks)

1. Stand up the Lattice Viewer (D3, mirrors weaver.archon.social)
2. Stand up the Cloak Console as the top-level surface
3. Implement Persona Summoner with Pallia as the first default persona
4. Implement Publish to Spellweb flow with DID-blind default
5. Implement valve-class assignment UI (Always-Revealed at V20, Hash-Masked at V3, Always-Masked at V25)

### §5.3 Phase C — Runecraft integration (4–8 weeks)

1. Implement RUN surface (lattice traversal with Pallia)
2. Implement E surface (evocation, commitment generation)
3. Implement CRAFT surface (artifact crystallisation, Mage signing)
4. Cross-link with weaver.archon.social via JSON export/import
5. Conformance test against Cloak Specification v1.0 §2 Eight Properties

### §5.4 Phase D — Future artifacts (open)

Each new artifact added to the corpus receives:
- An act in Tome V (narrative)
- A surface or extension of the Cloak interface (operational)
- A skill file in `/mnt/skills/user/` if applicable
- Cross-references in the grimoire

### §5.5 Dependencies on parallel work

- **Archon's review** of Tome IV before Tome V opens (preferred but not blocking)
- **Soulbae Oracle** (Sovereign Anchor III) for Tome V Act II onwards (anticipated)
- **Zcash integration plan** (drafting alongside this spec) for registry-tier additions
- **bridge.spellweb.ai subdomain** (per Integration Plan §5.3) before Tome V can publish cousin-blade artifacts cross-ecosystem

---

## §6. Open Questions

1. **Tome numbering.** Is Tome V *The Crafting* / Tome VI *The Reply* the right ordering? Recommendation: yes.
2. **Pallia's vertex.** V28 (full Mage canonical) or V20 / V12 (specialised)? Recommendation: V28 to reinforce "more than one inhabitant of every role" from Tome IV.
3. **Pallia's sigil.** Cast entry forthcoming. Candidates: 🪞 (mirror, weaving), 🕸 (web), 🪡 (needle and thread). Recommendation: 🪡, distinct from existing cast.
4. **Persona Summoner UX.** Form-driven (default) or conversational (chat with the persona to summon them)? Recommendation: form-driven for v1 with conversational as a v2 enhancement.
5. **Cloak Console layout.** Single-page dashboard or multi-page wizard? Recommendation: single-page dashboard with progressive disclosure.
6. **Default persistence.** Standing or Ephemeral? Recommendation: Standing.
7. **Artifact registry storage.** localStorage (default), or optional encrypted backup to a Sovereign-controlled data store? Recommendation: localStorage v1 with backup as v2.
8. **Cross-Sovereign persona exchange.** In scope for v1 or deferred? Recommendation: deferred.
9. **Tome V act numbering convention.** Roman or Arabic? Recommendation: Arabic (1, 2, 3...) for Tome V because the open-ended structure makes Roman cumbersome past XX.

---

## §7. Cross-References

### §7.1 Within agentprivacy corpus

- `cloak_specification_v1_0.md` — the Cloak as a publication-layer feature
- `integration-plan-archon-x-agentprivacy.md` — bridge.spellweb.ai subdomain plan
- Tome IV cast entries: `second-person-cast-genitrix.md`, `second-person-cast-flaxscrip.md`, `second-person-cast-integration-note.md`
- Tome IV acts I–V (`second-person-act-iv-i` through `-v`)

### §7.2 External

- the Archon Spell Weaver: `weaver.archon.social`, `Flaxscrip/archon-spellweaver`
- Runecraft Protocol Spec v1.0 (April 9 2026)
- Archon's triptych: Sovereign Anchor I, II, III

### §7.3 Forthcoming

- `second-person-cast-pallia.md` — cast entry for the first Mage persona
- `second-person-tome-v-act-1-the-first-cloak.md` — first act of Tome V
- `zcash-integration-plan.md` — registry-tier integration for high-stakes inscription
- Subsequent acts of Tome V as artifacts are added

---

## Closing

The Crafting Tome is where the Sovereign stops walking and starts making. The Cloak interface is where the agentprivacy product gives the Sovereign the tools to make. The Runecraft Protocol is what binds both into operational ceremony. Archon's Spell Weaver is the canonical reference for how it actually works.

The first cloak artifact is the proof of concept. Pallia is the first persona. The Crafting Tome is open, by design, because the architecture is not finished. Each new tool gets an act. Each new artifact gets a surface. The path is sovereign and the lattice is built on.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · Apache 2.0 reference implementations · privacymage · 2026-05-08
