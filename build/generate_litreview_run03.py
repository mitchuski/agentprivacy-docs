#!/usr/bin/env python3
"""Generate the run-03 lit-review artefacts from _run_data_03.json.

Run 03 = residue stress sweep (workflow wf_af6caf5a-745, 2026-08-17):
five multi-modal sweep seats -> five per-residue refuter seats (D3-isolated,
default-to-coverage) -> one judge seat. Outputs follow the run-02 pattern:
generated artefacts, never hand-edited; fix the run data and regenerate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LITR = ROOT / "papers" / "Programme" / "pipeline" / "litreview"
DATA = LITR / "_run_data_03.json"

RUN_ID = "wf_af6caf5a-745"
DATE = "2026-08-17"

FM = f"""---
artefact: litreview-runtime-output
runtime: weis-litreview-runtime (run 03, residue stress sweep)
run_id: {RUN_ID}
predecessor: wf_ba400906-67b (run 02, 2026-07-15)
target: WP-14 (weis_seventh_capital, WEIS 2027)
date: {DATE}
register: standards
generated: true
note: "Generated artifact. Do not hand-edit; fix _run_data_03.json / the runtime and regenerate via build/generate_litreview_run03.py. Verdict spread: {{spread}}. Verdicts are candidates only; assignment and P4 are the First Person's."
---
"""


def main():
    res = json.loads(DATA.read_text(encoding="utf-8"))
    sweeps, refs, judge = res["sweeps"], res["refutations"], res["judge"]
    verdicts = judge["verdicts"]
    spread = (f"{sum(v['verdict'] == 'COVERED' for v in verdicts)} COVERED / "
              f"{sum(v['verdict'] == 'NARROWED' for v in verdicts)} NARROWED / "
              f"{sum(v['verdict'] == 'SURVIVES' for v in verdicts)} SURVIVES "
              f"across {len(verdicts)} residues")
    fm = FM.replace("{spread}", spread)
    n_items = sum(len(s["items"]) for s in sweeps)

    # ---- RUN_MANIFEST_03.md
    m = [fm, "# Lit-review runtime · run 03 manifest (residue stress sweep)", ""]
    m += [f"**Purpose.** Run 02 (wf_ba400906-67b) returned 0 VALIDATED / 5 MIRAGE and left "
          "five residual novel cores. Those residues are the claims WP-14 now rests on, so this "
          "run stresses the residues themselves against a widened, time-advanced corpus "
          "(2023-2026 window, searched 2026-08-17).", ""]
    m += ["## Seat configuration",
          "",
          "| Seat | Count | Role | Sees |",
          "|---|---|---|---|",
          f"| sweep:* | {len(sweeps)} | multi-modal prior-art search (WEIS/econ venues; formal preprints; law+standards; data-as-labour; shelf-life/erosion) | its modality brief + the PVM position + the five residues + WebSearch |",
          f"| refute:* | {len(refs)} | per-residue DELEGATOR - hunts covering art, instructed to default to coverage | the residue + sweep digest + WebSearch; never a prover argument (D3) |",
          "| judge | 1 | rules SURVIVES / NARROWED / COVERED per residue; assembles bibliography additions | residues + refuter outputs + sweep items |",
          ""]
    m += ["**D4b honest limit (unchanged from run 02).** All seats run on the same model weights; "
          "the separation is context isolation, not weight diversity. The operating rule stands: "
          "an all-SURVIVES result would be treated as a failed enforcement of the adversarial "
          "discipline. This run returned " + spread + ".", ""]
    m += ["## Run statistics", "",
          f"- Sweep items surfaced: {n_items} across {len(sweeps)} modalities",
          f"- Refuter covering candidates: {sum(len(r['covering_candidates']) for r in refs)}",
          f"- Bibliography additions proposed: {len(judge['bibliography_additions'])}",
          f"- Verdict spread: **{spread}**", ""]
    m += ["## Judge headline", "", judge["headline"], "",
          "## Outputs (this directory)", "",
          "- `residue_verdicts_03.md` - per-residue verdict, restated residual, basis, and the refuter's covering art.",
          "- `bibliography_additions_03.md` - new resolvable citations proposed for the WP-14 bibliography (A4 verifies before tier-A use).",
          "- `_run_data_03.json` - full structured run output (sweeps, refutations, judge).", ""]
    (LITR / "RUN_MANIFEST_03.md").write_text("\n".join(m), encoding="utf-8")

    # ---- residue_verdicts_03.md
    r = [fm, "# Residue verdicts: run-02 residues stress-tested (run 03)", ""]
    r += [f"Verdict spread: **{spread}**. Vocabulary: SURVIVES = the residue stands as stated; "
          "NARROWED = partial coverage forces a smaller residue (restated below); COVERED = the "
          "residue as stated is anticipated. Confidence labels follow run-02 practice; percentages "
          "are runtime-internal and do not enter tier-A artefacts (GR-2).", ""]
    order = {"COVERED": 0, "NARROWED": 1, "SURVIVES": 2}
    for v in sorted(verdicts, key=lambda v: (order[v["verdict"]], v["ctr"])):
        ref = next((x for x in refs if x["ctr"] == v["ctr"]), None)
        r += [f"### {v['ctr']} — {v['verdict']} "
              f"({v.get('confidence_label', '')}, {v.get('confidence_pct', '')}%)", ""]
        r += ["**Residual restatement (what now survives).** " + v["residual_restatement"], ""]
        r += ["**Basis.** " + v["basis"], ""]
        if ref:
            strong = [c for c in ref["covering_candidates"] if c.get("strength") == "strong"]
            partial = [c for c in ref["covering_candidates"] if c.get("strength") == "partial"]
            if strong or partial:
                r += ["**Covering art found by the refuter seat.**", ""]
                for c in strong + partial:
                    r += [f"- [{c.get('strength')}] {c['citation']} ({c.get('year', '')}) — "
                          f"{c['how_it_covers']} <{c['url']}>"]
                r += [""]
            r += ["**Absence report (D2).** " + ref["absence_report"], ""]
    (LITR / "residue_verdicts_03.md").write_text("\n".join(r), encoding="utf-8")

    # ---- bibliography_additions_03.md
    b = [fm, "# Bibliography additions proposed by run 03", ""]
    b += [f"{len(judge['bibliography_additions'])} new resolvable citations surfaced this run and "
          "judged worth adding to the WP-14 bibliography. Provenance-gated per run-02 practice: "
          "A4 (citation-verifier) re-verifies every entry against a primary record before any "
          "tier-A use; `provenance_confidence` below is the runtime's own label, not A4's.", ""]
    for i, c in enumerate(sorted(judge["bibliography_additions"],
                                 key=lambda c: (c.get("year", ""), c["citation"])), 1):
        b += [f"{i}. {c['citation']} ({c.get('year', 'n.d.')}). "
              f"<{c['url']}> · provenance_confidence: {c.get('provenance_confidence', 'unlabelled')}"]
    b += [""]
    (LITR / "bibliography_additions_03.md").write_text("\n".join(b), encoding="utf-8")

    print(f"Generated 3 run-03 artefacts in {LITR}")
    print(f"Spread: {spread}; sweep items {n_items}; "
          f"bib additions {len(judge['bibliography_additions'])}")


if __name__ == "__main__":
    main()
