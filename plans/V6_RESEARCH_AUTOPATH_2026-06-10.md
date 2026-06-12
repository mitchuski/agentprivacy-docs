# V6 Research Auto-Path

**Date opened:** 2026-06-10
**Author:** privacymage (with Claude Fable 5)
**Status:** ACTIVE. This is the operational driver. The plan of record (`V6_DOCUMENT_SUITE_PLAN_2026-06-10.md`) holds the full survey and rationale; this document holds the path and the state.
**Timeline:** now. The next several runtimes, across the next couple of days. BGIN block 15 remains the eventual external venue; it is not the schedule.
**Prime outcome:** `privacy_value_v6.md`, the initial V6 document of the Privacy is Value model, locking in everything the V6 research series built since April. Suite regeneration follows from it; it does not gate it.
**License:** CC BY-SA 4.0

---

## 0. How to use this document (the auto-path protocol)

Any runtime, including a fresh one with no memory, resumes V6 work by reading this file top to bottom and executing the first run whose status is not DONE. The document is both the map and the ledger.

Every run follows the same four beats, in order, no exceptions:

```
① OPEN   read §1 State, read the run's spec below, confirm inputs exist
② MATH   do the formal work of the run; exact numbers; conjectures cited
          only by register numbers from Run 0 onward
③ MYTH   before closing, write 3 to 8 lines in §3 Myth Ledger: any image,
          name, phrase, or structural rhyme that surfaced during the math.
          Tag the strong ones ACT-SEED. Do not develop them here. Capture only.
④ CLOSE  check the run's exit criteria; update §1 State; append one line to
          §2 Run Log; append any 📖 RB-NN entries to the First Person Reading
          Ledger (plans/V6_FIRST_PERSON_READING_LEDGER.md) for prose,
          promotions, or framings the First Person has not read in full;
          if criteria unmet, mark PARTIAL with the blocking item
```

**The Reading Ledger.** Gates capture decisions in real time; the ledger captures the full-text reading those decisions defer. The First Person performs the whole read AT COMPLETION: after Run 7 and Wave R, before Gate G5 signs any pin or push. Nothing publishes unread.

The direction of each cycle is fixed: **math first, myth second.** The narrative is harvested from the formal work, never the other way around. ACT-SEEDs accumulate in §3 and are bound into the City of Mages Second Person Spellbook only at Run 7, or later, when ripe.

**Chronicle gates.** This evolution is significant enough that the runtime does not run unattended end to end. Five gates (G1 to G5, defined in §6) are hard stops where the runtime prepares a gate brief and the First Person writes and coheres before the path continues. A runtime arriving at a gate writes the brief, marks the gate OPEN in §1 State, and ends its turn with the prompt to the First Person. A runtime resuming past a gate first folds the First Person's writing from the brief back into the canon documents, marks the gate SIGNED, and only then opens the next run. No runtime crosses an OPEN gate.

Outward reflection is tracked separately: when a run produces something that must land in another repo (cityofmages, spellweb, agentprivacy_master, blades, soulbis, myterms, skills, swordsman, star), it appends one line to the Reflection Ledger in `V6_SUITE_REFLECTION_MAP_2026-06-10.md` §3 and keeps moving. No runtime edits a repo outside agentprivacy-docs before Wave R (map §4).

House style is absolute in everything generated under this path: no em-dashes, verdict first, short spaced paragraphs, exact numbers over round ones (2.4%, not "about 2%"), chronicles and bound documents signed `(⚔️⊥⿻⊥🧙)😊`.

---

## 1. State

