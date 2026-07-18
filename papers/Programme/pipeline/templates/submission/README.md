# Submission templates · V6 research programme

LaTeX/BibTeX scaffolding so every paper work package formats once and submits
many. Built by A8 (tooling seat), 2026-07-07. Toolchain matches
`build/build_v6_academic_pdfs.py`: xelatex (MiKTeX), `article` class, 11pt,
25mm margins; bibliography via classic `bibtex` (latexmk is not on the
pipeline machine's PATH).

## Layout

```
templates/submission/
├── README.md            · this file
├── preprint/            · general IACR-eprint/arXiv-ready article scaffold
│   ├── main.tex         · entry point; compile with xelatex
│   ├── preamble.tex     · packages, theorem environments, notation macros
│   └── sections/        · eight stubs matching the programme's build stages
│       ├── 00_abstract.tex
│       ├── 01_introduction.tex      (intro + contributions)
│       ├── 02_related_work.tex
│       ├── 03_model_preliminaries.tex
│       ├── 04_theorems.tex
│       ├── 05_evaluation.tex
│       ├── 06_threats_to_validity.tex
│       └── 07_conclusion.tex
├── references/
│   └── pv_v6.bib        · ONE canonical BibTeX file; verified entries only
└── venues/
    └── README.md        · per-venue class files, page limits, retarget steps
```

## How a paper work package consumes this

1. **Copy, do not edit in place.** Copy `preprint/` into the work package's
   own directory. This scaffold stays generic; drift belongs downstream.
2. **Keep the bibliography canonical.** Cite `references/pv_v6.bib` (copy it
   alongside or reference it by relative path). New references are added to
   the canonical file here, under its verification policy (see the header of
   `pv_v6.bib`): every entry web-verified for authors/title/year/venue before
   it becomes citable; unverifiable entries stay commented out and marked
   UNVERIFIED.
3. **Write into the section stubs.** Each stub's header comment states the
   discipline that applies to that section (preconditions named with results,
   conjectures only as formal conjectures with proof obligations, no
   confidence percentages, negative results reported with the same
   prominence as positive ones). The stubs encode `GROUND_RULES.md` GR-2
   TIER-A, GR-7, and GR-8 for prose written at this tier.
4. **Compile** from the copied `preprint/` directory:

   ```
   xelatex -interaction=nonstopmode main.tex
   bibtex  main
   xelatex -interaction=nonstopmode main.tex
   xelatex -interaction=nonstopmode main.tex
   ```

5. **Retarget to a venue** using the checklist in `venues/README.md`
   (swap the document class, set anonymization, switch the bibliography
   style, remove the scaffold-only `\nocite{*}`).

## Rules inherited from the pipeline

- External literature only in the bibliography; no canon-internal citations
  at this tier (at most one URL to the public spec, placed in the paper text).
- Vocabulary is the formal register throughout: boundary agent S, delegation
  agent M, data subject / source X, structural context erasure,
  conditional-independence residual.
- Generated artifacts (the compiled PDF) are never hand-edited; fix the
  source, rebuild.
