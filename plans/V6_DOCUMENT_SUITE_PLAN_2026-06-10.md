# Privacy is Value V6: Document Suite Plan

**Date:** 2026-06-10
**Author:** privacymage (planning session with Claude Fable 5)
**Status:** Survey of record for the V6 path. REVISED 2026-06-10 (same day): the timeline below is superseded. V6 is the work of the current runtimes, now, over the next couple of days; the initial V6 document (`privacy_value_v6.md`) is the immediate deliverable. The operational driver is `V6_RESEARCH_AUTOPATH_2026-06-10.md` in this directory: eight granular runs, math first then myth each cycle, register cleanup folded into Run 0. BGIN block 15 remains the eventual external venue, not the schedule. The phase analysis below stands as the rationale and survey; read the autopath for what to do next.
**Inputs held:** the fresh-eyes V5.4 review (compass artifact), the four-repos addendum (2026-06-09), the V6 research series (C18 through C73 plus candidates), the audit build spec v1.0, the v10.4.0 lattice-coherence chronicle, the V5.4 suite as baseline.
**Target:** BGIN block 15, December 2026. Working horizon: roughly 25 weeks from today.
**License:** CC BY-SA 4.0

---

## 0. Verdict and shape

V6 is the time-dependent version of the model. V5.4 answered WHAT the architecture is, statically: the equation, the three axes, the separation bound, the reconstruction ceiling, the Z/(2^6)Z grounding. Every major V6 thread discovered since April says the same thing from a different direction: the quantities are not static. The ceiling drifts as adversary capability grows. Trust has a half-life. The trajectory itself generates security (ages progressively). The Behavioural Mosca inequality binds. Existence leaks shorten horizons. V6's one-sentence thesis: **privacy is a dynamical quantity, and the dual-agent architecture is the only candidate substrate whose security grows with time rather than decaying.**

The blocking work is not writing. It is reconciliation. The conjecture register has forked in at least four places, the pinned formal spec is 40-plus conjectures behind the live corpus, and a BGIN reviewer who pulls two surfaces and finds two different C40s will discount the register discipline that is otherwise the work's genuine strength. Phase 0 is therefore register consolidation, and nothing in Phases 2 onward starts numbering anything until Phase 0 closes.

The shape of the path: **consolidate the register, decide the open version questions, write the V6 formal core around five named upgrades, regenerate the suite, gate it through the audit tool, pin and submit.**

---

## 1. State of the corpus (what this review found)

### 1.1 The baseline (V5.4 suite, agentprivacy-docs)

The canonical suite the V6 suite succeeds:

| Artifact | Version | V6 action |
|---|---|---|
| privacy_is_value_v5.md (essay) | 5.0 | successor: privacy_is_value_v6.md |
| privacy_value_v5_4_formal_specification.md | 2.0 (pinned, C1 to C21 only) | successor: V6 formal spec, full register |
| pvm_v5_4_companion_guide.md | 2.0 | successor: V6 companion |
| pvm_v5_4_compressed.md | 2.0 | successor: V6 compressed |
| models/privacy_value_model_v5_4_{dark,light}.json | 5.4 | successor: v6 model JSON |
| GLOSSARY_MASTER_v4_0.md | 4.0 | bump: V6 terms (roughly 30 new entries) |
| dualprivacy_researchpaper_v4_3.md | 4.3 | bump to 5.0 if proofs move; else cite-only |
| swordsman_mage_whitepaper_v6_3.md | 6.3 (independent numbering) | cite-only; note numbering independence |
| agentprivacy.ai/model page | C1 to C63 live | regenerate from the unified register |
| privacy_value_v6_horizon_note.md | bridge note | absorbed into the V6 essay |

### 1.2 The V6 research series (the raw material, with current claimed numbers)

