---
wp: WP-03
tier: G
artifact: grant-edition
title: "The Privacy is Value Research Programme: Grant Edition"
status: release-draft-v3 (P1 marked at L101; chain complete, the runtime touches this WP no further; frontmatter levelled by A0 at the cycle-9 sweep, L112/F2)
role: A2
date: 2026-07-09
gate_target: A0 targeted re-check per L100(b); clean = P1 (chain complete, no A4/A9 stations)
handoff: A0
extraction_basis: E1 claims C01-C13, C16, C23, C25, C26, C27, C36, C37, C38 plus E2 claims C01-C05, C07-C10, C14, C15 (E2-C06 consumed as a prohibition only; no price figure appears); programme shape per programme/V6_RESEARCH_PROGRAMME_v2.md; the public specification cited once as framing reference class only
downstream: WP-05 (ZCG proposal) and WP-26 (funding applications) build on this document; it is the base grant-facing rehydration, not itself a submission
---

# The Privacy is Value Research Programme

## Grant Edition: what is proven, what is measured, and what funding would measure next

<!-- ============================================================
A2 HANDOFF NOTE TO A0 (pipeline apparatus; REMOVE BEFORE ANY RELEASE)

Draft-v1 (A2, 2026-07-09), per tasks/WP-03_A2_draft_2026-07-09.md.
This is the base grant-facing rehydration. WP-05 and WP-26 adapt it
per funder; nothing here is addressed to a named funder.

Tier discipline held (GR-2 TIER-G):
- Measurement gaps are stated as numbered work packages WP-A to
  WP-H, each with deliverable, method, and evaluation criterion.
- Budget lines are [budget: first-person] placeholders throughout,
  per the task card; no monetary figure of any kind appears (L057
  fiat retirement; GR-3 canonical figures absent entirely; the
  funding-atlas ask ranges of the programme document are NOT
  imported).
- Proven-conditional results appear only with their preconditions
  and the capacity-deficit condition stated in the same passage,
  time-indexed per GR-7 (the L044 decomposition wording of E2-C01
  and E1-C02 is followed, never paraphrased stronger).
- Conjectures appear only as the work packages that would test
  them; no register C-number appears in the body (the task card's
  instruction; claims are carried as [E1-Cnn]/[E2-Cnn] extraction
  markers, uppercase, per the E1/E2 files).
- E2-C06 is consumed as a prohibition only: no market or price
  statement of any kind appears in the account of the first 2026
  instance.
- A9's cycle-1 findings on the source whitepaper (L015 to L023)
  inform what is NOT imported: no static-ceiling sentence family,
  no "forever unreconstructable" or "permanent gap" language, no
  canonical figures in any formulation, no whitepaper-internal
  version metadata. The whitepaper is cited once, as the public
  specification reference class, and carries no claim weight here.
- UK spelling; no em-dashes; verdict-first sections (GR-5).

Inline [E1-Cnn]/[E2-Cnn] markers are the claim trace and are
stripped at release together with this comment and the trace map
section at the end. At release, add an applicant/institution block
per funder (WP-05/WP-26 work).

Claims needed but not found in E1/E2, recorded for A0 rather than
invented (GR-9):
- No E1/E2 claim supports the economic strand of the programme
  (thrust T3, the seventh-capital and valuation material); this
  edition therefore carries the T3 thrust as programme structure
  only, with no claims, and says so in section 1 and in Limits.
  The E4 extraction is the eventual source if a grant edition
  section on value is wanted.
- No E1/E2 claim carries the statement "no standardised
  capacity-measurement methodology exists"; the gap is carried
  here through E2-C04's formalisation obligation, which is what
  the extraction supports.

A7 ADDENDUM (draft-v2, 2026-07-09, voice pass per
tasks/WP-03_A7_voice_2026-07-09.md): prose only; claims, markers,
placeholders, table, references and trace map unchanged in
substance. One wording weakened, never strengthened: section 3
"The time index is not hypothetical" replaced with the
verified-instance formulation. Voice classes and the one
flagged-not-fixed item are recorded in
chronicles/2026-07-09_a7-wp03-voice.md.

