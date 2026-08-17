// Property tests for the Field Guide × TrustGraph meet-and-overlay model.
// Run: node test.mjs   — exits nonzero on any failure. Zero-dep, offline.
//
// Each property is a claim the counter-spec makes. If you disagree with the
// counter-spec, the fastest way to say so is to break one of these.

import { avatar, rdid } from './src/identity.mjs';
import {
  TrustGraph,
  offer,
  accept,
  confirm,
  questCoCompletion,
  stewardRedeem,
  MEET_TTL_SEC,
} from './src/meet.mjs';
import { Knowledge, PASSPORT_FIELDS } from './src/knowledge.mjs';
import { audienceFor, project, AUDIENCES, NEVER_PROJECTED } from './src/promise.mjs';
import { nearby } from './src/nearby.mjs';
import { freshness, FRESHNESS_FLOOR } from './src/erosion.mjs';
import { toIso, DAY } from './src/time.mjs';
import { canonical, digest, CANON_DOMAIN } from './src/canonical.mjs';
import { proposeFork } from './src/story.mjs';

let passed = 0;
let failed = 0;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const red = (s) => `\x1b[31m${s}\x1b[0m`;
function check(name, cond) {
  if (cond) {
    passed++;
    console.log(`  ${green('PASS')} ${name}`);
  } else {
    failed++;
    console.log(`  ${red('FAIL')} ${name}`);
  }
}
function section(t) {
  console.log(`\n${t}`);
}

// --- fixtures (of the test kind, not the overlay kind) ---------------------
const T0 = 1755000000; // fixed clock; nothing here reads the wall clock
const ISLINGTON = { lat: 51.5344, lon: -0.1016 };
const GREENWICH = { lat: 51.4826, lon: -0.0077 };
const VIEW = { ...ISLINGTON, nowUtc: T0 }; // viewport + clock for nearby()

const mitch = avatar('avatar-mitch', 'secret-mitch');
const maya = avatar('avatar-maya', 'secret-maya');
const jon = avatar('avatar-jon', 'secret-jon');
const dave = avatar('avatar-dave', 'secret-dave');
const nodes = new Map([mitch, maya, jon, dave].map((n) => [n.avatarId, n]));

function meet(graph, A, B, opts = {}) {
  const {
    nonceA = `n-${A.avatarId}-${B.avatarId}`,
    nonceB = `m-${B.avatarId}`,
    at = ISLINGTON,
    scanAt = { lat: at.lat + 0.0001, lon: at.lon + 0.0001 },
    t = T0,
    confirmT = t + 10,
    consentB = true,
    consentA = true,
    tamper = null,
    presentA = null,
    presentB = null,
  } = opts;
  const off = offer(A, { nonce: nonceA, lat: at.lat, lon: at.lon, nowUtc: t, presentAs: presentA });
  const acc = accept(B, off, {
    nonce: nonceB,
    lat: scanAt.lat,
    lon: scanAt.lon,
    nowUtc: t + 5,
    consent: consentB,
    presentAs: presentB,
  });
  if (tamper) tamper(acc);
  return confirm(A, acc, graph, { nowUtc: confirmT, consent: consentA });
}

function poi(k, who, over = {}) {
  return k.witness(
    who.avatarId,
    {
      poiId: 'london-british-museum',
      title: 'British Museum',
      placeKind: 'Museum',
      lat: 51.5345,
      lon: -0.1017,
      source: 'city-discover',
      rite: 'desk-witness',
      wikiSlug: 'british-museum',
      note: 'the reading room smells of dust',
      ...over,
    },
    { nowUtc: T0 },
  );
}

