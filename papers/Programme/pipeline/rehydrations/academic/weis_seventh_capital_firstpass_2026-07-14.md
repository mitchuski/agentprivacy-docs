---
tier: A
venue: WEIS-2027
wp: WP-14
status: SUPERSEDED LINEAGE (preserved first pass, 2026-07-14; the live draft is
  weis_seventh_capital.md, draft-v4 as of 2026-07-16). Do not cite or quote this
  file as current. Known pre-ruling claims it still carries and the live draft
  has retired (checklist A3, ledger L141/L148) - raw stock "can hold, invest in,
  compound, and transfer" and the "wedge capture" framing (rentier reframe, L134);
  frontier-capability drift wording (two-clock re-type, L145/L146). Kept on disk
  as lineage only.
date: 2026-07-14
thrust: T3 (Value and Governance / economics)
anonymisation: >
  Non-anonymised first pass (2027 CFP not yet published; A13 re-checks
  2026-11-01). Structured so that names and first-person self-citation swap
  to third person is a later mechanical pass, not a rewrite.
role: A2 (register-translator; first-pass prose port of the A12 skeleton and
  methodology note). Downstream: A3 (M(u,y) and theorem legs), A4 (bib), A5
  (economist referee), A7/A8 (polish).
extraction_basis: E4-seventh-capital C01..C12; companion
  weis_valuation_methodology_note.md; imported guarantee WP-07 (cited, not
  re-proven).
---

<!-- ============================================================
A2 TRACE MARKERS (pipeline internal; strip at release). Each section carries
the E4 claim IDs and their STATUS so a downstream role can audit that no claim
exceeds its extraction status (role A2 definition of done). Legend:
  C55  = register conjecture, confidence "architectural", status occupied
  C42  = register conjecture, active (Sybil-resistance stake)
  C95  = register conjecture, active (evidence-graph anti-score)
  C11  = register conjecture, active (behavioural density / maturity)
  C66  = register conjecture, active (reading not authority)
  DA   = design-assumption (E4)
  EE   = empirical-external
  CON  = contested / fenced (GR-3), rebuilt per methodology note
No confidence percentages appear in asserted prose (GR-2, tier A). Fenced
figures (678x, 31,000x, 70:1, 74x, any fiat) appear nowhere (GR-3). Any
reconstruction/ceiling statement carries preconditions and R(t) in-passage
(GR-7). The imported guarantee is WP-07's, cited not re-proven.
============================================================ -->

# Behavioural Data as a Seventh Capital Class, and the Architecture that Prices It

*Working paper, first pass. Prepared for WEIS 2027 (Thrust T3, Value and
Governance). Format-free venue; written for the security economist and the
economist of data markets, not for the cryptographer. The one
information-theoretic result the argument rests on is imported from a
companion technical paper and cited, never re-proven here.*

---

## Abstract

<!-- carries C01, C03, C04(rebuilt), C10, C11(sep) -->

Behavioural data, the record of what a person attends to, for how long, asks,
and declines to do, is treated in this paper as a distinct capital class: a
stock that yields returns, compounds, can be invested, and transfers across
contexts. We take the position, against both the incumbent treatment of that
stock as capital owned by the observing firm and the data-as-labour proposal
that would price it as a wage, that it is a capital class the data subject
owns. The subject nonetheless captures a near-zero share of the surplus the
stock generates. We argue this share is not a preference or an accident but the
equilibrium of a bargaining game whose rules are the consent interface:
notice-and-consent is a take-it-or-leave-it offer whose outside option is
exclusion from the service, and it drives the subject's share toward zero,
while a bilateral propose-and-respond protocol (instantiated by IEEE Std
7012-2025) inverts the offer direction and moves the share into an interior
bargaining regime. We replace two magnitudes that circulate in the
project's own prior essays, and which we decline to reproduce as measured
facts, with a valuation methodology in which every number carries its
assumptions in the same table: a bounded surplus-appropriation share and a
non-identified but positive and super-additive aggregation wedge, both
reported as ranges. We name the market mechanism, consent-interface bargaining,
a subject-side aggregator, and a non-transferable quality stake, through which
the value is realised for the subject or lost to the observer. Finally we make
precise the sense in which the stock is non-depreciating in the subject's
hands: it rests on an architectural separation of an observing boundary agent
from an acting delegation agent, whose guarantee is information-theoretic
rather than a policy promise, is imported here from a companion paper, and is
time-indexed: it holds against a fixed adversary class under non-collusion and
degrades on a computable schedule R(t). The sovereignty this architecture
protects therefore has a market price, and that price is currently paid to
someone else. We report the negative results, the unidentified wedge, the
unmeasured appreciation claim, the open Sybil-resistance conjecture, with the
same prominence as the positive ones.

