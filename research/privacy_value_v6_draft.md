# Privacy Value Model V6 · Working Draft

**Status:** GROWING DRAFT under the V6 autopath. Parts accumulate here across Runs 1 to 5; Run 6 assembles the final `privacy_value_v6.md` from this file. Conjectures are cited by register number per `CONJECTURE_REGISTER_V6.md` (authoritative, G1-signed 2026-06-10).
**Assembly directive (G2, First Person, 2026-06-10):** the final document inherits the V5.4 formal-specification form and 24-section skeleton, to show the path is clear. The thesis carries two strands in this order: strand one, the gathering turn (V6 as the model opening outward in the second person, to the City of Mages and beyond, to fill the equation with data; V5 answered WHAT, V6 asks WHO); strand two, the emergent dynamical results of April to June 2026 (Parts I to V here) as V6's significant additions. The Parts below become new and revised sections woven into the V5.4 skeleton, not a replacement structure.
**Drafted:** Run 1 opened 2026-06-10
**Authors:** privacymage, with Claude Fable 5
**License:** CC BY-SA 4.0

---

# Part I · The Ceiling Moves

## I.1 Verdict

The reconstruction ceiling of V5.4 is correct and incomplete. Correct: under its stated conditions it is an instance of an established family of information-theoretic bounds, not an internal invention. Incomplete: it was stated as a static quantity, and 2026 has now produced two public demonstrations that the quantity moves. The numerator of the ceiling is a property of the adversary's models, and the adversary's models improve. The denominator is a property of the person, and the person does not change to match. V6 therefore restates the ceiling as a function of time, names its preconditions, grounds it externally, and reorganizes the model's existing temporal conjectures as one coherent thread: the countermeasure (trajectory dynamics), the taxonomy (aging categories), and the planning bound (the Behavioural Mosca).

## I.2 The V5.4 ceiling, restated with its preconditions

V5.4 §11.1 states, with the label Proven:

> R_max = (C_S + C_M) / H(X) < 1. Perfect reconstruction of the First Person's state is impossible.

V6 carries the result forward with the label **Proven, conditional regime**, and states the conditions that were implicit:

**Precondition 1 (non-collusion / channel independence).** The capacities C_S and C_M may be summed only if the two observation channels are conditionally independent given the First Person and are not combined by a single adversary beyond the stated capacities. Formally, the regime assumes I(Y_S; Y_M | X) = 0 and that no third channel carries the inter-agent residue. The wiretap literature shows exactly this assumption is what fails when observers combine: Csiszár and Körner (1978) and the colluding-wiretapper extensions. The empirical multi-agent literature now measures the failure: AgentLeak (El Yagoubi, Badu-Marfo, Al Mallah, arXiv:2602.11510) finds that multi-agent configurations reduce per-channel output leakage (27.2% versus 43.2% single-agent) while unmonitored inter-agent channels raise total system exposure to 68.9%. Part II treats this in full. Here it is the boundary condition: **the ceiling holds in the regime the Amnesia Protocol is designed to enforce, and only there.**

**Precondition 2 (fixed adversary model).** C_S and C_M are channel capacities evaluated against a stated adversary class: its compute, its inference models, its correlation methods. The bound says nothing about a later, stronger class. This precondition is the door V6 walks through in §I.3.

**External grounding.** Within the conditional regime the ceiling is an instance of an established family, and V6 cites the family rather than internal papers:

- Wyner (1975), the wire-tap channel: the separation bound I(S; M | FP) < ε* of V5.4 §10.1 is a restatement of weak-secrecy equivocation.
- Fano (1961); Cover and Thomas: the error floor P_e ≥ 1 − R_max of V5.4 §11.2 is the standard source-coding converse.
- Leung-Yan-Cheong and Hellman (1978): secrecy capacity as a difference of channel capacities in the Gaussian wiretap channel, the closest classical analogue of capacity-budgeted reconstruction.
- The Bayes-capacity bound of quantitative information flow (the Miracle Theorem): a tight upper bound on leakage to any reconstruction adversary, which upper-bounds what any decoder extracts per observation.
- Geiger and Kubin, relative information loss: a Fano-grounded lower bound on reconstruction error under lossy observation.

This move costs nothing and buys defensibility: the claim is no longer "proven in our internal paper" but "an instance of a family of bounds the field already accepts, under named preconditions."

## I.3 The time-dependent ceiling R(t)

**Definition (V6).** Let H(X) be the source entropy of the First Person's private state over the horizon of interest. Let C_S(t) and C_M(t) be the effective capacities of the two observation channels evaluated against the strongest adversary class available at time t. The reconstruction ceiling is

> R(t) = (C_S(t) + C_M(t)) / H(X)

and the V5.4 guarantee becomes a **shelf life**:

> t* = sup { t : R(t) < 1 }

**The mechanism is the decoder, not the data.** Observations already emitted do not change after emission. What changes is what can be extracted from them: better inference models raise the effective capacity of a channel whose physical recordings are fixed. H(X) is fixed by the person. Therefore R(t) is non-decreasing under capability growth, and a separation architecture adequate at t₀ can be inadequate at T > t₀ with no new disclosure by the subject. This is the reconstruct-later threat (C48; City-register restatement C60) given its exact mechanism: the archive sits still while the ceiling rises to meet it.

