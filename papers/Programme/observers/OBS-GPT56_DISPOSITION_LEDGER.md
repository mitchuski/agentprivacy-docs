# OBS-GPT56_DISPOSITION_LEDGER.md

**Artefact class:** observer disposition ledger (first pass, agent-proposed)
**Register:** formal (pipeline scaffold)
**Authority:** non-canonical until Mitchell's ruling on Section 5; dispositions below are proposals
**Packet:** AgentPrivacy Whole-Corpus Observer Assessment, OpenAI GPT-5.6 Thinking
**Packet manifest sha256:** c266da74657070d3c6b4fbe592964ff3bb70af669923b948e78c1bc7ab1c8d2a
**Protocol:** OBSERVER_INTAKE_PROTOCOL.md
**Date:** 2026-07-10

*take the critique whole; disposition it one claim at a time.*

---

## 0. Verdict first

The packet is high quality and mostly convergent with existing house doctrine. Of the substantive claims, most are accepted or accepted-with-amendment because they restate principles the pipeline already enforces (register wins, claim classes, projection discipline, human gates). Three findings genuinely earn their keep: the exact mutual-information decomposition critique (routed to CTR-OBS-01), the demand for operational definitions under the reconstruction bound (CTR-OBS-02, folds into V6), and the two-map doctrine separating experience from evidence (adopted into the protocol). The observer's numerical scores are retained but not ingested. Nothing in the packet forces a change to the V6 submission thesis; one finding tightens it favourably.

One uncomfortable confirmation is logged honestly: the observer's "canonical version drift beneath the experience" hypothesis has at least one live supporting instance inside our own skill surfaces (OBS-GPT56-014). Register wins; the surface is the bug.

## 1. Disposition ledger

Legend: A = accepted, M = amended, R = rejected, D = deferred. Confidence percentages follow house discipline and attach to the *disposition reasoning*, not the observer's claim.

### 1.1 Provenance and framing

**OBS-GPT56-001** · Packet is non-canonical, requires verification, must not be cited as independent proof.
Disposition: **A**. Self-classification matches protocol rule 1 exactly. Header adopted verbatim. (Operational, 99%)

**OBS-GPT56-002** · The discovery sequence itself is evidence about the public experience.
Disposition: **A**. Route trace filed to the experience map. First entry in the route ledger; future observers compared against it. (Operational, 95%)

**OBS-GPT56-003** · The observer's own manifest (v0.3 yaml) is also non-canonical.
Disposition: **A**. Filed as reference-only pending rights and content review. Not ingested. (Operational, 99%)

### 1.2 Whole-corpus model

**OBS-GPT56-004** · AgentPrivacy is a path-dependent research and experience system, not one site or repo; the corpus includes routes, state, absences, and handoffs, not only prose.
Disposition: **A**. Matches design intent as Mitchell has stated it. The ten-layer table is adopted as a working map for the experience register, marked Architectural. (Architectural, 90%)

**OBS-GPT56-005** · agentprivacy.ai is not reducible to /model; earlier observer passes over-weighted /model and public repos as proxies.
Disposition: **A**. The observer's self-correction is retained as the canonical example of the projection-as-proxy trap. Regression seed RS-05. (Operational, 95%)

**OBS-GPT56-006** · The public agentprivacy-spellbook repository is historical, not current live-site source.
Disposition: **A**, already established by Mitchell's in-conversation correction which the packet records. Action: apply the new `historical` status flag to the repository README so the trap is labelled at source. Regression seed RS-01. (Operational, 95%)

### 1.3 Central assessment

**OBS-GPT56-007** · The strongest contribution is the separation of protection and delegation; Swordsman and Mage encode privilege separation, held-out evaluation, refusal authority, proposal versus acceptance.
Disposition: **A**. Convergent restatement of C17 (architecture over policy) and the three-axis gating Φ_agent · Φ_data · Φ_inference. Useful as external confirmation of legibility: an outside agent recovered the core from partial access. Not evidence of correctness, only of communicability. (Operational, 90%)

**OBS-GPT56-008** · Discovery friction is intentional epistemic design, not automatically a defect; but intentional mystery must never excuse factual contradiction. Two categories: intentional experiential ambiguity versus unintentional canonical inconsistency.
Disposition: **A**. Adopted as standing doctrine in the protocol (rule 6). The packet's phrasing "preserve mystery in the journey; remove ambiguity from the evidence" is retained with attribution as an observer-coined proverb, not house canon. (Architectural, 90%)

