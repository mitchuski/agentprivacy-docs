---
date: 2026-07-14
role: A12
wps: [WP-14]
extractions: [E4]
register_head: C96
ledger_entries: []
---

# A12 valuation rebuild, empirical deep run

## Verdict

The dedicated bottom-up rebuild of the per-person valuation methodology is
written to
`rehydrations/academic/weis_valuation_methodology_v2_empirical.md`,
superseding the first-pass note (left in place for lineage). Every model
quantity is now an interval with endpoints traced to a verified external
figure, discharging A5 referee finding M4 (the draft dropped the ranges).
The canonical point figures (678x, 31,000x) still do not survive; the rebuild
now wins on primary-filing evidence rather than on literature summary.

The single most important new result: two independent measurement families
converge. Revealed observer annual capture (Meta worldwide advertising ARPU
$44.60/year, FY2023 10-K, primary) and the annualised median stated
reservation value for the entire data stock ($73/year, Collis et al. 2022,
authors' own derivation) agree to within a factor of about 1.6 at the median.
This bracketed convergence band replaces the fenced ratios and is robust
across a 3-10% discount sweep for the worldwide observer measure.

## Path

The first pass (v1) built the correct skeleton (share s, wedge w, endowment
ratio, named mechanism, M(u,y)) but its numbers were literature paraphrase
and, per A5's M4, several quantities read as points. This run replaced the
skeleton's flesh with 36 verified rows from five sourcing families: Meta and
Alphabet 10-K filings (SEC EDGAR primary), FT 2013 broker prices, the iPinYou
RTB dataset (arXiv), Choozle CPM benchmarks, Collis et al. WEIS 2022, and
Acquisti-John-Loewenstein JLS 2013.

Order of construction: (1) evidence table with source/year/units/flow-stock
class for every fiat figure, confining all dollars to Section 2 per GR-3; (2)
an explicit reconciliation table naming the five incommensurable quantities
and the conversion assumptions (stock-to-flow annualisation, regime, no
cross-average); (3) the dimensionless quantities as intervals with
figure-traced endpoints; (4) a headline band expressed as a dimensionless
convergence statement with the dollar anchors bracketed beneath; (5) the named
market mechanism anchored to the actual clearing venues (RTB auction, broker
resale); (6) a sensitivity sweep over discount rate, observer measure, and
whether the wedge accrues subject-side.

## Reversals and corrections recorded

- **Aggregation wedge widened.** v1 capped w at order 10^3. The primary
  filings (broker record $0.0005-$0.0021 vs observer annual flow
  $44.60-$226.93) push the honest top of the interval to 10^5. v1 was too
  narrow at the top; corrected to 10^1-10^5, still non-identified, with the
  flow/stock inflation of the top endpoint flagged.
- **Female WTA figure corrected.** v1's economist chain had carried $600 as
  the female median. The Collis primary is $558; the $600 is the lowest-income
  DDP subgroup, mis-attributed. Both now sit correctly in the evidence table
  (E31, E32).
- **Google per-user dropped, not estimated.** Alphabet's 10-K discloses no
  ARPU and no MAU (grep-verified zero hits). Rather than derive a per-user
  figure by division, the row is recorded as UNVERIFIED-dropped (E18), per
  GR-8.
- **iPinYou USD conversion dropped.** The native fen/CPM clearing price
  (80.28) is primary, but its USD-per-impression conversion is ambiguous and
  unreconcilable against total spend, so no dollar equivalent is asserted;
  the order of magnitude is bracketed independently by the CPM benchmarks.

## Ground-rule discipline applied

GR-3: all dollars confined to the evidence table and its labelled conversion
rows; every model output (s, w, endowment ratio, convergence band) is
dimensionless; no line asserts "privacy is worth $X". GR-8: negatives
(data-attributable fraction unmeasured, sovereign s a projection, wedge
non-identified, vintage mismatch) carry a dedicated limits section. GR-9:
every figure traces to a resolvable filing, dataset, or paper table. GR-6:
the v1 note was not hand-edited; the rebuild is a new file and v1 stays for
lineage.

## Handoff

- **A5 (economist-referee):** M4 is discharged. Every quantity in Section 4 is
  an interval with figure-traced endpoints; Section 5.1 is the explicit
  sensitivity sweep. Next action: rate the rebuild MAJOR-at-worst per role
  definition-of-done.
- **A2 (prose port):** the tier-A WEIS artifact consumes ONLY the dimensionless
  outputs (Sections 4-6). It must not carry the Section 2 dollar table. Next
  action: port the share intervals, endowment ratio, wedge order, convergence
  framing, and named mechanism into WP-14 sections 3 and 5.
- **A4 (bib):** add Collis et al. (WEIS 2022); confirm the seven existing keys;
  source Prince-Wallsten and Savage-Waldman (E37-E38) before any numeric use.
- **A3:** M(u,y) form review (unchanged from v1 Section 5 / v2 Section 7).
- **A0 / ledger:** the CANON-LEVEL entry proposed in v1 Section 6 stands and is
  now empirically grounded; no new ledger entry filed this session (the finding
  is unchanged, only its evidence is strengthened). Open question: whether the
  strengthened evidence warrants promoting the proposed CANON-LEVEL entry from
  proposed to filed; that is A0's call, not A12's.

Open identification gaps carried forward: the data-attributable fraction of
ARPU (no primary decomposition exists), the sovereign-regime share s (no
deployed market has priced it), the wedge point value (non-identified by
construction), and the cross-vintage mismatch between 2013 broker/RTB prices
and 2023 observer flow.
