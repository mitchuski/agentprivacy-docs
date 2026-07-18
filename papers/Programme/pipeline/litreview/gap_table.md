---
artefact: litreview-runtime-output
runtime: weis-litreview-runtime
run_id: wf_ba400906-67b
brief: chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md
target: WP-14 (weis_seventh_capital, WEIS 2027)
date: 2026-07-15
register: standards
generated: true
note: "Generated artifact. Do not hand-edit; fix the runtime inputs and rebuild. Verdict spread: 0 VALIDATED / 5 MIRAGE / 0 BLOCKED across 5 candidates, 20-item corpus. CTR-series IDs are candidates only; assignment is the First Person's."
---

# Gap table: the privacy-value corpus on unit-of-analysis x economic-framing

## Gap grid: unit_of_analysis x economic_framing

Corpus n = 20. Each cell lists the corpus items that land there. Short keys resolve to full citations in the bibliography.

| unit \ framing | none | cost_model | incentive_model | market_pricing |
|---|---|---|---|---|
| **subject_impact** | ISO/IEC 29134:2017; ISO/IEC 29100:2011 | (empty) | Delacroix-Lawrence 2019 | Laudon 1996; Samuelson 2000; Schwartz 2004; Purtova 2015/17; Prins 2006; Arrieta-Ibarra et al. 2018; Posner-Weyl 2018; Acquisti-John-Loewenstein 2013; Collis et al. 2022; Beresford-Kuebler-Preibusch 2012; Grossklags-Acquisti 2007 |
| **system_property** | Dwork 2006; Sweeney 2002; Smith 2009 | (empty) | Anderson 2001 | **(empty, 0 items)** |
| **both** | (empty) | (empty) | Acquisti-Taylor-Wagman 2016 | Spiekermann et al. 2015 |
| **unclear** | (empty) | (empty) | (empty) | (empty) |

Row/column totals: subject_impact = 14, system_property = 4, both = 2, unclear = 0. Column totals: none = 5, cost_model = 0, incentive_model = 3, market_pricing = 12.

## The load-bearing cell: {system_property x market_pricing}

**Exact membership count in the corpus: 0.**

No item in this 20-paper corpus both (a) takes the unit of measurement to be a property of the release mechanism or system, rather than the reported impact on a named subject, and (b) prices that property as a market quantity. The four system_property items either carry no economic framing at all (Dwork, Sweeney, Smith are formal leakage or indistinguishability bounds with `economic_framing = none`) or frame economics as incentive misalignment rather than pricing (Anderson, `incentive_model`). Conversely, every market_pricing item measures a subject-reported valuation, a legal entitlement of a named subject, or a market-position quantity attached to a subject, not a system property.

**What this means for the WEIS contribution claim.** This emptiness is a genuine structural feature of the assembled corpus, and it motivates the PVM position, but under discipline D2 it must be reported as `not_found_in_corpus(system_property x market_pricing, this 20-item corpus)` and NOT as "no prior work prices a system property." The adjudicated verdict on CTR-LR-02 is explicit that the literal in-corpus emptiness is a corpus-selection artefact: the external differential-privacy-markets strand (Ghosh-Roth 2011 and successors) does price the DP disclosure bound as a traded commodity and therefore occupies this cell outside the corpus window. Confidence that the cell is empty *within this corpus*: high (certain by inspection). Confidence that the cell is empty *in the field*: refuted (see CTR-LR-02 verdict). The defensible WEIS framing is therefore narrower than "we are first to price a system property": it is "we price a finite, adversary-relative, time-drifting reconstruction bound held as inalienable subject-owned capital," which is the residual that survives adjudication.

## Second grid: adversary_model coverage

| adversary_model | count | items |
|---|---|---|
| **explicit** | 2 | Dwork 2006; Smith 2009 |
| **implicit** | 7 | Samuelson 2000; Delacroix-Lawrence 2019; Acquisti-Taylor-Wagman 2016; Spiekermann et al. 2015; Anderson 2001; Sweeney 2002; ISO/IEC 29134:2017 |
| **absent** | 11 | Laudon 1996; Schwartz 2004; Purtova 2015/17; Prins 2006; Arrieta-Ibarra et al. 2018; Posner-Weyl 2018; Acquisti-John-Loewenstein 2013; Collis et al. 2022; Beresford-Kuebler-Preibusch 2012; Grossklags-Acquisti 2007; ISO/IEC 29100:2011 |

Reading: an explicit adversary appears only in the two pure formal-metric papers (Dwork, Smith), both of which have `economic_framing = none`. Every market_pricing item has an absent or (in two survey cases) merely implicit adversary. The intersection {explicit adversary} x {market_pricing} is also empty in the corpus. This reinforces the same gap from a different axis: adversary-relativity and pricing do not co-occur in any corpus item, which is exactly the join the PVM reconstruction bound R(t) attempts, and exactly the join that the CTR-LR-05 residual (adversary-relative drifting horizon carried into a capital valuation) is scoped to.
