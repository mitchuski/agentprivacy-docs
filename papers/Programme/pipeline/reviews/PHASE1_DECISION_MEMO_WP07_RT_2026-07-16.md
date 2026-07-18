# Phase-1 decision memo: what does WP-07's R(t) measure, and what may WP-14's durability leg claim?

**Date:** 2026-07-16
**Occasion:** Phase 1 of `plans/SOIL_PROPAGATION_PLAN_2026-07-16.md` (the gate). Ledger L141 headline 1; L142.
**Posture:** this memo is decision PREP. It lays out the readings, quotes the exact passages, and traces the consequences of each branch. It decides no theory and edits no artifact. The ruling is A3's and the First Person's (GR-10). One candidate construction is sketched for branch (c); it is unverified and is routed to A3 as a proof obligation, not adopted.
**Documents:** `rehydrations/academic/linear_cap_paper.md` (WP-07, revision-draft-v2, AWAITING-P4); `rehydrations/academic/weis_seventh_capital.md` (WP-14, draft-v3); `research/pvm-v6-soil-and-the-programme-runtime-evolutions.md` (the ruling, L140).

---

## 1. The question

> Does the time drift of WP-07's R(t) measure (a) adversary reconstruction of a fixed archive under growing informational capability, (b) auditor certification of a fixed true value, or (c) two separable clocks, of which the economics may cite one?

Everything in evolution 3 hangs on the answer: the Phase-2 re-pin of E2-C02 (the single source of the moving-ceiling chain), the WP-14 durability leg (the sharpened M3 blocker), and the wording of every downstream moving-ceiling surface. Until the object is named, it is unknown whether the fix is a re-wording or a re-derivation.

## 2. Exhibit A: what WP-07 actually says

The paper is not ambiguous. It states the certification reading explicitly, in four places, and the certified-bound semantics was ADDED deliberately at A5 review 1 (MAJOR-2, ledger L077) to repair an earlier overclaim. The relevant passages, quoted exactly:

**ER-6 semantics paragraph** (`linear_cap_paper.md:225`):

> "The quantities the theorems consume are Shannon functionals of the joint law: I(O_i, Z_i; X | Z_{i-1}) depends on no decoder class and does not change as adversaries improve. [...] What is non-decreasing in t is therefore the certified value, not the information: growth of the class can expose leakage a weaker class missed, forcing the honest certificate upward or its revocation, while the underlying mutual information is constant. [...] every time-indexed statement in this paper, in particular the expiry of Corollary 5.4, is a statement about what the certification licenses at time t, not a statement that information accrues to the transcript. The same reading applies to the time-indexed capacities of Remark 3.4."

**Corollary 5.4** (`linear_cap_paper.md:332`):

> "Per ER-6's certified-bound semantics, the expiry is a claim about the certification: at t*_lin the certificates no longer witness a deficit, and the floor that decays is the certified floor; nothing here asserts that the transcript's information about the source has grown."

**Section 6, threats to validity** (`linear_cap_paper.md:390`):

> "What expires is what the certification licenses at time t; the transcript's mutual information about the source is a fixed functional of the joint law, and nothing here asserts that it grows."

**Remark 3.4** (`linear_cap_paper.md:170`) defines R(t) = (C_S(t) + C_M(t))/H(X) "with capacities evaluated against the strongest decoder class available at time t", with the fading-wiretap precedent [gopala2008secrecy]; per the ER-6 cross-reference, those capacities carry the certified-bound reading.

**Structural observation (load-bearing for the branches).** The model of Definition 3.5 contains NO variable representing adversary side information. The adversary classes of Definition 3.6 differ only in WHICH transcript coordinates they observe (final output vs whole transcript), never in what they know from outside the system. H(X) is fixed by the source; I(T; X) is a fixed functional of the joint law; the ONLY time-dependent object anywhere in WP-07 is the certificate epsilon_i(t). There is nothing in the model that can grow with the calendar except what the auditor knows.

## 3. Exhibit B: what the economics requires

**The ruling (evolution 3)** (`research/pvm-v6-soil-and-the-programme-runtime-evolutions.md`, L131-154):

> "What actually drifts is the adversary's informational capability, his accumulating linkage corpus and side priors, against a release that is never re-queried. [...] R(t) is a calendar-time, adversary-informational-capability erosion clock. [...] the guarantee the durability leg imports (WP-07) must bound reconstruction under growing linkage and side information, not under growing compute, or the security half and the economic half of the model describe different objects."

