---
tier: A
venue: WEIS-2027
wp: WP-14
role: A3 (formalist)
status: derivation (drop-in replacement for the draft's Proposition P1 "Basis and obligation" text)
date: 2026-07-15
discharges: A5 review-1 finding M1 (L131) in full; minors m1 (M(u,y) disposition),
  m2 (P4 vs A1 relationship), m3 (shadow-exchange-rate objection).
extraction_basis: >
  E4-seventh-capital C10 (IEEE 7012 propose-and-respond; Promise Theory
  invitation/imposition), C11 (dual-token incentive compatibility = P4;
  GR-7 hazard NOT propagated), C05 (M(u,y)); E2-moving-ceiling C01
  (imported guarantee, Precondition 1 = non-collusion = Assumption A1).
  Dimensionless endpoints from weis_valuation_methodology_v2_empirical.md
  Section 4.1 and weis_seventh_capital_S5_patch.md Section 5.1.
discipline: >
  Tier A (GR-2): P1 is stated as a proved comparative-statics result of one named
  model with its assumptions; no confidence percentages. GR-3: no fenced figure,
  no fiat; every quantity is a share, a ratio, or a dimensionless order. GR-4
  vocabulary (boundary agent S, delegation agent M, data subject X). GR-7: the
  imported guarantee is invoked only with A1-A3 in-passage and R(t); P4 discharges
  A1 only, not the whole guarantee. GR-8: the negative (P1 depends on the interface
  as extensive form, and the sovereign interval is a projection, not a measurement)
  is kept at equal prominence. No em-dashes; UK spelling.
---

# WP-14 · Derivation of Proposition P1, self-contained

This note converts the draft's Proposition P1 from a deferred proof obligation
into a worked result. It fixes one bargaining model, states the disagreement
point and outside option explicitly for each of the two consent interfaces,
and derives the two comparative-statics directions. It then resolves three
minors: the disposition of the market-maturity gate M(u,y) (m1), the
relationship between Proposition P4 and Assumption A1 (m2), and the
shadow-exchange-rate objection to P4's premise (m3).

---

## 0. The revised statement (self-contained)

**Proposition P1 (the consent interface sets the appropriation share).**
Normalise the appropriable per-subject, per-period *data* surplus to 1, split
between the data subject X (share $s$) and the counterparty M (share $1-s$).
Model the consent interface as the extensive form of one non-cooperative
alternating-offers bargaining game (Rubinstein 1982) between X and M, in which
the interface fixes (i) which party posts the first offer and (ii) how many
offer/response rounds precede exercise of an outside option. Write $h_X$ for X's
outside-option payoff and $h_M$ for M's, each a share of the same normalised
surplus. Then:

- **(a) Extraction regime (notice-and-consent).** The interface is a single
  round in which M posts a take-it-or-leave-it offer and X may only accept or
  exercise her outside option. The unique subgame-perfect share of X is
  $s = h_X$. Because X's only realisable price for her record is the atomised
  broker-resale price, she being admitted to neither the aggregation nor the
  real-time-bidding venue where her data actually clears, $h_X \approx 0$, and
  therefore $s \to 0$.

- **(b) Sovereign regime (IEEE 7012 propose-and-respond).** The interface is a
  bilateral game in which X posts the first offer, M accepts, counters once, or
  declines, and outside options are credible and roughly symmetric and
  non-binding. The unique subgame-perfect share of X is interior; in the
  frictionless limit it equals X's bargaining power $\beta \in (0,1)$, so for
  $\beta \in [0.3, 0.7]$ (relative patience within a bounded, roughly symmetric
  range) $s \in [0.3, 0.7]$.

- **(c) Realisation.** The *realised* subject share is
  $s_{\text{realised}} = M(u,y)\, s$, where $M(u,y) \in [0,1]$ is the
  market-maturity gate of Section 3 of the draft. $s_{\text{realised}} \to s$
  only as the sovereignty market matures ($u \to 1$, $y \to \infty$), and
  $s_{\text{realised}} \to 0$ when no counterparty can price sovereignty
  ($u \to 0$).

The claim is a *mechanism* result, not a moral one: the interface, read as the
extensive form of the game, sets the share; the subject's preference does not
enter the equilibrium share at all.

---

## 1. Model choice, and why one model, not two

**Choice (one line).** We use Rubinstein (1982) alternating-offers bargaining,
because the consent interface *is* the extensive form of the game, it fixes who
proposes and how many rounds, so a non-cooperative model that reads the
equilibrium share off the extensive form is exactly what the sentence "the
interface sets the share" has to mean; the Nash bargaining solution then enters
only as this same model's frictionless limit (Binmore, Rubinstein and Wolinsky
1986), a theorem about the model, not a second model offered as interchangeable.

