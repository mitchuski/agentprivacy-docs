---
artifact: weis-seventh-capital-skeleton
tier: A
venue: WEIS-2027
wp: WP-14
role: A12
date: 2026-07-14
thrust: T3 (Value and Governance / economics)
anonymisation: >
  Non-anonymised first pass (2027 CFP not yet published; A13 re-checks
  2026-11-01). Structured so names and first-person self-citation swap to
  third-person is a later mechanical pass, not a rewrite. The 2026 CFP used
  double-anonymous review.
extraction_basis: >
  E4-seventh-capital c01, c02, c03, c04, c05, c06, c07, c08, c09, c10,
  c11, c12. Companion artifact: weis_valuation_methodology_note.md (the
  Section 5 substrate). Imported result: WP-07 linear-cap theorem
  (information-theoretic guarantee, cited not re-proven).
template_target: templates/submission/preprint/sections/00..07
status: skeleton-v1 (A12; awaiting A5 economist-referee scope pass)
handoff: A2 (prose), A3 (M(u,y) and theorem legs), A4 (bib), A5 (referee), A0 (ledger, canon-level)
---

<!-- ============================================================
A12 SKELETON NOTE (pipeline internal; strip at release)
Section-by-section outline for WP-14, mapped one-to-one onto the eight
preprint stubs in templates/submission/preprint/sections/. Each section
below states: PURPOSE, the E4 CLAIMS it carries, and the PROOF/MEASUREMENT
OBLIGATION it owes. GR discipline: no fenced figure (678x/31,000x) is
reproduced (GR-3); no confidence percentage is asserted (GR-2, tier A); any
ceiling/R<1 statement carries preconditions and R(t) in the same passage
(GR-7); negative results carry equal prominence (GR-8); GR-4 vocabulary
throughout (boundary agent S, delegation agent M, data subject X; no City
vocabulary, no emoji).
============================================================ -->

# WP-14 skeleton: Behavioural Data as a Seventh Capital Class, and the Architecture that Prices It

Target venue: WEIS 2027 (interdisciplinary economics-of-information-security
audience, format-free, no page limit). Thrust T3. Home thesis: behavioural
data is a distinct capital class; architectural separation of an observing
boundary agent S from an acting delegation agent M yields
information-theoretic rather than policy-promise guarantees; those
guarantees are time-indexed R(t) and expire on a computable schedule; the
resulting sovereignty has a market price currently paid to someone else.

Write for the economist and the security economist, not the cryptographer.
The information-theoretic result is imported and cited (WP-07); this paper's
own contribution is the economic reframing, the valuation methodology, and
the market mechanism.

---

## Section map (preprint stub -> WP-14 section)

### 00_abstract.tex -> Abstract

- **Purpose.** Verdict-first, one page. State on the first line that
  behavioural data is a distinct capital class whose returns are currently
  appropriated by the observer, that the appropriation is set by the consent
  interface as a bargaining protocol, and that an architectural separation
  supplies an information-theoretic (imported, time-indexed) rather than
  policy guarantee. State the valuation result as a share and a wedge with
  ranges, never as a fenced ratio and never in fiat.
- **E4 claims carried.** C01 (capital class), C03 (extraction vs
  sovereignty), C04 (the rebuilt valuation, in its share/wedge form), C10
  (consent interface / IEEE 7012), C11 (structure and economics enforce the
  separation).
- **Obligation.** No 678x, no 31,000x, no fiat figure. The main economic
  claim and the named market mechanism both appear on the first page. The
  imported guarantee is cited as imported and stated with its time index.

### 01_introduction.tex -> Introduction and contributions

- **Purpose.** Arrive as an implementer facing the appropriation problem in
  deployed data markets, not as a framework author. Motivate from the
  observed fact that the subject captures a near-zero share of the surplus
  her behavioural data generates, and that the consent interface is the
  mechanism that sets that share. State the main result informally with
  preconditions named: under a bilateral bargaining protocol with a credible
  outside option and a Sybil-resistant quality signal, and under the
  structural separation whose guarantee WP-07 supplies, the subject's share
  can move into a bargaining regime; the guarantee is time-indexed and
  expires. Close with a numbered contribution list, each item naming its
  section.
- **E4 claims carried.** C01, C03, C04, C10; forward-reference C11.
- **Obligation.** Contributions numbered and section-anchored. The
  motivation is the deployed-market problem; the model earns its place by
  what it predicts about s. No claim is strengthened for flow (GR-8).
  Candidate contributions:
  1. A capital-class formalisation of behavioural data with its five
     properties made precise (Section 3).
  2. A valuation methodology replacing two fenced canonical figures with a
     bounded appropriation share and a non-identified aggregation wedge,
     every assumption in-table, sensitivity as ranges (Section 5).
  3. A market mechanism, consent-interface bargaining plus subject-side
     aggregation plus a non-transferable quality stake, through which the
     value is realised or lost (Sections 4 and 5).
  4. A statement of the architectural guarantee as imported, time-indexed,
     and expiring, with the economic reading of its expiry (Sections 3, 6).

