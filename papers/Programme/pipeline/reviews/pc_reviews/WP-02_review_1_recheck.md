---
wp: WP-02
reviewer_role: A5
persona: regulator (supervisory-authority policy reviewer; same persona as review 1)
artifact_version: draft-v4
date: 2026-07-02
verdict: blocking-resolved
---

# Review 1 re-check · WP-02

Artifact re-checked: `rehydrations/policy/enforceable_by_architecture.md` (release-draft v4). This is a targeted re-check of review 1's BLOCKING weakness 1 only, not a second review. Scope: (a) does draft v4 resolve the BLOCKING item; (b) did the correction introduce any new BLOCKING defect. The pipeline apparatus comment at the head of the file was again ignored except insofar as it identifies which passages changed.

## The BLOCKING item, restated

Review 1, weakness 1: draft v3 asserted that "the reconstruction bound R_max = (C_S + C_M)/H(X) < 1 and the error floor P_e >= 1 - R_max hold under the two preconditions stated below, and only under them." Neither precondition (non-collusion; fixed adversary class) constrains the sum C_S + C_M relative to H(X); two conditionally independent but individually high-capacity channels satisfy both preconditions with R_max >= 1. The misstatement was internally inconsistent with the brief's own section 3, whose definition t* = sup { t : R(t) < 1 } presupposes that R can reach one with the preconditions intact. The prescribed correction: under the two preconditions the error-floor relation holds; when additionally C_S + C_M < H(X), a measurable condition, R_max < 1; carry the corrected statement through section 3 and recommendation 2.

## The corrected passages, quoted and assessed

**1. Section 2, core statement.** Draft v4 now reads:

> "Under the two preconditions stated below, and only under them, the architecture guarantees two structural facts: the leakage of the two channels is additive rather than compounding, and the error floor P_e >= 1 - R_max holds. When, additionally, C_S + C_M < H(X), a capacity-deficit condition that is measurable and declarable for a given system and adversary class, R_max < 1 and reconstruction of the private state, in the sense of the error floor, is impossible against the stated adversary class. The preconditions do not by themselves place R_max below one; whether the deficit holds is a numerical fact about the system, which is exactly why it must be declared."

Assessment: this is the correct decomposition, in substance the statement review 1 prescribed. What the preconditions buy (additivity; the error-floor relation) is separated from what the numerical deficit buys (the strict bound). The error-floor relation is indeed valid under the preconditions alone; where R_max >= 1 it is vacuous but not false, and the brief no longer claims otherwise. The sentence "The preconditions do not by themselves place R_max below one" states the previously missing negative explicitly, and the concession is turned into the argument for declaration, which is the right rhetorical use of it in a conformity-language brief. Resolved.

**2. Section 2, the capacity-deficit block.** The indented conditions list now carries a third named entry:

> "**Capacity-deficit condition (measurable and declarable).** C_S + C_M < H(X): the combined capacity of the two observation channels, evaluated per Precondition 2, falls short of the entropy of the private state. Two structurally separated channels of sufficient combined capacity satisfy both preconditions with R_max at or above one; the deficit is a separate, system-specific fact, and it is the quantity a deployer measures and declares."

Assessment: the condition is set at the same typographical prominence as the two preconditions and is never separated from the claim. The block states, in the artifact's own voice, the counterexample review 1 said a vendor's counsel would produce; the brief now pre-empts it rather than inviting it. The deficit is correctly tied to Precondition 2 for its evaluation basis, so the three conditions form a coherent set rather than a list. Resolved.

**3. Section 3, time-indexing.** The passage now reads, in relevant part:

> "The time index attaches to the capacity-deficit condition of section 2: H(X) is fixed by the source, while the effective capacities are properties of the adversary class available at time t, so R(t) can pass one, with both preconditions intact, once C_S(t) + C_M(t) reaches H(X). What expires at t* is the deficit condition, not the architecture."

Assessment: this closes the internal inconsistency that made weakness 1 self-undermining. In v3, the t* definition presupposed that R(t) could reach one under intact preconditions while section 2 asserted it could not; in v4, section 3 states exactly that possibility and locates the time index on the deficit condition. "What expires at t* is the deficit condition, not the architecture" is a genuinely clarifying sentence for a supervisory reader, and it makes recommendation 3 (validity horizons) cohere with recommendation 2 (declared deficit) rather than sit beside it. Resolved.

**4. Recommendation 2.** Now reads:

> "**Require named preconditions and a declared capacity deficit on any separation or non-reconstructability claim.** A guarantee claimed without its non-collusion condition, its stated adversary class, and its capacity-deficit condition C_S + C_M < H(X) (section 2) is incomplete as stated and should be treated as unsubstantiated."

Assessment: the recommendation now demands exactly the three conditions section 2 states, no fewer and no more. Under v3, recommendation 2 would have condemned the brief's own section 2 as unsubstantiated; under v4 the brief passes its own test. Resolved.

The correction is also carried into the executive summary ("under stated and auditable preconditions together with one measurable capacity condition") and section 7 ("within them the strict reconstruction bound holds only while the declared capacity deficit holds"). Both carries are consistent with the section 2 statement.

## Internal-consistency statement

Sections 2 and 3 and recommendation 2 are now internally consistent. Section 2 states a three-condition claim (two preconditions plus the capacity deficit); section 3 places the time index on the deficit and thereby explains, rather than contradicts, how R(t) can cross one; recommendation 2 requires declaration of precisely the three conditions section 2 names. The executive summary and the limits section carry the same three-condition structure. No passage of draft v4 asserts or implies that the preconditions alone bound R_max below one.

## New BLOCKING defects introduced by the correction

None found. Specific checks performed: (a) the error-floor claim under preconditions alone is mathematically safe (vacuous, not false, where the deficit fails); (b) "impossible ... in the sense of the error floor" is qualified as review 1's own prescribed wording was, and does not overclaim zero-error impossibility; (c) the deficit block does not smuggle a measurability claim beyond "measurable and declarable," which the brief already carried at v3 and which review 1 addresses at MAJOR severity (weakness 4), not here; (d) the section 3 addition does not assert any drift rate and the "no drift claim" disclaimers survive.

## Items not re-adjudicated

The 4 MAJOR items (weaknesses 2, 3, 4, 5 of review 1: the Article 22 versus Articles 25/32 legal hook; unaddressed recommendations; unverifiable declared quantities; the enforcement-erasing dichotomy) and the 7 MINOR items (weaknesses 6 to 12: single-vendor exemplar; non-monotone t* definition; unattestable Precondition 1; unquantified magnitudes; release hygiene; "scored as such"; recommendation 4's overlap with Article 32(1)(d)) **remain open and are not re-adjudicated here**. This re-check neither confirms nor withdraws any of them; they stand as written in review 1 and fall to the normal revision cycle. One remark of overlap only: the v4 correction slightly sharpens weakness 7, since section 3 now explicitly contemplates R(t) crossing one while t* is still defined as a supremum; the first-crossing definition review 1 proposed remains the cheaper fix. That is a note on an open MINOR, not a new finding.

## Verdict

**blocking-resolved.** Draft v4 states the section 2 guarantee as the correct two-part decomposition, names the capacity-deficit condition at the same prominence as the two preconditions, carries the correction coherently through section 3, recommendation 2, the executive summary and the limits section, and introduces no new BLOCKING defect. The gate decision on the review 1 MAJOR items is A0's, not this re-check's.
