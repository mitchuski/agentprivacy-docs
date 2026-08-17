# Reflection map — ARWorld ↔ the DTG ZKP lab

*What Max shared around ARWorld, set against the ToIP DTG ZKP task-force work, object by
object and rule by rule.*

Every row names the property that holds it. Those anchors are **checked**:
`runtimes/reflection/test.mjs` runs the suites, extracts every property that actually
exists, and asserts that every anchor in this file resolves and that every property is
either anchored here or explicitly excused at the bottom. If a property is renamed or
deleted, this map goes red. That is the point — a correspondence table that cannot go
stale loudly is just prose with a border.

**Inputs on the ARWorld side** (all from Max, 2026-08-12 to 2026-08-15):
`MITCH_ARWORLD_FIELD_GUIDE_HANDOFF.md` · `ARWORLD_DISCOVERY.md` ·
`ARWORLD_TRUST_WEIGHTED_POI.md`.
**Inputs on the lab side:** `dtgwg-cred-spec-main_mage` — `runtimes/07-trust-graph-formation`,
`runtimes/01-uniqueness-nullifier`, the predicate & assurance-boundary decision document,
explorations X1/X4/X6, and now `explorations/X11-field-guide-deployment.md`.

Status vocabulary, closed: **reflected** (both sides say the same thing) · **refined** (the
game sharpened what the lab had) · **diverged** (deliberately different, with a reason) ·
**absent** (one side has no analogue and cannot be given one) · **new** (neither side had it).

---

## A. The nouns

| ARWorld | Lab / cred-spec | Status | Held by |
|---|---|---|---|
| `TrustLinkHolon` — TRUST_WEIGHTED §3.3 | VRC: a bilateral relationship credential; the runtime 07 edge | reflected | `prop:B1` `prop:B4` |
| The Meet QR exchange (proposed) | Mage proposes ⊥ Swordsman proves, across the Gap | reflected exactly, across a substrate change | `prop:B5` `prop:M7` |
| Witness rite — DISCOVERY §3 | `encounter()`: the collision producing a matching compression | reflected, plus four gates the physical world needs | `prop:B8` |
| `PoiDiscovery` holon — TRUST_WEIGHTED §3.1 | Knowledge under the Swordsman; the data layer of three-layer identity | reflected | `prop:K1` `prop:K5` |
| `DisclosurePolicy` audiences — §3.2 | decision §19/§20 observable events; X4 event minimisation | refined: per-holon, closed allow-list rather than a strip-list | `prop:P2` `prop:P8` |
| `peerAvatarId` + `peerDisplayName` — §4.2 | cred-spec R-DID uniqueness: "a new, unique R-DID for every counterparty" | **diverged** — ARWorld ships a globally stable pair; the rule requires pairwise | `prop:D2` `prop:D3` `prop:D4` `prop:B6` |
| OASIS avatar | M-DID / PHC personhood-anchored member, via the runtime 01 nullifier | **absent** — nothing to anchor to. §C.1 | `prop:B7` |
| `fixture=arworld-trust-poi-phase0` | — | stand-in for the left half of the query rule; retires when the rite ships | `prop:N1` |
| `wikiSlug` → FedWiki page — handoff §8 | — | **new** — the seam neither side had modelled. §C.3 | `prop:W5` |
| Partner venue / steward — DISCOVERY §6 | — | **new**, and asymmetric: a receipt, never an edge | `prop:S1` |

## B. The rules

| ARWorld says | Lab says | Status | Held by |
|---|---|---|---|
| "Peeking a card is **encounter**, not discovery" — DISCOVERY §2 | G5a: a bare proposal never touches the graph | reflected — the same rule at the place layer and the person layer | `prop:M1` |
| "No central trust score" — TRUST_WEIGHTED §1 | the runtime 07 edge carries no weight or direction | reflected, then extended: **distance is not a currency either** | `prop:M2b` `prop:B9` |
| "Multi-hop / friend-of-friend spam" out of scope — §8 | runtime 07 models propagation via `connected()`, correctly | **diverged, deliberately** — "does trust reach" ≠ "who may see". X11 §5 | `prop:B9` `prop:P5` `prop:N7` |
| Shared completed adventure is an edge source — §3.3 | G1: the graph grows only on mutual consent | **refuted** — co-completion is co-presence with a timestamp | `prop:M10` |
| Idempotent on `(avatarId, poiId)` — §4.1 | G6: one VRC per pair | reflected at both layers | `prop:K1` `prop:B4` |
| "One rite, two skins" — DISCOVERY §4 | — | reflected as a closed rite vocabulary; no auto-Witness on walk-by | `prop:K3` `prop:K2` |
| "Mage never returns raw Swordsman conversation" — §3.2 | decision §19/§20; X4 | reflected as a closed allow-list, and as self-keeps-its-note | `prop:P1` `prop:N6` `prop:P3` |
| "Distance first; trust never pulls Greenwich onto an Islington viewport" — §2 | — | product invariant, held mechanically | `prop:N3` `prop:N5` |
| Cap the overlay (Unity: 12) — §5 | — | product invariant, held | `prop:N4` |
| "Should overlay pins require recency, e.g. 90 days?" — §9.3 | X6: assurance decays as a **rate, not a cliff** | reflected — arrived at independently, from a map-rendering problem | `prop:E1` `prop:E2` `prop:E3` `prop:E5` |
| — | X6: the two clocks are asymmetric | refined: your own trail never erodes | `prop:E4` |
| "Do not invent a museum trust score" — DISCOVERY §7 | — | extended from the score to the **edge** | `prop:S1` |
| Default disclosure "allow title/kind/geo on link" — §4.1 | — | reflected; ceiling defaults to `acquaintance` so a grant means something | `prop:P6` `prop:P9` `prop:P4` |