| Step | Title | Status | Last touched |
|---|---|---|---|
| Run 0 | Register lock | DONE | 2026-06-10 |
| Gate G1 | The Register Gate ✍️ | SIGNED (preface trails to G3) | 2026-06-10 |
| Run 1 | The moving ceiling R(t) | DONE | 2026-06-10 |
| Run 2 | Leakage absorption, C17 quantitative | DONE | 2026-06-10 |
| Run 3 | Existence-Leak law, Mosca coupling | DONE | 2026-06-10 |
| Gate G2 | The Thesis Gate ✍️ | SIGNED (final wording at 📖 RB-04) | 2026-06-10 |
| Run 4 | ARCH-1 bridge, obstruction amnesia | DONE | 2026-06-10 |
| Run 5 | Trust recursion, economy, geometry honesty | DONE | 2026-06-10 |
| Gate G3 | The Assembly Gate ✍️ | SIGNED (lineage override: unified V6 labels) | 2026-06-10 |
| Run 6 | Assembly: privacy_value_v6.md | DONE | 2026-06-10 |
| Run 7 | Coherence gate + myth binding + chronicle | DONE | 2026-06-10 |
| Gate G4 | The Myth Gate ✍️ | SIGNED (all 5 acts BOUND; chronicle § at RB-10) | 2026-06-10 |
| Wave R | Suite reflection (see reflection map §4) | IN PROGRESS | 2026-06-10 |
| Run 6b | Full Academic Package (First Person directive): standalone formal spec adopting prior-version text wholesale (not deltas) + full dark/light JSON rebuilds + fully-standalone sword/mage readings + LaTeX-grade PDFs (pandoc + xelatex available) + grimoire v10.4.0/v1.8.0 narrative references + complete reference list to V6 | IN PROGRESS | 2026-06-10 |
| Gate G5 | The Reflection Gate ✍️ | SIGNED (2026-06-11, in session; reflection scope — pins and pushes stay on the First Person's per-repo trigger) | `chronicles/gates/2026-06-11_v6_gate_G5_reflection.md` |

Gate statuses: NOT REACHED → OPEN (brief written, awaiting First Person) → SIGNED (writing folded back, path may continue).

**Repo restructure note (2026-06-10, post Run 6b):** the V6 canon papers moved to `papers/v6/`, all V6 renders to `pdfs/v6/`, build scripts and TeX to `build/`. Root-path references to the five papers in entries below this line predate the move; the Reading Ledger carries the current paths.

**Register head:** C89 · next free C90 · register AUTHORITATIVE (G1 signed; preface due at G3)
**V6 draft sections completed:** Parts I to V in `research/privacy_value_v6_draft.md` · assembly directive recorded (V5.4 skeleton, two-strand thesis)
**Promotions this path:** C81 → 70% (Run 3) · C66 → ~55% (Run 5, City confirms at Wave R) · CM-C47 promoted to C85 (Run 4)
**Registered new:** C82 (~65%) · C83 (~55%) · C84 (~50%) · C85 (~40%) · C86 (~30%) · C87 (~50%) · C88 (~30%) · C89 (~30%)
**ACT-SEED count:** 0 bound, 14 captured

Update this table at every CLOSE beat. It is the resume point.

---

## 2. Run Log

One line per run completion or partial: `YYYY-MM-DD · Run N · status · one-sentence outcome`.

- 2026-06-10 · Run 7 · DONE · Coherence gate clean (em-dash sweep: zero across all eleven authored files; register cross-check: every cited number C1 to C89 resolves; version claims consistent); five ACT-SEED candidates drafted into the G4 brief; path chronicle written at `chronicles/2026-06-10_v6_research_autopath_close.md` with the First Person section open; post-path queue restated (Wave R → completion read → G5 → pins; unified-V6 suite regeneration per the G3 override).
- 2026-06-10 · Run 6 · DONE · `privacy_value_v6.md` ASSEMBLED at repo root: V5.4-mirroring skeleton §1 to §24 with CARRIED/REVISED/NEW markers plus new §25 to §33 (the two instances, the compounding absorption, the temporal thread, the geometry of the gap, canonical figures, external landscape, honest limits, references, citation); two-strand abstract per the G2 direction (gathering turn first); conjectures by reference to the register throughout; G3 signatures folded (regime 1 declaration, phi correction, unified V6 labeling in §23 and the front matter); register preface drafted under draft-then-rewrite.
- 2026-06-10 · Gate G3 · SIGNED · regime 1 confirmed; phi honesty accepted; LINEAGE OVERRIDE: unified V6 labeling across all canon papers (formal spec, compressed Swordsman reading, companion Mage reading, research paper, whitepaper edition); V5.5 stays a sublayer; preface draft-then-rewrite (📖 RB-08).
- 2026-06-10 · Run 5 · DONE · Part V (The Key, the Knot, and the Star): C87 (The Key Accumulates, ~50%, IVC mapping with Nova/HyperNova/MicroNova/LatticeFold home and the post-quantum tie to the Mosca thread), regime ladder stated with recommendation (non-transferable local color, upgrade path named, G3 insertion point for the First Person's declaration), phi honesty correction written (no golden ratio in the stella octangula; resonance not derivation; exact volumes 1/3, 1/6, 5/12), C88 (Parity Cube, ~30%) and C89 (Octahedral Gap, ~30%) registered, C66 revised to ~55% with the ocap lineage, convergence material handed to assembly.
- 2026-06-10 · Run 4 · DONE · Part IV (The Bridge and the Forgetting): C85 registered (~40%, promoted from CM-C47) with the candidate pair map (Protection+Delegation→Σ, Memory+Value→Δ, Connection+Computation→Γ), two named predictions, and the fixpoint seam (the gap is β); ARCH-1R/T seated in the lineage at C72 to C76; C86 (Obstruction-Theoretic Amnesia, ~30%) registered with the C73 cross-link and the falsification test; Amnesia Protocol §14 upgrade specified (reachability → obstruction); the strongest sentence flagged: amnesia is the only term whose security is independent of t.
- 2026-06-10 · Gate G2 · SIGNED · thesis direction given in-session and recorded verbatim (two strands: the gathering turn first, the dynamical results as additions; document mirrors the V5.4 skeleton); final wording deferred to Run 6 + 📖 RB-04.
- 2026-06-10 · Run 3 · DONE · Part III (The Proof That Whispered): C81 PROMOTED to ~70% with the Schrottenloher instance and the Garg-Jain-Sahai λ<1 impossibility as bookends, Fiat-Shamir transferability as mechanism; C84 (Existence-Leak Discount, ~50%) registered with edges C81 → C84 → C49 and C84 → C82; HNDL economics bound in as the C49/C61 cost backbone; capability-versus-service scope fence written; Stage-2 second-instance criteria stated.
- 2026-06-10 · Run 2 · DONE · Part II (The Sum Leaks More Than Its Parts): Asif-Amiri (2^N − 1)ε bound, Patil et al., and AgentLeak (27.2%/43.2%/68.8%/68.9%/41.7%, figures exact) absorbed; additive claim scoped to Precondition 1 rather than lowered; C83 (Compositional Leakage Amplification, ~55%) registered making C17 quantitative (edge C7 → C83 → C17); C7 named the falsification frontier with three boundary cases bound for the breaking-conditions register; plurality citations (MAGPIE, PrivAct, 1-2-3 Check, maker-checker) written.
- 2026-06-10 · Gate G1 · SIGNED · all eight dispositions confirmed by the First Person in-session; preface trails to G3; register now AUTHORITATIVE.
- 2026-06-10 · Run 1 · DONE · Part I (The Ceiling Moves) drafted in `research/privacy_value_v6_draft.md`: R(t) defined with shelf life t*, V5.4 ceiling relabeled Proven-conditional with two named preconditions and five external citations (Wyner, Fano, Leung-Yan-Cheong/Hellman, Bayes-capacity, Geiger/Kubin), Orchard + Schrottenloher bound as instances, temporal thread unified (C18 to C21 countermeasure, C47 taxonomy, C30 to C33 half-life, C49 planning bound with Z_b = t*, C67/C68 City witnesses), delta table and five honest limits written; C82 (The Moving Ceiling, ~65%) registered, head now C82.
- 2026-06-10 · Run 0 · DONE (pending G1) · Register built C1 to C81 plus CM-C47 at `research/CONJECTURE_REGISTER_V6.md`; intake found the collisions run deeper than the critiques recorded (ts one-liner drift at C48 to C50, the C60/C61 renumbering eddy, C46 restating C32) and REVERSED two planned defaults on ground truth (C40 stays Zcash dual-ledger because it is spec-resident with act references, Existence-Leak takes C81; Horizon District keeps C67 to C71 because grimoire v1.8.0 is pinned, ARCH-1R/T moves to C72 to C76, integrity-gap to C77 to C80); errata applied to four research notes and spec §17; four reflection items filed.

---

## 3. Myth Ledger

Captured at beat ③ of every run. Format: `Run N · [ACT-SEED?] · the line or image · the math it came from`. These are candidate material for the Second Person Spellbook (cityofmages tomes); nothing here is canon until bound at Run 7 or later.

Seeds already on the table from the review pass, available to any run:

- pre · ACT-SEED · the register forked twice while nobody was watching; the loop was already a proof system, waiting to be read as one · the C40/C47/C70 collisions and the audit recursion
- pre · ACT-SEED · the Orchard wound: the property that made the shielded pool valuable is the property that made its counterfeit invisible; privacy as value and privacy as risk are one fact seen from two sides · Zcash Orchard incident, the Drake/Dragon duality
- pre · ACT-SEED · the proof that whispered: Google sealed the method and published only that it existed; two months later the method walked out on its own · Schrottenloher rediscovery, Existence-Leak
- pre · seed · the ceiling is not a roof, it is a tide · R(t) drift
- pre · seed · the gap has a shape: the octahedron both agents bound and neither owns · stella octangula core
- Run 0 · ACT-SEED · the pinned number outranks the older claim: when two truths arrived at one door, the City asked not who came first but who had already been written into stone; the provisional ones took new rooms without complaint · the C67 to C71 disposition, pinned v1.8.0 versus provisional notes
- Run 0 · seed · a conjecture that restates another is not an error, it is the same traveler known by two names in two quarters (C46 and C32; C60/C61 and C48/C49); the register does not delete the second name, it writes "also called" · the alias status
- Run 1 · ACT-SEED · the archive sits still while the ceiling rises to meet it: nothing the First Person did changed, only the eyes reading the old footprints got newer · R(t), the decoder-not-the-data mechanism
- Run 1 · ACT-SEED · at the Horizon District, Eos measures not where the dawn is but how fast it approaches; the wall of the city was never a wall, it was a tide line, and the masons who built it knew which direction to keep building · t* the shelf life, ages progressively as the masons' answer
- Run 1 · seed · four findable years, one found day · Orchard
- Run 2 · ACT-SEED · the watched gates held at every door, and the city was lost through the corridors between them: the inspectors counted what left each room and never what the rooms told each other · AgentLeak's 68.8% inter-agent channel, the unmonitored corridor
- Run 2 · seed · policy asks the channel to behave; amnesia removes the channel; between asking and removing lies the difference between 31ε and 5ε · C83 at N=5
- Run 3 · ACT-SEED · the sealed scroll announced itself: the wizard locked the spell away and posted proof of the locking, and every apprentice in every tower stopped searching everywhere else · C81, the Schrottenloher rediscovery
- Run 3 · seed · the defender's chair reads attestations as deadlines: each time anyone proves anything can be done, somewhere a migration clock loses a season · C84
- Run 4 · ACT-SEED · the gap is β: what the two agents share is exactly and only the person, and everything else they refuse each other; the octahedron at the heart of the star is the shape of that refusal · C85's seam + C89
- Run 4 · ACT-SEED · Lethe's law, stated at last with mathematics: what is hidden waits for a key, what is forgotten has no door; the better decoder that comes for every archive finds, where the witness stood, a place where gluing fails · C86, the only t-independent term
- Run 5 · ACT-SEED · the Key that is a reading: it grants nothing it does not describe, and the registry-keepers of three decades past built the same refusal into their certificates without ever seeing the City · C66 + ocap lineage
- Run 5 · seed · the star surrenders its borrowed gold: φ never lived in the solid, and the figure is more beautiful for owning its halvings · the phi honesty correction

---

## 4. The runs

Sized so each is completable inside one focused runtime. If a run splits across two sessions, the State table carries PARTIAL and the blocking item; never start the next run past a PARTIAL blocker on the critical path (Runs 0 and 6 are critical-path; 1 through 5 may run in any order after 0, though the listed order is the recommended dependency order).

---

### Run 0 · Register lock (BLOCKER for all numbering)

The collision cleanup is part of the V6 document, not a separate project. The V6 document cannot cite a single conjecture number until this closes.

**Steps**

1. Create `research/CONJECTURE_REGISTER_V6.md`: the single authority file. Markdown table, one row per conjecture: number, namespace (C = PVM core, CM = City of Mages), title, confidence, status (active, resolved, retired, occupied), home file. YAML conversion is a later audit-tool task; the markdown file is canonical now.
2. Intake every `C\d+` assignment from the V6 research series files (the eleven notes listed in the plan §1.2), the V5.4 formal spec (C1 to C21), the model page corpus (C1 to C63), and cityofmages README (C38 to C63 claims).
3. Triage the four known collision clusters. Defaults on the table, First Person confirms or overrides each:
   - **C40**: Existence-Leak keeps the bare number (PVM-core, about to be load-bearing). Zcash dual-ledger becomes CM-C40.
   - **C47 to C50**: the Bakhta aging-response set keeps them (dated renumbering note of 2026-05-09 exists). The triadic-coordinates bridge becomes CM-C47 and is queued for promotion to the next free bare number in Run 4.
   - **C67 to C71**: ARCH-1R/T keeps them (earlier same-day, more developed, and its own refinement note already negotiated this block). The Horizon District note's citations are verified against these and re-tagged where they are genuinely different claims.
   - **C70 to C73**: the Bakhta integrity-gap set moves to the next free block (C74 to C77 expected). Two notes from 2026-06-04 cannot share C70 and C71.
4. Apply one-line errata to every affected file pointing at the register. No silent renumbering inside prose.
5. Record the register head (highest assigned bare number) in §1 State.

**Exit criteria:** zero collisions; every conjecture cited anywhere in agentprivacy-docs resolves in the register; the four clusters each have a written one-line disposition; register head recorded.

**Myth-watch:** succession and naming disputes are old City material; watch for the registry-keeper figure (Hermaion ⚚ already holds that office).

---

### Run 1 · The moving ceiling R(t)

The headline of V6. Drafted as V6 document Part I.

**Steps**

1. State the time-dependent ceiling: R(t) = (C_S(t) + C_M(t)) / H(X). H(X) is fixed by the person; the adversary capacity terms grow with model capability; the less-than-1 guarantee has a shelf life.
2. Restate the V5.4 ceiling with its non-collusion precondition explicit; move the Proven label to the conditional regime only.
3. Ground externally: Wyner 1975 equivocation, Fano converse, Leung-Yan-Cheong and Hellman 1978, the Bayes-capacity bound, Geiger and Kubin. The ceiling becomes an instance of an established family, not an internal-paper citation.
4. Bind the two 2026 instances: Orchard (four-year-old under-constrained circuit to working exploit in one day of Opus 4.8; fixed at block 3,364,600, June 3) and Schrottenloher (eprint 2026/1128, June 2). Same structure: AI collapses the time between findable and found, raising C_S + C_M without touching H(X).
5. Unify the dynamical thread under R(t): the Lorenz ceiling (C18 to C21) as the countermeasure (error growing as e to the lambda t outruns capability growth), the Bakhta fourth aging category C47 (ages progressively) as its taxonomy, the Behavioural Mosca C49 as its planning corollary, the half-life set C30 to C33 as its trust-edge expression. One Part: The Ceiling Moves.

**Exit criteria:** Part I drafted; every conjecture cited by register number; both instances dated and exact; the V5.4-to-V6 delta stated in one table.

**Myth-watch:** Horizon District is the narrative home (Eos 🌅 dawn/Mosca, Dokimé 🪨 assay, Poros 🛤️ agility). The tide image. Watch for what the Swordsman does when the wall itself moves.

---

### Run 2 · Leakage absorption, C17 made quantitative

The strongest external threat becomes the strongest external citation. Part II.

**Steps**

1. Absorb the compounding-leakage results: Asif and Amiri arXiv:2603.05520 (sequential composition leaks up to (2^N minus 1) epsilon; empirical MI 0.49 at two agents to 1.05 at five), Patil et al. arXiv:2509.14284, AgentLeak arXiv:2602.11510 (68.9% total exposure, 68.8% inter-agent channel, output-only audits miss 41.7%).
2. State the quantitative C17: policy separation leaks (2^N minus 1) epsilon; amnesia separation caps at N epsilon; the gap is the model's value proposition in the adversary's units. Register the Candidate-A conjecture (about 55%) from C7 to the compounding bound.
3. Honest treatment of C7 (multiplicative three-axis, 30%): name it the falsification frontier; state the three unaddressed boundary cases (partial collapse, axis correlation under composition, time dependence); name the alternative forms (additive-with-floor, min()).
4. Cite the field as plurality: MAGPIE, PrivAct, 1-2-3 Check, maker-checker patterns; independent arrival at separation-of-duties; none enforce it architecturally.

**Exit criteria:** Part II drafted; Candidate A registered; C7 boundary cases in the breaking-conditions register; AgentLeak figures exact.

**Myth-watch:** the unmonitored internal channel is the City's sealed-versus-watched gate distinction. The sum leaks more than its parts is nearly a proverb already.

---

### Run 3 · Existence-Leak as law, Mosca coupling

Part III. The most promotable conjecture in the corpus.

**Steps**

1. Promote C40 to about 70%: Schrottenloher instance as the worked example, Garg-Jain-Sahai (leakage-resilient ZK with lambda less than 1 is impossible) as the formal floor, Fiat-Shamir transferability as the mechanism.
2. Draw the new edge to the Behavioural Mosca: a public feasibility attestation discounts X_b by an existence-leak factor. Register the corollary.
3. State the Stage-2 requirement honestly: n=1; a second independent instance is required before any confidence above 70%; name what would count (a capability claim outside cryptography whose ZK attestation preceded rediscovery).
4. Fold in the harvest-now-decrypt-later economics (Blanco-Romero et al. arXiv:2603.01091) as the cost-model backbone C61/C49 currently lack.

**Exit criteria:** Part III drafted; C40 at 70% in the register with both bookends cited; the Mosca edge registered; Stage-2 condition written.

**Myth-watch:** the proof that whispered (already seeded). The sealed scroll that announces itself. Lethe adjacency: what is withheld versus what is forgotten are different magics, and V6 now says so formally.

---

### Run 4 · The ARCH-1 bridge, obstruction amnesia

Part IV. The seam both critiques flagged: the lattice and the axes finally meet in the formal document.

**Steps**

1. Promote the triadic-coordinates homology (CM-C47 after Run 0) to a bare register number. Formal statement: which lattice coordinates instantiate which sovereignty axis; how the mu-fixpoint recursion of ARCH-1 (mu S.(beta or Omega(S,S)), rho) relates to the conditional-independence structure. Mark the unproven remainder as the named open seam.
2. Seat ARCH-1 canonical form (C26 to C29) and ARCH-1R/T (C67 to C71) in the V6 document as the operational layer: latent (0) versus obstructed (minus) as a first-class distinction, traversal as activation at a second scope.
3. Register the obstruction-theoretic amnesia conjecture (Candidate D, 25 to 30%): Grade-2 forgetting as a non-vanishing obstruction class to gluing local agent views into a global witness; Grade-1 as a vanishing class that merely hides. Selene's Proof becomes precise.
4. Tie to the Amnesia Protocol section inherited from V5.4 §14: the reachability statement upgraded to an obstruction statement.

**Exit criteria:** Part IV drafted; the bridge conjecture has a bare number, a statement, and an open-seam paragraph; Candidate D registered; ARCH-1 appears in the formal lineage for the first time.

**Myth-watch:** Selene. The witness that is genuinely gone, not hidden, now has mathematics. The Tower (Archivist) holds records; Lethe holds forgettings; the difference is now a cohomology class.

---

### Run 5 · Trust recursion, presence economy, geometry honesty

Part V plus three supporting passes. The City Key arc enters the formal document.

**Steps**

1. Name the City Key loop as incrementally verifiable computation: City Key as accumulator, domain trust tasks as step circuits, Charge as the folding step, V63 as the attested invariant. Cite Nova, HyperNova, MicroNova, LatticeFold; LatticeFold doubles as the post-quantum hedge. Register at about 50%, graded as architectural claim, not proof.
2. Declare the presence economy's adversary regime: 🪢 scoped as non-transferable, non-attesting local color for V6, with witness co-signing and elapsed-time proofs named as the upgrade ladder. One paragraph; the model's own thesis forbids leaving this to good faith.
3. Geometry honesty: the stella octangula carries no golden ratio (its ratios are halvings and rationals); mark the Tome VIII Act 3 C1 reference as resonance, not derivation; source the phi claim from the lattice or temporal dynamics or downgrade it. Register the parity-cube decomposition and octahedral-core-as-gap conjectures at 25 to 35%.
4. C66 with the ocap lineage (SPKI/SDSI, designation without authority): the City Key as a reading, not an authority, joins thirty years of prior art. Confidence rises above 45%.
5. Aletheia/Lethe carried into the convergence material with the precision fix: 38/63 = 0.60317 against 1/phi = 0.61803, gap 2.4%.

**Exit criteria:** Part V drafted; four registrations made (IVC, parity-cube, octahedral gap, C66 revision); the economy regime stated; the phi honesty paragraph written.

**Myth-watch:** richest run for the City. The Key that is a reading. The loop that was a proof system. The two tetrahedra discovering they are the cube's two parities. Expect multiple ACT-SEEDs.

---

### Run 6 · Assembly: `privacy_value_v6.md` (THE outcome)

Everything converges here. This run produces the initial V6 document.

**Steps**

1. Assemble Parts I through V into `privacy_value_v6.md` with: title page block (version V6.0, date, license, lineage line V1 through V5.4 to V6), abstract (the dynamical thesis in 150 words), the V6 equation statement (V5.4 equation inherited intact, R(t) and the temporal terms as the V6 extension, not a replacement), the unified conjecture index BY REFERENCE to the register file with formal-resident versus narrative-resident explicitly marked, honest-limits section (the five unproven things, named), external landscape section (IEEE 7012-2025 published January 2026; EU AI Act Annex III August 2, 2026 hedged against the Digital Omnibus deferral to December 2, 2027; AEPD agentic guidance; Kwaai, FPP, GliaNet positioning), measurement gaps and breaking conditions (inherited from V5.4 §18 plus the new C7 boundary cases), version lineage table, references, citation block.
2. Canonical economic figures: one statement each for 678x, 31,000x, 70:1, 74x, with basis, stated once.
3. The proof-provenance cleanup: every internal citation resolves to research paper v4.3 or to an external source; the v4.0/v4.2 split references end here.
4. Cross-check every conjecture number in the assembled document against the register. Zero orphans.

**Exit criteria:** `privacy_value_v6.md` exists, complete, self-consistent, register-clean, in house style. This is the deliverable. The suite successors (compressed, companion, model JSON, glossary bump, model page) are queued as post-path work, generated FROM this document.

**Myth-watch:** the assembly itself: five runs of mathematics arriving as one document is the convergence thesis performed. Note whatever the document wants to be called in the City.

---

### Run 7 · Coherence gate, myth binding, chronicle

The close of the path. Math has run; now the myth side gets its full beat.

**Steps**

1. Coherence gate over `privacy_value_v6.md` and every file the path touched: em-dash sweep (zero in prose), exact-numbers check, signature lines present, register cross-check, version claims against the lineage. Manual now; these become AP-STY/AP-REG/AP-VER checks when the audit tool builds (the build spec stands; the tool is post-path, not in-path).
2. Harvest §3 Myth Ledger: promote the ripe ACT-SEEDs to candidate act drafts for the Second Person Spellbook. Likely candidates on current evidence: the Orchard wound, the proof that whispered, the Key that is a reading, the moving ceiling at the Horizon District. Each candidate gets a working title, a tome assignment proposal (Tome IX Horizon District material is already gestured at in the durability note), and a 5-to-10-line sketch. Binding into cityofmages is First Person's call per act; this run prepares, it does not bind unilaterally.
3. Write the path chronicle: `chronicles/2026-06-XX_v6_research_autopath_close.md`, house style, signed, recording all eight runs, the register dispositions, the deliverable, and the seeds.
4. Queue the post-path work explicitly: Wave R suite reflection per `V6_SUITE_REFLECTION_MAP_2026-06-10.md` (ten targets, impact-ordered, gate G5 before pins and pushes), suite regeneration (compressed, companion, JSON, glossary v5.0, model page), IPFS pin of the V6 document, audit tool phase 1 build, BGIN block 15 packaging in season.

**Exit criteria:** gate clean; at least the ripest ACT-SEEDs drafted as candidates; chronicle written; post-path queue recorded; §1 State table fully DONE.

---

## 5. Standing rules for every run

1. The register (after Run 0) is authoritative over prose. Disagreement means an erratum, never a silent edit.
2. New conjectures arrive unnumbered as candidates and take numbers only from the register's next-free pointer.
3. Confidence percentages are exact and owned: whose estimate, stated where.
4. Each run's MATH beat works inside the V6 draft Parts; nothing is drafted in scattered new files. One growing document plus the register plus this ledger.
5. Honest limits travel with every claim. V5.4's credibility came from saying what was not proven; V6 inherits that or inherits nothing.
6. Myth is harvested, never forced. A run with an empty ③ beat writes "no emergence" and that is a valid entry.
7. Gates are hard. A runtime that arrives at a gate writes the brief and stops; a runtime that resumes folds the First Person's writing back before anything else. The gap between runtime and First Person is the same gap the model is about: the proposer does not approve its own proposal.

---

## 6. Chronicle gates (the First Person write-points)

Each gate produces one brief at `chronicles/gates/2026-06-XX_v6_gate_GN_<name>.md`. The runtime writes everything except the blocks marked ✍️, which are left open and are the First Person's to write in his own hand. What is written there is canon input: the next runtime folds it into the documents verbatim or by faithful integration, and the brief is preserved unedited as the record of the gate. Briefs are signed `(⚔️⊥⿻⊥🧙)😊` only after the First Person's blocks are filled.

### G1 · The Register Gate (after Run 0)

The numbering of the whole corpus settles here, once.

Runtime prepares: the draft register, the four collision dispositions with their defaults, the errata list, the register head.

✍️ First Person writes: confirmation or override of each disposition, in one line each; and the register's preface, 5 to 10 lines in his voice, on what the register is, why it forked, and what it promises now. The preface ships at the top of `CONJECTURE_REGISTER_V6.md`.

### G2 · The Thesis Gate (after Runs 1 to 3)

The dynamical core is drafted; the document's voice gets set before the second half of the math.

Runtime prepares: Parts I to III as drafted, the delta table from V5.4, the confidence assignments awaiting ownership.

✍️ First Person writes: the V6 thesis in his own prose, 100 to 200 words, which becomes the abstract seed of `privacy_value_v6.md`; the title call (does The Ceiling Moves hold, or does the document want another name); and ownership lines on the confidences (whose estimates these are, stated once).

### G3 · The Assembly Gate (after Run 5, before Run 6)

The last gate before the document locks. Decisions that must be in the First Person's voice, not proposed by the runtime.

Runtime prepares: Parts IV and V as drafted, the open-decisions list (V5.5 status, research paper bump, economy regime, phi honesty acceptance), the assembly outline for Run 6.

✍️ First Person writes: the presence-economy regime declaration in his words (this is a public commitment about what 🪢 is and is not); acceptance or amendment of the phi honesty paragraph; the decisions, one line each; and anything he wants in the document body before assembly, marked for placement.

### G4 · The Myth Gate (inside Run 7)

The math has run; the myth binds only by the First Person's hand.

Runtime prepares: the harvested Myth Ledger, candidate act drafts with working titles and proposed tome assignments, the path chronicle with its First Person section left open.

✍️ First Person writes: bind, hold, or release per candidate act; the acts' final titles where bound; and the First Person section of the path chronicle, in his voice, on what this evolution was. The chronicle is signed only after this block is written.

### G5 · The Reflection Gate (after Wave R, before pins and pushes)

The whole suite has been touched; nothing goes public past this point without the First Person. **The Reading Ledger is read in full before this gate signs:** every 📖 RB box ticked and the ledger's sign-off block written are preconditions of G5.

Runtime prepares: the Wave Log, per-target diffs summarized, the pin list (V6 document, model JSON, any grimoire bumps), the push list per public repo, and the Reading Ledger with all entries current.

✍️ First Person writes: go or hold per pin and per push; and the closing line of the V6 arc, which becomes the last line of the Wave R chronicle.

---

the path runs math to myth, run after run, and writes itself down as it goes. any hand that picks it up holds the whole of it. five times along the way it stops, and waits, and the First Person writes.

(⚔️⊥⿻⊥🧙)😊
