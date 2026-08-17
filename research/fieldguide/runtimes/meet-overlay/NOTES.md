# meet-overlay — design notes

Reference model behind [`../../COUNTER-SPEC-meet-and-overlay.md`](../../COUNTER-SPEC-meet-and-overlay.md).
Zero-dep: Node stdlib only, offline, deterministic (no wall clock, no randomness —
every time and nonce is passed in, so a run is reproducible).

```sh
node test.mjs         # 54 properties, exits nonzero on any failure
node ../verify.mjs    # + the conformance pack and the Python consumer
```

## Correspondence with the DTG lab

**Reuses:** `dtgwg-cred-spec-main_mage/runtimes/07-trust-graph-formation` and
`01-uniqueness-nullifier` — not by copying, and no longer only by description.
`../lab-bridge/test.mjs` **imports them** and runs the same scenarios through
both models, so a change to a gate or a rejection name in the lab turns this
workbench red. Until 2026-08-15 this section was the only link between the two,
and a table in a notes file cannot go stale loudly.

The lab-side write-up is `explorations/X11-field-guide-deployment.md` in that
repo, which reports back what survived deployment and what did not.

This is runtime 07 moved from a community of agents into a city of walking
players.

| Lab (runtime 07) | Here | Note |
|---|---|---|
| `joinCommunity` → M-DID via nullifier | `avatar()` | **Weaker.** OASIS avatars are not personhood-anchored; lab gate G2 has no analogue. See counter-spec §7. |
| `encounter()` — shared matching compression | `offer` + `accept` nonces + tag | The proverb becomes a QR. |
| `Mage.propose` | `accept()` | The scanner proposes the smallest edge. |
| `Swordsman.prove` | `confirm()` | The offerer recomputes and signs. Same Gap. |
| G1 mutual consent | gate 3 / M1 | Identical. |
| G3 self-edge | gate 2 / M3 | Identical. |
| G4 R-DID freshness | `rdid()` / M9, P7 | Extended: the R-DID is what the overlay *shows*, not just what the edge stores. |
| G7 forged commitment | gate 7 / M7 | Identical. |
| G6 duplicate edge | gate 8 / M8 | Identical. |
| G8 propagation via `connected()` | **deliberately absent** | The lab asks whether trust *reaches*. The overlay asks who may *see*. Those are different questions and conflating them is how a trust score gets built by accident. |

That last row is the substantive divergence. Transitive reachability is a real
property of a trust graph and runtime 07 is right to model it. It just must not
be the thing that answers "whose pins go on my map" — see counter-spec §3.1.

## Three gates the lab model does not have

Physical meeting introduces failure modes a proverb exchange does not:

- **freshness** (`meet-offer-expired`) — an offer is a moment. TTL 120 s.
- **replay** (`meet-offer-replayed`) — nonces are single-use, so a photographed
  QR is already spent.
- **co-location** (`meet-not-colocated`) — 50 m. Asserted by the client, which is
  a stated limit, not a proof. Counter-spec §7.

## Things found by writing the tests

- **Aliasing must migrate, not map.** K4 failed on the first run: a lookup-only
  alias splits one player's pre-claim and post-claim witnesses into two holons
  with a `witnessCount` that misreports both. Fixed in `knowledge.mjs`; this is a
  live bug in any lookup-only implementation.
- **A deny-list cannot be tested.** The first draft of `promise.mjs` stripped
  named fields. P2 — bolt a junk field onto a holon, assert it never surfaces —
  is unwritable against a deny-list, because a deny-list passes it by ignoring
  the field. Inverting to a closed allow-list is what made the property
  expressible, and the property is worth more than the ten lines it cost.
- **A default ceiling of `link` makes grants meaningless.** P6 caught it: if every
  holon caps at `link`, granting someone `acquaintance` silently does nothing.
  Default ceiling is now `acquaintance`, with quest pins at `link`.
- **A wiki fork is a quantifier change, not an audience.** Writing `story.mjs`
  is what surfaced it: the Promise ladder is scoped to a counterparty, a
  federated page is not, and `public` — the *least* private rung, the one a
  cautious player picks — is the exact rung a naive fork path would read as
  permission to publish worldwide. Publication became its own consent, and
  `WORLD` is deliberately not on the ladder so it cannot be reached by widening.
- **Two languages round differently and neither is wrong.** The Python consumer
  found it on `pj-halfway`: JS `Math.round` is half-up, Python `round` and C#
  `Math.Round` are half-to-even, and the same pin lands ~110 m apart. This is the
  entire argument for writing a second-language consumer instead of asserting
  interop. The vector now sits on the boundary on both axes.
- **The display name undoes the pairwise R-DID.** Added after reading
  `ARWORLD_TRUST_WEIGHTED_POI` §4.2, which returns `peerAvatarId` and
  `peerDisplayName` on every overlay pin. All the care in `rdid()` buys nothing
  if a global name rides alongside it — two viewers just join on the name. D2 is
  the property that catches it: take two viewers' projections of the same pin and
  assert *no* identifier field is equal between them. The fix (a face chosen per
  edge at meet time) is smaller than the leak, and better product.

## Open, not modelled

- ZK. This proves the relations exist, not that they can be proven in zero
  knowledge. The circuit question is downstream and does not block the demo.
- **Edge** erosion and revocation. Discoveries now erode (`erosion.mjs`, half-life
  90 days, floor 0.25) but a TrustLink does not: once formed it is permanent, and
  a meet from four years ago is not a meet from Tuesday. There is no unfriend
  path either. Both belong in a second pass and both are straightforward — the
  horizon machinery already exists, it just is not applied to the edge.
- Observer leakage budget. `runtimes/quiet-presentation` is the right lens on the
  overlay: what does a peer learn from the *pattern* of pins, independent of any
  single projection? Not modelled here.
- Steward edges. `stewardRedeem` returns a receipt and stops. The asymmetric
  player→venue disclosure object it gestures at is unbuilt.
