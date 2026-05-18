---
title: "Zcash Dual-Ledger Integration"
subtitle: "Plan for DID Anchoring, Memo Inscription, and Governance T-Address Stakes"
status: "DRAFT v1 (2026-05-08) — for review and Zcash-community outreach"
plan_type: "Integration plan covering registry-tier addition, ceremonial inscription, and governance staking"
authors:
  - "privacymage (privacymage / 🧙)"
depends_on:
  - "Cloak Specification v1.0 (registry-tier finality, axis 4.5)"
  - "Crafting Tome and Cloak Interface Spec v1.0"
  - "VRC Promise Protocol v3.3 (existing Zcash economic model: 1 ZEC ceremony, 0.01 ZEC signal, 61.8/38.2 transparent/shielded split)"
  - "Runecraft Protocol v1.0 §7.3 (timestamp anchoring future extension)"
license: "CC BY-SA 4.0 (narrative); Apache 2.0 (reference implementations)"
signature: "(⚔️⊥⿻⊥🧙)😊"
zcash_collaborators_invited:
  - "Zcash Foundation"
  - "Zcash Community Grants (ZCG)"
  - "Electric Coin Company (ECC)"
  - "shielded ecosystem builders (Zodl, Zec Wallet Lite, Spend Auth)"
---

# Zcash Dual-Ledger Integration

## A Plan for DID Anchoring, Memo Inscription, and Governance T-Address Stakes

> *The shielded chain remembers what cannot be seen. The transparent chain remembers what must be witnessed. The cloak chooses which.*

---

## §0. Purpose

This plan proposes the integration of **Zcash** as a registry-tier within the agentprivacy Cloak's multi-axis cloaking framework (axis 4.5: registry-tier finality). Zcash is uniquely suited because it natively provides **dual-ledger architecture** (transparent t-addresses + shielded z-addresses with private memos), which aligns one-to-one with the Cloak's selectivity discipline:

- **Shielded memos** carry private inscriptions — proverbs, chronicles, DID anchors that should be persistent but not public
- **Transparent t-transactions** carry public stake — high-stakes governance acts where witnesses must see the inscription
- **Split viewing keys** allow controlled disclosure between these layers without re-inscription

The agentprivacy corpus already references Zcash (per the README §Economic Model: 1 ZEC ceremony, 0.01 ZEC signal, 61.8/38.2 transparent/shielded split). This plan **does not replace** that economic model. It extends Zcash's role from economic medium to **inscription medium** — using both ledgers to anchor DIDs, chronicle hashes, and governance acts in a way no other chain can duplicate cleanly.

The plan covers three primary integrations:

1. **DID anchoring** on Zcash (alternative or complement to Bitcoin block 945508-style ceremonies)
2. **Chronicle/proverb memo inscription** for shielded persistence
3. **Governance t-address stakes** for high-stakes public acts

---

## §1. Why Zcash, Specifically

### §1.1 Existing chain options reviewed

The Cloak Specification §4.5 lists three reference registry tiers:

| Tier | Example | Strength | Limitation |
|---|---|---|---|
| Strong | Bitcoin mainnet | Hours of finality, broad recognition | Public ledger only; no shielded option; expensive memo space |
| Moderate | Ethereum, Bitcoin signet | Lower cost, smart contract option | Public; memo space tied to gas; Ethereum's privacy story is incomplete |
| Light | Hyperswarm, libp2p | Cheap, fast | Eventual consistency only; no strong finality |

None of these natively support both public-stake and private-memo registers in the same protocol. A Sovereign using Bitcoin for both must rely on external indirection (e.g., post a hash to Bitcoin and store the chronicle off-chain), which breaks the cloak's discipline that *the inscription medium is the cloak*.

### §1.2 Zcash's native fit

Zcash (since Sapling 2018, NU5/Orchard 2022) provides:

