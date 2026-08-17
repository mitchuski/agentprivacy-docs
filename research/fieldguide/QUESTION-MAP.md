# Question map — every question in the ARWorld pack, and what answers it

*Twenty questions across Max's three documents. Each row names the properties that
answer it, and those anchors are checked: `runtimes/questions/test.mjs` runs the
suites and fails if a question has no property, if an anchor does not resolve, or
if the inventory drifts from twenty.*

The point of the check is the middle column of the failure mode. It is easy to
answer a question in prose and believe it is handled; it is hard to keep believing
that when a suite says the row is empty.

Sources: `MITCH_ARWORLD_FIELD_GUIDE_HANDOFF.md` §10 · `ARWORLD_TRUST_WEIGHTED_POI.md`
§6 and §9 · `ARWORLD_DISCOVERY.md` §10.

Run: `cd runtimes && node verify.mjs`

---

## Handoff §10 — "What we want you to propose"

| # | The question | The answer | Held by |
|---|---|---|---|
| **Q-H1** | "Fixture vs live Trust. How should 1-hop edges actually be created for two Hitchhikers who meet in London?" | A co-located, expiring, single-use, bilaterally consented QR meet → one `TrustLink`. Eight gates. | `prop:M1` `prop:M2` `prop:M3` `prop:M4` `prop:M5` `prop:M6` `prop:M7` `prop:M8` `prop:M9` |
| **Q-H2** | "Promise on discoveries. Should Mage project title/kind/geo on `link` by default? How do we avoid leaking `questId` / notes?" | Yes to title/kind/geo/exact position at `link`. A **closed allow-list**, not a strip-list, so a field added later cannot leak by omission. | `prop:P1` `prop:P2` `prop:P3` `prop:P8` |
| **Q-H3** | "Self list / passport. Anything missing on the holon for a reinstall to restore 'places I Witnessed'?" | Nothing, once `disclosure` is added. The holon carries every field Unity stamps and a restore is lossless over that set. | `prop:K5` |
| **Q-H4** | "Id remap. Alias table vs new `poiId`? Field Guide must not invent ids." | Alias table, resolved server-side — but as a **migration, not a lookup**, or the same player's pre- and post-claim visits split into two holons. | `prop:K4` |
| **Q-H5** | "Mage card vs place proof. Is person card + FedWiki slug enough?" | Enough. A place-level projection would be a third identifier for a thing that already has two. The card is an r-card; see the cred-spec note. | `prop:W5` |
| **Q-H6** | "Shared quest as Trust edge. Is that enough 1-hop for overlay without a Meet ceremony?" | **No.** Co-completion is co-presence with a timestamp and no consent. It should prompt a meet, not be one. | `prop:M10` |
| **Q-H7** | "Swordsman parent. Is that the right Knowledge home?" | Yes — and that is exactly why the projection must be computed at read time rather than stored. | `prop:N2` `prop:N6` `prop:N8` |

## ARWORLD_TRUST_WEIGHTED_POI §9 — open questions

| # | The question | The answer | Held by |
|---|---|---|---|
| **Q-T1** | "Is witness = quest check-in only, or also tap-to-peek 'Save to trail'?" | Both, through **one rite**. A save that skips the rite is a second meaning of discovery. Consumers with a stake may set a higher bar. | `prop:K3` `prop:Q1a` `prop:Q1c` `prop:Q1d` |
| **Q-T2** | "Default Promise: are discoveries `link`-visible or `acquaintance`-only until the user toggles?" | `link`-visible for title/kind/geo/slug; the note needs an explicit grant. Ceiling defaults to `acquaintance` so a grant means something. | `prop:P4` `prop:P6` `prop:P9` |
| **Q-T3** | "Should overlay pins require the peer to be 'recent' (e.g. witnessed in last 90 days)?" | Yes, but as a **rate with a floor**, not a cliff. 90-day half-life, drop below 0.25. Your own trail never erodes. | `prop:E1` `prop:E2` `prop:E3` `prop:E4` `prop:E5` |
| **Q-T4** | "Sharedrops / Launchboard: later, same edge type as cap-table trust… without mixing equity into the map UI." | Keep the second half, refuse the first. **Different kinds**, so an economic claim cannot be derived from a social edge and the map cannot read one. | `prop:Q3a` `prop:Q3b` `prop:Q3c` `prop:Q3d` |

## ARWORLD_TRUST_WEIGHTED_POI §6 — "Acceptance for Phase 0"

Their checklist, run rather than read.

| # | The criterion | Status | Held by |
|---|---|---|---|
| **Q-A1** | "With fixture on, map near Islington shows floor pins **and** at least 2 overlay pins tagged Maya/Jon." | executable | `prop:A1` |
| **Q-A2** | "Overlay pins are within `spawnRadiusM` of player." | executable | `prop:A2` `prop:R2` |
| **Q-A3** | "Peek on overlay shows peer name when `audience=link`." | executable — and it **found a bug**: peer attribution was reaching `public` too | `prop:A3` |
| **Q-A4** | "Fixture off → behaviour equals today's floor-only CityPOI." | executable, as an exact equivalence | `prop:A4` |
| **Q-A5** | "No fake 'trust score' UI." | executable, structurally: a pin may carry only known numeric fields | `prop:A5` `prop:R5` `prop:R8` |

## ARWORLD_DISCOVERY §10 — open questions

| # | The question | The answer | Held by |
|---|---|---|---|
| **Q-D1** | "Must discovery always require camera on device, or is GPS-in-radius + hold-to-Witness enough outdoors?" | No — and the question belongs one layer down. Both rites are real; the holon records which; anything with a stake sets its own bar. | `prop:Q1a` `prop:Q1b` `prop:Q1c` `prop:Q1d` |
| **Q-D2** | "Can a partner **reject** anonymous OSM duplicates of their venue (replace pin id)?" | Yes. The claim registers an alias and migrates existing Knowledge; the client never learns anything changed. | `prop:K4` |
| **Q-D3** | "Does redeem at till create a TrustLink (player ↔ steward), or only a receipt holon?" | A receipt. A `TrustLink` is symmetric and these parties are not. | `prop:S1` |
| **Q-D4** | "Photo retained? v1: proof-of-presence without storing image; later optional MediaHolon." | Their v1 answer, made mechanical: a salted presence proof, image dropped. A `MediaHolon` needs its own consent and is never projected. | `prop:Q2a` `prop:Q2b` `prop:Q2c` `prop:Q2d` `prop:Q2e` |

---

## Also answered, though nobody asked

Their §5 score-terms table was specification, not a question — but it was unimplemented,
and a ranking rule that only exists in a table is a rule nobody can break a test on.

| Term | Held by |
|---|---|
| distance is the primary sort | `prop:R1` |
| the hard cut is on true distance, so no band drags a far pin in | `prop:R2` |
| `trustOverlay` is worth something | `prop:R3` |
| …but bounded: it is a band, not a promotion | `prop:R4` |
| "this is not Yelp" — rank never depends on other people's counts | `prop:R5` |
| memorial/plaque clutter filtered | `prop:R6` |
| the cap applies after ranking, not before | `prop:R7` |
| origin changes the marker style and nothing else | `prop:R8` |
