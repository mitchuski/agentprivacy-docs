# Venue notes · templates/submission/venues

Per-venue formatting facts for the programme's publication atlas (programme
Part E). Class-file and page-limit rows below were verified against the live
venue pages on 2026-07-07 where marked; deadline columns are owned by A13 in
`programme/deadlines.md` and are not duplicated here once that file is
populated. TODO rows await A13's verification pass or the next CFP.

Rule: the preprint scaffold in `../preprint/` is the working format. A venue
retarget swaps the document class and preamble; `sections/` and
`../references/pv_v6.bib` carry over unchanged.

## Peer-reviewed venues

| Venue | Class / template | Page limit | Anonymization | Citation style | Verified |
|---|---|---|---|---|---|
| PoPETs | `\documentclass[sigconf,review,anonymous]{acmart}`; sample at petsymposium.org/files/sample-popets.tex | 12 pp body at submission (13 pp camera-ready); references and appendices unlimited | Anonymized (`review,anonymous` options) | ACM (acmart default, numeric) | 2026-07-07, petsymposium.org/authors-2026.php |
| IEEE SaTML | `\documentclass[conference]{IEEEtran}` | 12 pp body; references and appendices unlimited | Double-blind; note: LLM use must be disclosed and motivated in the submission | IEEE | 2026-07-07, satml.org/call-for-papers |
| FC (main + workshops) | LNCS `llncs.cls`, `splncs04.bst` | FC'27: regular 15 pp + refs/appendices; short 8 pp + refs; **SoK 20 pp + refs/appendices** | Anonymized (regular/short/SoK): no author names, affiliations, acknowledgments, or obvious references; non-anonymous online preprint elsewhere permitted | Springer LNCS | 2026-08-17, ifca.ai/fc27/cfp.html (papers due 2026-09-17 firm; workshops 2026-09-01; notify 2026-11-05; camera-ready 2026-12-22; conf 2027-02-08/12 Barbados; submit.inf.unibe.ch/fc27) |
| SOUPS | USENIX template (LaTeX or Word), soups CFP page | 12 pp excluding acknowledgments, bibliography, appendices | TODO verify current cycle | USENIX | partial 2026-07-07, usenix.org SOUPS CFPs (12 pp confirmed for 2024/2025 cycles) |
| CPP | `\documentclass[sigplan,screen]{acmart}` | 12 pp incl. tables/figures, excl. bibliography and marked appendices | TODO verify (recent CPPs lightweight double-blind) | ACM | partial 2026-07-07, popl26.sigplan.org/home/CPP-2026 |
| ITP | TODO: recent editions use LIPIcs (`lipics-v2021.cls`); verify for the 2027 edition | TODO | TODO | LIPIcs | pending A13 |
| WEIS | No fixed class; "whatever academic formats are usual in their field", PDF only | No stated page limit (WEIS 2026); interdisciplinary accessibility emphasised | **Double-blind** (verified WEIS 2026: no author names/affiliations; third-person self-citation) — corrects the earlier "historically not anonymous" note | author's choice | 2026-08-17, weis2026.econinfosec.org (2026 cycle: submit 02-01, notify 03-06, conf 06-02/03; accepted papers invited to J. Cybersecurity special issue; 2027 site pending) |
| IEEE S&P workshops | `\documentclass[conference]{IEEEtran}` typical; per-workshop CFP governs | often 6 pp short-paper | per workshop | IEEE | pending per-workshop CFP |
| First Monday | Journal, web submission; no LaTeX class (HTML/Word workflow) | n/a (journal-length) | Not anonymous | journal house style | pending A13 |
| Internet Policy Review / J. of Information Policy | Journal workflows, no LaTeX class expected | n/a | TODO | journal house style | pending A13 |

## Non-refereed and community venues

| Venue | Format | Notes | Verified |
|---|---|---|---|
| IACR eprint | Any reasonable format; the preprint scaffold as-is | Rolling; account/endorsement requirements noted in A13's task; establishes priority dates | pending A13 |
| arXiv (cs.CR) | The preprint scaffold as-is; xelatex accepted via arXiv's TeX pipeline | Rolling; endorsement may be required for a first submission in category | pending A13 |
| HotPETs | Short workshop format alongside PETS; CFP typically permits PoPETs-style formatting | Not archival | pending A13 |
| RWOT | Collaborative markdown/paper workflow, no class | Week-long co-authoring event | pending A13 |
| MyData | Talk + community paper; CFP governs | pending A13 | pending A13 |
| Metagov seminar | Talk; no paper class | rolling seminar cadence | pending A13 |

## Retargeting checklist (per submission)

1. Copy `../preprint/` into the work package's submission directory.
2. Replace `\documentclass` and, where the venue class carries its own
   packages (acmart, IEEEtran, llncs), remove the conflicting lines from
   `preamble.tex` (geometry and font-size options come from the venue class;
   the theorem environments and notation macros stay).
3. Set the anonymization toggle to match the venue rule; strip
   acknowledgments and artifact URLs that deanonymize.
4. Switch `\bibliographystyle` to the venue's (ACM-Reference-Format for
   acmart, IEEEtran for IEEEtran, splncs04 for LNCS).
5. Remove `\nocite{*}` (scaffold-only) and confirm every remaining citation
   resolves.
6. Check the page limit against the venue row above and the current CFP;
   the CFP wins over this table.
