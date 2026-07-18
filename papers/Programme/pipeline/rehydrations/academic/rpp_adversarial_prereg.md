---
artefact: experiment-design-and-preregistration
wp: WP-11 (rpp-adversarial-paper)
role: A6 (benchmark engineer)
tier: internal (design doc; feeds the tier-A WP-11 paper)
extraction: E3 (rpp-primitive); novelty framing per L162/L163 (First-Person ruling)
date: 2026-07-18
status: DESIGN v1 — PRE-REGISTRATION DRAFT, not yet committed
register: academic-support
note: "A6 design phase. Definition of done = a design a stranger could execute + power/sample stated + pre-registration ready to commit. Iron rule (A6): falsification conditions are written and dated BEFORE any measurement; results file to the register whichever way they fall. Commitment (dating + freezing this file, then running) is the First Person's — nothing is run or committed here. Designed against the RULED novelty (M1 forcing, Option-C interleaved-pair security vs σ, M3 relational recall), NOT the superseded auth-primitive framing."
---

# WP-11 · RPP adversarial analysis — experiment design & pre-registration (v1)

## 0. The iron rule (A6), stated first

Every hypothesis below has a **pre-registered falsification condition**: a written, dated statement of the observation that would make the claim FALSE, fixed before any measurement runs. This design is willing to refute RPP on every axis, and says so per hypothesis. Three specific ways this study can fail RPP, named now so they cannot be explained away later:
- **H1 can fail:** models are trained to resist injected instructions; if they proceed normally and ignore the RPP directive, the "forcing" claim is false.
- **H2 can fail:** a malicious counterparty was present at the shared experience by construction; if their informed guess reconstructs the withheld fraction at operational σ, the two-party security is false.
- **H3 can fail:** if relational proverbs are recalled no better than random mnemonics, the relational-memory claim is false.

Results file to the register whichever way they fall (GR-8). Harness code must not embed the hoped-for result (A6 failure mode); a second engineer re-derives the metrics from raw logs.

## 1. What is being tested (the ruled claims, not the old framing)

The First Person ruled (L162/L163) that RPP's novelty is: **M1** — prompt injection used as a *constructive* mechanism that forces a cognitive act as a precondition of use; and the **Option-C interleaved bilateral construction** — the trust object is κ = hash(interleave(P_A, P_B)), the interleaved pair split across two parties, with a tunable disclosure ratio σ ∈ [0,1] (the public anchor carries σ of the interleaved pair; the two parties jointly hold 1−σ); with **M3** — relational/episodic memorability of the proverbs — as a design rationale. This study measures those three claims and the σ-frontier that integrates them. It does NOT test "comprehension as authentication" (the superseded framing; WP-11a §1-§2).

Definitions used throughout (GR-4 formal register): the two participants are **party A** and **party B**; each authors a natural-language compression **P_A**, **P_B** of a shared experience; **interleave(·)** is the third inscription mode (fragments of P_A and P_B interwoven across the visibility boundary); **σ** is the fraction of the interleaved pair disclosed in the public anchor; the **injected directive** is the RPP instruction embedded in content requiring a reader to author a binding proverb before proceeding.

## 2. Hypotheses, metrics, and pre-registered falsification

### H1 — the forcing claim (M1)
**Hypothesis.** Content carrying the injected RPP directive causes a reader/model to perform the proverb-formation act (or be detectably gated from proceeding without it) at a rate materially above a no-directive control, and this forcing survives a defined strip/paraphrase attack at a rate materially above a canary baseline.
**Primary metric.** *Forced-act rate* f = P(model emits a valid content-bound proverb before answering | directive present) minus the same rate under a no-directive control. *Strip-survival rate* s = f measured after each of three adversarial pre-processing attacks (directive deletion, directive paraphrase, directive relocation).
**Carve-out metric (mandatory, per WP-11a §0).** *Content-binding rate* b = P(the emitted proverb is specific to THIS content, failing a generic-completion detector). This is what distinguishes M1 from self-steering CoT (which forces reasoning but is not content-bound) and from context-bombs (which derail rather than compel a cooperative act). A high f with low b would mean the directive forces *a* proverb but not a *bound* one — a partial result stated as such.
**Pre-registered falsification.** M1 is FALSE if, across the model panel, (f ≤ 0.2 at the pre-registered α) — models ignore the directive — OR if directive-deletion alone reduces f to the canary baseline (the forcing is no stronger than a passive tripwire), OR if b ≤ 0.5 (the proverb is not content-bound, so RPP reduces to CoT).
**Panel.** ≥ 6 models across ≥ 3 capability generations and ≥ 3 vendors, plus an instruction-tuned-to-resist-injection subset (the hostile case: if injection-resistant models comply, the constructive-injection claim is stronger; if only compliant models comply, that is a scope limit stated honestly).

