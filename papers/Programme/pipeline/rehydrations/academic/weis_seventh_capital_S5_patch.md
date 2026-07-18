---
patch: weis_seventh_capital S5.1/S5.2 replacement
target: rehydrations/academic/weis_seventh_capital.md (tier-A, WEIS-2027)
answers: A5 review-1 finding M4 (L131) — "roughly one order of magnitude"
  share-shift asserted with NO interval on either endpoint; the draft dropped
  the A12-note ranges and kept the 10x conclusion, a smuggled semi-quantitative
  residue of the retired 678x.
discipline: tier-A. GR-3 (fiat appears nowhere; dollar anchors are cited as
  EXTERNAL evidence by author/year only, never printed as figures, never as an
  asserted value of privacy). GR-4 vocabulary. GR-8 negatives kept. UK spelling,
  no em-dashes. Every endpoint is a dimensionless share, ratio, or order.
source_of_endpoints: companion internal note
  weis_valuation_methodology_v2_empirical.md, Sections 4.1-4.3 (v2, post
  adversarial verification 2026-07-14): the endpoints below are the DIMENSIONLESS
  outputs of that note; the note's dollar evidence table stays internal (A2
  discipline) and is not carried here.
role: A0/A12 synthesis (valuation rebuild handoff to A2/A3 revision loop)
date: 2026-07-14
---

