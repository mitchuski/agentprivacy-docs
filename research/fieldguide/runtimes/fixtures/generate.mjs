// Generate the conformance vectors. Deterministic: fixed clock, fixed inputs,
// no randomness anywhere. Re-running must produce a byte-identical vectors.json
// or something has drifted — that is itself the first conformance check.
//
//   node generate.mjs        # writes vectors.json
//
// Two kinds of vector:
//
//   rejection   — an input and the register code it must produce. This is the
//                 half that catches real interop bugs, because implementations
//                 agree about success and disagree about failure.
//   projection  — a holon and an audience, with the canonical form and digest
//                 the Promise layer must produce. This is the half a
//                 second-language consumer can verify without sharing a line
//                 of code (see ../consumer-py).
//
// Projection vectors deliberately omit `peerRef` / `peerDisplayName`: those
// need the owner's secret and their shared edge, which is state rather than
// encoding. What must be byte-exact across implementations is WHICH FIELDS
// travel and HOW they are written down.

import { writeFileSync } from 'node:fs';
import { avatar } from '../meet-overlay/src/identity.mjs';
import { TrustGraph, offer, accept, confirm, questCoCompletion, stewardRedeem } from '../meet-overlay/src/meet.mjs';
import { Knowledge } from '../meet-overlay/src/knowledge.mjs';
import { project } from '../meet-overlay/src/promise.mjs';
import { nearby } from '../meet-overlay/src/nearby.mjs';
import { proposeFork } from '../meet-overlay/src/story.mjs';
import { canonical, digest } from '../meet-overlay/src/canonical.mjs';
import { toIso, DAY } from '../meet-overlay/src/time.mjs';

const T0 = 1755000000;
const ISLINGTON = { lat: 51.5344, lon: -0.1016 };
const GREENWICH = { lat: 51.4826, lon: -0.0077 };

const A = avatar('avatar-a', 'secret-a');
const B = avatar('avatar-b', 'secret-b');
const C = avatar('avatar-c', 'secret-c');
const nodes = new Map([A, B, C].map((n) => [n.avatarId, n]));

const rejections = [];
const push = (id, layer, code) => rejections.push({ id, layer, code });

// --- meet ------------------------------------------------------------------
function meetWith(g, opts = {}) {
  const {
    from = A, to = B, nonceA = 'nonce-a', nonceB = 'nonce-b',
    at = ISLINGTON, scanAt = { lat: at.lat + 0.0001, lon: at.lon + 0.0001 },
    t = T0, confirmT = t + 10, consentB = true, consentA = true,
    confirmer = from, tamper = null,
  } = opts;
  const off = offer(from, { nonce: nonceA, lat: at.lat, lon: at.lon, nowUtc: t, presentAs: 'A' });
  const acc = accept(to, off, { nonce: nonceB, lat: scanAt.lat, lon: scanAt.lon, nowUtc: t + 5, consent: consentB, presentAs: 'B' });
  if (tamper) tamper(acc);
  return confirm(confirmer, acc, g, { nowUtc: confirmT, consent: consentA });
}

push('mt-01', 'meet', meetWith(new TrustGraph(), { confirmer: C }).reason);
push('mt-02', 'meet', meetWith(new TrustGraph(), { to: A }).reason);
push('mt-03', 'meet', meetWith(new TrustGraph(), { consentB: false }).reason);
push('mt-04', 'meet', meetWith(new TrustGraph(), { confirmT: T0 + 5000 }).reason);
{
  const g = new TrustGraph();
  meetWith(g);
  push('mt-05', 'meet', meetWith(g, { to: C, nonceB: 'nonce-c' }).reason);
}
push('mt-06', 'meet', meetWith(new TrustGraph(), { scanAt: GREENWICH }).reason);
push('mt-07', 'meet', meetWith(new TrustGraph(), { tamper: (a) => (a.claimedLink = 'forged') }).reason);
{
  const g = new TrustGraph();
  meetWith(g);
  push('mt-08', 'meet', meetWith(g, { nonceA: 'nonce-a2' }).reason);
}

// --- knowledge -------------------------------------------------------------
const base = {
  poiId: 'london-british-museum', title: 'British Museum', placeKind: 'Museum',
  lat: 51.519400, lon: -0.126900, source: 'city-discover', rite: 'desk-witness',
  wikiSlug: 'british-museum', note: 'the reading room smells of dust',
};
{
  const k = new Knowledge();
  const { source, ...noSource } = base;
  push('kn-01', 'knowledge', k.witness(A.avatarId, noSource, { nowUtc: T0 }).reason.split(':')[0]);
  push('kn-02', 'knowledge', k.witness(A.avatarId, { ...base, source: 'yelp' }, { nowUtc: T0 }).reason.split(':')[0]);
  push('kn-03', 'knowledge', k.witness(A.avatarId, { ...base, rite: 'auto-walkby' }, { nowUtc: T0 }).reason.split(':')[0]);
}

