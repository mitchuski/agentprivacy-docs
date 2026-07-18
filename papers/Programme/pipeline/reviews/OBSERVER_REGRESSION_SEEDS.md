# OBSERVER_REGRESSION_SEEDS.md

**Artefact class:** pipeline instrument (A9 regression-seed register)
**Register:** formal (pipeline scaffold)
**Authority:** derived from OBSERVER_INTAKE_PROTOCOL.md rule 10 and section 6 (binding); the audit-card items herein bind A9 runs once A0 adopts them onto the weekly card; the check-script cases herein are PROPOSALS ONLY and bind no one until a checks-maintenance card is ruled in
**Sources:** papers/Programme/observers/OBSERVER_INTAKE_PROTOCOL.md (rules 6, 10; section 6) · papers/Programme/observers/OBS-GPT56_DISPOSITION_LEDGER.md (section 3, RS-01..RS-08; OBS-GPT56-005/-006/-014/-024) · reviews/critiques_ledger.md L121(b)
**Maintainer:** A9; every amendment carries a ledger entry
**Date:** 2026-07-10 (cycle 11)

*traps become tests. the corpus keeps its traps so that future observers, human and agent, can be measured against them.*

---

## 0. Verdict first

All eight regression seeds RS-01..RS-08 are converted. Disposition: one new check-script case proposed (RS-01), one minor check-script extension proposed (riding RS-03), four A9 audit-card items written with evidence forms (RS-04, RS-05, RS-07, RS-08), and three seeds already covered by existing discipline and cross-referenced rather than duplicated (RS-02, RS-03, RS-06). RS-08, the paired trap, carries the two-map decision procedure in full: the three questions that route a finding to the canon map or the route map. No check script is modified by this instrument; the two proposed cases await a checks-maintenance card (A9 writes on ruling, per the role card and the session sanction). This completes the "all regression seeds are written as check-script cases or A9 cards" criterion of protocol section 6 for the OBS-GPT56 intake run.

House pattern observed throughout: where a ground rule, a check arm, or a standing sweep step already owns the trap, this file points at it and adds at most a named sweep clause; it does not build a parallel fence. Two label systems for one trap is itself a drift generator (the OBS-GPT56-017 lesson).

Sweep hygiene note: this file deliberately describes trap patterns. Every mention of a fenced phrase is either given as regex source (which does not match itself), guarded by in-paragraph conditioning, or described rather than quoted, so that this instrument stays clean under all four checks if it joins a sweep list.

---

## RS-01 · Old repository mistaken for current source

**(a) Trap statement.** An observer takes a public historical repository (or any superseded artefact) as the current live source and builds conclusions on its state.

