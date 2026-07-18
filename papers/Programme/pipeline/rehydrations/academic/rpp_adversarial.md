---
title: "Compelled Comprehension: Prompt Injection as a Cooperative Mechanism and a Two-Party Interleaved Construction for Relational Key Recovery"
wp: WP-11 (rpp-adversarial-paper)
role: A2 (register-translator) — draft skeleton
tier: A
venue: SOUPS or Financial Cryptography (usable security / applied crypto)
extraction: E3 (rpp-primitive); prior art WP-11a; benchmark prereg (A6); formalism (A3)
date: 2026-07-18
status: DRAFT v1 (A2 skeleton — structured claim-marked draft, not final prose; A7 voice pass and A3/A6 section-insertion pending; A5-pc review post-results)
register: academic
note: "A2 skeleton per role discipline: every used claim maps to a section and carries its STATUS marker; nothing exceeds its source STATUS; GR-4 vocabulary applied; no percentage confidences (GR-2 tier-A). Components: related work from WP-11a; construction+security from rpp_adversarial_formalism.md (Defs 1-3/7, Theorem 8, Prop 6); experimental design from rpp_adversarial_prereg.md (H1-H3, σ-frontier). Results sections are DESIGN-ONLY (prereg_required; no data exists). STATUS markers: [DEF] definition, [THM-C] proven-conditional theorem, [CONJ] labelled conjecture, [EMP] empirical/measured-by-Hn, [SUBST] cited substrate, [RESIDUE] WP-11a novelty residue, [DEPLOY] E3-C32 design-vs-deployment boundary, [NARR→neutral] narrative-canon restated register-neutrally per GR-4."
---

# Compelled Comprehension: prompt injection as a cooperative mechanism and a two-party interleaved construction for relational key recovery

## Abstract [skeleton]

Prompt injection is studied almost exclusively as a threat. We invert it: an injected directive can be a *cooperative* mechanism that compels a reader to perform a designated generative act — authoring a short natural-language compression (a proverb) bound to the content — as a precondition of use [DEF: forcing, Def 1]. We build on this a two-party construction for key recovery in which two participants who share an experience each author a proverb independently; the trust object is the *interleaved pair*, split across the two parties with a tunable disclosure ratio σ, over a hard-cryptographic substrate [DEF: construction; SUBST: fuzzy extractors]. We give the construction a security definition against the honest adversary — a malicious *informed counterparty* — and prove a conditional bound reducing security to a single measurable quantity: the residual entropy of a proverb given a co-participant's complete knowledge [THM-C: Theorem 8]. We state a pre-registered experiment that can refute each claim: whether the injection forces the act, whether an informed counterparty reconstructs the withheld share, and whether relational proverbs are recalled better than random mnemonics; and we identify the disclosure-security frontier over σ as the decisive measurement [EMP: H1-H3]. We claim no unconditional security, and we distinguish the mechanism (compulsion) from the guarantee (two-party entropy) throughout.

## 1. Introduction [skeleton]

**Motivation.** Credential recovery today rests on a *static held secret*: a stored seed, a set of guardian shares, a memorised passphrase. This paper explores the alternative in which access is a matter of an ongoing relational disclosure rather than a fixed possession — identity carried as an ongoing process between parties rather than a stored configuration [NARR→neutral: the seventh-capital "identity as an ongoing relational disclosure, not a static held credential" reading; formal kernel at the understanding-as-key lineage]. The security question this raises is precise: if what you recover from is a shared understanding, how much of it can a party who *shared the experience* reconstruct?