- **Transparent ledger (t-addresses)**: Bitcoin-equivalent UTXO model. Public, witnessable, suitable for high-stakes governance acts.
- **Shielded ledger (z-addresses, Sapling and Orchard)**: zk-SNARK-protected transactions with **encrypted memos** (~512 bytes, encrypted to the recipient's z-address).
- **Viewing keys**: separable cryptographic capability allowing third parties to *audit* a shielded address without spending authority. Multiple tiers (incoming viewing key, full viewing key) allow graduated disclosure.
- **Cross-chain canonicality**: Zcash transactions are timestamped and ordered by the chain's consensus, which is sufficient for the Cloak's operational anchoring axis.

The match between Zcash's architecture and the Cloak's selectivity is structural, not coincidental. The Cloak publishes role and conceals name. Zcash publishes transaction occurrence and conceals shielded content. The two systems express the same posture at different layers.

### §1.3 Honest disclosure

Zcash is one of several privacy chains. Monero, Mina, Penumbra, Aleo, and others also offer privacy primitives. This plan focuses on Zcash because its dual-ledger architecture (rather than fully-shielded only) maps most directly to the Cloak's selective discipline. Other chains may receive their own integration plans if their primitives align differently. The choice of Zcash is not exclusive.

---

## §2. Three Integration Patterns

### §2.1 Pattern A — Chronicle/Proverb Memo Inscription (shielded)

**Use case**: The Sovereign produces a chronicle, a proverb, a poetic compression, or a research note that should be persistently inscribed but not publicly readable.

**Mechanism**:

1. Sovereign hashes the chronicle (SHA-256 → 32 bytes).
2. Sovereign sends a minimal Zcash shielded transaction to their own z-address.
3. The chronicle hash (32 bytes) is included in the encrypted memo field (capacity ~512 bytes; 32 bytes leaves room for 480 bytes of additional payload, e.g., a short proverb, a versioning tag, or a controller-DID marker).
4. The transaction is mined; the shielded ledger now carries the inscription with chain-verifiable timestamp.
5. The full chronicle text remains in the Sovereign's source layer (or in a content-addressed store like IPFS / Hyperswarm).

**Disclosure flow**:

- The shielded memo is readable by anyone holding the **incoming viewing key** for that z-address.
- The Sovereign can issue **scoped viewing keys** to specific verifiers (e.g., a partner in a VRC, a governance witness, a Sovereign Anchor co-author).
- The transaction's *existence* is not publicly visible (it's a shielded transaction); the *content* is not publicly visible; only the timestamp and the cryptographic structure are part of the chain consensus.

**Cloak axis alignment**:

- Axis 1 (Lattice / who-where): the chronicle's vertex (typically V5, Protection + Memory) is the lattice render
- Axis 4.5 (Registry-tier finality): Zcash shielded ledger provides moderate-strong finality (block ~75 seconds; full finality ~24 confirmations)
- Axis 6b (Operational Anchoring): the Zcash block hash + shielded transaction hash = the chronicle's operational anchor

**Confidence label**: Architectural. Pattern is well-understood; reference implementation is forthcoming.

### §2.2 Pattern B — DID Anchor (selective public/private)