A2 REVISION-1 ADDENDUM (draft-v3, 2026-07-09, per
tasks/WP-03_A2_revision_2026-07-09.md): all nine L100 findings
resolved under the four A0 programme-shape rulings recorded in
L100. MAJOR-1: WP-H mechanisation floor stated. MAJOR-2: WP-C
observation windows fixed at six months (two per funded period),
qualifying instance defined, null trigger tied to the renewal
decision; the same qualification rule governs WP-E's
second-instance clause. MAJOR-3: the independence sentence
qualified; WP-A's erasure arm instantiated from the built record
per [E1-C38] with the two-process engine arm declared as the WP-F
interface; WP-C's interim estimation instrument and WP-B interface
declared. MAJOR-4: WP-G opens with a month-0 feasibility gate,
candidate named from the built record per [E1-C36], three-month
failure deadline reported as the negative outcome. MINOR-1: Zcash
agency restored to the verified record. MINOR-2: the fixed
corroboration model re-attached to the steep-then-shallow profile
where E2-C14 holds it; monotonicity carried clean; trace map
corrected. MINOR-3: the unconsumed Bergstra-Burgess reference
removed. MINOR-4: WP-A given a pre-registered decision rule.
MINOR-5: register and pre-registration locators stated in section
5. No fix strengthens any claim beyond its extraction STATUS;
reversals and wording decisions in
chronicles/2026-07-09_a2-wp03-revision-1.md.
============================================================ -->

---

### Executive summary

The verdict first. This programme has one proven, conditional theorem family. The field's published measurements show that deployed multi-agent AI systems operate outside the regime that theorem requires. The quantities that decide whether the theorem's protection can be established, and for how long it lasts, are currently unmeasured. That is the fundable proposition: this document states the proven core in full exactly once, with its conditions; states the external evidence; and converts every unmeasured quantity into a numbered work package with a deliverable, a method and an evaluation criterion. Funding this programme funds measurement, not advocacy.

The programme studies structural separation for personal AI agents: a boundary agent S that faces the outside world and a delegation agent M that acts on the data subject's behalf, with structural context erasure between agent invocations so that neither agent accumulates the other's view. For this pattern there is a proven conditional result. Under a non-collusion precondition and a stated adversary class, the leakage of the two observation channels is additive rather than compounding, and a reconstruction error floor holds. When, additionally, the combined channel capacity falls short of the entropy of the private state (a declarable, system-specific capacity-deficit condition), reconstruction of the private state is bounded away from certainty against the stated adversary class. The guarantee is time-indexed: the capacities are properties of the adversary class of the day, so the deficit condition, not the architecture, is what expires as stronger adversary classes arrive. [E2-C01, E1-C02: Proven-conditional; E2-C02: definition]

The evidence that this matters is external and recent. Published measurement of deployed multi-agent systems finds leakage concentrating on exactly the inter-agent channel whose absence defines the proven regime, with output-only audits missing a material fraction of violations. A proven composition bound permits global leakage to grow exponentially with chain depth when that channel exists, and the published measurements show it rising with depth in practice. [E1-C09, E1-C10: Empirical-external] And two verified 2026 incidents show capability arriving on external schedules against fixed artefacts: a cryptographic soundness flaw that sat unfound through multiple audits until an auditor using a model released the previous day found it within a day of that release, and a withheld quantum-algorithm improvement that was independently reconstructed within two months. [E2-C05, E2-C07: Verified-record]

What is missing is measurement, and the gaps are stated here as eight work packages, WP-A to WP-H, each fundable alone, with the two inter-package interfaces declared in place rather than left implicit: WP-A's second erasure arm is an interface to WP-F, and WP-C names its interim estimation instrument and inherits WP-B's methodology on delivery. Budgets are held as placeholders for the programme owner to complete per funder. The programme's standing method commitment travels with every package: falsification conditions are published before measurement, and results are filed to the programme's public conjecture register whichever way they fall; the register and pre-registration locators are stated in section 5. A result against the programme's prediction is filed with the same prominence as a confirmation.

### 1 · Programme shape

Verdict: the programme is thesis-shaped and grant-shaped already; this edition carries the claims of its separation-and-time thrust, and only those.

The full programme decomposes into three thrusts. Thrust T1, separation and time, asks what privacy architectural separation buys and for how long, by information-theoretic proof and benchmark measurement. Thrust T2, protocol and identity, asks whether shared understanding rather than a stored secret can root identity and recovery. Thrust T3, value and governance, asks what behavioural sovereignty is worth and what institutions price it. The thrust structure, work-package atlas, standards matrix, and calendar are maintained in the programme document; this edition is the claim-bearing grant surface for T1. The T2 and T3 thrusts appear in this document as structure only: no T2 or T3 claim is made here, because this edition's claim basis is the two audited claim inventories behind T1 (the separation cluster and the time cluster), and honesty about that boundary is part of the method being funded. [Programme structure; no extraction claim consumed]

The work packages in section 4 are T1's measurement gaps plus the reference-implementation and formalisation work that T1 results gate. Each is written to be fundable alone, and where a package touches another's deliverable the interface and the standalone fallback are stated inside the package itself: WP-A's second erasure arm is declared as an interface to WP-F, and WP-C, funded alone, uses a declared interim estimation instrument and inherits WP-B's methodology on delivery. Together they form the measurement layer of the programme.

