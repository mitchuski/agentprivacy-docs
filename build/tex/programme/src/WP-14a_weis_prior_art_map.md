---
title: "WEIS-specific prior-art map for the seventh-capital thesis"
subtitle: "WP-14 · tier A · WEIS-2027 · 2026-07-14"
author: "The Privacy-is-Value Research Programme"
date: "2026-07-14"
---
# WEIS Prior-Art Map — WP-14 (seventh capital / S–M separation / priced-elsewhere)

**Role discipline (A10):** external, resolvable citations only. Every entry below was web-verified for author, title, year and venue against a primary or near-primary record (archive PDF, publisher landing page, or author page). Entries I could not fully confirm are marked **UNVERIFIED**. No citation is invented. Vocabulary follows GR-4: the observing agent is the **boundary agent S**, the acting agent is the **delegation agent M**.

**Our thesis, stated for positioning (WP-14):**
1. behavioural/personal data is a distinct capital class (the "seventh capital");
2. architectural separation between an observing **boundary agent S** and an acting **delegation agent M** yields information-theoretic (not policy) guarantees, time-indexed as R(t);
3. privacy has a market price that is currently captured by a party other than the data subject.

Relation tags used: **AGREES** · **EXTENDS-WE-BUILD-ON** · **CONTRADICTS-WE-MUST-ANSWER** · **GAP-WE-FILL**.

---

## Coverage statement (no silent gaps)

WEIS per-year sites use two live patterns: `weis<YEAR>.econinfosec.org/` (accepted-papers/program pages) and `econinfosec.org/archive/weis<YEAR>/papers/<n>.pdf` (per-paper PDFs). Findings:

- **Fully enumerated accepted-paper lists (paper-by-paper):** WEIS 2022 and WEIS 2023. WEIS 2023's full accepted list contains **no** privacy-valuation / personal-data-market paper (nearest-adjacent: Cecere/Jean/Lefrere/Tucker on platform regulatory compliance). WEIS 2022 contains the Collis et al. valuation paper (entry P3) plus Telang/Garg on app privacy-label demand (adjacent, not valuation).
- **Confirmed archive PDF hosting (individual papers retrieved or path-verified):** WEIS 2007 (entry P1), WEIS 2015 (entry P2).
- **NOT enumerated paper-by-paper:** WEIS 2002–2006, 2008–2014, 2016–2021, 2024, 2025. For these years I searched by author and topic rather than walking every accepted list, so a non-flagship privacy-economics paper in those years could exist that this map does not name. The flagship privacy-valuation lineage (Acquisti and collaborators; the privacy-paradox field experiments) is captured across the whole span via targeted search.
- **Tooling limitation (not a coverage gap):** the WebFetch renderer cannot parse PDF binaries in this environment (no poppler), so numeric results were taken from readable HTML mirrors, publisher landing pages, author-hosted abstracts, and press summaries rather than from the PDF body directly. Where a number rests on a secondary summary rather than the paper's own table, the entry says so.
- **Archive index page** `econinfosec.org/weis-archive/` lists editions 2002–2023 but carries no per-paper metadata; it returned 403 on the `/archive/weis2015/` directory index even though individual `/archive/weis2015/papers/*.pdf` files resolve.

---

## Verified entries

