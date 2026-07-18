---
wp: WP-07
tier: A
artifact: theory-paper
title: "Sequential Composition of Leakage-Budgeted Agents: an Exponential-to-Linear Separation under Structural Context Erasure"
status: revision-draft-v3 (post A5 review 1, L077; mathematical legs revised by A3 2026-07-09: BLOCKING-1 hypotheses added to Prop 4.2; MAJOR-1 statement leg in Remark 5.7 and section 4; MAJOR-2 certified-bound semantics at ER-6 and Cor 5.4; MAJOR-3 ER-1 requantified; MINORs 1/2/3/7/8; MINOR-4 adopted as Prop 5.5b. Prose legs revised by A2 2026-07-09: eleven-item re-alignment of abstract and sections 1-2/6-7 to the revised theory core; MAJOR-4 estimation-gap passage in section 6 and "auditable" softened; MINOR-5 DP-contrast sharpened; MINOR-6 citation role re-anchored. P1 passed at A0 targeted re-check, L080; review 2 superseded by that re-check per the A5 memo's own criterion. P3 station L081: one-sentence :207 fix applied by A3; A9 re-run GREEN, L082. AWAITING-P4 since 2026-07-09; frontmatter levelled to manifest by A0 at the cycle-6 sweep, L098/F1, per the L093 precedent. EROSION LEG added by A3 2026-07-16 per the First-Person branch-(c) direction, ledger L143/L145: Definition 3.9 (background side-information family; informed adversary), Corollary 5.4b (cap survives conditioning; floor erodes through H(X | B_t); informed deficit + t*_inf), clock-separation cross-references at abstract / contribution 4 / Remark 3.4 / ER-6 / section 2 / OP 5.8 scope note / section 5.4 / section 6 / section 7. Zero new citation keys. REVIEW STATIONS RUN 2026-07-16: A9 consistency audit GREEN (all six checks; 5.4b math independently verified; two cosmetic notes applied: Remark 3.4 definite article, A_tr(t) now used in 5.4b(ii)); targeted A5 adversarial review of the erosion leg = MINOR, no proof defect, all four MINORs + two NOTEs discharged same day by A3 (5.3 preamble re-scoped to certification index; "genuinely falls" weakened to non-increase per GR-8; "real" qualified to the model's sense; one-calendar clause added at Def 3.9; Markov violation examples widened with "for instance"; portability remark added at 5.4b). Awaiting-P4 on the revised text)
role: A3
date: 2026-07-07
gate_target: awaiting-P4 (P3 passed; P4 is the First Person's; the runtime stops here)
handoff: the P4 owner (PoPETs Issue 2 = 2026-08-31, read by ~08-24; Issue 3 = 2026-11-30)
extraction_basis: >
  E1 claims c01, c02, c03, c04, c05, c06, c08 (mathematical content only,
  conjecture apparatus restated as theorem-or-conjecture per tier), c09, c10, c12;
  E2 claims c01, c02, c04, c11, c12. Traceability appendix at end of file
  (pipeline apparatus, strip at release).
template_target: templates/submission/preprint/ (sections 03, 04 x2, per mapping note below)
bib: templates/submission/references/pv_v6.bib (all keys resolve; the two A3-proposed additions verified and added by A4, 2026-07-07)
---

<!-- ============================================================
A3 APPARATUS NOTE (pipeline internal; REMOVE BEFORE ANY RELEASE)

OUTCOME OF TASK ITEM (4): PROVEN. The Nε cap is established as a
conditional theorem (Theorem 5.1) under numbered engineering
requirements ER-1 to ER-5, with three necessity propositions
(Prop 4.3: budget form; Prop 5.5: erasure; Prop 5.5b: provenance,
adopted at revision 1) showing three of the five hypotheses
are individually load-bearing, and a tightness proposition
(Prop 5.6). What remains open is not a mathematical step: it is
the empirical question of whether any given deployed system
satisfies ER-1 to ER-5, stated in Remark 5.7 as an engineering
hypothesis, and the Grade-2 criterion, posed as Open Problem 5.8
(restyled from Conjecture at A5 review 1, MINOR-7) with proof
obligations and the missing step named.

PoPETs FEASIBILITY READ (first-person decision input, per A0
addendum; deadlines verified per ledger L061):
- Issue 2 (submission 2026-08-31, ~8 weeks out): FEASIBLE ONLY
  under three conditions met promptly: (i) A2 delivers sections
  0-2 and 6-7 prose within ~3 weeks; (ii) the evaluation section
  is scoped as analysis of published measurements (AgentLeak,
  Asif-Amiri empirics) rather than new experiments, since WP-08
  benchmark work cannot land in time; (iii) a P4 first-person
  read slot exists before ~2026-08-24. The theory core (this
  file) is submission-shaped now; the LaTeX scaffold is ready
  (L063); two citations await verification (A8/A4). WP-02
  experience prices one A5 review loop at about a week; two
  loops fit.
- Issue 3 (submission 2026-11-30): COMFORTABLE. Allows WP-08
  empirical grounding in section 5 (evaluation), a second review
  loop, and no pressure on the P4 queue (WP-01/WP-25 reads are
  queued ahead of this paper).
- A3 recommendation, for what it is worth to the decision:
  Issue 2 with the analysis-only evaluation scope if the
  first-person read can be scheduled; otherwise Issue 3 without
  regret, since the imported empirical literature is recent and
  will not be stale by November.

TEMPLATE MAPPING: section 3 below maps to preprint section
03_model_preliminaries; sections 4 and 5 map to 04_theorems
(split into two .tex files or one with subsections, A8's call at
port time); the limits material at the end of section 5 seeds
06_threats_to_validity.
============================================================ -->

# Sequential Composition of Leakage-Budgeted Agents: an Exponential-to-Linear Separation under Structural Context Erasure

## 0. Abstract

Multi-agent systems built from sequentially invoked language-model agents leak information about the sensitive contexts they process, and system-scale measurement locates the dominant share of that leakage in the channels between agents rather than in final outputs. We give an information-theoretic account of when per-agent leakage budgets compose and when they do not. In a model of N sequentially invoked agents with declared interfaces and explicit carried state, the best guarantee available under the budget discipline the empirical literature measures (marginal, output-only constraints) is geometric: the known (2^N − 1)ε bound for the adversary that observes only the final output is an upper bound, not an attained leakage, and we exhibit a two-agent composition in which every marginal budget is zero yet the adversary that observes the whole transcript recovers a context completely. We then prove a conditional linear cap: under five numbered engineering requirements (declared channels only, structural context erasure at every invocation boundary, fresh local randomness, context provenance, and conditional interface-inclusive budgets ε_1, ..., ε_N), transcript leakage about a source X satisfies I(T; X) ≤ Σ_i ε_i. Three necessity constructions show that the erasure requirement, the conditional budget form, and the provenance requirement are individually indispensable, and the cap is achieved, so it is tight. The exponential-to-linear comparison is a comparison of upper-bound guarantees under their stated budget semantics, not of attainable leakages, and the conditional budget at the same numerical level is the more demanding constraint; the unconditional separation is the zero-budget construction. The central result is a decomposition, not an unconditional ceiling. The structural requirements license additive budget accounting and a Fano error floor. A strict sub-unity bound on reconstruction additionally requires the declared capacity-deficit condition Σ_i ε_i(t) < H(X): a numerical fact about a specific system-adversary pair at a stated time, not a consequence of the architecture, and the component of any deployed guarantee that expires as adversary capability grows. Separately, against an informed adversary holding background side information B_t that accumulates with calendar time under the Markov chain B_t → X → T, the cap survives conditioning while the error floor erodes through the residual entropy H(X | B_t): the strict component's deficit condition becomes Σ_i ε_i < H(X | B_t), a second, genuinely time-varying expiry channel that requires no growth in what the transcript reveals (Corollary 5.4b).

## 1. Introduction

Language-model agents are now deployed in pipelines: one agent's output becomes working material for the next, across invocations that may be separately built, separately budgeted, and separately audited. Measurement at system scale shows where such pipelines leak. In a recent benchmark across production LLMs, the channels between agents were observable in deployed frameworks and carried the dominant share of leakage about sensitive contexts, and audits that inspect only final outputs missed a substantial fraction of violations [elyagoubi2026agentleak] (exact figures are recorded at Definition 3.6).

The theory matches the measurement. Asif and Amiri prove that in a sequential pipeline satisfying their Markov structure, with mutually independent sensitive variables and a marginal per-agent budget I(O_i; S_i) ≤ ε_i on each agent, leakage about the joint secrets at the final output is at most the geometric sum Σ_i 2^{N−i} ε_i, that is (2^N − 1)ε in the uniform case; that geometric sum is the guarantee the marginal discipline provides, an upper bound with no matching attainability construction known, and their measurements show mutual information rising with chain depth [asif2026infotheoretic]; independent composition analysis reaches the same qualitative conclusion [patil2025composition]. Per-agent budget certification, in the form the current literature states it, does not compose: N certified agents are not a certified system.

This paper asks what discipline restores linear accounting, and against which adversary. Two distinctions organise the answer. The first is the adversary. Bounds stated against the final output do not survive the passage to the adversary that observes the whole transcript, and the transcript adversary is the one the measurements say exists. Proposition 4.3 exhibits a two-agent composition satisfying structural context erasure and zero marginal budgets, including interface-inclusive marginal budgets, in which the transcript adversary nevertheless recovers a context exactly; it is the formal counterpart of the measured dominance of inter-agent-channel leakage. The second is the form of the budget: what it ranges over (the public output alone, or everything the invocation emits including its forward interface) and whether it is conditioned on what the invocation received. Marginal budgets fail even at budget zero; conditioning on the received interface is what prices the correlation the marginal misses (Section 3.4).

The main result is a conditional linear cap (Theorem 5.1): under five numbered engineering requirements (ER-1 declared channels only, ER-2 structural context erasure, ER-3 fresh local randomness, ER-4 context provenance, ER-5 conditional interface-inclusive budgets), transcript leakage about the source is at most the sum of the declared budgets, Nε in the uniform case. Three of the five hypotheses are individually load-bearing, each with a necessity construction defeating the cap at declared budget zero. Dropping the conditional budget form while keeping erasure caps nothing (Proposition 4.3); dropping erasure while keeping zero budgets caps nothing (Proposition 5.5, a persistent-pad construction with total leakage at zero declared budget); dropping context provenance while keeping erasure and zero budgets caps nothing (Proposition 5.5b, in which the environment routes the source around the priced interface through context assembly). No necessity construction is offered for ER-1 or ER-3. By Theorem 5.1 the five are jointly sufficient, and Proposition 5.6 shows the cap is achieved. The exponential-to-linear separation is therefore a separation between disciplines, not mechanisms, and a comparison of upper-bound guarantees under stated budget semantics, not of attainable leakages (Remark 5.7).

Throughout, the results are stated inside a decomposition discipline (Remark 3.4). The structural requirements license two things: additive budget accounting, and a Fano error floor for any estimator of the source from the transcript (Corollary 5.4). They do not by themselves place the leakage-to-entropy ratio below one. The strict claim that reconstruction is incomplete requires, in addition, the declared capacity-deficit condition Σ_i ε_i(t) < H(X), evaluated against a stated decoder class at a stated time t. That condition is a measurable numerical fact about a system-adversary pair, not a consequence of the architecture; it is the component that expires as decoder classes grow, and the paper never states the strict bound without it.

Our contributions are:

1. A composition model for sequentially invoked agents in which carried state is explicit and structural context erasure is a property of the composition operator rather than a notational assumption (Definitions 3.5 to 3.8), together with a taxonomy of budget forms (marginal versus conditional, output-only versus interface-inclusive) that the results show to be the load-bearing distinctions (Section 3.4).

2. An account of the exponential regime: the amplification bound imported with its hypotheses carried exactly (Theorem 4.1 [asif2026infotheoretic]), an in-model reproduction under the named local hypotheses of no carried state, independent noise and bounded contamination, the last formally incomparable to the source's hypotheses (Proposition 4.2), and the observation that marginal budgets do not bind the transcript adversary even at budget zero (Proposition 4.3).

3. A conditional linear cap (Theorem 5.1): transcript leakage at most Σ_i ε_i under ER-1 to ER-5, with necessity constructions for three of the five hypotheses, the budget form, erasure and provenance (Propositions 4.3, 5.5 and 5.5b), tightness (Proposition 5.6), and the composed error floor with its declared, time-indexed deficit condition (Corollary 5.4).

4. A framing discipline that separates what the architecture guarantees (additivity and the floor) from what must be declared and expires (the deficit), with the time-indexed budgets of ER-6 given precedent in the fading-wiretap literature [gopala2008secrecy], together with a side-information corollary (Corollary 5.4b) separating ER-6's certification clock, whose drift is epistemic, from the informed adversary's erosion clock, the one time-varying quantity in the paper whose drift is not a statement about certification.

5. A formally stated open problem (Open Problem 5.8) on the criterion separating recoverable from unrecoverable erasure, carried with its proof obligations and its unstarted first step named.

Every result in this paper is conditional on the numbered requirements of Section 3.5, which are obligations on implementations, not facts about deployed systems; measurement indicates deployed frameworks routinely violate the first of them today [elyagoubi2026agentleak]. Whether a given system satisfies ER-1 to ER-5 is an empirical conformance question, testable per instance and answered here for no system. Section 6 states the threats to validity, including the commitment that measured results against these predictions are reported with the same prominence as confirmations.

The paper is organised as follows. Section 2 positions the results against the wiretap, converse, multi-agent leakage, covert-channel, information-flow, differential-privacy and time-varying-capacity literatures. Section 3 gives the model, the budget taxonomy, and the engineering requirements. Section 4 treats the regime without erasure, including the imported amplification bound and the transcript-adversary construction. Section 5 proves the linear cap, its necessity and tightness results, and states the one open problem. Section 6 records threats to validity, and Section 7 concludes.

## 2. Related work

**The wiretap lineage.** The objects this paper computes with are the classical ones. Wyner introduced the wiretap channel and equivocation at the adversary as the measure of secrecy [wyner1975wiretap]; Leung-Yan-Cheong and Hellman characterised the secrecy capacity of the Gaussian channel as a difference of capacities [leungyancheong1978gaussian]; Csiszár and Körner treated broadcast channels with confidential messages, the general single-eavesdropper form of the family [csiszar1978broadcast]. Section 3.2 states the two-agent base results as in-model instances of this family rather than as new results. The failure of additive accounting for colluding observers, by contrast, is elementary and needs no citation: joint information can exceed the sum of marginal informations, with the interaction identity in Theorem 3.1 locating the excess and Proposition 5.5 exhibiting the extremal case at zero marginals, and requirement ER-1 exists to exclude exactly this failure mode.

**Fano and the source-coding converses.** The error floor is Fano's inequality [fano1961transmission] in its standard converse form [cover2006elements], applied at the level of the composed transcript (Theorem 3.2, Corollary 5.4). We add only precision: the normalised form of the floor carries an alphabet-entropy hypothesis that informal statements frequently elide, and Theorem 3.2 states it.

**Sequential multi-agent leakage.** The regime this paper addresses was opened by Asif and Amiri's information-theoretic treatment of agent pipelines: under their Markov structure, with mutually independent sensitive variables and marginal per-agent budgets, final-output leakage is bounded by the geometric sum, and their measurements show mutual information growing with chain depth [asif2026infotheoretic]. We import their Theorem 4.1 with citation, carrying its hypotheses exactly (Section 4). Our Proposition 4.2 closes the same doubling recursion inside our model under three named local hypotheses: no carried state, independent noise, and bounded contamination. The two hypothesis sets are formally incomparable, neither implying the other: their model constrains the secrets' joint law and the pipeline's Markov structure, ours prices the coupling between upstream flow and downstream contexts directly, and neither result claims the other's hypotheses. AgentLeak supplies the system-scale measurement: inter-agent channels are observable in deployed frameworks and carry the dominant share of leakage, which is what motivates stating our main results against the transcript adversary (Definition 3.6) [elyagoubi2026agentleak]. Patil, Stengel-Eskin and Bansal reach the same qualitative conclusion by composition analysis [patil2025composition]. Relative to this line, our contribution is not a sharper amplification bound; it is the characterisation of a discipline under which amplification collapses to additivity, with necessity constructions for both of the discipline's central hypotheses.

**Covert channels.** ER-1 (declared channels only) is a covert-channel exclusion obligation, and its conformance audit is a channel inventory. The quantitative treatment of unintended channels as information channels goes back to Millen, who applied Shannon capacity to covert channels in secure systems [millen1987covert]. The necessity construction of Proposition 5.5 can be read in those terms: state carried across an invocation boundary is an unpriced channel, and the composition-level bound fails through it at zero declared budget.

**Language-based information flow.** Static, language-level enforcement of noninterference-style properties is surveyed by Sabelfeld and Myers [sabelfeld2003language]. That programme certifies flows by analysing program text before execution. The setting here is complementary: the composed agents are opaque, no per-agent program analysis is assumed, and the requirements of Section 3.5 are architectural obligations on the composition, with budgets standing where typing judgements cannot reach; section 6 records which requirements are auditable by inspection and which require statistical estimation. Nothing here replaces language-based enforcement inside an agent; the results concern what composition preserves when per-agent internals are inaccessible.

**Differential privacy composition.** Differential privacy is the reference discipline for budgets that compose: basic sequential composition is a theorem (the ε parameters add), advanced composition degrades sublinearly, and the reason composition holds with no architectural assumptions is that the guarantee is worst-case over neighbouring inputs and over adaptively chosen mechanisms [dwork2014algorithmic]. That worst-case quantification is the honest analogue of ER-5's conditioning on the received interface: both price the adversary's best use of what earlier stages expose. The results here can be read as identifying what that convenience costs to reproduce for mutual-information budgets over opaque agents: additivity is not automatic (Section 4 exhibits exponential amplification, and complete failure against the transcript adversary at zero budget), and it must be earned by architecture, namely erasure, conditioning, and provenance (Theorem 5.1). We make no claim that the budgets of ER-5 imply any differential-privacy guarantee; the two disciplines quantify over different adversaries and different neighbouring relations.

**Time-varying capacity.** Evaluating secrecy against a varying channel state has precedent in the fading wiretap channel literature [gopala2008secrecy]. ER-6's time-indexed budgets and the expiring deficit of Corollary 5.4 follow that precedent at the system level: capacity against the strongest available decoder class is a function of time, and the strict component of any guarantee is dated. The side-information erosion of Corollary 5.4b is a different time dependence from the fading channel's: there the channel state varies while the source is fixed; here every channel and budget is fixed and what varies is the adversary's background knowledge of the source, entering through the conditional-entropy term of Fano's inequality [fano1961transmission; cover2006elements].

## 3. Model and preliminaries

### 3.1 Notation

Random variables are uppercase, realisations lowercase, alphabets calligraphic. X is a source (the data subject's protected variable) over a finite alphabet 𝒳 with H(X) > 0. I(·;·) denotes mutual information, I(·;·|·) conditional mutual information, H(·) Shannon entropy in bits. "U ⊥ V" abbreviates independence; "U ⊥ V | W" conditional independence. For a sequence (A_1, ..., A_N) we write A_{1:i} = (A_1, ..., A_i) and A_{<i} = A_{1:i−1}.

All results in this paper are information-theoretic statements about a stated model under stated hypotheses. Every hypothesis is listed in section 3.5 as a numbered engineering requirement or stated locally in the result that uses it; no result transfers to a system in which the corresponding hypothesis fails, and section 5 exhibits explicit failure constructions.

### 3.2 The two-agent base architecture

Two agents observe the source through separate channels: a boundary agent S emitting Y_S = E_S(X, N_S) and a delegation agent M emitting Y_M = E_M(X, N_M), where N_S, N_M are independent local randomness sources. The architectural intent is that S enforces selective disclosure under a budget I(X; Y_S) ≤ C_S while M executes delegated capability under a budget I(X; Y_M) ≤ C_M, with no unmediated channel between the two.

The following three results are standard; we state and prove them in-model because the composition theorems of sections 4 and 5 reduce to them at N = 2, and because their precise hypotheses are load-bearing. They are instances of an established family: wiretap equivocation [wyner1975wiretap], secrecy capacity as a capacity difference [leungyancheong1978gaussian], broadcast channels with confidential messages as the family's general single-eavesdropper form [csiszar1978broadcast], and the source-coding and Fano converses [fano1961transmission; cover2006elements]. The failure of the additive form under collusion needs no citation: it is the elementary fact that joint information can exceed the sum of marginal informations, and the interaction identity in Theorem 3.1's proof locates the excess exactly.

**Theorem 3.1 (additive bound under conditional independence).**
If I(Y_S; Y_M | X) = 0, then

> I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M),

with equality if and only if additionally I(Y_S; Y_M) = 0.

*Proof.* By the chain rule, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M | Y_S). The interaction identity I(X; Y_M) − I(X; Y_M | Y_S) = I(Y_S; Y_M) − I(Y_S; Y_M | X) (both sides equal the co-information of the triple) gives, under I(Y_S; Y_M | X) = 0,

