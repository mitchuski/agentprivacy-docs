---
date: 2026-07-15
role: A12
wps: [WP-14]
extractions: [E4-seventh-capital]
register_head: C96
ledger_entries: [L133]
---

# A12 Run-3: data-attributable observer capture and the wedge that turned out to be rent

## Verdict

Two objects that Run-2's hostile lenses (L132) left wide are now tightened in the
working valuation rebuild (weis_valuation_methodology_v2_empirical.md), and the
tightening produced one reversal worth naming up front: the aggregation wedge is
not super-additive at the order the canon and v2 asserted. Its genuinely
super-additive component is order 10^0-10^1 and saturates; the large
observer-to-broker gap is rent, atomisation discount, and lifetime accumulation,
not compounding data value.

Concretely:

1. Observer capture is now DATA-ATTRIBUTABLE. Gross ARPU is retired as the data
   proxy and replaced by x x ARPU, x the targeting-premium fraction, x in [0.04,
   0.52], central band [0.2, 0.4], policy-clean midpoint ~0.20. Worldwide that is
   $8.92-$17.84/yr central versus $44.60/yr gross.

2. The wedge is split and re-derived stock/stock. The upper endpoint no longer
   crosses the flow/stock boundary L132 flagged; the super-additive claim collapses
   from [10^1, 10^5] to [10^0, 10^1] under returns-to-scale evidence.

## Path

### The fraction: two regimes that must not be conflated

The deep-sourcing returned seven estimates of the data-attributable fraction of
gross ad value. The trap is averaging them. They split into an AGGREGATE family
(what a publisher's or advertiser's realised outcome actually loses when tracking
is removed) and a MARGINAL family (the gap on a single untracked impression while
the rest of the market stays tracked). The marginal cluster is remarkably
consistent at ~50-52% (Johnson E40; Kraft price premium E41; Google E44) but it is
a selection-conditional comparison struck in an equilibrium where 99.77% of
impressions stay targeted, and it structurally overstates the aggregate. The
aggregate family is the correct one for scaling capture: ~0.04 publisher-realized
(Marotta E39), ~0.18-0.23 controlled regression (Laub E42), ~0.20 ATT revenue loss
(Kraft E41), ~0.27 advertiser-side implied from +37% CPA (Wernerfelt E43). Central
band [0.2, 0.4], midpoint ~0.20.

Reversal recorded (GR-8): the ~13x divergence between the independent Marotta ~4%
and Google's own ~52% is unresolved and I did not resolve it. Both are reported
with equal prominence; E44 carries a vendor-conflict flag; the GumGum figure (E45)
is dropped UNVERIFIED because the author sells the competing product.

### The wedge: fixing the boundary, then watching the super-additivity evaporate

v2's wedge top divided the observer's gross ANNUAL flow by a one-time broker record
price. That is a flow over a stock; the ratio carries units of yr^-1 and inflates.
The fix the task set was a like-for-like stock/stock top: lifetime data-attributable
capture (x x ARPU x tenure = $107-$214 worldwide central, a STOCK) over the one-time
targeted broker record ($0.0021 E20, a STOCK). That lands at 5.1x10^4 to 1.0x10^5,
dimensionally clean, and the data-attributable fraction alone shaves the central top
from v2's ~4.5x10^5 to ~1x10^5.

But the more important move was the returns-to-scale evidence (Bajari et al. E46-E47;
de Fortuny E48; Varian E49; Neumann E50). It says aggregation value saturates: forecast
error falls only at 1/sqrt(N)+1/sqrt(T), the variety dimension N is flat-to-negative,
Google discards 99.9% of its data, and two-attribute broker profiling is ~24% accurate.
There is no empirical term that carries an aggregation wedge to order 10^3+. So the
order 10^4-10^5 observer-to-broker gap cannot be super-additive aggregation. It
decomposes into a small genuine aggregation premium (w_super, order 10^0-10^1, anchored
on the intra-market segment ratio E19 general record -> E20 targeted segment, ~4x), plus
market-position rent (the broker resale market prices an atomised record far below its
realised value because the subject is not the clearing venue), plus lifetime accumulation.

This is the reversal. v2 said "w is super-additive, order 10^1-10^5". That does not
survive. The super-additive part is order 10^0-10^1; the bigness is rent. I did not
soften this to keep the wedge impressive; the honest wedge is small and the impressive
number is an appropriation gap, which is arguably the stronger claim for the thesis
anyway (the subject is being denied a rent, not out-competed on aggregation).

### What I did not touch

The bear-check on the s-share and endowment-ratio results: the fraction bears on
s(extraction) through 1/x, a factor of ~2.5-5, which does not change s's order (stays
10^-4/-5). So s (4.1), the WTA:WTP ratio (4.2), and the no-triangulation headline (5)
are left as Run-2 set them, with the 1/x factor noted in place. No re-opening of what
already survived.

## Handoff

- OPEN: which single x within [0.04, 0.52] is correct is not identified; the Marotta
  vs Google ~13x gap is unresolved (register-process/A4 territory, not A12's to close).
- OPEN (CANON-LEVEL, L133): the register process must decide whether the canon's
  wedge surfaces carry "super-additive, order 10^1-10^5" (they should not, per the
  returns-to-scale evidence) or the corrected "super-additive component order 10^0-10^1,
  saturating; large gap is rent". Supersedes the wedge lines in L130 and L132. A12 does
  not resolve canon (GR-10).
- A4: add the ten Run-3 bib entries E39-E50 (Section 9 handoff), E44 vendor-conflict,
  E45 UNVERIFIED/dropped, before any prose port.
- A2/A3: carry x x ARPU (not gross) and the split wedge into the WP-14 revision loop;
  the "super-additive" adjective must not port without the saturation caveat.
- NEXT ACTION (WP-14): A5 economist-referee re-read of the tightened wedge and
  observer-capture sections, confirming the super-additive-to-rent correction reads as
  a strengthening of honesty, not a weakening of the result.
