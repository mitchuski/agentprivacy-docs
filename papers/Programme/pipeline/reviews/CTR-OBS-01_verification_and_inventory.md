# CTR-OBS-01 · Independent Verification and Blast-Radius Inventory

**Seat:** A3 (Formalist) · cycle 11 · card per L121(a)
**Date:** 2026-07-10
**Inputs:** OBSERVER_INTAKE_PROTOCOL.md (binding), OBS-GPT56_DISPOSITION_LEDGER.md §1.4 (OBS-GPT56-011) and §2 (CTR-OBS-01, CTR-OBS-02), L121, the pipeline artifact set, the canon specification (READ-ONLY).
**Writes:** this file and the seat chronicle only. No artifact, extraction, rehydration, manifest, ledger, or canon surface is modified. Per protocol rule 5, the formal correction is PROPOSED here and routes through the register on Mitchell's ruling; prose patches never precede it.

Verdict first. The observer's decomposition is correct and standard (Part 1 derives it from first principles; every step is a Cover and Thomas identity). Under Precondition 1 the joint leakage is SUBADDITIVE, not additive: exact additivity requires, in addition, marginal independence of the two outputs. The reconstruction floor P_e >= 1 - (C_S + C_M)/H(X) SURVIVES unconditionally within the Precondition-1 regime, because the capacity-sum numerator upper-bounds the true joint information there; the marginal-redundancy term only raises the true floor, so the stated guarantee is conservative and the correction tightens the model favourably. The defect is confined to the wording class "holds exactly (when)" attached to the equality form. Part 2 inventories every carrying surface: the three awaiting-P4 papers are ALREADY CONFORMANT (WP-07 and WP-04 state the inequality with the exact equality condition and no proof anywhere uses exact additivity; WP-27 carries no additivity content), the live pipeline sites reduce to ONE extraction claim (E1-C04) and ONE rehydration sentence (WP-03 grant edition, which inherits E1-C04's wording verbatim), and the equality-form sites otherwise live in canon and on canon-adjacent surfaces, where only the register process may act.

---

## Part 1 · Independent verification

Notation: X the source, Y_S and Y_M the two agents' observation outputs, all standard Shannon quantities in bits (Cover and Thomas, *Elements of Information Theory*, 2nd ed., 2006; chain rule Thm 2.5.2, non-negativity of conditional mutual information Cor 2.6.3 / 2.90, Fano Thm 2.10.1). Capacities C_S, C_M satisfy I(X; Y_S) <= C_S and I(X; Y_M) <= C_M against the declared class (the pipeline's Assumption 2 / Precondition 2). Precondition 1 is I(Y_S; Y_M | X) = 0 with no third channel carrying the inter-agent residue.

### 1.1 The chain rule

> I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M | Y_S).   (1)

This is the chain rule for mutual information (Cover and Thomas Thm 2.5.2) and holds with no assumptions.

### 1.2 The interaction identity

> I(X; Y_M | Y_S) = I(X; Y_M) − I(Y_S; Y_M) + I(Y_S; Y_M | X).   (2)

Derivation from entropies. By definition,

- I(X; Y_M) − I(X; Y_M | Y_S) = [H(Y_M) − H(Y_M|X)] − [H(Y_M|Y_S) − H(Y_M|X, Y_S)],
- I(Y_S; Y_M) − I(Y_S; Y_M | X) = [H(Y_M) − H(Y_M|Y_S)] − [H(Y_M|X) − H(Y_M|X, Y_S)].

Both right-hand sides equal H(Y_M) − H(Y_M|X) − H(Y_M|Y_S) + H(Y_M|X, Y_S); this common value is the co-information (interaction information) of the triple. Hence I(X; Y_M) − I(X; Y_M | Y_S) = I(Y_S; Y_M) − I(Y_S; Y_M | X), which rearranges to (2). Identity (2) is unconditional.

### 1.3 The exact decomposition

Substituting (2) into (1):

> **I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M) + I(Y_S; Y_M | X).**   (3)

This is the observer's stated relation (OBS-GPT56-011), verified. It is symmetric in S and M, as it must be.

### 1.4 Consequence under Precondition 1: subadditivity

Set I(Y_S; Y_M | X) = 0 in (3):

> I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M) <= I(X; Y_S) + I(X; Y_M),   (4)

