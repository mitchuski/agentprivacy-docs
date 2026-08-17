// Time on the wire is ISO-8601 (ARWORLD_TRUST_WEIGHTED_POI §3.1). Time in the
// arithmetic is epoch seconds. Converting at the boundary rather than in the
// middle is deliberate: the DTG lab's canonical suite exists because an
// unpinned timestamp encoding is exactly the thing two implementations silently
// disagree about, and then their digests differ for a reason nobody can find.
//
// Pin it here, once, and the Python consumer of this model gets the same bytes.

export const toIso = (epochSec) => new Date(epochSec * 1000).toISOString();
export const fromIso = (iso) =>
  typeof iso === 'number' ? iso : Math.floor(Date.parse(iso) / 1000);

export const DAY = 86400;
