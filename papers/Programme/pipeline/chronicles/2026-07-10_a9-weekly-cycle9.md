---
date: 2026-07-10
role: A9
wps: [WP-13, WP-01, WP-02, WP-03, WP-04, WP-07, WP-25, WP-27, WP-28]
extractions: [E1, E2, E10]
register_head: C96
ledger_entries: []
---

# A9 weekly consistency sweep · cycle 9

## Verdict

The suite is green with three minor findings and one ledger-tail orphan, none blocking, nothing fixed at this seat. All four deterministic checks pass on all eleven files of the card's explicit list (the three awaiting-P4 papers, the policy brief, the grant edition, the three public drafts, both prior-art reviews, and the E10 method-record extraction): 44 check cells, exit 0 across all four runs, non-vacuous. The argv-less guard holds: each of the four checks invoked with no arguments exits 2 with the loud refusal; none exits 0. Register head triple-agrees at C96 (register :5, manifest :4, check_register_refs HEAD constant). Cross-document consistency across the three papers holds: every trace marker resolves (WP-27 consumes 30 of E10's 31 claims exactly as its frontmatter and trace map state; WP-04 consumes exactly E2-C01..C15; WP-07's consumed set matches its extraction_basis with the five non-basis E1 markers all inside the recorded-exclusions block), and no factual statement about a shared external diverges between papers. The ledger-tail audit (L095-L110) finds every PROPOSED item executed, carried, or queued except one orphan, L102(c). The three findings: the manifest's WP-02 row is two events behind the file and the ledger; WP-03's frontmatter is one station behind the manifest (the L098 F1 class); and two of the three TIER-P public drafts declare no tier in frontmatter, which leaves check_tier_vocab's GR-5 arm unable to bind on them (manual census this run: zero em-dashes in both, so coverage gap, not content breach). One proposed ledger entry returns to A0.

Session constraints from A0: fix nothing; canon read-only; the three awaiting-P4 papers read-only; no manifest, ledger, or tracker writes; no git. The two concurrent seats' surfaces are out of this sweep by instruction: the A2 standards draft (WP-09) is not yet on disk in rehydrations/standards/ and was not sought further; extractions/E7-identity-vrc.md is not yet on disk and was not sought further. Neither was read or judged.

## Check matrix (run of record)

Invocation: `python <check>.py <explicit paths>` from `checks/` as cwd, the eleven card files passed explicitly in one run per check. Exit 0 on all four runs.

| File | versions | figures_fence | register_refs | tier_vocab |
|---|---|---|---|---|
| rehydrations/academic/linear_cap_paper.md | PASS | PASS | PASS | PASS |
| rehydrations/academic/moving_ceiling_sok.md | PASS | PASS | PASS | PASS |
| rehydrations/academic/conjecture_governance_method.md | PASS | PASS | PASS | PASS |
| rehydrations/policy/enforceable_by_architecture.md | PASS | PASS | PASS | PASS |
| rehydrations/grants/grant_edition.md | PASS | PASS | PASS | PASS |
| rehydrations/public/the_moving_ceiling.md | PASS | PASS | PASS | PASS* |
| rehydrations/public/the_uncarved_date.md | PASS | PASS | PASS | PASS* |
| rehydrations/public/competence_without_history.md | PASS | PASS | PASS | PASS |
| reviews/WP-04_prior_art.md | PASS | PASS | PASS | PASS |
| reviews/WP-27_prior_art.md | PASS | PASS | PASS | PASS |
| extractions/E10-method-record.md | PASS | PASS | PASS | PASS |

*Starred cells pass with reduced coverage: no `tier:` key in frontmatter, so the tier-gated arms (GR-5 em-dash scan at TIER-P) do not execute on these two files. See finding 3.

Guard probe: check_versions, check_figures_fence, check_register_refs, check_tier_vocab each invoked with no arguments; all four exit 2 with the L082 refusal line; none exits 0.

## Evidence and path

1. Boot per CLAUDE.md: GROUND_RULES.md, roles/A9-consistency-auditor.md, tasks/A9_weekly_2026-07-10.md read in order; role, writes, and definition of done stated before touching anything.

2. Item 1, deterministic checks: the 44-cell matrix above, followed by the argv-less guard probe. Both halves green.

