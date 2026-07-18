# WP-14 · A5 review 2 (proper) · WEIS economist-referee pass on the REVISED draft

**Artifact:** `rehydrations/academic/weis_seventh_capital.md` (tier A, WEIS 2027 target, thrust T3), status `draft-v2`, dated 2026-07-15.
**Reviewer persona:** economist referee, WEIS program committee.
**Reviewed against:** WEIS venue conventions (format-free, interdisciplinary, data-markets economics). No access to project canon, no goodwill toward it; judged on what the paper contains.
**Supersedes:** the L135 process entry (review-2 against an un-integrated, byte-identical-to-firstpass artifact after a crashed integration). This pass judges the actually-revised paper. Review-1 = L131 (`WP-14_A5_economist_2026-07-14.md`).
**Date:** 2026-07-15

---

## Summary (three sentences)

The revision has done the load-bearing work: Proposition P1 is now a self-contained, correctly-signed comparative-statics result derived from one bargaining model, the critical propertization literature is engaged and its three standing objections are answered by architecture rather than merely cited, the valuation carries dimensionless intervals on every endpoint with the share-shift derived rather than asserted, the ordinal is demoted to provenance with a predicate-led title, and the rent finding is reconciled with the capital thesis at the prominence of a positive result. Five of the six majors are discharged in the artifact and the sixth (M3, durability) is handled as honestly as a companion-dependent claim can be, by an explicit submission gate that withdraws the leg to an open problem if WP-07 is not citable. It does not yet clear unconditional accept because the durability leg and, unflagged, the propertization alienability answer both rest on an imported guarantee a referee cannot see, and a short list of concrete minors (including an internal inconsistency in the share-shift arithmetic) remains; but nothing outstanding is MAJOR.

**Overall rating: MINOR REVISION (accept-class), conditional on WP-07 citability at camera-ready.** No desk-reject grounds. This clears the pipeline target and moves off MAJOR: the paper is now framing plus methodology plus a proven mechanism plus a real literature engagement, not framing plus promises.

---

## Three strengths

1. **P1 is now a real result and it carries its own sharpest objection.** The extraction derivation does not lean on the near-zero outside option alone; the paper states outright that a symmetric two-sided bargain with both outside options near zero would split near one half, so the extraction share requires *both* the single-round sole-proposer extensive form *and* exclusion from the clearing venue. That is the precise mechanism claim review-1 asked for, and pre-empting the "you just assumed a weak outside option" rebuttal is exactly what a good PC rewards.

2. **The propertization engagement answers, it does not name-drop.** Objection (i) is met with structural (object-level) inalienability set against Schwartz's legal-construction inalienability; objection (ii) is met with the rent finding, which makes the remedy a redistribution of position rather than an unattainable replication of scale; objection (iii) is met and then honestly bounded ("nothing in the architecture guarantees a non-regressive distribution of the rent it redistributes"). The concession on (iii) is the tell that the section is doing real work.

3. **The rent finding is reported as a strengthening, not hidden as a retraction.** Section 6 leads with the result that runs against the project's own prior essays, argues that a claim surviving deletion of its most convenient premise is stronger, and drops "super-additive" from every surviving surface. Giving a disconfirmation the prominence of a confirmation is rare and is this paper's second-strongest asset after the honesty discipline that was already present in review-1.

---

## Disposition of the review-1 / L135 majors (judged against the REVISED text)

**M1 (contribution — derive P1): DISCHARGED.**
The Results section is no longer a set of IOUs. P1 uses one model (Rubinstein alternating-offers), names Nash only as the frictionless limit rather than a second interchangeable model, and derives both directions as comparative statics: the extraction regime is an ultimatum game with M as sole proposer whose unique SPE share is `s = h_X -> 0` given exclusion from the clearing venue, and the sovereign regime is X-proposes-first alternating-offers whose interior SPE share equals `beta = rho_M/(rho_X+rho_M)` in the frictionless limit, with `[0.3,0.7]` shown as the image of beta over relative patience within a factor of about 2.3. The signs and the limit are correct. This is a self-contained worked result by the standard of a format-free economics venue and it answers the single highest-leverage change of review 1. Residual (minor): the ultimatum SPE offer could be one line more explicit, and the finite 7012 protocol (propose, counter-once, decline) is idealised as an infinite-horizon alternating game to invoke the outside-option principle; a sharp referee will want a footnote acknowledging the bounded-round idealisation.

