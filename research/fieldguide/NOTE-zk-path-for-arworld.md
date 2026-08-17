# Exploration note — could the Field Guide's trust layer be zero-knowledge?

**For:** Max and the ONODE side
**From:** Mitch — the trust-graph side of the same team
**Date:** 2026-08-15
**Status:** exploration. Nothing here is on our roadmap, and none of it blocks the desk demo.

Short answer: yes, three parts of it usefully, one part of it beautifully — but **not yet**, and the
blocker is not a circuit. It is key custody. That is the whole note in a sentence; the rest is why,
what it would cost in real numbers, and the order I would do it in.

---

## 1. The precondition nobody can skip

Today ONODE holds every avatar's keys, every edge, and every discovery, and computes `fromGraph` on
the server.

**A zero-knowledge proof presented to a party that already holds your secrets protects nothing.** If
the client proves to ONODE "I hold an edge with the owner of this pin," ONODE already knew that —
it issued the edge, it stores the edge, it can read the edge. The proof is decoration.

So the first step towards ZK is not circom. It is moving signing keys to the device — what the
credentials spec calls a **personal network vault**, "under the exclusive control of that person,"
who "may sometimes choose to delegate use of their credentials or keys to a VTA." OASIS today is the
delegated cloud VTA, which the spec explicitly permits. It just means ZK has nothing to bite on yet.

I say this first because it is the least fun part and the easiest to skip past into circuits.

There is one honourable exception, and it is where I would actually start — see §3.1. Proving things
to a **third party** is valuable immediately, because ONODE is not the audience.

## 2. What is worth proving, and what is not

The instinct is to reach for the write path. Resist it: `POST /poi/witness` is a player telling their
own server about their own visit. There is no counterparty and nothing to hide. **ZK belongs at the
presentation surface, not the write surface** — which is also where the credentials spec puts it.

Four candidate statements, in the order I would rank them:

| | Statement | Verifier | Payoff |
|---|---|---|---|
| **A** | "These two personas have a relationship" — without revealing either relationship DID | any third party | high, available now |
| **B** | "This pin belongs on my map" — I hold an edge with its owner, and their policy admits me — without revealing *which* peer | the server | very high, needs §1 |
| **C** | "We were within R metres of each other at time T" — without revealing where | anyone | the interesting one |
| **D** | "This discovery is fresher than H" — without revealing when | the server / a peer | small, cheap, nice-to-have |

## 3. The three that are real

### 3.1 A — the pairwise proof, which the spec already defines

The spec's **pairwise ZKP** is available to any two parties holding a relationship credential, with
no community anywhere in the picture — exactly the situation the Field Guide is in. Its named
application is precisely the share card:

> "disclose the parties' P-DIDs (persona DIDs) while hiding the underlying R-DIDs, enabling a public,
> verifiable claim that two known personas have a relationship without exposing the private pairwise
> channel between them or enabling correlation across the holder's other presentations."

That is the r-card, upgraded. Today a shared card asserts things about one person. With a pairwise
proof, a card can carry a *verifiable relationship claim* — "these two personas know each other" —
that a stranger can check, without the two of them leaking the pairwise channel or becoming
correlatable across every other card they have ever shared.

**Why start here:** the verifier is a third party, so it pays off even while ONODE still holds the
keys, and it needs no change to the overlay at all.

### 3.2 B — the private overlay query, which is the actual prize

Right now the server assembles your map because it can see your whole graph. The ZK version inverts
it: the **client** proves

> "there exists an edge between me and the owner of discovery *D*, and *D*'s policy admits the
> audience I am claiming"

without revealing which peer, and the server returns the pin without learning your social graph.

That is a set-membership proof plus a small policy predicate — structurally the same shape as the
lab's `nullifier_membership` circuit, which is already built and measured. The edge set is the
membership tree; the policy check is a handful of comparisons.

**This is where the design stops being a privacy story and becomes a privacy property.** It is also
strictly gated on §1: without device-held keys there is nobody to keep the secret from.

