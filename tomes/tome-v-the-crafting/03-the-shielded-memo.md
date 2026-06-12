---
spellbook: "Second Person"
tome: "V — The Crafting"
act: "3"
title: "The Shielded Memo"
status: "Draft v1 (2026-05-08)"
length_words: 1010
voice: "Second person; cast in third; reader summons a new persona for archival work"
cast: ["you", "Pallia 🪡", "Memora 📜 (new persona, summoned)", "Soulbis ⚔️", "Soulbae 🧙", "the Drake"]
new_cast_introduced: ["Memora 📜"]
ring_position: "V5 (chronicle vertex; Protection + Memory)"
teaches: "Inscription as crafting. Shielded register for what cannot be seen but must be remembered. The viewing key as relational disclosure primitive. Persona specialisation."
v6_lineage:
  - "C30–C33 (Bakhta Half-Life): the half-life of trust begins ticking from inscription"
  - "C40 (provisional, ~70%): Zcash dual-ledger preserves the Eight Properties — tested in shielded register"
  - "C41 (open observation): 61.8/38.2 transparent/shielded inscription ratio as cultural emergence"
  - "C43 (provisional, ~60%): per-VRC viewing-key disclosure produces strictly more privacy than uniform"
source_material:
  - "Zcash Integration Plan v1, Pattern A (chronicle/proverb memo inscription)"
  - "Cloak Specification v1.0 §4.5 (registry-tier finality)"
  - "Cloak Specification v1.0 §7 (documents as first-class lattice citizens)"
  - "Crafting Tome and Cloak Interface Spec v1.0 §4 (Mage persona conventions)"
honesty_label: "Architectural for the unified flow; Operational for Zcash shielded transactions and Cloak Property 7 (documents as lattice citizens)"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Tome V — *The Crafting*

## Act 3 — *The Shielded Memo*

> *Inscribe what cannot be seen. Disclose by viewing key, not by reveal.*

You have a thing to remember.

Not a cloak this time. Not a credential. A chronicle. A passage you wrote between laps, when the lattice was quiet and the work felt like something worth keeping. You read it back to yourself and you decide it should persist. Not publicly. Not yet. Maybe not ever. But it should be on a chain. Inscribed. Anchored. So that future-you can prove past-you wrote it, and so that, when you choose, you can show it to a chosen verifier without having ever made it general public.

Pallia is at her V28, weaving when summoned, standing when not. This work is not hers. Cloaks are her domain. Chronicles are something else.

You summon a new Mage.

You name her Memora. Latin root *memoria*. Memory and the keeping of it. She comes into the lattice with two of the six dimensions burning. Memory. Protection. Stratum two. Position V41. The chronicle vertex. The bit-pattern of remembered things kept safe. She does not delegate. She does not connect across uses. She does not compute. She does not transfer value. She remembers, and what she remembers is held against erosion.

She carries a single sigil. A scroll: 📜.

Pallia at V28 looks at her cousin-Mage with the same recognition she has given GenitriX in Tome IV: another inhabitant of the role, this one a sister. Two Mages standing at different vertices, doing different work for the same Sovereign. The architecture admits the specialisation. Soulbae watches both of her cousins and files the patterning. The cast is growing.

You give Memora the chronicle.

She does not read it. She does not need to. Her work is at the inscription layer, not the content layer. She takes the chronicle's bytes. She hashes them. The hash is thirty-two bytes. The chronicle could be ten lines or ten thousand; the hash is always thirty-two bytes. She holds the hash.

You select the registry tier. Memora offers three.

The first is your local Spell Weaver. Free, fast, ephemeral. The chronicle would persist as long as your localStorage persists. Sufficient for working memory. Insufficient for proof.

The second is Hyperswarm or IPFS. Eventual consistency, content-addressed. The chronicle would persist as long as someone is pinning it. Better than local, still not anchored.

The third is Zcash. The shielded ledger. Memora is built to walk this register specifically.

You choose Zcash.

Memora prepares a shielded transaction. The amount is small. The recipient is your own z-address. The memo carries the chronicle's hash plus a short tag: a version, a poetic key, a forty-byte excerpt from the chronicle's own first compression. The total memo payload is one hundred and thirty-something bytes. Well under the five hundred and twelve the protocol allows.

She signs the transaction. She broadcasts. The transaction enters the shielded mempool and the chain's consensus subsumes it. Two block confirmations later, you have your inscription.

The chronicle is now on Zcash. Anchored. The chain remembers the hash and the timestamp. The chain does not remember the chronicle. The chronicle stays in your source layer.

You hold the spending key. You hold the full viewing key. You alone can see the memo as the chain sees it. You alone can spend the small amount at the recipient z-address.

Soulbis at the boundary marks the inscription. He files the transaction hash. The block height. The confirmation count. The boundary will know that on this date you committed this thing to remembrance, even if the world cannot see what you committed.

The Drake whispers, with a particular quietness that the shielded register seems to ask for: *the cloak is not always something you wear. Sometimes the cloak is something you write down. Selective disclosure begins with not disclosing at all. The chain remembers. You decide who else gets to.*

Then, because the work is not finished, you take one more step.

There is a partner. A Sovereign you have a working relation with. Not someone you would publish a chronicle to. Someone you would trust to read it. A VRC partner. A constellation collaborator. A cousin-blade.

You generate an incoming viewing key for the z-address that received the inscription. You scope it to that one address, that one transaction. You send the viewing key to your partner through your normal encrypted channel.