**OBS-GPT56-009** · The project is more implemented than a documentation-only reading suggests, but implementation maturity varies and lacks a universal status layer.
Disposition: **M**. The maturity-variance observation is accepted. The remedy is amended: no new universal status layer is built. Instead the existing single-source-of-truth pattern is extended, with `historical` and `superseded` flags plus per-artefact status drawn from the release substrate (see OBS-GPT56-020). New parallel infrastructure is exactly the uncontrolled expansion the packet itself warns against. (Architectural, 85%)

**OBS-GPT56-010** · The auto-research harness may be the most important technical asset; its value depends on genuine proposer and prover separation, deterministic overrides, pinned evidence, human disposition, and visible negative results.
Disposition: **M**. The separation requirements are accepted; they restate GROUND_RULES.md and the A0 to A13 role-card architecture. The superlative ("most important") is rejected as score-class opinion. The observer did not inspect the current harness; its description is of documents about the harness. Filed as an outside hypothesis for comparison against the actual implementation, per the packet's own instruction. (Conjectural, 70% that the harness-as-Research-OS framing survives internal comparison)

### 1.4 Formal-register critiques

**OBS-GPT56-011** · Mutual-information additivity as stated needs correction: the general relation is I(X;Y_S,Y_M) = I(X;Y_S) + I(X;Y_M) − I(Y_S;Y_M) + I(Y_S;Y_M|X); conditional independence given X gives an upper bound after subtracting marginal redundancy; exact additivity needs marginal independence too.
Disposition: **M**, routed to **CTR-OBS-01**. The observer's decomposition is standard and correct as information theory. The amendment: this does not break the reconstruction ceiling, it tightens it in the favourable direction. If joint leakage is subadditive under conditional independence, then R computed from C_S + C_M remains a valid (conservative) upper bound, and the marginal redundancy term −I(Y_S;Y_M) only lowers true joint information further. The defect is precision of statement in surfaces that claim exact additivity, not soundness of the ceiling. Proof obligation filed; formal register resolves; prose surfaces patch afterwards, never first. Cross-check against V5.4 skill surfaces that state "additive information bounds: proven" without the redundancy qualifier. (Conjectural pending formal write-up, 85% that the ceiling survives with a strictly tighter bound)

**OBS-GPT56-012** · A capacity ratio below one does not independently establish universal impossibility of reconstruction; operational definitions required for the private variable, channel models, side information, composition, adversary, decoder, error criterion, and Fano-style assumptions.
Disposition: **A**, routed to **CTR-OBS-02** and folded into the V6 submission checklist rather than opened as a separate workstream. V6's time-dependent R(t), compositional leakage amplification, and the Behavioral Mosca thread already target exactly this gap; the packet supplies a clean external checklist for the assumptions section. This strengthens the pre-registered falsification posture rather than threatening it: the honest-limits section is the competitive differentiator, and the observer has just written part of it for free. (Architectural, 90%)

**OBS-GPT56-013** · Algebraic coherence of the 64-state lattice is not itself a privacy proof; retain as compositional model, transformation grammar, and indexing system; do not infer confidentiality from elegance.
Disposition: **A**. Convergent with existing discipline; the lattice has never been claimed as a confidentiality proof in the register. Action: vocabulary check script extended to flag lattice-adjacent uses of unqualified *secure* and *proof* on public surfaces. (Operational, 90%)

**OBS-GPT56-014** · Canonical version drift exists beneath the experience (observer hypothesis to falsify).
Disposition: **M**, partially confirmed, logged honestly. Live instance found during this pass: the V4-era root skill surface records the 96 versus 64 edge discrepancy as open and unresolved, while the holographic-bound register records a 96/64 resolution (boundary-encodes-volume, C6 thread). One of these surfaces is stale. Register wins; the skill surface is the bug and is queued for a version-hygiene patch. Second known instance class: stale conjecture numbering (~C40 / ~60% versus live C81 / 70%), previously caught. The hypothesis is not fully accepted: drift exists at surface level, not at register level, which is precisely the failure mode the pipeline was built to catch. Regression seed RS-06. (Operational, 95% on the specific instance; Conjectural, 60% that no further undetected instances exist)

**OBS-GPT56-015** · Hashes, signatures, identity, and truth must remain distinct; a ceremonial artefact may be meaningful without being a security proof.
Disposition: **A**. Restates VRC discipline and the proof-qualifier rule. Adopted into the vocabulary check (protocol section 3). (Operational, 95%)

**OBS-GPT56-016** · Rights-aware corpus operation: default-deny third-party PDFs, retain licences, distinguish reference-only from ingestible, never convert projections into evidence.
Disposition: **A**. Protocol rules 8 and 9. (Operational, 95%)

### 1.5 Taxonomy and process proposals

