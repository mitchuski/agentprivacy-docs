// LAB BRIDGE — the Field Guide model run against the DTG lab it came from.
//
//   node test.mjs
//
// Until now the relationship between this workbench and the ToIP DTG ZKP lab
// was a correspondence table in a NOTES file. A table is prose: it cannot go
// stale loudly, and nothing breaks when the two drift apart.
//
// This suite makes it a dependency. It imports `runtimes/07-trust-graph-
// formation` and `runtimes/01-uniqueness-nullifier` from the lab **for real**
// and runs the same scenarios through both models. If the lab changes a gate,
// a rejection name, or the shape of an edge, this goes red — which is the only
// version of "these two are related" that is worth anything.
//
// It is also how the deployment reports back. Runtime 07 is a reference model
// with no real consumer; the Field Guide is one. Most of what 07 says survived
// contact with a walking AR game. One gate did not, and L7 is that finding,
// written as a live failing check rather than a caveat.

import { existsSync } from 'node:fs';
import { pathToFileURL } from 'node:url';

// --- locate the lab --------------------------------------------------------
const LAB =
  process.env.DTG_LAB ||
  '/Volumes/24mitchuski/mouseaugust/dtgwg-cred-spec-main_mage';
const LAB_07 = `${LAB}/runtimes/07-trust-graph-formation/src/trust-graph.mjs`;

if (!existsSync(LAB_07)) {
  console.error(`\n  lab not found at ${LAB_07}`);
  console.error(`  set DTG_LAB=/path/to/dtgwg-cred-spec-main_mage and re-run\n`);
  process.exit(2);
}

// pathToFileURL, not the bare path — Windows absolute paths parse as a 'c:' URL
// scheme in the ESM loader and the import fails for a reason that is not the lab's.
const lab = await import(pathToFileURL(LAB_07).href);
const { joinCommunity, roster, TrustGraph: LabGraph, dreamCycleTurn, Mage, Swordsman, encounter, rdid: labRdid } = lab;

// --- the Field Guide model -------------------------------------------------
import { avatar, rdid as fgRdid } from '../meet-overlay/src/identity.mjs';
import { TrustGraph as FgGraph, offer, accept, confirm } from '../meet-overlay/src/meet.mjs';
import { REGISTER } from '../fixtures/register.mjs';

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
    console.log(`  ${red('FAIL')} ${name}${detail ? ` — ${detail}` : ''}`);
  }
}

const T0 = 1755000000;
const AT = { lat: 51.5344, lon: -0.1016 };

// --- lab side --------------------------------------------------------------
const VTC = 'vtc:field-guide';
const L1 = joinCommunity('human-1', VTC);
const L2 = joinCommunity('human-2', VTC);
const L3 = joinCommunity('human-3', VTC);
const members = roster([L1, L2, L3]);

// --- game side -------------------------------------------------------------
const A = avatar('avatar-a', 'secret-a');
const B = avatar('avatar-b', 'secret-b');
const C = avatar('avatar-c', 'secret-c');

function fgMeet(g, from, to, opts = {}) {
  const {
    nonceA = `n-${from.avatarId}-${to.avatarId}`, nonceB = `m-${to.avatarId}`,
    consentB = true, consentA = true, tamper = null, confirmer = from, t = T0,
    scanAt = { lat: AT.lat + 0.0001, lon: AT.lon + 0.0001 },
  } = opts;
  const off = offer(from, { nonce: nonceA, lat: AT.lat, lon: AT.lon, nowUtc: t, presentAs: 'x' });
  const acc = accept(to, off, { nonce: nonceB, lat: scanAt.lat, lon: scanAt.lon, nowUtc: t + 5, consent: consentB, presentAs: 'y' });
  if (tamper) tamper(acc);
  return confirm(confirmer, acc, g, { nowUtc: t + 10, consent: consentA });
}

console.log('\nlab bridge — the same claims, run through both models\n');
console.log(`  lab: ${LAB}\n`);