3. Item 2, cross-document consistency (new this week: WP-27 against WP-04/WP-07).
   - Trace maps. WP-27: every inline marker is within E10-C01..C31 and every referenced claim exists in extractions/E10-method-record.md (31 claim headers, monotone, no gaps); the frontmatter consumption statement (C01-C24 and C26-C30 full, C25 dating evidence only, C31 not consumed with reason) matches the trace map's "Consumed (30 of 31)" block exactly. WP-04: markers are exactly E2-C01..C15, all defined. WP-07: E1-c01..c06, c08..c10, c12 plus E2-c01/c02/c04/c11/c12 in the body per extraction_basis; the non-basis markers (E1-c07, c13, c36, c39, c40 at linear_cap_paper.md:441-499) all sit inside the traceability appendix's recorded-exclusions block, unchanged from the cycle-6 verification.
   - Shared externals, no divergence found. Asif-Amiri: (2^N − 1)ε uniform-case bound with MI 0.49 to 1.05 from two to five agents (WP-07 :76/:242) against "roughly doubling from two to five agents" (WP-04 :320); arXiv:2603.05520 in both reference lists and in grant_edition.md:276 and enforceable_by_architecture.md:392; consistent with E1-C09/E2-C12. AgentLeak: 68.8 per cent inter-agent against 27.2 per cent per-channel output over 4,979 traces on five production LLMs (WP-07 :189) against "4,979 traces on five production LLMs ... high-sixties per-cent range" (WP-04 :320); arXiv:2602.11510 and the El Yagoubi, Badu-Marfo, Al Mallah attribution identical everywhere; consistent with E1-C10. Patil, Stengel-Eskin and Bansal arXiv:2509.14284 cited as preprint (2025) in WP-07 :411, grant :276, policy :392, per the L070(2) verification. Chevignard-Fouque-Schrottenloher at CRYPTO 2025 (WP-04 :381; prior_art :62, the L095 correction intact). The 2026 instance chronology (Babbush et al. 2026-03-31 with the roughly-tenfold figure carrying its spacetime-volume metric; Schrottenloher reconstruction roughly two months later, ePrint 2026/1128; Gidney same-day disclosure; ecdsa.fail record) identical across WP-04 :316, E2-C07, and prior_art :64-:67. WP-27 shares no external citation with WP-04/WP-07 (its references are the meta-research set), and the circuit-workshop fence holds: no ecdsa.fail, mechanism, count, or tier-structure content anywhere in WP-27.
   - The known descriptor item ("five production LLMs" in the papers against "five frontier models" in the extractions and canon) is consistent between the two papers and remains the L097 rider on the register brief, first-person queue; not re-filed.
   - The L069(c) WP-04/WP-07 divergence remains notation-only and self-documented at moving_ceiling_sok.md:115-119.

4. Item 3, manifest coherence. Register head triple-agrees at C96 (research/CONJECTURE_REGISTER_V6.md:5, manifest.yaml:4, checks/check_register_refs.py HEAD). The tracker (tracker/index.html, generated by tools/fleet_tracker.py) mirrors the manifest at every swept WP including WP-27 at awaiting-P4, so it was rebuilt after L110; read as-is, no tracker finding. Frontmatter against manifest: WP-04 (draft-v4 + gate_target awaiting-P4), WP-07 (levelled per L098 F1), and WP-27 (draft-v3 + gate_target/handoff levelled per L110) all carry the executed levelled form; WP-28 draft-v3 agrees; WP-01 post-ready-v5 agrees (version field in body frontmatter). Two divergences found, filed as findings 1 and 2 below.

5. Item 4, ledger-tail audit (L095-L110): verdict in its own section below.

6. Item 5, known-tension registry. E1 is not on this cycle's explicit list; recorded out of band for the registry: check_versions on extractions/E1-amnesia-gap.md still fails with exactly the three L033 findings at the same lines as cycles 5-6 (:42 retired citation; :119 and :259 static-ceiling in faithful canon quotes), exit 1. Unchanged, not fixed, operative entry L033. The E10 "swept_complete at stated depth" coverage statement is NOT a finding per the card and L103; its depth statements are the fence, and the file's header, sweep record, and manifest note (manifest.yaml:24) mutually agree on that stated depth.

## Findings (nothing fixed at this seat)

1. **Manifest WP-02 row stale, two events behind the record.** manifest.yaml:30 carries `status: release-draft-v5` and the note "next A5 review 2", while the file is at release-draft-v6 (rehydrations/policy/enforceable_by_architecture.md:6, gate_target naming the L064(b) targeted re-check) and the ledger closed the review-2 loop on 2026-07-07 (L064 review 2 verdict; L067 revision executed at v6, loop CLOSED, release-strip awaiting the first-person author block; L110(b) already schedules the release-strip for cycle 9). The tracker inherits the stale row since it renders the manifest. Apparatus surface, A0-owned (manifest is A0-only); same family as cycle-6 F2. Proposed: A0 levels the row at serialisation or at the cycle-close rebuild.

