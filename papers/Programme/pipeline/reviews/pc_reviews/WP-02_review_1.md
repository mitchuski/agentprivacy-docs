---
wp: WP-02
reviewer_role: A5
persona: regulator (supervisory-authority policy reviewer)
artifact_version: draft-v3
date: 2026-07-02
verdict: major
---

# Review 1 · WP-02

Artifact reviewed: `rehydrations/policy/enforceable_by_architecture.md` (release-draft v3). Reviewed as a submitted policy brief before a supervisory-authority policy team. The pipeline apparatus comment at the head of the file was ignored except to assess whether the brief stands once it is stripped (see weakness 10).

## Summary (3 sentences)

The brief argues that structural separation between delegated AI agents yields an information-theoretic reconstruction guarantee that policy-level controls cannot, and asks conformity-assessment and procurement language to distinguish the two and to require named preconditions and validity horizons on any separation or non-reconstructability claim. Its regulatory scheduling is handled carefully, its limits section is unusually honest for the genre, and the time-indexing recommendation is genuinely actionable; but the central technical claim is misstated as drafted (the inequality R_max < 1 does not follow from the two stated preconditions), and the legal bridge from a reconstruction bound to Article 22 GDPR, rather than to Articles 25 and 32 where architectural measures actually live, is asserted rather than argued. A supervisory-authority policy team would engage with the framing but could not act on the recommendations in their present form; major revision required.

## Strengths (exactly 3)

1. **The Omnibus caveat is handled correctly and prominently.** The provisional agreement is dated, its non-adoption at the time of writing is flagged, and the argument is explicitly insulated from which application date prevails. This is exactly the discipline a supervisory reviewer looks for and usually does not find.

2. **The limits section is proportionate and specific.** The brief disclaims a drift rate for R(t), disclaims empirical-law status for its planning rule, and attributes the leakage measurements to the field rather than to itself. Very few submitted briefs in this genre distinguish what they proved from what they cite.

3. **The time-indexing recommendation is the brief's real contribution and is stated in usable form.** Requiring a named adversary class and a validity horizon t* on privacy and non-reconstructability attestations, on the analogy of certificate expiry, is concrete, checkable at the level of documentation, and portable into questionnaire language today. Recommendation 3 could be lifted nearly verbatim into guidance.

## Weaknesses (numbered; severity BLOCKING | MAJOR | MINOR)

1. **BLOCKING · Section 2 misstates the one guarantee the brief exists to state.** The text asserts that "the reconstruction bound R_max = (C_S + C_M)/H(X) < 1 and the error floor P_e >= 1 - R_max hold under the two preconditions stated below, and only under them." Neither precondition (non-collusion; fixed adversary class) constrains the sum C_S + C_M relative to H(X). Whether R_max is below one is a system-specific numerical fact about channel capacities and source entropy, not a consequence of the architecture; two conditionally independent but individually high-capacity channels satisfy both preconditions and still yield R_max >= 1. The brief's own section 3 concedes this by defining t* as the horizon up to which R(t) < 1, which presupposes that R can reach one with the preconditions intact. For a brief whose declared purpose is to state one guarantee "precisely," and whose recommendation 2 would have assessors treat imprecisely conditioned claims as unsubstantiated, this is self-undermining: a vendor's counsel or a notified body's technical expert will produce the counterexample in one paragraph and the brief's credibility does not recover. The correct statement is available and cheap: under the two preconditions the error-floor relation holds; when additionally C_S + C_M < H(X), a measurable condition, R_max < 1 and reconstruction in the stated sense is impossible against the stated adversary class.

2. **MAJOR · The legal hook is mismatched with the technical guarantee, and the provisions that actually mandate architecture are absent.** Article 22 GDPR concerns decisions based solely on automated processing that produce legal or similarly significant effects; the guarantee offered is a confidentiality and reconstruction property of observation channels. The brief never bridges the two: it does not say which Article 22 element (the right not to be subject, human intervention, the right to contest) is made enforceable by a reconstruction bound, and it never engages the "solely" and "significant effects" thresholds whose application to agentic systems is precisely what is contested. Meanwhile Article 25 (data protection by design and by default) and Article 32 (security of processing), the provisions under which a supervisory authority would actually demand architectural measures, are cited nowhere in a brief titled "Enforceable by Architecture." As drafted, the title promises an Article 25 argument and delivers an Article 22 slogan.

