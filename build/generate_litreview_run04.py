#!/usr/bin/env python3
"""Generate the run-04 lit-review artefacts from _run_data_04.json.

Run 04 = normative/anti-commodification strand sweep (Veliz direction),
workflow wf_23f4f7ad-527, 2026-08-17: four sweep seats (market-inalienability
theory; Veliz corpus + reception; collective/group privacy + externalities;
inalienable-pricing formal precedents) -> two targeted refuter seats
(inalienability leg of CTR-LR-02; collective-externality join) -> one judge
producing a positioning map, threat verdicts, bibliography additions, and
per-paper citation recommendations. Generated artefacts, never hand-edited;
fix _run_data_04.json / the runtime and regenerate.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LITR = ROOT / "papers" / "Programme" / "pipeline" / "litreview"
DATA = LITR / "_run_data_04.json"

RUN_ID = "wf_23f4f7ad-527"
DATE = "2026-08-17"

FM = f"""---
artefact: litreview-runtime-output
runtime: weis-litreview-runtime (run 04, normative/anti-commodification strand)
run_id: {RUN_ID}
predecessors: wf_ba400906-67b (run 02), wf_af6caf5a-745 (run 03)
target: WP-14 (weis_seventh_capital, WEIS 2027); secondary WP-04
date: {DATE}
register: standards
generated: true
note: "Generated artifact. Do not hand-edit; fix _run_data_04.json / the runtime and regenerate via build/generate_litreview_run04.py. {{spreadnote}} Verdicts and placements are candidates only; adoption and P4 are the First Person's."
---
"""


def main():
    res = json.loads(DATA.read_text(encoding="utf-8"))
    sweeps, refs, judge = res["sweeps"], res["refutations"], res["judge"]
    tv = judge["threat_verdicts"]
    spread = " / ".join(f"{v['target'].split(':')[0][:60]}: {v['verdict']}" for v in tv)
    fm = FM.replace("{spreadnote}", f"Threat verdicts: {spread}.")
    n_items = sum(len(s["items"]) for s in sweeps)

    # ---- RUN_MANIFEST_04.md
    m = [fm, "# Lit-review runtime · run 04 manifest (normative strand)", ""]
    m += ["**Purpose.** First-person direction 2026-08-17: bring the anti-commodification "
          "pole (Veliz; the Radin market-inalienability lineage) and the collective-privacy "
          "literature into the WP-14 corpus, and stress-test the two joins that direction "
          "exposes: the inalienability leg of CTR-LR-02, and the carrying of the collective "
          "externality into a subject-side valuation. Unlike runs 02/03 this run also returns "
          "PLACEMENT: per-paper citation recommendations for the strand.", ""]
    m += ["## Seat configuration", "",
          "| Seat | Count | Role |",
          "|---|---|---|",
          f"| sweep:* | {len(sweeps)} | anti-commodification theory · Veliz corpus + reception · collective/group privacy + externalities · inalienable-pricing precedents |",
          f"| refute:* | {len(refs)} | targeted threat checks (D2/D3): priced+inalienable join; collective-externality join |",
          "| judge | 1 | positioning map + threat verdicts + bibliography + citation placements |",
          ""]
    m += ["**D4b honest limit (standing).** Same model weights across seats; separation is "
          "context isolation. D2 phrasing enforced in absence reports.", ""]
    m += ["## Run statistics", "",
          f"- Sweep items surfaced: {n_items} across {len(sweeps)} modalities",
          f"- Refuter covering candidates: {sum(len(r['covering_candidates']) for r in refs)}",
          f"- Bibliography additions proposed: {len(judge['bibliography_additions'])}",
          f"- Citation placements proposed: {len(judge['citation_recommendations'])}", ""]
    m += ["## Judge headline", "", judge["headline"], "",
          "## Outputs (this directory)", "",
          "- `normative_strand_04.md` - positioning map, threat verdicts, citation placements.",
          "- `bibliography_additions_04.md` - new resolvable citations (A4 verifies before tier-A use).",
          "- `_run_data_04.json` - full structured run output.", ""]
    (LITR / "RUN_MANIFEST_04.md").write_text("\n".join(m), encoding="utf-8")

    # ---- normative_strand_04.md
    r = [fm, "# The normative strand: positioning map, threat verdicts, placements (run 04)", ""]
    r += ["## Positioning map: the poles of the personal-data-value debate", ""]
    for p in judge["positioning_map"]:
        r += [f"### {p['pole']}", "",
              f"**Anchors.** {p['anchors']}", "",
              f"**Claim.** {p['claim']}", "",
              f"**PVM relation.** {p['pvm_relation']}", ""]
    r += ["## Threat verdicts", ""]
    for v in tv:
        r += [f"### {v['target'].split(':')[0]} — {v['verdict']} "
              f"({v.get('confidence_label', '')}, {v.get('confidence_pct', '')}%)", "",
              f"**Target.** {v['target']}", "",
              f"**Restatement (what survives).** {v['restatement']}", "",
              f"**Basis.** {v['basis']}", ""]
        ref = next((x for x in refs if x["target"][:40] == v["target"][:40]), None)
    r += ["## Refuter outputs (covering art + absence reports)", ""]
    for ref in refs:
        r += [f"### {ref['target'].split(':')[0]} — refuter recommendation: {ref['recommendation']}", ""]
        strong = [c for c in ref["covering_candidates"] if c.get("strength") == "strong"]
        partial = [c for c in ref["covering_candidates"] if c.get("strength") == "partial"]
        for c in strong + partial:
            r += [f"- [{c.get('strength')}] {c['citation']} ({c.get('year', '')}) — "
                  f"{c['how_it_covers']} <{c['url']}>"]
        r += ["", "**Absence report (D2).** " + ref["absence_report"], ""]
    r += ["## Citation placements proposed", ""]
    for c in judge["citation_recommendations"]:
        r += [f"- **{c['paper']}** · {c['where']}: {c['what']} *Cites:* {c['citations']}"]
    r += [""]
    (LITR / "normative_strand_04.md").write_text("\n".join(r), encoding="utf-8")

    # ---- bibliography_additions_04.md
    b = [fm, "# Bibliography additions proposed by run 04", ""]
    b += [f"{len(judge['bibliography_additions'])} citations. A4 (citation-verifier) "
          "re-verifies every entry against a primary record before tier-A use; "
          "`provenance_confidence` is the runtime's label, not A4's.", ""]
    for i, c in enumerate(sorted(judge["bibliography_additions"],
                                 key=lambda c: (c.get("year", ""), c["citation"])), 1):
        b += [f"{i}. {c['citation']} ({c.get('year', 'n.d.')}). "
              f"<{c['url']}> · provenance_confidence: {c.get('provenance_confidence', 'unlabelled')}"]
    b += [""]
    (LITR / "bibliography_additions_04.md").write_text("\n".join(b), encoding="utf-8")

    print(f"Generated 3 run-04 artefacts in {LITR}")
    print(f"Threat verdicts: {spread}")
    print(f"Sweep items {n_items}; bib additions {len(judge['bibliography_additions'])}; "
          f"placements {len(judge['citation_recommendations'])}")


if __name__ == "__main__":
    main()
