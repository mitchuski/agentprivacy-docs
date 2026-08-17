// CANONICAL ENCODING — the byte-exact form of a projection.
//
// This exists so a second implementation can prove it agrees. A counter-spec
// that only a JavaScript model can evaluate is a description; a counter-spec
// with a canonical form and a second-language consumer is a target you can be
// tested against. The DTG lab learned this the expensive way: `runtimes/
// canonical` exists because two implementations agreed on every field and still
// produced different digests, and nobody could see why for a day.
//
// Rules, all of them chosen to be boring in every language:
//
//   - keys sorted lexicographically, ASCII
//   - one `key=value` per line, joined with \n
//   - an ABSENT key is omitted entirely; it is not an empty value. `note`
//     missing and `note` empty are different facts and must not collide.
//   - numbers are fixed to 6 decimal places. Not because we need micrometres,
//     but because `1` vs `1.0` vs `1e0` is the single most common way two
//     JSON serialisers silently disagree.
//   - booleans are `true` / `false`
//   - the domain line is part of the preimage, so a projection digest can
//     never be confused with a commitment digest
//
// If you are implementing this in C#: `value.ToString("F6",
// CultureInfo.InvariantCulture)`. The invariant culture matters — a decimal
// comma will pass every unit test written in a de-DE locale and fail every
// interop check.

import { createHash } from 'node:crypto';

export const CANON_DOMAIN = 'arworld/canonical/v0';

export function num(x) {
  return Number(x).toFixed(6);
}

function enc(v) {
  if (typeof v === 'number') return num(v);
  if (typeof v === 'boolean') return v ? 'true' : 'false';
  return String(v);
}

export function canonical(obj) {
  const lines = [CANON_DOMAIN];
  for (const k of Object.keys(obj).sort()) {
    const v = obj[k];
    if (v === undefined || v === null) continue; // absent ≠ empty
    lines.push(`${k}=${enc(v)}`);
  }
  return lines.join('\n');
}

export function digest(obj) {
  return createHash('sha256').update(canonical(obj), 'utf8').digest('hex');
}