### 2 · What is proven, and under exactly which conditions

Verdict: one conditional theorem family, decomposed so that what the architecture buys and what must be separately declared are never confused.

The pattern under study assigns the protective and the delegating function to two agents. An agent has structural context erasure with respect to an origin if no sequence of permitted operations can reconstruct that origin from the agent's current state: separation enforced by erasure is distinguished from separation enforced by policy, where recovery is prohibited but remains possible. [E1-C06: definition, design status]

The proven core, stated with its conditions. Let H(X) be the entropy of the data subject's private state, let C_S and C_M be the information capacities of the two observation channels, and write R_max = (C_S + C_M)/H(X). Under Precondition 1 (non-collusion: the two observation channels are conditionally independent given the data subject, I(Y_S; Y_M | X) = 0, and no third channel carries the inter-agent residue) and Precondition 2 (capacities evaluated against a stated, fixed adversary class), two structural facts hold: the capacity sum is licensed as additive, and the error floor P_e >= 1 - R_max holds. The preconditions do not by themselves place R_max below one. The strict bound R_max < 1 holds exactly when, additionally, the capacity-deficit condition C_S + C_M < H(X) holds: a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture. The deficit condition is deliberately not a third precondition; two conditionally independent channels of sufficient combined capacity satisfy both preconditions with R_max at or above one, which is exactly why the deficit must be declared alongside the preconditions. [E2-C01, E1-C02: Proven-conditional]

The separation bound itself, I(S; M | X) < ε*, holds in the regime structural context erasure is designed to enforce, and only there: it requires the same two preconditions, and every use of it in this programme states them. [E1-C01: Proven-conditional] Within Precondition 1, additive mutual-information leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), holds exactly when the two observation channels are conditionally independent given X; the compounding results of section 3 describe the complement of this regime and do not contradict it. The two are one theorem family on two sides of one architectural line, the line being whether the inter-agent channel exists. [E1-C04: Proven-conditional] Degradation is graceful within the conditional regime: small violations of the separation bound produce small privacy losses, not catastrophic failure. [E1-C03: Proven-conditional]

The guarantee carries a date. Define R(t) = (C_S(t) + C_M(t))/H(X), where H(X) is fixed by the source and the effective capacities are evaluated against the strongest adversary class available at time t, and define the shelf life t* = sup{t : R(t) < 1}. These are definitions, not claims: they make explicit that the deficit condition is the time-indexed quantity, that R(t) can cross one with both preconditions intact, and that what expires at t* is the deficit condition, not the architecture. [E2-C02: definition; time thread per E2-C01]

None of this is a private theorem. Within its conditional regime the family instantiates results the field has accepted for decades: wire-tap channel equivocation (Wyner, 1975), the source-coding converse (Fano, 1961; Cover and Thomas), secrecy capacity as a capacity difference (Leung-Yan-Cheong and Hellman, 1978), and the colluding-observer failure mode (Csiszar and Korner, 1978). What is new is the deployment pattern that makes the preconditions hold inside an agentic AI system by construction, and the measurement programme below. [E1-C05: grounding map]

### 3 · What the field has measured: the evidence that the gap is real

Verdict: deployed systems enforce separation by policy, measured leakage concentrates on the channel whose absence defines the proven regime, and 2026 supplied two verified instances of capability arriving on external schedules.

The multi-agent privacy field arrived at separation-of-duties independently and repeatedly across 2025 and 2026; the published systems enforce it with prompt-level or training-level controls, none architecturally. [E1-C11: Empirical-external] A recently released vendor governance toolkit is a documented instance of the class: its own documentation records that the policy engine and the agents run in the same process and trust boundary, so violation of the separation remains possible though prohibited. Policy governance and structural separation compose rather than compete; the point is that they are different layers with different failure modes. [E1-C27: Empirical-external]

The measured consequences. A proven composition bound (external to this programme) shows that under sequential composition of N agents with per-agent leakage constraint ε, global leakage is bounded by (2^N - 1)ε, with measured mutual information rising from 0.49 at two agents to 1.05 at five in the published experiments. [E1-C09: Empirical-external] Independent measurement across 1,000 scenarios, 4,979 traces and five frontier models finds unmonitored inter-agent channels leaking at 68.8 per cent, total system exposure at 68.9 per cent, and output-only audits missing 41.7 per cent of violations, even as per-channel output leakage falls in multi-agent configurations. The exposure concentrates on the inter-agent channel: the channel whose deletion defines Precondition 1. [E1-C10: Empirical-external]