This directly answers the M1 defect. The first-pass draft named "Nash bargaining
with outside options, *or* the Rubinstein alternating-offers model" as if the two
were interchangeable substitutes. They are not offered as substitutes here. There
is one model, the non-cooperative alternating-offers game. The cooperative Nash
solution appears once, as the $\Delta t \to 0$ limit of that game's subgame-perfect
equilibrium, and is used only to name the interior interval $[0.3,0.7]$ as an
image of a bargaining-power parameter. No result rests on the axiomatic Nash
solution standing on its own.

The choice matters for a second reason. The two interfaces differ precisely in
their extensive form: notice-and-consent is a one-round game with M as proposer,
the propose-and-respond protocol is a multi-round game with X as proposer. A
cooperative solution concept, which abstracts away the extensive form, cannot by
construction distinguish the two interfaces except by an ad hoc asymmetry in an
exogenous bargaining-power parameter. The non-cooperative model derives the
asymmetry from the protocol instead of assuming it, which is the whole content
of the proposition.

---

## 2. Primitives

**The pie.** Let the appropriable per-subject, per-period *data-derived* surplus
be $1$. This is the surplus that exists when the subject's behavioural record is
used under agreement. It is explicitly the *data* surplus, not the subject's
total welfare from the exchange; the consumption value of any free service the
subject receives in a zero-price two-sided market is a separate object and is not
in this pie (this scopes the claim, and is the honest answer to the "near zero
*net of the service*" objection, m6, which the S5 patch carries as the upper
allowance on $h_X$).

**Agents.** X is the data subject. M is the counterparty (the observing firm,
carrying, where relevant, the boundary agent S and the delegation agent M of the
architecture; here "M" is the single economic counterparty across the table from
X). The split $(s, 1-s)$ is over the pie of $1$.

**Outside options.** $h_X \in [0,1]$ is the share X can secure by walking away
from this counterparty; $h_M \in [0,1]$ is the share M secures by walking away
from this subject. Both are measured as shares of the same normalised surplus.

**The interface as extensive form.** The consent interface determines two things
about the game: the *identity of the first proposer* and the *number of
offer/response rounds* before an outside option is taken. Everything else, the
pie and the outside options, is held fixed across interfaces. The comparative
static is therefore a comparative static in the extensive form alone, which is
what licenses the reading "the interface, not the subject, sets the share".

---

## 3. The bargaining model, stated once

Two players split a pie of $1$ by alternating offers. Player $i$ has per-period
discount factor $\delta_i \in (0,1)$; write $\delta_i = e^{-\rho_i \Delta t}$ for
discount rate $\rho_i > 0$ and period length $\Delta t$.

**Full alternating offers (Rubinstein 1982).** With player 1 proposing first and
no outside options, the unique subgame-perfect equilibrium gives player 1 the
share
$$
x^{*}_1 = \frac{1 - \delta_2}{1 - \delta_1 \delta_2}, \qquad
x^{*}_2 = \frac{\delta_2 (1 - \delta_1)}{1 - \delta_1 \delta_2},
$$
agreement is immediate, and in the symmetric case $\delta_1 = \delta_2 = \delta$
player 1 gets $1/(1+\delta)$.

