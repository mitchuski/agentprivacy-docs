// THE OVERLAY — `GET /api/trustgraph/poi/nearby`, with the fixture removed.
//
// The query rule from handoff §3 / ARWORLD_TRUST_WEIGHTED_POI §3.3, now
// executable on both sides:
//
//     TrustEdge(A, B) AND DisclosurePolicy(B, audienceForA).allows(fields)
//
// Phase A satisfies the left side with a Maya/Jon JSON file. Here the left side
// is meet.mjs (a real, co-located, bilaterally consented TrustLink) and the
// right side is promise.mjs (a per-holon closed allow-list). `fixture` is not a
// parameter of this function, because once both sides exist there is nothing
// for it to stand in for. An empty `fromGraph` is the honest answer when you
// have not met anyone yet.
//
// Response shape follows ARWORLD_TRUST_WEIGHTED_POI §4.2.
//
// Invariants carried from handoff §11:
//   - distance-first; the overlay must not pull Greenwich into an Islington
//     viewport
//   - cap the overlay count (Unity: 12)
//   - peek never shows raw Swordsman context

import { metresBetween } from './geo.mjs';
import { audienceFor, project, AUDIENCES } from './promise.mjs';

// ARWORLD_TRUST_WEIGHTED_POI §4.2: the caller may pass `audience=`, and the
// server masks "per peer policy for that audience (or stricter of
// link/acquaintance)". So the query parameter is a CEILING the caller accepts,
// never a claim that raises them — asking for `acquaintance` when the owner
// granted you `link` gets you `link`, silently and correctly.
const stricter = (a, b) =>
  AUDIENCES.indexOf(a) <= AUDIENCES.indexOf(b) ? a : b;
import { freshness, aboveHorizon } from './erosion.mjs';

export const DEFAULT_CAP = 12;

export function nearby(
  { knowledge, graph, nodes },
  viewerAvatarId,
  { lat, lon, radiusM = 2200, cap = DEFAULT_CAP, nowUtc, explain = false, audience: requested },
) {
  const dist = (h) => metresBetween(lat, lon, h.lat, h.lon);
  const inRadius = (h) => dist(h) <= radiusM;
  // Every pin that could have appeared and did not, with the reason named from
  // the closed register. A desk demo where the overlay is empty should be able
  // to say WHY in one call rather than by bisecting the query.
  const excluded = [];
  const drop = (h, reason) => explain && excluded.push({ poiId: h.poiId, reason });

  // --- self: the caller's own trail. Full fields, and it never erodes —
  //     erosion is about how much a peer's old enthusiasm should move you,
  //     not about whether you were there. ---
  const self = knowledge
    .mine(viewerAvatarId)
    .filter(inRadius)
    .sort((p, q) => dist(p) - dist(q))
    .map((h) => ({
      poiId: h.poiId,
      title: h.title,
      placeKind: h.placeKind,
      lat: h.lat,
      lon: h.lon,
      wikiSlug: h.wikiSlug,
      rite: h.rite,
      trail: h.trail,
      markerStyle: h.markerStyle,
      note: h.note,
      witnessedUtc: h.witnessedUtc,
      witnessCount: h.witnessCount,
      origin: 'self',
    }));

  // --- fromGraph: 1-hop peers only, each pin projected at the audience that
  //     peer granted this viewer, eroded, then distance-first and capped. ---
  const candidates = [];
  for (const [, holon] of knowledge.holons) {
    if (holon.avatarId === viewerAvatarId) continue;
    if (!inRadius(holon)) {
      drop(holon, 'out-of-radius');
      continue;
    }
    const granted = audienceFor(graph, holon.avatarId, viewerAvatarId);
    const audience = granted && requested ? stricter(granted, requested) : granted;
    if (!audience || audience === 'self') {
      drop(holon, 'no-trust-edge');
      continue;
    }
    // §9.3 recency, as a rate with a floor under it rather than a cliff.
    if (nowUtc !== undefined && !aboveHorizon(holon.witnessedUtc, nowUtc)) {
      drop(holon, 'below-freshness-horizon');
      continue;
    }
    const pin = project(holon, audience, {
      ownerNode: nodes.get(holon.avatarId) || null,
      viewerAvatarId,
      presentation: graph.presentationOf(holon.avatarId, viewerAvatarId),
    });
    if (!pin) {
      drop(holon, 'audience-capped-private');
      continue;
    }
    if (nowUtc !== undefined) {
      // Unity fades the ring by this rather than popping the pin.
      pin.freshness = Number(freshness(holon.witnessedUtc, nowUtc).toFixed(4));
    }
    candidates.push({ pin, d: dist(holon) });
  }

  const ranked = candidates.sort((p, q) => p.d - q.d);
  for (const c of ranked.slice(cap)) {
    if (explain) excluded.push({ poiId: c.pin.poiId, reason: 'over-overlay-cap' });
  }
  const fromGraph = ranked.slice(0, cap).map((c) => c.pin);

  const out = { ok: true, radiusM, self, fromGraph, fixture: false, cap };
  if (explain) out.excluded = excluded;
  return out;
}