**Conjecture C82 (The Moving Ceiling).** Registered this run, taking the next free number per the G1-signed register. Statement: frontier AI capability growth raises the effective adversary capacities C_S(t) + C_M(t) against fixed behavioural archives without raising H(X), so R(t) drifts upward and every static reconstruction guarantee has a finite shelf life t*; the drift rate is coupled to frontier model capability, not to any action of the subject. Confidence: ~65% (estimator: privacymage with Claude Fable 5, 2026-06-10; mechanism strongly evidenced at n=2 public instances, functional form of the drift unparameterized).

## I.4 The two instances of 2026

Both occurred within nine days of this draft, and they are the strongest convergence-within-corpus material the model has ever had: the same structure, two substrates.

**Instance 1: Zcash Orchard.** A soundness flaw in `halo2_gadgets` (`ecc::chip::mul`, an under-constrained variable-base scalar multiplication arising from `assign_advice()` where the stricter `copy_advice()` was required) was present from Orchard's launch in May 2022. It was findable for roughly four years. Anthropic released Claude Opus 4.8 on 2026-05-28; Taylor Hornby found the flaw the next day, 2026-05-29, and with the model's help wrote a complete exploit generating unlimited, undetectable counterfeit ZEC in a regtest environment. ZEC fell roughly 27 to 33% in 24 hours after disclosure; the issue was fixed by the NU6.2 hard fork at block 3,364,600 on 2026-06-03. Reading in R(t) terms: the circuit's H(X) never changed; the decoder improved overnight; four findable years collapsed into one found day.

**Instance 2: the Schrottenloher rediscovery.** Google Quantum AI withheld a roughly 10x Shor optimization for secp256k1, publishing only a zero-knowledge proof that the result existed. On 2026-06-02 André Schrottenloher published an independent rediscovery (Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms, eprint 2026/1128), roughly two months after the attestation. Reading in R(t) terms: the attestation of feasibility discounted the search space for every reader; the existence proof leaked an upper bound on difficulty (C81, treated fully in Part III); the time between findable and found collapsed again, this time with the searching done partly by the attestation itself.

One structure, twice: **AI and public attestation each raise the capability term while the source term sits still.** The first instance moves C(t) by improving the decoder. The second moves it by pricing the search. Neither touched the protected object.

## I.5 The temporal thread, unified

V6 does not invent its temporal machinery this week. The corpus has been accumulating it since April; what was missing was the spine. R(t) is the spine.

**The countermeasure: trajectory dynamics (C18 to C21).** If the sovereignty path π(t) exhibits strange-attractor dynamics with Lyapunov exponent λ > 0 (C18, 25%), then an adversary's best-fit reconstruction π'(t) diverges as |δ₀|·e^(λt): the defense widens with walk time through the trajectory's own dynamics. V6's architectural claim is a race condition: choose the substrate so that trajectory divergence outruns capability drift. In symbols, the effective ceiling an adversary faces on trajectory data is R(t) discounted by the divergence term, and the design goal is that the discount grows faster than the drift. This is a conjecture chain (C18 through C21 sit at 10 to 30%), and V6 states it as the candidate countermeasure, not an established one. The empirical key remains the unmeasured λ on real forge trajectory data.

**The taxonomy: ages progressively (C47, ~50%).** Bakhta's three aging categories (gracefully, bounded, brittle) cover substrates whose security holds or decays. A substrate where the defense widens with time through its own dynamics is a fourth category, ages progressively, and it is the category the dual-agent architecture should be engineered to inhabit. R(t) gives the taxonomy its axis: a substrate's aging category is the sign and shape of its effective ceiling's time derivative.

**The trust-edge expression: half-life (C30 to C33).** The same temporal logic one layer up: trust edges decay from inscription (C30, 60%) unless renewed; productive edges outlast transactional ones (C32, 50%; alias C46); half-lives compose across the three axes (C33, 45%). In V6 the half-life family and the moving ceiling are one discipline read at two layers: everything in the architecture ages, and the engineering question is always which direction.

**The planning bound: the Behavioural Mosca (C49, ~70%; City-register restatement C61).** X_b + Y_b > Z_b, where X_b is migration time to an unreconstructable substrate, Y_b is the verification horizon of the behavioural evidence, and Z_b is the adversary capability maturity time. V6 closes the loop: **Z_b is exactly the shelf life t\* of §I.3.** The two 2026 instances are downward revisions of Z_b observed in public (the Schrottenloher note called the first of these the falling Z). The inequality binds harder this month than it did in April, and that sentence will remain true of most future months. The harvest-now-decrypt-later economics literature (Blanco-Romero et al., arXiv:2603.01091) supplies the cost model: storage and future workload as the two axes, which is the X-side discipline C60 already gestures at.

**The substrate witnesses: Horizon District (C67, C68).** The City register carries the cryptographic-substrate expression: the cryptographic Mosca (C67) and resource-estimation-as-durability-signal with the e^(−λt) reading (C68). The formal document and the City said the same thing in the same week without coordination, which is the convergence discipline working as designed.

## I.6 The delta from V5.4