**Frictionless limit (Binmore, Rubinstein and Wolinsky 1986).** As
$\Delta t \to 0$ the first-mover advantage vanishes and the proposer's share
converges to
$$
x^{*}_1 \longrightarrow \frac{\rho_2}{\rho_1 + \rho_2},
$$
the more patient player (lower $\rho$) taking the larger share. This limit is the
asymmetric Nash bargaining solution
$s = \arg\max_{s}\, (s - d_X)^{\beta}(1 - s - d_M)^{1-\beta}$ with disagreement
point $(d_X, d_M)$ and the subject's bargaining power
$\beta = \rho_M/(\rho_X + \rho_M)$; with $d_X = d_M = 0$ it gives $s = \beta$.

**Outside options (the outside-option principle; Binmore, Rubinstein and
Wolinsky 1986; Sutton 1986).** When a player may abandon the table for an outside
option $h_i$, the subgame-perfect split is unchanged from the no-outside-option
split *if* $h_i$ is below that player's inside share (a non-binding threat), and
equals $h_i$ for that player *if* $h_i$ exceeds the inside share (a binding
threat). Outside options enter as threat points, not as the disagreement point of
the continuation game.

These three facts are the whole toolkit. The two interfaces are two instances of
the same game.

---

## 4. Interface (a): notice-and-consent, the extraction regime

**Extensive form.** Notice-and-consent gives the subject no power to propose: she
is shown posted terms and may accept, or decline and be excluded from the service.
This is a single-round game in which M is the proposer and X is the responder,
that is, an ultimatum game (the one-round restriction of the alternating-offers
game with M moving first).

**Disagreement point and outside option, explicitly.** If X declines, she is
excluded from the service and receives her outside option $h_X$. X is not admitted
to the aggregation venue or the real-time-bidding auction where behavioural data
clears; the only price she can realise on her own is the atomised broker-resale
price of a single record, which is near zero as a share of the appropriable
surplus. Hence $h_X \approx 0$. M, declining this one subject, continues to
operate on every other subject's data, so the marginal value of this subject's
record to M is small and $h_M \approx 0$ as well. The disagreement point of the
one-shot game is $(h_X, h_M) \approx (0,0)$.

**Derivation.** In the ultimatum game the responder accepts any offer weakly
above her outside option and the proposer offers exactly that. M therefore offers
X the share $h_X$ and keeps $1 - h_X$. The unique subgame-perfect share is
$$
s_{\text{extraction}} = h_X.
$$
With $h_X \approx 0$, $s_{\text{extraction}} \to 0$.

**What drives the result (GR-8, stated plainly).** The near-zero share is *not*
produced by a near-zero disagreement point on its own: if both outside options
are near zero and the game were the *symmetric two-sided* bargain, the split
would be near $1/2$, not near $0$. The extraction result requires *both* features
that notice-and-consent supplies: (i) the extensive form makes M the sole
proposer in a single round, which lets M appropriate everything down to X's
outside option, and (ii) that outside option is near zero because X is excluded
from the clearing venue. Change either, and the share moves. This is the precise
sense in which the *interface* sets the share: it is the extensive form (i),
combined with the market-access fact behind (ii), and not any preference of X.

**Cross-reference to the empirical endpoint.** The dimensionless extraction
interval $s \in [\sim 10^{-5},\, 0.05]$ carried in
`weis_valuation_methodology_v2_empirical.md` Section 4.1 and the S5 patch is
exactly the comparative-statics image of $h_X \approx 0$: the lower orders are
the ratio of the subject's realisable broker price (times the unmeasured annual
resale multiplicity) to the appropriable surplus, and the upper $0.05$ is the
generous, unmeasured allowance for uncaptured consumer surplus from the free
service (the zero-price side, m6). The proposition supplies the mechanism; the v2
note supplies the endpoints; they agree by construction.

---

## 5. Interface (b): IEEE 7012 propose-and-respond, the sovereign regime