### 3.3 C — proximity without location, which is the one I would most like to build

The spec's **witness credential** already anticipates the statement — its own example is "both
parties provided proof that they were at the same event at the same time." Put that in a circuit and
it becomes:

> "our two positions were within R metres of each other at time T" — **without either position
> being revealed to anyone, including the server**

A meet currently sends both sets of coordinates to ONODE, which is a location-tracking database
accumulating as a side effect of a friendship feature. The ZK version leaks nothing but a boolean.

It is a range proof over a squared-distance comparison — cheap in-circuit, well under the numbers in
§4. The awkward part is not the maths; it is that a phone's GPS is self-asserted, so the proof
establishes "these two devices *claimed* nearby positions," not "these two people were together."
ZK makes the claim private; it does not make it true. Pairing it with a signed location attestation
is a much larger problem and I would not put it on the path.

Even so: **turning "we were in the same place" from a database row into a proof that reveals nothing
is a genuinely nice thing for a walking game to be able to say.**

## 4. What it costs, measured rather than adjectival

From the task force lab — Groth16 over BN254, circom 2.x, real proofs, not simulations:

| Circuit | Statement | Constraints | Prove | Verify | Proof |
|---|---|---|---|---|---|
| `nullifier_membership` | secret in a tree of depth 20 (≈1M), nullifier correctly derived, transcript bound | 11,523 | ~683 ms | ~8 ms | 721 B |
| `dual_issuer` | attestations from two *distinct* issuers | 10,717 | ~738 ms | ~8 ms | 725 B |
| `guardian_threshold` | 3 distinct guardians authorised a recovery | 16,078 | ~830 ms | ~10 ms | 723 B |

Read for the Field Guide:

- **Proof size ~721 bytes.** Irrelevant on mobile. Ship it in a header.
- **Verify ~8 ms.** ONODE can verify these all day.
- **Prove ~700 ms on a developer laptop.** On a mid-range phone, assume several times that. Fine for
  a meet — a once-per-relationship ceremony where the player is already looking at a QR code. **Not**
  fine per-pin on a map that repaints as you walk, which is a real constraint on statement B: it wants
  one proof per query, not one per pin.
- **Trusted setup.** Groth16 needs one per circuit. The lab's is a lab fixture and says so. A
  production deployment needs a real ceremony, which is a governance exercise, not an afternoon.
- One number worth knowing because it is so cheap: **binding a proof to a transcript cost exactly one
  constraint.** Context binding is essentially free, and unbound proofs are replayable, so there is no
  reason to skip it.

## 5. The path I would suggest

Each step is useful on its own and none of them strands you.

0. **Nothing.** Ship the meet rite and the overlay with ordinary signatures. Get the objects right —
   the identifiers, the pairs, the annotations. Every ZK step below is easier if the credential shapes
   are already spec-aligned, and that work has to happen anyway.
1. **Statement A** — the pairwise relationship proof on the r-card. Third-party verifier, no key
   migration needed, and it is the spec's own worked example.
2. **Keys to the device.** The real one. Everything after this depends on it.
3. **Statement C** — proximity as a witness annotation. Small circuit, and it removes a
   location-tracking liability rather than adding a feature.
4. **Statement B** — the private overlay query. The prize, and the most work.
5. **Community-anchored proofs**, if OASIS ever forms a community with personhood governance. Then
   the map can carry claims like "a real person, exactly one membership" without revealing who.

## 6. What I could bring

The lab has the membership circuit and its numbers, the conformance instrument, and a task force whose
charter is exactly this deferred layer. If any of statements A–D become interesting, I would rather
build them there — as public evidence with measurements attached — than as something bespoke inside
OASIS. That way the answer is reusable by anyone implementing the spec, and the Field Guide is the
deployment that motivated it rather than the only place it works.

The honest caveat on all of it: I have not written any of these circuits. The costs in §4 are for
adjacent statements from the same family, which is a reasonable guide and not a quote.
