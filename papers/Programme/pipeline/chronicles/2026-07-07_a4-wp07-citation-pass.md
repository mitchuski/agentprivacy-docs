---
date: 2026-07-07
role: A4
wps: [WP-07, WP-04]
extractions: [E2]
register_head: C96
ledger_entries: []
---

# A4 · WP-07 citation pass, bounded-contamination verdict, bibliography close

**Verdict first.** The pre-P1 obligation L065(b) resolves ORTHOGONAL: the draft's Proposition 4.2 "bounded contamination" condition and the actual hypotheses of Asif-Amiri Theorem 4.1 (arXiv:2603.05520) are formally incomparable, neither implying the other. Their theorem assumes the Eq. (2) Markov structure plus mutually independent sensitive variables; the draft's condition instead bounds the secret-transcript coupling given earlier secrets and permits dependent secrets. The draft's scope note is accurate as written. Separately: both flagged citations (Gopala-Lai-El Gamal 2008; arXiv:2509.14284) verified against primary sources; E2-C12's CITATIONS line found correct and faithful to spec §26; pv_v6.bib closed from 21 to 60 verified entries (0 UNVERIFIED) with every sweep reference re-verified live; the full xelatex/bibtex/xelatex/xelatex cycle run twice with zero bibtex warnings, zero undefined citations, and 60 bibitems rendered. The full evidence table is the verification note on tasks/WP-07_A4.md.

## Path

1. Boot per CLAUDE.md; role A4 only; task card WP-07_A4; WP-01's A4 note read as the P2-evidence precedent.
2. Pre-P1 obligation first. Three passes over arXiv:2603.05520v1 (abstract page, then two targeted full-text extractions including Appendix A.1) to obtain the theorem statement verbatim, the Eq. (2) Markov structure, the proof's recursion (their ℒ_i := I(O_i; S_i | S_{<i}), Eq. 25 recursion, Eq. 27 closed form), and an explicit negative: no assumption anywhere constrains the public inputs D_i against the sensitive variables, and no condition of the bounded-contamination form appears. Counterexamples in both directions were then constructible (D_1 = S_2 defeats bounded contamination under their hypotheses; S_2 = S_1 defeats mutual independence under the draft's), fixing the verdict at orthogonal rather than stronger or weaker.
3. Import-fidelity finding, flagged not patched (A3 owns proofs): the draft's restated Theorem 4.1 carries neither source hypothesis; as restated it is stronger than the source theorem. Proposed ledger entry below.
4. Gopala-Lai-El Gamal resolved via DBLP and the arXiv precursor (54(10):4687-4698, 2008, DOI confirmed); a search snippet claiming issue 9 was rejected in favour of the DBLP record, per the role card's snippet rule. arXiv:2509.14284 resolved live (Patil, Stengel-Eskin, Bansal; 2025-09-16; no published venue found). E2-C12's line then checked against its canon source: spec §26 does cite the Patil work by name; the line is correct and A1 may clear the in-flight annotation on E2-C12 and the same load on E1-C09. E2 untouched by me.
5. Bibliography close: 39 entries added under the header policy, each re-verified against a live authoritative source (arXiv abstract pages, Crossref, DBLP, PubMed, PMLR, petsymposium.org, federalreserve.gov, csrc.nist.gov, globalriskinstitute.org, live fetches of the five 2026 web records, and eprint.iacr.org via direct HTTP with a browser user agent). FEDS 2025-093 author list re-verified (Mascelli, Rodden), entering VERIFIED. The ResearchGate-only HNDL item was left out entirely rather than UNVERIFIED-commented: with no venue or author list there is nothing to key an entry on.
6. Compile cycle per the scaffold README, run in a scratchpad copy first (consume-by-copy) and then in the scaffold to regenerate main.pdf from its changed input (GR-6). Both clean; 60 bibitems via the scaffold's \nocite{*}.
7. Draft edits confined to the permitted class: three UNVERIFIED citation-key markers removed, References section updated to the verified state. No mathematics, no prose.

