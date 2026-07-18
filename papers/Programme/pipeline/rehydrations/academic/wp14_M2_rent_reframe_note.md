---
tier: A
wp: WP-14
role: A12
venue_target: WEIS-2027
date: 2026-07-15
answers: >
  A5 review-1 (L131) findings M2 (novelty/positioning against the
  personal-data-as-property literature) and M5 (framing legibility: the
  "seventh capital" ordinal), and integrates the Run-3 rent finding (L134)
  into the capital-class thesis. Minor m7 (subject-side aggregator =
  data-cooperative/data-trust instrument, under-attributed) is discharged as a
  by-product of the M2 propertization engagement.
discipline: >
  Tier-A. GR-3 (no 678x/31,000x/70:1/74x; no asserted fiat value of privacy;
  external dollar anchors cited by author/year only, never printed). GR-4
  vocabulary (boundary agent S, delegation agent M, data subject X, structural
  context erasure, conditional-independence residual; no emoji). GR-7 (every
  reconstruction/ceiling mention carries A1-A3 preconditions and R(t)
  in-passage). GR-8 (the rent finding is a negative result and is given the
  prominence of a positive one). GR-9 (every claim traces below). UK spelling,
  no em-dashes.
extraction_basis: >
  E4-seventh-capital C01 (the capital predicates), C06/C42 (non-transferable
  stake), C07 (reputation appreciation, directional conjecture), C10 (7012
  market structure); companion weis_valuation_methodology_v2_empirical.md
  Sections 4.3-4.4 (the rent finding); ledger L134 (Run-3 finalisation);
  imported guarantee WP-07 with Assumptions A1-A3 and R(t), cited not re-proven.
external_additions_for_A4: >
  Laudon (1996); Samuelson (2000); Schwartz (2004); Purtova (2015/2017);
  Prins (2006); Delacroix and Lawrence (2019). All external, tier-A permitted;
  A4 to verify each against the bib before release. None is canon-internal.
handoff: A2 (drop-in prose port), A3 (P1 sequencing with the sovereign
  interval), A4 (six external citations + retitle), A5 (re-review M2/M5).
---

<!-- ============================================================
A12 NOTE (pipeline internal; the drop-in prose blocks below are tier-A and are
ported by A2 into weis_seventh_capital.md; the rationale/handoff commentary is
stripped at release). This note does NOT hand-edit the draft (GR-6); it supplies
replacement/insertion text and a location list for the A2 revision loop, in the
same manner as weis_seventh_capital_S5_patch.md.
============================================================ -->

# WP-14 · Discharging M2 (propertization) and M5 (framing), and integrating the rent finding

## 0. Verdict

Three things are done here.

1. **M2 is discharged by engagement, not deflection.** The "third position"
   (data as capital the subject owns) is propertization of personal data, and
   propertization has a large, mostly critical literature the draft ignored. The
   drop-in text in Section 1 below cites it (Laudon; Samuelson; Schwartz;
   Purtova; Prins; Delacroix and Lawrence) and answers its three standing
   objections, alienability, thin markets, and distributional regressivity,
   naming precisely what the architecture adds that bare property rights do not:
   structural (information-theoretic) inalienability of the reconstruction and a
   by-construction non-transferable quality stake. The architecture converts
   Schwartz's *contractual* hybrid inalienability into a *structural* one.

2. **The rent finding is integrated honestly, and it strengthens the paper.**
   The Run-3 evidence (L134) rejects super-additive aggregation: the
   observer-to-broker gap is market-position rent (atomisation discount plus
   position rent plus lifetime accumulation), not compounding data value. The
   subject-side aggregator therefore **redistributes a positional rent; it does
   not unlock latent compounding value**. This is not a retreat. It is a
   *better* answer to the thin-market objection under M2, because it does not
   depend on individuals replicating a platform's aggregation technology; it
   depends only on pooling bargaining position, which is exactly what a data
   cooperative or data trust does. Better to have found it than a referee.

3. **M5 is discharged by de-emphasis (recommended over justification).** Lead
   with the capital predicates, which need no count; demote the IIRC "seventh"
   ordinal to a one-clause provenance note. Retitle recommended. Draft in
   Section 3 below.

Nothing here asserts a fiat value or reintroduces a fenced figure. Every dollar
anchor is cited to external evidence by author and year and never printed.

---

## 1. M2 discharge: engage the propertization literature (drop-in for Section 2)