<!-- ============================================================
REPLACEMENT TEXT for the draft's Section 5.1 and Section 5.2. Drop in verbatim,
replacing the current 5.1 (share table with cells "near zero"/"interior"/"small
integer multiple") and 5.2 (wedge table with no order stated). The point of the
patch: the "order-of-magnitude appropriation gap" is now a DERIVED consequence
of two independently stated dimensionless intervals, not a bare prose assertion.
No fiat figure appears; the dollar anchors that justify the intervals live in
the internal methodology note and are cited here only by external source.
============================================================ -->

**5.1 The surplus-appropriation share.** We replace the retired present-day gap
with the bounded, range-valued share $s$ of Section 3. Both regimes are stated
as dimensionless intervals on the same normalised per-period surplus, so the
appropriation gap is the arithmetic difference of two stated intervals, not a
free-standing claim.

| Quantity | Regime interval (dimensionless) | Endpoint basis (external evidence, cited not printed) |
|---|---|---|
| $s$ (extraction) | order $10^{-4}$ to $5\times10^{-2}$ | Lower/anchor: $s$ is (the subject's per-period realisable value) over (the per-period appropriable surplus), both per-period. The only price the subject can realise in a market she accesses is the atomised broker-resale price of one record; taken as an annual realisation and divided by the observer's gross annual advertising flow per user, this is of order $10^{-4}$ (broker resale prices per record, Steel et al. 2013 / OECD 2013; per-user gross advertising flow, Meta 2023 Form 10-K; both external). The anchor moves with the unmeasured annual resale multiplicity of a record and is reported as an order, not a point. Upper $5\times10^{-2}$: an unmeasured generous allowance for uncaptured consumer surplus from the zero-price side of the two-sided market (Section 6), not a measurement. |
| $s$ (sovereign; **projection**) | $[0.3,\,0.7]$ | Nash bargaining split of the same normalised surplus once a credible outside option exists: $0.5$ symmetric, $0.3$ counterparty-favourable, $0.7$ subject-favourable. This is a bargaining projection (Proposition P1), not a measurement; no deployed sovereignty market has been observed to price $s$ (Section 6). |
| WTA/WTP endowment ratio (value-based) | $[\approx1.2,\,\approx4]$ | Ratio of the elicited monetary valuations to accept disclosure versus to pay for protection (Acquisti, John and Loewenstein 2013, external). The lower/anchor $\approx1.2$–$1.4$ is the value wedge in that experiment; the upper reach brackets larger endowment effects in the broader literature. A separate participation-proportion ratio of order $5$ in the same experiment is a ratio of the shares of subjects choosing privacy under the two framings, not a ratio of valuations, and is cited as direction-only corroboration of the endowment effect, never as its magnitude. |

The appropriation gap is now derived rather than asserted. It is the movement of
$s$ from the extraction interval to the sovereign interval:
$$\log_{10} s_{\text{sovereign}} - \log_{10} s_{\text{extraction}} \;\approx\; (-1) - (-4) \;=\; 3,$$
i.e. a share-shift of three orders of magnitude at the anchors, widening to about
four at the lower extraction endpoint ($10^{-5}$) and narrowing at the
free-service allowance. The shift is a consequence of the two stated intervals,
expressed as a change in a dimensionless share and never as a ratio to a
near-zero base. The single figure that circulated in the project's prior essays
is not reconstructed; what survives is the interval-to-interval movement, which
is why the endpoints, not a headline multiple, are the content of this
subsection.

**5.2 The aggregation wedge.** The prior draft carried a single wedge, positive
and super-additive, of order $10^{1}$ to $10^{5}$. That object does not survive:
its top divided an annual flow by a one-time stock (a flow-versus-stock crossing)
and its super-additivity is asserted by no external measurement. We replace it
with the two distinct objects the single wedge conflated, give each an
order-of-magnitude interval derived from stated endpoints, refuse to
point-identify either, and drop the word "super-additive" entirely.

| Quantity | Interval (dimensionless) | Endpoint basis (external evidence, cited not printed) |
|---|---|---|
| $w_{\text{model}}$ = single-record modelling/targeting premium: a targeted-segment record over a general record within the same broker market (like-for-like, stock over stock) | order $\approx 10^{0}$, saturating, **NOT super-additive**, **not point-identified** | The anchor is a cross-sectional price-LEVEL ratio between two record TYPES for one subject's record (Steel et al. 2013 / OECD 2013, external), of order a few. It does not measure the returns to AGGREGATING many subjects' data, and no external figure in the evidence set measures aggregation super-additivity. Returns-to-scale evidence bounds any aggregation term to order $\approx 10^{0}$: forecast error falls only at the diminishing $1/\sqrt{N}+1/\sqrt{T}$ rate, with genuine but diminishing gains in history length and the data-variety dimension robustly flat-to-negative, i.e. super-additivity in variety is rejected (Bajari, Chernozhukov, Hortacsu and Suzuki 2018, external); a $0.1\%$ subsample suffices for a given estimation task, so the marginal analytic value of additional volume at scale is $\approx 0$ (Varian 2014, external); combined-attribute broker profiling is barely above chance (Neumann, Tucker and Whitfield 2019, external). |
| $w_{\text{gap}}$ = observer-to-broker realised-value gap: the observer's lifetime targeting-attributable capture per user over the one-time atomised broker-resale price of a record (like-for-like, stock over stock) | order $10^{4}$ to $10^{5}$, **not point-identified**, and it is RENT, not aggregation value | Both terms are stocks (lifetime accumulated observer capture over the subject's tenure, the annual gross flow scaled by the external targeting-attributable fraction; a one-time record price), so the ratio is dimensionless and the flow-versus-stock boundary the prior draft crossed is removed (Meta 2023 Form 10-K per-user gross flow; the targeting-attributable fraction from the online-advertising literature; Steel et al. 2013 / OECD 2013 broker prices; all external). The gap is large because the record is atomised and the subject is not admitted to the clearing venue, not because data value compounds: it decomposes into an atomisation discount, market-position rent, and lifetime accumulation, none of which is super-additive aggregation value. It moves with region, tenure, and which broker price anchors the denominator, and is reported as an order, not a point. |

The gap is where the counterparty's surplus originates and is exactly the object
a subject-side aggregator (Section 5.3) would need to capture. We assert its sign
and its order-of-magnitude interval; we do NOT assert super-additivity, because no
external figure in the evidence set measures it and the returns-to-scale record
rejects it in the variety dimension. We assert no point value, and the obligation
(Proposition P2, Section 6) is to resist letting the interval harden into one,
because the exact gap fixes a region, a tenure, and a denominator that the
available data do not identify, and because most of its size is rent rather than
data value. This is the honest residue of the retired high-end intuition: the
observer-to-broker gap is large, its lower and upper orders are stated, and it is
correctly attributed to atomisation discount, market-position rent, and lifetime
accumulation rather than to compounding aggregation; it is neither a per-person
monetary amount nor the essay figure.

<!-- ============================================================
NOTES FOR THE A2/A3 REVISION LOOP (strip at release):

1. This patch discharges M4 by construction: 5.1 and 5.2 now carry an interval
   on every endpoint, and the "order-of-magnitude" language in the prose is a
   DERIVED difference of two stated intervals, not a bare residue. The retired
   678x/31,000x do not reappear; the surviving quantities are s-shift (3-4
   orders), the split wedge (w_model order ~10^0, saturating, not super-additive;
   w_gap order 10^4..10^5, non-identified, rent not aggregation), and the
   value-based endowment ratio (~1.2-1.4 with a participation-rate ~5
   corroboration).

2. GR-3 is held tighter than the internal note: NO dollar figure is printed
   here. The dollar anchors (Meta FY2023 10-K per-user gross ad flow; Steel et
   al. 2013 / OECD 2013 broker prices; AJL 2013 monetary constants) are cited by
   external source only. If A4 prefers, the OECD 2013 and Steel et al. 2013
   references can carry the broker-price anchor to keep the bib to primary
   external sources.

3. The endowment-ratio row was CORRECTED against the internal note's adversarial
   pass: the prior "small integer multiple" cell silently rode a participation
   ratio (~5). The value-based ratio is ~1.2-1.4 (AJL monetary constants); the
   ~5 is participation, cited as direction-only. This also answers minor m5
   (WTA/WTP over-read).

4. The extraction endpoint's residual non-identification (annual resale
   multiplicity of a record) is stated in-cell so the share is genuinely
   dimensionless and not a hidden flow/stock quotient. This also gives m6 (value
   of the free service) an explicit home as the upper allowance.