---

## 1. Introduction and contributions

<!-- carries C01, C03, C04, C10; forward-ref C11(sep) -->

Consider the position of an implementer building a data market, not that of a
framework author. Two facts about deployed personal-data markets are hard to
dispute. First, behavioural data is valuable: firms that aggregate and model it
earn returns on it, and those returns are large. Second, the person whose
behaviour produced the data captures almost none of that value. The standard
readings of the second fact are that the subject does not care about privacy
(contradicted by stated preferences), or that the data is worth little at the
margin (true of an atomised record, false of the aggregate), or that the
subject has agreed to the arrangement (true only in the thin sense that she
clicked accept).

This paper takes a mechanism view of the second fact. The subject's share of
the surplus is the equilibrium of a bargaining game, and the rules of that
game are set by the interface through which consent is expressed. Under
notice-and-consent the subject faces a take-it-or-leave-it offer whose only
outside option is exclusion from the service. A bargaining model with an
outside option that weak has an equilibrium subject share that tends to zero.
The near-zero share is not evidence that the data is worthless; it is the
predicted outcome of the interface. Change the interface and the prediction
changes.

The change we study is a bilateral propose-and-respond protocol in which the
subject proposes terms and the counterparty accepts, negotiates once, or
declines. This structure is now a published standard, IEEE Std 7012-2025,
Machine Readable Personal Privacy Terms. It inverts the direction of the offer
and, when paired with a credible outside option and a way to signal quality,
moves the subject's equilibrium share off the floor and into an interior range.

For that repricing to be worth anything, the stock being priced must be
defensible: the value of a data subject's sovereignty over her behavioural
record collapses if an observer can reconstruct the record anyway. We therefore
rest the economics on an architectural claim, that an observing boundary agent
S and an acting delegation agent M can be structurally separated so that S
never accumulates the context M holds, with structural context erasure between
agent invocations. The information-theoretic content of that separation, a
bound on what S can reconstruct about the subject, is developed and proved in a
companion technical paper (WP-07). We import it, cite it, and never re-prove
it. What matters for the economics is stated once, plainly, and always in the
same breath as its preconditions: the guarantee holds against a fixed adversary
class under non-collusion, and it is time-indexed. The reconstruction residual
R(t) is not a static ceiling; it degrades on a schedule as adversary capability
grows. A guarantee that expires is exactly what makes the associated
sovereignty an asset with a term structure rather than a promise.

**Contributions.** This paper contributes:

1. A capital-class formalisation of behavioural data, with its five properties
   (returns, compounding, investability, opportunity access, cross-context
   transfer) restated as measurable predicates rather than metaphors
   (Section 3).
2. A valuation methodology that replaces two magnitudes from the project's
   prior essay lineage, which we do not reproduce as measured facts, with a
   bounded surplus-appropriation share and a non-identified, positive,
   super-additive aggregation wedge, every assumption carried in the same
   table as the quantity it feeds and all sensitivity expressed as ranges
   (Section 5).
3. A market mechanism, consent-interface bargaining, subject-side aggregation,
   and a non-transferable quality stake, through which the sovereignty value is
   realised for the subject or lost to the observer (Sections 4 and 5).
4. A statement of the architectural guarantee as imported, time-indexed, and
   expiring, together with the economic reading of its expiry: the asset has a
   term structure (Sections 3 and 6).

No claim in this paper is strengthened to make the argument flow. Where a
quantity is not identified we say so; where a directional claim is unmeasured
we label it a conjecture and name the measurement that would settle it.

---

## 2. Related work: positioning inside three literatures

<!-- carries C02 (corrected against IIRC); positions C01, C03 -->

The thesis sits at the intersection of three literatures, and its contribution
is best seen as a specific move within each rather than a departure from all
of them.

**The economics of privacy.** Acquisti, Taylor and Wagman (2016) establish that
privacy is jointly cost- and benefit-bearing, that the value of personal data is
context-dependent, and, decisively for this paper, that data value is
aggregation-dependent: the same records are worth little atomised and much in
combination. Acquisti, John and Loewenstein (2013) measure the gap between what
individuals will accept to disclose and what they will pay to protect, a
willingness-to-accept over willingness-to-pay endowment ratio that is the
demand-side signature of the appropriation problem. We use these as the
measured anchors of our valuation (Section 5) and inherit their framing: the
subject values her own data above the price the market pays her for it, and the
gap is structural.