2. **WP-03 frontmatter one station behind the manifest (the L098 F1 class).** rehydrations/grants/grant_edition.md:6-8 carries `status: draft-v3` with gate_target "A0 targeted re-check per L100(b); clean = P1" and handoff A0, while manifest.yaml:31 has WP-03 at release-draft-v3, gate P1, chain complete, first-person acts remaining (L101, which itself ratified a frontmatter levelling). The gate_target still reads as instructions for a station already passed. Proposed: A0 levels status/gate_target/handoff to the P1-passed, first-person-queue state, the class executed on WP-04 (L093), WP-07 (L098 F1), and WP-27 (L110).

3. **Tier undeclared in two TIER-P public drafts; GR-5 check arm cannot bind.** rehydrations/public/the_moving_ceiling.md:1-10 and rehydrations/public/the_uncarved_date.md:1-9 have no `tier:` key in frontmatter; the manifest declares both tier P (manifest.yaml:29, :54) and the sibling WP-28 declares `tier: P` in-file (competence_without_history.md:10). GR-2 requires every artifact to declare its tier in frontmatter, and checks/_common.py tier_of returns None without the key, so check_tier_vocab's TIER-P em-dash arm (GR-5) does not execute on these two files; their PASS cells are tier-blind. Manual census this run: zero em-dashes in both files (the_uncarved_date.md:9 "Acts 2–4" is an en-dash, which GR-5 does not ban). Coverage gap, not content breach. Proposed resolution is a rule question, not a fix this seat may make: either A0 adds `tier: P` to both frontmatters (one line each; WP-01 is post-ready, so the addition should ride a sanctioned micro-touch), or a recorded ruling states that publish-shaped public frontmatter omits tier, in which case a checks-maintenance card (A9 writes, ledgered per the role card) should teach the checks to classify by manifest.

## Ledger-tail audit (L095-L110)

Verdict: 15 of 16 entries fully accounted for; one orphan, L102(c).

| Entry | PROPOSED items | Disposition |
|---|---|---|
| L095 | (a) staleness item leaves sweep list; (b) L082(c)/L091(d) close on A9 verification; (c) nothing owed | executed (L098 (a)/(b); (c) vacuous) |
| L096 | (a) manifest flip; (b) widening card cycle 7; (c) Cx-a/b/c adoption | (a) executed in-session; (b) executed at L103; (c) queued first-person (restated in manifest E10 note) |
| L097 | (a) manifest flip; (b) A7 then A5; (c) WP-05/WP-26 routing; (d) descriptor rider | (a) executed; (b) executed L099/L100; (c) carried (L101(b), L110(b)); (d) queued first-person (register-brief item (e)) |
| L098 | (a) closes executed; (b) executed; (c) next A9 adds grant_edition + E10 widening output | executed: both are on this cycle's card list |
| L099 | (a) manifest flip; (b) A5 next; (c) A7 findings close | executed (L100) |
| L100 | (a) revision card; (b) re-check; (c) chain note | executed (L101) |
| L101 | (a) manifest flip; (b) first-person queue + WP-05/WP-26; (c) A9 adds grant_edition | (a) executed; (b) queued first-person / carried; (c) executed this run |
| L102 | (a) fence binding; (b) pre-P1 record resolutions; (c) A10 role-card refresh joins apparatus list | (a) executed L104; (b) executed L106; **(c) ORPHANED** — not executed, not in any next-cycle line (absent from L110(b)), not on the first-person queue; no carrier found in cycle-7/8 chronicles or tasks. Self-described non-blocking; still names no carrier. |
| L103 | (a) A2 draft cuts; (b) dating tension to first-person queue; (c) optional deepening card | (a) executed L104; (b) queued first-person; (c) optional, restated at L110(b) |
| L104 | (a) manifest flip; (b) A3 next; (c) obligations to citation station; (d) chain continues | executed (L105, L106) |
| L105 | (a) manifest flip; (b) A4 then A5-pc; (c) probe adopted | executed (L106, L107 probe run) |
| L106 | (a) A5-pc next, ambush closed; (b) ELN pass deferred unless pressed; (c) chain continues | (a)/(c) executed L107; (b) carried (named open in WP-27 §6) |
| L107 | (a) revision loop; (b) re-check; (c) A9 P3 then flip | executed (L108, L109, L110) |
| L108 | (a) A2 legs; (b) re-check; (c) N=3 adopted at placement | executed (L109) |
| L109 | (a) manifest flip; (b) A9 P3; (c) availability decision rides P4 | (a)/(b) executed (L110); (c) queued first-person (L107(2)) |
| L110 | (a) manifest flip; (b) cycle-9 slate; (c) WP-27 P4 to first-person queue | (a) executed; (b) weekly sweep = this run, WP-02 release-strip contingent on first-person author block (queued), WP-05/WP-26 on first-person direction (queued), E10 deepening optional; (c) queued first-person |