3. **MAJOR · The recommendations name no addressee and no instrument.** Conformity assessment for Annex III systems is predominantly internal control against harmonised standards, with third-party assessment confined to narrow categories. The brief does not say whether its four asks are directed at the European standardisation deliverables, at common specifications, at Commission guidance, at EDPB guidelines, or at public-procurement templates, which are not conformity assessment at all. "Assessment and procurement questionnaires should ask" is not implementable language until the brief says whose questionnaire, adopted through which mechanism, binding on whom. A policy team cannot route an unaddressed recommendation.

4. **MAJOR · The quantities the recommendations require declared cannot currently be verified by any assessor.** Recommendations 2 and 3 require deployers to declare C_S, C_M, H(X), an adversary class, and a horizon t*. The brief offers no measurement methodology, no reference to standards work that would supply one, and no account of how an assessor distinguishes a well-founded capacity evaluation from a self-serving one. Absent that, the requirement produces exactly the boilerplate attestation culture the brief criticises in policy separation: the declaration exists, and nothing behind it can be checked.

5. **MAJOR · The policy/architecture dichotomy erases legal enforcement, and the thesis disparages the audience.** Enforcement of Article 22 today lives in neither prompts nor architecture: it lives in supervision, administrative fines, and judicial remedy. The brief's framing that enforcement "lives in" one of two technical strata, and its thesis that architecture makes rights "enforceable rather than nominal," together imply that current supervisory enforcement is nominal. That claim is unsupported anywhere in the text and is rhetorically counterproductive in a document submitted to the people doing the enforcing. The defensible claim, that architecture reduces reliance on continuous behavioural compliance and makes violations detectable or impossible rather than merely punishable, is weaker and would survive.

6. **MINOR · A single vendor exemplar carries the entire "policy separation" class.** Section 1 rests the empirical characterisation of current practice on one named vendor's toolkit and the brief's reading of that vendor's own documentation. The characterisation is contestable by the vendor, and no second instance is offered. Either add a second, independent instance or soften "illustrates the class" to "provides one documented instance."

7. **MINOR · The definition of t* is ill-behaved unless R(t) is monotone.** t* = sup { t : R(t) < 1 } designates the last time the ratio is below one; if R(t) is not monotone the guarantee is said to "remain in force" up to t* even across interior excursions above one. The brief disclaims any drift assumption, yet the definition quietly presumes monotone growth. Define t* as the first crossing (inf { t : R(t) >= 1 }) or state the monotonicity assumption.

8. **MINOR · Precondition 1 is not attestable as written.** "No third channel carries the inter-agent residue" leaves "residue" undefined and gives no operational test covering shared infrastructure, logging, orchestration state, or vendor telemetry. As conformity language this will not survive first contact with an assessor; as a mathematical condition it needs one defining sentence.

9. **MINOR · Key empirical magnitudes are unquantified in the body.** "Substantial leakage" and "a material fraction of violations" carry the argument of section 1; the reader must excavate the cited measurement papers to learn whether the fraction is 5 percent or 50. One clause with the headline figures, attributed to the citations, would do.

10. **MINOR · Release hygiene is incomplete beyond the apparatus comment.** Stripping the marked HTML comment leaves the brief structurally intact: the executive summary, seven sections, recommendations, limits, and references all stand. But the YAML frontmatter, the inline square-bracket claim markers throughout the body, and the "[per E1-cNN]" tags inside the reference list are apparatus outside the marked comment, and after stripping, the document carries no author, no institution, and no statement of interests. A supervisory authority does not process an unattributed brief.

11. **MINOR · "Scored as such" presumes a scoring scheme that conformity assessment does not have.** Recommendation 1 asks that policy separation be "scored as such"; presumption of conformity is binary. Say what should follow from the classification (for example, that policy separation cannot substantiate a non-reconstructability claim) rather than gesturing at a score.

12. **MINOR · Recommendation 4 largely restates an existing obligation without saying so.** A process for regularly testing, assessing and evaluating the effectiveness of security measures is already required of controllers under Article 32(1)(d) GDPR. Presenting attestation-triggered review as a new ask forgoes the cheaper and stronger move: an interpretive reading that existing law already requires horizon re-evaluation on public feasibility attestations.

## Desk-reject grounds (if applicable)

Not applicable. The brief is in genre, at genre length, competently referenced, and addresses a live regulatory window; it warrants review rather than return.

## The single change that most improves acceptance odds

Restate the section 2 guarantee correctly: under the two preconditions the error-floor relation P_e >= 1 - R_max holds; when additionally C_S + C_M < H(X), a measurable and declarable condition, R_max < 1 and reconstruction in the stated sense is impossible against the stated adversary class. Carry the corrected statement through section 3 and recommendation 2. Everything else in this review is negotiable in revision; a misstated central guarantee in a brief about stating guarantees precisely is not.