> I(X; Y_M | Y_S) = I(X; Y_M) − I(Y_S; Y_M) ≤ I(X; Y_M),

with equality exactly when I(Y_S; Y_M) = 0. ∎

The bound is an inequality; conditional independence given X still permits marginal correlation of Y_S and Y_M through X itself, and that correlation only lowers the joint leakage relative to the sum. The inequality direction is all that any downstream guarantee uses.

**Theorem 3.2 (Fano error floor).**
Let |𝒳| ≥ 3 and let Y be any observation with I(X; Y) < ∞. For any estimator X̂(Y) taking values in 𝒳,

> P_e := Pr[X̂(Y) ≠ X] ≥ (H(X) − I(X; Y) − 1) / log(|𝒳| − 1).

If moreover H(X) ≥ log(|𝒳| − 1) (in particular if X is uniform), then with R := I(X; Y)/H(X),

> P_e ≥ 1 − R − 1/H(X).

*Proof.* Fano's inequality [fano1961transmission; cover2006elements] gives H(X | Y) ≤ h(P_e) + P_e log(|𝒳| − 1) ≤ 1 + P_e log(|𝒳| − 1), where h is binary entropy. Rearranging and substituting H(X | Y) = H(X) − I(X; Y) gives the first display. The second follows since (H(X) − I − 1)/log(|𝒳| − 1) ≥ (H(X) − I − 1)/H(X) when H(X) ≥ log(|𝒳| − 1) and H(X) − I − 1 ≥ 0; when H(X) − I − 1 < 0 the second display is vacuous and holds trivially. ∎