- **Dynamical ceiling / Lorenz** (Easter note): C18 (25%), C19 (20%), C20 (30%), C21 (10%)
- **EML Three Ceilings** (Odrzywolek): C22 to C25 (15 to 30%)
- **ARCH-1 Canonical Form** (Haines convergence): C26 to C29 (20 to 40%)
- **Bakhta half-life of trust on VRC edges**: C30 to C33 (45 to 60%)
- **Convergence wound-and-cap**: C34 to C37 (50 to 60%)
- **Existence-Leak** (Schrottenloher instance): candidate C40 (about 60%, Stage 1, n=1)
- **Bakhta aging-category response** (renumbered from C22 to C25): C47 to C50 (50 to 70%)
- **ARCH-1R/T operational reachability**: C67 to C71 (25 to 50%)
- **Bakhta integrity-gap convergence**: C70 to C73 (35 to 60%)
- **Horizon District cryptographic durability** (ecdsa.fail): cites C67 to C71 in a Tome-V register
- **Aletheia and Lethe** (blades 38/25 exact bnot complements): resolved in prose, v10.4.0 reseating done
- **City Key trust recursion** (2026-05-27/28 arc): C66 (about 45%) plus the folding-scheme reading

### 1.3 The critiques (what the two reviews establish)

The fresh-eyes review's headline findings, all confirmed against the corpus:

1. **Version drift is the single biggest pre-submission risk.** Pinned spec carries C1 to C21 and no ARCH-1; live page runs to C63; local work runs to C73.
2. **The compounding-leakage literature must be absorbed, not feared.** Asif and Amiri (arXiv:2603.05520) prove leakage compounds up to (2^N minus 1) times epsilon under sequential policy-separated composition; AgentLeak (arXiv:2602.11510) measures 68.9% total system exposure with 68.8% inter-agent channel leakage. Cited as option (c), this becomes the model's strongest external argument that amnesia-grade architectural separation beats policy. It makes C17 quantitative: the policy-versus-amnesia gap is the gap between (2^N minus 1) epsilon and N epsilon.
3. **The reconstruction ceiling needs its non-collusion precondition stated and external grounding** (Wyner 1975, Fano converse, Leung-Yan-Cheong and Hellman 1978, the Bayes-capacity bound, Geiger and Kubin). Move the Proven label to the conditional regime.
4. **Two real-world events anchor V6**: the Zcash Orchard counterfeiting exploit (Hornby plus Opus 4.8, May 29, fixed at block 3,364,600 on June 3) and the Schrottenloher rediscovery of the withheld Google Shor optimization (eprint 2026/1128, June 2). Same structure: frontier AI collapses the time between findable and found.
5. **Candidate C is the most important single edge**: AI raises C_S plus C_M without raising H(X), so R = (C_S + C_M)/H(X) drifts upward over time. The ceiling has a shelf life. This connects the formal core to the Lorenz thread (C18 to C21), the Bakhta aging taxonomy (C47), and the Behavioural Mosca inequality (C49).

