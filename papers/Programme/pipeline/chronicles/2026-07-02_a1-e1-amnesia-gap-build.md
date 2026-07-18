---
date: 2026-07-02
role: A1
wps: [WP-02, WP-07, WP-08, WP-09, WP-10, WP-16, WP-23]
extractions: [E1, E2]
register_head: C96
ledger_entries: []
---

# A1 session · E1 amnesia-gap extraction built

## Verdict

`extractions/E1-amnesia-gap.md` is built and passes `check_register_refs` (PASS, head C96). Thirty-nine claims: 4 Proven-conditional, 9 Design-assumption, 22 Conjecture-Cnn keyed to the register at head C96, 4 Empirical-external, 0 Verified-record, 0 CONTESTED. All ten manifest sources resolved via SOURCES.md and swept; none unreachable. Two hygiene findings are proposed to the ledger through A0 rather than appended directly, per this run's serialisation override. E1 is ready for A2 (WP-02) and A3 (WP-07) consumption, with the TIER-S filter note at the top of the file as the task card required.

## Path

Boot per CLAUDE.md: GROUND_RULES, role card A1, task card E1_A1, then template, E2 exemplar, SOURCES.md, manifest (read-only), chronicles/README. The register was read at Bands I to X to key every STATUS field; the two long table rows the initial scan elided (C81, C92) were fetched individually.

Source resolution was clean. `whitepaper-PT` resolved to the Promise-Theoretic Foundations chapter of `swordsman_mage_whitepaper_v6_3.md`; `bakhta-notes` to its three registered files; `ceremony-specs` to its five registered files across DOCS, MASTER and COM roots; `tome-ii` to the seven acts of the Lyapunov tome, swept through frontmatter lineage plus text.

Extraction decisions worth recording:

1. **Overlap with E2 handled by pointer, not duplication.** The R(t) time thread (C18, the moving-ceiling apparatus) appears in E1 only where spec §11.4 places it inside the E1 source set, with primary home noted as E2. Conversely E2-C12 already names E1 as the primary home of the compounding-absorption material; E1-C09 to E1-C11 now hold it in full.
2. **Spec §16 engineering rows classified down, filed up.** Spec §16 lists two-extension autonomy and DOM-free measurement among proven results at 95%. Their warrant is implementation-level, not information-theoretic. Reclassifying silently would launder a correction (GR-6/GR-10), so E1-C39 carries the Design-assumption status with the disagreement stated, and a ledger entry is proposed for the register process to confirm the labelling.
3. **Stale local numbering in the Bakhta integrity-gap note.** The note's §5 mints C70 to C73 locally; the register assigns C77 to C80 (Band VII). The register governs; the mapping is recorded inside E1-C19 and a hygiene ledger entry is proposed so future readers of the note do not miscite.
4. **Mythopoetic sources restated, not imported.** Tome II and the Aletheia-Lethe note yielded claims in mathematical vocabulary only: the tome's acts reduced to their register lineage (C28, C29, C47 to C50) and the note reduced to complement-pair arithmetic plus C54. C53 (mythological readings of bnot-pairs) was deliberately NOT extracted: its claim content is canon-internal naming, which GR-4 keeps upstream.

## Reversals

- An early draft carried C53 as a claim block; reversed on the GR-4 ground above. The arithmetic it decorates survives as E1-C28.
- The bilateral cloak ceremony spec was read expecting amnesia-relevant material; it yielded none (its content is productive VRC formation, E3/E6 territory). Recorded as swept with zero claims rather than forcing a claim to justify the sweep.
- Whitepaper-PT trust-tier thresholds (50/150/500 signals) were considered and excluded: the source itself labels them uncalibrated design parameters, and they belong to E3's cluster if anywhere.

## Session overrides observed

No git operations; no direct ledger appends (entries proposed in the A0 report instead); manifest untouched (status change requested in report); canon read-only throughout.

## Handoff

- **E1:** built, checked, awaiting A0 status bump pending → drafted, and A0 serialisation of the two proposed ledger entries.
- **Open question for A0/register process:** whether spec §16's 95% label should be scoped to the information-theoretic rows only (erratum-class question, not resolved here).
- **WP-02 (A2):** next action is to draw exclusively on E1-C01 to E1-C05, E1-C09 to E1-C11, E1-C27, honouring the filter note; preconditions travel with every citation of E1-C01/E1-C02.
- **WP-07 (A3):** next action is the formalisation obligations named inside E1-C08 (the chain-break engineering claim) and E1-C12/E1-C13 (obstruction machinery, currently unconstructed).
- **WP-08 (A6):** E1-C09/E1-C10 fix the external baselines the benchmark must reproduce before measuring the amnesia break.
- **Blocked:** nothing blocked for this extraction.
