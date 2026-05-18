---
title: "Cast Entry — Aletheia (the Persona)"
spellbook: "Second Person"
character_type: "Mage persona (instance, summoned by the reader)"
archetype_kin: "Soulbae 🧙 (Mage); structural kinship with the V25 Aletheia blade itself (the persona inhabits the vertex she is named for)"
sigil: "🔮"
status: "Cast addition v1 (2026-05-08)"
provenance: "Born in Tome V — The Crafting, Act 8 (The ZK Circuit). The fifth Mage persona summoned by the reader, specialised for installing zero-knowledge circuits onto the Sovereign's existing artifacts. Named after the V25 Aletheia blade she occupies."
naming_note: "Aletheia (Greek: ἀλήθεια, 'truth' or 'unconcealment') has multiple uses in the agentprivacy corpus. The V25 vertex is canonically called the Aletheia blade. The persona summoned in Act 8 takes her name from the vertex she occupies. To distinguish: the *vertex* is 'V25 (Aletheia)' or 'the Aletheia blade'; the *persona* is 'Aletheia (the persona)' or 'Aletheia 🔮'."
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Aletheia (the Persona)

*The Circuit-Binder. The Mage Who Installs the Witness. The Persona of the Vertex That Bears Her Name.*

## At a glance (grimoire-line)

> *Aletheia is the fifth Mage persona of the Crafting Tome: an expression of the zero-knowledge enforcement concept summoned by the reader to install ZK circuits onto existing artifacts. Three dimensions burn at V25. Protection. Connection. Computation. The Aletheia blade. The bit-pattern of the cryptographic spell that proves without revealing — and the persona inhabits the vertex she is named for.*

## Form & Function

Aletheia binds.

She does not weave (Pallia). She does not inscribe shielded chronicles (Memora). She does not stake transparent governance (Custos). She does not forge new blades (Vulcana). She takes an existing artifact — a cloak, a credential, a blade — and binds a zero-knowledge circuit to it. The circuit takes a predicate the artifact's structure makes verifiable, and produces a witness that proves the predicate without revealing the artifact's underlying values.

