# Research Note — The Circuit Workshop: a trust-gated optimization loop, run to closure

*Records the completed research cycle of the tigzkp_mage circuit workshop (2026-07-03 → 07-09):
a seven-seat persona-fleet that optimized a real ZK circuit under adversarial verification
discipline, closed its entire lever space with proof-grade results, and issued a closure
certificate. Second corpus instance of the trust-gated self-improvement loop (after ecdsa.fail).
2026-07-09.*

**Stage:** 1 (worked synthesis · pre-peer-review)
**Lineage anchors (PVM-native):** C13 (bilateral witness — an attestation is only as good as the
witnesses the attester did not choose) · the negative-results ledger tradition (shor_mage →
tigzkp_mage) · the Game of 42 compute-axis heptad (seat registry + conform gate).
**Extends:** `research/2026-06-09_horizon_district_cryptographic_durability_note.md` (§1, the
trust-gated self-improvement loop) · the TIG letter lineage (letter 1: lattice-structure
conjecture; letter 2: gated, sharing is the First Person's).
**Honest framing:** this note records the *discipline and its outcomes at claim level*, not the
mechanisms. Specific levers, constraint counts, tier structure, and submission strategy are
deliberately withheld — they constitute an open competitive edge (the TIG challenge is a proposal,
not yet live) and live in the private provenance repo. Research agents needing the full ledger
request access through the First Person.

---

## 1. The object: a research runtime, not a result

The tigzkp_mage workshop ran five rounds of Swordsman ⊥ Mage autoresearch against a Poseidon-heavy
privacy-pool withdraw circuit, working **blind** — from the compiled R1CS artifact alone, no source,
no symbol table — on the TIG "Accelerating Witness Generation through Circuit Optimization"
problem shape (CEL Team proposal). Seven seats on the Game-of-42 compute-axis pattern: Measure →
Propose (two lenses, held apart) → Hold-apart → Assay → Critic → Chronicle, with a keystone that
alone writes the ledgers and a door (commit / publish / contact) that belongs to the First Person
alone.

The cycle **closed**. Not "ran out" — closed: every candidate lever family was either validated
and folded, or killed with a certificate stating *why it can never work*, and the final round
issued a closure certificate over the last open family. The frontier moved materially past the
reference optimizer class along the way, and the ending state carries exactly one open item — a
protocol-admissibility question that gates which of two final numbers is the submission number,
answerable only when the challenge goes live.

## 2. The same shape as ecdsa.fail — and it caught the same failure mode

The durability note (2026-06-09 §1) records ecdsa.fail's discipline: a bounded change is worth
nothing until it survives an adversarial **held-out gate** it cannot tune, and the failure mode
the gate exists to reject is the **nonce-island mirage** — a change that passes a self-chosen
probe and dies on the full set.

The workshop is the same architecture, and it earned the vocabulary: its Assay verdicts are
literally `VALIDATED / MIRAGE / BLOCKED`. The machinery:

- **Fiat-Shamir seed separation (the Gap seat).** Verification points derive from a hash of the
  proposal artifact itself; the proposer is structurally blind to them and forbidden from
  suggesting any. C13 in mechanical form: witnesses the attester did not choose.
- **Certificates over trust.** Every rewrite ships with independently re-runnable evidence:
  held-out equivalence at dozens of points, per-rewrite syntactic certificates, and a symbolic
  witness-computability proof. One assay found its own prior verdict on disk from an interrupted
  run — and refused to trust it, re-executing every decision-bearing number.
- **Checkers proven non-vacuous.** A verification pass that reports success on zero items is
  suspect; the workshop unit-tested its certificate checkers against deliberately corrupted
  inputs before accepting their PASS.
- **Pre-registered verdict rules.** Probes declared their success/failure branches *before*
  running. Twice, a probe's honest answer was "the instrument I pre-registered cannot decide
  this" — filed as such, never softened into a win.

Across the cycle the gate rejected multiple confident proposals whose mechanisms were sound but
whose yields were mirages, including one where the load-bearing claim fired zero times in over a
hundred opportunities. The gate held every time. That is the note-worthy result.

## 3. What the cycle proved about research epistemics (transferable, no edge)

Five standing lessons, each paid for with a concrete reversal recorded at win-prominence:

1. **Floor claims need closure certificates, not censuses of known families.** A "practical floor"
   was certified from a census of every known lever family — and falsified within hours by a
   family the census had no row for. The certificate that finally held (final round) was earned
   the hard way: exhaustive per-item rule-firing, a forward-derived counting model confirmed at
   three independent parameter points with zero contact with the target artifact, and an
   emptiness census over the last unmeasured shape.
2. **Wrong-direction proxies are silent killers.** A family was priced "likely ~0" using a
   measurement that answers the converse question. Measured properly, it was the largest single
   move of the cycle. Computable-from is not the same as consumed-by; reachable is not the same
   as needed.
3. **A gated ceiling is not a ceiling until the gate is priced.** A lever priced at a large yield
   died at zero because its final expressibility gate — unpriced at proposal time — rejected
   every candidate. The inverse error also occurred (a ~0 pricing that cascaded far past its
   nominal bound). Single-shot mass bounds do not survive cascades, in either direction.
4. **Negative results at win-prominence compound.** The killed-levers ledger (seven entries, each
   with its dying evidence) is what made the final closure certificate *possible*: closure is a
   statement over the whole space, and only filed kills make the space enumerable.
5. **The method dominated the model.** The cycle spanned a frontier-model transition mid-flight
   (seat provenance recorded per round). Both models reproduced every ledger number to the digit;
   the discipline — seeds, certificates, pre-registration, keystone-only ledgers — carried the
   quality, not the engine. One late-cycle observation worth keeping: the sharpest single result
   of the cycle came from a seat that looked where the census said nothing lived.

## 4. Where it goes

The workshop's method — the two-tier certified optimizer, the seed discipline, the certificate
apparatus, the kill-catalog for this circuit class — transfers next to a **production privacy-pool
circuit suite** (successor generation of the calibration circuit's own family; a preliminary
blind measurement already shows a material certified reduction is available on the shipped
artifacts). That work opens from a handoff document in the provenance repo; its outward face —
any contact, report, or disclosure — remains gated at the door.

Provenance: private repo `zk_mage` (full ledgers: frontier, claims register CR-1..CR-16, killed
levers K-1..K-7, forty-plus chronicles, and the run evidence the ledgers cite). The second TIG
letter remains behind gate 001. This note is the public-safe projection of that record.

## 5. Conjecture-shaped residue (for the register, if adopted)

- **Cx-a (workshop epistemics):** *In adversarially-gated optimization loops, the expected value
  of a research round is dominated by the certificate class it produces (validation, kill, or
  closure), not by its frontier delta.* Evidence: the cycle's two most consequential rounds moved
  the frontier by zero.
- **Cx-b (proxy inversion):** *Any pricing derived from a proxy measuring the converse relation
  (computable-from vs consumed-by; reachable vs needed) should be treated as unpriced.* Evidence:
  both directions of mispricing observed in one cycle, magnitudes 4× and ∞ (finite→0).
- **Cx-c (continuation of the C13 line):** *Held-out gates compose: seed-separation at the
  proposal layer plus certificate non-vacuity at the checker layer catches failure modes either
  alone admits.* Evidence: the mirage class that passed all point-equivalence checks and was
  caught only by the (certificate ∧ frontier-beat) conjunction.
