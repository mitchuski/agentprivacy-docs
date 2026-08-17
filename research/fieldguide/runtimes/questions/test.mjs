// QUESTION COVERAGE — every question in the ARWorld pack has a runnable answer.
//
//   node test.mjs
//
// ../../QUESTION-MAP.md lists all twenty questions from Max's three documents
// and anchors each to the properties that answer it. This checks the map rather
// than the model:
//
//   every question carries at least one anchor   — no row answered by prose alone
//   every anchor resolves to a live property     — no answer that has been deleted
//   the inventory stays at twenty                — a new question in their docs
//                                                  must be added deliberately
//
// The middle failure is the one worth having. It is easy to answer a question in
// prose and believe it is handled; it is harder to keep believing that when a
// suite says the row is empty.

import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';

const HERE = fileURLToPath(new URL('.', import.meta.url));
const MAP = readFileSync(fileURLToPath(new URL('../../QUESTION-MAP.md', import.meta.url)), 'utf8');

const SUITES = ['meet-overlay', 'fixtures', 'lab-bridge', 'acceptance', 'open-questions'];

const live = new Set();
for (const s of SUITES) {
  let out = '';
  try {
    out = execFileSync(process.execPath, [`${HERE}../${s}/test.mjs`], { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] });
  } catch (e) {
    out = e.stdout || '';
  }
  for (const line of out.split('\n')) {
    const m = line.replace(/\x1b\[[0-9;]*m/g, '').match(/^\s+(?:PASS|FAIL)\s+([A-Z]+\d+[a-z]?)\s/);
    if (m) live.add(m[1]);
  }
}

// Question rows look like: | **Q-H1** | "…" | … | `prop:M1` `prop:M2` |
const rows = [...MAP.matchAll(/\|\s*\*\*(Q-[A-Z]+\d+)\*\*\s*\|([^\n]*)/g)].map((m) => ({
  id: m[1],
  anchors: [...m[2].matchAll(/prop:([A-Z]+\d+[a-z]?)/g)].map((x) => x[1]),
}));

let passed = 0;
let failed = 0;
const green = (s) => `\x1b[32m${s}\x1b[0m`;
const red = (s) => `\x1b[31m${s}\x1b[0m`;
const check = (name, cond, d) => {
  if (cond) { passed++; console.log(`  ${green('PASS')} ${name}`); }
  else { failed++; console.log(`  ${red('FAIL')} ${name}${d ? `\n         ${d}` : ''}`); }
};

const EXPECTED = 20;
const groups = { 'Q-H': 7, 'Q-T': 4, 'Q-A': 5, 'Q-D': 4 };

console.log('\nquestion coverage — QUESTION-MAP.md against the live suites\n');
console.log(`  ${rows.length} questions · ${new Set(rows.flatMap((r) => r.anchors)).size} distinct answers · ${live.size} properties live\n`);

{
  check(`QM1 the inventory is ${EXPECTED} questions`, rows.length === EXPECTED, `found ${rows.length}`);
}
{
  const bare = rows.filter((r) => r.anchors.length === 0).map((r) => r.id);
  check('QM2 no question is answered by prose alone', bare.length === 0, `unanswered: ${bare.join(', ')}`);
}
{
  const dangling = rows.flatMap((r) => r.anchors.filter((a) => !live.has(a)).map((a) => `${r.id}→${a}`));
  check('QM3 every answer resolves to a property that runs', dangling.length === 0, `dangling: ${dangling.join(', ')}`);
}
{
  const wrong = Object.entries(groups).filter(([p, n]) => rows.filter((r) => r.id.startsWith(p)).length !== n);
  check('QM4 all four source sections are represented in full', wrong.length === 0, wrong.map(([p, n]) => `${p} expected ${n}, got ${rows.filter((r) => r.id.startsWith(p)).length}`).join('; '));
}
{
  // Their §6 acceptance checklist is the part they can act on today, so it gets
  // its own assertion rather than being folded into the count above.
  const acceptance = rows.filter((r) => r.id.startsWith('Q-A'));
  const allRun = acceptance.every((r) => r.anchors.length > 0 && r.anchors.every((a) => live.has(a)));
  check('QM5 every Phase 0 acceptance criterion is executable', allRun);
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
