// The questions that had only prose answers. Run: node test.mjs

import {
  RITE_ASSURANCE, riteAdmits, CONSUMER_BARS,
  captureProof, attachMedia,
  EDGE_KINDS, deriveSharedropClaim, MAP_READABLE_EDGE_FIELDS,
} from './src/answers.mjs';
import { project, NEVER_PROJECTED } from '../meet-overlay/src/promise.mjs';

let passed = 0;
let failed = 0;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const red = (s) => `\x1b[31m${s}\x1b[0m`;
const check = (name, cond, d) => {
  if (cond) { passed++; console.log(`  ${green('PASS')} ${name}`); }
  else { failed++; console.log(`  ${red('FAIL')} ${name}${d ? ` — ${d}` : ''}`); }
};
const section = (t) => console.log(`\n${t}`);

// ===========================================================================
section('Q1 — DISCOVERY §10.1: must discovery require the camera?');
// ===========================================================================
{
  check('Q1a both a desk witness and a camera fetch are real discoveries', riteAdmits('desk-witness', { minAssurance: CONSUMER_BARS.trail }).admitted && riteAdmits('camera-fetch', { minAssurance: CONSUMER_BARS.trail }).admitted);
}
{
  const r = riteAdmits('desk-witness', { minAssurance: CONSUMER_BARS.tillRedeem });
  check('Q1b a consumer with a stake may set a higher bar (a till redeem)', r.admitted === false && r.reason === 'rite-below-required-assurance');
}
{
  check('Q1c the same desk witness still counts for the trail and the overlay', riteAdmits('desk-witness', { minAssurance: CONSUMER_BARS.overlay }).admitted);
}
{
  check('Q1d the rite vocabulary stays closed — no auto-anything', riteAdmits('auto-walkby').admitted === false && Object.keys(RITE_ASSURANCE).length === 4);
}

// ===========================================================================
section('Q2 — DISCOVERY §10.4: is the photo retained?');
// ===========================================================================
{
  const p = captureProof('camera-fetch', new Uint8Array(2_400_000), { salt: 's' });
  check('Q2a a camera fetch yields a presence proof and drops the image', p.retained === false && typeof p.proof === 'string' && p.imageBytes === undefined);
}
{
  const a = captureProof('camera-fetch', new Uint8Array(1000), { salt: 'x' });
  const b = captureProof('camera-fetch', new Uint8Array(1000), { salt: 'y' });
  check('Q2b the proof is salted — two captures do not collide into one id', a.proof !== b.proof);
}
{
  const r = captureProof('desk-witness', null, { salt: 's' });
  check('Q2c a desk witness produces no capture proof at all', r.proof === null && r.retained === false);
}
{
  const r = attachMedia({ poiId: 'x' }, { url: 'blob:1' }, {});
  check('Q2d a MediaHolon needs its own consent, like publication does', r.attached === false && r.reason === 'no-media-consent');
}
{
  const { holon } = attachMedia({ poiId: 'x', title: 'X', placeKind: 'Pub', lat: 1, lon: 1 }, { url: 'blob:1' }, { mediaConsent: true });
  const leaked = ['public', 'link', 'acquaintance'].some((a) => {
    const p = project(holon, a);
    return p && p.media !== undefined;
  });
  check('Q2e if a MediaHolon exists it is never projected at any audience', leaked === false && holon.media.neverProjected === true);
}

// ===========================================================================
section('Q3 — TRUST_WEIGHTED §9.4: sharedrops on the same edge type?');
// ===========================================================================
{
  const r = deriveSharedropClaim({ kind: 'TrustLink', a: 'x', b: 'y' });
  check('Q3a an economic claim cannot be derived from a social edge', r.claim === null && r.reason === 'edge-kind-not-economic');
}
{
  check('Q3b the edge-kind vocabulary is closed to social edges only', EDGE_KINDS.length === 1 && EDGE_KINDS[0] === 'TrustLink');
}
{
  // Equity added to the edge later must not be able to reach a pin. Structural,
  // so nobody has to remember the UI rule.
  const edge = { kind: 'TrustLink', a: 'x', b: 'y', presentA: 'A', presentB: 'B', formedUtc: 1, capTableShares: 4200, sharedropTier: 'gold' };
  const readable = Object.keys(edge).filter((k) => MAP_READABLE_EDGE_FIELDS.includes(k));
  const economic = Object.keys(edge).filter((k) => /share|cap|equity|tier/i.test(k));
  check('Q3c the map reads a closed field set — equity on the edge cannot reach it', economic.length > 0 && economic.every((k) => !readable.includes(k)));
}
{
  check('Q3d "equity" is not smuggled through the projection allow-list either', ['capTableShares', 'sharedropTier'].every((f) => {
    const p = project({ poiId: 'p', title: 't', placeKind: 'k', lat: 1, lon: 1, [f]: 9 }, 'acquaintance');
    return p[f] === undefined;
  }) && NEVER_PROJECTED.length > 0);
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