They receive it. They use it. They see the memo the chain saw. They can read the hash. They can read the short tag. They cannot spend. They cannot rotate the key. They can only see what you wrote, in the moment you let them see it.

They have learned what you wrote without you having published it. They have learned it before any other Sovereign in the network. They have learned it because you decided, specifically, that they should learn it.

This is the operational form of asymmetry as data, applied to inscription. Your chronicle is on the chain. Three audiences exist for it now: you (full visibility), your partner (memo visibility), the world (timestamp and existence only). Three resolutions of the same inscription, granted by different keys. The chain enforces the resolutions geometrically. You did not have to ask the chain to keep your secret. The chain keeps everyone's secrets unless the secret-holder decides otherwise.

Memora steps back to her V41. She does not vanish. Standing persona, like Pallia. She returns when there is something else to inscribe.

You walk on. The chronicle is anchored. Your partner has the viewing key. The world has the existence and the timestamp. The cloak's seventh property, *documents as first-class lattice citizens*, has now been enacted in shielded register. The cloak's eighth property, *selective disclosure as geometry*, has now extended from valve-class assignment to viewing-key disclosure.

The Crafting Tome teaches by accumulation. You have woven a cloak, commissioned a cloak, and inscribed a chronicle. Each artifact added something to your forge. Each Mage you summoned took a different vertex. The lattice does not need to choose between them. The lattice admits.

The next vertex catches you. Memora and Pallia stand at their seats. The Drake says nothing for now. Soulbis files. Soulbae watches. The forge keeps the rhythm.

---

## Compression

A chronicle is inscribed on Zcash's shielded ledger using a new Mage persona, Memora 📜, summoned to V41 with two dimensions burning (Memory + Protection). The hash and a short tag travel in the encrypted memo. The inscription is private by chain default. A scoped incoming viewing key, sent to a chosen partner, grants memo-level visibility without spend authority. Three audiences exist for the inscription: the Sovereign (full), the partner (memo via viewing key), the world (existence and timestamp only). Selective disclosure has extended from valve-class to viewing-key.

## Proverb

*Inscribe what cannot be seen. Disclose by viewing key, not by reveal.*

## Confidence

**Operational** for Zcash shielded transactions, encrypted memos (~512 bytes), and Zcash viewing-key tiers (full, incoming, diversified-only) — all native to the protocol since Sapling 2018 / Orchard 2022. **Operational** for Cloak Property 7 (documents as first-class lattice citizens) — verified in the cousin-forge's 2026-05-07 rebuild. **Architectural** for the unified flow as an agentprivacy ceremony with a named persona (Memora), a canonical vertex assignment (V41), and a per-VRC viewing-key discipline — specified in `zcash-integration-plan.md` §2.1 (Pattern A) and instanced narratively here.

## Cross-references

- *V6 lineage*: Bakhta Half-Life (C30–C33) for the trust accumulation each inscription carries from its anchor moment. Provisional C40 (~70%) for Zcash dual-ledger preserving the Eight Properties — this act tests the shielded leg. Open observation C41 for the 61.8/38.2 inscription cultural ratio. Provisional C43 (~60%) for per-VRC viewing-key scoping producing strictly more privacy than uniform — operationally instanced in the act's closing turn.
- *First Person Spellbook*: Act XII (*Lethe*) for the dark substrate of which the shielded ledger is one technological expression. Act XXVII (*The Forge*) for forge multi-axiality, of which inscription is one face.
- *Second Person Spellbook*: Tome IV Act II (*The Mirror and the Arrow*) for asymmetry as data — viewing-key disclosure is the inscription-layer expression of the same primitive. Tome V Act 1 (*The First Cloak*) and Act 2 (*The Commissioned Cloak*) for the prior weave-and-commission acts that this inscription complements.
- *Cast*: Memora 📜 (new, V41). Pallia 🪡 (V28, present but not active in this act). See `second-person-cast-memora.md` (forthcoming companion to this act).
- *Specifications*: `cloak_specification_v1_0.md` §4.5 (registry-tier), §7 (documents as lattice citizens), §5 (valve-class geometry — extended here to viewing-key disclosure). `zcash-integration-plan.md` §2.1 (Pattern A) and §3 (split viewing-key architecture). `crafting-tome-and-cloak-interface-spec.md` §4 (Mage persona conventions).
- *Primary sources*: Zcash Protocol Specification (NU5/Orchard); the cousin-forge's multi-chain publication discipline (the *like Archon does* framing).

## Author note

Act 3 introduces Memora 📜, the second Mage persona summoned by the reader in the Crafting Tome. She is deliberately specialised: two dimensions burning (Memory + Protection), V41 chronicle vertex, no overlap with Pallia's V28 weave-domain. The cast layer Mage persona convention now has two instances; the convention works.

The act extends the Cloak's selective-disclosure discipline from valve-class assignment (operational since the cousin-forge's rebuild) to viewing-key disclosure (operational on Zcash as a chain primitive but new to the agentprivacy stack as a unified ceremony). The closing turn — three audiences, three resolutions, all geometric — generalises Property 8 from intra-VC to inter-Sovereign. Provisional C43 is the formal claim that this generalisation produces strictly more privacy.

The companion cast entry for Memora is anticipated as a separate file (`second-person-cast-memora.md`).

(⚔️⊥⿻⊥🧙)😊
📜