**WP-14 Section 2, the clock distinction the paper now defends against the DP strand** (`weis_seventh_capital.md:285-289`):

> "R(t) runs a different clock. It indexes a single fixed release, never re-queried, whose per-subject reconstruction residual rises as the adversary's informational capability, its accumulating linkage corpus and side priors rather than its computational power, which differential privacy already saturates, grows along calendar time."

This is a claim that the adversary's actual reconstruction ability rises. It is exactly the claim WP-07's ER-6 declines to make.

**Also found, and needed regardless of branch: WP-14 is internally split.** Its own Assumption A3 (`weis_seventh_capital.md:558-569`) still carries the pre-L139 compute-flavoured drift:

> "As frontier capability grows the numerator drifts upward against a fixed archive while H(X) does not, so R(t) drifts upward on a schedule..."

Section 2 says informational capability, not compute; Section 3's Assumption A3 says frontier capability driving the NUMERATOR. These do not agree with each other, before either agrees with WP-07. The A3-assumption display also inherits whichever object the Phase-1 ruling names (see the numerator/denominator point in Section 5 below). This is a pipeline artifact fix for the WP-14 revision loop, not canon; it is filed with this memo's ledger entry.

## 4. The three readings, assessed against the text

### Reading (a): reconstruction; the fix is wording only. NOT AVAILABLE.

The plan's branch (a) assumed WP-07 might already prove adversary-reconstruction erosion and merely say it badly. The text forecloses this. The paper does not omit the erosion reading; it DENIES it, three times, in load-bearing review-hardened passages (Section 2 above), and the denial is correct in the model as stated, because the model contains no adversary side-information variable through which real erosion could enter. Re-wording ER-6 to say the adversary's information grows would make the paper assert something its own model cannot express and its own theorems do not touch. Branch (a) should be recorded as formally closed. The live choice is (b) against (c).

### Reading (b): certification; the proven object is the certificate clock. TRUE OF THE CURRENT TEXT.

This is what WP-07 proves today. If the ruling adopts (b) alone, i.e. leaves WP-07 as is:

- The WP-14 durability leg reverts to a stated open problem. The honest fallback is already drafted and named in WP-14 (`weis_seventh_capital.md:966-968`): "If the companion that proves the guarantee ... is not citable when this paper is submitted, the durability claim must be withdrawn to a stated open problem." The withdrawal trigger changes from "not citable" to "citable but proves a different object", which the L141 audit already sharpened M3 into.
- WP-14 Section 2's clock distinction survives as a DEFINITIONAL distinction (the empty-cell fact of L139 stands: no DP refinement runs a calendar-time adversary-capability clock) but loses its proven underwriting; the paper must say the erosion clock is posited, not proven.
- Phase 2's re-pin of E2-C02 still proceeds, but the moving-ceiling chain must carry the same honesty label: the informational-erosion drift is a register conjecture with no theorem behind it.
- The inalienability bridge (evolution 4, "durable for the term R(t) permits") weakens to the same conditional status.

Cost: honest, immediate, submission-safe only with the durability leg withdrawn. Nothing in WP-07 changes, so its AWAITING-P4 status is undisturbed.

### Reading (c): both clocks, separated, with the erosion clock derived. AVAILABLE, REQUIRES A SMALL RE-DERIVATION.

The machinery to express real erosion exists in WP-07's own toolkit; what is missing is one modelled variable and one corollary. Candidate shape, routed to A3 as a proof obligation (NOT verified here):

Introduce the adversary's side information as an explicit, calendar-indexed variable: a family Z_adv(t) (the accumulating linkage corpus and side priors), non-decreasing in t in the sense that Z_adv(s) is a function of Z_adv(t) for s <= t, with the Markov hypothesis **Z_adv(t) -- X -- T** (the corpus is information about the source gathered from the world, not a tap on the transcript; a tap is an ER-1 violation already excluded).

Two displays then follow from the existing theorems:

1. **The budget survives conditioning.** Under the Markov hypothesis, I(T; X, Z_adv) = I(T; X) + I(T; Z_adv | X) = I(T; X), and expanding the other way, I(T; X | Z_adv(t)) = I(T; X) - I(T; Z_adv(t)) <= I(T; X) <= Sigma_i epsilon_i. The linear cap of Theorem 5.1 is not eroded by the corpus.
2. **The floor erodes through the denominator.** Fano with side information, for any estimator X-hat(T, Z_adv(t)):

   P_e(t) >= (H(X | Z_adv(t)) - Sigma_i epsilon_i - 1) / log(|X| - 1).

   The deficit condition becomes **Sigma_i epsilon_i < H(X | Z_adv(t))**, and the shelf life t*_adv = sup{t : Sigma_i epsilon_i < H(X | Z_adv(t))}. H(X | Z_adv(t)) is non-increasing in t as the corpus grows. This is real erosion, of exactly the object the economics names: the transcript never says more (display 1), the certificates never weaken, and the protection still expires, because the adversary's residual prior uncertainty about the source sinks toward the declared budgets.