**M2 (novelty — propertization + its objections): DISCHARGED.**
Section 2 now carries a dedicated subsection citing Laudon 1996, Samuelson 2000, Schwartz 2004, Purtova 2015, Prins 2006, and Delacroix and Lawrence 2019, and takes the three standing objections in turn with a structural answer to each. The alienability answer (structural, object-level inalienability via non-reconstruction) is genuinely novel relative to Schwartz's legal-construction inalienability, and the paper states plainly what it adds. Residuals (minor): the alienability answer is time-bounded, since it holds only for the term R(t) permits and full alienation returns after `t*`, which is a weaker protection than doctrinal inalienability and is only half-acknowledged; and the thin-markets answer assumes the subject-side aggregator can actually form, which is itself the classic collective-action barrier the paper defers to the unmeasured M(u,y) gate.

**M3 (foundation — WP-07 black box / R(t) schedule / term structure): PARTIAL.**
Two components, split verdict. The term-structure over-claim is DISCHARGED: the paper explicitly retracts it ("we deliberately do not claim a full term structure of dated maturities ... we claim no more than a finite, adversary-relative horizon"), which is precisely the fallback review-1 offered, and A3 now gives R(t) = (C_S(t)+C_M(t))/H(X) with the deficit condition and `t* = sup{t : R(t) < 1}` defined, the drift carried as a register conjecture not a theorem. But the load-bearing durability leg remains unevaluable at review by construction: WP-07 is still a black box, and the paper handles this by making citability a stated submission blocker that withdraws the leg to an open problem if the companion is not citable. That is the correct honest move and the best a paper can do with a companion that is not yet public, but a referee still cannot verify durability now, so the leg is not yet standing. See the accept-class blocker below for the under-scoped-gate problem this creates.

**M4 (rigor — valuation intervals): DISCHARGED.**
The S5 patch is folded in. Section 5.1 gives s(extraction) as order `10^-4` to `5x10^-2`, s(sovereign) as `[0.3,0.7]`, and the WTA/WTP ratio as `[~1.2,~4]` (corrected off the participation-proportion ratio to the value wedge), each with a cited external endpoint basis and no fiat printed. The appropriation gap is now DERIVED as a log-difference of two stated intervals rather than asserted as "roughly one order of magnitude," and 5.2 splits the wedge into w_model (order ~10^0, saturating, "super-additive" dropped) and w_gap (order 10^4-10^5, reclassified as rent). This is the one over-generous win. Residual (minor, new): the log-difference arithmetic reads `(-1) - (-4) = 3` for the sovereign-minus-extraction anchor, but the sovereign row is `[0.3,0.7]` whose log lies in `[-0.52,-0.15]`, not `-1` (which is `s=0.1`, below the stated interval); the true anchor difference is about 3.5 to 3.7. The slip is conservative (it understates the gap) but it is an internal inconsistency between the table and the derivation and a referee doing the arithmetic will catch it.

**M5 (framing — the seventh ordinal): DISCHARGED.**
The title now leads with the predicates ("Behavioural Data as Subject-Owned Capital: Five Predicates and the Architecture that Prices Them"); the abstract states the ordinal "is provenance only and the argument rests no weight on it"; and Section 2 carries an explicit "the claim is a predicate claim, not an ordinal one" paragraph disclaiming economic weight on the count and correcting the six-capital enumeration against the IIRC source. Exactly the requested fix. Residual (cosmetic only): the word "seventh" and the filename survive as provenance, but the argument no longer depends on them.

