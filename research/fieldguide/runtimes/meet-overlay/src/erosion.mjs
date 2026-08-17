// EROSION — ARWORLD_TRUST_WEIGHTED_POI §9.3: "should overlay pins require the
// peer to be recent (e.g. witnessed in the last 90 days)?"
//
// Yes. But 90 days as a boolean is a cliff, and a cliff is wrong for the same
// reason it is wrong in the DTG lab's `erosion-record` suite: assurance decays
// as a RATE. A pin does not stop being true on day 91. It stops being a good
// reason to walk somewhere, gradually, and the map should say so gradually.
//
// So: freshness is a half-life, and the horizon is a floor under it. Unity gets
// the scalar and can fade the ring rather than popping the pin.
//
// Your OWN trail never erodes. Erosion is about how much a peer's old
// enthusiasm should move you, not about whether you were there.

import { fromIso, DAY } from './time.mjs';

export const HALF_LIFE_DAYS = 90;
export const FRESHNESS_FLOOR = 0.25; // ~180 days at a 90-day half-life

export function ageDays(witnessedUtc, nowUtc) {
  return (nowUtc - fromIso(witnessedUtc)) / DAY;
}

export function freshness(witnessedUtc, nowUtc) {
  const d = Math.max(0, ageDays(witnessedUtc, nowUtc));
  return 0.5 ** (d / HALF_LIFE_DAYS);
}

export const aboveHorizon = (witnessedUtc, nowUtc) =>
  freshness(witnessedUtc, nowUtc) >= FRESHNESS_FLOOR;
