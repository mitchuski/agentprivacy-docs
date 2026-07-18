# Chronicles · V6 Rehydration Pipeline

The path record of the programme. The ledger (`reviews/critiques_ledger.md`) holds findings; the manifest holds state; the chronicles hold the work itself: what was attempted, what was decided, what changed direction, and why. Together they are the longitudinal record of how a mythopoetic canon is converted into formal artifacts without loss of honesty. That record is itself a research object: it feeds the method-and-path extraction and the thesis chapter on conjecture governance as a method.

## Rules

1. **One file per session or cycle**, named `YYYY-MM-DD_slug.md`. A session writes its own chronicle and never edits another's. A0 may write cycle-level chronicles spanning several sessions.
2. **Formal register.** Plain research English. GR-4 vocabulary applies (boundary agent, delegation agent, data subject, structural context erasure). Canon vocabulary appears only when quoting a source by title. No em-dashes. UK spelling.
3. **Verdict-first.** Open with what the session produced or decided, then the path that led there. A chronicle that reads as a diary has failed; it should read as a lab notebook entry.
4. **Record reversals with the same prominence as progress** (GR-8 applies to the path record too). A dead end named is a contribution; a dead end omitted is a defect.
5. **Trace outward, never duplicate.** Findings go to the ledger and are cited here by entry ID. Status changes go to the manifest via A0 and are cited here by WP/E id. The chronicle carries only what neither instrument can: sequence, reasoning, and turning points.
6. **Every chronicle ends with a handoff block**: open questions, blocked items, and the single next action per WP touched.

## Frontmatter

```yaml
---
date: YYYY-MM-DD
role: A0..A13 (or "first-person")
wps: [WP-NN, ...]          # work packages touched
extractions: [EN, ...]      # extractions read or built
register_head: C89          # as observed this session
ledger_entries: [LNNN, ...] # entries filed this session
---
```

## Why this exists

The programme claims that the two-register discipline, the gate structure, and the conjecture register are a reusable method for governing speculative technical work. That claim needs evidence, and the evidence is this directory: a contemporaneous, per-session record of the method in use, including its failures. Write each entry as if a methods examiner will read it, because one will.