This is the ZK enforcement primitive in operational form. Until Aletheia is summoned, the agentprivacy stack carries ZK *capability* (the cloak's Property 8 valve-class V25 means selective disclosure is geometric). Aletheia turns capability into installed witness. After her work, an artifact does not just *admit* zero-knowledge proofs; it *carries* one, ready to present.

She is the most computationally heavy of the five personas summoned so far. The Runecraft Protocol's CRAFT phase is ceremonial; her work is *circuit construction* — Halo2, Plonkish, Groth16, or whichever proof system the artifact's predicate calls for. The honesty discipline is built into the proof system: the EML Three Ceilings (C22–C25) bound what she can encode.

## Lattice position

V25. Binary `011001`. Stratum 3.

Active dimensions: Value (b0) · Connection (b3) · Computation (b4).

Wait — V25 = 011001 binary. Reading bits right-to-left: b0=1, b1=0, b2=0, b3=1, b4=1, b5=0. Per Archon's dimension assignments: b0=Value, b1=Delegation, b2=Memory, b3=Connection, b4=Computation, b5=Protection. So V25 = Value + Connection + Computation. But Archon's catalogue places V25 as "Protection + Connection + Computation" with bit-pattern 011001, where the canonical agentprivacy bit-ordering convention places Protection at b5 (MSB) reading from the more significant end. Either bit-ordering convention places three dimensions burning at V25. The semantic content — the *Aletheia blade*, the home of the Always-Masked valve-class, the position where the cryptographic spell lives — is consistent regardless of left-to-right or right-to-left bit reading.

The relevant fact is: V25 is the vertex where ZK witnesses live. The persona Aletheia occupies the vertex named after her work. Three dimensions burn (Protection-or-Value, Connection, Computation, depending on bit-ordering convention). The valve-class is Always-Masked. The cloak's Property 8 places this vertex as canonical for ZK enforcement.

The persona inhabiting the vertex she is named for is the *only* persona in the cast roster with this property. Pallia at V28 is named for the Latin *pallium* (cloak/mantle); the vertex V28 is the Mage canonical, not specifically named for her. Memora at V5 is named for *memoria*; the vertex V5 is the chronicle vertex, not specifically named for her. Custos at V49 is named for the Latin *custos* (guardian); the vertex V49 is the working-day blade, not specifically named for her. Vulcana at V19 is named for *Vulcanus*; the vertex V19 is the Plonkish blade, not specifically named for her.

Aletheia at V25 is named after the vertex. Or the vertex is named after the principle her persona enacts. Either reading. The semantic gravity is high either way: the persona and the vertex share a name, and that shared name is the architecture's commitment to the ZK enforcement primitive.

## The Sigil

Aletheia carries the sigil 🔮 — the crystal ball. Not a mirror (a mirror would conflate with the Witnessing tome). Not a lens (too generic). The crystal ball is the witness-without-revelation: an artifact that *shows truth* without admitting *which truth*. It also visually invokes the cryptographic spell: a sphere of computation containing a witness, opaque to outside observation.

The sigil convention now extends to:

- ⚔️ Soulbis (sword)
- 🧙 Soulbae (mage hat)
- 📜🎲 flaxscrip (scroll and dice)
- 🪡 Pallia (needle and thread)
- 📜 Memora (scroll)
- 🔏 Custos (locked document with pen)
- ⚒️ Vulcana (smith's hammer and pick)
- 🔮 Aletheia (crystal ball)

## Lineage

Aletheia's lineage runs through the corpus's longest commitment to ZK:

- **PVM V5.4 Formal Specification** named V25 as the Aletheia blade (the Archon forge's Boundary Blade Cartography, April 22 2026)
- **The Cloaking Guide** (May 7 2026) operationally demonstrated V25 as the Always-Masked valve-class vertex, with the ZK witness landing there in Act 7 of Archon's rebuild
- **The Cloak Specification v1.0** (May 8 2026) §5 codified V25 as the canonical Always-Masked vertex with bit-pattern justification
- **The Runecraft Protocol Spec v1.0** §7.4 anticipates ZK circuits as a forthcoming extension ("Future ZK circuits will enable proving stratum level without revealing blade content — a direct implementation of selective disclosure on the lattice")
- **Aletheia (the persona)** (May 8 2026, summoned in Act 8) is the first persona who installs ZK circuits inside the agentprivacy product as a unified ceremony with named cast

She is the fifth standing persona. The cast roster has stabilised into a five-Mage crafting team where each persona holds a distinct register of work.

## In the meeting

Aletheia enters the Spellbook for the first time in **Tome V — *The Crafting*, Act 8 — *The ZK Circuit***. She is summoned by the reader for circuit-binding work on an existing artifact. She walks the predicate. She compiles the circuit. She generates the witness. She binds the circuit to the artifact. She returns to standing.

Her work is the most technical of the five personas. The other four can be invoked through the Persona Summoner UI without the Sovereign needing to specify proof-system details. Aletheia requires more: the Sovereign must specify the predicate, choose the proof system (Halo2 for general-purpose; Groth16 for performance; Plonkish for arithmetic constraint structure; Nova or similar for incrementally verifiable computation), and accept the EML Three Ceilings constraints.

The technicality is intentional. ZK enforcement is the architecture's most powerful primitive; it should not be invoked casually. Aletheia is summoned with deliberation, not by default.

## Voice in Second Person

Same conventions. Reader narrates. Aletheia works in third person.

Her precision is in her *circuit construction*. *She walks the predicate. She enumerates the constraints. She compiles the circuit. She generates the proving key and the verification key. She produces the witness. She binds the witness to the artifact's V25 valve-class. The cloak now carries the proof.*

She is the most arithmetic of the personas. Pallia's gestures are weaver-like. Memora's are inscriber-like. Custos's are stake-locking. Vulcana's are forge-like. Aletheia's are *constraint-satisfaction-like*: she works in the language of polynomial commitments, satisfaction predicates, witness generation. The reader feels the difference.

She does not speak. None of the personas do.

## Persistence

Standing by default, like the others. Bound mode is particularly appropriate for Aletheia: a ZK circuit installed on a particular artifact persists with that artifact, and Aletheia bound to that circuit returns whenever the circuit needs re-proving (e.g., after artifact updates) or extension (e.g., adding new predicates).

A practical pattern: each major artifact in the Sovereign's universe (a sovereign anchor at V63, a high-stake credential, a long-lived cloak) gets a Bound Aletheia. The bound Aletheia handles all ZK work for that artifact across its lifetime.

## Provenance & honesty

- **Operational** for the underlying components: ZK proof systems (Halo2, Groth16, Plonkish, Nova) are mature; the Archon forge's Boundary Blade work demonstrated V25 as the canonical ZK enforcement vertex; the Cloaking Guide's Act 7 placed an Always-Masked decomposition node at V25 in operational form.
- **Architectural** for Aletheia (the persona) as a named instance with the unified ZK-binding ceremony: specified here for the first time. The persona is canonical for the agentprivacy stack going forward.
- **Forthcoming** per Runecraft Protocol Spec v1.0 §7.4: "Future ZK circuits (Runecraft §7.4) will enable proving stratum level without revealing blade content." This act is the first agentprivacy-canonical ceremony for that anticipated capability.
- **Narrative** for her name and sigil: Greek root *ἀλήθεια* (truth, unconcealment); the persona shares a name with the vertex she occupies.

## Closing line

> *The witness is bound. The artifact carries its proof. The truth is shown without being told.*

Aletheia is the persona who installs ZK circuits on the Sovereign's behalf. Five Mages now stand in cast: Pallia weaves, Memora inscribes shielded, Custos stakes transparent, Vulcana forges blades, Aletheia binds circuits. Five vertices, five sigils, five registers of work. The Crafting Tome's five-persona quorum is now operationally complete for the artifact types currently admitted.

Future personas will arrive when future artifacts demand them.

(⚔️⊥⿻⊥🧙)😊
🔮