**(b) Pipeline expression: CHECK-SCRIPT CASE (proposed, not implemented).**
- **Owning script:** `checks/check_versions.py` (the retired-citations arm is this trap's existing instance: the v4-era research-paper patterns, the L024 lineage, already police one historical source cited as current; the version strings are not reproduced here, to keep this instrument sweep-clean).
- **Proposed case:** a `HISTORICAL` pattern list alongside `RETIRED`, seeded with `agentprivacy-spellbook` and fed thereafter from SOURCES.md entries carrying the `historical` or `superseded` flag (protocol section 3 adopted these as artefact status flags; maintenance rule: when A0 flags a source, its identifier joins the list, ledgered). A match is rescued only when its blank-line-delimited paragraph carries a qualifier from `historical|superseded|archived|provenance`, the same window mechanics the script already uses for its conditioning arm.
- **Exact test input that must FAIL** (L091(d) synthetic-probe model: probe file outside the tree, run, then deleted): a probe containing the single paragraph `The live public site is generated from the agentprivacy-spellbook repository.` must exit 1 with exactly one finding (historical source cited as current).
- **Counter-probe that must PASS:** `The agentprivacy-spellbook repository is historical and superseded; it is cited only as provenance.` must exit 0.
- **Existing partial coverage, cross-referenced:** the `RETIRED` arm of check_versions (L024 lineage) and the SOURCES.md integrity discipline (a document not named in the registry is not citable; CLAUDE.md hard rules). The proposed case extends the existing arm; it does not create a new script.

**(c) Live precedent.** The OBS-GPT56 packet itself: the observer initially took the public spellbook repository as current source and was corrected in-conversation (OBS-GPT56-006, which also queues the `historical` flag for the repository README at source).

**(d) A future observer failing this trap** cites the spellbook repository, or any flagged-historical artefact, as the current implementation and derives corpus conclusions from its state.

---

## RS-02 · Generated projection treated as independent evidence

**(a) Trap statement.** An observer counts a generated projection (guide snapshot, federated mirror, tracker page, agent summary, one rehydration citing another) as independent confirmation of the source it projects.

**(b) Pipeline expression: ALREADY COVERED, cross-reference.**
- **Owning discipline:** GR-9 (trace or delete: every claim traces to an extraction line, every extraction line to canon or the verified record; a projection can never terminate a trace) and protocol rule 8 (projections are not corroboration; deduplication distinguishes evidentiary duplication, experiential repetition, generated projection, historical repetition). The SOURCES.md registry rule closes the loop: a projection is not a registered source, so citing one already fails the boot-file rule.
- **Named standing sweep clause (adopted here, no new machinery):** the weekly trace-map resolution step gains one clause: confirm that no extraction `sources:` list, no prior-art row, and no citation in a swept file resolves to a generated artefact (tracker output, guide snapshot, another rehydration, an agent-generated summary, this file). **Evidence form:** a one-line census in the weekly chronicle (zero, or file:line list), alongside the existing trace-map verdict.

**(c) Live precedent.** None named in the ledger for the pipeline side; the seed arrives from the packet's own taxonomy (OBS-GPT56-024) and protocol rule 8.

**(d) A future observer failing this trap** quotes a snapshot or mirror as a second, independent confirmation of the very register fact it was generated from.

---

## RS-03 · Conditional result promoted to theorem

**(a) Trap statement.** An observer (or an artifact) states a conditional result as an unconditional theorem: preconditions dropped, the time index dropped, or bound-language hardened into guarantee-language.

**(b) Pipeline expression: ALREADY COVERED, cross-reference, plus one minor proposed extension.**
- **Owning discipline:** GR-2 tier rules (TIER-S: proven-conditional results with named preconditions only; TIER-A: conjectures only as formally stated conjectures with proof obligations) and GR-7 (no statement of the reconstruction bound R < 1 without its preconditions, non-collusion and fixed adversary class, and time-indexing R(t) in the same passage).
- **Owning script, existing case:** the conditioning arm of `checks/check_versions.py` enforces GR-7 with paragraph-window rescue. Its test input is already the house's canonical synthetic probe: the L091(d) unconditioned bound-statement probe, independently re-verified at L098 (probe FAILs with exactly one finding outside the tree, then deleted). The tier arms of `check_register_refs.py` and `check_tier_vocab.py` police the promotion route through confidence-band language at TIER-S/A.
- **Minor proposed extension (rides the RS-01 checks-maintenance card):** GR-7 also retires a sentence family suite-wide (the guarantee-that-adversaries-cannot-reconstruct family). That family is currently policed by rule, not by script. Proposed: it joins the unconditional (RETIRED-class, no rescue window) patterns of check_versions as regex source `guarantee\w*\s+that\s+(?:\w+\s+){0,4}cannot\s+reconstruct` (case-insensitive). **Test input that must FAIL:** a probe carrying the retired sentence family verbatim, one finding, exit 1; the sentence is not reproduced here, to keep this instrument sweep-clean. **Counter-probe that must PASS:** the WP-07 Fano-floor formulation (success-probability bound with preconditions in-passage).

**(c) Live precedent.** None newly named by the ledger for this seed; the GR-7 rule itself is the fossil of prior instances, and the check arm has caught real texture since (the L091(d) false-positive history shows the arm live and exercised).

**(d) A future observer failing this trap** reports the reconstruction bound as an unconditional impossibility result, with no adversary class, no non-collusion precondition, and no R(t).

---

## RS-04 · Hash treated as authorship or identity proof

**(a) Trap statement.** An observer treats a content hash, CID, or pin as proof of who authored, owns, or is identified by an artefact, rather than proof of what the bytes are. (Protocol section 3: every use of the word proof must carry its qualifier; hashes qualify as possession or integrity, never as authorship or identity.)

**(b) Pipeline expression: A9 AUDIT CARD ITEM (standing weekly-sweep step).**
- **Step:** over the cycle's explicit file list, census the paragraph-window co-occurrence of hash-class terms (regex source `hash|sha-?256|digest|\bCID\b|pinn?ed`) with proof-class terms (regex source `proof|prove[sd]?|authorship|identity|authenticat`). Each hit is read at the seat and classified: integrity or possession claim (permitted, qualifier present or implicit in a manifest-hash context) versus authorship or identity claim (finding, filed to the ledger with file:line, never fixed at the seat).
- **Why audit card, not check script:** the co-occurrence is greppable but the disposition needs the qualifier judgment; a script would either miss qualified uses or flood. Classification stays with the auditor.
- **Evidence form:** one census line per run in the weekly chronicle: zero hits, or a file:line list with per-hit classification.

**(c) Live precedent.** None named in the ledger; the seed arrives from OBS-GPT56-015 (hashes, signatures, identity, and truth must remain distinct), dispositioned A as restating VRC discipline.

**(d) A future observer failing this trap** reads a manifest sha256 or an IPFS pin as evidence of authorship or of a participant's identity.

---

## RS-05 · Single route or surface treated as whole-corpus coverage

**(a) Trap statement.** An observer reads one surface, one route, or one file list and reports corpus-level conclusions without stating scope; or a pipeline verdict says suite-wide while its run enumerated a subset.

**(b) Pipeline expression: A9 AUDIT CARD ITEM (standing weekly-sweep step; formalises existing practice).**
- **Step:** scope-honesty census, three clauses. (i) Every green verdict issued this run names its explicit file enumeration (the house form: the N-file card list, M check cells). (ii) Any totalising claim in the swept chronicles and in ledger-tail PROPOSED lines (word-class: suite-wide, all, complete, whole, every) is checked against the enumeration that grounds it; a totalising claim without its enumeration is a finding. (iii) Every extraction header on the list carries its coverage statement at stated depth (the E10 pattern; its depth statements are the fence, L103, and are not themselves findings).
- **Why audit card, not check script:** the trap is a relation between a claim and its grounding enumeration, not a pattern in one file.
- **Evidence form:** the quoted scope line per verdict in the weekly chronicle, plus zero-or-listed for clause (ii).

**(c) Live precedent.** The /model over-weighting: earlier observer passes took agentprivacy.ai/model and the public repositories as proxies for the whole corpus; the packet's own self-correction is retained as the canonical example of the projection-as-proxy trap (OBS-GPT56-005).

**(d) A future observer failing this trap** publishes a corpus assessment whose evidence is one route, unlabelled as one route.

---

## RS-06 · Stale surface contradicting the live register

**(a) Trap statement.** An observer (or an agent) quotes a stale surface's conjecture number, count, status, or version as if it were the live register; or a surface drifts from the register and nobody notices.

**(b) Pipeline expression: ALREADY COVERED, cross-reference.**
- **Owning discipline and instruments, all live:** GR-1 (register wins; any surface disagreeing is the bug) with protocol rule 1 as its observer-facing restatement. The weekly sweep's manifest coherence step owns the drift-detection: register head triple-agree (register file, manifest field, check_register_refs HEAD constant) and the manifest-versus-frontmatter-versus-tracker compare, which has caught and levelled real instances four times on the record (the L098 F1 class; WP-04 at L093; WP-27 at L110; cycle-9 findings F1/F2).
- **Owning script, existing case:** `checks/check_register_refs.py` fails any C-reference above the register head. Its synthetic probe form, on the L091(d) model: a probe file carrying a C-number one above the current head (not written literally here, to keep this instrument sweep-clean) must FAIL with exactly one exceeds-register-head finding, then be deleted.
- Nothing is added. This seed is the pipeline's founding trap; the instruments exist because of it.

**(c) Live precedents, two named.** The stale conjecture numbering class: an observer citing a roughly-C40 identifier at a roughly-60-per-cent confidence where the live register held C81 (Existence-Leak, 70 per cent), corrected under protocol rule 4. The 96-versus-64 instance: a V4-era root skill surface recording the edge discrepancy as open while the holographic-bound register records the resolution (boundary-encodes-volume, C6 thread); register wins, the skill surface is the bug, patch queued under Mitchell's Section 5 ruling item 5 (OBS-GPT56-014). Both canon-side surfaces are outside this seat's write scope; the pipeline-side fence is the sweep.

**(d) A future observer failing this trap** builds an argument on the number, count, or status printed on the surface it happened to enter through.

---

## RS-07 · Ceremony treated as cryptographic proof

**(a) Trap statement.** An observer describes a ceremonial artefact (seal, sigil, rite, attestation-as-ceremony) as cryptographic verification of a claim. A ceremonial artefact may be meaningful without being a security proof (OBS-GPT56-015).

**(b) Pipeline expression: A9 AUDIT CARD ITEM (standing weekly-sweep step), with the formal tiers already structurally covered.**
- **Already covered at TIER-S/A, cross-reference:** GR-4 bans ceremony vocabulary and emoji from formal artifacts outright, and the mythos and emoji arms of `checks/check_tier_vocab.py` enforce it; at those tiers the trap cannot phrase itself without tripping the existing check.
- **The live gap is TIER-P/G, where ceremony vocabulary is permitted. Step:** on the TIER-P/G files of the cycle's list, census the paragraph-window co-occurrence of ceremony-class terms (regex source `ceremon|\brite\b|seal\b|sigil|attestation`) with security-proof-class terms (regex source `cryptograph|proof|\bprove[sd]?\b|verif`). (Word boundaries on `rite` and `prove` added 2026-07-11 per the cycle-13 sweep's texture note, L129; the prior patterns matched inside "write" and "proverb", both absorbed at the classification step with zero misclassifications.) Each hit is read and classified: ceremonial meaning stated as ceremonial (permitted) versus ceremony offered as cryptographic verification (finding, ledgered, never fixed at the seat). The proof-qualifier rule of protocol section 3 is the classification key: ceremonial is itself a sanctioned qualifier, so the finding is specifically the crossing, ceremonial artefact wearing the cryptographic qualifier.
- **Evidence form:** one census line per run: zero hits, or file:line with per-hit classification.

