---
wp: CANON (whitepaper batch L015-L023 execution; approved first-person per L045, full rigour)
role: register-process executor (acts on direct first-person approval, recorded L045)
tier: canon
extraction: none
branch: none
gate_target: first-person diff review; clears WP-03 blocker on completion
due: 2026-07
---

# Task card · whitepaper reconciliation · register-process executor

**Objective:** Execute the approved whitepaper hygiene batch on `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md` (backup at `archive/canon-backups-2026-07-02/`). PAPERS_INDEX is the authority side. Line numbers below are from the A9 pass (L015-L023); re-locate if drifted.
**Items, per the rulings:**
1. L015: Document Metadata version 6.2 → 6.3; Version History table backfilled (5.x lineage as found + 6.2 + 6.3 rows + the 2026-06-10 V6 edition note row).
2. L016: header/metadata dates: keep the body date, add the edition note to Version History so both dates are explained; no silent date change.
3. L017: ":1925 Research Paper: v4.2" and ":1763 Dual Privacy Architecture v3.5" both repointed to the V6 research-paper edition (per PAPERS_INDEX pointer `papers/v6/dualprivacy_researchpaper_v6.md`).
4. L018: edition note's pinned head C89 → C96.
5. L019: Promise Theory Reference v1.4 → v1.5.
6. L020: VRC Promise Protocol v3.4: glob `specs/` for a v3_4 file; if absent, revert citation to v3.3 and note it.
7. L021/L022 (GR-7, in-passage conditioning ruled REQUIRED, blanket note insufficient): rewrite the six static-ceiling passages (:69, :99, :891-917 strongest, :1763, :1787) so each carries, in the same passage, the non-collusion precondition, the stated adversary class, and time-indexing R(t); ALSO apply the L044 decomposition where the passage asserts R_max < 1 from architecture alone (the parallel spec session's exemplar wording; "60 pieces remain forever unreconstructable" and "permanent gap" class sentences must not survive). Keep each passage's rhetorical weight; condition it, do not gut it.
8. L023 (GR-3): align each canonical-figure occurrence to its sanctioned formulation per spec §30 (Canonical Figures): 70:1 as the spellbook-corpus compression ratio framing; 31,000x as the accessible-volume value gap under full behavioural capture; $47k-$52k marked indicative. Where an occurrence cannot carry the sanctioned formulation without breaking its sentence, prefer removal.
**Output:** the corrected whitepaper; complete before/after quote list for every edited passage (first-person diff review).
**Definition of done:** all eight items executed or explicitly reported impossible with reason; `python checks/check_versions.py` on the whitepaper shows the version finding and retired citations gone and static findings reduced to zero or explained; `checks/check_figures_fence.py` findings reduced or explained; before/after list complete; A0 notified.
**Out of scope:** the spec (parallel session); the register; content beyond the eight items; any new claims.
**Handoff:** A0 (clears WP-03's L003-decision blocker; manifest change); first person (diff review).
