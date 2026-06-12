---
title: "Dual-Agent Harness — Framework Specification v1"
version: "1.0"
date: "2026-06-10"
author: "privacymage"
status: "working_paper"
license: "Apache-2.0"
register: "CONJECTURE_REGISTER_V6.md · head C89 (C82 moving ceiling, C83 non-collusion, C9 holographic, C67–C71 Horizon)"
framework_home: "C:/Users/mitch/agentprivacy-dual-agent-harness"
sibling_specs: "specs/DUAL_TERRITORY_CEREMONY_SPEC_v1.md"
---

# Dual-Agent Harness — Framework Specification v1

**A framework for building Swordsman ⚔️ ⊥ Mage 🧙 harnesses: interchangeable autoresearch
loops where a proposer (Mage, reduces) and a prover (Swordsman, validates) are held apart by a
held-out gate the proposer cannot tune to. One engine, many purposes, swappable crews — built
to be given to many ecosystems.**

> **Honest framing, carried into every instance.** A harness produces *validated* improvements to
> a stated objective; only the held-out gate makes a claim true. The first instance is quantum
> resource estimation — a durability signal, not an attack.

---

## 1. The architecture

The agentprivacy V6 master inscription **is** the architecture, proven on Z/64Z
(`privacy_value_v6_formal_specification.md`):

```
(⚔️ ⊥ ⿻ ⊥ 🧙) 😊  =  neg ⊕ bnot → succ            neg(bnot(x)) = succ(x)
```

- **⚔️ Swordsman = `neg` = the prover.** Signs/commits only what survives the full held-out gate.
- **🧙 Mage = `bnot` = the proposer.** Conceals/reduces; re-expresses paid work as free operations.
- **⿻ the Gap = the held-out gate.** The non-collusion precondition `I(Y_S;Y_M|X)=0` made real:
  the proposer cannot tune to the witnesses the prover will draw.
- **→ succ = the validated result.** It emerges *only* from the two held apart.

The ceiling the loop pushes against is `R(t) = (C_S(t) + C_M(t)) / H(X)` — two capacities, two
agents (C82, *Proven, conditional regime*; non-collusion the precondition, C83). **A proposer that
grades itself builds mirages**, so the Gap is the whole point, not an add-on.

## 2. The framework directory

`agentprivacy-dual-agent-harness/` (standalone; serves many ecosystems, so it is not owned by any
one of them):

```
core/dual_agent_loop.mjs   the generic engine: dualAgentHarness(config, rt). Never edited per harness.
core/SEAT_CONTRACT.md      what a harness config provides (the three seats, objective, schemas).
bindings/personas-and-skills.md   how to seat agentprivacy-skills personas + role-skills.
harnesses/ecdsafail-pqc/   instance #1 (config + provenance).
harnesses/_TEMPLATE/       copy to start a new harness.
SKILL.md · README.md · ECOSYSTEMS.md · LICENSE
```

A harness is a **config** passed to the engine with a runtime adapter `rt = {agent, parallel,
pipeline, phase, log}`. (The Claude Agent SDK / a node runner import the engine; the Workflow tool,
which has no `import`, runs a self-contained bundle — see `shor_mage/harness/swordsman_mage_pqc.mjs`.)

## 3. The seats and the complement pair

The config seats a **Mage** (proposer persona + reduction skills + finders), a **Swordsman**
(prover persona + `agentprivacy-horizon-gate` + domain skills), and a **Gap** (the held-out
mechanism). When the objective is a *product* of factors (cost × size), split the Mage into
**Factor-A-Min ⊥ Factor-B-Min** finders and let the Swordsman run a **cliff-watcher** on
`Δ(product)`. See `core/SEAT_CONTRACT.md` and `bindings/personas-and-skills.md`.

---

## 4. Integration map — how it links into the work

The framework references each ecosystem; it does not duplicate them (the link-out rule).

