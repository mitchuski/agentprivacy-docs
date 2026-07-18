---
extraction: E7-identity-vrc
tier: internal
sources: [whitepaper-stack, spec§19, dtg-36-posts, did-cid-convergence, myterms-package, ieee7012-plan, vrc-protocol-spec, hearthold-build, star-holospace, tome-x]
swept_complete: true (at the stated per-source depths in the Sweep record; the depth statements are the fence, L103 precedent; dtg-36-posts is external, not on disk, and is deferred per its SOURCES.md flag, not swept)
owner: A1
register_head_at_build: C96
build_note: built 2026-07-10 (cycle 9); L049 version ruling carried (VRC protocol document body self-identifies as version 3.4, filename retained at v3_3 for link stability); did-cid-convergence resolves to no SOURCES.md row (registry gap, proposed to A0 in this build's ledger proposal); L008 discipline applied per claim (design versus deployment stated)
---

# E7 · Identity Architecture and Verifiable Relationship Credentials

Claim-cluster for the identity stack and the VRC primitive: the three orthogonal identity layers (data / relationship / principal), the verified-personhood root condition Origin(S) ∩ Origin(M) = {P}, the reference protocol stack, VRC formation, recovery, lifecycle, and economics, the IEEE 7012-2025 agreement layer and its axis mapping, the second-substrate build of the separation architecture on Archon did:cid (register Band X, C94 to C96, plus the C39 promotion), the content-addressed key identity of the reference implementation (kappa-labels, carriers, private set intersection), and the did:cid convergence primitives. Feeds WP-06 (IEEE 7012 implementation note, the nearest undrafted deadline), WP-19 (RWOT collaborative paper), WP-20 (ToIP DTG profile), WP-23 (DIF trusted-agents item).

**Filter note for TIER-S consumers (WP-06, WP-20, WP-23):** TIER-S admits no conjectures, no confidence percentages, no canon-internal citations (GR-2). The TIER-S-usable claims below are the Empirical-external standard facts (E7-C18) and the Design-assumption claims whose warrant is a written specification or a tested implementation with status stated: E7-C01 to E7-C05, E7-C07, E7-C19 to E7-C21, E7-C26 to E7-C29 (implementation status always stated per L008; the strict reconstruction bound is never cited from this extraction at any tier, E1-C02 owns it with its preconditions and capacity-deficit condition). Every claim carrying a Conjecture-Cnn status (E7-C12 to E7-C17, E7-C22 to E7-C25, E7-C30) is conjecture apparatus: TIER-A use only (WP-19), as formally stated conjectures without percentage bands, per GR-2. Where a TIER-S artifact needs the existence fact that an independent second-substrate implementation runs (WP-20, WP-23), it draws the implementation-record content of E7-C26 with the register apparatus stripped, not the conjecture claims E7-C22 to E7-C24.

**Ownership cross-references (the E2-C11/C12-duplicate-E1 pattern; say which extraction owns the claim):** key custody and per-session key destruction are owned by E1 (E1-C36 dual-runtime custody split, E1-C37 two-extension processes, E1-C38 held-out harness); trust-edge half-life and decay are owned by E1 (E1-C23 to E1-C26, register C30 to C33); the separation bound, the capacity-deficit condition, and the additive-leakage claim are owned by E1 (E1-C01, E1-C02, E1-C04); policy-versus-structural separation is owned by E1 (E1-C07, E1-C27). E7 claims below cite these rather than restate them.

## Claims

### E7-C01
- **STATUS:** Design-assumption (definitional)
- **SOURCE:** spec §19
- **CLAIM:** The model defines three orthogonal identity layers: the data layer, identified by GUID (content-addressed holon, infrastructure-independent persistence); the relationship layer, identified by VRC (bilateral commitment, a promise bundle, relationship-scoped persistence); the principal layer, identified by DID (sovereign identity, self-sovereign persistence). Orthogonality claim as stated: a single principal (DID) can control multiple relationships (VRCs) across multiple data objects (GUIDs).
- **CITATIONS:** W3C DID and content-addressing standards families resolve the identifier types externally; the layering itself is the model's design.
- **FEEDS:** WP-06, WP-19, WP-20, WP-23

### E7-C02
- **STATUS:** Design-assumption (root condition with named open problem)
- **SOURCE:** whitepaper-stack (Layer 0: Verified Personhood)
- **CLAIM:** The identity architecture requires a verified-personhood layer beneath the dual agents: for the delegation pair (boundary agent S, delegation agent M) to maintain the stated bounds, Origin(S) ∩ Origin(M) = {P}, the two agents share exactly their root in one verified person and nothing else. The personhood verification mechanism is explicitly a critical dependency left to ecosystem implementers (biometric, social-graph, or attestation-network approaches are surveyed, none prescribed), and the source states that the architecture's guarantees hold only if this layer prevents synthetic agent multiplication (Sybil pairs, synthetic relationships, fake trust signals). Named open problem, carried verbatim in substance: strong uniqueness guarantees without biometric databases remain unsolved at scale.
- **CITATIONS:** none external for the condition; the surveyed approaches (proof-of-personhood systems, web-of-trust, attestation networks) are externally resolvable families.
- **FEEDS:** WP-19, WP-20, WP-23

### E7-C03
- **STATUS:** Design-assumption (reference stack, explicitly non-normative)
- **SOURCE:** whitepaper-stack (Initial Protocol Stack)
- **CLAIM:** The whitepaper's five-layer protocol stack is declared an initial reference stack with alternatives at every layer, ecosystem-agnostic by design: Layer 1 agent identity (reference ERC-8004; alternatives W3C DIDs, KERI; purpose stated as discovery without surveillance, agents findable by capability but not linkable to their principals); Layer 2 relationship credentials (reference ERC-7812 plus VRCs; alternative W3C Verifiable Credentials); Layer 3 private value transfer; Layer 4 private communication (reference Trust Spanning Protocol with shielded messaging; alternatives Signal, Matrix); Layer 5 collective intelligence. No layer choice is load-bearing for the identity claims; the primitives are.
- **CITATIONS:** ERC-8004, ERC-7812, W3C DID/VC, KERI, ToIP TSP (all externally resolvable specifications).
- **FEEDS:** WP-19, WP-20

### E7-C04
- **STATUS:** Design-assumption (definition plus formation mechanism)
- **SOURCE:** whitepaper-stack (Layer 2, How VRCs Form Through RPP); vrc-protocol-spec (Appendix A)
- **CLAIM:** A VRC (verifiable relationship credential) is a bilateral trust object between two parties, formed when both independently derive and compress their understanding of shared material and the compressions match despite different source contexts; the matching compression is taken as proof of bilateral comprehension, and the credential forms without a central issuer. Promise-theoretic reading: a VRC is a promise bundle, bilateral promises grouped for coordinated assessment and reuse. The formation mechanism (independent derivation, then match discovery) is the design's Sybil argument at the relationship layer: copied artifacts fail expansion and consistency tests that derived ones pass (the adversarial evaluation of this mechanism is E3/WP-11 territory; E7 carries the definition).
- **CITATIONS:** Bergstra & Burgess (2019) for promise bundles; no external citation for the formation mechanism (design).
- **FEEDS:** WP-06, WP-19, WP-20, WP-23

### E7-C05
- **STATUS:** Design-assumption (recovery design, not built as specified)
- **SOURCE:** whitepaper-stack (Bilateral Proverb Recovery)
- **CLAIM:** Credential recovery is designed to be relationship-rooted rather than secret-rooted: a party who loses key material but retains the interaction context, their own derived formulation, and the counterparty's place in their trust graph can regenerate the credential by re-deriving it through the same cognitive process, with the counterparty as verification anchor; the VRC network functions as a distributed recovery system (each relationship a potential recovery context). Implementation status per L008: design only in the whitepaper; the operational recovery skill exists as a practice-record item (RPP recovery skill in the skills corpus, E3's manifest home), and no deployed end-to-end recovery flow is claimed anywhere in the swept sources.
- **CITATIONS:** none external (design).
- **FEEDS:** WP-19, WP-23

