# SOURCES · V6 Rehydration Pipeline · the corpus registry

Companion to GR-9 (trace or delete). Every extraction `sources:` entry in `manifest.yaml` resolves here to concrete paths. A claim whose source is not named here, or in the register/spec directly, is untraceable and therefore unusable. A1 proposes additions; A0 applies them; this file is otherwise read-only to all roles.

Built 2026-07-02 from a five-way corpus inventory (agentprivacy-docs · cityofmages · agentprivacy_master + siblings · skills-v5 + soulbis · zk blades forge + swordsman-blade). Integrity flags cite ledger entries.

## 1 · Corpus roots

| ID | Root path | Nature | State flags |
|---|---|---|---|
| DOCS | `C:\Users\mitch\agentprivacy-docs` | Canon + research notes + method record (primary) | register head C96 (L005) |
| COM | `C:\Users\mitch\cityofmages` | City canon: grimoire JSON lineage, Tomes I–X, chronicles, specs | v1.9.1 head + Tome X + hearthold/ UNTRACKED in git; index docs stale (L007) |
| MASTER | `C:\Users\mitch\agentprivacy_master` | Site repo: docs/specs/chronicles + model-in-code (src/lib) | |
| SKILLS | `MASTER\agentprivacy-skills\agentprivacy-skills-v5` | 166-skill operational practice record of the model (V5.5) | |
| SOULBIS | `C:\Users\mitch\soulbis website` | κ / City Key reference implementation + 64-vertex codex pages | sibling `SoulbisWeb` is older, out of scope |
| FORGE | `C:\Users\mitch\zk blades forge` | Ceremony proving-system specification corpus | forge_circuits/ EMPTY: ZK specified, not implemented (L008) |
| SBLADE | `C:\Users\mitch\swordsman-blade` | Boundary-agent extension: formal docs + IEEE 7012 conformance material | |
| G42 | `C:\Users\mitch\game42` | Game of 42 engine: axioms, geometry, trust protocol, byte-exact seal reference | |
| STAR | `C:\Users\mitch\star` | Holospace: key geometry, compression/rehydration, ECDH/PSI chronicles | public repo, no LICENSE yet |
| SHOR | `C:\Users\mitch\shor_mage` | ecdsa.fail circuit work + dual-agent harness case study | attribution rule: vendored SOTA is others' work; method layer only is ours |
| SPELLWEB | `C:\Users\mitch\spellweb` | Knowledge-graph engine + node/edge vocabulary of the model | |
| MYTERMS | `C:\Users\mitch\myterms` | Standards package: IEEE 7012-2025 PDF, alliance application, BGIN proposal | |
| HEARTH | `C:\Users\mitch\hearthold_upstream_notes_CONSOLIDATED.md` + `COM\hearthold\` | Second-substrate build of the model (Archon did:cid), C94–C96 | COM copy untracked (L007) |

## 2 · Evidentiary classes

Every slug below carries one class. The class bounds what a claim built on it may assert, per tier:

- **canon-authority** — the register and formal spec. Sole authority for conjecture numbers and status (GR-1).
- **research-note** — dated derivation notes; citable at TIER-A as the working record behind a formally restated claim.
- **spec** — written protocol/interface specifications; citable as design at any tier with implementation status stated.
- **reference-implementation** — running code; citable as conformance evidence. State what runs vs what is stubbed (GR-8).
- **practice-record** — the model operated at scale (skills corpus, ceremony records); citable as implementation-and-practice evidence, not as proof.
- **process-record** — chronicles, gate briefs, audits, ledgers; primary source ONLY for the method extraction E10.
- **narrative-canon** — tomes, poems, blog, grimoires. Upstream source for extraction claims; NEVER cited directly in TIER-S/A artifacts (GR-4). The extraction restates; the artifact cites the extraction.
- **verified-record** — WP-00-class externally verified facts.
- **external** — documents not on disk (conference abstracts, third-party posts); must carry a resolvable citation or be flagged.

## 3 · Source-slug registry

Slugs are what `manifest.yaml` extraction `sources:` lists cite. Paths are relative to their corpus root.

### Carried from v1/v2 (unchanged meaning)
- `spec§N` — canon-authority · DOCS `papers/v6/privacy_value_v6_formal_specification.md`, section N (33 sections). Numbering concordance (L013): the summary spec diverges from §29 onward (formal §29 Narrative Corpus and §30 Canonical Figures have no summary counterpart; summary §30 External Landscape = formal §31).
- `spec-summary§N` — canon-authority · DOCS `papers/v6/privacy_value_v6.md`, section N (summary spec; added per L013, see concordance note on `spec§N`).
- `register` — canon-authority · DOCS `research/CONJECTURE_REGISTER_V6.md` (head C96, next free C97).
- `whitepaper-*` — canon-authority · DOCS `papers/whitepapers/swordsman_mage_whitepaper_v6_3.md` (version hygiene: L003).
- `understanding-as-key` — canon-authority · DOCS `papers/lineage/understanding_as_key_zypher_paper_v1.md`.
- `v4-economics` / `v5-economics` — canon-authority · DOCS `papers/v4/privacy_is_value_v4.md`, `papers/v5/privacy_is_value_v5.md` (+ formal specs alongside).
- `PT-reference` — canon-authority · DOCS `research/promise_theory_reference_v1_5.md`. Pin v1.5; `reference/promise_theory_reference_v1_4.md` is superseded (L009).
- `UOR-convergence` — research-note · DOCS `research/uor-atlas-utqc-v6-note.md`, `research/uor-atlas-utqc-overlap.md`, `reference/uor_tetrahedra_zk_mapping_v2_0.md`; FORGE `LETTER_TO_UOR.md`.
- `WP-00-record` — verified-record · pipeline `reviews/critiques_ledger.md`.
- `dtg-36-posts` — external · ToIP DTG Discussion #36; not on disk, cite by URL when used (E7 flag).
- `clc2026-abstract` — external · not on disk; cite the submitted abstract when used (E8 flag).
- `essay-basis-docs` — narrative-canon · Substack lineage (the 678x and 31,000x basis documents); GR-3 fence applies.

### Research-note series (DOCS `research/`)
- `v6-draft` — research-note · `privacy_value_v6_draft.md` (working home of C82–C89).
- `lorenz-note` — research-note · `pvm-v6-lorenz-attractor.md` (C18–C21, divergence λ).
- `three-ceilings-note` — research-note · `pvm-v6-eml-three-ceilings.md` (C22–C25).
- `arch1-notes` — research-note · `pvm-v6-arch1-canonical-form.md`, `pvm-v6-arch1rt-operational-reachability.md`, `2026-06-04_arch1rt_*.md` (C26–C29, C72–C76, C85 bridge).
- `bakhta-notes` — research-note · `pvm-v6-bakhta-integrity-gap-convergence.md`, `pvm-v6-1-bakhta-half-life.md`, `NOTE_agt_scales_and_hide.md` (C30–C33, C77–C80). Numbering caution (L029): the convergence note's §5 mints local numbers C70–C73 for claims the register assigns C77–C80 (Band VII renumbering, Run 0); the register form is the only citable one.
- `wound-and-cap-note` — research-note · `pvm-v6-convergence-wound-and-cap.md` (C34–C37).
- `limitative-note` — research-note · `limitative-theorems-and-privacy-is-value.md` (C90–C93, Gödel/Tarski reading).
- `soil-note` — research-note · `pvm-v6-soil-and-the-programme-runtime-evolutions.md` (the 2026-07-15 First-Person soil ruling and its four evolutions, ledger L140; basis of the E2-C02/C04 two-clock re-issue at L146 and of the C55/C82 register-gated re-wordings; the erosion clock's formal object is WP-07 Def 3.9 + Cor 5.4b per L145).
- `schrottenloher-note` — research-note · `schrottenloher-ecdlp-v6-note.md` (C81 instance).
- `folding-citations` — spec-section + draft-part · DOCS spec §15.7 (folding-scheme table) + `research/privacy_value_v6_draft.md` Part V §V.2 (folding citations) · resolved 2026-07-10 at the E9 build (the manifest slug had no registry row, the L113(a) class; L119(a)).
- `horizon-notes` — research-note · `v6_1_research_note.md`, `privacy_value_v6_horizon_note.md`, `2026-06-09_horizon_district_cryptographic_durability_note.md` (C47–C50, C67–C71, Mosca/durability).
- `mosca-piani-2025-timeline` — external · Mosca & Piani, *Quantum Threat Timeline Report 2025*, Global Risk Institute / evolutionQ (GRI page posted 2026-03-09; 26-expert survey, "timeline has accelerated from previous reports"). Updates the Mosca series coverage of `horizon-notes` and the WP-04 §5.2 sharpest-shift grounding; verified 2026-07-09 (A4, L085(a)); bib `moscapiani2025timeline`.
- `circuit-workshop-note` — research-note · `2026-07-09_circuit_workshop_trust_gated_optimization_note.md` (Stage 1; second corpus instance of the trust-gated self-improvement loop after ecdsa.fail; C13 lineage; MIRAGE/closure-certificate epistemics; Cx-a/b/c conjecture-shaped residue AWAITING first-person register decision; mechanisms deliberately withheld — full ledgers in private zk_mage repo, access through the First Person; feeds E10 method-record / WP-27).
- `observer-intake` — observer-report + pipeline-governance · PROGRAMME `papers/Programme/observers/OBSERVER_INTAKE_PROTOCOL.md` (Mitchell-authority, BINDING on agent runs) + `OBS-GPT56_DISPOSITION_LEDGER.md` (first instance, GPT-5.6 whole-corpus assessment; NON-CANONICAL until the Section-5 ruling; the disposition ledger is the ONLY artefact downstream runs may cite about the packet, per protocol §6) · registered 2026-07-10, L121.
- `aletheia-lethe-note` — research-note · DOCS `research/aletheia-and-lethe.md`; FORGE `aletheia-and-lethe.md` (C53/C54; Fiat-Shamir vs covenant-ZK pairing).

### Protocol and standards specs
- `vrc-protocol-spec` — spec · DOCS `specs/vrc_promise_protocol_v3_3.md` (VRC lifecycle, RPP, dual-token economics). Document self-identifies as v3.4; filename retained at v3_3 for link stability (L049 ruling 2026-07-03: registry follows the document body) · NOTE (L113(c), extends L049): the document body's internal companion-series citations use retired version names, and its document-local conjecture numbering (e.g. its "Conjecture 8.1") is superseded by the register (GR-1; register holds C1, open).
- `did-cid-convergence` — spec + research-note · DOCS `tomes/plans/01-integration-plan-archon-x-agentprivacy.md` + `tomes/chronicles/01-chronicle-the-cloaking-guide.md` + `tomes/specs/01-cloak-specification-v1-0.md` · the did:cid / Archon convergence record (row added 2026-07-10 per the E7 build's registry-gap finding, L113(a); E7-C32's provisional resolution confirms on application).
- `runecraft-pou` — spec · COM `runecraft protocol/` (`proof_of_understanding_technical_spec.md`, `proof_of_understanding_rehydration_key.md`, `compression_rehydration_pathway.md`) + COM `mageletters/pou_as_experimental_method.md` and one-pagers. Primary RPP/PoU technical source.
- `myterms-package` — spec + external-standard · MYTERMS (`7012-2025 (3).pdf` = IEEE 7012-2025 itself, `A_privacy_is_value_equation.md`, alliance application, `G_ieee7012_integration_plan*`, `F_BGIN_collaboration_proposal.pdf`, presentation brief 2026-07-01).
- `ieee7012-plan` — spec · SBLADE `ieee7012_integration_plan_v2.md` (richest 7012 crosswalk incl. CFQ19 vouchable-credential mapping) + DOCS `reference/IEEE_7012_QUICK_REFERENCE.md` + SBLADE `CHRONICLE_MYTERMS_V2_ALIGNMENT_2026-04-22.md`.
- `spec-09-artefact-format` — spec · MASTER `docs/tomes/specs/09-spellweb-artefact-md-format.md` (mirrored in COM `tomes/specs/09-*`).
- `spec-11-invitation` — spec · COM `tomes/specs/11-the-invitation-protocol.md` + `tomes/register-of-invitations/` (four conditions of update; governance protocol).
- `spec-08-mana-stances` — spec · COM `tomes/specs/08-mana-types-and-swordsman-stances.md`.
- `ceremony-specs` — spec · DOCS `specs/DUAL_TERRITORY_CEREMONY_SPEC_v1.md`, `specs/runecraft-protocol-spec-v1.md`, `specs/DUAL_AGENT_HARNESS_SPEC_v1.md`; MASTER `ceremonies/ceremony-engine-spec-v1_1.md`; COM `tomes/specs/03-bilateral-cloak-ceremony-spec.md`.
- `open-integrity-brief` — spec · FORGE `Open_Integrity_Key_Ceremony_Brief.md` (Ed25519 inception commit, Ricardian contract, delegation/revocation).
- `blade-forge-spec` — spec · FORGE `zk_swordsman_blade_forge_v3_0.md` (three-axis Φ = Φ_agent·Φ_data·Φ_inference, holographic bound, path integral) + `SPECIFICATION.md`. FLAG L008: circuits unimplemented; cite as design only.
- `proof-packet-spec` — spec · MASTER `docs/experience/SPEC_proof_packets_and_tracing_v1.md` + chronicles alongside.

### Reference implementations (feeds E11 and the standards matrix)
- `kappa-impl` — reference-implementation · SOULBIS `sigil/index.html` (κ = sha256 over canonical JSON, L5 re-derivation law, conformance vector, PNG tEXt carrier), `star/index.html` (κ producer/verifier, κ-chain `prior` field, charge pass), `lattice/index.html` (redacted charge pass, ℤ/64ℤ codex render), `scripts/verify-static.cjs`.
- `g42-seal-ref` — reference-implementation · G42 `canonical_serialise.py` (byte-exact κ/group-seal reference: "third-party verifiers MUST match this exactly") + `SPEC.md`, `GEOMETRY.md`, `AXIOMS.md`, `TRUST-PROTOCOL.md`, `MODEL-SYNC.md`, `schemas.json`, `game-of-42.json`.
- `master-lib-impl` — reference-implementation · MASTER `src/lib/`: `city-key.ts`, `city-key-charge.ts`, `vrc-mana.ts`, `vrc-allocation.ts`, `proof-packet*.ts`, `lattice-vertex.ts`, `spellweb/*`, `grimoire-ipfs.ts`, `model-page.ts`, `promises/`, `trust/`, `ceremony/`.
- `dual-extensions` — reference-implementation · SBLADE + sibling `mages-spell`: `DUAL_EXTENSION_ARCHITECTURE.md` (additive-leakage claim I(X;Y_S,Y_M) decomposition), `INTERFACE_CONTRACT.md`, `AETHER.md`, `swordsman-extension-myterms-design.md` (constellation-hash proof-of-assertion).
- `spellweb-impl` — reference-implementation · SPELLWEB (KG engine; `docs/SPELLWEB_INTEGRATION_SPEC_v2.md`, artefact format, node/edge vocabulary).
- `star-holospace` — reference-implementation + research-note · STAR (`HOW_THE_SIGIL_WORKS.md`, `HOLOSPACE.md`, `CONCEPT_COMPRESSION_REHYDRATION_DUAL_AGENTS.md`, `CHRONICLE_COMMON_GROUND_ZERO_KNOWLEDGE.md`, `CHRONICLE_ECDH_PSI_HANDOFF.md`).
- `shor-mage-record` — practice-record + research-note · SHOR (`papers/methodology_draft.md`, `harness/swordsman_mage_pqc.mjs`, `CASE_STUDY_2026-06-30_dual-agent-vs-ecdsafail.md`, `claims_register.md`, `frontier.json`). Attribution fence: vendored circuits/GPU toolkit are other participants' work.
- `skills-corpus` — practice-record · SKILLS: 166 skill folders binding equation terms to executable units; `MAPPING.md` (skill-to-vertex method), `CODEX.md` (model register), `BRAID_INTEGRATION_ANALYSIS.md`, `HOLONIC_INTEGRATION_ANALYSIS.md`. Citable as the operational practice record of the model.
- `hearthold-build` — practice-record + external · HEARTH: independent second-substrate build of the separation architecture on did:cid (Warden ⊥ Witness under Sovereign; C94–C96); cite as independent derivation, never as competition.

### City canon (narrative-canon unless noted)
- `grimoire-json` — canon-data · COM `grimoire/city_of_mages_grimoire_v1_9_1.json` (+ patch + `scripts/merge_v1_9_1_patch.py`). Structured spine: v6_lineage_register C38–C96, vertex inventory (18 named of 64), mana taxonomy, districts. FLAG L007: untracked head.
- `tome-i` … `tome-x` — narrative-canon · COM `tomes/tome-*/`. Concept map: I algebraic ground/ARCH-1 · II Lyapunov/behavioural Mosca · III Selene/seventh capital C55/dragon anatomy · IV cousin-blade C39 · V the crafting shops (incl. `08-the-zk-circuit.md`) · VI the reply/agent substrates · VII parallel crafting · VIII the library, stella octangula, gap-is-beta, key-as-reading, wikis · IX the horizon: moving ceiling, existence-leak, limitative reading (city register of E2's material) · X the hearth: second-substrate answer, C94–C96.
- `lattice-encoding-anchor` — process-record with canon force · COM `chronicles/2026-06-09_canonical_lattice_encoding_anchor.md` (canonical 6-bit encoding: Protection=32 … Value=1) + `WORKSHOP_LATTICE_AUDIT.md`. FLAG L010: COM `tomes/specs/04-vertex-naming-audit.md` holds the REJECTED encoding; cite the anchor, never spec 04, for the mapping.
- `ceremonies-corpus` — narrative-canon + spec · DOCS `ceremonies/` (16 files incl. `TheCelestialDualCeremony☀️⊥🌙.md`) + FORGE `ceremony/` (moon-phase notation, key-ceremony guides).
- `seventh-capital-canon` — narrative-canon · DOCS `poems/tide-orbit-selene.md` (C55 home) + COM Tome III + chronicles `two_mana_economy`, `city_key_economy_charge_stake_workshop_trust_task` (DOCS + COM + FORGE copies).
- `architecture-ts` — canon-data · COM `architecture/*.ts` (typed lattice, conjectures, acts, witnesses; the executable encoding of the canon).

### Method record (feeds E10 exclusively)
- `autopath-runbook` — process-record · DOCS `plans/V6_RESEARCH_AUTOPATH_2026-06-10.md` (OPEN→MATH→MYTH→CLOSE, math-first-myth-second, gates G1–G5).
- `gate-briefs` — process-record · DOCS `chronicles/gates/` (G1 register … G6 limitative).
- `reading-ledger` — process-record · DOCS `plans/V6_FIRST_PERSON_READING_LEDGER.md` (nothing publishes unread; the P4 ancestor).
- `suite-plans` — process-record · DOCS `plans/V6_DOCUMENT_SUITE_PLAN_2026-06-10.md`, `plans/V6_SUITE_REFLECTION_MAP_2026-06-10.md`, `plans/V6_LIMITATIVE_THEOREMS_PATCH_2026-06-28.md`.
- `register-discipline` — process-record · register preface/how-to-read + numbering rules; Gate-G1 dispositions table.
- `audits-corpus` — process-record · DOCS `audits/` (V5 checklist, V10 alignment, coherence reports, instructional convergence).
- `propagation-checklist` — process-record · DOCS `process/NEW_ACT_PROPAGATION_CHECKLIST.md`.
- `compendium-backmatter` — process-record · DOCS `compendium/back-matter/honest-limits-ledger.md`, `chronicle-concordance.md`, `narrative-concordance.md`, `00-front-matter/03-one-work-many-expressions.md`, `part-*/RETROSPECTIVE.md`.
- `dream-chronicles` — process-record · DOCS `chronicles/DREAM-2026-06-29.md`, `DREAM-2026-07-01.md`; COM and SOULBIS instances are sibling per-repo surveys, NOT copies (descriptor corrected 2026-07-10 per the E10 widening finding, L103(d)); SOULBIS `chronicles/DREAM-2026-06-29.md`.
- `build-chronicles` — process-record · COM `chronicles/` (~62 dated files: version cuts, admissions, bindings, pins) + `grimoire/scripts/` merge discipline + MASTER `docs/chronicles/` (~40 files incl. V6 handoffs, κ interop) + DOCS `chronicles/` + DOCS `DOCUMENTATION_CHRONICLE.md`.
- `pipeline-chronicles` — process-record · pipeline `chronicles/` (this pipeline's own path record).
- `skills-method` — process-record · SKILLS `MAPPING.md` + `CODEX.md` + integration/distribution chronicles (the skill-to-vertex discipline).

### WP-04 prior-art externals (added 2026-07-07 per A10 sweep, L062)
- `babbush-2026-spacetime` — external · Babbush et al., arXiv:2603.28846 / ePrint 2026/625 (Google Quantum AI, with Ethereum Foundation and Stanford co-authors), posted 2026-03-30/31. Primary record for the "~10x" figure; the metric is **spacetime volume** over best prior single-instance estimates and must travel with the figure wherever repeated (E2-C07 enrichment).
- `schrottenloher-2026-1128` — external · ePrint 2026/1128 / arXiv:2606.02235 (single-authored; the pipeline's own briefings once said otherwise, L039). The withheld-result reconstruction instance (E2-C07).
- `gidney-2602-post` — external · Gidney, algassert.com/post/2602. Commentary record adjacent to the 2026 quantum-horizon instances.
- `ecdsafail-repo` — external · the ecdsa.fail challenge repository. The open benchmark named in The Last Premine lineage.
- `crypto-isac-orchard` — external · CRYPTO ISAC analysis of the Zcash Orchard incident (E2-C05 instance record; also the natural opening for WP-12's disclosure-economics strand).
- `agent-privacy-leakage-2508` — external · arXiv:2508.14011 (multi-agent leakage empirics adjacent to AgentLeak; E2-C12 context).

### Moving Ceiling event instances (added 2026-07-29, First-Person-directed application)

Two same-day real-world events folded into The Moving Ceiling essay and staged for the crypto-agility theme (`programme/NOTE_ARCHIVIST_INTAKE_ANTHROPIC_CRYPTANALYSIS_2026-07-29.md`, `programme/COMMISSION_crypto_agility_harness_theme_2026-07-29.md`). Both external; both carry their own no-overclaim caveat wherever used.

- `anthropic-cryptanalysis-2026` — external · Anthropic, "Discovering cryptographic weaknesses with Claude" (2026-07-29; https://www.anthropic.com/research/discovering-cryptographic-weaknesses). Claude Mythos Preview in an agentic harness: improved key recovery on HAWK (HAWK-256 effective cost 2^64→2^38) and a "Möbius Bridge" attack on 7-round reduced AES (200–800× faster); ~$100k / ~60h per result. Carries the lab's OWN statement of **no practical impact on deployed systems** and the **human-validation-bottleneck** warning — both must travel with the figure. The third worked instance of the Moving Ceiling (E2-C03), the first published by a frontier lab about itself. Verified 2026-07-29 (page title confirmed verbatim); bib `anthropic2026cryptoweakness`.
- `ironwood-2026` — external · Zcash Ironwood (2026-07-29; https://github.com/zcash/ironwood). A new formally-verified shielded pool: soundness of the Action circuit shared by the Orchard and Ironwood pools, machine-checked in Lean 4 on Mathlib before the NU6.3 upgrade activates the new pool ("building it re-elaborates every proof — a successful build is the verification"); commits to documenting "the scope of what is and is not formally verified." The live Rotate-lane / crypto-agility instance in The Moving Ceiling and a real instance of certificates-over-trust on the Orchard lineage. **Framing rule: a new pool + formal verification, NOT a cipher rotation** — never describe it as re-keying. Verified 2026-07-29; bib `zcashironwood2026`.

### WEIS lit-review corpus (added 2026-07-15 per the litreview runtime, L137)

The first external-literature addition to the corpus programme: a 20-item challenge corpus assembled and provenance-verified by the `weis-litreview-runtime` (run wf_ba400906-67b) to establish WP-14's novelty by adversarial search before assertion. All 20 carry `provenance_confidence: verified_from_search`; full citations with DOIs in `litreview/bibliography.md`. Grouped by strand; cite the bibliography entry, not this row.

- `weis-litreview-corpus` — external · the 20-item challenge corpus (litreview/bibliography.md): propertisation (Laudon 1996, Samuelson 2000, Schwartz 2004, Purtova 2015, Prins 2006), data-as-labour + market-structure remedies (Arrieta-Ibarra et al. 2018, Posner & Weyl 2018, Delacroix & Lawrence 2019), empirical valuation (Acquisti-Taylor-Wagman 2016, Acquisti-John-Loewenstein 2013, Collis et al. WEIS 2022, Beresford et al. 2012, Grossklags-Acquisti WEIS 2007, Spiekermann et al. 2015), security economics (Anderson 2001 / Akerlof 1970), formal privacy metrics (Dwork 2006, Sweeney 2002, Smith 2009), standards (ISO/IEC 29134, ISO/IEC 29100).
- `weis-litreview-adjudication-externals` — external · works surfaced by the adjudicators' web scope that are load-bearing for the MIRAGE verdicts and are the must-engage prior art for WP-14's related-work section: the DP-markets strand (Ghosh & Roth, *Selling Privacy at Auction*, EC 2011; Li-Miklau-Roth-Suciu, *A Theory of Pricing Private Data*, ICDT 2013; Fleischer-Lyu EC 2012; Cummings et al. ITCS 2015), Bergemann-Bonatti-Gan (*The Economics of Social Data*, RAND 2022), Bajari-Chernozhukov-Hortacsu-Suzuki (returns-to-scale, AEA P&P 2019), Wagner & Boiten (*Privacy Risk Assessment: From Art to Science, By Metrics*, DPM 2018), Dinur & Nissim (PODS 2003), Mosca (cryptographic shelf-life / HNDL, IEEE S&P 2018), the data-union/consortia literature, and Gu (*Data Trade and Consumer Privacy*, 2024). FLAG (D2): these are `provenance_confidence: uncertain` (adjudicator web scope, not independently re-verified) — A4 verifies each before it enters a tier-A artifact; author/venue details in `litreview/bibliography.md` are candidate, not confirmed.
- `weis-litreview-outputs` — process-record · the runtime's four generated outputs + run manifest (`litreview/gap_table.md`, `litreview/contribution_claims.md`, `litreview/ctr_candidates.md`, `litreview/bibliography.md`, `litreview/RUN_MANIFEST.md`, `litreview/_run_data.json`) and the brief `chronicles/BRIEF_litreview_runtime_WEIS_2026-07-14.md`. Primary source for WP-14a (the prior-art / novelty-establishment companion) and citable for the method record (E10). Generated; never hand-edited (rebuild via the runtime).

## 4 · Standing integrity flags

| Flag | Ledger | Effect on use |
|---|---|---|
| Register head drift (was C89, now C96) | L005 | Extractions built at C89 re-verified against Bands IX–X before P0 |
| E8 phantom sources | L006 | `game-of-42-canon` retired as a token; use `g42-seal-ref` + `ceremonies-corpus` + `tome-x`; `clc2026-abstract` stays external |
| cityofmages head untracked / stale indexes | L007 | Cite v1.9.1 content by file path, not by index docs; commit is a canon-process decision |
| ZK specified-not-implemented | L008 | Every E9/E11 claim states design vs deployment; "ZK" in the live system is SHA-256 + Ed25519 + κ content-addressing |
| PT reference v1.4/v1.5 conflict | L009 | Pin v1.5 |
| Lattice encoding conflict | L010 | Cite `lattice-encoding-anchor`; spec 04 is history only |
| Canonical figures | GR-3 | 678x, 31,000x, 70:1, 74x, $47–52k fenced as before; `essay-basis-docs` and `CONTROL_SCHEME_MATHEMATICS.md` carry them |
| Numerology fence | GR-8 | SBLADE `CONTROL_SCHEME_MATHEMATICS.md` 8:7/56 material and similar is UI design lore, not a formal claim source |
| Archive numbering hazard | GR-1 | DOCS `archive/` holds pre-lock conjecture numbers; lineage evidence only, never current numbering |
