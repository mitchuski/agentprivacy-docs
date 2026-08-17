---
wp: WP-04
tier: A
artifact: sok-paper
title: "SoK: The Shelf Life of Privacy Guarantees"
status: draft-v4
role: A3 (L062(d) referee-grade sweep, Kagai engagement, L088 MAJOR-4; revision-1 lineage L090)
date: 2026-07-09
gate_target: awaiting-P4 (P3 passed L093; P4 is the First Person's; the runtime stops here)
handoff: the P4 owner (First Person read; FC workshops deadline 2026-09-01)
venue_target: HotPETs or FC workshop (FC workshops deadline 2026-09-01)
extraction_basis: E2 claims C01-C05, C07-C15 (E2-C06 consumed as a prohibition only; no price figure appears); novelty fence = reviews/WP-04_prior_art.md, ledger N1-N7 / S1-S6, binding
scaffold: templates/submission/preprint/ section structure mirrored in markdown
---

# SoK: The Shelf Life of Privacy Guarantees

## Time-Indexed Reconstruction Bounds over Fixed Archives

<!-- ============================================================
A3 HANDOFF NOTE TO A0 (pipeline apparatus; REMOVE BEFORE ANY RELEASE)

Draft-v2, formal pass over A2's draft-v1. Inline [E2-Cnn] markers
remain the claim trace and are stripped at release. Register
C-identifiers stay through P1-P3 per the A0 provisional ruling
(L066(c)).

FORMAL STATEMENTS CHANGED AT THIS PASS (one line each):
- Proposition 1: restated with explicit hypotheses (finite alphabet,
  budgets against the declared class), split into (a) capacity-sum
  bound (inequality with equality condition) and (b) exact Fano
  floor (with the 1/H(X) term and the alphabet-entropy hypothesis);
  proof supplied; recorded as restated known bounds, N2 confined to
  the decomposition reading. The rounded floor P_e >= 1 - R_max is
  no longer asserted (it is not exactly implied by Fano; precision
  divergence from spec 11.2 / E2-C01 wording, ledger proposal in
  chronicle, same class as L065(e)).
- Definition 2: restated sup-accurate with domain and conventions;
  new Remark 1 states what the supremum does and does not assert,
  surfaces the monotonicity question (L054, open) honestly, and
  removes any first-crossing dependence.
- Section 4.1: new Definition 3 (decoder class as gain-function
  family; effective capacity as supremum over the class, with a
  compatibility requirement bridging to Proposition 1); new Lemma 1
  (structural monotonicity under the ordering hypothesis; sup and
  first-crossing coincide) with proof; the empirical residue stated
  exactly as A10 fenced N3 (structural given ordering; only the
  rate empirical; demotion clause retained).
- Conjecture 2 (C81): candidate probability model added; the named
  missing step is that the bare inequality is immediate (hence
  empty) under the naive model, so the proof obligation is an
  attestation class in which it is non-vacuous; formal GJS
  object-distinction sentence added.
- Conjecture 3 (C93): difficulty functional given an explicit
  symbol Delta_k(X) (source writes D(X); renamed to avoid collision
  with the discount D(a) of Conjecture 4); fixed-corroboration-model
  hypothesis explicit.
- Conjecture 4 (C84): axioms (D1)-(D3) for the discount functional
  supplied; conjecture explicitly held at schema level until an
  elicitation study identifies a conforming D.
- Section 6.4: formal-pass decision recorded: both limitative
  framings retained at related-work status only, no formal
  statement made.
- Abstract / 1 / 1.1(2) / 8 / 9: "additive" tightened to
  capacity-sum bound wording; "proof owed at the formal pass"
  removed; conclusion restated to the post-pass status.
- Public-spec URL placed once, Section 3.1 footnote, per L066(c).

REVISION 1 (2026-07-09, A3 seat, per A5 review 1 / L088). Statement-
and remark-level only; Proposition 1 and Lemma 1 proofs untouched:
- MAJOR-1, route (a): Definition 3's closing bridge restated as a
  desideratum. Compatibility now claims only the per-channel
  extraction bound; the joint-estimator floor is named as the
  finished definition's owed delivery; residue (ii) wording aligned
  (joint output + sub-additivity named); conclusion's next-steps
  clause aligned.
- MAJOR-2: abstract + contribution 5 recast to the operational form
  (displayed inequality vacuously true under the naive prior model;
  the obligation is the operational form). Section 6.1 unchanged.
- MAJOR-3: new Remark 2 (availability semantics) in 3.4: D_t =
  capability realisable by some adversary regardless of publication;
  public trajectory = auditor's lower estimate (errs unsafe);
  attestation moves the estimate, not R(t); propagation is a distinct
  D_t growth. 5.8's withheld-capability paragraph read explicitly
  against it; Conjecture 4's Z_b stated as the planner's estimate
  with t* its derived referent (conflation removed).
- MINOR-1: 3.4's "nothing about it is chosen" reconciled with
  Section 8 (inputs declared; crossing computed given them).
- MINOR-2: 5.2's ECDLP-ladder sentence no longer says "instrument
  C(t) directly" (instruments the adversary trajectory, upstream).
- MINOR-3: Lemma 1's equality clause now carries both nonemptiness
  guards; proof unchanged (it already assumed both).
- MINOR-5: contribution 2 leads with the obligation separation;
  novelty clause second.
- Untouched per card: 5.8 first paragraph's Zcash citation block
  (A4, MINOR-4 — observed landed concurrently); Kagai engagement
  passages in 2 / 5.1 / 8 / References note (L062(d) sweep owns
  MAJOR-4).

L062(d) SWEEP (2026-07-09, A3 seat, per L088 MAJOR-4 / L062(d)):
- Kagai, Branch, But & Allen 2025 (Telecom 6(4):100) read
  referee-grade at its primary record (publisher PDF via the MDPI
  asset host; author list verified via Crossref). Verdict: ENGAGED
  as an instance of the archival regime, section 5.1 (existing key
  kagai2025harvest; zero bib changes).
- The four process-narration passages (2 / 5.1 / 8 / References
  closing note) rewritten as ordinary related-work prose; the Kagai
  entry moved into the reference list proper; the unresolved-
  preprint fence unchanged (still not cited).
- Symbol collision disclosed in-text at 5.1: their R(t) is the
  compromise probability Pr{Ha(t) >= Ld}, not this paper's
  capacity-to-entropy ratio.
- Revision 1's eleven sites (L090) untouched.

NOTATION vs WP-07 (linear_cap_paper.md section 3), flagged not
silently harmonised:
- C_S, C_M: WP-07 treats them as DECLARED BUDGETS (ER-5/ER-6);
  WP-04 defines them as class-relative EFFECTIVE CAPACITIES via
  Definition 3's supremum. Same symbols, different definitional
  route; WP-07's ER-6 already defers the ordering to this paper.
  DIVERGENCE FLAGGED, left standing.
- Fano floor: WP-04 now matches WP-07 Theorem 3.2's exact form
  (deliberate, recorded here); both diverge from the canon's
  rounded form (spec 11.2), see chronicle ledger proposal.
- R(t), t* formulas identical in both papers; WP-07 Remark 3.4's
  t* gloss carries no sup-semantics caveat and inherits the L054
  question; flagged for WP-07's next touch (chronicle proposal).
- Grade-1/Grade-2: WP-04 5.6 uses the terminology; WP-07
  Definition 3.8 is the operational definition; consistent, not
  restated here.

A2 WORK-LIST DISCHARGE: items 1-5 discharged by the changes above
(item 5's profile stays a remark, as A2 left it); item 6 unchanged
(UNVERIFIED items still not cited; A4 resolves); item 7 unchanged
(bib additions await A4/A8; arXiv:2509.14284 still not cited,
its E2-C12 annotation now reads verification-in-flight per the
2026-07-07 E2 maintenance touch); item 8 discharged (URL placed
per L066(c)). E2-C07's re-issue (same touch) is already matched
by Section 5.8's wording: primary attribution Babbush et al.,
tenfold claim carrying its spacetime-volume metric.

NUMBERING NOTE FOR A8 (port time): the file has no "Definition 1"
(draft-v1 numbered the R(t)/t* definition as Definition 2,
mirroring its position after Proposition 1's material; this pass
kept the numbering to avoid breaking the many in-text references).
Renumber mechanically at LaTeX port when environments are assigned.

STILL OPEN FOR A4/A7/A8: citation resolution and bib additions
(~36 entries, L066(b)); referee-grade sweep of the everlasting-
privacy / long-term-confidentiality families before P1 (L062(d));
prose voice pass (A7); math-symbol normalisation at LaTeX port
(A8; this pass introduced unicode math in the formal statements
it touched, the rest of the file remains ASCII-math).
============================================================ -->

## Abstract

Privacy guarantees over recorded data degrade in a specific and under-formalised way: the record is fixed at disclosure time, while the adversary's decoding capability keeps improving. At least four literatures observe this independently, as harvest-now-decrypt-later, as retroactive de-anonymisation, as cryptoperiod practice, and as the motivation for everlasting-privacy constructions, but no common formal object connects them. This paper systematises these literatures under a time-indexed reconstruction ratio R(t) = (C_S(t) + C_M(t))/H(X), the ratio of the effective capacities of the channels leaving a two-agent disclosure architecture, evaluated against the strongest adversary class available at time t, to the entropy of the protected source [E2-C02]. Under two named preconditions, non-collusion between the channels and evaluation against a declared adversary class, the capacity sum bounds the joint leakage and a Fano-type error floor holds; the strict bound R(t) < 1 holds exactly when a third, deliberately separate condition holds, the declared capacity-deficit condition C_S(t) + C_M(t) < H(X), and it is this deficit condition, not the architecture, that expires at the shelf life t* = sup{t : R(t) < 1} [E2-C01][E2-C02]. The drift itself decomposes into two mechanisms kept distinct throughout: method-and-compute growth, which erodes computationally protected channels and moves certified estimates but cannot raise leakage through an information-theoretic bound, and side-information growth, which erodes even information-theoretic floors through the residual entropy of the source given the adversary's accumulating background [E2-C02]. We survey the families the ratio organises, including two verified 2026 instances of the archival regime, state the adversary-ordering formalisation this systematisation requires as an explicit programme, state the existence-leak conjecture for capability attestations in its operational form, that conditioning on attested feasibility provably reduces the adversary's search cost (its bare inequality I(feasibility; method) > 0 is shown vacuously true under the naive prior model), with the 2026 withheld-capability episode as its single verified instance, and report one countermeasure direction as an unvalidated open problem. Conjectures are stated as conjectures with proof obligations; the survey's unification claim is made to our knowledge and its known referee risks are stated in the threats section.

## 1 Introduction

A confidentiality guarantee issued today over data recorded today is, implicitly, a claim about every future adversary who will ever hold the recording. The wiretap lineage that grounds information-theoretic secrecy fixes the adversary together with the channel (Wyner 1975; Leung-Yan-Cheong and Hellman 1978; Csiszár and Körner 1978) and therefore cannot express the deployed-systems situation in which the channel output is archived and the adversary class improves against it year over year. The situation itself is well documented. The harvest-now-decrypt-later literature treats it as an economic threat model (Blanco-Romero et al. 2026). The retroactive de-anonymisation record shows datasets released as safe becoming unsafe when auxiliary data and methods arrived later (Narayanan and Shmatikov 2008; Gymrek et al. 2013; Erlich et al. 2018). The consent-side statement of the same phenomenon is the end run: inference from accumulating background data circumvents anonymity and consent protections alike, so a guarantee's effective strength is a function of the evolving external data environment rather than of its issuing assumptions (Barocas and Nissenbaum 2014). Key-management practice bounds key lifetimes administratively (Barker 2020). The everlasting-privacy line constructs protocols whose privacy survives later, computationally unbounded adversaries, precisely because its authors did not trust computational assumptions to age (Moran and Naor 2006; Haines et al. 2023). These strands share a phenomenon and do not share a formalism [S1: the phenomenon is theirs, not ours].

This paper's position is that the shared object is a ratio. Let H(X) be the entropy of the protected source, fixed at disclosure time, and let C_S(t) and C_M(t) be the effective capacities of the two channels leaving a disclosure architecture that splits data flow between a boundary agent S and a delegation agent M, evaluated against the strongest adversary class available at time t. The reconstruction ratio is R(t) = (C_S(t) + C_M(t))/H(X), and the shelf life of the guarantee is t* = sup{t : R(t) < 1} [E2-C02]. The formal content of this paper is a decomposition of what makes R(t) < 1 a guarantee at all: two preconditions (non-collusion and a declared adversary class) license the capacity-sum bound on joint leakage and a Fano-type error floor, and a separate, declarable, measurable capacity-deficit condition licenses the strict bound. The preconditions do not by themselves place the ratio below one. What expires at t* is the deficit condition, not the architecture [E2-C01].

We write this as a systematisation of knowledge rather than a results paper for a stated reason: the value of the ratio is that five literatures that do not cite one another become instances of one object, and the honest status of the object's own apparatus is mixed. The bound decomposition is conditional and elementary; the adversary ordering it presupposes is a formalisation programme, not a finished definition [E2-C04]; the drift of R(t) and the leakage of capability attestations are conjectures carried in the research programme's conjecture register with stated evidence status; and the countermeasure direction we can name has no measurement behind it at all [E2-C10]. Each of these appears below at exactly that status. A result against the model's prediction, should one arrive, is filed to the register with the same prominence as a confirmation, and this paper commits to that in writing.

### 1.1 Contributions

1. **A derived shelf life (Section 3).** The definition of the reconstruction ratio R(t) = (C_S(t) + C_M(t))/H(X), capacities evaluated against the strongest adversary class available at time t, and of the shelf life t* = sup{t : R(t) < 1} as a quantity derived from an architecture and an adversary class, where prior art states lifetimes as declared requirements (Mosca 2018; Barker 2020) or compares declared lifetimes against declared horizons [N1][E2-C02].
2. **The deficit decomposition (Section 3).** A separation of obligations within the guarantee: the two preconditions, non-collusion and a declared adversary class, are attestable properties of a deployment and license the capacity-sum bound on joint leakage and a Fano-type error floor, while the capacity-deficit condition licensing the strict bound R < 1 is a numerical comparison that no architectural property entails, and it is the deficit condition, not the architecture, that expires. The wiretap lineage owns the floor machinery; the novelty claim is confined to isolating a declared, measurable deficit condition as the time-indexed part of a privacy guarantee, which to our knowledge no prior work does [N2][E2-C01].
3. **An adversary-ordering programme (Section 4).** The formalisation programme for "adversary class at time t": an ordered family {D_t} with D_t ⊆ D_t' for t ≤ t', under which the monotonicity of R(t) is structural (Lemma 1) and only the rate is empirical. The family is grounded at definition level in the gain-function framework of quantitative information flow, where adversary models are currently per-scenario and unordered in time, and the programme remains contingent: its residual obligations are named exactly in Section 4.1, and if they fail the monotonicity demotes to a modelling assumption [N3][E2-C04].
4. **The unification (Section 5).** To our knowledge, no prior systematisation organises harvest-now-decrypt-later, retroactive de-anonymisation, quantum-horizon estimation, cryptoperiod practice, continual-observation differential privacy, and everlasting-guarantee constructions as instances of a single time-indexed reconstruction bound; the nearest prior SoK is confined to e-voting (Haines et al. 2023) and the nearest survey of long-term guarantees covers integrity, not confidentiality (Vigil et al. 2015) [N7].
5. **An existence-leak law (Section 6).** The conjecture that a zero-knowledge proof of capability feasibility leaks an upper bound on reconstruction or search difficulty, scoped to capability attestations, floored by the leakage-resilient zero-knowledge impossibility of Garg, Jain and Sahai (2011), and instantiated by a verified 2026 episode. Its displayed inequality, I(feasibility; method) > 0, is shown in Section 6.1 to be vacuously true under the naive prior model; the contribution is the conjecture's operational form and its proof obligation, an attestation class in which conditioning on attested feasibility provably and quantifiably reduces the adversary's search cost [N4][E2-C08].
6. **An attestation discount (Section 6).** The conjecture that public feasibility attestations shorten the effective migration horizon of Mosca-style planning independently of any actual attack, Z_b' = Z_b - D(a) [N5][E2-C09].
7. **A named open problem (Section 7).** The divergence countermeasure, reconstruction error growing as e^(lambda t) along a diverging data trajectory, presented strictly as an open problem: lambda is unmeasured, and we found neither anticipation nor support in the literature [N6][E2-C10].

## 2 Systematization Method

**Corpus and verification.** The survey beneath this paper swept nine categories: harvest-now-decrypt-later; migration-timeline analysis in the Mosca lineage; cryptoperiod and key-management practice; retroactive de-anonymisation; quantum resource estimation for elliptic-curve discrete logarithms; the wiretap lineage's treatment of time; everlasting and long-term guarantees, including prior SoKs on expiring guarantees; differential privacy under continual observation; and adjacent work on existence leaks, leakage-resilient zero knowledge, and quantitative information flow. Forty-one works and primary records were resolved to a live publisher page, index entry, or DOI, including the nearest published neighbour to this paper's central definition, which is engaged in Section 5.1 (Kagai, Branch, But and Allen 2025). One further candidate work could not be bibliographically resolved (no resolvable venue or author list); it is excluded from citation and flagged where relevant (Sections 5.1 and 8).

**Inclusion criterion.** A work enters the survey if it gives confidentiality, anonymity, or reconstruction a time axis: a guarantee that decays, a lifetime that is declared or compared, an adversary that improves, or a construction whose purpose is to survive such improvement.

**Organising question.** For each family we ask where time enters the guarantee. Three answers occur: time enters through the releases (more output accumulates against a fixed adversary, the continual-observation regime); through the channel (the channel itself varies while the adversary class is fixed, the fading regime); or through the adversary (the recorded output is fixed and the decoder class grows, the archival regime). The ratio R(t) formalises the third answer, which is the one the surveyed families instantiate and the one the formal lineages have not treated as an object (Section 5.7).

**Claim discipline.** Every claim in this paper is fenced by a prior-art novelty ledger built before drafting: assertions presented as new are stated no wider than the ledger's wording; assertions the literature anticipates are framed as synthesis with the anticipating work cited. Conjectures are stated as conjectures with their register identifier in the research programme's conjecture register and a qualitative statement of their evidence status; no conjecture is presented as a result. Negative findings, including the absence of support for the open problem of Section 7, are reported with the same prominence as positive ones.

## 3 Model and Preliminaries: the Time-Indexed Reconstruction Bound

### 3.1 Notation and system model

Random variables are uppercase; H(X) is Shannon entropy in bits and I(X;Y) mutual information, with standard definitions per Cover and Thomas (2006). The source X is the data subject's protected information, taking values in a finite alphabet 𝒳 with |𝒳| ≥ 3 and H(X) > 0, and with H(X) fixed by the source at disclosure time [E2-C02]. The disclosure architecture routes data flow through two agents: a boundary agent S, which mediates the subject's outward disclosures, and a delegation agent M, which performs delegated processing.[^spec] Their outward-facing outputs are Y_S and Y_M. An adversary observes the outputs available to its class and attempts to reconstruct X; for an estimator X̂ of X from the observed outputs, P_e := Pr[X̂ ≠ X] denotes its error probability. C_S(t) and C_M(t) denote the effective capacities of the two channels with respect to the strongest adversary class available at time t; capacity here is the adversary-relative effective capacity of each output channel for information about X, a notion whose formalisation is taken up in Section 4 (Definition 3) [E2-C02][E2-C04].

[^spec]: The disclosure architecture and its running model are maintained publicly at https://agentprivacy.ai/model. This is the only non-literature URL this paper carries, per its claim discipline.

### 3.2 Assumptions

**Assumption 1 (non-collusion).** I(Y_S; Y_M | X) = 0, and no third channel carries the inter-agent residue: the two outputs are conditionally independent given the source, and the architecture provides no side channel that recreates their joint structure [E2-C01].

**Assumption 2 (declared adversary class).** The capacities C_S and C_M are evaluated against a stated adversary class, declared together with any bound derived from them; against that class the channel leakages about the source are bounded as I(X; Y_S) ≤ C_S and I(X; Y_M) ≤ C_M [E2-C01]. (Definition 3 in Section 4 states what "evaluated against a class" is required to mean for these bounds to be well defined; no result in this section uses more than the two displayed inequalities.)

### 3.3 The conditional floor and the deficit condition

**Proposition 1 (capacity-sum bound and conditional error floor).** Let X take values in a finite alphabet 𝒳 with |𝒳| ≥ 3, and let Assumptions 1 and 2 hold, so that I(X; Y_S) ≤ C_S and I(X; Y_M) ≤ C_M against the declared class. Write R_max := (C_S + C_M)/H(X). Then:

(a) *(capacity-sum bound)* I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M) ≤ C_S + C_M, with equality in the first inequality if and only if I(Y_S; Y_M) = 0;

(b) *(error floor)* every estimator X̂(Y_S, Y_M) satisfies

> P_e ≥ (H(X) − C_S − C_M − 1) / log(|𝒳| − 1),

and if moreover H(X) ≥ log(|𝒳| − 1) (in particular if X is uniform on 𝒳), then

> P_e ≥ 1 − R_max − 1/H(X).

[E2-C01]

*Proof.* (a) By the chain rule, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M | Y_S). The interaction identity I(X; Y_M) − I(X; Y_M | Y_S) = I(Y_S; Y_M) − I(Y_S; Y_M | X) (both sides equal the co-information of the triple) gives, under Assumption 1, I(X; Y_M | Y_S) = I(X; Y_M) − I(Y_S; Y_M) ≤ I(X; Y_M), with equality exactly when I(Y_S; Y_M) = 0; Assumption 2 supplies the outer bound. (b) Fano's inequality (Fano 1961; Cover and Thomas 2006) gives H(X | Y_S, Y_M) ≤ h(P_e) + P_e log(|𝒳| − 1) ≤ 1 + P_e log(|𝒳| − 1), with h the binary entropy. Substituting H(X | Y_S, Y_M) = H(X) − I(X; Y_S, Y_M) ≥ H(X) − C_S − C_M by (a) and rearranging gives the first display. For the second: when H(X) − C_S − C_M − 1 ≥ 0 and H(X) ≥ log(|𝒳| − 1), the first display's right side is at least (H(X) − C_S − C_M − 1)/H(X) = 1 − R_max − 1/H(X); when H(X) − C_S − C_M − 1 < 0 the second display's right side is negative and the bound holds trivially. ∎