// ===========================================================================
section('M — the Meet rite (§10.1: how a 1-hop edge is actually created)');
// ===========================================================================
{
  const g = new TrustGraph();
  const r = meet(g, mitch, maya, { consentB: false });
  check('M1 a scan alone is an encounter, not an edge', r.formed === false && r.reason === 'unilateral-no-mutual-consent' && g.links.size === 0);
}
{
  const g = new TrustGraph();
  const r = meet(g, mitch, maya);
  check('M2 co-located mutual consent forms one TrustLink', r.formed === true && g.links.size === 1 && r.holon.kind === 'TrustLink');
  check('M2b the link holon carries no score, only a commitment', r.holon.score === undefined && typeof r.holon.link === 'string');
}
{
  const g = new TrustGraph();
  const r = meet(g, mitch, mitch);
  check('M3 self-edge is forbidden (self-Sybil, not a relationship)', r.formed === false && r.reason === 'self-edge-forbidden');
}
{
  const g = new TrustGraph();
  const r = meet(g, mitch, maya, { confirmT: T0 + MEET_TTL_SEC + 60 });
  check('M4 an expired offer is refused (a meet is a moment)', r.formed === false && r.reason === 'meet-offer-expired');
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya, { nonceA: 'reused' });
  const r = meet(g, mitch, jon, { nonceA: 'reused' });
  check('M5 a replayed offer nonce is spent (photographed QR is dead)', r.formed === false && r.reason === 'meet-offer-replayed');
}
{
  const g = new TrustGraph();
  const r = meet(g, mitch, maya, { scanAt: GREENWICH });
  check('M6 a non-co-located meet is refused (the rite is physical)', r.formed === false && r.reason === 'meet-not-colocated');
}
{
  const g = new TrustGraph();
  const r = meet(g, mitch, maya, { tamper: (a) => (a.claimedLink = 'forged-commitment') });
  check('M7 a forged link commitment is caught across the Gap', r.formed === false && r.reason === 'link-commitment-forged');
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const r = meet(g, mitch, maya, { nonceA: 'fresh-nonce' });
  check('M8 one TrustLink per pair (idempotent)', r.formed === false && r.reason === 'duplicate-link' && g.links.size === 1);
}
{
  check('M9 R-DIDs are fresh per counterparty (unlinkable)', rdid(mitch, maya.avatarId) !== rdid(mitch, jon.avatarId));
}
{
  const g = new TrustGraph();
  const e = questCoCompletion(mitch.avatarId, maya.avatarId, 'murder-stones');
  check('M10 §10.6 shared quest completion is an encounter, never an edge', e.formsEdge === false && e.consentA === false && g.links.size === 0);
}

// ===========================================================================
section('K — Knowledge (PoiDiscovery holon)');
// ===========================================================================
{
  const k = new Knowledge();
  const a = poi(k, mitch);
  const b = poi(k, mitch);
  check('K1 witness is idempotent on (avatarId, poiId)', a.created === true && b.created === false && b.witnessCount === 2 && a.holonId === b.holonId);
}
{
  const k = new Knowledge();
  const r = k.witness(mitch.avatarId, { poiId: 'x', title: 'X', placeKind: 'Pub', lat: 1, lon: 1 }, { nowUtc: T0 });
  check('K2 a missing required field is refused', r.ok === false && r.reason === 'missing-required-field:source');
}
{
  const k = new Knowledge();
  const r = poi(k, mitch, { rite: 'auto-walkby' });
  check('K3 an unknown rite is refused (no auto-Witness on walk-by)', r.ok === false && r.reason === 'unknown-rite:auto-walkby');
}
{
  const k = new Knowledge();
  poi(k, mitch, { poiId: 'poi-osm-way-123', title: 'The Castle' });
  k.alias('poi-osm-way-123', 'venue-the-castle'); // partner claims the node
  const r = poi(k, mitch, { poiId: 'poi-osm-way-123', title: 'The Castle' });
  check('K4 §10.4 an id remap migrates existing Knowledge, mints no second id', r.created === false && r.poiId === 'venue-the-castle' && k.mine(mitch.avatarId).length === 1 && r.witnessCount === 2);
}
{
  const k = new Knowledge();
  poi(k, mitch, { trail: 'murder-stones', questId: 'q-1', markerStyle: 'stone' });
  const restored = k.restorePassport(mitch.avatarId)[0];
  const holon = k.mine(mitch.avatarId)[0];
  const lossless = PASSPORT_FIELDS.every((f) => holon[f] === undefined || restored[f] === holon[f]);
  check('K5 §10.3 a reinstall restores every field Unity stamps locally', lossless && restored.rite === 'desk-witness' && restored.witnessedUtc === toIso(T0));
}

