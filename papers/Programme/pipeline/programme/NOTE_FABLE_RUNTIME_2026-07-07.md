---
date: 2026-07-07
type: runtime-note
owner: A0 (first-person directed)
status: ACTIVE · cycle 1 cut and launched 2026-07-07
---

# The Fable auto-research runtime

## What this is

The paper-elevation runtime: a standing pattern of Fable-model agent sessions that
takes the already-decomposed research papers (the WP list in `manifest.yaml`; the
decomposition is decided and is not re-litigated here) and drives each one up the
gate ladder toward submittable form — draft → P0 → P1 → P2 → P3 — **stopping at P3
in every case**. P4 is the First Person's and no runtime session marks, simulates,
or proceeds past it (GR; manifest `p4_owner`).

This note is the runtime's boot file. Any fresh session resumes the runtime by
reading this note, then `GROUND_RULES.md`, then the open task cards in `tasks/`
whose frontmatter carries `runtime: fable`, executing the first not-DONE card in
its role, and writing its chronicle. The pattern is the autopath protocol
(`plans/V6_RESEARCH_AUTOPATH_2026-06-10.md` §0) applied to the publication atlas.

## Standing rules (inherit, do not restate)

- All of `GROUND_RULES.md` and the pipeline `CLAUDE.md` bind every runtime session.
- Canon read-only. Manifest A0-only. Ledger append-only. Chronicles mandatory.
- Math first, myth second: formal artifacts are built from extractions; no claim
  is strengthened to make prose flow.
- Nothing TIER-A ships without an IACR eprint preprint; prereg before the two
  empirical papers (WP-08, WP-11); no more than two standards contributions in
  flight (A13 sequences).
- No git commits or pushes from any runtime session; the First Person triggers those.

## The elevation loop, per paper WP

Each academic WP runs the same five-station loop, one role-session per station,
each session ending in a chronicle and (where owned) a ledger append:

1. **A10 · prior-art** — novelty sweep; what exists, what the paper may claim.
2. **A3 · formal draft** — skeleton → full draft from the WP's extraction, theorem
   discipline (assumptions explicit, conjectures as conjectures with confidence).
3. **A4 · citations** — every reference verified against the published text (P2).
4. **A5 · adversarial review** — persona reviewer for the venue; BLOCKING items
   loop back to A3; clean review = P1 evidence.
5. **A9 · consistency** — the four deterministic checks green (P3); then the card
   flips to `awaiting-P4` and the runtime touches it no further.

A0 (this standing session) cuts cards, serialises ledger appends, reruns
`tools/fleet_tracker.py` at every close-out, and keeps this note's cycle log.

## Sequencing (from the programme's own atlas)

- **Cycle 1 (now):** the enablers — A13 deadline verification (every venue date in
  `deadlines.md` is "assume until verified"); the submission scaffold (LaTeX/BibTeX
  templates per venue — the one thing the programme leaves unspecified); WP-04
  prior-art (the SoK is the nearest paper and feeds the flagship).
- **Cycle 2:** WP-04 A3 draft from E2 + the readiness-audit findings; WP-02 A5
  review 2 (its own chain, hard date 2026-08-01).
- **Cycle 3+:** WP-07/08 Paper One behind the SoK; standards notes (WP-06, WP-09)
  as A13's sequencing allows; WP-27 methods paper accumulates from the chronicles.
- The 42×n plurality rehydration layer stays parked per its own activation gate
  (WP-01/02 shipped, WP-07 at preprint, E10 exists). This runtime does not jump it.

## Model note

Runtime sessions run on the Fable model (session default as of 2026-07-07). Where
a station is proof-audit or citation-verification and the runtime operator judges
a tighter analytical register is needed, the A4/A9 stations may be run with a
model override; the chronicle records which model held the seat.

## Cycle log

- **2026-07-07 · cycle 1 cut:** cards `A13_deadlines_2026-07-07.md`,
  `SCAFFOLD_submission_templates_2026-07-07.md`, `WP-04_A10.md`. Launched as three
  parallel Fable sessions. Readiness audit of the existing paper corpus running in
  parallel; its report feeds the WP-04 A3 card in cycle 2.
