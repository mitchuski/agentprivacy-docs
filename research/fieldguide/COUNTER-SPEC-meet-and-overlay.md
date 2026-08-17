# Counter-spec: Meet and overlay — replacing the Phase 0 fixture

**For:** Max and the ARWorld side, and whoever picks up ONODE
**From:** Mitch — the trust-graph side of the same team
**Re:** [MITCH_ARWORLD_FIELD_GUIDE_HANDOFF.md](./MITCH_ARWORLD_FIELD_GUIDE_HANDOFF.md) §10,
[ARWORLD_TRUST_WEIGHTED_POI.md](./ARWORLD_TRUST_WEIGHTED_POI.md),
[ARWORLD_DISCOVERY.md](./ARWORLD_DISCOVERY.md)
**Date:** 2026-08-15

The ask was for the smallest honest next graph work: holons plus one or two endpoints
to replace the A2 Maya/Jon fixture for a two-avatar desk demo, and a list of what the
client must send that it does not send yet.

This is that, and it is **runnable rather than argued**. Everything below is
implemented as a zero-dependency reference model, a conformance pack, and a
second-language consumer that agrees with it byte-for-byte:

```sh
cd runtimes && node verify.mjs      # Node + Python stdlib. No install, offline.

  PASS  meet-overlay    54/54   the model
  PASS  fixtures          8/8   the conformance pack
  PASS  consumer-py     15/15   second-language agreement
```

Each claim in this document names the property that holds it up. If you disagree
with a ruling, the fastest way to say so is to break its test — that is the most
useful thing you can send back.

It follows the same discipline as my ToIP DTG lab: this is **evidence, not spec**,
it binds nobody, and §7 below states plainly what it does *not* establish.

---

## 0. Two things to settle before the rest is worth reading

Having now read `ARWORLD_TRUST_WEIGHTED_POI.md` and `ARWORLD_DISCOVERY.md`, most
of this counter-spec turns out to agree with what we have already written down.
Two places do not, and both are load-bearing.

### 0.1 One of our own shipped edge sources should come out

`ARWORLD_TRUST_WEIGHTED_POI` §3.3 lists three sources of a trust edge, and source
2 is **"shared completed adventure / quest proof (same STAR quest or London
registry key)"**. The handoff asks the same thing as an open question (§10.6). My
answer is **no**, and I want to be plain that this contradicts a line in a spec
you have already shipped rather than merely answering an open question.

Co-completion is co-presence with a timestamp. There is no consent in it. If it
mints edges, then the same document's §8 out-of-scope line — *"auto-following
strangers who stood near the same POI"* — becomes false by construction, just
with a quest between the strangers and the following. You already ruled out
auto-Witness on walk-by for exactly this reason; this is the same rule one layer
up, at the person level instead of the place level.

Co-completion should **prompt** a Meet — "you both finished Murder Stones, say
hello?" is a lovely moment and the right place to put the QR. It should not be
one. *(Property M10.)*

### 0.2 A leak that undoes the pairwise reference

The `/poi/nearby` response in §4.2 returns `peerAvatarId` (a raw guid) and
`peerDisplayName` (a global profile name) on every overlay pin. Either one alone
defeats the pairwise R-DID I propose in §3.1: two people who have both met the
same person receive the same identifier for them, compare notes, and reconstruct
a trail neither was shown.

The fix is small and, I think, actually better product. A display name is
**chosen per edge at meet time**, not read off a profile — the face you show this
person. That is the Mage projection applied at the person layer rather than the
place layer, which is what your own §1 says the system is for. Maya can be "Maya"
to me and "M." to Jon, and nothing joins the two.

*(Properties D1–D4. D2 is the one to read: it takes two viewers' projections of
the same pin and asserts no identifier field is equal between them.)*

---

## 0.3 Where this sits (for anyone reading it from the standards side)

This is not a side project that borrowed an idea from my ToIP DTG ZKP task-force
lab. It is a **deployment consumer** of that lab, and it is wired up as one:
`runtimes/lab-bridge/` imports the lab's `07-trust-graph-formation` and
`01-uniqueness-nullifier` directly and runs the same scenarios through both
models, so a change to a gate or a rejection name there turns this red.