5. Sequence with M1: once A3 derives P1 in full, the sovereign interval [0.3,0.7]
   should be cross-referenced to that derivation's comparative statics so the
   interior share is visibly a projection FROM the bargaining solution, not a
   guessed band.

6. WEDGE ROW SUPERSEDED (Run-3 finalisation, 2026-07-15, ledger L134; sources
   weis_valuation_methodology_v2_empirical.md Sections 0/2.5/4.3-4.4). The old 5.2
   row ("$w$ ... positive, super-additive, order $10^{1}$ to $10^{5}$") is GONE. It
   is replaced by two rows because the single wedge conflated a flow/stock crossing
   with an unmeasured super-additivity claim: (a) $w_{\text{model}}$, the
   single-record modelling/targeting premium, order $\approx 10^{0}$, SATURATING,
   with "super-additive" DROPPED (no external figure measures aggregation
   super-additivity and Bajari et al. 2018 rejects it in the variety dimension);
   (b) $w_{\text{gap}}$, the observer-to-broker realised-value gap, order
   $10^{4}$ to $10^{5}$, rebuilt STOCK/STOCK so the flow/stock boundary is removed,
   and relabelled RENT (atomisation discount + market-position rent + lifetime
   accumulation), not aggregation value. The Acquisti-Taylor-Wagman
   super-additivity citation is dropped from this row. GR-3 held: still no fiat
   figure printed; the targeting-attributable fraction that scales the observer
   flow is cited to the online-advertising literature by source only. If A2 wants a
   single-line 5.2, keep $w_{\text{gap}}$ as the headline order and footnote
   $w_{\text{model}}$ as the only genuinely data-value component.
============================================================ -->
