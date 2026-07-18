---
extraction: E6-promise-governance
tier: internal
sources: [whitepaper-PT, PT-reference, bakhta-notes, spec-11-invitation, open-integrity-brief, hearthold-build, tome-i]
swept_complete: true
owner: A1
register_head_at_build: C97
build_note: built 2026-07-18 at the second Extraction Frontier Cycle run; the manifest's C77-C80-note token resolves through bakhta-notes (the convergence note carries its own in-file erratum confirming C70-C73 local → C77-C80 register, extending the L029 caution); four fanned sweeps + A1 direct verification of load-bearing quotes; tome-i claims restated register-neutrally per the narrative-canon rule
---

# E6 · Promise Governance

Claim-cluster for the governance layer: the imported Promise Theory axioms and their formal mapping onto the model, the assessment/trust machinery, the governance thesis (structure over policy), the Bakhta convergence and half-life conjecture families (C77-C80, C30-C33), the two written governance protocols (invitation protocol, key ceremony), and the hearthold second-substrate corroboration (C94-C96). Feeds WP-18 (applied PT paper, the primary consumer), WP-21 (ceremony governance, with E8), WP-03/WP-05 (grants, governance sections), WP-10 (developer edition).

Two register cautions bind the whole file: local conjecture numbers in the convergence note (C70-C73) are superseded by register C77-C80 (in-file erratum + L029); and the two Bakhta papers are distinct sources — the 2025 half-life paper grounds C30-C33, the April 2026 high-assurance paper grounds C77-C80 — "Bakhta convergence" without a year is ambiguous and no rehydration uses it bare.

## Claims

### E6-C01
- **STATUS:** Design-assumption (imported axiom)
- **SOURCE:** PT-reference :239-240 (§1.1); whitepaper PT sections
- **CLAIM:** The autonomy axiom is imported as foundational: "An agent can only make promises about its own behavior. No agent can make a promise on behalf of another agent."
- **CITATIONS:** Bergstra & Burgess, Promise Theory: Principles and Applications, 2nd ed. (2019)
- **FEEDS:** WP-18, WP-21

### E6-C02
- **STATUS:** Design-assumption
- **SOURCE:** PT-reference :260; whitepaper :141
- **CLAIM:** The two-agent architecture is derived from the axiom: "A single agent that both protects and delegates would violate the autonomy axiom by making promises in domains it cannot independently control" — the separation of boundary agent and delegation agent is presented as forced by the axiom, not chosen.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18

### E6-C03
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :344-348 (§2.1), :65-66; whitepaper :179-183, :731, :735
- **CLAIM:** The promise graph is: boundary agent promises protection to the principal (a (+) give-promise); delegation agent promises delegation to the principal (a (+) give-promise) and accepts authorization (a (-) use-promise); the principal promises authorization to both; and the boundary/delegation separation is itself written as an interior promise of no direct information flow.
- **CITATIONS:** Bergstra & Burgess 2019 ((+)/(-) promise typology)
- **FEEDS:** WP-18

### E6-C04
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :52-53, :264-272 (§1.2)
- **CLAIM:** A promise body decomposes as b = (τ, χ), type and constraint, mapped onto the model's compressed notation; the notation is claimed to carry PT promise-body semantics, not merely to resemble them.
- **CITATIONS:** Bergstra & Burgess notation
- **FEEDS:** WP-18

### E6-C05
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :298-309 (§1.3)
- **CLAIM:** PT's conditional-promise operator b|c is identified with the model's conditional-independence relation: the claim is that (s ⊥ m | X) instantiates the conditional operator, the two agents "operate coherently because they share the conditioning variable" X, and the notation's vertical bar carries the PT conditional semantics.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-07 (vocabulary only)