**M6 (rent vs compounding — does the rent finding undercut the capital framing?): DISCHARGED.**
The flat contradiction L135 flagged is resolved. The abstract now scopes compounding to "through reputation as a conjecture"; Section 3 predicate (ii) states compounding "holds in one sense and is rejected in another," relocating it onto the reputational relationship stock (Proposition P5, conjectural) and conceding that raw-record aggregation does not compound; and Section 6 reports the rejection of raw-data compounding at positive prominence. The capital thesis survives because four of the five predicates (returns, investability, opportunity access, cross-context transfer) do not depend on compounding, and a rent-yielding positional asset is capital in the ordinary economic sense (land is the canonical case). Residual (minor): the cleanest reconciliation is left implicit. The honest shape of the surviving claim is *rentier* capital, a positional rent-yielding asset, not productive or compounding capital, and the paper still nominally lists compounding among the predicates "the thesis relies on" while conceding it is conjectural and off the data stock. A referee may press whether "compounds" belongs in the five-predicate list at all, or whether the paper should concede outright that behavioural data is more like land than like reproducible capital.

**Score: 5 of 6 majors discharged in the artifact; M3 partial (over-claim discharged, durability leg honestly gated but unverifiable at review). No major remains fully open.**

---

## Judged afresh: the three hostile probes

**Is P1 now a real self-contained result?** Yes. It fixes the pie and the outside options across interfaces, varies only the extensive form the interface sets, and derives share-to-zero in one and an interior share in the other, with the correct frictionless-limit expression for the interior share and a stated precondition (bounded relative patience) for the `[0.3,0.7]` image. It even isolates *which* feature of the interface does the work, ruling out the weak-outside-option-alone reading. A WEIS economist reads this as a proven mechanism, not a promise. The only thing standing between it and a textbook-clean statement is the bounded-round idealisation of 7012 and the absence of an explicit one-line ultimatum SPE; both are footnote-level.

**Does the propertization engagement ANSWER the objections or merely cite them?** It answers. The alienability answer supplies a structural mechanism (non-reconstruction bounds what disclosure can transfer) that is materially different from the legal-construction inalienability in the literature it cites; the thin-markets answer is load-bearing on the rent finding and coherent with it; the regressivity answer is made and then honestly bounded. This is engagement of the kind that survives a co-referee who knows the Schwartz and Purtova literature. The residual is not that the objections are unanswered but that two of the answers (alienability, and durability in M3) are concentrated on the same unseen guarantee, which the paper does not fully flag.

**Does the rent reframing let the capital thesis survive, or does "capital that does not compound" hollow it out?** It survives, and the reframing is the paper's most honest move rather than a wound. "Capital that does not compound" is not an oxymoron: rent-yielding positional assets are capital, and the paper's own substrate (aggregation saturates, the large gap is rent) points straight at the land/licence analogy. The thesis is not hollowed out because it never needed raw-data compounding; it needed durability, returns, investability, transfer, and opportunity access, four of which are untouched by the rent finding and the fifth (durability) is a separate, architecture-borne claim. What the paper has not quite done is *name* the surviving object as rentier capital and retire "compounding" from the predicate list to a clearly conjectural side-claim. That is a sharpening, not a hole.

---

## Remaining weaknesses

### MAJOR
None outstanding. M1, M2, M4, M5, M6 are discharged; M3's over-claim is discharged and its residual is a gated, unverifiable-at-review dependency, handled below as the accept-class condition rather than as an open major.

### The one item that most stands between MINOR and clean ACCEPT

**The WP-07 submission gate under-scopes its own dependency.** Section 6 gates "the durability leg (Sections 3, 4 P4, 6, 7)" on WP-07 being citable and withdraws it to an open problem otherwise. But the Section 2 alienability answer to propertization (objection (i)) rests on the identical imported guarantee: structural inalienability holds only because the observer "cannot reconstruct the underlying record ... bounded by the guarantee imported from WP-07," for the term R(t) permits. If WP-07 is not citable at submission, the alienability answer collapses on the same fault line as durability, yet it is not named in the gate. Two of the paper's four headline moves (non-depreciation durability; propertization-answered-by-structure) are therefore load-bearing on one unseen artifact. Fix: widen the Section 6 gate to name the Section 2 alienability answer explicitly, so a reader knows both revert together if WP-07 does not land. This is a one-paragraph scoping correction, not a re-derivation, which is why it is MINOR and not MAJOR; but it is the single change that most improves acceptance odds now.

