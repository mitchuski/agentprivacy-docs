---
artefact: submission-plan
wp: WP-04 (moving-ceiling-sok)
venue: FC 2027 (Financial Cryptography and Data Security), SoK track
tier: internal
date: 2026-08-17
status: plan-v1 (submission decision + P4 = First Person)
note: "CFP facts verified 2026-08-17 against ifca.ai/fc27/cfp.html; venue atlas row updated same day. WP-04 is at awaiting-P4 (P0..P3 passed, L093); nothing here overrides that gate."
---

# FC'27 submission plan · WP-04 "SoK: The Shelf Life of Privacy Guarantees"

## Why this venue, this track

FC'27 has a dedicated **SoK category: 20 pages + references and appendices**, LNCS
format. WP-04 is an SoK by construction (A5's review-1 explicitly found "the
systematisation earns SoK"), and its manifest venue target was "HotPETs or FC
workshop". The main-track SoK slot is the stronger target than an FC workshop:
same conference, full proceedings, and the 20-page budget fits (current article-class
render is 19 pp at 11pt/27mm; LNCS sets tighter type, first fit-check below).
The FC topic list includes privacy technologies and regulatory issues; the SoK's
shelf-life framing (guarantees decaying against adversary capability, incl.
harvest-now-decrypt-later) sits naturally in FC's applied-crypto audience.

## Dates (all verified 2026-08-17, AoE)

| Milestone | Date |
|---|---|
| **Paper submission (firm)** | **2026-09-17** |
| Notification | 2026-11-05 |
| Camera-ready | 2026-12-22 |
| Conference (Barbados) | 2027-02-08 to 02-12 |

Fallback if P4 does not clear in time: HotPETs / FC workshop cycle
(workshop CFPs due 2026-09-01 were for workshop *proposals*; individual
workshop paper deadlines follow each workshop's own CFP), or PETs/PoPETs.

## Submission requirements checklist

- [x] **Format**: LNCS `llncs.cls`, PDF only. Draft LNCS render built:
      `pdfs/programme/WP-04_FC27_anon.pdf` via `build/build_fc27_wp04.py`.
      Fit-check 2026-08-17: **22 pp total including references** against the
      20 pp + refs/appendices SoK budget - body is at or within budget; if a
      final LNCS-template compile runs long, move systematisation tables to
      an appendix (permitted).
- [ ] **Anonymization**: strip author names, affiliations, acknowledgments,
      obvious self-references. In-text: the companion-paper references to
      WP-07 must read as third-person citations to an anonymous preprint or
      be genericised ("a companion manuscript"). Non-anonymous preprint
      elsewhere is permitted, so the guide/eprint copy can stay up.
- [ ] **Strip pipeline apparatus**: frontmatter, claim-traceability markers,
      extraction references (the release build already drops frontmatter;
      verify no C-numbers or WP-numbers survive in prose).
- [ ] **Citations**: Springer LNCS style (`splncs04.bst`); port from the
      markdown citation list into `references/pv_v6.bib` entries (A4-verified
      entries only).
- [ ] **P4**: the First Person reads the exact PDF to be submitted and makes
      the submission decision. The runtime does not submit.
- [ ] Submission site: submit.inf.unibe.ch/fc27/

## Required edits before submission (content)

1. Run-04 normative-strand additions (if the First Person adopts them after
   adjudication): at most one motivating citation; the SoK stays technical.
2. GR-8 limits section: verify present and proportionate (it is, per P3).
3. Appendices: LNCS SoK allows appendices beyond 20 pp; the systematisation
   tables can move there if the fit-check exceeds budget.