<!-- A2: INSERT as a new subsection in Section 2, placed AFTER the
"Data as labour versus data as capital" block and BEFORE the
"Personal-data-market design and its failures" block. It carries the
propertization literature the draft's "third position" restates, answers the
three objections, and states the architecture's marginal contribution over bare
property. m7 is discharged inside it (data-trust/cooperative attribution). -->

**Propertization of personal data, and why the architecture is not just a
property right.** The position that behavioural data is capital *the subject
owns* is a propertization claim, and propertization of personal data has a
decades-old and largely critical literature that the seventh-capital framing
must answer rather than restate. Laudon (1996) proposed treating personal
information as an owned, licensable asset traded in a national information
market; Samuelson (2000) asked directly whether privacy could be protected by
an intellectual-property-style right and was sceptical; Schwartz (2004) set out
a model of propertized personal information but only with explicit safeguards,
because he took the naive version to fail; Purtova (2015) and Prins (2006)
analysed the European commodification debate and its hazards; and the
data-trust and data-cooperative strand (Delacroix and Lawrence 2019) proposed
fiduciary intermediation as an alternative to individual ownership altogether.
A referee who knows this literature will read "seventh capital" as a rebranding
of propertization unless the paper says what it adds. It adds two things, and
both are structural rather than doctrinal.

The literature levels three standing objections at propertization, and we take
each in turn.

*Objection (i): alienability defeats the protection.* A right the subject can
sell is a right the subject will be pressured to sell; once the data is
transferred under a default rule of free alienability, the protection is gone
(Samuelson 2000). Schwartz's (2004) response was to build *hybrid
inalienability* into the property right by legal construction, use-transferable
but with restrictions on onward transfer, precisely because unrestricted
alienability is self-defeating. Our response is to make the inalienability
*structural* rather than contractual. What the subject discloses under the
protocol is a scoped, single-purpose disclosure, not a handover of the stock,
because the observing side cannot reconstruct the underlying record from the
disclosure: the boundary agent S and the delegation agent M are separated so
that S never accumulates the context M holds, with structural context erasure
between agent invocations, and the residual an observer can reconstruct is
bounded by an information-theoretic guarantee imported from a companion paper
(WP-07). That guarantee is not a static ceiling: it holds against a fixed
adversary class (Assumption A2) under non-collusion (Assumption A1), and its
reconstruction residual is time-indexed, $R(t)$ bounded below one at the time of
evaluation and degrading on a computable schedule as adversary capability grows
(Assumption A3). Within that term, the asset cannot be fully alienated by an
act of disclosure, because disclosure does not transfer what disclosure cannot
reconstruct. The alienability objection is answered not by forbidding sale in
law but by making full transfer information-theoretically unavailable for the
duration $R(t)$ permits. Second, the quality stake on which the market's
signalling depends (Section 4.3) is *non-transferable by construction*: it
cannot be minted by fabricated accounts, purchased to bypass the practice
requirement, or moved between accounts (register conjecture C42). This is
Schwartz's inalienability again, but as a property of the object rather than a
clause a court must enforce. Bare property rights make everything alienable by
default; the architecture makes the two things that matter, the reconstruction
and the quality stake, non-alienable by design.

*Objection (ii): thin markets.* Individual data is worth almost nothing atomised,
transaction costs dwarf the per-record price, and no functioning market exists at
the level of the single subject. Our own valuation confirms the premise and is
sharper about its cause than the objection is (Section 5): the atomised
broker-resale price of one record sits several orders of magnitude below the
observer's realised lifetime capture, and the returns-to-scale evidence shows
that this gap is **not** the product of super-additive aggregation the subject
could never replicate. It is market-position rent, the discount a record suffers
because the subject is not admitted to the venue where behavioural data actually
clears (Section 5.2, Section 5.3). That distinction is what defeats the
thin-market objection. If the gap were compounding aggregation value, capturing
it would require each subject to reproduce a platform's aggregation technology,
and the objection would bite. Because the gap is positional rent, capturing it
requires only pooling *bargaining position*, which is exactly the function of the
subject-side aggregator, the mediator-of-individual-data / data-cooperative /
data-trust instrument (Arrieta-Ibarra et al. 2018; Posner and Weyl 2018;
Delacroix and Lawrence 2019). The thin-market objection assumes the only thing to
aggregate is data value; the finding that the gap is rent shows the thing to
aggregate is admission to the clearing venue.

