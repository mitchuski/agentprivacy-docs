---
artifact: weis-valuation-methodology-note
tier: A
venue: WEIS-2027 (target; CFP not yet published, A13 re-checks 2026-11-01)
wp: WP-14
role: A12
date: 2026-07-14
extraction_basis: >
  E4-seventh-capital claims c01, c02, c03, c04 (the rebuild target), c05
  (M(u,y) operationalisation), c06, c07, c08, c09, c10, c11, c12.
  Register rows referenced: C55 (architectural, occupied), C42 (active
  conjecture), C95 (active conjecture), C11 (active), C66, C81. No
  confidence percentages carried into asserted claims (GR-2, TIER-A).
purpose: >
  Discharge the E4-C04 rebuild obligation. Replace the GR-3 fenced
  figures 678x and 31,000x with a valuation methodology in which every
  number carries its assumptions in the same table, sensitivity is
  expressed as ranges, and a concrete market mechanism is named through
  which sovereignty value is realised or lost. Position the
  seventh-capital thesis inside the WEIS / data-markets literature.
status: draft-v1 (A12; awaiting A5 economist-referee review and A3 review of the M(u,y) operationalisation)
handoff: A2 (prose port), A3 (M(u,y) form review), A4 (bib additions), A5 (economist-referee pass)
---

<!-- ============================================================
A12 APPARATUS NOTE (pipeline internal; strip at release)
This note is the methodology substrate for WP-14 section 5 (evaluation)
and section 3 (the appropriation-share and M(u,y) definitions). It does
NOT reproduce 678x or 31,000x as asserted facts; it names them only as
the objects under rebuild, per the GR-3 sanctioned formulation for
A12's replacement obligation. Fiat figures appear NOWHERE (GR-3/L057);
all magnitudes are ratios, shares, or dimensionless wedges.
============================================================ -->

# WEIS valuation methodology note: rebuilding the per-person value gap

## 0. Verdict

The two canonical per-person value-gap magnitudes do not survive a tier-A
rebuild as asserted facts, and the rebuild wins (role law; GR-3, GR-6).

- The present-day gap figure (canon: 678x) is not point-identified. What
  is well-posed and defensible is a **surplus-appropriation share** s in
  [0, 1], empirically near zero under the current consent regime, together
  with a **data-aggregation wedge** w that is large, positive, and
  super-additive but bounded and not point-identified. The single number
  678 is one draw from a wide distribution over dataset composition,
  model class, and counterfactual, and is dropped.
