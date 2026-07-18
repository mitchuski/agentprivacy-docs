---
date: 2026-07-02
role: A2
wps: [WP-02]
extractions: [E2]
register_head: C96
ledger_entries: []
---

# A2 session · WP-02 policy brief skeleton

## Verdict

The TIER-S skeleton for the policy brief "Enforceable by Architecture" now exists at `rehydrations/policy/enforceable_by_architecture.md`, eight sections plus external references, with an A8 handoff note mapping every section to its extraction claims. All four pipeline checks pass. Six claim-level `[E1-trace-pending]` markers await the E1 extraction, which a parallel session is building this cycle. No ledger entries were filed directly: A0 serialises appends this run, so two proposed entries travel in the session report instead. The manifest was not touched; a status change for WP-02 (pending to draft-v1) is requested through A0.

## Path

The session ran the fast-pass fallback anticipated by the task card. E1 is not on disk, so the separation-bound preconditions were read directly from the canon specification, and E2 supplied the three assigned claims: the proven-conditional reconstruction bound with its two named preconditions, the definitional restatement R(t) with shelf life t*, and the attestation-discount planning rule stripped of all conjecture apparatus. The regulatory anchor (Annex III application date 2026-08-02, the Digital Omnibus deferral hedge, the AEPD reading of Article 22 onto agents, IEEE 7012-2025) came from the specification's external landscape section, all of it externally citable and therefore admissible at TIER-S.

Three decisions shaped the draft and are recorded with their reasons.

First, spec resolution. The session briefing named `privacy_value_v6.md` as the spec, while `SOURCES.md` resolves the `spec§N` slug to `privacy_value_v6_formal_specification.md`. Both files exist and agree in substance, but their late sections are numbered differently: the summary spec places External Landscape and Standards Context at section 30, matching the task card's citation, while the formal specification places the same material at section 31 (its section 30 is Canonical Figures, and it carries an additional Narrative Corpus section the summary lacks). Both surfaces were read; content was taken where they agree. The numbering divergence is escalated per GR-10 as a proposed ledger entry rather than resolved here.

Second, claim-marker form. The task card writes extraction claim identifiers as E2-C01 and similar. The register-reference check rejects any token of the form C followed by digits in a TIER-S artifact, and the check scans the full file including apparatus blocks. Writing the markers in the card's form would fail the gate the card also requires. Reversal: the draft carries the identifiers in lowercase (E2-c01, E2-c02, E2-c09), with the equivalence stated in the A8 handoff note. A proposed ledger entry asks A0 to either whitelist extraction-claim identifiers in the check or standardise the lowercase convention.

Third, scope trims to stay inside carried STATUS. The worked 2026 instances were excluded entirely: they are not in the assigned claim set, and the canon's price-action figure for the first instance is under a standing contested-item prohibition. The policy-versus-structural separation contrast was reduced from the canon's comparative epsilon claim, which is conjecture-held, to the mechanical test criterion (can any permitted operation sequence recover the shared origin), stated as a design definition and marked `[E1-trace-pending]`. The upward-drift claim behind the moving ceiling was likewise excluded; Section 4 of the brief derives its policy force from the definition alone, which is the honest TIER-S reading.

## Checks

`check_tier_vocab`, `check_register_refs`, `check_figures_fence`, `check_versions`: all PASS against the artifact (run with `python`, Windows, 2026-07-02). The artifact declares `tier: S` in frontmatter. Marker census: six claim-level `[E1-trace-pending]` markers (three in Section 2, one in Recommendation 1, one in Section 8, one on the multi-agent measurement references), plus one meta-mention inside the A8 handoff note that names the marker convention.

## Handoff

- **WP-02, next action:** A0 to review the skeleton, apply the requested manifest change (status pending to draft-v1; gate P0 subject to A0's extraction-fidelity read), and decide the two proposed ledger entries. Then A8 takes the draft to prose; the A8 handoff note at the top of the artifact is the working brief.
- **Blocked:** completion of the six E1 traces, blocked on E1 landing (parallel session, this cycle). Whoever holds the artifact when E1 lands re-points every marker at a concrete E1 claim identifier or deletes the sentence per GR-9.
- **Open question:** which section-numbering scheme `spec§N` should canonically denote (summary spec versus formal specification) from section 29 onward; escalated via proposed ledger entry, register process to decide.
- **Open question:** claim-marker case convention at TIER-S; escalated via proposed ledger entry.
