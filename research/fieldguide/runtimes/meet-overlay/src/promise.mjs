// PROMISE — what a peer's peek may show. Handoff §10 open problem 2.
//
// Today `nearby` only strips notes for `public`, and the card falls back to the
// bootstrap disclosure tokens (`max-public`, `max-link`). That is a policy on
// the AVATAR. What the spec wants — and what this models — is a policy per
// PoiDiscovery, evaluated per audience, applied as a CLOSED allow-list.
//
// The closed allow-list is the whole point. A deny-list leaks by omission: the
// day someone adds `questId` or `deviceModel` to the holon, a deny-list ships
// it and a test written against a deny-list still passes. Here the projection
// starts empty and copies in only named fields, so a new holon field is
// invisible until somebody deliberately names it. `test.mjs` asserts that by
// bolting a junk field onto a holon and checking it never surfaces.
//
// Two rulings this file makes, both of them opinionated:
//
//  1. AUDIENCE IS GRANTED, NOT COMPUTED. A 1-hop TrustLink gets you `link`.
//     Nothing gets you `acquaintance` except the owner handing it to you. And
//     graph distance never raises an audience — 2 hops is not "half of link",
//     it is nothing. This is what "no central trust score" means when you make
//     it mechanical: distance is not a currency.
//
//  2. THE PEER REFERENCE IS PAIRWISE. A projection carries the owner's R-DID
//     toward this viewer, never the raw avatarId. Two viewers who both see
//     Mitch's pins hold two unjoinable references to him.

import { coarse } from './geo.mjs';
import { rdid } from './identity.mjs';

// Closed, ordered, additive. Each tier is a superset of the one before it.
export const AUDIENCES = ['private', 'public', 'link', 'acquaintance'];

const PUBLIC_FIELDS = ['poiId', 'title', 'placeKind', 'lat', 'lon', 'markerStyle'];
const LINK_FIELDS = [...PUBLIC_FIELDS, 'wikiSlug', 'rite', 'trail', 'witnessedUtc'];
const ACQUAINTANCE_FIELDS = [...LINK_FIELDS, 'note'];

export const ALLOW = {
  private: [],
  public: PUBLIC_FIELDS,
  link: LINK_FIELDS,
  acquaintance: ACQUAINTANCE_FIELDS,
};

// Named so a leak test can assert against the list rather than a vibe.
export const NEVER_PROJECTED = [
  'questId',
  'questPinRole',
  'source',
  'client',
  'avatarId',
  'parent',
  'holonId',
  'witnessCount',
  'disclosure',
  'kind',
  'trustgraph_kind',
  // The two that undo everything else. `peerAvatarId` is the raw guid the
  // current /poi/nearby response returns; `displayName` is a global profile
  // name. Either one lets two viewers who have both met the same person join
  // their views and reconstruct a trail the pairwise R-DID was there to split.
  // A display name still reaches the player — but off the EDGE, not the
  // profile. See project()'s `presentation` argument and property P10.
  'peerAvatarId',
  'displayName',
];

const rank = (a) => AUDIENCES.indexOf(a);

// The per-holon policy. `null` means "use the default for this source".
// A player marking one pin private is `{ maxAudience: 'private' }` and it
// disappears from every peer's map without touching any other pin.
export function policyFor(holon) {
  if (holon.disclosure) return holon.disclosure;
  // Default ceiling is `acquaintance` — the owner can hand out everything they
  // hold, but only by granting it. Quest pins default one tier tighter: a quest
  // pin says what you are DOING, not just where you are, so its note never
  // leaves the owner regardless of who they befriend.
  if (holon.source === 'quest') return { maxAudience: 'link' };
  return { maxAudience: 'acquaintance' };
}

// What audience does `viewer` hold on `owner`'s Knowledge?
// Returns null when the viewer holds nothing — the pin is simply not there.
export function audienceFor(graph, ownerAvatarId, viewerAvatarId) {
  if (ownerAvatarId === viewerAvatarId) return 'self';
  const granted = graph.grantedAudience(ownerAvatarId, viewerAvatarId);
  if (granted) return granted;
  if (graph.isOneHop(ownerAvatarId, viewerAvatarId)) return 'link';
  return null; // no edge, no grant: not in fromGraph at all
}

// The Mage projection of one discovery, for one audience. Closed allow-list.
export function project(
  holon,
  audience,
  { ownerNode = null, viewerAvatarId = null, presentation = null } = {},
) {
  const policy = policyFor(holon);
  const capped = rank(audience) > rank(policy.maxAudience) ? policy.maxAudience : audience;
  if (capped === 'private' || rank(capped) < 1) return null;

  const allowed = ALLOW[capped].filter((f) => !(policy.deny || []).includes(f));
  const out = {};
  for (const f of allowed) {
    if (holon[f] !== undefined) out[f] = holon[f];
  }
  if (capped === 'public') {
    // Coarse geo: enough to say Islington, not enough to say this doorway.
    if (out.lat !== undefined) out.lat = coarse(out.lat);
    if (out.lon !== undefined) out.lon = coarse(out.lon);
  }
  // Wire names follow ARWORLD_TRUST_WEIGHTED_POI §4.2 (`origin`, `audience`).
  // Note for Max: that spec and the handoff's §7.2 TrailPin table disagree —
  // TrailPin calls them `trustOrigin` / `trustAudience`. One of the two should
  // give. I have followed the API doc and left the rename to Unity's mapper.
  out.origin = 'trust';
  out.audience = capped;
  // Peer attribution is a `link`-and-above field. Found by ARWORLD_TRUST_
  // WEIGHTED_POI §6's own acceptance checklist: "peek on overlay shows peer name
  // when audience=link" — which means at `public` it must NOT, and §3.2 spells
  // public out as "title + kind + lat/lon only". The first draft attached the
  // name at every tier, which quietly published *who* alongside *where* at the
  // one tier meant to say least. A public pin is anonymous: something was
  // witnessed here, by nobody you are told about.
  if (rank(capped) >= rank('link')) {
    // Pairwise, not the raw avatarId — see ruling 2 above.
    if (ownerNode && viewerAvatarId) out.peerRef = rdid(ownerNode, viewerAvatarId);
    // The face the owner chose for THIS viewer, taken off their shared edge.
    if (presentation) out.peerDisplayName = presentation;
  }
  return out;
}