| Quantity | V5.4 | V6 |
|---|---|---|
| Reconstruction ceiling | R_max static, labeled Proven | R(t) monotone under capability growth; Proven in the conditional regime; shelf life t* defined |
| Preconditions | implicit | named: non-collusion (Precondition 1), fixed adversary class (Precondition 2) |
| Proof provenance | internal papers (v4.2/v4.3) | external family: Wyner 1975, Fano, Leung-Yan-Cheong and Hellman 1978, Bayes-capacity, Geiger and Kubin |
| Adversary | single fixed class | capability-indexed family; drift coupled to frontier models (C82, ~65%) |
| Temporal machinery | absent from the spec | one thread: countermeasure C18 to C21, taxonomy C47, half-life C30 to C33, planning bound C49 with Z_b = t* |
| Worked instances | none | Orchard (2026-05-29 to 2026-06-03) and Schrottenloher (eprint 2026/1128, 2026-06-02) |

## I.7 Honest limits of Part I

1. λ > 0 (C18) remains unmeasured; the countermeasure is a conjecture chain at 10 to 30%, and without it V6 has named the threat's time-dependence without a proven time-dependent defense.
2. C82 has no functional form: the drift of C_S(t) + C_M(t) is asserted monotone under capability growth but not parameterized; n=2 public instances is evidence of mechanism, not of rate.
3. The shelf life t* is defined, not estimated. Estimating it for any real archive requires the capacity-growth model Part I does not have.
4. Precondition 1 is stated, not verified for any deployed system; Part II owns that problem.
5. Both 2026 instances are single events read through the model's lens; alternative readings (ordinary fuzzing progress, ordinary cryptanalytic progress) are not excluded, only rendered less economical.

---

# Part II · The Sum Leaks More Than Its Parts

## II.1 Verdict

The strongest external threat to the model is now its strongest external citation. Two independent 2025 to 2026 results prove that leakage compounds under sequential multi-agent composition when separation is enforced by policy, and one measurement study confirms it empirically at scale. Read carelessly, this falsifies the model's additive-leakage claim. Read correctly, it is the first quantitative statement of the model's central architectural thesis: the gap between policy separation and amnesia separation is the gap between exponential and linear leakage in the depth of the agent chain. Part II performs that absorption, registers the quantitative conjecture, and pays the honesty bill on C7.

## II.2 The compounding results, stated exactly

**The bound.** Asif and Amiri (Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems, Rensselaer Polytechnic Institute, arXiv:2603.05520, 2026-03-09) prove a Cumulative Leakage Bound (their Theorem 4.1): under sequential composition of N agents with per-agent constraint I(O_i; S_i) ≤ ε_i, global leakage satisfies

> I(O_N; S_1, ..., S_N) ≤ Σ_i 2^(N−i) ε_i

which in the uniform case is (2^N − 1)ε. The proof runs on the chain rule for mutual information and the conditional data processing inequality. Their empirical confirmation: on MedQA with LLaMA-7B, average mutual information rises from 0.49 at two agents to 1.05 at five, consistent with the compounding the theorem predicts. Patil, Stengel-Eskin and Bansal (The Sum Leaks More Than Its Parts, arXiv:2509.14284) reach the same conclusion through composition analysis.

**The measurement.** AgentLeak (El Yagoubi, Badu-Marfo and Al Mallah, Polytechnique Montréal, arXiv:2602.11510; 1,000 scenarios, 4,979 traces across GPT-4o, GPT-4o-mini, Claude 3.5 Sonnet, Mistral Large, Llama 3.3 70B) measures the failure in deployed-style systems: multi-agent configurations reduce per-channel output leakage to 27.2% versus 43.2% single-agent, while unmonitored inter-agent channels leak at 68.8%, raising total system exposure to 68.9%. Output-only audits miss 41.7% of violations.

**What this does and does not contradict.** V5.4 §16 asserts additive leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), at 95% confidence. The compounding bound does not contradict the additive claim in the model's own regime: additivity holds exactly when the channels are conditionally independent given X and nothing carries the inter-agent residue, which is Precondition 1 of Part I. The compounding bound describes what happens OUTSIDE that regime: when agents pass outputs to one another (sequential composition), each hop conditions the next, the chain rule compounds, and the per-agent budgets multiply out to (2^N − 1)ε. The two results are one theorem family on two sides of one architectural line. The line is whether the inter-agent channel exists.

## II.3 C17 made quantitative, and conjecture C83

V5.4's C17 (amnesia-enforced separation is tighter than policy-enforced, 60%) was qualitative. The compounding literature supplies the missing arithmetic.

Policy separation leaves the inter-agent channel in place and asks it to behave. The sequential bound then applies: worst-case leakage (2^N − 1)ε in chain depth N. Amnesia separation removes the channel structurally: each agent's budget stands alone, conditioning cannot accumulate, and total leakage is bounded by the sum of independent budgets, Nε. The gap between the two regimes is the gap between exponential and linear in N, and at N = 2 (the dual-agent case) it is already the difference between 3ε and 2ε; at N = 5 it is 31ε versus 5ε.

**Conjecture C83 (Compositional Leakage Amplification).** Registered this run. Statement: under policy-only separation, behavioural leakage compounds toward the (2^N − 1)ε sequential bound with agent-chain depth N, whereas amnesia-enforced separation, by breaking the Markov chain between agents, caps total leakage at the additive bound Nε; the policy-to-amnesia gap is therefore exponential-to-linear in N. Confidence: ~55% (estimator: privacymage with Claude Fable 5, 2026-06-10; the bound is proven, the conjecture is that real amnesia implementations achieve the break, which is an engineering claim about the Amnesia Protocol, not a theorem). Edge drawn: C7 → C83 → C17. AgentLeak's 68.9% total exposure with 68.8% inter-agent leakage is the field measuring exactly the channel the Amnesia Protocol exists to delete.

