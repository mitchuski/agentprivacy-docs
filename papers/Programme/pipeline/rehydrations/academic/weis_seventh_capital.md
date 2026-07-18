---
tier: A
venue: WEIS-2027
wp: WP-14
status: draft-v4 (2026-07-16 durability-leg revision per L143/L145: the M3 metric
  divergence is RESOLVED by WP-07's erosion leg (Def 3.9 + Cor 5.4b). Assumption A3
  rewritten to the two-clock form with the informed deficit $C_S + C_M < H(X | B_t)$
  and the erosion ratio $R(t) = (C_S + C_M)/H(X | B_t)$ (drift moved from numerator
  to denominator, fixing the S2/Assumption-A3 internal split, L143 finding 2);
  abstract, S1 clock paragraph, S2 companion-proof sentence, S3 inalienability
  passage, and S6 limits re-typed from "frontier/adversary capability grows" to
  background-information accumulation; S6 submission gate updated to resolved form
  (citability remains the gate; metric agreement discharged). LM3 DISCHARGED
  2026-07-16 (L147): the marginal-product falsifier's strength bounded to the
  measured settings (S1 + S2 scope paragraph; directed-not-universal, blunting
  markets reportable per GR-8). A4 full P2 pass + reference interleave still
  open.)
date: 2026-07-16
thrust: T3 (Value and Governance / economics)
anonymisation: >
  Non-anonymised first pass (2027 CFP not yet published; A13 re-checks
  2026-11-01). Structured so that names and first-person self-citation swap
  to third person is a later mechanical pass, not a rewrite.
role: A2 (register-translator; revision loop v2). Applies A3's self-contained
  Proposition P1 derivation (M1), the S5 valuation patch (M4), A12's
  propertization engagement, rent integration and predicate-led retitle
  (M2/M5/M6), and the R(t) schedule with WP-07 submission-gating (M3).
  Downstream: A4 (bib + retitle), A5 (economist re-review), A7/A8 (polish).
extraction_basis: E4-seventh-capital C01..C12; companion
  weis_valuation_methodology_v2_empirical.md (rent finding, L134); E2-moving-ceiling
  C01/C02/C03 (imported guarantee, R(t), the drift); imported guarantee WP-07
  (cited, not re-proven). Derivation inputs wp14_P1_derivation.md (A3),
  wp14_M2_rent_reframe_note.md (A12), weis_seventh_capital_S5_patch.md (A0/A12).
---

<!-- ============================================================
A2 TRACE MARKERS (pipeline internal; strip at release). Each section carries
the E4/E2 claim IDs and their STATUS so a downstream role can audit that no claim
exceeds its extraction status (role A2 definition of done). Legend:
  C55  = register conjecture, confidence "architectural", status occupied (capital-class thesis)
  C42  = register conjecture, active (Sybil-resistance stake)
  C95  = register conjecture, active (evidence-graph anti-score)
  C11  = register conjecture, active (behavioural density / maturity)
  C66  = register conjecture, active (reading not authority)
  DA   = design-assumption (E4)
  EE   = empirical-external
  E2   = moving-ceiling extraction (imported guarantee, R(t), drift C82)
  L134 = Run-3 finalisation (rent finding; super-additivity of raw data REJECTED)
  P1model = Rubinstein (1982) alternating-offers, Nash as its frictionless limit (A3)
  PROP = external propertization literature (Laudon/Samuelson/Schwartz/Purtova/Prins/Delacroix-Lawrence), tier-A permitted (A12)
No confidence percentages appear in asserted prose (GR-2, tier A). Fenced
figures (678x, 31,000x, 70:1, 74x, any fiat) appear nowhere (GR-3); external
dollar anchors are cited by author/year only, never printed. Any
reconstruction/ceiling statement carries preconditions and R(t) in-passage
(GR-7). The word "super-additive" is attached to no surviving surface (L134).
The imported guarantee is WP-07's, cited not re-proven; its citability at
submission is a submission-gating precondition (Section 6).
============================================================ -->

# Behavioural Data as Subject-Owned Capital: Five Predicates and the Architecture that Prices Them

*Working paper, revision v2. Prepared for WEIS 2027 (Thrust T3, Value and
Governance). Format-free venue; written for the security economist and the
economist of data markets, not for the cryptographer. The one
information-theoretic result the argument rests on is imported from a companion
technical paper (WP-07) and cited, never re-proven here; the durability leg of
the thesis is gated on that companion being a real, citable paper at
submission (Section 6).*

---

## Abstract

<!-- carries C01, C03(scoped), C10, L134(rent), P1model, E2 -->

Behavioural data, the record of what a person attends to, asks, and declines to
do, is treated here as subject-owned capital: a stock satisfying the five
defining predicates of a capital form (it yields returns, compounds through
reputation as a conjecture, can be invested in, gates opportunity access, and
transfers across contexts). The framing arose by analogy with the six-capital
integrated-reporting frame, from which the informal "seventh capital" label
derives; that ordinal is provenance only and the argument rests no weight on it.
Against both the incumbent treatment of the stock as firm-owned capital and the
data-as-labour proposal that would price it as a wage, we hold that it is capital
the data subject owns. This is a propertization claim, and we engage the critical
propertization literature directly, answering its two load-bearing objections
(alienability and thin markets) by architecture rather than doctrine. The subject
nonetheless captures a near-zero share of the surplus the stock generates. We
argue this share is the subgame-perfect equilibrium of one bargaining game whose
rules are the consent interface: notice-and-consent is a single-round
take-it-or-leave-it offer whose subject share equals her near-zero outside option
(exclusion from the service), while a bilateral propose-and-respond protocol (IEEE
Std 7012-2025) inverts the offer direction and moves the interior share to the
subject's bargaining power. We replace two magnitudes circulating in the project's
prior essays, which we decline to reproduce, with a valuation carrying every
assumption in the same table: a bounded surplus-appropriation share, and a
non-identified observer-to-broker realised-value gap that the returns-to-scale
evidence attributes to market-position rent rather than to any super-additivity of
aggregated data. We report that rent finding at the prominence of a positive
result: raw behavioural-data aggregation does not compound, so a subject-side
aggregator redistributes a positional rent rather than unlocking latent value.
Finally we make precise the sense in which the stock is durable: it rests on an
architectural separation of an observing boundary agent S from an acting
delegation agent M, whose guarantee is information-theoretic, imported from the
companion paper, and time-indexed. It holds against a fixed adversary class under
non-collusion and, where the declared capacity-deficit condition holds, its
reconstruction residual R(t) is bounded below one at evaluation and rises as the
adversary's background information accumulates against the fixed archive, so the
asset is durable only for a finite, adversary-relative horizon. The sovereignty the architecture protects therefore
has a market price, currently paid to someone else. We report the negative
results, the unidentified rent, the unmeasured appreciation claim, the open
Sybil-resistance conjecture, and the shadow-exchange hazard to the separation's
incentive compatibility, with the same prominence as the positive ones.

---

## 1. Introduction and contributions

<!-- carries C01, C03(scoped), C10, L134; forward-ref predicates -->

Consider the position of an implementer building a data market, not that of a
framework author. Two facts about deployed personal-data markets are hard to
dispute. First, behavioural data is valuable: firms that aggregate and model it
earn returns on it. Second, the person whose behaviour produced the data
captures almost none of that value. The standard readings of the second fact are
that the subject does not care about privacy (contradicted by stated
preferences), or that the data is worth little at the margin (true of an
atomised record, false of the aggregate), or that the subject has agreed to the
arrangement (true only in the thin sense that she clicked accept).

This paper takes a mechanism view of the second fact. The subject's share of the
surplus is the equilibrium of a bargaining game whose rules are set by the consent
interface. Read as the extensive form of an alternating-offers game,
notice-and-consent is an ultimatum game in which the observing counterparty is the
sole proposer, and its unique subgame-perfect outcome hands the subject only her
outside option, near zero because she is not admitted to the venue where
behavioural data clears. That a sole proposer captures almost all the surplus in a
one-shot take-it-or-leave-it game is the textbook ultimatum result (Guth et al.
1982; the one-shot limit of Rubinstein 1982 alternating offers), and formal
data-market models in which an intermediary's bargaining power fixes the consumer's
residual surplus reach the same place (Gu 2024); we claim neither the derivation
nor its direction as new. The near-zero share is not evidence that the data is
worthless; it is the predicted outcome of the interface. Change the interface and
the prediction changes. What the paper takes from this is not the equilibrium but
its application: the subject-side share is written as a structural venue-exclusion
parameter rather than as a taste for privacy, and the reform is a specific
permutation of the proposer role.

The change we study is a bilateral propose-and-respond protocol in which the
subject proposes terms and the counterparty accepts, negotiates once, or
declines. This structure is a published standard, IEEE Std 7012-2025, Machine
Readable Personal Privacy Terms; that inverting the proposer to shift bargaining
power is the standard's own stated purpose. It inverts the direction of the offer
and, when paired with a credible outside option, moves the subject's equilibrium
share off the floor and into an interior range governed by bargaining power rather
than by appropriation.

For that repricing to be worth anything, the stock being priced must be
defensible: the value of a subject's sovereignty over her behavioural record
collapses if an observer can reconstruct the record anyway. We therefore rest the
economics on an architectural claim, that an observing boundary agent S and an
acting delegation agent M can be structurally separated so that S never
accumulates the context M holds, with structural context erasure between agent
invocations. The information-theoretic content of that separation, a bound on what
S can reconstruct, is developed and proved in a companion paper (WP-07), imported
and cited, never re-proven. What matters for the economics is stated with its
preconditions (Section 3, Assumptions A1 to A3): the guarantee holds against a
fixed adversary class under non-collusion, and where a declared capacity-deficit
condition holds its reconstruction residual R(t) is bounded below one at
evaluation. R(t) is not a static ceiling; it is an erosion clock. The archive and
the disclosed budgets are fixed, and the residual rises because the adversary's
background information, its linkage corpus and side priors, accumulates along
calendar time and shrinks the record's residual uncertainty. The companion paper
proves the erosion's form and direction for a declared background model; the rate
of erosion is a register conjecture, not a theorem. The shelf life is therefore
finite and what expires is the informed deficit condition, not the architecture.
A guarantee with a finite, adversary-relative horizon is exactly what makes the
sovereignty an asset durable for a term rather than forever.