Six of runtime 07's gates survived contact with a walking AR game unaltered,
including the structural one — the proposer/prover Gap, which here becomes a
phone recomputing what the phone that just scanned it claimed. Four gates were
added, all four accounted for. One gate has **no analogue and cannot be given
one** (§7: personhood), and one property the lab has was deliberately declined
(§3.1: reachability is not visibility).

The lab-side write-up of all that is
`dtgwg-cred-spec-main_mage/explorations/X11-field-guide-deployment.md`.
Nobody needs to read it. It matters here only because it means the rulings in
this document are not my preferences — they are a model with an upstream that
will break loudly if I drift from it.

---

## 1. Where this comes from

`runtimes/07-trust-graph-formation` in the DTG lab already models the left-hand
side of your query rule — bilateral consent, personhood anchoring, no self-edge,
a fresh R-DID per counterparty, and a commitment the prover recomputes rather
than trusts. Your `fromGraph` fixture is standing in for something that already
has a reference construction.

What the physical game adds is that the shared secret is not a proverb between two
agents. It is a **co-located, expiring, single-use exchange between two phones**.
So the Meet rite here is runtime 07 plus three gates it does not have: co-location,
freshness, and replay.

---

## 2. The Meet rite — `POST /api/trustgraph/witness`

One endpoint, three steps. It is the person-side twin of `/poi/witness`, and the
name collision in §6.3 of your handoff is worth keeping exactly as it is.

```text
A opens Meet          → step=offer     QR on A's screen
B scans the QR        → step=accept    B has consented
A confirms on device  → step=confirm   A has consented → TrustLink exists
```

**The scan alone is an encounter, not an edge.** Peeking a card is encounter only
(§1 of your handoff); scanning is too. An edge needs both hands. *(Property M1.)*

### 2.1 `step=offer`

```json
{ "step": "offer", "nonce": "<128-bit random, client>", "lat": 51.5344, "lon": -0.1016 }
```

Returns the `MeetOffer` to encode in the QR: `{ a, nonce, lat, lon, issuedUtc,
expiresUtc, tag }`. TTL **120 s** — a QR held up between two people, not a
credential you keep in a wallet.

### 2.2 `step=accept`

```json
{ "step": "accept", "offer": { ... }, "nonce": "<B's nonce>",
  "lat": 51.5345, "lon": -0.1017, "consent": true }
```

B derives the shared compression from both nonces and the offer tag, mints
`rdidB`, and asserts a link commitment. B **cannot** mint the edge.

### 2.3 `step=confirm`

A recomputes everything from public parts and signs. Eight gates, in order, each
with a named rejection reason — the same closed-vocabulary style as the DTG
conformance register:

| # | Gate | Rejection | Property |
|---|------|-----------|----------|
| 1 | confirmer opened this meet | `offer-not-mine` | — |
| 2 | no self-edge | `self-edge-forbidden` | M3 |
| 3 | bilateral consent | `unilateral-no-mutual-consent` | M1 |
| 4 | offer not expired | `meet-offer-expired` | M4 |
| 5 | nonce single-use | `meet-offer-replayed` | M5 |
| 6 | within 50 m | `meet-not-colocated` | M6 |
| 7 | commitment recomputed, not trusted | `link-commitment-forged` | M7 |
| 8 | one link per pair | `duplicate-link` | M8 |

Gate 7 is the one that matters structurally. The confirming side never trusts the
scanning side's `claimedLink`; it recomputes it from the public parts. Proposer and
prover are held apart. That is the same non-collusion property as the DTG lab's
Gap, and it is why a tampered client cannot talk its counterparty into an edge.

### 2.4 `TrustLinkHolon`

```json
{
  "kind": "TrustLink",
  "trustgraph_kind": "TrustLink",
  "a": "avatar-mitch",
  "b": "avatar-maya",
  "rdidA": "<A's R-DID toward B>",
  "rdidB": "<B's R-DID toward A>",
  "link": "<recomputed commitment>",
  "presentA": "Mitch",
  "presentB": "Maya",
  "formedUtc": "2026-08-15T21:20:10Z",
  "placeHint": { "lat": 51.53, "lon": -0.10 }
}
```

`presentA` / `presentB` are each side's chosen face toward the other, supplied on
`offer` and `accept` respectively. They live on the **edge**, never on the
profile — that is §0.2.

