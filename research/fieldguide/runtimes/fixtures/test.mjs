// Conformance-pack properties. Run: node test.mjs
//
// These do not test the model. They test the VECTORS — that the register is
// honest, that the encoding is stable, and that the pack is safe to hand to
// somebody implementing this in another language.

import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { fileURLToPath } from 'node:url';
import { REGISTER, CODES } from './register.mjs';
import { project, NEVER_PROJECTED } from '../meet-overlay/src/promise.mjs';
import { canonical, digest } from '../meet-overlay/src/canonical.mjs';

const url = new URL('./vectors.json', import.meta.url);
const read = () => readFileSync(url);
const v = JSON.parse(read());

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

console.log('\nconformance pack — register coverage, closure, determinism, encoding\n');

// F1 — the property that makes a register worth having.
{
  const seen = new Set(v.rejections.map((r) => r.code));
  const missing = CODES.filter((c) => !seen.has(c));
  check(`F1 every register code is triggered live (${seen.size}/${CODES.length})`, missing.length === 0, missing.join(', '));
}

// F2 — closed vocabulary: nothing escapes the register.
{
  const stray = v.rejections.filter((r) => !CODES.includes(r.code));
  check('F2 no vector produces a code outside the register', stray.length === 0, stray.map((s) => s.code).join(', '));
}

// F3 — each entry means something distinct and is documented.
{
  const dupes = CODES.length !== new Set(CODES).size;
  const undocumented = REGISTER.filter((r) => !r.means || !r.layer);
  check('F3 the register has no duplicates and every entry is documented', !dupes && undocumented.length === 0);
}

// F4 — determinism. Regenerating must be byte-identical; the pack is only a
// conformance target if it does not move under its own generator.
{
  const before = createHash('sha256').update(read()).digest('hex');
  execFileSync(process.execPath, [fileURLToPath(new URL('./generate.mjs', import.meta.url))], { stdio: 'ignore' });
  const after = createHash('sha256').update(read()).digest('hex');
  check('F4 regenerating the pack is byte-identical', before === after);
}

// F5 — the digests in the pack actually follow from the canonical form.
{
  const bad = v.projections.filter(
    (p) => p.expect.projected && digest(project(p.holon, p.audience)) !== p.expect.digest,
  );
  check('F5 every projection digest recomputes from its holon', bad.length === 0, bad.map((b) => b.id).join(', '));
}

// F6 — and the canonical string in the pack matches too, so a consumer that
// cannot reproduce a digest can diff the preimage and see exactly where.
{
  const bad = v.projections.filter(
    (p) => p.expect.projected && canonical(project(p.holon, p.audience)) !== p.expect.canonical,
  );
  check('F6 every canonical preimage in the pack is reproducible', bad.length === 0);
}

// F7 — the leak check, applied to the shipped artefact rather than the code.
// The pack is what someone else implements against; if a forbidden field is
// visible in a vector, it will be visible in their implementation.
{
  const leaked = [];
  for (const p of v.projections) {
    if (!p.expect.projected) continue;
    for (const f of NEVER_PROJECTED) {
      if (p.expect.fields.includes(f)) leaked.push(`${p.id}:${f}`);
    }
  }
  check('F7 no shipped vector exposes a NEVER_PROJECTED field', leaked.length === 0, leaked.join(', '));
}

// F8 — a private ceiling produces no vector at all, at any audience.
{
  const priv = v.projections.filter((p) => p.id.startsWith('pj-private@'));
  check('F8 a private holon yields no projection at any audience', priv.length === 3 && priv.every((p) => p.expect.projected === false));
}

console.log(`\n  ${passed} passed, ${failed} failed\n`);
process.exit(failed === 0 ? 0 : 1);