**The reframe earned.** The model has argued since V5.3 that architecture beats policy. That argument now has the adversary's own units: policy separation does not merely leak somewhat more, it leaks with a different asymptotic shape. AgentLeak's headline (separation helps per-channel, total exposure rises anyway) is the model's thesis stated empirically by an independent team with no knowledge of the model.

## II.4 The honesty bill on C7

C7 (three-axis separation is multiplicative, 30%) is load-bearing for the entire Φ_v5 gating form and remains the corpus's most exposed conjecture. V6 names it the **falsification frontier** and states the three boundary cases the multiplicative form does not yet address:

1. **Partial collapse.** One axis at 0.1 rather than 0. The multiplicative form predicts near-total gating; an additive-with-floor or min() form predicts graceful degradation. No measurement distinguishes them yet. Falsification test (inherited from the 2026-06 review and now register-bound): any real deployment exhibiting partial single-axis collapse without proportionate collapse of reconstruction resistance falsifies the multiplicative form.
2. **Axis correlation under composition.** The compounding results of §II.2 imply the axes can become positively correlated under sequential composition: conditioning that flows through an inter-agent channel couples what the model treats as orthogonal. The determinant form det(Σ) partially captures correlation; the scalar product Φ_agent · Φ_data · Φ_inference does not. V6 carries the scalar form as the stated model and flags the determinant form as the candidate correction.
3. **Time dependence.** The axes are treated as static; Part I made the ceiling time-dependent, and the axes cannot be less time-dependent than the ceiling they gate. The differential form dV/dt = ∇·J + S − D, gestured at since the v4 essay, remains unincorporated. Its natural home is the Lorenz thread (C18 to C21), and it stays a named open seam in V6.

These three cases enter the breaking-conditions register of the assembled document (the V5.4 §18 successor) verbatim.

## II.5 The field as plurality

The multi-agent privacy field arrived at separation-of-duties independently and repeatedly in 2025 to 2026: MAGPIE (arXiv:2506.20737, multi-agent contextual privacy evaluation), the 1-2-3 Check multi-agent reasoning line grounded in Nissenbaum's contextual integrity, PrivAct (arXiv:2602.13840, internalizing contextual privacy via preference training), and the maker-checker and supervisor-worker patterns across the agent-orchestration literature. This is plurality, not precedence: the Swordsman-Mage pair is one named instance of a structure many teams reached. The model's distinctive claim is narrower and sharper than the pattern: none of these systems enforce separation architecturally. All use prompt-level or training-level controls. The model predicts they fail under composition, and §II.2's measurements are consistent with that prediction at 68.9% total exposure.

## II.6 Honest limits of Part II

1. C83's amnesia side is an engineering claim: that the Amnesia Protocol's structural forgetting actually breaks the Markov chain in deployed form. No deployed measurement exists. The bound it would achieve is proven; the achieving is not.
2. The additive claim of V5.4 §16 retains its 95% label only inside Precondition 1. V6 lowers nothing but scopes everything.
3. The compounding bound is worst-case; real sequential systems may sit well under it. The argument's force is asymptotic shape, not measured constants, except where AgentLeak supplies constants.
4. The plurality citations corroborate the pattern, not the model's gating algebra. No external team has tested Φ multiplicativity, which is why C7 stays at 30% and keeps its frontier label.

---

# Part III · The Proof That Whispered

## III.1 Verdict

The Existence-Leak conjecture is the corpus's most promotable claim and this Part promotes it: from candidate (~60%, registered C81 at Run 0) to ~70%, on the strength of one worked public instance and one published impossibility theorem that together bracket the claim from below and above. It also draws the edge that did not exist before this week: existence-leak discounts the Behavioural Mosca planning horizon, which couples Part III to Part I's shelf life and makes the law operational rather than ornamental. The Stage-2 requirement is stated plainly: n=1, and the confidence stops at 70% until a second independent instance arrives.

## III.2 The law, stated

**C81 (Existence-Leak), promoted to ~70% this run.** A zero-knowledge proof of an attack's feasibility leaks an upper bound on the attack's reconstruction difficulty: I(feasibility; method) > 0 even under perfect method-hiding. Publishing that a thing can be done prices the search for how.

**The floor (impossibility).** Garg, Jain and Sahai proved that leakage-resilient zero-knowledge with leakage parameter λ < 1 is impossible. There is no construction that drives method-leakage to zero while attesting feasibility. This is the formal backbone: the law is not an empirical accident, it is the impossible-to-avoid residue of attestation itself.

**The mechanism (transferability).** Fiat-Shamir NIZK proofs are publicly transferable: they convey "the prover knows the secret" to every reader forever (Dinh, Deniable Knowledge). A feasibility attestation is therefore a broadcast, not a disclosure event with an audience boundary. Every capable searcher receives the same discount on the same search space at the same time.