### P1 — Grossklags & Acquisti, WEIS 2007
- **CITATION:** Jens Grossklags, Alessandro Acquisti. "When 25 Cents Is Too Much: An Experiment on Willingness-To-Sell and Willingness-To-Protect Personal Information." *6th Workshop on the Economics of Information Security (WEIS 2007)*, Pittsburgh, June 2007. Archive PDF: `https://econinfosec.org/archive/weis2007/papers/66.pdf` (also mirrored at `cs.cit.tum.de/.../2007-WEIS-Grossklags-Acquisti.pdf`). VERIFIED (author, title, year, WEIS venue all confirmed across archive path, TUM mirror, Semantic Scholar, DBLP/researchr).
- **FINDING:** Yes/no offers and open valuations show a strong majority preferring money over data even when the monetary advantage of releasing (or not protecting) is very small; measured willingness-to-protect (a WTP) is far below willingness-to-accept-to-sell (a WTA).
- **RELATION:** EXTENDS-WE-BUILD-ON — this is the WEIS-native root of "subjects under-price their own data," which is the demand-side half of our "price captured by someone else." It also sets up a **CONTRADICTS-WE-MUST-ANSWER** tension: if subjects value data at cents, a referee will ask how it can be a distinct capital class. Our answer must separate individual WTP from the aggregate market price.
- **HANDLE FOR VALUATION:** the paper's own threshold framing is the "25 cents" of the title (a per-decision offer at which subjects still sold). Exact table figures were not extracted from the PDF body (binary-render limit); treat the 25-cent figure as the load-bearing quotable and pull precise means/medians from the PDF in the valuation rebuild.