The time index has a verified instance base; 2026 supplied two instances. First, a soundness flaw in the Zcash Orchard protocol (a missing constraint in variable-base scalar multiplication) was present from activation in May 2022 and was not found by multiple prior audits, including audits assisted by earlier AI models. It was found on 2026-05-29, by an auditor using a model released the previous day, with counterfeiting demonstrated in local testing; an emergency soft fork followed on 2026-06-02 and a hard fork on 2026-06-03. No evidence of exploitation exists, and, because of the protocol's privacy properties, non-exploitation cannot be cryptographically proven. [E2-C05: Verified-record] Second, a quantum-algorithms team published, on 2026-03-31, a roughly tenfold improvement in the spacetime volume of a Shor's-algorithm attack on secp256k1 (a spacetime-volume figure, not a per-axis qubit or gate count), withholding methods behind a zero-knowledge proof of existence. An independent researcher reconstructed the result about two months later; a second researcher disclosed the same day that he had held the core technique unpublished for about a year; and an open challenge using the published verifier as its scoring filter subsequently exceeded the withheld benchmark. [E2-C07: Verified-record]

What these instances instantiate, this programme reads as follows, and states as hypothesis rather than result: analysis capability against fixed artefacts arrives on external release schedules, uncoupled from any action of the data subject; whether that translates into a measurable upward drift of R(t) for behavioural archives is exactly the question work package WP-C is designed to answer, not a premise of this document. [E2-C03 appears here only as the hypothesis WP-C tests]

### 4 · The work packages: measurement gaps stated as fundable units

Verdict: eight gaps, eight packages; each names what is unknown, what will be delivered, how it will be evaluated, and what a negative result looks like. Conjectures held in the programme's register appear in this document only here, as the work packages that would test them.

| WP | Title | Tests or delivers | Indicative duration | Budget |
|---|---|---|---|---|
| WP-A | Separation benchmark: policy versus structure | The chain-break claim [E1-C07, E1-C08] | 6 to 9 months | [budget: first-person] |
| WP-B | Adversary classes and capacity evaluation | The formalisation the deficit condition needs [E2-C04] | 6 months | [budget: first-person] |
| WP-C | The moving-ceiling observatory | The drift hypothesis and the planning corollary [E2-C03, E2-C09] | 12 months, renewable | [budget: first-person] |
| WP-D | The divergence number | The unmeasured trajectory-divergence parameter [E2-C10] | 9 months | [budget: first-person] |
| WP-E | Existence leak and disclosure policy | The feasibility-attestation leakage law [E2-C08, E2-C14, E2-C15] | 6 months | [budget: first-person] |
| WP-F | Reference implementation, completed and attestable | The specified two-process erasure engine [E1-C36, E1-C37, E1-C38] | 9 months | [budget: first-person] |
| WP-G | Trust half-life, measured | The decay-curve conjectures [E1-C23, E1-C25, E1-C26] | 12 months, longitudinal | [budget: first-person] |
| WP-H | Formal foundations: composition and obstruction | The composition model and the forgetting criterion [E1-C16, E1-C12, E1-C13] | 12 months | [budget: first-person] |

**WP-A · Separation benchmark: policy versus structure.** The gap: whether real erasure implementations achieve the chain break, capping total leakage at the additive bound Nε rather than the sequential bound (2^N - 1)ε, has never been measured. The sequential compounding bound itself is proven and published externally [E1-C09]; the chain-break claim is an engineering claim about erasure protocols, not a theorem [E1-C08]. The qualitative form, that erasure-enforced separation yields tighter guarantees than policy-enforced separation, is likewise held as conjecture [E1-C07].

**Deliverable:** an open benchmark and report measuring leakage growth with agent-chain depth N under two arms, policy-separated and erasure-separated, on matched tasks.

**Method:** extend the published multi-agent leakage measurement protocol [E1-C10] with mutual-information instrumentation of inter-agent channels at N = 2 to 5; pre-registered analysis plan; both arms instrumented identically. The erasure-separated arm instantiates from the built record: the workflow-level harness realising the held-apart pattern, of which exactly one instance is built and which holds two seats apart, so its built depth capability is N = 2 and the deeper chain lengths require extending that harness under this package [E1-C38]. A second erasure arm on the two-process erasure engine is declared as an interface to WP-F and runs only if WP-F delivers, because the engine is specified and its code is not written [E1-C37].

**Evaluation criterion:** measured leakage-versus-depth curves discriminate between the additive bound Nε and the sequential bound (2^N - 1)ε in each arm under a pre-registered decision rule: the statistical test, the effect threshold, and the depth range at which the two bounds are distinguishable at the study's power are stated in the analysis plan before measurement begins (at N = 2 the bounds differ by a single ε, so discrimination is powered at the deeper chain lengths). The package succeeds if the measurement discriminates under that rule, whichever way it falls; an erasure arm that tracks the sequential bound is a reportable negative result and is filed as such.

**Budget:** [budget: first-person].