**The instance (worked, public, dated).** Google Quantum AI withheld a roughly 10x Shor optimization for secp256k1 and published only a zero-knowledge proof that the optimization existed. On 2026-06-02, André Schrottenloher published an independent rediscovery (eprint 2026/1128), roughly two months after the attestation. The proof of feasibility collapsed the search: knowing the target was reachable, and roughly how far away, a capable searcher walked to it. I(feasibility; method) > 0, measured in the wild, with a time constant of weeks.

**Bracket complete.** The impossibility theorem says the leak cannot be zero. The instance says the leak is operationally large. The law lives between the bookends, and 70% is the defensible reading of n=1 with a proven floor.

## III.3 The Mosca coupling, and conjecture C84

The Behavioural Mosca inequality (C49, ~70%; City restatement C61) plans against Z_b, the adversary capability maturity time, which Part I identified with the shelf life t* of R(t) < 1. Existence-leak shortens it.

**Conjecture C84 (Existence-Leak Discount).** Registered this run. Statement: whenever feasibility of a capability is publicly attested (ZK proof, demonstrated exploit, benchmark claim, or credible existence announcement), the planning horizon Z_b for every archive threatened by that capability must be discounted: Z_b' = Z_b − D(a), where the discount D(a) grows with the attestation's specificity and the searcher population's capability. Equivalently, in an AI-accelerated discovery regime the migration deadline X_b + Y_b < Z_b' tightens on every public attestation, independent of any actual attack occurring. Confidence: ~50% (estimator: privacymage with Claude Fable 5, 2026-06-10; the direction is forced by C81, the functional form of D(a) is unparameterized at n=1). Edges drawn: C81 → C84 → C49, and C84 → C82 (attestations are one of the drift mechanisms of the moving ceiling; the Schrottenloher instance is simultaneously an instance of both).

**The cost model underneath.** The harvest-now-decrypt-later economics literature (Blanco-Romero et al., arXiv:2603.01091) reframes HNDL as a two-axis cost problem: storage cost against future workload cost. The Cloud Security Alliance (2026-05-18) frames HNDL as an ongoing operation against AI infrastructure. This supplies C49 and C61 the cost backbone they previously lacked: an adversary's decision to harvest is an option purchase, the attestation of feasibility raises the option's value, and C84 is the repricing event. Behavioural archives are harvested under exactly this calculus, which is why the inequality binds for behavioural data even though no behavioural "Shor moment" has been attested yet.

## III.4 What the law is not

Three scope fences, to keep the promotion honest:

1. **Not all ZK use leaks meaningfully.** The law concerns capability claims: attestations whose subject is "X can be done." Service claims (proving a statement about a transaction, an identity attribute, a state transition) attest instances, not capabilities; their existence-leak is the trivial fact that the proof system works, already public. The dual-agent architecture's own ZK usage is service-shaped, which is why the law indicts adversary attestation dynamics without indicting the model's own proofs. The distinction is load-bearing and stated here once.
2. **Not a deniability result.** The law does not say provers should hide that they can prove. It says planners must price the attestations of others into Z_b. It is read from the defender's chair.
3. **Not yet a behavioural result.** Both bookends are cryptographic. The transfer to behavioural capability claims (a published model card claiming re-identification performance, a benchmark on reconstruction from sparse traces) is the conjectured part, and it is exactly what a second instance should test.

## III.5 Stage 2, stated

C81 stops at 70% and C84 at 50% until a second independent instance arrives. What would count: a capability claim outside cryptography whose public attestation (not whose method publication) preceded independent rediscovery on a timescale clearly shorter than the prior search baseline. A synthetic-data reconstruction benchmark followed by independent replication against real traces would be the cleanest behavioural instance. What would not count: rediscovery following method publication (that is ordinary diffusion), or coincident discovery without an attestation in between (that is ordinary parallel progress).

## III.6 Honest limits of Part III

1. n=1. The promotion to 70% leans on the impossibility floor; without Garg-Jain-Sahai the instance alone would justify no more than the prior ~60%.
2. The Schrottenloher reading has an alternative: ordinary cryptanalytic progress that would have arrived regardless. The two-month interval after a multi-year quiet period renders this less economical, not impossible. Part I §I.7 carries the same caveat for the same event.
3. D(a) has no functional form and no units. C84 is a planning directive (discount on attestation) before it is a quantity.
4. The capability-versus-service distinction (§III.4) is asserted from the model's architecture, not derived; a critic may find capability-shaped residue in service proofs. The Fiat-Shamir transferability mechanism applies to both, which is why the fence is a scope statement and not a theorem.

---

# Part IV · The Bridge and the Forgetting

## IV.1 Verdict

The lattice and the axes finally meet in the formal document. Both 2026-06 reviews named the same seam: ARCH-1 is canonical narrative and absent from the formal lineage, and the conjecture that bridges the three-axis model to the lattice's triadic coordinates lived only in a narrative repo, where, as the addendum put it, it does not exist for a reviewer. Part IV promotes the bridge into the core register (C85), seats ARCH-1 and its operational layer in the formal lineage with their G1-confirmed numbers, and registers the obstruction-theoretic reading of amnesia (C86) that makes Selene's Proof a precise statement instead of a strong sentence.

## IV.2 The bridge: conjecture C85

