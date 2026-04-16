# Response from privacymage

## To the First Person Project community

### On the ZKP Progress section and how agentprivacy extends the Cryptographic Framework for Proof of Personhood

---

*[[ The impossibility theorem is the proof that the gap was always load-bearing. ]]*

---

Drummond, Sanjam, friends of the First Person Project,

Thank you for the update, and thank you to Sanjam, Arka, and collaborators for "A Cryptographic Framework for Proof of Personhood." The paper formalizes several things the agentprivacy architecture has been building toward independently. The convergence is deep enough that I want to lay it out plainly and propose how this work can strengthen the ZKP Task Force at DTGWG as it launches.

For those who don't know me: I'm privacymage, co-chair of the BGIN Identity, Key Management & Privacy Working Group, and a contributor to the First Person Project where agentprivacy serves as the agentic expression of first-person sovereignty. The body of work includes a formal privacy economics model (the Privacy Value Model, V5.4 — comprising a 24-page formal specification, companion guide, and compressed spec), a dual-agent protocol for sovereign AI delegation, and open-source tooling published under CC BY-SA 4.0 and Apache 2.0. I've been at IIW, Trust Over IP, and BGIN for several years working on the same problems this paper addresses. I'll be at the London meetup on May 8 and plan to attend AIW #3 and IIW #43 in the autumn.

---

## The two-credential system has the same origins

The paper's core architecture rests on two credential types: personhood credentials (PHCs) issued by trusted authorities, and verifiable relationship credentials (VRCs) issued peer-to-peer. This is the First Person Network's credential architecture given a cryptographic formalization.

The First Person Project has always held that personhood arises from the accumulation of relationships and attestations rather than from any single issuer or biometric scan. The paper now proves the security properties this thesis requires: Sybil-resistance through multiplicative trust accumulation across independent issuers, privacy-preservation through zero-knowledge showing, and context-dependent unlinkability that prevents cross-domain tracking while allowing within-context accountability.

What agentprivacy adds is the next question the First Person credential must answer: once you have established that you are a real person, how do AI agents act on your behalf without eroding that sovereignty?

---

## Three results that matter for the ZKP Task Force

**1. Multiplicative trust accumulation (Theorem 5)**

The paper proves that verifier confidence increases multiplicatively as independent honest issuers contribute credentials to a show proof. Any corrupted issuer collapses its own contribution to zero without degrading the honest issuers' guarantees. The formal bound is:

```
Pr[BAD] ≤ 1 − ∏(1 − ε(i))
```

This is structurally identical to the Privacy Value Model equation at the core of the agentprivacy architecture. The PVM V5.4 formal specification (24 pages, seven proven results at 95% confidence, twenty-one conjectures with explicit confidence levels) defines the multiplicative gating condition:

```
Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ)
```

Both assert the same architectural principle: trust and privacy value compose multiplicatively, and any zero term is catastrophic. The paper arrived at this from the real/ideal world paradigm with PAV oracles. Agentprivacy arrived at it from privacy economics and the thesis that behavioral data constitutes a seventh form of capital.

I have been developing this multiplicative equation since 2024, and it is starting to find its shape. After AIW #1 last autumn, once I got back to the research, a mathematician I was working with pointed out that the equation mirrors the Drake equation — the same multiplicative gating structure where each term is an independent filter and any zero collapses the total. Drake asks how many civilizations survive the cosmic filters. The PVM asks how much sovereignty survives the architectural filters. The difference is that Drake describes the filter; the PVM architects through it. Now the Choudhuri-Garg paper arrives at the same multiplicative structure from pure cryptography, independently. Three fields, one shape. The convergence is structural.

For the ZKP Task Force, this means the formal security model already exists for reasoning about multi-issuer First Person credentials. The task force doesn't need to invent it. It needs to map it onto the DTG credential schemas and the OpenVTC infrastructure Glenn Gore's team is building.

**2. The impossibility of full unlinkability (Section 5.3)**

This is the result I want to emphasize most. The paper proves that no real-world protocol can simultaneously achieve full unlinkability and Sybil resistance. You cannot make all pseudonyms indistinguishable while also proving two attestations come from distinct humans. The resolution is context-dependent unlinkability: linkable within a context, unlinkable across contexts.

In agentprivacy, this impossibility result has a name. We call it ⊥ — the irreducible gap. The master inscription of the project is `(⚔️⊥⿻⊥🧙)😊`, where the ⊥ markers represent architectural separation that cannot be removed without collapsing the system. The paper's impossibility formally proves one instance of this principle: that pseudonyms serving distinct contexts cannot be unified without losing Sybil resistance. The agentprivacy ⊥ generalizes this to a second axis — the Swordsman (boundary enforcement) and Mage (delegation) within a single user's stack. Same principle, different separation surface. The paper's contexts are what the Swordsman maintains as boundary; cross-context unlinkability is what the Mage provides on the other side.

