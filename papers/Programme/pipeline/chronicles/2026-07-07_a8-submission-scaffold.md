---
date: 2026-07-07
role: A8
wps: [programme-wide (feeds WP-04, WP-07, and every TIER-A paper WP)]
extractions: []
register_head: C89
ledger_entries: []
---

# A8 (tooling seat) · submission scaffold built and compiled

## Verdict

`templates/submission/` exists and compiles. The preprint scaffold
(`preprint/main.tex`, `preamble.tex`, eight section stubs) produced a
four-page PDF under the pipeline's actual toolchain (MiKTeX xelatex 4.15,
bibtex 0.99d; the sequence xelatex, bibtex, xelatex, xelatex, run from the
`preprint/` directory). The canonical bibliography
`references/pv_v6.bib` carries 21 entries, all 21 verified against the live
web this session, zero UNVERIFIED; all 21 resolved through bibtex into the
compiled PDF (21 `\bibitem` lines in the generated `.bbl`, zero unresolved
citations, zero bibtex warnings on the final run). `venues/README.md` holds
per-venue class and page-limit rows, verified where the live CFP confirmed
them and marked TODO pending A13 otherwise. The top `README.md` states how a
paper work package consumes the scaffold. The compiled `main.pdf` is kept in
`preprint/` as compile evidence; auxiliary files were removed. One
canon-level bibliographic discrepancy was found and is proposed to A0 below,
not resolved here (GR-10).

## Honest compile record

What was run: the full four-pass cycle above, ending in `main.pdf`
(4 pages) with the bibliography fully resolved. What was not run:
`latexmk`, which is absent from this machine (MiKTeX cannot find a perl
engine); the scaffold documentation therefore prescribes the manual
four-pass sequence rather than latexmk. No venue-class compile (acmart,
IEEEtran, llncs) was attempted; the definition of done named the preprint
scaffold only, and the venue classes are recorded as retarget instructions,
not tested templates.

## Path

The session booted per `CLAUDE.md`, `GROUND_RULES.md`, the A8 role card,
and the task card. `build/build_v6_academic_pdfs.py` (repository root, not
`pipeline/build/`) fixed the toolchain assumptions: xelatex via MiKTeX,
`article` class, 11pt, 25mm margins, black link colour, blue URL colour.
The scaffold mirrors these so a paper compiled from it matches the house
PDFs.

The bibliography was harvested from the two permitted canon reads: the
v4.3 research paper's 13-entry reference list and the V6 edition's wiretap
lineage (Wyner; Leung-Yan-Cheong and Hellman; the Fano converse), plus the
leakage literature and the WP-02 legal anchors named on the task card.
Every entry was then verified against the live web this session (arXiv
abstract pages, dblp, publisher catalogues, IEEE Xplore, EUR-Lex, the
venue CFP pages). The A4 chronicle of 2026-07-02 had already verified the
two 2026 arXiv anchors end to end; this session re-confirmed their author
lists and titles independently (AgentLeak: El Yagoubi, Badu-Marfo and
Al Mallah, Polytechnique Montreal, arXiv:2602.11510, noting the v1 title
differs from the current one; Asif and Amiri, arXiv:2603.05520).

One discrepancy against canon emerged: the v4.3 bibliography lists
"Bergstra, J.A. & Burgess, M. (2019). Promise Theory: Principles and
Applications. O'Reilly Media." The public record (publisher catalogues,
the author's own page) shows the book is independently published (first
edition CreateSpace 2014; second edition 2019, ISBN 978-1696578554);
O'Reilly published a different Burgess title. The .bib entry uses the
correct publisher with a source comment; the canon file was not touched.

Venue rows were verified live where the CFPs are published: PoPETs 2026
(acmart, `sigconf,review,anonymous`, 12 pages at submission, 13 camera),
IEEE SaTML 2026 (IEEEtran conference, 12 pages body, LLM-use disclosure
required), CPP 2026 (acmart sigplan, 12 pages), SOUPS (USENIX template,
12 pages, confirmed against recent cycles rather than a 2027 CFP), FC
(LNCS class family confirmed, limits left TODO). Rows for ITP, WEIS,
HotPETs, RWOT, MyData, the journals, and all deadline columns are marked
pending A13, whose deadline-verification task card is issued but had not
produced an updated `programme/deadlines.md` at session time; duplicating
half-verified dates here would have created a second source of truth, so
the venues file defers to A13's file by name.

## Reversals

1. **BibTeX comment semantics.** The first bibtex run failed with a parse
   error: the .bib footer contained a commented-out `(at)article` template
   written with a literal at-sign, and bibtex scans for the at-sign even
   inside `%` comments. The template text now spells the at-sign out. This
   is worth knowing for the UNVERIFIED-entry convention: commented-out
   entries must not contain a literal at-sign, or they break the build they
   are meant to be excluded from. The convention documented in the .bib
   header takes this into account.
2. **Session interruption.** The session hit a runtime limit immediately
   after the final compile verification and before the chronicle was
   written; on resumption the on-disk scaffold was tail-checked complete
   (all 19 files, no truncation) and nothing was rebuilt.

No other reversals; the toolchain, once identified, behaved as the build
script predicted.

## Proposed ledger entries (for A0 adjudication; not appended, per task card)

1. **CANON-LEVEL.** `papers/lineage/dualprivacy_researchpaper_v4_3.md`,
   References item 1, attributes "Promise Theory: Principles and
   Applications" (Bergstra and Burgess, 2019) to O'Reilly Media. Public
   record: independently published, 2nd edition 2019, ISBN 978-1696578554
   (1st edition CreateSpace, 2014). Canon is read-only; correction, if
   accepted, belongs to the register process. The scaffold's .bib already
   carries the verified publisher.
2. **TOOLING.** latexmk is not runnable on the pipeline machine (MiKTeX
   reports no perl engine). Any future task card or script assuming
   latexmk will fail; the working sequence is xelatex, bibtex, xelatex,
   xelatex. Recorded in `templates/submission/README.md`.
3. **TOOLING (minor).** BibTeX parses at-signs inside `%` comments; the
   UNVERIFIED-entry convention for `pv_v6.bib` therefore requires
   commented-out entries to be written without a literal at-sign.

## Handoff

- **Open questions:** whether A0 accepts the Promise Theory publisher
  discrepancy as a ledger entry; whether venue-class test compiles
  (acmart/IEEEtran/llncs) should be a follow-up tooling task before the
  first real retarget.
- **Blocked items:** venue deadline and remaining class/limit rows blocked
  on A13's `programme/deadlines.md` pass (task card issued 2026-07-07).
- **Next action per WP touched:** WP-04 and WP-07 A3 sessions copy
  `templates/submission/preprint/` and write into the section stubs;
  A0 adjudicates the three proposed ledger entries; A13's completed
  deadlines file supersedes the TODO rows in
  `templates/submission/venues/README.md`.
