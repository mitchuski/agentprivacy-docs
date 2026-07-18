---
artifact: weis-valuation-methodology-v2-empirical
tier: internal
supersedes: weis_valuation_methodology_note.md (draft-v1; left in place for lineage)
venue_target: WEIS-2027 (this note is the evidence substrate; the tier-A WEIS artifact stays fiat-free and consumes only the dimensionless outputs of Sections 3-4)
wp: WP-14
role: A12
date: 2026-07-14
extraction_basis: >
  E4-seventh-capital claims c04 (the rebuild target), c05 (M(u,y)),
  c06, c10, c11. Register rows referenced: C55 (architectural, occupied),
  C42 (active). No confidence percentages carried into asserted claims.
purpose: >
  DEDICATED bottom-up rebuild of the per-person valuation methodology from
  verified external measurements. Discharges A5 referee finding M4 (v1
  dropped the ranges): every model quantity below is an interval with
  endpoints traced to a figure. Dollar amounts appear ONLY in the evidence
  table and its explicit conversion rows (GR-3); every model OUTPUT is a
  share, a ratio, or a dimensionless order-of-magnitude interval. No line
  asserts "privacy is worth $X".
handoff: A5 (economist-referee pass), A2 (prose port of dimensionless outputs), A4 (bib), A3 (M(u,y) form)
---