We record a precision point: the normalised form 1 − R − 1/H(X) requires the stated alphabet-entropy hypothesis; for strongly non-uniform sources with H(X) < log(|𝒳| − 1) only the first display applies. The log(|𝒳| − 1) denominator additionally requires the estimator to range over 𝒳 itself; for estimators taking values in a strict superset of 𝒳 the denominator weakens to log |𝒳|.

**Theorem 3.3 (robustness to approximate separation).**
If I(Y_S; Y_M | X) ≤ ε, then I(X; Y_S, Y_M) ≤ I(X; Y_S) + I(X; Y_M) + ε.

*Proof.* As in Theorem 3.1, I(X; Y_M | Y_S) = I(X; Y_M) − I(Y_S; Y_M) + I(Y_S; Y_M | X) ≤ I(X; Y_M) + ε. ∎

Failure of separation is therefore continuous: a violation of size ε costs at most ε additional bits of joint leakage.

**Remark 3.4 (the decomposition; what the architecture does and does not buy).**
Write R_max = (C_S + C_M)/H(X). Theorems 3.1 and 3.2 yield: under the separation requirement (ER-1 below) and against a stated adversary class (ER-6 below), leakage budgets add, and any estimator faces the error floor P_e ≥ 1 − R_max − 1/H(X) (uniform-source form). These structural requirements do **not** by themselves place R_max below one: two conditionally independent channels of sufficient combined capacity satisfy every structural requirement with R_max ≥ 1, at which point the floor is vacuous. The strict bound R_max < 1 holds exactly when, additionally, the capacity-deficit condition

> C_S + C_M < H(X)

