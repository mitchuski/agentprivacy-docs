// The questions in the ARWorld pack that had only prose answers, given
// runnable ones. Three of them, each quoted where it is answered.

import { H } from '../../meet-overlay/src/hash.mjs';

// ---------------------------------------------------------------------------
// ARWORLD_DISCOVERY §10.1
//   "Must discovery always require camera on device, or is GPS-in-radius +
//    hold-to-Witness enough outdoors?"
//
// Answer: no, and the question is better asked one layer down. Both rites are
// real discoveries — §8.2's "one rite, two skins" already settles that — so the
// graph should not pick. What the graph owes you is that the holon RECORDS
// which rite happened, and that anything with a stake can set its own bar.
//
// A trail mark and a till redeem are not the same stake. Let the redeem require
// a camera fetch while the trail accepts a desk witness, and neither has to win
// the argument globally.
// ---------------------------------------------------------------------------
export const RITE_ASSURANCE = {
  'desk-witness': 1, // in radius, deliberate, no lens
  'camera-fetch': 2, // in radius, deliberate, and something was seen
  seal: 2,           // a parish pin; a deliberate mark
  banish: 1,         // an omen dismissed
};

export function riteAdmits(rite, { minAssurance = 1 } = {}) {
  const a = RITE_ASSURANCE[rite];
  if (a === undefined) return { admitted: false, reason: `unknown-rite:${rite}` };
  if (a < minAssurance) return { admitted: false, reason: 'rite-below-required-assurance' };
  return { admitted: true, assurance: a };
}

// Consumers declare their own bar rather than the graph declaring one for them.
export const CONSUMER_BARS = {
  trail: 1,        // your own map: a desk witness is a discovery
  overlay: 1,      // a peer's map: same
  storyRelease: 1, // unlock a story at the pin
  tillRedeem: 2,   // money changes hands; ask for the lens
};

// ---------------------------------------------------------------------------
// ARWORLD_DISCOVERY §10.4
//   "Photo retained? v1: proof-of-presence without storing image; later
//    optional MediaHolon under Knowledge."
//
// Answer: v1 keeps the proof and drops the image, as they propose. Modelled so
// that "we forgot to delete it" is a failing test rather than an incident.
//
// A camera fetch yields a *presence digest* — enough to say a capture happened,
// not enough to reconstruct what was captured. If a MediaHolon ever lands, it
// inherits the publication rule from story.mjs: an image is not an audience
// tier away from the world, it is its own consent, and it is never projected.
// ---------------------------------------------------------------------------
export function captureProof(rite, imageBytes, { salt }) {
  if (rite !== 'camera-fetch') return { proof: null, retained: false };
  // One-way, salted, and the bytes are dropped on the floor immediately.
  return {
    proof: H('arworld/presence/v0', salt, String(imageBytes?.length ?? 0)),
    retained: false,
    imageBytes: undefined,
  };
}

export function attachMedia(holon, media, { mediaConsent = false }) {
  if (!mediaConsent) return { attached: false, reason: 'no-media-consent' };
  return {
    attached: true,
    holon: { ...holon, media: { ...media, kind: 'MediaHolon', neverProjected: true } },
  };
}

// ---------------------------------------------------------------------------
// ARWORLD_TRUST_WEIGHTED_POI §9.4
//   "Sharedrops / Launchboard: later, same edge type as cap-table trust …
//    without mixing equity into the map UI."
//
// Answer: the "without mixing equity into the map" half is right and the "same
// edge type" half should be refused. An edge that means *we met in London* and
// an edge that means *you hold equity* are different claims with different
// consequences, and one object carrying both means any surface reading edges
// can accidentally read the other kind.
//
// Keeping the map clean is a UI decision, and UI decisions get revisited by
// someone who was not in the room. Keeping the KINDS separate is structural: a
// sharedrop claim simply cannot be derived from a social edge, so nobody has to
// remember not to.
// ---------------------------------------------------------------------------
export const EDGE_KINDS = ['TrustLink']; // closed. Social edges only.

export function deriveSharedropClaim(edge) {
  if (edge.kind === 'TrustLink') {
    return { claim: null, reason: 'edge-kind-not-economic' };
  }
  return { claim: null, reason: `unknown-edge-kind:${edge.kind}` };
}

// What the map is allowed to read off an edge. Closed, so an equity field added
// to the edge later cannot reach a pin.
export const MAP_READABLE_EDGE_FIELDS = ['a', 'b', 'presentA', 'presentB', 'formedUtc'];