**WP-B · Adversary classes and capacity evaluation.** The gap: without a formal model of "adversary class at time t", declared capacities cannot be independently evaluated. The capacity-deficit condition of section 2 is declarable, but the phrase requires formalisation as an ordered family of decoder classes, with monotonicity following from the ordering and only the rate empirical; that formalisation is an obligation the programme has named and not yet discharged [E2-C04].

**Deliverable:** a formal adversary-class model grounded in the quantitative information flow and Bayes-capacity literature, plus a capacity-evaluation methodology applied end to end to one reference system with declared C_S, C_M, H(X) and t*.

**Method:** formal definition and proof of the monotonicity structure; instantiation against at least two named decoder classes; documented evaluation walk-through.

**Evaluation criterion:** an independent party, given the methodology and the reference system, reproduces the declared capacities within stated tolerance; failure to specify a usable ordering is reported as a finding against the formalisation, not absorbed.

**Budget:** [budget: first-person].

**WP-C · The moving-ceiling observatory.** The gap: the upward drift of R(t) is a hypothesis, and its verified instance base currently numbers two [E2-C05, E2-C07]. The programme holds as hypothesis that frontier capability growth raises effective capacities against fixed archives without raising H(X), so that R(t) drifts upward on a schedule coupled to model releases rather than to any action of the data subject [E2-C03]; it holds as a separate hypothesis a planning corollary, that every public feasibility attestation shortens the effective migration horizon independently of any actual attack [E2-C09].

**Deliverable:** a longitudinal instance register (successors to the two 2026 instances, gathered under the WP-00 verification discipline) and a capability-tracking instrument producing dated re-estimates of t* for named archive classes.

**Method:** pre-registered predictions of drift direction and bounds per archive class; instance verification against primary records; a public re-estimate at the close of each observation window. Funded alone, the observatory uses a declared interim instrument for the dated t* re-estimates: published capability results serve as the auditor's lower-estimate inputs, with the estimation method declared alongside each re-estimate; on delivery of WP-B's capacity-evaluation methodology the observatory inherits it and restates prior estimates under it. The WP-B interface is stated here so that funding WP-C alone carries no undeclared dependency.

**Evaluation criterion:** predictions are filed before observation windows open. Observation windows are six months long, two per funded period. A qualifying instance is a publicly verifiable event, verified under the WP-00 discipline of the method above, that moves a dated t* re-estimate earlier for a named archive class. Instances that contradict the drift hypothesis are filed with the same prominence as instances that confirm it; two consecutive windows with no qualifying instance is itself a reportable finding on the hypothesis's scope and is reported into the renewal decision.

**Budget:** [budget: first-person].

**WP-D · The divergence number.** The gap: the divergence parameter λ has never been measured. The programme's countermeasure hypothesis, that a sovereignty path with positive trajectory divergence makes reconstruction error grow with time and can outrun capability drift, depends on that parameter; the programme names it its most-needed number, and holds the whole chain at low confidence pending measurement [E2-C10].

**Deliverable:** a measurement design for λ on recorded behavioural trajectories, and either a first estimate with stated uncertainty or a published null.

**Method:** operationalise trajectory divergence on paired perturbed trajectories; simulation first, then instrumented pilot data under consent; analysis plan pre-registered before pilot data is collected.

**Evaluation criterion:** the package succeeds when a defensible estimate or bound for λ exists in public, including λ indistinguishable from zero; a null result retires the countermeasure hypothesis from the programme's active set and is filed at the same prominence as a positive.

**Budget:** [budget: first-person].

**WP-E · Existence leak and disclosure policy.** The gap: the existence-leak law is held as conjecture, open pending a second independent instance. The law states that a zero-knowledge proof of capability feasibility leaks a nonzero upper bound on reconstruction or search difficulty, floored externally by the known impossibility of leakage-resilient zero knowledge below rate one; it concerns capability attestations, not instance attestations [E2-C08]. Two adjacent statements need grounding: that reconstruction difficulty is monotone non-increasing in the number of corroborating systems, a statement carried clean as the extraction holds it, whose accompanying steep-then-shallow decay profile is the component that requires a fixed corroboration model [E2-C14], and that a live content address under deduplication leaks the existence of its content to a holder of a candidate, which is stated in the programme's design notes without external grounding [E2-C15].

**Deliverable:** a formal statement of the law in an attestation class where it is non-vacuous, a case-study corpus beginning from the verified 2026 instance [E2-C07], and a short disclosure-policy note addressed to the zero-knowledge standards community.

**Method:** formalisation against the leakage-resilient zero-knowledge literature; a corroboration model fixed before the steep-then-shallow profile is evaluated, the monotonicity statement standing as carried; deduplication side-channel demonstrated or refuted on a testbed and grounded in the existing side-channel literature.