**C85 (Triadic-Constraint Homology, promoted from CM-C47).** Registered this run at ~40%, carrying the City-register confidence unchanged; promotion changes residence, not evidence. Statement: the model's three sovereignty axes Φ_agent(Σ) · Φ_data(Δ) · Φ_inference(Γ) and the lattice's triadic coordinates (Datum · Stratum · Spectrum, the PRISM reading of Z/(2⁶)Z) are instances of one triadic primitive, such that axis values are computable from lattice position and lattice traversals induce axis dynamics.

**The candidate map, stated so it can fail.** The six lattice dimensions group in pairs onto the axes: Protection and Delegation instantiate the agent axis Σ (who holds the boundary and who acts); Memory and Value instantiate the data axis Δ (what persists and what it is worth); Connection and Computation instantiate the inference axis Γ (what can be joined and what can be derived). Under this map, stratum (the popcount layer, 0 to 6) measures total sovereignty activation; the datum (vertex identity) fixes the axis signature; the spectrum (the walk's edge structure) carries the dynamics. The map predicts: bnot-pairs (which complement all six bits) inverr all three axes simultaneously, which is consistent with the Aletheia/Lethe reading (V38 transmits, V25 holds; 38 XOR 25 = 63, full activation); and stratum-3 vertices (balanced, 20 of 64) are the only seats where no axis dominates, which is testable against the City's stratum-3 peerage observations.

**The fixpoint relation, stated as the open seam.** ARCH-1 is Σ := μS.(β ∨ Ω(S,S)) with activation ρ. The candidate correspondence to the conditional-independence structure: β, the base case the recursion cannot dissolve, corresponds to the First Person's irreducible kernel, the entropy that conditions the separation bound I(S; M | FP) < ε*; the two arguments of Ω(S, S) correspond to the two agents as self-compositions of the sovereign schema; and conditional independence is the requirement that the two recursion branches share only β. Under this reading, **the gap is β**: what the agents have in common is exactly and only the First Person, and the separation bound is the information-theoretic shadow of the fixpoint's base case. This paragraph is the seam, named: it is a structural correspondence with no proof obligation discharged, offered at the same epistemic grade as C26 (40%), on which it leans. What a proof requires: a formal statement of Ω for the dual-agent instantiation, and a derivation that I(branch₁; branch₂ | β) = 0 follows from the schema rather than being assumed beside it.

**Residence note.** CM-C47 remains in the City register as an alias pointing here; City prose keeps its number with one erratum at Wave R. The bridge now exists for a reviewer.

## IV.3 The operational layer: ARCH-1R/T seated (C72 to C76)

The reachability extension enters the formal lineage with its G1-confirmed numbers. What it adds to the model, in one paragraph: ARCH-1 says what the sovereign schema IS; R/T says what it can REACH and what blocks it. The ternary classification τ: T → {+, 0, −} distinguishes latent (0, not yet activated) from obstructed (−, structurally blocked), a distinction binary reachability cannot express (C75: the hard-versus-soft dependency split is this distinction lifted to cascade propagation). The traversal orbit T = orbit(ρ, G) makes ρ one operator at two scopes (C72, ~35%): the activation of the schema and the walk of the lattice are the same move read locally and globally. C74 (~25%) holds the speculative end: latency may have an algebraic signature on the lattice itself, an open-walk state of the neg ⊕ bnot composition rather than a runtime annotation. C76 (~30%) carries the relational claim: classifying rel(a, b) rather than entities is strictly more expressive for sovereignty, because authorization obstruction attaches to the relation independent of either relatum.

The model-facing payoff is C73 (~50%), the highest-confidence claim of the family: **terminal obstruction, the structural loss of β, is a primitive obstruction class distinct from path obstruction, and the Amnesia Protocol is its canonical instance.** Forgetting is not a blocked path to the memory; it is the absence of any path because the base case is gone. This is the reachability statement of amnesia, and §IV.4 gives it the cohomological upgrade.

## IV.4 The forgetting: conjecture C86

V5.4 §14.1 defines structural amnesia as: no sequence of permitted operations can reconstruct O from the agent's current state. That is a reachability statement, quantified over paths. It leaves open the stronger question a reviewer should ask: even if no single path reconstructs O, can the system's local views be GLUED into a global witness that recovers it?

**C86 (Obstruction-Theoretic Amnesia).** Registered this run at ~30%. Statement: structural (Grade-2) forgetting is the condition that the obstruction class to gluing the agents' local views into a global witness of O is non-vanishing; Grade-1 forgetting (hiding, encryption, access control) is the condition that the obstruction class vanishes and only the gluing data is withheld. Equivalently: after Grade-2 amnesia there exists no global section over the cover formed by the agents' views that restricts to each view and recovers O; after Grade-1 there does, and recovering it is a key-management problem, not a mathematical impossibility.

Three notes keep the registration honest:

1. **The neighborhood is right, the machinery is unbuilt.** The natural formal home is sheaf-theoretic: views as sections over a cover, reconstruction as the existence of a global section, the obstruction as a Čech cohomology class. The corpus's existing Yoneda material (an object is determined by its morphisms) is adjacent: an O whose morphism-traces have been structurally severed is not determined. None of this is constructed for the dual-agent instantiation yet; ~30% prices a framing, not a theorem.
2. **The relation to C73 is division of labor, not duplication.** C73 places amnesia in R/T's obstruction taxonomy (WHERE it sits: terminal, not path). C86 says WHAT forgetting is mathematically (a non-vanishing gluing obstruction). Cross-linked in the register; registered separately because they fail separately: a counterexample to the taxonomy placement would not touch the cohomological claim, and vice versa.
3. **What it buys if it holds.** Selene's Proof, "the witness is genuinely gone, not hidden," becomes: the obstruction class is non-zero, and no future key, subpoena, or capability growth changes a cohomological fact. This is the one defense in the model that C82's moving ceiling cannot erode, because there is no archive left for the better decoder to read. Amnesia is the only term in the equation whose security is independent of t. That sentence, if C86 survives, is the strongest sentence in the model.

## IV.5 The Amnesia Protocol section, upgraded

The assembled document revises the V5.4 §14 inheritance in three moves: the §14.1 definition gains the obstruction formulation beside the reachability one (stated as conjectural, C86); the Grade-1/Grade-2 distinction gains its formal criterion (vanishing versus non-vanishing class); and the protocol's verification story gains its falsification test: produce any composition of agent views, under any future capability, that recovers a Grade-2-forgotten O, and C86 is dead. The protocol's engineering (what is deleted, when, attested how) is unchanged from V5.4; Part IV changes what the deletion means.

## IV.6 Honest limits of Part IV

1. C85's pair-to-axis map is one candidate among several possible groupings of six dimensions into three pairs (there are 15); the stated map is motivated, not derived, and the stratum-3 and bnot-pair predictions are its first two tests.
2. The fixpoint-to-independence correspondence (the gap is β) discharges no proof obligation; it is registered inside C85's confidence, not separately.
3. C86 imports cohomological language without constructing the site, the cover, or the coefficient structure for the dual-agent case. A skeptic may fairly call it a metaphor with a research program attached; the register prices that at 30%.
4. ARCH-1R/T's own program (the toy graph simulator, the obstruction-transformation laws, the σ and cost layers) remains undone; seating the family in the lineage does not advance it.
5. Nothing in Part IV measures anything. It is the structural Part; its empirical content is two predictions under C85 and one falsification test under C86.

---

# Part V · The Key, the Knot, and the Star

## V.1 Verdict

The City Key arc of 2026-05-27/28 is the most formally interesting thing in the corpus that was not yet in the formal lineage, and Part V brings it in on three fronts: the trust recursion is named as a folding scheme (C87), the presence economy receives the adversary-regime statement the model's own thesis demands (declared at Gate G3 in the First Person's words; the recommended regime is stated here), and the geometry pays its honesty bill (the stella octangula carries no golden ratio, and two genuinely new geometric conjectures are registered in exchange, C88 and C89). The City Key's own status claim, C66, gains thirty years of prior art.