Note what this does to the SHAPE of R(t): WP-07's current ratio puts the drift in the NUMERATOR (certified capacities grow); the erosion clock puts it in the DENOMINATOR (residual source entropy given the corpus shrinks). The natural erosion ratio is R_adv(t) = Sigma_i epsilon_i / H(X | Z_adv(t)), rising in t with fixed budgets. The soil figure is exact for it: the plot (X) is fixed, nothing is added to it, and the cover (H(X | Z_adv(t))) is stripped by the weather (the corpus) on a calendar. If (c) is adopted, E2-C02, WP-14's Assumption A3 display, and the spec's moving-ceiling sections should re-pin to this object, and WP-07 keeps ER-6's certificate clock beside it, explicitly named as a different clock (the paper then carries three: the certificate clock, the erosion clock, and the DP composition clock it already distinguishes in related work).

What (c) costs and risks:

- A3 must verify the two displays and their hypotheses (the Markov condition doing all the work; where the corpus DOES contain transcript material, the erosion and the leakage interact and the clean split fails, which is worth a stated fence).
- WP-07 gains a definition, a corollary, and a related-work sentence; it is AWAITING-P4 after a full review cycle, so the addition re-opens P3 checks (and arguably a targeted A5 look), a real cost against the PoPETs windows named in its apparatus note.
- The empirical status of H(X | Z_adv(t)) and its schedule is a register conjecture exactly as the current drift schedule is; (c) does not manufacture a measured schedule, it types the object the conjecture is about.
- Honesty guard: the corollary must not be advertised as bounding what corpora adversaries actually hold; it conditions on a declared corpus model the way ER-6 conditions on a declared decoder class.

### The decision, restated for the ruling

- **(b)** = leave WP-07 untouched; WP-14 durability leg withdraws to a stated open problem; the moving-ceiling chain re-pins with a "posited, not proven" label.
- **(c)** = add the side-information variable and the erosion corollary to WP-07 (A3 verification + one review touch); WP-14 durability leg stands on the new corollary with the deficit condition restated as Sigma epsilon_i < H(X | Z_adv(t)); the chain re-pins to the denominator-drift object.
- Either way, WP-14's internal A3-assumption/Section-2 split is fixed in the revision loop, and Phase 2's sweep wording follows the branch.

## 5. Consequences table

| Surface | Branch (b) certification only | Branch (c) two clocks, erosion derived |
|---|---|---|
| WP-07 text | unchanged (AWAITING-P4 undisturbed) | + side-information definition, + erosion corollary, + related-work sentence; P3 re-run, targeted A5 look advisable |
| WP-14 durability leg | withdrawn to stated open problem (fallback at :966 executes) | stands, citing the erosion corollary; Assumption A3 display re-typed to H(X | Z_adv(t)) form |
| WP-14 M3 gate | closes by honest withdrawal | closes by reconciliation; submission gate wording per L138(c) still applies |
| WP-14 S2 clock distinction | definitional only; label as posited | proven-underwritten (conditional on corpus model) |
| E2-C02 re-pin (Phase 2) | informational drift as register conjecture, "no theorem behind it" label | informational drift typed to the denominator object, corollary citable |
| Evolution-4 bridge (lease the harvest) | conditional, same label | stands for the term t*_adv permits |
| Soil figure | analogy only | analogy with a display behind it (weather = Z_adv(t), cover = H(X | Z_adv(t))) |

## 6. What this memo does not do

It does not choose (b) or (c); that is the First Person's with A3's verification. It does not edit WP-07, WP-14, E2, or any canon surface. It does not assert the candidate corollary is true; the two displays above are unverified sketch until A3 works them. It does not mark P4 or any gate.

**Recommended next mechanical steps once ruled:** (b) -> execute WP-14's drafted fallback in the revision loop, then unblock Phase 2 with the conjecture label; (c) -> A3 session on WP-07 (verify displays, place the corollary), then the WP-14 revision-loop fix, then Phase 2 with the typed object.
