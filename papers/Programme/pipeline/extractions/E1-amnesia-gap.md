---
extraction: E1-amnesia-gap
tier: internal
sources: [spec§10, spec§11, spec§14, spec§16, spec§26, whitepaper-PT, bakhta-notes, aletheia-lethe-note, tome-ii, ceremony-specs, limitative-note]
swept_complete: true
owner: A1
register_head_at_build: C96
resweep_note: L044 re-issue pass + L034 incremental sweep 2026-07-02 (limitative-note added, C91 extracted as E1-C40); L031 filter/FEEDS reconciliation same session; maintenance touch 2026-07-07 (E1-C40 FEEDS rerouted per L065(d); E1-C09 citation verified same day per L070(2)); CTR-OBS-01 re-issue pass 2026-07-10 (E1-C04 corrected to the subadditive bound with equality condition, per L125)
---

# E1 · The Amnesia Gap

Claim-cluster for the separation bound, structural context erasure, and the conditional-independence residual: I(S; M | X) < ε*, the amnesia-versus-policy distinction (C17, made quantitative by C83), the obstruction upgrade (C86), the compounding-leakage literature and its regime boundary, the promise-theoretic grounding, the Bakhta convergence and half-life conjectures, the complement-pair algebra, the limitative (Gödel) reading of structural context erasure (register Band IX), and the implementation designs that enforce the Precondition-1 regime. Feeds WP-02 (policy brief), WP-03, WP-05, WP-07 (theory paper), WP-08 (benchmark), WP-09 (BGIN paper), WP-10 (developer edition), WP-16 (Lean), WP-23 (DIF profile).

**Filter note for TIER-S consumers (per task handoff; reconciled with the FEEDS lines 2026-07-02 per ledger L031):** the Proven-conditional core lives in spec §10.1, §10.5, §10.6, §11.1 to §11.3, §11.5 and the information-theoretic rows of §16 (claims E1-C01 to E1-C05 below). Everything sourced to spec §11.4, §14.4, §14.6, §14.7, the research notes, the tome, and the ceremony specs is conjecture apparatus, empirical-external context, or design; TIER-S artifacts draw on E1-C01 to E1-C05 (preconditions always stated; wherever the strict bound R_max < 1 is cited, the capacity-deficit condition is stated with them, per the corrected spec §11.1 and L044) and the Empirical-external claims E1-C09 to E1-C11, E1-C27 only. **WP-09 clause (L111(a), 2026-07-10):** in the discussion-paper genre (WP-09, BGIN), the design-status claims E1-C06, E1-C36, E1-C37, E1-C38 are additionally admissible at TIER-S as design descriptions with implementation status carried verbatim; the WP-02 operation-sequence fence is genre-specific to the policy brief, not tier-wide, and this clause does not widen the WP-02 allow-list. Conjecture-status claims feed WP-09 as labelled open questions only, never as claims (L111(b)); such FEEDS entries carry the open-question-feed annotation.

**Reconciliation ruling (L031, 2026-07-02, A1):** the allow-list above is authoritative and the stricter reading stands; it has governed WP-02 through release-draft v4, whose extraction basis draws only allow-listed E1 claims. The FEEDS lines were narrowed to agree; a claim's FEEDS names WP-02 if and only if the claim is on the allow-list. Per claim: **E1-C06** stays off the allow-list and off WP-02 (design-status definition, warrant is design-level not proven-conditional; WP-02 v4 deleted the operation-sequence test and rests the structural-versus-policy distinction on E1-C04 and E1-C27, both allow-listed; reintroducing the test at TIER-S requires a register-process ruling per the fence recorded in WP-02 v4). **E1-C17** loses WP-02 from FEEDS (semantic grounding in Promise Theory, not a proven-conditional result; TIER-S admits no interpretive grounding, and WP-02 has never cited it through v4). **E1-C31** loses WP-02 from FEEDS (register-held conjecture C49; the brief's planning-language slot is carried by E2-C09, which WP-02 v4 lists in its extraction basis with conjecture apparatus stripped; a second conjecture-sourced planning feed at a tier that forbids conjectures would duplicate apparatus without adding an allow-listed warrant).

**Reconciliation ruling (L111, 2026-07-10, A1):** the filter note and FEEDS lines reconcile to WP-09 draft-v1 under the three A0 rulings recorded at ledger L111; claim statements are unchanged (the L031 method). (a) The design-status claims E1-C06, E1-C36, E1-C37, E1-C38 gain WP-09 as design-feeds under the WP-09 clause above. (b) The conjecture-status claims E1-C07, E1-C08, E1-C19, E1-C22, E1-C31, E1-C32 carry WP-09 as open-question-feeds, consumed as labelled open questions only, never as claims (E1-C07 and E1-C08 gain the feed; E1-C19, E1-C22, E1-C31, E1-C32 already named WP-09 and are now annotated). (c) E1-C17 and E1-C18 lose WP-09 from FEEDS: interpretive grounding is not consumed at TIER-S in any genre (the L031 interpretive-grounding precedent), and WP-09 draft-v1 does not cite them.

## Claims