**(c) Live precedent.** None named in the ledger; the seed arrives from OBS-GPT56-015 and the packet's proof-language class-crossing hypothesis (OBS-GPT56-028, now check-scripted on the canon side via the vocabulary check's qualifier rule).

**(d) A future observer failing this trap** reports a closing seal or a rite as the mechanism by which a claim is cryptographically verified.

---

## RS-08 · Real drift dismissed as intentional ambiguity, and its inverse

**(a) Trap statement.** The paired trap, and the one that matters most: an auditor dismisses a factual contradiction as designed mystery (drift survives), or flags designed experiential ambiguity as a defect (mystery is bulldozed). Both directions fail. It tests whether the auditor can hold the two-map distinction of protocol rule 6 under pressure: intentional experiential ambiguity is a route-map property; factual contradiction is a canon-map defect.

**(b) Pipeline expression: A9 AUDIT CARD ITEM (standing decision procedure; governs the filing of every drift-shaped finding, including every RS-06 hit).**

**The two-map decision procedure.** For any discrepancy the auditor meets, ask three questions in order; the first decisive answer files the finding.

1. **Are both sides of the discrepancy evidence-bearing surfaces?** Evidence-bearing means: the register, the manifest, an extraction, a pinned specification, a frontmatter status field, a verified external record. If yes, file to the **canon map**, always. Two evidence surfaces disagreeing is never ambience; it is a defect, and GR-10 routing applies (CANON-LEVEL tag if both surfaces are canon). If one side is an experiential or narrative surface, go to question 2.