*Attribution.* Neither part of Proposition 1 is new, and this paper claims neither as a contribution. Part (a) is the standard sub-additivity of leakage under conditional independence, the summation regime of the wiretap lineage (Wyner 1975; Leung-Yan-Cheong and Hellman 1978), whose general single-eavesdropper form is the broadcast channel with confidential messages (Csiszár and Körner 1978). The failure of the summed bound under collusion needs no citation: it is the elementary fact that joint information can exceed the sum of marginal informations once the outputs correlate beyond what the source explains, and the interaction identity in the proof of (a) locates the excess exactly (Section 8, assumption failure). Part (b) is the Fano converse in its source-coding form (Fano 1961; Cover and Thomas 2006). The proposition is recorded as a restated known-bound pair with its exact hypotheses; the claim this paper makes is confined to the decomposition reading below [N2]. A precision note: the floor is often quoted in the rounded form P_e ≥ 1 − R_max; the exact converse carries the additive 1/H(X) term and the alphabet-entropy hypothesis of (b), and only the exact form is asserted here.

The decomposition that this paper isolates as its second contribution is what Proposition 1 does not say. The two preconditions do not by themselves place R_max below one [E2-C01]. The strict bound R_max < 1 holds exactly when, additionally, the **capacity-deficit condition** holds:

> C_S + C_M < H(X),

a measurable, declarable, numerical fact about a given system and adversary class, not a consequence of the architecture [E2-C01]. (At the level of hypotheses the equivalence is definitional, since R_max is the deficit ratio; its content is the separation of obligations: Assumptions 1 and 2 are attestable properties of a deployment, while the deficit is a numerical comparison that no architectural property entails.) The deficit condition is deliberately not listed as a third assumption: two conditionally independent channels of sufficient combined capacity satisfy both assumptions with R_max at or above one, and at R_max ≥ 1 the error floor of Proposition 1(b) is vacuous, which is exactly why the deficit condition must be declared alongside the preconditions wherever the strict bound is claimed [E2-C01]. Per this discipline, no passage of this paper states R < 1 without its preconditions and its time index.

### 3.4 The time index and the shelf life

**Definition 2 (reconstruction ratio and shelf life).** Fix a disclosure time t_0 and, for each t ≥ t_0, let C_S(t) and C_M(t) be the effective capacities of the two channels against the strongest adversary class available at time t, with H(X) fixed by the source at t_0. The reconstruction ratio is

> R(t) = (C_S(t) + C_M(t))/H(X), t ≥ t_0,

and the shelf life of the guarantee is

> t* = sup{t ≥ t_0 : R(t) < 1},

with two conventions: t* = ∞ if R(t) < 1 for all t ≥ t_0, and t* undefined (the guarantee never held) if {t ≥ t_0 : R(t) < 1} is empty [E2-C02][N1].

**Remark 1 (what the supremum does and does not assert).** Definition 2 takes the supremum reading deliberately, and it is the weaker of the two available readings. What it asserts is exact: by definition of the supremum, R(t) ≥ 1 for every t > t*, so no time after t* satisfies the deficit condition. What it does not assert is equally exact: absent further hypotheses, R(t) < 1 need not hold for all t ∈ [t_0, t*], since a non-monotone R may reach one and return below it before t*; the interval up to t* is not certified, only the region beyond t* is excluded. The first-crossing quantity inf{t ≥ t_0 : R(t) ≥ 1} is not used anywhere in this paper, and no statement below depends on the two readings coinciding. They coincide exactly when {t : R(t) < 1} is an interval with left endpoint t_0, in particular whenever R is non-decreasing; and whether R is non-decreasing is precisely the ordering question of Section 4, where Lemma 1 derives monotonicity from the ordered-family hypothesis, which is a hypothesis about adversary classes, not an established fact. The behaviour of t* under a non-monotone R is therefore an open question of the formalisation programme, recorded here rather than assumed away.

**Remark 2 (availability semantics).** Definition 2's phrase "the strongest adversary class available at time t" admits two readings, and this paper fixes the first: D_t is the class of decoders realisable by some adversary at time t, whether or not the enabling methods are published; the publicly documented capability trajectory is an auditor's lower estimate of D_t. The archival regime forces this reading: an adversary holding the recording decodes it with whatever capability it has, disclosed or not, so a ratio evaluated against publicly available capability alone would certify a guarantee that an undisclosed capability had already voided. Two consequences follow and are used below. First, R(t) and t* are properties of realisable capability and are therefore not directly observable: any computed shelf life is an estimate of t* built from the auditor's lower estimate of {D_t}, and the estimation error is in the unsafe direction, since understating D_t overstates t*. Second, a disclosure or attestation of an already-realised capability moves the auditor's estimate of R(t), not R(t) itself; where publication additionally extends what other adversaries can realise, that propagation is a distinct, subsequent growth of D_t. Conjecture 1's coupling of drift to release events is a claim about this propagation mechanism; Section 5.8's withheld-capability episode is read against these semantics in place, and the attestation discount of Conjecture 4 acts on the planner's estimate of the horizon, not on the derived crossing [E2-C02][E2-C04].

