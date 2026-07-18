---
date: 2026-07-10
role: A4
wps: [WP-27]
extractions: []
register_head: C96
ledger_entries: []
---

# A4 · WP-27 citation station · verification pass

**Verdict.** All 14 references in `rehydrations/academic/conjecture_governance_method.md` (draft-v2) verified at a primary record; zero unresolved citations. Both L102(b)/L104(c) obligations discharged: the numbered-problem-list tradition resolved at the Hilbert 1902 Bulletin of the American Mathematical Society record (doi:10.1090/S0002-9904-1902-00923-3, via Crossref), and the Evans and Cooper edition pins landed (Evans 2003, Addison-Wesley Professional, first edition, ISBN 978-0-321-12521-7; Cooper 1990, Business Horizons 33(3):44-54, doi:10.1016/0007-6813(90)90040-I, with Winning at New Products, Addison-Wesley, 1986, as the book origin). All four checks PASS with the explicit path. Frontmatter status stays draft-v2; the pass is recorded as an A4 addendum in the handoff comment block, per the grant_edition addenda pattern.

## What was verified, and against what

Crossref DOI API for the six walled journal records (DeMillo 1978; Kahneman and Klein 2009; Mellers et al. 2014; Nosek et al. 2018; Scheel et al. 2021; Schuler and Zeller 2013 journal version), matching the sweep's route for PNAS 403 and APA PsycNet walls. arXiv abstracts for Lu et al. 2408.06292 and Zhuge et al. 2410.10934 (author lists and the review-automation quotes checked verbatim). rfc-editor.org for RFC 6962 (June 2013, Experimental, obsoleted by RFC 9162). The COS initiative page for the Registered Reports format, the over-300-journals figure, and Chambers's role. Archived scholarly record for Kelly and Weaver 2004 (no DOI exists; Semantic Scholar record plus hosted PDF). Publisher record (InformIT/Pearson) for Evans. Crossref for the Cooper 1990 article, the Chambers 2013 Cortex editorial (doi:10.1016/j.cortex.2012.12.016, a new pin this session), the Schuler-Zeller conference version (doi:10.1109/ICST.2011.32, DOI added), and Hilbert 1902.

Citation-role check passed on every in-text citation: each supports exactly its sentence. The one comparative import re-checked at record is Schuler-Zeller's sensitivity claim; the abstract's wording ("even more sensitive than mutation testing") covers the draft's. Zhuge is cited more conservatively than its record ("approaching" versus "as reliable as"), which is the safe direction and was left alone.

## Corrections applied (both surfaces)

Draft: Chambers entry pinned to the Cortex editorial; Cooper entry pinned to the 1990 Business Horizons record with the 1986 book origin, and both in-text "(Cooper)" instances year-pinned to "(Cooper 1990)"; Evans entry pinned to first edition with ISBN; Schuler-Zeller conference DOI and journal-version title added; Hilbert 1902 added to the references as the Section 6 anchor; references preamble updated (re-verified at the citation station; pins discharged); Section 6 unswept-neighbours paragraph updated to name the resolved Hilbert record and the discharged pins while keeping the ELN and philosophy-of-science items open.

Prior-art review (`reviews/WP-27_prior_art.md`), reconciled row for row: Chambers row (editorial pin added; committee name corrected to Registered Reports Steering Committee per the current COS page), Schuler-Zeller row (conference DOI), Evans and Cooper family-7 rows (pins), precision note 4 (RESOLVED at record, with the routing note), sweep count (A4 addendum: 14 works at record, both concept anchors converted), limits section (the two pre-P1 instructions marked discharged with the station and date). The L093(b)/L095 lesson is respected: no metadata now differs between the sweep and the paper.

## Reversals and dead ends

- The AMS landing page for Hilbert 1902 returns HTTP 403; resolution went through the Crossref DOI record instead, the same route the sweep used for PNAS and APA. Recorded so the next seat does not re-attempt the landing page.
- I considered leaving the Hilbert record out of the draft's references and carrying it only in the prior-art review, since the body does not argue the comparison. Reversed: Section 6 names the tradition, and a named record without a listed reference would leave the anchor unfindable from the paper; the reference is listed with its role stated. Whether Section 3.1 or Section 5 should argue numbering-as-prior-art is claim-shaped and is routed to A3/A2 via A0, not decided here.
- Cooper's 1986 first edition predates the coined term Stage-Gate; the pin therefore leads with the 1990 article (where the term and system are presented at record) and carries the 1986 book as origin, rather than dating the system to a book that does not use the name.

## Checks

`python checks/check_versions.py rehydrations/academic/conjecture_governance_method.md` PASS; same invocation form for `check_register_refs.py` PASS, `check_tier_vocab.py` PASS, `check_figures_fence.py` PASS. Exact invocations on the record in the task-card verification note.

## Handoff

- **WP-27, next action:** A3/A2 decide whether Section 3.1 or Section 5 argues the numbered-problem-list comparison (the record is anchored and listed; the framing sentence is theirs). After that, the next station per the cycle plan (A5 review; the named ambush of the review's precision note 4 is now closed at record).
- **Open question:** the ELN/timestamped-record family remains BACKGROUND with no primary record adopted; Section 6 still names it open. If a referee presses, a record-level ELN pass is the close.
- **Blocked:** nothing. Proposed ledger entry returned to A0 in the seat report; no ledger write made from this seat.