## Reversals and corrections recorded

- **Chevignard-Fouque-Schrottenloher is CRYPTO 2025, not CRYPTO 2024.** The sweep row (reviews/WP-04_prior_art.md §5) says CRYPTO 2024; DBLP and Crossref agree on CRYPTO 2025 (pp. 384-415, DOI 10.1007/978-3-032-01878-6_13). The ePrint precursor 2024/222 likely seeded the error. I initially took the sweep's year as given and reversed on the live record.
- **Haines et al. author order corrected**: Haines, Mosaheb, Müller, Pryvalov (petsymposium.org + DBLP), against the sweep's Haines, Müller, Mosaheb, Pryvalov.
- **ecdsa.fail organisation**: site self-describes as Eigen Labs; the sweep says Layr Labs (the GitHub organisation name of the same company). Site self-description carried.
- **Upgrades**: MDPI Telecom 6(4):100 authors resolved via Crossref (Kagai, Branch, But, Allen), clearing the sweep's AUTHORS UNVERIFIED flag; Erlich 2018 and Rocher 2019 enriched with volume/issue/pages and article number; Jain et al. ICML 2023 author list resolved in full.
- **Tooling dead end named**: a grep for bibitems with over-escaped pattern returned 0 against a 60-entry .bbl; re-checked directly before concluding anything. Publisher fetch blocks (IEEE Xplore, MDPI, Nature, Springer) were re-routed through Crossref/DBLP/PubMed rather than trusted from search snippets.

## Proposed ledger entries (for A0 to serialise; ledger not appended by me)

1. [WP-07][P2][A4] Bounded-contamination verdict ORTHOGONAL (evidence in the WP-07_A4 verification note, hypothesis statement quoted). Companion finding, owner A3: the draft's imported Theorem 4.1 restatement omits the source's two hypotheses (Eq. (2) Markov structure; mutual independence of the sensitive variables) and is stronger than the source theorem as restated; carry both hypotheses inside the imported statement. Prop 4.2 itself needs no change; its scope note is accurate.
2. [WP-04][P3][A4] Three sweep corrections from bib re-verification: Chevignard et al. CRYPTO 2024 -> CRYPTO 2025; Haines et al. author order; ecdsa.fail organisation Eigen Labs. Plus upgrades: Telecom authors resolved (Kagai, Branch, But, Allen); FEDS 2025-093 authors verified (Mascelli, Rodden). WP-04 SoK draft cites should be checked against the corrected rows at its next touch (it did not cite the affected rows' UNVERIFIED items, so no blocking exposure found by me).
3. [E1,E2][P2][A4] arXiv:2509.14284 VERIFIED; E2-C12's CITATIONS line correct and faithful to spec §26; closes L065(a) and L066(a) verification legs; A1 clears the in-flight annotations on E2-C12 (and E1-C09's citation load) at next touch.
4. [SUITE][P3][A4] pv_v6.bib at 60 verified / 0 UNVERIFIED; scaffold main.pdf regenerated against the new bib; both compile runs clean.

## Handoff

- **A5-crypto-pc**: receives rehydrations/academic/linear_cap_paper.md with the verification note on tasks/WP-07_A4.md; the bounded-contamination verdict is at the top of that note. The one open mathematical item for review attention is the import-fidelity flag on the draft's Theorem 4.1 restatement (proposed entry 1), which A3 should fix before or during P1.
- **A3**: import-fidelity fix (two hypotheses into the imported Theorem 4.1 statement); nothing else in the draft's mathematics was touched or contested.
- **A1**: E2-C12 annotation clearance per proposed entry 3; no E2 edit made by me.
- **A0**: serialise proposed entries 1-4; gate bookkeeping (P2 evidence on file for the citation leg).
- Single next action per WP: WP-07 -> A3 one-line hypothesis fix, then A5-crypto-pc review; WP-04 -> A10/A0 record the three sweep corrections before the SoK's P1.