- **2026-07-07 · cycle 1 CLOSED:** all three seats reported and chronicled.
  A13: deadlines.md fully verified, zero assume rows (L061 — BGIN pulls to Oct,
  First Monday closed, CPP 2027 precedes WP-16, PoPETs Issue 2 = 2026-08-31).
  A8: templates/submission/ built and compiled (21/21 verified bib; L063 carries
  a CANON-LEVEL v4.3 publisher correction for the first-person queue).
  A10: reviews/WP-04_prior_art.md — 40 works verified, 2 UNVERIFIED, zero
  CONTESTED; novelty ledger N1–N7 / S1–S6 (L062; SOURCES.md externals added).
  Session-limit interruption on A8/A10 mid-close-out; both resumed from
  transcript, outputs tail-checked, nothing rebuilt. Operational lesson: the
  chronicle is the last thing a limit kills — resume, verify disk, close out.
- **2026-07-07 · cycle 2 CLOSED (four seats, one same-day revision loop):**
  A3/WP-07: linear_cap_paper.md — the Nε cap PROVEN (Thm 5.1, conditional on
  ER-1..5, necessity both directions, tightness; only C86 carried as
  conjecture with its missing step named; L065). A2/WP-04:
  moving_ceiling_sok.md draft-v1 — 15/15 E2 claims, 68 trace markers, novelty
  fence honoured, checks PASS (L066). A5/WP-02: review 2 = MAJOR (the
  measurement-vocabulary self-contradiction — review 1's own prescription
  gone stale under the approved attestation frame; L064 with the A0 fence
  ruling) → A2+A8 revision to release-draft-v6 same day → A0 targeted
  re-check PASS on all five findings; review-2 loop closed (L067). Convergent
  catch of note: A2 and A3 independently flagged the same unregistered
  citation (arXiv:2509.14284) from opposite sides.
- **2026-07-07 · cycle 3 CLOSED (7 sessions incl. 3 micro-fix resumes;
  L068-L071):** the v6-docs update executed the pipeline way — extractions
  edited by A1 (E2-C07 Babbush+metric re-issue; E1-C40 reroute; the 2509.14284
  annotations cleared same-day after A4 verified it), register/canon changes
  filed as reviews/REGISTER_BRIEF_2026-07-07.md for the first person (C83
  annotate-or-split, C86 TIER-A carriage, C82 xref, v4.3 publisher diff x4
  sites). WP-04: A3 formal pass -> draft-v2, P0 PASSED (A0 spot-trace 3/3).
  WP-07: A4 pass -> ORTHOGONAL verdict with counterexamples both ways, Thm 4.1
  import-fidelity defect found and fixed, bib 21->60/0, P2 evidence on file.
  A7 letter (1,795 w) live on :7373 under PUBLISH-AFTER-EPRINT. Two more
  interruption events recovered by transcript-resume against verified disk.
- **2026-07-08/09 · cycle 4 CLOSED (6 seats + 5 micro-fix resumes;
  L072-L082):** WP-07 ran the whole ladder to the hard stop — A0 P0
  spot-trace (L072); A2 completion of the five stubs + A9 weekly sweep in
  parallel (L073-L075; the sweep's canon-level model-descriptor finding
  became register-brief item (e)); A5-crypto-pc review 1 = MAJOR REVISION
  (1 BLOCKING: Prop 4.2 false under carried state, counterexample supplied;
  4 MAJOR; 8 MINOR; core survived full re-derivation; L077); same-day
  revision loop (A3 math legs incl. Prop 5.5b adoption L078; A2 eleven-
  sentence re-alignment L079); A0 targeted re-check x6 with two hand
  re-derivations = P1 (L080); A9 P3 station blocked on one pre-review
  sentence, :207 fixed, re-run GREEN (L081/L082). **WP-07 = awaiting-P4.**
  Ops: one session-limit interruption recovered by transcript-resume;
  argv-less checks/ invocations found to pass vacuously — evidence lines
  corrected on the record (L082), guard is a hardening candidate.