### E1-C01
- **STATUS:** Proven-conditional
- **SOURCE:** spec §10.1, §10.5
- **CLAIM:** The separation bound I(S; M | X) < ε* (mutual information between boundary agent S and delegation agent M, conditioned on the data subject X, bounded above by ε*) holds under Precondition 1 (non-collusion / channel independence: I(Y_S; Y_M | X) = 0 and no third channel carries the inter-agent residue) and Precondition 2 (capacities and adversary evaluated against a stated, fixed adversary class). The bound holds in the regime structural context erasure is designed to enforce, and only there.
- **PRECONDITIONS:** non-collusion; fixed adversary class. Never cite without both.
- **CITATIONS:** Wyner 1975 (wire-tap channel, weak-secrecy equivocation); Csiszár & Körner 1978 (colluding-observer failure mode of the summation assumption).
- **FEEDS:** WP-02, WP-07, WP-09

### E1-C02
- **STATUS:** Proven-conditional (tightened 2026-07-02 per L044: "under budget constraints" made explicit as the capacity-deficit condition)
- **SOURCE:** spec §11.1, §11.2, §11.5, §16 row (corrected 2026-07-02, L044 execution)
- **CLAIM:** R_max = (C_S + C_M)/H(X) with the Fano error floor P_e ≥ 1 − R_max, within Preconditions 1 and 2 of §10.5, which license the additive capacity sum and prove the floor; the preconditions "do not by themselves place R_max below one" (spec §11.1). The strict bound R_max < 1 holds when, additionally, the capacity-deficit condition C_S + C_M < H(X) holds: "a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture" (spec §11.1). This condition is what the spec §16 table abbreviates as "under budget constraints": "the budget constraint is the capacity-deficit condition C_S + C_M < H(X) that places the ceiling below one" (spec §16 row, corrected). Time-indexed per spec §5.5: the capacities are evaluated against the stated adversary class at a stated time; the deficit condition, not the preconditions, is the quantity that erodes as stronger classes arrive, and the bound says nothing about a later, stronger class (E2 holds the time thread; the full decomposition is E2-C01).
- **PRECONDITIONS:** non-collusion; fixed adversary class; the strict bound additionally requires the declared capacity-deficit condition (stated together with the preconditions, never as a third precondition); time-indexing R(t) stated in the same passage (GR-7).
- **CITATIONS:** Fano (1961); Cover & Thomas (source-coding converse); Leung-Yan-Cheong & Hellman 1978 (secrecy capacity as capacity difference).
- **FEEDS:** WP-02, WP-07, WP-09

### E1-C03
- **STATUS:** Proven-conditional
- **SOURCE:** spec §11.3, §16
- **CLAIM:** Graceful degradation: small ε violations of the separation bound produce small privacy losses; failure is continuous, not catastrophic, within the conditional regime.
- **PRECONDITIONS:** as E1-C01.
- **CITATIONS:** documented in Research Paper v4.2 per spec §16; standard information-theoretic continuity argument.
- **FEEDS:** WP-02, WP-07

### E1-C04
- **STATUS:** Proven-conditional (re-issued 2026-07-10 per CTR-OBS-01, L125)
- **SOURCE:** spec §16, §14.7 (corrected 2026-07-10, CTR-OBS-01/L125 execution)
- **CLAIM:** Additive mutual-information leakage bound: under Precondition 1 (the two observation channels conditionally independent given X and nothing carrying the inter-agent residue), the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most I(X; Y_S) + I(X; Y_M), with equality if and only if additionally the two outputs are marginally independent (I(Y_S; Y_M) = 0). Every downstream ceiling and floor statement uses only the at-most direction, which the redundancy term only tightens. The 95% label of spec §16 applies to the at-most bound in that regime and nowhere else. The compounding results (E1-C09, E1-C10) describe the complement of the regime and do not contradict the bound; the two are one theorem family on two sides of one architectural line, the line being whether the inter-agent channel exists.
- **PRECONDITIONS:** Precondition 1 (no inter-agent channel); equality additionally requires marginal independence of the outputs.
- **CITATIONS:** chain rule for mutual information and the interaction identity (Cover & Thomas); scoping stated in spec §16 "Scoped, not lowered" (corrected wording).
- **FEEDS:** WP-02, WP-07, WP-08, WP-09

### E1-C05
- **STATUS:** Design-assumption (grounding map, not a new result)
- **SOURCE:** spec §10.6
- **CLAIM:** Within the conditional regime the separation bound and ceiling are instances of an established family rather than internal results: Wyner wire-tap equivocation; the Fano converse; Leung-Yan-Cheong and Hellman secrecy capacity; the Bayes-capacity bound of quantitative information flow (Miracle Theorem); Geiger and Kubin relative information loss. Citation strategy: cite the family plus named preconditions, not internal papers.
- **CITATIONS:** as listed in the claim; all externally resolvable.
- **FEEDS:** WP-02, WP-07

### E1-C06
- **STATUS:** Design-assumption (definition)
- **SOURCE:** spec §14.1, §10.4, §14.6
- **CLAIM:** Structural context erasure (structural amnesia): an agent has structural amnesia with respect to origin O if no sequence of permitted operations can reconstruct O from the agent's current state (a reachability statement quantified over paths). Classification test: if some operation sequence can recover shared origin, the separation is policy-enforced; if none can, it is amnesia-enforced. Grade-1 (hiding: encryption, access control, recoverable with keys) is distinguished from Grade-2 (forgetting: mathematically unrecoverable); the conjectural formal criterion for the distinction is E1-C12.
- **CITATIONS:** none (definitional).
- **FEEDS:** WP-07, WP-08, WP-09 (design-feed per L111), WP-10, WP-23

