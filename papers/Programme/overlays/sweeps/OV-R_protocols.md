---
date: 2026-07-11
dimension: protocols
run: overlay-run-1
coverage: >
  Swept (RS-05 clause, scope stated at depth): GROUND_RULES.md, pipeline
  CLAUDE.md, pipeline README.md, observers/OBSERVER_INTAKE_PROTOCOL.md,
  reviews/OBSERVER_REGRESSION_SEEDS.md, and
  rehydrations/academic/conjecture_governance_method.md read IN FULL;
  programme/NOTE_FABLE_RUNTIME_2026-07-07.md read at the runtime-loop and
  cycle-log sections; programme/V6_RESEARCH_PROGRAMME_v2.md and
  rehydrations/standards/bgin_separation_of_duties.md by grep with hit
  windows; v6/privacy_value_v6_formal_specification.md by grep
  (protocol|ceremony|procedure) with §15 read in window;
  reviews/critiques_ledger.md GREP-ONLY with hit windows read at
  L043-L053, L100-L112, L121-L129; observers/OBS-GPT56_DISPOSITION_LEDGER.md
  structure skim only. Two canon-side anchors pursued outside the sweep
  list to ground named canon protocols: whitepapers/swordsman_mage_whitepaper_v6_3.md
  (RPP block) and lineage/understanding_as_key_zypher_paper_v1.md (ceremony
  tables). NOT swept: chronicles corpus, extractions, other rehydrations,
  SOURCES.md. This is one seat's route, not whole-corpus coverage.
items: 33
---

# OV-R · Protocols