- **2026-07-09 · cycle 5 CLOSED same-day (7 seats + 3 sanctioned resumes;
  L083-L093):** WP-04 ran the full ladder to the hard stop — A4 citations
  44/44 + L062 discharge (L085); pre-review repairs L087 (Mosca-Piani
  retarget, unresolved-works narrowing, CK attribution); A5 SoK review =
  MAJOR REVISION 0-BLOCKING/4-MAJOR/5-MINOR, core clean (L088); same-day
  loop: A3 seven items incl. Definition-3 bridge demoted to desideratum +
  Remark 2 availability semantics (L090), A4 Zcash pins (L089), L062(d)
  Kagai read referee-grade and ENGAGED, L062 closes entire (L091); A0
  re-check = P1 (L092); A9 P3 GREEN zero body findings (L093).
  **WP-04 = awaiting-P4** (FC workshops 09-01). Same cycle, off-ladder:
  WP-01 -> post-ready-v5 with the cycle-4 coda, arc reader serving :7373
  (L084); dual-agent harness brief written (chronicles/
  2026-07-09_dual-agent-harness-brief.md); first-person circuit-workshop
  note registered as the loop's second instance (L086); E2 FEEDS hygiene
  (L083). Hardening list for the weekly sweep: argv-less guard, R
  STATIC fix, prior_art row staleness.
- **2026-07-09 · cycle 6 CLOSED same-day (6 seats + the standing A0;
  L095-L101):** the maintenance cycle became the runtime's third full
  chain day. Hardening first, at the A0 seat, verified twice: the
  L082(c) argv-less guard (all four checks exit 2 loudly on a pathless
  run), the L091(d) STATIC split (\bR\b word-bounded case-sensitive
  digit-run-refusing; the prior_art "or <1450" false positive dead, the
  synthetic GR-7 probe still failing correctly) — A9's independent
  verification closed both. A10 reconciled prior_art.md's thirteen
  stale rows with the A4-verified metadata (L095; L093(b) leaves the
  sweep list). A1 built **E10 method-record, the WP-27 seed** (18
  claims at C96, earned-twice rules carrying both earning events,
  Cx-a/b/c NOT extracted pending first-person adoption, seven sources
  deferred to a widening pass; L096). A9 weekly sweep GREEN 32/32 with
  E10's first entry; its F1/F2 findings (WP-07 frontmatter staleness,
  manifest note duplicates) executed at A0 (L098). And **WP-03 ran its
  ENTIRE chain in one cycle** (L097-L101): A2 draft-v1 (eight work
  packages, 33 traced claims, budgets first-person placeholders) → A0
  P0 spot-trace 3/3 → A7 voice pass to draft-v2 with one honest
  weakening (the E1-C09 "compounding" flag adjudicated and micro-touched
  at A0 pre-review — the fix-before-review lesson applied) →
  A5-assessor review 1 = MAJOR REVISION 0-BLOCKING/4-MAJOR/5-MINOR
  (proven core traced clean; defects clustered in evaluation-criterion
  discipline) → same-day revision under four A0 programme-shape rulings
  (WP-H mechanisation floor; WP-C six-month windows + qualifying-instance
  rule; declared interfaces in place of asserted independence; WP-G
  month-0 feasibility gate) → A0 targeted re-check CLEAN = **P1, chain
  complete**. WP-02 release-strip still awaits the author block.