### E1-C07
- **STATUS:** Conjecture-C17 (register confidence 60%)
- **SOURCE:** spec §10.4, §14.4
- **CLAIM:** Amnesia-enforced separation provides tighter Φ_agent guarantees than policy-enforced separation: ε_amnesia < ε_policy. Policy-enforced violation is possible though prohibited; amnesia-enforced violation is structurally excluded. Qualitative at V5.4; made quantitative by C83 (E1-C08).
- **CITATIONS:** none external for the conjecture itself; instances at E1-C27 (policy side), E1-C36/E1-C37 (amnesia side, design).
- **FEEDS:** WP-07, WP-08, WP-09 (open-question-feed per L111)

### E1-C08
- **STATUS:** Conjecture-C83 (register confidence ~55%)
- **SOURCE:** spec §14.7
- **CLAIM:** Compositional Leakage Amplification: under policy-only separation, behavioural leakage compounds toward the sequential bound (2^N − 1)ε with agent-chain depth N; amnesia-enforced separation breaks the Markov chain between agents and caps total leakage at the additive bound Nε; the policy-to-amnesia gap is exponential-to-linear in N (3ε versus 2ε at N = 2; 31ε versus 5ε at N = 5). The sequential bound is proven externally (E1-C09); the conjecture is that real amnesia implementations achieve the chain break, an engineering claim about the erasure protocol, not a theorem. Register edge: C7 → C83 → C17.
- **CITATIONS:** arXiv:2603.05520 (the proven bound); AgentLeak measurement as the channel evidence (E1-C10).
- **FEEDS:** WP-07, WP-08, WP-09 (open-question-feed per L111)

### E1-C09
- **STATUS:** Empirical-external
- **SOURCE:** spec §14.7, §26
- **CLAIM:** Asif and Amiri prove (their Theorem 4.1) that under sequential composition of N agents with per-agent constraint I(O_i; S_i) ≤ ε_i, global leakage satisfies I(O_N; S_1, ..., S_N) ≤ Σ_i 2^(N−i) ε_i, uniform case (2^N − 1)ε, via the chain rule and the conditional data processing inequality; empirically, average mutual information rises 0.49 (two agents) to 1.05 (five agents) on MedQA with LLaMA-7B. Patil, Stengel-Eskin and Bansal reach the same conclusion through composition analysis.
- **CITATIONS:** arXiv:2603.05520 (Asif & Amiri, RPI, 2026-03-09); arXiv:2509.14284 (Patil, Stengel-Eskin & Bansal, preprint 2025-09-16; verified by A4 2026-07-07, L070(2); citable downstream, cite as preprint).
- **FEEDS:** WP-02, WP-07, WP-08, WP-09

### E1-C10
- **STATUS:** Empirical-external
- **SOURCE:** spec §10.5, §14.7, §26
- **CLAIM:** AgentLeak (1,000 scenarios, 4,979 traces, five frontier models) measures: multi-agent configurations reduce per-channel output leakage to 27.2% versus 43.2% single-agent, while unmonitored inter-agent channels leak at 68.8%, raising total system exposure to 68.9%; output-only audits miss 41.7% of violations. This measures the inter-agent channel whose deletion defines the Precondition-1 regime.
- **CITATIONS:** arXiv:2602.11510 (El Yagoubi, Badu-Marfo & Al Mallah, Polytechnique Montréal).
- **FEEDS:** WP-02, WP-07, WP-08, WP-09

### E1-C11
- **STATUS:** Empirical-external (landscape)
- **SOURCE:** spec §26
- **CLAIM:** The multi-agent privacy field arrived at separation-of-duties independently and repeatedly in 2025 to 2026: MAGPIE (arXiv:2506.20737), the contextual-integrity multi-agent reasoning line, PrivAct (arXiv:2602.13840), and maker-checker / supervisor-worker orchestration patterns. All use prompt-level or training-level controls; none enforce separation architecturally. The model's prediction that these fail under composition traces to C83 (E1-C08); the 68.9% total-exposure measurement (E1-C10) is consistent with that prediction. Plurality, not precedence.
- **CITATIONS:** arXiv:2506.20737; arXiv:2602.13840; arXiv:2602.11510.
- **FEEDS:** WP-02, WP-09, WP-10

### E1-C12
- **STATUS:** Conjecture-C86 (register confidence ~30%)
- **SOURCE:** spec §14.6
- **CLAIM:** Obstruction-Theoretic Amnesia: Grade-2 forgetting is the condition that the obstruction class to gluing the agents' local views into a global witness of O is non-vanishing; Grade-1 is the condition that the class vanishes and only the gluing data is withheld (key management, not mathematical impossibility). If C86 holds, structural erasure is the only term in the model whose security is independent of t, because no archive remains for a stronger decoder. Honest limit: the sheaf-theoretic machinery (views as sections, obstruction as a Čech class) is unconstructed for the dual-agent instantiation; ~30% prices a framing, not a theorem. Falsification: any composition of agent views, under any future capability, that recovers a Grade-2-forgotten O.
- **CITATIONS:** none external (honest limit stated in canon).
- **FEEDS:** WP-07, WP-16