**Evaluation criterion:** either the law is stated and proved in a non-vacuous attestation class, or the vacuity obstruction is characterised and published; the deduplication claim is resolved in either direction on the testbed; a second qualifying instance, qualification under the same rule stated in WP-C's evaluation criterion, or its absence over the project window, is reported against the law's held status.

**Budget:** [budget: first-person].

**WP-F · Reference implementation, completed and attestable.** The gap: the strongest specified design has no code. The two erasure grades are instantiated in a deployed browser-storage design (per-session key destruction against persisted keys, with the cross-boundary binding carried manually by the data subject, enforcing the non-collusion regime by construction at that layer) [E1-C36]; the stronger two-process design, separate extension processes with separate storage and permissions communicating only via an explicit message channel, is specified but its code is not written [E1-C37]; and a workflow-level harness realising the held-apart pattern has exactly one built instance [E1-C38]. The definitional test for the two grades of erasure is design-status, not proven [E1-C06].

**Deliverable:** the two-process implementation built to its specification, with a design-time channel inventory and a conformance walk-through suitable for the standards bodies the programme already sits in (structure per the programme's standards matrix).

**Method:** build to the published specification; channel inventory enumerating every inter-agent surface (process, storage, logging, orchestration, telemetry); erasure implemented as storage destruction, structural rather than instructed; third-party documentary audit.

**Evaluation criterion:** the audited inventory shows no inter-agent channel and the erasure is structural, or the surfaces that prevent that showing are named publicly; implementation status is reported per component, with specified-but-not-built never presented as built.

**Budget:** [budget: first-person].

**WP-G · Trust half-life, measured.** The gap: three trust-decay conjectures whose named formalisation path, empirical longitudinal measurement, is exactly what this package supplies [E1-C25]. The programme conjectures that a trust edge in a relationship-credential network decays with a half-life from inscription unless renewed or augmented, with the parametric form named structurally rather than derived [E1-C23]; that edges formed by productive work decay slower than edges formed by transactional work at comparable initial weight [E1-C25]; and that total trust half-life composes multiplicatively across the three separation axes, so that ageing in one axis cannot be compensated by another [E1-C26].

**Deliverable:** a longitudinal dataset of inscribed trust edges under consent, with fitted decay curves per edge-formation class, and a public analysis.

**Method:** the package opens with a month-0 feasibility gate: securing an operating relationship-credential network under consent is the first milestone, with the candidate named from the built record, the deployed relationship-credential implementation already described under WP-F (per-session key destruction against persisted keys, the cross-boundary binding carried by the data subject) [E1-C36]; if no network is secured within three months, that failure is reported as the package's negative outcome and the package closes. The gate's report states the secured network's expected edge volume and the observation cadence before instrumentation begins. Instrumentation then proceeds: classify edge formation (productive versus transactional) at inscription time, before outcomes are visible; pre-registered comparison of decay constants; the multiplicative composition claim tested against per-axis ageing where the data supports it.

**Evaluation criterion:** the parametric form fits or is rejected on stated statistical criteria; a rejected form, or no measurable difference between formation classes, is filed as a negative result at full prominence; failure at the month-0 feasibility gate, or an observation window that proves too short to bound the decay constants, is reported as the package's outcome with any partial constraints published.

**Budget:** [budget: first-person].

**WP-H · Formal foundations: composition and obstruction.** The gap: the composite separation claim, that protection multiplies across the agent, data and inference axes so that collapse of any axis weakens the whole bound, is the programme's named falsification frontier and is not proven [E1-C16]. The deeper account of what forgetting is mathematically, that grade-2 erasure corresponds to a non-vanishing obstruction to gluing the agents' local views into a global witness, is a framing whose machinery is explicitly unconstructed [E1-C12], and its companion placement claim, that erasure is the canonical instance of a terminal obstruction, fails or stands independently of it [E1-C13].

**Deliverable:** a machine-checked formalisation of the separation bound and the composition model in a proof assistant, with every assumed axiom listed as a finding; and either a construction of the obstruction machinery for the two-agent instantiation or a documented account of why it does not go through.

**Method:** mechanisation first of the proven core of section 2, then of the composition model with the multiplicativity claim isolated as the explicit unproven step; the obstruction work run as a bounded formalisation attempt with a stated stop condition.

**Evaluation criterion:** the mechanisation strand carries a floor: the proven core of section 2, mechanised end to end with its axiom list published, is the minimum outcome, and below that floor the package reports failure; partial mechanisation counts only above the floor, and the axiom list is published as a result, not a footnote. An obstruction construction that fails within the bounded attempt is written up as a negative result, and any composition counterexample found is filed against the composite claim at full prominence.

**Budget:** [budget: first-person].

### 5 · Method commitment: pre-registration and the negative-results rule

Verdict: the honesty discipline is the differentiator, and it is written into every deliverable above before measurement begins.

Every work package carries the same commitments, in writing, at proposal time. Falsification conditions are published before measurement begins. Analysis plans for WP-A, WP-C, WP-D and WP-G are pre-registered on an OSF-class public pre-registration platform, the specific platform fixed at adaptation alongside the applicant block. Results are filed to the programme's public conjecture register, which is public in the same reference class as the specification cited in the references, whichever way they fall, and a result against the programme's prediction is filed with the same prominence as a confirmation. Implementation status is always reported per component, with specified-but-not-built never presented as built.

For an assessor, the practical consequence is that no package's value depends on the programme being right. The evaluation criteria in section 4 name their negative outcomes explicitly because those outcomes are deliverables, not failure modes. This document itself contains no claim stronger than its audited source inventory supports, and the section 6 limits are part of the offer, not a disclaimer appended to it.

### 6 · Limits

Verdict: this document claims less than a persuasive grant text might, deliberately, and the residue is stated here in funder-legible terms.

The proven core is conditional twice over. Outside its two preconditions, non-collusion and a stated adversary class, it makes no statement; within them, the strict reconstruction bound holds only while the capacity-deficit condition holds, and that condition is a declared numerical fact about the system under a named adversary class; the architecture does not supply it. The preconditions are exactly what fails when observers collude or channels are combined; the deficit is exactly what erodes as stronger adversary classes arrive, which is why the guarantee is presented time-indexed as R(t) throughout. [E2-C01, E1-C02, E2-C02]

Every rate in this document is unknown. The drift of R(t), the divergence parameter, the trust-edge decay constants, and the chain-break behaviour of real erasure implementations are all unmeasured; that is not a weakness of the proposal but its content, and each has a named work package with a named negative outcome. The verified instance base for the time thesis is two instances; two instances motivate an observatory, they do not establish a law, and section 3 states the drift reading as the hypothesis WP-C tests. [E2-C03, E2-C05, E2-C07]

The empirical characterisation of multi-agent leakage in section 3 is the field's measurement, not this programme's; the programme's benchmark (WP-A) does not yet exist, which is the point of funding it. [E1-C09, E1-C10, E1-C11]

Implementation is ahead of proof in one place and behind specification in another. One workflow-level instance of the held-apart pattern is built and in use; the two-process erasure engine is specified and its code is not written; nothing in this document presents the specified design as a deployed system. [E1-C36, E1-C37, E1-C38]

The economic strand of the programme (behavioural data as a capital class, and its valuation) appears in this document only as programme structure. Its claim inventory is a separate audited extraction not consumed here, and this edition asserts no monetary value figure of any kind; budget lines are placeholders completed by the programme owner per funder.

Findings against this framework, should they arise, will be reported with the same prominence as findings for it.

### References (external only; author-date; venue formatting at adaptation)

- Wyner, A. D. (1975). 'The wire-tap channel', Bell System Technical Journal.
- Fano, R. M. (1961). Transmission of Information; Cover, T. M. and Thomas, J. A. (2006). Elements of Information Theory.
- Leung-Yan-Cheong, S. K. and Hellman, M. E. (1978). 'The Gaussian wire-tap channel'.
- Csiszar, I. and Korner, J. (1978). 'Broadcast channels with confidential messages'.
- Asif and Amiri (2026). Sequential-composition leakage bound and measurements. arXiv:2603.05520; Patil, Stengel-Eskin and Bansal (2025). Composition analysis. arXiv:2509.14284 (preprint). [per E1-C09]
- El Yagoubi, Badu-Marfo and Al Mallah (2026). AgentLeak inter-agent channel measurement. arXiv:2602.11510. [per E1-C10]
- Multi-agent privacy landscape: MAGPIE, arXiv:2506.20737; PrivAct, arXiv:2602.13840. [per E1-C11]
- Microsoft (2026). Agent Governance Toolkit documentation. github.com/microsoft/agent-governance-toolkit. [per E1-C27]
- Zcash Foundation (2026). 'Zebra 4.5.3 and 5.0.0: Emergency Soft Fork and NU6.2 Activation', zfnd.org; BlockSec incident analysis (2026). [per E2-C05]
- Babbush et al. (2026). arXiv:2603.28846 / eprint.iacr.org/2026/625; Schrottenloher reconstruction, eprint.iacr.org/2026/1128; Gidney disclosure post (2026); ecdsa.fail leaderboard record. [per E2-C07]
- Garg, Jain and Sahai. Leakage-resilient zero knowledge (impossibility floor). [per E2-C08]
- Mosca, M. (2018). 'Cybersecurity in an era with quantum computers: will we be ready?'; Blanco-Romero et al. (2026). Harvest-now-decrypt-later economics. arXiv:2603.01091. [per E2-C09]
- Bakhta, A. (2025). On the Half-Life of Cryptographic Trust, StarkWare. [per E1-C23, E1-C25, E1-C26]
- Public specification (framing reference class only, no claim weight): Privacy is Value, V6 whitepaper edition, agentprivacy.ai.

---

### Trace map (pipeline apparatus; stripped at release with the inline markers)

Every claim-bearing passage carries an inline [E1-Cnn] or [E2-Cnn] marker; this map records consumption per section, with STATUS as carried in the extractions. Nothing in this draft exceeds its extraction STATUS; conjecture-status claims appear only inside section 4 work packages as test targets, per the tier discipline.

- Executive summary: E2-C01, E1-C02 (Proven-conditional, decomposition wording); E2-C02 (definition); E1-C09, E1-C10 (Empirical-external); E2-C05, E2-C07 (Verified-record). Method commitment sentences are GR-8 obligations, not claims.
- Section 1: programme structure only, from programme/V6_RESEARCH_PROGRAMME_v2.md; zero extraction claims; the T3 exclusion is recorded in the handoff note and Limits.
- Section 2: E1-C06 (definition, design status); E2-C01 + E1-C02 (Proven-conditional; preconditions, deficit condition and time index stated in-passage per GR-7); E1-C01 (Proven-conditional); E1-C04 (Proven-conditional); E1-C03 (Proven-conditional); E2-C02 (definition); E1-C05 (grounding map).
- Section 3: E1-C11, E1-C27, E1-C09, E1-C10 (Empirical-external); E2-C05, E2-C07 (Verified-record, wording held to the extraction accounts; the tenfold figure carries its spacetime-volume metric per the E2-C07 re-issue); E2-C03 stated as hypothesis-under-test only. E2-C06 consumed as a prohibition: no market or price statement appears in the E2-C05 account.
- Section 4 (work packages; conjectures as test targets only): WP-A tests E1-C07, E1-C08 (conjecture status) against E1-C09, E1-C10 baselines; its erasure-separated arm instantiates from E1-C38 (design-assumption; one built instance, workflow level, two seats, carried verbatim) with the two-process engine arm declared as the WP-F interface per E1-C37 (specified, code not written, carried verbatim). WP-B discharges E2-C04 (design-assumption, formalisation obligation). WP-C tests E2-C03 and E2-C09 (conjecture status) on the E2-C05/E2-C07 instance base; its interim estimation instrument and WP-B interface are method statements, not claims. WP-D tests the E2-C10 chain (conjecture status; unmeasured parameter). WP-E tests E2-C08, grounds E2-C14 and E2-C15 (conjecture status; scope fences carried: capability attestations only; guessable candidate space; E2-C14 carried with monotonicity clean and the fixed-corroboration-model requirement attached to the steep-then-shallow profile, per the extraction). WP-F builds from E1-C36, E1-C37, E1-C38 (design-assumption; implementation status per source carried verbatim: one built instance, engine specified not built) and E1-C06. WP-G tests E1-C23, E1-C25, E1-C26 (conjecture status); its month-0 feasibility gate names the candidate network from E1-C36 (design-assumption; deployed as described at spec date, carried verbatim). WP-H tests E1-C16 and attempts E1-C12, with E1-C13 carried as the independent placement claim (all conjecture status; the E1-C12 machinery stated as unconstructed); its mechanisation floor is a method statement over the section 2 proven core, not a new claim.
- Section 5: GR-8 method obligations; no extraction claims.
- Section 6: restates section 2 and 3 claims at equal or weaker strength; markers inline.
- Not consumed, and why: E1-C14/E2-C13 and the Band IX limitative readings (E1-C40, E2-C14's Tarski framing beyond its testable monotonicity component) are framing conjectures with no funder-legible test smaller than WP-E/WP-H and are left to their registered homes; E1-C15 (betweenness persistence) offers a computable static measurement but no programme-critical gap, left out to keep the package set at eight; E1-C17, E1-C18 (semantic grounding) carry no security content beyond E1-C01/E1-C02 and are not consumed (the Promise Theory reference formerly attached under a citation-strategy tag was removed at draft-v3 as carrying no consuming passage); E1-C19 to E1-C22, E1-C24, E1-C28 to E1-C35, E1-C39 are convergence, encoding, or register-hygiene material outside this edition's scope; E2-C11 and E2-C12 duplicate E1 homes consumed above.
- Claims needed but absent from E1/E2, not invented (GR-9): the T3 economic claims (E4 material) and any standalone statement that no standardised capacity-measurement methodology exists (carried instead through E2-C04's obligation wording). Recorded for A0 in the handoff note.
