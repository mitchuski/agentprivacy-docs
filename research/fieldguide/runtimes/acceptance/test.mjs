// Their checklist, executable.
//
//   node test.mjs
//
// A-properties are ARWORLD_TRUST_WEIGHTED_POI §6 "Acceptance for Phase 0" — the
// five unticked boxes, run rather than read.
// R-properties are §5 "Unity score terms" — the ranking table, made mechanical.
//
// This is the suite the Field Guide team can run against their own criteria.

import { metresBetween } from '../meet-overlay/src/geo.mjs';
import { Knowledge } from '../meet-overlay/src/knowledge.mjs';
import { TrustGraph } from '../meet-overlay/src/meet.mjs';
import { nearby } from '../meet-overlay/src/nearby.mjs';
import { avatar } from '../meet-overlay/src/identity.mjs';
import { loadPhase0, PHASE0, FLOOR, NODES, PLAYER, ISLINGTON, SPAWN_RADIUS_M } from './src/fixture.mjs';
import { rank, markerStyle, ALLOWED_NUMERIC, strip, BANDS } from './src/ranking.mjs';

let passed = 0;
let failed = 0;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const red = (s) => `\x1b[31m${s}\x1b[0m`;
function check(name, cond, detail) {
  if (cond) {
    passed++;
    console.log(`  ${green('PASS')} ${name}`);
  } else {
    failed++;
    console.log(`  ${red('FAIL')} ${name}${detail ? `\n         ${detail}` : ''}`);
  }
}
const section = (t) => console.log(`\n${t}`);

const T0 = 1755000000;
const distanceOf = (p) => metresBetween(ISLINGTON.lat, ISLINGTON.lon, p.lat, p.lon);

// Build the map exactly as §10's one-line stack describes it: local floor
// first, then merge the trust overlay, then rank distance-first.
function buildMap({ fixture, audience = 'link', cap = 12 } = {}) {
  const knowledge = new Knowledge();
  const graph = new TrustGraph();
  if (fixture) loadPhase0(knowledge, graph, { nowUtc: T0 });
  const view = { ...ISLINGTON, radiusM: SPAWN_RADIUS_M, nowUtc: T0, cap, audience };
  const r = nearby({ knowledge, graph, nodes: NODES }, PLAYER.avatarId, view);
  const floor = FLOOR.map((f) => ({ ...f, origin: 'floor' }));
  const merged = rank([...floor, ...r.self, ...r.fromGraph], { spawnRadiusM: SPAWN_RADIUS_M, cap, distanceOf });
  return { ...r, floor, merged };
}