**Contribution.** Three, none of them the crowded "comprehension-as-authentication" framing (which we show is anticipated, §2):
1. *Forcing as a cooperative use of prompt injection* [RESIDUE: M1; DEF: Def 1]. The injected directive compels a content-bound generative act as a precondition of use. The novelty is the cooperative, embedded, content-binding use of a mechanism the literature treats only as an attack; we do not claim unforgeability, and we make the distinction from self-directed chain-of-thought and from adversarial "context bombs" explicit and measurable.
2. *A two-party interleaved construction with a tunable disclosure ratio* [RESIDUE: Option C; DEF: Def 7]. The secret is the interleaved pair of two independently authored proverbs, split across two parties; σ tunes how much of the shared knowledge the public anchor carries. The construction is a human-readable surface over a hard-cryptographic substrate, not a replacement for it [DEPLOY].
3. *A security definition and a conditional theorem* [THM-C: Theorem 8] reducing security to one measurable quantity, together with a pre-registered experiment that can refute it [EMP].

**Posture.** We claim no unconditional security; every security statement is conditional on a quantity the pre-registered experiment measures, and every mechanism claim is bounded by a named scope. The experiment is registered before it is run, and its falsification conditions are stated in §5.

## 2. Related work [from WP-11a]

**The auth-primitive axis is crowded — and is not our pitch** [RESIDUE: the superseded framing]. Read as "authenticate by demonstrated comprehension," the idea is anticipated: cognitive authentication [Weinshall 2006], the Turing-test-as-auth lineage [Naor 1996; von Ahn et al. 2003], knowledge-based authentication [Ellison et al. 2000; Just-Aspinall 2009; Schechter et al. 2009], and the named category "cognitive authentication" in the comparative framework of [Bonneau et al. 2012]. GOTCHA [Blocki-Blum-Datta 2013] already binds a human-generated response to a stored commitment. We do not claim this axis.

**Prompt injection is studied as a threat** [RESIDUE: M1 positioning]. The corpus is adversarial: indirect injection [Greshake et al. 2023], direct injection [Perez-Ribeiro 2022], OWASP LLM01. The only constructive uses are *adversarial-defensive* — "context bombs" that derail a hostile agent [Tracebit 2026] and canary/tripwire honeypots — or *self-directed* reasoning steering [Kojima et al. 2022]. Cooperative injection that compels a legitimate reader's content-bound generative act as a use-precondition is, to our search, unoccupied; the paper distinguishes itself from context bombs (cooperative vs adversarial) and from chain-of-thought (content-bound vs self-directed) explicitly.

**Key-from-shared-context and fuzzy extraction is the substrate we build on** [SUBST]. Independent derivation from shared context is prior art [Mayrhofer-Gellersen 2009]; every such scheme converges the two inputs to the *same* token and verifies equality. We do not; the interleaved pair is two divergent authorings, never compared for equality. The reproduce-from-noisy-input primitive is [Dodis-Reyzin-Smith 2004; Juels-Wattenberg 1999]; we cite it as substrate and claim no part of it. The one direct neighbour is a defensive publication that *derives* a key from a *single* narrative [TDCommons 9969]; our construction is bilateral, injection-forced, and carries a graded disclosure ratio, none of which it has.

**Compression-as-comprehension is a background thesis we do not assert** [RESIDUE: N3 demoted]. That compression ratio tracks capability is an established and separately contested claim [Chaitin 2006; Delétang et al. 2024; Huang et al. 2024; contra arXiv:2306.02305]; we use compression only as an internal instrument and make no general claim.

## 3. The construction [from formalism §1, §2, §6]