*Objection (iii): distributional regressivity.* Under alienable propertization the
poor sell their privacy cheaply and the wealthy retain it, so privacy becomes a
luxury good and the market entrenches inequality. Two features of the architecture
bear on this, and we state the limit as plainly as the response. The structural
inalienability of the reconstruction (objection (i)) means the regressive
transaction, a subject alienating the stock itself for a low price, is not the
transaction the architecture supports; what is priced is scoped disclosure within
a retained stock, not sale of the stock. The fiduciary-intermediary form
(Delacroix and Lawrence 2019) is designed to redistribute bargaining position
toward those with the least of it, and the aggregator instrument inherits that
purpose. The honest limit: nothing in the architecture guarantees a
non-regressive *distribution* of the rent it redistributes; it changes who is
admitted to the venue, not how the surplus is split once inside, and the split is
the sovereign-regime bargaining share $s$, which is a projection and not a
measurement (Section 6). We claim the architecture removes the specific
regressive mechanism propertization is charged with, forced alienation of the
stock, not that it delivers a distributively just outcome.

The claim to novelty, then, is not that behavioural data can be owned, which the
propertization literature proposed and criticised long ago, but that the two
objections that sank naive propertization, alienability and thin markets, are
answered by structure: information-theoretic non-depreciation makes full
alienation unavailable for the term $R(t)$ permits, and the finding that the
observer-to-broker gap is rent rather than compounding value makes the remedy a
redistribution of position rather than an unattainable replication of scale.

---

## 2. Rent integration: adjust the compounding predicate and drop "super-additive"

The Run-3 finding (companion note Sections 4.3-4.4; ledger L134) is that the
evidence **rejects super-additive aggregation of raw behavioural data**. Forecast
error falls only at the diminishing rate the returns-to-scale literature reports;
the data-variety dimension is flat-to-negative, so super-additivity in variety is
affirmatively rejected; a small subsample suffices for a given estimation task,
so the marginal analytic value of additional volume at scale is near zero; and
combined-attribute broker profiling is barely above chance (Bajari, Chernozhukov,
Hortacsu and Suzuki 2018; Varian 2014; Neumann, Tucker and Whitfield 2019, all
external). The large observer-to-broker gap is therefore rent (atomisation
discount plus market-position rent plus lifetime accumulation), not compounding
data value. This must be carried into the capital-class thesis at every point
where the draft asserts super-additivity or raw-data compounding. The correction
does not weaken the thesis; it relocates the "bigness" from an unmeasured
productive-efficiency claim to a measured distributional one.

### 2.1 The compounding predicate is scoped, not deleted (Section 3)

The five capital predicates include (ii) *compounding*. Split it into what
survives and what does not, and give the negative equal prominence (GR-8):

- **Reputation may compound (directional conjecture, unmeasured).** A reputation
  built from prior consented disclosures may lower the cost of the next, so
  returns accrue on the accumulated relationship stock. This is Proposition P5's
  claim and it corresponds to a design assumption in the extraction (E4-C07), not
  a register theorem and not a measured result; the forgery-cost curve that would
  settle it is named as open work (Section 6). It is carried as a conjecture.
- **Raw behavioural-data aggregation does not compound (measured, external).** The
  value of aggregated raw data over atomised records saturates rather than
  compounds; super-additivity in the variety dimension is rejected by the
  returns-to-scale evidence above. The paper must not assert that raw-data
  aggregation is super-additive, and the word "super-additive" is dropped from the
  wedge throughout.

The capital-class thesis does not need raw-data compounding. It rests on the
other four predicates and on reputation compounding *as a conjecture*, and it is
strictly more honest for saying which of the two kinds of compounding is measured
(the raw-data kind, and it is negative) and which is conjectural (the reputation
kind).

<!-- A2 replacement for Section 3 predicate (ii). Drop in verbatim. -->

> (ii) *Compounding*: this predicate holds in one sense and is rejected in
> another, and we separate them. A reputation built from prior consented
> disclosures may lower the cost of the next, so returns accrue on the
> accumulated relationship stock; this is a directional conjecture (Proposition
> P5, corresponding to a design assumption in the extraction), unmeasured, and
> carried as such. Aggregation of the *raw* behavioural record, by contrast, does
> not compound: the returns-to-scale evidence shows aggregate data value saturates
> and rejects super-additivity in the data-variety dimension (Section 5.2). The
> compounding the thesis relies on is reputational and conjectural, not a
> super-additivity of raw data, which the evidence denies.

### 2.2 The mechanism reads as rent redistribution (Section 5.3 wedge-capture bullet)

The draft's "wedge capture" bullet (Section 5.3) says a subject-side aggregator
returns "a negotiated fraction of the wedge" to subjects, with the wedge implied
to be aggregation value. Correct it to rent redistribution.