**OBS-GPT56-017** · Adopt the thirteen-item claim-class list (observation, design principle, hypothesis, conjecture, conditional theorem, formal theorem, empirical result, implementation claim, ceremonial attestation, narrative, planned, historical, superseded).
Disposition: **M**. Rejected as a parallel taxonomy; the house already runs Operational, Architectural, Conjectural, Anticipated with percentages, and two label systems for one corpus is itself a drift generator. Amended to adopt the two genuinely missing items, `historical` and `superseded`, as artefact status flags. The proof-qualifier list is adopted in full. (Architectural, 85%)

**OBS-GPT56-018** · Run seven observer classes over the whole site; emit route manifests per observer; never label one route whole-site coverage.
Disposition: **D**. The single-route rule is accepted immediately (protocol section 4). The full multi-observer programme and any published route manifest are deferred: they interact with the intentional-discovery design and with the pending property-hosting decision, both Mitchell's calls. Filed as Anticipated, with **CTR-OBS-03** capturing the measurable version (route entropy, time to first coherent model, revision counts, source-authority mistakes) as a candidate research programme. (Anticipated, 75% that some reduced form ships alongside V6 era work)

**OBS-GPT56-019** · Measure the intended difficulty: discovery entropy, model revisions, false assumptions from historical repos, complementarity of routes.
Disposition: **M**. Merged into CTR-OBS-03 rather than run as a separate instruction. (Anticipated, 75%)

**OBS-GPT56-020** · Build a signed or content-addressed release manifest (framework version, conjecture head, grimoire versions, source commits, hashes, supersession links, rights ledger) as an internal substrate largely invisible to the experience.
Disposition: **M**. The need is accepted; the build is amended to extend existing canon rather than create parallel canon. The corpus already has the pattern: data/game-of-42.json as single source of truth, Grimoire v10.2.0 as canonical, the IPFS-pinned formal spec, content-addressed skill files. The release manifest becomes one more generated artefact from the same pipeline, answering the packet's eight questions (current release, conjecture head, supersession, projection source, claim class, deployed mechanisms, historical repos, ingestion rights). Never hand-edited on-page. Hosting property deferred to Section 5. (Architectural, 85%)

**OBS-GPT56-021** · Add route manifests and deliberate path invitations (path cards).
Disposition: **D**. Same gate as OBS-GPT56-018. The invitation list is retained as good copy candidates for whenever Mitchell rules. (Anticipated, 70%)

**OBS-GPT56-022** · Add subtle optional status affordances on public surfaces rather than compliance banners.
Disposition: **D**. Touches the two-register boundary and the experiential surface; Mitchell's call. The agent notes only that the *optional and subtle* framing is compatible with existing voice rules where a banner regime would not be. (Anticipated, 70%)

**OBS-GPT56-023** · Consolidate the Research OS around one run schema, immutable snapshots, proposer-challenger-gate separation, deterministic checks, negative-result retention.
Disposition: **A** in principle; scoped as consolidation of the existing scaffold (CLAUDE.md boot, GROUND_RULES.md, manifest.yaml, role cards, check scripts) rather than a new build. No new run schema is invented if manifest.yaml can be extended. (Architectural, 80%)