**Data as labour versus data as capital.** Arrieta-Ibarra, Goff,
Jimenez-Hernandez, Lanier and Weyl (2018) and Posner and Weyl (2018) argue that
behavioural data should be treated as labour, remunerated by something like a
wage, against the incumbent treatment of it as capital owned by the firm;
Lanier (2013) frames the same intuition as data dignity. Our position is a
deliberate third one, and the tension is the paper's clearest point of contact
with the literature, so we state it rather than eliding it. We agree with the
data-as-labour camp that the returns to behavioural data are misappropriated.
We disagree on the remedy. The data-as-labour proposal keeps the stock in the
firm's hands and compensates the subject for a flow of contributions; our
proposal reassigns ownership of the stock to the subject and treats her return
as a return on owned capital, not a wage. The distinction is not merely
rhetorical. A wage is priced per contribution and stops when the contribution
stops; an owned, non-depreciating stock yields as long as it is held and can be
invested, compounded, and transferred. The seventh-capital framing is the claim
that behavioural data has the second character, not the first, provided an
architecture exists that keeps the stock from depreciating in the subject's
hands. That proviso is the whole of Section 3 and Section 6.

The framing extends an existing capital taxonomy. Integrated-reporting practice
recognises six capitals. We state the enumeration correctly, from the source:
the International Integrated Reporting Council's International Framework lists
Financial, Manufactured, Intellectual, Human, Social and Relationship, and
Natural capital. (An earlier internal enumeration in the project's own
whitepaper lineage diverged from this list; the divergence is corrected here
and is not repeated.) Behavioural sovereignty is proposed as a seventh entry
in that reference frame. In the project's conjecture register this thesis is
carried as an occupied, architectural-class conjecture (C55); we state it here
as a thesis with a proof obligation, not as a settled result, and the whole of
Section 3 is the attempt to make its five capital properties precise enough to
be tested.

**Personal-data-market design and its failures.** Spiekermann, Acquisti, Bohme
and Hui (2015) catalogue why personal-data markets fail: asymmetric
information, externalities, and adverse selection. Anderson (2001) and the WEIS
tradition read information-security and data markets through Akerlof's (1970)
market for lemons: when a buyer cannot distinguish high-quality consented fresh
data from noise, the market unravels. This literature is the one the paper most
directly answers. We do not restate that data is valuable; we take the field's
diagnosis of market failure and propose an architectural repair with three
parts (Section 4): the structural separation whose guarantee is imported and
time-indexed, a non-transferable Sybil-resistant quality stake, and a
propose-and-respond bargaining protocol. The claim to novelty is not the
observation that these markets fail but the mechanism proposed to make one
clear.

---

## 3. Model and preliminaries

<!-- carries C01 (properties made precise), C03 (two regimes of s), C05 (M defined, proposed), C06/C42 (stake defined), GR-7 preconditions as numbered assumptions -->

We fix vocabulary and define every economic object before it is used.

**Agents and the data subject.** Let X be the data subject. Two agents act on
her behalf or upon her. The *boundary agent* S observes and mediates: it is the
surface through which the subject is watched and through which requests to
disclose reach her. The *delegation agent* M acts: it carries out tasks the
subject delegates. The architectural claim, developed in the companion paper
and imported here, is that S and M can be separated so that S does not
accumulate the task context M holds, and that context is erased between agent
invocations (structural context erasure). The subject's behavioural record is
the object both agents could in principle reconstruct; the separation bounds
what the observing side can.

**The appropriable surplus and the subject share.** Normalise the appropriable
data-derived surplus attributable to one subject over one period to 1. The
subject captures share $s \in [0,1]$; the counterparty captures $1-s$. The
share is dimensionless by construction, which is why the valuation that follows
can be stated entirely in shares, wedges, and ratios without any monetary
figure. We will speak of two regimes: an *extraction* regime, in which the
consent interface drives $s$ toward zero, and a *sovereign* regime, in which a
bilateral protocol moves $s$ into an interior range. These are two regimes of
the same variable, not two variables.

**The aggregation wedge.** Let $w$ denote the ratio of the value of
aggregated-and-modelled behavioural data to the value of the same data
atomised in broker markets. Aggregation of behavioural data is super-additive
(Acquisti, Taylor and Wagman 2016), so $w$ is greater than one, positive, and
large; we will argue for its sign and its super-additivity and give an
order-of-magnitude interval, and we will decline to give it a point value,
because a single value silently fixes a dataset composition, a model class, and
a counterfactual buyer that the data do not identify.