**No score, no weight, no direction.** *(Property M2b.)* A relationship either
exists or it does not; nothing in the overlay path reads a number off it. Place
hint is rounded to ~1 km — a meet has a place, but not a doorway.

---

## 3. Promise — per-holon disclosure

`PoiDiscovery` gains one optional field:

```json
"disclosure": { "maxAudience": "acquaintance" | "link" | "public" | "private",
                "deny": ["note"] }
```

Projection is a **closed allow-list**, not a strip-list. This is the single most
important change to what `/poi/nearby` does today.

| Audience | Fields |
|---|---|
| `public` | `poiId`, `title`, `placeKind`, `markerStyle`, **coarse** lat/lon (~100 m) |
| `link` | + `wikiSlug`, `rite`, `trail`, `witnessedUtc`, exact geo |
| `acquaintance` | + `note` |
| `private` | nothing — the pin is absent, not blank |

Never projected at any audience: `questId`, `questPinRole`, `source`, `client`,
`avatarId`, `parent`, `holonId`, `witnessCount`, `disclosure`.

Today's behaviour ("public strips notes") is a deny-list, and a deny-list leaks by
omission: the day someone adds `deviceModel` to the holon, it ships, and a test
written against a deny-list still passes. Here the projection starts empty and
copies in only named fields. **Property P2 bolts a junk field onto a holon and
asserts it never surfaces at any audience** — that is the test that keeps this
honest a year from now.

Answering your §10.2 question directly: **yes, project title/kind/geo on `link` by
default**, and yes, exact geo at `link` — a peer you have physically met can see
where you were. `questId` and `note` are the two that must never ride along.
*(Properties P1, P8.)* Quest pins cap one tier tighter, at `link`, even for an
acquaintance: a quest pin says what you were *doing*, not just where you were.
*(Property P9.)*

### 3.1 Two rulings, both opinionated

**Audience is granted, not computed.** A 1-hop TrustLink gets you `link`. Nothing
gets you `acquaintance` except the owner handing it to you (`grant`). And graph
distance never raises an audience — two hops is not half of `link`, it is nothing.
*(Properties P5, P6, N7.)*

This is what "no central trust score" means once you make it mechanical: **distance
is not a currency.** The moment 2-hop peers leak in at a reduced tier, you have
built a score with extra steps, and every player's incentive becomes edge farming.

**The peer reference is pairwise.** A projection carries the owner's R-DID toward
*this* viewer, never the raw `avatarId`. Two people who have both met me hold two
unjoinable references to me and cannot collude to reconstruct my trail.
*(Property P7.)* This is the one change that touches Unity — see §6.

---

## 4. The overlay — `GET /poi/nearby`, fixture removed

The query rule from your §3, now executable on both sides:

```text
TrustEdge(A, B) AND DisclosurePolicy(B, audienceForA).allows(PoiDiscovery fields)
```

Left side is §2 (a real meet). Right side is §3 (a closed allow-list). Signature is
unchanged; `fixture` becomes a no-op and then goes away.

`fromGraph` = for every 1-hop peer, their discoveries in radius, each projected at
the audience that peer granted this viewer, then distance-first, then capped at 12.

**An empty `fromGraph` is the correct answer when you have not met anyone.**
*(Property N1.)* Your invariant "do not disable `UsePoiFixture` in production until
live edges exist" is right for today and should be retired the day the Meet rite
ships — a fixture that outlives its stand-in becomes a lie the product tells.

Invariants held under test: Greenwich never enters an Islington viewport *(N3)*;
the cap is 12 *(N4)*; ordering is distance-first *(N5)*; self keeps its own note
while the peer projection does not *(N6)*.

---

### 4.1 Erosion — answering `ARWORLD_TRUST_WEIGHTED_POI` §9.3

> *"Should overlay pins require the peer to be recent (e.g. witnessed in the last
> 90 days)?"*

Yes — but 90 days as a boolean is a cliff, and a pin does not stop being true on
day 91. Freshness is a **half-life of 90 days** with a floor at **0.25** (≈180
days), and the scalar ships in the response so Unity can fade the ring rather
than pop the pin. *(Properties E1, E2, E5.)*

**Your own trail never erodes.** *(Property E4.)* Erosion governs how much a
peer's old enthusiasm should move you, not whether you were somewhere.