Each of the contributions below was put to an adversarial prior-art search, and
each returned the same verdict: the broad object is already owned by named prior
work, and only a narrow residue survives. What the paper defends as novel is
therefore not any single object but the conjunction of those residues held within
one instrument, and it is offered as a candidate that survived a named search
rather than as an empty cell. Two residues are load-bearing. The first is the
pricing of a finite, adversary-relative, time-drifting reconstruction bound R(t)
as inalienable subject-owned capital, with the observer-to-subject value gap
decomposed as market-position rent; this sits beside, and must be distinguished
from, the differential-privacy-markets literature that already prices a disclosure
budget as a commodity. That budget is not adversary-independent: it is calibrated
against a worst-case adversary and accounted along a query and release-composition
clock, whereas R(t) indexes a fixed release to an adversary's informational
capability growing along the calendar horizon, a distinct clock we develop and
scope in Section 2. The second is
a directed internal falsifier of the data-as-labour remedy: in the settings the
returns-to-scale evidence has measured, the marginal product of an additional raw
record is approximately zero at operating scale, so raising the subject's
compensation toward that marginal product self-defeats there, and the
redistributive object is re-specified as venue and clearing-position rent rather
than a wage; the falsifier's scope is exactly the scope of that evidence, stated
in Section 5 (Sections 2 and 5).

**Contributions.** This paper contributes:

1. A capital-class formalisation of behavioural data, with its five properties
   (returns, reputation-scoped compounding, investability, opportunity access,
   cross-context transfer) restated as measurable predicates rather than
   metaphors, and positioned within the critical propertisation literature
   rather than against it (Sections 2 and 3).
2. A valuation methodology that replaces two magnitudes from the project's prior
   essay lineage, which we do not reproduce as measured facts, with a bounded
   surplus-appropriation share and a non-identified observer-to-broker
   realised-value gap that the returns-to-scale evidence attributes to
   market-position rent rather than to super-additive aggregation; the same
   evidence supplies a directed correction to the data-as-labour programme, since
   a marginal product near zero for the raw record leaves no wage to raise, with
   every assumption carried in the same table as the quantity it feeds and all
   sensitivity expressed as ranges (Section 5).
3. A market mechanism, consent-interface bargaining for price discovery, a
   subject-side aggregator for rent redistribution, and a non-transferable
   quality stake for signalling, through which the sovereignty value is realised
   for the subject or lost to the observer (Sections 4 and 5).
4. A statement of the architectural guarantee as imported, time-indexed, and
   finite-horizon, together with the economic reading of its horizon: the asset
   is durable only for a term, and only if the companion paper that proves the
   guarantee is a citable companion at submission (Sections 3 and 6).

**What this paper does not claim.** The adversarial search that shaped the
contributions above also fixed their ceiling, and the boundary is stated here with
the same prominence as the claims. We do not claim to be first to treat personal
data as an ownable asset: propertisation of personal data is a decades-old, and
largely critical, literature (Section 2). We do not claim to be first to price a
privacy or disclosure system property as a market quantity: the
differential-privacy-markets strand prices the disclosure bound as a traded
commodity and occupies that cell already (Ghosh and Roth 2011, and successors). We
do not claim the derivation of the subject's near-zero share as a subgame-perfect
equilibrium; that is the textbook ultimatum result. We do not claim the finite,
adversary-relative durability horizon as a new form; an adversary-relative
shrinking horizon is the structure of Mosca's cryptographic shelf-life inequality
(Mosca 2018), from which our term structure descends only by substituting an
information-theoretic reconstruction bound for the cryptographic break-time clock.
And we do not claim the diagnosis that intermediaries capture the surplus as data
aggregates; that diagnosis is formalised elsewhere (Bergemann, Bonatti and Gan
2022). Each of these broad objects is prior art; what is defended is the narrow
conjunction that sits on top of them.

No claim in this paper is strengthened to make the argument flow. Where a
quantity is not identified we say so; where a directional claim is unmeasured we
label it a conjecture and name the measurement that would settle it; and the one
result that runs against the project's own prior essays, that raw-data
aggregation does not compound, is reported with the prominence of a confirmation.

---

## 2. Related work: positioning inside five literatures

<!-- carries C02 (corrected against IIRC); positions C01, C03; PROP subsection (M2); m5 (WTA/WTP) -->

The thesis sits at the intersection of five literatures, and its contribution is
best seen as a specific move within each rather than a departure from all of
them.

**The economics of privacy.** Acquisti, Taylor and Wagman (2016) establish that
privacy is jointly cost- and benefit-bearing, context-dependent, and
aggregation-dependent: the same records are worth little atomised and much in
combination. Acquisti, John and Loewenstein (2013) measure the gap between what
individuals will accept to disclose and what they will pay to protect. We treat
their willingness-to-accept over willingness-to-pay endowment ratio as consistent
evidence of the appropriation problem, not as its signature: the elicited value
wedge is a small multiple, and a larger participation-proportion ratio in the same
experiment is a ratio of subject shares under two framings, not of valuations, so
we use it only as direction-only corroboration (Section 5.1). The subject values
her own data above the price the market pays her, and the gap is structural.

**Pricing privacy as a system property: the differential-privacy-markets strand.**
The paper prices a property of the release mechanism rather than a subject's
reported impact, so it must sit beside the literature that already prices such a
property as a market quantity, and this is the strand the current framing most
directly answers. Ghosh and Roth (2011) auction a differential-privacy budget,
compensating subjects for a bounded disclosure and deriving an equilibrium price
for it; Li et al. (2013) build a theory of pricing private-data
queries; Fleischer and Lyu (2012) and Cummings et al. (2015) extend the pricing of
privacy loss to correlated and to aggregated-estimation settings. This strand
prices a system property, the disclosure bound, as a traded commodity, so the
claim that no market attaches to a system property does not survive contact with
it, and we do not make that claim. The move from a subject-reported impact
assessment to a quantified system-level metric is likewise not ours to claim:
Wagner and Boiten (2018) already argue that the privacy-impact-assessment tradition
should be replaced by quantified metrics, and we adopt the system-property unit
rather than propose the transition to it. What the paper adds over this strand is a
specific and narrower object, tested against it rather than asserted past it. The
differential-privacy budget priced there is not adversary-independent: it is
calibrated against a worst-case adversary of unbounded computation and arbitrary
auxiliary knowledge, entering the guarantee as a supremum (Mironov 2017; Bun and
Steinke 2016; Dong, Roth and Su 2022), and it carries a genuine temporal axis, with
privacy loss accounted as it accumulates across composed mechanisms (Kairouz, Oh and
Viswanath 2015; Dwork, Rothblum and Vadhan 2010) or across a stream of published
outputs under continual observation (Dwork, Naor, Pitassi and Rothblum 2010);
adversary-aware refinements parametrise which fixed adversary class the guarantee is
calibrated against (Cummings et al. 2024; Swanberg et al. 2025). What that literature
holds fixed is therefore not the adversary but the clock: its temporal axis is added
queries or releases against a held-fixed worst-case adversary. R(t) runs a different
clock. It indexes a single fixed release, never re-queried, whose per-subject
reconstruction residual rises as the adversary's informational capability, its
accumulating linkage corpus and side priors rather than its computational power,
which differential privacy already saturates, grows along calendar time; and that
residual is held as inalienable subject-owned capital that scoped disclosure does not
transfer, with the observer-to-subject value gap decomposed as market-position rent
rather than as super-additive aggregation. The companion paper carries this clock as
proved material rather than as framing: conditioning on the accumulating background
cannot raise the disclosed transcript's leakage above its budget, while the
reconstruction floor erodes through the record's residual entropy given that
background; the protection does not leak more, it matters less. Where differential privacy does run a wall
clock, in age-dependent and temporally-discounted formulations and in the data-value
decay of Valavi et al. (2022), the polarity is opposite: the guarantee strengthens as
data ages through relevance decay. We state this as a clock distinction and not a
categorical barrier, because adversary-aware differential privacy already carries
adversary capability as an explicit static parameter and computational differential
privacy already recognises informally that a fixed release erodes as adversary
capability grows, so a calendar-indexed capability clock is a natural but as-yet
unformalised extension rather than an impossibility. It is that quadruple, the
calendar-time adversary-capability clock, structural inalienability, subject-side
holding, and rent decomposition, and not the pricing of a system property as such,
that the paper defends, and it defends it as the residue that survived a search
against this strand, scoped to that strand.