**The market-maturity gate.** The project's value equation carries a
multiplicative market-maturity factor, written $M(u,y)$, that gates realised
value: no market able to price sovereignty, no value captured, however large
the potential. In the source material this factor has a name and a role but no
functional form, domain, or units. We therefore propose an operationalisation
as this paper's own construction, to be reviewed before it is treated as
settled, and we label it a proposal rather than an established definition.
Proposed: $M : [0,1] \times \mathbb{R}_+ \to [0,1]$, dimensionless, with
$u \in [0,1]$ the market participation (the fraction of counterparties able to
price sovereignty, that is, able to accept a 7012 proposal and settle against a
subject-side aggregator) and $y \in \mathbb{R}_+$ a measure of market depth
(time-in-operation or liquidity). A candidate form with the required boundary
behaviour is
$$M(u,y) = u\,\bigl(1 - e^{-y/\tau}\bigr),$$
monotone non-decreasing in both arguments, valued in $[0,1]$, with
$M(0,y)=0$ (no participation, no capture) and $M(u,y)\to u$ as depth grows
($\tau>0$ a market-formation time constant). Realised value is
$M(u,y)$ times potential value. The purpose of the form is to give $M$ the
domain, units, and monotonicity the equation needs, so that the argument can
use it without inventing argument semantics silently; the specific form is a
proposal, and any form with the same boundary behaviour would serve.

**The capital properties as predicates.** The seventh-capital thesis claims
behavioural sovereignty has five properties of a capital form. We restate each
as a predicate that could in principle be checked rather than as a metaphor.
(i) *Returns*: holding the stock and disclosing from it selectively yields
coordination the subject could not otherwise obtain (the return is
trust-enabled access, not a coupon). (ii) *Compounding*: a reputation built
from prior consented disclosures lowers the cost of the next, so returns
accrue on the accumulated stock. (iii) *Investability*: the separation
architecture is the capital good in which the subject invests to protect the
stock. (iv) *Opportunity access*: the stock gates entry to coordination that
requires demonstrated trust. (v) *Cross-context transfer*: a portable,
subject-held record can be presented across counterparties. These predicates
are stated as the content of the thesis, not as demonstrated facts; Section 6
records which of them remain unmeasured.

**Preconditions of the imported guarantee.** The information-theoretic
guarantee that underwrites the non-depreciation of the stock is imported from
the companion paper. We state its preconditions here as numbered assumptions,
so that later sections can reference them, and so that the guarantee is never
invoked without them (GR-7 discipline).

- **Assumption A1 (non-collusion).** The boundary agent S and the delegation
  agent M do not collude to pool the context each holds.
- **Assumption A2 (fixed adversary class).** The guarantee is stated against a
  specified adversary class of bounded capability; it is not a claim against
  every possible adversary.
- **Assumption A3 (time-indexing).** The reconstruction residual is a function
  of time, $R(t)$, not a constant. Under A1 and A2 it is bounded below one at
  the time of evaluation and increases as adversary capability grows; the bound
  degrades on a computable schedule.

The threat model of the economics is a passive observer that appropriates
surplus (Sections 4 and 5). The imported guarantee is what prevents that
observer from reconstructing, under A1 and A2 and for the duration that $R(t)$
permits, the record whose sovereignty is being priced.

**The quality stake.** Reputation in the model is grounded in a
non-transferable, non-purchasable proof-of-practice resource earned through
sustained sovereign practice and spent on graph inscriptions. Its defining
economic property is non-transferability: it cannot be minted by fake accounts,
bought to bypass the practice requirement, or moved between accounts. We define
it here as the quality-and-Sybil signal used in Section 4.3 and carry its
Sybil-resistance property forward as a conjecture, not a theorem (register
conjecture C42), with the proof obligation stated where it is used.

---

## 4. Results: economic propositions

<!-- P1 carries C04,C10; P2 carries C04; P3 carries C06/C42; P4 carries C11(sep); P5 carries C07(DA). No confidence bands (GR-2). GR-7 in P4. -->

We state the economic results as propositions, each with its preconditions.
Where a proposition rests on a register conjecture we say so and give the proof
obligation and the unstarted step; we attach no confidence band to any of them
(tier-A discipline). The information-theoretic guarantee itself is not among
these propositions: it is imported from the companion paper and cited.