<!-- A2 replacement for the "Wedge capture" bullet in Section 5.3. -->

> - *Rent capture* (not wedge capture) is a subject-side aggregator. Today the
>   observer-to-broker gap accrues entirely to the observer, but that gap is not
>   super-additive aggregation value the aggregator would have to reproduce: the
>   returns-to-scale evidence shows raw-data value saturates (Section 5.2), and the
>   gap is market-position rent, the discount an atomised record suffers because
>   the subject is not admitted to the venue where behavioural data clears. A data
>   coalition, mediator of individual data, or data trust (Arrieta-Ibarra et al.
>   2018; Posner and Weyl 2018; Delacroix and Lawrence 2019) aggregates *bargaining
>   position* on the subject side and returns a negotiated fraction of that rent to
>   subjects. It redistributes a positional rent; it does not unlock latent
>   compounding value, because the evidence says there is none to unlock. This is
>   the honest and, we argue, stronger form of the claim: the remedy does not
>   require individuals to replicate platform-scale aggregation.

### 2.3 Location list for "super-additive" and raw-data compounding (A2 sweep)

Every occurrence below asserts or implies super-additive raw-data aggregation and
must be reconciled with Section 5.2 as already patched (the S5 patch splits the
wedge into $w_{\text{model}}$, order $\approx 10^0$ and saturating, and
$w_{\text{gap}}$, order $10^4$ to $10^5$, rent not aggregation). The S5 patch
already fixes Section 5.1/5.2; the following are the *remaining* surfaces:

- **Abstract** (draft line ~69): "a non-identified but positive and
  super-additive aggregation wedge" -> "a non-identified observer-to-broker
  realised-value gap that the evidence attributes to market-position rent rather
  than to super-additive aggregation". And line ~54, "a stock that yields returns,
  compounds, ..." -> qualify "compounds" to "compounds through reputation
  (conjecturally)" or leave the enumeration and let predicate (ii) carry the
  scope; A2's choice, but the abstract must not leave "compounds" reading as a
  raw-data claim.
- **Introduction, contribution 2** (draft line ~143): "a non-identified,
  positive, super-additive aggregation wedge" -> "a non-identified
  observer-to-broker gap, attributed to rent rather than to super-additivity".
- **Section 2, data-as-capital block** (draft line ~193): "an owned,
  non-depreciating stock yields as long as it is held and can be invested,
  compounded, and transferred" -> keep, but "compounded" now points to the scoped
  predicate (ii); no change needed if predicate (ii) is patched, though a
  parenthetical "(reputationally; Section 3)" removes any ambiguity.
- **Section 3, aggregation-wedge paragraph** (draft line ~256): "Aggregation of
  behavioural data is super-additive (Acquisti, Taylor and Wagman 2016), so $w$ is
  greater than one..." -> this is the load-bearing wrong sentence. Replace with:
  the observer-to-broker gap is large and positive, but the returns-to-scale
  evidence (Bajari et al. 2018; Varian 2014; Neumann et al. 2019) shows aggregate
  raw-data value saturates and rejects super-additivity in variety, so the gap is
  attributed to market-position rent, not to super-additive aggregation; drop the
  Acquisti-Taylor-Wagman super-additivity attribution from this sentence (their
  aggregation-dependence result stands as context, but it does not establish
  super-additivity of the gap).
- **Proposition P2** (draft lines ~360-369): retitle from "the aggregation wedge
  is positive and super-additive" to "the observer-to-broker gap is positive and
  is rent, not super-additive aggregation". Replace the body so it asserts sign,
  order, and the rent attribution, and states the returns-to-scale evidence that
  rejects super-additivity; the proof obligation becomes resisting the hardening
  of the interval into a point *and* not re-importing the super-additive
  adjective. This aligns P2 with the S5-patched Section 5.2.
- **Section 5.4** (draft lines ~499-504): the "compounding thesis" prose. Keep it,
  but bind "compounding" to reputation explicitly and label it a conjecture; the
  tier multipliers remain illustrative. This surface is already honest about the
  multipliers; it needs only the reputation-scoping clause so "compounding" does
  not read as raw-data compounding.
- **Conclusion** (draft line ~604): "a stock the data subject can hold, invest in,
  compound, and transfer" -> "compound" reads as reputational per predicate (ii);
  a parenthetical or the patched predicate carries it.

### 2.4 Why this is a strengthening, stated for the record (GR-8)

