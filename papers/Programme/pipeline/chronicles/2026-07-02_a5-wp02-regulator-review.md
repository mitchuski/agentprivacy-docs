---
date: 2026-07-02
role: A5
wps: [WP-02]
extractions: []
register_head: not observed (A5 read scope is the artifact only)
ledger_entries: []
---

# A5 · WP-02 · Regulator review of "Enforceable by Architecture" (draft v3)

## Verdict

Major revision. The review is filed at `reviews/pc_reviews/WP-02_review_1.md` with one BLOCKING weakness, four MAJOR, seven MINOR, and no desk-reject grounds. The BLOCKING item was not appended to the ledger this session (ledger writes suspended by session instruction); it is delivered to A0 as a proposed entry in the handoff block below, placeholder [Lxxx]. Gate P1 should not advance until it is resolved.

## Path

The session held the A5 role under the regulator persona for the WP-02 chain. Read scope was enforced as the role card requires: the artifact `rehydrations/policy/enforceable_by_architecture.md` only, plus pipeline governance and template files needed to produce the outputs. No extraction, no register, no canon document, and no prior chronicle was read. The apparatus comment at the head of the artifact was ignored except to assess whether the brief stands once stripped.

The reading proceeded as a supervisory-authority policy team would take a submitted brief: legal framing first, then the precision of the technical claims, then implementability of the recommendations, then genre and hygiene.

The decisive finding emerged on the second pass through section 2. The brief asserts that R_max = (C_S + C_M)/H(X) < 1 holds under its two preconditions, non-collusion and fixed adversary class. Neither precondition constrains the capacity sum relative to the source entropy, so the inequality is a system-specific numerical condition, not a consequence of the architecture; the artifact's own section 3 presupposes that R(t) can reach one with the preconditions intact. In a brief whose declared purpose is to state one guarantee precisely, and whose recommendation 2 would have assessors treat imprecisely conditioned claims as unsubstantiated, this is self-undermining and was graded BLOCKING. The repair is cheap and is named in the review.

The legal-framing findings were graded MAJOR rather than BLOCKING after deliberation. The guarantee offered is a confidentiality and reconstruction property, yet the brief's hook is Article 22 GDPR, which concerns automated decisions; Articles 25 and 32, where a supervisory authority would actually anchor architectural demands, are never cited. This mismatch weakens the brief substantially but does not falsify it, and it is repairable in revision without touching the technical core, hence MAJOR.

One grading reversal is recorded. The single-vendor exemplar in section 1 was initially graded MAJOR on the ground that one vendor's self-documentation carries the empirical characterisation of an entire deployment class. On re-reading, the surrounding sentence is hedged ("where they enforce it at all") and survey citations accompany the instance, so the finding was downgraded to MINOR with a concrete repair (add a second instance or soften the class claim). Recorded because the initial grading would have changed the weakness profile A0 sees.

Points in the brief's favour were credited without goodwill: the Digital Omnibus caveat is handled correctly and the argument is insulated from which application date prevails; the limits section is proportionate and specific; and the validity-horizon recommendation is the brief's genuinely actionable contribution.

## Handoff

**Open questions.** Whether the WP-02 chain wants the Article 25/32 anchoring (review weakness 2) treated as mandatory for release or as an editorial choice for A8; the review takes no position on which instrument (standardisation deliverables, common specifications, guidance) the recommendations should target, only that one must be named.

**Blocked items.** Gate P1 for WP-02 is blocked on the BLOCKING weakness until A0 rules. Proposed ledger entry, for A0 to file verbatim or amend:

[Lxxx][WP-02][P1][2026-07-02][A5]
FINDING: Section 2 of rehydrations/policy/enforceable_by_architecture.md (draft v3) asserts that R_max = (C_S + C_M)/H(X) < 1 holds under the two stated preconditions. Neither precondition constrains C_S + C_M relative to H(X); the inequality is a system-specific numerical condition, not a consequence of the architecture. Section 3's definition of t* presupposes R(t) can reach one with the preconditions intact, so the artifact is also internally inconsistent on this point.
EVIDENCE: Artifact text, section 2 (the sentence beginning "Then the reconstruction bound") read against Preconditions 1 and 2; section 3 (definition of t*). Full analysis at reviews/pc_reviews/WP-02_review_1.md, weakness 1.
PROPOSED: Restate the guarantee: under the two preconditions the error-floor relation P_e >= 1 - R_max holds; when additionally C_S + C_M < H(X), a measurable and declarable condition, R_max < 1 and reconstruction in the stated sense is impossible against the stated adversary class. Carry the correction through section 3 and recommendation 2.
STATUS: open

**Next action per WP touched.** WP-02: A0 to log the review as P1 evidence, file the proposed entry with a real ledger ID, and route the artifact back to A8 for major revision; the single change most improving acceptance odds is the section 2 restatement above.
