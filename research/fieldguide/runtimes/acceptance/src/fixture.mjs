// The Phase 0 fixture — Maya and Jon — as executable state rather than a file.
//
// ARWORLD_TRUST_WEIGHTED_POI §6 ships two invented peers near the Islington demo
// origin and a §6 acceptance checklist to go with them. That checklist is the
// most obviously runnable thing in the whole pack and it is currently five
// unticked boxes in a markdown file. This suite makes it a test you can run.
//
// The point worth noticing while reading it: **"fixture on" and "fixture off"
// differ only in how the edges got there.** Seeding two consented edges and two
// peers' discoveries produces exactly the state a pair of real meets would.
// That is the strongest argument that the fixture retires cleanly — it is not a
// special code path to be removed later, it is ordinary state arriving by an
// unusual door.

import { avatar } from '../../meet-overlay/src/identity.mjs';
import { toIso } from '../../meet-overlay/src/time.mjs';

export const ISLINGTON = { lat: 51.5344, lon: -0.1016 };
export const SPAWN_RADIUS_M = 2200; // Unity `spawnRadiusM`

export const PLAYER = avatar('avatar-you', 'secret-you');
export const MAYA = avatar('avatar-maya', 'secret-maya');
export const JON = avatar('avatar-jon', 'secret-jon');

// Peers and pins as described in §6: Maya on galleries and quiet pubs, Jon on
// parks and viewpoints, and one self discovery so both ring styles render.
export const PHASE0 = {
  id: 'arworld-trust-poi-phase0',
  peers: [
    {
      node: MAYA,
      presentAs: 'Maya',
      pins: [
        { poiId: 'poi-osm-node-375848733', title: 'Duke of Cambridge', placeKind: 'Pub', lat: 51.5346, lon: -0.0987, note: 'Good for a quiet pint after the gallery.' },
        { poiId: 'london-japanese-gallery', title: 'Japanese Gallery', placeKind: 'Gallery', lat: 51.5352, lon: -0.1031 },
        { poiId: 'london-art-space-gallery', title: 'Art Space Gallery', placeKind: 'Gallery', lat: 51.5361, lon: -0.1008 },
      ],
    },
    {
      node: JON,
      presentAs: 'Jon',
      pins: [
        { poiId: 'london-islington-green', title: 'Islington Green', placeKind: 'Park', lat: 51.5372, lon: -0.1032 },
        { poiId: 'london-canal-viewpoint', title: 'Canal Viewpoint', placeKind: 'Viewpoint', lat: 51.5389, lon: -0.0994 },
        { poiId: 'london-library', title: 'Islington Library', placeKind: 'Library', lat: 51.5330, lon: -0.1051 },
      ],
    },
  ],
  self: [
    { poiId: 'demo-poi-8', title: 'The Local', placeKind: 'Pub', lat: 51.5358, lon: -0.0994 },
  ],
};

// The floor: generic OSM/seed pins that exist whether or not anyone witnessed
// them. `hasRealCopy` marks a curated seed with real narration; `memorial`
// marks the low-value OSM clutter §5 wants penalised or filtered.
export const FLOOR = [
  { poiId: 'poi-osm-way-1', title: 'British Museum', placeKind: 'Museum', lat: 51.5194, lon: -0.1270, hasRealCopy: true },
  { poiId: 'poi-osm-way-2', title: 'The Castle', placeKind: 'Pub', lat: 51.5350, lon: -0.1020 },
  { poiId: 'poi-osm-way-3', title: 'Highbury Fields', placeKind: 'Park', lat: 51.5432, lon: -0.1004 },
  { poiId: 'poi-osm-node-9', title: 'Memorial Plaque', placeKind: 'Memorial', lat: 51.5345, lon: -0.1018, memorial: true },
  { poiId: 'poi-osm-way-far', title: 'Royal Observatory', placeKind: 'Museum', lat: 51.4826, lon: -0.0077 },
];

export const NODES = new Map([PLAYER, MAYA, JON].map((n) => [n.avatarId, n]));

const T0 = 1755000000;

// `fixture=arworld-trust-poi-phase0` — seed the peers, their edges, and the
// player's own pin. Nothing here is a special case downstream: after this runs,
// the graph and the knowledge store hold exactly what two real meets and six
// real witnesses would have left behind.
export function loadPhase0(knowledge, graph, { nowUtc = T0 } = {}) {
  for (const peer of PHASE0.peers) {
    // The edge a meet would have formed, minus the ceremony.
    graph.links.set([PLAYER.avatarId, peer.node.avatarId].sort().join('|'), {
      kind: 'TrustLink',
      trustgraph_kind: 'TrustLink',
      a: PLAYER.avatarId,
      b: peer.node.avatarId,
      presentA: 'You',
      presentB: peer.presentAs,
      link: `fixture-${peer.node.avatarId}`,
      formedUtc: nowUtc,
    });
    for (const pin of peer.pins) {
      knowledge.witness(peer.node.avatarId, { ...pin, source: 'demo', rite: 'desk-witness' }, { nowUtc });
    }
  }
  for (const pin of PHASE0.self) {
    knowledge.witness(PLAYER.avatarId, { ...pin, source: 'demo', rite: 'desk-witness' }, { nowUtc });
  }
  return { seeded: true, fixture: PHASE0.id, witnessedUtc: toIso(nowUtc) };
}