**Data as labour versus data as capital.** Arrieta-Ibarra et al. (2018) and Posner
and Weyl (2018) argue that behavioural data should be treated as labour,
remunerated like a wage, against the incumbent treatment as firm-owned capital;
Lanier (2013) frames the same intuition as data dignity. Our position is a
deliberate third one, and the tension is the paper's clearest point of contact
with the literature. We agree the returns are misappropriated; we disagree on the
remedy. The data-as-labour proposal keeps the stock in the firm's hands and
compensates the subject for a flow of contributions; ours reassigns ownership of
the stock to the subject and treats her return as a return on owned capital. A
wage is priced per contribution and stops when it stops; an owned, durable stock
yields as long as it is held and can be invested, compounded (reputationally;
Section 3), and transferred. The capital framing is the claim that behavioural
data has the second character, provided an architecture keeps the stock from
depreciating in the subject's hands. That proviso is the whole of Sections 3 and 6.
One point of contact here is sharper than a disagreement over remedy, and it is
stated as a directed correction rather than a fresh claim. The data-as-labour
remedy raises the subject's compensation toward the marginal product of her
contribution through a data-labour cartel. The returns-to-scale evidence we rely on
in Section 5 (Bajari et al. 2019 and the wider finding that data is not the new
oil) indicates that the marginal product of an additional raw record is
approximately zero at the scale where these markets operate, so there is no wage
to raise and the remedy self-defeats on its own terms. The strength of this
correction is bounded by the strength of that evidence, and we state the bound:
the near-zero finding is measured in a small number of settings (retail demand
forecasting in Bajari et al.; the estimation-task subsample argument in Varian;
broker-profile accuracy in Neumann et al.), each with a specific production
function, and it is an extrapolation, not a theorem, that every market where a
data-labour cartel would bargain has the same diminishing shape. The falsifier is
therefore directed, not universal: it binds wherever the root-N, flat-in-variety
returns shape holds, and a measured market in which the marginal record retains
substantial product would blunt it there and would be reported at the same
prominence as the finding itself. We therefore re-specify the redistributive
object not as a wage but as rent on venue access, and the instrument that
redistributes it, a subject-side aggregator pooling bargaining position, is the
data-union, data-cooperative and consortia programme's device (Arrieta-Ibarra et
al. 2018; Posner and Weyl 2018; Delacroix and Lawrence 2019), imported here rather
than introduced. We offer this correction as a residue that survived a search
against those same programmes, not as a claim that they are unaware of scale
effects.

**Propertisation of personal data, and why the architecture is not just a
property right.** The position that behavioural data is capital *the subject
owns* is a propertisation claim, and propertisation of personal data has a
decades-old and largely critical literature that the framing must answer rather
than restate. Laudon (1996) proposed treating personal information as an owned,
licensable asset traded in a national information market; Samuelson (2000) asked
directly whether privacy could be protected by an intellectual-property-style
right and was sceptical; Schwartz (2004) set out a model of propertised personal
information but only with explicit safeguards, because he took the naive version
to fail; Purtova (2015) and Prins (2006) analysed the European commodification
debate and its hazards; and the data-trust and data-cooperative strand (Delacroix
and Lawrence 2019) proposed fiduciary intermediation as an alternative to
individual ownership altogether. A referee who knows this literature will read
subject-owned capital as a rebranding of propertisation unless the paper says
what it adds. It adds two things, and both are structural rather than doctrinal.

The literature levels three standing objections at propertisation, and we take
each in turn.

*Objection (i): alienability defeats the protection.* A right the subject can
sell is a right she will be pressured to sell; under free alienability the
protection is gone once the data transfers (Samuelson 2000). Schwartz's (2004)
response built *hybrid inalienability* into the right by legal construction. Our
response makes the inalienability *structural*. What the subject discloses is a
scoped, single-purpose disclosure, not a handover of the stock, because the
observing side cannot reconstruct the underlying record from it: S and M are
separated so S never accumulates the context M holds (structural context erasure
between agent invocations), and the residual an observer can reconstruct is
bounded by the guarantee imported from WP-07. That guarantee is not a static
ceiling: it holds against a fixed adversary class (Assumption A2) under
non-collusion (Assumption A1), and where the informed capacity-deficit condition
holds its residual R(t) is bounded below one at evaluation and rises as the
adversary's background information accumulates (Assumption A3). The shape of that horizon, an
adversary-relative term that shortens as adversary capability grows, is not new:
it is the structure of Mosca's cryptographic shelf-life inequality and the
harvest-now-decrypt-later threat model (Mosca 2018), and what the paper substitutes
is an information-theoretic reconstruction bound for that literature's cryptographic
break-time clock, carried into a capital valuation (Sections 3 and 6). Within that
term the asset cannot be fully alienated by disclosure, because disclosure does not
transfer what it cannot reconstruct. Second, the quality stake (Section 4.3) is
*non-transferable by construction*: it cannot be minted by fabricated accounts,
purchased, or moved between accounts (register conjecture C42). This is Schwartz's
inalienability as a property of the object rather than a clause a court must
enforce.

*Objection (ii): thin markets.* Individual data is worth almost nothing atomised,
transaction costs dwarf the per-record price, and no functioning market exists at
the single-subject level. Our valuation confirms the premise and is sharper about
its cause (Section 5): the atomised broker-resale price sits several orders of
magnitude below the observer's realised lifetime capture, and the returns-to-scale
evidence shows this gap is *not* super-additive aggregation the subject could never
replicate. It is market-position rent, the discount a record suffers because the
subject is not admitted to the venue where behavioural data clears (Sections 5.2,
5.3). The diagnosis that the data intermediary captures the total information value
as the number of subjects grows, while each individual captures almost nothing
because her data is informative about others through a social-data externality, is
formalised by Bergemann, Bonatti and Gan (2022); we concede that this rent
diagnosis is anticipated there rather than original to us, and locate the paper's
residue in the directed falsifier of the labour remedy above and in carrying the
diagnosis into the reconstruction-bound frame, not in the diagnosis itself. If the
gap were compounding aggregation value, capturing it would require each subject to
reproduce a platform's aggregation technology. Because it is positional rent,
capturing it requires only pooling *bargaining position*, exactly the function of
the subject-side aggregator, the mediator-of-individual-data, data-cooperative or
data-trust instrument (Arrieta-Ibarra et al. 2018; Posner and Weyl 2018; Delacroix
and Lawrence 2019).

*Objection (iii): distributional regressivity.* Under alienable propertisation the
poor sell privacy cheaply and the wealthy retain it. The structural inalienability
of the reconstruction (objection (i)) means the regressive transaction, alienating
the stock itself for a low price, is not the transaction the architecture supports;
what is priced is scoped disclosure within a retained stock. The fiduciary form
(Delacroix and Lawrence 2019) is designed to redistribute bargaining position
toward those with the least of it. The honest limit: nothing in the architecture
guarantees a non-regressive *distribution* of the rent it redistributes; it changes
who is admitted to the venue, not how the surplus is split once inside, and that
split is the projected sovereign-regime share s (Section 6). We claim the
architecture removes the specific regressive mechanism propertisation is charged
with, forced alienation of the stock, not that it delivers a distributively just
outcome.

Stated as the result of a search rather than as an assertion, the broad claims
gathered here each have named prior owners, and were recorded as anticipated. That
behavioural data can be owned was proposed and criticised long ago; that a
disclosure system property can be priced as a market quantity is the
differential-privacy-markets strand's (Ghosh and Roth 2011, and successors); that
an intermediary captures the surplus as data aggregates is Bergemann, Bonatti and
Gan's (2022); that an adversary-relative horizon shrinks a protection term is
Mosca's (2018). What survived the search is the narrow conjunction that sits across
them: the two objections that sank naive propertisation are answered by structure
rather than doctrine, with structural inalienability of the reconstruction making
full alienation unavailable for the term R(t) permits, and the rent finding,
sharpened by a directed falsifier of the labour remedy, making redistribution a
pooling of bargaining position rather than an unattainable replication of scale.
That conjunction, priced on a finite, adversary-relative, time-drifting
reconstruction bound R(t), is the paper's defensible residue, and it is offered as
a candidate that survived a named prior-art search, not as an empty cell.

**Personal-data-market design and its failures.** Spiekermann, Acquisti, Bohme
and Hui (2015) catalogue why personal-data markets fail: asymmetric information,
externalities, and adverse selection. Anderson (2001) and the WEIS tradition read
these markets through Akerlof's (1970) market for lemons: when a buyer cannot
distinguish high-quality consented fresh data from noise, the market unravels.
This is the literature the paper most directly answers on the design side. We take
the field's diagnosis and propose an architectural repair with three parts
(Section 4): the structural separation whose guarantee is imported and
time-indexed, a non-transferable Sybil-resistant quality stake, and a
propose-and-respond bargaining protocol. The move we defend is not the observation
that these markets fail but the specific mechanism proposed to make one clear.

**The claim is a predicate claim, not an ordinal one.** The substantive thesis is
that behavioural sovereignty satisfies the five defining predicates of a capital
stock, made testable in Section 3: returns, compounding (reputationally and as a
conjecture; raw-data aggregation does not, Section 5.2), investability, opportunity
access, and cross-context transfer. The thesis stands or falls on those
predicates, not on a place in any enumeration. For provenance: the framing arose
by analogy with integrated-reporting practice, which recognises six capitals
(Financial, Manufactured, Intellectual, Human, Social and Relationship, and
Natural, per the International Integrated Reporting Council); an earlier
enumeration in the project's prior lineage diverged from that list and is corrected
here (Section 6). That analogy is the origin of the "seventh capital" label and
nothing more; the reporting taxonomy carries no economic weight. In the project's
conjecture register the thesis is an occupied, architectural-class conjecture
(C55); we state it as a thesis with a proof obligation, its five predicates being
the content.

---

## 3. Model and preliminaries

<!-- carries C01 (predicates made precise), C03 (two regimes of s), C05 (M defined), C06/C42 (stake), E2 preconditions as numbered assumptions, m2 synthesis (P4 discharges A1) -->

We fix vocabulary and define every economic object before it is used.

