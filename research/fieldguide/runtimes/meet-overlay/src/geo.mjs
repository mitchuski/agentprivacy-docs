// Distance. Haversine, metres. Used by two different gates:
//   - the Meet rite (were these two avatars actually in the same place?)
//   - the nearby query (distance-first, and nothing outside the viewport)

const R = 6371000;
const rad = (d) => (d * Math.PI) / 180;

export function metresBetween(lat1, lon1, lat2, lon2) {
  const dLat = rad(lat2 - lat1);
  const dLon = rad(lon2 - lon1);
  const a =
    Math.sin(dLat / 2) ** 2 +
    Math.cos(rad(lat1)) * Math.cos(rad(lat2)) * Math.sin(dLon / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(a));
}

// Coarse geo for the public audience: ~100 m of resolution, enough to say
// "Islington", not enough to say "this doorway".
export const coarse = (n) => Math.round(n * 1000) / 1000;