### E6-C06
- **STATUS:** CONTESTED (modal-status seam between two canon surfaces)
- **SOURCE:** PT-reference :348 ("Separation promise"), :306 vs whitepaper :743 ("Not 'shouldn't' or 'promises not to'—**cannot** by architectural design. This isn't policy")
- **CLAIM:** The reference types the separation as a promise (voluntary, in principle breakable by an autonomous agent); the whitepaper types the same separation as structural impossibility (not a promise, a cannot). The reference's own Part V-D (structural unrepresentability) is a candidate reconciling reading — PT describes the relation the architecture enforces — but no surface states the reconciliation, and a PT-literate referee will press exactly here: a promise that cannot be broken is not a promise in Burgess's sense. WP-18's central exposition burden. Ledger entry filed; wording reconciliation is a canon disposition.
- **CITATIONS:** Burgess 2015 (arXiv:1505.01716) for the unrepresentability apparatus
- **FEEDS:** WP-18 (as its load-bearing seam)

### E6-C07
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** PT-reference :513-514 (§3.1); whitepaper :204
- **CLAIM:** Assessment locality is imported: α(π) is the observing agent's own determination that promise π was kept; there is no global assessor.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-21

### E6-C08
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** PT-reference :517-518, :542-543
- **CLAIM:** The compression-assessment protocol (E3's RPP) is typed as PT assessment made continuous: where PT treats assessment as binary or scalar, compression ratio is claimed as a natural quantified assessment metric — "compression proves the promise of knowledge transfer was kept."
- **CITATIONS:** none beyond PT
- **FEEDS:** WP-18 (cross-links E3-C01)

### E6-C09
- **STATUS:** Design-assumption (parameters provisional; two-ladder note applies)
- **SOURCE:** PT-reference :547-557 (§3.2); whitepaper :211-218
- **CLAIM:** Trust is defined as a 0-1 expectation of future promise-keeping accumulated from assessment events, with the four participation tiers as bins of accumulated assessment evidence (stated bins 0.0-0.2 / 0.2-0.5 / 0.5-0.8 / 0.8-1.0). The tier system carries the E3-C27 reconciliation: two ladders share the tier names (engagement signals vs credential maturity), and the bins are design parameters, not calibrated values.
- **CITATIONS:** Bergstra & Burgess 2019 (trust as expectation)
- **FEEDS:** WP-18, WP-10

### E6-C10
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** PT-reference :573-586 (§3.3)
- **CLAIM:** Three assessment modes are imported — direct assessment α(π), belief without observation β(π), evidence with partial information ε(π) — and bilateral credential formation is typed as evidence-based (ε-mode), not direct-observation-based.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18

### E6-C11
- **STATUS:** Design-assumption (governance mechanism)
- **SOURCE:** PT-reference :596-605 (§4.1); whitepaper :233-238
- **CLAIM:** PT's invitation/imposition distinction is imported as the consent architecture: an invitation establishes the acceptance relationship before any specific proposal; an imposition proposes without prior acceptance. The model classifies consent-first flows as invitations and surveillance-default flows (the take-it-or-leave-it consent banner) as impositions.
- **CITATIONS:** Bergstra & Burgess 2019 §10.2; Burgess & Fagernes 2007 (norms grounding)
- **FEEDS:** WP-18, WP-21, WP-02 (vocabulary)

### E6-C12
- **STATUS:** Design-assumption (the governance thesis)
- **SOURCE:** PT-reference :1150-1151; whitepaper :555; tome-i Act ζ (upstream narrative form, restated)
- **CLAIM:** The governance thesis: separation is enforced through structure rather than policy — each agent promises only its own behaviour, no agent promises on behalf of another, and the architecture's non-retention (structural context erasure) replaces rule-enforcement. The thesis's narrative form ("amnesia rather than policy, structural separation rather than rule enforcement") is upstream canon; formal artifacts cite the reference, never the tome.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-21, WP-02

### E6-C13
- **STATUS:** Conjecture-C17 (register ~60%)
- **SOURCE:** PT-reference :182-193 (§0.6); NOTE_agt_scales_and_hide.md :29-46, :96-156
- **CLAIM:** Policy-enforced separation is weaker than structurally enforced separation because the violation remains possible though prohibited. Grounding: Burgess's lockdown critique ("the amount of information needed to 'lock down' every agency is too large", Spacetimes with Semantics II §6.5), which the reference calls "C17 in Burgess's own words, eleven years early"; instance: the Microsoft Agent Governance Toolkit's self-documented same-process trust boundary, which the C17 analysis predicts as the failure mode (ε_amnesia < ε_policy). The governance decomposition scales/hide/bones maps policy → Φ_inference, structural separation → Φ_agent, algebraic foundation → Φ_data, gated multiplicatively.
- **CITATIONS:** Burgess, Spacetimes with Semantics II, arXiv:1505.01716 (2015), §6.5; Microsoft Agent Governance Toolkit (April 2026, MIT); OWASP Agentic AI Top 10
- **FEEDS:** WP-18, WP-02

### E6-C14
- **STATUS:** Design-assumption (formal-mapping; A4 verification obligation attached)
- **SOURCE:** PT-reference :170-176 (§0.5), :356-371 (§2.2); whitepaper :193; tome-i Act ζ (upstream form)
- **CLAIM:** The conditional-independence residual (the model's central "gap") is claimed to be an irreducible super-agent promise in the formal sense of Burgess 2015 Definition 29: a promise arising from the composite's interior cooperation, attributable to no single sub-agent. CITATION DIVERGENCE (A4 obligation): the whitepaper attributes a differently worded version of the definition to "Bergstra & Burgess §8.3" (2019) while the reference pins the formal object to Burgess 2015 Def 29; the §8.3 wording has not been verified verbatim against either source. A4 verifies both before any tier-A use; until then rehydrations cite Burgess 2015 Def 29 only.
- **CITATIONS:** Burgess 2015 (arXiv:1505.01716) §3.10 Def 29 (primary); Bergstra & Burgess 2019 §8.3 (unverified paraphrase, do not cite until A4)
- **FEEDS:** WP-18

### E6-C15
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :739-759 (§5.2); whitepaper :255-264
- **CLAIM:** Bilateral credentials (VRCs) are typed as PT promise bundles — grouped reusable bilateral promises under coordinated assessment — with matching independent compressions as the bundle-verification event, and accumulated trust licensing the bundle to skip per-interaction re-verification. Anchor typing: content identifier = content promise, credential = coordination promise, decentralized identifier = identity promise.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-19

### E6-C16
- **STATUS:** Design-assumption (formal-mapping; GR-7 conditioning carried in-claim)
- **SOURCE:** PT-reference :764-775 (§5.3)
- **CLAIM:** PT promise-scope (the set of agents with knowledge of a promise) is mapped onto the model's information boundary, and the conditional reconstruction bound is read as a scope guarantee: under the stated preconditions (non-collusion, stated adversary class) and the declared capacity-deficit condition, with the bound time-indexed as R(t) on the clocks E2-C02 types, no adversary within the model expands its scope to the full private state. The scope reading adds no strength to the bound; it renames what the conditioned theorem already says.
- **CITATIONS:** in-suite (WP-07 for the conditioned form; cited, not re-proven)
- **FEEDS:** WP-18

### E6-C17
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** PT-reference :667-668 (§5.1); whitepaper :244
- **CLAIM:** The model's compressed notation instances are typed as PT coordination promises C(b): voluntary subordination aligning behaviour around a shared promise body.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18

### E6-C18
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :783-795 (Part V-B); whitepaper :1601
- **CLAIM:** The three graphs are typed by promise mode: the knowledge graph as what agents can promise (capability), the promise graph as what they do promise (commitment), the trust graph as which promises assessed as kept (reputation); the principal's identity is claimed as their intersection.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-19

### E6-C19
- **STATUS:** Design-assumption (mechanism definition)
- **SOURCE:** PT-reference :717-721 (Part V, V5.1)
- **CLAIM:** Bilateral verification is typed as a witness promise — an agent promising that another agent's promise was kept — with the witness's own trust-graph position staked on the testimony; false testimony breaks the witness promise.
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18, WP-21

### E6-C20
- **STATUS:** Design-assumption (formal-mapping)
- **SOURCE:** PT-reference :62; whitepaper :1235
- **CLAIM:** PT valency (bounded simultaneous exclusive commitment capacity) is mapped to the capacity constraint C_S + C_M < H(X): the budget condition is read as a valency limit preventing total revelation. The mapping is vocabulary; the mathematical content lives in the conditioned theorem (E2-C01).
- **CITATIONS:** Bergstra & Burgess 2019
- **FEEDS:** WP-18

### E6-C21
- **STATUS:** Design-assumption (external framing adopted as premise)
- **SOURCE:** bakhta-notes convergence note :23
- **CLAIM:** The integrity gap is defined as "the structural distance between what a deployer *claims* about an AI system's behavior and what an outside party can *independently verify*", with the load-bearing move that the gap is architectural rather than procedural: independent verification infeasible by deployment structure, not merely unexercised.
- **CITATIONS:** Bakhta, Toward High-Assurance AI Safety by Design for Autonomous Systems (StarkWare, April 2026)
- **FEEDS:** WP-18, WP-02

### E6-C22
- **STATUS:** Conjecture-C77 (register ~60%; local number C70 superseded, in-file erratum)
- **SOURCE:** bakhta-notes convergence note :61 (§2)
- **CLAIM:** The integrity gap and the model's separation between privacy-that-scales and privacy-that-hides are one topological object named from two sides — the assurance-stack side and the relationship side. The note's own cap: §6 holds this at ~60% and forbids merging the two registers; a reader of §2 alone would overstate the equivalence.
- **CITATIONS:** Bakhta 2026
- **FEEDS:** WP-18

### E6-C23
- **STATUS:** Conjecture-C78 (register ~60%; local C71 superseded)
- **SOURCE:** bakhta-notes convergence note :63 (§2), :43
- **CLAIM:** Bakhta's specification-intent gap (a finite formal specification satisfiable by a system violating the intent it captures; Goodhart applied to behavioural contracts) and the model's irreducible promise are claimed to be one object: the boundary where formalisation hands off — named by the assurance stack as where formal methods end, and by the model as where value lives.
- **CITATIONS:** Bakhta 2026 §4.1
- **FEEDS:** WP-18, WP-14 (vocabulary only)

### E6-C24
- **STATUS:** Conjecture-C79 (register ~45%; local C72 superseded)
- **SOURCE:** bakhta-notes convergence note :65 (§2)
- **CLAIM:** Bakhta's open composition problem (assembling assurance across providers under different trust models at runtime) and the model's hardest open item (recursive proof composition across providers under heterogeneous trust at runtime) are the same shared technical frontier; progress on either is progress on both.
- **CITATIONS:** Bakhta 2026 §6
- **FEEDS:** WP-18, WP-22

### E6-C25
- **STATUS:** Conjecture-C80 (register ~35%; local C73 superseded)
- **SOURCE:** bakhta-notes convergence note :88-92 (§4), :105 (§5)
- **CLAIM:** Promoting the assurance stack's unilateral provider-held assumption set A to a bilateral co-signed credential (attested by both, verifiable by anyone, forgeable by neither) yields a strict assurance gain in the multi-provider case, by making the provider-verifier distance non-unilaterally-rewritable; null or marginal gain in the single-provider case.
- **CITATIONS:** Bakhta 2026
- **FEEDS:** WP-18, WP-20

### E6-C26
- **STATUS:** Conjecture-C30 (register ~60%)
- **SOURCE:** bakhta-notes half-life note :26-33
- **CLAIM:** A trust edge in the credential network has a half-life whose clock starts at inscription: T(t) = T₀ · 2^(−(t−t₀)/τ) for a single inscription, decaying monotonically until renewed or augmented. The translation from cryptographic-primitive half-life to trust-edge half-life is structural, not derived; empirical path is post-deployment.
- **CITATIONS:** Bakhta, On the Half-Life of Cryptographic Trust (StarkWare, 2025) — the EARLIER paper, distinct from the 2026 high-assurance paper
- **FEEDS:** WP-18

### E6-C27
- **STATUS:** Conjecture-C31 (register ~55%)
- **SOURCE:** bakhta-notes half-life note :38-45
- **CLAIM:** Shielded (recallable-witness) and transparent (public-witness) inscriptions have distinct half-life curves for isomorphic trust content, not interconvertible without a discrete reveal step.
- **CITATIONS:** Bakhta 2025
- **FEEDS:** WP-18

### E6-C28
- **STATUS:** Conjecture-C32 (register ~50%)
- **SOURCE:** bakhta-notes half-life note :48-55
- **CLAIM:** Trust edges formed by productive work decay slower than edges formed by transactional work even at comparable initial value — the clock differs, not the starting point.
- **CITATIONS:** Bakhta 2025
- **FEEDS:** WP-18, WP-14 (reputational-fertility adjacency; the C55 scoping applies — this is the reputational channel, never raw-record compounding)

### E6-C29
- **STATUS:** Conjecture-C33 (register ~45%)
- **SOURCE:** bakhta-notes half-life note :59-66, :83-88
- **CLAIM:** Total trust half-life composes multiplicatively across the three separation axes, τ_total = τ_Σ · τ_Δ · τ_Γ, collapsing if any axis τ → 0 (the temporal extension of the multiplicative gating). Scope disclaimer carried from source: C30-C33 are named structurally and used operationally, not derived; they complement, not replace, the accumulation term, and are the behavioural-architecture analogue of the primitive-aging analysis, not its extension. No half-life claim in the family carries empirical evidence.
- **CITATIONS:** Bakhta 2025; PVM V5.4 formal specification (in-suite)
- **FEEDS:** WP-18

### E6-C30
- **STATUS:** Design-assumption (external taxonomy adopted for positioning)
- **SOURCE:** bakhta-notes convergence note :35-53 (§1)
- **CLAIM:** The assurance-claim ladder is imported for positioning: L1 execution integrity, L2 bounded-property satisfaction, L3 safety in the world, with the specification-intent gap as a structural limit between L2 and L3 that no evidence stack closes ("no stack substitutes for alignment, oversight, governance"); the five-layer bundle is governed by an assumption set A that is unilateral in the source architecture — the premise E6-C25 moves against.
- **CITATIONS:** Bakhta 2026
- **FEEDS:** WP-18, WP-02

### E6-C31
- **STATUS:** Design-assumption (governance-of-canon mechanism; specified, one live instance)
- **SOURCE:** spec-11-invitation :28-38 (the four conditions), :24 (the three postures)
- **CLAIM:** Canonical-document updates are governed by four conditions: (1) congruent geometry — consistency with the model's foundational mathematics; (2) recognisable signature — attributable authorship; (3) filed witness — an authorised reviewer witnesses the act and "signs the binding, not the page"; (4) preservation of the prior — append-only history, every prior state recoverable. Documents carry one of three permission postures: sealed, open to resident annotation, or invitation (a reserved append region for a named external contributor of congruent geometry).
- **CITATIONS:** none (internal governance spec, v1, 2026-05-17)
- **FEEDS:** WP-21, WP-18

### E6-C32
- **STATUS:** Design-assumption (governance mechanism)
- **SOURCE:** spec-11-invitation :52-66; register-of-invitations README :20-22, :43
- **CLAIM:** Invitation authority is scope-locked and origin-preserving: an accepting external contributor writes only in the reserved region, witnessed; the act confers no residency and no transferable authority; completed contributions bind permanent joint authorship, non-retractable — withdrawal is recorded as annotation, never erasure ("the city does not erase. the city annotates"). The register is the institution, its entries instances; the reserved seat outlasts any occupant, and the one live entry (a named invitee, folio open, no fixed expiry) illustrates the posture without defining it.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E6-C33
- **STATUS:** Design-assumption (governance mechanism)
- **SOURCE:** spec-11-invitation :42-48 (protocol of waiting), :70-72 (geometry adjudication)
- **CLAIM:** A pending invitation expires by silence, not by clock, with periodic review choosing seal-and-archive or renewal, never destruction. Admissibility is adjudicated by expert reading, not vote: extensions of the foundations are accepted; coherent challenges to the foundations are accepted as contested entries with both forms preserved; incoherent violations are declined with reasons returned. The contested-entry path is a governance primitive: disagreement is filed, not suppressed.
- **CITATIONS:** none
- **FEEDS:** WP-21, WP-18

### E6-C34
- **STATUS:** Design-assumption (spec; pre-deployment)
- **SOURCE:** open-integrity-brief :15-16, :42-48, :59-61, :94-97, :120-143, :159-168
- **CLAIM:** The repository trust root is a signed empty inception commit (dedicated non-reused Ed25519 key, ~128-bit) whose message is a Ricardian contract and whose committer field is the signing-key fingerprint, binding identity to key. Authority then delegates by a trust-transition commit installing an allowed-signers list, after which the inception key is retired; rotation and revocation are performed by currently authorised keys via signed commits with timestamped revocation notes, revoked-key use blocked on protected branches. Status: pre-ceremony planning; specified, not deployed.
- **CITATIONS:** Ed25519; Git SSH-signing; Ricardian contract (Grigg)
- **FEEDS:** WP-21, WP-10

### E6-C35
- **STATUS:** Design-assumption (promise-theoretic framing of E6-C34)
- **SOURCE:** open-integrity-brief :206-213
- **CLAIM:** The inception commit's Ricardian contract is framed as a PT promise — "a bilateral declaration of the repository's trust rules, made by the key to the network. Agents can only promise their own behavior" — and the inception key's self-retirement is framed as the root authority's voluntary act ("The inception key chose its own obsolescence. That choice is sovereignty").
- **CITATIONS:** Bergstra & Burgess (via the brief's own framing)
- **FEEDS:** WP-21, WP-18

### E6-C36
- **STATUS:** CONTESTED (two delegation grammars with opposite properties, un-unified)
- **SOURCE:** spec-11-invitation :52-66 vs open-integrity-brief :120-143, :206-213
- **CLAIM:** The corpus's two written governance protocols handle delegation oppositely on three axes: origin persistence (invitation: the originating author persists, credited forever; ceremony: the root key retires itself); scope (invitation: authority locked to one region, non-transferable; ceremony: delegated keys gain repository-wide authority); revocability (invitation: joint authorship non-retractable, revocation exists only as annotation; ceremony: keys fully revocable and blocked). They govern different object classes (canonical prose vs code-signing), so no single statement is contradicted — but the model has no unified delegation grammar stating which pattern applies where, and WP-18 must not present either as the general theory. Ledger entry filed; unification is a design disposition.
- **CITATIONS:** none
- **FEEDS:** WP-18, WP-21

### E6-C37
- **STATUS:** Design-assumption (voluntary-participation invariant; upstream narrative form)
- **SOURCE:** tome-i Act ε (restated register-neutrally; formal artifacts cite the PT reference, never the tome)
- **CLAIM:** Participation is not compelled: the principal may decline the role and the architecture does not enforce occupancy, while the two agents perform their boundary and projection functions without requiring a prior consent ceremony. The voluntary-participation invariant is the governance-side face of the invitation/imposition distinction (E6-C11).
- **CITATIONS:** none (upstream narrative canon)
- **FEEDS:** WP-18, WP-21

### E6-C38
- **STATUS:** Conjecture-C96 (register ~60%) · independent-corroboration evidence
- **SOURCE:** hearthold-build README :40-42, :50-55
- **CLAIM:** The control-plane/data-plane split is independently built and live-tested on a second substrate: authorization (Sovereign), enforcement/custody (Warden), and world-facing action (Witness) are separated so that "a compromise of the always-on host can no longer author authority", with each role defined by an explicit prohibition (the authorizer never runs as a server; the custodian never acts in the world; the actor is never the authority). ATTRIBUTION FENCE: the build is a cousin project's independent work; cite as external corroboration, never as this programme's implementation.
- **CITATIONS:** external cousin build (House of Archon, did:cid substrate; tracked at v0.11.0, 19/19 e2e per its README)
- **FEEDS:** WP-18, WP-06, WP-20

### E6-C39
- **STATUS:** Conjecture-C94 (register ~55%) · independent-corroboration evidence
- **SOURCE:** hearthold-build README :16-24, :51-53; for-the-city-of-mages :11-14, :64-68
- **CLAIM:** The separation principle is realised on two independent, interoperating substrates ("same theorem, two embodiments"): the cousin build holds custodian and actor conditionally independent given the private state, with additive leakage and the conditioned reconstruction bound asserted (asserted design property, not a measured result). Independence of substrate is offered as evidence the principle holds independent of implementation.
- **CITATIONS:** external cousin build; cross-project interop test recorded in its README
- **FEEDS:** WP-18, WP-06

### E6-C40
- **STATUS:** Conjecture-C95 (register ~55%) · independent-corroboration evidence
- **SOURCE:** hearthold-build README :59-61, :102-109; consolidated notes :70-114
- **CLAIM:** The cousin build's governance runs consent-first without a score: scoped revocable delegation (issue → accept → revoke, revoked delegations failing verification, live-tested); disclosure as a signed decomposable evidence graph "never a raw dump and never a reputation number", with the relying party judging for itself; release gated by a lattice check between independent sensitivity and authorization scales, external disclosure always requiring fresh proof-of-human approval. OPEN FORK (First-Person, unresolved): whether the no-score stance forbids any computed reputation or only emitted reputation with a privately held value inside the custodian — C95-adjacent, filed, unruled.
- **CITATIONS:** external cousin build
- **FEEDS:** WP-18, WP-20, WP-02

### E6-C41
- **STATUS:** Design-assumption · independent-corroboration evidence
- **SOURCE:** hearthold-build README :43, :84-86; for-the-city-of-mages :21, :29-31, :42-44
- **CLAIM:** The cousin build reifies the promise layer as a first-class object: a three-graph structure (knowledge → promise → trust) instantiated as a fixed set of verifiable credential types, governance located in a two-faced trust registry (authorising issuers outward, grading agent autonomy inward — "thin credential, fat registry"), and mutual promises modelled as reciprocal signed credentials (a published partner credential answered by a counter-credential). This is the E6-C18 typing independently rebuilt. TERMINOLOGY COLLISION (cross-reference, not resolved here): the cousin build's "Witness" is role-wise adjacent to the City's actor vocabulary; the E7/L113(d) Witness-glossary requirement covers it.
- **CITATIONS:** external cousin build; ToIP TRQP
- **FEEDS:** WP-18, WP-19, WP-20

## Contested items

| Item | Conflict | Ledger |
|---|---|---|
| E6-C06 | Separation typed as a promise (reference) vs structural impossibility (whitepaper); reconciling reading (unrepresentability) exists but is stated nowhere | L155 |
| E6-C36 | Two delegation grammars with opposite origin-persistence/scope/revocability; no unified grammar states which applies where | L155 |

## Notes for consumers

- The E6-C14 citation divergence (whitepaper "§8.3" paraphrase vs Burgess 2015 Def 29) is an A4 verification obligation before tier-A use.
- The whitepaper carries stale in-body pointers to "Promise Theory Reference v1.0" (:281, :1759) against its own metadata pin v1.5; v1.5 is the only citable version (L009 kin; ledger note filed).
- "Bakhta convergence" is ambiguous between the 2025 half-life paper (C30-C33) and the 2026 high-assurance paper (C77-C80); every rehydration names the year.
- Confidence descends monotonically within both Bakhta families (C30 60% → C33 45%; C77 60% → C80 35%); the composition and bilateral-credential claims are the weakest members, and no claim in either family carries empirical evidence.

## Sweep record

| Source | Swept | Depth |
|---|---|---|
| PT-reference (v1.5) | 2026-07-18, fanned reader + A1 quote verification (:239-240, :1150-1151) | full document; v1.4 not read (superseded, L009) |
| whitepaper-PT | 2026-07-18, fanned reader | PT sections in full; stale v1.0 pointers noted |
| bakhta-notes (3 files) | 2026-07-18, fanned reader + A1 quote verification (convergence :15, :23) | all three in full; L029 caution enforced via the in-file erratum; C77-C80-note manifest token resolves here |
| spec-11-invitation + register | 2026-07-18, fanned reader + A1 quote verification (:24, :30-31) | spec + both register files in full |
| open-integrity-brief | 2026-07-18, fanned reader + A1 quote verification (:213) | full document |
| tome-i | 2026-07-18, fanned reader | all six acts listed; governance content read in Acts ε and ζ; restated register-neutrally, never cited downstream |
| hearthold-build | 2026-07-18, fanned reader + A1 quote verification (README :50-51) | README + bridge doc + consolidated notes; attribution fence applied per claim |