## Reversals

None this session. One scoping note recorded for honesty: the card's item 1 names a ten-file list in its own summary line while enumerating eleven files; the enumeration governs and all eleven were swept. No check was re-run to obtain a different result; the E1 run in item 5 is out-of-band registry evidence, not a matrix cell.

## Proposed ledger entry (returned to A0, not filed)

[Lnnn][WP-13][P3/weekly][2026-07-10][A9 (weekly sweep cycle 9; serialised by A0)]
FINDING: Cycle-9 sweep GREEN: 44/44 check cells PASS non-vacuous over the explicit eleven-file card list (three awaiting-P4 papers + policy brief + grant edition + three public drafts + both prior-art reviews + E10), exit 0 x4; argv-less guard probe holds (four checks, no args, exit 2, none exit 0). Register head triple-agrees C96 (register :5, manifest :4, check HEAD). Cross-doc NEW THIS WEEK verified: WP-27 trace map resolves against E10 at 31 claims (30 consumed exactly as declared; C31 exclusion reasoned); WP-04/WP-07 maps still resolve (non-basis E1 markers confirmed recorded exclusions); zero shared-external divergence across the three papers (Asif-Amiri bound+MI figures, AgentLeak 68.8/27.2/4,979 figures-with-metric, Patil preprint status, Chevignard CRYPTO 2025, Babbush ~10x spacetime-volume with metric carried, reconstruction chronology; WP-27 shares no externals and its circuit-workshop fence holds). Tracker mirrors manifest incl. WP-27 awaiting-P4 (rebuilt post-L110). L033 tension unchanged out of band (E1 :42/:119/:259). E10 stated-depth fence respected, not a finding (L103). THREE MINOR FINDINGS, fixed by no one at the seat: F1 manifest.yaml:30 WP-02 row two events stale (release-draft-v5 + "next A5 review 2" vs file v6 + L064/L067 loop closed; release-strip already on the cycle-9 slate); F2 grant_edition.md:6-8 frontmatter one station behind manifest P1 (the L098 F1 levelling class); F3 the_moving_ceiling.md/the_uncarved_date.md declare no tier: key (GR-2), so check_tier_vocab's GR-5 arm is tier-blind on them (manual census: zero em-dashes both; en-dash at uncarved :9 permitted) — resolution is a rule choice: add tier: P (WP-01 needs a sanctioned micro-touch, post-ready) OR rule public frontmatter tier-less and cut a checks-maintenance card to classify by manifest. LEDGER-TAIL AUDIT L095-L110: all PROPOSED items executed/carried/queued EXCEPT L102(c) ORPHANED (A10 role-card refresh "joins the apparatus list": no carrier in any next-cycle line, task, or queue; non-blocking by its own wording).
EVIDENCE: chronicles/2026-07-10_a9-weekly-cycle9.md (check matrix, external-comparison anchors, per-entry audit table); the check runs of record at this seat; manifest.yaml:30-31, enforceable_by_architecture.md:6, grant_edition.md:6-8, the_moving_ceiling.md:1-10, the_uncarved_date.md:1-9, L064/L067/L102/L110 at their entries.
PROPOSED: (a) A0 levels the WP-02 manifest row and the WP-03 frontmatter (F1/F2, the L093/L098/L110 executed class); (b) F3 routes to A0 as a rule choice, with the checks-maintenance card cut to A9 only if the tier-less ruling is taken; (c) A0 either executes L102(c) as a micro-touch, restates it in a cycle line, or closes it as declined, ending the orphan; (d) next A9 weekly adds the WP-09 standards draft and E7 when their chains reach a station, and drops nothing.
STATUS: proposed(returned to A0 by A9; A9 filed nothing)

## Handoff

- **Open questions:** F3's resolution path (declare tier in-file, or rule public frontmatter tier-less and reclassify by manifest) is A0's rule choice before any checks-maintenance card exists. L102(c)'s disposition (execute, carry, or decline) is A0's.
- **Blocked items:** none at this seat. Nothing in this sweep blocks any awaiting-P4 paper; all three remain untouched.
- **Next actions per WP touched:** WP-13: next weekly per cadence; add WP-09 and E7 to the list when on disk and past their first station. WP-02: A0 manifest row levelling (F1); release-strip card remains on the cycle-9 slate contingent on the first-person author block. WP-03: A0 frontmatter levelling (F2); first-person budgets/applicant block remain queued. WP-01/WP-25: F3 disposition, then nothing further owed by the runtime (WP-01 post-ready). WP-04/WP-07/WP-27: no action; awaiting P4, first-person queue.