// ===========================================================================
// The shared core: five gates that must behave identically in both.
// ===========================================================================
{
  const lg = new LabGraph();
  const fg = new FgGraph();
  const labR = dreamCycleTurn(members, lg, L1, L2, 'meet', true, true);
  const fgR = fgMeet(fg, A, B);
  check('B1 a consenting meet forms exactly one edge in both models', labR.grew === true && lg.edges.length === 1 && fgR.formed === true && fg.links.size === 1);
}
{
  const lg = new LabGraph();
  const fg = new FgGraph();
  const labR = dreamCycleTurn(members, lg, L1, L2, 'meet', true, false);
  const fgR = fgMeet(fg, A, B, { consentB: false });
  check('B2 unilateral consent is refused by both, under the same name', labR.reason === 'unilateral-no-mutual-consent' && fgR.reason === 'unilateral-no-mutual-consent');
}
{
  const lg = new LabGraph();
  const fg = new FgGraph();
  const labR = dreamCycleTurn(members, lg, L1, L1, 'meet', true, true);
  const fgR = fgMeet(fg, A, A);
  check('B3 a self-edge is refused by both, under the same name', labR.reason === 'self-edge-forbidden' && fgR.reason === 'self-edge-forbidden');
}
{
  const lg = new LabGraph();
  const fg = new FgGraph();
  dreamCycleTurn(members, lg, L1, L2, 'meet', true, true);
  const labR = dreamCycleTurn(members, lg, L1, L2, 'meet-again', true, true);
  fgMeet(fg, A, B);
  const fgR = fgMeet(fg, A, B, { nonceA: 'fresh' });
  check('B4 the edge is idempotent in both (duplicate-edge / duplicate-link)', labR.reason === 'duplicate-edge' && fgR.reason === 'duplicate-link');
}
{
  // The Gap: in both models the prover recomputes the commitment and refuses
  // the proposer's claim. This is the structural property, not a detail.
  const lg = new LabGraph();
  const shared = encounter(L1, L2, 'meet');
  const cand = Mage.propose(L1, L2, shared, true, true);
  cand.claimedVrc = 'forged';
  const labV = Swordsman(members, lg).prove(cand);
  const fg = new FgGraph();
  const fgR = fgMeet(fg, A, B, { tamper: (a) => (a.claimedLink = 'forged') });
  check('B5 the Gap holds in both — a forged commitment is recomputed away', labV.signed === false && labV.reason === 'vrc-commitment-forged' && fgR.reason === 'link-commitment-forged');
}
{
  const labFresh = labRdid(L1, L2.member) !== labRdid(L1, L3.member);
  const fgFresh = fgRdid(A, B.avatarId) !== fgRdid(A, C.avatarId);
  check('B6 R-DID freshness per counterparty holds in both', labFresh && fgFresh);
}

// ===========================================================================
// The finding. Runtime 07 gate G2 requires both endpoints to be personhood-
// anchored. The Field Guide has nothing to anchor to, so the game's own node
// type does not clear the lab's own gate. This is not a bug in either model —
// it is the boundary between them, and it belongs in a test rather than a
// caveat, because a caveat cannot go red.
// ===========================================================================
{
  const lg = new LabGraph();
  // An OASIS avatar presented to the lab's prover: it has an id, but no
  // personhood anchor, so it is not in the community roster.
  const impostor = { member: A.avatarId, secret: A.secret };
  const cand = Mage.propose(L1, impostor, encounter(L1, { member: A.avatarId }, 'meet'), true, true);
  const verdict = Swordsman(members, lg).prove(cand);
  check('B7 an OASIS avatar fails the lab personhood gate (G2) — the honest boundary', verdict.signed === false && verdict.reason === 'endpoint-not-personhood-anchored');
}

// ===========================================================================
// The delta, asserted rather than asserted-in-prose. The Field Guide adds
// exactly four gates to the lab's core and no others: three physical ones a
// proverb exchange between two agents does not need (freshness, replay,
// co-location) plus one routing check (`offer-not-mine`) that only exists
// because the rite is carried over an HTTP endpoint rather than between two
// co-present processes. Writing the count down here is what makes a fifth,
// added quietly, go red.
// ===========================================================================
{
  const LAB_CORE = new Set([
    'endpoint-not-personhood-anchored',
    'self-edge-forbidden',
    'unilateral-no-mutual-consent',
    'r-did-mismatch',
    'vrc-commitment-forged',
    'duplicate-edge',
  ]);
  const RENAMED = new Map([
    ['duplicate-link', 'duplicate-edge'],
    ['link-commitment-forged', 'vrc-commitment-forged'],
  ]);
  const fgMeetCodes = REGISTER.filter((r) => r.layer === 'meet').map((r) => r.code);
  const novel = fgMeetCodes.filter((c) => !LAB_CORE.has(RENAMED.get(c) || c));
  const expected = ['offer-not-mine', 'meet-offer-expired', 'meet-offer-replayed', 'meet-not-colocated'];
  check(
    `B8 the physical delta is exactly ${expected.length} gates and no more`,
    novel.length === expected.length && expected.every((e) => novel.includes(e)),
    `novel: ${novel.join(', ')}`,
  );
}

// ===========================================================================
// The deliberate divergence. Runtime 07 models transitive reachability and is
// right to: "does trust reach" is a real question about a trust graph. The
// overlay asks a different one — "who may see" — and answering it with
// reachability is how a trust score gets built by accident. Both models are
// correct; they are answering different questions, and that must be visible.
// ===========================================================================
{
  const lg = new LabGraph();
  dreamCycleTurn(members, lg, L1, L2, 'e12', true, true);
  dreamCycleTurn(members, lg, L2, L3, 'e23', true, true);
  const labReaches = lg.connected(L1.member, L3.member);

  const fg = new FgGraph();
  fgMeet(fg, A, B);
  fgMeet(fg, B, C, { nonceA: 'n-bc' });
  const fgSees = fg.isOneHop(A.avatarId, C.avatarId);

  check('B9 trust REACHES two hops in the lab and SEES nothing two hops in the game', labReaches === true && fgSees === false);
}

// ===========================================================================
// Domain separation: the two models must never produce a value the other
// could mistake for its own. A Field Guide link commitment is not a DTG VRC.
// ===========================================================================
{
  const labVal = labRdid(L1, L2.member);
  const fgVal = fgRdid(A, B.avatarId);
  const collide = labVal === fgVal;
  check('B10 the two models are domain-separated — no digest can be confused', !collide);
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