### E1-C13
- **STATUS:** Conjecture-C73 (register confidence ~50%)
- **SOURCE:** spec §14.6 (cross-reference); register Band VII
- **CLAIM:** Terminal-obstruction is a primitive obstruction class and structural context erasure is its canonical instance (placement claim: WHERE erasure sits in the obstruction taxonomy, terminal not path). Division of labour with C86 (WHAT forgetting is mathematically): the two fail independently; a counterexample to the taxonomy placement does not touch the cohomological claim, and vice versa.
- **CITATIONS:** none external; home document pvm-v6-arch1rt-operational-reachability.md (outside E1 sources; cited here only via spec §14.6).
- **FEEDS:** WP-07, WP-16

### E1-C14
- **STATUS:** Conjecture-C18 (register confidence 25%)
- **SOURCE:** spec §11.4
- **CLAIM:** Dynamical reconstruction ceiling: if the sovereignty path exhibits strange-attractor dynamics with positive Lyapunov exponent, reconstruction error grows as |π(t) − π'(t)| ~ |δ_0| · e^(λt), λ > 0; a second ceiling independent of the information-theoretic one (remove either, the other stands). λ is unmeasured. Primary home of the time thread is E2 (E2-C10).
- **CITATIONS:** none external yet.
- **FEEDS:** WP-07 (as open problem)

### E1-C15
- **STATUS:** Conjecture-C51 (register confidence: open)
- **SOURCE:** spec §10.2
- **CLAIM:** The conditional-independence residual (the gap) is the node of maximal betweenness centrality C_B(v) = Σ_{s≠v≠t} σ_st(v)/σ_st in the trust graph, and remains so across trust-graph evolutions (the persistence is C51; the static measurement is computable via Brandes' O(V·E) algorithm).
- **CITATIONS:** Brandes, U. (2001), Journal of Mathematical Sociology 25(2), 163-177.
- **FEEDS:** WP-07

### E1-C16
- **STATUS:** Conjecture-C7 (register confidence 30%)
- **SOURCE:** spec §10.3
- **CLAIM:** Composite separation is multiplicative across the three axes: Φ_v5 = Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ); collapse of any axis weakens the whole bound. Multiplicativity is the conjecture (C7, the V6 falsification frontier); the per-axis definitions are spec §4.
- **CITATIONS:** none external.
- **FEEDS:** WP-07, WP-16

### E1-C17
- **STATUS:** Design-assumption (semantic grounding)
- **SOURCE:** whitepaper-PT (Promise-Theoretic Foundations: Autonomy Axiom)
- **CLAIM:** A single agent promising both protection and delegation behaviours violates the Promise Theory autonomy axiom (an agent can only make promises about its own behaviour). The dual-agent architecture assigns protection promises to boundary agent S, delegation promises to delegation agent M, and authorisation promises to the data subject; none promises on another's behalf. Grounding is semantic; the security properties come from E1-C01/E1-C02 and the implementation mechanisms, not from Promise Theory.
- **CITATIONS:** Bergstra & Burgess (2019), Promise Theory: Principles and Applications.
- **FEEDS:** WP-10 (WP-02 removed 2026-07-02 per the L031 reconciliation ruling in the filter note; WP-09 removed 2026-07-10 per the L111 reconciliation ruling in the filter note)

### E1-C18
- **STATUS:** Design-assumption (semantic interpretation)
- **SOURCE:** whitepaper-PT (The First Person System as Superagent; The Gap as Irreducible Promise)
- **CLAIM:** The composite (data subject + S + M) is a superagent with interior promises (protect, delegate, authorise, and the separation promise of no direct information flow) and exterior promises (coordination via M, boundary via S). The conditional-independence property S ⊥ M | X is interpretable as an irreducible promise of the superagent: attributable to no single component, arising from the promises the components do not make to each other; on this reading no adversary can extract it from any single component. The formal content is E1-C01; this claim supplies interpretation only.
- **CITATIONS:** Bergstra & Burgess (2019) §8.3 (irreducible promises).
- **FEEDS:** WP-07 (WP-09 removed 2026-07-10 per the L111 reconciliation ruling in the filter note)

### E1-C19
- **STATUS:** Conjecture-C77 (register confidence ~60%)
- **SOURCE:** bakhta-notes (pvm-v6-bakhta-integrity-gap-convergence.md §2, §5)
- **CLAIM:** Bakhta's integrity gap (architectural infeasibility of independent verification) and the model's privacy-that-scales versus privacy-that-hides separation are one object: a topological, not procedural, distinction; the two literatures converged independently. Numbering note: the source note carries stale local numbers C70 to C73 for this block; the register assigns C77 to C80 (Band VII, renumbered at Run 0). The register numbering governs.
- **CITATIONS:** Bakhta, A. (2026), Toward High-Assurance AI Safety by Design for Autonomous Systems, StarkWare.
- **FEEDS:** WP-07, WP-09 (open-question-feed per L111)

### E1-C20
- **STATUS:** Conjecture-C78 (register confidence ~60%)
- **SOURCE:** bakhta-notes (integrity-gap note §2, §5)
- **CLAIM:** The specification-intent gap (a finite formal specification Φ can be satisfied by a system violating the intent it was meant to capture; behavioural intent is not a formal object) and the model's irreducible promise are one object seen from two sides: the proof side (where formal methods hand off to alignment) and the relationship side (where value lives). Non-formalizability of behavioural intent is the load-bearing premise of both.
- **CITATIONS:** Bakhta (2026); Goodhart-applied-to-behavioural-contracts framing per the source manuscript.
- **FEEDS:** WP-07