**Agents and the data subject.** Let X be the data subject. Two agents act on her
behalf or upon her. The *boundary agent* S observes and mediates: it is the
surface through which the subject is watched and through which requests to
disclose reach her. The *delegation agent* M acts: it carries out tasks the
subject delegates. The architectural claim, developed in the companion paper and
imported here, is that S and M can be separated so that S does not accumulate the
task context M holds, and that context is erased between agent invocations
(structural context erasure). The subject's behavioural record is the object both
agents could in principle reconstruct; the separation bounds what the observing
side can. In the bargaining model of Section 4, "M" also names the single
economic counterparty across the table from X; the two uses coincide because the
counterparty is the observing firm carrying both agents.

**The appropriable surplus and the subject share.** Normalise the appropriable
per-subject, per-period *data-derived* surplus to 1. It is explicitly the data
surplus, not the subject's total welfare: the consumption value of any free
service in a zero-price two-sided market is a separate object and is not in this
pie (this scopes the claim and answers the "near zero *net of the service*"
objection, which Section 5.1 carries as the upper allowance on the extraction
share). The subject captures share $s \in [0,1]$, the counterparty $1-s$; the
share is dimensionless, which is why the valuation can be stated in shares, gaps,
and ratios without any monetary figure. We speak of two regimes of the one
variable: an *extraction* regime, in which the interface drives $s$ toward zero,
and a *sovereign* regime, in which a bilateral protocol moves $s$ into an interior
range.

**The realised-value gap.** Let $w_{\text{gap}}$ denote the ratio of the
observer's lifetime targeting-attributable capture per user to the one-time
atomised broker-resale price of a record, both measured as stocks. It is large and
positive. We argue in Section 5.2, on the returns-to-scale evidence, that this gap
is market-position rent (an atomisation discount, a position rent, and lifetime
accumulation) rather than super-additive aggregation value, and we give it an
order-of-magnitude interval and decline a point value. A separate, genuinely
data-value component, the single-record modelling premium $w_{\text{model}}$, is
of order one and saturating, and is not super-additive: no external figure in the
evidence set measures aggregation super-additivity, and the returns-to-scale
record rejects it in the variety dimension (Section 5.2).

**The market-maturity gate.** The project's value equation carries a
multiplicative market-maturity factor $M(u,y)$ that gates realised value: no
market able to price sovereignty, no value captured. In the source it has a name
and a role but no functional form, domain, or units. We propose, as this paper's
own construction to be reviewed before it is treated as settled, $M : [0,1] \times
\mathbb{R}_+ \to [0,1]$, with $u \in [0,1]$ the market participation (the fraction
of counterparties able to accept a 7012 proposal and settle against a subject-side
aggregator) and $y \in \mathbb{R}_+$ market depth. A candidate form with the
required boundary behaviour is
$$M(u,y) = u\,\bigl(1 - e^{-y/\tau}\bigr),$$
monotone non-decreasing, valued in $[0,1]$, with $M(0,y)=0$ and $M(u,y)\to u$ as
depth grows ($\tau>0$ a market-formation time constant). The *realised* share is
$s_{\text{realised}} = M(u,y)\, s$: the bargaining share $s$ of Section 4 gated by
whether a counterparty able to price sovereignty is at the table. The form is a
proposal; any form with the same boundary behaviour would serve, and $\tau$ is
unestimated.

**The capital properties as predicates.** The thesis claims behavioural
sovereignty has five properties of a capital form; we restate each as a checkable
predicate rather than a metaphor. (i) *Returns*: holding the stock and disclosing
from it selectively yields coordination the subject could not otherwise obtain
(the return is trust-enabled access, not a coupon). (ii) *Compounding*: this holds
in one sense and is rejected in another. A reputation built from prior consented
disclosures may lower the cost of the next, so returns accrue on the accumulated
relationship stock; this is a directional conjecture (Proposition P5,
corresponding to a design assumption in the extraction), unmeasured, and carried
as such. Aggregation of the *raw* behavioural record, by contrast, does not
compound: the returns-to-scale evidence shows aggregate data value saturates and
rejects super-additivity in the variety dimension (Section 5.2). The compounding
the thesis relies on is reputational and conjectural, not a super-additivity of
raw data, which the evidence denies. (iii) *Investability*: the separation
architecture is the capital good in which the subject invests to protect the
stock. (iv) *Opportunity access*: the stock gates entry to coordination that
requires demonstrated trust. (v) *Cross-context transfer*: a portable,
subject-held record can be presented across counterparties. These are the content
of the thesis, not demonstrated facts; Section 6 records which remain unmeasured.

**The economic character, in one figure.** The capital class the predicates
describe is land-like, and the analogy is offered as an organising figure whose
every leg is carried elsewhere in the paper as a result or a stated assumption,
not as an argument in itself. Land is the canonical capital asset that yields
rent by position rather than value by aggregation; one cannot make more of it by
piling up more of the same, and the marginal product of one additional unit is
near zero at scale, which is the returns-to-scale finding of Section 5.2. Its
worth is locational, set by what the road connects it to: here the consent
interface is the road, and the value is the appropriation share of Section 4.
Its exposure erodes on a calendar with nothing added to the plot: the archive is
fixed and the adversary's background accumulates, the erosion clock of
Assumption A3. And it is leased, never conveyed: a scoped disclosure transfers a
season's harvest, not the ground, because the observing side cannot reconstruct
the underlying record from it for the term the erosion clock permits, which is
the structural-inalienability answer of Section 2. The one quantity that
genuinely accumulates is the cultivated fertility of the relationship, the
reputational stock of predicate (ii), and it is a conjecture, not a measured
aggregation of records. The figure adds no claim; it states the shape the five
predicates and the imported guarantee jointly take.

**Preconditions of the imported guarantee.** The information-theoretic guarantee
that underwrites the durability of the stock is imported from the companion
paper. We state its preconditions here as numbered assumptions, so that later
sections can reference them, and so that the guarantee is never invoked without
them (GR-7 discipline).

- **Assumption A1 (non-collusion).** The boundary agent S and the delegation
  agent M do not collude to pool the context each holds; formally the inter-agent
  conditional independence $I(Y_S; Y_M \mid X) = 0$ holds with no third channel
  carrying the residue.
- **Assumption A2 (fixed adversary class).** The guarantee is stated against a
  specified adversary class of bounded capability; it is not a claim against every
  possible adversary.
- **Assumption A3 (time-indexing and the two deficit conditions).** The companion
  paper separates two clocks, and the economics prices the second. The first is
  certificational: declared capacities are certified against the estimation and
  attack tooling available at time $t$, and what drifts as tooling improves is the
  certified value, not the information. The second is the erosion clock. Let $B_t$
  denote the adversary's accumulating background information (its linkage corpus
  and side priors, carried about the source through the world and not through the
  disclosed transcript); the residual uncertainty $H(X \mid B_t)$ is non-increasing
  in calendar time while $H(X)$, the capacities, and every certificate stay fixed.
  A1 and A2 license the additive capacity structure and an error floor but do not
  by themselves place the residual below one. The strict bound holds exactly while
  the informed capacity-deficit condition $C_S + C_M < H(X \mid B_t)$ holds, a
  measurable numerical fact about a system, an adversary class, and a declared
  background model, not a consequence of the architecture. The governing ratio is
  $R(t) = (C_S + C_M)/H(X \mid B_t)$, non-decreasing in $t$, with finite shelf
  life $t^{*} = \sup\{t : R(t) < 1\}$ coinciding with the first crossing. The
  erosion's form and direction are proved in the companion for a declared
  background model; its rate is a register conjecture, not a theorem. What expires
  at $t^{*}$ is the informed deficit condition, not the architecture.

The threat model of the economics is a passive observer that appropriates surplus.
The imported guarantee prevents that observer from reconstructing, under A1 and A2
with the deficit condition declared and for the duration $R(t)$ permits, the record
whose sovereignty is being priced.

**A synthesis to foreground: the separation's incentive design underwrites A1.**
Assumption A1 is a statement about behaviour; Proposition P4 (Section 4) is one
about incentives. Under two domain-scoped units of account with no exchange
between them, P4 makes maintaining the separation the earnings-maximising
strategy, so non-collusion is chosen by rational agents rather than merely hoped
for. In this precise sense P4 is a sufficient condition for A1 to hold as an
equilibrium: it *discharges A1*, and A1 only. It does not touch A2, the deficit
condition, or the time-indexing of A3, and it holds only while the two token
domains stay frictionally separate (Proposition P4 states the threshold and the
honest reversion). Even with A1 fully discharged, $R(t)$ still drifts and $t^{*}$
is still finite; the discharge secures non-collusion, not durability.

**The quality stake.** Reputation in the model is grounded in a non-transferable,
non-purchasable proof-of-practice resource earned through sustained sovereign
practice and spent on graph inscriptions. Its defining economic property is
non-transferability: it cannot be minted by fake accounts, bought to bypass the
practice requirement, or moved between accounts. We define it here as the
quality-and-Sybil signal used in Section 4.3 and carry its Sybil-resistance
property forward as a conjecture, not a theorem (register conjecture C42), with
the proof obligation stated where it is used.

---

## 4. Results: economic propositions

<!-- P1 carries C10 + P1model (A3 derivation); P2 carries L134 (rent, super-additive dropped); P3 carries C06/C42; P4 carries C11 + m2/m3 threshold; P5 carries C07(DA) + reputation compounding (M6). No confidence bands (GR-2). GR-7 in P4. -->

We state the economic results as propositions, each with its preconditions. Where
a proposition rests on a register conjecture we say so and give the proof
obligation and the unstarted step; we attach no confidence band to any of them.
The information-theoretic guarantee itself is not among these propositions: it is
imported from the companion paper and cited.

**Proposition P1 (the consent interface sets the appropriation share).** Normalise
the appropriable per-subject, per-period data surplus to 1, split between X (share
$s$) and the counterparty M (share $1-s$). Model the consent interface as the
extensive form of one non-cooperative alternating-offers bargaining game
(Rubinstein 1982): the interface fixes which party posts the first offer and how
many offer/response rounds precede exercise of an outside option, while the pie
and the outside options $h_X, h_M$ are held fixed across interfaces. Then under a
notice-and-consent interface $s \to 0$, and under a bilateral propose-and-respond
interface $s$ moves to an interior share equal to X's bargaining power.