**Proposition P1 (the appropriation share is set by the interface).** Under a
consent interface that offers the subject a take-it-or-leave-it choice whose
outside option is exclusion from the service, the subject's equilibrium
bargaining share $s$ tends to zero. Under a bilateral propose-and-respond
interface that supplies a credible outside option, $s$ moves into an interior
range.
*Basis and obligation.* The two directions are the comparative statics of a
standard bargaining model (Nash bargaining with outside options, or the
Rubinstein alternating-offers model) applied to the two interfaces. The claim
is a mechanism result, not a moral one: it says the interface, not the
subject's preference, sets the share. The proof obligation is to state the
bargaining model explicitly, fix the outside-option assumption for each
interface, and derive the two comparative-statics directions; the interior
range in the sovereign case is a projection from the bargaining solution, not a
measurement, and is labelled as such wherever it appears (this is the point at
which A3 owns the formal model). The propose-and-respond structure is that of
IEEE Std 7012-2025 (one round maximum, bilateral signed record).

**Proposition P2 (the aggregation wedge is positive and super-additive).** The
value of aggregated-and-modelled behavioural data is super-additive over
atomised records, so the wedge $w$ is greater than one, positive, and bounded.
*Basis and obligation.* The complementarity and network structure of data value
is documented empirically (Acquisti, Taylor and Wagman 2016). We assert the
sign and super-additivity of $w$ and an order-of-magnitude interval only. We do
not assert a point value, and the obligation is precisely to resist the
temptation to let the interval harden into one: the exact wedge depends on
composition, model class, and counterfactual, none of which the available data
identify.

**Proposition P3 (a non-transferable stake resists the Sybil attack that
unravels the market).** A personal-data market fails when a buyer cannot
distinguish high-quality consented data from noise; the failure is
informational (Akerlof 1970; Spiekermann et al. 2015). A non-transferable,
non-purchasable proof-of-practice stake makes the cost of a quality claim equal
to the difficulty of earning the stake, which resists the Sybil attack that
would otherwise flood the signal with cheaply minted identities.
*Basis and obligation.* This is stated as a conjecture (register conjecture
C42), carried with its proof obligation and no confidence band. The cost-to-
forge argument is explicit: non-transferability closes the three cheap paths to
a false signal (mint via fake accounts, purchase, transfer). The unstarted step
is the adversary-regime analysis that would establish that no cheaper path
exists and would bound the residual Sybil advantage; until that step is
discharged the proposition is a candidate repair for the lemons failure, not a
demonstrated one.

**Proposition P4 (the separation is incentive-compatible).** If the two agents
earn in two domain-scoped units with no exchange between them, protection-domain
earnings buying only protection tooling and delegation-domain earnings buying
only delegation tooling, then maintaining the separation of S and M is the
earnings-maximising strategy, whereas a single unified unit would make
information-sharing between the agents earnings-maximising.
*Basis and obligation.* This is a mechanism-design claim with a no-exchange-pool
assumption; the obligation is to state the agents' payoff functions and show
that separation is a best response under the two-unit design and defection is a
best response under the one-unit design. One caution is load-bearing and is
observed here rather than buried: the source material for this proposition also
contains a sentence asserting that under the single-unit design the
reconstruction ceiling "fails" and "mathematical guarantees collapse". That
sentence is stated in the source without its preconditions and without time-
indexing, and it is not imported. The reconstruction guarantee, with
Assumptions A1 to A3 and the schedule $R(t)$, lives in the companion paper and
is cited there; this proposition asserts only the incentive-compatibility of
the separation, not any static statement about reconstruction.

**Proposition P5 (reputation capital appreciates while surveillance data
depreciates).** Reputation built from consistent consented disclosure is
claimed to appreciate over time, while surveillance data depreciates under a
freshness decay.
*Basis and obligation.* This is a directional conjecture, unmeasured, and is
labelled as such (it corresponds to E4-C07, a design assumption in the
extraction, not a register theorem). The supporting argument, that reputation is
hard to forge because it requires simultaneous behavioural consistency, correct
personal-meaning derivation, and narrative continuity across time, is a design
claim, not a proof; forgery is argued to fail on any of the three, but no
measured forgery-cost curve is offered. The measurement that would settle the
proposition is named in Section 6.

---

## 5. Valuation methodology and evaluation

<!-- carries C04 (rebuild lives here), C08 (multipliers illustrative), C09 (anti-score, independent derivation), C12 (compression-as-assessment, ratios fenced). GR-3 throughout: no 678x/31,000x/70:1/1000:1/fiat. -->

This section carries the valuation. Its discipline is that every number appears
in the same table as its assumptions, that measured quantities and projections
are visibly separated, and that no magnitude from the project's prior essay
lineage is reproduced as a measured fact. The evaluation is an analysis of
published measurements, not a new experiment.