### MINOR
- **m1 (new) — the share-shift arithmetic contradicts its own table.** Section 5.1 computes `(-1) - (-4) = 3` while the sovereign row is `[0.3,0.7]` (log `[-0.52,-0.15]`, not `-1`). Reconcile the anchor with the table; the honest figure is about 3.5 to 3.7 at the anchors, which the prose "widening to about four at the lower extraction endpoint" already half-states.
- **m2 — the alienability protection expires at t*.** Structural inalienability is only as durable as the guarantee; after `t*` full alienation returns. Say so where objection (i) is answered, not only in Section 6, so the propertization answer is not read as unconditional.
- **m3 — the thin-markets answer assumes the aggregator forms.** Pooling bargaining position across many subjects is the collective-action problem the M(u,y) gate defers and does not measure; concede that the remedy's feasibility rests on aggregator formation.
- **m4 — P1's finite-round idealisation is unstated.** 7012 is propose/counter-once/decline; the paper invokes infinite-horizon alternating-offers and the outside-option principle. Add a footnote acknowledging the idealisation.
- **m5 — "compounds" still sits in the predicate list.** Consider retiring it to a conjectural side-claim and naming the surviving object as rent-yielding (rentier) capital; this would make M6 airtight rather than merely reconciled.

**Carried from review-1, now retired by the revision:** original m1 (M(u,y) unused) is largely retired, since M(u,y) now gates `s_realised` and weakens the sovereign result in the correct direction, though tau remains unestimated and the form is still a proposal; original m2 (A1 vs P4 unconnected) is retired, now foregrounded as an explicit synthesis (P4 discharges A1); original m3 (shadow-exchange) is retired, now a stated threshold with equal-prominence reversion; original m4/m5/m6 are addressed in the folded valuation and Section 3 scoping; original m7 (data-cooperative attribution) is retired, Delacroix and Lawrence now cited.

---

## Desk-reject verdict

**No desk reject.** In scope for WEIS T3, positioned inside four relevant literatures, legible to a non-cryptographer, honest about its limits, free of figure-hygiene and unconditioned-ceiling sins, and now carrying at least one self-contained worked result. Its remaining defects are a gated companion dependency and a short list of minors, which are what MINOR revision is for.

## The single change that most improves acceptance odds

**Widen the WP-07 submission gate to cover the Section 2 alienability answer, and add the one-line rentier-capital concession (m5).** The first removes the last place a referee can say a headline contribution silently depends on an unseen artifact; the second makes the capital thesis unimpeachable rather than merely reconciled. With those two edits and the arithmetic fix (new m1), this is an accept.

## What still blocks unconditional acceptance, named plainly

1. **WP-07 is not citable at review.** The durability leg and the propertization alienability answer both depend on it; the paper gates the former and, as written, does not gate the latter. This is a conditional-accept item: verify WP-07 citability at camera-ready or both sections revert to stated open problems.
2. **A handful of minors**, chiefly the share-shift arithmetic inconsistency (new m1) and the unretired "compounding" predicate (m5).

Nothing on this list is MAJOR. The paper has moved from MAJOR REVISION to MINOR REVISION / conditional accept.

---

*A5 economist-referee pass, review 2 (proper), against the revised draft-v2. BLOCKING: 0. MAJOR: 0 outstanding (M1/M2/M4/M5/M6 discharged; M3 partial, over-claim discharged, durability leg gated). MINOR: 5 live plus 1 accept-class condition (WP-07 gate scope). Verdict: MINOR REVISION, accept-class, conditional on WP-07 citability. Supersedes the L135 process entry. Findings mirrored to the critiques ledger at L136.*