### E1-C21
- **STATUS:** Conjecture-C79 (register confidence ~45%)
- **SOURCE:** bakhta-notes (integrity-gap note §2, §5)
- **CLAIM:** The shared technical frontier of the assurance stack and the relationship model is recursive proof composition across providers under heterogeneous trust models, assembled at runtime; progress on either programme is progress on both.
- **CITATIONS:** Bakhta (2026) §6 (composition problem).
- **FEEDS:** WP-07

### E1-C22
- **STATUS:** Conjecture-C80 (register confidence ~35%)
- **SOURCE:** bakhta-notes (integrity-gap note §4, §5)
- **CLAIM:** Promoting a unilateral assumption set A (held by the provider, inspected by the auditor) to a bilateral co-signed credential (attested by both, verifiable by anyone, forgeable by neither) yields a strict assurance gain in the multi-provider case by making the provider-verifier distance non-unilaterally-rewritable; null or marginal in the single-provider case.
- **CITATIONS:** Bakhta (2026); the open question is carried back to the source author per the note.
- **FEEDS:** WP-07, WP-09 (open-question-feed per L111)

### E1-C23
- **STATUS:** Conjecture-C30 (register confidence 60%)
- **SOURCE:** bakhta-notes (pvm-v6-1-bakhta-half-life.md §C30)
- **CLAIM:** A trust edge in the relationship-credential network has a half-life τ_VRC whose clock starts at inscription: T(t) = T_0 · 2^(−(t−t_0)/τ_VRC) for a single inscription, decaying monotonically until renewed (fresh inscription, same axis) or augmented (complementary inscription, co-supporting axis). The parametric form is conjectural; the half-life is named structurally, not derived.
- **CITATIONS:** Bakhta, A. (2025), On the Half-Life of Cryptographic Trust, StarkWare (the framework being translated).
- **FEEDS:** WP-03, WP-07

### E1-C24
- **STATUS:** Conjecture-C31 (register confidence 55%)
- **SOURCE:** bakhta-notes (half-life note §C31)
- **CLAIM:** Shielded and transparent inscription registers have different half-life curves even when carrying isomorphic trust content: recallable witness (holder retains the viewing key) versus public witness (anyone with the chain reads it); the two are not interconvertible without a discrete reveal step.
- **CITATIONS:** Bakhta (2025).
- **FEEDS:** WP-07

### E1-C25
- **STATUS:** Conjecture-C32 (register confidence 50%)
- **SOURCE:** bakhta-notes (half-life note §C32)
- **CLAIM:** A trust edge formed by productive work has a longer half-life than one formed by transactional work, even when initial values are comparable (the clock differs, not the starting weight). C46 is a register alias of this claim; C44 is the comparison statement at the moment of inscription.
- **CITATIONS:** Bakhta (2025); empirical longitudinal measurement named as the formalisation path.
- **FEEDS:** WP-07

### E1-C26
- **STATUS:** Conjecture-C33 (register confidence 45%)
- **SOURCE:** bakhta-notes (half-life note §C33)
- **CLAIM:** Total trust half-life composes multiplicatively across the three separation axes: τ_total = τ_Σ · τ_Δ · τ_Γ; ageing in one axis cannot be compensated by another, and the product collapses if any single τ approaches zero. This extends the multiplicative gating (E1-C16) through the time domain.
- **CITATIONS:** Bakhta (2025); structural argument from the V5.4 gating claim.
- **FEEDS:** WP-07

### E1-C27
- **STATUS:** Empirical-external (vendor documentation)
- **SOURCE:** bakhta-notes (NOTE_agt_scales_and_hide.md)
- **CLAIM:** Microsoft's Agent Governance Toolkit (released 2026-04-02; Ed25519 DIDs, inter-agent trust protocol, policy interception, 0-1000 trust scoring) is a live instance of policy-enforced separation: its own documentation states the policy engine and agents run in the same process, the same trust boundary as every Python agent framework, with container isolation recommended but external to the toolkit's enforcement. This is the ε_policy class of E1-C07: violation possible though prohibited. No reconstruction bound, no information-theoretic guarantee, no structural separation. The layers compose (policy governance outside, structural separation beneath) rather than compete.
- **CITATIONS:** Microsoft (2026), Agent Governance Toolkit, MIT License, github.com/microsoft/agent-governance-toolkit.
- **FEEDS:** WP-02, WP-09, WP-10

### E1-C28
- **STATUS:** Design-assumption (arithmetic on the encoding; verifiable by computation)
- **SOURCE:** aletheia-lethe-note
- **CLAIM:** On the Z/(2^6)Z encoding, vertices 25 (011001) and 38 (100110) are exact bitwise complements: bnot(25) = 38, 25 AND 38 = 0, 25 XOR 38 = 63; both have Hamming weight 3 (equal stratum, peer structure). The AND = 0 identity is the algebraic form of the orthogonality (⊥) between the pair; the XOR = 63 identity states that the pair jointly spans all six dimensions. The pair occupies at the proof-medium / witness-substrate layer the same involution relationship (bnot) that the agent layer assigns via neg and bnot with neg ∘ bnot = succ; the non-interactive proof transform (Fiat-Shamir) is paired with witness-unretrievability as the two complementary halves of one zero-knowledge architecture. Encoding note: under the 2026-06-09 canonical encoding lock (Protection=32 ... Value=1), vertex 38 carries the transmission-medium reading and vertex 25 the holding-substrate reading (a reseat from earlier grimoire pins, reconciled in v10.4.0; the arithmetic is unchanged). Mythological names stay upstream per GR-4.
- **CITATIONS:** Fiat & Shamir 1986 (non-interactive transform, for the protocol identification only); arithmetic verifiable directly.
- **FEEDS:** WP-16