### 4.1 agentprivacy-docs (home of the law)
This spec lives here, beside `specs/DUAL_TERRITORY_CEREMONY_SPEC_v1.md`. The algebra and the
dual-agent law are in `privacy_value_v6_formal_specification.md` and `dualprivacy_researchpaper_v6.md`;
the conjectures are C82 (moving ceiling), C83 (non-collusion / compositional leakage), C9
(holographic sufficiency — the precompute lead), C67–C71 (the Horizon District / the first
instance's domain). When a surface and the register disagree, the register wins.

### 4.2 agentprivacy-skills (the crew)
The catalog of **8 swordsman / 7 mage / 7 balanced** personas + role skills is the source of seat
assignments. The operational method is the skill `meta/agentprivacy-dual-agent-harness` (the
plugin-registered **mirror** of the framework's `SKILL.md`); it composes
`role/agentprivacy-separation-enforcement` (the held-apart law, `det(Σ)≠0`) and
`meta/agentprivacy-horizon-gate` (the un-tuneable gate). Always-load: `persona/agentprivacy-architect`
(the harness designer — *"the system that trusts its agents to behave has already delegated
sovereignty to hope"*).

### 4.3 star — the Swordsman's Key + UOR (attestation & addressing)
**The deepest link: star already runs this algebra.** Its master figure is `(⚔️ ⊥ ⿻ ⊥ 🧙)` with the
same `neg`/`bnot` operators, and its pages sync over `BroadcastChannel('agentprivacy-succ')` — the
*succ*. star content-addresses artifacts by a **κ-label** `sha256:<hex>` (UOR; Law L5: *identity is
content, not location*), derived from canonical JSON (`star/index.html` → `canonicalJSON`,
`kappaLabel`; `HOLOSPACE.md`). Three integration points:

1. **Result attestation (Swordsman seat → Swordsman's Key).** When the Swordsman validates a result,
   it stamps the result object's κ-label (`kappaLabel(result)`) and may ed25519-sign the identity
   block (Phase 3, `CHRONICLE_SWORDSMAN_KEY_2026-05-27.md` §5). A validated harness output becomes a
   `{identity, trace, witness, kappa}` tuple — a verifiable City Key.
2. **UOR addressing of configs & outputs.** A harness config and its validated outputs are
   κ-addressed artifacts (same content ⇒ same κ), provisionable/resumable by κ with no registry
   (`HOLOSPACE.md` boot model; `.devcontainer/devcontainer.json`).
3. **Result lineage (the κ-chain).** Each result's `prior` field links the previous κ — a
   content-addressed chain of validated steps without a registry
   (`CONCEPT_COMPRESSION_REHYDRATION_DUAL_AGENTS.md` §4).

**Disposition:** the harness adopts the κ-label as the canonical name of a validated result; the
Swordsman seat is the natural holder of the Swordsman's Key. (star's Swordsman holds *no memory* —
identity + geometry + proof only — which is exactly the prover's posture.)

### 4.4 agentprivacy_master — the surface
The site presents the framework already: `/model` (V(π,t) + the C-register), `/guide/swordsman` and
`/guide/mage` (the archetype codices), and `/guide/agentic-deployments` (the Threshold District V59,
Staff Shop's alexandrite archetype-modal stone). Proposed surface (choose one to start):
- **(recommended)** a new route **`/guide/dual-agent`** — the prover ⊥ proposer ⊥ gate page, an
  export codex like `/guide/mage`, linking to `/model` and `/guide/agentic-deployments`
  (`src/app/guide/dual-agent/page.tsx`, add to `src/lib/nav.ts`).
- a §on `/model` — how V(π,t) gates in the dual-agent register (C58 Forge(t) ∥ Threshold).
- a subpage under `/guide/agentic-deployments` — the Threshold as the operational realization.

### 4.5 spellweb — the graph vocabulary
Schema in `src/types/graph.ts` (NodeType/EdgeType unions); data in `src/data/nodes.ts`,
`src/data/edges.ts`; visuals in `src/data/theme.ts`. spellweb already carries `con-dualagent`,
`con-gap`, the `proves` edge, persona/cast/skill nodes, and swordsman/mage `domain`s. Proposed
additions (matching the snake_case-verb convention):
- **NodeType** `harness` (one new type); seats as existing types — `seat-swordsman`/`seat-mage` as
  `cast`, `seat-gap` as `concept`.
- **EdgeTypes**: reuse `proves`; add `proposes` (Mage proposes) and `gates` (the held-apart Gap,
  dashed amber — separation). Node ids `harness-*`, `seat-*` per the `shop-*`/`cast-*` convention.
- One instance: `harness-ecdsafail-pqc` linked `built_on` the shor_mage kit + `proves`→a result node.

### 4.6 shor_mage — instance #1 (built)
The PQC kit holds the self-contained runnable bundle (`harness/swordsman_mage_pqc.mjs`) and the
toolchain the Gap uses (the GPU island toolkit; trailmix circuits). It stays PQC-only and links out
to this framework for the generic method.

---

## 5. Instance roadmap

| # | Instance | Objective | The Gap | Status |
|---|---|---|---|---|
| 1 | `ecdsafail-pqc` | cheapest reversible secp256k1 point-add (Toffoli × qubits) | Fiat-Shamir 9,024 | ✅ built |
| 2 | **`myterms`** | best `SD-BASE` agreement + spell constellation per page (PVM score) | unlock lattice + IEEE-7012 registry + constellation-hash witness | ✅ built (config + extension-runtime adapter + mock pass, §6); real-bus wiring pending |
| 3+ | future | ZKP-audit, gas/cost, … | a held-out gate the proposer can't game | ⬜ |

The abstraction only becomes honest at instance #2 — myterms is where the engine's seams get
pressure-tested, because it already has a real dual-agent split to seat against.

## 6. Scope — the myterms instance (the next build)

**myterms** implements IEEE 7012-2025 (machine-readable personal privacy terms) as the agreement
layer of the dual-agent architecture, with two browser extensions that are **already** a
proposer/prover split:

- **🧙 Mage = `mymage/`** (proposer/intelligence): deep-scans the page, rates six privacy
  dimensions, proposes a candidate **blade** (hexagram over `Z/(2⁶)Z`) + a spell constellation, and
  sends `INTELLIGENCE` / `CONSTELLATION_WAVE` to the Swordsman (`mymage/src/background/index.ts`).
- **⚔️ Swordsman = `myswordsman/`** (prover/enforcer): owns the canvas (the Mage cannot render —
  a hard held-apart boundary), records bilateral IEEE-7012 agreements, and gates forging with
  `checkCanForge()` (`myswordsman/src/content/blade-forge.ts`; `src/background/index.ts`). Its
  `src/lib/uor.ts` already verifies `neg(bnot(x)) = succ(x)` (`verifyCriticalIdentity`).
- Their handshake/sync is `myswordsman/src/content/ceremony-channel.ts` (`MAGE_PRESENT` /
  `SWORD_PRESENT` / `CONVERGENCE_READY`).

**What's missing to make it a harness:** the loop is single-round and heuristic, not a held-apart
autoresearch loop. The instance wires:
- **Objective:** maximise the PVM score `Φ = Φ_agent(Σ)·Φ_data(Δ)·Φ_inference(Γ)` of the chosen
  agreement + constellation, subject to user intent / low friction. (A product objective ⇒ a
  complement pair of Mage finders + a cliff-watcher.)
- **The Gap (held-out, un-tuneable by the Mage):** (a) the **unlock lattice** — the Mage proposes a
  blade, the Swordsman checks earned unlock (layer/forgings/domains); the Mage cannot lower it.
  (b) the **IEEE-7012 registry** — agreement IDs come from Customer Commons, the Mage cannot mint
  them. (c) the **constellation-hash witness chain** — cast spells must hash to the recorded
  hexagram (double-spend prevention). (d) **bilateral immutable recording** — auditor-disputable.
- **Seats:** Mage ← `agentprivacy-cipher`/`agentprivacy-weaver` + selective-disclosure skills;
  Swordsman ← `agentprivacy-sentinel`/`agentprivacy-gatekeeper` + `horizon-gate` +
  `separation-enforcement`; design ← `agentprivacy-architect`.
- **Integration points:** (1) `INTELLIGENCE` → blade proposal (threshold-gated); (2)
  `CONSTELLATION_WAVE` → witness-hash verification; (3) convergence → bilateral chronicle.
- **Result attestation:** validated agreements κ-addressed via the star Swordsman's Key (§4.3) —
  the bilateral chronicle entry as a κ-named, optionally signed City Key.

A `harnesses/myterms/` config will be added to the framework; the runnable form attaches to the
existing extension message bus rather than a Workflow bundle.

---

## 7. Coherence rules

1. **The engine is generic; never special-case a target in `core/`.** Targets live in `harnesses/`.
2. **Link out, don't duplicate.** V6 stays in agentprivacy-docs; personas in agentprivacy-skills;
   attestation in star; the PQC toolchain in shor_mage. This framework references them.
3. **Every harness declares its Gap.** A config without a real `heldApartRule` is rejected by review.
4. **Honest framing travels.** A harness produces validated improvements; only the Gate makes a
   claim true.

*Provenance: the framework `agentprivacy-dual-agent-harness/`; the V6 algebra
(`privacy_value_v6_formal_specification.md`); the first instance (`shor_mage/`); the attestation
substrate (`star/`); the next instance's existing agentic work (`myterms/`, `myswordsman/`,
`mymage/`).*
