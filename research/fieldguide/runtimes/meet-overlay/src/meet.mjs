// THE MEET RITE — `POST /witness` (person), not `/poi/witness` (place).
//
// This is the answer to handoff §10 open problem 1: how a 1-hop edge actually
// gets created for two Hitchhikers who meet in London, so `nearby` can drop the
// Maya/Jon fixture flag.
//
// It is runtimes/07-trust-graph-formation ported to the game's physical
// setting. The lab model proves the RELATIONS (bilateral consent, R-DID
// uniqueness, no self-edge, the Gap). What the physical world adds is that the
// shared "matching compression" is not a proverb — it is a co-located, expiring,
// single-use QR exchange. Three gates the lab model does not have:
//
//   co-location  the two avatars were within meetRadiusM of each other
//   freshness    the offer had not expired
//   replay       the offer nonce is single-use
//
// Structure of the rite, mirroring the Witness pipeline (§5) so it reads the
// same way to a player:
//
//   A opens Meet          -> offer(A)            QR on screen
//   B scans the QR        -> accept(B, offer)    B has consented
//   A confirms on device  -> confirm(A, accept)  A has consented -> edge
//
// The scan alone is an ENCOUNTER, not an edge. Peeking is encounter only (§1),
// and so is scanning: an edge needs both hands.

import { H, pair } from './hash.mjs';
import { rdid } from './identity.mjs';
import { metresBetween } from './geo.mjs';

const DOMAIN_OFFER = 'arworld/meet-offer/v0';
const DOMAIN_SHARED = 'arworld/meet-shared/v0';
const DOMAIN_LINK = 'arworld/trust-link/v0';

export const MEET_TTL_SEC = 120; // a QR on a screen between two people
export const MEET_RADIUS_M = 50; // "we are standing together", not "same borough"

// ---------------------------------------------------------------------------
// Step 1 — A opens Meet. The offer is what the QR encodes.
// ---------------------------------------------------------------------------
// `presentAs` is the face A chooses to show THIS counterparty — the Mage
// projection made literal at the person layer. It is per-edge, not per-profile,
// which is what keeps the pairwise R-DID from being undone by a global display
// name (see promise.mjs and property P10).
export function offer(nodeA, { nonce, lat, lon, nowUtc, presentAs = null }) {
  return {
    kind: 'MeetOffer',
    a: nodeA.avatarId,
    nonce,
    lat,
    lon,
    presentAs,
    issuedUtc: nowUtc,
    expiresUtc: nowUtc + MEET_TTL_SEC,
    tag: H(DOMAIN_OFFER, nodeA.avatarId, nonce, nowUtc),
  };
}

// ---------------------------------------------------------------------------
// Step 2 — B scans. B derives the shared compression and consents. B cannot
// mint the edge: this is a proposal (the Mage's smallest reduction).
// ---------------------------------------------------------------------------
export function accept(nodeB, off, { nonce, lat, lon, nowUtc, consent = true, presentAs = null }) {
  const [x, y] = pair(off.a, nodeB.avatarId);
  const shared = H(DOMAIN_SHARED, x, y, off.nonce, nonce, off.tag);
  return {
    kind: 'MeetAccept',
    offer: off,
    b: nodeB.avatarId,
    nonceB: nonce,
    lat,
    lon,
    presentAs,
    scannedUtc: nowUtc,
    consentB: consent,
    shared,
    rdidB: rdid(nodeB, off.a),
    claimedLink: H(DOMAIN_LINK, x, y, shared),
  };
}

// ---------------------------------------------------------------------------
// Step 3 — A confirms. A is the Swordsman here: A recomputes everything from
// public parts and never trusts the scanner's claimedLink (the Gap). Only a
// validated, mutually consented, co-located, fresh, unreplayed meet signs.
// ---------------------------------------------------------------------------
export function confirm(nodeA, acc, graph, { nowUtc, consent = true }) {
  const reject = (reason) => ({ formed: false, reason });
  const off = acc.offer;

  // 1. the confirmer must be the avatar who opened the meet
  if (off.a !== nodeA.avatarId) return reject('offer-not-mine');
  // 2. no self-edge — a TrustLink with oneself is self-Sybil, not a relationship
  if (off.a === acc.b) return reject('self-edge-forbidden');
  // 3. bilateral consent — the graph grows ONLY when both hands are on it
  if (!acc.consentB || !consent) return reject('unilateral-no-mutual-consent');
  // 4. freshness — an offer is a moment, not a credential you keep in a wallet
  if (acc.scannedUtc > off.expiresUtc || nowUtc > off.expiresUtc) {
    return reject('meet-offer-expired');
  }
  // 5. replay — the nonce is single-use, so a photographed QR is spent
  if (graph.nonceSeen(off.a, off.nonce)) return reject('meet-offer-replayed');
  // 6. co-location — the rite is physical, like every other Witness in the game
  if (metresBetween(off.lat, off.lon, acc.lat, acc.lon) > MEET_RADIUS_M) {
    return reject('meet-not-colocated');
  }
  // 7. the Gap — recompute the link commitment from public parts; do not trust
  //    the scanner's assertion (non-collusion between proposer and prover)
  const [x, y] = pair(off.a, acc.b);
  const link = H(DOMAIN_LINK, x, y, acc.shared);
  if (link !== acc.claimedLink) return reject('link-commitment-forged');
  // 8. one TrustLink per pair — idempotent
  if (graph.hasLink(off.a, acc.b)) return reject('duplicate-link');

  const holon = {
    kind: 'TrustLink',
    trustgraph_kind: 'TrustLink',
    a: off.a,
    b: acc.b,
    rdidA: rdid(nodeA, acc.b),
    rdidB: acc.rdidB,
    link,
    // Each side's chosen face toward the other. Not a profile field: it lives
    // on the edge, so the same avatar can be "Maya" to one peer and "M." to
    // another with nothing joining the two.
    presentA: off.presentAs,
    presentB: acc.presentAs,
    formedUtc: nowUtc,
    // where it happened, coarsely — a meet has a place, but not a doorway
    placeHint: { lat: Math.round(off.lat * 100) / 100, lon: Math.round(off.lon * 100) / 100 },
  };
  graph.addLink(holon, off.nonce);
  return { formed: true, holon };
}

