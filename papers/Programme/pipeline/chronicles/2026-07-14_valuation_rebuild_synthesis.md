---
date: 2026-07-14
role: A0/A12 (valuation rebuild synthesis after adversarial verification)
wps: [WP-14]
extractions: [E4-seventh-capital]
register_head: C96
ledger_entries: [L132]
---

# Valuation rebuild synthesis: three hostile lenses applied, convergence headline killed, endpoints restored

## Verdict

The dedicated valuation rebuild (weis_valuation_methodology_v2_empirical.md)
survives adversarial verification WITH FIXES, all of which are now applied in
place. The single largest change is a retirement, not a repair: the v1 headline
that two measurement families "converge to within a factor of about 1.6-2" is
withdrawn. A seller's reservation value (a one-time stock, stated WTA) and a
third party's gross-revenue flow (advertising ARPU) have no theoretical reason
to coincide; their numerical proximity for one region/horizon slice is an
artifact of the annualisation knob, not corroboration. The rebuild now reports
per-category ranges and refuses a single triangulated headline. This is the more
honest outcome and the one the commensurability lens forces.

Three surviving dimensionless outputs replace the headline: the
surplus-appropriation share $s$ moves from order $10^{-4/-5}$ (extraction) to
order $10^{-1}$ (sovereign projection), a three-to-four order share-shift; the
aggregation wedge $w$ is positive, super-additive, order $10^{1}$ to $10^{5}$,
non-identified; the WTA:WTP value wedge is about 1.2-1.4 with a participation-
rate endowment signal of about 5. No fiat value of privacy is asserted anywhere
(GR-3/L057 held).

## Path

Three hostile lenses were run against the rebuild. Their dispositions and the
fixes applied:

**Lens 1, number provenance (SURVIVES-WITH-FIXES).** Every dollar figure in the
Section 2 evidence table was independently checked against its primary table.
A10's blanket suspicion of the stated-preference figures is discharged: E26-E36
(Collis et al. 2022; AJL 2013) match the primary PDFs verbatim, and E1-E17 match
the FY2023 Meta and Alphabet 10-Ks. Three defects survived and are fixed. (i)
E21 ($0.005/attribute) is the one figure that could not be independently
confirmed and that also anchored a model interval endpoint (the wedge lower
bound); it is re-marked UNVERIFIED and dropped from numeric use, and the wedge
lower bound is re-derived from E19->E20 (about 4x, which rounds to order
$10^{1}$, so the model output is unaffected). (ii) E22 (iPinYou 80.28 fen) is
relabelled as the training-partition total winning-price CPM, correcting a
market/paying-price conflation. (iii) E23-E25 (Choozle CPM) are downgraded from
"VERIFIED-secondary" to "indicative (single-vendor benchmark, unconfirmed)".

**Lens 2, commensurability (SURVIVES-WITH-FIXES; four high-severity attacks, all
sustained).** (a) The "factor 1.6/2 convergence" headline is retired; the
sensitivity sweep is now read as the evidence that the overlap is a chosen slice
(the median WTA anchor moves across a 3.3x span by discount choice alone and
straddles the observer number on both sides). (b) The claim that WTA and ARPU
"price the same stock from opposite sides of one market" is withdrawn from
assumption A-REGIME; a reservation value and a gross-revenue flow are declared
non-commensurable, and any triangulation claim is downgraded to "two
independently-sourced brackets happen to overlap in order of magnitude". (c) The
WTA:WTP endowment ratio anchor of 5.37 is corrected: 5.37 is a ratio of
participation proportions (52.1% vs 9.7%), not a ratio of valuations, and
inflated the effect roughly fourfold; the value-based anchor is 1.2-1.4 (E34/E35
monetary constants), and the [2,7] interval is replaced by [~1.2, ~4]. The 5.37
is kept only as direction-only corroboration. (d) The flagship s(extraction)
anchor carried units of yr^-1 (a one-time record price over an annual flow), so
it was not a share at all; it is rebuilt as (subject annual realisation)/(annual
surplus) with the annual resale multiplicity f made explicit, restoring genuine
dimensionlessness. The GR-3 "dimensionless by construction" claim, previously
overstated at exactly the quantity replacing 678x, now holds at the numeric
endpoint.

**Lens 3, dimensionality (folded into 2d above).** The same units defect was the
third lens's core attack; the resale-frequency fix discharges it, and the
appropriation gap is now the arithmetic difference of two dimensionless
intervals rather than a bare prose assertion.

## Deliverables

1. The rebuild note is patched in place (it is a working artifact, not a
   generated file, so in-place editing is correct here; the tier-A WEIS artifact
   remains the generated surface and is NOT hand-edited, per GR-6). Sections
   0, 2, 3, 4.1, 4.2, 4.3, 5, 5.1, and 8 all updated.
2. Headline decision: triangulation does NOT support a single per-person annual
   value. Per-category ranges are the deliverable (Section 5). For the record,
   the observer annual capture is order $10^{1}$ to $10^{2}$ and the median-WTA
   annualised reservation is order $10^{1}$; they overlap only for the worldwide
   region and r in [5%,10%], and the overlap is coincidental.
3. The tier-A Section 5 revision patch (weis_seventh_capital_S5_patch.md) answers
   A5 finding M4: it restores an interval on every endpoint in the draft's 5.1
   and 5.2 so the order-of-magnitude share-shift is a DERIVED difference of two
   stated intervals, fiat-free and dimensionless, with the dollar anchors cited
   as external evidence only.

## Reversals recorded (GR-8)

- v1's "two families converge (factor ~2)" is reversed to "coincidental overlap
  of a chosen slice; per-category ranges instead". A stronger-sounding claim was
  demoted to an honest weaker one; this is the correct direction.
- v1's endowment ratio anchor (5.37, interval [2,7]) is reversed to a value-based
  anchor (~1.2-1.4, interval [~1.2,~4]). The effect the note can claim shrank
  roughly fourfold. Recorded with equal prominence.
- v1's s(extraction) numeric endpoint is reversed: it was dimensionally a rate,
  not a share, and is rebuilt. The GR-3 compliance claim was overstated and is
  now corrected rather than defended.

## Handoff

- **A2/A3 (WP-14 revision loop):** apply weis_seventh_capital_S5_patch.md as the
  5.1/5.2 replacement; it discharges M4 and sequences with M1 (A3's P1
  derivation should cross-reference the sovereign interval [0.3,0.7]). Open: the
  patch keeps GR-3 tighter than the internal note (no dollar figures printed);
  confirm that reading with A4's bib.
- **A4 (bib):** the endowment-ratio correction routes a source obligation, the
  broader endowment-effect literature that would justify the upper reach to ~4;
  and m7's data-cooperative citations (Delacroix & Lawrence 2019 and kin). Steel
  et al. 2013 / OECD 2013 can carry the broker-price anchor as primary external.
- **A0 / register process:** L132 filed as CANON-LEVEL (GR-10 escalation, not
  resolution): the "convergence/triangulation" framing that circulated in the
  rebuild lineage does not survive commensurability review and must not re-enter
  any canon surface as corroboration; the register process, not a rehydration,
  decides the canon surface. A12 does not resolve canon.
- **Blocked:** none. The rebuild landed; the S5 patch is ready for the revision
  loop; the CANON-LEVEL note awaits the register process.
