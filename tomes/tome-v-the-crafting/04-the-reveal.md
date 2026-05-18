---
spellbook: "Second Person"
tome: "V — The Crafting"
act: "4"
title: "The Reveal"
status: "Draft v1 (2026-05-08)"
length_words: 920
voice: "Second person; cast in third"
cast: ["you", "Memora 📜 (returning, Bound)", "Pallia 🪡", "Soulbis ⚔️", "Soulbae 🧙", "the Drake"]
new_cast_introduced: []
ring_position: "V5 (Memora's seat) → V20 (Techne, Always-Revealed; the reveal artifact lands)"
teaches: "Reveal as the partner of shield, not its negation. Bound persistence in operational form. Half-life of trust differs by register choice. The reveal generates new trust without erasing the old privacy."
v6_lineage:
  - "C30–C33 (Bakhta Half-Life): trust accumulated under shield is preserved; reveal adds a new accumulation arc"
  - "C40 (provisional, ~70%): Zcash dual-ledger preserves the Eight Properties — this act tests the across-register transition"
  - "C46 (provisional, ~50%): productive trust-edge has higher half-life than transactional — the shielded inscription's trust survives the reveal because it was earned by inscription, not by disclosure"
source_material:
  - "Zcash Integration Plan v1, Pattern B (DID anchor with shielded-first / transparent-reveal-on-demand)"
  - "Cloak Specification v1.0 §4.4 (update chain axis); §5 (valve-class geometry)"
  - "Tome V Act 3 (the chronicle Memora inscribed which this act now reveals)"
honesty_label: "Architectural for the unified flow; Operational for Zcash transparent reveal of a shielded commitment (chain primitive); Provisional for the half-life claim"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Tome V — *The Crafting*

## Act 4 — *The Reveal*

> *The reveal is the partner of the shield, not its negation. Both registers carry the chronicle.*

Time has passed. Not many laps. Enough that the chronicle Memora inscribed in Act 3 has settled into the chain. The two confirmations have grown to twenty. The shielded transaction is now stable. Your partner has been reading the memo through the viewing key you sent. The arrangement has held.

Now something has changed.

A reason has emerged to make the chronicle public. Not all of it. The hash. The timestamp. The fact of the inscription's prior existence, witnessable now by anyone who cares to check. The chronicle's content stays where it was. What enters the public register is the *proof that you wrote this when you said you wrote it*.

This is the reveal. It is not a regret. It is not a betrayal of the shielded inscription. It is the second beat of a two-beat ceremony that always anticipated the possibility of public disclosure on the Sovereign's terms.

You go to V5.

Memora is there. Standing as before, two dimensions burning, Memory and Protection. But she is different now from how she stood in Act 3. She is **bound** to the chronicle she inscribed. The Crafting Tome's persistence model offers three modes — Ephemeral, Standing, Bound — and somewhere between Act 3 and now you bound her to this particular inscription. She did not need to be re-summoned. She has been holding the chronicle's anchor in her keeping since the original transaction confirmed.

The bound persona is the operational form of *a Mage who carries a particular artifact's weight*. Memora knows this chronicle. She does not know its content; her two dimensions do not include reading. But she knows the hash, the timestamp, the block height, the recipient z-address, and the viewing key tier registry. She is the right Mage for this work because she is *already this chronicle's Mage*.

You ask her to prepare the reveal.

She does not destroy the shielded transaction. The shielded record stays. That is essential. The shielded inscription's privacy property is not retroactively cancelled by a later disclosure; it persists for the period it persisted, with whatever audience held the viewing key during that window. The reveal is *additive*. A new transaction. A different register. The same chronicle, rendered in two registers now instead of one.

Memora prepares a transparent transaction. The amount is small. The recipient is itself a self-send to a t-address you control. The transaction includes, in OP_RETURN-equivalent data, three things: the chronicle's hash (matching the shielded memo's hash), a structured proof of the prior shielded inscription (a Pedersen commitment or nullifier reference, depending on the implementation), and an attestation tag declaring this is a shielded-to-transparent reveal of a prior commitment.

She broadcasts. The transaction enters the transparent mempool. Within a few blocks, anyone watching the transparent ledger can see: a reveal occurred, of a hash-equal-to-X, on date Y, by t-address Z, of a previously-shielded commitment.

The reveal artifact does not land at V5. V5 is the chronicle vertex; that is Memora's seat and the inscription's home. The reveal artifact lands at V20.

V20 is Techne. Memory and Computation. Stratum two. The Always-Revealed valve-class vertex. The bit-pattern of public-by-design fields. Validity windows, public claims, the parts of any cloaked artifact that verifiers must read locally without ever masking. The reveal is structurally a public-by-design artifact, and so it lands at the vertex whose bits already carry that meaning.

