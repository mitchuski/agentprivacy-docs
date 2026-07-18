# THE EXTRACTION FRONTIER CYCLE · a standing agent cycle for the V6 Rehydration Pipeline

**Date:** 2026-07-18 · **Owner:** First Person (invocation) · A0/A1 (execution) · **Status:** ACTIVE — run 1 (E3) executed the day this plan was written
**Authority:** pipeline `GROUND_RULES.md` + `roles/A1-extractor.md` + `manifest.yaml` (A0-writable only). This plan adds no new authority; it packages the existing discipline into one repeatable cycle.

---

## 1. What this cycle is

The extraction layer (E1–E11) is the traceability spine of the whole programme: every public, academic, standards, and grants artifact rehydrates from extraction claims, never from canon directly (GR-9 trace-or-delete). The **frontier** is the boundary between extractions that exist and those that do not. Every pending work package sits behind a pending extraction, so *advancing the frontier is the single move that unlocks the most new work per session.*

One cycle = one extraction built (or one widening sweep of an existing one) + the suite coherence loop + a downstream unlock report. It is deliberately session-sized.

## 2. The frontier map (at plan date)

| Extraction | Status | Unlocks when built | Risk notes |
|---|---|---|---|
| E3 rpp-primitive | **run 1 of this cycle** | WP-11 (RPP adversarial paper), WP-11a (prior art), WP-10 (developer edition, with E1), WP-19 (RWoT, with E7) | L049/L113(c) version hygiene on vrc-protocol-spec; GR-3 fence (70:1 lives here) |
| E6 promise-governance | pending | WP-18 (applied PT paper) | PT-reference pinned v1.5 (L009) |
| E8 ceremony-governance | pending | WP-21 (Metagov governance paper) | L006 phantom-source fence: `game-of-42-canon` retired, use g42-seal-ref + ceremonies-corpus + tome-x; `clc2026-abstract` external |
| E11 implementation-record | pending | Part-D conformance evidence; feeds WP-06/WP-20/WP-23 standards matrix | L008 design-vs-deployment stated PER ITEM; this extraction is mostly that statement |
| E5 algebraic-home | pending · **highest risk** | WP-17 (lattice note), WP-16 (Lean mechanisation, with E1) | run LAST or with A3 seated in the same session; L010 lattice-encoding anchor fence |
| E2 widening sweep | open (manifest note) | hardens every moving-ceiling inheritor | remaining v3 sources; now also carries the two-clock vocabulary |

Default order: **E3 → E6 → E8 → E11 → E5**, then the E2 widening sweep and per-file re-sweeps against the register head. A0 may reorder when a work package with a real date needs its extraction first.

## 3. The cycle, phase by phase

**Phase 0 · Boot and coherence (A0).** Read `GROUND_RULES.md`, the manifest, the register head. Run the suite coherence loop (the WP-13 greps of ledger L152, WIDENED patterns: `frontier capabilit|frontier capacity|frontier growth|grow as frontier|grow with frontier`, the multiples, compound-near-value) against every live surface. Close what the ruling authority already licenses; route the rest. This keeps the corpus the sweep is about to read coherent BEFORE claims are extracted from it.

**Phase 1 · Pick (A0).** Next extraction from the frontier map, or the manifest's stated open sweep. One per cycle.

**Phase 2 · Sweep (A1, fanned out).** Resolve every `sources:` slug through `SOURCES.md` (a source not there is not citable; propose additions to A0, never cite around the registry). Fan out parallel read-only readers, one per source group. Each returns candidate-claim blocks: exact file+line, VERBATIM quote, one-line register-neutral restatement, type suggestion, implementation status. Standing integrity flags travel with the prompts: L007 (COM untracked, cite by path), L008 (design vs deployment per claim), L009 (PT v1.5), L010 (lattice anchor), L049/L113(c) (vrc-spec versioning, local conjecture numbers superseded), GR-3 (figures fenced), GR-4 (no mythopoetic vocabulary in restatements). Large practice-record corpora (skills, chronicles) are sampled at STATED depth, and the sweep record says so honestly (the E10 precedent).

**Phase 3 · Build (A1, main thread).** Synthesize the extraction per `templates/extraction_template.md`: one claim per block, sequential numbers, STATUS from the fixed vocabulary (Proven-conditional / Conjecture-Cnn at register wording / Design-assumption / Empirical-external / Verified-record / CONTESTED), preconditions where proven-conditional, FEEDS lists naming work packages. Verify the load-bearing verbatim quotes DIRECTLY against source files before writing (reader output is candidate, not evidence). **Execution-verification rule (L157):** any sweep claim about CODE BEHAVIOR (as opposed to text content) is verified by RUNNING it before it enters the extraction — quote fidelity does not verify behavioral claims; the E8-C14 refutation is the standing precedent (a verbatim-faithful quote carried a false behavioral claim into a CONTESTED row and a source-repo warning comment). Canon disagreements: tag CONTESTED, ledger CANON-LEVEL, move on (GR-10; A1 never resolves). Claims that restate a registered conjecture use the register row's current wording (GR-1), at the head the manifest states.

**Phase 4 · Verify (A0).** P0 spot-trace: pick ≥3 claims, walk each to its source line, verdict per trace. Run the checks suite on the new file (`check_register_refs` is the binding one for extractions). Then, and only then, the manifest row: `status: pending → drafted`, note with claim count at register head, `built:` date. Manifest is A0-writable only.

**Phase 5 · Record (A0).** Ledger entry (append-only): what was built, claim census by status, contested items, registry additions proposed, the unlock report (which WPs are now startable and what their next role-chain step is). Chronicle per `chronicles/README.md`, verdict-first, handoff block. Nothing is committed or pushed; diffs await the First Person (G-M).

**Hard gates, every cycle:** P4 is never marked, simulated, or assumed. Register rows and canon dispositions are the First Person's. Generated artifacts are rebuilt, never hand-edited (GR-6). A cycle without a chronicle is unfinished.

## 4. How to invoke it

One line in any docs-repo session:

> run the extraction frontier cycle — plan `plans/EXTRACTION_FRONTIER_CYCLE_2026-07-18.md`, pick the next E from the frontier map

Variants: name the extraction explicitly ("…run it on E6"); or "coherence-only" to run Phase 0 as a standalone weekly loop (that IS WP-13); or "widening" to re-sweep an existing extraction against a moved register head instead of building a new one. The cycle also runs as a multi-agent workflow when asked (seat-isolated readers, then A1 build; the WEIS litreview runtime is the precedent) — the phases and gates are identical either way.

## 5. Definition of done for the arc

All eleven extractions at drafted-or-better, each with `swept_complete: true` at stated depth, zero unresolved CONTESTED items older than one register cycle, and the manifest's per-row notes current at head. At that point the frontier flips character: the cycle becomes maintenance (widening sweeps on register bumps + the Phase-0 coherence loop) and the constraint moves to the work-package chains and the P4 queue, which are the First Person's.

## 6. Honesty ledger for this plan

The cycle can build claim inventories and keep them coherent; it cannot make the claims true, cannot verify external citations without A4 passes, and cannot substitute for the First-Person reads that gate everything public. E5 is flagged highest-risk in the manifest for a reason: the algebraic-home material is the most conjectural band of the corpus, and its extraction should expect a high CONTESTED count rather than force resolution. If a cycle finds the corpus too incoherent to extract from (Phase 0 keeps finding canon-level conflicts), the right output is a ledger of CANON-LEVEL findings and NO extraction, not a clean-looking file.