**Extensive form.** IEEE Std 7012-2025 inverts the offer direction: the subject
posts machine-readable terms first, and the organisation accepts, negotiates once,
or declines, with a bilateral signed record and one round of counter maximum
(E4-C10). This is an alternating-offers game with X as the first proposer and at
least two rounds (propose, then accept or counter-once), the "negotiate once"
step giving it genuine two-sidedness rather than the degenerate one-round
structure of interface (a).

**Disagreement point and outside option, explicitly.** The standard makes the
subject's outside option *credible* in a way notice-and-consent does not. A
machine-readable term set can be presented to more than one counterparty, and a
subject-side aggregator (Section 5.3 of the draft) gives the subject an alternative
route to realise value; the subject can therefore credibly withhold or multi-home.
Her outside option $h_X$ is now non-negligible. We take the two outside options to
be roughly symmetric and *non-binding* (each below its holder's inside share); by
the outside-option principle they then set the threat points but do not pin the
split, which is governed by the bargaining powers. The disagreement point of the
continuation game is the inside disagreement (perpetual delay), value $0$ to each,
with $h_X, h_M$ entering only as non-binding threats.

**Derivation.** With X proposing first, the subgame-perfect share of X is
$x^{*}_X = (1 - \delta_M)/(1 - \delta_X \delta_M)$, which is interior for any
$\delta_X, \delta_M \in (0,1)$. In the frictionless limit ($\Delta t \to 0$),
the first-mover advantage vanishes and
$$
s_{\text{sovereign}} \longrightarrow \beta = \frac{\rho_M}{\rho_X + \rho_M}
\in (0,1),
$$
an interior share equal to X's bargaining power.

**The interval $[0.3, 0.7]$ as a projection from the solution, not a guessed
band.** The interior share is $s = \beta$. The sovereign interval carried in the
S5 patch and the v2 note is the image of $\beta$ over a bounded, roughly symmetric
range of relative patience:

| $\beta = \rho_M/(\rho_X+\rho_M)$ | relative patience | $s_{\text{sovereign}}$ | reading |
|---|---|---|---|
| $0.5$ | $\rho_X = \rho_M$ (symmetric) | $0.5$ | symmetric Nash split |
| $0.3$ | $\rho_X \approx 2.3\,\rho_M$ (X less patient / weaker) | $0.3$ | counterparty-favourable |
| $0.7$ | $\rho_M \approx 2.3\,\rho_X$ (X more patient / stronger) | $0.7$ | subject-favourable |

So $s_{\text{sovereign}} \in [0.3, 0.7]$ is exactly the set of Nash splits when
neither party is more than roughly $2.3$ times as impatient as the other. This is
a *bargaining projection* with a stated precondition (relative patience bounded
within that ratio), not a measured band and not a guessed one. Wherever the
interval appears it is labelled a projection: no deployed sovereignty market has
been observed to price $s$ (draft Section 6; GR-8). The endpoints $0.3$ and $0.7$
are the S5 patch's "counterparty-favourable" and "subject-favourable" cells, now
supplied with the parameter ($\beta$, hence the patience ratio) they are the image
of.

**What drives the result.** The share moves off the floor for two mutually
reinforcing reasons, both supplied by the interface: (i) the extensive form now lets X propose,
removing the pure-ultimatum appropriation of interface (a), and (ii) the credible
outside option means M cannot drive X below her threat point. Neither reason is a
change in X's preferences; both are changes in the protocol. This is again the
mechanism reading.

---

## 6. The two comparative-statics directions, together

Holding the pie and the (near-symmetric) fundamentals fixed and varying only the
interface:

$$
\text{notice-and-consent} \;\Longrightarrow\; s = h_X \approx 0,
\qquad
\text{7012 propose-and-respond} \;\Longrightarrow\; s = \beta \in [0.3, 0.7].
$$

The move from the first to the second is the appropriation gap of draft
Section 5.1: a shift of the subject's share from order $10^{-4}/10^{-5}$ to order
$10^{-1}$, expressed always as a change in a dimensionless share and never as a
ratio to a near-zero base. Both directions are subgame-perfect equilibria of one
model; the only thing that changed between them is the extensive form the
interface imposes.

---

## 7. Minor m1: the disposition of M(u,y). Use, do not cut.

**Decision: use it, as a gate on the realised share.** The market-maturity factor
M(u,y) is integrated into P1 rather than cut, because doing so discharges the
"decoration / unidentified free parameter" charge by *use* rather than by
deletion, and because the resulting comparative static is genuinely load-bearing:
it is what separates the sovereign *bargaining ceiling* from the sovereign
*realised* share.

**The comparative static.** The bargaining share $s$ of Sections 4 and 5 is the
share the subject would capture *conditional on a counterparty able to price
sovereignty being at the table*. Whether such a counterparty exists, and whether
the market is deep enough to clear, is exactly what M(u,y) gates. So the realised
share is the product
$$
s_{\text{realised}} = M(u,y)\, s, \qquad M(u,y) \in [0,1],
$$
with $u$ the fraction of counterparties able to accept a 7012 proposal and settle
against a subject-side aggregator, and $y$ market depth. Then, using the boundary
behaviour of the proposed form $M(u,y) = u\,(1 - e^{-y/\tau})$:

- $\partial s_{\text{realised}}/\partial u > 0$ and
  $\partial s_{\text{realised}}/\partial y > 0$: the realised subject share rises
  with market participation and with market depth. This is a testable directional
  prediction and is the operational content the draft's open item ("estimate
  M(u,y) and its time constant $\tau$ from an operating market") would settle.
- $u \to 0 \Rightarrow M \to 0 \Rightarrow s_{\text{realised}} \to 0$
  irrespective of the interface. This gives the extraction regime a *second*,
  market-structural reason for the near-zero share, independent of the
  bargaining-protocol reason of Section 4: today no counterparty prices
  sovereignty, so $u \approx 0$ and $M \approx 0$, and the subject captures
  near-zero even of a bargaining share she might in principle win.
- $u \to 1,\ y \to \infty \Rightarrow M \to 1 \Rightarrow s_{\text{realised}}
  \to s = \beta \in [0.3,0.7]$: the interval $[0.3,0.7]$ is therefore the mature,
  deep-market *ceiling* on the realised share, approached but not promised.

**Honesty label preserved (GR-8).** M(u,y) remains this paper's own proposal:
the functional form is chosen for its boundary behaviour and $\tau$ is
unestimated. Using it does not strengthen any claim; it *weakens* the sovereign
result in the correct direction, converting $[0.3,0.7]$ from a promise into a
maturity-gated ceiling, and it makes the extraction regime's near-zero share
overdetermined (protocol and market-maturity both push it to zero) rather than
resting on the protocol alone. The claim "realised share is the bargaining share
gated by market maturity" is what is asserted; no value of $M$ or $\tau$ is
asserted.

---

## 8. Minors m2 and m3: P4, Assumption A1, and the shadow exchange rate

### 8.1 m2: P4 discharges A1, conditionally, and this is a synthesis to foreground

**The two objects.** Assumption A1 is a precondition of the imported guarantee
(E2-C01, Precondition 1): the boundary agent S and the delegation agent M do not
pool the context each holds, formally the conditional-independence condition
$I(Y_S; Y_M \mid X) = 0$ with no third channel carrying the inter-agent residue.
A1 is a statement about *behaviour*. Proposition P4 is a statement about
*incentives*: under two domain-scoped units of account with no exchange between
them (protection-domain earnings buy only protection tooling, delegation-domain
earnings buy only delegation tooling), maintaining the separation is the
earnings-maximising strategy, whereas a single unified unit makes context-pooling
earnings-maximising (E4-C11).

**The relationship.** P4 is a *sufficient condition for A1 to hold as an
equilibrium*. It supplies the economic reason that A1 is an assumption one may
reasonably make rather than a hope: under the two-unit no-exchange design,
rational agents *choose* non-collusion, so $I(Y_S; Y_M \mid X) = 0$ is an
equilibrium property, not an exogenous stipulation. In this precise sense P4
*discharges* A1. This is a genuine synthesis and should be foregrounded: the
guarantee's behavioural precondition is underwritten by the mechanism-design
proposition, so the paper is not assuming what P4 pretends to prove; it is proving
(conditionally, see 8.2) the assumption the guarantee needs.

**Scope of the discharge (GR-7, load-bearing).** P4 discharges A1 *only*. It does
not touch Assumption A2 (fixed adversary class), the capacity-deficit condition
$C_S + C_M < H(X)$ that E2-C01 requires in addition for the strict bound
$R_{\max} < 1$, or Assumption A3 (time-indexing). Those are independent of the
agents' incentives. In particular, even with A1 fully discharged by a holding P4,
the residual $R(t)$ still rises as the adversary's background information
accumulates against the fixed archive (the erosion clock of Assumption A3, the
drift living in the residual entropy $H(X \mid B_t)$, not in any weakening of the
certificates) and the shelf life
$t^{*}$ is still finite: P4 secures the *non-collusion* precondition, not the
*durability* of the guarantee. The asset still has a term structure. Nothing in
this synthesis converts the imported guarantee into a static ceiling, and the
retired sentence "mathematical guarantees collapse" is not reintroduced.

### 8.2 m3: the shadow-exchange-rate objection, and the threshold that answers it

**The objection.** Two domain-scoped units that both buy real tooling are fungible
in practice through a shadow exchange rate; a secondary market that converts
protection-domain value into delegation-domain value defeats the "no swap pool"
premise, and if the tokens are effectively fungible the incentive to pool context
returns. The premise carries the whole of P4, and asserting "there is no exchange
pool" as a binary fact is empirically fragile: anything with value tends to
develop a shadow rate.

**The resolution: replace the binary premise with a threshold.** The honest and
more defensible statement is not "no exchange pool exists" but "the effective
conversion friction between the two domains is high enough that pooling context is
not earnings-maximising net of conversion cost". Formally, let colluding (pooling
context) generate an additional joint surplus $\Delta > 0$, realised as a mix of
the two domain units, and let $\phi$ be the shadow exchange rate net of conversion
friction (units of delegation-value obtainable per unit of protection-value).
Non-collusion is the best response, and hence A1 is discharged, exactly when the
shadow-rate-converted collusion surplus fails to exceed the separation earnings:

