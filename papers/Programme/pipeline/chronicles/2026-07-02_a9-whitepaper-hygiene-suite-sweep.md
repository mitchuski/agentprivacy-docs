---
date: 2026-07-02
role: A9
wps: [WP-03, WP-13]
extractions: []
register_head: C96
ledger_entries: []
---

# A9 session · whitepaper hygiene pass and standing suite sweep

## Verdict

The whitepaper hygiene pass that blocks WP-03 is complete. Ten findings were prepared as proposed ledger entries and handed to A0 for serialisation; none were filed directly because parallel producer sessions were writing during this run and A0 serialises ledger appends. The three public rehydrations pass all four checks clean. The whitepaper fails the versions check (8 unconditioned static-ceiling passages across 6 locations, 1 version field for reconciliation) and the figures fence check (12 occurrences for sanctioned-formulation review). The HEAD constant in `checks/check_register_refs.py` equals the manifest `register_head` (both 96). One check-script defect was found and proposed, not applied: the retired-citation pattern misses the colon form the whitepaper actually uses. WP-03's `A9-hygiene-pass` blocker can clear once the human rules on the reconciliation batch and A0 applies the manifest change.

## Scope and constraints

Session overrides from A0: no git operations; no direct ledger appends; no edits outside `chronicles/`; manifest read-only. Canon is read-only per GR-6 and GR-10; every defect was filed as a proposed entry, none fixed. Sweep scope was every .md under `rehydrations/` plus `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md`, with the four checks run under `python` (3.12 toolchain resolved on first attempt).

## Path

1. Boot per `CLAUDE.md`: ground rules, role card, task card. Confirmed the ledger head at L012, so all proposed entries carry the `[Lxxx]` placeholder for A0 to serialise.
2. Verified `HEAD = 96` in `check_register_refs.py` line 7 against `manifest.yaml` `register_head: C96`. Equal. No drift this run.
3. Enumerated `rehydrations/`. The initial tree listing held three files (`public/the_moving_ceiling.md`, `public/competence_without_history.md`, `public/the_uncarved_date.md`). A second listing minutes later showed `policy/enforceable_by_architecture.md` newly present, which matches A2's in-flight WP-02 work. Per the run instructions this file was excluded from the sweep and no findings were filed against it; it is noted for the next A9 run.
4. Ran all four checks against the three public rehydrations plus the whitepaper. Rehydrations: 12 of 12 check-file cells pass, including the standing GR-5 items (no em-dashes at TIER-P, no figures, no over-head conjecture references). Whitepaper: register_refs pass, tier_vocab pass (no tier frontmatter, so tier gates do not bind; the whitepaper is canon, not a tiered artifact), versions fail (9 findings), figures fence fail (12 findings).
5. Read the whitepaper's front matter, terminology section, reconstruction-ceiling section, companion-document section, and Document Metadata section in full, and reconciled version references item by item against `reference/PAPERS_INDEX.md`, `SOURCES.md`, and the formal specification's section 30 sanctioned-figure table.
6. Composed the proposed ledger batch (ten entries) and this chronicle.

## Findings in brief

The full batch is in the report to A0. In outline: the whitepaper disagrees with itself three ways on version (header 6.3, metadata 6.2, Version History table ending at 5.0); the header date and the edition note disagree with no Version History record of the V6 edition decision; the metadata cites the retired Research Paper v4.2 while the body cites a third identity, Dual Privacy Architecture v3.5; the edition note pins register head C89 against the current C96; the metadata cites Promise Theory Reference v1.4 against the L009 pin of v1.5, and VRC Promise Protocol v3.4 where only v3.3 exists on disk; line 69 carries the GR-7 retired sentence family verbatim; five further static-ceiling passages lack in-passage conditioning; the 70:1, 31,000x and 47k to 52k figures appear in formulations that drift from the section 30 sanctioned forms, while 74x conforms and 678x is absent.

## Reversals and dead ends

1. An initial glob for `checks/*` through one path form returned empty and was re-run with the directory as the search root; a tooling quirk, not a repository fact. Recorded so the empty result is not mistaken for a missing checks directory.
2. The automated versions check appeared to clear the retired-citation rule, and a first reading took that at face value. Manual reconciliation reversed this: the retired citation is present at line 1925 in a bold-plus-colon form (`**Research Paper:** v4.2`) that the check's regex (`Research Paper v4\.2`) cannot match. The check result was a false pass for that rule; the finding stands and a pattern widening is proposed. The same manual pass also explains the doubled findings at lines 69 and 99: the static-ceiling regex matches both `R < 1` and `reconstruction ceiling` on the same line, so counts overstate locations.
3. The line-count utility first reported 1,144 lines against check line numbers up to 1,867; resolved as a counting artefact (blank lines uncounted by the utility), not file corruption. The file has 1,945 lines.

## Handoff

- **WP-03**: blocker `A9-hygiene-pass` is discharged on A9's side. Open question for the human: the L003 decision batch, in particular whether the line-8 edition note's blanket reading instruction satisfies GR-7 for the six static-ceiling locations, or whether the whitepaper needs an in-body reconciliation edit through the canon process. Next action: A0 serialises the ten proposed entries into the ledger and puts the batch on the human's weekly decision list; on decision, A0 applies the manifest change.
- **WP-13** (standing sweep): all current rehydrations clean. Open item: `rehydrations/policy/enforceable_by_architecture.md` was in flight (A2) and unswept; next A9 run sweeps it once A2's session closes. Second open item: the proposed `check_versions.py` pattern widening must not be applied while parallel sessions invoke the checks; A0 schedules it between sessions.
- No git operations were performed; nothing was committed, pushed, or staged.