The rejection of super-additivity is a result against a claim the project's prior
essays leaned on (the high-end value figure gestured at aggregation compounding).
It is reported here with the prominence of a positive result, per GR-8. It
improves the paper on two independent axes. First, the thin-market objection under
M2 is now answered without an unmeasured super-additivity assumption. Second, the
valuation no longer rests any load on a quantity the evidence denies; the surviving
"bigness" is rent, which is measured in kind (an atomisation discount and a
position discount) even though its magnitude is non-identified. A claim that
survives the deletion of its most convenient premise is stronger, not weaker.

---

## 3. M5 discharge: de-emphasise the ordinal, lead with the predicates

### 3.1 Recommendation

**Recommended: de-emphasise the "seventh" ordinal and lead with the five capital
predicates.** Justifying the IIRC frame for a WEIS audience is the weaker option.
The IIRC six-capitals model is a corporate sustainability-reporting taxonomy with
no standing in economics; to the target reader, human capital (Becker) and social
capital (Coleman; Putnam) are already economic objects, "manufactured" and
"natural" capital overlap with physical capital, and the count "six" carries no
economic content, so "seventh" reads as branding. The substantive claim, that
behavioural data satisfies the five capital predicates (returns, compounding
scoped to reputation, investability, opportunity access, cross-context transfer),
does not need the count and is legible without it. Retain the IIRC lineage as a
one-clause provenance note (it is where the ordinal came from, and the enumeration
error the project's prior lineage carried was corrected against it, Section 6),
but do not let the title or thesis lead with it.

### 3.2 Retitle (recommended to A4)

Current: *Behavioural Data as a Seventh Capital Class, and the Architecture that
Prices It.* The ordinal is in the title, which is the most branding-exposed
position. Recommended replacement, predicate-led:

> **Behavioural Data as Subject-Owned Capital: Five Predicates and the
> Architecture that Prices Them.**

Alternatives A4 may prefer: *Pricing Behavioural Data as a Capital Stock: A
Mechanism and an Architecture*; or *Subject-Owned Behavioural Capital: The
Predicates, the Rent, and the Architecture*. Any of these leads with the
substantive claim and drops the ordinal from the headline.

### 3.3 Drop-in replacement for the IIRC paragraph in Section 2

<!-- A2: REPLACE the current Section 2 paragraph beginning "The framing extends
an existing capital taxonomy..." with the following. It demotes the ordinal to
provenance and leads with the predicate claim. -->

> **The claim is a predicate claim, not an ordinal one.** The substantive thesis
> is that behavioural sovereignty satisfies the five defining predicates of a
> capital stock, set out and made testable in Section 3: it yields returns, it
> compounds (reputationally, and as a conjecture; raw-data aggregation does not,
> Section 5.2), it can be invested in, it gates opportunity access, and it
> transfers across contexts. The thesis stands or falls on those predicates, not
> on a place in any enumeration. For provenance we note that the framing arose by
> analogy with integrated-reporting practice, which recognises six capitals
> (Financial, Manufactured, Intellectual, Human, Social and Relationship, and
> Natural, per the International Integrated Reporting Council's framework); an
> earlier enumeration in the project's own prior lineage diverged from that list
> and is corrected here and not repeated (Section 6). That analogy is the origin
> of the "seventh" label and nothing more; the reporting taxonomy carries no
> economic weight, and the argument makes none rest on it. In the project's
> conjecture register the thesis is carried as an occupied, architectural-class
> conjecture (C55); we state it here as a thesis with a proof obligation, its five
> predicates being the content, and Section 3 the attempt to make them precise
> enough to test.

### 3.4 One-line consequence for the abstract and introduction

Where the abstract and introduction currently open on "a seventh capital class",
lead instead on the predicates and demote the ordinal to a subordinate clause,
for example: "Behavioural data satisfies the five defining predicates of a capital
stock (a framing that arose by analogy with the six-capital integrated-reporting
frame, from which the informal 'seventh capital' label derives)." A2 to reconcile
the two opening surfaces with the retitle; the ordinal survives only as
provenance, never as the headline.

---

## 4. Handoff

- **A2 (prose port):** apply Section 1 (new Section-2 subsection), Section 2.1-2.3
  (compounding predicate rescope + rent-capture bullet + the seven-surface
  super-additive sweep), and Section 3.3-3.4 (IIRC paragraph replacement +
  abstract/intro de-emphasis). Sequence 2.3 with the already-issued S5 patch
  (which owns Section 5.1/5.2); the S5 patch and this note together must leave the
  word "super-additive" attached to no surviving surface. Apply the retitle if A4
  approves.
- **A3:** the sovereign-regime share $s \in [0.3,0.7]$ (Section 5.1, S5 patch)
  should be cross-referenced to the P1 derivation once complete (M1), so the
  interior share is visibly a projection from the bargaining solution; the rent
  reframe does not change P1, but the "wedge capture -> rent capture" relabel means
  P1's price-discovery leg and the aggregator's rent-redistribution leg are two
  distinct mechanisms and should be kept distinct in the P1 write-up.
- **A4 (bib):** add six external citations, all tier-A permitted, all to be
  verified against the bib before release: Laudon, K.C. (1996), "Markets and
  Privacy", *Communications of the ACM* 39(9); Samuelson, P. (2000), "Privacy As
  Intellectual Property?", *Stanford Law Review* 52(5); Schwartz, P.M. (2004),
  "Property, Privacy, and Personal Data", *Harvard Law Review* 117(7); Purtova, N.
  (2015), "The Illusion of Personal Data as No One's Property", *Law, Innovation
  and Technology* 7(1) (A4 to confirm year/title against the property-rights
  companion piece); Prins, C. (2006), "Property and Privacy: European Perspectives
  and the Commodification of Our Identity", in *The Future of the Public Domain*;
  Delacroix, S. and Lawrence, N.D. (2019), "Bottom-up Data Trusts: Disturbing the
  'One Size Fits All' Approach to Data Governance", *International Data Privacy
  Law* 9(4). Also confirm the retitle (Section 3.2).
- **A5 (re-review):** M2 is answered by engagement (Section 1) and M5 by
  de-emphasis (Section 3); the rent integration (Section 2) both discharges the
  L134 correction and supplies the thin-market answer M2 asked for. m7 is
  discharged inside Section 1 (data-trust/cooperative attribution).
- **A0 / ledger:** append this note's disposition of M2/M5 and the rent
  integration; the CANON-LEVEL wedge finding is already filed (L133/L134) and is
  not reopened here. This note is a rehydration-layer engagement of external
  literature and a framing choice; it raises no new canon conflict (GR-10 not
  triggered).

---

## 5. Trace (GR-9)

- Section 1 (propertization engagement): external literature (Laudon 1996;
  Samuelson 2000; Schwartz 2004; Purtova 2015; Prins 2006; Delacroix and Lawrence
  2019), tier-A permitted; the architecture's two additions trace to E4-C01 (the
  separation and the predicates), E4-C06/C42 (non-transferable stake), and the
  imported guarantee WP-07 with Assumptions A1-A3 and $R(t)$ (E2-C01/C02, carried
  with preconditions and time-indexing per GR-7).
- Section 2 (rent integration): companion note
  weis_valuation_methodology_v2_empirical.md Sections 0/2.5/4.3-4.4; ledger L134
  (Run-3 finalisation); external returns-to-scale evidence (Bajari et al. 2018;
  Varian 2014; Neumann et al. 2019); reputation-appreciation scope traces to
  E4-C07 (design assumption / directional conjecture) and Proposition P5.
- Section 3 (M5): E4-C02 (the IIRC enumeration and its corrected form) and E4-C01
  (the five predicates); the ordinal-de-emphasis is a framing choice, not a canon
  claim.
- No fenced figure (678x, 31,000x, 70:1, 74x) and no asserted fiat value appears;
  external dollar anchors are cited by author and year only (GR-3). Every
  reconstruction mention carries A1-A3 and $R(t)$ (GR-7). The super-additivity
  rejection is reported with positive-result prominence (GR-8).

---

## Addendum (2026-07-16, L148): the soil figure, adopted downstream

The rent reframe this note argued is now organised by the First-Person soil ruling (L140): the seventh capital is land-based rentier capital, data as soil. The four legs map onto this note's material exactly: rent-by-position is Section 1's decomposition; value-as-share is the bargaining position this note hands to the interface; the erosion clock is Assumption A3 in its post-L145 form (the residual entropy H(X | B_t) falling against a fixed archive, WP-07 Cor 5.4b); and lease-the-harvest-not-the-land is the structural-inalienability answer (Section 2 of the main draft). The one surviving compounding channel remains the reputational one this note already scoped (E4-C07 / Proposition P5), and the honesty guard stands: the fertility conjecture must not re-import the aggregation intuition the evidence refuted. The figure entered the main draft at the Section 3 predicates block (draft-v4); this note needs no re-argument.