// --- overlay ---------------------------------------------------------------
{
  const g = new TrustGraph();
  meetWith(g);
  const k = new Knowledge();
  k.witness(B.avatarId, { ...base, poiId: 'far', ...GREENWICH }, { nowUtc: T0 });
  k.witness(C.avatarId, { ...base, poiId: 'stranger', ...ISLINGTON }, { nowUtc: T0 });
  k.witness(B.avatarId, { ...base, poiId: 'ancient', ...ISLINGTON, witnessedUtc: toIso(T0 - 730 * DAY) }, { nowUtc: T0 });
  k.witness(B.avatarId, { ...base, poiId: 'hidden', ...ISLINGTON, disclosure: { maxAudience: 'private' } }, { nowUtc: T0 });
  for (let i = 0; i < 14; i++) {
    k.witness(B.avatarId, { ...base, poiId: `bulk-${i}`, lat: ISLINGTON.lat + i * 0.0001, lon: ISLINGTON.lon }, { nowUtc: T0 });
  }
  const r = nearby({ knowledge: k, graph: g, nodes }, A.avatarId, { ...ISLINGTON, nowUtc: T0, explain: true });
  const seen = new Set();
  let n = 1;
  for (const e of r.excluded) {
    if (seen.has(e.reason)) continue;
    seen.add(e.reason);
    push(`ov-${String(n++).padStart(2, '0')}`, 'overlay', e.reason);
  }
}

// --- story -----------------------------------------------------------------
{
  const k = new Knowledge();
  const env = { playerSite: 'privacy.fieldguide', canonicalSite: 'harness.localhost', nowUtc: T0 };
  k.witness(A.avatarId, base, { nowUtc: T0 });
  const h = k.mine(A.avatarId)[0];
  push('st-01', 'story', proposeFork(h, { ...env }).reason);
  push('st-02', 'story', proposeFork({ ...h, disclosure: { maxAudience: 'private' } }, { ...env, publishConsent: true }).reason);
  push('st-03', 'story', proposeFork({ ...h, wikiSlug: 'city-discover' }, { ...env, publishConsent: true }).reason);
  push('st-04', 'story', proposeFork({ ...h, forkedSlug: 'x' }, { ...env, publishConsent: true }).reason);
}

// --- encounters ------------------------------------------------------------
push('en-01', 'encounter', questCoCompletion(A.avatarId, B.avatarId, 'murder-stones').reason);
push('en-02', 'encounter', 'steward-redeem');
stewardRedeem(A.avatarId, 'venue-punch-bowl', { offerId: 'pilgrims-tea', nowUtc: T0 });

// --- projection vectors ----------------------------------------------------
const holons = [
  { id: 'pj-full', holon: { ...base, markerStyle: 'museum', trail: 'london', questId: 'q-1', witnessedUtc: toIso(T0), avatarId: B.avatarId, holonId: 'h1', witnessCount: 3 } },
  { id: 'pj-quest', holon: { ...base, source: 'quest', questId: 'murder-stones-3', questPinRole: 'waystation', witnessedUtc: toIso(T0), avatarId: B.avatarId } },
  { id: 'pj-deny', holon: { ...base, witnessedUtc: toIso(T0), avatarId: B.avatarId, disclosure: { maxAudience: 'acquaintance', deny: ['wikiSlug'] } } },
  { id: 'pj-private', holon: { ...base, witnessedUtc: toIso(T0), avatarId: B.avatarId, disclosure: { maxAudience: 'private' } } },
  // Deliberately adversarial: both coordinates land exactly on a .5 boundary
  // under the public coarsening (×1000). JavaScript's Math.round is half-up
  // toward +infinity; Python's round() and C#'s Math.Round are half-to-EVEN by
  // default. Two conformant-looking implementations place this pin 100 m apart
  // and neither is obviously wrong. The vector exists so the disagreement is
  // caught by the pack instead of by a player.
  { id: 'pj-halfway', holon: { ...base, lat: 51.534500, lon: -0.101500, witnessedUtc: toIso(T0), avatarId: B.avatarId } },
];

const projections = [];
for (const { id, holon } of holons) {
  for (const audience of ['public', 'link', 'acquaintance']) {
    const p = project(holon, audience);
    projections.push({
      id: `${id}@${audience}`,
      audience,
      holon,
      expect: p === null
        ? { projected: false }
        : { projected: true, fields: Object.keys(p).sort(), canonical: canonical(p), digest: digest(p) },
    });
  }
}

const out = {
  spec: 'arworld-meet-overlay conformance vectors',
  version: '0.1',
  generatedFrom: 'runtimes/fixtures/generate.mjs (deterministic; no clock, no randomness)',
  clock: toIso(T0),
  rejections,
  projections,
};

writeFileSync(new URL('./vectors.json', import.meta.url), JSON.stringify(out, null, 2) + '\n');
console.log(`wrote vectors.json — ${rejections.length} rejection vectors, ${projections.length} projection vectors`);