Two per-person magnitudes circulate in the project's prior essays: a present-day
per-person value gap, and a larger accessible-volume gap under full behavioural
capture. Neither survives a tier-A rebuild as an asserted point estimate, and we
do not reproduce either. The reasons are structural. A per-person gap of the
form (potential value)/(currently captured value) is ill-posed precisely in the
extraction regime the thesis describes, because the denominator, the value the
subject currently captures, tends to zero, and a ratio to a near-zero base is a
division artefact rather than a measurement. The larger figure was, in the
project's own prior text, already reframed away from an arithmetic ratio and
toward a statement about accessible coordination modes; a quantity its own
source declares non-arithmetic cannot be re-imported as a valuation ratio. We
therefore replace the first magnitude with a share-and-wedge methodology and
retire the second as a number, keeping only the structural claim beneath it.

**5.1 The surplus-appropriation share.** We replace the present-day gap with
the bounded, range-valued share $s$ of Section 3.

| Quantity | Definition | Regime range | Assumptions carried in-table |
|---|---|---|---|
| $s$ (extraction) | subject share of per-subject data surplus under notice-and-consent | near zero | outside option is service exclusion; take-it-or-leave-it consent; no secondary market accessible to the subject; the broker price for an atomised record is the subject's only realisable price and is near zero (Acquisti, Taylor and Wagman 2016) |
| $s$ (sovereign, upper bound; **projection**) | subject share under a bilateral price-posting protocol with a credible outside option | interior, well away from zero | IEEE 7012 propose-and-respond bargaining; roughly symmetric outside options; quality signalled by the non-transferable stake of Section 4.3; **this is a bargaining projection, not a measurement** |
| WTA/WTP endowment ratio | ratio of the price to accept disclosure to the price to pay for protection | small integer multiple (**measured, framing-sensitive**) | Acquisti, John and Loewenstein (2013); the demand-side signature of the appropriation gap; order- and framing-sensitive, hence a range |

The appropriation gap is the movement of $s$ from the extraction range to the
sovereign range: a shift of roughly one order of magnitude in the subject's
captured share, expressed as a change in share and never as a ratio to a
near-zero base. This is the defensible residue of the retired present-day
figure. The single number is not reconstructed and is not claimed.

**5.2 The aggregation wedge.** We replace nothing here; we name the object the
prior high-end figure gestured at and refuse to point-identify it.

| Quantity | Definition | Range | Assumptions carried in-table |
|---|---|---|---|
| $w$ | value of aggregated-and-modelled behavioural data over the same data atomised in broker markets | greater than one, positive, super-additive, bounded; order of magnitude spans a wide interval and is **not point-identified** | complementarity and network effects in data (Acquisti, Taylor and Wagman 2016; OECD 2013); the exact wedge depends on dataset composition, model class, and counterfactual buyer, and a single value fixes all three silently |

The wedge is where the counterparty's surplus originates and is exactly the
object a subject-side aggregator would need to capture. We assert its sign,
super-additivity, and a wide interval; we assert no point. This is the honest
residue of the high-end intuition: the value released by aggregation is large.
It is not the essay figure, and it is not a per-person monetary amount.

**5.3 The market mechanism, instantiated.** The value is lost in the extraction
regime and realised in the sovereign one through three concrete instruments.

- *Price discovery* is the consent interface read as a bargaining protocol
  (Proposition P1): notice-and-consent sets $s$ near zero; IEEE 7012
  propose-and-respond moves it into the interior range.
- *Wedge capture* is a subject-side aggregator. Today the wedge $w$ accrues
  entirely to the firm because only the firm aggregates. A data coalition or
  mediator of individual data, the market instrument of the data-as-labour
  design literature (Arrieta-Ibarra et al. 2018; Posner and Weyl 2018),
  aggregates behavioural streams on the subject side and returns a negotiated
  fraction of the wedge to subjects. We adopt the instrument while taking the
  data-as-capital side of the ownership question (Section 2).
- *Quality signalling* is the non-transferable stake (Proposition P3), the
  candidate repair for the lemons failure that would otherwise unravel the
  market of the first two instruments.

Stated plainly: in the extraction regime the subject's share $s$ is near zero
and the wedge $w$ accrues entirely to the observer, so the sovereignty the
thesis describes has a market price and that price is currently paid to someone
else. This is the home thesis as a mechanism claim, with the mechanism named,
and with no monetary figure and no reproduced ratio.

**5.4 The tier ladder as illustrative parameters.** The model sketches a
reputation ladder in which higher accumulated relationship credentials unlock
higher-value coordination. The specific value multipliers attached to the ladder
in the source are illustrative design parameters with no empirical derivation;
the source itself labels them theoretical projections. We report the compounding
thesis, that privacy enables trust, trust enables higher-stakes delegation, and
higher stakes generate higher returns that attract better opportunities, and we
report the multipliers as illustrative, never as measured returns. No multiplier
value is asserted as an observed rate.