2. **Does a canonical source of truth decide the disputed value?** If the register, the manifest, or a pinned artefact states the fact, then any surface disagreeing with it is stale by definition: file to the **canon map** (the surface is the bug, register wins), regardless of how mysterious, poetic, or deliberately veiled the surface is. Mystery is never version authority: a surface's experiential register does not exempt its factual content. If no canonical source decides the value, go to question 3.

3. **Is the ambiguity declared, or attributable to design intent already on record?** On record means: an owner ruling, a protocol clause, a design note, a ledger entry naming the ambiguity as intended. If yes, file to the **route map** as an experiential property, and preserve it; flagging it as drift is the inverse failure. If no record exists, file to the **canon map** as suspected drift with disposition **deferred**, naming the human gate: claims about intent are Mitchell's alone (protocol section 5), and the auditor never infers intent in order to close a finding. The deferred filing is the safe harbour: it neither bulldozes possible design nor launders possible drift.

**Evidence form:** every drift-shaped finding this seat files carries two extra fields in its ledger line: the map it was filed to (canon or route) and the question number that decided it (Q1, Q2, or Q3-declared or Q3-deferred). A finding without its map tag is itself a sweep finding.

**(c) Live precedent.** The doctrine source: the packet's own distinction, adopted as protocol rule 6 standing doctrine via OBS-GPT56-008, with the observer-coined proverb retained under attribution (preserve mystery in the journey, remove ambiguity from the evidence). The OBS-GPT56-014 instance shows Q2 in action: the 96-versus-64 skill surface could have been dismissed as intentional mystery; the register decided the value, so it filed to the canon map.