### 02_related_work.tex -> Related work

- **Purpose.** Position inside, not beside, three literatures: the
  economics of privacy (Acquisti, Taylor and Wagman 2016; Acquisti, John
  and Loewenstein 2013); the data-as-labour versus data-as-capital debate
  (Arrieta-Ibarra, Goff, Jimenez-Hernandez, Lanier and Weyl 2018; Posner and
  Weyl 2018; Lanier 2013); and personal-data-market design and its failures
  (Spiekermann, Acquisti, Bohme and Hui 2015; Anderson 2001; Akerlof 1970).
  State the paper's third position: data as an owned capital stock, not a
  labour flow, with the returns reassigned to the subject by architecture.
  Correct the IIRC six-capital enumeration here.
- **E4 claims carried.** C02 (six-capital reference frame, corrected against
  IIRC); positions C01 and C03 against the literature.
- **Obligation.** The IIRC enumeration is stated correctly (Financial,
  Manufactured, Intellectual, Human, Social and Relationship, Natural); the
  whitepaper's divergent list is not repeated. The data-as-labour tension
  is argued explicitly, not elided. Every positioning claim cites the
  external work, not the canon (GR-4, GR-9).

### 03_model_preliminaries.tex -> Model and preliminaries

- **Purpose.** Fix vocabulary and define every economic object before use.
  Define: data subject X; boundary agent S and delegation agent M;
  structural context erasure between invocations; the appropriable surplus
  and the subject share s in [0, 1]; the aggregation wedge w; the
  market-maturity gate M(u, y) with domain, units, and boundary behaviour
  (from the methodology note Section 5); the capital-class properties
  (returns, compounding, investability, opportunity access, cross-context
  transfer) stated as measurable predicates. Name the preconditions of the
  imported guarantee as numbered assumptions: non-collusion, fixed adversary
  class, and time-indexing R(t) (GR-7). State the threat model: a passive
  observer that appropriates surplus; the adversary class against which the
  imported guarantee holds.
- **E4 claims carried.** C01 (capital properties made precise), C03
  (extraction/sovereignty as two regimes of s), C05 (M(u,y) defined), C06
  (non-transferable proof-of-practice resource defined as the quality
  stake).