holds. The deficit condition is a measurable, declarable, numerical fact about a given system and adversary class; it is not a consequence of the architecture, and we deliberately do not list it among the structural requirements. It is also a time-indexed quantity: with capacities evaluated against the strongest decoder class available at time t, the governing ratio is R(t) = (C_S(t) + C_M(t))/H(X) with shelf life t* = sup{t : R(t) < 1}; R(t) can cross one with every structural requirement intact, and what expires at t* is the deficit condition, not the architecture. The supremum is not in general a first crossing: R(t) may cross one and return, in which case t* marks the last time the deficit condition holds, not the first time it fails. When C_S(t) + C_M(t) is non-decreasing in t (the regime of ER-6's growing decoder class, and the hypothesis under which Corollary 5.4 below states the composed shelf life), R(t) is non-decreasing, the supremum coincides with the first crossing, and the expiry reading is exact. Treating channel capacity as a time-indexed quantity has precedent in the study of fading wiretap channels, where secrecy capacity is defined against a varying channel state [gopala2008secrecy]. This decomposition (structural requirements license additivity and the floor; the declared deficit licenses the strict bound; the deficit expires) is the paper's framing discipline, and every bound below is stated within it. A second, distinct clock, whose drift is real rather than certificational, is treated at Corollary 5.4b: there the capacities and budgets are held fixed and what moves is the informed adversary's residual uncertainty H(X | B_t) about the source. The two clocks must not be conflated, and every time-indexed reconstruction statement downstream of this paper should name which one it runs on.

### 3.3 N-agent sequential composition

We now generalise from two parallel observers to a chain of N sequentially invoked agents, the regime measured by the recent multi-agent leakage literature [asif2026infotheoretic; elyagoubi2026agentleak].

**Definition 3.5 (sequential composition).**
A *sequential composition of N agents* consists of invocations i = 1, ..., N where invocation i:

1. receives an *interface message* Z_{i−1} from its predecessor (Z_0 := ⊥, a constant);
2. holds a *sensitive context* S_i and *carried state* ρ_{i−1} (ρ_0 := ⊥);
3. draws *local randomness* N_i;
4. emits a *public output* O_i, a *forward interface* Z_i, and carried state ρ_i via a measurable map

> (O_i, Z_i, ρ_i) = f_i(Z_{i−1}, ρ_{i−1}, S_i, N_i).

We write V_i := (O_i, Z_i) for the invocation's total emission and T := (V_1, ..., V_N) for the *transcript*.

**Definition 3.6 (adversary classes).**
The *final-output adversary* 𝔄_out observes O_N. The *transcript adversary* 𝔄_tr observes T. Clearly any bound against 𝔄_tr implies the same bound against 𝔄_out. Measurement at system scale shows the channels internal to T are observable in deployed systems and carry the dominant share of leakage (68.8 per cent of inter-agent channel traces leaking, against 27.2 per cent per-channel output leakage, in a 4,979-trace benchmark across five production LLMs [elyagoubi2026agentleak]); we therefore treat 𝔄_tr as the realistic passive adversary and state our main results against it.

**Definition 3.7 (structural context erasure, as a composition property).**
The composition is *context-erasing at boundary i* if ρ_i = ⊥: no state survives the invocation boundary except the declared forward interface. The composition has *structural context erasure* if it is context-erasing at every boundary, in which case Definition 3.5 reduces to

> (O_i, Z_i) = f_i(Z_{i−1}, S_i, N_i).

Consequently (interface sufficiency): for every i, conditional on (Z_i, S_{i+1}, N_{i+1}), the emission V_{i+1} is independent of the entire invocation-i history (Z_{i−1}, S_i, N_i). The implication is one-way: retained state may be causally inert, so the conditional independence does not entail ρ_i = ⊥, and erasure is defined by the structural condition, not by the independence it implies. Erasure is thus a *reachability* property of the composition operator: no permitted continuation of the system can reconstruct the erased working context except through what the declared interface carries, and the information available downstream about the erased material is bounded through Z_i by the data processing inequality.

**Definition 3.8 (erasure grades).**
Erasure at boundary i is *Grade 1* (hiding) if there exists key material K in the system (any variable measurable with respect to the system's retained state, including operator-held state) such that the erased context is recoverable as a function of (Z_i, K). It is *Grade 2* (forgetting) if no such K exists in the closure of the system's permitted operations. Grade 1 withholds gluing data; Grade 2 destroys the witness. The closure of the system's permitted operations is left informal here, and no theorem below depends on the grade criterion (section 5.3 states this dependence-freedom explicitly). A candidate formal criterion separating the grades is posed as Open Problem 5.8; the definition above is operational and suffices for the theorems.

**Definition 3.9 (background side information; the informed adversary).**
A *background side-information family* is a collection {B_t : t ≥ 0} of random variables such that (i) for s ≤ t, B_s is a measurable function of B_t (the background only accumulates), and (ii) for every t the Markov chain B_t → X → T holds, equivalently I(T; B_t | X) = 0. The *informed transcript adversary* 𝔄_tr(t) observes (T, B_t). Hypothesis (ii) states that the background carries information about the source only through the world's dependence on the source (linkage corpora, auxiliary records, side priors), never through a tap on the system: for instance a background containing transcript material, or one correlated with the invocations' internal randomness, violates it, and no result below applies to such a background (section 5.4); the displayed condition is exact. The index t is the same calendar time as ER-6's certification index: "two clocks" names two quantities drifting on one calendar, not two time axes. The family is a declared model of the adversary's accumulation, in the same sense that ER-6's decoder class is declared; nothing in this paper asserts what any actual adversary holds.

### 3.4 What the per-agent constraint must range over

The composition theorems below turn on two attributes of the per-invocation leakage constraint, and we fix vocabulary for them now. A budget is *output-only* if it constrains O_i alone, and *interface-inclusive* if it constrains V_i = (O_i, Z_i). A budget is *marginal* if it is an unconditional mutual information, and *conditional* if it conditions on the received interface Z_{i−1}. Section 4 shows that marginal output-only budgets govern only the final-output adversary and place no nontrivial constraint on the transcript adversary, even at budget zero. Section 5 shows that conditional interface-inclusive budgets, combined with structural context erasure, yield the linear cap against the transcript adversary.

### 3.5 Engineering requirements

Every hypothesis used by any result below is either one of the following numbered requirements or stated explicitly in the result itself (section 4's marginal-regime results carry local hypotheses in place). Each requirement is an obligation on an implementation, not a fact about the world. The necessity constructions of sections 4 and 5 (Propositions 4.3, 5.5 and 5.5b) show what fails when the conditional budget form (ER-5), erasure (ER-2) or provenance (ER-4) is dropped alone; no necessity construction is offered for ER-1 or ER-3, whose sufficiency is claimed only in conjunction with the rest.

- **ER-1 (declared channels only; non-collusion).** No channel connects one invocation to another except the declared components of Definition 3.5: the interfaces {Z_i} and the modelled carried state {ρ_i}. No undeclared side channel exists. ER-1 does not itself constrain the carried state: the destruction of ρ_i is ER-2's obligation alone. Assembly of a downstream context from upstream emissions is not a channel in this sense; it is the environment's routing, governed by ER-4. At N = 2 (parallel form) this is I(Y_S; Y_M | X) = 0 together with the absence of any third channel carrying the inter-agent residue. ER-1 is what the functional form of Definition 3.5 encodes; a system with side channels is outside the model. That the additive structure fails without ER-1 is elementary, not a cited result: joint information exceeds the sum of marginals as soon as the observations correlate beyond what the source explains, with Theorem 3.3 pricing the excess and Proposition 5.5 exhibiting the extremal case at zero marginal budgets; system-scale measurement shows deployed multi-agent frameworks routinely violate ER-1 today [elyagoubi2026agentleak].

- **ER-2 (structural context erasure).** ρ_i = ⊥ at every boundary (Definition 3.7): the platform destroys all invocation state except the declared forward interface. This is a structural property of the runtime (state destruction), not an instructed behaviour of the agent.

- **ER-3 (fresh local randomness).** The local randomness sources N_1, ..., N_N are mutually independent and jointly independent of the source and contexts (X, W_1, ..., W_N), with W_i as in ER-4.

- **ER-4 (context provenance).** Each sensitive context is assembled from the source, private freshness, and the received interface only: S_i = φ_i(X, W_i, Z_{i−1}), where W_1, ..., W_N are mutually independent and jointly independent of X and of {N_j}. In particular no downstream context is assembled from upstream *emissions* except through the declared (and therefore budgeted) interface. Contamination routed through Z_{i−1} is permitted, because ER-5 prices it; contamination routed around Z is excluded.

- **ER-5 (conditional, interface-inclusive leakage budgets).** For each invocation a declared budget ε_i ≥ 0 with

> I(O_i, Z_i; X | Z_{i−1}) ≤ ε_i.

  The budget covers everything the invocation emits, including the forward interface, and is conditioned on what the invocation received. It is a per-invocation, locally defined quantity: it depends only on the joint law of one invocation's input interface, emission, and the source. Certification of a declared bound on it is class-and-time-indexed per ER-6.

- **ER-6 (stated adversary class, time-indexed).** All budgets and capacities are evaluated against a stated decoder class at a stated time t; every ε_i is ε_i(t), non-decreasing in t under growth of the class. No bound in this paper says anything about a decoder class stronger than the one declared. (The formalisation of the ordered decoder-class family is developed in companion work on the time-indexed ratio R(t); here it enters only through the indexing of budgets.)

  *Semantics of the time index (certified bounds).* The quantities the theorems consume are Shannon functionals of the joint law: I(O_i, Z_i; X | Z_{i−1}) depends on no decoder class and does not change as adversaries improve. The declared ε_i(t) are certified upper bounds on these fixed but unknown quantities: a conformance audit at time t certifies ε_i(t) using the estimation and attack tooling of the decoder class available at t, and a certificate is only as strong as the class that produced it. What is non-decreasing in t is therefore the certified value, not the information: growth of the class can expose leakage a weaker class missed, forcing the honest certificate upward or its revocation, while the underlying mutual information is constant. Theorem 5.1 and its corollaries hold with any values that genuinely bound the Shannon quantities; every time-indexed statement in this paper, in particular the expiry of Corollary 5.4, is a statement about what the certification licenses at time t, not a statement that information accrues to the transcript. The same reading applies to the time-indexed capacities of Remark 3.4. This certified clock is not the only time dependence a deployment faces: Corollary 5.4b treats the informed adversary whose background side information grows with calendar time (Definition 3.9), a drift that is real rather than certificational and that no conformance audit arrests.

- **ER-7 (declared deficit for strict reconstruction claims).** Any claim that reconstruction is strictly incomplete (error floor bounded away from zero) requires, in addition to ER-1 to ER-6, the declared numerical fact Σ_i ε_i(t) < H(X) (base case: C_S + C_M < H(X)). This is a property of a system-adversary pair at a time, never a consequence of ER-1 to ER-5, and it is the component that expires as t grows (Remark 3.4).

## 4. The sequential bound without erasure

This section treats the budget regime the empirical literature measures: chained agents under marginal output-only budgets. Throughout this section the composition model is Definition 3.5, the budget is the marginal output-only constraint I(O_i; S_i) ≤ ε_i on each agent's leakage about its own context, and the secrets of interest are the per-agent contexts S_{1:N}. Structural hypotheses are stated per result and are not uniform across the section: Theorem 4.1 is imported with its source's Markov structure; Proposition 4.2 assumes no carried state and independent noise (its hypotheses (i) and (ii) below); Proposition 4.3's construction satisfies structural context erasure outright. Carried state and contexts assembled from upstream outputs are permitted by the model but are excluded wherever a result's stated hypotheses exclude them.

**Theorem 4.1 (sequential amplification; imported).**
Consider a sequential pipeline of N agents satisfying the source's Markov structure (its Eq. (2): S_{i−1} → (O_{i−1}, D_i, S_i) → O_i → O_{i+1} → ⋯ → O_N for each i ∈ {1, ..., N}, where D_i denotes the public or task-relevant inputs to agent i), and assume the sensitive variables S_1, ..., S_N are mutually independent. If each agent satisfies the local leakage constraint I(O_i; S_i) ≤ ε_i, then the final output satisfies

> I(O_N; S_1, ..., S_N) ≤ Σ_{i=1}^{N} 2^{N−i} ε_i,

and in the uniform case ε_i = ε,

> I(O_N; S_1, ..., S_N) ≤ (2^N − 1) ε.

*Provenance.* This is Theorem 4.1 of Asif and Amiri [asif2026infotheoretic], proved there via the chain rule and the conditional data processing inequality; we import it with citation and do not re-derive it. The same authors report the empirical counterpart: average mutual information rising from 0.49 to 1.05 as chain depth grows from two to five agents (MedQA, LLaMA-7B). Composition analysis by Patil, Stengel-Eskin and Bansal reaches the same qualitative conclusion [patil2025composition].

**Proposition 4.2 (in-model reproduction under bounded contamination).**
In the model of Definition 3.5 with O_i = Z_i (full passthrough) and per-agent constraint I(O_i; S_i) ≤ ε_i, suppose additionally:

(i) *no carried state*: ρ_i = ⊥ for every i, equivalently O_i = f_i(O_{i−1}, S_i, N_i); under full passthrough this is structural context erasure (Definition 3.7);

(ii) *independent noise*: N_1, ..., N_N are mutually independent and jointly independent of (S_1, ..., S_N);

(iii) *bounded contamination*: for every i,

> I(O_{i−1}; S_i | S_{1:i−1}) ≤ I(O_{i−1}; S_{1:i−1}).

Then L_i := I(O_i; S_{1:i}) satisfies the recursion L_i ≤ 2 L_{i−1} + ε_i, and hence L_N ≤ Σ_{i=1}^{N} 2^{N−i} ε_i.

*Proof.* By the chain rule, L_i = I(O_i; S_i) + I(O_i; S_{1:i−1} | S_i) ≤ ε_i + I(O_i; S_{1:i−1} | S_i). By (i), O_i = f_i(O_{i−1}, S_i, N_i), and inductively O_{i−1} is a measurable function of (S_{1:i−1}, N_{1:i−1}); hence by (ii), N_i is independent of (S_{1:i}, O_{i−1}) jointly, and in particular N_i ⊥ (S_{1:i−1}, O_{i−1}) | S_i. Given S_i, the emission O_i is therefore a measurable function of (O_{i−1}, N_i) with N_i conditionally independent of (S_{1:i−1}, O_{i−1}); hence S_{1:i−1} → O_{i−1} → O_i is a Markov chain conditionally on S_i, and the conditional data processing inequality gives I(O_i; S_{1:i−1} | S_i) ≤ I(O_{i−1}; S_{1:i−1} | S_i). Expanding,

> I(O_{i−1}; S_{1:i−1} | S_i) = I(O_{i−1}; S_{1:i−1}) + I(O_{i−1}; S_i | S_{1:i−1}) − I(O_{i−1}; S_i)
> ≤ L_{i−1} + I(O_{i−1}; S_i | S_{1:i−1})
> ≤ 2 L_{i−1},

using bounded contamination in the last step. The recursion L_i ≤ 2L_{i−1} + ε_i with L_0 = 0 solves to L_N ≤ Σ_i 2^{N−i} ε_i. ∎

*Scope note (binding).* Bounded contamination is **our** sufficient condition for closing the doubling recursion inside this model; it names the mechanism (the downstream context S_i correlates with the upstream transcript at most as strongly as the upstream secrets do). Whether it coincides with the hypotheses of [asif2026infotheoretic] is a citation-resolution item; Theorem 4.1 stands on its own citation and Proposition 4.2 on its own proof, and neither claims the other's hypotheses.

The doubling term is genuinely a contamination term: when the downstream context is independent of the upstream flow given earlier secrets (I(O_{i−1}; S_i | S_{1:i−1}) = 0, the exogenous case), the same computation yields the additive recursion L_i ≤ L_{i−1} + ε_i under the same no-carried-state hypothesis, *for the final-output adversary*. Hypothesis (i) is load-bearing, not decorative: with carried state permitted, zero marginal budgets bound nothing even at the final output. (Take S_1, S_2 independent uniform bits; invocation 1 emits fresh junk O_1 = U with U uniform and independent of the secrets, retaining ρ_1 = S_1; invocation 2 emits O_2 = ρ_1. Every marginal budget holds at ε = 0 and bounded contamination holds with both sides zero, yet I(O_2; S_1, S_2) = H(S_1).) The regimes are therefore three: with carried state, no function of the marginal budgets bounds leakage (here at the final output, and at transcript scale in Proposition 5.5); without carried state, under marginal budgets only, amplification up to the geometric sum (Proposition 4.2); under erasure with the conditional budgets of ER-5, the linear cap (Theorem 5.1). The next proposition shows why the final-output adversary is the wrong one to design against even inside the middle regime.

**Proposition 4.3 (marginal budgets do not bind the transcript adversary).**
There is a two-agent sequential composition satisfying structural context erasure (ER-2), fresh randomness (ER-3), exogenous contexts, and *zero* marginal budgets, in which the transcript adversary recovers a context completely:

> I(O_1; S_1) = I(O_2; S_2) = 0, and moreover I(V_1; S_1) = I(V_2; S_2) = 0, yet I(O_1, O_2; S_1, S_2) = H(S_2).

*Construction.* Let S_1, S_2 be independent uniform bits and N_1 a uniform bit independent of both. Agent 1 emits O_1 = Z_1 = S_1 ⊕ N_1. Agent 2 emits O_2 = Z_1 ⊕ S_2 (and Z_2 = ⊥). Marginally, O_1 is uniform and independent of S_1 (one-time pad), and O_2 = S_1 ⊕ N_1 ⊕ S_2 is uniform and independent of S_2; so every marginal budget is met at ε = 0, including the interface-inclusive marginal I(V_i; S_i) = 0. But O_1 ⊕ O_2 = S_2: the transcript adversary reads S_2 exactly. Consistently with Theorem 4.1, the final output alone reveals nothing (I(O_2; S_1, S_2) = 0). ∎

Three consequences. First, a bound stated against the final output, such as Theorem 4.1, does not survive the passage to the transcript adversary, and the transcript adversary is the one system-scale measurement says exists [elyagoubi2026agentleak]. Second, the failure is not repaired by including the interface in a *marginal* budget; the construction defeats that too. The load-bearing attribute is *conditioning*: the conditional budget of ER-5 evaluates I(V_2; S_2 | Z_1) = H(S_2) and prices the correlation the marginal misses. Third, the construction satisfies erasure: structural context erasure alone, without the conditional budget discipline, caps nothing. Erasure and budget form are separately necessary; section 5 shows they are jointly sufficient. These three facts make Proposition 4.3 the paper's unconditional separation: zero declared budget on one side against total recovery of a context on the other, with no attainability hypothesis on either side. The exponential-to-linear comparison of Remark 5.7 is, by contrast, a comparison of upper-bound guarantees under stated budget semantics (see the second fence there).

## 5. The linear cap under structural context erasure

### 5.1 The cap

**Theorem 5.1 (linear cap).**
Consider a sequential composition of N agents satisfying ER-1 (declared channels only), ER-2 (structural context erasure), ER-3 (fresh randomness), ER-4 (context provenance), and ER-5 (conditional interface-inclusive budgets ε_1, ..., ε_N). Then against the transcript adversary,

> I(T; X) ≤ Σ_{i=1}^{N} ε_i,

and in the uniform case I(T; X) ≤ Nε.

*Proof.* Write V_i = (O_i, Z_i) and T = (V_1, ..., V_N). By the chain rule,

> I(T; X) = Σ_{i=1}^{N} I(V_i; X | V_{1:i−1}).

Fix i and set A := V_{1:i−1}; note Z_{i−1} is a coordinate of A (for i = 1, both are trivial).

*Step 1 (transcript measurability).* By ER-1, ER-2 and ER-4, each V_j with j < i is a measurable function of (X, W_{1:j}, N_{1:j}): inductively, V_j = f_j(Z_{j−1}, φ_j(X, W_j, Z_{j−1}), N_j) and Z_{j−1} is a coordinate of V_{j−1}. Hence A is a measurable function of (X, W_{<i}, N_{<i}).

*Step 2 (fresh inputs are conditionally independent of the past).* By ER-3 and ER-4, (W_i, N_i) ⊥ (X, W_{<i}, N_{<i}), hence by Step 1, (W_i, N_i) ⊥ (A, X) jointly. Since (X, Z_{i−1}) is a measurable function of (A, X), it follows that (W_i, N_i) ⊥ A | (X, Z_{i−1}). Conditional on (X, Z_{i−1}), the emission V_i = f_i(Z_{i−1}, φ_i(X, W_i, Z_{i−1}), N_i) is a measurable function of (W_i, N_i) and the conditioned values, so by the data processing inequality

> I(V_i; A | X, Z_{i−1}) ≤ I(W_i, N_i; A | X, Z_{i−1}) = 0.

*Step 3 (exchange).* Expanding I(V_i; (X, A) | Z_{i−1}) by the chain rule in both orders,

> I(V_i; X | Z_{i−1}) + I(V_i; A | X, Z_{i−1}) = I(V_i; A | Z_{i−1}) + I(V_i; X | A, Z_{i−1}).

Since Z_{i−1} is a function of A, I(V_i; X | A, Z_{i−1}) = I(V_i; X | A). With Step 2 this gives

> I(V_i; X | A) = I(V_i; X | Z_{i−1}) − I(V_i; A | Z_{i−1}) ≤ I(V_i; X | Z_{i−1}) ≤ ε_i,

using ER-5. Summing over i completes the proof. ∎

The proof isolates where each requirement acts. ER-2 (with ER-1) is what makes the received interface Z_{i−1} a sufficient statistic of the past for invocation i, so that the conditional budget prices everything the invocation can correlate with; Step 2 is exactly the point that fails when carried state survives (Proposition 5.5). ER-4 is what prevents the environment from smuggling upstream emissions into downstream contexts around the priced interface. ER-5's conditioning is what Proposition 4.3 showed to be irreplaceable.

**Corollary 5.2 (per-agent secrets variant).**
Suppose instead of ER-4 the contexts S_1, ..., S_N are mutually independent and jointly independent of {N_j} (exogenous per-agent secrets), and the budgets take the form I(V_i; S_i | Z_{i−1}) ≤ ε_i. Then

> I(T; S_1, ..., S_N) ≤ Σ_{i=1}^{N} ε_i.

*Proof.* Apply Theorem 5.1 with X := (S_1, ..., S_N), φ_i the i-th projection and W_i trivial; its hypotheses hold. It remains to reduce the theorem's budget to the stated one:

> I(V_i; S_{1:N} | Z_{i−1}) = I(V_i; S_i | Z_{i−1}) + I(V_i; S_{≠i} | Z_{i−1}, S_i),

and the second term vanishes: conditional on (Z_{i−1}, S_i), V_i is a function of N_i, while N_i ⊥ (S_{1:N}, N_{<i}) jointly and (Z_{i−1}, S_i, S_{≠i}) are functions of that tuple, so N_i ⊥ S_{≠i} | (Z_{i−1}, S_i). ∎

**Example 5.3 (the two-agent base as an instance).**
The parallel architecture of section 3.2 is the N = 2 composition with Z_1 = ⊥ and S_i = X: the budgets of ER-5 reduce to I(Y_S; X) ≤ C_S and I(Y_M; X) ≤ C_M, and Theorem 5.1 returns I(Y_S, Y_M; X) ≤ C_S + C_M, the additive bound of Theorem 3.1 in budget form. The composition framework strictly generalises the base architecture.

**Corollary 5.4 (composed error floor, and the deficit condition).**
Under the hypotheses of Theorem 5.1 with |𝒳| ≥ 3, any estimator X̂(T) of the source from the full transcript satisfies

> P_e ≥ (H(X) − Σ_i ε_i − 1) / log(|𝒳| − 1),

and, for H(X) ≥ log(|𝒳| − 1), P_e ≥ 1 − (Σ_i ε_i + 1)/H(X). Per ER-7, the declared deficit Σ_i ε_i < H(X) licenses strict incompleteness: retaining the binary-entropy term in Fano's inequality, P_e = 0 would force H(X | T) = 0 and hence I(T; X) = H(X), contradicting Theorem 5.1 under the deficit; so Σ_i ε_i < H(X) already implies P_e > 0. The displayed floor, which relaxes the binary-entropy term to one bit, is positive exactly under the stronger condition Σ_i ε_i < H(X) − 1; between the two thresholds the deficit still licenses P_e > 0 while the displayed linear bound is vacuous. The deficit is a numerical fact about the system-adversary pair at the evaluation time t of ER-6, not a consequence of ER-1 to ER-5. With certified budgets ε_i(t) non-decreasing in t, the composed shelf life is t*_lin = sup{t : Σ_i ε_i(t) < H(X)}, and what expires at t*_lin is the deficit, not the composition discipline: every structural requirement can hold while the floor decays to nothing. Per ER-6's certified-bound semantics, the expiry is a claim about the certification: at t*_lin the certificates no longer witness a deficit, and the floor that decays is the certified floor; nothing here asserts that the transcript's information about the source has grown.

*Proof.* Theorem 5.1 and Theorem 3.2 with Y := T. ∎

**Corollary 5.4b (informed-adversary floor; the erosion clock).**
Under the hypotheses of Theorem 5.1 with |𝒳| ≥ 3, let {B_t} be a background side-information family (Definition 3.9). Then:

(i) *(the cap survives conditioning)* for every t,

> I(T; X | B_t) = I(T; X) − I(T; B_t) ≤ I(T; X) ≤ Σ_i ε_i;

(ii) *(the floor erodes through the residual entropy)* any estimator X̂(T, B_t) of the informed transcript adversary 𝔄_tr(t), taking values in 𝒳, satisfies

> P_e(t) ≥ (H(X | B_t) − Σ_i ε_i − 1) / log(|𝒳| − 1),

and, when H(X | B_t) ≥ log(|𝒳| − 1), P_e(t) ≥ 1 − R_inf(t) − 1/H(X | B_t), where R_inf(t) := Σ_i ε_i / H(X | B_t);

(iii) *(monotonicity and expiry)* H(X | B_t) is non-increasing in t. Strict incompleteness of reconstruction by the informed adversary is licensed by the *informed deficit condition* Σ_i ε_i < H(X | B_t): retaining the binary-entropy term in Fano's inequality exactly as at Corollary 5.4, P_e(t) = 0 would force I(T, B_t; X) = H(X), while I(T, B_t; X) = I(B_t; X) + I(T; X | B_t) < (H(X) − H(X | B_t)) + H(X | B_t) = H(X) under the informed deficit. With certified budgets ε_i(t) non-decreasing (ER-6) and H(X | B_t) non-increasing, the informed shelf life t*_inf = sup{t : Σ_i ε_i(t) < H(X | B_t)} coincides with the first crossing.

*Proof.* (i) Expanding I(T; X, B_t) by the chain rule in both orders, I(T; X) + I(T; B_t | X) = I(T; B_t) + I(T; X | B_t); the second term on the left vanishes by Definition 3.9(ii), and Theorem 5.1 bounds I(T; X). (ii) Theorem 3.2 with Y := (T, B_t), using H(X) − I(X; T, B_t) = H(X | T, B_t) = H(X | B_t) − I(T; X | B_t) ≥ H(X | B_t) − Σ_i ε_i by (i); the normalised form follows as at Theorem 3.2 with H(X | B_t) in place of H(X). (iii) For s ≤ t, B_s is a measurable function of B_t, so H(X | B_t) = H(X | B_t, B_s) ≤ H(X | B_s); the exact-Fano computation is displayed in the statement; a non-decreasing left-hand side against a non-increasing right-hand side makes the deficit set an interval whose supremum is the first exit. ∎

The proof uses only Theorem 5.1's conclusion, so the corollary is portable to any composition carrying a certified transcript cap Σ_i ε_i, however obtained. Three readings fence the corollary. First, what erodes and what does not. The transcript's leakage about the source does not grow; by (i) its incremental value to the informed adversary, I(T; X | B_t) = I(T; X) − I(T; B_t), is non-increasing in t, since I(T; B_t) is non-decreasing by the data processing inequality along the accumulation. What erodes is the height of the floor, because the informed adversary's uncertainty about the source starts from H(X | B_t), not H(X). The protection does not leak more; it matters less. Second, the clock separation. ER-6's certified drift is epistemic: it records what an audit can license, and better estimation tooling can arrest or even reverse an over-conservative certificate. The drift here is real in the model's sense: what moves is the modelled quantity itself, not a certificate of a fixed quantity; the adversary's residual uncertainty does not rise, any fall in it is genuine, and no audit arrests it. A deployed guarantee therefore carries two dated components, a certified deficit against a declared decoder class (Corollary 5.4) and an informed deficit against a declared background family (this corollary), and the two expire independently. Third, vacuity at the far end. The normalised form's hypothesis H(X | B_t) ≥ log(|𝒳| − 1) itself expires as the background accumulates, leaving only the unnormalised display; and past t*_inf the floor is vacuous for every architecture satisfying every requirement, because the corollary bounds what the transcript adds to an informed adversary and cannot prevent the world from learning the source by other means.

### 5.2 Necessity and tightness

**Proposition 5.5 (necessity of erasure).**
Drop ER-2 only. Then no bound of the form I(T; X) ≤ g(Σ_i ε_i) with g(0) = 0 holds: there is a two-invocation composition with carried state, satisfying ER-1, ER-3, ER-4 and ER-5 with ε_1 = ε_2 = 0, in which I(T; X) = H(X).

*Construction.* Let X be uniform on {0,1}^m and let the agent draw a persistent uniform pad ρ ∈ {0,1}^m at first invocation (ρ ⊥ X), retaining it as carried state. Invocation 1 emits V_1 = O_1 = X ⊕ ρ with Z_1 = ⊥; invocation 2 emits V_2 = O_2 = ρ. Both conditional budgets are zero: I(X ⊕ ρ; X | ⊥) = 0 and I(ρ; X | ⊥) = 0. Yet O_1 ⊕ O_2 = X, so I(T; X) = m = H(X), with m arbitrary. The proof of Theorem 5.1 fails exactly at Step 2: with ρ surviving the boundary, V_2 is not conditionally independent of V_1 given (X, Z_1), and the correlation carried by ρ is priced by no budget. ∎

Each emission is individually a one-time-pad ciphertext or a pad, individually independent of the source; jointly they determine it. The construction is the composition-level form of the classical observation that per-component independence does not bound joint information, and it identifies undestroyed cross-invocation state as an unpriced channel. Together with Proposition 4.3 (which showed the conditional budget necessary while erasure held), it shows ER-2 and ER-5 are individually necessary; the next proposition adds the third construction, for ER-4.

**Proposition 5.5b (necessity of provenance).**
Drop ER-4 only. Then no bound of the form I(T; X) ≤ g(Σ_i ε_i) with g(0) = 0 holds: there is a two-invocation composition satisfying ER-1, ER-2, ER-3 and ER-5 with ε_1 = ε_2 = 0, in which a downstream context is assembled from an upstream emission around the declared interface and I(T; X) = H(X).

*Construction.* Let X be uniform on {0,1}^m. Invocation 1 holds a trivial context (φ_1 constant), draws N_1 uniform on {0,1}^m independent of X, and emits V_1 = O_1 = N_1 with Z_1 = ⊥ and ρ_1 = ⊥. The environment assembles the downstream context from the public upstream emission: S_2 = X ⊕ O_1, which violates ER-4 (assembly from an emission other than through Z_1). Invocation 2 emits V_2 = O_2 = S_2 with Z_2 = ⊥ and ρ_2 = ⊥. Both conditional interface-inclusive budgets are zero: I(V_1; X | Z_0) = I(N_1; X) = 0 and I(V_2; X | Z_1) = I(X ⊕ N_1; X) = 0. Yet O_1 ⊕ O_2 = X, so I(T; X) = m = H(X). Erasure holds at every boundary and no undeclared channel connects the invocations; the leak travels entirely through the environment's context assembly, the route ER-4 exists to exclude. The proof of Theorem 5.1 fails exactly at Step 2: V_2 is not of the form f_2(Z_1, φ_2(X, W_2, Z_1), N_2), and its dependence on the upstream randomness N_1 is priced by no conditional budget, since Z_1 = ⊥ carries nothing to condition on. ∎

Propositions 4.3, 5.5 and 5.5b are the paper's necessity constructions: the conditional form of the budget (ER-5), structural context erasure (ER-2), and context provenance (ER-4) are individually indispensable, each defeated at declared budget zero when dropped alone. No necessity construction is offered for ER-1 (declared channels) or ER-3 (fresh randomness); the results claim their sufficiency in conjunction with the rest, not their individual indispensability. By Theorem 5.1 the five together are sufficient.

**Proposition 5.6 (tightness).**
The cap of Theorem 5.1 is achieved: for X = (X_1, ..., X_N) with independent uniform bits, the composition O_i = X_i, Z_i = ⊥ satisfies all hypotheses with ε_i = 1 and I(T; X) = N = Σ_i ε_i. Hence Nε cannot be improved without further hypotheses.

**Remark 5.7 (the exponential-to-linear separation, and what remains empirical).**
Against the final-output adversary with marginal budgets and contaminated contexts, the available guarantee is the geometric sum Σ 2^{N−i} ε_i, i.e. (2^N − 1)ε uniformly (Theorem 4.1); under the composition discipline ER-1 to ER-5 the guarantee against the transcript adversary is Nε (Theorem 5.1). At N = 2 the uniform comparison is 3ε against 2ε; at N = 5, 31ε against 5ε; the ratio (2^N − 1)/N grows without bound. Three fences on interpreting the separation. First, it is a separation between *disciplines*, not mechanisms: Proposition 4.3 shows erasure without conditional interface-inclusive budgets caps nothing, Proposition 5.5 shows budgets without erasure cap nothing, and Proposition 5.5b shows budgets with erasure but without provenance cap nothing; the linear regime requires the conjunction. Second, it is a comparison of *guarantees*, not of attainable leakages, and its two ε parameters are not the same object. Both displays are upper bounds: no construction here or in the cited literature attains leakage of geometric order under marginal budgets, and the source's own depth measurements (Theorem 4.1's provenance note) do not exhibit geometric growth. Moreover the conditional interface-inclusive budget at level ε is the strictly more demanding constraint on an implementation than a marginal budget at the same numeral: Proposition 4.3's composition meets every marginal budget at zero while its conditional budget is I(V_2; S_2 | Z_1) = H(S_2). The comparison is therefore between the best guarantees available under each stated budget semantics, not a like-for-like ratio of leakages; the unconditional separation this paper proves is Proposition 4.3, where zero declared budget coexists with total transcript recovery of a context. Third, the mathematical content is now exhausted by the conditional theorems: what remains open is empirical, namely whether any given deployed system satisfies ER-1 to ER-5. That is a conformance property of an implementation, testable per instance by channel inventory (ER-1), runtime state audit (ER-2, ER-3), provenance analysis (ER-4) and leakage measurement against the declared class (ER-5, ER-6); it is an engineering hypothesis about a system, never a theorem about all systems, and this paper proves nothing about implementations that have not been so audited.

### 5.3 The grade criterion, stated as an open problem

The theorems above use the operational grade distinction of Definition 3.8 and never the deeper criterion. The deeper criterion is open, and we state it as an open problem with its proof obligations, because a positive resolution upgrades the *time* status of Grade-2 erasure: a Grade-2-erased context leaves nothing archived for a stronger decoder class to revisit, making erasure the only mechanism in the model whose guarantee would carry no certification index (contrast Corollary 5.4, where the certified deficit expires, and Corollary 5.4b, whose erosion clock is unaffected either way; see the scope note below).

**Open Problem 5.8 (obstruction-theoretic grade criterion).**
There exists a formalisation of the N-invocation system in which the retained local views (the variables surviving each boundary) are sections of a presheaf of partial reconstructions over a suitable cover of the joint observation space, such that: (a) erasure at a boundary is Grade 2 (Definition 3.8) if and only if the obstruction class to gluing the local sections into a global section witnessing the erased context is non-vanishing; and (b) erasure is Grade 1 if and only if the class vanishes and only the gluing data (key material) is withheld.

*Proof obligations.* (i) Construct the site: a cover and topology on which the candidate Čech class lives, for at least the two-agent instantiation. (ii) Prove the correspondence between recoverability-with-keys and vanishing of the class. (iii) Exhibit the class as a computable invariant in one non-trivial instance.

*The missing step, named.* Obligation (i) is unstarted: no candidate construction of the cover and topology has been written down; the sheaf-theoretic vocabulary is at present imported, not constructed. Nothing in sections 3 to 5 depends on this problem.

*Scope of the upgrade.* The time-status upgrade a positive resolution would license concerns the erasure guarantee itself: nothing archived remains for a stronger decoder class to revisit, so that guarantee carries no certification index. It does not arrest the erosion clock of Corollary 5.4b, which runs on background the adversary accumulates outside the system and is indifferent to every property of the composition, erasure included.

*Falsifier scope.* The statement is existentially quantified over formalisations and is therefore a research programme rather than a falsifiable conjecture: a failed candidate site refutes that candidate, not the existential. What is falsifiable is any fixed candidate criterion: once a site is fixed, any composition of retained views, under any future capability, that recovers Grade-2-erased material would exhibit a vanishing effective obstruction where the candidate criterion demanded a non-vanishing one, refuting that candidate. Obligation (i) is what converts the problem into a falsifiable conjecture, and it is unstarted; the label "open problem" rather than "conjecture" records exactly this.

### 5.4 Limits of the results

*(Seeds section 6; A3 content, A2 may reframe prose.)*

- Every result is conditional on ER-1 to ER-5, which are obligations, not observations. System-scale measurement of deployed multi-agent frameworks shows ER-1 is routinely violated today [elyagoubi2026agentleak]; a system that has not been audited against the requirements inherits nothing from Theorem 5.1.
- Nothing here bounds active adversaries, adversaries that corrupt an agent, or side channels outside the declared interfaces (timing, resource usage); the model is passive-observational.
- The cap Nε is a leakage bound, not a reconstruction impossibility. Strict incompleteness of reconstruction requires the declared deficit of ER-7, which is time-indexed and expires (Corollary 5.4). No sentence in this paper asserts a reconstruction ceiling without its preconditions and its time index, and none should survive editing that does.
- Theorem 4.1 is imported, not re-derived; Proposition 4.2 closes the same recursion in-model under local hypotheses (no carried state, independent noise, bounded contamination) whose correspondence to the source's hypotheses is a citation-resolution obligation.
- The exponential-to-linear comparison is a comparison of upper-bound guarantees under different budget semantics (Remark 5.7, second fence); no attainability construction for the geometric regime is exhibited or claimed. The unconditional separation is Proposition 4.3.
- The budgets ε_i(t) are certified upper bounds on fixed Shannon quantities (ER-6); every expiry statement is a claim about the certification, not about information accruing to the transcript (Corollary 5.4).
- The informed-adversary floor (Corollary 5.4b) is conditional on the Markov hypothesis of Definition 3.9. A background corpus containing transcript material violates it; conditioning on such a background can increase leakage beyond the cap, and the corollary is then inapplicable. The background family is a declared model, in the same sense that ER-6's decoder class is declared, and the empirical schedule of H(X | B_t) is not estimated here. Past t*_inf the floor is vacuous for every architecture: the corollary bounds what the transcript adds to an informed adversary; it cannot prevent the world from learning the source by other means.
- The Fano floor's normalised form carries an alphabet-entropy hypothesis (Theorem 3.2) frequently elided in informal statements.
- Per the programme's reporting discipline, a measured result against these predictions (for instance, a conformant system exhibiting super-linear transcript leakage) would be reported with the same prominence as a confirmation.

## 6. Threats to validity

**Conditionality and conformance.** Every result in this paper is conditional on ER-1 to ER-5, which are obligations on implementations, not observations about the world. System-scale measurement indicates that deployed multi-agent frameworks routinely violate ER-1 today [elyagoubi2026agentleak]. Conformance is testable per instance: channel inventory for ER-1, runtime state audit for ER-2 and ER-3, provenance analysis for ER-4, and leakage measurement against the declared decoder class for ER-5 and ER-6. The requirements are not equally auditable, and the ER-5 leg is the hard one. Conformance to ER-5 requires estimating a conditional mutual information between an invocation's full emission and the source given the received interface, a notoriously hard statistical problem for high-dimensional text channels, and this paper specifies no estimator. Such estimation is feasible only against restricted decoder classes, so an ER-5 conformance verdict is always relative to the class whose estimation and attack tooling produced it. This is one reason ER-6 indexes budgets by decoder class and time: under its certified-bound semantics, a certificate for ε_i(t) is only as strong as the class that produced it, and growth of the class can force the honest certificate upward. Conformance is an engineering hypothesis about a system, never a theorem about all systems; a system that has not been audited against the requirements inherits nothing from Theorem 5.1, and this paper asserts conformance for no deployed system.

**Adversary model.** The model is passive-observational. Nothing here bounds active adversaries, adversaries that corrupt or replace an agent, or side channels outside the declared interfaces, including timing and resource usage. Extending the ER-1 inventory to physical side channels is an audit problem this paper does not solve.

**Leakage versus reconstruction, and expiry.** The cap Σ_i ε_i is a leakage bound, not a reconstruction impossibility. The strict claim that reconstruction is incomplete additionally requires the declared capacity-deficit condition of ER-7, evaluated against the stated adversary class at a stated time, and that condition expires in the certified sense of ER-6: the certified budgets ε_i(t) are non-decreasing as the decoder class grows, and the floor of Corollary 5.4 decays to vacuity at the shelf life t*_lin while every structural requirement remains intact. What expires is what the certification licenses at time t; the transcript's mutual information about the source is a fixed functional of the joint law, and nothing here asserts that it grows. No sentence in this paper asserts strict incompleteness of reconstruction without the deficit condition and its time index, and none should survive editing that does.

**Two clocks, and the corpus model.** The expiry of the previous paragraph is certificational. Corollary 5.4b adds a second, real expiry: against an informed adversary whose background side information accumulates, the error floor erodes through H(X | B_t) with every certificate intact and no growth in what the transcript reveals. That result is conditional on the declared background family and its Markov hypothesis (Definition 3.9): whether any actual adversary's corpus satisfies the hypothesis, and how fast H(X | B_t) falls, are empirical questions this paper does not answer, symmetric to the conformance questions above. A deployed guarantee should declare its corpus model alongside its decoder class, and its two deficits expire independently.

**Import fidelity.** Theorem 4.1 is imported on its citation and not re-derived; its hypotheses (the source's Markov structure and the mutual independence of the sensitive variables) are carried inside the imported statement. Proposition 4.2 is proved here under our own local hypotheses (no carried state, independent noise, and bounded contamination), and its named condition and the source's hypothesis set are formally incomparable: the source's hypotheses do not imply bounded contamination, and bounded contamination does not imply them. No result in Section 5 depends on that correspondence.

**Statement precision.** The normalised form of the Fano floor requires the alphabet-entropy hypothesis of Theorem 3.2; for strongly non-uniform sources only the unnormalised display applies. The additive two-agent bound is an inequality with a stated equality condition, not an identity (Theorem 3.1).

**Reporting commitment.** A measured result against these predictions, for instance a system audited as conformant to ER-1 to ER-5 exhibiting super-linear transcript leakage, would falsify the conformance audit, the model's fit to that system, or the applicability of the theorem, and it would be reported with the same prominence as a confirmation.

## 7. Conclusion

We have given a composition model for sequentially invoked agents in which the two regimes of the recent multi-agent leakage literature are two sides of one architectural line. Without erasure and conditional interface-inclusive budgets, per-agent certification does not compose: the guarantee available on leakage about the joint secrets at the final output is only the geometric sum (Theorem 4.1, imported; an upper bound, with no attainability construction known), and against the transcript adversary marginal certification is vacuous even at budget zero (Proposition 4.3, the paper's unconditional separation). Under the five requirements ER-1 to ER-5, transcript leakage is capped by the sum of the declared budgets (Theorem 5.1); three of the five hypotheses are individually necessary (Propositions 4.3, 5.5 and 5.5b), and the cap is tight (Proposition 5.6). The exponential-to-linear comparison is a comparison of upper-bound guarantees under stated budget semantics, not of attainable leakages (Remark 5.7).

The framing discipline carries as much weight as the mathematics. What the architecture guarantees is additive accounting and an error floor whose height depends on declared numbers. The strict claim that reconstruction is incomplete is licensed only by a declared capacity-deficit at a stated time against a stated decoder class, and that component expires. Corollary 5.4b adds the second clock: even with every certificate intact, the floor an informed adversary faces is non-increasing, eroding as background side information accumulates, on a drift no audit arrests. Guarantees for deployed systems should be stated in this decomposed form: structural properties audited, numerical conditions declared and dated, the decoder class and the background corpus model both named.

Three items remain open. First, conformance: whether any given deployed system satisfies ER-1 to ER-5 is an empirical, per-instance question, and benchmark measurement of candidate conformant systems is future work. Second, the grade criterion: Open Problem 5.8 states a candidate formal separation between erasure that hides and erasure that forgets, with its proof obligations and its unstarted first step named; a positive resolution would upgrade the time status of the strongest erasure grade, since nothing archived would remain for a stronger decoder class to revisit. Third, the adversary model: active adversaries and physical side channels are outside the model, and the requirements' audit surface for them is undefined. The results are offered in the decomposed, conditional, dated form in which they are true.

## References

Cited by bib key against `templates/submission/references/pv_v6.bib` (60 verified entries as of 2026-07-07). The two entries formerly proposed as UNVERIFIED were verified and added by A4 on 2026-07-07; the UNVERIFIED markers are removed at each use:

- `gopala2008secrecy` (VERIFIED 2026-07-07, in bib): Gopala, P. K., Lai, L. and El Gamal, H., "On the Secrecy Capacity of Fading Channels", IEEE Transactions on Information Theory, 54(10), 2008, pp. 4687-4698, doi 10.1109/TIT.2008.928990. Role: time-varying-capacity precedent for the time-indexed budgets of ER-6 and Remark 3.4.
- `patil2025composition` (VERIFIED 2026-07-07, in bib): Patil, V., Stengel-Eskin, E. and Bansal, M., "The Sum Leaks More Than Its Parts: Compositional Privacy Risks and Mitigations in Multi-Agent Collaboration", arXiv:2509.14284. Role: independent composition-analysis corroboration of Theorem 4.1's regime, per the extraction record.

Verified keys used: `wyner1975wiretap`, `leungyancheong1978gaussian`, `csiszar1978broadcast`, `fano1961transmission`, `cover2006elements`, `asif2026infotheoretic`, `elyagoubi2026agentleak`, `gopala2008secrecy`, `patil2025composition`, `millen1987covert` (section 2), `sabelfeld2003language` (section 2), `dwork2014algorithmic` (section 2).

<!-- ============================================================
TRACEABILITY APPENDIX (GR-9; pipeline apparatus, STRIP AT RELEASE)

Section 3.2 / Thm 3.1            -> E1-c04 (additive form scoped to Precondition 1;
                                    stated here as inequality with equality condition,
                                    which is the mathematically exact form and implies
                                    the extraction's usage), E1-c01 (separation bound
                                    regime), E1-c05 (citation-family strategy)
Thm 3.2                          -> E1-c02 / E2-c01 (Fano floor component; alphabet
                                    hypothesis added here as precision, flagged in
                                    chronicle)
Thm 3.3                          -> E1-c03 (graceful degradation)
Remark 3.4                       -> E2-c01 (L044 decomposition, quoted structure),
                                    E2-c02 (R(t), t*), E1-c02 (deficit as declared
                                    fact); E2-c04 (sup-semantics caveat: sup = first
                                    crossing under monotone decoder-class growth,
                                    added 2026-07-08 per L069(b)); Gopala-Lai-El
                                    Gamal per A0 addendum (c)
Def 3.5-3.7                      -> E1-c06 (erasure definition, reachability form),
                                    E2-c11 (Grade-1/Grade-2)
Def 3.6 adversary figures        -> E1-c10 (AgentLeak measurements)
Def 3.8 / Open Problem 5.8       -> E1-c06, E1-c12 (C86 restated with proof
                                    obligations; register confidence deliberately
                                    omitted per TIER-A; restyled Conjecture -> Open
                                    Problem at revision-1 per A5 MINOR-7, register
                                    status of C86 unchanged, GR-1 respected)
ER-1                             -> E1-c01 Precondition 1, E1-c10
ER-2..ER-5                       -> E1-c06, E1-c08 (the chain-break mechanism, made
                                    theorem-shaped), E1-c36/c37 lineage acknowledged
                                    as design instances (not cited in body)
ER-6                             -> E1-c02 / E2-c01 preconditions; E2-c02 (t-index)
ER-7                             -> E2-c01 (capacity-deficit condition, "not a third
                                    precondition" discipline respected: stated as a
                                    separate requirement class for CLAIMS, not as a
                                    structural requirement)
Thm 4.1 (imported)               -> E1-c09 (exact statement granularity; E2-c12 dup)
Prop 4.2                         -> in-model derivation (A3); sufficient condition
                                    named, correspondence flagged to A4; hypotheses
                                    (i) no-carried-state and (ii) independent-noise
                                    added at revision-1 per A5 BLOCKING-1, proof's
                                    independence step now derived from them; the
                                    post-4.2 paragraph's "even without erasure"
                                    replaced by the no-carried-state wording with
                                    an inline counterexample showing (i) load-bearing
Prop 4.3                         -> in-model construction, this session (A3);
                                    interpretation traces to E1-c10 (inter-agent
                                    channel measurements); surfaced as the paper's
                                    unconditional separation at revision-1 per A5
                                    MAJOR-1
Thm 5.1, Cor 5.2, Ex 5.3,
Cor 5.4, Props 5.5/5.6           -> in-model results, this session (A3); the
                                    conjectured Nε cap of E1-c08 (C83) is the
                                    target statement, now proven conditional on
                                    ER-1..ER-5; Remark 5.7 states the empirical
                                    residue of C83 without register citation;
                                    Cor 5.4 thresholds reconciled (exact-Fano
                                    P_e > 0 under Σε < H(X); displayed floor
                                    positive under Σε < H(X) − 1) per A5 MINOR-1,
                                    expiry-as-certification clause per A5 MAJOR-2
Prop 5.5b                        -> necessity construction for ER-4, supplied by
                                    the A5 review memo (MINOR-4), verified and
                                    adopted by A3 at revision-1; numbered 5.5b to
                                    keep existing statement numbers stable until
                                    A8 port renumbers
Remark 5.7 figures (3ε/2ε etc.)  -> E1-c08 (worked comparisons); third fence
                                    (guarantee semantics, non-commensurable ε)
                                    added at revision-1 per A5 MAJOR-1
ER-1 rewording, ER-6 semantics   -> revision-1 per A5 MAJOR-3 / MAJOR-2: ER-1
                                    requantified over channels outside Definition
                                    3.5's declared components; ER-6 carries the
                                    certified-bound semantics of ε_i(t); ER-5
                                    gloss "auditable" -> "locally defined" with
                                    pointer to ER-6 (assist to MAJOR-4, A2's item)
Section 5.4 limits               -> GR-7, GR-8 discipline; E2-c01 (no strict bound
                                    without deficit + time index)
Def 3.9, Cor 5.4b, clock notes   -> in-model results, A3 session 2026-07-16;
                                    occasioned by the First-Person soil ruling and
                                    the branch-(c) direction (ledger L140/L143/L145);
                                    the erosion clock is the formal object the
                                    register's informational-capability typing of
                                    R(t) requires (E2-c02/E2-c04 re-pin target);
                                    zero new citation keys (side-information Fano
                                    via Thm 3.2 [cover2006elements]); Markov +
                                    declared-corpus fences per GR-7/GR-8; OP 5.8
                                    scope note added so the grade upgrade is not
                                    read as arresting the erosion clock

EXCLUSIONS (decisions, recorded in chronicle):
- E1-c40 (C91, Goedel reading of erasure): FEEDS WP-07 per extraction,
  but not formally statable at TIER-A without a reduction the register
  itself does not claim; excluded from this artifact, flagged to A0.
- E1-c07 (C17 qualitative), E1-c13..c26, c30..c35: outside the six
  definition-of-done items; conjecture apparatus not needed by the
  theory core; available to A2 for discussion sections only insofar
  as TIER-A permits formally stated conjectures.
- E1-c39 engineering rows: implementation material, WP-10's surface.

A2 ADDENDUM (completion pass, 2026-07-08; abstract, sections 1-2, 6-7;
A3's entries above untouched):
Abstract, sec 1, sec 7           -> restatements of in-paper results only (Thm 4.1
                                    import, Props 4.2/4.3, Thm 5.1, Props 5.5/5.5b/5.6,
                                    Cors 5.2/5.4, Remarks 3.4/5.7, Open Problem 5.8); no
                                    claim exceeds its in-paper statement; measurement
                                    hooks trace to E1-c09 (Asif-Amiri, Patil et al.)
                                    and E1-c10 (AgentLeak), stated qualitatively;
                                    exact figures remain solely in Def 3.6 and the
                                    Thm 4.1 provenance note
Sec 2 related work               -> the stub's citation list exactly, no additions;
                                    family-citation strategy per E1-c05; Asif-Amiri
                                    positioning (formal incomparability of hypothesis
                                    sets) per the A4 verification note, ORTHOGONAL
                                    verdict with counterexamples both ways
                                    (tasks/WP-07_A4.md)
Sec 6 threats to validity        -> prose expansion of section 5.4 (A3's seed list
                                    retained in place, unedited; the duplication
                                    resolves at A8 port time, where 5.4 seeds
                                    06_threats_to_validity); import-fidelity
                                    paragraph traces to the A4 note; conformance
                                    paragraph mirrors Remark 5.7
Sec 7 Open Problem 5.8 line      -> conditional restatement of section 5.3's own
                                    preamble; no strengthening

A2 REVISION-1 ADDENDUM (2026-07-09; prose legs of A5 review 1, per
tasks/WP-07_A2_revision.md and the A3 handoff list; A3's entries and
theory core sections 3-5 untouched):
Abstract, sec 1, sec 7           -> re-aligned to the revised theory core:
                                    guarantees framing for the exponential regime
                                    (MAJOR-1 prose leg; anchor Remark 5.7 second
                                    fence), necessity trio 4.3/5.5/5.5b (MINOR-4
                                    surface), Prop 4.2's local hypotheses named
                                    (BLOCKING-1 downstream), Open Problem 5.8
                                    naming (MINOR-7 downstream), "auditable"
                                    softened to "numbered"/"five requirements"
                                    (MAJOR-4); every change is a restatement or a
                                    weakening, no claim strengthened
Sec 2                            -> MINOR-6: csiszar1978broadcast re-anchored to
                                    broadcast-with-confidential-messages lineage;
                                    superadditivity stated as elementary with
                                    in-paper anchors (Thm 3.1 identity, Prop 5.5);
                                    MINOR-5: DP contrast sharpened (basic
                                    composition a theorem, advanced sublinear,
                                    worst-case quantification as the analogue of
                                    ER-5's conditioning); info-flow paragraph's
                                    "auditable at runtime" softened with pointer
                                    to sec 6; zero new citation keys
Sec 6                            -> MAJOR-4: estimation-gap passage (ER-5
                                    conformance requires MI estimation; feasible
                                    only against restricted decoder classes; one
                                    reason ER-6 indexes by class and time),
                                    type-consistent with ER-6's certified-bound
                                    semantics (A3, MAJOR-2); expiry sentence
                                    carries the certified-bound reading; import
                                    fidelity names Prop 4.2's local hypotheses
============================================================ -->