## V.2 The trust recursion is a folding scheme: conjecture C87

The Three Keys chronicle describes the loop precisely: each domain's proof composes on the prior, the output of the loop is an input to the loop, no single domain suffices, and the fixed point is V63. Structurally, this is incrementally verifiable computation, and the mapping is almost mechanical:

- the City Key ≅ the folded instance, the accumulator
- each domain's trust task ≅ a step circuit
- Charge (the trace folded into 🪢) ≅ the folding step
- carrying the deepened key back to the first domain ≅ the IVC recursion
- V63 as fixed point ≅ the invariant the accumulated proof attests

**C87 (The Key Accumulates).** Registered this run at ~50%. Statement: the City Key trust recursion admits an IVC realization in which the Key is a succinct accumulator of domain proofs, verifiable in time independent of loop count. The literature home is exactly the folding line: Nova; HyperNova (CRYPTO 2024, with the zero-knowledge completion and the NovaBlindFold update of 2026-02-20); MicroNova (IEEE S&P 2025, efficient on-chain verification); and LatticeFold (Boneh and Chen, ASIACRYPT 2025), which matters twice, because it is both a folding advance and plausibly post-quantum, tying the Key directly to the Behavioural Mosca thread of Parts I and III: if the Key's proving substrate is lattice-based, the recursion's attestations age gracefully under the very horizon C67 and C49 plan against. Honest grade carried from the source review: this is an architectural claim, not a proof; the deviation hash chain and the Key wire format have no circuit realization yet, and ~50% prices the mapping, not an implementation.

## V.3 The presence economy: regime statement

Charge earns 🪢 from self-attested, client-side traces; Stake commits it to vertices. As local color this is charming and safe. But the chronicles frame presence as a proof layer in the trust recursion, and the moment 🪢 influences any admission, coalition, or attestation decision, three attacks are live: **replay** (re-importing traces), **simulation** (a headless browser walking the manifold at machine speed), and **sybil farming** (presence accrued across disposable keys). C42 (stake economics generate Sybil resistance, ~50%) is the same gap seen from the other side. The model's own thesis, architecture over policy, forbids leaving this to good faith.

The regime ladder, ascending: (1) 🪢 scoped as non-transferable, non-attesting local color; (2) witness co-signing at gates, presence countersigned by a domain the bearer passed through; (3) elapsed-time proofs (VDF-style) rate-limiting accrual to wall clock. **The recommended V6 regime is (1), stated publicly, with (2) and (3) as the named upgrade path**: it is cheap, honest, and true to the current implementation (an integer in localStorage). The declaration itself is the First Person's, made at Gate G3 and inserted here verbatim at assembly:

> **Regime declaration (G3, First Person, 2026-06-10, regime 1 confirmed; wording house-voice, rewrite open at 📖 RB-04):** 🪢 presence mana is non-transferable, non-attesting local color. It is earned by walking, carried on the bearer's own Key, and spends nothing but meaning. It is not proof, not stake-weight, not an input to any admission, coalition, or attestation decision, and no surface in the suite may say otherwise. When presence is ever asked to attest, the economy moves up the ladder first: witness co-signing at gates, then elapsed-time proofs. The architecture earns the claim before the prose makes it.

Until and unless the regime moves up the ladder, no surface in the suite may describe 🪢 as proof, stake-weight, or attestation input; Wave R carries the one-line footer to /star and /achievements.

## V.4 The geometry, honestly

Tome VIII Act 3 seats the stella octangula as the manifold's figure: the Swordsman tetrahedron (neg, protect) crossed with the Mage tetrahedron (bnot, project). Three geometric facts, two of them new edges and one of them a correction:

**The correction first.** The classical stella octangula contains no golden ratio. Its characteristic ratios are halvings (the tetrahedra meet at edge midpoints) and its volume relations are rational: each tetrahedron has volume 1/3 of the bounding cube, the octahedral core has volume 1/6, the compound 5/12. Kepler's triangle has φ; Kepler's star does not. The act's reference to C1 (φ as optimal protect:project ratio) must therefore read as **resonance, not derivation**: φ enters the corpus from the lattice's disclosure ratios (C54: 38/63 = 0.60317 against 1/φ = 0.61803, gap 2.4%) and from the temporal dynamics where C1 originally lived, never from the named solid. One paragraph in Tome VIII and blog post 18 carries this at Wave R. Do not let the beauty of the figure smuggle the number.

**C88 (The Parity Cube).** Registered this run at ~30%. The compound's convex hull is the cube, and the two tetrahedra are exactly the two ways to inscribe a regular tetrahedron in it: the even and odd parity classes of the cube's 8 vertices, {0,1}³ split by popcount parity. Statement: this parity split is the canonical seat of the neg/bnot duality at the 3-bit scale, and {0,1}⁶ = {0,1}³ × {0,1}³ gives each agent a cube, making the stella octangula the 3-bit shadow of the full 64-vertex architecture, with the C85 pair map (Σ, Δ, Γ as the three bit-pairs) as the candidate factoring. Whether the decomposition is canonical or coincidental is one working session's question; ~30% prices it before that session.

**C89 (The Octahedral Gap).** Registered this run at ~30%. The intersection of the two tetrahedra is the octahedron at the core: the region both agents bound and neither owns. Statement: the octahedral core is the geometric locus of the conditional-independence bound, the volume spanned by neither C_S nor C_M alone, and "the gap is the proof" thereby gains a shape with measurable volume (1/6 of the bounding cube, exactly half of either agent's tetrahedron). Read with Part IV's seam (the gap is β), the chain is: the base case of the recursion, the conditioning variable of the separation bound, and the octahedron at the heart of the star are three readings of one thing. That chain is the conjecture; the volume arithmetic is just true.

## V.5 The Key is a reading: C66 revised

The City Key's status claim ("a portable projection of lattice-standing that grants nothing it does not already describe," C66, ~45%) is the credential-versus-capability distinction from the object-capability lineage: SPKI/SDSI, the ocap discipline, designation without authority. Naming that lineage does two things: it raises C66's defensibility (revision to ~55% registered this run, City register owner confirms at Wave R), and it places the Key in exactly the plurality register the corpus prefers: independent arrival, three decades apart, at the principle that descriptions must not be bearer instruments. The Swordsman's Key (ed25519 identity) is the capability-shaped object in the triad; the City Key is deliberately not, and now says so with citations.

## V.6 Convergence material carried forward to assembly

Three items Part V hands to Run 6 and Run 7 rather than treating: the Aletheia/Lethe complement-pair material enters the assembled convergence section with the exact figures (38 AND 25 = 0, 38 XOR 25 = 63, δ(38) = 0.60317, gap to 1/φ of 2.4%); the proem-as-arithmetic observation (the proem promised what happens between them, the algebra says 63, Tale 30 names 63) is cited as convergence-within-corpus at its best; and the Orchard incident's candidate act (privacy as value and privacy as risk as one structural fact seen from two sides, in Shielded Labs' own words) goes to the Myth Gate for the First Person's binding call.

## V.7 Honest limits of Part V

1. C87 has no circuit. The folding mapping is structural; whether the deviation hash chain admits an efficient folding realization depends on details that do not exist. The conjecture would survive a slow implementation but not an impossible one.
2. The regime statement binds the suite's prose, not its code; nothing in V6 adds enforcement to 🪢, it adds honesty about the absence of enforcement.
3. C88's "canonical not coincidental" question is genuinely open; the working session it needs has not happened.
4. C89's identification of the octahedron with the conditional-independence locus is a reading; the volume facts are theorems, the correspondence is not.
5. The C66 revision rests on a literature citation, not new evidence about the Key; ten points of confidence is the price of good company, no more.

---

*Parts complete. Run 6 assembles `privacy_value_v6.md` from this draft under the G2 assembly directive.*
