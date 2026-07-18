# WP-14 · A5 review 1 · WEIS economist-referee pass

**Artifact:** `rehydrations/academic/weis_seventh_capital.md` (tier A, WEIS 2027 target, thrust T3)
**Reviewer persona:** economist referee, WEIS program committee (Workshop on the Economics of Information Security)
**Reviewed against:** WEIS venue conventions (format-free, interdisciplinary audience, data-markets economics). The reviewer has no access to the project canon and no goodwill toward it; the paper is judged on what it contains.
**Date:** 2026-07-14

---

## Summary (three sentences)

The paper argues that behavioural data is a distinct, subject-owned capital class whose near-zero surplus share is the equilibrium of a consent-interface bargaining game, that a bilateral propose-and-respond protocol (IEEE 7012) moves that share off the floor, and that an imported information-theoretic separation guarantee (time-indexed R(t)) is what keeps the stock from depreciating in the subject's hands. It is competently written, honestly self-limiting, cleanly positioned against Acquisti, the data-as-labour camp, and the WEIS lemons lineage, and its negative-results discipline is genuinely above the field median; on GR-7 conditioning and figure hygiene it is exemplary. It is not yet acceptable because its central economic proposition is deferred as a "proof obligation" rather than derived, its novelty claim ignores the decades-old personal-data-as-property literature that its "third position" restates, and its durability argument rests on a companion paper a referee cannot see.

**Overall rating: MAJOR REVISION.** No desk-reject grounds. Clears the pipeline's MAJOR-at-worst target, but only on the strength of the framing and the honesty discipline; the results are thin.

---

## Three strengths

1. **Honesty discipline is real and would be rewarded by a good PC.** Section 6 gives negatives the prominence of positives, names five open items with the measurement that would settle each, quarantines a source sentence it refuses to import (P4), and commits to reporting disconfirming results. This is rare and it is the paper's strongest asset. The reviewer would fight a co-referee who dismissed it.

2. **Positioning inside the literature is deliberate, not decorative.** Section 2 states the data-as-labour tension rather than eliding it, correctly reads the WTA/WTP endowment gap as a demand-side anchor, and answers the Spiekermann/Akerlof market-failure diagnosis with a mechanism rather than restating that data is valuable. The paper is inside the WEIS conversation, not beside it.

3. **The reconstruction guarantee is handled with unusual care.** Every invocation of R(t) travels with its preconditions (non-collusion, fixed adversary class) and its time-indexing, stated as numbered assumptions A1-A3 and reused by reference. The "guarantee expires -> the asset has a term structure" move is the paper's cleanest original economic idea.

---

## Weaknesses

### MAJOR

**M1 (contribution) — the central economic proposition is not derived; the Results section is a set of IOUs.**
Proposition P1 (the interface sets the appropriation share) is the paper's load-bearing economic claim, and it is not proved. The "Basis and obligation" text offers *two different* bargaining models as if interchangeable ("Nash bargaining with outside options, *or* the Rubinstein alternating-offers model"), then defers the actual derivation to a "proof obligation... (this is the point at which A3 owns the formal model)." P2, P3, P4, P5 are likewise stated with obligations deferred. A WEIS economist expects at least one self-contained, fully worked result. P1 needs no exotic conjecture — share→0 under a weak outside option is standard comparative statics — so there is no excuse not to write it down: fix the disagreement points, state the outside options for each interface explicitly, and derive the two directions. As it stands the paper is a framing plus a methodology plus a set of promises. **This is the single change that most improves acceptance odds** (see below).

**M2 (novelty/positioning) — the "third position" restates the personal-data-as-property literature without citing it.**
The paper's claimed-novel move is "data as a capital class *the subject owns*," presented as a deliberate third position between firm-owned capital and data-as-labour. This is propertization of personal data, and it has a large, decades-old, and largely *critical* literature that the paper does not engage: Laudon (1996, "Markets and Privacy"), Samuelson (2000, "Privacy as Intellectual Property?"), Schwartz (2004, "Property, Privacy, and Personal Data," Harv. L. Rev.), Purtova, Prins, and the data-trust / data-cooperative strand (Delacroix & Lawrence 2019). A referee who knows this literature will read the "seventh capital" as a rebranding of propertization and will want to know what the architecture adds that property rights alone do not — and why the well-rehearsed objections to propertization (alienability defeats the protection, thin markets, distributional regressivity) do not apply here. The paper cannot claim a third position while ignoring the literature that occupies it.

**M3 (foundation) — the durability argument rests on a companion paper the referee cannot evaluate, and the term-structure claim is asserted, not derived.**
The entire non-depreciation / term-structure argument depends on WP-07's imported guarantee, which is a black box to the reviewer. Two problems follow. First, at submission WP-07 must be a real, citable, available artifact, and the guarantee must be stated precisely enough (what R measures, in what metric, over what schedule) that a referee can judge whether the *economic* implications actually follow. Second, the paper draws an asset-pricing conclusion — "the asset has a term structure" — from the mere existence of a decay schedule R(t) whose shape and timescale it never gives. A term structure is a function of the schedule; importing that R(t) exists does not license a claim about the term structure without the schedule. Either give the schedule's shape (even qualitatively, with bounds) or downgrade "term structure" to "the stock has a finite, adversary-relative horizon."

