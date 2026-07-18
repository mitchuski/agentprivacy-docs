# 2026-07-18 · A3 · RPP formalism

**Verdict first.** WP-11's formal spine is drafted: the A3 formalist gave the two ruled claims precise statements — forcing (behavioral) and withheld-fraction security (a conditional information-theoretic reduction) — and enforced the discipline that they are separate registers. `rehydrations/academic/rpp_adversarial_formalism.md`, tier-A register, four checks pass, ledger L165. The security is reduced to two quantities the A6 benchmark already measures; the one remaining piece of load-bearing math is a First-Person construction decision (which concrete interleave).

## The two properties, kept apart

The whole point of this section is that RPP's two claims live in different registers and must never be conflated (the modal error of E6-C06, made concrete):

- **Forcing (Definition 1)** is a *behavioral* property of a reader population under the injected directive — `(f, b, s)`-forcing: it raises the probability of a *content-bound* proverb by `f`, binds to the content at rate `b`, survives strip attacks at `s`. It is explicitly **not** a security guarantee (Remark 1): a model performing the act is a success of the mechanism, not a break. And it is model-relative (Remark 2): forcing is the *dual* of injection-resistance, so `f` weakens on hardened models — the honest scope is carried in the reader population itself. The coordinate `b` is what separates RPP from chain-of-thought (which forces reasoning but with `b ≈ 0`, self-directed).

- **Security (Definitions 2–3, Proposition 4)** is *information-theoretic* and holds regardless of whether any reader "understood." It rests on the residual fuzzy conditional min-entropy of A's proverb given a co-participant's complete knowledge, `H̃(P_A | P_B, E)`, and on the interleave's leakage `δ`. Proposition 4 is a **proven-conditional reduction**: `ε ≤ 2^(−(m−δ))`, with two gaps named rather than hand-waved (interleave-faithfulness, the fuzzy-sketch entropy-loss term).

## Why this is the honest form

- **The brain-wallet discharge is now precise, not asserted.** The critique says a single human-memorable secret has low entropy against a public target. Proposition 4 shows the security here is not one proverb's entropy but `H̃(P_A | P_B, E)` — A's residual entropy *given a co-participant's full knowledge of the shared experience and their own half*. So the critique isn't refuted by hand — it's relocated to a measured quantity `m`, and the honest threat is exactly the informed co-participant.
- **The benchmark and the math meet.** Corollary 5: `r(σ)` estimates `ε(σ)`, and the pre-registered falsification `r(0.618) ≥ 0.5` *is* the formal statement `m − δ ≤ 1 bit`. So H2 measures precisely the two inputs Proposition 4 reduces security to.
- **Monotonicity is a labelled conjecture, not a theorem** (Proposition 6): `ε` decreases as `σ` decreases *if* the interleave is "graceful," and the missing step — that a concrete interleave actually adds entropy as it withholds more — is named and left refutable by H2's isotonic test.
- **The firewall (§5)** partitions everything: proved-conditional / definition / empirical / engineering-requirement / conjecture / cited-substrate / assumed. Nothing is asserted unconditionally secure. Fuzzy extractors (DRS 2004, JW 1999) are cited as substrate, not claimed. The kinship to WP-07's Corollary 5.4b (same informed-adversary conditional-entropy family) is cited without asserting identity.

## Handoff

- **First Person — the remaining load-bearing math:** choose a *concrete* interleave `I` and show it faithful (Prop 4 gap i) and graceful (Prop 6). Until an `I` is fixed, the security is a template, not a theorem. This is a construction decision, separate from the earlier architecture ruling.
- **A6:** add one measurement — `δ(σ) = I(A_σ; W)` directly — so both of Proposition 4's inputs are measured rather than one inferred. No other benchmark change.
- **A4:** cite DRS 2004 + JW 1999 at primary records (already in the WP-11a spine); confirm the fuzzy conditional min-entropy notation matches the source.
- **A5-pc (post-results):** the two places a PC breaks this are the named Proposition-4 gaps and the gracefulness conjecture — both labelled, both empirically refutable, which is the defensible posture. Check the paper never states Proposition 6 as proved.
- **The paper is now A2-draftable** on the skeleton — forcing (Def 1, H1-measured) + the conditional security reduction (Prop 4, H2-measured) + the σ-frontier (H2×H3) — once a concrete `I` is fixed.

Nothing run, committed, or pushed.

## Addendum · interleave I* ruled + the dance-not-stance grounding

The First Person ruled the concrete interleave: **I\*** (extract-then-block-interleave, the graded path over all-or-nothing). This binds the formalism to an object — Definition 7 + Theorem 8. Choosing I\* discharges the two named gaps by reducing them to the fuzzy extractor's standard guarantee: splitting becomes δ ≤ δ_ext (bounded, not empirical, because a co-participant re-derives the other party's blocks and the rest is near-uniform), faithfulness is met by the symmetric schedule, and **gracefulness is proven for I\*** (uniform independent blocks), upgrading Proposition 6 from Conjecture to Proposition. Theorem 8: ε ≤ 2^(−((1−σ)·m − δ_ext)), monotone in σ. The whole security question collapses to **one empirical unknown, m** — how guessable a proverb is to a co-participant who was there — which is exactly benchmark H2.

The First Person also grounded *why* the graded path: in the understanding-as-key research the disclosure-security trade is the generative mechanism, **"identity as a dance, not a stance"** — a stance is a static held secret; a dance is an ongoing relational disclosure whose trajectory over σ is the identity. Graded σ is the formal shadow (AONT would force a stance). The residual-entropy kernel is in the swept source (understanding-as-key :872, "attackers cannot enumerate without understanding the relationship itself" = m); the *phrase* "dance not stance" was NOT located there and is flagged as an A1/A4 SOURCES item — locate the further understanding-as-key document, add to SOURCES, cite at primary record before WP-11's motivation leans on it. The formal statements stand independently of the framing.

The WP-11 formal spine is now complete for A2 drafting: forcing + a concrete-construction security theorem + the σ-frontier grounded as the dance-not-stance thesis.