**OBS-GPT56-024** · Seed observer regression traps (old repo as current, projection as evidence, conditional-to-theorem promotion, hash as identity proof, ceremony as cryptographic proof, single route as coverage, mystery as version authority, drift dismissed as ambiguity).
Disposition: **A**. All eight adopted as regression seeds RS-01 through RS-08 for A9 and the check scripts. Two are already demonstrated live (RS-01 by this packet's own history; RS-06 by OBS-GPT56-014). (Operational, 90%)

**OBS-GPT56-025** · Harden public cryptographic behaviour: WebCrypto, no unencrypted secret storage by default, verify imported signatures, versioned schemas, exposed threat assumptions, mode labels (experimental, ceremonial, verified).
Disposition: **A** as a review checklist against the public experiences (Star, Sigil, forge, key export paths). No specific defect is confirmed by this pass; the observer asserts none, it prescribes defaults. Queued as an audit card, priority behind V6 formal work. (Operational as checklist, 90%; no claim about current defect status)

**OBS-GPT56-026** · Publish two research output tracks: architecture research, and observer/auto-research research, the latter treating the public ecosystem as an agent-evaluation environment.
Disposition: **M**. The second track is genuinely additive and is filed alongside the existing three-paper pipeline as a fourth candidate, not a replacement: the amnesia-gap, Moving Ceiling SoK, and RPP adversarial papers keep their slots. The observer-evaluation paper would draw directly on CTR-OBS-03 and this ledger as data. (Anticipated, 65%)

**OBS-GPT56-027** · The numerical scorecard (originality 9.5, formal precision 5, canonical machine coherence 4, and so on).
Disposition: **R** as canon input, retained verbatim in the observer ledger per protocol rule 7. One note without endorsement: the two lowest scores (formal-claim precision, canonical machine coherence) point at the same two CTR items this pass already opened, which is at least consistent. (Operational, 95% on the handling; the scores themselves carry no house confidence)

**OBS-GPT56-028** · Ten falsification hypotheses offered to the loop (dual-agent split as stable core, difficulty as epistemic design, harness centrality, drift beneath experience, proof-language class crossing, and so on).
Disposition: **A** as a standing challenge set. Current standings from this pass: dual-agent core, confirmed convergent; intentional difficulty, confirmed by owner declaration; drift beneath experience, partially confirmed at surface level (OBS-GPT56-014); proof-language crossing, plausible and now check-scripted; harness centrality, open pending internal comparison; consolidation over expansion as next step, accepted and enacted by this very ledger. Remaining hypotheses stay open with the packet as their source. (Mixed; per-item confidence recorded above)

## 2. CTR candidates filed

**CTR-OBS-01** · Exact joint-information decomposition for the dual-agent channel. State I(X;Y_S,Y_M) with the marginal redundancy and conditional-dependence terms explicit; prove the conditions under which the C_S + C_M numerator in R remains a valid upper bound; show the bound is conservative (tighter true ceiling) under conditional independence given X. Interaction with V6 R(t) and compositional leakage to be stated, since repeated interaction is exactly where marginal redundancy grows. Confidence that the ceiling survives strengthened: 85%. C-series assignment: Mitchell only.

**CTR-OBS-02** · Operational adversary model for R and R(t). Definitions required: private variable X, channel models per agent, side information, memory and composition across sessions, decoder class, error criterion, capacity units, and the Fano-style assumptions under which R < 1 implies a reconstruction-error floor. Deliverable: assumptions section of the V6 submission plus the falsification bounty conditions pointed at the weakest assumption. Confidence this lands inside the existing V6 scope without schedule damage: 80%.

**CTR-OBS-03** · Discovery as measurable epistemic design. Candidate metrics: time to first coherent model, model-revision count, source-authority error rate, route divergence and complementarity, reachable-corpus proportion per entry point, trap detection rate against RS-01 to RS-08. Status: Anticipated; blocked on Mitchell's route-manifest rulings. Confidence a publishable form exists: 70%.

## 3. Regression seeds filed

RS-01 old repository mistaken for current source (live precedent: this packet). RS-02 generated projection treated as independent evidence. RS-03 conditional result promoted to theorem. RS-04 hash treated as authorship or identity proof. RS-05 single route or single surface treated as whole-corpus coverage (live precedent: /model over-weighting). RS-06 stale surface contradicting live register (live precedents: ~C40 numbering; 96/64 skill surface). RS-07 ceremony treated as cryptographic proof. RS-08 real drift dismissed as intentional ambiguity, and its inverse, intentional ambiguity flagged as drift.

Each seed becomes a check-script case or an A9 audit card. RS-08 is the paired trap and matters most: it tests whether the auditor can hold the two-map distinction under pressure.

## 4. What this ledger deliberately does not do

It does not patch any formal register text (CTR items carry that forward under proof obligation). It does not rename, renumber, or promote any conjecture. It does not alter any public surface, essay, or experience route. It does not treat the observer's architecture reading as validation of the architecture. It does not expand the corpus; every accepted item lands inside existing scaffolding. Consolidation over expansion, as the packet itself recommends and as this pass enacts.

## 5. Ruling requests for Mitchell

1. **CTR-OBS-01 and CTR-OBS-02:** confirm filing, and rule whether either is a C-series candidate now or post-V6-draft.
2. **Release manifest hosting:** which property carries the generated release substrate; note the interaction with the pending INT-01 ceremony-route hosting decision, since one ruling could settle both.
3. **Route manifests and path cards (OBS-GPT56-018, -021):** publish, keep private, or hold. This is the intentional-discovery boundary and only you can price the trade.
4. **Status affordances (OBS-GPT56-022):** whether any status control appears on public surfaces, and if so which register's voice it speaks in.
5. **Skill-surface version patch (OBS-GPT56-014):** confirm the 96/64 correction to the V4-era root skill surface, and whether the patch waits for the next content-addressed skill release or ships alone.
6. **Fourth paper slot (OBS-GPT56-026):** whether the observer-evaluation paper enters the pipeline behind the existing three or waits for CTR-OBS-03 data.

---

*the outside eye sees the seam. the register decides the stitch. both entries stay in the book.*
