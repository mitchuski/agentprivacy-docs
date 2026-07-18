# κ-Addressed Holon Interoperability — Spec v1

**Status:** IMPLEMENTED (content edges) · SPEC (relational edges)
**Origin:** the dual-agent harness (`~/dual-agent-harness`, `HOLONS.md`, head on
`github.com/mitchuski/agentprivacy-harness`)
**Companion:** `specs/DUAL_AGENT_HARNESS_SPEC_v1.md` · `reference/vrc_promise_protocol_v3_3.md`
**Date:** 2026-07-12

## Purpose

Define the content-addressing convention by which a result the harness produces
becomes an **interoperable, independently verifiable unit** — a *holon* — that
any system in the corpus (the model instruments, the spellweb graph, a future
`hologram-technologies` site) can carry and re-derive without trusting its
source. One law, computed identically everywhere, is the interoperability
substrate.

## 1 · The κ-label

A **holon** is any object carrying a `κ` field:

```
κ = "sha256:" + sha256( canonicalJson( holon with the κ field removed ) )
```

- `canonicalJson` — JSON with recursively sorted keys and no whitespace.
- The κ field is **excluded from its own preimage**, so the object can carry its
  own address.

This is the City Key / sigil **Law L5**: *a κ-label is never trusted, only
re-derived.* Reference implementation: `tools/kappa.mjs` (`canonicalJson`,
`sha256Hex`, `kappaOf`, `verifyKappa`). Any consumer that vendors this one
function re-derives a holon minted anywhere byte-for-byte; two divergent
implementations do not catch each other, they break addressing, so there is
exactly one.

## 2 · What the harness mints as holons

- **`artefact.v1`** — a sealed result: run reference, per-proposal verdicts and
  Gap-seed re-derivations, a frontier beat, an `evidenceManifest`, and a `door`
  block naming the outward actions software did not take.
- **`runtime-feed.v1`** — a workshop's produced math (the moving ceiling R(t),
  the ℤ/64ℤ lattice). Self-addressing: `buildFeed` stamps its own κ, so a state
  snapshot is a verifiable holon.

*State is content-addressed:* the κ that seals a result at the door is the same
κ that addresses runtime state during a run.

## 3 · Edges

- **Content edge** — a hash reference to bytes (an `evidenceManifest` entry).
  Verified by **re-hashing**; needs no signature, because the content is its own
  witness. **IMPLEMENTED.**
- **Relational edge (VRC)** — a κ→κ reference between holons, governed by the
  edge rule: *a reference proposes an edge; a counterparty's signature mints it*
  (`vrc_promise_protocol_v3_3.md`). Verified by re-deriving both endpoints and
  checking the signature. **SPEC** until real signatures land.

## 4 · Verification is an auditor, not a harness

Every interoperability claim a holon makes is **enumerable**: does its κ
re-derive, do its content edges re-hash, do its relational endpoints resolve.
There is nothing to tune to — you cannot craft a holon whose κ re-derives to a
value it does not have. So the mesh verifier `tools/holon_audit.mjs` is a
deterministic, agent-free **auditor**, not a harness (harnesses are for
adversarial claim spaces too large to check; auditors are for enumerable facts —
the retired universe-builder is the corpus's record of that boundary).

> **The harness mints the holons; the auditor verifies the mesh.**

A holon's *substantive* claim ("40% smaller and still correct") remains the job
of the minting harness; only the *integrity of the mesh* is the auditor's.

## 5 · Reach

Because `kappa.mjs` and `holon_audit.mjs` live in the shared harness core and
operate on any instance directory, every runtime inherits κ-addressed state with
no per-instance code change:

```
node <harness>/tools/mint_artefact.mjs  <instance>  <run>
node <harness>/tools/holon_audit.mjs    <instance>/artefacts
```

lexon_pvm, shor_mage, privacy_pools_v2, and every future runtime become
content-addressed the moment they are run through the harness. A consuming site
(`hologram-technologies`) vendors this spec plus `kappa.mjs` and re-derives the
whole mesh; the corpus stays home, the κ travels.

## Interop map

| this spec's term | corpus cognate |
|---|---|
| κ-label / holon | `con-content-addressing` (spellweb); content-addressed liveness C93 (PVM V6); holonic memory `A_h(τ)` |
| relational edge / VRC | `vrc_promise_protocol_v3_3.md`; the edge rule (`universe/universe.json`) |
| auditor vs harness | `ADOPTION.md` step 0; the retired universe-builder |
| the door | T6 — outward actions are the First Person's |

```
(⚔️⊥⿻⊥🧙)😊 = neg ⊕ bnot → succ
```