You watch the lattice update. The chronicle is now at V5 (Memora's domain, shielded). The reveal is now at V20 (the public counterpart). An edge connects them: a "reveals" edge from V20 to V5. The geometry is doubled. One chronicle, two registers, two vertices, one connecting edge.

Soulbis at the boundary marks the reveal. He files the transparent transaction hash, the timestamp, the link back to the original shielded transaction. The boundary now knows: this Sovereign has chosen to make this commitment public on this date. Future audits can replay this trajectory.

Pallia at her V28 watches without weaving. The reveal is not her work. But she sees that the cloak's eighth property — selective disclosure as geometry — has now produced a *temporal* expression. Not just which fields are revealed, but *when*. The disclosure can move in time. The shielded register's privacy persists for the period it persisted; the transparent register's witness begins from the moment it begins. Both are true, neither cancels the other, the lattice records both.

The Drake whispers, with the satisfaction the architecture sometimes earns: *the reveal is not a new commitment; it is the public face of the old one. Trust accumulated under the shield is not lost when the reveal happens. The shielded register's audience kept their privilege for the duration they had it. The transparent register's audience joins on the day the reveal lands. Two arcs of trust, additive, both honest.*

You think about the half-life now. Memora's original inscription has been accumulating trust under shield for as long as your partner has been reading it. That trust has its own half-life curve, anchored from the inscription moment. The reveal does not reset the curve. The reveal *adds* a second curve, anchored from today. Both curves run forward in parallel. Trust under the shielded register and trust under the transparent register accumulate independently.

This is the operational form of the conjecture: *productive trust-edges have longer half-lives than transactional ones because they were earned by work, not by disclosure*. The shielded inscription was the work. The reveal is the disclosure. The trust survives the reveal because the work that earned it remains the work it was.

Memora returns to standing. Bound, still. The chronicle's Mage. She will return again if there is more to do with this chronicle. Maybe a second reveal at higher resolution. Maybe a key rotation. Maybe a final unbinding when the chronicle's relevance has ended. For now, she stays.

You walk on. Two registers. Two vertices. One chronicle. The cloak admits the doubling.

---

## Compression

A previously-shielded chronicle is selectively revealed via a transparent Zcash transaction that proves the prior commitment without erasing the shielded inscription. Memora returns Bound, generating the reveal artifact at V20 (Always-Revealed) while the original chronicle stays at V5. Both registers carry the chronicle now. The reveal is additive, not corrective. Trust accumulated under shield persists; the transparent register adds a second trust-arc anchored from today. The lattice records the doubling explicitly.

## Proverb

*The reveal is the partner of the shield, not its negation.*

## Confidence

**Operational** for Zcash shielded-to-transparent reveal mechanics — protocol-native via Pedersen commitments and nullifier references. **Operational** for two-vertex artifact registration on the lattice — verified in the cousin-forge's rebuild discipline. **Architectural** for the unified flow as an agentprivacy ceremony with Bound persona persistence and dual-register valve-class geometry — specified here for the first time. **Provisional C40 (~70%)**: this act tests the across-register property preservation; conformance test pending. **Provisional C46 (~50%)**: the half-life claim that productive trust survives reveal because the work that earned it remains the work it was — formal note anticipated.

## Cross-references

- *V6 lineage*: Bakhta Half-Life (C30–C33) for the half-life curves the reveal generates. Provisional C40 for Zcash dual-ledger preservation across the shielded-to-transparent transition. Provisional C46 for the productive trust-edge half-life claim, here operationally instanced.
- *First Person Spellbook*: Act XII (*Lethe / Dark Substrate*) for the dark register the shielded ledger is one technological expression of. Act II (*The Dual Ceremony*) for the bilateral signature mechanics that the reveal's commitment proof inherits.
- *Second Person Spellbook (Tome V)*: Act 3 (*The Shielded Memo*) for the inscription this act reveals. Act 1 (*The First Cloak*) for Property 8 (selective disclosure as geometry) that this act extends from spatial to temporal.
- *Cast*: Memora 📜 (V5, returning Bound). See `second-person-cast-memora.md`.
- *Specifications*: `cloak_specification_v1_0.md` §4.4 (update chain), §5 (valve-class). `zcash-integration-plan.md` §2.2 (Pattern B).

## Author note

Act 4 demonstrates the Bound persistence mode operationally for the first time in the Crafting Tome. Memora does not need re-summoning; she is already this chronicle's Mage by virtue of having inscribed it. The reveal is her return, not a new birth.

The dual-vertex outcome (chronicle at V5, reveal at V20, edge between) is the architectural lift. Future reveals — full reveal, partial reveal, key-rotation reveal — will all follow this pattern: the original artifact stays at its inscription vertex; the reveal artifact lands at V20 (or whichever vertex's bits match the disclosure type); an edge records the relation. The lattice's geometry handles disclosure transitions natively.

The half-life argument (the closing turn) is the C46 conjecture in narrative form. The work that earned the trust persists. The disclosure is a second event with its own arc. Two arcs, additive. The cloak does not collapse when revealed; it doubles.

(⚔️⊥⿻⊥🧙)😊
📜