**3.1 Proverbs and the injected directive** [DEF: Def 1]. Two parties A and B share an experience E and each author a natural-language compression P_A, P_B (a *proverb*, the protocol's term for a short content-bound summary). The directive is injected into the content and requires a reader to author a proverb bound to that content before proceeding. We call the directive *(f, b, s)-forcing* over a reader population if it raises the probability of the bound act by f over a no-directive baseline, the act is content-specific at rate b, and the gap survives strip/paraphrase attacks at s [DEF: Def 1]. Forcing is a behavioral property of a reader population, model-relative (it is the dual of injection-resistance), and is *not* a security guarantee [DEF, Remark 1-2]. The coordinate b separates the mechanism from self-directed chain-of-thought.

**3.2 The interleaved bilateral pair I\*** [DEF: Def 7]. A fuzzy extractor whitens each proverb to near-uniform bits s_A, s_B (tolerating rewording, removing natural-language redundancy) [SUBST]; a symmetric block schedule interleaves them into a stream Z; the public anchor discloses a σ-fraction of Z, the two parties jointly hold the (1−σ); the commitment is κ = H(Z) [DEF]. The choice of the graded interleave I* over an all-or-nothing transform is what makes σ a smooth disclosure knob rather than a binary switch.

**3.3 Layering: a human-readable surface over hard crypto** [DEPLOY]. The whitened stream Z is the security layer; the human-readable proverb is a separate surface layer serving knowledge-sharing and recall. σ applies to both in lockstep. The hard-cryptographic layer (the hash, the signatures, the content-addressing) is assumed from the implementation record and not re-derived here. The interleaved inscription path and the σ budget are, in the deployed system, design-layer rather than shipped [DEPLOY: E3-C32]; this paper evaluates the specified construction and says so.

## 4. Threat model and security [from formalism §3, §6]

**4.1 The honest adversary: a malicious informed counterparty** [DEF: Def 3]. The adversary is party B, who was present at E and holds their own proverb P_B, the shared context E, and the public anchor A_σ. This is the correct threat model, not an outside guesser: a co-participant holds one half by construction. The construction is *(t, ε)-secure* if the probability that the adversary reconstructs the withheld fraction W within fuzzy tolerance t is at most ε [DEF: Def 3].

**4.2 The security theorem** [THM-C: Theorem 8]. Under the interleave I*, the construction is (t, ε)-secure with ε ≤ 2^{−((1−σ)·m − δ_ext)}, where m is the residual fuzzy conditional min-entropy of A's proverb given a co-participant's knowledge and δ_ext is the extractor's bounded uniformity loss. The bound is monotone in σ [THM-C, with Prop 6 proven for I*]. Choosing I* discharges the interleave's two requirements (faithfulness, gracefulness) into the extractor's standard guarantee, leaving one empirical unknown: m [EMP: H2].

**4.3 What this does and does not claim** [DEF, Remark; the layering]. Security rests on the two-party entropy split, not on the forcing (§3.1): a reader performing the compelled act contributes nothing to security unless m is high. The brain-wallet objection — that a single memorable secret is low-entropy against a public target — does not apply, because there is no single-party secret: security is m = H̃(P_A | P_B, E), and the objection is relocated to a measured quantity, with the honest residual being the informed co-participant [RESIDUE: brain-wallet discharge]. We claim no unconditional security; the strongest statement is (t, 2^{−((1−σ)·m − δ_ext)})-secure, with m measured (§5).

**4.4 The disclosure-security frontier** [EMP: σ-frontier]. Higher σ shares more readable knowledge but lowers (1−σ)·m; lower σ is more secure but harder to recover (§5, H3). The decisive question is whether a σ-band exists where security and recoverability both hold; if none does, the construction has no operating point, and we report that [EMP].

## 5. Experimental design and pre-registration [from prereg; DESIGN-ONLY, no data]

The falsification conditions below are pre-registered before any measurement; results will be filed whichever way they fall. Three hypotheses, each refutable [EMP]:

- **H1 (forcing).** The directive is (f, b, s)-forcing over a model panel spanning capability generations, vendors, and an injection-resistant subset. *Falsified if* models ignore the directive, a trivial strip defeats it, or the emitted proverb is not content-bound (reducing the mechanism to chain-of-thought) [EMP].
- **H2 (security vs σ).** A malicious informed counterparty cannot reconstruct the withheld fraction; reconstruction success r(σ) estimates ε(σ) over σ ∈ {0, 0.382, 0.5, 0.618, 1} [CONJ: φ-candidate σ values, register C54, candidates not optima]. *Falsified if* r(σ) exceeds the pre-registered baseline at an operating σ or is not monotone [EMP]. Scope: the semantic layer only; the hard crypto is assumed.
- **H3 (relational recall).** Human participants regenerate a relational proverb within tolerance above matched random mnemonics, gap widening with time. *Falsified if* no better than random at any delay [EMP]. The recall advantage's premise is established memory science [Craik-Lockhart 1972; Slamecka-Graf 1978], so the claim is the systems application, not the effect.

**The σ-frontier** integrates H2 and H3: a non-empty σ-band where both hold is the pre-registered success condition; its absence refutes the construction as specified [EMP]. Power, sample, analysis plan, and harness (with adversarial independence between the interleave author and the reconstruction adversary) are in the design document; analysis code is frozen against synthetic ground truth before real data.

## 6. Limitations and honesty [GR-8]

- The interleaved path and σ budget are design-layer, not deployed [DEPLOY: E3-C32].
- We drop the word "unforgeable": the compelled act is reproducible by any equally-capable model, and forcing is a behavioral, model-relative property, weaker on injection-resistant readers [DEF, Remark 2]. This is a scope, stated.
- Security is conditional on m, an empirical quantity; a low-m proverb (one a co-participant can guess) is insecure under any interleave [THM-C caveat].
- The φ values for σ are candidate operating points, not asserted optima [CONJ].
- We make no general compression-equals-comprehension claim [RESIDUE: N3 demoted].
- Monotonicity in σ is proven for the chosen interleave I* but is a conjecture for arbitrary interleaves [CONJ: Prop 6 scope].

## 7. Conclusion [skeleton]

Prompt injection, read as a cooperative mechanism, compels an authored act; a two-party interleaved construction over a hard-cryptographic substrate turns two such acts into a recoverable secret whose security is exactly the residual entropy of one party's proverb given the other's knowledge. The construction claims no unconditional security and is stated so that a single pre-registered experiment can refute each of its three claims.

## Appendix · claim traceability [A2 discipline]

| Section | Claim | Source | STATUS |
|---|---|---|---|
| 3.1, Abstract | forcing (f,b,s) | formalism Def 1 | [DEF] behavioral, model-relative, not a guarantee |
| 3.2 | interleave I* | formalism Def 7 | [DEF] construction |
| 4.1 | informed-counterparty security | formalism Def 3 | [DEF] |
| 4.2 | ε ≤ 2^{−((1−σ)·m − δ_ext)} | formalism Theorem 8 | [THM-C] proven-conditional on extractor + m |
| 4.2, 6 | monotonicity in σ | formalism Prop 6 | [CONJ] proven for I*, conjecture for arbitrary I |
| 4.3 | brain-wallet discharge | WP-11a §3 + formalism §4 | [RESIDUE] relocated to measured m |
| 4.4, 5 | σ-frontier | prereg + formalism §6 | [EMP] can refute the construction |
| 5 | H1/H2/H3 + falsifications | prereg H1-H3 | [EMP] design-only, no data |
| 2 | related-work positioning | WP-11a §0-§5 | [RESIDUE]/[SUBST] |
| 3.2, 4.2 | fuzzy extractor | DRS 2004 / JW 1999 | [SUBST] cited, not claimed |
| 1 | dance-not-stance motivation | poems/tide-orbit-selene.md:26 (narrative-canon) + Zypher :872 | [NARR→neutral] restated; formal kernel cited |
| 3.3, 5, 6 | deployment status | E3-C32 | [DEPLOY] design-layer, stated |

**Downstream markers for the chain.** A7 (voice): a polish pass on §1/§7 only; the formal and experimental sections are A3/A6 territory and their STATUS markers must survive. A3: insert the full Definitions 1-7 and Theorem 8 statements into §3-§4 verbatim from the formalism (this skeleton summarises them). A6: insert the full pre-registration (arms, power, harness) as an appendix or supplement. A4: verify every §2 citation at primary record before submission (the WP-11a spine + TDCommons-9969 full text + the three memory DOIs). A5-pc: review post-results; the two break-points are the named Proposition-4 gaps and the Prop-6 scope. Nothing in this draft exceeds its source STATUS (A2 definition of done).