since I(Y_S; Y_M) >= 0. **Equality holds if and only if additionally I(Y_S; Y_M) = 0 (marginal independence).** Precondition 1 therefore licenses SUBADDITIVITY, not additivity. Note that under Precondition 1 the triple forms the Markov chain Y_S — X — Y_M, so by data processing I(Y_S; Y_M) <= min(I(X; Y_S), I(X; Y_M)): the redundancy term is bounded by the smaller marginal leakage, and it is typically strictly positive precisely when both channels carry overlapping information about X.

The "holds exactly when" formulation is wrong in both directions as an equivalence:

- **Precondition 1 does not give equality.** Any pair of channels both genuinely informative about X in overlapping ways has I(Y_S; Y_M) > 0 under Precondition 1, and (4) is then strict.
- **Equality does not require Precondition 1.** By (3), equality holds iff I(Y_S; Y_M) = I(Y_S; Y_M | X); both can be positive. Witness: W a uniform bit independent of X, Y_S = Y_M = W. Then I(Y_S; Y_M) = I(Y_S; Y_M | X) = 1, Precondition 1 fails, and I(X; Y_S, Y_M) = 0 = I(X; Y_S) + I(X; Y_M).

### 1.5 The floor survives, and tightens favourably

Under Preconditions 1 and 2, (4) with the capacity bounds gives

> I(X; Y_S, Y_M) <= I(X; Y_S) + I(X; Y_M) <= C_S + C_M.   (5)

Fano's inequality (Cover and Thomas Thm 2.10.1) for any estimator X̂(Y_S, Y_M) over the alphabet 𝒳, |𝒳| >= 3, gives H(X | Y_S, Y_M) <= 1 + P_e log(|𝒳| − 1); with H(X | Y_S, Y_M) = H(X) − I(X; Y_S, Y_M) >= H(X) − (C_S + C_M) by (5),

> P_e >= (H(X) − C_S − C_M − 1) / log(|𝒳| − 1),   (6)