### P2 — Cofone, WEIS 2015
- **CITATION:** Ignacio N. Cofone. "The Value of Privacy: Keeping the Money Where the Mouth Is." *WEIS 2015*, Delft. Archive PDF: `https://econinfosec.org/archive/weis2015/papers/WEIS_2015_cofone.pdf`. VERIFIED (title, author, WEIS 2015 venue via archive path and Semantic Scholar).
- **FINDING:** Argues the privacy paradox is explicable inside a rational-choice framework; low willingness-to-pay for privacy explains the thin market for privacy-enhancing technologies (uses Tor's free-but-used status and Facebook as case studies).
- **RELATION:** CONTRADICTS-WE-MUST-ANSWER — if low WTP is rational rather than a market failure, an architectural remedy looks unnecessary. We must answer by distinguishing a rational low WTP for *policy* privacy from an information-theoretic leakage bound R(t) that a rational subject cannot purchase at any price under the current architecture. Partial **AGREES** on "someone else captures the value."
- **HANDLE FOR VALUATION:** cites Facebook as ~850 million users generating a firm valuation of ~US$100 billion (2015 framing) as an illustration of subject-generated value accruing to the platform. This is a scene-setting figure from a secondary case description, not an estimated per-user price; use only as context.

### P3 — Collis, Moehring, Sen & Acquisti, WEIS 2022  ★ strongest empirical anchor
- **CITATION:** Avinash Collis, Alex Moehring, Ananya Sen, Alessandro Acquisti. "Information Frictions and Heterogeneity in Valuations of Personal Data." *WEIS 2022*. PDF: `https://weis2022.econinfosec.org/wp-content/uploads/sites/10/2022/06/weis22-collis.pdf`; SSRN 3974826 ("...Valuations of Social Media Data", Nov 2021). VERIFIED (accepted-papers list, PDF URL, SSRN, CMU/Penn summaries).
- **FINDING:** Incentive-compatible mechanism elicits how much compensation users require to share their Facebook data; finds large dispersion and systematic under-valuation by women, Black, and low-income users; an information treatment compresses the dispersion.
- **RELATION:** EXTENDS-WE-BUILD-ON (empirics) and **GAP-WE-FILL** (mechanism). Their remedy for the frictions is *information provision* — a policy lever. Ours is *architecture* (S–M separation). Their demographic dispersion is direct evidence that consent/notice regimes misprice, which our information-theoretic guarantee sidesteps.
- **HANDLE FOR VALUATION (quote precisely):** median WTA to share **all** Facebook data = **US$750** (YouGov sample) and **US$1,000** (DDP sample), one-time (not monthly), 2021 elicitation. Demographic medians (YouGov): Black **$500** vs White **$1,000**; Female **$600** vs Male **$1,000**. (Figures via the Penn Carey Law summary of the paper; confirm against the PDF's tables in the rebuild.)

### P4 — Acquisti, John & Loewenstein, "What Is Privacy Worth?" (WEIS-adjacent)
- **CITATION:** Alessandro Acquisti, Leslie K. John, George Loewenstein. "What Is Privacy Worth?" *Journal of Legal Studies* 42(2), Article 1, 2013 (DOI 10.1086/671754). Earlier presented as a workshop paper (WISE 2009 version at `pages.stern.nyu.edu/~bakos/wise/papers/wise2009-6a1_paper.pdf`; author copy at heinz.cmu.edu). VERIFIED (JLS volume/issue, three authors, year via ideas.repec, chicagounbound, author page). Venue is JLS, not WEIS — labelled adjacent.
- **FINDING:** Field experiment with a $10 anonymous vs $12 identified gift-card design shows large endowment and order effects: subjects endowed with anonymity demand far more to give it up (WTA) than subjects without it will pay to obtain it (WTP); valuations cluster at focal/extreme points.
- **RELATION:** EXTENDS-WE-BUILD-ON — instability and framing-dependence of privacy valuations undercut consent/notice (policy) guarantees and motivate a guarantee that does not depend on subject valuation at all, i.e. our information-theoretic R(t).
- **HANDLE FOR VALUATION:** design constants are exact and quotable: **$10 anonymous card** vs **$12 identified card** (a **$2** wedge to switch); WTA:WTP disparity reported as roughly **5×** (secondary summaries; verify the exact ratio in the JLS tables for the rebuild).

### P5 — Beresford, Kübler & Preibusch, "Unwillingness to Pay for Privacy" (adjacent)
- **CITATION:** Alastair R. Beresford, Dorothea Kübler, Sören Preibusch. "Unwillingness to Pay for Privacy: A Field Experiment." *Economics Letters* 117(1): 25–27, 2012; earlier IZA Discussion Paper 5017 (2010) and WZB working paper. VERIFIED (IZA, SSRN 1634484, ScienceDirect, WZB PDF). Venue is Economics Letters / IZA, not WEIS — adjacent, but the canonical privacy-paradox field experiment.
- **FINDING:** Subjects buy a DVD from one of two otherwise-identical stores differing only in how much personal data they demand. With a **€1** discount at the data-hungry store, almost everyone gives up the extra data; with equal prices, purchases split roughly evenly despite stated privacy concern.
- **RELATION:** CONTRADICTS-WE-MUST-ANSWER — the hardest empirical for our capital-class claim ("people sell everything for €1"). We answer: market price ≠ subject WTP; the seventh-capital claim concerns the aggregate value captured downstream, not the subject's marginal willingness to pay at the point of sale.
- **HANDLE FOR VALUATION:** the **€1** price wedge that flips nearly all buyers to the data-demanding store (2010–2012). Quotable as an upper bound on point-of-sale subject WTP.

### P6 — Acquisti, Taylor & Wagman, "The Economics of Privacy" (adjacent survey — must-cite)
- **CITATION:** Alessandro Acquisti, Curtis R. Taylor, Liad Wagman. "The Economics of Privacy." *Journal of Economic Literature* 54(2): 442–492, 2016 (DOI 10.1257/jel.54.2.442). VERIFIED (AEA, ideas.repec, author PDF, Duke Scholars). Adjacent venue (JEL) but authored by WEIS-community principals and is THE field survey.
- **FINDING:** Canonical survey of the economic value and consequences of protecting vs disclosing personal information, the trade-offs, externalities, and consumer decision-making anomalies.
- **RELATION:** GAP-WE-FILL + EXTENDS-WE-BUILD-ON — the survey treats personal data as an economic good with externalities and information asymmetries; it does **not** frame data as a distinct capital class, and it contains no architectural or information-theoretic (R(t)) treatment. This is the map against which our novelty is measured; a referee will expect us to locate ourselves inside it.
- **HANDLE FOR VALUATION:** survey, not a primary estimate. Use it to source the accepted range of WTP/WTA estimates rather than as a single number.

### P7 — Acquisti & Grossklags, "Privacy and Rationality in Individual Decision Making" (WEIS 2004 origin)
- **CITATION:** Alessandro Acquisti, Jens Grossklags. "Privacy and Rationality in Individual Decision Making." *IEEE Security & Privacy* 3(1): 26–33, 2005 (DOI 10.1109/MSP.2005.22). An earlier version was presented at WEIS 2004. VERIFIED for the IEEE S&P publication (IEEE/ACM DL, PSU, Semantic Scholar); the WEIS 2004 presentation attribution is asserted by SSRN/author records — mark the WEIS-2004 line **UNVERIFIED** and cite the IEEE venue as primary.
- **FINDING:** Empirically and theoretically documents bounded rationality and information asymmetry in privacy decisions; subjects behave inconsistently with rational-agent models.
- **RELATION:** EXTENDS-WE-BUILD-ON — foundational reason to replace consent/notice (which presumes a rational, informed subject) with an architectural guarantee that holds regardless of subject rationality.
- **HANDLE FOR VALUATION:** methodology constants only: a **US$16** lump-sum for an online survey, **119** respondents (May 2004). Not a data-value estimate.

### P8 — Arrieta-Ibarra, Goff, Jiménez-Hernández, Lanier & Weyl, "Should We Treat Data as Labor?" (adjacent — rival framing)  ★ key positioning fight
- **CITATION:** Imanol Arrieta-Ibarra, Leonard Goff, Diego Jiménez-Hernández, Jaron Lanier, E. Glen Weyl. "Should We Treat Data as Labor? Moving Beyond 'Free'." *AEA Papers and Proceedings* 108: 38–42, 2018 (DOI 10.1257/pandp.20181003). VERIFIED (AEA, SSRN 3093683, EconPapers vol/pages).
- **FINDING:** Argues data currently treated as free capital should instead be treated (at least partly) as **labour** — a compensated factor input — to restore a functioning market for user contributions.
- **RELATION:** CONTRADICTS-WE-MUST-ANSWER — the single closest rival to our framing. They say data is *labour*; we say it is a distinct *capital* class ("seventh capital"). Our related-work section must draw the labour-vs-capital line explicitly and say why an information-theoretic boundary (S–M) changes the accounting in a way a labour-compensation scheme does not.
- **HANDLE FOR VALUATION:** conceptual, no primary estimate.

### P9 — Posner & Weyl, "Data as Labor" (Radical Markets) (adjacent — book form of P8)
- **CITATION:** Eric A. Posner, E. Glen Weyl. "Data as Labor," chapter 5 in *Radical Markets: Uprooting Capitalism and Democracy for a Just Society*. Princeton University Press, 2018. VERIFIED (De Gruyter/Princeton chapter listing, radicalmarkets.com). Book, not a venue paper.
- **FINDING:** Full-length statement of the data-as-labour programme, including data-union / data-cooperative institutions as the labour-market analogue.
- **RELATION:** CONTRADICTS-WE-MUST-ANSWER — same axis as P8; cite the book once as the canonical long-form and engage P8 as the citable venue paper.
- **HANDLE FOR VALUATION:** conceptual.

---

## Adjacent / watch-list (named, not yet load-bearing)

- **Cecere, Jean, Lefrere & Tucker**, "Trade-offs in Automating Platform Regulatory Compliance By Algorithm," WEIS 2023 — the only 2023 paper touching platform data governance; not valuation. VERIFIED (2023 accepted list).
- **Telang & Garg**, "Impact of App Privacy Label Disclosure on Demand: An Empirical Analysis," WEIS 2022 — privacy-label demand effects, adjacent to consent/notice economics; not a valuation estimate. VERIFIED (2022 accepted list).
- **Kuerbis & Mueller**, "Exploring the role of data enclosure in the digital political economy," WEIS 2022 — "data enclosure" is conceptually near the capital-class claim; worth reading before final related-work. VERIFIED (2022 accepted list).
- **Spiekermann & Korunovska**, "Towards a value theory for personal data," *Journal of Information Technology* 2017 — survey-experiment value theory (1,269 Facebook users); adjacent, potential valuation input. UNVERIFIED as to exact figures (only landing page seen).

---

## SYNTHESIS

### (1) Where the seventh-capital thesis is genuinely novel vs. what WEIS has already published

WEIS and its adjacent literature have thoroughly established three things our paper leans on but must **not** re-claim as novel: (a) subjects systematically under-price their own data and behave irrationally about it (P1, P7); (b) privacy valuations are unstable, endowment- and framing-dependent (P4); and (c) the WTA/WTP gap and the privacy paradox are real and measurable (P1, P4, P5). Two things are contested rather than settled and are where we must fight: whether the paradox implies a market failure at all (Cofone, P2, says no), and whether data is best modelled as **labour** (Arrieta-Ibarra/Weyl, P8/P9) or as something else.

Genuinely novel, and absent from the WEIS body of work as surveyed:
- **Data as a distinct capital class with its own accounting** ("seventh capital"). The field's default is data-as-economic-good (P6) or data-as-labour (P8/P9). No WEIS paper found frames behavioural data as a seventh capital class.
- **An information-theoretic, not policy, guarantee.** Every WEIS/adjacent treatment found operates on incentives, disclosure, consent, notice, or compensation — all policy instruments. None derives a leakage bound from the *architecture* of the observing/acting split (our boundary agent S vs delegation agent M).
- **Time-indexed R(t).** The literature reports static valuations and static paradoxes; a time-indexed reconstruction bound tied to an architectural separation has no precedent in the corpus mapped here.

The "priced-elsewhere" claim (our point 3) is the *least* novel: P1, P2, P3, P5 all already show value flowing away from the subject. We should present point 3 as well-supported established ground, and spend our novelty budget on points 1 (capital class) and 2 (architectural/information-theoretic guarantee).

### (2) The WEIS (+ must-cite adjacent) papers our related-work MUST engage or a referee will reject us

1. **Acquisti, Taylor & Wagman, JEL 2016 (P6)** — the field survey; not citing it reads as not knowing the field.
2. **Collis, Moehring, Sen & Acquisti, WEIS 2022 (P3)** — the current WEIS-native empirical on data valuation; our valuation section must reconcile with it.
3. **Arrieta-Ibarra, Goff, Jiménez-Hernández, Lanier & Weyl, 2018 (P8)** — the rival capital-vs-labour framing; we must draw the line explicitly.
4. **Acquisti, John & Loewenstein, JLS 2013 (P4)** — the canonical WTA/WTP-instability result; grounds our "policy guarantees are weak" move.
5. **Grossklags & Acquisti, WEIS 2007 (P1)** — the WEIS-native root of subject under-pricing; positions us inside WEIS's own lineage rather than beside it.

(Beresford et al., P5, is the sixth and is the specific paper a sceptical referee will wield against the capital-class claim; pre-empt it.)

### (3) Strongest empirical numbers — shortlist for the valuation rebuild (A12)

Ranked by strength and directness for a per-subject data-price estimate:
1. **Collis et al. 2022 (P3):** median WTA **$750 / $1,000** (one-time, all Facebook data, 2021), with demographic splits ($500 Black / $1,000 White; $600 female / $1,000 male). Strongest, most recent, WEIS-native. Verify against the PDF tables.
2. **Acquisti, John & Loewenstein 2013 (P4):** **$10 anonymous vs $12 identified** gift-card design; **$2** switching wedge; ~**5×** WTA:WTP disparity. Exact design constants; ratio to be confirmed in JLS tables.
3. **Beresford et al. 2012 (P5):** **€1** discount flips nearly all buyers to surrender extra personal data — an upper bound on point-of-sale subject WTP.
4. **Grossklags & Acquisti 2007 (P1):** the **25-cent** sell-threshold framing; extract precise means/medians from the PDF in the rebuild.
5. **Cofone 2015 (P2):** ~**850M users / ~$100B** Facebook valuation — context only, a firm-value illustration, not a per-user estimate.

**Caveat for A12:** figures 1, 2 and 4 currently rest partly on secondary summaries (press releases, publisher landing pages, law-school blog) because the PDF bodies did not render in this environment. Each must be re-confirmed against the paper's own tables before it enters a TIER-A/TIER-S valuation figure. Do not let any of these numbers cross the GR-3 fiat-value fence: they are external literature quotations for positioning, not canon value claims.