// ===========================================================================
section('P — Promise (per-holon disclosure, §10.2)');
// ===========================================================================
{
  const k = new Knowledge();
  poi(k, mitch, { questId: 'murder-stones-3' });
  const h = k.mine(mitch.avatarId)[0];
  const p = project(h, 'link');
  check('P1 a link projection carries neither questId nor note', p.questId === undefined && p.note === undefined && p.title === 'British Museum');
}
{
  const k = new Knowledge();
  poi(k, mitch);
  const h = k.mine(mitch.avatarId)[0];
  h.deviceModel = 'iPhone 17'; // somebody adds a field to the holon later
  const leaked = AUDIENCES.filter((a) => a !== 'private').some((a) => {
    const p = project(h, a);
    return p && p.deviceModel !== undefined;
  });
  check('P2 the allow-list is closed — a new holon field never surfaces', leaked === false);
}
{
  const k = new Knowledge();
  poi(k, mitch);
  const h = k.mine(mitch.avatarId)[0];
  const p = project(h, 'public');
  const coarsened = p.lat === Math.round(h.lat * 1000) / 1000 && p.lat !== h.lat;
  check('P3 public gets coarse geo and loses wikiSlug / rite / note', coarsened && p.wikiSlug === undefined && p.rite === undefined && p.note === undefined);
}
{
  const k = new Knowledge();
  poi(k, mitch, { disclosure: { maxAudience: 'private' } });
  const h = k.mine(mitch.avatarId)[0];
  const hidden = AUDIENCES.every((a) => project(h, a) === null);
  check('P4 a per-holon private ceiling hides one pin from everyone', hidden);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  meet(g, maya, jon, { nonceA: 'n-maya-jon' });
  check('P5 audience is granted, not computed — 2 hops is nothing', audienceFor(g, jon.avatarId, mitch.avatarId) === null && audienceFor(g, maya.avatarId, mitch.avatarId) === 'link');
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya);
  const h = k.mine(maya.avatarId)[0];
  const before = project(h, audienceFor(g, maya.avatarId, mitch.avatarId));
  g.grant(maya.avatarId, mitch.avatarId, 'acquaintance');
  const after = project(h, audienceFor(g, maya.avatarId, mitch.avatarId));
  check('P6 acquaintance requires an explicit grant by the owner', before.note === undefined && after.note === 'the reading room smells of dust');
}
{
  const k = new Knowledge();
  poi(k, maya);
  const h = k.mine(maya.avatarId)[0];
  const toMitch = project(h, 'link', { ownerNode: maya, viewerAvatarId: mitch.avatarId });
  const toJon = project(h, 'link', { ownerNode: maya, viewerAvatarId: jon.avatarId });
  check('P7 the peer reference is pairwise — two viewers cannot join it', toMitch.peerRef !== toJon.peerRef && toMitch.peerRef !== maya.avatarId);
}
{
  const k = new Knowledge();
  poi(k, mitch, { questId: 'q-9', client: 'field-guide-unity' });
  const h = k.mine(mitch.avatarId)[0];
  const leaked = AUDIENCES.flatMap((a) => {
    const p = project(h, a, { ownerNode: mitch, viewerAvatarId: maya.avatarId });
    return p ? NEVER_PROJECTED.filter((f) => p[f] !== undefined) : [];
  });
  check('P8 no NEVER_PROJECTED field appears at any audience', leaked.length === 0);
}
{
  const k = new Knowledge();
  poi(k, mitch, { source: 'quest', questId: 'q-3' });
  const h = k.mine(mitch.avatarId)[0];
  const p = project(h, 'acquaintance');
  check('P9 a quest pin caps at link even for an acquaintance', p.note === undefined && p.audience === 'link');
}

// ===========================================================================
section('N — the overlay (GET /poi/nearby, fixture removed)');
// ===========================================================================
{
  const g = new TrustGraph();
  const k = new Knowledge();
  poi(k, maya);
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N1 no meet yet — fromGraph is honestly empty, not a fixture', r.fromGraph.length === 0 && r.fixture === false);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya);
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N2 after a real meet the peer pin appears as trust origin', r.fromGraph.length === 1 && r.fromGraph[0].origin === 'trust' && r.fromGraph[0].audience === 'link');
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya, { poiId: 'greenwich-obs', title: 'Royal Observatory', ...GREENWICH });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N3 Greenwich never enters an Islington viewport', r.fromGraph.length === 0);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  for (let i = 0; i < 15; i++) {
    poi(k, maya, { poiId: `pin-${i}`, title: `Pin ${i}`, lat: 51.5344 + i * 0.0001 });
  }
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N4 the overlay is capped (Unity: 12)', r.fromGraph.length === 12);
  const asc = r.fromGraph.map((p) => p.lat);
  check('N5 distance-first ordering', asc.every((v, i, arr) => i === 0 || arr[i - 1] <= v));
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, mitch, { poiId: 'mine-1' });
  poi(k, maya, { poiId: 'theirs-1' });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N6 self keeps its own note; the peer projection does not', r.self[0].note === 'the reading room smells of dust' && r.fromGraph[0].note === undefined);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  meet(g, maya, jon, { nonceA: 'n-maya-jon' });
  const k = new Knowledge();
  poi(k, jon, { poiId: 'jons-pin' });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N7 a 2-hop peer contributes nothing to the map', r.fromGraph.length === 0);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya, { disclosure: { maxAudience: 'private' } });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('N8 a pin the owner marked private stays off a 1-hop peer map', r.fromGraph.length === 0);
}

