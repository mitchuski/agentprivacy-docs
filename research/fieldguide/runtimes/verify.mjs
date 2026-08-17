// Run everything and print a paste-able report.
//
//   node verify.mjs
//
// Same shape as the DTG lab's ceremony orchestrator: rebuild, run the suites,
// print something a person can paste into an issue without editing it. If you
// are filing a disagreement with the counter-spec, paste this above it — it
// says which version of the model you were arguing with.

import { execFileSync } from 'node:child_process';
import { readFileSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';

// fileURLToPath, not URL.pathname — pathname yields "/C:/…" on Windows, which
// node cannot open, and every suite then fails for a reason that is not the model's.
const HERE = fileURLToPath(new URL('.', import.meta.url));
const PYTHON = process.platform === 'win32' ? 'python' : 'python3';

const SUITES = [
  { name: 'meet-overlay', cmd: process.execPath, args: [`${HERE}meet-overlay/test.mjs`], what: 'the model' },
  { name: 'fixtures', cmd: process.execPath, args: [`${HERE}fixtures/test.mjs`], what: 'the conformance pack' },
  { name: 'consumer-py', cmd: PYTHON, args: [`${HERE}consumer-py/consume.py`], what: 'second-language agreement' },
  { name: 'lab-bridge', cmd: process.execPath, args: [`${HERE}lab-bridge/test.mjs`], what: 'agreement with the DTG lab' },
  { name: 'acceptance', cmd: process.execPath, args: [`${HERE}acceptance/test.mjs`], what: 'their Phase 0 checklist + score terms' },
  { name: 'open-questions', cmd: process.execPath, args: [`${HERE}open-questions/test.mjs`], what: 'the questions that had only prose' },
  { name: 'questions', cmd: process.execPath, args: [`${HERE}questions/test.mjs`], what: 'every question maps to a property' },
  { name: 'reflection', cmd: process.execPath, args: [`${HERE}reflection/test.mjs`], what: 'the reflection map cannot rot' },
];

const results = [];
for (const s of SUITES) {
  let out = '';
  let ok = true;
  try {
    out = execFileSync(s.cmd, s.args, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
  } catch (e) {
    ok = false;
    out = `${e.stdout || ''}${e.stderr || ''}`;
  }
  const m = out.match(/(\d+)\s+passed,\s+(\d+)\s+failed/);
  const agreed = out.match(/(\d+)\/(\d+)\s+digests byte-exact/);
  results.push({
    ...s,
    ok,
    tally: m ? `${m[1]}/${Number(m[1]) + Number(m[2])}` : agreed ? `${agreed[1]}/${agreed[2]}` : '?',
  });
}

const vectors = readFileSync(new URL('./fixtures/vectors.json', import.meta.url));
const packDigest = createHash('sha256').update(vectors).digest('hex');
const pack = JSON.parse(vectors);

const allGreen = results.every((r) => r.ok);
const w = Math.max(...results.map((r) => r.name.length));

console.log('\n--- arworld meet-overlay: verification report ---\n');
for (const r of results) {
  console.log(`  ${r.ok ? 'PASS' : 'FAIL'}  ${r.name.padEnd(w)}  ${r.tally.padStart(7)}   ${r.what}`);
}
console.log(`\n  vectors.json      sha256 ${packDigest}`);
console.log(`  register          ${new Set(pack.rejections.map((x) => x.code)).size} codes, all triggered live`);
console.log(`  projection vectors ${pack.projections.length}`);
console.log(`  node              ${process.version}`);
console.log(`\n  ${allGreen ? 'ALL GREEN' : 'FAILURES ABOVE'}\n`);

process.exit(allGreen ? 0 : 1);