### E1-C29
- **STATUS:** Conjecture-C54 (register confidence ~40%)
- **SOURCE:** aletheia-lethe-note
- **CLAIM:** Phi-Adjacency: disclosure ratios of complement (bnot) pairs cluster near 1/φ. Instance: δ(38) = 38/63 ≈ 0.6032, within 2% of 1/φ ≈ 0.6180 (with δ(25) = 25/63 ≈ 0.3968 ≈ 1/φ² on the complement side). Register note: C54 follows the number, not the name (the 2026-06-09 reseat keeps disclosure-φ on vertex 38).
- **CITATIONS:** none external; the ratio is arithmetic, the clustering claim is the conjecture.
- **FEEDS:** WP-16

### E1-C30
- **STATUS:** Conjecture-C47 (register confidence ~50%)
- **SOURCE:** tome-ii (Act 6, The Fourth Aging Category; frontmatter honesty label)
- **CLAIM:** "Ages progressively" is a fourth ageing category for trust substrates beyond the cryptographic literature's three (ages by parameter growth, by substrate migration, by fresh attestation): under the dynamical ceiling, the path's security grows with time through its own dynamics rather than through refresh or migration. Dependency: conditional on C18 (λ > 0), which is unmeasured.
- **CITATIONS:** Bakhta (2025) for the three-category taxonomy; none for the fourth category.
- **FEEDS:** WP-07

### E1-C31
- **STATUS:** Conjecture-C49 (register confidence ~70%)
- **SOURCE:** tome-ii (Act 7, The Behavioural Mosca)
- **CLAIM:** Behavioural Mosca Inequality: Mosca's X + Y > Z (migration time plus security lifetime exceeding adversary maturity) has a behavioural analogue; migration to a structurally separated substrate must complete before observation capability matures enough to reconstruct behavioural traces recorded today. Register alias: C61 restates this in the city register. L031 reconciliation: not fed to WP-02; the brief's planning language is carried by E2-C09 (see the filter note ruling).
- **CITATIONS:** Mosca, M. (2018) (original inequality).
- **FEEDS:** WP-09 (open-question-feed per L111), WP-07 (WP-02 removed 2026-07-02 per the L031 reconciliation ruling in the filter note)

### E1-C32
- **STATUS:** Conjecture-C48 (register confidence ~65%)
- **SOURCE:** tome-ii (Act 7 frontmatter, v6 lineage)
- **CLAIM:** The reconstruct-later threat model for behavioural data (record now under today's adversary, reconstruct under tomorrow's) is structurally isomorphic to Bakhta's Threat Model 1 (harvest-now-decrypt-later for cryptographic material). Register alias: C60 (renumbering eddy, v1.5.0 patch).
- **CITATIONS:** Bakhta (2025); HNDL literature as the cryptographic side.
- **FEEDS:** WP-07, WP-09 (open-question-feed per L111)

### E1-C33
- **STATUS:** Conjecture-C50 (register confidence ~60%)
- **SOURCE:** tome-ii (Act 6 frontmatter, v6 lineage)
- **CLAIM:** The model's multiplicative gating (E1-C16) and Bakhta's compositional defence are the same defence structure instantiated at different substrates (behavioural architecture versus cryptographic primitives).
- **CITATIONS:** Bakhta (2025, 2026).
- **FEEDS:** WP-07