<!-- ============================================================
A12 EMPIRICAL APPARATUS NOTE (pipeline internal; never released; the
tier-A WEIS artifact cites the DIMENSIONLESS outputs of Sections 3-6, not
this note's dollar table). GR-3 discipline: all fiat figures are CITED
EXTERNAL MEASUREMENTS confined to Section 2 (evidence table) and its
labelled conversion rows in Section 5; every model output (s, w, the
endowment ratio, the per-category ranges) is dimensionless, and the v1
"convergence" framing is retired (Sections 0, 3, 5). No fiat
"value of privacy" is asserted anywhere.
============================================================ -->

# WEIS valuation methodology, v2: an empirically grounded bottom-up rebuild

## 0. Verdict

The canonical point figures (678x, 31,000x) do not survive; the rebuild wins
(role law; GR-3, GR-6). What survives is stronger than the point figures
because it is now anchored in verified primary filings and primary
experimental tables, and every quantity is an interval.

Three findings are load-bearing and new relative to draft-v1:

1. **Two independently-sourced brackets overlap in order of magnitude (this is
   NOT a triangulation).** The revealed annual flow the observing platform
   captures per user (Meta worldwide advertising ARPU, $44.60 in FY2023,
   primary 10-K) and the median user's stated reservation value for the entire
   data stock, annualised over a chosen horizon ($22.50-$75/year across the
   plausible discount/tenure range, from the $750 median WTA of Collis et al.
   2022), both fall in the low-to-mid tens of dollars per year for the
   worldwide region and a 12-year-or-shorter horizon. The earlier "factor of
   about 1.6" headline is RETIRED. The two quantities are a seller's
   reservation value (a one-time stock) and a third party's gross revenue flow;
   no equilibrium theory predicts they coincide, and the subject-side number
   becomes a flow only after an annualisation knob whose setting moves it across
   the full $22.50-$833/year band (E30-E33, perpetuity r=3% through the
   declined-income subgroup). Their order-of-magnitude proximity for one
   region/horizon slice is a bracketing convenience, not corroboration; it is
   reported with the full annualisation-induced band beside it (GR-8), never as
   two families "agreeing".

2. **An endowment effect is present; its magnitude anchor is CORRECTED.** In
   the one experiment in the set that puts WTA and WTP on the same choice
   (Acquisti, John and Loewenstein 2013), the elicited monetary constants are
   $10 anonymised versus $12 identified (E34) and $10 versus $14 (E35): a
   WTA:WTP ratio of VALUATIONS of about 1.2 to 1.4. A separate statistic from
   the same experiment, 52.1% choosing privacy when endowed with it versus 9.7%
   when they must buy it (E36), is a ratio of PARTICIPATION PROPORTIONS (5.37),
   not a ratio of monetary valuations, and v1 mis-imported it as the endowment
   ratio anchor, inflating the reported effect roughly fourfold. The endowment
   RATIO is re-anchored on the monetary wedge (~1.2-1.4) actually elicited; the
   5.37 participation ratio is retained only as separate corroboration that an
   endowment effect exists in direction, never as its magnitude.

3. **The aggregation wedge is re-derived on a data-attributable, stock/stock
   basis, and its super-additive claim collapses under returns-to-scale
   evidence (Run-3 tightening).** Two quantities were conflated in v2's single
   w. (a) The single-record MODELLING/TARGETING premium, taken like-for-like
   within the broker market (general demographic record E19 $0.0005 to targeted
   segment E20 $0.0021, ~4x), is order ~10^0. This is a cross-sectional
   price-LEVEL ratio between two record TYPES for one subject's record; it does
   NOT measure super- or sub-additivity of AGGREGATING many subjects' data, and
   NO figure in the set directly measures aggregation super-additivity. Independent
   returns-to-scale evidence (Bajari et al. 2018, E46-E47: forecast error falls
   only at the diminishing 1/sqrt(N)+1/sqrt(T) rate, with genuine but diminishing
   gains in history-length T and data variety N robustly flat-to-negative, i.e.
   super-additivity in variety is affirmatively REJECTED; Varian E49: a 0.1%
   subsample suffices for the estimation task, so the marginal analytic value of
   additional volume is ~0 at scale; third-party broker profiling accuracy is low,
   E50) shows any aggregation term SATURATES rather than compounds, and points to
   order ~10^0. (b) The observer-to-broker realised-value GAP, now built
   STOCK/STOCK (lifetime data-attributable capture $107-$214 over a one-time
   targeted broker record $0.0021, worldwide central band), is order 10^4 to 10^5
   and no longer crosses the flow/stock boundary L132 flagged; but the same
   returns-to-scale evidence shows this gap is NOT aggregation value, it is
   atomisation discount plus market-position rent plus lifetime accumulation. v2's
   characterisation of w as "super-additive, order 10^1-10^5" is CORRECTED: the
   word "super-additive" is DROPPED entirely (no figure demonstrates it and E47
   rejects it); what survives is a single-record modelling premium of order ~10^0
   that saturates; the large gap is rent, not aggregation, and it must not
   harden into a point (GR-8).

The market mechanism through which the value is realised or lost is named in
Section 4 and is concrete: the real-time-bidding programmatic auction and the
data-broker resale market are where behavioural data actually clears, and the
subject is a counterparty in neither.

### Run-3 tightening note (2026-07-15)

Run-3 does not re-open what survived Run-2's three hostile lenses (L132). It
tightens exactly two objects the hostile verifier left wide.

1. **Observer capture is now DATA-ATTRIBUTABLE, not gross.** v2 carried gross
   ARPU as the proxy for data-attributable surplus and flagged the fraction as
   unmeasured. Run-3 brackets the targeting-premium fraction x from external
   literature (E39-E45): x in [0.04, 0.52], central band [0.2, 0.4], policy-clean
   midpoint ~0.20 (ATT aggregate). The proxy carried downstream is x x ARPU, not
   ARPU. Worldwide, that is $8.92-$17.84/yr central versus $44.60/yr gross
   (Section 4.4). NARROWED: the data proxy drops to 0.2x-0.4x of the v2 figure;
   gross is kept only as an upper bound. NOT narrowed: which single x is correct
   stays open, and the ~13x gap between the independent ~4% (E39) and Google's
   own ~52% (E44) is unresolved (GR-8).

2. **The wedge is split and its super-additive claim collapses.** v2's single
   w (order 10^1-10^5) built its top by dividing the observer's GROSS ANNUAL flow
   by a ONE-TIME broker record price, crossing a flow/stock boundary (L132).
   Run-3 (i) fixes the boundary by building the top STOCK/STOCK (lifetime
   data-attributable capture $107-$214 over a one-time targeted record $0.0021,
   worldwide central) and (ii) applies returns-to-scale evidence (E46-E50:
   Bajari et al.'s 1/sqrt(N)+1/sqrt(T) convergence, genuine-but-diminishing gains
   in T, and flat-to-negative variety effect N; Varian's finding that a 0.1%
   subsample suffices, evidencing ~0 marginal analytic value at scale; low broker
   profiling accuracy) to show any aggregation term saturates and points to order
   ~10^0. NARROWED: the SUPER-ADDITIVE claim collapses entirely, from [10^1,10^5]
   to a single-record modelling premium of order ~10^0 (the word "super-additive"
   is dropped; no figure demonstrates it and E47 rejects it); the top is now
   dimensionally clean; the data-attributable fraction shaves the central top
   from ~4.5x10^5 to ~1x10^5. NOT narrowed (and now correctly labelled): the raw
   observer-to-broker gap remains order 10^4-10^5, non-identified, but is rent and
   atomisation discount and accumulation, NOT aggregation value (Section 4.3).

3. **Untouched:** the s-share intervals (Section 4.1), the WTA:WTP endowment
   ratio (Section 4.2), and the no-triangulation headline (Section 5) are left as
   Run-2 set them. The data-attributable fraction bears on s only through 1/x,
   which does not change its order and is noted in place (Section 4.4).

## 1. Why a bottom-up rebuild, and what the figures are NOT

Every dollar figure in Section 2 is **gross advertising (or ad-resale)
revenue or a stated-preference elicitation**. No primary source in the set
decomposes platform revenue into the portion attributable specifically to
behavioural-data targeting versus reach, creative, and brand. Therefore:

- ARPU is the flow the observer captures per user. GROSS ARPU is an **upper
  bound** for the data-attributable surplus, not the "value of a person's data",
  and is no longer used as the data proxy. Run-3 partially closes the
  data-attributable measurement gap: the observer-capture proxy carried
  downstream is **x x ARPU**, where x is the targeting-premium fraction, x in
  [0.04, 0.52], central band [0.2, 0.4], policy-clean midpoint ~0.20 (Section
  4.4, E39-E45). What remains open is which single x within that band is correct;
  the fraction is bounded, not point-identified (GR-8).
- No Google/Alphabet per-user figure is asserted. Alphabet's 10-K discloses
  neither ARPU nor a user/MAU count (grep-verified zero hits in the primary
  filing); any circulating Google "revenue per user" is an analyst division
  and is marked UNVERIFIED, not carried.
- Meta retired ARPU/MAU reporting after Q1-2024 (switched to ARPP on Daily
  Active People). FY2023 is the last clean full-year ARPU vintage; the figures
  are not comparable to post-2024 ARPP.

The point-figure failure modes from draft-v1 (Section 1 there) still hold and
are not repeated: ill-posed near-zero denominator, aggregation dependence,
and the non-arithmetic reframing of the high-end figure. This note's job is
the positive construction the referee asked for.

## 2. Evidence table (all fiat figures live here, GR-3)

Every row is a CITED EXTERNAL MEASUREMENT with source, year, units, and
flow/stock class. None is a model output; none asserts a value of privacy.

### 2.1 Revealed observer capture (advertising flow per user)

| # | Figure | Units | Year | Flow/stock | Source (resolvable) | Confidence |
|---|---|---|---|---|---|---|
| E1 | 44.60 | USD / Facebook+Messenger MAU / year, worldwide | FY2023 | per-year flow | Meta 2023 Form 10-K, ARPU section (SEC EDGAR CIK 1326801, acc. 000132680124000038) | VERIFIED-primary |
| E2 | 13.12 | USD / MAU / quarter, worldwide | Q4-2023 | per-quarter flow | same 10-K, ARPU table | VERIFIED-primary |
| E3 | 68.44 | USD / MAU / quarter, US & Canada | Q4-2023 | per-quarter flow | same 10-K, ARPU-by-region | VERIFIED-primary |
| E4 | 23.14 | USD / MAU / quarter, Europe (incl. RU, TR) | Q4-2023 | per-quarter flow | same 10-K | VERIFIED-primary |
| E5 | 5.52 | USD / MAU / quarter, Asia-Pacific | Q4-2023 | per-quarter flow | same 10-K (position + 11x consistency check) | VERIFIED-primary |
| E6 | 4.50 | USD / MAU / quarter, Rest of World | Q4-2023 | per-quarter flow | same 10-K | VERIFIED-primary |
| E7 | 226.93 | USD / MAU / year, US & Canada | FY2023 | per-year flow | sum of quarterly regional rows (Meta method); annual regional total not printed in 10-K | VERIFIED-secondary |
| E8 | 75.57 | USD / MAU / year, Europe | FY2023 | per-year flow | as E7 | VERIFIED-secondary |
| E9 | 20.04 | USD / MAU / year, Asia-Pacific | FY2023 | per-year flow | as E7 | VERIFIED-secondary |
| E10 | 15.83 | USD / MAU / year, Rest of World | FY2023 | per-year flow | as E7 | VERIFIED-secondary |
| E11 | 131,948 | USD millions, total advertising revenue | FY2023 | per-year flow | Meta 2023 10-K income statement (~98% of total revenue) | VERIFIED-primary |
| E12 | 134,902 | USD millions, total revenue | FY2023 | per-year flow | Meta 2023 10-K | VERIFIED-primary |
| E13 | 237,855 | USD millions, Google advertising total | FY2023 | per-year flow | Alphabet 2023 10-K (SEC EDGAR CIK 1652044, acc. 000165204424000022, goog-20231231.htm) | VERIFIED-primary |
| E14 | 175,033 | USD millions, Google Search & other | FY2023 | per-year flow | same Alphabet 10-K | VERIFIED-primary |
| E15 | 31,510 | USD millions, YouTube ads | FY2023 | per-year flow | same Alphabet 10-K | VERIFIED-primary |
| E16 | 31,312 | USD millions, Google Network | FY2023 | per-year flow | same Alphabet 10-K | VERIFIED-primary |
| E17 | 307,394 | USD millions, Alphabet total revenue | FY2023 | per-year flow | same Alphabet 10-K (ad ~77% of total) | VERIFIED-primary |
| E18 | (none) | Google per-user / ARPU | — | — | Alphabet 10-K discloses NO ARPU and NO MAU (grep = 0 hits) | UNVERIFIED - dropped |

### 2.2 Data-broker resale and RTB spot prices (per-record / per-impression)

| # | Figure | Units | Year | Flow/stock | Source (resolvable) | Confidence |
|---|---|---|---|---|---|---|
| E19 | 0.0005 | USD / person, general demographic (= $0.50 per 1,000) | 2013 | per-record, one-time | FT "How much is your personal data worth?" (Steel et al.); reprinted fastcompany.com/2682323 | VERIFIED-secondary |
| E20 | ~0.0021 | USD / person, targeted segment (e.g. auto-buyer; = $2.11 per 1,000) | 2013 | per-record, one-time | same FT interactive | VERIFIED-secondary |
| E21 | ~0.005 | USD / data attribute | 2013 | per-record, one-time | FT interactive (paywalled); fastcompany reprint 403'd; NOT independently confirmed against Steel et al. primary | UNVERIFIED - dropped from numeric use |
| E22 | 80.28 | Chinese fen, training-set total winning-price CPM (x1000 = CPM) | 2013 | per-impression clearing (RTB), training partition | Zhang, Yuan, Wang, Shen, arXiv:1407.7073, Table 3 (iPinYou training partition) | VERIFIED-primary (native unit, training-set winning price); USD conversion UNVERIFIED |
| E23 | 1 to 5 | USD CPM, open exchange | c.2023-24 | per-impression price | Choozle CPM benchmark (choozle.com/blog/cpm-cheat-sheet) | indicative (single-vendor benchmark, unconfirmed) |
| E24 | 5 to 15 | USD CPM, private marketplace | c.2023-24 | per-impression price | same | indicative (single-vendor benchmark, unconfirmed) |
| E25 | 10 to 25+ | USD CPM, programmatic guaranteed | c.2023-24 | per-impression price | same | indicative (single-vendor benchmark, unconfirmed) |

Note on E22: native figure only, and specifically the TRAINING-partition total
winning-price CPM (winning/paying price x1000 in fen), not a market-wide
average; the earlier "avg market/paying clearing price" gloss conflated market
price with paying price and omitted the train/test split. No dollar equivalent
is asserted. Order of magnitude cross-checked only indicatively by E23-E25
(single-vendor benchmark, unconfirmed): open-exchange $1-5 CPM = $0.001-$0.005
per impression. This cross-check is order-of-magnitude only and is not a model
input.

### 2.3 Stated-preference valuations (WTA / WTP)

| # | Figure | Units | Year | Flow/stock | Source (resolvable) | Confidence |
|---|---|---|---|---|---|---|
| E26 | 750 | USD, median WTA (entire Facebook data stock), YouGov N=4,149 | 2021 | one-time stock | Collis, Moehring, Sen, Acquisti, WEIS 2022 (weis2022.econinfosec.org ...weis22-collis.pdf, p.9) | VERIFIED-primary |
| E27 | 1,000 | USD, median WTA, DDP sample | 2021 | one-time stock | same, Section 5 | VERIFIED-primary |
| E28 | 73 | USD / year (authors' annualisation of E26 over 12-yr tenure) | 2021 | derived per-year flow | same (authors' own derivation) | VERIFIED-primary (derived) |
| E29 | 6.1 | USD / month (authors' derivation) | 2021 | derived per-month flow | same | VERIFIED-primary (derived) |
| E30 | 1,000 (White) / 500 (Black) | USD, median WTA by race | 2021 | one-time stock | same, heterogeneity section | VERIFIED-primary |
| E31 | 1,000 (Men) / 558 (Women) | USD, median WTA by sex | 2021 | one-time stock | same (CORRECTS v1's $600 female figure) | VERIFIED-primary |
| E32 | 600 | USD, median WTA, lowest-income group (DDP) | 2021 | one-time stock | same (the true source of the mis-attributed $600) | VERIFIED-primary |
| E33 | 10,000 | USD, median WTA, income-declined group | 2021 | one-time stock | same (highest subgroup) | VERIFIED-primary |
| E34 | $10 anon vs $12 identified; $2 wedge | USD, experimental design constants (Exp 2 real cards) | 2013 | per-decision | Acquisti, John, Loewenstein, JLS 42(2):249-274 (heinz.cmu.edu/~acquisti/papers/...JLS-2013.pdf) | VERIFIED-primary |
| E35 | $10 vs $14; $4 wedge (Exp 1 arm) | USD, design constants | 2008/2013 | per-decision | same | VERIFIED-primary |
| E36 | 52.1% (WTA) vs 9.7% (WTP); ratio 5.37 | share of subjects choosing privacy | 2013 | per-choice proportion | same (Exp 2) | VERIFIED-primary |

### 2.4 Named comparators not asserted numerically (GR-8/GR-9)

| # | Comparator | Flow/stock | Status |
|---|---|---|---|
| E37 | Prince & Wallsten, "How much is privacy worth around the world?" | per-month WTA by data type | named comparator; no verified figure in this note's input; A4 to source before any numeric use |
| E38 | Savage & Waldman, "Privacy tradeoffs in smartphone applications" | per-app WTP | named comparator; A4 to source before numeric use |

These two are recorded so the flow-class landscape is complete and the note
does not silently imply the four measured families are the only ones. Their
specific figures are UNVERIFIED here and are not carried.

### 2.5 Data-attributable fraction (targeting premium) and returns to scale (Run-3)

Two evidence families added in Run-3. The first (E39-E45) measures the fraction
of gross advertising value attributable to behavioural data, so observer capture
can be written x x gross rather than gross. The second (E46-E50) bounds the
super-additivity of aggregation. All figures are dimensionless ratios; the one
dollar figure (E43) is a CITED EXTERNAL MEASUREMENT, never an asserted value of
privacy (GR-3). Publisher-side and advertiser-side premia are DIFFERENT
quantities and are never averaged together (GR-8).

| # | Figure | Units | Year | Class | Source (resolvable) | Confidence |
|---|---|---|---|---|---|---|
| E39 | ~4% (reported ~$0.00008/impression) | percent uplift in publisher revenue per cookied vs uncookied impression | 2019 | AGGREGATE (publisher-realized average) | Marotta, Abhishek & Acquisti, "Online Tracking and Publishers' Revenues", WEIS 2019 (millions of RTB transactions, one large US media company) [https://weis2019.econinfosec.org/wp-content/uploads/sites/6/2019/05/WEIS_2019_paper_38.pdf] | VERIFIED-secondary |
| E40 | 52% revenue gap for opt-out impressions; 0.23% opt-out incidence | percent revenue gap (targetable vs opted-out); percent opt-out incidence | 2020 | MARGINAL (selected opt-out minority) | Johnson, Shriver & Du, "Consumer Privacy Choice in Online Advertising", Marketing Science 39(1):33-51 [https://pubsonline.informs.org/doi/10.1287/mksc.2019.1198] | VERIFIED-secondary |
| E41 | 51% marginal price premium (trackable vs untrackable); ~20% aggregate Apple-user ad-revenue decline under ATT | percent price premium; percent aggregate revenue decline | 2023-24 | MARGINAL (51%) + AGGREGATE (~20%) | Kraft, Bleier, Skiera & Koschella, "Granular Control and Privacy Decisions: Evidence from Apple's ATT", SSRN 4598472 [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4598472] | VERIFIED-secondary |
| E42 | -18% (desktop EU 2016, 42M impr / 111 pubs) and -23% (mobile in-app 2023, 218M impr / 10,526 apps) ad-impression price without tracking | percent price decrease | 2023 | AGGREGATE (controlled price regression) | Laub, Miller & Skiera, "The Economic Value of User Tracking for Publishers", arXiv 2303.10906 / SSRN 4251233 [https://arxiv.org/abs/2303.10906] | ATTRIBUTION VERIFIED; MAGNITUDE PENDING (author/venue/direction consistent, but the -18%/-23% split and the impression/publisher/app descriptors are NOT yet independently confirmed against the primary table; A4/A12 to confirm verbatim before this controlled-regression leg is treated as settled, GR-9) |
| E43 | +31% cost per incremental customer without offsite tracking data (median $38.16 -> $49.93); implies ~1-1/1.31 = ~0.24 data-attributable (superseding published version) | percent CPA increase; USD per incremental customer (cited external) | 2025 | AGGREGATE (advertiser-side) | Wernerfelt, Tuchman, Shapiro & Moakler, "Estimating the Value of Offsite TRACKING Data to Advertisers: Evidence from Meta", NBER WP 32765 / SSRN 4915952, Marketing Science 2025 (~107,000 advertisers) [https://www.nber.org/papers/w32765] | VERIFIED-secondary (published version supersedes the 2022 working paper SSRN 4198438, which reported +37%/$43.88->$60.19/~0.27; the newer +31%/~0.24 is used, and the central x-band [0.2,0.4] is unaffected either way) |
| E44 | Top-500 publishers avg -52% / median -64% revenue without third-party cookies | percent publisher revenue decrease | 2019 | MARGINAL, DOWN-WEIGHTED (vendor conflict) | Ravichandran & Korula (Google), "Effect of disabling third-party cookies on publisher revenue" (RCT, Google Ad Manager) [https://services.google.com/fh/files/misc/disabling_third-party_cookies_publisher_revenue.pdf] | VERIFIED-secondary (first-party vendor study; ~13x above E39, reported with equal prominence GR-8) |
| E45 | Contextual eCPM ~36% lower than behavioural | percent CPM difference | 2019-20 | (dropped) | Dentsu Aegis / GumGum industry study [https://gumgum.com/blog/landmark-study-proves-the-effectiveness-of-contextual-over-behavioral-targeting] | UNVERIFIED - dropped (vendor-authored, direct commercial conflict; not load-bearing) |
| E46 | Relative forecast error converges to its floor at rate 1/sqrt(N)+1/sqrt(T); marginal value of each data point decreases to zero as data size grows | dimensionless convergence rate | 2018 | returns-to-scale (SUB-additive in quantity) | Bajari, Chernozhukov, Hortacsu & Suzuki, "The Impact of Big Data on Firm Performance", NBER WP 24334 (Assertion 2 / Implication 1) [https://www.nber.org/papers/w24334] | VERIFIED-primary |
| E47 | History-length T effect on big-error probability ~-0.35 in the no-trend model, flattening to ~-0.06 under time fixed effects (genuine but diminishing forecast gains in T); data-variety N effect "robustly flat", insignificant, negative in >=2 specs | change in probability (dimensionless) | 2018 | returns-to-scale (T delivers real diminishing gains; super-additivity in VARIETY N REJECTED) | Bajari et al., NBER WP 24334 (AR1-AR2 magnitudes as printed; all-groups GR2) | VERIFIED-primary |
| E48 | Naive-Bayes classifier keeps improving with diminishing returns even past ~500M entries (the strongest pro-scale case, still diminishing) | data entries (count) | 2013 | returns-to-scale (diminishing at extreme volume) | de Fortuny, Martens & Provost, "Predictive Modeling with Big Data: Is Bigger Really Better?", Big Data 1(4):215-226 (cited in Bajari et al.) | VERIFIED-secondary |
| E49 | Google reportedly powers decision-support using only 0.1% subsamples | fraction of data used | 2014 | revealed marginal value ~0 at scale | Varian, "Big Data: New Tricks for Econometrics", JEP 28(2):3-28 (cited in Bajari et al.) | VERIFIED-secondary |
| E50 | Two-attribute broker profiling ~24.4% correct (range 12.9-32.3%); gender alone ~random (~50%); single-attribute improvement over random 0-77% | percent correctly identified / percent improvement over random | 2019 | low aggregation accuracy (bounds modelling premium) | Neumann, Tucker & Whitfield, "How Effective Is Third-Party Consumer Profiling?", Marketing Science 38(6):918-926 [doi 10.1287/mksc.2019.1188] | VERIFIED-secondary |

**Reading the fraction (E39-E45).** The evidence splits into two regimes that
must not be conflated. (A) The AVERAGE realized uplift behavioural data adds to a
publisher's actual revenue is small: ~4% (E39). (B) The MARGINAL impression-level
premium (a trackable impression vs an otherwise-identical untracked one) is large
and consistent at ~50-52% (E40, E41, E44), with controlled price regressions and
aggregate ATT revenue loss landing at ~18-27% (E41, E42, E43). The marginal ~50%
cluster OVERSTATES the aggregate data-attributable fraction because it is a
conditional/selection comparison struck in an equilibrium where most other
impressions remain tracked (E40's 0.23% opt-out incidence is itself the selection
warning, and is a negative-side fact: revealed demand to opt out is tiny). The
AGGREGATE family (~0.04 publisher-realized; ~0.18-0.23 controlled regression E42,
magnitude PENDING independent confirmation; ~0.20 ATT revenue loss; ~0.24 implied
advertiser-side, E43 superseding published version) is the correct family for
scaling observer capture. **Defensible central band x in [0.2, 0.4]** (anchored by
E41 ATT ~0.20 and E43 advertiser ~0.24; E42's controlled-regression leg is held as
corroboration pending confirmation, and the band does not depend on it), bounded
below by ~0.04 (E39) and above by ~0.52 (E40/E44 marginal, hostile-verifier
stress), with ~0.20 (E41 ATT aggregate) as the policy-clean midpoint. NEGATIVES
(GR-8): the ~13x divergence between the independent E39 (~4%) and Google's own E44
(~52%) is unresolved and undercuts any single point estimate; the largest marginal
figures come from parties with a commercial stake (Google E44, Meta-affiliated
data E43, GumGum E45); publisher-side and advertiser-side premia are different
quantities; all estimates are context- and era-specific (2016-2024, RTB display vs
in-app vs social).

**Reading returns to scale (E46-E50).** The empirical record says aggregation
value SATURATES rather than compounds. Forecast error falls only at the
diminishing 1/sqrt(N)+1/sqrt(T) rate; history-length T delivers genuine but
diminishing forecast gains, while the VARIETY dimension N is robustly
flat-to-negative, i.e. super-additivity in variety is affirmatively REJECTED
(E46-E47); even the most favourable "bigger is better" evidence shows only
diminishing marginal gains past 500M entries (E48); a firm using only a 0.1%
subsample for a given estimation task reveals ~0 marginal analytic value of
additional volume at scale (Varian, E49; note this is a subsample-suffices claim,
not a data-disposal claim: the firm retains the full corpus and uses it
elsewhere); and broker profiling on combined attributes is barely better than
chance (E50). No figure in the set directly measures aggregation super-additivity,
and E47 rejects it in the variety dimension; there is no empirical term that would
carry an aggregation wedge to order 10^2+. This bounds the single-record modelling
premium (w_super) to order ~10^0 (Section 4.3).

## 3. Reconciling the incommensurable measures (no silent averaging)

The figures above measure **five different quantities**. They are not
interchangeable and are never averaged across categories. Stated explicitly:

| Measure | What it prices | Native unit / class | Cannot be compared to X without... |
|---|---|---|---|
| Observer capture (E1-E10) | gross ad revenue the platform realises per user | per-year flow | ...scaling by the data-attributable fraction x in [0.2,0.4] central (E39-E45, Section 4.4); gross alone overstates the data proxy |
| Broker resale (E19-E21) | spot price to buy one atomised record | per-record, one-time stock | ...an aggregation model to reach modelled value |
| RTB clearing (E22-E25) | price of one ad impression at auction | per-impression | ...impressions/user/year to reach a per-user flow |
| Stated WTA (E26-E33) | compensation demanded to surrender the whole stock | one-time stock | ...an annualisation assumption (tenure or discount rate) |
| Endowment wedge (E34-E36) | anonymised-vs-identified pricing gap / WTA-WTP proportion gap | per-decision / ratio | ...nothing; it is already dimensionless as a ratio |

**Conversion assumptions, stated once and used consistently:**

- **A-STOCK-TO-FLOW.** To compare a one-time WTA (E26) with an annual observer
  flow (E1), annualise the stock. Two defensible routes: (i) authors'
  amortisation over the observed 12-year tenure, giving E28 = $73/year (note
  simple division $750/12 = $62.50; the authors' $73 embeds a present-value
  method, so the two differ by the discount assumption); (ii) perpetuity
  annuitisation at rate r: flow = $750 x r. See Section 5 for the r-sweep.
- **A-REGIME.** The observer flow (E1) is realised gross advertising turnover
  under the *extraction* regime; the WTA (E26) is a *reservation value* (the
  compensation the subject would demand to surrender the stock) in a
  *bargaining* regime. These are NOT two prices of one good from opposite sides
  of one market: one is a seller's outside-option floor, the other a third
  party's gross revenue flow. No equilibrium theory predicts a reservation
  value equals a gross-revenue flow; they would coincide only under competitive
  pass-through with the subject as counterparty, a condition this note
  explicitly says does not hold (Section 6, "the subject is a counterparty in
  neither"). Their numerical proximity is therefore a bracketing convenience,
  NOT corroboration, and the earlier claim that the overlap is "informative
  rather than tautological" is WITHDRAWN. A triangulation claim would have to
  supply the missing pass-through/bargaining model that makes reservation ~=
  gross flow and show it plausible; absent that, this note reports two
  independently-sourced brackets that happen to overlap in order of magnitude,
  nothing more.
- **A-NO-CROSS-AVERAGE.** The five families are never pooled into one mean.
  The headline band (Section 5) is a *bracketing* of two like-classed
  quantities (annual observer flow; annualised subject reservation), not an
  average over all five.

## 4. The dimensionless model quantities, with intervals (discharges M4)

Every quantity below is an interval; each endpoint traces to a figure. This
is the referee-requested content that draft-v1 dropped.

### 4.1 Surplus-appropriation share s

Normalise the appropriable per-subject data surplus over one period to 1. The
subject captures s; the observer captures 1 - s. Dimensionless by
construction (GR-3 satisfied).

| Regime | Interval | Endpoint provenance |
|---|---|---|
| s (extraction) | [~10^-5, 0.05], dimensionless | Lower/anchor: the share must be (subject's annual realisation) / (annual appropriable surplus), BOTH per-year. So the numerator uses the broker resale price times the annual resale multiplicity f (records clearing per year): s ~ f x (broker record price E19-E20, ~$0.0005-$0.0021) / (observer annual flow E1, $44.60/yr). v1 set the numerator to a one-time record price over an annual flow, which carries units of yr^-1 and is NOT a share; that endpoint is CORRECTED here by making the numerator an annual flow via f. With f of order 1 to 10 (unmeasured), s ~ 10^-5 to 10^-4; the anchor moves with f, which is the residual non-identification and is stated, not hidden. Upper 0.05 = an UNMEASURED generous allowance for uncaptured consumer surplus from the free service (the zero-price side of the two-sided market; not data-attributable; stated as a gap, GR-8), NOT a measured figure. |
| s (sovereign, projection) | [0.3, 0.7] | Nash bargaining split with roughly symmetric outside options once a credible outside option exists (IEEE 7012, E4-C10). 0.5 = symmetric Nash; 0.3 = firm-favourable asymmetry; 0.7 = subject-favourable. This is a bargaining-theoretic PROJECTION, not a measurement; no deployed sovereignty market has been observed to price s (GR-8). Soft cross-check only: annualised median subject reservation (E28 $73/yr, or the wider $22.50-$75/yr band) is of the same order as observer capture E1 ($44.60/yr), consistent with a subject able to command a non-trivial share once at the table. Per Section 3 A-REGIME a reservation value and a gross-revenue flow are not commensurable, so this corroborates direction, not magnitude. |

The "appropriation gap" is the movement of s from the extraction interval to
the sovereign interval: a shift from order 10^-4/-5 up to order 10^-1, i.e.
three to four orders of magnitude in the subject's captured share, with BOTH
endpoints now dimensionless shares of the same per-period surplus, expressed as
a share change and never as a ratio to a near-zero base. Because both s values
are shares of one normalised per-period surplus, GR-3 dimensionlessness holds at
the numeric endpoints, not merely "by construction" of the normalisation; the
corrected extraction anchor (annual flow over annual flow, with the resale
multiplicity f explicit) is what makes this true. This is the honest residue of
"678x". The number 678 is not reconstructed.

### 4.2 WTA:WTP endowment ratio

| Quantity | Interval | Anchor | Provenance |
|---|---|---|---|
| WTA:WTP endowment ratio (value-based) | [~1.2, ~4] | ~1.2-1.4 | Primary VALUE anchor: the elicited monetary constants $10 vs $12 (E34) and $10 vs $14 (E35) give a WTA:WTP ratio of valuations of ~1.2-1.4 (AJL 2013). The upper reach to ~4 brackets the larger endowment effects reported across the broader privacy endowment-effect literature (NOT in this verified set; flagged for A4 to source before any tighter claim). The 5.37 figure from E36 is a ratio of PARTICIPATION PROPORTIONS (52.1% vs 9.7% choosing privacy), NOT a ratio of monetary valuations; it is cited below as direction-only corroboration and is explicitly NOT the anchor. |

The corrected value-based ratio (~1.2-1.4, reaching higher in the broader
literature) sits at or above the ~1-2 typical of ordinary private goods, and
the participation-rate gap (5.37, E36) independently signals that far more
subjects will hold privacy than will buy it. Both are demand-side signatures of
the appropriation problem: the subject values holding privacy above the price at
which she would buy it. But the magnitude of the value wedge is modest in this
verified set (~1.2-1.4); the strong effect (5.37) is in participation, not in
elicited dollars, and the two are not interchangeable. v1 conflated them.

### 4.3 Aggregation wedge w (re-derived, Run-3)

v2 reported a single w spanning order 10^1 to 10^5 whose top divided the
observer's GROSS ANNUAL flow by a ONE-TIME broker record price, crossing a
flow/stock boundary (L132). Run-3 separates the two quantities v2 conflated and
fixes the boundary crossing.

| Quantity | Interval | Provenance / basis |
|---|---|---|
| **w_super** = single-record modelling/targeting premium, like-for-like within the broker market (same time basis, stock/stock); a price-LEVEL ratio, NOT an aggregation-returns measurement | **order ~10^0, saturating (NOT super-additive)** | Anchor: intra-market segment-price LEVEL premium, general demographic record E19 ($0.0005) to targeted segment E20 ($0.0021) = ~4x (order 10^0.6). This is a cross-sectional ratio between two record TYPES for one subject's record; it does NOT measure super- or sub-additivity of aggregating many subjects' data, and NO figure in the set directly measures aggregation super-additivity. Bounded by returns-to-scale evidence, NOT extrapolated: forecast error falls only at 1/sqrt(N)+1/sqrt(T), T gains are genuine but diminishing and variety N is flat-to-negative with super-additivity affirmatively rejected (E46-E47), extreme-volume gains are diminishing (E48), a 0.1% subsample suffices for a given estimation task so marginal analytic value is ~0 at scale (E49), combined-attribute broker profiling is barely above chance (E50), and the marginal data-attributable premium is ~0.2-0.5 (E41-E43). No empirical term compounds this beyond order ~10^0. |
| **appropriation/rent gap** = lifetime data-attributable observer capture / one-time atomised broker record (STOCK/STOCK) | **order 10^4 to 10^5, non-identified** | Numerator: lifetime data-attributable capture (a STOCK) = x x ARPU x tenure = [0.2,0.4] x $44.60/yr x 12yr = $107-$214 (worldwide, central band; Section 4.4). Denominator: one-time targeted broker record E20 ($0.0021, like-for-like with a modelled profile), a STOCK. w = $107-$214 / $0.0021 = 5.1x10^4 to 1.0x10^5. Both terms are stocks; the flow/stock boundary L132 flagged is removed. |

**How the flow/stock crossing is fixed.** v2's top was (annual flow) / (one-time
stock), dimensionally (yr^-1) and inflating. Run-3's top is (lifetime accumulated
stock) / (one-time stock): the observer's data-attributable take accumulated over
a subject's tenure, divided by the one-time price the atomised record fetches. Both
are stocks, so the ratio is a clean dimensionless number. Applying the
data-attributable fraction x also lowers the central top from v2's ~4.5x10^5
(gross, US-and-Canada) to ~1x10^5 (data-attributable, worldwide), about
two-thirds of an order.

**Is the upper reach super-additive, or does it saturate? It saturates, and no
figure even measures super-additivity.** The returns-to-scale evidence (E46-E50)
is decisive: the observer-to-broker gap of order 10^4-10^5 is NOT the product of
super-additive aggregation. It decomposes into (i) w_super, the single-record
modelling/targeting premium, order ~10^0 (and even this is a price-LEVEL ratio,
not an aggregation-returns measurement); (ii) the ATOMISATION DISCOUNT and
MARKET-POSITION RENT (the broker resale market prices an atomised record 4-5
orders below its realised lifetime value precisely because neither the subject nor
small buyers are the clearing venue, Section 6); and (iii) lifetime accumulation
(the ~12x tenure factor). Only (i) is a data-value premium; (ii) and (iii) are
rent and accumulation. **v2's "w is super-additive, order 10^1-10^5" is
CORRECTED**: the word "super-additive" is dropped entirely (no figure in the set
demonstrates it and E47 affirmatively rejects it in the variety dimension); the
single-record modelling premium is order ~10^0; the large gap is rent, not
compounding aggregation.

**What survives, stated plainly.** The economically meaningful wedge a subject-side
aggregator could re-capture as VALUE-ADD (w_super) is narrow, order ~10^0, and
bounded by hard returns-to-scale evidence; no figure in the set even measures
aggregation super-additivity, so the label is dropped. The full observer-to-broker
gap (order 10^4-10^5) is real and now dimensionally clean (stock/stock), but it is
the appropriation gap (rent extracted because the subject is not admitted to the
clearing venue), not evidence of super-additive data value. Both remain
non-identified as point values (GR-8): w_super because its anchor is a price-level
ratio and its ceiling is a bound not a measurement, the rent gap because it moves
with region, tenure, and which broker price anchors the denominator (stress:
US-and-Canada, x=0.4, general record $0.0005 pushes it to ~2x10^6; worldwide,
x=0.04, targeted record holds it near 1x10^4). The interval is NARROWER than v2's
in the sense that matters: the super-additive claim has collapsed entirely (from
[10^1,10^5] to a single-record modelling premium of order ~10^0), and the residual
bigness is now correctly attributed to rent.

### 4.4 Data-attributable observer capture (Run-3)

v2 carried GROSS ARPU as the observer-capture proxy and flagged the
data-attributable fraction as an open gap. Run-3 replaces gross with
**x x gross**, where x is the targeting-premium fraction from E39-E45.

| Quantity | Interval | Provenance |
|---|---|---|
| x = data-attributable (behavioural-targeting) fraction of gross ad value | [0.04, 0.52], central band [0.2, 0.4], policy-clean midpoint ~0.20 | Lower ~0.04: publisher-realized average uplift (E39, Marotta et al.). Central band: ATT aggregate revenue loss ~0.20 (E41, Kraft et al.), advertiser-side ~0.24 implied from +31% CPA (E43, Wernerfelt et al., superseding published version; the retired 2022 working paper gave +37%/~0.27), with controlled price regressions ~0.18-0.23 (E42, Laub et al.) as corroboration whose magnitude is PENDING independent confirmation. Upper ~0.52: marginal auction premium / opt-out gap (E40, E44), a selection-conditional MARGINAL figure that overstates the aggregate and is held as a hostile-verifier stress. |
| data-attributable annual observer capture (worldwide) = x x E1 | central $8.92-$17.84/yr; full range $1.78-$23.19/yr | x-band x $44.60/yr (E1). Midpoint ~$8.92/yr at x=0.20. Dollar figures are labelled conversions of the dimensionless x against a cited external ARPU (GR-3); the MODEL output is x itself. |

Relative to the gross figure used in v2, scaling by x shaves the data-attributable
proxy to roughly 0.04x-0.52x of gross (central 0.2x-0.4x): gross is retained only
as an upper bound. This is the proxy carried into the wedge numerator (Section 4.3)
and the mechanism discussion (Section 6). It does NOT change the ORDER of the
extraction share s (Section 4.1): using data-attributable surplus rather than gross
as the denominator of s raises s by 1/x (a factor of ~2.5-5), which leaves s at
order 10^-4/-5; that endpoint is left as in v2, with this factor noted.

## 5. Per-person annual value: per-category ranges, NOT a single headline (conversions in-table)

The user asked for a defensible real-number range. The honest answer is that
triangulation does NOT support a single headline range, and per-category ranges
are given instead. This is the more honest outcome, and it is the one the
adversarial commensurability pass forces (Section 3, A-REGIME). GR-3 requires
the model's asserted OUTPUT to be dimensionless; the only dimensionless outputs
that survive are the share-shift and the wedge-order of Section 4, NOT a
"convergence" number.

**What is NOT asserted (RETIRED):** the v1 claim that two measurement families
"converge to within a factor of about 2" is withdrawn. A seller's reservation
value (a one-time stock) and a third party's gross-revenue flow have no
theoretical reason to coincide (Section 3, A-REGIME); the subject side becomes a
flow only after an annualisation knob whose setting moves the median anchor
across the full $22.50-$833/year band below. Landing near the observer flow is a
property of a chosen region/horizon slice, engineered by that free
discount/tenure choice, not an independent measurement agreeing. The overlap is
reported as a coincidental order-of-magnitude proximity for one slice, with the
full annualisation-induced band beside it (GR-8).

**Asserted (dimensionless) outputs:** (i) the surplus-appropriation share s
moves from order 10^-4/-5 (extraction) to order 10^-1 (sovereign projection), a
three-to-four order share-shift (Section 4.1); (ii) the aggregation wedge splits
(Run-3): the single-record modelling premium w_super is order ~10^0 and SATURATES
(returns-to-scale, E46-E50; "super-additive" is dropped, no figure demonstrates it
and E47 rejects it), while the observer-to-broker realised-value gap is order 10^4
to 10^5, stock/stock, non-identified, and is rent plus atomisation discount plus
accumulation, NOT aggregation value (Section 4.3); (iii)
the data-attributable fraction of observer capture is x in [0.2,0.4] central,
[0.04,0.52] full (Section 4.4); (iv) the WTA:WTP value wedge is ~1.2-1.4 with a
participation-rate endowment signal of ~5 (Section 4.2). No single per-person
dollar-per-year figure is asserted as "the value of privacy".

**Per-category ranges (cited external measurements + labelled conversions; NOT
triangulated, NEVER pooled into one mean):**

| Category | Low | Anchor | High | Conversion assumption (in-table) |
|---|---|---|---|---|
| Observer GROSS annual capture (upper bound only) | $15.83/yr (E10, Rest of World) | $44.60/yr (E1, worldwide) | $226.93/yr (E7, US & Canada) | none beyond regional selection; gross ad flow, retired as the data proxy, kept as an upper bound |
| Observer DATA-ATTRIBUTABLE annual capture (Run-3) | $1.78/yr (x=0.04, worldwide) | $8.92/yr (x=0.20, worldwide) | $23.19/yr (x=0.52, worldwide) | x x E1; x in [0.04,0.52] targeting-premium fraction (E39-E45); central band $8.92-$17.84/yr (x in [0.2,0.4]) |
| Annualised subject reservation (median WTA) | $22.50/yr (E26 $750 x r=3%) | $62.50-$73/yr (E26 $750; simple /12yr = $62.50; authors' PV = E28 $73) | $75/yr (E26 $750 x r=10%) | one-time WTA annualised; the horizon/discount knob ALONE spans this row (perpetuity r=3% to r=10%), so the anchor is a chosen slice, not a datum |
| Annualised subject reservation (full subgroup band) | $42/yr (E30 Black $500 / 12yr) | - | $833/yr (E33 declined-income $10,000 / 12yr) | one-time subgroup WTA / 12-yr tenure; reported with equal prominence (GR-8) so the reader sees the band straddles the observer flow on both sides |
| Broker resale (one-time record) | $0.0005 (E19) | - | $0.0021 (E20) | one-time per-record price; E21 dropped (UNVERIFIED) |
| Endowment wedge (value-based) | ~1.2 (E34) | - | ~1.4 (E35) | ratio of elicited monetary valuations; the 5.37 of E36 is a participation ratio, cited separately, not here |

**No single headline range (dimensionless):** per-category, both the observer
annual capture and the median-WTA annualised reservation happen to fall in order
10^1 to 10^2 USD/year for the worldwide region and a 12-year-or-shorter horizon,
but this overlap is coincidental (Section 3, A-REGIME) and slice-dependent: it
holds for r in [5%, 10%] and worldwide, and fails for r<=3% (WTA falls below the
observer flow), for the US & Canada region (observer flow rises to $227/yr), and
for the declined-income subgroup (WTA rises to $833/yr). Neither category is
"the value of privacy", and the model does NOT assert they agree. The surviving
dimensionless outputs are the s-shift and the w-order of Section 4, not a
headline dollar-per-year number.

### 5.1 Sensitivity of the band

The band moves under three assumptions. Each row shows the median anchor
shifting; endpoints scale similarly.

| Assumption swept | Setting | Annualised subject reservation (from E26 $750) | Observer capture used |
|---|---|---|---|
| Discount rate r (A-STOCK-TO-FLOW route ii, perpetuity $750 x r) | r = 3% | $22.50/yr | — |
| | r = 5% | $37.50/yr | — |
| | r = 10% | $75.00/yr | — |
| | authors' PV method (E28) | $73/yr | — |
| | simple /12yr | $62.50/yr | — |
| Which observer measure | worldwide (E1) | — | $44.60/yr |
| | Europe (E8) | — | $75.57/yr |
| | US & Canada (E7) | — | $226.93/yr |
| Does wedge w accrue subject-side? | no (extraction, s~10^-4) | subject realises ~broker price, ~$0.001/yr-equiv | observer keeps ~$44.60/yr |
| | yes (sovereign, s in [0.3,0.7]) | subject realises 0.3-0.7 of surplus; at s=0.5 and observer-flow normalisation, order $22-$113/yr | observer keeps remainder |

Reading the sensitivity: the sweep is the EVIDENCE that the overlap is a chosen
slice, not a discovered fact. The annualised median subject reservation moves
from $22.50/yr (r=3%) through $62.50-$75/yr (simple /12yr and r=10%) while the
observer measure moves from $44.60/yr (worldwide) to $226.93/yr (US & Canada): a
stock can be annualised to match almost any target flow by choosing the horizon,
so the fact that one slice (worldwide observer, r in [5%,10%]) overlaps is a
property of that slice, engineered by the free discount/tenure choice. At r<=3%
the subject reservation falls below the worldwide observer flow; at the US &
Canada region the observer flow sits above the entire median-WTA band. The
single largest mover is **which observer measure** (a factor of ~14 from Rest of
World to US & Canada), and the second is the **discount/horizon knob** (a factor
of ~3.3 from r=3% to r=10%); between them they straddle the observer number on
both sides, which is exactly why no single headline point is asserted. Whether
the wedge accrues subject-side (extraction vs sovereign regime) moves the
subject's realised share by the three-to-four order share-shift of Section 4.1.

## 6. The market mechanism (named, load-bearing)

The role's failure mode is a monetary claim with no market mechanism. The
mechanism is concrete and has a pricing venue that actually exists:

**Where behavioural data clears today.** The real-time-bidding programmatic
advertising auction (E22-E25) and the data-broker resale market (E19-E21) are
the two spot markets in which behavioural data is priced. The subject is a
counterparty in **neither**. The observer aggregates, models, and sells
access, and captures the annual flow (E1-E10); the subject's only realisable
market price is the broker resale price, 4-5 orders of magnitude below the
flow. This is why s is near zero in the extraction regime (Section 4.1): not
because the subject values privacy at zero (she does not, E26), but because
she is not admitted to the market where her data clears.

**How the share s moves.** The consent interface is the bargaining protocol
that sets s. Notice-and-consent is a take-it-or-leave-it offer whose outside
option is service exclusion, which drives the subject's equilibrium share to
zero (a mechanism result, not a moral one). IEEE Std 7012-2025
propose-and-respond (subject proposes terms; organisation accepts, negotiates
once, or declines; bilateral signed record) inverts the offer direction and
supplies a credible outside option, moving s into the bargaining interval
(E4-C10).

**Where the wedge w is captured.** A subject-side aggregator / data coalition
(the data-as-labour market instrument, Arrieta-Ibarra et al. 2018; Posner and
Weyl 2018) aggregates individual behavioural streams on the subject side and
sells access, moving the wedge w (Section 4.3), or a negotiated fraction of
it, back to subjects instead of the observer.

**Why the market does not unravel.** Personal-data markets fail on adverse
selection toward a lemons equilibrium (Akerlof 1970; Spiekermann et al. 2015).
A non-transferable, non-purchasable, Sybil-resistant quality stake (E4-C06,
register C42, carried with its proof obligation) is the quality signal that
lets the market of the two paragraphs above price quality without unravelling.
This is a design claim and an open conjecture, not a measured result.

**What is lost, stated plainly.** In the extraction regime the subject's share
s is near zero and the wedge w accrues entirely to the observer. The
sovereignty the thesis describes has a market price, that price is currently
paid to someone else, and the venue where it is paid is the RTB auction and
the broker resale market named above.

## 7. M(u,y) market-maturity gate (unchanged from v1; A3 owns entry)

The proposed operationalisation carries forward from draft-v1 Section 5
unchanged: M : [0,1] x R_+ -> [0,1], M(u,y) = u(1 - e^{-y/tau}), with u =
fraction of counterparties able to price sovereignty and y = market depth.
As a product factor, realised value = M(u,y) x potential value, so u = 0
(no counterparty can price sovereignty) yields zero capture, which is exactly
the extraction-regime observation (Section 6): the subject is not admitted to
the pricing venue, so M ~ 0 today. A3 owns whether this form enters WP-14.

## 8. Limits (GR-8)

- **Data-attributable fraction is bounded, not point-identified (Run-3).** The
  fraction x attributable specifically to behavioural targeting is now bracketed
  by external literature at x in [0.04, 0.52], central band [0.2, 0.4], policy
  midpoint ~0.20 (E39-E45). What remains open is which single x is correct: the
  ~13x divergence between the independent publisher-realized ~4% (E39) and
  Google's own ~52% (E44) is unresolved, and publisher-side vs advertiser-side
  premia are different quantities. Gross ARPU is retired as the data proxy and
  kept only as an upper bound; the proxy carried downstream is x x ARPU. Two
  provenance corrections in this finalisation: E43 now cites the superseding
  published version (NBER w32765 / Marketing Science 2025, +31% -> ~0.24; the 2022
  working paper SSRN 4198438 +37%/~0.27 is retired), and E42's -18%/-23% split is
  ATTRIBUTION-VERIFIED but MAGNITUDE-PENDING independent confirmation against the
  primary table (A4/A12), so its controlled-regression leg is corroboration only
  and the central band [0.2, 0.4] does not depend on it.
- **Sovereign-regime s is a projection.** [0.3, 0.7] is bargaining theory, not
  measurement. A deployed sovereignty market that fails to move s despite a
  working 7012 protocol and a functioning stake is reported with equal
  prominence as a confirmation (GR-8).
- **The wedge is re-derived and its super-additive claim is withdrawn
  (Run-3).** The single-record modelling/targeting premium w_super is order ~10^0
  and SATURATES (bounded by returns-to-scale evidence E46-E50, not extrapolated);
  its anchor is a cross-sectional price-LEVEL ratio (E19->E20 ~4x), NOT an
  aggregation-returns measurement, and NO figure in the set directly measures
  aggregation super-additivity, which E47 affirmatively rejects in the variety
  dimension. The word "super-additive" is dropped entirely; v2's "super-additive,
  order 10^1-10^5" is withdrawn. The full observer-to-broker realised-value gap
  (order 10^4-10^5) is now a clean STOCK/STOCK comparison (lifetime
  data-attributable capture over one-time record), so the flow/stock crossing L132
  flagged is removed, but that gap is rent plus atomisation discount plus
  accumulation, not aggregation value. Both remain non-identified as points; the
  rent gap moves with region, tenure, and denominator choice (stress range ~1x10^4
  to ~2x10^6).
- **Vintage mismatch.** Broker prices (E19-E21) and the RTB dataset (E22) are
  2013 and historical; observer ARPU (E1-E10) is FY2023; stated WTA (E26-E33)
  is 2021. Cross-vintage comparison may understate current broker prices and
  is a source of the per-category bands' width, not a point estimate.
- **Meta metric discontinuity.** FY2023 is the last clean ARPU vintage; not
  comparable to post-2024 ARPP.
- **Google per-user dropped, not estimated** (E18): no primary basis exists.
- **iPinYou USD conversion dropped** (E22): native fen figure only, and
  specifically the training-partition winning-price CPM.
- **E21 ($0.005/attribute) dropped as UNVERIFIED**: the FT interactive is
  paywalled and the reprint 403'd; it is not used as the wedge lower-bound
  endpoint, which is re-derived from E19->E20 (~4x, rounding to order 10^1).
- **The extraction share is dimensionless only with an explicit resale
  frequency.** s(extraction) is (subject annual realisation)/(annual surplus);
  the numerator is the broker record price times the unmeasured annual resale
  multiplicity f. v1's numeric endpoint divided a one-time stock price by an
  annual flow (units yr^-1, not a share); the corrected anchor states f and
  moves with it. The order (10^-5 to 10^-4) is robust for f of order 1 to 10.
- **The endowment ratio anchor was corrected.** v1 anchored the WTA:WTP ratio on
  a participation-proportion ratio (5.37, E36), which is not a ratio of
  valuations and inflated the effect ~fourfold; the value-based anchor is
  ~1.2-1.4 (E34/E35). The participation ratio is retained only as direction-only
  corroboration.
- **No triangulated headline.** The v1 "two families converge to within a factor
  of ~2" claim is retired. A reservation-value stock and a gross-revenue flow
  have no theoretical reason to coincide; their overlap for one region/horizon
  slice is coincidental and is reported with the full annualisation-induced band
  ($22.50-$833/yr) beside it (GR-8). Per-category ranges replace the single
  headline.
- The M(u,y) form, the Sybil-resistance signal (C42), and reputation
  appreciation (E4-C07) are open conjectures / proposals, not measured returns.

## 9. Handoff

- **A5 (economist-referee):** the M4 finding is discharged in Section 4 (every
  quantity is now an interval with figure-traced endpoints) and Section 5.1
  (explicit sensitivity sweep). Rate the rebuild.
- **A2 (prose port):** the tier-A WEIS artifact consumes ONLY the dimensionless
  outputs of Sections 4-6 (share intervals, endowment ratio, wedge order,
  per-category ranges, named mechanism); the v1 convergence/triangulation
  framing is retired and must not be ported. Apply the S5 patch
  (weis_seventh_capital_S5_patch.md) for the 5.1/5.2 replacement. It must not
  carry the Section 2 dollar table; that stays in this internal note.
- **A4 (bib):** add Collis et al. (WEIS 2022); confirm AJL (2013), ATW (2016),
  Arrieta-Ibarra et al. (2018), Posner-Weyl (2018), Spiekermann et al. (2015),
  Akerlof (1970), IEEE 7012-2025; source Prince-Wallsten and Savage-Waldman
  (E37-E38) before any numeric use. **Run-3 additions (E39-E50):** Marotta,
  Abhishek & Acquisti (WEIS 2019); Johnson, Shriver & Du (Marketing Science
  2020); Kraft, Bleier, Skiera & Koschella (SSRN 4598472, ATT); Laub, Miller &
  Skiera (arXiv 2303.10906, cite as attribution-verified/magnitude-pending until
  the primary -18%/-23% table is confirmed); Wernerfelt, Tuchman, Shapiro &
  Moakler (cite the superseding published version NBER WP 32765 / SSRN 4915952 /
  Marketing Science 2025, +31%; the 2022 working paper SSRN 4198438 +37% is
  retired); Ravichandran & Korula (Google 2019, mark vendor-conflict);
  Bajari, Chernozhukov, Hortacsu & Suzuki (NBER WP 24334, 2018); de Fortuny,
  Martens & Provost (Big Data 2013); Varian (JEP 2014); Neumann, Tucker &
  Whitfield (Marketing Science 2019). All are VERIFIED-secondary except E46-E47
  (VERIFIED-primary); E45 (GumGum) is UNVERIFIED and must not be cited as
  load-bearing.
- **A3:** M(u,y) form review (Section 7).
- **A0 / ledger:** the CANON-LEVEL entry proposed in draft-v1 Section 6 stands;
  this note adds the empirical grounding (the 678x/31,000x replacement is now
  anchored in primary filings, not literature summary). **Run-3 CANON-LEVEL
  escalation (L133; finalised at L134):** v2's "aggregation wedge is
  super-additive, order 10^1-10^5" does NOT survive the returns-to-scale evidence;
  the word "super-additive" is dropped entirely (no figure demonstrates it and E47
  affirmatively rejects it in the variety dimension), what survives is a
  single-record modelling premium of order ~10^0 that saturates, and the large
  observer-to-broker gap is rent, not aggregation. This supersedes the wedge
  characterisation in L130/L132. The register process, not A12, decides the canon
  surface (GR-10).