// ===========================================================================
section('D — the display-name join (the leak the pairwise R-DID nearly lost)');
// ===========================================================================
{
  const g = new TrustGraph();
  meet(g, maya, mitch, { presentA: 'Maya', nonceA: 'n-maya-mitch' });
  meet(g, maya, jon, { presentA: 'M.', nonceA: 'n-maya-jon' });
  check('D1 a face is chosen per edge, not per profile', g.presentationOf(maya.avatarId, mitch.avatarId) === 'Maya' && g.presentationOf(maya.avatarId, jon.avatarId) === 'M.');
}
{
  const g = new TrustGraph();
  meet(g, maya, mitch, { presentA: 'Maya', nonceA: 'n-maya-mitch' });
  meet(g, maya, jon, { presentA: 'M.', nonceA: 'n-maya-jon' });
  const k = new Knowledge();
  poi(k, maya);
  const h = k.mine(maya.avatarId)[0];
  h.displayName = 'Maya Okonjo'; // a global profile name, as ONODE has today
  const toMitch = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW).fromGraph[0];
  const toJon = nearby({ knowledge: k, graph: g, nodes }, jon.avatarId, VIEW).fromGraph[0];
  const joinable = Object.keys(toMitch).filter((f) => toMitch[f] === toJon[f] && ['peerRef', 'peerDisplayName', 'displayName', 'peerAvatarId'].includes(f));
  check('D2 no identifier in a projection is shared between two viewers', joinable.length === 0);
  check('D3 the global profile displayName never reaches either viewer', toMitch.displayName === undefined && toJon.displayName === undefined);
  check('D4 the raw avatarId never reaches either viewer', !Object.values(toMitch).includes(maya.avatarId));
}

// ===========================================================================
section('E — erosion (§9.3 recency, as a rate rather than a cliff)');
// ===========================================================================
{
  const f0 = freshness(toIso(T0), T0);
  const f90 = freshness(toIso(T0 - 90 * DAY), T0);
  const f180 = freshness(toIso(T0 - 180 * DAY), T0);
  check('E1 freshness is 1 at zero age and halves each 90 days', Math.abs(f0 - 1) < 1e-9 && Math.abs(f90 - 0.5) < 1e-6 && Math.abs(f180 - 0.25) < 1e-6);
}
{
  const f89 = freshness(toIso(T0 - 89 * DAY), T0);
  const f91 = freshness(toIso(T0 - 91 * DAY), T0);
  check('E2 there is no cliff at 90 days — it is a rate', Math.abs(f89 - f91) < 0.02 && f89 > FRESHNESS_FLOOR && f91 > FRESHNESS_FLOOR);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya, { witnessedUtc: toIso(T0 - 730 * DAY) });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('E3 a two-year-old peer pin falls below the horizon', r.fromGraph.length === 0);
}
{
  const g = new TrustGraph();
  const k = new Knowledge();
  poi(k, mitch, { witnessedUtc: toIso(T0 - 730 * DAY) });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('E4 your own trail never erodes', r.self.length === 1);
}
{
  const g = new TrustGraph();
  meet(g, mitch, maya);
  const k = new Knowledge();
  poi(k, maya, { witnessedUtc: toIso(T0 - 45 * DAY) });
  const r = nearby({ knowledge: k, graph: g, nodes }, mitch.avatarId, VIEW);
  check('E5 a fading pin still ships, carrying its freshness for the fade', r.fromGraph.length === 1 && r.fromGraph[0].freshness > 0.7 && r.fromGraph[0].freshness < 0.75);
}