*Basis and obligation (self-contained).* We use one model, not two. Rubinstein
alternating-offers is chosen because the consent interface *is* the extensive form
of the game; the cooperative Nash bargaining solution enters only once, as the
frictionless ($\Delta t \to 0$) limit of that game's subgame-perfect equilibrium
(Binmore, Rubinstein and Wolinsky 1986), and is used only to name the interior
interval, never as a second, interchangeable model. A cooperative solution
concept abstracts away the extensive form and so cannot distinguish the two
interfaces except by an ad hoc bargaining-power asymmetry; the non-cooperative
model derives the asymmetry from the protocol, which is the whole content of the
proposition.

- *Extraction regime (notice-and-consent).* The interface gives the subject no
  power to propose: she sees posted terms and may accept or be excluded, a
  single-round ultimatum game with M as sole proposer. If X declines she realises
  her outside option $h_X$; because she is not admitted to the aggregation or
  real-time-bidding venue where behavioural data clears, the only price she can
  realise is the atomised broker-resale price of one record, so $h_X \approx 0$.
  The unique subgame-perfect share is $s_{\text{extraction}} = h_X \to 0$. This is
  *not* produced by the near-zero outside option alone: a symmetric two-sided
  bargain with both outside options near zero would split near one half. The
  extraction result requires *both* features the interface supplies, the
  single-round sole-proposer extensive form and exclusion from the clearing venue.
  This is the precise sense in which the interface, not the subject's preference,
  sets the share.

- *Sovereign regime (IEEE 7012 propose-and-respond).* The standard inverts the
  offer direction: the subject posts machine-readable terms first, and the
  organisation accepts, counters once, or declines. This is an alternating-offers
  game with X as first proposer and genuine two-sidedness. A term set can be
  presented to more than one counterparty, and a subject-side aggregator gives an
  alternative route to realise value, so X's outside option is now credible; taken
  as roughly symmetric and non-binding, the outside options set threat points but
  do not pin the split, which is governed by bargaining powers (the outside-option
  principle; Binmore, Rubinstein and Wolinsky 1986; Sutton 1986). With X proposing
  first the subgame-perfect share is interior for any discount factors, and in the
  frictionless limit equals X's bargaining power $\beta = \rho_M/(\rho_X+\rho_M) \in
  (0,1)$. The interior interval $[0.3, 0.7]$ of Section 5.1 is the image of $\beta$
  over a bounded, roughly symmetric range of relative patience (neither party more
  than about $2.3$ times as impatient as the other): $0.5$ symmetric, $0.3$
  counterparty-favourable, $0.7$ subject-favourable. It is a bargaining projection
  with a stated precondition, not a measured or guessed band; no deployed
  sovereignty market has been observed to price $s$ (Section 6), and we port no
  value of $\beta$.

- *Realisation.* The realised share is $s_{\text{realised}} = M(u,y)\, s$, making
  $[0.3,0.7]$ the *mature-market ceiling*, approached only as participation and
  depth grow ($u \to 1$, $y \to \infty$), never promised. It also gives the
  extraction regime a second, market-structural reason for the near-zero share:
  today no counterparty prices sovereignty, so $u \approx 0$, $M \approx 0$, and
  the subject captures near-zero even of a share she might in principle win. Using
  $M(u,y)$ *weakens* the sovereign result in the correct direction; no value of $M$
  or $\tau$ is asserted.

**Proposition P2 (the observer-to-broker gap is positive and is rent, not
super-additive aggregation).** The observer's lifetime targeting-attributable
capture per user exceeds the atomised broker-resale price of a record by a large,
positive, order-of-magnitude interval; that gap is market-position rent (an
atomisation discount, a position rent, and lifetime accumulation), not
super-additive aggregation value.
*Basis and obligation.* The returns-to-scale evidence shows aggregate raw-data
value saturates: forecast error falls only at a diminishing rate, the variety
dimension is flat-to-negative so super-additivity in variety is affirmatively
rejected, a small subsample suffices for a given estimation task, and
combined-attribute broker profiling is barely above chance (Bajari, Chernozhukov,
Hortacsu and Suzuki 2018; Varian 2014; Neumann, Tucker and Whitfield 2019, all
external). We assert the sign, the order-of-magnitude interval, and the rent
attribution, and we do *not* assert a point value or a super-additive adjective.
The obligation is to resist letting the interval harden into a point and to resist
re-importing super-additivity: the exact gap depends on region, tenure, and which
broker price anchors the denominator, none of which the data identify. This is a
result against the project's prior essays, which leaned on aggregation compounding,
and Section 6 reports it as such.

**Proposition P3 (a non-transferable stake resists the Sybil attack that unravels
the market).** A personal-data market fails when a buyer cannot distinguish
high-quality consented data from noise; the failure is informational (Akerlof
1970; Spiekermann et al. 2015). A non-transferable, non-purchasable
proof-of-practice stake makes the cost of a quality claim equal to the difficulty
of earning the stake, which resists the Sybil attack that would otherwise flood
the signal with cheaply minted identities.
*Basis and obligation.* This is a conjecture (register conjecture C42), carried
with its proof obligation and no confidence band. The cost-to-forge argument is
explicit: non-transferability closes the three cheap paths to a false signal (mint
via fake accounts, purchase, transfer). The unstarted step is the adversary-regime
analysis that would establish no cheaper path exists and bound the residual Sybil
advantage; until it is discharged the proposition is a candidate repair for the
lemons failure, not a demonstrated one.

**Proposition P4 (the separation is incentive-compatible, up to a conversion-
friction threshold).** If the two agents earn in two domain-scoped units with
sufficiently high conversion friction between them, protection-domain earnings
buying only protection tooling and delegation-domain earnings buying only
delegation tooling, then maintaining the separation of S and M is the
earnings-maximising strategy, whereas a single unified unit would make
context-pooling earnings-maximising.
*Basis and obligation.* The obligation is to state the agents' payoff functions
and show separation is a best response under the two-unit design and defection
under the one-unit design. Two cautions are load-bearing. First, the premise is
not the binary "no exchange pool exists" but a threshold: let colluding generate
additional joint surplus $\Delta > 0$ and let $\Phi \in [0,1]$ be the fraction of
it each agent realises in its own numeraire at the shadow exchange rate net of
conversion friction; non-collusion is the best response exactly when $\Phi\,\Delta
< \kappa$, the margin forgone by colluding. Under strict no-exchange ($\Phi = 0$)
this holds trivially; as the shadow market becomes liquid ($\Phi \to 1$) it fails
once $\Delta \ge \kappa$. We report the reversion with equal prominence: a
sufficiently liquid shadow exchange rate reintroduces collusion, and then P4 does
not discharge A1 and the non-collusion precondition reverts to a bare assumption.
Bounding the conversion friction against the collusion surplus is an open item
(Section 6). Second, the source material also contains a sentence asserting that
under the single-unit design the reconstruction ceiling "fails" and "mathematical
guarantees collapse"; stated without preconditions or time-indexing, it is not
imported. This proposition asserts only incentive-compatibility up to the
threshold, discharging A1 alone; it makes no static statement about
reconstruction, and $R(t)$ still drifts.

**Proposition P5 (reputation capital may appreciate while surveillance data
depreciates).** Reputation built from consistent consented disclosure is claimed
to appreciate over time, while surveillance data depreciates under a freshness
decay. This is the one sense in which the compounding predicate of Section 3
survives, and it survives only as a conjecture.
*Basis and obligation.* This is a directional conjecture, unmeasured (it
corresponds to E4-C07, a design assumption in the extraction, not a register
theorem). The supporting argument, that reputation is hard to forge because it
requires simultaneous behavioural consistency, correct personal-meaning
derivation, and narrative continuity across time, is a design claim, not a proof;
no measured forgery-cost curve is offered. Crucially, this reputational
compounding is the *only* compounding the thesis relies on: raw behavioural-data
aggregation does not compound (Proposition P2), so the thesis rests on this
conjecture and the other four predicates, not on any super-additivity of raw data.
The measurement that would settle it is named in Section 6.

---

## 5. Valuation methodology and evaluation

<!-- 5.1/5.2 = S5 patch verbatim (M4); 5.3 wedge->rent capture (M6, A12 2.2). GR-3 throughout: no 678x/31,000x/70:1/fiat; dollar anchors cited by external source only. -->

This section carries the valuation. Every number appears in the same table as its
assumptions, measured quantities and projections are visibly separated, and no
magnitude from the project's prior essay lineage is reproduced as a measured fact;
the evaluation is an analysis of published measurements, not a new experiment.

Two per-person magnitudes circulate in the project's prior essays, a present-day
value gap and a larger accessible-volume gap under full capture, and neither
survives a tier-A rebuild as a point estimate. A gap of the form (potential
value)/(currently captured value) is ill-posed in the extraction regime, because
the denominator tends to zero and a ratio to a near-zero base is a division
artefact; the larger figure was already reframed in the prior text away from an
arithmetic ratio, and a quantity its own source declares non-arithmetic cannot be
re-imported as a valuation ratio. We replace the first with a share methodology and
the second with a rent-attributed gap.

**5.1 The surplus-appropriation share.** We replace the retired present-day gap
with the bounded, range-valued share $s$ of Section 3. Both regimes are stated as
dimensionless intervals on the same normalised per-period surplus, so the
appropriation gap is the arithmetic difference of two stated intervals, not a
free-standing claim.