// ---------------------------------------------------------------------------
// The Trust layer: an accumulating set of signed TrustLink holons. No score.
// ---------------------------------------------------------------------------
export class TrustGraph {
  constructor() {
    this.links = new Map(); // "a|b" (sorted) -> holon
    this.nonces = new Set(); // "avatarId|nonce" — spent offers
    this.grants = new Map(); // "from|to" -> audience explicitly granted
  }
  _key(a, b) {
    return pair(a, b).join('|');
  }
  hasLink(a, b) {
    return this.links.has(this._key(a, b));
  }
  addLink(holon, nonce) {
    this.links.set(this._key(holon.a, holon.b), holon);
    this.nonces.add(`${holon.a}|${nonce}`);
    return true;
  }
  nonceSeen(a, nonce) {
    return this.nonces.has(`${a}|${nonce}`);
  }
  // 1-hop only. Deliberately NOT transitive — see promise.mjs and NOTES.md.
  neighbours(avatarId) {
    const out = [];
    for (const h of this.links.values()) {
      if (h.a === avatarId) out.push(h.b);
      else if (h.b === avatarId) out.push(h.a);
    }
    return out;
  }
  isOneHop(a, b) {
    return this.hasLink(a, b);
  }
  linkFor(a, b) {
    return this.links.get(this._key(a, b)) || null;
  }
  // The face `owner` chose to show `viewer`, read off their shared edge.
  // Null when there is no edge — there is then nobody to show a face to.
  presentationOf(ownerAvatarId, viewerAvatarId) {
    const h = this.linkFor(ownerAvatarId, viewerAvatarId);
    if (!h) return null;
    return h.a === ownerAvatarId ? h.presentA : h.presentB;
  }
  // An upgrade past `link` is GRANTED by the owner, never derived from the graph.
  grant(fromAvatarId, toAvatarId, audience) {
    this.grants.set(`${fromAvatarId}|${toAvatarId}`, audience);
  }
  grantedAudience(fromAvatarId, toAvatarId) {
    return this.grants.get(`${fromAvatarId}|${toAvatarId}`) || null;
  }
}

// ---------------------------------------------------------------------------
// Handoff §10 open problem 6 — "is a shared quest completion enough 1-hop for
// overlay without a Meet ceremony?" This function is the answer, and the answer
// is no. Co-completion yields an ENCOUNTER — a candidate with no consent on it.
// It can prompt a Meet. It cannot be one.
// ---------------------------------------------------------------------------
export function questCoCompletion(avatarIdA, avatarIdB, questId) {
  return {
    kind: 'Encounter',
    reason: 'shared-quest-completion',
    a: avatarIdA,
    b: avatarIdB,
    questId,
    consentA: false,
    consentB: false,
    formsEdge: false,
  };
}

// ---------------------------------------------------------------------------
// ARWORLD_DISCOVERY §10.3 — "does redeem at till create a TrustLink (player <->
// steward), or only a receipt holon?"
//
// A receipt. A till redeem IS co-located and bilateral, so it clears the Meet
// rite's physical gates — but a TrustLink is a SYMMETRIC object, and these two
// parties are not symmetric. A steward is a public-facing counterparty who
// serves hundreds of people a week; a player is one person. Minting a
// TrustLink would put every pilgrim's trail inside the venue's `fromGraph` in
// exchange for a cup of tea, which is a data harvest wearing a loyalty card.
//
// If a steward edge is genuinely wanted later it needs its OWN kind, with
// one-way disclosure (player -> venue, aggregate only) and no reciprocal query
// right. That is a different object, not this one with a flag.
// ---------------------------------------------------------------------------
export function stewardRedeem(avatarId, venueId, { offerId, nowUtc }) {
  return {
    kind: 'RedeemReceipt',
    avatarId,
    venueId,
    offerId,
    redeemedUtc: nowUtc,
    formsEdge: false,
  };
}
