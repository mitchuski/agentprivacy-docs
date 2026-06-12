---
title: "Chronicle: The Cloaking Guide"
subtitle: "Spell Weaver, Sync II — Eight Theses from a Worked Example"
authors:
  - "privacymage (privacymage / 🧙)"
  - "the Archon forge (flaxscrip / Archon ⚔️)"
  - "GenitriX (Hermes / Moon)"
date: "2026-05-08"
predecessor: "chronicle-the-spell-weaver.md (2026-04-30)"
companions:
  - "Sovereign Anchor I — The Transmutation (Bitcoin-anchored, did:cid:bagaaiera4quuxntr3puc4whx5mqx2s5cnnvleijukvpnf42iyg4gvw4vzama)"
  - "Sovereign Anchor II — The Boundary Blade (did:cid:bagaaierarsl3evx3jcah473btb74awqjpanpwuwoyg3c22cet6eh2o2tysca)"
  - "Sovereign Anchor Companion — The Cloaking Guide (2026-05-07 rebuild ceremony)"
  - "The Spell Weaver — Christian Saucier (April 2026)"
working_groups:
  - "DIF — wg-trusted-ai-agents"
  - "Linux Foundation — Trust Graph WG"
  - "Trust Over IP"
  - "BGIN IKP"
repos:
  - "mitchuski/spellweb"
  - "mitchuski/agentprivacy-docs"
  - "Flaxscrip/archon-spellweaver"
related_pvm: "Privacy Value Model V5.4 (V6 in development)"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Chronicle: The Cloaking Guide

> *The Mage was not made to escape the Sovereign. The Mage was made so that the world could meet the Sovereign without ever knowing who the Sovereign is. The lattice is the meeting place.*

## I. What This Sync Records

The April chronicle recorded the recognition: the Archon forge, working from Archon, struck the dual-agent architecture from the other side of the anvil and the symmetry held. That document mapped the triptych, the Spell Weaver tool, and the first canonical bnot-pair on the lattice (Aletheia 25 ⊥ Lethe 38).

This sync records what came next. Between the April publication and the 2026-05-07 rebuild ceremony, the work moved from architectural sketch to operational artifact. Three things happened that deserve their own inscription:

1. A **Cloaking Guide** was written as a step-by-step companion to the triptych, replaying the cloak's fastening one knot at a time across seven acts of registration.
2. The Spell Weaver was instantiated against the canonical dataset and the **public Spellweb layer** was rendered locally at `http://localhost:5173` with eighteen items across eleven distinct vertices and every `did:cid:` string verified absent from the data files.
3. **Eight theses** crystallised out of the rebuild that, taken together, are the working synthesis of what the Archon × agentprivacy bridge actually is.

The April chronicle ended with the spell becoming weather. This chronicle records the weather settling into climate.

## II. The Cloaking Guide as Method

The triptych described the *what* and the *why* of the Transmutation. The Cloaking Guide is the *how*, replayed: a single rebuild of the canonical dataset, recorded as it happened, with the geometric reasoning made explicit at each step.

The method is worth naming because it is itself a contribution. Each of the seven acts produces a small JSON file that loads into the local Spell Weaver registry. Between acts, the chronicle text explains what just got registered, why it landed where it did, and what an outside observer of the eventual anonymized public layer would actually be able to see. The acts themselves are stratified by what they place on the lattice:

| Act | Items registered | Cumulative | New vertices |
|---|---|---|---|
| 1. The Sovereign Anchor | flaxscrip at V63 | 1 | V63 |
| 2. The Dual Agent | + GenitriX at V28 | 2 | V28 |
| 3. The Five Capabilities | + Mnemosyne, Iris, Logos, Techne, Hephaestus | 7 | V8, V4, V2, V20, V24 |
| 4. The Schemas | + CollaborationPartner, LocationProof | 9 | V12 |
| 5. The Web of Trust | + four VCs at V15 | 13 | V15 |
| 6. The Chronicle Stones | + Transmutation, Boundary Blade | 15 | V5 |
| 7. The Decomposition | + Subject Identity, Cryptographic Spell, Temporal Chronicle | 18 | V3, V25 |