**5.5 The compression-as-assessment mechanism.** The coordination economy is
claimed to be made viable by a compression protocol under which agents exchange
compressed representations with expand-on-demand rather than full records,
driving per-interaction coordination cost toward near-zero while preserving
privacy, and under which compression fidelity is a quantified assessment (in the
Promise Theory sense) that the knowledge-transfer promise was kept. The
extractable claim is the mechanism, compression fidelity read as a measurable
assessment signal. The specific compression ratios attached to the mechanism in
the source are not reproduced here as facts; the mechanism, not any ratio, is
the claim.

**5.6 An independent second-substrate derivation.** An independent build of the
same separation architecture on a different substrate kept the custody split
between the observing and acting sides and dropped the reputation score
entirely, disclosing instead a signed, decomposable evidence graph verified
offline against issuer identifiers, which never computes or emits a tier, score,
or ranking (register conjecture C95, the evidence-graph anti-score). We present
this as an independent derivation, never as a competitor. Its sharper economic
reading is itself conjectural and is carried as such: an emitted reputation
scalar is a computed projection that compresses many underlying facts into a
single rankable handle, correlatable across contexts and accumulable by an
adversary, whereas single-use selective disclosure emits the minimum for one
decision. That the scoreless posture is tighter in leakage terms is a
conjecture whose magnitude is unproven; it rhymes with the register's existence-
leak and reading-not-authority conjectures (C66) but is not a measured result,
and the evidence-graph format travels with its W3C Verifiable Credentials
citation.

---

## 6. Threats to validity

<!-- limits of C04, C05, C07, C08, C06/C42, C02; GR-7 R(t); GR-8 equal-prominence reporting commitment -->

This section gives the negative results the prominence of the positive ones. It
is not a coda; it is a result.

**The valuation is not point-identified.** The surplus-appropriation share $s$
is bounded and its extraction-regime value is defensibly near zero, but its
sovereign-regime value is a bargaining projection, not a measurement: no
deployed sovereignty market has been observed to price $s$. The aggregation
wedge $w$ is asserted only in sign, super-additivity, and an order-of-magnitude
interval; it is not identified, and the paper must not let the interval harden
into a point. Any quantitative reading of the valuation that treats either
quantity as a point estimate is misusing it.

**The market-maturity gate is a proposal.** The functional form given for
$M(u,y)$ in Section 3 is this paper's own construction, chosen for its boundary
behaviour, and is neither established in the source material nor measured. Its
time constant $\tau$ is unestimated. It is presented so that the value equation
can be written down honestly, not because the form is known to be correct.

**Two propositions rest on open conjectures.** The Sybil-resistance of the
non-transferable stake (Proposition P3, register conjecture C42) is an open
conjecture with an unstarted adversary-regime step, not a theorem. The
appreciation-versus-depreciation claim (Proposition P5) is a directional design
conjecture, unmeasured, and the unforgeability argument beneath it is a design
argument, not a forgery-cost measurement. Neither is reported as a settled
result.

**The tier multipliers are illustrative.** The reputation-ladder multipliers of
Section 5.4 are design parameters, not measured returns, and are reported only
as illustrative.

**A reference enumeration was corrected.** The six-capital reference frame the
thesis extends was stated incorrectly in the project's prior whitepaper lineage;
we corrected it against the International Integrated Reporting Council source in
Section 2. The divergence is recorded and flagged for the project's own record;
the seventh-capital thesis is unaffected by it.

**The imported guarantee expires.** The information-theoretic guarantee that
makes the stock non-depreciating in the subject's hands is not a static
property. It holds against a fixed adversary class (Assumption A2) under
non-collusion (Assumption A1), and its reconstruction residual is time-indexed
(Assumption A3): $R(t)$ is bounded below one at the time of evaluation and
degrades on a computable schedule as adversary capability grows. The guarantee
itself is developed and proved in the companion paper and is cited there, not
restated as a ceiling here. The economic consequence is stated plainly: the
asset has a term structure, and a valuation that ignores the schedule
overstates the stock's durability. We do not claim, anywhere, that adversaries
cannot reconstruct the record; we claim a time-indexed, precondition-bound
bound on what they can, sourced to the companion paper.

**Reporting commitment.** A measured result that runs against the predictions of
this paper, for instance a deployed sovereignty market that fails to move $s$
despite a working 7012 protocol and a functioning stake, or an aggregation wedge
that measures far outside the asserted interval, will be reported with the same
prominence as a confirmation. The honesty of the negative result is the moat,
not an embarrassment to be minimised.

