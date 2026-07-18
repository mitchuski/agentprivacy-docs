---
date: 2026-07-09
role: A4
wps: [WP-04]
extractions: []
register_head: C96
ledger_entries: []
---

# A4 citation pass on the WP-04 SoK (cycle 5)

**Verdict first.** All 44 reference entries of `rehydrations/academic/moving_ceiling_sok.md` verified against primary published sources; zero unresolvable; zero bib additions needed (the WP-07 station's 60-entry close already covered the SoK's whole list); six metadata corrections applied to the draft; the L062 Harnik-Pinkas-Shulman-Peleg obligation confirmed discharged in section 6.2; the L074 descriptor line executed at section 5.9 ("five production LLMs"); compile cycle exit 0 twice with 60 bibitems and zero warnings; four checks non-vacuous exit 0 on the explicit three-file list. Two substantive citation-role findings reported, not edited: the Mosca-Piani sharpest-shift clause cites the wrong edition, and the draft's two-unresolved-works framing is half stale. Full verification note in P2 evidence form on `tasks/WP-04_A4.md`; ledger entry proposed to A0 in the report (this seat does not append).

## Path

1. Boot reads per the card: ground rules, role card, task card, the draft in full, `reviews/WP-04_prior_art.md`, the pv_v6.bib header policy, L062/L066/L070/L074/L082, the WP-07 A4 verification note (fetch-block precedent), `SOURCES.md` (registry discipline), the scaffold README (compile sequence), and the four check scripts (argv interface confirmed: file list required, L082).

2. Inventory before fetching. Cross-mapping the draft's References section against pv_v6.bib showed every entry already keyed: the card's expectation of missing keys was already met by the WP-07 close (L070(3)). The station's work therefore shifted from addition to re-verification, role-checking, and annotation: all 44 `[bib: to add]` markers in the draft were stale against the actual bib state.

3. Live verification. Crossref resolved 26 DOI records in one scripted pass (including FEDS 2025-093 through its DOI after the federalreserve.gov URL I derived returned 404: a reversal recorded; the DOI registration record carries Mascelli and Rodden). The arXiv API resolved all 10 arXiv-carried items, with one route reversal: the plain-http endpoint returned HTTP 200 with an empty body; https with redirect-follow works. DBLP confirmed CRYPTO 2025 for Chevignard-Fouque-Schrottenloher (the draft still said CRYPTO 2024, the sweep-era error L070 had corrected only in the bib). Direct-UA fetches verified ePrint 2026/1128, ePrint 2026/625 (upgrading the bib's not-re-verified caveat on the Babbush twin; note field added under the header policy), the zfnd.org post (both block heights and the 2026-06-03 date exact), the Gidney 2602 post (dated 01 Jun 2026; opens "A year ago, I found a way to make quantum attacks on elliptic curve cryptosystems ten times cheaper", directly supporting section 5.8's withholding sentence), blocksec.com, cryptoisac.org, ecdsa.fail (Eigen Labs; benchmark-arena scoring), and the GRI pages.

4. The one edition-level role failure. The section 5.2 clause "the sharpest upward shift of the series in its most recent edition (Mosca and Piani 2024)" is supported by the 2025 edition of the Quantum Threat Timeline (GRI page posted 2026-03-09: 26 experts, timeline "accelerated from previous reports"), not by the cited 2024 report (sixth edition, 32 experts), and the 2024 report is no longer the most recent edition. The A10 sweep row already knew both facts; the draft collapsed them onto the 2024 citation. Decision, recorded as the session's main judgement call: NOT fixed at this seat. Retargeting a citation to a different work changes a claim's support, which exceeds the metadata-only edit class, and the 2025 edition is in neither pv_v6.bib nor SOURCES.md (citing around the registry is barred). Proposed to A0 instead, with the bib/registry addition pre-verified this session.

5. Stale unresolved-works framing found in passing: sections 2, 5.1, 8 and the References closing note still describe the MDPI Telecom item as bibliographically unresolved; it resolved at the WP-07 station (Kagai, Branch, But, Allen; `kagai2025harvest`). Reported for A2/A3 with the L062(d) referee-grade sweep as the natural home; four prose passages, out of edit class.

6. Edits applied (metadata class only): Chevignard year in-text and entry; Haines author order; ecdsa.fail operator; FEDS authors + DOI; Jain full author list; seven page-range enrichments; 44 key annotations; the References header sentence updated from "await addition" to the resolved state; and the sanctioned L074 line at section 5.9. No claim, no proof, no prose beyond these.