- **Obligation.** Every symbol defined before use; each architectural
  precondition a numbered Assumption so Section 4 can reference it (per the
  stub's instruction). M(u,y) is introduced with its domain and units and
  labelled a proposed operationalisation, not canon. No ceiling statement
  appears without its preconditions and R(t) (GR-7).

### 04_theorems.tex -> Results (economic propositions)

- **Purpose.** The economic results, each stated with preconditions,
  conjectures carried with proof obligations and no confidence band. The
  information-theoretic guarantee itself is imported from WP-07 and cited,
  not re-proven here.
- **E4 claims carried and their obligation:**
  - **P1 (appropriation share).** Under notice-and-consent with outside
    option equal to service exclusion, the subject's equilibrium bargaining
    share s tends to zero; under a bilateral propose-and-respond protocol
    with a credible outside option, s moves into an interior range.
    *Obligation:* state the bargaining model (Nash or Rubinstein), the
    outside-option assumption, and prove the two comparative-statics
    directions. Carries C04, C10.
  - **P2 (aggregation wedge).** The value of aggregated-and-modelled
    behavioural data is super-additive over atomised records; the wedge w is
    positive and bounded. *Obligation:* state the complementarity assumption
    and cite the empirical support (Acquisti-Taylor-Wagman 2016); assert
    sign and super-additivity only, not a point value. Carries C04.
  - **P3 (Sybil-resistant quality signal).** A non-transferable,
    non-purchasable proof-of-practice resource resists the Sybil attack that
    unravels a personal-data market toward a lemons equilibrium.
    *Obligation:* register conjecture C42, stated as a conjecture with its
    proof obligation and no confidence percentage; the cost-to-forge
    argument made explicit; the open step named. Carries C06/C42.
  - **P4 (incentive-compatibility of separation).** Two domain-scoped
    non-swappable tokens make maintaining the S/M separation the
    earnings-maximising strategy, where a single unified token would make
    information-sharing between the agents earnings-maximising.
    *Obligation:* state as a mechanism-design claim with the no-swap-pool
    assumption; the GR-7 hazard in the source (the collapsed-ceiling
    sentence) is NOT imported; the reconstruction ceiling itself lives in
    WP-07 with its preconditions and is cited there, time-indexed. Carries
    C11.
  - **P5 (appreciation versus depreciation).** Reputation capital is claimed
    to appreciate while surveillance data depreciates under freshness decay.
    *Obligation:* stated as a directional conjecture (C07), unmeasured,
    honesty-labelled; the unforgeability argument (three simultaneous
    constraints) stated as a design claim, not a proof. Carries C07.
- **Obligation (section-level).** No confidence percentages (GR-2). Every
  conjecture carries a named proof obligation and its unstarted step. The
  imported guarantee is cited, and any statement touching R<1 is
  time-indexed with its preconditions in the same passage (GR-7).

### 05_evaluation.tex -> Valuation methodology and evaluation

- **Purpose.** The rebuilt valuation, drawn directly from
  weis_valuation_methodology_note.md. Present the appropriation-share table
  and the aggregation-wedge table with every assumption in the same table
  and sensitivity as ranges. Instantiate the market mechanism: 7012
  propose-and-respond price discovery, subject-side aggregator for the
  wedge, non-transferable stake as the quality signal. Present the
  tier-ladder multipliers as illustrative design parameters, explicitly not
  measured returns. Present the independent second-substrate build (the
  evidence-graph anti-score, C09) as independent derivation, never as
  competition. Evaluation is analysis of published measurements (Acquisti
  WTA/WTP ranges, broker-price ranges), not new experiments.
- **E4 claims carried.** C04 (the rebuild lives here), C08 (tier
  multipliers, illustrative), C09 (evidence-graph anti-score, independent
  derivation), C12 (compression-fidelity-as-assessment; the 70:1 and 1000:1
  ratios stay fenced, the mechanism is the claim).
- **Obligation.** Every number carries its assumptions in-table; ranges not
  points; measured quantities and projections are visibly separated (GR-8);
  678x and 31,000x are not reproduced; no fiat figure; the 70:1 and 1000:1
  compression ratios are not reproduced as facts. C09 travels with its W3C
  Verifiable Credentials citation and the independent-derivation flag.

### 06_threats_to_validity.tex -> Threats to validity

- **Purpose.** Give the negative results the same prominence as the
  positive ones (GR-8). State every fence.
- **E4 claims carried (as limits).** Limits of C04 (share and wedge not
  point-identified; the sovereign-regime share is a projection, not a
  measurement), C05 (M(u,y) is a proposed operationalisation, not canon and
  not measured), C07 (appreciation is directional and unmeasured), C08 (tier
  multipliers are illustrative, not measured returns), C06/C42 (Sybil
  resistance is an open conjecture), C02 (IIRC enumeration divergence,
  flagged CANON-LEVEL).
- **Obligation.** The imported guarantee is time-indexed and expires: state
  R(t) with its preconditions (non-collusion, fixed adversary class) in the
  same passage, and cite WP-07 for the guarantee itself; do not restate a
  static ceiling (GR-7). State the reporting commitment: a measured result
  against the predictions (for instance a sovereignty market that fails to
  move s) is reported with equal prominence (GR-8). Name the aggregation
  wedge's non-identification as a live threat to any quantitative reading.

### 07_conclusion.tex -> Conclusion

- **Purpose.** The decomposition: behavioural data is a capital class; the
  guarantee that makes the stock non-depreciating in the subject's hands is
  architectural, imported, and dated; the sovereignty has a market price
  currently appropriated by the observer; the market mechanism that would
  repatriate it is named and buildable. State the open items as future
  work.
- **E4 claims carried.** Synthesis of C01, C03, C04, C10, C11; the imported
  guarantee's economic reading.
- **Obligation.** Open items named precisely: identification of the
  aggregation wedge; estimation of M(u,y) and its time constant; empirical
  test of the Sybil-resistance conjecture (C42); measurement of the
  reputation-appreciation claim (C07); observation of a deployed sovereignty
  market moving s. The paper closes in the decomposed, conditional, dated
  form in which its claims are true.

---

## Cross-cutting obligations (apply to every section)

1. **No fenced figure.** 678x, 31,000x, 70:1, 74x, and any fiat figure
   appear nowhere (GR-3, L057). The valuation is shares, wedges, and ranges.
2. **No confidence percentages** in asserted claims (GR-2, tier A).
   Register conjectures (C42, C95, C07-related) are stated as conjectures
   with proof obligations, by name, without bands.
3. **Time-indexing** of any reconstruction or ceiling statement, with
   non-collusion and fixed-adversary-class preconditions in the same passage
   (GR-7). The guarantee is imported from WP-07 and cited there.
4. **Vocabulary** is boundary agent S, delegation agent M, data subject X,
   structural context erasure; no City-of-Mages vocabulary, no emoji (GR-4).
5. **Trace or delete** (GR-9): every claim traces to an E4 line; the artifact
   cites the extraction and the external literature, never the narrative
   canon directly.
6. **Honesty prominence** (GR-8): the limits section is proportionate; a
   result against prediction is reported with the same prominence as a
   confirmation, in writing.

## Handoff

- **A2:** prose port of Sections 1, 2, 6, 7; the data-as-labour tension in
  Section 2 is the delicate passage.
- **A3:** review the M(u,y) form (methodology note Section 5) and the P1/P4
  theorem legs (bargaining model, mechanism-design claim).
- **A4:** verify and add the ten bibliography entries listed in the
  methodology note Section 8.
- **A5:** economist-referee pass on the methodology note and this skeleton;
  target MAJOR-at-worst.
- **A0:** file the proposed CANON-LEVEL ledger entry (methodology note
  Section 6): the 678x/31,000x non-survival and the IIRC enumeration
  correction.
- **A13:** re-check the WEIS 2027 CFP on 2026-11-01 for anonymisation and
  format requirements.