$$
\text{P4 discharges A1} \iff \Phi(\phi)\,\Delta \;<\; \kappa,
$$

where $\Phi(\phi) \in [0,1]$ is the fraction of the collusion surplus each agent
can actually realise in its own domain's numeraire at shadow rate $\phi$ (with
$\Phi(0) = 0$ under strict no-exchange and $\Phi \to 1$ as the shadow market
becomes frictionless), and $\kappa$ is the earnings margin the agent forgoes by
colluding. Under strict no-exchange ($\phi = 0$, $\Phi = 0$) the condition holds
trivially and P4 is exactly the draft's proposition. As the shadow market becomes
liquid ($\Phi \to 1$), the condition fails once $\Delta \geq \kappa$, and the
collusion incentive P4 was meant to remove returns.

**What this buys, and what it concedes (GR-8).** It converts P4's premise from a
fragile binary into a stated threshold that is (i) more defensible (it does not
claim the impossible, that no shadow rate can ever form), (ii) testable (the
conversion friction and the collusion surplus are, in principle, measurable design
quantities), and (iii) honest about the objection: *a sufficiently liquid shadow
exchange rate reintroduces the collusion incentive, and in that case P4 does not
discharge A1 and the guarantee's non-collusion precondition reverts to a bare
assumption*. This last clause is reported with equal prominence: the two-token
design underwrites A1 only to the extent the two domains are kept frictionally
separate, and keeping them so is a design obligation, not an automatic property.
It becomes an open item, of the same kind as the Sybil-resistance conjecture:
bound the conversion friction $\Phi(\phi)$ against the collusion surplus $\Delta$,
or concede that A1 is assumed independently.