**Remark 2b (two mechanisms of growth, and two clocks).** The family {D_t} grows through two mechanisms that this survey keeps distinct, because they erode different things. The first is method-and-compute growth: better estimators, better solvers, more resources. For computationally protected channels (the cryptoperiod and harvest-now-decrypt-later families of Section 5.3) this mechanism genuinely erodes the protection; for a channel whose leakage bound is information-theoretic it cannot, since such a bound already holds against unbounded computation, and what it moves instead is the certified estimate of the capacities, the auditor's quantity of Remark 2. The second is side-information growth: the adversary's auxiliary corpus and priors accumulate, so every decoder in the class works from more background than before. This mechanism erodes even information-theoretic floors, and it is the one the retroactive de-anonymisation record of Section 5.4 instantiates. The companion theory paper carries the second mechanism as proved material: with B_t the adversary's accumulating background (accumulation ordered in t, Markov B_t → X → T against source X and transcript T), the disclosed transcript's leakage bound survives conditioning while the Fano floor erodes through the residual entropy H(X | B_t), so the informed deficit condition reads C_S + C_M < H(X | B_t) and the erosion requires no growth in what the transcript reveals [E2-C02][E2-C04]. Where a passage below speaks of drift without qualifying its mechanism, the load-bearing mechanism for information-theoretically bounded disclosures in the archival regime is the second.

The decomposition of Section 3.3 makes the time-dependence precise: the deficit condition, not the preconditions, is the time-indexed quantity. R(t) can cross one with both preconditions intact; what expires at t* is the deficit condition, not the architecture [E2-C01]. This is the formal shape of the archival regime: the recording is fixed, the assumptions under which it was made can remain true forever, and yet no time beyond t* satisfies the declared deficit against the then-strongest adversary class.

The distinction against declared lifetimes is the content of the first contribution [N1]. A cryptoperiod (Barker 2020) and the security shelf life x of Mosca's planning inequality (Mosca 2018) are requirements stated by the data owner; the vulnerability-window comparisons of the harvest-now-decrypt-later literature compare a declared confidentiality lifetime against a projected decryption horizon. In Definition 2, t* is derived from the architecture's declared capacities and the adversary-class trajectory: the inputs are declared quantities (Section 8), and the crossing time, given them, is computed, not chosen.

## 4 The Ordered Adversary Family: a Formalisation Programme

### 4.1 The programme

Definition 2 uses the phrase "strongest adversary class available at time t". For the ratio to be an object rather than a metaphor, that phrase requires formalisation as an ordered family of decoder classes {D_t}, with D_t ⊆ D_t' whenever t ≤ t', so that later adversary classes can do everything earlier ones could [E2-C04]. The natural grounding is quantitative information flow, where adversaries are modelled by gain functions and leakage is quantified against them, with capacity as a worst case over gain functions (Alvim et al. 2012; Alvim et al. 2020). We give the grounding at definition level, prove the one structural lemma it licenses, and then state exactly what remains open; the boundary between the structural and the empirical content below is the boundary of the claim [N3][E2-C04].

**Definition 3 (decoder class; effective capacity relative to a class).** A *decoder class* D is a set of adversary models in the sense of quantitative information flow: each element d ∈ D specifies a gain function g_d (Alvim et al. 2012) together with the strategy resources permitted in realising a g_d-optimal attack. A *capability-indexed family* is a map t ↦ D_t from times to decoder classes. Let ℓ be a leakage functional, valued in bits, defined per adversary model, and subject to the *compatibility requirement*: for every model d and every estimator X̂ realisable by d from a channel output Y, I(X; X̂(Y)) ≤ ℓ_d(X → Y). The *effective capacity* of a channel with output Y against the class D is

> C(Y; D) = sup_{d ∈ D} ℓ_d(X → Y),

and Definition 2's capacities are C_S(t) = C(Y_S; D_t), C_M(t) = C(Y_M; D_t) [E2-C02][E2-C04]. The compatibility requirement is the minimum a witness for the functional ℓ must satisfy, and what it secures is exactly per-channel: every estimator realisable within the class from a single channel output Y extracts at most C(Y; D) bits about X. Two things it does not secure, and this definition does not claim, are Assumption 2's displayed inequalities read with these effective capacities, which remain a substantive assumption on the class-channel pair and can fail precisely when the effective capacity sits below the true mutual information, and the extension of Proposition 1's floor to estimators of X from the joint output (Y_S, Y_M), which needs in addition a sub-additivity clause for ℓ across conditionally independent channels that is nowhere required here. What a finished definition must additionally deliver, per item (ii) of the empirical residue below, is that joint-estimator floor: until a functional delivering it is exhibited, Proposition 1's floor evaluated with effective capacities is a desideratum of the programme, not a consequence of the compatibility requirement.

**Lemma 1 (structural monotonicity).** Let t ↦ D_t be a capability-indexed family satisfying the *ordering hypothesis*: D_t ⊆ D_t' whenever t ≤ t'. Then C(Y; D_t) ≤ C(Y; D_t') for each channel, hence R(t) is non-decreasing; consequently {t ≥ t_0 : R(t) < 1} is, when nonempty, an interval with left endpoint t_0; and whenever both {t ≥ t_0 : R(t) < 1} and {t ≥ t_0 : R(t) ≥ 1} are nonempty, so that t* is defined and finite, the supremum of Definition 2 equals the first-crossing quantity inf{t ≥ t_0 : R(t) ≥ 1}. (If only the sub-unity set is nonempty, t* = ∞; if the sub-unity set is empty, t* is undefined by Definition 2's convention while the first-crossing quantity is t_0, so the equality clause is not asserted there.)

*Proof.* A supremum over a larger set is no smaller, so each effective capacity is non-decreasing in t under the ordering hypothesis, and R(t), a sum of non-decreasing functions over the positive constant H(X), is non-decreasing. For non-decreasing R, if R(s) < 1 and t_0 ≤ t ≤ s then R(t) < 1, so the sub-unity set is an interval with left endpoint t_0. Let τ = sup{t : R(t) < 1} and σ = inf{t : R(t) ≥ 1}, both sets nonempty. For every t > τ, R(t) ≥ 1, so σ ≤ τ + δ for every δ > 0, giving σ ≤ τ. Conversely, for every t < τ there is, by definition of the supremum, an s ∈ (t, τ] with R(s) < 1, hence R(t) ≤ R(s) < 1 by monotonicity; so every member of {t : R(t) ≥ 1} is at least τ, giving σ ≥ τ. ∎

Under the ordering hypothesis, then, the monotone non-decrease of R(t) against a fixed archive is structural, the two readings of t* in Remark 1 coincide, and the empirical content of any drift claim reduces to the rate of increase, not its sign [E2-C04][N3].

**The empirical residue, stated exactly.** What Lemma 1 does not supply is the programme, and it is threefold. (i) *The ordering hypothesis itself.* That later adversary classes can do everything earlier ones could is plausible under non-regression of published methods, but it is a modelling assumption about capability, not a theorem; capability can in principle regress (methods lost, compute repriced), and no result above survives such regress. (ii) *The functional ℓ.* The compatibility requirement of Definition 3 is stated, not discharged: the QIF candidates (g-leakage, Bayes capacity and its logarithm) quantify leakage against gain models, but a bit-valued functional calibrated against source entropy, uniformly over a class, such that the Fano argument of Proposition 1 survives the substitution of effective for information-theoretic capacities against estimators from the joint output, for instance via a sub-additivity clause across conditionally independent channels, has not been exhibited; this is the exact missing step between Definition 3 and a finished definition, and it is the delivery named at the definition's close. (iii) *Instantiation.* No published adversary series is presently expressed as a nested gain-function family: QIF adversary models are per-scenario and unordered in time, continual-observation differential privacy fixes the adversary while releases grow (Dwork et al. 2010), and the quantum resource-estimate literature provides point estimates without treating the series as an ordered process (Sections 5.7 and 5.8). The programme is contingent in the following sense: if (i) fails for the adversary classes of interest, or (ii) admits no witness, then decoder classes cannot be coherently ordered as gain-function families, the monotonicity of Lemma 1 demotes from a structural fact to a modelling assumption, this paper's fourth section demotes with it to a discussion, and Remark 1's supremum reading becomes load-bearing rather than merely cautious [E2-C04][N3].

### 4.2 The drift conjecture

That guarantees erode against fixed archives is not a conjecture; it is the shared observation of the harvest-now-decrypt-later corpus, the everlasting-privacy motivation, and the retroactive de-anonymisation record surveyed in Section 5 [S1]. What the research programme adds, and holds at conjecture status, is a claim about the driving process:

**Conjecture 1 (informational-capability drift; programme register C82 as re-typed 2026-07-17, moderate confidence, rate unestablished).** Adversary informational capability grows against fixed archives: the linkage corpus and side priors accumulate along calendar time, shrinking H(X | B_t) while nothing is added to the archive and no action of the data subject is involved; R(t) drifts upward on a schedule, and every static reconstruction guarantee has a finite shelf life t* [E2-C03]. Frontier-model releases enter only informationally, through improved extraction of linkage from existing corpora, never as computation against the information-theoretic guarantee, which is compute-saturated. In the terms of Definition 3, the claim is that the realised family trajectory t ↦ D_t grows as background accumulates and that the growth strictly increases the effective capacities against fixed archives. *Proof obligation:* the erosion form is proven conditional in the companion (Definition 3.9 and Corollary 5.4b); what remains conjectural is the rate: a formalised accumulation model and at least one measured capability series showing capacity increase attributable to background growth against a fixed archive; the two verified 2026 instances of Section 5.8 are consistent with the conjecture but constitute a single year's cluster, not a series. *Mechanism typing (Remark 2b):* the component of any such drift that bears on an information-theoretically bounded disclosure is the informational one; the register's re-typing of the conjecture to that mechanism was executed 2026-07-17.

## 5 The Surveyed Families Under the Bound

Each family below is read against Definition 2: which component of R(t) does the family vary, declare, or construct against?

### 5.1 Harvest-now-decrypt-later: the deficit condition as economics

The HNDL literature is the archival regime stated as a threat economics. Blanco-Romero et al. (2026) reframe HNDL as an economic problem and quantify adversary storage and collection costs across TLS 1.2/1.3, QUIC and SSH with an open testbed; the adversary is indexed by cost, not by decoder class, and no shelf-life quantity is derived from architecture. A Federal Reserve Board analysis of distributed-ledger data (FEDS 2025-093) notes that ledger immutability makes the archive term irreducible, which in the terms of Section 5.6 is the statement that an archive that cannot be erased has no t-independent term [E2-C11 contrast]. In R(t) terms, HNDL is the observation that C(t) will cross the deficit threshold for recorded ciphertext and that collection is rational before the crossing; what the family does not contain is a ratio against source entropy or a derived t* [N1 residue].

The nearest published neighbour to Definition 2's purpose is the temporal-risk model of Kagai, Branch, But and Allen (2025), which presents itself as the first formal model of the HNDL adversary: a resource-accumulating attacker specified by collection capability, deferred decryption power and a temporal horizon, with compromise stated as the lifetime-versus-horizon condition Ld > Ha, a time-indexed compromise probability Pr{Ha(t) ≥ Ld} (written R(t) there; the symbol names a probability, not this paper's capacity-to-entropy ratio), break-time curves parameterised by hardware trajectories (logical qubits, error-correction overhead), and a sectoral exposure window W = max(0, Ld − Ha(t_mig)) under which hybrid and forward-secure mechanisms reduce the modelled risk horizon by over two-thirds. Read against Definition 2, the work is the archival regime formalised as risk arithmetic over declared quantities: the confidentiality lifetime Ld is a regulatory or sectoral retention input, the horizon Ha(t) is a projected scalar under scenario curves, and neither is derived from the disclosing architecture; there is no ratio against source entropy, no derived shelf life, and no ordering of decoder classes, the adversary being indexed by a single horizon rather than by a growing class of estimators. It therefore instantiates this family rather than anticipating the object: t* is the computed counterpart of its projected Ha, derived from declared channel capacities and an adversary trajectory rather than adopted from forecast baselines [N1 residue][N3 residue]. A further work, a preprint reported to formalise the same lifetime-versus-horizon condition, is bibliographically unresolved (no resolvable venue or author list) and is therefore not cited; it is the one open referee risk of this kind for the unification claim (Section 8).

### 5.2 Migration timelines: the horizon as elicited input

Mosca's inequality, x + y > z (security shelf life plus migration time exceeding the collapse horizon), is the planning rule of the transition literature (Mosca 2018), and the Quantum Threat Timeline series supplies z as expert-elicited probability distributions (Mosca and Piani 2024), with the sharpest upward shift of the series in its most recent edition (Mosca and Piani 2025) [E2-C03 grounding]. All three quantities are declared or elicited; none is derived from system structure. In the terms of this paper, Definition 2's t* plays the role of z, not of x: it is the architecture's computed collapse horizon for a given adversary trajectory. The cryptographic-agility literature systematised by Näther et al. (2024) addresses y, the cost of changing cryptography under threat evolution; it measures switching cost, not any property of the protected data trajectory, which distinguishes it from the open problem of Section 7. Public capability rulers such as the graded ECDLP challenge ladder of Dallaire-Demers, Doyle and Foo (2025) instrument the adversary trajectory itself, which sits upstream of any particular channel's effective capacity, and are, in this paper's terms, measurement infrastructure for the adversary family of Section 4.

### 5.3 Cryptoperiods: the declared lifetime

NIST key-management practice bounds key lifetimes administratively, typically at one to three years (Barker 2020). This is a weak anticipation of the shelf-life idea: institutional practice already treats protection as time-bounded [S1 adjacency]. The distinction is categorical, not quantitative: cryptoperiods bound key usage, and rotation does nothing for already-exfiltrated ciphertext, which is exactly the regime R(t) addresses; the guarantee over the archive is untouched by rotating the key that produced it.

### 5.4 Retroactive de-anonymisation: measured instances of capability drift

This record is the empirical backbone of the archival regime. Netflix Prize microdata released as perturbed and safe was re-identified when auxiliary data arrived (Narayanan and Shmatikov 2008). Anonymised genomes were re-identified through public genealogy databases that did not exist at scale when the data was shared (Gymrek et al. 2013), and long-range familial search made a majority of a large population identifiable through relatives' enrolment, coverage growing without any action of the subjects (Erlich et al. 2018), a sharp instance of third-party growth eroding a guarantee whose issuing assumptions never changed [S1]. Generative models estimate re-identification success against incomplete releases (Rocher et al. 2019), and mobility traces identify most individuals from four spatio-temporal points (de Montjoye et al. 2013), which calibrates how small H(X) can be relative to auxiliary channels [E2-C02 intuition]. Read against Section 4: Rocher et al. is the nearest methodological neighbour to the decoder-class idea, predicted reconstruction success under an explicit attacker model, but the attacker model is static; the family {D_t} is exactly what is missing [E2-C04][N3 residue]. Read against Remark 2b, this family is the record of the second mechanism: the transcript of each release was fixed, no decoder became cleverer in any way the issuing guarantees priced, and what grew was the background corpus against which the release was decoded. The companion theory paper's erosion result is this mechanism stated exactly, the floor falling through H(X | B_t) while the leakage bound on the release itself stands intact [E2-C02].

### 5.5 Differential privacy under continual observation: the dual problem

Continual-observation differential privacy gives privacy a time axis in which the releases accumulate against a fixed adversary (Dwork et al. 2010; Chan, Shi and Song 2011), with tight continual-release costs still an active topic (Jain et al. 2023). The archival regime is the dual: one release, fixed transcript, growing decoder. The two regimes compose in deployed systems, but the dual problem, a fixed transcript decoded by tomorrow's adversary, is not posed in this strand, and the distinction is load-bearing for what "privacy over time" means in each [N7 positioning].

### 5.6 Everlasting constructions: the t-independent term

The everlasting-privacy line owns the observation that only unconditional protection is independent of t [S2]. Moran and Naor (2006) coin everlasting privacy for vote secrecy against later, computationally unbounded adversaries, motivated exactly by the ageing of computational assumptions; Aumann, Ding and Rabin (2002) achieve everlasting security against any future advance provided the adversary's storage was bounded at transmission time, a constructive answer to drift within its model; Unruh (2013) gives the composable form and locates what cannot be made everlasting classically; and Haines et al. (2023) systematise the e-voting protocols with everlasting privacy, the only prior SoK on time-robust privacy guarantees we found. The long-term archiving survey of Vigil et al. (2015) covers renewal architectures for integrity, authenticity and proof of existence, with confidentiality explicitly out of scope.

Read against Definition 2, these constructions engineer terms of the capacity sum to zero against all future classes, which is the only way to make a term of R(t) constant in t [S2][E2-C11]. The research programme's related design claim is that structural context erasure between agent invocations, distinguished as Grade-2 forgetting (mathematically unrecoverable) from Grade-1 hiding (recoverable with keys), removes the archive term entirely; the Grade-1/Grade-2 naming is offered as terminology, and the placement of an erasure term inside the R(t) decomposition is, per the novelty fence, the only part of this not owned by the everlasting lines [E2-C11][S2]. The deep version of the erasure claim, a non-vanishing obstruction to gluing local views into a global witness, is carried in the programme register as C86 at low confidence with its machinery unconstructed, and is mentioned here only to state that it is not used anywhere in this paper [E2-C11].

### 5.7 The wiretap lineage and time: the missing regime