and in the rounded house form (alphabet-entropy hypothesis H(X) >= log(|𝒳| − 1), and eliding the 1/H(X) term as WP-04's precision note records), P_e >= 1 − R_max with R_max = (C_S + C_M)/H(X). **The numerator C_S + C_M upper-bounds the true joint information under Precondition 1, so the floor computed from it remains valid; it is conservative.** The true joint information is C_S + C_M diminished by at least the redundancy I(Y_S; Y_M) (evaluating (4) at the capacity-attaining laws), so the true error floor sits ABOVE the declared one by I(Y_S; Y_M)/log(|𝒳| − 1) in the unnormalised form. The correction moves the guarantee in the deployer's favour; nothing downstream weakens. Equivalently: the effective ceiling is R_true = R_max − I(Y_S; Y_M)/H(X) <= R_max, so the declared R_max is an upper bound on the true ratio, which is the only direction any ceiling statement uses.

### 1.6 What would break it, stated precisely

1. **Failure of Precondition 1.** If I(Y_S; Y_M | X) > 0, (3) shows joint information can EXCEED the sum, without bound relative to the marginals. Extremal witness (the pipeline already carries it as WP-07 Prop 4.3 / Prop 5.5's family): Y_S, Y_M iid uniform bits, X = Y_S xor Y_M. Then I(X; Y_S) = I(X; Y_M) = 0 yet I(X; Y_S, Y_M) = H(X) = 1. The floor computed from C_S + C_M is then invalid as stated; WP-07 Theorem 3.3 prices small violations (joint <= sum + ε when I(Y_S; Y_M | X) <= ε).
2. **Can I(X; Y_M | Y_S) <= C_M fail in general?** Yes. In the xor witness, I(X; Y_M | Y_S) = 1 while I(X; Y_M) = 0 <= C_M = 0 is consistent with a zero-capacity certificate: the conditional term is not bounded by the marginal capacity in general, because (2) adds I(Y_S; Y_M | X). **Does it matter for the floor under Precondition 1? No.** With I(Y_S; Y_M | X) = 0, (2) gives I(X; Y_M | Y_S) = I(X; Y_M) − I(Y_S; Y_M) <= I(X; Y_M) <= C_M automatically. The chain-rule sum (1) is then bounded by C_S + C_M with no further hypothesis; the conservative floor needs nothing beyond Preconditions 1 and 2.
3. **Failure of Precondition 2** (capacities certified against too weak a class) breaks (5) at the capacity step, not at the decomposition; that is CTR-OBS-02 / ER-6 territory, out of this card's scope but noted for the joint ruling.
4. **Interaction with R(t) and composition** (the CTR-OBS-01 filing's last clause). In repeated interaction the favourable term is the marginal redundancy I(Y_S; Y_M), which grows only to the benefit of the bound; the dangerous term is the conditional dependence I(Y_S; Y_M | X), which is exactly what accumulating cross-agent state creates. This is already the content of WP-07's Prop 5.5 (persistent pad) and the ER-1/ER-2 discipline: the formal write-up should state that the composition threat enters through the LAST term of (3), not the third.

**Verification verdict: OBS-GPT56-011's mathematics is CORRECT; the disposition ledger's amendment (the ceiling survives and tightens favourably) is CORRECT; the defect class is precision of the equality wording only.** This is standard information theory throughout; nothing here is new mathematics.

---

## Part 2 · Blast-radius inventory

Classification key: **(i) EXACT** = exact-additivity wording (equality asserted, or "holds exactly (when)" attached to the equality); **(ii) BOUND** = capacity-sum / at-most / additive-rather-than-compounding wording, already consistent with subadditivity; **(iii) UNAFFECTED** = no additivity claim carried, or the "exactly" is the genuine definitional iff of the deficit condition (R_max < 1 iff C_S + C_M < H(X), which is unaffected by CTR-OBS-01 and must not be swept up in the fix).

### 2.1 Pipeline extractions

| Site | Wording (quoted) | Class | Touchable | Fix on ruling |
|---|---|---|---|---|
| extractions/E1-amnesia-gap.md:50 (E1-C04) | "I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly when the two observation channels are conditionally independent given X ... (Precondition 1)" | **EXACT** | A1-writable, but only AFTER the canon corrects (E1-C04 quote-traces spec §16/§14.7; GR-9 forbids an extraction stronger or weaker than its source; the L044 order of operations applies: register/canon first, then A1 re-issue) | One sentence: "is at most I(X; Y_S) + I(X; Y_M) when ... (Precondition 1), with equality iff additionally I(Y_S; Y_M) = 0" |
| extractions/E1-amnesia-gap.md:34 (E1-C02) | "Preconditions 1 and 2 ... license the additive capacity sum and prove the floor" | BOUND | (A1) | None required; optional "capacity-sum bound" hygiene |
| extractions/E1-amnesia-gap.md:79 (E1-C08) | "caps total leakage at the additive bound Nε" | BOUND | (A1) | None |
| extractions/E2-moving-ceiling.md:20-21 (E2-C01) | "the capacity sum C_S + C_M is licensed as additive and the Fano error floor ... holds"; the "holds exactly when" at the deficit condition is the definitional iff | BOUND / UNAFFECTED | (A1) | None |
| extractions/E7-identity-vrc.md:17 | ownership pointer: "the additive-leakage claim [is] owned by E1 (E1-C04)" | UNAFFECTED (pointer; inherits E1-C04's eventual wording) | (A1) | None |
| extractions/E10-method-record.md:194 | "additive model changes" (versioning vocabulary) | UNAFFECTED (different sense of "additive") | — | None |

### 2.2 Pipeline rehydrations, per artifact

**WP-07 · rehydrations/academic/linear_cap_paper.md · awaiting-P4 · UNTOUCHABLE (hard stop) · needs NOTHING.**
Already CTR-OBS-01-conformant; it contains the Part-1 mathematics in full:

- :130-141 Theorem 3.1 is stated as the INEQUALITY "I(X; Y_S, Y_M) <= I(X; Y_S) + I(X; Y_M), with equality if and only if additionally I(Y_S; Y_M) = 0", proved via the chain rule and the interaction identity, i.e. exactly (1)-(4) above. :143: "The inequality direction is all that any downstream guarantee uses."
- :159 Theorem 3.3 prices ε-violations (item 1.6.1 above). :166 Remark 3.4's "holds exactly when" is the deficit-condition definitional iff, class (iii), correct as written. :325 Example 5.3 "the additive bound of Theorem 3.1 in budget form" names the bound. :394 threats-to-validity states it verbatim: "The additive two-agent bound is an inequality with a stated equality condition, not an identity (Theorem 3.1)."
- **Per-theorem proof dependence (the load-bearing question):** Thm 3.1 proves the bound (uses (1)+(2), concludes <=). Thm 3.2 is Fano, no additivity. Thm 3.3 uses (2) with the ε slack. Thm 5.1's proof is chain rule + data processing + budget inequalities only, every step one-directional. Cor 5.2 and Cor 5.4 consume Thm 5.1's inequality. Props 4.2, 4.3, 5.5, 5.5b are explicit constructions. Prop 5.6 (tightness) exhibits one instance attaining the cap (independent components), an existence statement, not an appeal to a general equality law. **No proof in WP-07 uses exact additivity; every result needs only subadditivity.** The paper's results are untouched by CTR-OBS-01 under any ruling.

**WP-04 · rehydrations/academic/moving_ceiling_sok.md · awaiting-P4 · UNTOUCHABLE (hard stop) · needs NOTHING.**

- :206 Proposition 1(a) is the capacity-sum bound "I(X; Y_S, Y_M) <= I(X; Y_S) + I(X; Y_M) <= C_S + C_M, with equality in the first inequality if and only if I(Y_S; Y_M) = 0", proof :218 via the same interaction identity; attribution :220 names it "the standard sub-additivity of leakage under conditional independence". :222's "holds exactly when" is the deficit-condition iff, explicitly flagged in-text as definitional, class (iii). :258/:266 name the missing joint-estimator sub-additivity clause for effective capacities as an open desideratum (correct posture). :64 records the 2026-07-07 A3 pass that tightened "additive" to bound wording suite-wide in this paper.
- **Proof dependence:** Prop 1(b) consumes only 1(a)'s outer bound; Lemma 1 is a supremum-monotonicity argument, no additivity. **No WP-04 proof uses exact additivity.**

**WP-27 · rehydrations/academic/conjecture_governance_method.md · awaiting-P4 · UNTOUCHABLE · UNAFFECTED.** Grep confirms no additivity content (the sole "holds exactly" is seat discipline prose, :253).

| Site | Wording (quoted) | Class | Touchable | Fix on ruling |
|---|---|---|---|---|
| WP-03 rehydrations/grants/grant_edition.md:133 | "additive mutual-information leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), holds exactly when the two observation channels are conditionally independent given X" [E1-C04] | **EXACT** (inherits E1-C04 verbatim) | Release-draft-v3 at P1, chain complete, pre-P4: reopenable by a ruled A2/A3 micro-card | One sentence, same as E1-C04's; sequenced after the E1-C04 re-issue so the trace stays exact |
| WP-03 grant_edition.md:111, :131 | "additive rather than compounding"; "the capacity sum is licensed as additive" | BOUND | — | None |
| WP-03 grant_edition.md:166, :172 | "the additive bound Nε" (twice, WP-A benchmark framing) | BOUND | — | None |
| WP-02 rehydrations/policy/enforceable_by_architecture.md:322 | "the leakage of the two channels is additive rather than compounding" | BOUND | Release-draft-v6 at P1 (release-strip pending) | None required; optional "at most additive" hygiene if a card ever reopens the file |
| WP-02 :122, :218 | apparatus/trace-map "additive-capacity structure", "additive-leakage structure" | BOUND | — | None |
| WP-09 rehydrations/standards/bgin_separation_of_duties.md:280 | "two structural facts are proven: the leakage of the two channels is additive rather than compounding, and the reconstruction error floor P_e >= 1 - R_max holds" | BOUND | Release-draft-v3 at P1, pre-P4 | None required; optional one-word tightening ("at most additive") on the same ruled card if reopened |
| WP-09 :284, :318 | "the additive guarantee above" (pointer to :280); OQ-2 "cap total leakage at additive growth" | BOUND | — | None |
| Public: competence_without_history.md:31 | "caps linearly ... 31ε and 5ε" with honesty label | BOUND | draft-v3 at P0 | None |
| Public: the_moving_ceiling.md, the_uncarved_date.md, letter_the_fleet_and_the_cap.md, two_agents_walk_into_a_circuit.md | no additivity claims | UNAFFECTED | — | None |

### 2.3 Canon and canon-adjacent surfaces (READ-ONLY; inventory only; register process / first person)

| Site | Wording (quoted) | Class | Fix class on ruling |
|---|---|---|---|
| papers/v6/privacy_value_v6_formal_specification.md:679 (§14.7) | "§16 asserts additive leakage, I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), at 95% confidence ... additivity holds exactly when the channels are conditionally independent given X and nothing carries the inter-agent residue, which is Precondition 1" | **EXACT** (the strongest instance: "holds exactly when" as an iff, wrong in both directions per §1.4) | One sentence |
| papers/v6/privacy_value_v6_formal_specification.md:778 (§16 table) | "**Additive MI bounds** \| Mutual information leakage from conditional independence is additive, not multiplicative: I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M)" | **EXACT** | One table cell ("at most additive: I <= sum, equality iff marginal independence") |
| papers/v6/privacy_value_v6_formal_specification.md:786 (§16 "Scoped, not lowered") | "additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly in the Precondition-1 regime" | **EXACT** | One sentence |
| papers/v6/privacy_value_v6_formal_specification.md:426 (§10.5) | "the additive capacity sum, and with it the error floor ... hold in the regime ... and only there"; the deficit-condition paragraph's "holds exactly when, additionally, C_S + C_M < H(X)" | BOUND-leaning ambiguous ("additive capacity sum ... hold"); the deficit "exactly" is the genuine iff, class (iii) | Optional one word ("the capacity-sum bound") |
| papers/v6/privacy_value_v6.md:132 | "additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) holds exactly in the Precondition-1 regime" | **EXACT** (same sentence family as spec :786) | One sentence |
| papers/v6/privacy_value_v6.md:88 | "The bound, the additivity of the capacity sum of §11, and the error floor hold when ..." | BOUND-leaning ambiguous | Optional one word |
| papers/v6/dualprivacy_researchpaper_v6.md:30 (§2.2) | "The additive-leakage result I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M), asserted at 95% in the v4.3 lineage, holds at that confidence inside the non-collusion regime only" | **EXACT** | One sentence |
| papers/v6/pvm_v6_compressed.md:112 | "**Theorem (95%):** Conditional independence ⟹ additive MI bound ⟹ R_max < 1" | **EXACT**, and additionally carries the pre-L044 conflation (preconditions ⟹ R_max < 1) apparently unswept by the L044 execution | Structural for the line (two defects in one display); flagged for the register process as an L044 propagation gap as well as a CTR-OBS-01 site |
| papers/v6/pvm_v6_compressed.md:235 | "Additive leakage I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) at 95% inside Precondition 1 only" | **EXACT** | One sentence |
| papers/whitepapers/swordsman_mage_whitepaper_v6_3.md:747 | "When observations are conditionally independent, information leakage becomes additive rather than multiplicative" | EXACT-leaning ambiguous ("becomes additive") | One word ("at most additive") |
| papers/whitepapers/swordsman_mage_whitepaper_v6_3.md:917 | corrected decomposition; "holds exactly when the measurable capacity-deficit condition ... additionally holds" | UNAFFECTED (deficit iff) | None |
| papers/v5/privacy_value_v5_4_formal_specification.md:634 (§16 table) | same equality table row as v6 :778 | **EXACT**, in a superseded artifact | Candidate for the `historical`/`superseded` flag (OBS-GPT56-017) rather than a text edit; first person's call |
| COM hearthold/README.md | "leakage stays additive and the reconstruction ceiling holds, R < 1" (static) | EXACT-leaning + GR-7 class | Already ledgered at L113(b); rides the standing propagation-pass item |
| V5.4-era root skill surfaces | "additive information bounds: proven" without the redundancy qualifier | **EXACT** class (per the disposition ledger's own cross-check instruction at OBS-GPT56-011) | First-person propagation queue; outside pipeline write scope |
| pipeline tracker/docs/*.html | mirrors of the above | UNAFFECTED as sites (generated; regenerate after source fixes; GR-6) | None directly |

### 2.4 Inventory summary

- **EXACT sites: 10** (plus 3 EXACT-leaning ambiguous). Pipeline-side: 2 (E1-C04; grant_edition:133, which inherits it). Canon/canon-adjacent: 8 (spec x3 + v6 paper + dualprivacy + compressed x2 + V5.4 spec) plus hearthold README, whitepaper :747, and the V5.4 skill surfaces in the adjacent ring.
- **BOUND sites: 12+**, all already consistent with the corrected mathematics; none requires a fix.
- **UNAFFECTED: all remaining swept surfaces**, including every deficit-condition "holds exactly when" (a genuine definitional iff that the correction must not disturb).
- **The three awaiting-P4 papers need nothing.** WP-07 and WP-04 already state and prove the correct inequality with the exact equality condition; no theorem in either paper uses exact additivity; WP-27 carries none. The papers' results are untouched under any ruling.
- **Every needed fix is one-sentence class** except pvm_v6_compressed.md:112, which stacks the CTR-OBS-01 defect on an unswept L044 conflation and needs its display rewritten.
- **Order of operations if the ruling accepts:** canon spec first (register process), then A1 re-issues E1-C04 (L044 pattern), then the single WP-03 sentence on a ruled micro-card, then regenerate mirrors; canon-adjacent surfaces (hearthold, skills, whitepaper, compressed, V5.4 flagging) ride the standing first-person propagation pass.

---

## Proposed canonical correction (one sentence, for the ruling)

> Under Precondition 1 the joint leakage satisfies I(X; Y_S, Y_M) = I(X; Y_S) + I(X; Y_M) − I(Y_S; Y_M), hence is at most the sum of the marginal leakages, with equality if and only if the two outputs are also marginally independent (I(Y_S; Y_M) = 0); every downstream ceiling and floor statement uses only the at-most direction, which the redundancy term only tightens.

The replacement rule for the wording class: "holds exactly (when Precondition 1)" becomes "is at most the sum (under Precondition 1), with equality iff additionally I(Y_S; Y_M) = 0". The deficit-condition "holds exactly when C_S + C_M < H(X)" is a different, correct "exactly" and is out of the fix's scope.

## Proposed ledger entry

[Lnnn][OBSERVERS/CTR-OBS-01][verification+inventory][2026-07-10][A3 (cycle-11 card per L121(a); serialised by A0)]
FINDING: CTR-OBS-01 VERIFIED INDEPENDENTLY at the A3 seat: the exact decomposition I(X;Y_S,Y_M) = I(X;Y_S) + I(X;Y_M) − I(Y_S;Y_M) + I(Y_S;Y_M|X) derived from the chain rule and the interaction identity (Cover-Thomas identities throughout; both sides of the identity equal the triple's co-information); under Precondition 1 the joint is SUBADDITIVE with equality iff marginal independence I(Y_S;Y_M)=0; "holds exactly when Precondition 1" is wrong in BOTH directions (P1 does not give equality; equality does not need P1, witness Y_S=Y_M=W ⊥ X); the floor P_e >= 1 − (C_S+C_M)/H(X) SURVIVES as a conservative bound under Preconditions 1+2 (the numerator upper-bounds true joint information; the true floor sits higher by I(Y_S;Y_M)/log(|𝒳|−1)); I(X;Y_M|Y_S) <= C_M can fail in general (xor witness) but holds automatically under P1, so nothing further is needed; the composition threat enters through I(Y_S;Y_M|X), not the redundancy term. BLAST RADIUS: 10 EXACT sites (+3 ambiguous) — pipeline-side only E1-C04 (:50) and its verbatim inheritor grant_edition.md:133; the rest canon/canon-adjacent (spec §14.7:679, §16:778/:786, privacy_value_v6.md:132, dualprivacy:30, pvm_v6_compressed:112/:235 with :112 ALSO carrying an unswept pre-L044 conflation, V5.4 spec :634 superseded-class, whitepaper :747, hearthold README = L113(b), V5.4 skill surfaces); 12+ BOUND sites need nothing; ALL deficit-condition "holds exactly when" instances are the genuine definitional iff and are fenced OUT of the fix. THE THREE AWAITING-P4 PAPERS NEED NOTHING: WP-07 Thm 3.1 and WP-04 Prop 1(a) already state the inequality with the exact equality condition and prove it via the interaction identity; per-theorem audit confirms NO proof in either paper uses exact additivity (Thm 5.1 = chain rule + DPI one-directional; Cor 5.2/5.4 consume the bound; Prop 5.6 tightness is an existence instance); WP-27 carries no additivity content.
EVIDENCE: reviews/CTR-OBS-01_verification_and_inventory.md (full derivation + per-site table with quotes and line anchors); chronicles/2026-07-10_a3-ctr-obs-01.md; the file reads of record at every anchored site.
PROPOSED: (a) the one-sentence canonical correction (review file, final section) goes to Mitchell inside the cycle-11 decisions list with the Section-5 CTR-OBS-01 ruling request; (b) on acceptance the order is canon-spec correction (register process) -> A1 re-issue of E1-C04 (L044 pattern) -> one ruled WP-03 micro-card for :133 -> mirror regeneration; canon-adjacent surfaces ride the standing propagation pass; (c) pvm_v6_compressed.md:112 is flagged to the register process as an L044 propagation gap independent of this ruling; (d) no surface is touched by the runtime before the ruling (protocol rule 5; GR-10).
STATUS: open(awaiting Mitchell's CTR-OBS-01 ruling; cycle-11 decisions list)