| Quantity | Regime interval (dimensionless) | Endpoint basis (external evidence, cited not printed) |
|---|---|---|
| $s$ (extraction) | order $10^{-4}$ to $5\times10^{-2}$ | Lower/anchor: $s$ is (the subject's per-period realisable value) over (the per-period appropriable surplus). The only price the subject can realise in a market she accesses is the atomised broker-resale price of one record; taken as an annual realisation and divided by the observer's gross annual advertising flow per user, this is of order $10^{-4}$ (broker resale prices per record, Steel et al. 2013 / OECD 2013; per-user gross advertising flow, Meta 2023 Form 10-K; both external). The anchor moves with the unmeasured annual resale multiplicity of a record and is reported as an order, not a point. Upper $5\times10^{-2}$: an unmeasured generous allowance for uncaptured consumer surplus from the zero-price side of the two-sided market (Section 6), not a measurement. |
| $s$ (sovereign; **projection**) | $[0.3,\,0.7]$ | Nash bargaining split of the same normalised surplus once a credible outside option exists: $0.5$ symmetric, $0.3$ counterparty-favourable, $0.7$ subject-favourable, the image of the bargaining-power parameter $\beta$ under bounded relative patience (Proposition P1). This is a bargaining projection, not a measurement; no deployed sovereignty market has been observed to price $s$ (Section 6). |
| WTA/WTP endowment ratio (value-based) | $[\approx1.2,\,\approx4]$ | Ratio of the elicited monetary valuations to accept disclosure versus to pay for protection (Acquisti, John and Loewenstein 2013, external). The lower/anchor $\approx1.2$–$1.4$ is the value wedge in that experiment; the upper reach brackets larger endowment effects in the broader literature. A separate participation-proportion ratio of order $5$ in the same experiment is a ratio of the shares of subjects choosing privacy under the two framings, not a ratio of valuations, and is cited as direction-only corroboration of the endowment effect, never as its magnitude. |

The appropriation gap is now derived rather than asserted. It is the movement of
$s$ from the extraction interval to the sovereign interval:
$$\log_{10} s_{\text{sovereign}} - \log_{10} s_{\text{extraction}} \;\approx\; (-1) - (-4) \;=\; 3,$$
a share-shift of about three orders of magnitude at the anchors, widening to about
four at the lower extraction endpoint and narrowing at the free-service allowance.
The shift is a consequence of the two stated intervals, expressed as a change in a
dimensionless share and never as a ratio to a near-zero base. The single figure
that circulated in the project's prior essays is not reconstructed; what survives
is the interval-to-interval movement, which is why the endpoints, not a headline
multiple, are the content of this subsection.

**5.2 The realised-value gap.** The prior draft carried a single wedge, positive
and super-additive, of order $10^{1}$ to $10^{5}$. That object does not survive:
its top divided an annual flow by a one-time stock, and its super-additivity is
asserted by no external measurement. We replace it with the two distinct objects
the single wedge conflated, give each an order-of-magnitude interval derived from
stated endpoints, refuse to point-identify either, and drop the word
"super-additive" entirely.

| Quantity | Interval (dimensionless) | Endpoint basis (external evidence, cited not printed) |
|---|---|---|
| $w_{\text{model}}$ = single-record modelling/targeting premium: a targeted-segment record over a general record within the same broker market (like-for-like, stock over stock) | order $\approx 10^{0}$, saturating, **not super-additive**, **not point-identified** | The anchor is a cross-sectional price-level ratio between two record types for one subject's record (Steel et al. 2013 / OECD 2013, external), of order a few. It does not measure the returns to aggregating many subjects' data, and no external figure in the evidence set measures aggregation super-additivity. Returns-to-scale evidence bounds any aggregation term to order $\approx 10^{0}$: forecast error falls only at a diminishing rate, with genuine but diminishing gains in history length and the data-variety dimension robustly flat-to-negative, i.e. super-additivity in variety is rejected (Bajari, Chernozhukov, Hortacsu and Suzuki 2019, external); a small subsample suffices for a given estimation task, so the marginal analytic value of additional volume at scale is $\approx 0$ (Varian 2014, external); combined-attribute broker profiling is barely above chance (Neumann, Tucker and Whitfield 2019, external). |
| $w_{\text{gap}}$ = observer-to-broker realised-value gap: the observer's lifetime targeting-attributable capture per user over the one-time atomised broker-resale price of a record (like-for-like, stock over stock) | order $10^{4}$ to $10^{5}$, **not point-identified**, and it is **rent**, not aggregation value | Both terms are stocks (lifetime accumulated observer capture over tenure, the annual gross flow scaled by the external targeting-attributable fraction; a one-time record price), so the ratio is dimensionless and the flow-versus-stock boundary the prior draft crossed is removed (Meta 2023 Form 10-K per-user gross flow; the targeting-attributable fraction from the online-advertising literature; Steel et al. 2013 / OECD 2013 broker prices; all external). The gap is large because the record is atomised and the subject is not admitted to the clearing venue, not because data value compounds: it decomposes into an atomisation discount, market-position rent, and lifetime accumulation, none of which is super-additive aggregation value. It moves with region, tenure, and which broker price anchors the denominator, and is reported as an order, not a point. |

The gap is where the counterparty's surplus originates and is exactly the object a
subject-side aggregator (Section 5.3) would need to capture. We assert its sign
and its order-of-magnitude interval; we do *not* assert super-additivity, because
no external figure in the evidence set measures it and the returns-to-scale record
rejects it in the variety dimension. We assert no point value, and the obligation
(Proposition P2, Section 6) is to resist letting the interval harden into one,
because the exact gap fixes a region, a tenure, and a denominator that the
available data do not identify, and because most of its size is rent rather than
data value. This is the honest residue of the retired high-end intuition: the
observer-to-broker gap is large, its lower and upper orders are stated, and it is
correctly attributed to atomisation discount, market-position rent, and lifetime
accumulation rather than to compounding aggregation; it is neither a per-person
monetary amount nor the essay figure.

**5.3 The market mechanism, instantiated.** The value is lost in the extraction
regime and realised in the sovereign one through three concrete instruments, and
they are three *distinct* mechanisms, not one.

- *Price discovery* is the consent interface read as a bargaining protocol
  (Proposition P1): notice-and-consent sets $s$ near zero; IEEE 7012
  propose-and-respond moves it into the interior range, gated to the realised
  share by market maturity $M(u,y)$.
- *Rent capture* (not wedge capture) is a subject-side aggregator. Today the
  observer-to-broker gap accrues entirely to the observer, but that gap is not
  super-additive aggregation value the aggregator would have to reproduce: the
  returns-to-scale evidence shows raw-data value saturates (Section 5.2), and the
  gap is market-position rent, the discount an atomised record suffers because the
  subject is not admitted to the venue where behavioural data clears. A data
  coalition, mediator of individual data, or data trust (Arrieta-Ibarra et al.
  2018; Posner and Weyl 2018; Delacroix and Lawrence 2019) aggregates *bargaining
  position* on the subject side and returns a negotiated fraction of that rent to
  subjects. It redistributes a positional rent; it does not unlock latent
  compounding value, because the evidence says there is none to unlock. This is the
  honest and, we argue, stronger form of the claim: the remedy does not require
  individuals to replicate platform-scale aggregation.
- *Quality signalling* is the non-transferable stake (Proposition P3), the
  candidate repair for the lemons failure that would otherwise unravel the market
  of the first two instruments.

Stated plainly: in the extraction regime the share $s$ is near zero and the
observer-to-broker gap accrues entirely to the observer, so the sovereignty has a
market price currently paid to someone else. The two levers are distinct: price
discovery raises the subject's share of the pie she is admitted to; rent capture
is about admission to the clearing venue in the first place. This is the home
thesis as a mechanism claim, with the mechanisms named and kept distinct, and no
monetary figure or reproduced ratio.

**5.4 The tier ladder as illustrative parameters.** The model sketches a
reputation ladder in which higher accumulated relationship credentials unlock
higher-value coordination. The specific value multipliers attached to the ladder
in the source are illustrative design parameters with no empirical derivation; the
source itself labels them theoretical projections. We report the compounding
thesis, that privacy enables trust, trust enables higher-stakes delegation, and
higher stakes generate higher returns that attract better opportunities, and we
bind that "compounding" explicitly to *reputation* and carry it as the directional
conjecture of Proposition P5, never to raw-data aggregation, which does not
compound (Section 5.2). The multipliers are reported as illustrative, never as
measured returns; no multiplier value is asserted as an observed rate.

**5.5 The compression-as-assessment mechanism.** The coordination economy is
claimed viable by a compression protocol under which agents exchange compressed
representations with expand-on-demand rather than full records, driving
per-interaction cost toward near-zero while preserving privacy, and under which
compression fidelity is a quantified assessment (in the Promise Theory sense) that
the knowledge-transfer promise was kept. The extractable claim is the mechanism,
compression fidelity read as a measurable assessment signal; the specific
compression ratios in the source are not reproduced as facts.

**5.6 An independent second-substrate derivation.** An independent build of the
same separation architecture on a different substrate kept the custody split and
dropped the reputation score entirely, disclosing instead a signed, decomposable
evidence graph verified offline against issuer identifiers, which never emits a
tier, score, or ranking (register conjecture C95, the evidence-graph anti-score).
We present this as an independent derivation, not a competitor. Its sharper
economic reading is itself conjectural: an emitted reputation scalar is a computed
projection correlatable across contexts and accumulable by an adversary, whereas
single-use selective disclosure emits the minimum for one decision. That the
scoreless posture is tighter in leakage terms is a conjecture whose magnitude is
unproven; it rhymes with the register's existence-leak and reading-not-authority
conjectures (C66) but is not a measured result, and the evidence-graph format
travels with its W3C Verifiable Credentials citation.

---

## 6. Threats to validity

<!-- limits of P1, M(u,y), C07, tier multipliers, C42, C02; E2 R(t) (M3); L134 rent as positive-prominence negative (M6/GR-8); WP-07 submission gating (M3); shadow-exchange reversion (m3); GR-8 equal-prominence reporting -->

This section gives the negative results the prominence of the positive ones. It is
not a coda; it is a result.

**The rent finding runs against the project's own prior essays, and we report it
as such.** The evidence rejects super-additive aggregation of raw behavioural data:
the observer-to-broker gap is market-position rent, not compounding data value
(Section 5.2, Proposition P2). The project's prior high-end figure gestured at
aggregation compounding; that gesture is denied by the returns-to-scale record and
retired. We report this with the prominence of a positive result, and it
strengthens the paper on two axes. The thin-market objection to propertization is
now answered without an unmeasured super-additivity assumption (Section 2), and the
valuation rests no load on a quantity the evidence denies; the surviving "bigness"
is rent, measured in kind as an atomisation and a position discount even though its
magnitude is non-identified. A claim that survives the deletion of its most
convenient premise is stronger, not weaker. The only compounding the thesis retains
is reputational and conjectural (Proposition P5).

**The valuation is not point-identified.** The share $s$ is bounded and its
extraction value is defensibly near zero, but its sovereign value is a bargaining
projection, not a measurement: no deployed sovereignty market has been observed to
price $s$. The realised-value gap $w_{\text{gap}}$ is asserted only in sign, an
order-of-magnitude interval, and its rent attribution; the genuine data-value
component $w_{\text{model}}$ is of order one and saturating; neither is
point-identified, and the paper must not let either interval harden into a point.

**The market-maturity gate is a proposal.** The functional form for $M(u,y)$ in
Section 3 is this paper's own construction, chosen for its boundary behaviour,
neither established in the source nor measured, with $\tau$ unestimated. It is
presented so the value equation can be written down honestly, not because the form
is known to be correct.

**Two propositions rest on open conjectures.** The Sybil-resistance of the
non-transferable stake (Proposition P3, register conjecture C42) is an open
conjecture with an unstarted adversary-regime step. The appreciation-versus-
depreciation claim (Proposition P5) is a directional design conjecture, unmeasured,
its unforgeability argument a design argument, not a forgery-cost measurement.
Neither is reported as settled.

**The separation's incentive compatibility rests on a conversion-friction
threshold.** Proposition P4 discharges Assumption A1 only up to a threshold: if a
sufficiently liquid shadow exchange rate forms between the two domain-scoped units,
context-pooling becomes earnings-maximising again and A1 reverts to a bare
assumption. Bounding the conversion friction $\Phi$ against the collusion surplus
$\Delta$, or conceding A1 is assumed independently, is an open item.

**The tier multipliers are illustrative.** The reputation-ladder multipliers of
Section 5.4 are design parameters, not measured returns.

**A reference enumeration was corrected.** The six-capital reference frame was
stated incorrectly in the project's prior whitepaper lineage and corrected against
the International Integrated Reporting Council source (Section 2). The divergence is
recorded; the predicate thesis is unaffected, since it rests no weight on the
ordinal.

**The imported guarantee has a finite, adversary-relative horizon, and its
citability is submission-gating.** The guarantee is not a static property. It holds
against a fixed adversary class (Assumption A2) under non-collusion (Assumption A1),
and only where the informed capacity-deficit condition $C_S + C_M < H(X \mid B_t)$
holds does $R(t) = (C_S + C_M)/H(X \mid B_t)$ satisfy $R(t) < 1$; that deficit
condition is a measurable numerical fact about a system, an adversary class, and a
declared background model, not a consequence of the architecture. $R(t)$ is bounded
below one at evaluation and rises as the adversary's background information
accumulates against a fixed archive, shrinking $H(X \mid B_t)$ while the capacities
and every certificate stay fixed, so the shelf life $t^{*} = \sup\{t : R(t) < 1\}$
is finite; the erosion's form and direction are proved in the companion for a
declared background model, and its rate is carried in the register as a conjecture,
not a theorem. We deliberately do not claim a full "term structure" of
dated maturities, which would require a schedule for $R(t)$ the register carries
only as a conjectural upward drift; we claim no more than a finite,
adversary-relative horizon. What expires at $t^{*}$ is the deficit condition, not
the architecture. We do not claim adversaries cannot reconstruct the record; we
claim a time-indexed, precondition-bound bound on what they can, sourced to the
companion paper. Two consequences: a valuation ignoring the horizon overstates the
stock's durability; and the entire durability leg is gated on WP-07 being a real,
citable companion at submission. If the companion that proves the guarantee (with
Assumptions A1 to A3 and the erosion result A3 imports) is not citable when this
paper is submitted, the durability claim must be withdrawn to a stated open problem,
because this paper imports that result and does not re-prove it. This gating is a
submission blocker, not a polish item. The metric-agreement half of the gate is
resolved: the companion's erosion result is stated on the adversary's accumulating
background information, not on computational capability, so the object Section 2
distinguishes from the differential-privacy composition clock is the object the
companion proves.

**Reporting commitment.** A measured result that runs against the predictions of
this paper, for instance a deployed sovereignty market that fails to move $s$
despite a working 7012 protocol and a functioning stake, or a realised-value gap
that measures far outside the asserted interval, will be reported with the same
prominence as a confirmation. The honesty of the negative result is the moat, not
an embarrassment to be minimised.

---

## 7. Conclusion

<!-- synthesis C01, C03, L134, P1model, E2; open items named precisely -->

The argument decomposes into four claims held together conditionally. First,
behavioural data is subject-owned capital: a stock the subject can hold, invest in,
compound (reputationally, as a conjecture; raw-data aggregation does not, Section
5.2), and transfer, rather than a labour flow or a firm-owned asset, and the two
objections that sank naive propertization, alienability and thin markets, are
answered by structure rather than doctrine. Second, the subject captures a
near-zero share of the surplus that stock generates, and that share is not a
preference but the subgame-perfect equilibrium of a bargaining game whose rules are
the consent interface; a bilateral propose-and-respond protocol moves the interior
share to the subject's bargaining power, gated to a realised share by market
maturity. Third, the value is realised or lost through a mechanism with three
distinct levers, price discovery through the consent interface, rent redistribution
through a subject-side aggregator, and quality signalling through a non-transferable
Sybil-resistant stake, so the sovereignty has a market price currently paid to
someone else. Fourth, what makes the stock durable is architectural, an
information-theoretic separation of the observing boundary agent from the acting
delegation agent, imported from a companion paper, holding against a fixed adversary
class under non-collusion with a declared capacity-deficit condition, and
time-indexed so it holds only for a finite, adversary-relative horizon $t^{*}$.

None of the four claims is asserted beyond its evidence. The valuation is a share
and a rent-attributed gap with ranges, not two magnitudes from the prior essays;
the one place the evidence contradicted those essays, the rejection of raw-data
compounding, is reported at the prominence of a positive result. The market
mechanism is buildable but unbuilt. The guarantee is proved elsewhere, dated, and
gated on the companion being citable at submission. The conclusion is a
decomposition, not a triumph, and the open items are its real content:

- Bound the realised-value gap $w_{\text{gap}}$ empirically, or more tightly than a
  wide order-of-magnitude interval, keeping its rent attribution.
- Estimate the market-maturity gate $M(u,y)$ and its time constant $\tau$ from an
  operating market, and test the proposed functional form and the realised-share
  prediction $s_{\text{realised}} = M(u,y)\, s$.
- Bound the conversion friction $\Phi$ against the collusion surplus $\Delta$ so
  that Proposition P4 discharges Assumption A1 in equilibrium, or concede A1 is
  assumed independently.
- Discharge the Sybil-resistance conjecture (C42) with the adversary-regime step, or
  refute it.
- Measure the reputation-appreciation claim (Proposition P5) against a forgery-cost
  curve.
- Observe a deployed sovereignty market and test whether a working 7012 protocol and
  a functioning stake actually move the subject's share $s$.

The paper closes in the decomposed, conditional, and dated form in which its claims
are true. Behavioural data is subject-owned capital on five predicates; the
architecture that would let a subject hold it is specifiable; the guarantee that
would make it worth holding is imported, on a clock, and gated on a citable
companion; and the price of the sovereignty it protects is, for now, collected by
someone else.

---

## References

*(Handoff to A4: verify each against `templates/submission/references/pv_v6.bib`
and add. IEEE 7012 already in extraction citations; confirm bib key. Confirm the
predicate-led retitle. New bargaining and propertization and returns-to-scale
citations flagged below are tier-A permitted external sources.)*

- Acquisti, A., Taylor, C., Wagman, L. (2016). The Economics of Privacy. *Journal
  of Economic Literature* 54(2).
- Acquisti, A., John, L., Loewenstein, G. (2013). What Is Privacy Worth?
  *Journal of Legal Studies* 42(2).
- Akerlof, G. (1970). The Market for Lemons. *Quarterly Journal of Economics*
  84(3).
- Anderson, R. (2001). Why Information Security is Hard: An Economic Perspective.
  *ACSAC* (WEIS lineage).
- Arrieta-Ibarra, I., Goff, L., Jimenez-Hernandez, D., Lanier, J., Weyl, E.G.
  (2018). Should We Treat Data as Labor? Moving beyond Free. *AEA Papers and
  Proceedings* 108.
- Bajari, P., Chernozhukov, V., Hortacsu, A., Suzuki, J. (2019). The Impact of Big
  Data on Firm Performance: An Empirical Investigation. *AEA Papers and
  Proceedings* 109, 33-37. [A4-verified 2026-07-15; returns-to-scale evidence,
  Sections 2 and 5.2; year corrected 2018 to 2019 for consistency]
- Bergstra, J., Burgess, M. (2019). *Promise Theory: Principles and Applications*
  (2nd ed.).
- Binmore, K., Rubinstein, A., Wolinsky, A. (1986). The Nash Bargaining Solution
  in Economic Modelling. *RAND Journal of Economics* 17(2). [A4: add; frictionless
  limit and outside-option principle, Section 4 P1]
- Delacroix, S., Lawrence, N.D. (2019). Bottom-up Data Trusts: Disturbing the "One
  Size Fits All" Approach to Data Governance. *International Data Privacy Law*
  9(4). [A4: add; data-trust/cooperative instrument, Sections 2 and 5.3]
- International Integrated Reporting Council (2013, rev. 2021). *International
  Framework* (the six-capitals model).
- IEEE Std 7012-2025. *IEEE Standard for Machine Readable Personal Privacy Terms*
  (2026-01-20).
- Lanier, J. (2013). *Who Owns the Future?* Simon and Schuster.
- Laudon, K.C. (1996). Markets and Privacy. *Communications of the ACM* 39(9).
  [A4: add; propertization, Section 2]
- Nash, J. (1950). The Bargaining Problem. *Econometrica* 18(2). [A4: add;
  cooperative solution named as the frictionless limit, Section 4 P1]
- Neumann, N., Tucker, C.E., Whitfield, T. (2019). Frontiers: How Effective Is
  Third-Party Consumer Profiling? *Marketing Science* 38(6). [A4: add;
  combined-attribute profiling near chance, Section 5.2]
- OECD (2013). *Exploring the Economics of Personal Data*.
- Osborne, M.J., Rubinstein, A. (1990). *Bargaining and Markets*. Academic Press.
  [A4: add; textbook reference for the alternating-offers derivation, Section 4 P1]
- Posner, E., Weyl, E.G. (2018). *Radical Markets*. Princeton University Press
  (chapter on data as labour).
- Prins, C. (2006). Property and Privacy: European Perspectives and the
  Commodification of Our Identity. In *The Future of the Public Domain*. [A4: add;
  propertization, Section 2]
- Purtova, N. (2015). The Illusion of Personal Data as No One's Property. *Law,
  Innovation and Technology* 7(1). [A4: confirm year/title; propertization,
  Section 2]
- Rubinstein, A. (1982). Perfect Equilibrium in a Bargaining Model. *Econometrica*
  50(1). [A4: add; the one bargaining model, Section 4 P1]
- Samuelson, P. (2000). Privacy As Intellectual Property? *Stanford Law Review*
  52(5). [A4: add; propertization and the alienability objection, Section 2]
- Schwartz, P.M. (2004). Property, Privacy, and Personal Data. *Harvard Law
  Review* 117(7). [A4: add; hybrid inalienability, Section 2]
- Spiekermann, S., Acquisti, A., Bohme, R., Hui, K.-L. (2015). The challenges of
  personal data markets and privacy. *Electronic Markets* 25(2).
- Steel, E., et al. (2013). How much is your personal data worth? *Financial
  Times* data-broker pricing feature. [A4: confirm citable form; broker-price
  anchor, Section 5; OECD 2013 may carry this anchor instead]
- Sutton, J. (1986). Non-Cooperative Bargaining Theory: An Introduction. *Review
  of Economic Studies* 53(5). [A4: add; outside-option principle, Section 4 P1]
- Varian, H. (2014). Big Data: New Tricks for Econometrics. *Journal of Economic
  Perspectives* 28(2). [A4: add; subsample sufficiency, Section 5.2]
- W3C (2022). *Verifiable Credentials Data Model 1.1*.

<!-- Litreview-reflection references (WP-14a run wf_ba400906-67b; A4-verified
2026-07-15, L138). The differential-privacy-markets strand is the must-engage
prior art surfaced by the adversarial search; the rest place the ultimatum
result, the rent diagnosis, the PIA-to-metric transition, and the durability
antecedent. Interleave alphabetically at submission. -->
- Bergemann, D., Bonatti, A., Gan, T. (2022). The Economics of Social Data.
  *RAND Journal of Economics* 53(2), 263-296. [rent diagnosis / social-data
  externality, Section 2]
- Cummings, R., Ligett, K., Roth, A., Wu, Z.S., Ziani, J. (2015). Accuracy for
  Sale: Aggregating Data with a Variance Constraint. *ITCS 2015*, 317-324.
  [differential-privacy-markets strand, Section 2]
- Fleischer, L.K., Lyu, Y.-H. (2012). Approximately Optimal Auctions for Selling
  Privacy when Costs are Correlated with Data. *EC '12*, 568-585.
  [differential-privacy-markets strand, Section 2]
- Ghosh, A., Roth, A. (2011). Selling Privacy at Auction. *EC '11*, 199-208.
  [differential-privacy-markets strand; prices the disclosure bound as a
  commodity, the occupant of the system-property x market-pricing cell, Section 2]
- Gu, J. (2024). Data Trade and Consumer Privacy. arXiv:2406.12457. [formal
  data-market bargaining; intermediary bargaining power sets consumer surplus,
  Section 1]
- Guth, W., Schmittberger, R., Schwarze, B. (1982). An Experimental Analysis of
  Ultimatum Bargaining. *Journal of Economic Behavior and Organization* 3(4),
  367-388. [the textbook ultimatum result; the near-zero share derivation is not
  claimed as new, Section 1]
- Li, C., Li, D.Y., Miklau, G., Suciu, D. (2013). A Theory of Pricing Private
  Data. *ICDT '13*, 33-44 (extended in *ACM TODS* 39(4), 2014).
  [differential-privacy-markets strand, Section 2]
- Mosca, M. (2018). Cybersecurity in an Era with Quantum Computers: Will We Be
  Ready? *IEEE Security and Privacy* 16(5), 38-41. [the adversary-relative
  shrinking-horizon antecedent for R(t); the durability form is not claimed as
  new, Sections 1 and 2]
- Wagner, I., Boiten, E. (2018). Privacy Risk Assessment: From Art to Science, by
  Metrics. *DPM 2018* (ESORICS Workshops), LNCS 11025, 225-241. [PIA-to-metric
  transition; the subject-impact to system-property move is not claimed as new,
  Section 2]

<!-- Differential-privacy-refinements references (WP-14a run wf_aea45393-332, the
CTR-LR-02b DP-stress test resolving LM2; extraction-verified 2026-07-15, L139).
These engage the DP strand that the R(t) residue is distinguished from by a clock
argument (Section 2). Interleave alphabetically at submission; final A4 P2 confirm
the two arXiv adversary-aware entries. -->
- Bun, M., Steinke, T. (2016). Concentrated Differential Privacy: Simplifications,
  Extensions, and Lower Bounds. *TCC 2016*, LNCS 9985, 635-658. [zCDP; fixed-adversary
  composition accounting, Section 2]
- Cummings, R., Hod, S., Sarathy, J., Swanberg, M. (2024). ATTAXONOMY: Unpacking
  Differential Privacy Guarantees Against Practical Adversaries. arXiv:2405.01716.
  [adversary-aware DP; capability as a static parameter, Section 2]
- Dong, J., Roth, A., Su, W.J. (2022). Gaussian Differential Privacy. *Journal of the
  Royal Statistical Society: Series B* 84(1), 3-37. [f-DP; hypothesis-testing
  adversary, Section 2]
- Dwork, C., Naor, M., Pitassi, T., Rothblum, G.N. (2010). Differential Privacy under
  Continual Observation. *STOC 2010*, 715-724. [continual-release clock, Section 2]
- Dwork, C., Rothblum, G.N., Vadhan, S. (2010). Boosting and Differential Privacy.
  *FOCS 2010*, 51-60. [advanced composition, Section 2]
- Kairouz, P., Oh, S., Viswanath, P. (2015). The Composition Theorem for Differential
  Privacy. *ICML 2015*, PMLR 37, 1376-1385. [optimal composition, Section 2]
- Mironov, I. (2017). Renyi Differential Privacy. *IEEE CSF 2017*, 263-275. [RDP;
  composition-clock accounting, Section 2]
- Swanberg, M., Annamalai, M.S.M.S., Hayes, J., Balle, B., Smith, A. (2025). A Unified
  Framework for Adversary-Aware Differential Privacy Bounds. arXiv:2507.08158.
  [adversary-aware DP bounds, Section 2]
- Valavi, E., Hestness, J., Ardalani, N., Iansiti, M. (2022). Time and the Value of
  Data. Harvard Business School WP 21-016 / arXiv:2203.09118. [data-value relevance
  decay; opposite-polarity wall clock, Section 2]

<!-- External dollar-anchor sources (Meta 2023 Form 10-K per-user gross advertising
flow; the online-advertising literature's targeting-attributable fraction) are
cited by source only and print no figure (GR-3); A4 to place them as the endpoint
basis of Section 5.1/5.2 without printing any dollar value. -->

<!-- Companion internal reference (not a public citation): the imported
information-theoretic guarantee, its Assumptions A1-A3, the informed
capacity-deficit condition, and the erosion result (WP-07 Definition 3.9 +
Corollary 5.4b, revision-draft-v3 2026-07-16: background family B_t, cap survives
conditioning, floor erodes through H(X | B_t)) are developed in WP-07. At release
this becomes the appropriate public spec URL (at most one, per GR-3/tier-A) or a
companion-paper citation, at A4's discretion. SUBMISSION-GATING: if WP-07 is not a
citable companion at submission, the durability leg (Sections 3, 4 P4, 6, 7)
reverts to a stated open problem, per Section 6. The METRIC-AGREEMENT half of the
gate is RESOLVED (L145): the companion's erosion object is the informational
background, matching Section 2's clock distinction. -->
