// The map ranking — ARWORLD_TRUST_WEIGHTED_POI §5, made mechanical.
//
// Their table specifies the terms: distance is the primary sort with a hard cut
// at `spawnRadiusM`; a curated seed with real narration is worth a soft −350 m;
// a pin in `fromGraph` or in `self` gets a score band; memorial/plaque clutter
// is penalised or filtered.
//
// Modelling it as an **effective distance** rather than an abstract score is
// deliberate. A score invites a leaderboard; a distance in metres cannot become
// one, because every term has to answer "how many metres is this worth?" out
// loud. "Maya was here" is worth walking 400 m for. That is a sentence a
// designer can argue with, which "+0.3 trust weight" is not.
//
// The invariant that carries §1's "this is not Yelp": the hard cut is on TRUE
// distance, never effective distance. No bonus can drag a far pin into the
// viewport — and no amount of other people's enthusiasm changes where a pin
// ranks for you (property R5).

export const BANDS = {
  hasRealCopy: 350,   // §5: soft −350 m, curated seed with real narration
  fromGraph: 400,     // a peer you have met was here
  self: 600,          // your own trail
  memorial: -1500,    // §5: penalty; see FILTER_MEMORIAL for the other option
};

export const FILTER_MEMORIAL = true; // §5 says "penalty / filter"; we filter

export function effectiveDistance(pin, trueDistanceM) {
  let d = trueDistanceM;
  if (pin.hasRealCopy) d -= BANDS.hasRealCopy;
  if (pin.origin === 'trust') d -= BANDS.fromGraph;
  if (pin.origin === 'self') d -= BANDS.self;
  if (pin.memorial) d -= BANDS.memorial; // negative band = penalty
  return d;
}

// One ranked list from the floor plus the overlay. `spawnRadiusM` cuts on TRUE
// distance before any band is applied.
export function rank(pins, { spawnRadiusM, cap, distanceOf }) {
  const admitted = [];
  for (const p of pins) {
    const d = distanceOf(p);
    if (d > spawnRadiusM) continue;                       // hard cut, true distance
    if (FILTER_MEMORIAL && p.memorial) continue;          // §5 clutter stays out
    admitted.push({ pin: p, d, eff: effectiveDistance(p, d) });
  }
  admitted.sort((a, b) => a.eff - b.eff || a.d - b.d);
  return admitted.slice(0, cap).map((x) => ({ ...x.pin, _d: Math.round(x.d), _eff: Math.round(x.eff) }));
}

// §5 marker styles, and the whole of §6's last acceptance line: the style is the
// only thing that varies by origin. There is no number attached to a person.
export function markerStyle(pin) {
  if (pin.origin === 'self') return 'ring-teal';
  if (pin.origin === 'trust') return 'ring-gold';
  return pin.markerStyle || 'discover-default';
}

// Every numeric field a pin is allowed to carry. Closed on purpose: a
// `trustScore`, a `reputation`, or a `popularity` cannot appear without failing
// property A5. `_d`/`_eff` are ranking internals and are stripped before a pin
// leaves the server.
export const ALLOWED_NUMERIC = ['lat', 'lon', 'freshness', 'witnessCount', 'radiusM'];

export const strip = (pin) => {
  const { _d, _eff, ...rest } = pin;
  return rest;
};