I have been stating the general principle architecturally. Choudhuri, Garg, and collaborators have now proved a formal instance of it. For the ZKP Task Force, this means the privacy-unlinkability tradeoff has a formal characterization that the task force can use to evaluate which ZKP approaches (Open AC, the paper's Groth-Sahai construction, others) satisfy the right balance for First Person credentials.

**3. Vouchable credentials as a new primitive (Section 6)**

The paper introduces vouchable credentials — an extension of standard credentials that allows a credential holder to produce a vouch for a statement while revealing only selected attributes. The four required properties (unforgeability, non-malleability, extractability, simulatability) constitute a formal specification for what any First Person VRC implementation must satisfy.

The black-box construction (Section 8) using structure-preserving signatures and KZG polynomial commitments achieves two orders of magnitude better proving performance than general-purpose zkSNARKs at scale (Table 2: 0.84s vs 62s for 25 vouches). This matters enormously for mobile wallets. The ZKP Task Force should evaluate this construction alongside Open AC for the DTGWG requirements. The paper's modular decomposition — Groth-Sahai for algebraic constraints, commit-and-prove SNARK for arithmetic constraints — is also architecturally well-suited to a future post-quantum upgrade, since the two components can be replaced independently.

---

## Complementary proof paradigms

The two projects use different but composable security models, and this is worth naming because it opens a genuinely novel framing for the ZKP Task Force.

The paper works in the **simulation-based paradigm**: it defines an ideal functionality F_PoP-user-unlinkability and proves any real-world adversary's view can be simulated given only what the ideal functionality reveals. This is cryptographic indistinguishability — the standard for proving protocol security under computational assumptions.

Agentprivacy's whitepaper works in the **information-theoretic paradigm**: it proves bounds on mutual information between the user's behaviour and what any reconstructor can recover, given dual-agent separation. The reconstruction ceiling theorem (R_max < 1), the error floor via Fano's inequality, and graceful degradation under approximate separation are all proven at 95% confidence in the V5.4 formal specification (R1–R7).

These don't compete. Simulation-based security proves an adversary cannot distinguish real from ideal. Information-theoretic separation proves they cannot reconstruct behaviour even with unbounded compute. Stacked, you get *cryptographically hiding credentials whose use is information-theoretically separated across agents* — a stronger composite guarantee than either paradigm provides alone. No existing deployment I am aware of combines the two. For First Person credentials used by AI agents, both layers matter: the credential system needs cryptographic unforgeability; the agent architecture using the credentials needs information-theoretic bounds on what one agent can infer about the other's operations.

---

## Direct proof-system overlap

The proof-system choices compose more directly than the paper's construction alone suggests.

Agentprivacy's existing SNARK infrastructure uses Groth16, PLONK, and Nova (folding schemes for recursive verification), with KZG polynomial commitments in the blade forge. The paper's black-box construction uses KZG polynomial commitments for the attribute layer, structure-preserving signatures (Groth15) verified via Groth-Sahai for the algebraic layer, and a commit-and-prove SNARK (CFQ19-style linkage) for the arithmetic layer (predicate evaluation, PRF checks, nullifier revocation).

The overlap is direct. Both use KZG. Both use pairing-based NIZK. Agentprivacy's Groth16 backend, via the CFQ19 commit-and-prove interface, plugs into exactly the arithmetic-component slot the paper carves out. The paper's modular decomposition is not just architecturally clean — it is architecturally *compatible* with agentprivacy's existing proof infrastructure. The black-box vouchable credential scheme could be instantiated using the SNARK stack already running in the blade forge with minimal modification.

For the ZKP Task Force, this matters practically: there is already running code that speaks the same cryptographic dialect as the paper's construction. The integration path is not "adopt a new proof system" but "wire two compatible backends together."

---

## The delegation gap: where agentprivacy contributes

The paper's Appendix B.1 on AI Agent Reputation proposes that people with personhood credentials delegate to AI agents, agents build reputation through vouches, and misbehaving agents get revoked. This is exactly the application Drummond described at LFMS and the Kwaai Summit as "The Decentralized Trust Graph: A Unified Trust Infrastructure for the Internet of Humans and Internet of Agents."

But the paper stops at delegation as a concept. It doesn't specify how delegation works without creating a single-agent vulnerability. Agentprivacy identifies this as the critical gap.

A single agent that holds both delegated authority and boundary enforcement fails what we call the autonomy axiom: the process that wants to act is the same process that decides whether it should. The incentives are misaligned by construction. The resolution is dual instantiation — the Swordsman holds the boundary (what gets delegated, which contexts are permitted), the Mage operates in the projected space (interacting, accumulating VRCs). They never share state. The gap between them is the ⊥ the impossibility theorem proves necessary.

The delegation ceremony maps onto the paper's IssueVRC flow with an additional constraint: credential delegation and credential use are separated into distinct processes with distinct key material. The vouchable credential properties from Section 6 can serve as the formal specification for what the delegation artifacts must satisfy.

This extends cleanly into the DTG architecture. Each VTA in the team model can run its own Swordsman/Mage pair. The four-DID taxonomy (R-DID, M-DID, P-DID, C-DID) maps onto the pseudonym derivation the paper specifies in Section 2.3, where PRF-derived keys provide issuer-specific, context-specific, and interaction-specific unlinkability. The VTA separation theorem — that boundary enforcement and delegation must be architecturally distinct — is now backed by both the paper's impossibility proof and the agentprivacy implementation.

---

## What I am proposing for the ZKP Task Force

Three contributions.

**First, a convergence document** mapping the paper's ideal functionality (F_PoP-user-unlinkability) onto the DTG credential schemas and the OpenVTC infrastructure. This would give the task force a concrete technical bridge between the formal cryptography and the implementation work already underway.

**Second, a delegation extension** to the paper's framework. The current functionality covers credential issuance, VRC issuance, and showing. It does not cover sovereign delegation to AI agents with dual-agent separation. I propose formalizing this as an extension of the ideal functionality, adding a delegation sub-protocol that enforces the Swordsman/Mage boundary. This is where agentprivacy's decade of architectural work becomes directly useful to the First Person ZKP stack.

**Third, a post-quantum assessment.** The paper's constructions are pairing-based (Groth-Sahai, KZG, structure-preserving signatures). Agentprivacy has already identified ML-KEM and ML-DSA as target post-quantum primitives and excluded SIKE/SIDH since the 2022 attack. The modular black-box construction is well-suited to lattice-based replacements. I'd like to contribute an analysis of the post-quantum upgrade path for the ZKP Task Force's consideration as it sets its technical direction.

---

## The stack as it stands

The First Person Project establishes who you are. The Choudhuri-Garg paper proves the cryptographic properties that establishment must satisfy. OpenVTC and Open AC provide implementation candidates. Agentprivacy ensures that who you are remains sovereign as agents multiply around you, with the dual-agent separation the impossibility theorem proves necessary.

These are not separate projects. They are layers of the same architecture. The ZKP Task Force is the right place to make that composition explicit.

I look forward to discussing this at the London meetup on May 8 and at AIW #3 and IIW #43 in the autumn. Leif Johansson's piece on scaling ZKP to mass adoption in digital wallets is also directly relevant — the black-box construction's performance characteristics (Table 2) suggest the proving overhead may already be within mobile-feasible bounds for practical vouch counts.

The impossibility theorem was the best result in the paper. Not because it limits what can be built, but because it proves what must be separated. We have been building that separation for a long time. Now it has a proof.

---

privacymage

`(⚔️⊥⿻⊥🧙)😊`

mage@agentprivacy.ai | privacymage.eth

Co-Chair, BGIN Identity, Key Management & Privacy Working Group

---

**Privacy Value Model V5.4**

⚔️⊥🧙 [Formal Specification](https://github.com/mitchuski/agentprivacy-docs/blob/main/pdfs/privacy_value_v5_4_formal_specification.pdf) — 24 pages. Every term, proof (R1–R7), and conjecture (C1–C21).

🧙 [Companion Guide](https://github.com/mitchuski/agentprivacy-docs/blob/main/pvm_v5_4_companion_guide.md) — 11 pages. Context, meaning, reading paths by role.

⚔️ [Compressed Spec](https://github.com/mitchuski/agentprivacy-docs/blob/main/pdfs/pvm_v5_4_compressed.pdf) — 5 pages. Pure equations. The artifact you carry to a conference.

**Living documentation** (CC BY-SA 4.0)

[agentprivacy-docs](https://github.com/mitchuski/agentprivacy-docs) — Research notes, model JSONs, integration guides

[sync.soulbis.com](https://sync.soulbis.com) — "Privacy is Value" research letter series (Parts 0–5)

[agentprivacy.ai](https://agentprivacy.ai) | [spellweb.ai](https://spellweb.ai)