---

## 9. Assumptions, collected

- **A-P1-1 (pie is the data surplus).** The normalised pie is the appropriable
  per-subject per-period data-derived surplus, not the subject's total welfare;
  free-service consumption value is a separate object (m6), carried as the upper
  allowance on $h_X$.
- **A-P1-2 (interface = extensive form).** The consent interface fixes the first
  proposer and the number of rounds; the pie and the outside options are held
  fixed across interfaces.
- **A-P1-3 (extraction outside option).** Under notice-and-consent X's outside
  option is exclusion from the service, realising only the atomised broker price,
  so $h_X \approx 0$ as a share of the appropriable surplus.
- **A-P1-4 (sovereign outside options).** Under 7012 the outside options are
  credible, roughly symmetric, and non-binding (each below its holder's inside
  share), so the split is governed by bargaining powers via the outside-option
  principle.
- **A-P1-5 (bounded relative patience).** In the frictionless limit the subject's
  share is $\beta = \rho_M/(\rho_X + \rho_M)$; the interval $[0.3,0.7]$ is the
  image of $\beta$ under relative patience bounded within a factor of about
  $2.3$. Outside this range the projected interval widens, and the paper does not
  claim a value of $\beta$.
- **A-P1-6 (maturity gate).** Realised share is $s_{\text{realised}} = M(u,y)\,s$;
  M(u,y) is a proposal, $\tau$ unestimated.