**M4 (rigor regression) — the "roughly one order of magnitude" share-shift is asserted in prose with no interval, and is less rigorous than the paper's own methodology substrate.**
Section 5.1 concludes that the appropriation gap is "a shift of roughly one order of magnitude in the subject's captured share" and calls it "the defensible residue of the retired present-day figure." But the table cells backing it read only "near zero," "interior, well away from zero," and "small integer multiple" — no numeric endpoints. A "roughly 10x" claim with no interval on either endpoint is exactly the point-estimate-without-range failure the paper elsewhere disavows; the "one order of magnitude" is a smuggled semi-quantitative residue doing rhetorical work. Show the endpoint ranges (an extraction range and a sovereign range, each with its interval and source) so the 10x is a derived consequence of two stated intervals, or drop the magnitude and keep only the directional claim. Right now the paper is *less* quantitatively disciplined than the substrate it was ported from.

**M5 (framing legibility) — "seventh capital" indexes off an accounting-reporting construct that is arbitrary to an economist.**
The "seventh" counts off the IIRC Integrated Reporting six-capitals frame — a corporate-sustainability-reporting taxonomy, not an economics-of-capital construct. To the target audience, human capital (Becker) and social capital (Coleman, Putnam) are economic objects; "manufactured" and "natural" capital overlap with physical capital; the count "six" has no economic standing and neither does "seventh." As written, the headline reads as branding. Either justify why the IIRC frame is the right reference for an economics venue (and not, e.g., a human-capital or intangible-capital framing), or de-emphasise the ordinal and lead with the substantive claim (behavioural data has the five capital predicates), which does not need the count.

### MINOR

**m1 — M(u,y) is proposed and then never used.** The market-maturity gate is given a domain, units, and a candidate sigmoid, labelled honestly as a proposal, and then does no work: no proposition uses it, no comparative static turns on it, τ is unestimated. Either use it to derive something or cut it to a one-line remark. As is, it is decoration that invites the "unidentified free parameter" objection without buying anything.

**m2 — A1 (assumed non-collusion) and P4 (incentive-compatible non-collusion) may be circular or redundant, and the paper never connects them.** The imported guarantee *assumes* non-collusion (A1); Proposition P4 argues the two-token design makes non-collusion the earnings-maximising strategy. P4 is therefore plausibly what *discharges* A1 — the economic reason A1 is an assumption one may reasonably make rather than a hope. The paper treats them as unrelated. State the relationship: if P4 underwrites A1, that is a genuine synthesis and should be foregrounded; if A1 is assumed independently, P4 is decorative. Leaving it implicit invites the charge that the guarantee assumes what P4 pretends to prove.

**m3 — P4's no-exchange-pool assumption is empirically fragile and undefended.** Two domain-scoped units that both buy real tooling are fungible in practice through a shadow exchange rate; a secondary market defeats the "no swap pool" premise. The assumption carries the whole proposition and is asserted, not defended. Say why the pool is non-circumventable (or acknowledge that a shadow rate reintroduces the collusion incentive P4 is meant to remove).

**m4 — "super-additive" is conflated with "w > 1," and "bounded" is stated without a bound.** w > 1 (aggregate value exceeds atomised broker price) is not the same property as super-additivity (value of the union exceeds the sum of parts); the paper uses them interchangeably. Separately, w is repeatedly called "bounded" with no bound given; "bounded" without the bound is vacuous. Tighten both.

**m5 — the WTA/WTP gap is over-interpreted.** Calling the endowment ratio "the demand-side signature of the appropriation problem" loads a specific causal reading onto a gap with several competing explanations (endowment effect, uncertainty, framing, which the paper itself notes are "framing-sensitive"). Use it as consistent evidence, not as a signature of appropriation specifically.

**m6 — the near-zero extraction share ignores the value of the free service to the subject.** In a two-sided/zero-price market the subject receives the service in exchange; "captures almost none of the value" treats the data surplus in isolation from the consumption surplus the subject receives. An economist will ask whether s is near zero *net of the service's value to the subject*. Address the zero-price side (Rochet-Tirole-style), or scope the claim to the data surplus explicitly and concede it is not the subject's total welfare from the exchange.

**m7 — the subject-side aggregator is the MID / data-cooperative instrument and is under-attributed.** The "subject-side aggregator" is the mediator-of-individual-data / data-cooperative / data-trust construct; it is credited only to Arrieta-Ibarra et al. and Posner & Weyl. Cite the data-trust / data-cooperative strand (Delacroix & Lawrence 2019 and kin) so the instrument is placed in its own literature rather than presented as a fresh device.

---

## Desk-reject verdict

**No desk reject.** Grounds against: the paper is in scope for WEIS T3, positioned inside the relevant literatures, legible to a non-cryptographer, honest about its limits, and free of the figure-hygiene and unconditioned-ceiling sins that would justify summary rejection. Its defects are of contribution weight and completeness, which are what MAJOR revision is for.

## The single change that most improves acceptance odds

**Derive Proposition P1 in full.** Convert the central mechanism claim from a deferred "proof obligation" into a self-contained result: pick one bargaining model (not two), state the disagreement/outside-option points for the notice-and-consent interface and for the 7012 propose-and-respond interface, and derive share→0 in the first and an interior share in the second as comparative statics. That one worked result changes the paper from "a framing plus a methodology plus promises" into "a framing plus a methodology plus a proven mechanism," which is what a WEIS PC needs to see to move from MAJOR to accept-class. Everything else on this list is secondary to that.

---

*A5 economist-referee pass, review 1. BLOCKING: 0. MAJOR: 5 (M1-M5). MINOR: 7 (m1-m7). Verdict: MAJOR REVISION. No desk-reject grounds. Findings mirrored to the critiques ledger at L131.*