// ===========================================================================
section('S — stewards (ARWORLD_DISCOVERY §10.3)');
// ===========================================================================
{
  const g = new TrustGraph();
  const r = stewardRedeem(mitch.avatarId, 'venue-punch-bowl', { offerId: 'pilgrims-tea', nowUtc: T0 });
  check('S1 a till redeem is a receipt, never a TrustLink', r.kind === 'RedeemReceipt' && r.formsEdge === false && g.links.size === 0);
}

// ===========================================================================
section('C — canonical encoding (so a second language can agree)');
// ===========================================================================
{
  const a = digest({ title: 'X', lat: 51.5, note: undefined });
  const b = digest({ title: 'X', lat: 51.5, note: '' });
  check('C1 an absent field and an empty field are different facts', a !== b);
}
{
  const a = digest({ lat: 1, lon: 2 });
  const b = digest({ lon: 2, lat: 1 });
  check('C2 key order does not change the digest', a === b);
}
{
  const same = digest({ lat: 1 }) === digest({ lat: 1.0 });
  const diff = digest({ lat: 1 }) !== digest({ lat: 1.000001 });
  check('C3 numbers are fixed to 6dp — 1 and 1.0 agree, 1.000001 does not', same && diff);
}
{
  check('C4 the domain is part of the preimage', canonical({}).startsWith(CANON_DOMAIN));
}

// ===========================================================================
section('W — the wikiSlug seam (§8: fork, never overwrite, never spam)');
// ===========================================================================
const FORK_ENV = { playerSite: 'privacy.fieldguide', canonicalSite: 'harness.localhost', nowUtc: T0 };
{
  const k = new Knowledge();
  poi(k, mitch);
  const r = proposeFork(k.mine(mitch.avatarId)[0], { ...FORK_ENV });
  check('W1 a plain Witness writes no page (§8: would spam the neighborhood)', r.forked === false && r.reason === 'no-publication-consent');
}
{
  const k = new Knowledge();
  poi(k, mitch, { disclosure: { maxAudience: 'acquaintance' } });
  const h = k.mine(mitch.avatarId)[0];
  const without = proposeFork(h, { ...FORK_ENV });
  const with_ = proposeFork(h, { ...FORK_ENV, publishConsent: true });
  check('W2 publication is not reachable by widening an audience', without.forked === false && with_.forked === true);
}
{
  const k = new Knowledge();
  poi(k, mitch, { disclosure: { maxAudience: 'private' } });
  const r = proposeFork(k.mine(mitch.avatarId)[0], { ...FORK_ENV, publishConsent: true });
  check('W3 a private pin is unpublishable even with consent', r.forked === false && r.reason === 'holon-ceiling-private');
}
{
  const k = new Knowledge();
  poi(k, mitch, { questId: 'murder-stones-3' });
  const r = proposeFork(k.mine(mitch.avatarId)[0], { ...FORK_ENV, publishConsent: true });
  const body = JSON.stringify(r.page);
  check('W4 a forked page carries public-tier fields only', !r.publishedFields.includes('note') && !r.publishedFields.includes('questId') && !body.includes('reading room') && !body.includes('murder-stones-3'));
}
{
  const k = new Knowledge();
  poi(k, mitch);
  const r = proposeFork(k.mine(mitch.avatarId)[0], { ...FORK_ENV, publishConsent: true });
  check('W5 the fork links the canonical slug and claims a new one', r.slug !== 'british-museum' && r.page.canonicalSlug === 'british-museum' && r.page.journal[0].type === 'fork' && r.page.journal[0].site === 'harness.localhost');
}
{
  const k = new Knowledge();
  poi(k, mitch);
  const h = k.mine(mitch.avatarId)[0];
  h.forkedSlug = 'london-british-museum-witnessed';
  const r = proposeFork(h, { ...FORK_ENV, publishConsent: true });
  check('W6 forking is idempotent — a second Witness does not re-fork', r.forked === false && r.reason === 'already-forked');
}
{
  const k = new Knowledge();
  poi(k, mitch, { wikiSlug: 'city-discover' });
  const r = proposeFork(k.mine(mitch.avatarId)[0], { ...FORK_ENV, publishConsent: true });
  check('W7 a generic floor pin has nothing to fork from', r.forked === false && r.reason === 'no-canonical-slug');
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
