# 2026-07-18 · A6 · RPP adversarial benchmark design + pre-registration

**Verdict first.** WP-11's next chain step is done: the A6 benchmark engineer drafted the experiment design and pre-registration for the RPP adversarial paper, against the *ruled* novelty (M1 forcing, Option-C interleaved-pair security vs σ, M3 relational recall) rather than the superseded auth-primitive framing. Three pre-registered hypotheses, each with a written falsification, integrated by the σ-frontier. Design v1 at `rehydrations/academic/rpp_adversarial_prereg.md`, four checks pass, ledger L164. Nothing run or committed — the commitment step (dating + freezing the prereg, and setting the adversary budget) is the First Person's.

## Why a prereg and not the paper

WP-11 is `prereg_required`, and the A6 iron rule is that falsification conditions are written and dated *before* any measurement. Two of the three core claims are still assertions — "the injection forces the thinking" (M1) and "the two-party split resists a malicious counterparty" — so a paper drafted before they're operationalized would overclaim. The prereg turns each into something that can come back false, and says so.

## The three hypotheses, each refutable

- **H1 (forcing).** The injected directive forces a *content-bound* proverb-formation above a no-directive control and survives strip/paraphrase above a canary baseline. Can fail: models are trained to resist injection; if they ignore the directive, M1 is false. The content-binding metric is the empirical form of the mandatory carve-out from CoT (which forces reasoning but not a *bound* act).
- **H2 (Option-C security vs σ).** A malicious *informed* counterparty — present at the shared experience, holding P_B and the public σ-fraction — cannot reconstruct the withheld (1−σ) of P_A. Measured as r(σ) across σ ∈ {0, 0.382, 0.5, 0.618, 1}. Can fail: if an informed counterparty reconstructs at the majority-public sweet-spot, or σ isn't monotone, the two-party security is false — and that refutation is reported at contribution prominence. Scope: the semantic layer only; the hard crypto (E11) is assumed, not re-tested.
- **H3 (relational recall).** Humans regenerate the relational proverb within tolerance above matched random mnemonics, gap widening with time. Can fail: no better than random, or not recoverable-enough at a month. A usable-security/IRB study, sharing its design with the outstanding WP-11a M3 sweep.

## The σ-frontier — the measurement that can sink the whole design

H2 and H3 pull opposite ways on σ: more public means easier recall but weaker security. The decisive question is whether a σ-band exists where *both* hold. If none does, the σ-tunable interleaved construction has no operating point, and the paper reports the mechanism non-viable-as-specified. This is the "t*-of-comprehension" crossover the A6 role card anticipated, made concrete for the ruled construction — and it means the design can refute not just a hypothesis but the architecture.

## Discipline carried

Seven control arms (E3-C34 precedent), pre-registered power/sample/analysis (per-model not pooled; analysis code frozen against synthetic ground truth before real data), adversarial independence (the H2 adversary written by someone other than the interleave author; the content-binding detector validated, not a black box), and a deployment-honesty statement (interleaved+σ are E3-C32 design-layer; φ values candidate not optima; hard crypto assumed from E11).

## Handoff

- **First Person:** commit and date the prereg before any run (the iron rule's non-delegable freeze); set the H2 adversary optimisation budget — a policy choice, not technical (a generous budget makes a passing H2 stronger and a failing one honest).
- **A3 (next chain step):** give H2 a security *definition* (indistinguishability of the withheld (1−σ) given P_B + σ-disclosure + informed prior) and state what r(σ) estimates; give H1's "forcing" a definition the metric points at.
- **A4:** TDCommons-9969 full text + the three memory DOIs; confirm H2's threat model is distinct from TDCommons at the full-claim level.
- **A5-pc:** pre-read for unfalsifiability/peeking holes now; the adversarial review proper runs post-results.
- The H3 usable-security study and the WP-11a M3 SOUPS/USEC sweep share a design — run once.

Nothing run, committed, or pushed. This is design + pre-registration only.