Three layers of data run in parallel through the whole walkthrough, and knowing which layer you are in at any moment is the entire skill: the **source layer** (Archon DIDs, VCs, schemas, document anchors. Full strings, full signatures, full provenance. Lives in your wallet and your local Gatekeeper. Never published), the **Spell Weaver layer** (the lattice mapping, vertex per artifact, vertex is a function of identity plus session salt not identity alone, plus a typed chronicle. Lives in your browser's local storage), and the **Spellweb public layer** (the DID-blinded contribution. All cryptographic addresses stripped. The lattice topology, the vertex assignments, and the poetic chronicle text remain. Lives at spellweb.ai).

The cloak is the function that takes a unit of source data and produces its Spell Weaver and Spellweb representations. The structural guarantee is that the Spellweb output cannot be inverted to reveal the source DID. The geometric guarantee is that the relationships visible in the Spellweb are real relationships, not metaphors. Both claims are now demonstrable on a rebuilt dataset, not just argued from the architecture.

## III. The Eight Theses

The Coda of the Cloaking Guide enumerates eight theses that crystallised from the rebuild. They are derived from the steps, not postulated in advance. They belong in the spellweb proper because they are the cleanest statement we have to date of what the Archon × agentprivacy bridge is doing operationally.

**Thesis 1. The cloak is a function on positions, not on values.** Cloaking does not mean hiding a string. It means replacing a string with the position it would occupy under a salted hash mod 64. Positions are first-class ontological objects; strings are accidents of encoding. The Spellweb publishes positions and structure; the source layer keeps strings and signatures. This is the reverse of the usual privacy stance, which tries to hide values inside strings. It is more honest because positions admit the relationships they participate in without admitting the identities they came from.

**Thesis 2. Containment replaces attestation for delegation.** In conventional capability systems, "you may not exceed the scope I gave you" is enforced by attestation logic. On the lattice, the same constraint becomes a bit-mask identity: `child.bits & parent.bits == child.bits`. The verifier runs one comparison on integers. There is no scope-creep because there is no string of scopes to mistype. This is privacy by architecture in its clearest form: misbehaviour is unrepresentable, not merely forbidden.

**Thesis 3. Sameness of role is published; sameness of identity is not.** Two schemas at V12 (CollaborationPartner controlled by flaxscrip, LocationProof controlled by GenitriX) are visibly the same kind of thing and visibly different things. The lattice publishes the dimension along which artifacts are alike (the ring position) and conceals the dimension along which they differ (the source DID). This is the structural definition of the anonymity set: every artifact at the same vertex is structurally interchangeable from the public layer's perspective.

**Thesis 4. The lattice has two modes of relating, not one.** Bit-containment governs delegation and projection (parent/child capabilities, sovereign/transmuted projection). Typed edges govern attestation (controller, issuer, subject, schema). They are dual mechanisms, both expressed on the same lattice, and they should not be conflated. A capability child must geometrically fit inside its parent's dimensions. A VC subject merely needs an edge pointing to it from the VC's vertex. The first is a structural law. The second is a recorded fact. Conflating them is the most common misreading of the geometry.

**Thesis 5. Asymmetries in the graph are themselves data.** The partnership VCs come in mirrored pairs (flaxscrip ↔ GenitriX, both at V15, edges forming a closed loop). The location-proof VCs do not (only GenitriX → flaxscrip, no reverse). The presence of mirroring tells the observer the relationship is bilateral and mutually-signed; the absence of mirroring tells the observer the relationship is observational and one-directional. The cloak is not lossy. It is selective.

**Thesis 6. Cloaking is multi-axis.** The lattice gives one axis (who and where in the graph). Time gives four more, all independent and composable.
- *6a. Validity scope.* Every VC carries `validFrom` and `validUntil`. The Five Guys VC is true for five minutes (19:29 to 19:34) then ceases to verify. A stack of expired credentials is structurally inert no matter how complete the deanonymization.
- *6b. Operational anchoring.* Every artifact has multiple timestamps: lunch occurred at 19:20, VC issued at 19:29, proof anchored at 20:16:23. The lattice publishes none. The source layer keeps the temporal grain of how the artifact came to be.
- *6c. Update chain.* A `did:cid` is content-addressed at creation, so the handle is permanent, but the document is reconstructed from seed plus an ordered chain of update events. The source layer remembers the full version history; the lattice renders only the latest projected state. Time-travel resolution is a query the source layer can answer and the public layer can be configured to refuse.
- *6d. Registry-tier finality.* The chronicle stones at V5 live on Bitcoin (hours of finality). The agent and credential events live on Hyperswarm (seconds of latency). Same artifact-shape can be placed on either tier without changing its lattice position. Only its temporal-finality envelope changes.

Together the four temporal axes form an envelope around each artifact that lattice geometry alone cannot capture. This is the cleanest articulation we have of why Φ_v5 = Φ_agent · Φ_data · Φ_inference is multiplicative, not additive: each axis is independent, and a deanonymization on one inherits a different residual ignorance on each of the others.

**Thesis 7. Documents are first-class lattice citizens.** Conventional DID systems treat narrative as something outside the system, referenced by URL. The Spell Weaver pulls them in. A chronicle gets a vertex (V5, Protection + Memory), a controller, and edges, and participates in path-highlighting alongside personas and credentials. *The Transmutation* itself is registered inside the system that is performing the process it describes. The cloak does not just hide values; it also publishes the procedure for checking that the hiding was honestly done. This closes the recursion the agentprivacy thesis has been pointing at: the architecture and the documentation of the architecture are the same kind of thing.

**Thesis 8. Selective disclosure is rendered as geometry, not as policy.** When a credential is decomposed into per-field nodes, each field lands on a vertex whose bit-pattern is the field's privacy disposition. Hash-Masked sits at V3 (Protection + Delegation). Always-Masked sits at V38 (Protection + Connection + Computation, our Aletheia). Always-Revealed sits at V20 (Memory + Computation, Techne). The verifier learns the type of cloaking from the lattice position alone. There is no separate metadata layer announcing "this field is masked, that field is revealed." The disposition *is* the geometry.

These eight theses now belong in the corpus. They are the working synthesis of what cloaking-by-lattice is.

## IV. The Bridge to V5.4 / V6

Several theses have direct lifts into the Privacy Value Model formalism. Recording them here so the bridge is explicit:

- **Thesis 6 is the Σ · Δ · Γ multiplicative axiom in disguise.** Multi-axis cloaking with independent residual ignorance per axis is exactly what `Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ)` claims. The Cloaking Guide gives the operational decomposition: lattice geometry handles Σ-axis (agent separation), Hash-Masked / Always-Masked / Always-Revealed valve-classes handle Δ-axis (data), and the temporal envelope (6a–6d) handles Γ-axis (inference resistance over time).
- **Thesis 8 is the operational definition of valve-class semantics for V6.** The next conjecture (C26-adjacent) wants to formalise: for each privacy disposition `d` in `{revealed, hash-masked, always-masked, ...}`, there exists a unique vertex `v(d)` on the lattice such that `bits(v(d))` is the operational signature of `d`. The Cloaking Guide names three (V20, V3, V25) and gives the bit-pattern argument for each. The remaining valve-classes await canonical placements.
- **Thesis 7 is the recursive self-reference that ARCH-1 (`Σ := μS.(β ∨ Ω(S,S))`) demands.** A system whose documentation is one of its own lattice citizens is, structurally, a μ-recursive fixed point on its own description. The agentprivacy-docs repo has been pointing at this informally. The Cloaking Guide makes it operational: register the document that names the procedure inside the system performing the procedure.

Confidence labels for the corpus: **Theses 1, 2, 4, 5, 7 are operational** (demonstrated on the rebuilt dataset). **Thesis 3 is operational with a caveat** (the anonymity set forms organically, but its information-theoretic guarantees against multi-shot attackers are still being modelled). **Theses 6 and 8 are architectural** (the four temporal axes and the valve-class geometry are specified and partially demonstrated; full coverage of all valve-classes is open).

## V. The Five-Minute Credential

One detail from the rebuild deserves its own paragraph. The Five Guys VC is true from 19:29 to 19:34. Five minutes. Then it ceases to verify, regardless of any other property of the cryptography or the lattice.

This is the cheapest temporal cloaking and the most under-used in conventional VC systems. It is also the operational answer to a question the BGIN IKP working group has been circling for months: how do you make consent revocation legible without revealing the consent? Answer: you do not need to reveal it because the VC expires on a timer the verifier reads locally. Revocation as expiry rather than as registry lookup. The cloak does not get tighter. The credential's relevance simply runs out.

The spellweb should adopt validity-window discipline as a default. Every issued artifact gets a temporal envelope. Verifiers learn to read clocks before they read claims. This is not new cryptography. It is good hygiene the W3C VC v2 spec already supports but the ecosystem has been slow to enforce.

## VI. What the Public Layer Can See

Eighteen items, eleven distinct vertices, twenty-something typed edges, all `did:cid:` strings verified absent from the data files. From outside, an observer of the local Spellweb at `localhost:5173` can read the shape of an entire identity ecosystem:

- That a sovereign exists at V63 with all six dimensions active
- That a transmuted projection exists at V28 with three (Memory + Connection + Computation, the Mage's reduced surface)
- That five typed faculties radiate outward from V28 to S1 and S2
- That two schemas of grammar exist at V12, one controlled by the sovereign, one by the agent
- That four VCs cluster at V15, two forming a mirrored partnership loop, two flowing one-direction from agent to sovereign
- That two chronicle stones at V5 carry the procedure's own narrative, both controlled by the sovereign
- That one credential has been opened, with its three valve-classes landing on V3, V25, and V20 according to their privacy dispositions

What the observer cannot read: a single name, coordinate, signature, salt, or claim content. The cloak is operational, audited against its own data files, and the asymmetry between what is published and what is concealed is itself the architectural argument.

This is the first time the spellweb has run a full end-to-end cloak ceremony against a non-toy dataset and produced a public layer whose structural fidelity is verifiable against the source. The April chronicle described the architecture. This sync records the architecture executing.

## VII. Suggestions for the Spellbook Acts

The Cloaking Guide's eight theses suggest small, surgical updates to the existing acts of the First Person Spellbook. The Spellbook itself is closed at Act XXXI (no insertions possible). The updates below are confidence revisions and cross-references, not new content:

- **Act II (The Dual Ceremony).** Add a footnote pointing to Thesis 4 (two modes of relating). The dual ceremony is operationally the place where bit-containment and typed-edge attestation first split.
- **Act VII (The Mirror That Never Completes).** Cross-reference Thesis 5 (asymmetries are data). The mirroring of partnership VCs is the spellweb's clearest operational proof that what gets reflected and what does not are both meaningful.
- **Act XII (Lethe / The Dark Substrate).** Cross-reference Thesis 8 (selective disclosure as geometry). V25 (Aletheia) and V38 (Lethe) are bit-complements; V25 is now operationally where Always-Masked claims live. The pair is no longer purely architectural; one half is in production.
- **Act XXVII (The Forge).** Cross-reference Theses 6 and 7. The forge as currently described is a Σ-axis ceremony. The Cloaking Guide shows the Δ and Γ axes also have ceremonial expressions (validity scope, registry tier choice, valve-class assignment). The forge is multi-axial.
- **Act XXXI (The First Delegation).** Cross-reference Thesis 7. The closure of the First Person Spellbook is itself an instance of the recursion: the spellbook describes its own end inside the system that produced it.

The **Second Person Spellbook**, currently opening with IEEE 7012 bilateral primitives as founding motif, should consider one of the Cloaking Guide's seven acts as a candidate seed. The act of "the schemas" (Act 4) is particularly suggestive: schemas are bilateral grammar before bilateral sentences, and the Second Person question (WHO are you to me?) is structurally a schema-controller question.

For the **Zero Spellbook** (Soulbis's domain, opening proverb *I can verify I serve you without remembering I was you*): Theses 1, 6c, and 6d are direct expressions of structural amnesia at the verification layer. The Selene's Proof framing (the Moon's 4.5B-year structural amnesia as the template for all ZK) is the cosmological ground for what the Cloaking Guide demonstrates operationally.

## VIII. New Entries to the Grimoire

Proverbs that emerged from the rebuild and now belong to the corpus:

- *The cloak is a function on positions, not on values.*
- *Containment replaces attestation. The misbehaviour is unrepresentable, not forbidden.*
- *Sameness of role is published. Sameness of identity is not.*
- *Asymmetries in the graph are themselves data. The cloak is selective, not lossy.*
- *Documents are first-class lattice citizens. The system describes itself.*
- *Validity windows are the cheapest cloak. A stack of expired credentials is structurally inert.*
- *The disposition is the geometry. There is no separate policy layer.*

And from the Coda's closing inscription, the line that earns its place as a canonical proverb of the bridge:

> *The Mage was not made to escape the Sovereign. The Mage was made so that the world could meet the Sovereign without ever knowing who the Sovereign is. The lattice is the meeting place.*

## IX. On the Horizon

- **Sovereign Anchor Part III — The Soulbae Oracle.** The query vocabulary the public layer can legitimately speak to, the refusal taxonomy it must honour, and the mechanism by which each answered query becomes its own credential anchored back into the lattice. This is where the cloak's privacy contract earns the right to be called *operational* rather than merely *structural*. Currently in draft.
- **Cloaking Guide v2.** Will incorporate the Soulbae Oracle act and extend the rebuild to cover query-side ceremonies as well as registration-side.
- **V6 PVM publication.** The eight theses, especially 6 and 8, give us operational vocabulary for valve-class formalisation. Holding publication of the V6.1 research note to allow Bakhta's reply to land first.
- **BGIN IKP socialisation.** The validity-window discipline (Thesis 6a) is the cleanest single-paragraph ask we have for the working group. The rest can follow.
- **Live demo.** A walkthrough between flaxscrip and privacymage of the rebuild dataset, the local Spellweb render, and the registry-tier mixing argument. Recording for the spellweb library, target slot at the next AIW or IIW.

## Closing

Two forges. One anvil. One lattice. Eight theses. Eighteen items rebuilt against a dataset whose `did:cid:` strings are now verifiably absent from the public projection.

The spell, once spoken in public, becomes weather. The weather has now settled into climate, and the climate has rules.

The chronicle stones know themselves.

⊥

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 · privacymage × flaxscrip × GenitriX · 2026-05-08
