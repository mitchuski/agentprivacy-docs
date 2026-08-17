// STORY — the `wikiSlug` seam. Handoff §8, the one join the counter-spec had
// not touched.
//
// §8 sets the rule: FedWiki is lore, not the POI database; the game does not
// write journal pages on every Witness ("would spam the neighborhood"); and the
// only sanctioned two-way path is to **fork** a stub page that links the
// canonical slug — Dave's neighbourhood model, not an overwrite API.
//
// Modelling it turned up something that is not in any of the three specs, and
// that I think matters more than the feature does:
//
//   A WIKI FORK IS NOT AN AUDIENCE. IT IS A QUANTIFIER CHANGE.
//
// The Promise ladder — public / link / acquaintance — answers "how much do I
// show THIS counterparty". Every tier on it, including `public`, is scoped to
// somebody you are handing something to. A federated wiki page has no
// counterparty. It is readable by everyone, forever, and it propagates by
// design: that is what federation IS. So `public` on the Promise ladder and
// `public` on a wiki are false friends, and a fork path that reads the audience
// ladder to decide what it may publish will quietly publish a player's trail to
// the world because their pin was marked with the LEAST private tier.
//
// Hence: publication is its own consent, per discovery, defaulting to off, and
// it is not implied by any audience whatsoever. `WORLD` is deliberately not a
// member of AUDIENCES — it cannot be reached by widening.

import { project } from './promise.mjs';
import { digest } from './canonical.mjs';
import { toIso } from './time.mjs';

export const WORLD = 'world'; // not on the audience ladder, and never will be

// ---------------------------------------------------------------------------
// After a Witness, the client MAY offer a fork. It may not perform one.
// Returns a refusal or a page ready to be forked into the player's own space.
// ---------------------------------------------------------------------------
export function proposeFork(holon, { publishConsent = false, playerSite, canonicalSite, nowUtc }) {
  const refuse = (reason) => ({ forked: false, reason });

  // 1. §8 — the game does not write a page on every Witness.
  if (!publishConsent) return refuse('no-publication-consent');
  // 2. Publication is not reachable by widening an audience. A pin whose owner
  //    chose `private` is out regardless of what they tap next.
  const policy = holon.disclosure || {};
  if (policy.maxAudience === 'private') return refuse('holon-ceiling-private');
  // 3. A place needs a canonical page to link to. Without a slug there is
  //    nothing to fork FROM, and minting one would make the game the source of
  //    truth for lore — which is exactly the inversion §8 forbids.
  if (!holon.wikiSlug || holon.wikiSlug === 'city-discover') {
    return refuse('no-canonical-slug');
  }
  // 4. Idempotent per (avatarId, poiId): a second Witness does not re-fork.
  if (holon.forkedSlug) return refuse('already-forked');

  // The forked page carries the PUBLIC projection only — never the note, never
  // the quest. A player publishing a stub about the British Museum is not
  // publishing what they thought about it.
  const shown = project(holon, 'public');

  const forkedSlug = `${holon.poiId}-witnessed`;
  const page = {
    title: shown.title,
    // Fedwiki journal: the fork event names where it came from. This is the
    // whole reason to fork rather than copy — the provenance survives, and the
    // canonical page can still see its own lineage.
    journal: [
      { type: 'fork', site: canonicalSite, date: nowUtc * 1000 },
      { type: 'create', date: nowUtc * 1000, item: { title: shown.title } },
    ],
    story: [
      {
        type: 'paragraph',
        id: digest({ poiId: shown.poiId, slug: forkedSlug }).slice(0, 16),
        text: `Witnessed ${toIso(nowUtc).slice(0, 10)}. See [[${holon.wikiSlug}]].`,
      },
    ],
    // Join keys, per handoff §8: space is the poiId, story is the slug.
    poiId: shown.poiId,
    canonicalSlug: holon.wikiSlug,
    site: playerSite,
  };

  return { forked: true, slug: forkedSlug, page, publishedFields: Object.keys(shown).sort() };
}