7. Compile and checks. xelatex/bibtex/xelatex/xelatex exit 0 in a scratchpad copy and again in place (GR-6: the .bib changed, so the generated main.pdf was rebuilt); 60 bibitems, zero bibtex warnings, zero undefined citations. The four checks ran with the explicit file list (draft, task card, this chronicle): exit 0 x4, non-vacuous.

## Reversals

- The federalreserve.gov FEDS page URL constructed from the title returned a 404; verification rerouted through the Crossref DOI record. The draft's institutional-author entry was nonetheless upgradeable from the DOI record alone.
- The arXiv API's http endpoint silently returned an empty body before the https+redirect route succeeded; an argv-less-vacuity-shaped trap in miniature, caught by checking the byte count rather than the exit code.
- A first grep for bibitems in main.bbl returned 0 due to shell escaping, briefly suggesting a broken bibliography; recounted correctly at 60. Recorded because a wrong count nearly entered the evidence line.
- The "warning" match in the in-place .blg turned out to be the bst function-call counter line ("warning$ -- 0"), not a warning; verified before claiming a clean log.

## Handoff

- **WP-04, single next action:** A5-pc review seats on the draft with the A4 verification note on top (card handoff line). Before or at that seat, A0 routes: (a) the Mosca-Piani 2025-edition citation retarget (bib + SOURCES.md + one clause; pre-verified this session); (b) the stale two-unresolved-works framing (A2/A3, folds into the L062(d) referee-grade sweep); (c) the Csiszar-Korner collusion-attribution wording (A3; same class as the WP-07 L079 residual).
- **Open question:** whether the SoK engages Kagai et al. (Telecom 2025) now that it is resolved; it is the strongest of the two named referee risks to N7 and is currently held out of the survey by a staleness, not by a decision.
- **Blocked:** nothing. Ledger entry proposed in the report to A0; this seat appended nothing to the ledger.

## Addendum (same date, seat resumed under the L085(a) sanction)

A0 sanctioned the Mosca-Piani retarget this seat had proposed and pre-verified. Executed exactly to the sanction's scope: `moscapiani2025timeline` added to pv_v6.bib (61 verified, 0 UNVERIFIED; verification comment carries the GRI page evidence); registry row `mosca-piani-2025-timeline` added to SOURCES.md beside `horizon-notes`; the section 5.2 sentence split so the elicitation clause keeps (Mosca and Piani 2024) and the sharpest-shift clause cites (Mosca and Piani 2025); the 2025 entry added to the draft's References with its key; section 6.3's 2024 citation left standing, the 2024 report supporting what it is cited for there. Compile re-run twice, exit 0 x4 both, 61 bibitems, zero warnings, zero undefined citations; four checks re-run on the explicit three-file list, exit 0 x4. Citation-role finding 1 of the verification note is thereby resolved; findings 2 (stale unresolved-works framing) and 3 (Csiszar-Korner attribution) remain routed to A2/A3 as before. Addendum recorded on the task card, section 5. No other file touched; handoff unchanged: A5-pc next.

## Second addendum (same date, seat resumed under the L088 MINOR-4 sanction)

The A5 review's MINOR-4 routed to this seat: three load-bearing particulars in the section 5.8 Zcash sentence sat inside the three-record block citation without a carrying record each. All three verified at the primary records and CONFIRMED; zero claim-level flags for A3. (1) Prior audits incl. earlier-AI-assisted audits: carried by BlockSec and CRYPTO ISAC; pinned to both. (2) Model released the previous day: carried by BlockSec; one record-level tension found and adjudicated, this addendum's reversal-class event: CRYPTO ISAC says "approximately four days after" the release where BlockSec says the day before; the release announcement (anthropic.com, 2026-05-28) against the Zcash Foundation discovery date (Friday, May 29) settles it for BlockSec and for the draft's wording. The adjudication went one record beyond the three cited, to the release announcement itself, because two cited records disagreed and the coupling is load-bearing for the paragraph's Conjecture 1 reading. (3) PoC counterfeiting in local testing: carried by CRYPTO ISAC (consensus-identical local test environment); pinned there. Edit: inline citation insertions only, terminal block citation retained for the chronology; no prose word changed; the A3 statement-level seat working the same file was not touched at any of its anchors. Checks re-run on the explicit three-file list, exit 0 x4. Task card addendum at section 6.