The lineage that supplies Proposition 1's machinery fixes the adversary with the channel (Wyner 1975; Leung-Yan-Cheong and Hellman 1978; Csiszár and Körner 1978). The closest it comes to a time axis is the fading-channel analysis of Gopala, Lai and El Gamal (2008), where the channel varies in time and the eavesdropper is known only statistically. The contrast is exact and, to our knowledge, unremarked: in the fading regime the channel varies while the adversary class is fixed; in the archival regime the recorded channel output is fixed while the adversary class varies. The regime in which an adversary decodes yesterday's recording with tomorrow's decoder is outside the lineage's model, and Definition 2 is our proposal for its missing object [N7][E2-C02].

### 5.8 Two 2026 instances (verified record, presented as evidence)

Both instances below are verified public record and are presented as evidence for the archival regime, never as contributions of this paper [S4].

**Proof-system soundness under improved audit capability.** A soundness flaw in the Zcash Orchard shielded protocol, a missing constraint in variable-base scalar multiplication in halo2_gadgets, was present from Orchard's activation in May 2022; multiple prior audits, including audits assisted by earlier AI models, did not find it (BlockSec 2026; CRYPTO ISAC 2026); it was found on 2026-05-29 by Taylor Hornby (Shielded Labs audit) using a frontier model released the previous day (BlockSec 2026), with proof-of-concept counterfeiting demonstrated in local testing (CRYPTO ISAC 2026); an emergency soft fork followed on 2026-06-02 (block 3,363,426) and the NU6.2 hard fork on 2026-06-03 (block 3,364,600); no evidence of exploitation exists, and, because of the pool's privacy properties, non-exploitation cannot be cryptographically proven [E2-C05] (Zcash Foundation 2026; BlockSec 2026; CRYPTO ISAC 2026). Read against the model: the archive (the chain) was fixed; audit capability moved with a model release; the guarantee's effective status changed with no action by any data subject [E2-C03 instance].

**Withheld capability with attested existence.** Google Quantum AI published (2026-03-31) a roughly tenfold improvement, in spacetime volume over best prior single-instance estimates, in Shor-algorithm resource requirements for secp256k1, withholding circuit-level methods and publishing instead a zero-knowledge proof of the claimed resource counts (Babbush et al. 2026); the prior baseline series into which this lands is public and steep (Roetteler et al. 2017; Gidney and Ekerå 2021; Litinski 2023; Chevignard, Fouque and Schrottenloher 2025; Gidney 2025). An independent reconstruction reached parity roughly two months later (Schrottenloher 2026), its author noting that the original relied on a zero-knowledge proof in place of revealed circuits; the same day, a first-person account disclosed that the core technique had been held internally for roughly a year under publication restriction (Gidney 2026); and an open challenge, using the published zero-knowledge verifier as its automatic scoring filter, subsequently exceeded the withheld benchmark (ecdsa.fail record, 2026) [E2-C07]. The metric qualification travels with the figure wherever this episode is repeated: the tenfold claim is the paper's own, in spacetime volume; per-axis factors reported elsewhere differ. Read explicitly against the availability semantics of Remark 2: on the realisable-capability reading, D_t contained the withheld technique from its internal discovery onward, so for the roughly one year of restriction every public estimate of the affected R(t) ran below its realised value and correspondingly overstated t*; the attestation of 2026-03-31 moved the auditor's estimate, not the ratio; and the independent reconstruction two months later is the distinct propagation event of Remark 2, the point at which the capability became realisable beyond its originating holder. This episode is the instance behind Section 6 [E2-C07][E2-C08 instance].

### 5.9 Adjacent empirics: multi-agent leakage

The measured leakage of multi-agent LLM systems is external empirical work and enters this survey as context for why the two-channel architecture of Section 3 is the unit of analysis: sequential composition compounds leakage up to (2^N - 1) epsilon across N agents, with measured mutual information roughly doubling from two to five agents (Asif and Amiri 2026), and a benchmark across 4,979 traces on five production LLMs measures inter-agent channel leakage in the high-sixties per-cent range of traces (El Yagoubi, Badu-Marfo and Al Mallah 2026) [E2-C12][S6]. These are measurements of leakage in deployed compositions, not capacity attestations, and they bound neither term of Definition 2; they motivate the non-collusion assumption's centrality (Section 8).

## 6 The Existence-Leak Law and the Attestation Discount

The second 2026 instance raises a question the disclosure literature does not answer: what does a zero-knowledge proof of capability existence itself disclose? The attesting paper treats withholding plus attestation as responsible disclosure (Babbush et al. 2026) and does not model what the existence proof leaks; the reconstruction paper reports parity but does not quantify how much the attestation accelerated it (Schrottenloher 2026). That gap is the territory of this section [N4].

### 6.1 The existence-leak conjecture

**Conjecture 2 (existence-leak law; programme register C81, held open pending a second independent instance).** *Candidate model.* Fix a probability space (Ω, ℱ, P) carrying a random variable M with values in a countable method space ℳ, representing the adversary's prior uncertainty over which technique, if any, achieves the capability; a cost functional c : ℳ → ℝ₊ ∪ {∞}, the resources the method requires against the stated instance; and, for an attested resource level τ, the feasibility indicator F_τ := 1{c(M) ≤ τ}. A *capability attestation at level τ* is a verifiable disclosure of the event {F_τ = 1} that reveals no other function of M; a zero-knowledge proof of claimed resource counts is the instance class. *Statement.* For capability attestations, I(F_τ; M) > 0: a zero-knowledge proof that a capability is feasible leaks a nonzero upper bound, namely τ, on the reconstruction or search difficulty of the method. *Scope fence:* the conjecture concerns capability attestations; instance attestations, such as a proof that a particular transaction is valid, are out of scope. *Floor and object distinction:* the impossibility of leakage-resilient zero knowledge below leakage parameter one (Garg, Jain and Sahai 2011) shows the protocol-internal analogue cannot be driven to zero. Formally, the two results concern different random variables: Garg, Jain and Sahai bound the information a verifier obtains about the witness W of a single interactive execution through a leakage oracle, a protocol-internal quantity, whereas Conjecture 2 concerns I(F_τ; M), the information the public feasibility event carries about the method across systems; neither quantity bounds the other, and the cross-system form is, to our knowledge, unclaimed in this literature [E2-C08][N4]. *The named missing step.* Under the candidate model the bare inequality is immediate whenever the prior makes F_τ non-constant: F_τ is then a non-constant function of M, so I(F_τ; M) = H(F_τ) > 0. Stated so, the law would be true and empty. The conjectural content is operational, and the proof obligation is correspondingly: (i) an attestation class and an adversary search model in which the claim is non-vacuous, that is, in which conditioning on {F_τ = 1} provably and quantifiably reduces the expected search cost of reaching parity with the attested capability; and (ii) a second independent instance, the register's own bar for raising the conjecture's status. *Evidence:* the 2026 episode of Section 5.8, in which parity followed attested existence in roughly two months and the attestation's verifier became the search's scoring function [E2-C07].

### 6.2 The liveness instance and deduplication side channels

The deduplication side-channel literature substantially anticipates the confirmation mechanism that the programme's design surface re-derives, and is cited here as such per the novelty fence [S3]. Harnik, Pinkas and Shulman-Peleg (2010) showed that cross-user deduplication lets a client confirm whether specific content already exists server-side, feasible exactly over guessable candidate spaces. The programme's claim extends this to content addressing: a live content address is an existence claim about its content; under deduplication, an adversary holding a candidate confirms existence by comparing the candidate's hash against a known-live address; the address does not leak the content, but the liveness of the address leaks the existence of the content, and existence bounds the search. The scope limit is inherited unchanged from Harnik et al.: a guessable candidate space; for high-entropy content the upper bound still leaks while recovery may remain infeasible [E2-C15]. The residue not owned by the prior work, per the fence, is cross-system corroboration and subsumption under Conjecture 2:

**Conjecture 3 (corroboration monotonicity; programme register C93, moderate confidence).** Fix a candidate space 𝒞 for the content of a known-live address and a corroboration model in which k independent systems each resolve the same address; let Δ_k(X) denote the reconstruction difficulty of the content, valued as the adversary's expected search cost over 𝒞 given the k resolutions. (The source of this claim writes the difficulty as D(X); the symbol is changed here to avoid collision with the discount functional D(a) of Conjecture 4.) The conjecture: under a fixed corroboration model, Δ_k(X) is monotone non-increasing in k [E2-C14][E2-C15]. *Proof obligation:* the fixed corroboration model itself: a joint law over candidate spaces and resolver behaviour under which each additional independent resolution weakly narrows the candidate space, together with a proof of the comparison Δ_{k+1}(X) ≤ Δ_k(X) within it. Under such a model the programme additionally expects a steep-then-shallow profile in k, which is not asserted here beyond monotonicity. *Remark:* the genealogy-database record of Section 5.4 (Gymrek et al. 2013) is a naturally occurring instance of the monotonicity, each new database narrowing the candidate space.

### 6.3 The attestation discount on migration horizons

