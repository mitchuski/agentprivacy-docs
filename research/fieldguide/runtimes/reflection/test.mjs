// REFLECTION COVERAGE — the map cannot rot.
//
//   node test.mjs
//
// ../../REFLECTION-MAP.md sets the ARWorld work against the DTG lab work, row by
// row, and anchors every row to a property with `prop:XX`. This suite runs the
// real suites, collects the properties that actually exist, and checks the map
// against them in BOTH directions:
//
//   every anchor resolves      — a renamed or deleted property turns the map red
//   every property is placed   — a new property must be mapped or explicitly
//                                excused, so the map cannot quietly fall behind
//
// The second direction is the one that matters. Anchors going stale is annoying;
// a map that silently stops describing the work is worse, because it keeps
// reading as if it does.

import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const MAP_PATH = fileURLToPath(new URL('../../REFLECTION-MAP.md', import.meta.url));

const SUITES = [
  `${HERE}../meet-overlay/test.mjs`,
  `${HERE}../fixtures/test.mjs`,
  `${HERE}../lab-bridge/test.mjs`,
];

// --- what actually exists --------------------------------------------------
const live = new Set();
for (const s of SUITES) {
  let out = '';
  try {
    out = execFileSync(process.execPath, [s], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
  } catch (e) {
    out = e.stdout || '';
  }
  for (const line of out.split('\n')) {
    const m = line.replace(/\x1b\[[0-9;]*m/g, '').match(/^\s+(?:PASS|FAIL)\s+([A-Z]+\d+[a-z]?)\s/);
    if (m) live.add(m[1]);
  }
}

// --- what the map claims ---------------------------------------------------
const map = readFileSync(MAP_PATH, 'utf8');
const anchored = new Set([...map.matchAll(/prop:([A-Z]+\d+[a-z]?)/g)].map((m) => m[1]));

const fence = map.match(/```unmapped\n([\s\S]*?)```/);
const excused = new Map();
if (fence) {
  for (const line of fence[1].split('\n')) {
    const m = line.match(/^([A-Z]+\d+[a-z]?)\s+—\s+(.+)$/);
    if (m) excused.set(m[1], m[2].trim());
  }
}

// --- check -----------------------------------------------------------------
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

console.log('\nreflection coverage — REFLECTION-MAP.md against the live suites\n');
console.log(`  ${live.size} properties live · ${anchored.size} anchored · ${excused.size} excused\n`);

{
  const dangling = [...anchored].filter((p) => !live.has(p)).sort();
  check('R1 every anchor in the map resolves to a live property', dangling.length === 0, `dangling: ${dangling.join(', ')}`);
}
{
  const orphans = [...live].filter((p) => !anchored.has(p) && !excused.has(p)).sort();
  check('R2 every live property is mapped or explicitly excused', orphans.length === 0, `unplaced: ${orphans.join(', ')}`);
}
{
  const both = [...anchored].filter((p) => excused.has(p)).sort();
  check('R3 nothing is both anchored and excused', both.length === 0, `both: ${both.join(', ')}`);
}
{
  const bare = [...excused.entries()].filter(([, why]) => !why || why.length < 12).map(([p]) => p);
  check('R4 every excused property carries a reason', bare.length === 0, `bare: ${bare.join(', ')}`);
}
{
  // The map's whole claim is that the two bodies of work touch. If no row cites
  // the bridge suite, the reflection is being asserted rather than exercised.
  const bridgeAnchors = [...anchored].filter((p) => p.startsWith('B'));
  check(`R5 the map is anchored to the lab bridge in ${bridgeAnchors.length} places`, bridgeAnchors.length >= 5);
}
{
  const statuses = ['reflected', 'refined', 'diverged', 'absent', 'new'];
  const missing = statuses.filter((s) => !map.includes(`**${s}**`) && !map.includes(`| ${s} `) && !map.includes(`${s} —`));
  check('R6 every status in the closed vocabulary is actually used', missing.length === 0, `unused: ${missing.join(', ')}`);
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
