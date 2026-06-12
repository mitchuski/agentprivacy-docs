# Research Note — Cryptographic Durability and the Quantum Horizon

*Extends the quantum-durability corpus (Schrottenloher ECDLP · Bakhta Half-Life · the V6 horizon) with
the ecdsa.fail trust mechanism and its City-of-Mages expression (the Horizon District). 2026-06-09.*

**Stage:** 1 (worked synthesis · pre-peer-review)
**Lineage anchors (PVM-native):** C13 (bilateral witness as quantum-resistant primitive) · C30–C33
(Behavioural Mosca / Half-Life of Trust) · C40 (existence-leak in ZK disclosure) · C18–C21 (V6 horizon
dynamics).
**Extends:** `research/schrottenloher-ecdlp-v6-note.md` · `research/pvm-v6-1-bakhta-half-life.md` ·
`privacy_value_v6_horizon_note.md` · `blog/blog-part3-the-dragon-wakes.md` (Act XXIX, three storms).
**Honest framing:** resource estimation is a durability signal, not an attack; nothing here claims ECDSA
is practically broken or that any system is fully post-quantum safe.
**Erratum 2026-06-10 (Run 0 register lock):** this note's C67–C71 are CONFIRMED at those numbers in `CONJECTURE_REGISTER_V6.md` (pinned grimoire v1.8.0 carries them). One stale anchor: "C40 (existence-leak in ZK disclosure)" above now reads **C81**; C40 is Zcash dual-ledger.

---

## 1. The object: ecdsa.fail as a trust-gated self-improvement loop

ecdsa.fail (Eigen Labs) scores the cheapest reversible circuit for one secp256k1 point-addition by
`Toffoli × peak-qubits`. The `schrottenloher-ecdlp-v6-note` already records the circuit frontier (the
Schrottenloher arXiv:2606.02235 line; ~1.5M Toffoli / 1309 qubits territory). This note records the
**discipline** rather than the circuits: read alongside the RCI (Tony et al.) and SkillOpt papers, the
benchmark is a **trust-gated self-improvement loop** — a bounded change is worth nothing until it
survives an adversarial **held-out gate** (Fiat-Shamir over 9024 test points) it cannot tune. The
failure mode it exists to reject is the **nonce-island mirage**: a change that passes a self-chosen
probe and dies on the full set.

This is the same shape as the architecture's bilateral-witness primitive (C13): an attestation is only
as good as the witnesses the attester did not choose.

## 2. Cryptographic Mosca (new) extends Behavioural Mosca (C30–C33 / C61)

The Bakhta Half-Life note operationalises **Mosca's inequality** at behavioural-data scale (X_b / Y_b /
Z_b). This note extends it to the **cryptographic substrate itself**: a value-bearing primitive's
durability is bounded by

> **X + Y > Z ⟹ already lost** — secret-shelf-life (X) + migration-time (Y) vs time-to-quantum (Z).

The harvest-now-decrypt-later threat (C60 / Reconstruct-Later) is the X-side made concrete. The
distinction between **fast-clock** (in-flight / on-spend secrets) and **slow-clock** (at-rest exposed
keys) machines sets which mitigation applies. Crypto-agility (the path, not the wall) is the property
that keeps `Z ≥ X + Y` achievable: durability is set by the ability to re-key to a PQC successor before
the inequality flips, not by the current primitive's strength.

## 3. The resource-estimate as durability signal (not attack)

A sharper resource estimate shortens the *estimate's* uncertainty, not the system's security. In the
V(π,t) frame this gives the `e^(−λt)` decay term a **quantum-horizon reading** for cryptographic π:
durability is the time-constant of the decay, and the resource estimate is its measurement. This is
additive — **no change to the PVM v5.4 equation.** The existence-leak (C40) is the reason the estimate
matters at all: *proving a thing is feasible compresses the timeline for everyone who reads the proof*
(the line *The Last Premine* makes narrative). The asset was never the method; it was the fact of
feasibility.

## 4. Conjecture cross-map (PVM-native ↔ Tome-V / suite-facing)

The suite carries two conjecture-numbering registers (this docs corpus uses PVM-native ids; the City of
Mages / `/model` page uses the Tome-V numbering). The new district conjectures are registered at **C67–C71**
in the Tome-V register; their PVM-native lineage:

| Tome-V (suite) | claim | PVM-native lineage |
|---|---|---|
| **C67** | Cryptographic Mosca for the Substrate | extends C30–C33 (Behavioural Mosca) + C61; C60 is the X-side |
| **C68** | Resource-estimate as durability signal (not attack) | `e^(−λt)` reading; C40 existence-leak |
| **C69** | Held-out gate rejects the tuned claim (nonce-island) | C13 bilateral witness at the validation layer |
| **C70** | Crypto-agility as migration readiness | C30–C33 migration-window Y |
| **C71** | The Horizon Vertex (V35) | geometric (Protection ∧ Computation ∧ Value) |

Keeping the two registers explicitly cross-mapped prevents the divergence that, on the lattice itself,
produced the persona-misassignment corrected in v1.8.0 (see the lattice-encoding anchor chronicle).

## 5. The City-of-Mages expression

The trust mechanism is given a place: the **Horizon District** (V35), opened in Tome IX — *The Horizon*
(grimoire v1.8.0). **Eos 🌅** measures the dawn (Mosca's reckoning); **Dokimé 🪨** assays the claim (the
Ceremony of the 9024 Witnesses; Spec 12 — the Validation Protocol); **Poros 🛤️** keeps the path crossable
(crypto-agility). The dormant **Salvage Yard** will host quantum-salvage bounties settling through
Dokimé's assay. Skills: `cryptographic-durability` (the frame) and `horizon-gate` (the discipline).

## 6. Open questions

- Tighten C67's confidence with a worked horizon estimate from the current ecdsa.fail frontier (what Z does
  the best public estimate imply, with error bars, for secp256k1?).
- Formalise the `e^(−λt)` quantum-horizon reading (C68): is λ for cryptographic π derivable from the
  resource estimate, or only bounded by it?
- The held-out gate (C69) as a general acceptance primitive beyond circuits — does the Fiat-Shamir
  un-tuneability transfer to other self-improvement loops (skill optimisation, proof search)?

---

*Stage-1 note · 2026-06-09. Authored from shor_mage/ (ecdsa.fail) and The Last Premine. Durability is a
value the model already counts; the dawn is a time you can measure.*