## C. The three places the reflection breaks

These are the document. Everything above is agreement; these are the parts worth arguing about.

### C.1 Personhood — **absent**

Runtime 07 gate G2 requires both endpoints to be personhood-anchored. ARWorld has nothing to
anchor to, so an OASIS avatar presented to the lab's own prover is rejected. `prop:B7` is that
rejection, live. Consequence, stated rather than implied: **the Field Guide trust graph is a
pseudonym graph, not a personhood graph.** Every privacy property survives; no Sybil-resistance
property does, and none is claimed. Runtime 01 is where the anchor would come from.

### C.2 The pairwise reference — **diverged**

The cred-spec requires a fresh, unique R-DID per counterparty. The shipped `/poi/nearby`
response returns a raw avatar guid *and* a global display name on every peer pin, either of
which lets two viewers who have both met the same person join their views. `prop:D2` is the
generalised catch: two viewers' projections of one pin share **no** identifier field. The fix —
a face chosen per edge at meet time — costs one text field.

### C.3 Publication — **new**, and unmodelled on both sides

Handoff §8 sanctions forking a stub wiki page after a Witness. Neither the ARWorld docs nor the
lab has a concept for it, because both ladders are scoped to a counterparty and a federated page
has none. `public` is the *least* private rung, so a fork path reading the audience ladder
publishes a cautious player's trail to the world. Publication is therefore its own consent,
defaulting off, and `WORLD` is deliberately not on the ladder. `prop:W1` `prop:W2` `prop:W3`
`prop:W4` `prop:W6` `prop:W7`

## D. What ARWorld gave back to the lab

The reflection is not one-way. X11 files these upstream.

| Finding | Why it matters to the task force | Held by |
|---|---|---|
| The Gap survived a substrate change — agent-to-agent becomes phone-to-phone, unaltered | the strongest evidence runtime 07's central claim is structural rather than incidental | `prop:B5` `prop:B2` `prop:B3` |
| The deployment delta is **bounded at four gates**, asserted | a fifth added quietly turns the bridge red; the boundary is maintained, not described | `prop:B8` |
| "Reachability is not visibility" | a cheap second answer to discussion #11's list-inflation question — no threshold required | `prop:B9` |
| **A coarsening rule that does not name its rounding mode is not a rule** | JS rounds midpoints up; Python and C# round to even. Generalises to every numeric field in the P2 descriptor and transcript encodings | `prop:C3` `prop:C1` `prop:C2` `prop:C4` |
| The X1 conformance instrument, rebuilt in an unrelated domain, earned its keep within an hour | second data point for §26.2 fixture-format adoption, and for P5's third-consumer ask | `prop:F1` `prop:F2` `prop:F5` `prop:F7` |
| Domain separation between the two models is checked | a Field Guide link commitment can never be mistaken for a DTG VRC | `prop:B10` |

## E. Max's open questions, answered from the lab

| Question | Answer | Held by |
|---|---|---|
| handoff §10.1 — how are 1-hop edges created? | the Meet rite: eight gates, three steps | `prop:M2` `prop:M3` `prop:M4` `prop:M5` `prop:M6` `prop:M8` `prop:M9` |
| handoff §10.2 — Promise on discoveries | closed allow-list per audience, per holon | `prop:P1` `prop:P7` |
| handoff §10.3 — passport / reinstall | the holon carries every field Unity stamps | `prop:K5` |
| handoff §10.4 / DISCOVERY §10.2 — id remap, partner claims an OSM node | alias table — but as a **migration**, not a lookup | `prop:K4` |
| handoff §10.6 — shared quest as a trust edge | no | `prop:M10` |
| handoff §10.7 — Swordsman parent for discoveries | yes, and that is why projections are computed at read time | `prop:N2` `prop:N8` |
| TRUST_WEIGHTED §9.1 — witness = check-in only, or "save to trail" too? | both, through one rite | `prop:K3` |
| TRUST_WEIGHTED §9.2 — default `link` or `acquaintance`? | `link` projection, `acquaintance` ceiling | `prop:P6` |
| DISCOVERY §10.3 — does a till redeem create a TrustLink? | a receipt; the parties are not symmetric | `prop:S1` |
| DISCOVERY §10.4 — retain the photo? | no; and a `MediaHolon` belongs in `NEVER_PROJECTED` until someone writes it a policy | `prop:P8` |
| — the fork lane, once it exists | idempotent per (avatar, poi) | `prop:W6` `prop:D1` |

---

## Not a reflection

Properties that hold the workbench together without corresponding to anything on either side.
Listed so the coverage check can be exhaustive rather than polite.

```unmapped
F3 — register hygiene: no duplicate codes, every entry documented
F4 — pack determinism: regenerating vectors.json is byte-identical
F6 — the canonical preimage in the pack is reproducible, so a mismatch is diffable
F8 — a private holon yields no projection at any audience, checked on the shipped artefact
```
