// THE REJECTION REGISTER — the closed vocabulary of every way this model says no.
//
// Borrowed wholesale from the DTG lab's `runtimes/fixtures`, where the register
// is the most useful artefact in the repository and nobody expected it to be.
// The reason is simple: two implementations agree about success trivially and
// disagree about failure constantly. "It rejected the request" is not interop.
// "It rejected the request with `meet-not-colocated`" is.
//
// The discipline that makes it worth anything is the coverage property in
// test.mjs: EVERY code below must be triggered by a live vector. A register
// entry nobody can produce is a documentation claim, and documentation claims
// are what this whole workbench exists to replace.

export const REGISTER = [
  // --- the Meet rite (person) ---------------------------------------------
  { code: 'offer-not-mine', layer: 'meet', means: 'the confirming avatar did not open this meet' },
  { code: 'self-edge-forbidden', layer: 'meet', means: 'a TrustLink with oneself is self-Sybil' },
  { code: 'unilateral-no-mutual-consent', layer: 'meet', means: 'one hand on it; a scan is an encounter' },
  { code: 'meet-offer-expired', layer: 'meet', means: 'the offer was a moment and the moment passed' },
  { code: 'meet-offer-replayed', layer: 'meet', means: 'the nonce is spent; a photographed QR is dead' },
  { code: 'meet-not-colocated', layer: 'meet', means: 'the two devices were not in the same place' },
  { code: 'link-commitment-forged', layer: 'meet', means: 'recomputation across the Gap disagreed' },
  { code: 'duplicate-link', layer: 'meet', means: 'one TrustLink per pair' },

  // --- Knowledge (place) ---------------------------------------------------
  { code: 'missing-required-field', layer: 'knowledge', means: 'witness payload incomplete; suffixed with the field' },
  { code: 'unknown-source', layer: 'knowledge', means: 'source outside the closed enum' },
  { code: 'unknown-rite', layer: 'knowledge', means: 'rite outside the closed enum — no auto-Witness' },

  // --- the overlay: named reasons a pin is absent ---------------------------
  { code: 'out-of-radius', layer: 'overlay', means: 'outside the viewport; Greenwich stays in Greenwich' },
  { code: 'no-trust-edge', layer: 'overlay', means: 'no 1-hop link and no grant' },
  { code: 'below-freshness-horizon', layer: 'overlay', means: 'eroded past the floor' },
  { code: 'audience-capped-private', layer: 'overlay', means: 'the owner capped this pin below any projection' },
  { code: 'over-overlay-cap', layer: 'overlay', means: 'ranked out by distance beyond the cap' },

  // --- the story seam (wiki) -----------------------------------------------
  { code: 'no-publication-consent', layer: 'story', means: 'publication is its own consent and defaults off' },
  { code: 'holon-ceiling-private', layer: 'story', means: 'a private pin is unpublishable at any consent' },
  { code: 'no-canonical-slug', layer: 'story', means: 'nothing to fork from; the game is not the lore source' },
  { code: 'already-forked', layer: 'story', means: 'one fork per (avatar, poi)' },

  // --- encounters that are never edges --------------------------------------
  { code: 'shared-quest-completion', layer: 'encounter', means: 'co-presence with a timestamp; no consent in it' },
  { code: 'steward-redeem', layer: 'encounter', means: 'a receipt; the parties are not symmetric' },
];

export const CODES = REGISTER.map((r) => r.code);