### E1-C34
- **STATUS:** Conjecture-C28 (register confidence 30%)
- **SOURCE:** tome-ii (Act 3, The Terminal; Act 5, The Hole the Schema Cannot Bind)
- **CLAIM:** The reconstruction ceilings are independent because the canonical form factors into structurally separate components (β / μS / Ω); each ceiling operates at a distinct component, and the terminal β anchors the recursion (the sovereignty instantiation takes β = null). Tome reading (Act 5): the chooser is the component none of the ceilings reach; the formal content is the factorisation.
- **CITATIONS:** none external; home note pvm-v6-arch1-canonical-form.md (E5's source; cited here via tome-ii lineage).
- **FEEDS:** WP-16

### E1-C35
- **STATUS:** Conjecture-C29 (register confidence 20%)
- **SOURCE:** tome-ii (Acts 4 and 5)
- **CLAIM:** The Second Person Lift You := μS.(β ∨ Ω(S,S)): the schema can express the operations and their compositions but cannot bind the variable that chooses which composition is applied next; the chooser is structurally unbindable, and the architecture therefore admits any data subject rather than enforcing a particular one. The structural inability is operational (the grammar has no binder for it); the load-bearing-void reading is architectural.
- **CITATIONS:** none external.
- **FEEDS:** WP-07 (as design rationale), WP-16

### E1-C36
- **STATUS:** Design-assumption (implementation design; deployed as described at spec date)
- **SOURCE:** ceremony-specs (runecraft-protocol-spec-v1.md §4)
- **CLAIM:** The dual-runtime design instantiates the two erasure grades in browser storage: the delegation agent's Ed25519 keypair is generated once and persisted (localStorage, survives sessions); the boundary agent's Ed25519 keypair is generated per ceremony and destroyed at session close (sessionStorage, destroyed on tab close). The erasure is structural (storage destruction), not instructed (policy); this is an implementation instance of the E1-C06/E1-C07 class. The cross-territory binding is a manual export/import carried by the data subject; no automated inter-agent channel exists, which enforces the Precondition-1 regime by construction at this layer.
- **CITATIONS:** none external (design document); C17 linkage stated in the source.
- **FEEDS:** WP-09 (design-feed per L111), WP-10, WP-23

### E1-C37
- **STATUS:** Design-assumption (specified, not built at spec v1.1)
- **SOURCE:** ceremony-specs (ceremony-engine-spec-v1_1.md §3.1; DUAL_TERRITORY_CEREMONY_SPEC_v1.md §4, §6.6)
- **CLAIM:** The ceremony-engine design places the two agents in separate browser extension processes with separate storage and separate permissions, communicating only via an explicit message channel: a process-level instance of I(S; M | X) < ε*. Implementation status per source: the forge is operational; the two-extension engine is specified and the code is not written at spec v1.1. The ceremony cycle includes a re-instantiation step in which the disclosing role restarts with erased context between cycles.
- **CITATIONS:** none external (design document).
- **FEEDS:** WP-09 (design-feed per L111), WP-10, WP-23

### E1-C38
- **STATUS:** Design-assumption (engineering; one built instance)
- **SOURCE:** ceremony-specs (DUAL_AGENT_HARNESS_SPEC_v1.md §1, §3)
- **CLAIM:** The dual-agent harness operationalises the conditional-independence residual as a held-out gate at workflow level: the proposer (delegation seat) cannot tune to the witnesses the prover (boundary seat) will draw, realising I(Y_S; Y_M | X) = 0 as a mechanism rather than an assumption; a proposer that grades itself builds mirages, so the validated result emerges only from the two seats held apart. One instance built at spec date (the PQC circuit-optimisation harness).
- **CITATIONS:** none external (design document); instance record is E10/E11 material.
- **FEEDS:** WP-09 (design-feed per L111), WP-10

### E1-C39
- **STATUS:** Design-assumption (engineering; see ledger proposal on §16 labelling)
- **SOURCE:** spec §16; ceremony-specs (ceremony-engine-spec-v1_1.md §4)
- **CLAIM:** Two engineering rows of spec §16: (a) two-extension autonomy, separate OS processes enforce the separation bound at operating-system level; (b) DOM-free measurement, a layout primitive (layoutNextLine) that removes the reflow-based fingerprinting surface (getBoundingClientRect, offsetHeight, LayoutShift) at source, applying the separation at the rendering layer. Spec §16 lists both among proven results at 95%; this extraction classifies them as engineering claims because their warrant is implementation-level, not information-theoretic (filed to the ledger for register-process confirmation, not resolved here).
- **CITATIONS:** pretext library documentation (github.com/nicklasserra/pretext) for (b).
- **FEEDS:** WP-10

### E1-C40
- **STATUS:** Conjecture-C91 (register confidence ~60%; registered Run 8, 2026-06-28, Band IX)
- **SOURCE:** limitative-note §2, §3.3, §4; register Band IX
- **CLAIM:** Gödel reading of the agent axis: zero-memory (structural context erasure that destroys the witness; the register row names the canonical instance by its upstream name, which stays upstream per GR-4) is the Φ_agent instance of Gödel's first theorem: a witness real yet underivable from within, intrinsic to a single system; destroying the witness is a structural act of separation. Axis assignment per the source's synthesis (§4): the Gödel reading loads on Φ_agent (witness destroyed, true yet underivable from within), disjoint from the Tarski reading of the existence leak on Φ_inference (C92, homed at E2-C14); the source's §3.3 argues the separation of the two readings. Register edges: C91 → C14, C91 → C86 (E1-C12), C91 → C17 (E1-C07). Band IX fence applies: every join in the source is structural framing (~80%), not a theorem-to-theorem reduction (~50%); ~60% prices the framing conjecture, and no reduction is claimed.
- **CITATIONS:** Gödel 1931 (Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I).
- **FEEDS:** WP-04 (limitative/related-work shelf only: §6 related-work status at most, per L065(d)), WP-16. Rerouted 2026-07-07 per L065(d): WP-07 removed; the WP-07 theory draft excluded this claim as not statable at TIER-A without an unclaimed reduction. The claim, its register confidence, and the Band IX fence are unchanged; only the flow changed.

## Contested items

None tagged CONTESTED. Two classification findings proposed to the ledger via A0 (this cycle serialises appends): the spec §16 labelling question (see E1-C39) and the stale local conjecture numbers C70 to C73 in the Bakhta integrity-gap note (see E1-C19). Neither is a canon-surface contradiction; both are hygiene items.

## Sweep record

- spec §10, §11, §14, §16, §26: swept 2026-07-02, A1 (this session), full sections including V6 additions (§10.5, §10.6, §11.4, §11.5, §14.6, §14.7).
- whitepaper-PT (swordsman_mage_whitepaper_v6_3.md, Promise-Theoretic Foundations chapter): swept 2026-07-02, A1. Gap-relevant claims extracted (autonomy axiom, superagent, irreducible promise). Assessment/trust-tier, RPP-as-assessment, and VRC-as-promise-bundle material noted and left to E3/E6 (their manifest homes).
- bakhta-notes (pvm-v6-bakhta-integrity-gap-convergence.md; pvm-v6-1-bakhta-half-life.md; NOTE_agt_scales_and_hide.md): swept 2026-07-02, A1, full. Local numbering C70 to C73 in the integrity-gap note maps to register C77 to C80 (Band VII).
- aletheia-lethe-note (research/aletheia-and-lethe.md): swept 2026-07-02, A1, full. Mathematical content extracted; mythological naming stays upstream (GR-4). FORGE copy not consulted (DOCS copy is the registered path's first listing and carries the 2026-06-09 reseat notice).
- tome-ii (cityofmages/tomes/tome-ii-the-lyapunov, Acts 1 to 7): swept 2026-07-02, A1, via frontmatter lineage and honesty labels plus Act text. Claims restated in mathematical vocabulary only; narrative phrasing stays upstream.
- ceremony-specs: DUAL_TERRITORY_CEREMONY_SPEC_v1.md, DUAL_AGENT_HARNESS_SPEC_v1.md, runecraft-protocol-spec-v1.md (DOCS specs/), ceremony-engine-spec-v1_1.md (MASTER ceremonies/), 03-bilateral-cloak-ceremony-spec.md (COM tomes/specs/): swept 2026-07-02, A1. The bilateral cloak ceremony yielded no E1 claims (its content is productive VRC formation, homed to E3/E6); recorded as swept.
- limitative-note (research/limitative-theorems-and-privacy-is-value.md): swept 2026-07-02, A1 (this session), full, closing ledger L034. Inclusion: C91 extracted as E1-C40 at register wording and confidence (register Band IX, head C96). Exclusions, with reasons: C90, C92, C93 are homed at E2 (E2-C13, E2-C14, E2-C15 per the E2 re-sweep); the §2.2 second-theorem row and §2.3 from-within reading of the ceiling are not extracted per ledger L035 (no register number covers the join; uncitable until the register process rules); the remaining §2.2 correspondence rows (arithmetisation, verification predicate, diagonal lemma against the ARCH-1 fixed point, terminal obstruction) carry note-local confidences but no register numbers and are not extracted per GR-1 (the terminal-obstruction content is registered as C73 and already homed at E1-C13, whose register row does not carry the limitative framing); the Φ_data limitative twin is an open seam with no number by G6 disposition, correctly not extracted.
- L044 re-issue pass (2026-07-02, A1, this session): E1-C02 tightened after the canon correction landed (chronicle 2026-07-02_canon-l044-spec-decomposition.md); "under budget constraints" made explicit as the capacity-deficit condition with quote-traces to the corrected spec §11.1 and §16 row. No other E1 claim carried the conflation: E1-C01 concerns the separation bound, not R_max; E1-C03 to E1-C05 checked, none conditions R_max < 1 on the preconditions alone.
- Maintenance touch (2026-07-07, A1, this session): E1-C40 FEEDS rerouted per L065(d). The WP-07 theory draft (rehydrations/academic/linear_cap_paper.md) excluded the C91 reading as not statable at TIER-A without an unclaimed reduction; FEEDS now names WP-04 (limitative/related-work shelf, §6 related-work status at most) and WP-16, with WP-07 removed. The claim text, register confidence (~60%), edges, and Band IX fence are untouched; the reroute changes where the claim flows, not what it says. Open citation note flagged to A0 (not edited, outside this card): E1-C09's CITATIONS line carries arXiv:2509.14284, the same citation annotated verification-in-flight at E2-C12 per L066(a); it takes the same resolution when the A4 verdict lands.
- Same-day resolution (2026-07-07, A1, per A0 micro-task): the A4 verdict landed (L070(2)): arXiv:2509.14284 VERIFIED (Patil, Stengel-Eskin & Bansal, preprint 2025-09-16). The E1-C09 flag above is discharged: CITATIONS enriched with the verified state, citable downstream, cite as preprint; claim text unchanged. E2-C12's in-flight annotation cleared in the same pass (see E2 sweep record). check_register_refs re-run PASS on both files.
- CTR-OBS-01 re-issue pass (2026-07-10, canon-batch seat, per L125): E1-C04 re-issued after the canon correction landed (spec §14.7 and §16 corrected same session; chronicle 2026-07-10_canon-additivity-batch.md). The exact-additivity wording ("holds exactly when ... Precondition 1") corrected to the subadditive truth: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M) under Precondition 1, at most the sum, equality iff additionally I(Y_S; Y_M) = 0 (CTR-OBS-01 verification, reviews/CTR-OBS-01_verification_and_inventory.md). No other E1 claim carried the exact wording: E1-C02's "license the additive capacity sum" and E1-C08's "additive bound Nε" are BOUND class per the inventory and stand; the deficit-condition "holds exactly when C_S + C_M < H(X)" in E1-C02 is the genuine definitional iff and is fenced out of the fix.
