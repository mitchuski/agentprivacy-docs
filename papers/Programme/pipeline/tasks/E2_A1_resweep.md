---
wp: E2 (extraction maintenance; upstream of WP-01, WP-04, WP-22, WP-28)
role: A1
tier: internal
extraction: E2
branch: none (branch convention suspended; untracked tree)
gate_target: n/a (A0 runs check_register_refs on completion)
due: 2026-07
---

# Task card · E2 re-sweep · role A1 (Extractor)

**Objective:** Re-verify E2-moving-ceiling.md against register Bands IX and X (C90 to C96), clearing the manifest's `re-sweep-vs-C90-C96-pending` note. E2 was built at head C89; the register has since gained Band IX (C90 to C93, limitative reading) and Band X (C94 to C96, Hearthold).
**Inputs:** `extractions/E2-moving-ceiling.md`; `research/CONJECTURE_REGISTER_V6.md` (head C96) Bands IX and X in full; E2's widened sources per manifest (notably `limitative-note` for C90 to C93); `SOURCES.md`.
**Output:** the same file, updated: any claim whose register row moved re-verified; new Band IX/X claims added ONLY where they belong to the moving-ceiling inventory (limitative results bounding self-certification and the ceiling's knowability are in scope; Hearthold identity material likely is not, judge per claim); frontmatter records `register_head_at_build` bumped to C96 with a re-sweep note.
**Definition of done:**
- every existing E2 claim's STATUS re-checked against the register at C96 (confidence values, wording, no silent drift);
- Band IX (C90 to C93) swept for moving-ceiling-relevant claims; Band X (C94 to C96) swept and included or excluded with the reason recorded in the sweep record;
- one claim per block, template fields exact, mathematical vocabulary only;
- downstream note: list which consuming WPs (WP-01, WP-04, WP-22, WP-28) are touched by any changed or added claim, so A0 can flag re-traces;
- `checks/check_register_refs.py` passes on the file; ledger clean or filed; A0 notified.
**Out of scope:** resolving canon conflicts (CONTESTED + ledger); editing rehydrations; the manifest.
**Handoff:** A0 (clears the manifest note, flags downstream re-traces if any).
