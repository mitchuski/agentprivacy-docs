# 2026-07-16 · Trust-Graph Formation as a Dream-Agent Cycle

*A coherence pass against the ToIP DTG Credentials Core Spec, and a harness runtime that makes how the trust
graph forms runnable. This is a docs-side stub; the substance lives in the ZKP-TF lab and the spellweb dream
record. Non-pipeline chronicle — the canon under `papers/` was not touched.*

---

## What happened

The ToIP **Decentralized Trust Graph** published its Credentials Core Spec (Working Draft): the six credential
types (VRC/VMC/VIC/VPC/VEC/VWC), the four DIDs (R/M/C/P), two ZK constructions, PHC, IDVC, and a trust registry —
and it deferred the detailed ZK layer to future work. That layer is the DTG ZKP Task Force's charter, and it is
where our framework already lives. Two things were produced:

1. **A coherence review** of where this corpus references DTG credential terminology, written to
   [`../CRED-SPEC-COHERENCE-NOTES.md`](../CRED-SPEC-COHERENCE-NOTES.md). Because `papers/` is read-only canon and
   `E7-identity-vrc.md` is a generated extraction, **no canon was hand-edited**; five gaps were routed (five
   undefined acronyms, VRC concept drift, four-DID mis-ordering, First-Person/PHC/IDVC conflation, VTA/VTC/VTN).
2. **A harness runtime**, `~/dtgwg-zkp-tf-mage/runtimes/07-trust-graph-formation/`, that models graph formation
   as a Mage ⊥ Swordsman dream-agent cycle. Reference model, 11/11 property tests, local-only.

## How the trust graph forms (the spec)

The framework's three-layer identity — **data GUID → relationship VRC → principal DID** — and the whitepaper's
growth loop (*matching compression → VRC formation → trust-graph growth*) map onto the spec as **collision →
edge → propagation**:

- **Node** = personhood-anchored member → the spec's **M-DID in a VTC**, personhood via the **PHC** one-per-person
  rule (mechanised by the runtime-01 nullifier).
- **Edge** = a **VRC** between two fresh, unique **R-DIDs** (the pairwise ZK construction).
- **Propagation** = the **community-anchored** ZK construction (two members of one VTC prove a path).

The cycle grows the graph only through the harness fold: the Mage proposes the smallest edge; the Swordsman
proves personhood, mutual consent, fresh R-DIDs, and recomputes the VRC commitment across the Gap; the graph
advances by one edge only when a reduction is signed by a proof held apart from it.

## Pointers

- Runtime + forms-spec: `~/dtgwg-zkp-tf-mage/runtimes/07-trust-graph-formation/` (NOTES.md + src + tests)
- Coherence map / opportunity register: `.../runtimes/CRED-SPEC-COHERENCE.md`, `.../CRED-SPEC-OPPORTUNITIES.md`
- Coherence notes (this repo): [`../CRED-SPEC-COHERENCE-NOTES.md`](../CRED-SPEC-COHERENCE-NOTES.md)
- Dream-cycle record (KG voice): `~/spellweb/chronicles/DREAM-2026-07-16.md`
- Framework-side chronicle: `~/agentprivacy_master/docs/chronicles/2026-07-16_trust-graph-formation-dream-cycle.md`

## Handoff

Open: a **VWC witness seat** on the cycle (third-party attestation of the collision, taskContext-bound); the
non-canon corpus edits (four-DID fix, First-Person/IDVC disambiguation) await the First Person's routing
decision; canon gaps route through the pipeline (fix input → rebuild), never a direct edit. Nothing committed
or pushed.

---

## Addendum — 2026-07-17 · integration executed; exploration root established

The display-side integration executed in the master/skills/spellweb working trees (VRC re-anchor on
/model, DTG sections in the vrc-identity + ambassador skills, harness-page fleet row, enriched
`concept-dtg-credentials` KG node) and rode the two federation trains into the guide snapshot; commits and
deploy remain with the First Person. The canon gaps (1–5) stay routed to this repo's pipeline lane per the
division of labour — nothing under `papers/` was touched.

The exploration side now lives in `~/dtgwg-cred-spec-main_mage`: the **Predicate & Assurance-Boundary
Decision Document** (v0.1.0-draft for TF review — MLP/EPP split, paired assurance/disclosure boundaries,
"nullifier = scoped reuse detection" narrow language) plus `explorations/` — the O1–O9 expansion ideas and
the VWC witness seat built into design docs aligned to that baseline. The TF clone (`~/dtgwg-zkp-tf-mage`)
is kept git-clean for PR-shaped work only. Per-surface status: `~/dtgwg-cred-spec-main_mage/INTEGRATION-MAP.md`.