---

## 7. Conclusion

<!-- synthesis C01, C03, C04, C10, C11(sep); open items named precisely -->

The argument decomposes into four claims held together conditionally. First,
behavioural data is a distinct capital class: a stock the data subject can hold,
invest in, compound, and transfer, rather than a labour flow priced per
contribution or a firm-owned asset. Second, the subject currently captures a
near-zero share of the surplus that stock generates, and that share is not a
preference but the equilibrium of a bargaining game whose rules are the consent
interface; changing the interface to a bilateral propose-and-respond protocol
moves the share off the floor. Third, the value is realised or lost through a
nameable market mechanism, price discovery through the consent interface, wedge
capture through a subject-side aggregator, and quality signalling through a
non-transferable Sybil-resistant stake, so the sovereignty has a market price
that is currently paid to someone else. Fourth, what makes the stock
non-depreciating in the subject's hands is architectural, an information-
theoretic separation of the observing boundary agent from the acting delegation
agent, imported from a companion paper, holding against a fixed adversary class
under non-collusion, and time-indexed so that it expires on a computable
schedule. The stock is durable to the extent, and for the term, that the
architecture makes it so.

None of the four claims is asserted beyond its evidence. The valuation is a
share and a wedge with ranges, not two magnitudes from the prior essays, which
we declined to reproduce. The market mechanism is buildable but unbuilt. The
guarantee is proved elsewhere and dated. The conclusion is therefore a
decomposition, not a triumph, and the open items are its real content:

- Identify the aggregation wedge $w$ empirically, or bound it more tightly than
  a wide order-of-magnitude interval.
- Estimate the market-maturity gate $M(u,y)$ and its time constant $\tau$ from
  an operating market, and test the proposed functional form.
- Discharge the Sybil-resistance conjecture (C42) with the adversary-regime
  step, or refute it.
- Measure the reputation-appreciation claim (Proposition P5) against a
  forgery-cost curve.
- Observe a deployed sovereignty market and test whether a working 7012 protocol
  and a functioning stake actually move the subject's share $s$.

The paper closes in the decomposed, conditional, and dated form in which its
claims are true. Behavioural data is a seventh capital; the architecture that
would let a subject hold it is specifiable; the guarantee that would make it
worth holding is real, imported, and on a clock; and the price of the
sovereignty it protects is, for now, collected by someone else.

---

## References

*(Handoff to A4: verify each against `templates/submission/references/pv_v6.bib`
and add. IEEE 7012 already in extraction citations; confirm bib key.)*

- Acquisti, A., Taylor, C., Wagman, L. (2016). The Economics of Privacy.
  *Journal of Economic Literature* 54(2).
- Acquisti, A., John, L., Loewenstein, G. (2013). What Is Privacy Worth?
  *Journal of Legal Studies* 42(2).
- Akerlof, G. (1970). The Market for Lemons. *Quarterly Journal of Economics*
  84(3).
- Anderson, R. (2001). Why Information Security is Hard: An Economic
  Perspective. *ACSAC* (WEIS lineage).
- Arrieta-Ibarra, I., Goff, L., Jimenez-Hernandez, D., Lanier, J., Weyl, E.G.
  (2018). Should We Treat Data as Labor? Moving beyond Free. *AEA Papers and
  Proceedings* 108.
- Bergstra, J., Burgess, M. (2019). *Promise Theory: Principles and
  Applications* (2nd ed.).
- International Integrated Reporting Council (2013, rev. 2021). *International
  Framework* (the six-capitals model).
- IEEE Std 7012-2025. *IEEE Standard for Machine Readable Personal Privacy
  Terms* (2026-01-20).
- Lanier, J. (2013). *Who Owns the Future?* Simon and Schuster.
- OECD (2013). *Exploring the Economics of Personal Data*.
- Posner, E., Weyl, E.G. (2018). *Radical Markets*. Princeton University Press
  (chapter on data as labour).
- Spiekermann, S., Acquisti, A., Bohme, R., Hui, K.-L. (2015). The challenges of
  personal data markets and privacy. *Electronic Markets* 25(2).
- W3C (2022). *Verifiable Credentials Data Model 1.1*.

<!-- Companion internal reference (not a public citation): the imported
information-theoretic guarantee, its Assumptions A1-A3, and the schedule R(t)
are developed in WP-07. At release this becomes the appropriate public spec URL
(at most one, per GR-3/tier-A) or a companion-paper citation, at A4's
discretion. -->