This is the `erosion-record` lens from the DTG lab: assurance decays as a rate,
not a cliff. It is also the thing this model most needs next and does not have —
there is no revocation path on a TrustLink, and a link formed once is currently
permanent. Both belong in a second pass.

### 4.2 Wire alignment

Three small things I have followed rather than invented, plus one inconsistency
to resolve:

- **`witnessedUtc` is ISO-8601**, per §3.1 — not epoch. Pinned at the boundary in
  `src/time.mjs`. The DTG lab's canonical suite exists because an unpinned
  timestamp encoding is exactly what two implementations silently disagree about
  and then cannot explain their differing digests.
- **`origin` / `audience`** are the response field names, per §4.2.
- **`radiusM`** echoes at the top level of the response, per §4.2.
- **Inconsistency:** §4.2 calls them `origin` / `audience`; the handoff's §7.2
  `TrailPin` table calls them `trustOrigin` / `trustAudience`. One should give. I
  have followed the API doc and left the rename to Unity's mapper, but you may
  prefer the reverse.

### 4.3 Stewards — answering `ARWORLD_DISCOVERY` §10.3

> *"Does redeem at till create a TrustLink (player ↔ steward), or only a receipt
> holon?"*

A receipt. *(Property S1.)*

A till redeem clears the Meet rite's physical gates — it is co-located and
bilateral — so the temptation to reuse `TrustLink` is real. Resist it. A
`TrustLink` is a **symmetric** object, and these two parties are not symmetric: a
steward serves hundreds of people a week, a player is one person. Minting one
would put every pilgrim's trail inside the venue's `fromGraph` in exchange for a
cup of tea, which is a data harvest wearing a loyalty card — and it would arrive
by accident, through a code path nobody reviewed as a privacy decision.

If a steward edge is genuinely wanted later, it needs its own kind, with one-way
disclosure (player → venue, aggregate only) and no reciprocal query right. That
is a different object, not this one with a flag. Your §7 already says the right
thing — *"do not invent a museum trust score"* — this is the same instinct
applied to the edge rather than the score.

### 4.4 The `wikiSlug` seam — and the one finding I did not expect

Handoff §8 sets the rule and I agree with all of it: FedWiki is lore, not the POI
database; no journal page on every Witness; the only sanctioned two-way path is
to **fork** a stub that links the canonical slug, because that is Dave's
neighbourhood model rather than an overwrite API.

Modelling it turned up something none of the three specs says, and I think it
matters more than the feature does.

> **A wiki fork is not an audience. It is a quantifier change.**

The Promise ladder — `public` / `link` / `acquaintance` — answers *"how much do I
show **this** counterparty."* Every rung on it, `public` included, is scoped to
somebody you are handing something to. A federated wiki page has no counterparty:
it is readable by everyone, indefinitely, and it **propagates by design**. That
is what federation is for.

So `public`-the-Promise-tier and `public`-the-wiki-page are false friends, and
they are false friends in the most dangerous direction. `public` is the *least*
private rung on the ladder — the one a cautious player would pick. A fork path
that reads the audience ladder to decide what it may publish will take that
caution and turn it into worldwide publication.

Therefore: **publication is its own consent, per discovery, defaulting to off,
and it is not implied by any audience.** In the model `WORLD` is deliberately not
a member of `AUDIENCES` — it cannot be reached by widening. *(Property W2: a
holon with the most permissive possible ceiling still refuses to fork without a
separate publish consent.)*

The rest falls out:

| Behaviour | Property |
|---|---|
| A plain Witness writes no page (§8: "would spam the neighborhood") | W1 |
| A `private` pin is unpublishable at any consent | W3 |
| A forked page carries public-tier fields only — never the note, never the quest | W4 |
| The fork claims its own slug and *links* the canonical one, with a `fork` journal event naming the source site | W5 |
| One fork per (avatar, poi) — a second Witness does not re-fork | W6 |
| A generic floor pin (`wikiSlug: city-discover`) has nothing to fork from, so the game never becomes the source of truth for lore | W7 |

---

## 5. Your seven open problems, answered