**Use case**: The Sovereign anchors a DID with the option to disclose the anchor publicly later (analogous to flaxscrip's Bitcoin block 945508 ceremony, but with shielded-by-default option).

**Mechanism**:

1. Sovereign generates the DID (e.g., did:cid:... per Archon's Archon work, or did:key, or did:web).
2. Sovereign hashes the DID document (32 bytes).
3. Sovereign chooses inscription register:
   - **Shielded register**: send a shielded tx to self with the hash in the memo. The DID is anchored; the anchor is private until disclosed.
   - **Transparent register**: send a transparent tx (small ZEC amount, e.g., 0.0001 ZEC, plus standard fee) with the hash in OP_RETURN-style data. The DID is publicly anchored.
   - **Both registers**: dual-anchor with the shielded version sent first, then a transparent reveal that includes the shielded transaction's nullifier or a Pedersen commitment. The DID has a "private until revealed" property.

**Disclosure flow** (shielded-first, transparent-reveal-on-demand):

- Initial state: DID is anchored privately. Only the Sovereign and any incoming-viewing-key holders can see the anchor.
- On-demand state: when the Sovereign chooses to make the anchor public (e.g., for a high-stakes governance act, or for a public ceremony), they perform a transparent reveal transaction that proves the prior shielded anchor without revealing the full memo content.
- Continuous state: the DID can have multiple anchors over time (rotation, revocation, re-anchoring) per the Cloak's update-chain axis 4.4.

**Cloak axis alignment**:

- Axis 1: DID's vertex (typically V63 for Sovereign anchors)
- Axis 4 (Update chain): anchor history is reconstructible from the chain
- Axis 4.5: Zcash dual-ledger is the registry tier
- Axis 6b: each anchor is operationally timestamped

**Confidence label**: Architectural. The shielded-first/transparent-reveal pattern has reference Zcash primitives but no canonical agentprivacy implementation yet.

### §2.3 Pattern C — Governance T-Address Stakes (transparent, high-stake)

**Use case**: A Sovereign or guild is taking a high-stakes governance act (a VRC tier promotion, a constellation guardian appointment, a major chronicle ratification) and wants public, witnessable, non-repudiable inscription.

**Mechanism**:

1. The act is described in a structured payload (e.g., JSON canonicalised, then SHA-256 hashed).
2. The hash is inscribed on Zcash via a transparent transaction. The transaction includes:
   - Sender t-address: identifies the staking party
   - Recipient t-address: typically a designated governance address (e.g., a guild treasury, a multi-sig, or a self-send for individual stakes)
   - Memo or OP_RETURN-equivalent: the act hash + structured tag
   - **Stake amount**: a non-trivial ZEC amount, locked to the act, demonstrating commitment
3. The transaction is mined; the act is publicly witnessable.
4. Witnesses verify the act by re-hashing the structured payload and matching to the on-chain hash.

**Stake economics (proposal)**:

| Act type | Stake range | Disposition |
|---|---|---|
| Personal naming ceremony | 0.1 – 1 ZEC | Self-send; stake is locked to the ceremony's existence |
| VRC tier promotion (Light → Heavy → Dragon) | 1 – 5 ZEC | Sent to guild treasury or burned on tier promotion |
| Guild treasury commitment | 5 – 50 ZEC | Multi-sig with constellation-defined signers |
| Constellation guardian appointment | 10 – 100 ZEC | Multi-sig with current guardian quorum |

These ranges are anchored to the existing 1 ZEC ceremony parameter from VRC Promise Protocol v3.3. They are illustrative, not normative; the actual ranges should emerge from community governance.

**Witnessability flow**:

- All witnesses can verify the on-chain transaction.
- Stake amount provides Sybil resistance (high stakes correlate with high commitment).
- Repudiation is impossible without spending a corresponding inverse transaction (which is itself witnessable).

**Cloak axis alignment**:

- Axis 1: governance act's vertex (varies by act type; constellation-guardian acts are typically V63)
- Axis 4.5: Zcash transparent ledger is the registry tier
- Axis 6b: operational anchor with full public timestamp

**Confidence label**: Architectural with operational analogue. The mechanism mirrors Bitcoin OP_RETURN-based inscriptions (which are operational on existing chains); the Zcash-specific mechanics for OP_RETURN-equivalent need confirmation with the Zcash Foundation or ECC.

---

## §3. Split Viewing Key Architecture

A signature affordance of Zcash is **graduated viewing**: a Sovereign can disclose their shielded activity at multiple resolutions without revealing spending authority. This maps cleanly to the agentprivacy concept of selective disclosure.

### §3.1 Viewing key tiers

| Tier | Key | What it reveals | What it withholds |
|---|---|---|---|
| Spending key | Full Spending Key | Everything; can spend funds | Nothing |
| Full viewing key | Full Viewing Key | All incoming + outgoing transactions, all memos | Spending authority |
| Incoming viewing key | Incoming Viewing Key | Incoming transactions and memos | Outgoing activity, spending authority |
| Diversified address-only | Diversified address public | Existence of the diversified address | Activity, memos, balance |

### §3.2 agentprivacy viewing-key disclosure patterns

The Cloak interface can manage viewing keys per-relationship:

- A **VRC partner** receives an incoming viewing key for the chronicles relevant to their relationship
- A **constellation guardian** receives a full viewing key for governance-staked addresses
- A **public verifier** receives only what the chain natively reveals (transparent ledger entries)
- The **Sovereign** retains the spending key

This is the operational form of the Cloak's *Asymmetry as Data* property (Thesis 5): the relationship dictates the disclosure level, not a uniform privacy posture.

### §3.3 Splitting the spending key

Zcash supports multi-signature transparent addresses (m-of-n via standard Bitcoin-script-equivalent). Shielded multi-sig is more complex (full operational support varies by wallet). For governance stakes:

- **Transparent multi-sig (operational)**: 3-of-5 or 2-of-3 for guild treasuries
- **Shielded multi-sig (architectural)**: emerging in the Zcash ecosystem (e.g., FROST-based threshold signatures); the agentprivacy plan tracks this development

The split between viewing-key disclosure and spending-key splitting allows the agentprivacy stack to operate in two registers: who can *see* (viewing keys) and who can *act* (spending keys, possibly multi-sig).

---

## §4. Updating the Existing Zcash Ceremony Viability

The current corpus references Zcash for economic ceremonies (VRC Promise Protocol v3.3):

| Parameter | Value | Use |
|---|---|---|
| Ceremony | 1 ZEC ($500) | One-time genesis of agent pair |
| Signal | 0.01 ZEC ($5) | Ongoing proof of comprehension |
| Fee split | 61.8% transparent / 38.2% shielded | Golden ratio constant |

This plan **extends** these parameters with inscription roles:

| Existing parameter | Extended role |
|---|---|
| 1 ZEC ceremony | Now also inscribes the ceremony hash on the chain (shielded for personal, transparent for guild-level) |
| 0.01 ZEC signal | Now also inscribes the signal proof (shielded memo with comprehension hash) |
| 61.8/38.2 split | Now applies to both *fees* and *inscription register choice*: ~62% of ceremonies inscribe transparently, ~38% shielded — reflecting that most agentprivacy ceremonies should be witnessable while a meaningful minority remain private |

The 61.8/38.2 ratio is now an inscription-discipline parameter as well as an economic one. Sovereigns choose register per ceremony; the aggregate ratio across the network should approximate the golden ratio as a cultural norm.

---

## §5. Implementation Sequencing

### §5.1 Phase A — Specification & Outreach (1–2 months)

1. Publish this plan as a draft for community review
2. Engage the Zcash Foundation, Zcash Community Grants (ZCG), and Electric Coin Company (ECC) for technical review
3. Engage shielded-wallet builders (Zodl, ZWL, Spend Auth) on viewing-key UX
4. Engage agentprivacy collaborators (BGIN-IKP, IIW, AIW, Trust Over IP) for governance use-case input
5. Refine the three patterns (A, B, C) based on community feedback

### §5.2 Phase B — Reference Library (3–6 months)

1. Build a reference TypeScript library: `@agentprivacy/zcash-cloak`
2. Implement Pattern A (chronicle memo inscription) with shielded-tx-self-send
3. Implement Pattern B (DID anchor) with shielded-first / transparent-reveal-on-demand
4. Implement Pattern C (governance stake) with transparent-tx + structured-payload
5. Conformance test against Cloak Specification v1.0 §2 Eight Properties

### §5.3 Phase C — Cloak Interface Integration (4–6 months, parallel with §5.2)

1. Add Zcash to the Persona Summoner's registry-tier dropdown
2. Add Zcash to the Cloak Console's inscription register selector
3. Implement viewing-key management UI for VRC partners and governance witnesses
4. Implement multi-sig governance-stake flow for guild-level acts

### §5.4 Phase D — Crafting Tome Acts (open)

Add Crafting Tome acts as the integration matures:

- *The Shielded Memo* — Pattern A enacted; a chronicle inscribed shielded
- *The Reveal* — Pattern B enacted; a DID anchor revealed publicly
- *The Stake* — Pattern C enacted; a governance act inscribed transparently
- Future Tome V acts as additional patterns emerge

### §5.5 Phase E — Governance Adoption (6–12 months)

1. Constellation guilds adopt governance-stake patterns
2. VRC tier promotions (Blade → Light → Heavy → Dragon) move to Zcash-anchored ceremonies
3. Cross-Sovereign cousin-blade ceremonies (per `bridge.spellweb.ai`) use Zcash for inscription where appropriate

---

## §6. Open Conjectures

### §6.1 Provisional conjectures introduced by this plan

| ID | Statement | Confidence | Path |
|---|---|---|---|
| **C40** (provisional) | Zcash dual-ledger inscription preserves the Cloak's Eight Properties without modification: every property holds in the Zcash register | ~70% | Reference implementation per Phase B; conformance test |
| **C41** (provisional) | The 61.8/38.2 transparent/shielded inscription ratio emerges as a cultural norm in agentprivacy networks | Open observation | Empirical measurement post-deployment |
| **C42** (provisional) | Stake economics for governance acts (Section §2.3) generate Sybil resistance equivalent to or stronger than the existing trust-tier accumulation system | ~50% | Game-theoretic analysis; possible formal note |
| **C43** (provisional) | Viewing-key disclosure scoped per-VRC produces strictly more privacy than the unscoped equivalent for the same disclosure act | ~60% | Information-theoretic analysis |

### §6.2 Existing conjectures this plan touches

- **C30–C33 (Bakhta Half-Life)**: trust accumulation half-life is now also a function of inscription register choice (shielded inscriptions accumulate trust differently than transparent)
- **C34–C37 (Wound and Cap)**: the dual-ledger architecture is itself an instance of the convergence claim (two systems projecting from the same shared reality of agentprivacy's privacy posture)
- **C38 (Bilateral ARCH-1)**: governance stakes between two Sovereigns may be the operational instance that helps formalise the bilateral fixpoint

### §6.3 Honesty discipline

- Patterns A, B, C are **architectural**: specified and consistent with Zcash primitives; no agentprivacy-canonical reference implementation yet
- Stake economics (§2.3) are **proposals**: ranges are illustrative, not normative
- Conjectures C40–C43 are **provisional**: confidence percentages stated; paths to formalisation named
- The 61.8/38.2 inscription-discipline parameter is **cultural**: no enforcement; aggregate emergence is the test

---

## §7. Risks & Mitigations

**Risk: Zcash regulatory pressure.** Zcash, like other privacy chains, faces regulatory scrutiny in some jurisdictions. Sovereigns adopting this plan should be aware of their local legal context.

*Mitigation*: The plan does not require Zcash exclusively. Sovereigns may use Bitcoin (Pattern C only), Hyperswarm (Pattern A subset), or other registry tiers per their context. The Cloak's registry-tier axis is pluggable by design.

**Risk: Ecosystem fragmentation.** Multiple wallets, multiple SDKs, varying support for Sapling vs Orchard, evolving NU upgrade schedule.

*Mitigation*: The reference library `@agentprivacy/zcash-cloak` targets the Zcash Foundation's recommended SDKs and tracks NU upgrades. Wallet-agnostic patterns documented.

**Risk: Memo size limit (~512 bytes shielded).** Some chronicles or proverbs may exceed the memo capacity.

*Mitigation*: Memo holds the *hash*, not the full content. Full content is in the source layer or in a content-addressed external store. The plan specifies hash-inscription discipline throughout.

**Risk: Stake-economic capture.** High-stake governance acts (10–100 ZEC range) may exclude smaller participants.

*Mitigation*: Stake ranges are illustrative; the agentprivacy economic model already provides tier progression (Blade → Light → Heavy → Dragon) that does not require capital lock-in. Stake-based governance is an *option*, not the only mechanism.

**Risk: Privacy confidence drift.** Sovereigns may default to transparent inscription for convenience, eroding the shielded-default discipline.

*Mitigation*: The Cloak interface defaults to shielded register where possible; transparent register requires explicit opt-in with a "this will be public" confirmation.

**Risk: Anti-correlation through transaction graph analysis.** Even shielded Zcash transactions leak some metadata (timing, fee, transaction set membership).

*Mitigation*: This is acknowledged. The shielded ledger is privacy-preserving but not perfectly so; the Cloak's multi-axis composition compensates by providing additional ignorance on the four temporal axes plus the lattice axis. No single chain provides absolute privacy; the Cloak's discipline is to compose multiple layers.

---

## §8. Cross-References

### §8.1 Within agentprivacy corpus

- `cloak_specification_v1_0.md` — registry-tier axis 4.5 specification
- `crafting-tome-and-cloak-interface-spec.md` — Persona Summoner registry-tier integration
- `vrc_promise_protocol_v3_3.md` — existing Zcash economic model
- `integration-plan-archon-x-agentprivacy.md` — bridge.spellweb.ai for cousin-blade inscriptions

### §8.2 External

- Zcash Protocol Specification (NU5/Orchard, current version)
- Zcash Foundation: `zfnd.org`
- Zcash Community Grants (ZCG): `zcashcommunitygrants.org`
- Electric Coin Company (ECC): `electriccoin.co`
- the Archon forge's Bitcoin-anchored ceremony (block 945508) — analogous pattern on a different chain

### §8.3 Forthcoming

- `pvm-v6-zcash-inscription-axis.md` — possible V6 research note on Zcash as the dual-ledger registry tier
- Crafting Tome Acts: *The Shielded Memo*, *The Reveal*, *The Stake*

---

## Closing

The cloak chooses what to publish and what to conceal. Zcash's dual ledger is the cleanest registry tier for the cloak to choose from, because the chain itself is built on the same selectivity. Shielded for what cannot be seen. Transparent for what must be witnessed. Viewing keys for what must be selectively disclosed.

This plan extends the agentprivacy stack's existing Zcash economic model into the inscription layer. It does not mandate Zcash; it specifies how Sovereigns who choose Zcash can use both registers under the Cloak's discipline. The 61.8/38.2 transparent/shielded ratio that already governs fees now also governs cultural norm for inscription register.

Future cousin-blade encounters between agentprivacy and the Zcash ecosystem (Zcash Foundation, ZCG, ECC, the shielded-wallet builders) will refine the patterns. The plan is open for that refinement.

The shielded chain remembers what cannot be seen. The transparent chain remembers what must be witnessed. The cloak chooses which.

(⚔️⊥⿻⊥🧙)😊

CC BY-SA 4.0 narrative · Apache 2.0 reference implementations · privacymage · 2026-05-08