- **2026-07-10 · cycle 7 CLOSED (4 seats + the standing A0;
  L102-L105):** the methods paper was born and reached draft-v2/P0 in
  one cycle. A10 swept WP-27's prior art first (the L062 discipline):
  13 verified records + 2 inversion anchors, novelty = the ASSEMBLY
  (N1) plus three inversions (N2-N4), S1-S6 conceded with the
  strongest neighbours named in the sweep itself (Schuler-Zeller
  checked coverage; The AI Scientist as the non-delegable gate's
  defining anti-pattern; Certificate Transparency for append-only);
  fence BINDING (L102). A1 widened E10 in parallel: 18→**31 claims**,
  swept_complete at stated depth, second earning events on C12/C17,
  three findings filed not smoothed (the V5-audit 111/111
  self-contradiction carried as unreliable; the production-direction
  dating tension routed FIRST-PERSON; the SOURCES.md dream-chronicles
  descriptor corrected at A0) (L103). A2 drafted the paper from the
  widened extraction: 30/31 claims consumed, both contested items
  carried as CONTENT (the method catching its own instrument's
  overclaim is §4.4's strongest material), checks green on first
  invocation; A0 P0 spot-trace 3/3 (L104). A3 discharged the four
  formalisation stubs as Definitions 1-4 with design invariants
  I1-I12 — non-delegability formalised as an ABSENCE in the
  agent-only subsystem, the ledger's enforcement stated exactly as
  procedural-not-cryptographic, the production direction as a
  derivation-graph constraint with its own dating honestly indexed —
  and narrowed three sentences the sweep caught (L105). WP-02
  release-strip still awaits the author block; WP-05/WP-26 await
  first-person direction from the WP-03 base.
- **2026-07-10 · cycle 8 CLOSED (5 seats + 1 boot-death relaunch +
  the standing A0; L106-L110):** WP-27 ran its back half to the hard
  stop — the runtime's THIRD paper at awaiting-P4, and the first whose
  review probe caught the paper's own named failure mode firing inside
  the paper that names it. A4: 14/14 verified at primary records, both
  standing obligations discharged (Hilbert 1902 at its Bulletin DOI as
  the problem-list anchor; Evans 2003 first edition; Cooper 1990 at its
  journal record), both surfaces reconciled; the routed
  numbering-as-prior-art decision ruled ARGUE at A0 and applied
  pre-review (L106). A5-pc review 1 = MAJOR REVISION 0-BLOCKING/
  4-MAJOR/6-MINOR; the mandatory L105(c) probe found the 111/111
  catcher misattributed to "generation four" against E10-C24's own
  enumeration (MAJOR-1) — the strengthening failure mode, in the
  methods paper, caught by the method (L107). Same-day loop: A3 legs
  (I9 WEAKENED to exactly E10-C05 under the A0 extraction-shopping
  ruling; Definition 1 given its consolidation origin; the I_A
  adoption criterion = nine record-checkable invariants with three
  reasoned exclusions; L108) then A2 legs (E10-C24-verbatim
  reattribution + an added sentence recording, truthfully, that the
  misattribution was caught by the paper's own review station; the
  transfer hypothesis operationalised with N=3 pre-registered ladder
  transits and severally-vs-jointly null semantics; the
  record-availability paragraph stating current fact with release
  RESERVED to the first person; L109) → A0 re-check CLEAN = P1 → A9
  P3 with four MINOR count/direction findings micro-touched at A0
  against E10's own text, re-run GREEN (L110). OPS: the first A5
  instance died at boot on a session limit with nothing on disk —
  verified empty, relaunched fresh; the resume rule applies only when
  completed work exists.
- **2026-07-10 · cycle 9 CLOSED (5 seats + the standing A0;
  L111-L115):** the forward cycle — a fourth artifact entered the
  atlas's active set and two enablers landed. **WP-09 (BGIN
  separation-of-duties discussion paper) born and driven to
  draft-v2/P0 in one cycle:** A2 drafted from E1 at TIER-S first-run
  green under three A0 extraction-basis rulings (design-status claims
  admitted as design descriptions in the discussion-paper genre;
  conjectures as labelled open questions only; the c17/c18 exclusion
  confirmed) — eight open questions, four deliverables (L111); the E1
  filter/FEEDS reconciliation executed as an A1 micro-card on the
  L031 pattern (L114); A8 grounded every venue mechanic live
  (Block #15 2026-10-15/16 Washington D.C.; the IKP WG's CURRENT name
  form caught as a variance; SR-class documents; two in-genre
  exemplars; the group's own dual-agent-systems thread as venue-fit)
  or kept it deliberately generic (L115); A0 P0 spot-trace faithful
  with one fix-before-review narrowing (bounded-away-from-certainty)
  and the deadlines.md class softening executed. **E7 identity-vrc
  BUILT** (32 claims; 19 design-assumption at L008 discipline, 11
  conjectures at register wording; dtg-36-posts deferred honestly;
  checks read BEFORE drafting = first-run green, the ordering lesson)
  — WP-06's chain can start the moment a standards slot opens; the
  build also surfaced a CANON-LEVEL GR-7 candidate (the COM hearthold
  README asserting the strict bound statically, the exact L044 class)
  routed to the first person with the standing propagation item
  (L113). **Weekly sweep GREEN 44/44** with the ledger-tail audit
  finding the record's only orphan in sixteen entries (L102(c), the
  A10 role-card refresh — executed, mission generalised); WP-02
  manifest row and WP-03 frontmatter levelled; tier: P declared in
  the two public drafts, un-blinding the GR-5 check arm (L112).
  Standards-in-flight: 2 of 2 (WP-02 P1-blocked, WP-09 active).
  LATE-CYCLE FIRST-PERSON SEED (L116): the privacy-pools ceremony
  blog-seed chronicle arrived from the circuit-workshop side (the
  trust-gated loop's live instance, harness instance #4) — a public
  post series serialising the pool deployment as worked-in-public
  content, closing the arc's L038 gap with an event class that cannot
  be back-dated; staging fences BINDING (post 1 = method only,
  publishable now; posts 2+ trail the letter/kit/ceremony doors;
  numbers in the seed are courtesy copies of private authorities).
  A7 seated on post 1 same-cycle; Mitch's spin + posting = the gate.
- **2026-07-10 · cycle 10 CLOSED (3 seats + the standing A0;
  L118-L120):** **WP-09 completed its chain — the runtime's FIFTH
  artifact driven to its hard stop** (after WP-07, WP-04, WP-27
  academic and WP-03 grant): A5-regulator review 1 = MAJOR REVISION
  0-BLOCKING/3-MAJOR/5-MINOR with TIER-S discipline HOLDING under
  hostile reading — the defects were legibility and checkability,
  "the class on which a working-group chair loses the room" (the
  guarantee passage illegible to the members who must vote on it;
  the implementation record unattributed; the deficit declaration
  silent on who supplies H(X)) (L118) → same-day revision under
  three A0 rulings (the plain-reading gloss verified as a correct
  complement restatement of the Fano floor; proposer-attribution
  with availability in RESERVED form, no commitment minted, the
  L107(2) principle; the entropy-side sentence as its own paragraph
  protecting the spot-trace unit) → A0 spot-trace + targeted
  re-check CLEAN = **P1, chain complete** (L120). In parallel **E9
  proving-substrate BUILT** (22 claims, L008 design-vs-deployment
  per claim with the forge inventory re-verified directly; one
  honestly-CONTESTED practice-record drift in the shor-mage corpus
  tagged at E9-C21 and correctly downgraded from canon-level; the
  folding-citations registry gap executed; L119) — WP-22's enabler
  ready, gated like WP-06 on a standards slot. Both slots held
  (WP-02, WP-09 at P1 release posture).
- **2026-07-10 · cycle 11 CLOSED (2 seats + the standing A0;
  L121-L124) — THE OBSERVER-INTAKE CYCLE:** the first external
  observer layer entered the record. Mitch's two artefacts registered
  (L121): OBSERVER_INTAKE_PROTOCOL.md is now BINDING on runtime
  sessions (ten rules; "an observer can find seams; only the register
  decides stitches") and the OBS-GPT56 disposition ledger (28 claims,
  3 CTR candidates, 8 regression seeds) is registered non-canonical
  pending the Section-5 ruling. **A3 VERIFIED CTR-OBS-01 from first
  principles** (L123): under Precondition 1 joint leakage is
  SUBADDITIVE (equality needs marginal independence too); "holds
  exactly when" is wrong in both directions; **the floor SURVIVES
  conservatively — the observer's critique tightens the ceiling
  favourably**; blast radius = 10 exact-wording sites of which only
  TWO are pipeline-touchable (E1-C04; grant_edition:133), the three
  awaiting-P4 papers ALREADY CONFORMANT (no proof uses exact
  additivity — the A3/A5 stations had it right), plus one NEW find:
  pvm_v6_compressed:112 carries an unswept pre-L044 conflation (the
  L047 execution missed the compressed edition). **A9 converted the
  eight regression seeds** (L122): four audit-card items + the
  two-map decision procedure for RS-08 join the weekly; two
  check-script arms ruled in and IMPLEMENTED at A0 with
  both-direction probes ledgered (L124: the GR-7 retired sentence
  family as a static arm; historical-artefact-without-qualifier with
  SOURCES-fed patterns). Nothing touched canon, the register, or any
  awaiting-P4 surface; the consolidated decisions list went to the
  first person.
- **2026-07-10 · cycle 12 CLOSED (2 seats + the standing A0;
  L125-L127) — THE RULINGS-EXECUTION CYCLE:** the first person ruled
  on the observer decisions the same day they were asked (L125: the
  CTR-OBS-01/02 feedback on v5.4 INCLUDED IN THE V6 UPDATE ahead of
  its socialisation; observer material surfaces through CHRONICLES
  ONLY; the v5-root 96/64 correction approved; the
  observer-evaluation paper enters as candidate WP-29; D7 execute;
  WP-27's audit-invitation left open by design). Execution landed in
  full: **the canon additivity batch** (seven edits across four V6
  files on the L047 pattern — every exact-additivity site now
  carries the verified subadditive truth with the equality
  condition; pvm_v6_compressed :112 double-repaired incl. its
  unswept pre-L044 conflation; the V5.4 spec flagged superseded, not
  edited; the capacity-deficit iff FENCED intact everywhere; seven
  pre-edit backups at archive/canon-backups-2026-07-10/; net new
  check findings ZERO) + **E1-C04 re-issued** on the L044 pattern +
  the grant-edition inheritance line (artifact held at P1) —
  **AWAITING THE FIRST-PERSON DIFF REVIEW** (L127; before/after per
  site in the batch chronicle). **The skills 96/64 patch MADE**
  (uor-toroidal SKILL.md:34 corrected to the register's own
  resolution wording; the distinct 96-vs-192 question fenced open;
  THREE sibling stale surfaces found and routed, not over-applied;
  L126). WP-29 in the manifest, data-gated on CTR-OBS-03 behind the
  route-manifest ruling.
- **2026-07-10/11 · cycle 13 CLOSED (1 seat + the standing A0; L128)
  — THE AUDIT-AUDITS-THE-AUDITOR CYCLE:** the weekly sweep, first
  RS-adopted run, GREEN across 68 cells (65 PASS + E1's known L033
  FAIL(3) at exactly the predicted anchors); all five RS census items
  ran clean first time, non-flooding; the E1-C04 consumer-drift check
  CLEAN across WP-02/WP-03/WP-09 (only the licensed at-most direction
  cited; every surviving "exactly when" is the fenced deficit iff).
  The ledger-tail audit's second run caught the record's OWN error:
  L119(a) had recorded a manifest edit as "executed" before the edit
  was made, and it never landed. A0 executed the missing E9 levelling
  with the gap named inside the row, levelled WP-09's frontmatter
  (F2), corrected the record at L128, and banked the standing law:
  **"executed" is written AFTER the edit returns, never before.**
  Tracker regenerated (236 docs). Off-ladder at the first person's
  request: the twelve-cycles synthesis long read + the full LIBRARY
  READER (229 docs, wiki index) serving at :7474; A0 close-out now
  regenerates both readers alongside the tracker. A0 chronicle:
  2026-07-11_a0-fable-runtime-cycle-thirteen.md.
- **2026-07-11 · cycle 14 CLOSED (the standing A0 only, no seats;
  L129) — THE CLOSING CYCLE:** the RS-07 seed regexes gained their
  word boundaries (L129; RS-04's left deliberately unboundaried, no
  artifact observed) and the **CONSOLIDATION BRIEF written**
  (`programme/CONSOLIDATION_BRIEF_2026-07-11.md`): per-artifact final
  state, every remaining first-person act with its date, the gates in
  dependency order, the park definition. Nothing else was
  runtime-eligible and nothing else was started; the closing cycle's
  discipline is what it refused. **THE RUNTIME IS PARKED.** A0
  chronicle: 2026-07-11_a0-fable-runtime-cycle-fourteen.md.
- **Cycle 15 (armed, fires on the first-person diff review):** mirror
  regeneration + propagation ring, L127 closes, final weekly re-check
  over the levelled board, the runtime parks clean. No other scope
  without a new first-person ask.
  First-person queue (15): the standing thirteen (WP-07 ~08-24 ·
  WP-04 09-01 · WP-01 post · WP-02 author block 08-01 · register
  brief (a)-(e) · Cx-a/b/c · WP-03 acts · harness points 1-6 ·
  L103(c) · WP-27 P4 acts · L113(b) hearthold · pool post-1 · WP-09
  Block #15 acts) + **the canon-batch + skills DIFF REVIEW**
  (backups on disk; the batch chronicle is the review surface) +
  **the three sibling skill surfaces** (extend D5 now, or hold
  for the next content-addressed skill release).