| # | Question | Answer | Property |
|---|----------|--------|----------|
| 1 | How are 1-hop edges created? | Co-located, expiring, single-use, bilaterally consented QR Meet → `TrustLinkHolon`. `POST /witness`, three steps, eight gates. | M1–M9 |
| 2 | Promise on discoveries | Per-holon `disclosure` + closed allow-list per audience. `link` gets title/kind/exact geo/wikiSlug; `questId` and `note` never ride along. | P1–P3, P8, P9 |
| 3 | Self list / passport | The holon must carry every field Unity stamps: `rite`, `trail`, `questPinRole`, `markerStyle`, `wikiSlug`, `witnessedUtc`. A `restorePassport` read is lossless over that set. Nothing is missing today except `disclosure`. | K5 |
| 4 | Id remap | Alias table, resolved server-side, client keeps sending `poi-osm-…`. **But an alias must be a migration, not a lookup** — see §5.1. | K4 |
| 5 | Mage card vs place proof | Person card + `wikiSlug` is enough. A place-level Mage projection would be a third identifier for a thing that already has two (`poiId` for space, `wikiSlug` for story) — do not mint it. | — |
| 6 | Shared quest as a Trust edge | **No.** Co-completion is an encounter with no consent on it. It can *prompt* a Meet; it cannot be one. Otherwise the graph grows from co-presence, which is exactly the auto-Witness-on-walk-by you already ruled out. | M10 |
| 7 | Swordsman parent | **Yes, correct.** Knowledge is full context and homes under the Swordsman. The Mage is the per-audience projection minted at read time (§3) — which is precisely why the projection must be computed, never stored. | — |

### 5.1 A finding: aliasing is a migration

Registering `poi-osm-way-123 → venue-the-castle` as a lookup is not enough. A
player who Witnessed the pub before the partner claimed it and again afterwards
ends up with **two holons and a `witnessCount` that lies about both**. Claiming a
node has to carry existing Knowledge across with it, merging on collision and
keeping the earliest `witnessedUtc`.

I found this by writing the test, not by reasoning about it — the first version of
K4 failed. It is a live bug in any lookup-only implementation.

This also answers `ARWORLD_DISCOVERY` §10.2 — *"can a partner reject anonymous OSM
duplicates of their venue (replace pin id)?"* Yes: the claim registers the alias
and migrates existing Knowledge onto it. The client keeps sending `poi-osm-…` and
never learns anything changed.

### 5.2 The other open questions in the two specs

| Doc | Question | Answer |
|---|---|---|
| TRUST_WEIGHTED §9.1 | Witness = quest check-in only, or also tap-to-peek "save to trail"? | **Both, but through one rite.** `ARWORLD_DISCOVERY` §4 already settles it — one confirm path, two UI skins. A "Save to trail" button that skips `TryConsumePending` → `NotifyCheckIn` is a second meaning of discovery, and the handoff's §5 invariant forbids it. *(Property K3 refuses any rite outside the closed vocabulary.)* |
| TRUST_WEIGHTED §9.2 | Default Promise: `link`-visible or `acquaintance`-only until the user toggles? | **`link`-visible for title / kind / geo / wikiSlug; `acquaintance` for the note, and only by explicit grant.** The ceiling defaults to `acquaintance` so grants mean something; the *projection* a 1-hop peer receives is `link`. Quest pins cap at `link` regardless. *(P6, P9.)* |
| DISCOVERY §10.1 | Must discovery require the camera, or is GPS-in-radius + hold-to-Witness enough? | Not a graph question — both are in the rite vocabulary (`camera-fetch`, `desk-witness`) and the holon records which. Whatever you choose, record it: the `rite` field is what lets you answer this empirically later instead of re-arguing it. |
| DISCOVERY §10.4 | Photo retained? | Do not retain it in v1, as you propose. If a `MediaHolon` lands later it is Knowledge under the Swordsman, and it belongs in `NEVER_PROJECTED` until somebody writes a policy for it — an image leaks more than any field currently on the holon, including faces that never consented to the game at all. |

---

## 6. What Field Guide must send that it does not send yet

Small list. Nothing here is a new subsystem.

1. **A Meet UI** — QR display, scanner, and a confirm tap on the offering device.
   This is the only genuinely new client surface. Three calls, no new store.
2. **Client-side nonces and both endpoints' GPS** on offer and accept. You already
   have location; you are just not sending it on a person-to-person action yet.