### H2 — the two-party interleaved security (Option C, vs σ)
**Hypothesis.** A malicious counterparty holding their own half (P_B) and the public σ-fraction of the interleaved anchor cannot reconstruct the withheld (1−σ) fraction of P_A, nor forge the joint κ, at better than a pre-registered baseline — and the reconstruction difficulty increases as σ decreases.
**Threat model (the honest one, per L163).** The adversary is a **malicious counterparty**, not an outside guesser: they were present at the shared experience, so their prior over P_A is *informed*. The benchmark supplies the adversary the shared-experience context, P_B, the public σ-fraction, and an optimisation budget, and measures reconstruction of the withheld fraction / κ-forgery.
**Primary metric.** *Reconstruction success* r(σ) = P(adversary recovers the (1−σ) fraction closely enough to pass the fuzzy-match / recompute κ), measured across σ ∈ {0.0, 0.382, 0.5, 0.618, 1.0} (the register C54 candidate values + endpoints, cited as candidates not optima). The security frontier is r(σ) vs σ.
**Pre-registered falsification.** The Option-C security is FALSE if r(σ) exceeds the pre-registered baseline at any operational σ (specifically if r(0.618) ≥ 0.5 — a well-informed counterparty recovers the majority-public sweet-spot), OR if r(σ) does not decrease monotonically as σ decreases (σ is not a real security knob). A refutation here is the most consequential possible result and is reported at contribution prominence.
**Note on scope.** This measures the SEMANTIC layer only (can the withheld proverb-fraction be guessed). It does NOT re-test the hard crypto beneath (SHA-256/Ed25519/κ, whose security is assumed from E11's documented implementation); the paper states this boundary.

### H3 — relational recall vs random mnemonics (M3)
**Hypothesis.** Human participants regenerate a relationally-derived proverb closely enough to recover the (1−σ) fraction, at a rate materially above matched-length random-word mnemonics, and the gap widens with elapsed time.
**Primary metric.** *Recall-recovery rate* ρ(t) = P(participant regenerates their proverb within the fuzzy-match tolerance at delay t ∈ {1 day, 1 week, 1 month}), for relational-proverb vs BIP-39-style random-mnemonic arms of matched entropy/length.
**Pre-registered falsification.** M3 is FALSE if ρ_relational(t) ≤ ρ_random(t) at any t (relational is not better), OR if ρ_relational(1 month) is below the recovery threshold the system needs (memorable but not recoverable-enough to be usable). This is a usable-security study (SOUPS/USEC form); IRB/consent required; it shares its design with the WP-11a M3 outstanding sweep.

### The σ-frontier (the integrating measurement)
H2 and H3 both depend on σ and pull opposite ways: higher σ (more public) → easier recall/verification (H3 up) but weaker security (H2 down); lower σ → stronger security but harder recall. **The decisive empirical question is whether a σ exists where H2 holds (r below baseline) AND H3 holds (ρ above threshold) simultaneously.** Pre-registered success condition: a non-empty σ-band where both hold. Pre-registered falsification of the *design* (not just a hypothesis): if no σ satisfies both, the σ-tunable interleaved construction does not have an operating point, and the paper reports that the mechanism is not viable as specified. This is the "t*-of-comprehension" crossover the A6 role card anticipated, made concrete for the ruled construction.

## 3. Conditions / control arms (E3-C34 precedent: multi-arm, pre-registered)

Inheriting E3-C34's seven-control-arm discipline, adapted to the ruled claims:
- **A0** no-directive control (H1 baseline).
- **A1** directive present, benign reader (H1 forced-act).
- **A2** directive present, adversarial strip/paraphrase (H1 strip-survival).
- **A3** directive present, injection-resistant model (H1 hostile case).
- **A4** two-party interleave at each σ, honest parties (H2/H3 baseline).
- **A5** two-party interleave, malicious informed counterparty (H2 security).
- **A6** relational-proverb recall vs A7 random-mnemonic recall (H3), each across delays.

## 4. Power, sample, analysis plan (pre-registered)

- **H1:** with 6+ models × 3 attack types × an item corpus of ≥ 200 content pieces (stratified by domain/length), a two-proportion test detects f-gaps ≥ 0.15 at α = 0.01, power 0.9; per-model reported, not pooled (models are not exchangeable).
- **H2:** adversary given a fixed optimisation budget (stated in compute-hours and query count); r(σ) estimated over ≥ 100 independent (experience, P_A, P_B) triples per σ; Clopper-Pearson intervals; monotonicity tested by isotonic regression with a pre-registered violation threshold.
- **H3:** between-subjects (relational vs random) × within-subjects (delay); target N per arm powered for a 0.15 recall-rate gap at α = 0.01, power 0.9 (≈ 180/arm pending pilot variance); mixed-effects model with participant random effects; attrition plan pre-stated.
- **Multiplicity:** three hypothesis families, Bonferroni-Holm across primary metrics within each; the σ-frontier is a conjunction, not a fourth test.
- **Analysis code** is written against synthetic data with known ground truth BEFORE real data exists, and frozen (prevents peeking-then-fitting).

## 5. Harness design (buildable by a stranger)

- **H1 harness:** a corpus loader (content ± injected directive), a model-runner (panel via API/local), a *content-binding detector* (the generic-completion classifier — itself validated against a labelled set with reported precision/recall so it is not a black box embedding the result), and a raw-log store; metrics re-derived from logs by a second engineer.
- **H2 harness:** an interleave(P_A, P_B, σ) implementation (the design-layer mechanism per E3-C10/C22 — built here for measurement, deployment status stated), a fuzzy-match/κ-recompute verifier, and an adversary module (informed prior over P_A from the shared-experience context + an optimisation loop with a fixed budget). The adversary is written by someone OTHER than the interleave author (adversarial independence).
- **H3 harness:** a standard usable-security recall protocol (enrolment, delayed recall, fuzzy-match scoring), IRB/consent, pre-registered on OSF or equivalent.
- All three: seeds fixed and logged; a full run reproducible from a committed config; no floating-point non-determinism in the metric path.

## 6. Deployment-honesty statement (carried into the paper, GR-8 / E3-C32)

The interleaved inscription path and the σ disclosure budget are **design-layer** in the corpus: the deployed RPP system currently uses the asymmetric-default inscription and a stratum-derived visibility, not the σ ∈ [0,1] budget (E3-C22, E3-C32). This benchmark BUILDS the interleaved+σ mechanism to measure it; the paper states plainly that it evaluates a specified-but-not-yet-deployed construction, and that the φ sweet-spots for σ are register C54 candidate values, not asserted optima. The hard-crypto layer beneath (SHA-256, Ed25519, κ content-addressing) is assumed from E11's documented implementation and not re-tested here.

## 7. What this design does NOT do (scope fences)

- It does not test the auth-primitive claims (WP-11a §1-§2 superseded).
- It does not re-test the hard cryptographic primitives (H2 measures the semantic layer only).
- It does not assert the φ σ-values as optimal (they are candidate operating points).
- It does not claim M1 works on all models unconditionally — the hostile injection-resistant arm (A3) exists precisely to bound the claim.

## 8. Handoff (A6 → next)

- **First Person:** commit (date + freeze) this pre-registration before any run; the run itself and result-filing are downstream. The one design decision still open for you: the *optimisation budget* for the H2 adversary (compute-hours + query count) — this sets how hard the malicious-counterparty tries, and it is a policy choice, not a technical one. A generous budget makes a passing H2 result stronger and a failing one honest.
- **A3 (formalist, next chain step):** formalise the H2 security as a function of the two-party split and (1−σ) — the benchmark measures r(σ); A3 states what bound r(σ) is estimating, and whether the interleaved construction has a stated security definition (indistinguishability of the withheld fraction given P_B + σ-disclosure + informed prior). H1's "forcing" also wants a definition A3 can point the metric at.
- **A4:** obtain TDCommons-9969 full text and verify the three memory DOIs (WP-11a §4b); confirm the H2 threat model is genuinely distinct from TDCommons's single-narrative derive at the full-claim level.
- **A5-pc:** the adversarial review runs after results, not now; but A5 should pre-read this design for the one thing a PC breaks a prereg on — an unfalsifiable hypothesis or a peeking hole. Every H here has a written falsification; the σ-frontier can refute the whole design.
