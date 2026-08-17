// KNOWLEDGE — `POST /api/trustgraph/poi/witness` (place).
//
// A PoiDiscovery holon is the record that an avatar Witnessed a place. It is
// the game's Knowledge layer, already live (handoff §2 P1). Modelled here for
// two reasons: the overlay reads it, and two of Max's open problems live in it.
//
//   §10.3 passport / reinstall  — the holon must carry everything Unity stamps
//                                 locally, or a reinstall loses the trail.
//   §10.4 id remap             — a partner claims an OSM node. The client must
//                                 NOT invent a second id, so the remap is an
//                                 alias resolved server-side.
//
// Invariants held here: idempotent on (avatarId, poiId); Witness records a
// connection to a pin that already has a stable poiId, it never spawns one.

import { H } from './hash.mjs';
import { toIso, fromIso } from './time.mjs';

const DOMAIN_HOLON = 'arworld/poi-discovery/v0';

// Everything Unity's FieldPassport stamps locally, so `self` is a true restore
// path and not a lossy summary. If Unity starts stamping a new field, it goes
// here too or the reinstall silently drops it.
export const PASSPORT_FIELDS = [
  'poiId',
  'title',
  'placeKind',
  'lat',
  'lon',
  'source',
  'rite',
  'trail',
  'questId',
  'questPinRole',
  'wikiSlug',
  'markerStyle',
  'note',
  'witnessedUtc',
];

export const RITES = ['desk-witness', 'camera-fetch', 'seal', 'banish'];
export const SOURCES = ['city-discover', 'quest', 'seed', 'demo', 'partner'];

export class Knowledge {
  constructor() {
    this.holons = new Map(); // "avatarId|poiId" -> holon
    this.aliases = new Map(); // aliasPoiId -> canonicalPoiId
  }

  // §10.4 — a partner venue claims an OSM node. The client keeps sending
  // `poi-osm-way-123`; the server resolves it to the canonical id. One holon,
  // one witnessCount, no second id minted anywhere.
  //
  // An alias is a MIGRATION, not just a lookup. Found by a failing test: if
  // alias() only registered the mapping, a player who Witnessed the pub before
  // the partner claimed it and again afterwards ends up with two holons and a
  // witnessCount that lies about both. Claiming a node has to carry the
  // existing Knowledge across with it.
  alias(fromPoiId, toPoiId) {
    this.aliases.set(fromPoiId, toPoiId);
    const canonical = this.resolve(fromPoiId);
    for (const [key, h] of [...this.holons]) {
      if (h.poiId !== fromPoiId) continue;
      this.holons.delete(key);
      h.poiId = canonical;
      h.holonId = H(DOMAIN_HOLON, h.avatarId, canonical);
      const newKey = `${h.avatarId}|${canonical}`;
      const target = this.holons.get(newKey);
      if (target) {
        // Both ids already witnessed by this avatar: one place, one holon.
        target.witnessCount += h.witnessCount;
        if (fromIso(h.witnessedUtc) < fromIso(target.witnessedUtc)) {
          target.witnessedUtc = h.witnessedUtc; // keep the earliest visit
        }
      } else {
        this.holons.set(newKey, h);
      }
    }
  }
  resolve(poiId) {
    const seen = new Set();
    let id = poiId;
    while (this.aliases.has(id) && !seen.has(id)) {
      seen.add(id);
      id = this.aliases.get(id);
    }
    return id;
  }

  // POST /poi/witness. Avatar from JWT only. Idempotent on (avatarId, poiId).
  witness(avatarId, payload, { nowUtc }) {
    const required = ['poiId', 'title', 'placeKind', 'lat', 'lon', 'source'];
    for (const f of required) {
      if (payload[f] === undefined || payload[f] === null || payload[f] === '') {
        return { ok: false, reason: `missing-required-field:${f}` };
      }
    }
    if (!SOURCES.includes(payload.source)) {
      return { ok: false, reason: `unknown-source:${payload.source}` };
    }
    if (payload.rite && !RITES.includes(payload.rite)) {
      return { ok: false, reason: `unknown-rite:${payload.rite}` };
    }

    const poiId = this.resolve(payload.poiId);
    const key = `${avatarId}|${poiId}`;
    const existing = this.holons.get(key);
    if (existing) {
      existing.witnessCount += 1;
      return {
        ok: true,
        created: false,
        poiId,
        holonId: existing.holonId,
        witnessedUtc: existing.witnessedUtc,
        witnessCount: existing.witnessCount,
      };
    }

    const holon = {
      kind: 'PoiDiscovery',
      trustgraph_kind: 'PoiDiscovery',
      holonId: H(DOMAIN_HOLON, avatarId, poiId),
      avatarId,
      // parent = Swordsman when TrustGraph is bootstrapped, else the avatar.
      // §10.7: Knowledge is full-context, so it homes under the Swordsman; the
      // Mage is the projection of it, minted per audience in promise.mjs.
      parent: 'swordsman',
      // ISO-8601 on the wire, per ARWORLD_TRUST_WEIGHTED_POI §3.1
      witnessedUtc: payload.witnessedUtc ?? toIso(nowUtc),
      witnessCount: 1,
      disclosure: payload.disclosure ?? null, // per-holon Promise; null = default
    };
    for (const f of PASSPORT_FIELDS) {
      if (payload[f] !== undefined) holon[f] = payload[f];
    }
    holon.poiId = poiId;
    this.holons.set(key, holon);
    return {
      ok: true,
      created: true,
      poiId,
      holonId: holon.holonId,
      witnessedUtc: holon.witnessedUtc,
      witnessCount: 1,
    };
  }

  mine(avatarId) {
    return [...this.holons.values()].filter((h) => h.avatarId === avatarId);
  }

  // §10.3 — what a reinstalled client gets back. Server is source of truth
  // after 2xx; local prefs are cache.
  restorePassport(avatarId) {
    return this.mine(avatarId).map((h) => {
      const out = {};
      for (const f of PASSPORT_FIELDS) {
        if (h[f] !== undefined) out[f] = h[f];
      }
      return out;
    });
  }
}