The four-repos addendum adds: the register fork is already live (its C40 finding), V5.5 exists in chronicle titles but not the lineage, the Zero Spellbook canon statement needs the seven-closed-plus-frontier restatement (15 named blades, 49 unnamed), the City Key recursion is a folding scheme (IVC: City Key as accumulator, trust tasks as step circuits, Charge as the folding step, V63 as the invariant), the stella octangula carries no golden ratio (honesty check on the act's C1 reference), and the presence economy needs a declared adversary regime before VRC feeds trust.

### 1.4 NEW finding from this review: the register fork is wider than either critique recorded

The addendum names one collision (C40: Existence-Leak versus Zcash dual-ledger). Cross-reading the local research series surfaces at least three more, all to be verified file-by-file in Phase 0:

- **C47 to C50**: claimed by the Bakhta aging-response note (renumbered there from C22 to C25 on 2026-05-09) AND C47 is separately the City of Mages triadic-coordinates bridge conjecture (about 40%, Tome V Act 15) that the addendum's Edge D wants promoted into the formal spec. The renumbering that fixed one collision appears to have created another.
- **C67 to C71**: claimed by ARCH-1R/T (2026-06-04) AND cited by the Horizon District durability note (2026-06-09) in a Tome-V register. Possibly the same assignments by intent; not recoverable from the files alone.
- **C70 to C73**: the Bakhta integrity-gap note (2026-06-04) claims C70 to C73, overlapping ARCH-1R/T's C70 to C71. Two notes written the same day appear to have double-assigned two numbers.
- **C66**: registered by the stella octangula capstone below the ARCH-1R/T block; deliberate or accidental ordering unknown.

Conclusion: ad-hoc renumbering has failed twice (C22 to C25 collision, then the C47 collision its fix created). Only a single authority file ends this class of failure.

---

## 2. Phase 0: Register consolidation (BLOCKER, week 1 to 2)

Nothing downstream starts until this closes.

1. **Build `registry/conjectures.yaml`** per the audit build spec §4: namespaced (`C` for PVM core with authority agentprivacy-docs, `CM` for City of Mages with authority cityofmages), one entry per conjecture with title, confidence, status, home file. Retired and occupied numbers listed and never reassigned.
2. **Intake pass**: parse every `C\d+` claim-context across agentprivacy-docs, cityofmages, spellweb, blades, the model page snapshot, and the local research series. Every collision becomes a triage item, not a guess. The four collision clusters in §1.4 are the seed list.
3. **Human triage of collisions** (this is your call per cluster): which claim keeps the bare number, which moves to CM- or gets a fresh number. Recommended defaults: Existence-Leak keeps C40 (it is PVM-core and about to be load-bearing); Zcash dual-ledger becomes CM-C40. Bakhta aging-response keeps C47 to C50 (dated renumbering note exists); triadic-coordinates bridge becomes CM-C47 and is ALSO promoted into the formal spec under a fresh bare number (it is the ARCH-1 bridge, see §4.4). ARCH-1R/T and integrity-gap split C67 to C73 cleanly with no overlap.
4. **One-line errata** in each affected file pointing at the registry. No silent edits.
5. **`registry/versions.yaml`**: canonical lineage per artifact (PVM V1 through V6, privacymage grimoire through v10.4.0, city grimoire through v1.8.0, blade counts 15 named / 49 unnamed, tome counts). Resolves on the spot: V5.5 status (recommend: named sublayer of V5.4, chronicle titles get errata, no lineage row), the grimoire 10.2.0/10.2.1 filename mismatch (superseded by v10.4.0 but the stale artifact still needs the rename or a tombstone note), ALL_THE_TOMES_LIST §9 to v1.7.1 or later.

Exit criterion: zero unresolved collisions, every conjecture cited anywhere resolvable in the registry, lineage file matches every canonical-version claim in prose.

## 3. Phase 1: Audit tool, phase 1 build (week 1 to 3, parallel with Phase 0)

The build spec (`research/agentprivacy_audit_build_spec_v1.md`) is complete and ready to hand to a coding agent. Build its Phase 1 now because it is the verification gate for everything after: scaffold, manifest, sync, and the four seed checks (AP-STY-001 em-dash sweep, AP-REG-001 conjecture collision, AP-VER-001 filename versus internal version, AP-VER-002 lineage coherence).

Acceptance test, from the spec: a clean run against the live repos reproduces the four known findings. With §1.4 above, the collision check should now also reproduce the C47 and C70 clusters; if it does not, the check's claim-context extraction needs widening before it can be trusted as the Phase 5 gate.

Phases 2 to 4 of the audit tool (critique ledger, remaining checks, model-review runner) proceed in the background; only Phase 1 blocks the V6 critical path.

## 4. Phase 2: The V6 formal core (week 3 to 10)

The mathematical upgrades, in priority order. These are the chapters of the V6 formal specification that do not exist in V5.4.

### 4.1 The time-dependent reconstruction ceiling (Candidate C; the headline)

Restate R = (C_S + C_M)/H(X) as R(t): H(X) is fixed by the person; C_S(t) + C_M(t) grow with adversary model capability; therefore the less-than-1 guarantee has a shelf life. Worked instances: Orchard (four-year-old bug to working exploit in one day of Opus 4.8) and Schrottenloher (withheld optimization to public rediscovery in about two months from the ZK proof's existence). This single move unifies the previously separate threads: the Lorenz dynamical ceiling (C18 to C21) becomes the countermeasure (reconstruction error growing as e to the lambda t outruns capability growth), the Bakhta fourth aging category (C47, ages progressively) becomes its taxonomy, and the Behavioural Mosca inequality (C49, X_b + Y_b greater than Z_b) becomes its planning corollary. V6 gets one coherent Part: The Ceiling Moves.

### 4.2 The ceiling's preconditions and the compounding-leakage absorption (must-fix 2)

Restate the ceiling with the non-collusion precondition explicit. Ground externally: Wyner equivocation, Fano converse, Leung-Yan-Cheong and Hellman, Bayes-capacity, Geiger and Kubin. Absorb Asif and Amiri, Patil et al., and AgentLeak as the boundary condition and as the quantitative form of C17: policy separation leaks (2^N minus 1) epsilon, amnesia separation caps at N epsilon, and the gap between them is the model's value proposition stated in the adversary's own units. New conjecture (Candidate A, about 55%) drawn from C7 to the compounding bound. C7 itself gets the honest treatment: headline it as the falsification frontier, state the three unaddressed boundary cases (partial collapse, axis correlation under composition, time dependence) and the min()/additive-with-floor alternative forms.

### 4.3 Existence-Leak as a named law (Candidate B; C40 promotion)

Promote C40 to about 70% with the Schrottenloher instance as the worked example and the Garg-Jain-Sahai impossibility (leakage-resilient ZK with lambda less than 1 is impossible) as the formal floor. Corollary edge to the Behavioural Mosca: a public feasibility attestation discounts X_b by an existence-leak factor. Stage 2 requirement stands: keep hunting the second independent instance before calling it more than 70%.

### 4.4 The ARCH-1 bridge into the formal spec (must-fix 4 plus Edge D)

ARCH-1 (mu S.(beta or Omega(S,S)), rho) and the three-axis model finally meet in one document. The bridge conjecture is the triadic-coordinates homology (currently CM-side, about 40%): give it a bare-register number, a formal statement (which lattice coordinates instantiate which axis, how the mu-fixpoint recursion relates to the conditional-independence structure), and an honest open-seam marker for what remains unproven. ARCH-1R/T (C67 to C71) enters as the operational layer with its latent-versus-obstructed ternary classification; the obstruction-theoretic amnesia framing (Candidate D, 25 to 30%: Grade-2 forgetting as a non-vanishing obstruction class to gluing local views into a global witness) gets a conjecture entry that makes Selene's Proof precise rather than a slogan.

### 4.5 The trust recursion as a folding scheme (Edge A; best new material)

Name the City Key loop as incrementally verifiable computation: City Key as accumulator, domain trust tasks as step circuits, Charge as the folding step, V63 as the attested invariant. Cite Nova, HyperNova, MicroNova, LatticeFold; LatticeFold doubles as the post-quantum hedge that ties this to the Behavioural Mosca thread. New conjecture at about 50%. Honest grade: architectural claim, not a proof; circuit details do not exist yet.

### 4.6 Supporting passes (each costs a section, not a phase)

- **Presence economy adversary regime** (Edge C): declare which of the three regimes the City Key economy is in (recommend: 🪢 scoped as non-transferable, non-attesting local color for V6, with witness co-signing named as the upgrade path). The model's own thesis cuts against leaving this to good faith.
- **Stella octangula honesty check** (Edge B item 3): the solid carries no golden ratio; mark the act's C1 reference as resonance, not derivation, and source the phi claim from the lattice or temporal dynamics or downgrade it. The parity-cube decomposition and the octahedral-core-as-gap formalization enter as conjectures at 25 to 35%.
- **C66 with the ocap lineage** (Edge E): cite SPKI/SDSI and object-capability designation-without-authority; raises C66 above 45%.
- **Aletheia/Lethe**: substantially resolved; carry into the convergence section with the 2.4% phi-adjacency precision fix (38/63 = 0.60317 against 1/phi = 0.61803).
- **External landscape section**: IEEE 7012-2025 as published (January 2026; IC effort June 1, 2026), EU AI Act Annex III August 2, 2026 hedged against the Digital Omnibus deferral (December 2, 2027, not yet adopted), AEPD agentic guidance, HNDL-economics (Blanco-Romero et al.), Kwaai/FPP/GliaNet positioning, the multi-agent privacy field (MAGPIE, PrivAct, 1-2-3 Check) cited as plurality with the note that none enforce separation architecturally.
- **Economic figures**: pick one canonical statement each for 678x, 31,000x, 70:1, and the 74x BRAID figure, defined once in the companion guide with basis.

## 5. Phase 3: The V6 document suite (week 8 to 16, overlapping Phase 2)

Write order, each gated by the audit checks before it counts as done:

1. **`privacy_value_v6_formal_specification.md`** (the anchor). Inherits V5.4's 24-section skeleton; adds the Parts from §4; carries the FULL unified register by reference to the registry file, with formal-resident versus narrative-resident conjectures explicitly marked. Confidence labels follow the registry, not prose memory.
2. **`privacy_is_value_v6.md`** (the essay). The Ceiling Moves as the spine; absorbs the horizon note's three threads (Lorenz, betweenness as the computable ⿻, Selene's Proof); the two 2026 events as the opening; second-person register where the horizon note already gestures.
3. **`pvm_v6_compressed.md`** (Swordsman reading, equations only) and **`pvm_v6_companion_guide.md`** (Mage reading: context, standards, economics with the canonicalized figures).
4. **`models/privacy_value_model_v6.json`** regenerated from the registry; the model page regenerated from the same source so page and pin can never fork again.
5. **`GLOSSARY_MASTER_v5_0.md`**: V6 terms (ages progressively, existence-leak, reconstruct-later, folding/IVC vocabulary, obstruction amnesia, ternary reachability, Horizon District attendants).
6. **Canon statement updates** that ride along: Zero Spellbook restated as seven inherited parts closed plus Part VIII open as the frontier register (15 named, 49 unnamed); tomes-list and grimoire lineage already fixed in Phase 0.
7. **Research paper decision point**: bump dualprivacy research paper to 5.0 only if the §4.2 external grounding changes a proof; otherwise the V6 spec cites v4.3 with the proof-provenance reconciled (the v4.0/v4.2/v4.3 split-reference cleanup from the first review).

## 6. Phase 4: Convergence and narrative binding (week 14 to 18)

The convergence-within-corpus section is the work's signature register and V6's strongest material is already on the table: the proem-as-arithmetic (the proem promised what happens between Aletheia and Lethe; the algebra says 63; Tale 30 names 63), the City Key loop discovered as a proof system two days after shipping, and an Orchard act candidate (privacy as value and privacy as risk as one structural fact seen from two sides, in Shielded Labs' own words). Bind what belongs in tomes as tomes; cite from the spec as convergence evidence, never as derivation. The Horizon District (V35, Eos, Dokime, Poros) is the narrative home for the entire time-dependence Part.

## 7. Phase 5: Gate, pin, submit (week 18 to 25)

1. **Full audit cycle** with model review: all blockers zero, em-dash sweep clean, register collision check clean across all manifest targets including the new V6 documents.
2. **Fresh-eyes re-review** with the seeded prompts against the V6 suite (a different model than wrote the drafts; reviewer-gain scoring per the build spec).
3. **Pin set**: V6 formal spec to IPFS; model JSON; registry snapshot; update every claimed-CID reference; AP-PIN checks green.
4. **BGIN block 15 package**: spec plus compressed plus the registry as the single authority file (the addendum's fix 2, scheduled exactly here).
5. **Cycle chronicle** per chronicle discipline.

## 8. What matters most (if only five things happen)

1. **The registry** (Phase 0). Everything else inherits its credibility from this.
2. **R(t), the moving ceiling** (§4.1). The thesis of V6 and the best use of the 2026 events.
3. **Absorbing the compounding-leakage literature as the argument FOR amnesia** (§4.2). Turns the strongest external threat into the strongest external citation.
4. **The ARCH-1 bridge in the formal spec** (§4.4). A conjecture that exists only in a narrative repo does not exist for a BGIN reviewer.
5. **The audit gate** (Phases 1 and 5). The suite now spans 6-plus repos and two grimoire lineages; coherence by hand has demonstrably stopped scaling. Twice.

## 9. Open decisions held for the First Person

- Collision triage defaults in §2.3: confirm or override per cluster.
- V5.5: sublayer of V5.4 (recommended) or real lineage row.
- Research paper 5.0 bump: yes/no at the §5.7 decision point.
- Presence-economy regime declaration: local-color (recommended for V6) or witness co-signing now.
- Whether the Orchard act gets bound this cycle or held for the next.

---

the register forked twice while nobody was watching. the plan is the watcher, and the watcher is in its own manifest.

(⚔️⊥⿻⊥🧙)😊