**Conjecture 4 (attestation discount; programme register C84, weaker evidentiary support than Conjectures 1 to 3).** Let 𝒜 be a space of public feasibility attestations, preordered by specificity: a ⪯ a' when a' verifiably discloses at least every feasibility event a discloses, with ⊥ ∈ 𝒜 the null attestation. Call D : 𝒜 → [0, ∞) a *discount functional* if it satisfies (D1) normalisation, D(⊥) = 0; (D2) monotonicity in specificity, a ⪯ a' implies D(a) ≤ D(a'); and (D3) domination by disclosure, D(a) ≤ D(a_full) for every a, where a_full is full method publication. The conjecture: Z_b' = Z_b − D(a): horizon updates in Mosca-style planning are described by some discount functional D with D(a) > 0 for every non-null capability attestation, independently of any actual attack. Here Z_b is the planner's estimate of the collapse horizon, for which the shelf life t* of Definition 2 is the derived referent: per Remark 2, an attestation of an already-realised capability moves the estimate and not the derived crossing, so the discount acts on Z_b as an estimate; no claim is made that attestation moves t* itself [E2-C09][N5]. The Mosca lineage updates its horizon by expert belief (Mosca 2018; Mosca and Piani 2024); no found work formalises attestation-induced discounting, and the harvest-now-decrypt-later economics (Blanco-Romero et al. 2026) prices collection, not attestation. *Status of the axioms:* (D1) to (D3) are what the schema requires to be well posed; they do not determine D, and the conjecture is held at schema level until a concrete D is identified. *Proof obligation:* an elicitation or market study identifying a discount functional consistent with observed horizon updates causally attributable to attestations rather than to demonstrated attacks. Stated as a conjecture, not a result, at exactly the register's status.

### 6.4 Limitative framings (related-work status only)

The research programme also carries two readings that frame, without strengthening, the results above; both are register-carried framing conjectures, recorded by their source's own fence as structural framing rather than theorem-to-theorem reduction, and neither is used as a premise anywhere in this paper [S5]. The first (programme register C90, recorded as an observation with no reduction claimed) reads the load-bearing role of the unreconstructable remainder as an inversion of the limitative pattern in logic: an architecture whose R(t) approaches one does not merely lose a safety margin but loses the property that made the disclosure architecture valuable, on at least one axis [E2-C13]. The second (programme register C92, capped at the confidence of Conjecture 2, which it extends) reads Conjecture 2 as an undefinability phenomenon: a disclosing system cannot confine the truth of its own feasibility claim once that claim is corroborable elsewhere [E2-C14]. These framings are recorded here for completeness of the register translation. Formal-pass decision: both are retained at related-work status only. Neither admits a formal statement without a reduction their own source declines to claim, no formal statement of either is made in this paper, and neither appears in, nor is used by, the formal apparatus of Sections 3, 4 and 6.1 to 6.3.

## 7 Open Problem: Countermeasure by Divergence

The countermeasure directions surveyed above either engineer capacity terms to zero (Section 5.6), erase the archive term (Section 5.6), or reduce migration time (Section 5.2). The research programme names a fourth direction and this paper reports it strictly as an open problem, explicitly unvalidated [N6].

**Open problem (divergence outrunning drift; programme register C18 to C21, held at low confidence, unmeasured).** If the data subject's protected trajectory diverges, in the Lyapunov sense with exponent lambda > 0, from any snapshot of it, then reconstruction error from a fixed archive grows as e^(lambda t), and the design goal becomes trajectory divergence outrunning capability drift [E2-C10]. lambda is unmeasured; the programme records it as its most-needed number. We found no anticipation of this direction in the swept literature, and equally no support: the claim's confidence is low by the register's own assessment, and it earns its place in this survey only as a precisely stated open problem. The nearest neighbour is the agility literature's y (Näther et al. 2024), which measures the cost of changing the protection, not the divergence of the protected process [E2-C10].

## 8 Threats to Validity

**Construct validity.** The capacities of Definition 2 are declared quantities, not measurements: no standardised methodology exists for attesting C_S(t) or C_M(t) against a stated adversary class, and until one does, the deficit condition is checkable only as a declaration audit [E2-C01]. The multi-agent leakage measurements of Section 5.9 measure leakage of deployed compositions, not channel capacity, and do not operationalise the model's terms [E2-C12].

**Internal validity.** The evidence for Conjecture 1 is a single year's instance cluster (Section 5.8), and for Conjecture 2 a single episode; the register's own bar for raising Conjecture 2's status is a second independent instance, which has not occurred [E2-C08]. The Orchard instance's market context is deliberately omitted: the contemporaneous repricing is confounded by a concurrent, prominent institutional exit and is not attributable to the flaw alone; no price figure is carried in this paper [E2-C06 prohibition].

**External validity.** The bound of Section 3 is stated for a two-agent architecture under Assumptions 1 and 2; adversary classes outside the declared class, and architectures whose channel count or composition differs, are outside every quantitative statement in this paper. The survey is web-only, English-only, and single-session at its base; the disclosure-economics strand is touched only through one analysis (CRYPTO ISAC 2026) and non-English and paywalled venues were not systematically covered. The unification claim is made to our knowledge, and its nearest published neighbour is read and positioned rather than presumed: the temporal-risk model of Kagai, Branch, But and Allen (2025), engaged in Section 5.1, is a lifetime-versus-horizon formalisation specific to the quantum transition whose load-bearing quantities are declared or projected inputs, so it leaves the derived-ratio claim (N1) standing and does not reach the cross-domain systematisation that contribution 4 claims. One bibliographically unresolved work remains the open referee risk: a preprint reported to formalise the same lifetime-versus-horizon comparison, not cited pending resolution (Section 5.1); if on resolution it proves to derive rather than declare its quantities, the derived-ratio claim narrows as well.

**Assumption failure.** If Assumption 1 fails, collusion or a third channel recreates the inter-agent residue, the capacity-sum bound of Proposition 1(a) is unlicensed, and the floor of Proposition 1(b) with it: the conditional-independence residual is the entire content of the two-channel advantage, and the multi-agent measurements of Section 5.9 show inter-agent channels leaking in a majority of measured traces when architectures do not enforce the assumption [E2-C12]. If Assumption 2 fails, capacities evaluated against a weaker class than the operative adversary understate R(t) and overstate t*. If the deficit condition is asserted without declaration, the guarantee claim is unfounded even with both assumptions intact, since the preconditions alone never place R below one [E2-C01].

**Commitment.** A measured result against any conjecture of this paper, including a failure of the drift of Conjecture 1 to materialise against an instrumented archive, is filed to the research programme's register and reported with the same prominence as a confirmation.

## 9 Conclusion

Five literatures know that privacy guarantees over fixed archives expire; none of them says when, because none of them has an object whose value is the expiry. This paper systematised those literatures under one such object, the time-indexed reconstruction ratio R(t) and its derived shelf life t*, and separated, within the guarantee, what an architecture's preconditions buy from what only a declared and expiring capacity deficit can buy [E2-C01][E2-C02]. The apparatus is stated at its honest status: a conditional floor proved from standard machinery with its exact hypotheses stated and claimed only as a decomposition reading, an adversary-ordering programme grounded at definition level whose one structural lemma is conditional on an ordering hypothesis that remains the programme's empirical content [E2-C04], four conjectures carried at their register status with proof obligations, and one open problem whose key number is unmeasured [E2-C10]. The immediate next steps are the ones the statuses dictate: a witness for Definition 3's leakage functional delivering the joint-estimator floor of Section 4.1's residue (ii), and an instantiated ordering, or the section's demotion; a capacity-attestation methodology that would make the deficit condition auditable; and a second independent instance for the existence-leak law, which is the single observation that would most change this paper's standing.

---

## References (verified registry; bib status per canonical pv_v6.bib)

All entries below were resolved to a live record by the WP-04 prior-art sweep (2026-07-07) or are present in the canonical bibliography. All entries now resolve to keys in pv_v6.bib (61 verified entries, 0 UNVERIFIED); keys re-verified against primary records at the A4 citation pass, 2026-07-09, with the Mosca-Piani 2025 edition added under the L085(a) sanction.

