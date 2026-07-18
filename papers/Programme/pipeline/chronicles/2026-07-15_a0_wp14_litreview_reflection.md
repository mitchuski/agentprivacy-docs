# Chronicle · A0 · WP-14 lit-review runtime + reflection

**Session:** 2026-07-15
**Role:** A0 (orchestrator), running the litreview brief as pipeline workflows and reflecting the result into WP-14.
**Scope:** stand up the literature-review runtime from `chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md`, run it as the first external-literature addition to the corpus programme, and reflect the searched novelty into WP-14 sections 1 and 2.

---

## Verdict

The lit-review runtime ran and returned the honest outcome: **all five broad novelty candidates MIRAGE'd** (0 VALIDATED / 5 MIRAGE / 0 BLOCKED) against a 20-item provenance-verified corpus plus adjudicator web scope. This is the run working, not failing: the delegator seat was genuinely adversarial (a clean VALIDATED sweep would have meant D2/D3 were not enforced). Every headline MIRAGE carries a narrow surviving residue, and the disciplined WP-14 contribution is the **conjunction** of those residues, none written as "no prior work does X". The single biggest finding: the differential-privacy-markets pricing strand (Ghosh-Roth *Selling Privacy at Auction*, EC 2011, and successors) — which a WEIS PC knows and which the draft did not cite — already prices a disclosure bound as a commodity and occupies the {system\_property × market\_pricing} cell. That gap is now closed. The reflection into WP-14 §1/§2 was A4-citation-verified and A5-spot-reviewed at **accept-class-improved** (M2 residue discharged, M5 reanchored, zero new overclaims). Nothing was committed, pushed, or submitted. **P4 remains the First Person's** and was not simulated.

## Path taken

1. **Runtime (`weis-litreview-runtime`, run wf_ba400906-67b, 36 agents).** 20-item challenge corpus across five strands (propertisation, data-as-labour, empirical valuation, security economics, formal metrics, standards) extracted against the brief's fixed schema, each item provenance-gated (all `verified_from_search`). Five novelty candidates each adjudicated by an **isolated prover seat**, an **isolated delegator seat** (does not see the prover; hunts covering prior art), and a judge → VALIDATED/MIRAGE/BLOCKED. Seat configuration recorded in `litreview/RUN_MANIFEST.md` for D4b auditability, with the honest same-model limit stated. Four outputs written (`gap_table.md`, `contribution_claims.md`, `ctr_candidates.md`, `bibliography.md`) + raw `_run_data.json`. Checks green; C81 hold-back clean.
2. **Corpus registration (the first external-literature addition to the corpus programme).** SOURCES.md +3 rows (`weis-litreview-corpus`, `weis-litreview-adjudication-externals`, `weis-litreview-outputs`); manifest WP-14a registered (tier internal, chain [A10], status built, mirroring WP-11a's "novelty-established-before-asserted"); ledger **L137**.
3. **Reflection (`wp14-litreview-reflection`, run wf_947c1758-889, 3 agents).** A12/A2 economist-integrator produced drop-in revised §1 + §2; A4 verified the new citations; A5 spot-reviewed. Spliced into the draft (line-based, boundaries verified); 9 litreview-surfaced references added; ledger **L138**.

## Reversals and corrections on the record

- **All-MIRAGE is the outcome, not a defect.** The broad "third position / first-to-price-a-system-property" framings do not survive; only the narrow residues do. The paper's novelty was demoted accordingly. This is the brief's own discipline (MIRAGE is the valuable verdict).
- **The DP-markets strand was a real omission.** The draft claimed to price a system property without citing Ghosh-Roth et al., who already do. Engaged head-on; the paper now states exactly what it adds (the R(t) quadruple: adversary-relative + time-drifting + structurally inalienable + rent-decomposed, versus a static priced budget).
- **Three citation author-errors caught by A4 before tier-A use:** Aaron Roth is not an author of Li et al. 2013 (corrected inline to "Li et al. (2013)"); Wagner is Isabel not Ben; Gu is Jiadong, single author. A Bajari year discrepancy (2018/vol108 → verified 2019/vol109) reconciled across the §5.2 inline and References. This is precisely why adjudication-externals were flagged `provenance uncertain` and gated on A4.
- **A5 flagged a GR-8 honesty risk to hold (LM2):** calling the DP-markets budget "static, adversary-independent" understates adaptive/Rényi/continual DP; if contested, part of the R(t) residue collapses back into that strand. Recorded as a live minor for camera-ready, not silently kept.

## State at close

- **Manifest:** WP-14 = revised / gate P1, draft-v3, reflection applied; WP-14a = built (litreview/).
- **Draft:** `weis_seventh_capital.md` draft-v3, 11,228 words (was 9,925). §2 = "five literatures". register\_refs / versions / tier\_vocab PASS; 0 em-dashes; figures\_fence hits only the strip-at-release trace comments (lines 40, 729) — green at release.
- **Ledger:** L137 (corpus addition), L138 (reflection applied, accept-class-improved, LM1-LM3). Three CANON-LEVEL escalations from the prior arc (L130, L132, L134) still await the register process.

## Artifacts

- `litreview/` — RUN_MANIFEST.md, gap_table.md, contribution_claims.md, ctr_candidates.md, bibliography.md, _run_data.json (run wf_ba400906-67b)
- `rehydrations/academic/weis_seventh_capital.md` — draft-v3 (§1/§2 reflected)
- `chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md` — the brief this session executed
- SOURCES.md (+3 rows), manifest.yaml (WP-14a + WP-14 note), reviews/critiques_ledger.md (L137, L138)

## Handoff (when this is picked back up)

1. **LM2 is the highest-leverage open item and a GR-8 honesty item.** At camera-ready, state precisely what adaptive/Rényi/continual DP does and does not do relative to a per-subject reconstruction bound that drifts with frontier capability against a fixed archive — do not let the R(t) residue rest on flatly calling the DP budget adversary-independent. Then LM1 (make the conjunction's non-obviousness explicit) and LM3 (hedge the marginal-product-near-zero strength).
2. **WP-07 is still the critical path to submittability** (unchanged from the prior arc). The durability leg and now the §2 alienability answer both ride the imported guarantee; widen the WP-07 submission gate to name the alienability answer.
3. **A4 full P2 pass** across the whole draft (not only the new cites) remains pending; interleave the 9 new references alphabetically at submission; P3 trace-strip; A13 CFP re-check 2026-11-01.
4. **CTR-LR-01..05 are candidates only.** Conjecture assignment and the three canon-level escalations are the First Person's (brief §9, GR-10). P4 was not marked, simulated, or assumed.

the broad claims were mirages, and the run said so. what survives is narrow, searched, and sits beside the prior art it once ignored.
