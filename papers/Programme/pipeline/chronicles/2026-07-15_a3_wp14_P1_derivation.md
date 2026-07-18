---
date: 2026-07-15
role: A3
wps: [WP-14]
extractions: [E4-seventh-capital, E2-moving-ceiling]
register_head: C96
ledger_entries: []
---

# A3 · WP-14 Proposition P1 derived in full (discharges M1; resolves m1, m2, m3)

## Verdict

Proposition P1 is now a self-contained, worked comparative-statics result rather
than a deferred proof obligation. The derivation is at
`rehydrations/academic/wp14_P1_derivation.md`. One bargaining model is fixed
(Rubinstein 1982 alternating offers); the Nash bargaining solution enters only as
that model's frictionless limit (Binmore, Rubinstein and Wolinsky 1986), which is
the direct answer to the M1 defect of naming two models as interchangeable. Both
comparative-statics directions are derived: under notice-and-consent the
subgame-perfect subject share equals her outside option and tends to zero; under
IEEE 7012 propose-and-respond the share is interior and, in the frictionless
limit, equals the subject's bargaining power $\beta$. The sovereign interval
$[0.3,0.7]$ from the S5 patch is shown to be the image of $\beta$ under bounded,
roughly symmetric relative patience (0.5 symmetric, 0.3 counterparty-favourable,
0.7 subject-favourable), so it is now visibly a projection FROM the bargaining
solution, not a guessed band. Three minors resolved: m1 (M(u,y) is used, not cut),
m2 (P4 discharges A1 conditionally), m3 (the shadow-exchange objection is answered
by a threshold reframing).

## Path

The load-bearing modelling decision was which of the two named bargaining models
to keep. The reasoning that settled it: the consent interface *is* the extensive
form of the game (it fixes who proposes and how many rounds), so a non-cooperative
model that reads the equilibrium share off the extensive form is the only model
that can mean what "the interface sets the share" says. A cooperative solution
concept cannot by construction distinguish notice-and-consent from
propose-and-respond except by an ad hoc asymmetric bargaining-power parameter,
which would assume the very thing P1 must derive. Rubinstein alternating offers
was therefore chosen; Nash is retained only as the $\Delta t \to 0$ limit, a
theorem about the same model, so the derivation never presents two models as
interchangeable. This also gives the $[0.3,0.7]$ interval a parameter ($\beta$,
hence a relative-patience ratio bounded near $2.3$) to be the image of.

Extraction regime: modelled as the one-round ultimatum restriction with M as
proposer. The result $s = h_X$ falls straight out, and $h_X \approx 0$ because the
subject is admitted to neither the aggregation nor the RTB venue where her data
clears (v2 note Section 6). A negative was kept at equal prominence: the near-zero
share is not produced by the near-zero disagreement point alone (a symmetric
two-sided bargain with both outside options near zero would split near one-half);
it needs both the ultimatum extensive form and the market-access fact. This is the
precise mechanism reading.

Sovereign regime: modelled as X-first alternating offers with credible,
roughly-symmetric, non-binding outside options, handled by the outside-option
principle. The frictionless-limit share is $\beta$, and the interval is its image.

## Reversals and cautions recorded

- I did NOT cut M(u,y). The task offered use-or-cut; I judged that USE discharges
  the m1 "decoration" charge by integration rather than deletion and yields a real
  comparative static (realised share $= M(u,y)\, s$, rising in participation and
  depth, with the extraction near-zero share becoming overdetermined by
  protocol-and-maturity). Using it weakens the sovereign claim in the correct
  direction ($[0.3,0.7]$ becomes a maturity-gated ceiling, not a promise), so it
  does not breach the "do not strengthen a claim" rule; the proposal label and the
  unestimated $\tau$ are preserved.
- On m2/m3 I resisted the tempting strong form ("the two-token design proves
  non-collusion"). P4 discharges A1 (non-collusion) ONLY, and only under a stated
  threshold. It does not touch A2, the capacity-deficit condition, or the
  time-indexing A3, so the imported guarantee still expires; $R(t)$ still rises and
  $t^{*}$ is still finite (GR-7 held; the retired "guarantees collapse" sentence is
  not reintroduced). This scoping is recorded as load-bearing, not a hedge.
- m3: I replaced P4's fragile binary premise ("no exchange pool exists") with a
  conversion-friction threshold ($\Phi(\phi)\,\Delta < \kappa$). The honest
  reversion clause is kept at equal prominence: a sufficiently liquid shadow
  exchange rate reintroduces the collusion incentive and reverts A1 to a bare
  assumption. This is an admission, filed as an open item, not an argued-away
  objection.

## Discipline check

Tier A held. No confidence percentages. No fenced figure and no fiat (GR-3):
every quantity is a share, a ratio, or a dimensionless order; the $[0.3,0.7]$ and
$[\sim 10^{-5}, 0.05]$ endpoints are consumed from the v2 note / S5 patch as
dimensionless outputs. GR-4 vocabulary throughout (boundary agent S, delegation
agent M, data subject X); no emoji. GR-7 held (imported guarantee invoked only
with A1-A3 and R(t); P4 discharges A1 alone). GR-8 held (the two negatives above
kept at equal prominence). GR-9: every step traces to E4-C10 (7012), E4-C11 (P4,
dual token), E2-C01 (A1 = Precondition 1), E4-C05 (M(u,y)), and the two valuation
artifacts for the endpoints. No register conjecture invented, renumbered, or
promoted (GR-1).

## Handoff

- **WP-14 next action (A2):** port Section 0 of the derivation into the draft in
  place of the P1 "Basis and obligation" paragraph; add the realised-share
  sentence (Section 7) to draft 5.3; promote the m2 synthesis (P4 discharges A1,
  A1 only) into draft Section 3.
- **A4:** add the five bargaining references (Rubinstein 1982; Binmore-Rubinstein-
  Wolinsky 1986; Nash 1950; Sutton 1986; Osborne-Rubinstein 1990).
- **A5:** re-review target is the MAJOR-to-accept-class move; M1 and minors
  m1/m2/m3 are addressed. Still open for their owners: M2 (property literature),
  M3 (WP-07 citability + R(t) schedule), M5 (the ordinal), m4/m5/m7.
- **A0:** propose the ledger entry recording the P1 derivation and the m1/m2/m3
  dispositions (see derivation Section 11). Blocked items: none from A3. P4 gate
  is the First Person's and is untouched.