- The accessible-volume figure (canon: 31,000x) was already reframed in
  the canon itself from an arithmetic ratio to a non-arithmetic quantity
  ("the difference in accessible volume on the same manifold... topology,
  not arithmetic", v4-economics 219). A non-arithmetic quantity is not a
  valuation ratio. At tier A it is retired as a number and replaced by an
  unquantified structural claim about coordination modes an extraction
  architecture cannot reach without breaking its own revenue model.

Both outcomes carry a proposed CANON-LEVEL ledger entry (Section 6; GR-10).
Neither the 678x nor the 31,000x is propagated at tier A. No fiat figure
appears at any point.

The market mechanism through which the value is realised or lost is named
in Section 4 and is load-bearing: the role's failure mode is a monetary
claim with no market mechanism, and this note names one.

## 1. What the canon figures were, and why the point estimates fail

The spec 30 canonical-figures table records two magnitudes:

| Figure (fenced) | Canon gloss | Basis document (off-disk) |
|---|---|---|
| 678x | present-day per-person data-value gap ("just for data today") | Substack essay v2 |
| 31,000x | accessible-volume value gap under full behavioural capture | essay v4 |

Three structural reasons the point estimates cannot be asserted at tier A:

1. **Ill-posed denominator.** A per-person "gap" of the form V_potential /
   V_current is undefined when V_current, the value the data subject
   currently captures, tends to zero, which is precisely the extraction
   regime the thesis describes. A ratio to a near-zero base is not a
   measurement; it is a division artefact. The honest object is the
   subject's *share* of the appropriable surplus, which is bounded in
   [0, 1] and well-posed even at the extreme.

2. **Aggregation dependence.** The value of behavioural data is strongly
   super-additive: atomised records trade in broker markets for very
   little, while the same records aggregated and modelled are worth far
   more (Acquisti, Taylor and Wagman 2016). Any single ratio silently
   fixes a dataset composition, a model class, and a time, none of which
   the canon exposes. The wedge is real and large; the specific value is
   not identified.

3. **Reframed, not measured, at the high end.** The 31,000x figure was
   restated in the canon as a topological quantity, "the difference in
   accessible volume on the same manifold", not an arithmetic ratio
   (v4-economics 219; whitepaper 577, "boundary expressiveness... the
   holographic bound"). A quantity its own source declares non-arithmetic
   cannot be re-imported as a valuation ratio. It is retired as a number.

## 2. The rebuild, layer one: the appropriation share and the aggregation wedge

We replace 678x with two named, bounded, sensitivity-ranged quantities.
Every assumption sits in the same table as the quantity it feeds.

### 2.1 The surplus-appropriation share s

Let the appropriable data-derived surplus attributable to one subject over
one period be normalised to 1. The subject captures share s in [0, 1]; the
observing firm captures 1 - s. This is dimensionless by construction, so
the GR-3 fiat fence is satisfied without loss.

| Quantity | Definition | Regime value (range) | Assumptions in-table |
|---|---|---|---|
| s (extraction) | subject share of per-subject data surplus under notice-and-consent | [0, 0.05] | outside option = service exclusion; take-it-or-leave-it consent; no secondary market accessible to the subject; broker prices for atomised records are the subject's only realisable price and are near zero (Acquisti-Taylor-Wagman 2016) |
| s (sovereign, upper bound) | subject share under a bilateral price-posting protocol with a credible outside option | [0.3, 0.7] | IEEE 7012 propose-and-respond bargaining (E4-C10); Nash bargaining split with roughly symmetric outside options; quality signalled by a non-transferable stake (Section 4.3) |
| WTA/WTP endowment ratio | ratio of price to accept disclosure vs price to pay for protection | [2, 6] | Acquisti, John and Loewenstein 2013; measured demand-side signature of the appropriation gap; framing- and order-sensitive, hence a range not a point |

The appropriation gap is then the movement of s from the extraction range
to the sovereign range, a shift of roughly one order of magnitude in the
subject's captured share, expressed as a share change, never as a ratio to
a near-zero base. This is the honest residue of "678x": the subject
currently captures a share consistent with zero, and an architecture that
supplies a credible outside option and a quality signal can move that
share into a bargaining regime. The number 678 is not reconstructed and is
not claimed.

### 2.2 The aggregation wedge w

| Quantity | Definition | Range | Assumptions in-table |
|---|---|---|---|
| w | value of aggregated-and-modelled behavioural data / value of the same data atomised in broker markets | super-additive, positive, bounded; order 10^1 to 10^3 across the empirical range, not point-identified | complementarity and network effects in data (Acquisti-Taylor-Wagman 2016; OECD 2013); the exact wedge depends on dataset composition, model class, and the counterfactual buyer; a single value fixes all three silently |

The wedge is where the firm's surplus comes from and is exactly the object
a subject-side aggregator (Section 4.2) would need to capture. We assert
its sign and super-additivity, and a wide range; we do not assert a point.
This is the honest residue of the high-end intuition behind the essays: the
value released by aggregation is large. It is not 31,000, and it is not a
per-person dollar figure.

### 2.3 Sensitivity discipline

Every row above is a range, not a point. Where the literature supplies a
measured range (WTA/WTP), we carry the measured range and its known
sensitivities (framing, order). Where no measurement identifies the
quantity (w, sovereign-regime s), we carry an order-of-magnitude interval
and label it non-identified. No row collapses to a point estimate; the
role's second failure mode (point estimates without ranges) is thereby
excluded by construction.

## 3. The rebuild, layer two: the accessible-volume claim, de-numbered

The 31,000x figure is retired as a number (Section 1, reason 3). What
survives, and belongs in the paper as a qualitative structural claim
rather than a magnitude, is:

> An extraction architecture cannot activate subject-side protection
> without degrading the observation on which its own revenue depends; a
> sovereign architecture (structural separation of boundary agent S and
> delegation agent M, with structural context erasure between invocations)
> can reach coordination modes, portable and consented disclosure, that
> the extraction architecture cannot reach without redesign. The
> difference is an incentive-and-architecture constraint, not a measured
> ratio.

This is stated without a number. It is the honest content of the
"accessible volume" reframing once the mythopoetic manifold vocabulary is
removed (GR-4). It carries no valuation figure and makes no reconstruction
claim; the information-theoretic guarantee that underwrites the
separation, with its preconditions and time index, is imported from WP-07
(Section 5), not restated here.

## 4. The market mechanism: how sovereignty value is realised or lost

The role law requires a named market mechanism. The mechanism has three
components; the value is lost in the first regime and realised in the
second.

### 4.1 The consent interface as a bargaining protocol (where s is set)

The share s of Section 2.1 is not a preference; it is the equilibrium of a
bargaining game whose rules are the consent interface.

- **Notice-and-consent** is a take-it-or-leave-it offer in which the
  subject's outside option is exclusion from the service. In a Rubinstein
  or Nash bargaining model with an outside option that low, the subject's
  equilibrium share tends to zero. This is the extraction regime, and it
  is a mechanism result, not a moral one: the interface itself sets s
  near zero (E4-C10, imposition pattern; E4-C11, structure over policy).
- **IEEE 7012-2025 propose-and-respond** (the subject proposes terms; the
  organisation accepts, negotiates once, or declines; one round maximum;
  bilateral signed record) inverts the offer direction and supplies a
  credible outside option. The equilibrium share moves into the sovereign
  range of Section 2.1. The standard is the machine-readable protocol that
  changes the bargaining structure (E4-C10; IEEE Std 7012-2025).

### 4.2 A subject-side aggregator (where the wedge w is captured)

The aggregation wedge w (Section 2.2) is captured today by the firm
because only the firm aggregates. A data coalition or mediator of
individual data (the "data-as-labour" market design of Arrieta-Ibarra,
Goff, Jimenez-Hernandez, Lanier and Weyl 2018; Posner and Weyl 2018)
aggregates individual behavioural streams on the subject side and sells
access, moving the wedge, or a negotiated fraction of it, back to
subjects. The seventh-capital framing differs from the pure data-as-labour
proposal in what it treats the stock as (Section 7): but the aggregator is
the same market instrument, and it is the concrete venue in which the
wedge is realised for subjects rather than for the observer.

### 4.3 A non-transferable reputation stake as the quality signal (why the market does not collapse)

Personal-data markets fail on adverse selection: a buyer cannot tell
high-quality, consented, fresh data from noise, so the market unravels
toward a lemons equilibrium (Akerlof 1970; Spiekermann, Acquisti, Bohme
and Hui 2015; the WEIS market-for-lemons lineage, Anderson 2001). The
non-transferable, non-purchasable proof-of-practice resource of E4-C06
(register conjecture C42, carried with its proof obligation, no confidence
band at tier A) is the quality-and-Sybil signal that lets the market of
4.1 and 4.2 price quality: because the resource cannot be minted by fake
accounts, bought, or transferred, a claim's cost is the difficulty of
earning it, which resists the Sybil attack that would otherwise flood the
signal. This is the economic answer to the Spiekermann "why do these
markets fail" question: the failure is informational, and a Sybil-resistant
non-transferable stake is a candidate repair. It is a design claim and an
open register conjecture, not a measured result.

### 4.4 What is lost, stated plainly

In the extraction regime the subject's share s is near zero and the
aggregation wedge w accrues entirely to the observer. The sovereignty the
thesis describes therefore has a market price, and that price is currently
paid to someone else. This is the home thesis stated as a mechanism claim,
with the mechanism named, and with no fiat figure and no fenced ratio.

## 5. The market-maturity gate M(u,y): a proposed operationalisation

E4-C05 records that the value equation carries a multiplicative
market-maturity gate M(u,y) whose arguments u and y are given no
functional form, domain, or units in any swept source, and that defining
it is an A12/A3 obligation that must not be back-filled into canon. This
section proposes a definition as the rehydration's own construction, to be
reviewed by A3. It is not asserted as canon (GR-6); it is a candidate
operationalisation.

Proposed:

- Domain and units: M : [0, 1] x R_+ -> [0, 1], dimensionless gate.
- u in [0, 1]: market participation, the fraction of counterparties able
  to price sovereignty (able to accept a 7012 proposal and settle against
  a subject-side aggregator). u = 0 means no counterparty can price
  sovereignty.
- y in R_+: market depth, an increasing measure of time-in-operation or
  liquidity of the sovereignty market.
- Candidate functional form: M(u, y) = u * (1 - e^{-y / tau}), monotone
  non-decreasing in both arguments, valued in [0, 1], with M(0, y) = 0
  (no participation, no capture) and M(u, y) -> u as y grows (depth
  saturates). tau > 0 is a market-formation time constant.

As a product factor in the value equation, M gates realised value:
realised value = M(u, y) * potential value, so that in the absence of a
market able to price sovereignty (u = 0) no value is captured, which is
the standing caveat the canon states informally ("if the infrastructure
exists to capture that value"). The form is a proposal: its purpose here
is to give M the domain, units, and monotonicity the equation needs, so
that the WEIS paper can use it without inventing argument semantics
silently. A3 owns whether this form, or another with the same boundary
behaviour, enters WP-14.

## 6. Canon-figure verdict and proposed CANON-LEVEL ledger entry

Under the role law, where a canonical figure does not survive the rebuild
the rebuild wins and a CANON-LEVEL ledger entry is proposed (GR-10, GR-6).

**Verdict.**
- 678x: does not survive as an asserted point estimate. Replaced by the
  bounded surplus-appropriation share s (Section 2.1) and the
  non-identified aggregation wedge w (Section 2.2), both range-valued, with
  a named market mechanism (Section 4). The value 678 is not reproduced.
- 31,000x: does not survive as a valuation ratio. It was already reframed
  in the canon to a non-arithmetic quantity; at tier A it is retired as a
  number and replaced by the unquantified structural claim of Section 3.
- IIRC divergence (E4-C02): the whitepaper's six-capital enumeration
  (Financial, Manufactured, Natural, Human, Social, Cultural) diverges
  from the IIRC International <IR> Framework six capitals (Financial,
  Manufactured, Intellectual, Human, Social and Relationship, Natural).
  The enumeration must be corrected before tier-A reuse; the seventh-capital
  thesis (C55) is unaffected.

**Proposed ledger entry (A0 to file; A12 does not resolve canon):** a
CANON-LEVEL note recording that (a) the spec 30 figures 678x and 31,000x
do not survive the WP-14 tier-A rebuild and are replaced by the
share/wedge methodology and the de-numbered structural claim respectively;
(b) the IIRC six-capital enumeration in the whitepaper is incorrect against
the external source and is corrected in the extraction and the rebuild.
The register process, not this note, decides what the canon surfaces do
with the finding.

## 7. Positioning inside the literature (not beside it)

The seventh-capital thesis sits at the intersection of three strands of
the economics-of-information-security and data-markets literature, and its
distinct contribution is architectural.

- **Economics of privacy (Acquisti and colleagues).** Acquisti, Taylor
  and Wagman (2016) survey privacy as jointly cost- and benefit-bearing
  and document the aggregation-dependence of data value; Acquisti, John and
  Loewenstein (2013) measure the willingness-to-accept versus
  willingness-to-pay endowment gap, the demand-side signature of the
  appropriation problem. The rebuild uses these as its measured anchors
  (Section 2). The thesis inherits their framing: privacy value is
  context-dependent and the subject values her own data above its market
  price.

- **Data as labour versus data as capital (Arrieta-Ibarra, Lanier, Weyl,
  Posner).** Arrieta-Ibarra, Goff, Jimenez-Hernandez, Lanier and Weyl
  (2018) and Posner and Weyl (2018) argue behavioural data should be
  treated as labour, priced by something like wages, against the incumbent
  treatment of it as capital owned by the firm; Lanier (2013) frames this
  as data dignity. The seventh-capital thesis is a deliberate third
  position: it treats behavioural data as a *capital class the subject
  owns*, a stock that yields returns to the subject, rather than a labour
  flow priced per contribution. The productive tension with data-as-labour
  is the paper's clearest point of contact and must be argued, not elided:
  the thesis agrees with the DaL camp that the returns are misappropriated
  and disagrees on whether the remedy is a wage (labour) or an owned,
  non-depreciating stock (capital).

- **Personal-data-market design and its failures (Spiekermann; the WEIS
  lemons lineage).** Spiekermann, Acquisti, Bohme and Hui (2015) catalogue
  why personal-data markets fail: asymmetric information, externalities,
  adverse selection; Anderson (2001) and the WEIS tradition read security
  and data markets through Akerlof's (1970) market for lemons. The thesis
  answers this failure literature with a mechanism: structural separation
  (the information-theoretic guarantee of WP-07, imported and time-indexed
  R(t)) plus a non-transferable Sybil-resistant quality stake plus a 7012
  bargaining protocol. This is why the thesis is *inside* the literature:
  it takes the field's diagnosis of market failure and proposes an
  architectural repair, rather than restating that data is valuable.

The one-line position: the seventh-capital thesis accepts the
economics-of-privacy diagnosis of appropriation, takes the data-as-capital
side of the data-as-labour debate but reassigns ownership of the stock to
the subject, and answers the personal-data-market failure literature with
an architectural mechanism whose guarantee is information-theoretic and
dated rather than a policy promise.

## 8. Bibliography additions required (handoff to A4)

None of the following are yet in `templates/submission/references/pv_v6.bib`
(verified 2026-07-14). A4 to verify and add:

- Acquisti, Taylor, Wagman (2016), "The Economics of Privacy", Journal of
  Economic Literature 54(2).
- Acquisti, John, Loewenstein (2013), "What Is Privacy Worth?", Journal of
  Legal Studies 42(2).
- Arrieta-Ibarra, Goff, Jimenez-Hernandez, Lanier, Weyl (2018), "Should We
  Treat Data as Labor? Moving beyond Free", AEA Papers and Proceedings 108.
- Posner, Weyl (2018), Radical Markets, Princeton, chapter on data as labour.
- Lanier (2013), Who Owns the Future?, Simon and Schuster.
- Spiekermann, Acquisti, Bohme, Hui (2015), "The challenges of personal
  data markets and privacy", Electronic Markets 25(2).
- Anderson (2001), "Why Information Security is Hard: An Economic
  Perspective", ACSAC / WEIS lineage.
- Akerlof (1970), "The Market for Lemons", Quarterly Journal of Economics
  84(3).
- OECD (2013), "Exploring the Economics of Personal Data".
- IEEE Std 7012-2025, Machine Readable Personal Privacy Terms (already in
  extraction citations; confirm bib key).

## 9. Limits of this note (GR-8)

- The sovereign-regime share range [0.3, 0.7] is a bargaining-theoretic
  projection, not a measurement; no deployed sovereignty market has been
  observed to price s. It is labelled a projection wherever it appears.
- The aggregation wedge w is asserted only in sign, super-additivity, and
  order-of-magnitude interval; it is not identified, and the paper must not
  let the interval harden into a point.
- The M(u,y) form is a proposed operationalisation, not canon and not
  measured; A3 owns its entry.
- The Sybil-resistance quality signal (C42) and the reputation-appreciation
  claim (E4-C07) are open register conjectures carried with proof
  obligations, not measured returns; the tier-ladder multipliers (E4-C08)
  are illustrative design parameters and are reported as such, never as
  measured returns.
- A measured result against these predictions, for instance a sovereignty
  market that fails to move s despite a working 7012 protocol and a
  functioning stake, is reported with the same prominence as a
  confirmation (GR-8).