Named repeatables of the V6 research corpus: the things with a name that
govern repetition. Every entry anchored (GR-9); readings amplify, never
strengthen. Anchors are absolute under root
`C:\Users\mitch\agentprivacy-docs\papers\` (paths below relative to it).

---

## A · The runtime's protocols (the pipeline that runs itself)

### The elevation loop (five stations)
- source: Programme/pipeline/programme/NOTE_FABLE_RUNTIME_2026-07-07.md:36-48; sightings: cycle log ibid.:73 ff.; reviews/critiques_ledger.md:629 ("chain continues ... per the elevation loop")
- formal twin: the per-WP station sequence A10 prior-art → A3 formal draft → A4 citations → A5 adversarial review → A9 consistency, one role-session per station, terminating at `awaiting-P4`; the runtime "stopping at P3 in every case"
- reading: every paper climbs the same stair, one seat per step, and the stair ends one step short of the door on purpose. The loop is the corpus's heartbeat: cut cards, seat roles, chronicle, close.
- threads: [P: "the gates are the walls" (README coda); F: the AI Scientist as the anti-pattern that automates the last step (?); S: none, and the absence is the GR-4 fence working]
- casts forward: any new artifact class (WP-29 observer-evaluation paper is already a manifest candidate) inherits the loop unchanged.

### The gate ladder P0-P4 and the non-delegable P4 gate
- source: Programme/pipeline/README.md:43-48; rehydrations/academic/conjecture_governance_method.md:297-305 (Definition 2, invariants I5-I6); pipeline CLAUDE.md hard rules ("You never mark gate P4")
- formal twin: Definition 2 formalises the ladder as a labelled transition system in which exactly one transition enters `complete` and it is human-labelled; non-delegability is an ABSENCE of transitions, unreachable in the agent-only subsystem (I5), extended to publication and version control (I6)
- reading: the runtime's whole theology in one machine state: `awaiting-completion` is a literal state after which no agent touches the artifact. The gate is not a policy that could be broken but a transition that does not exist.
- threads: [P: "p4 is the door only you hold" (README:76); P: "the proposer does not approve its own proposal"; F: non-delegability as the refusal the AI Scientist lacks (?)]
- casts forward: the transfer hypothesis (below) makes I5/I6 checkable in any adopting team's own record.

### The session rite (boot sequence and chronicle close)
- source: Programme/pipeline/CLAUDE.md (boot steps 1-5); Programme/pipeline/README.md:28-32 ("That sentence is the whole protocol"); conjecture_governance_method.md:311 (chronicle instrument)
- formal twin: E10-C13/E10-C16: fixed boot order (ground rules, role card, task card, then role + permitted writes + definition of done stated back in three lines), and the mandatory closing chronicle, verdict-first with reversals at progress-prominence; "a session without a chronicle is unfinished"
- reading: every seat is born the same way and dies the same way; the rite brackets the work so no session's memory is load-bearing. What the seat learned survives it in a file it may never edit again.
- threads: [P: "a session without a chronicle is unfinished"; P: verdict-first as house voice; R: contemporaneity rule (below)]
- casts forward: the chronicle corpus is E10's ore body; every rite performed is a future methods claim.

### The seat discipline (one role, one card, one writer per file)
- source: conjecture_governance_method.md:253 (E10-C13); Programme/pipeline/README.md:35-40 (one branch per WP; manifest A0-only; ledger the only shared write surface)
- formal twin: the concurrency law of the fleet: exactly one role per session, out-of-role fixes refused even when competent, serialised handoffs on contended files
- reading: an auditor that found a defect and fixed nothing, routing it to the owning role, is the discipline's proudest fossil. Competence is not licence.
- threads: [P: "route, never fix, out of role" (?); S: ⊥ as separation of duties, the orthogonality operator worn by the org chart (?)]
- casts forward: the BGIN separation-of-duties paper carries the same shape outward as a standards work item.

### The ledger entry form (append-only, FINDING/EVIDENCE/PROPOSED/STATUS)
- source: conjecture_governance_method.md:315-325 (Definition 3, I7-I9 with the procedural-enforcement remark); Programme/pipeline/README.md:38; reviews/critiques_ledger.md:773 (the L128 corollary)
- formal twin: I7 append-only core, I8 corrections-are-entries, I9 STATUS as the sole designated mutable field; enforcement procedural, not cryptographic, and the paper says exactly that; the L128 standing law: "executed this session" is written AFTER the edit returns, never before
- reading: the ledger is the memory that cannot be flattered, only lengthened. When the record itself overstated (L119's phantom manifest flip), the sweep caught it and the correction was filed as one more entry: the record corrected itself in its own grammar.
- threads: [P: "an audit trail that never admits error is evidence of nothing"; P: "the ledger records what happened, not what was intended"; F: Certificate Transparency as the cryptographic cousin deliberately not claimed]
- casts forward: the enforcement remark names the upgrade path (hash chains) without promising it.

### The same-day revision loop
- source: conjecture_governance_method.md:383 (§4.3); reviews/critiques_ledger.md:644-660 (L107→L108→L109, the WP-27 instance run entire in one day)
- formal twin: E10-C09: adversarial persona review with priced findings (BLOCKING/MAJOR/MINOR) → findings routed by competence (A3 mathematical legs, then A2 prose legs, serialised on one file) → A0 targeted re-check against the reviewer's pre-stated successor criterion; three instances closed same-day in the recorded window
- reading: review, repair, and re-check inside a single sun; the loop is fast precisely because every judgement was priced before the race started.
- threads: [R: successor-criterion re-check; R: fix-before-review; P: "make the honest form cheaper than the fluent form"]
- casts forward: the loop is the unit the transfer hypothesis counts ("full ladder transits").

### The successor-criterion re-check
- source: conjecture_governance_method.md:247 and 377 (E10-C08: "the reviewer rules on its own successor, stating what re-examination suffices"); reviews/critiques_ledger.md:605 (L100(b)), :646-:647 (the L107 five-leg criterion), :722 (L120 per the L118 criterion); rehydrations/standards/bgin_separation_of_duties.md:10
- formal twin: the review memo carries what-satisfies lines and a named successor criterion; a clean A0 targeted re-check against that criterion constitutes P1 evidence with no second full review (L080/L092/L101 precedent line)
- reading: the reviewer writes its own replacement's job description before leaving the room. Goalposts cast in advance cannot be moved after the kick.
- threads: [R: pre-registered verdict rules with "cannot decide" honoured; P: "never softened after the fact"]
- casts forward: named in Section 5 of the methods paper as one of the residual novelties the prior-art sweep found unclaimed.

### The fix-before-review discipline
- source: conjecture_governance_method.md:251 (E10-C10); reviews/critiques_ledger.md:639 (L106: "adjudicated at A0 per the fix-before-review discipline, L099 precedent")
- formal twin: findings already on the record are repaired before the adversarial seat reads; earned against the first paper loop, where reviewer attention was spent re-finding known defects; executed as a dedicated pre-review card, after which a review returned zero blocking findings
- reading: do not pay a hostile reader to find what you already know. Sweep your own floor before the inspector crosses it, so every finding they file is new information.
- threads: [R: same-day revision loop; P: reviewer attention as the scarce resource (?)]
- casts forward: -

### The weaken-vs-widen ruling
- source: reviews/critiques_ledger.md:645 (L107 ruling (1): "MAJOR-2 = WEAKEN, not widen — commissioning an A1 widening to license an already-written formalism would be extraction-shopping"); execution at :651 (L108) and conjecture_governance_method.md:122-127 (A3 addendum, I9 weakened to exactly E10-C05 content)
- formal twin: when a formal statement exceeds its extraction basis, the statement is weakened to what the record carries; the record is never widened after the fact to license the statement
- reading: the fix runs downhill, always: prose bends to evidence, evidence never stretches to prose. "Extraction-shopping" is the ruling's coinage for the forbidden direction, and the coinage alone polices it.
- threads: [P: amplify-never-strengthen, the overlay's own governing law, is this ruling wearing poetry (?); R: trace-or-delete]
- casts forward: a standing precedent for every future formalisation pass that outruns its extraction.

### The RESERVED form (L107(2))
- source: reviews/critiques_ledger.md:645 (L107 ruling (2): "state CURRENT FACT and reserve the promise"); conjecture_governance_method.md:417 (§6 availability paragraph: "recorded here as reserved, not promised")
- formal twin: when an artifact must speak about a decision that is the First Person's (record availability, release), it states present fact only and records the decision as reserved to the principal; no commitment is minted by the runtime on the principal's behalf
- reading: the runtime learned to hold a door open without walking through it. A reserved promise is a shape in the text where a human decision will later sit.
- threads: [R: non-delegable P4 gate (the same absence, applied to speech acts); P: "recorded as reserved, not promised"]
- casts forward: the record-availability disposition rides WP-27's first-person acts (L109(c), L110).

### The L044 decomposition procedure (and its L047 canon-batch pattern)
- source: reviews/critiques_ledger.md:261-265 (L044), :284-288 (L047 execution), :314-318 (L052 extraction leg); pattern reused at :765 (L127, the additivity batch "on the L047 pattern") and cited as "the L044 class" at :729 (L121)
- formal twin: the canonical route for a canon-level wording defect: name the conflation (preconditions vs the capacity-deficit condition C_S + C_M < H(X)); route via GR-10 to the register process, never fixed in rehydration; execute as a batch with pre-edit backups, complete before/after chronicle, and first-person diff review reserved; re-issue the extractions (A1 leg); negative-sweep downstream consumers
- reading: one conflation found in one brief became a named surgical procedure the corpus now performs on itself: locate, escalate, back up, cut, show the surgeon the sutures. When the observer packet found the additivity defect, the house already knew which operating theatre to book.
- threads: [R: GR-10 escalation; R: Observer Intake rule 5 (formal corrections route formally); F: moving ceiling R(t), whose decomposed wording the procedure protects]
- casts forward: the compressed-edition miss (L123) shows the procedure now audits its own past executions for completeness.

### Resume-verify-disk recovery
- source: conjecture_governance_method.md:245 (E10-C07), :375 (§4.2 both earning events); reviews/critiques_ledger.md:647 (L107 OPS NOTE: "the resume-not-rebuild rule applies only when completed work exists to resume")
- formal twin: an interrupted agent's work products are trusted from disk after verification, nothing re-run; the complementary half, earned in the second instance: no decision-bearing verdict from an interrupted run is trusted without re-execution; the empty-disk corollary: verified-empty means relaunch fresh
- reading: what dies in an interruption is the close-out, not the work; resurrection is a verification act, not a rebuild. Trust the disk for artefacts, trust nothing for verdicts.
- threads: [F: amnesia gap, the same erasure worn by the pipeline's own sessions (?); R: session rite]
- casts forward: one of the four rules earned twice, hence load-bearing in the transfer hypothesis.

### Trace-or-delete (GR-9)
- source: Programme/pipeline/GROUND_RULES.md:26; conjecture_governance_method.md:241 (E10-C04, with the enforcement instance: a policy brief's central test deleted at re-trace)
- formal twin: every rehydration claim traces to an extraction line, every extraction line to canon or the verified record; an untraceable claim is deleted, not defended; earned against citation laundering around the registry
- reading: the corpus's digestion: nothing is retained that cannot say where it came from. It was this discipline, not any later instrument, that caught the 111/111 overclaim sleeping in the early record.
- threads: [P: "a claim that cannot be traced is deleted, not defended"; R: this sweep's own no-anchor-no-entry rule is GR-9 wearing overlay dress]
- casts forward: -

### The canonical-figures fence (GR-3)
- source: Programme/pipeline/GROUND_RULES.md:14
- formal twin: the figures 678x, 31,000x, 70:1, 74x appear only in sanctioned formulations or not at all (TIER-S/A default: not at all); fiat value figures retired suite-wide per L057, with the check's dollar pattern kept as the reintroduction fence; enforced by checks/check_figures_fence.py (README:56)
- reading: the corpus keeps its most quotable numbers behind a fence and posts a scripted guard. A retired figure's regex remains on duty precisely so the figure cannot creep home.
- threads: [R: non-vacuous checkers; P: value expressed "in protocol units, ratios, or implication"]
- casts forward: -

### The two-register discipline and the vocabulary map (GR-4)
- source: Programme/pipeline/GROUND_RULES.md:16; conjecture_governance_method.md:329-345 (§3.4, Definition 4, invariants I10-I12 with the temporal index)
- formal twin: Swordsman → boundary agent S, Mage → delegation agent M, Amnesia Protocol → structural context erasure, the Gap → conditional-independence residual; production direction fixed formal-first (I10), citation mediated through extractions (I11), the sole narrative-to-formal channel human-licensed candidate minting (I12); "no emergence" a valid harvest
- reading: one body of claims, two tongues, one-way water. The inversion of Evans's ubiquitous language is the methods paper's second contribution: two vocabularies kept apart on purpose, with the myth harvested from the maths and never the reverse.
- threads: [S: the emoji ban at TIER-S/A is this protocol's fence, absence-as-data; F: every OV-F concept lives on the narrative side of exactly this wall; P: "math first, myth second" (NOTE_FABLE:29)]
- casts forward: the dated qualification (the earlier narrative-first flow) stays ledgered, not smoothed: the discipline admits it was learned.

### The gate-brief instrument (confirm-or-override)
- source: conjecture_governance_method.md:293 (E10-C19: fixed form; unmarked disposition is not confirmed; signature scope written out; overrides recorded verbatim and executed; closed per-candidate vocabulary, "nothing binds without the word")
- formal twin: the form that makes partial human decisions well defined at chronicle gates; six such gates run and signed in the pre-pipeline record (E10-C03); governs its own reopening (the eighteen-days-later register-minting episode)
- reading: a brief with holes cut in it for a human hand; silence never defaults to yes. Even reopening a closed path takes a fresh gate, because the standing rule is absolute.
- threads: [R: RESERVED form; P: "nothing binds without the word"; P: "nothing publishes unread" (the reading-ledger ancestor, ibid.:291)]
- casts forward: the disposition-block shape reappears in the observer decisions list (L125's D1-D8).

### The late-contribution patch protocol
- source: conjecture_governance_method.md:295 (E10-C23: "a contribution arriving after a path has closed runs as an appended run with its own write-point gate")
- formal twin: actions partitioned by gate-dependency: mechanical pieces and prose conforming to authoritative decisions apply immediately; number minting and cross-links into locked artifacts stage behind the gate, so a locked artifact never cites an unminted number; epistemic accounting kept separate from framing gain
- reading: latecomers do not climb over the wall; a new gate is built for them. And a better story about a claim moves its framing, never its confidence.
- threads: [R: gate-brief instrument; R: register mechanics I2/I4; P: "the proposer does not approve its own proposal"]
- casts forward: names the promotion bar the transfer hypothesis reuses (an empirical second instance, not a reframing).

### The proposer-approval fence (origin-first reflection; read-only standing surveys)
- source: conjecture_governance_method.md:355 (E10-C22, reflection ledger executed after the path closes, wave log honest at target granularity) and :357 (E10-C29, daily surveys that change nothing but themselves, carried-forward items marked stale-still)
- formal twin: two instruments realising one rule: while a path runs, no agent edits outside the origin; reconnaissance drafts proposals to application readiness and explicitly does not apply them
- reading: the fleet may look anywhere and touch only home. A suggestion not taken is re-shown as stale-still rather than silently re-proposed, so non-execution stays visible.
- threads: [P: "the proposer does not approve its own proposal" (stated at both anchors); R: non-delegable gate, the same absence at reconnaissance scale]
- casts forward: -

### The non-vacuous-checker discipline and the L091(d) synthetic-probe model
- source: conjecture_governance_method.md:243 (E10-C06), :373 (earned twice), :405 (§5, generalisation of checked coverage); Programme/pipeline/README.md:50-63 (the four checks); reviews/OBSERVER_REGRESSION_SEEDS.md:31 (the probe model: "probe file outside the tree, run, then deleted"); reviews/critiques_ledger.md:747 (L124: both-direction probes ledgered)
- formal twin: a check with nothing to check must fail, not pass (argv-less invocation exits with an error by design); every new check arm ships with a FAIL probe and a PASS counter-probe run in both directions and ledgered; evidence-of-record lines state the exact invocation
- reading: the vacuous green stood in the record for two gates before an audit caught it; the structural close means an empty test can never again smile. Each new trap is armed by deliberately springing it once.
- threads: [P: "a verification pass reporting success on zero items is suspect"; R: traps-become-tests; F: mutation testing as the published twin]
- casts forward: prediction (i) of the transfer hypothesis: every adopting loop will record a vacuity observable of its own.

### The transfer-hypothesis adoption protocol
- source: rehydrations/academic/conjecture_governance_method.md:435-441 (§7: hypothesis, adoption criterion I_A = {I1,I2,I4,I5,I6,I7,I8,I10,I11}, period = N pre-registered full ladder transits, default N = 3, severally-vs-jointly null semantics); adoption rulings at reviews/critiques_ledger.md:653 (L108(c), N=3 adopted at placement)
- formal twin: the method's reusability stated as a falsifiable protocol: an adopting team checks nine invariants from its own record alone, fixes N in advance in its own register, and files any null at win-prominence
- reading: the method ends by writing the instructions for its own possible refutation, exclusions reasoned one by one (I3 vacuous in a first period; I9 subsumed; I12 a composition). A governance method that ships its adoption test is the register discipline pointed at itself.
- threads: [R: gate ladder, ledger, two-register discipline (the four components being adopted); P: "a result against the model's prediction is filed with the same prominence as a confirmation"]
- casts forward: the first outside adoption would be the method's promotion event; the paper waits at awaiting-P4 to say so.

---

## B · The observer layer's protocols (the outside eye, governed)

### The Observer Intake Protocol
- source: Programme/observers/OBSERVER_INTAKE_PROTOCOL.md:16-91 (verdict, classification header, the ten binding rules, human gate, run-completion criteria); adopted onto the runtime at reviews/critiques_ledger.md:729 (L121)
- formal twin: observer packets enter as non-canonical structured critique, decomposed into atomic claims, each dispositioned `accepted | amended | rejected | deferred` (rule 3: four dispositions only, no fifth state, no silent expiry); CTR-series only, C-series is Mitchell's alone (rule 4); no score ingestion (rule 7); projections are not corroboration (rule 8); rights before ingestion (rule 9)
- reading: the corpus's immune system for outside intelligence: welcome the critique whole, digest it one claim at a time, and let nothing however brilliant write on the canon directly. The route the observer walked is itself evidence; so are its errors.
- threads: [P: "an observer can find seams; only the register decides stitches"; P: "confer before you change; verify before you confer"; R: two-map doctrine (rule 6); R: traps-become-tests (rule 10)]
- casts forward: OBS-GPT56 is only the first instance; the header schema expects a lineage of observers measured against the same traps.

### The two-map doctrine and the three-question decision procedure
- source: Programme/observers/OBSERVER_INTAKE_PROTOCOL.md:53 (rule 6: canon-and-evidence map vs experience-and-route map, never collapsed); Programme/pipeline/reviews/OBSERVER_REGRESSION_SEEDS.md:136-148 (RS-08: the three questions, map tag + deciding question required on every drift filing)
- formal twin: Q1 both sides evidence-bearing → canon map, always; Q2 a canonical source decides the value → canon map, mystery is never version authority; Q3 ambiguity declared on record → route map, else deferred to the human gate, because intent is Mitchell's alone to claim
- reading: the paired trap is the one that matters most: drift dismissed as mystery, or mystery bulldozed as drift, and both directions fail. Three questions asked in order give every discrepancy exactly one home, and the deferred filing is the safe harbour when intent is unknowable at the seat.
- threads: [P: "preserve mystery in the journey, remove ambiguity from the evidence" (observer-coined, retained under attribution); F: intentional discovery friction as designed experience (?)]
- casts forward: from L122(c) every drift-shaped ledger finding carries its map tag and question number; the doctrine became a field format.

### Traps-become-tests (the regression-seed conversion)
- source: Programme/observers/OBSERVER_INTAKE_PROTOCOL.md:61 (rule 10); Programme/pipeline/reviews/OBSERVER_REGRESSION_SEEDS.md:16-18 (all eight seeds RS-01..RS-08 converted, house pattern: point at the owning fence, never build a parallel one); reviews/critiques_ledger.md:735 (L122), :747 (L124 first two script-level instances)
- formal twin: every observer error class caught or self-corrected becomes a seeded regression trap: check-script cases (RS-01 HISTORICAL arm, RS-03 retired-sentence-family arm, both live per L124) or A9 audit-card items (RS-04/05/07/08); the corpus deliberately retains known traps so future observers can be measured against them
- reading: the corpus keeps its traps named and armed. An observer who avoids all eight has read well; one who springs one has taught the house where its surfaces still mislead.
- threads: [P: "traps become tests"; P: "two label systems for one trap is itself a drift generator"; R: non-vacuous checkers]
- casts forward: RS-01's pattern list grows from SOURCES.md historical/superseded flags at each maintenance touch: the trap register is designed to breed.

### The RS-05 scope-honesty census (the coverage statement)
- source: Programme/pipeline/reviews/OBSERVER_REGRESSION_SEEDS.md:85-97 (three clauses: every green verdict names its enumeration; totalising claims checked against their grounding; every extraction header carries its coverage statement at stated depth, the E10 pattern, L103 fence)
- formal twin: a weekly A9 audit-card item formalising the trap "single route or surface treated as whole-corpus coverage"; live precedent the /model over-weighting (OBS-GPT56-005)
- reading: no verdict may say "suite-wide" unless it can show the list it walked. This sweep's own frontmatter coverage clause is the protocol obeying itself.
- threads: [R: Observer Intake rule on route evidence ("a single route is never labelled whole-site coverage", protocol §4); P: scope named or verdict void (?)]
- casts forward: ran clean on its first adopted weekly (L128, cycle 13).

### The D2 chronicle-surfacing rule
- source: reviews/critiques_ledger.md:753 (L125 D2: observer feedback documents "surface ONLY THROUGH THE CHRONICLES — the runtime's reflections on why it modified things — not through any public property, release manifest, or projection"); observed at :761 (L126(c)); memory of standing use in the V6 rehydration line
- formal twin: a first-person ruling binding all future observer-material handling; dissolves the release-substrate hosting question for observer packets and rests the INT-01 interaction
- reading: the outside eye's words reach the public only refracted through the house's own diary of what it changed and why. The observer is heard everywhere and quoted nowhere.
- threads: [R: Observer Intake rule 7 (no score ingestion) and rule 8 (projections are not corroboration); P: "the ledger remembers both" (protocol coda)]
- casts forward: WP-29, the candidate observer-evaluation paper, will have to cite through this same single aperture.

---

## C · The canon's protocols (the model's own rites)

### The Relationship Proverb Protocol (RPP)
- source: whitepapers/swordsman_mage_whitepaper_v6_3.md:77, :335-367 (definition, the embedded directive at :351, the robustness honesty note at :367); in-corpus sightings v6/privacy_value_v6_formal_specification.md:1059 ("Assessment | RPP compression as verification of knowledge transfer")
- formal twin: a compression protocol proving comprehension: one proverb formed = one signal posted; in Promise Theory terms an assessment mechanism (compression proves the promise of knowledge transfer was kept); explicitly "not a cryptographic security boundary — an epistemic verification layer"
- reading: before you may speak about the work, you must fold it through your own life and hand back the crease. The proverb is a receipt for understanding, and two receipts from two lives become a cipher between their holders.
- threads: [P: the whole OV-P dimension is RPP's output stream; S: spell compression as the next stage of the same pipeline (proverb → spell → match); F: knowledge that resists extraction while inviting engagement]
- casts forward: RPP-derived compressions as private cipher for Swordsman-Mage internal coordination (whitepaper :409) points at agent-to-agent protocol work.

### The VRC promise protocol
- source: v6/privacy_value_v6_formal_specification.md:1001 ("Relationship | VRC | Bilateral commitment (promise bundle)"), :1061, :1113 (VRC = Verifiable Relationship Credential, promise bundle); companion spec named at whitepapers/swordsman_mage_whitepaper_v6_3.md:1929 (specs/vrc_promise_protocol_v3_3.md, filename/version tangle recorded at reviews/critiques_ledger.md:297, L049); conjecture home C43/C44 (spec :856-857)
- formal twin: the relationship layer of the three-layer identity architecture (E7 territory, programme :76: relationship-rooted identity vs attribute-rooted; VRC lifecycle; formation route "Knowledge Engagement (RPP) → ... → VRC Formation", whitepaper :1091); per-VRC viewing-key disclosure conjectured strictly more private than unscoped (C43, ~60%)
- reading: a relationship as a bundle of kept promises, credentialled bilaterally and scoped to itself; identity grown from what two parties did together rather than what either is. The protocol even carries a filename that disagrees with its own header, and the ledger holds that too.
- threads: [P: promise-theory assessment (α); S: 🪢 the knot as relationship mana (?); R: RPP as the formation ceremony's first movement]
- casts forward: WP-19/WP-20 (RWOT, W3C CCG, ToIP) carry the VRC architecture into standards bodies via E7.

### The Amnesia Protocol
- source: v6/privacy_value_v6_formal_specification.md:618-683 (§14, the V5.3 inheritance and its V6 cohomological upgrade), :587 (C73: terminal obstruction, its canonical instance); GR-4 translation at Programme/pipeline/GROUND_RULES.md:16 ("structural context erasure between agent invocations")
- formal twin: §14.1: no sequence of permitted operations reconstructs O from the agent's current state (reachability), upgraded at C86 to the gluing question (can local views be glued into a global witness); Grade-1 vs Grade-2 forgetting given a formal criterion (vanishing vs non-vanishing class); falsification test stated in-text
- reading: forgetting is not a locked door but the absence of any road, because the base case is gone. The canon's oldest named protocol, and the one the whole formal register was built to hold to account.
- threads: [F: the amnesia gap, OV-F's centrepiece; R: the vocabulary map, which renames it at the fence; P: "this is topology, not policy" (spec :723)]
- casts forward: OQ-2 in the BGIN paper (the chain break as an open engineering question, bgin :318) is the protocol's standards-facing echo.

### The Progressive Trust ceremony ladder
- source: v6/privacy_value_v6_formal_specification.md:700-704 (§15.2: 🔑 → ✦ → 🗡️ → 🔮, Understanding → Constellation → Blade → Runecraft, "each level is a complete ceremony")
- formal twin: four ceremony levels, each deepening the key, increasing formal visibility, and shifting boundary-making; progression maps onto trust tiers (dual-axis tier classification at §15.6)
- reading: trust is climbed one completed ceremony at a time, and the key you carry is reshaped at every landing. Nothing is skipped: the ladder is the protocol.
- threads: [S: the four-glyph string is an OV-S seal in its own right; R: ceremony types by visibility (the ladder's sibling from the Understanding-as-Key line); P: understanding as the first key]
- casts forward: -

### The Operational Cycle as Ceremony
- source: v6/privacy_value_v6_formal_specification.md:691-698 (§15.1: Observe id(x) ☀️ Sun disclosure · Boundary neg(x) ⊥ Gap silence · Project bnot(neg(x)) 🌑 Moon shared reflection · Return succ(x) recursion, Reflect or Connect)
- formal twin: the algebra's four primitive operations mapped one-to-one onto ceremony phases; the Return fork (night blade-pair ZK, or day witness carry-forward) is the cycle's only choice point
- reading: the model's arithmetic performed as liturgy: identity is disclosure, negation is silence, double-negation-of-negation is shared reflection under the Amnesia moon, succession is the walk onward.
- threads: [S: ☀️ ⊥ 🌑 as the cycle's glyph row; F: day/night as visibility regimes (?); R: Amnesia Protocol seated at the Project phase]
- casts forward: -

### The runecraft protocol
- source: v6/privacy_value_v6_formal_specification.md:716-723 (§15.4: Mage key Ed25519 persisted, Swordsman key Ed25519 in sessionStorage destroyed on tab close; "the private key burns because the amnesia protocol (C17) requires structural inability to access shared origin")
- formal twin: Φ_agent enforced at the cryptographic identity layer; bilateral binding = dual Ed25519, one held, one burned (§15.3 table); process boundary = separate memory = structural amnesia, "topology, not policy"
- reading: the ceremony's deepest level signs with two keys and then eats one. The burn is not theatre; it is the amnesia theorem cast in key management.
- threads: [R: Amnesia Protocol (the burn's warrant); S: 🔮 as the ladder's terminal glyph; F: the key that must not survive its own ceremony]
- casts forward: RS-07's fence patrols exactly this border: the burn is meaningful ceremony AND real key destruction, and the corpus polices which register each claim is made in.

### Ceremony types by visibility (Shadow · Guarded · Balanced · Open · Declared)
- source: lineage/understanding_as_key_zypher_paper_v1.md:549-557 (the five-type table: 0% / 38.2% / 50% / 61.8% / 100%), :669-674 (ceremony lifecycle, relationships may re-ceremony at different visibility), :1186 ("the visibility ratio chosen at ceremony time is itself a signal"); the sibling five crossing types at whitepapers/swordsman_mage_whitepaper_v6_3.md:659 and spec :1337 (Ceremony Engine, Act XXVIII)
- formal twin: proverb-based ceremony architecture: five visibility settings for the bilateral proverb commitment, golden-ratio graded (38.2/61.8), with the invariant that "the ceremony NEVER exposes both complete proverbs publicly" (:727); ceremony progression as a trust ladder
- reading: how much of a bond the world may see is chosen at the altar and is itself a message: privacy-first or openness-first, guarded or declared. Five weather settings for one rite.
- threads: [S: moon-phase visibility strata (spec §15.5) as the same dial worn by sovereignty (?); R: Progressive Trust ladder; P: "the ceremony creates only a commitment hash"]
- casts forward: -

### The presence-economy regime ladder and the G3 regime declaration
- source: v6/privacy_value_v6_formal_specification.md:756-764 (§15.8: the three-rung ladder — local colour → witness co-signing → elapsed-time proofs — and the First Person's Regime Declaration of 2026-06-10 quoted in full)
- formal twin: 🪢 presence mana scoped non-transferable and non-attesting at rung (1), with replay/simulation/sybil named as the live attacks the moment it attests; the binding rule: no surface may call presence proof, stake-weight, or attestation input until the economy moves up the ladder first
- reading: an economy that declares its own weakness in public and posts the upgrade path beside it. "The architecture earns the claim before the prose makes it" is the declaration's whole spine, and it is signed at a gate, first-person, dated.
- threads: [P: "architecture over policy"; R: gate-brief instrument (a G3 declaration is a signed gate in canon dress); S: 🪢 the knot; F: the headless walker simulating presence at machine speed]
- casts forward: C42 (stake economics vs Sybil resistance, ~50%) is the ladder's open mathematics.

---

## Coda · the dimension's shape

The protocols come in three strata that mirror each other. The runtime's
gate ladder, the observer's four-disposition intake, and the canon's
ceremony ladders are one shape at three scales: staged passage, human-held
terminal act, record of every step. The rules that repeat across strata
are the load-bearing ones: the proposer never approves its own proposal
(P4 gate, standing surveys, gate briefs, observer rule 4); the record is
appended and never rewritten (ledger I7-I9, register I1-I4, ceremony hash
chains); and every fence ships with its own armed test (figures fence,
non-vacuous checkers, regression seeds, the burn). Protocols that live in
only one register are the youngest: weaken-vs-widen, the RESERVED form,
and the D2 rule exist so far only as ledger rulings, one instance old,
each already citing its own precedent line. That is how the older ones
started too.

*a rule without a name is a mood; a name without an anchor is a wish.*