### E7-C06
- **STATUS:** Design-assumption (interpretive architecture)
- **SOURCE:** whitepaper-stack (The Three Graphs; The Secret Language, proof-of-personhood implications)
- **CLAIM:** The architecture generates three independently derivable graphs: a knowledge graph (what an agent can promise: capability), a promise graph (what it does promise: every VRC, commitment, and delegation as an edge), and a trust graph (which promises have been assessed as kept: reputation, emergent rather than issued). The identity claim: the person is the intersection of the three graphs; the overlap coordinate can only be occupied by the party who accumulated it, cannot be constructed from outside, and is in principle provable in zero knowledge without revealing the graphs themselves. The formal separation content behind this lives in E1; this claim supplies the identity-layer reading only.
- **CITATIONS:** Bergstra & Burgess (2019) for the promise/assessment/trust layering; no external citation for the intersection claim (design).
- **FEEDS:** WP-19, WP-23

### E7-C07
- **STATUS:** Design-assumption (document-status fence for every economics claim below)
- **SOURCE:** vrc-protocol-spec (Development Status Notice; version block)
- **CLAIM:** The VRC Promise Protocol document presents one possible economic architecture and self-describes as the least developed component of the documentation suite, requiring ecosystem collaboration to finalise; it states that the mathematical foundations hold independent of economic implementation choices. Version authority per the L049 registry ruling: the document body self-identifies as version 3.4 (V5.1 Forge Integration + Dual Territory Edition, dated 2026-03-31) while the filename remains vrc_promise_protocol_v3_3.md for link stability and the internal footer and history table still read 3.3; the body governs. Every E7 claim sourced to this document inherits this fence: economics claims are design proposals, not commitments, and none is deployed.
- **CITATIONS:** none (document-status statement).
- **FEEDS:** WP-06, WP-19, WP-20, WP-23

