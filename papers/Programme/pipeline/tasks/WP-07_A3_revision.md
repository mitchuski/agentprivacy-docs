---
wp: WP-07 (paper-one-theory, TIER-A, PoPETs)
role: A3
runtime: fable
tier: A
branch: none (convention suspended)
gate_target: BLOCKING + mathematical MAJOR/MINOR items from A5 review 1 resolved (L077)
due: 2026-07-10
---

# Task card · WP-07 revision, mathematical legs · role A3 (Formalist)

**Objective:** Resolve the A5-crypto-pc review-1 findings that loop to A3
(the full memo is on `tasks/WP-07_A5.md`; read it in full before touching the
draft). The reviewer re-derived the core and found ONE false statement; the
fixes below are the reviewer's own what-satisfies lines, which you should
treat as the bar, not the script — if you find a better repair, take it and
record the reversal.

**Your items, in order of load:**
1. **BLOCKING-1 · Proposition 4.2 false as stated.** Add the two missing
   hypotheses ((i) ρ_i = ⊥ for all i, equivalently O_i = f_i(O_{i−1}, S_i, N_i);
   (ii) noises mutually independent and jointly independent of the secrets);
   replace "even without erasure" with the no-carried-state wording. Check the
   proof reads correct under the amended hypotheses (the reviewer says it
   does). Check the section-4 preamble's "full generality" sentence no longer
   contradicts the proposition.
2. **MAJOR-1, statement leg.** The exponential-vs-linear comparison is
   upper-bound-vs-upper-bound with non-commensurable ε semantics. Reframe at
   the statement level: comparison of guarantees under stated budget
   semantics; add the third fence to Remark 5.7 (the conditional budget at
   level ε is the strictly more demanding constraint — Prop 4.3's system has
   marginal budgets zero, conditional budget H(S_2)); surface Prop 4.3 as the
   paper's true unconditional separation. (A2 owns the abstract/§1/§7 wording
   leg afterwards — leave those sections alone.)
3. **MAJOR-2 · ε_i(t) typing.** One paragraph at ER-6 (or Remark 3.4) fixing
   the certified-bound semantics: the ε_i(t) are declared, certified upper
   bounds on fixed Shannon quantities; certification is class-and-time-indexed;
   what grows with t is the certified value, not the information. One clause
   in Corollary 5.4 making expiry a claim about the certification.
4. **MAJOR-3 · ER-1 wording.** Requantify over channels outside Definition
   3.5's declared components ({Z_i} and {ρ_i}); ρ's destruction stays ER-2's.
   Verify Proposition 5.5's hypothesis line reads satisfiable afterwards.
5. **MINORs 1, 2, 3, 7, 8** per the memo (Cor 5.4 one-bit inconsistency;
   estimator alphabet-range clause in Thm 3.2; Def 3.7 "Consequently";
   Conjecture 5.8 → Open Problem 5.8 or fix a candidate site — pick one and
   record why; Def 3.8 informal-closure pointer).
6. **MINOR-4, optional adoption:** the reviewer supplies a ready ER-4
   necessity construction. Adopt it (making the necessity trio honest) or
   leave for A2's weakened wording — your call, recorded.

**Out of scope:** the abstract and §§1-2/6-7 prose (A2's revision card runs
after yours — do not touch except where a statement you fix is quoted there,
in which case flag it in your report for A2); citations; extractions; canon;
manifest; ledger (proposed entry in your report).

**Definition of done:** all items resolved or reversal-recorded; four checks
in `checks/` exit 0; trace map updated where statements changed; chronicle
`chronicles/2026-07-09_a3-wp07-revision-1.md`; report to A0 with per-item
resolution summary + proposed ledger entry (L0nn) + the list of quoted
statements A2 must re-align.