---

## 10. What is not claimed (GR-8)

- The sovereign interior share $s \in [0.3,0.7]$ is a bargaining projection, not a
  measurement. No deployed sovereignty market has been observed to price $s$.
- The extraction result is a comparative static of the extensive form, not a claim
  that behavioural data is worth little; the surplus $1$ is by hypothesis
  appropriable and positive.
- P4 discharges A1 (non-collusion) only, and only under the conversion-friction
  threshold of Section 8.2; it does not discharge A2, the capacity-deficit
  condition, or A3, and it does not make the imported guarantee static. $R(t)$
  still rises, $t^{*}$ is still finite.
- A liquid shadow exchange rate between the two token domains reverts A1 to a bare
  assumption. Whether the friction is high enough is an open, design-dependent
  question.
- M(u,y) is used but not identified; the maturity ceiling $[0.3,0.7]$ is
  approached only as $u \to 1$, $y \to \infty$, and equals the *realised* share
  only in that limit.

---

## 11. Handoff

- **A2 (prose port).** Replace the draft's Proposition P1 "Basis and obligation"
  paragraph with Section 0's statement plus a compressed prose version of Sections
  4-6. Add one sentence to Section 5.3 tying the realised share to M(u,y) per
  Section 7. In Section 3, promote the m2 synthesis: state that P4 discharges A1
  under the Section 8.2 threshold, and that the discharge is of A1 only. Do not
  port any value of $\beta$, $M$, or $\tau$.
- **A4 (bib).** Add Rubinstein (1982, Econometrica); Binmore, Rubinstein and
  Wolinsky (1986, RAND J. Econ.); Nash (1950, Econometrica); Sutton (1986, Rev.
  Econ. Stud.); Osborne and Rubinstein (1990, *Bargaining and Markets*). IEEE
  7012-2025 already listed.
- **A5 (re-review).** M1 is discharged: P1 is one model, explicit disagreement
  and outside-option points per interface, both comparative-statics directions
  derived, the interior interval tied to a bargaining-power parameter. m1, m2, m3
  resolved here; m6 scoped in Section 2. M2 (property literature), M3 (WP-07
  citability and the R(t) schedule), M5 (the ordinal), and m4/m5/m7 remain for
  their owners.
- **A0 / ledger.** Propose an entry recording: P1 derived (model = Rubinstein
  alternating-offers, Nash as its frictionless limit); m1 disposition = use
  (realised = M(u,y) x bargaining share); m2 = P4 discharges A1 only, conditionally;
  m3 = binary no-exchange premise replaced by a conversion-friction threshold, with
  the honest reversion clause. No canon conflict; no register conjecture invented,
  renumbered, or promoted.