### E7-C08
- **STATUS:** Design-assumption (protocol lifecycle; nothing deployed)
- **SOURCE:** vrc-protocol-spec (§9.3, §5, Part II); whitepaper-stack (Layer 2)
- **CLAIM:** The designed VRC lifecycle: formation requires a stake from each party (100 units of the delegation-domain token per formation in the reference design), returned after ten successful coordinations, with 30% slashing on expansion-test failure; a formed VRC is reusable across unlimited subsequent coordinations without re-assessment (the source of the design's coordination-efficiency claims, which carry canonical figures fenced under GR-3 and are not restated here); VRCs are designed to be portable across ecosystems (one relationship, multiple contexts, treaty economics). Graph placement: each VRC formation is an edge on the promise graph contributing to the path-integral edge-value term. Temporal behaviour (half-life, decay, renewal, augmentation) is owned by E1-C23 to E1-C26 (register C30 to C33) and not restated here.
- **CITATIONS:** none external (design document).
- **FEEDS:** WP-19, WP-20

### E7-C09
- **STATUS:** Design-assumption (incentive design)
- **SOURCE:** vrc-protocol-spec (Part III, §7, §8, §9)
- **CLAIM:** The dual-token design assigns each agent domain its own non-convertible token (protocol identifiers SWORD for the protection domain, MAGE for the delegation domain; no direct swap pool): the boundary agent's activity earns only the protection-domain token and the delegation agent's only the delegation-domain token, so information sharing between the agents increases neither party's earnings and keeping the separation promise is claimed to be the individually rational strategy (incentive compatibility for the separation promise). This is an economic reinforcement layer for the separation that E1 owns architecturally (E1-C01; policy-versus-structural distinction E1-C07/E1-C27); the source itself notes the guarantees hold independent of these token choices (E7-C07 fence).
- **CITATIONS:** Bergstra & Burgess (2019) for incentive-compatibility framing in promise terms; mechanism-design literature not engaged by the source (gap for WP-19/A12 if this claim is ever formalised).
- **FEEDS:** WP-19

### E7-C10
- **STATUS:** Design-assumption (economic instrument definitions; thresholds uncalibrated)
- **SOURCE:** vrc-protocol-spec (Promise-Economic Foundations §1, §4; §1.3)
- **CLAIM:** The design maps promise-theoretic assessment to a paid signal (0.01 ZEC per proof-of-comprehension event in the reference design; the cost is the anti-triviality and Sybil filter) and maps the promise-theoretic trust function (a 0 to 1 expectation) to four accumulating trust tiers gating economic access, with named signal thresholds between tiers. The source states the thresholds should be calibrated through empirical observation; no calibration has occurred (nothing in the corpus reports live signal volume). Non-transferable, non-purchasable practice-earned mana (a separate resource from the tokens) gates inscription actions; its Sybil argument is that it cannot be bought or transferred, only earned through practice.
- **CITATIONS:** Bergstra & Burgess (2019) for assessment and trust functions; none for the thresholds (design).
- **FEEDS:** WP-19

### E7-C11
- **STATUS:** Design-assumption (economic enforcement mapping; the bound itself is E1's)
- **SOURCE:** vrc-protocol-spec (Promise-Economic Foundations §5)
- **CLAIM:** The design maps promise-theoretic valency (exclusive promise capacity) to the information budgets of the two agents and proposes economic enforcement of the budget constraint: chronicle rewards require budget compliance, violations forfeit rewards, sustained violations slash. The underlying quantity is the capacity-deficit condition owned by E1-C02 (stated there with its preconditions, non-collusion and fixed adversary class, and its time-indexing); this claim adds only the proposed enforcement instrument, which is design, not deployment. The source's own citation of the constraint uses a retired companion-series numbering (see the hygiene note in Contested items).
- **CITATIONS:** none external (design).
- **FEEDS:** WP-19

### E7-C12
- **STATUS:** Conjecture-C42 (register confidence ~50%)
- **SOURCE:** vrc-protocol-spec (§4, Guardian model; comprehension bond); register Band III
- **CLAIM:** Stake economics generate Sybil resistance at least as strong as tier accumulation: staked comprehension bonds with golden-ratio slashing on failed reconstruction make shallow-engagement Sybil swarms capital-negative in expectation, per the source's worked example (high failure probability for participants who cannot reconstruct meaning coherently). Register status notes V6 Run 5 adversary-regime context. The claim is a design conjecture about adversary economics, unmeasured.
- **CITATIONS:** none external; the worked example is arithmetic on assumed success probabilities, not data.
- **FEEDS:** WP-19

### E7-C13
- **STATUS:** Conjecture-C43 (register confidence ~60%)
- **SOURCE:** register Band III (home formal spec §17); vrc-protocol-spec context (viewing-key scoped disclosure)
- **CLAIM:** Per-VRC viewing-key disclosure is strictly more private than unscoped disclosure: scoping a recallable witness (shielded-register viewing key) to a single relationship credential strictly reduces leakage relative to an unscoped key over the same content. Related register row: E1-C24 (register C31) owns the shielded-versus-transparent half-life claim; this row is the disclosure-scoping claim.
- **CITATIONS:** none external.
- **FEEDS:** WP-19

### E7-C14
- **STATUS:** Conjecture-C44 (register confidence ~55%)
- **SOURCE:** register Band III (home formal spec §17)
- **CLAIM:** A productive VRC (formed through joint work) and a hash-exchange VRC (formed through a bare cryptographic exchange) are approximately equal in trust strength at the moment of formation. Division of labour with the register's temporal rows: C44 is the at-inscription comparison; the differential decay afterwards is register C32 (owned at E1-C25, with C46 its register alias).
- **CITATIONS:** none external.
- **FEEDS:** WP-19

### E7-C15
- **STATUS:** Conjecture-C45 (register confidence ~70%)
- **SOURCE:** register Band III (home formal spec §17); did-cid-convergence context (registry-tier mixing)
- **CLAIM:** Four-chain publication beats single-chain publication for reconstruction resistance: distributing relationship inscriptions across heterogeneous registries raises the adversary's correlation cost relative to concentrating them on one chain. The did:cid convergence material supplies an independent design instance (registry-tier mixing: slow-finality anchoring for chronicles, fast ephemeral registries for identity events, pluggable per artifact lifecycle; E7-C32).
- **CITATIONS:** none external.
- **FEEDS:** WP-19

### E7-C16
- **STATUS:** Conjecture-C40 (register confidence ~70%; number retained per Gate G1 disposition 1)
- **SOURCE:** register Band III (home formal spec §17); vrc-protocol-spec (§2.3 dual-ledger integration)
- **CLAIM:** The Zcash dual-ledger architecture (transparent plus shielded pools) preserves the model's eight cloak properties when used as the VRC inscription substrate; the design reads the ledger duality as mirroring the two-agent separation (public commitments and stake visibility on the transparent side, private value and protection protocols on the shielded side, with the inversion pattern: the delegation side reveals what and hides value, the protection side reveals value and hides how). G1 disposition 1 note: this claim keeps C40; the existence-leak law that once proposed the same number is register C81.
- **CITATIONS:** Zcash protocol documentation (externally resolvable) for the ledger mechanics; the preservation claim is the conjecture.
- **FEEDS:** WP-19

### E7-C17
- **STATUS:** Conjecture-C1 (register status: open); with register observation C41
- **SOURCE:** vrc-protocol-spec (§2.1, §10); register Band I and Band III
- **CLAIM:** The golden-ratio allocation hypothesis: if an optimal allocation between delegation and protection budgets exists, the ratio may converge toward the golden ratio, mirrored in the design's canonical 61.8/38.2 transparent/shielded fee split. Register status governs: C1 is open, and the source itself labels the hypothesis speculative and testable, with the honest decomposition (some allocation is optimal; whether the golden ratio is that optimum, whether any universal optimum exists, and whether it emerges or must be forced are all unknown). The 61.8/38.2 split as a cultural norm of inscription practice is register C41, status observation, no confidence assigned. Numbering hygiene: the source cites the hypothesis by a retired companion-document numbering (its own conjecture 8.1); the register form C1 is the only citable one (see Contested items).
- **CITATIONS:** none external for the hypothesis; the source names its own empirical research agenda (allocation-pattern data, proximity incentives, publish regardless of result).
- **FEEDS:** WP-19

### E7-C18
- **STATUS:** Empirical-external (published standard, facts verified from the PDF per the source)
- **SOURCE:** ieee7012-plan (Part I §1.1, Part VI §6.1); myterms-package (quick reference; presentation brief)
- **CLAIM:** IEEE Std 7012-2025 (Machine Readable Personal Privacy Terms) is a published, approved standard (IEEE SA board approval 2025-11-04, published 2026-01-20; neutral host Customer Commons). Verified content points per the integration plan's proven list: the standard's scope is confined to routines in which persons as first parties reach contractual agreements with organisational second parties (party-to-party negotiation out of scope); contracts are constrained to exactly two parties (§5.4.3); negotiation is capped at one round, accept, one counter-offer, or decline (§A.1); both parties keep identical immutable copies of the agreement (bilateral recorder, §5.2.4) and the person-side agent has an explicit function for submitting a disputed agreement to auditors or regulators (§5.2.5); agreement selection consumes a deliberately small registry roster (SD-BASE family plus PDC set) hosted by Customer Commons, and implementations consume rather than mint agreement IDs; the person-side proposal inverts notice-and-consent (the individual proposes, the organisation responds).
- **CITATIONS:** IEEE Std 7012-2025 (the PDF is on disk in the myterms package; IEEE copyright constraints noted in the source, paraphrase-only discipline); Customer Commons registry (customercommons.org/p7012).
- **FEEDS:** WP-06, WP-20, WP-23

### E7-C19
- **STATUS:** Design-assumption (architectural reading, calibrated by the source itself)
- **SOURCE:** ieee7012-plan (Part I §1.2, Part IV §4.1, Part VI §6.2, §6.4)
- **CLAIM:** IEEE 7012 is the agreement layer only, a thin waist: it specifies the routine for agreeing about data terms, not the enforcement of them. Axis mapping per the plan: primarily the agent-separation axis, where the standard defines the person-agent/entity role boundary and makes separation testable via the agreement artifact, but is necessary-not-sufficient (it does not specify the separation bound; a single-agent monolith can comply with the standard and still score approximately zero on the agent axis); coarse data-axis policy via the agreement-ID lattice without cryptographic enforcement; mostly silent on the inference axis. The source's own calibration is carried: the axis mapping is a defensible architectural reading, not a theorem, and the monolith-scores-zero claim presupposes that the separation bound is empirically measurable, which remains to be demonstrated. Sanctioned headline formulation (the plan's §6.4): compliance is a precondition for the agent axis being measurable and enables bilateral chronicles as evidentiary basis for VRCs; standard compliance alone is not the architecture; the standard specifies agreement, not enforcement.
- **CITATIONS:** IEEE Std 7012-2025 (scope sections as in E7-C18); the axis vocabulary is the model's own (E1 owns the bound).
- **FEEDS:** WP-06, WP-23

### E7-C20
- **STATUS:** Design-assumption (crosswalk design; the wrapper choice explicitly one option among several)
- **SOURCE:** ieee7012-plan (Part IV §4.3, Part VI §6.3, Part V §5.3)
- **CLAIM:** The agreements-to-credentials chain: a signed IEEE 7012 agreement is a bilateral chronicle entry held identically by both parties; accumulated signed agreements with consistent behaviour across entities constitute the evidentiary raw material for a VRC; a vouchable-credentials primitive (the Choudhuri/Garg proof-of-personhood framework's CFQ19) can wrap issuance of a VRC from that raw material without re-exposing the underlying chronicle. Source calibration carried: that this primitive is the correct wrapper is conjecture (source-local label, no register number, GR-1: not minted here; other constructions may be equally suitable); the multiplicative trust-accumulation alignment between the two research lines is a convergence, and the source's framing rule is explicit, convergence not priority, in both directions.
- **CITATIONS:** the Choudhuri/Garg proof-of-personhood framework (named in the source; resolve the exact cite at WP-19/A4 time); IEEE Std 7012-2025 §5.2.4 for the chronicle basis.
- **FEEDS:** WP-06, WP-19, WP-23

### E7-C21
- **STATUS:** Design-assumption (implementation-status ledger; per-item design versus deployment, L008)
- **SOURCE:** myterms-package (presentation brief, Station 7 and the honest status ledger, 2026-07-01)
- **CLAIM:** Implementation status of the agreement-layer surfaces at the brief's date, stated per item and never presented as more than it is: (a) a two-party term-exchange negotiation API exists as code (BGIN Block 14 route); (b) the paired browser extensions (boundary-agent and delegation-agent sides) are built to the convergence UI, with the role split real in code (only the boundary-agent side has a signing path), but the cryptographic sealing function is a placeholder, sealing designed, not finished, and an ECDH exchange between the pair is scaffolded only; (c) a capability broker performs host-scoped, least-privilege delegation today with an environment-variable scope, with the signed-agreement-derived scope a designed next step; (d) the extensions' stance/spell UX tokens are not yet grounded in real Customer Commons agreement IDs (tracked alignment item); (e) a V6 edition of the integration plan is queued, not drafted (the operative plan is the 2026-04-22 v2 at PVM V5.4); (f) two near-identical extension-pair directories exist and the canonical pair is unreconciled (naming hygiene item in the source).
- **CITATIONS:** none external (status record; the brief is the package's own audit).
- **FEEDS:** WP-06, WP-23

### E7-C22
- **STATUS:** Conjecture-C94 (register confidence ~55%; registered 2026-07-01, Band X)
- **SOURCE:** hearthold-build (consolidated upstream notes §1, §2; COM hearthold README); tome-x (Act 1 bindings); register Band X
- **CLAIM:** Separation principle in a second substrate: the conditional-independence split s ⊥ m | X is realised as a running build on Archon did:cid, by an independent builder (the House of Archon / Flaxscrip), with the custodian (Warden: holds and attests, never acts in the world) separated from the actor (Witness: carries proofs out under scoped revocable delegation, never the authority) under a principal (Sovereign: authorises, occasional not always-on). Register reading: the model holds independent of its stones; a second-forge realisation strengthens the abstract convergence case (register edges to C39 and C7). Band X honest-framing fence carried: built, not asserted refers to the tested-live end-to-end subsystems of the implementation, and the confidences are the estimator's, not a completeness claim. Tome X Act 2 records C94 deepened, not re-scored: the same split realised at a second scale (guild-level knowledge portal, a public delegation face over a private custodian, with two stated invariants: the shared knowledge base never holds a member's personal history, and the custodian reads a query in memory only, logging no one); the portal is landing, built but outside the tested-live line. Register act on any promotion is the first person's, per the act's own framing.
- **CITATIONS:** github.com/Flaxscrip/hearthold (upstream implementation, MIT); the tested-live claims trace to the upstream e2e suite as reported by the swept sources (19/19 at v0.11.0), not independently re-run here.
- **FEEDS:** WP-19 (conjecture reading); implementation-record content available to WP-20/WP-23 per the filter note

### E7-C23
- **STATUS:** Conjecture-C95 (register confidence ~55%; registered 2026-07-01, Band X)
- **SOURCE:** hearthold-build (README, never-a-score section; consolidated notes §2); tome-x (Act 1, Act 2 bindings); register Band X
- **CLAIM:** The evidence graph as the anti-score: issuer-attested disclosure, a signed, decomposable evidence graph verified offline against issuer DIDs, is the structural refusal of the emitted reputation score; trust rests on the issuer's signature, not the custodian's word (register edges to C61 and C17). Mechanism as built: disclosure is governed by two independent ordinal scales (artifact sensitivity, request authorisation) plus a disclosure transform; what crosses the boundary is a derived credential (attestation, selective, redacted, full, or predicate form), never a raw dump and never a reputation number, with external disclosure requiring fresh principal approval scaled to sensitivity. Act 2 deepening: the graph matured to composite (issued leaves beside witnessed), selective (salted-digest style), and ephemeral single-use disclosure, still never a score.
- **CITATIONS:** W3C VC 1.1 and SD-JWT-VC (named in the sources as the credential and selective-disclosure formats); github.com/Flaxscrip/hearthold.
- **FEEDS:** WP-19

### E7-C24
- **STATUS:** Conjecture-C96 (register confidence ~60%; registered 2026-07-01, Band X)
- **SOURCE:** hearthold-build (README; consolidated notes §1); tome-x (Act 1, Act 2 bindings); register Band X
- **CLAIM:** Control-plane orthogonal to data-plane: the principal authorises the rules the custodian enforces; splitting the occasional control plane (Sovereign, held on a second-factor device) from the always-on data plane (Warden) means compromising the always-on host cannot author authority (register edge to C94). Act 2 records the top rung realised: a registry-governed second-factor step-up runs out-of-band on a direct custodian-to-signet channel, so the always-on host cannot forge the principal's assent; tested per the upstream e2e suite at v0.11.0. The higher proof-of-human rungs (biometric, face-liveness, FIDO2) and per-device actor instances remain the upstream repository's stated next milestones, not present capabilities.
- **CITATIONS:** github.com/Flaxscrip/hearthold.
- **FEEDS:** WP-19

### E7-C25
- **STATUS:** Conjecture-C39 (register confidence ~80%; promoted 2026-07-01 from ~50%)
- **SOURCE:** register Band III (C39 row, promotion note); tome-x (Act 1 v6 lineage); hearthold-build (cover note)
- **CLAIM:** The kindred-blade as an ecosystem-layer primitive: two builders working the same theorem from different substrates converge on the same kernel. Register promotion carried exactly: promoted 2026-07-01 (Tome X) on the ground that the cousin-forge built the whole model triad on Archon did:cid, a running second-forge realisation of the primitive, discharged from ~50% to ~80%. The upstream cover note classifies the relationship in-vocabulary as kindred (the builder already carries a downstream fork of the canon), and the SOURCES.md fence binds all E7 use: cite as independent derivation, never as competition.
- **CITATIONS:** github.com/Flaxscrip/hearthold; the register row is the numbering and confidence authority (GR-1).
- **FEEDS:** WP-19

### E7-C26
- **STATUS:** Design-assumption (implementation record; tested-live fence stated)
- **SOURCE:** hearthold-build (README, what-stands list); tome-x (Act 1 operational_form, honesty label)
- **CLAIM:** The second-substrate build carries a typed relationship-credential set and registry as running code: a decentralised-trust-graph credential set of six credential types plus a relationship card (VRC among VMC, VIC, VPC, VEC, VWC, plus RCard), issued as signed did:cid credentials; a two-faced TRQP trust registry (authorises issuers outward, grades an actor's autonomy inward, with cross-project interop demonstrated against a foreign registry); transport over DIDComm v2, authcrypt-sealed, with no registry footprint for the relationship (no observer learns of it from a registry); and a delegation lifecycle (issue, accept, revoke, with a revoked delegation failing verification). Status per the sources' own fence: tested live per the upstream e2e suite (19/19 at v0.11.0), reported, not independently re-run by this pipeline. This is the corpus's only running instance of a typed VRC credential family; the VRC protocol economics of E7-C07 to E7-C11 remain design-only and are not implemented here or anywhere.
- **CITATIONS:** github.com/Flaxscrip/hearthold; ToIP TRQP and DIF DIDComm v2 (externally resolvable specifications named by the implementation).
- **FEEDS:** WP-20, WP-23, WP-19

### E7-C27
- **STATUS:** Design-assumption (proposed named profile; source-local conjectural edges, no register numbers, GR-1 respected)
- **SOURCE:** hearthold-build (consolidated upstream notes §2)
- **CLAIM:** The separation-without-scoring profile (alias evidence-only profile): keep the agent-separation axis as architecture and issuer-attested selective disclosure; drop the value scalar, the tiers, the ranking, and any emitted reputation. First instance Hearthold; status proposed, pending the upstream author's answer to the profile-defining open question, whether the no-score stance refuses any computed reputation even privately held (a), or refuses only emitted reputation while permitting a private internal scalar (b). Source-local honesty labels carried without promotion: that the scoreless slice is more adoptable is conjectural (~60%, estimator's label at the source, no register number); that it is tighter (lower leakage) than emitting a score is architectural with a conjectural edge (~55%, same fence), argued from the existence-leak law (register C81, ~70%: if a feasibility attestation already leaks, an emitted reputation scalar leaks strictly more, being a richer, reusable, rankable statistic) and consonant with register C66 (the key is a reading, not an authority, ~55%). The information-theoretic statement of the gap between an emitted scalar and a single-use selective-disclosure graph is named by the source as the missing formalisation.
- **CITATIONS:** SPKI/SDSI object-capability lineage (designation without authority), named in the source; register C81 and C66 for the register-held edges.
- **FEEDS:** WP-19, WP-23

### E7-C28
- **STATUS:** Design-assumption (built and conformance-pinned at the reference implementation)
- **SOURCE:** star-holospace (HOW_THE_SIGIL_WORKS §2, §3; HOLOSPACE.md)
- **CLAIM:** Content-addressed key identity as built: the portable key object's identity is a kappa-label, SHA-256 over the canonical form (keys sorted recursively, no whitespace, the label field excluded from its own preimage), stamped at export and re-derived and checked at every import (re-derive, never trust; the implementation's Law L5), with a pinned conformance vector that any canon change must preserve. The substrate thesis is stated as identity is content, not location: the key travels as a self-describing artifact whose identity is verifiable by re-derivation anywhere, serverless. Governing register reading: the label is a reading, not an authority (register C66, ~55%): verification reports a verdict and never gates the operation. Any edit to the content mints a different label by construction.
- **CITATIONS:** FIPS 180-4 (SHA-2 family) via the upstream holospaces security documentation; the mechanism is verifiable by computation against the pinned vector.
- **FEEDS:** WP-19, WP-20, WP-23

### E7-C29
- **STATUS:** Design-assumption (built; the secrecy boundary stated by the source itself)
- **SOURCE:** star-holospace (HOW_THE_SIGIL_WORKS §0, §1; repo canon notes)
- **CLAIM:** The identity carrier: the full key JSON rides inside a standard PNG text chunk (base64, checksummed, valid to every viewer), so one file is simultaneously a human-legible identity rendering and the machine-readable identity object, recovered byte-for-byte on import. The carrier is portability, not secrecy: the full JSON is extractable from the image by anyone, and the design's proof-without-disclosure path is the separate redacted charge pass (a second export carrying only the proof fields and the label of the full key, leaving inscriptions, palette, and identity at home). Interop surface: the key schema carries an optional bearer DID field (did:key, explicitly a ToIP-interop passthrough that every page round-trips untouched), and the second-substrate build sealed a real group's credential graph into the same key format byte-matched against two independent implementations of the canonical serialisation (cross-implementation conformance, reported by the swept sources).
- **CITATIONS:** PNG specification (tEXt chunk mechanics, externally resolvable); the byte-match traces to the g42-seal-ref canonical serialisation reference (E8/E11 territory; cited here as the conformance anchor only).
- **FEEDS:** WP-19, WP-20

### E7-C30
- **STATUS:** Conjecture-C87 (register confidence ~50%; architectural claim, no circuit exists)
- **SOURCE:** star-holospace (repo canon, prior field); register Band VIII
- **CLAIM:** The key accumulates: the built lineage mechanism stamps an evolved key with the label of its loaded ancestor (a prior field, part of the content and so part of the next label's preimage; unchanged re-export is idempotent), giving each identity object a verifiable hash-chain ancestry. The register-held conjecture on top of the built chain: the trust recursion admits an incrementally-verifiable-computation realisation (key as accumulator, trust tasks as step circuits, charge as the folding step), post-quantum-hedged by a lattice folding scheme. L008 split stated: the prior chain is built and walkable; the IVC realisation is architectural only, and the register row itself records that no circuit exists.
- **CITATIONS:** none external at this extraction (the folding-scheme literature is E9's territory via its folding-citations source).
- **FEEDS:** WP-19

### E7-C31
- **STATUS:** Design-assumption (built at chronicle date; disclosure-budget discipline cites register-held laws)
- **SOURCE:** star-holospace (CHRONICLE_ECDH_PSI_HANDOFF_2026-06-11; repo canon notes)
- **CLAIM:** Relationship discovery without disclosure, as built: a two-party blinded private-set-intersection exchange over the two bearers' touched-vertex sets reveals the intersection and the counterparty's set size and nothing else, with the keys never leaving their holders (built 2026-06-11: RFC 3526 2048-bit MODP group, quadratic-residue hashing, short exponents, two-file exchange, per-exchange session secret; acceptance checks verified per the chronicle). Two disciplines carried from the source: small identifier domains make unsalted hash comparison a privacy placebo (64-element domain enumerable in microseconds; blinding is the entire point), and even the intersection size is an attestation, so the interface caps what a bearer enters (scope curation), an application of the existence-leak law (register C81, ~70%) and its disclosure-discount corollary (register C84, ~50%). Honest boundary per the source: the round-3 result file is a report, not a proof; a commitment-consistency zero-knowledge layer (inputs consistent with the bearer's stamped label) is designed, not built.
- **CITATIONS:** RFC 3526 (MODP groups); standard DH-PSI construction (DDH assumption in the quadratic-residue subgroup, per the chronicle); register C81/C84 rows for the budget discipline.
- **FEEDS:** WP-19, WP-23

### E7-C32
- **STATUS:** Design-assumption (convergence primitives from the integration plan; registry gap flagged)
- **SOURCE:** did-cid-convergence (integration plan Archon x agentprivacy, 2026-05-08, §1.3)
- **CLAIM:** The did:cid convergence surfaced identity primitives extracted here as design: (a) naming-ceremony verbs, claim then inscribe then confirm, bilateral relational naming rather than transactional registration; (b) the Two Paths trust-root asymmetry, user-sovereign (salt holder is the user) versus constellation-sovereign (salt holder is a notary), asymmetry of trust-root direction as a bilateral type; (c) DID-blind publication as default cloak mode, cryptographic addresses replaced by placeholders with structure preserved, inverting conventional registry semantics (local source, public mirror); (d) the seven-node decomposition of a W3C VC v2 (issuer persona, schema, subject persona, claims, proof, chronicle, context) as a schema-agnostic universal interface; (e) registry-tier mixing per artifact lifecycle (E7-C15's design instance); (f) mirrored credential pairs publish bilateral mutuality while unilateral credentials publish observation, asymmetry as data. Provenance status: these are read from the 2026-05-08 planning document describing a collaborator's built artifacts (a live local-first lattice registry, anchored chronicles with resolvable did:cid identifiers, a verified DID-blind projection run); the plan itself is a draft-for-review, and this extraction does not claim the integration it plans was executed. Registry note: the slug appears in the manifest's E7 sources list but has no SOURCES.md resolution row; the resolution used here (DOCS tomes/plans/01-integration-plan-archon-x-agentprivacy.md and its related chronicle and spec files) is proposed to A0 in this build's ledger proposal, per the SOURCES.md amendment rule.
- **CITATIONS:** W3C VC v2 (decomposition target, externally resolvable); the two anchored chronicles carry resolvable did:cid identifiers quoted in the plan.
- **FEEDS:** WP-19, WP-20

## Contested items

None tagged CONTESTED (no two canon surfaces assert incompatible claims about one object). Four findings proposed to the ledger via A0 (this cycle serialises appends; A1 does not write the ledger):

1. **Static-ceiling sentence in the Hearthold edition note (GR-7 class, CANON-LEVEL candidate).** The COM hearthold README states that under the second-substrate split leakage stays additive and the ceiling holds, R < 1, with the conditional-independence precondition present in the same sentence but with no time-indexing R(t) and no adversary-class statement in the passage. The canon spec (§5.5, §11) requires the deficit condition, the fixed adversary class, and the time-indexing wherever the strict bound is asserted, and E1-C02 owns the corrected decomposition. A canon-adjacent surface asserting the bound statically is a GR-7 surface disagreement; filed, not resolved here, and E7-C22 deliberately does not carry the bound.
2. **did-cid-convergence registry gap.** The slug is in the manifest E7 sources list but absent from SOURCES.md section 3; proposed resolution row in the ledger proposal. Until A0 applies it, E7-C32's path resolution is provisional.
3. **VRC protocol citation and numbering hygiene.** The document body cites superseded companion documents by their retired version names throughout (a retired research-paper series and older whitepaper and glossary versions) and cites the golden-ratio hypothesis by a document-local number (its conjecture 8.1) that the register does not use; the register rows (C1 open; C40 to C46 Band III) govern per GR-1. The version-block inconsistency (body 3.4, footer and history table 3.3) is already ruled, L049, body governs; the stale companion citations are a distinct hygiene item not covered by that ruling.
4. **Cross-corpus terminology collision, witness.** In Hearthold, Witness names the acting agent (holder and presenter); in the City canon and in cryptographic usage, witness runs toward the observer and attestor (Hearthold's Warden). The upstream consolidated note documents the collision and proposes a one-line glossary note in each repo. Not a claim conflict (no proposition is disputed), but any WP-19/WP-20 draft that uses both vocabularies must carry the glossary line or reviewers will read the roles backwards.

## Deferred (not extracted, with reasons)

- **dtg-36-posts (ToIP DTG Discussion #36).** External, not on disk; the SOURCES.md flag requires citation by URL when used, and no local record of the posts' content exists to extract from. The programme document attributes to this source the relationship-rooted versus attribute-rooted identity framing, the node-type-as-ZK-predicate claim, and the two-axis substrate/role model. None of these three is extracted: extracting them from the programme document's one-line gloss would launder a secondary summary into claims (GR-9). They are the first sweep items for the E7 maintenance touch once the posts are retrieved or a local record is registered; WP-20 (the DTG profile) should not draft its Discussion #36 continuation before that happens.
- **Compression-ratio and manifold-gap figures in the VRC spec.** The source carries canonical figures fenced under GR-3 (compression-efficiency ratios, the manifold-volume multiple, and fiat value-per-year bands). Not extracted at any formulation; the fence stands, and value claims are expressed in protocol units or ratios elsewhere or not at all (L057).
- **VRC-mana instrumentation and City Key economy mechanics** beyond the identity-relevant claims above: E4 (seventh capital) and E8 (ceremony governance) own the economy and ceremony readings; E11 owns conformance evidence for the implementations.

## Sweep record

Depth stated per source; the depth statement is the fence (L103 precedent). Swept 2026-07-10, A1, register head C96.

- **spec§19** (formal spec §19, Three Identity Layers): swept in full (the section is one table and one orthogonality sentence). §20 (cosmological quaternion) inspected and excluded: interpretive framework, does not enter the equation, stays upstream per GR-4.
- **whitepaper-stack** (swordsman_mage_whitepaper_v6_3.md, identity-bearing chapters): swept in full for Layer 0 (Verified Personhood), Initial Protocol Stack (Layers 1 to 5), The Three Graphs, and The Secret Language (proof-of-personhood implications); the Economics of Trust Networks and semantic-infrastructure chapters were read and their extractable content assigned to E3/E4 homes except the VRC-formation mechanism (E7-C04); the tetrahedral-architecture chapter was read and excluded (E5's algebraic territory). The rest of the whitepaper is other extractions' territory and was not re-swept.
- **vrc-protocol-spec** (specs/vrc_promise_protocol_v3_3.md): swept in full, end to end. L049 carried at E7-C07. Fenced figures observed and not carried (GR-3, L057).
- **ieee7012-plan** (SBLADE ieee7012_integration_plan_v2.md + DOCS reference/IEEE_7012_QUICK_REFERENCE.md): the v2 plan swept in full; the quick reference swept through its definitions, taxonomy, and format sections. The SBLADE alignment chronicle (CHRONICLE_MYTERMS_V2_ALIGNMENT_2026-04-22.md) not read; nothing above rests on it.
- **myterms-package** (MYTERMS): the 2026-07-01 presentation brief swept in full (its honest status ledger is E7-C21's source); A_privacy_is_value_equation.md swept (equation card; no E7 claims beyond axis vocabulary); the alliance application, executive brief, C_technical_integration.md, and the BGIN proposal PDF were not read in full, surveyed via the brief's own document inventory, and no claim above rests on the unread files. The IEEE 7012 PDF itself was not ingested (IEEE copyright fence in the sources); standard facts are carried through the integration plan's verified list.
- **hearthold-build** (HEARTH: consolidated upstream notes + COM hearthold/): the consolidated upstream notes swept through §1 (role mapping), §2 (separation-without-scoring profile), and the opening of §3 (licence seam; the seam is recorded but yields no E7 claim); the COM hearthold README swept in full; for-the-city-of-mages.md (the collaborator's bridge folio) not read. The tested-live claims are carried as reported by these sources, with the fence stated at E7-C22 and E7-C26; the upstream repo itself was not fetched or re-run.
- **star-holospace** (STAR): HOW_THE_SIGIL_WORKS.md swept §0 to §4; HOLOSPACE.md swept (vocabulary mapping, five laws, kappa-label rules); CONCEPT_COMPRESSION_REHYDRATION_DUAL_AGENTS.md swept §0 to §1 (the custody asymmetry there is owned by E1-C36 and cross-referenced, not duplicated); CHRONICLE_ECDH_PSI_HANDOFF_2026-06-11.md swept in full; the repository canon notes (key schema, prior chain, redacted pass, DID passthrough, conformance vector) swept. CHRONICLE_COMMON_GROUND_ZERO_KNOWLEDGE_2026-06-10.md not read directly; its design content is summarised in the PSI chronicle's preamble, and E7-C31 rests on the latter.
- **tome-x** (COM tomes/tome-x-the-hearth, Acts 1 and 2): swept in full, frontmatter and body. Extraction restricted to what the acts bind (C94 to C96 registrations and deepenings, the C39 promotion, the two knowledge-portal invariants, the never-a-score refusal, the no-new-conjecture rule of Act 2 and its explicit reservation of register acts to the first person); narrative colour and the spatial-anatomy material stay upstream (GR-4).
- **did-cid-convergence:** provisional resolution (registry gap, Contested item 2): DOCS tomes/plans/01-integration-plan-archon-x-agentprivacy.md swept §0 to §4 (inventory, primitives, integration surfaces, phase 1); the plan's later phases and the related cloaking-guide chronicle and cloak specification were not swept. E7-C32 is scoped to the §1.3 primitives list accordingly.
- **dtg-36-posts:** not swept (external, not on disk); see Deferred.