- Alvim, M. S., Chatzikokolakis, K., Palamidessi, C., Smith, G. "Measuring Information Leakage Using Generalized Gain Functions." CSF 2012, pp. 265-279. [bib: pv_v6 alvim2012measuring]
- Alvim, M. S., Chatzikokolakis, K., McIver, A., Morgan, C., Palamidessi, C., Smith, G. *The Science of Quantitative Information Flow.* Springer, 2020. [bib: pv_v6 alvim2020science]
- Asif, S., Amiri, M. M. "Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems." arXiv:2603.05520, 2026. [bib: pv_v6 asif2026infotheoretic]
- Aumann, Y., Ding, Y. Z., Rabin, M. O. "Everlasting security in the bounded storage model." IEEE Trans. Inf. Theory 48(6):1668-1680, 2002. [bib: pv_v6 aumann2002everlasting]
- Babbush, R., et al. "Securing Elliptic Curve Cryptocurrencies against Quantum Vulnerabilities: Resource Estimates and Mitigations." arXiv:2603.28846; ePrint 2026/625, 2026. [bib: pv_v6 babbush2026securing]
- Barker, E. *Recommendation for Key Management: Part 1 General.* NIST SP 800-57 Part 1 Rev. 5, 2020. [bib: pv_v6 barker2020keymgmt]
- Barocas, S., Nissenbaum, H. "Big Data's End Run around Anonymity and Consent." In *Privacy, Big Data, and the Public Good*, Cambridge University Press, 2014. [bib: pv_v6 ADD barocas2014endrun; A4 verify; litreview run 04 wf_23f4f7ad-527, single motivating cite]
- Blanco-Romero, J., Almenares Mendoza, F., García Rubio, C., Campo, C., Díaz Sánchez, D. "On the Practical Feasibility of Harvest-Now, Decrypt-Later Attacks." arXiv:2603.01091, 2026. [bib: pv_v6 blancoromero2026hndl]
- BlockSec. "Zcash Orchard Soundness Bug Analysis." blocksec.com, 2026-06. [bib: pv_v6 blocksec2026zcash, record]
- Chan, T.-H. H., Shi, E., Song, D. "Private and Continual Release of Statistics." ACM TISSEC 14(3), art. 26, 2011. [bib: pv_v6 chan2011continual]
- Chevignard, C., Fouque, P.-A., Schrottenloher, A. "Reducing the Number of Qubits in Quantum Factoring." CRYPTO 2025, Springer, pp. 384-415. [bib: pv_v6 chevignard2025reducing]
- Cover, T. M., Thomas, J. A. *Elements of Information Theory.* 2nd ed., Wiley-Interscience, 2006. [bib: pv_v6 cover2006elements]
- CRYPTO ISAC. "The Zcash Orchard Bug and the New Economics of Vulnerability Discovery." cryptoisac.org, 2026-06. [bib: pv_v6 cryptoisac2026economics, record]
- Csiszár, I., Körner, J. "Broadcast Channels with Confidential Messages." IEEE Trans. Inf. Theory 24(3):339-348, 1978. [bib: pv_v6 csiszar1978broadcast]
- Dallaire-Demers, P.-L., Doyle, W., Foo, T. "Brace for impact: ECDLP challenges for quantum cryptanalysis." arXiv:2508.14011, 2025 (rev. 2026). [bib: pv_v6 dallairedemers2025brace]
- de Montjoye, Y.-A., Hidalgo, C. A., Verleysen, M., Blondel, V. D. "Unique in the Crowd: The privacy bounds of human mobility." Scientific Reports 3:1376, 2013. [bib: pv_v6 demontjoye2013unique]
- Dwork, C., Naor, M., Pitassi, T., Rothblum, G. N. "Differential privacy under continual observation." STOC 2010, pp. 715-724. [bib: pv_v6 dwork2010continual]
- ecdsa.fail challenge (Eigen Labs). Repository github.com/ecdsafail/ecdsafail-challenge; leaderboard, 2026. [bib: pv_v6 ecdsafail2026challenge, record]
- El Yagoubi, F., Badu-Marfo, G., Al Mallah, R. "AgentLeak: A Benchmark for Internal-Channel Privacy Leakage in Multi-Agent LLM Systems." arXiv:2602.11510, 2026. [bib: pv_v6 elyagoubi2026agentleak]
- Erlich, Y., et al. "Identity inference of genomic data using long-range familial searches." Science 362(6415):690-694, 2018. doi:10.1126/science.aau4832. [bib: pv_v6 erlich2018identity]
- Fano, R. M. *Transmission of Information: A Statistical Theory of Communication.* MIT Press, 1961. [bib: pv_v6 fano1961transmission]
- Mascelli, J., Rodden, M. "'Harvest Now Decrypt Later': Examining Post-Quantum Cryptography and the Data Privacy Risks for Distributed Ledger Networks." Federal Reserve Board, FEDS 2025-093, 2025. doi:10.17016/FEDS.2025.093. [bib: pv_v6 mascelli2025harvest]
- Garg, S., Jain, A., Sahai, A. "Leakage-Resilient Zero Knowledge." CRYPTO 2011, LNCS 6841, pp. 297-315. [bib: pv_v6 garg2011leakage]
- Gidney, C. "How to factor 2048 bit RSA integers with less than a million noisy qubits." arXiv:2505.15917, 2025. [bib: pv_v6 gidney2025million]
- Gidney, C. "The French have the Quantum Circuits." algassert.com/post/2602, 2026-06. [bib: pv_v6 gidney2026french, record]
- Gidney, C., Ekerå, M. "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits." Quantum 5:433, 2021. [bib: pv_v6 gidney2021factor]
- Gopala, P. K., Lai, L., El Gamal, H. "On the Secrecy Capacity of Fading Channels." IEEE Trans. Inf. Theory 54(10):4687-4698, 2008. [bib: pv_v6 gopala2008secrecy]
- Gymrek, M., McGuire, A. L., Golan, D., Halperin, E., Erlich, Y. "Identifying Personal Genomes by Surname Inference." Science 339(6117):321-324, 2013. [bib: pv_v6 gymrek2013identifying]
- Haines, T., Mosaheb, R., Müller, J., Pryvalov, I. "SoK: Secure E-Voting with Everlasting Privacy." PoPETs 2023(1):279-293. [bib: pv_v6 haines2023sok]
- Harnik, D., Pinkas, B., Shulman-Peleg, A. "Side Channels in Cloud Services: Deduplication in Cloud Storage." IEEE Security & Privacy 8(6):40-47, 2010. [bib: pv_v6 harnik2010side]
- Jain, P., Raskhodnikova, S., Sivakumar, S., Smith, A. "The Price of Differential Privacy under Continual Observation." ICML 2023, PMLR v202:14654-14678. [bib: pv_v6 jain2023price]
- Kagai, F., Branch, P., But, J., Allen, R. "Harvest-Now, Decrypt-Later: A Temporal Cybersecurity Risk in the Quantum Transition." Telecom 6(4):100, 2025. doi:10.3390/telecom6040100. [bib: pv_v6 kagai2025harvest]
- Leung-Yan-Cheong, S., Hellman, M. "The Gaussian Wire-Tap Channel." IEEE Trans. Inf. Theory 24(4):451-456, 1978. [bib: pv_v6 leungyancheong1978gaussian]
- Litinski, D. "How to compute a 256-bit elliptic curve private key with only 50 million Toffoli gates." arXiv:2306.08585, 2023. [bib: pv_v6 litinski2023compute]
- Moran, T., Naor, M. "Receipt-Free Universally-Verifiable Voting with Everlasting Privacy." CRYPTO 2006, LNCS 4117, pp. 373-392. [bib: pv_v6 moran2006receipt]
- Mosca, M. "Cybersecurity in an Era with Quantum Computers: Will We Be Ready?" IEEE Security & Privacy 16(5):38-41, 2018. [bib: pv_v6 mosca2018cybersecurity]
- Mosca, M., Piani, M. *Quantum Threat Timeline Report 2024.* Global Risk Institute / evolutionQ, 2024. [bib: pv_v6 moscapiani2024timeline]
- Mosca, M., Piani, M. *Quantum Threat Timeline Report 2025.* Global Risk Institute / evolutionQ, 2025 (GRI publication page posted 2026-03-09). [bib: pv_v6 moscapiani2025timeline]
- Narayanan, A., Shmatikov, V. "Robust De-anonymization of Large Sparse Datasets." IEEE S&P 2008, pp. 111-125. [bib: pv_v6 narayanan2008robust]
- Näther, C., Herzinger, D., Steghöfer, J.-P., Gazdag, S.-L., Hirsch, E., Loebenberger, D. "Toward a Common Understanding of Cryptographic Agility: A Systematic Review." arXiv:2411.08781, 2024. [bib: pv_v6 naether2024agility]
- Rocher, L., Hendrickx, J. M., de Montjoye, Y.-A. "Estimating the success of re-identifications in incomplete datasets using generative models." Nature Communications 10:3069, 2019. doi:10.1038/s41467-019-10933-3. [bib: pv_v6 rocher2019estimating]
- Roetteler, M., Naehrig, M., Svore, K. M., Lauter, K. "Quantum Resource Estimates for Computing Elliptic Curve Discrete Logarithms." ASIACRYPT 2017, LNCS 10625, pp. 241-270. [bib: pv_v6 roetteler2017quantum]
- Schrottenloher, A. "Optimized Point Addition Circuits for Elliptic Curve Discrete Logarithms." ePrint 2026/1128; arXiv:2606.02235, 2026. [bib: pv_v6 schrottenloher2026optimized]
- Unruh, D. "Everlasting Multi-Party Computation." CRYPTO 2013; J. Cryptology 31(4):965-1011, 2018. [bib: pv_v6 unruh2018everlasting]
- Vigil, M. A. G., Buchmann, J., Cabarcas, D., Weinert, C., Wiesmaier, A. "Integrity, authenticity, non-repudiation, and proof of existence for long-term archiving: A survey." Computers & Security 50:16-32, 2015. [bib: pv_v6 vigil2015integrity]
- Wyner, A. D. "The Wire-Tap Channel." Bell System Technical Journal 54(8):1355-1387, 1975. [bib: pv_v6 wyner1975wiretap]
- Zcash Foundation. "Zebra 4.5.3 and 5.0.0: Emergency Soft Fork and NU6.2 Activation." zfnd.org, 2026-06. [bib: pv_v6 zfnd2026zebra, record]

Not cited, pending bibliographic resolution (do not cite until resolved; see Sections 5.1 and 8): the time-dependent threat-model preprint (no resolvable venue or author list).