3. **`disclosure` on `POST /poi/witness`** (optional) so a player can mark a pin
   private at Witness time rather than after the fact.
4. **A `presentAs` field on offer and accept** — the face you show this person.
   One text field in the Meet UI, defaulted to whatever the player used last.
5. **`TrailPin.peerAvatarId` → `peerRef`**, carrying the pairwise R-DID instead of
   the raw guid, and `peerDisplayName` sourced from the edge rather than the
   profile (§0.2). A one-field rename plus one changed source in `TrailPin.cs`,
   `TrustWeightedPoiClient.cs`, and `CityPoiPeekOverlay.cs`.
6. **Read `freshness` on overlay pins** and fade the gold ring by it (§4.1).
   Optional, but without it the erosion floor becomes a pop rather than a fade.
7. **A publish toggle, if you want the wiki fork lane (§4.4)** — separate from
   the audience control, defaulting off, worded as publication rather than as
   sharing. "Add a stub page to the wiki" and "let friends see this" must not be
   the same switch.
8. **Drop `fixture=arworld-trust-poi-phase0`** from `TrustWeightedPoiClient` once
   `/witness` is live, and delete `RequestPhase0Fixture`.

Not on the list, per your §10: no Photon, no friends DB, no second profile store,
no FedWiki scraping, no auto-Witness. Nothing above needs any of them.

---

## 7. What this does *not* establish

The boundary is the pedagogy, so here it is plainly.

- **This is not zero-knowledge.** It is a reference model of the *relations*, in the
  same sense as lab runtime 07. A ZK version proves edge membership without
  revealing the pair; that is a later conversation and it does not block the desk
  demo.
- **It does not establish location integrity.** Co-location is asserted by the
  client's own GPS. A spoofed GPS spoofs a meet, and two colluding players can mint
  an edge from opposite ends of the country. I think that is acceptable *here* and
  the reason is structural: an edge exposes only what the owner's policy allows, and
  there is no score to farm. Name the adversary and the trade is visible; hide it
  and it becomes a surprise later.