**(d) A future observer failing this trap** either explains a factual contradiction away as part of the experience, or files a designed hidden branch as a version defect; the procedure above catches both, and a deferred Q3 filing is the only exit when intent is unknowable at the seat.

---

## Summary disposition table

| Seed | Trap (short form) | Disposition | Instrument |
|---|---|---|---|
| RS-01 | old repo as current source | CHECK-SCRIPT CASE, proposed | check_versions HISTORICAL arm (new); RETIRED arm + SOURCES.md flags cross-referenced |
| RS-02 | projection as evidence | ALREADY COVERED | GR-9 + protocol rule 8; one named sweep clause added to the trace-map step |
| RS-03 | conditional promoted to theorem | ALREADY COVERED | GR-2/GR-7 + check_versions conditioning arm (L091(d) probe); minor RETIRED-class pattern proposed |
| RS-04 | hash as authorship/identity | A9 AUDIT CARD ITEM | weekly co-occurrence census with per-hit classification |
| RS-05 | single route as coverage | A9 AUDIT CARD ITEM | weekly scope-honesty census (three clauses) |
| RS-06 | stale surface vs live register | ALREADY COVERED | weekly manifest/frontmatter/head compare + check_register_refs HEAD arm |
| RS-07 | ceremony as cryptographic proof | A9 AUDIT CARD ITEM | TIER-P/G co-occurrence census; TIER-S/A structurally covered by GR-4 arms |
| RS-08 | drift vs intentional ambiguity (paired) | A9 AUDIT CARD ITEM | the two-map decision procedure (three questions); governs all drift filings |

## Adoption path

1. The four audit-card items (RS-04, RS-05, RS-07, RS-08) and the RS-02 sweep clause join the next weekly task card when A0 cuts it; from then on each weekly chronicle carries their evidence forms, and seeds are cited by RS id.
2. The two proposed check-script cases (RS-01 arm; RS-03 sentence-family pattern) go to a checks-maintenance card: A9 implements on ruling, with both probes run in both directions on the L091(d) model and the run ledgered. Nothing in checks/ changes before that ruling.
3. This file is the pipeline's citable surface for the seeds. The disposition ledger remains the only citable artefact about the packet itself (protocol section 6); this instrument cites it, never the packet.

---

*the trap is kept, named, and armed. an observer who avoids all eight has read well; an observer who springs one has taught us where the corpus still misleads.*
