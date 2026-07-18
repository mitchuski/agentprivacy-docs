---
wp: programme-wide (feeds every TIER-A WP)
role: A8 (standards/policy writer seat, tooling session)
runtime: fable
tier: internal
branch: none (tree untracked; branch convention suspended)
gate_target: n/a (infrastructure; done = template builds a PDF)
due: 2026-07-08
---

# Task card · submission scaffold · role A8 (tooling seat)

**Objective:** Build `templates/submission/` — the LaTeX/BibTeX scaffolding the
programme leaves unspecified, so every paper WP formats once and submits many.
**Inputs:** `programme/V6_RESEARCH_PROGRAMME_v2.md` Part E venue list;
`build/build_v6_academic_pdfs.py` (the existing xelatex path — reuse its
toolchain assumptions, do not duplicate it); the readiness-audit finding that
no citation format is specified anywhere; live web for venue LaTeX classes.
**Output:** `templates/submission/` containing:
- `preprint/` — a general IACR-eprint/arXiv-ready article scaffold (main.tex,
  sections/ stubs matching the ten-stage build: abstract, intro+contributions,
  related-work, model+preliminaries, theorems, evaluation,
  threats-to-validity, conclusion), compiling under xelatex;
- `references/pv_v6.bib` — ONE canonical BibTeX file seeded with the real
  external references already verified in the corpus: the v4.3 bibliography
  (Cover &amp; Thomas, Fano, Shannon, Kraskov, Belghazi et al.), the v6 edition's
  wiretap lineage (Wyner 1975, Leung-Yan-Cheong &amp; Hellman 1978,
  Csiszár–Körner), the leakage literature (AgentLeak, Asif &amp; Amiri), and the
  WP-02 legal anchors (GDPR, AI Act, IEEE 7012) in a policy section;
- `venues/README.md` — per-venue notes: class file name, page limit,
  anonymization rule, citation style (populate from A13's verified deadlines
  where available; leave TODO rows otherwise);
- `README.md` — how a paper WP consumes the scaffold.
**Definition of done:** `xelatex` (or the build script's compiler) produces a
PDF from the preprint scaffold with the seeded .bib resolving; every .bib
entry is a real publication with correct authors/year/venue (verify each —
no hallucinated entries; anything unverifiable goes in commented-out form
marked UNVERIFIED); no canon vocabulary anywhere in the scaffold.
**Out of scope:** writing any paper content; touching papers/ or canon;
ledger appends (report to A0 via chronicle).
**Handoff:** chronicle to `chronicles/2026-07-07_a8-submission-scaffold.md`;
WP-04/WP-07 A3 sessions consume `templates/submission/preprint/`.