- **It does not establish personhood.** OASIS avatar creation is not
  personhood-anchored, so this is a **pseudonym graph, not a personhood graph** —
  one human can hold many avatars and mint edges between them. Lab runtime 07 gate
  G2 requires both endpoints to be personhood-anchored and rejects them otherwise;
  there is no equivalent here because there is nothing to anchor to. If Sybil
  resistance ever matters for the Field Guide, that is where it comes from
  (runtime 01's scoped nullifier), and it is a real piece of work rather than a
  flag to flip.
- **It does not establish that the note is safe.** `acquaintance` reveals free text
  a player wrote. The allow-list controls *which* fields travel, never what someone
  chose to type into one.
- **It does not establish that a presented name is true.** `presentAs` is
  self-asserted at meet time, so someone can present as "Maya" to a third party.
  That is survivable here because the name is scoped to one edge formed by a
  physical meeting — you are looking at the person while they choose it — but it
  is a name, not an attestation, and nothing downstream should treat it as one.

---

## 8. How to be tested against this

A counter-spec only a JavaScript model can evaluate is a description. This one
ships a conformance pack, so your ONODE implementation can be held to it the
same way an implementer will one day be held to the DTG spec.

### 8.1 The rejection register — `runtimes/fixtures/register.mjs`

**22 codes, every one triggered by a live vector** (property F1; F2 asserts
nothing escapes the vocabulary).

Two implementations agree about success trivially and disagree about failure
constantly. *"It rejected the request"* is not interop. *"It rejected the request
with `meet-not-colocated`"* is. This is the artefact from my DTG lab that turned
out to be worth the most and that nobody expected to be.

The overlay codes are worth having even when nothing is wrong: `GET /poi/nearby`
takes `explain=true` and returns an `excluded` array naming why each absent pin
is absent — `out-of-radius`, `no-trust-edge`, `below-freshness-horizon`,
`audience-capped-private`, `over-overlay-cap`. A desk demo with an empty overlay
should be able to say why in one call instead of by bisecting the query.

### 8.2 Vectors — `runtimes/fixtures/vectors.json`

Deterministic: fixed clock, no randomness, and property F4 asserts regenerating
is byte-identical. 22 rejection vectors, 15 projection vectors, each carrying the
canonical preimage *and* its digest — so an implementation that cannot reproduce
a digest can diff the preimage and see exactly which field it got wrong, rather
than staring at two unequal hashes.

### 8.3 A second language agrees — `runtimes/consumer-py/consume.py`

Python 3 stdlib only, sharing zero code with the JavaScript, re-implemented from
this document's prose. **15/15 projections byte-exact.**

### 8.4 What that consumer found, which is the point of writing it

The `public` tier coarsens geo to ~100 m. The obvious implementation is
`round(x * 1000) / 1000`, and it is wrong in a way no unit test catches:

| Language | `round(51534.5)` | Mode |
|---|---|---|
| JavaScript | **51535** | half-up, toward +∞ |
| Python | 51534 | half-to-even (banker's) |
| **C#** `Math.Round` | 51534 | **half-to-even by default** |

Two conformant-looking servers place the same pin **~110 m apart**, on opposite
sides of a street, and both pass their own tests. **This one is aimed at you:**
ONODE is C#, and `Math.Round` there is banker's rounding unless you pass
`MidpointRounding.AwayFromZero`.

The spec now names the mode — half-up, which is `floor(x + 0.5)` everywhere —
and vector `pj-halfway` sits exactly on the boundary on both axes so the
disagreement is caught by the pack instead of by a player. I checked that it
bites: swapping the correct coarsening for the naive one fails that vector and
only that vector.

Same family of trap, already handled: canonical numbers are fixed to 6 decimal
places because `1` vs `1.0` vs `1e0` is the commonest way two JSON serialisers
silently disagree, and C# needs `CultureInfo.InvariantCulture` or a decimal comma
will pass every test written in a de-DE locale and fail every interop check.

---

## 9. Two-avatar desk demo

```sh
# The model, end to end — no network, no install
cd runtimes && node verify.mjs                   # model + pack + Python consumer

# On ONODE, once /witness lands:
#  1. authenticate both avatars           POST /api/avatar/authenticate
#  2. A offers, B accepts, A confirms     POST /api/trustgraph/witness  (×3)
#  3. B witnesses a place near Islington  POST /api/trustgraph/poi/witness
#  4. A reads the overlay                 GET  /api/trustgraph/poi/nearby
#       → fromGraph contains B's pin, projected at `link`, with no fixture flag
```

Step 4 returning B's real pin with `"fixture": false` is the moment Phase A is
done and Maya and Jon can be deleted.

---

## 10. Files

```text
field_guide_privacymage/
  MITCH_ARWORLD_FIELD_GUIDE_HANDOFF.md      ← Max's handoff (input)
  ARWORLD_DISCOVERY.md                      ← Max (input)
  ARWORLD_TRUST_WEIGHTED_POI.md             ← Max (input)
  COUNTER-SPEC-meet-and-overlay.md          ← this file
  runtimes/
    verify.mjs                              runs all three, prints a paste-able report
    meet-overlay/
      test.mjs                              54 properties, zero-dep
      NOTES.md                              design notes + lab correspondence
      src/identity.mjs                      avatar, pairwise R-DID
      src/meet.mjs                          the rite; TrustGraph; quest + steward encounters
      src/knowledge.mjs                     PoiDiscovery, idempotence, alias migration
      src/promise.mjs                       disclosure policy, closed allow-list
      src/nearby.mjs                        the query rule; distance-first, eroded, capped, explainable
      src/story.mjs                         the wikiSlug seam; publication as its own consent
      src/erosion.mjs                       freshness half-life + horizon
      src/canonical.mjs                     byte-exact encoding for interop
      src/time.mjs                          ISO-8601 at the boundary
      src/geo.mjs, src/hash.mjs             haversine; sha256 domain separation
    fixtures/
      register.mjs                          22 rejection codes, closed vocabulary
      generate.mjs → vectors.json           deterministic conformance pack
      test.mjs                              8 pack properties incl. live-coverage + determinism
    consumer-py/
      consume.py                            Python stdlib only; 15/15 byte-exact
```

Related, in the DTG lab (`dtgwg-cred-spec-main_mage`):
`runtimes/07-trust-graph-formation` (this model's parent),
`runtimes/01-uniqueness-nullifier` (where personhood anchoring would come from),
`runtimes/quiet-presentation` (observer leakage budget — the right lens for §3).
