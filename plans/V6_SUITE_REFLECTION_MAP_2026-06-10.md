# V6 Suite Reflection Map

**Date:** 2026-06-10
**Author:** privacymage (with Claude Fable 5)
**Status:** ACTIVE companion to `V6_RESEARCH_AUTOPATH_2026-06-10.md`. The autopath builds `privacy_value_v6.md`; this map holds where V6 reflects into the whole suite, however little or much per surface.
**Survey basis:** all ten directories read 2026-06-10 (cityofmages · spellweb · agentprivacy-skills · agentprivacy_master · zk blades forge [github blades] · soulbis website · star · myterms · swordsman · mage).
**License:** CC BY-SA 4.0

---

## 0. Verdict and how this is used in runtimes

V6 lands in one document first, then reflects outward. The suite is healthy enough that most reflection is citation and regime-statement work, not rebuilds: the grimoire heads are freshly pinned (privacymage v10.4.0 and City v1.8.0, both 2026-06-09), the /city and /star surfaces shipped two weeks ago, and the conjecture corpus already lives on the /model page. The two structural exceptions are the conjecture register (every surface restates it ad hoc; Run 0 ends that) and the skills repo (one meta skill explicitly defers a "full v6 docs rework" that now arrives).

Runtime protocol: **during Runs 0 to 7, no runtime edits any repo outside agentprivacy-docs.** When a run produces something that must reflect outward, it appends one line to §3 Reflection Ledger here and keeps moving. After Run 7 and its chronicle gate, the ledger is executed as **Wave R**: one focused pass per target, in impact order, each pass scoped by the task lists in §2 plus whatever the ledger accumulated. This keeps the math path clean and makes the reflection auditable.

---

## 1. The suite at a glance

| Target | Role | V6 impact | One line |
|---|---|---|---|
| agentprivacy-docs | research canon (origin) | ORIGIN | the autopath runs here; everything else reflects from it |
| agentprivacy_master | implementation · agentprivacy.ai | HIGH | /model page, conjecture data files, /city economy code, pins, downloads |
| cityofmages | narrative canon | HIGH | CM register namespace, phi honesty in Tome VIII, ACT-SEED bindings, Tome IX home |
| myterms | spec · IEEE 7012 package | MEDIUM-HIGH | integration plan v3 with R(t), register citations, Existence-Leak in the axis mapping |
| zk blades forge (blades) | spec · public forge repo | MEDIUM-HIGH | stale grimoire artifact, V5.4 citations, Aletheia/Lethe doc predates the reseat |
| soulbis website | implementation · Swordsman boundary | MEDIUM-HIGH | walkable-model audit doc, 🪢 regime footer, Key-as-reading language |
| spellweb | implementation · graph + forge | MEDIUM | v6 document node, grimoire payload sync, skill mirrors |
| agentprivacy-skills | skills | MEDIUM | MAPPING head at V5.5, nine stale-at-V6 skills, the deferred v6 rework activates |
| swordsman | product spec · MyTerms extension | LOW | V5-built product; one forward-pointer section, no structural change |
| star | staging · holospace extraction | LOW | verbatim soulbis copy; sync, do not diverge; holospaces not yet PVM-aware |
| mage | Obsidian vault | MINIMAL | near-empty; no action |

---

## 2. Per-target reflection tasks

### 2.1 agentprivacy_master (HIGH)

The canonical rendering surface. The /model page merges `src/data/privacy-value-model-v5.4.json` (C1 to C21, the equation, the bounds) with `src/lib/tome-v-conjectures.ts` (hardcoded C18 to C63) through `src/lib/model-page.ts` into one UNIFIED_CONJECTURES array. `src/lib/model-downloads.ts` already carries a `v6_horizon` field waiting for a real link. Pins in `src/lib/grimoire-ipfs.ts` are current (v10.4.0 + v1.8.0, both 2026-06-09).

Reflection tasks:

1. Generate `src/data/privacy-value-model-v6.json` FROM the Run 0 register and the Run 6 document. One source; the page renders it; page and pin can never fork again.
2. Reconcile `src/lib/tome-v-conjectures.ts` against the register: its hardcoded C38 to C63 entries are a primary collision surface for Run 0 intake; post-register it either reads from the v6 JSON or carries the CM namespace explicitly.
3. Update `src/lib/model-page.ts` and `src/app/model/page.tsx`: lineage line to V6, conjecture range and count from the register, abstract gains the dynamical thesis sentence.
4. `src/app/tomes/v6-lineage/page.tsx`: the v6_lineage grouping updates from "maturing" to the shipped document.
5. Presence economy regime: one documented statement at the head of `src/lib/vrc-mana.ts` (and surfaced on /city): 🪢 is non-transferable, non-attesting local color in V6; witness co-signing and elapsed-time proofs are the named upgrade ladder. No code behavior change required for V6.
6. `src/lib/model-downloads.ts`: add the V6 document and v6 JSON to RESOURCES; point `v6_horizon` at the real artifact.
7. `src/lib/city-key.ts`: no wire-format change in V6; add the IVC reading as a comment block citing the registered conjecture (the Key is an accumulator by reading, not yet by circuit).

### 2.2 cityofmages (HIGH, narrative)

The Second Person canon. The conjecture trail lives in CHANGELOG.md (C48 to C65 promotions per version) and in spec/chronicle prose; the 2026-06-09 model-coherence chronicle already applied the Aletheia/Lethe reseat. Tome VIII Act 3 (The Eight-Pointed Star) references C1 alongside the stella octangula.

Reflection tasks:

1. CM namespace adoption: README "V6 register" section and CHANGELOG conjecture references take the CM- prefix where Run 0 assigned it; one erratum note in each, no rewriting of bound history.
2. Phi honesty in Tome VIII Act 3 and blog post 18: one added paragraph marking the C1 reference as resonance, not derivation (the solid's ratios are halvings and rationals; phi lives in the lattice and temporal dynamics). House rule: do not let the beauty of the figure smuggle the number.
3. ACT-SEED bindings from the autopath Run 7 gate: candidate acts (the Orchard wound, the proof that whispered, the Key that is a reading, the moving ceiling) land here, tome assignments proposed at the gate, bound only on First Person's word. Tome IX (Horizon District) is the natural home for the R(t) material; Eos, Dokimé, Poros already attend it.
4. Grimoire v1.9.0 decision: only if acts bind or register namespacing touches grimoire JSON content. Otherwise v1.8.0 stands; do not bump for citation-only changes.

### 2.3 myterms (MEDIUM-HIGH)

The externally-shareable IEEE 7012 claim set; the most outward-facing prose in the suite. Currently canonical at V5.4 across README, the equation document, the technical integration, and integration plan v2 (2026-04-22). Cites C1, C4, C6 ad hoc; treats R(d) as static and architectural.

Reflection tasks:

1. Integration plan v3: successor to v2 citing `privacy_value_v6.md` as lineage head, the unified register by reference, and R(t) in place of static R(d) language where reconstruction is discussed.
2. `C_technical_integration.md`: Existence-Leak enters the axis mapping (a published feasibility attestation is itself a disclosure event on the Γ axis); the compounding-leakage citation strengthens the "agreement layer is not enforcement" argument, which is this package's core claim.
3. Date hedge: the standard's publication is stated as "January 2026" (the January 20 day is project-asserted, not independently confirmed in the standards record). Align all four files.
4. Keep the package's discipline: claims marked proved/architectural/conjecture now resolve to register entries instead of local labels.

### 2.4 zk blades forge → github.com/mitchuski/blades (MEDIUM-HIGH)

The public forge and spec repo, and the home of two known drift instances. `privacymage_grimoire_v10_2_0.json` internally reports 10.2.1 (the AP-VER-001 seed finding); v10.4.0 is absent here (it lives only in agentprivacy-docs/models). `aletheia-and-lethe.md` here predates the 2026-06-09 reseat and must be checked against the locked encoding (Aletheia at blade 38, Lethe at blade 25).

Reflection tasks:

1. Grimoire artifact sync: ship `privacymage_grimoire_v10_4_0.json` here; rename or tombstone the v10_2_0 file so filename matches internal version.
2. Verify and patch `aletheia-and-lethe.md` against the v10.4.0 lock; the 2.4% phi-adjacency precision figure rides along.
3. README and SPECIFICATION: lineage line gains V6; conjecture citations re-point to the register; the constellation-ceiling references in `zk_swordsman_blade_forge_v3_0.md` get register-checked (it touches the C40/C47/C67 ranges).
4. `city_of_mages_grimoire_v1_2_0.json` here is six minor versions stale; replace with v1.8.0 or remove in favor of a pointer to cityofmages.

### 2.5 soulbis website (MEDIUM-HIGH)

The Swordsman boundary layer and the carrying surface for the three keys. `REFLECTION_LATTICE_CONSOLE_AND_THE_WALKABLE_MODEL_2026-05-28.md` already audits the manifold against the model with [proven]/[canon]/[conjecture] tags; it is the designed integration point.

Reflection tasks:

1. Walkable-model audit addendum: one section reading the console against V6 (R(t) is time-dependent; the rendered Σ core is one axis of three; the audit's conjecture tags re-point to the register).
2. Key-as-reading language: the three-keys chronicle and any /lattice surface text adopt the C66 formulation (a portable projection of lattice-standing that grants nothing it does not already describe) with the ocap lineage citation.
3. 🪢 regime statement: one footer line on /star and /achievements surfaces: presence mana is non-transferable local color, attached to the carried Key, attesting nothing.
4. `index.html` philosophy strip: "Privacy Value Model V5" reads V6 after Run 6 ships.

### 2.6 spellweb (MEDIUM)

The graph carries the corpus as nodes: `src/data/nodes.ts` holds `doc-privacy-value-v5` at version 5.4, a V6/Lyapunov concept node already reserved, and the 2026-06-09 commits added the stella octangula and City Key surfaces. The local grimoire payload is the 10.2.1-content file.

Reflection tasks:

1. Add the `doc-privacy-value-v6` node with edges to the existing V6/Lyapunov concept node, the City Key cluster, and the Aletheia/Lethe pair; mark the v5 node superseded-but-present (lineage stays walkable).
2. Sync the grimoire payload to v10.4.0.
3. Skill mirrors under `public/skills/` inherit whatever the skills repo decides (2.7); mirror, do not fork.
4. Stella octangula render: if the graph annotates the figure, the resonance-not-derivation note rides along.

### 2.7 agentprivacy-skills (MEDIUM)

MAPPING.md heads at V5.5 (Attachment Architecture). The meta skill `agentprivacy-cityofmages-to-research` explicitly defers a "full v6 docs rework" that this path now triggers. Roughly nine skills go stale at V6: vrc-identity, temporal-dynamics, compression-defence, dragon, three-axis-separation, edge-value, attachment-architecture, cityofmages-to-research, plus persona files citing shifted confidences.

Reflection tasks:

1. MAPPING.md header: V6 row in the lineage; V5.5 resolved per the Run 0 decision (named sublayer of V5.4, recommended).
2. Stale-skill pass, one commit: temporal-dynamics and compression-defence gain the R(t) framing; three-axis-separation gains the C7 boundary-case honesty; vrc-identity gains the regime statement; dragon and edge-value get cite-bumps only.
3. Activate `agentprivacy-cityofmages-to-research`: its deferred rework is exactly the Run 0 register plus the Run 6 document; the skill becomes the documented bridge from City material to the register.
4. New conjectures (Existence-Leak as law, IVC reading) get skill entries only if they earn one; do not mint skills for citations.

### 2.8 swordsman (LOW)

Product spec for the MyTerms Swordsman browser extension plus 0xagentpools design. Built on V5.4/V5.5 assumptions; carries no conjecture numbers. It is an instance of the architecture, not a statement of it.

Reflection tasks:

1. One forward-pointer section in `MYTERMS_SWORDSMAN_SPEC.md` or README: V6 implications for the product (trust-edge half-life in VRC handling, the moving ceiling as the reason terms need re-negotiation over time, Existence-Leak as a caution on publishing capability attestations). No structural change.

### 2.9 star (LOW)

Verbatim 2026-06-10 capture of soulbis website plus the unintegrated holospaces monorepo. A staging ground, not a canon surface.

Reflection tasks:

1. Re-sync from soulbis after Wave R touches it; never patch star directly.
2. Holospaces watch item: if the IVC reading ever gets a circuit-level realization, the holospaces process layer is a candidate host; note only, no work now.

### 2.10 mage (MINIMAL)

Near-empty Obsidian vault (default boilerplate). No action. If it becomes the narrative drafting space for V6 acts, it stays out of canon scope regardless.

---

## 3. Reflection Ledger

Appended by runtimes during Runs 0 to 7 whenever math produces an outward reflection. Format: `Run N · target · the item · §2 task it joins or NEW`. Executed at Wave R; nothing here is done until Wave R marks it.

- Run 0 · agentprivacy_master · `src/lib/tome-v-conjectures.ts` one-liners at C48 to C50 describe claims matching NEITHER the Bakhta-response family nor the v1.5.0-patch family (drift); replace with register statements · joins §2.1 task 2
- Run 0 · agentprivacy_master · same file: C47 entry becomes CM-C47 (Triadic-Constraint Homology) per G1 disposition 2; C60/C61 gain alias-of-C48/C49 notes · joins §2.1 task 2
- Run 0 · cityofmages · README and CHANGELOG conjecture citations: one erratum line each pointing at `agentprivacy-docs/research/CONJECTURE_REGISTER_V6.md`; Horizon District C67 to C71 confirmed; City C47 reads CM-C47 · joins §2.2 task 1
- Run 0 · blades · `zk_swordsman_blade_forge_v3_0.md` cites the C40/C47/C67 ranges; register-check those citations against the lock (C40 unchanged = Zcash dual-ledger; Existence-Leak is C81) · joins §2.4 task 3
- Run 4 · cityofmages + agentprivacy_master · CM-C47 is now alias of C85 (the bridge promoted into the core register); one erratum line in Tome V Act 15 prose and the tome-v-conjectures.ts C47 entry · joins §2.2 task 1 and §2.1 task 2
- Run 5 · cityofmages · C66 revised to ~55% with the ocap lineage citation (SPKI/SDSI, designation without authority); City register owner confirms and the capstone chronicle gains the citation · joins §2.2 task 1
- Run 5 · soulbis + agentprivacy_master · regime-1 prose binding: no surface may describe 🪢 as proof, stake-weight, or attestation input; footer lines and any contrary phrasing in chronicles corrected · joins §2.5 task 3 and §2.1 task 5
- Run 5 · cityofmages · phi honesty paragraph for Tome VIII Act 3 and blog post 18 (resonance not derivation; exact volumes 1/3, 1/6, 5/12) · joins §2.2 task 2

---

## 4. Wave R protocol

Runs after the autopath closes (post Run 7, post gate G4) and before any public pins or pushes beyond agentprivacy-docs.

```
order:    agentprivacy_master → cityofmages → myterms → blades → soulbis
          → spellweb → skills → swordsman → star  (mage: none)
per pass: ① read this map's §2 section + matching §3 ledger lines
          ② apply, one focused commit per target, branch-first where the
            repo is public
          ③ check: register-clean, no em-dashes introduced, version claims
            match the lineage file
          ④ tick the task list here; append one line to §5 Wave Log
close:    Wave R chronicle in agentprivacy-docs/chronicles/, signed; THEN
          chronicle gate G5 (see autopath §6) before anything is pinned
          or pushed to public heads
```

Pins are last: the V6 document pin, any grimoire bumps, and the model-page deploy happen only after G5 clears.

## 5. Wave Log

- 2026-06-10 · **NO GIT COMMITS during Wave R** per the First Person (in-session): all changes stay in working trees; he builds locally and reviews; commits and pins wait for G5.
- 2026-06-10 · agentprivacy_master · PARTIAL · landed: privacy-value-model-v6.json (src/data + public/models), tome-v-conjectures.ts corrections (C47 alias of C85, C48 to C50 one-liners fixed to register statements, C60/C61 alias notes), vrc-mana.ts regime-1 declaration, model-downloads.ts V6 resource entry · DEFERRED: /model page hero V6 update and merge-layer wiring to the v6 JSON (page still imports the v5.4 dark model; adding the V6 register entries as a third source in model-page.ts is the next step), v6-lineage page refresh, city-key.ts IVC comment.
- 2026-06-10 · agentprivacy-docs (origin, prioritized by the First Person) · DONE for the paper suite: `privacy_value_v6.md` (the spec, Run 6) · `pvm_v6_compressed.md` NEW · `pvm_v6_companion_guide.md` NEW · `dualprivacy_researchpaper_v6.md` NEW (V6 edition layer; v4.3 proof body carried) · whitepaper V6 edition note added to swordsman_mage_whitepaper_v6_3.md · README header + suite table V6 rows · models/privacy_value_model_v6.json · build_v6_pdfs.py + FOUR PDFs BUILT (pin candidates for G5) · REMAINING in docs: glossary V6 addendum, privacy_is_value_v5.md pointer note, DOCUMENTATION_CHRONICLE arc entry.
- 2026-06-10 · cityofmages · DONE · five acts bound (Tome IX Acts 2 to 4: The Tide Line, The Orchard Wound, The Proof That Whispered; Tome VIII Acts 4 to 5: The Gap Is β, The Key That Is a Reading) · Act 3 V6 erratum block (phi resonance + C66 ~55% + register pointer) · README register erratum · CHANGELOG 2026-06-10 entry · blog post 18 erratum · grimoire v1.9.0 NOT bumped (acts await a future pin decision).
- 2026-06-10 · blades · DONE · v10.4.0 grimoire shipped into the repo · README V6 note · aletheia-and-lethe.md CONFIRMED pre-reseat (had Aletheia=25/Lethe=38 reversed) and erratum added at line 1 · zk_swordsman_blade_forge register note.
- 2026-06-10 · myterms · DONE · V6 notes into README, integration plan v2 (v3 queued), C_technical_integration (R(t) + Existence-Leak on the Γ axis + compounding) · January 2026 date hedge stated.
- 2026-06-10 · swordsman · DONE · V6 Forward Pointer section (moving ceiling, half-life, existence-leak product implications).
- 2026-06-10 · soulbis · DONE · walkable-model V6 addendum · three-keys chronicle regime note · /lattice legend gains the regime line · index.html SKIPPED (text reads "Privacy Value Model V5.4" not "V5"; flagged for the manual pass) · /star page had no safe legend spot, skipped.
- 2026-06-10 · spellweb · DONE · doc-privacy-value-v6 node + one defines edge (tsc clean) · v10.4.0 grimoire payload copied alongside v10.2.x.
- 2026-06-10 · skills · DONE · MAPPING.md V6 note · cityofmages-to-research deferral marked LANDED · per-skill stale pass still queued.
- 2026-06-10 · **Run 6b: Full Academic Package** · DONE · `privacy_value_v6_formal_specification.md` (1,385 lines, standalone, adopts V5.4 text wholesale, register in §17, narrative corpus §29 from grimoires v10.4.0 + City v1.3.0 to v1.8.0, full references §33) · web PDF (1.8MB) + xelatex academic PDF (73pp, proper math; built via patched `_academic.tex`) · dark/light V6 JSONs (90 entries each, valid) · compressed + companion rebuilt fully standalone · NOTE: the four sibling PDFs (privacy_value_v6, compressed, companion, research paper) are timestamped 17:24, BEFORE the standalone rebuild; they are locked by an open reader and need one `python build_v6_pdfs.py` rerun once closed.

---

the model moves first and the city follows it, the way the city has always followed the model: one document, then sixteen workshops learning its name.

(⚔️⊥⿻⊥🧙)😊