// ===========================================================================
section('A — ARWORLD_TRUST_WEIGHTED_POI §6, "Acceptance for Phase 0"');
// ===========================================================================
{
  const m = buildMap({ fixture: true });
  const names = m.fromGraph.map((p) => p.peerDisplayName);
  const floorShown = m.merged.filter((p) => p.origin === 'floor').length;
  check('A1 fixture on: floor pins AND ≥2 overlay pins tagged Maya/Jon', floorShown > 0 && m.fromGraph.length >= 2 && names.includes('Maya') && names.includes('Jon'), `floor ${floorShown}, overlay ${m.fromGraph.length}, names ${[...new Set(names)]}`);
}
{
  const m = buildMap({ fixture: true });
  const outside = m.fromGraph.filter((p) => distanceOf(p) > SPAWN_RADIUS_M);
  check('A2 every overlay pin is within spawnRadiusM of the player', outside.length === 0, `outside: ${outside.map((p) => p.poiId)}`);
}
{
  const link = buildMap({ fixture: true, audience: 'link' });
  const pub = buildMap({ fixture: true, audience: 'public' });
  check('A3 peek shows the peer name at audience=link, and not at public', link.fromGraph.every((p) => !!p.peerDisplayName) && pub.fromGraph.every((p) => p.peerDisplayName === undefined));
}
{
  // The equivalence that makes the fixture retirable: with it off, the map is
  // byte-identical to a floor-only map. The fixture is not a code path.
  const off = buildMap({ fixture: false });
  const floorOnly = rank(FLOOR.map((f) => ({ ...f, origin: 'floor' })), { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check('A4 fixture off: fromGraph empty and the map equals floor-only, exactly', off.fromGraph.length === 0 && JSON.stringify(off.merged) === JSON.stringify(floorOnly));
}
{
  // "No fake trust score UI" — asserted structurally rather than by looking at
  // a screenshot. A pin may carry only known numeric fields, so a trustScore or
  // a reputation cannot appear without failing here.
  const m = buildMap({ fixture: true });
  const stray = [];
  for (const pin of [...m.merged, ...m.fromGraph, ...m.self]) {
    for (const [k, v] of Object.entries(strip(pin))) {
      if (typeof v === 'number' && !ALLOWED_NUMERIC.includes(k)) stray.push(`${pin.poiId}.${k}`);
    }
  }
  check('A5 no numeric field on any pin scores a person', stray.length === 0, `stray: ${stray.join(', ')}`);
}

// ===========================================================================
section('R — ARWORLD_TRUST_WEIGHTED_POI §5, the score terms');
// ===========================================================================
const at = (m) => ({ lat: ISLINGTON.lat + m / 111320, lon: ISLINGTON.lon });
{
  const pins = [
    { poiId: 'c', ...at(900), origin: 'floor' },
    { poiId: 'a', ...at(100), origin: 'floor' },
    { poiId: 'b', ...at(500), origin: 'floor' },
  ];
  const out = rank(pins, { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check('R1 with no modifiers, order is exactly distance order', out.map((p) => p.poiId).join('') === 'abc');
}
{
  const pins = [
    { poiId: 'near', ...at(100), origin: 'floor' },
    { poiId: 'far-but-loved', lat: 51.4826, lon: -0.0077, origin: 'self', hasRealCopy: true },
  ];
  const out = rank(pins, { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check('R2 the hard cut is on TRUE distance — no band drags Greenwich in', out.length === 1 && out[0].poiId === 'near');
}
{
  const pins = [
    { poiId: 'floor-600', ...at(600), origin: 'floor' },
    { poiId: 'peer-800', ...at(800), origin: 'trust' },
  ];
  const out = rank(pins, { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check('R3 a peer pin can outrank a nearer floor pin — the band does something', out[0].poiId === 'peer-800');
}
{
  const pins = [
    { poiId: 'floor-100', ...at(100), origin: 'floor' },
    { poiId: 'peer-800', ...at(800), origin: 'trust' },
  ];
  const out = rank(pins, { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check(`R4 but only by its band — ${BANDS.fromGraph} m does not beat 700 m`, out[0].poiId === 'floor-100');
}
{
  // §1: "This is not Yelp. It is not trending in London." A pin's rank for me
  // must not depend on how many other people have witnessed it.
  const knowledge = new Knowledge();
  const graph = new TrustGraph();
  loadPhase0(knowledge, graph, { nowUtc: T0 });
  const before = JSON.stringify(buildMapWith(knowledge, graph));

  // one hundred strangers pile onto the Duke of Cambridge
  for (let i = 0; i < 100; i++) {
    const s = avatar(`stranger-${i}`, `secret-${i}`);
    NODES.set(s.avatarId, s);
    knowledge.witness(s.avatarId, { poiId: 'poi-osm-node-375848733', title: 'Duke of Cambridge', placeKind: 'Pub', lat: 51.5346, lon: -0.0987, source: 'city-discover', rite: 'desk-witness' }, { nowUtc: T0 });
  }
  const after = JSON.stringify(buildMapWith(knowledge, graph));
  check('R5 no global popularity — 100 strangers do not move a pin for me', before === after);

  function buildMapWith(k, g) {
    const r = nearby({ knowledge: k, graph: g, nodes: NODES }, PLAYER.avatarId, { ...ISLINGTON, radiusM: SPAWN_RADIUS_M, nowUtc: T0, cap: 12 });
    return rank([...FLOOR.map((f) => ({ ...f, origin: 'floor' })), ...r.self, ...r.fromGraph], { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  }
}
{
  const m = buildMap({ fixture: true });
  check('R6 memorial/plaque clutter is filtered out of the map', !m.merged.some((p) => p.memorial));
}
{
  const many = Array.from({ length: 30 }, (_, i) => ({ poiId: `p${i}`, ...at(50 + i * 10), origin: 'floor' }));
  const out = rank(many, { spawnRadiusM: SPAWN_RADIUS_M, cap: 12, distanceOf });
  check('R7 the cap is applied after ranking, not before', out.length === 12 && out[0].poiId === 'p0');
}
{
  const m = buildMap({ fixture: true });
  const self = m.merged.find((p) => p.origin === 'self');
  const peer = m.merged.find((p) => p.origin === 'trust');
  const floor = m.merged.find((p) => p.origin === 'floor');
  check('R8 marker style is the only thing origin changes: teal, gold, default', markerStyle(self) === 'ring-teal' && markerStyle(peer) === 'ring-gold' && markerStyle(floor) === 'discover-default');
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
