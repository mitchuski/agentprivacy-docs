// Identity — one OASIS avatar, JWT is identity (handoff §11).
//
// The avatarId is the public handle the game already has. The secret never
// leaves the holder; it exists so each side can mint a FRESH, UNIQUE R-DID per
// counterparty (cred-spec R-DID uniqueness). Two peers who both know Mitch see
// two different R-DIDs for him and cannot join them.
//
// Swordsman = the full-context root. Mage = a projection of it. Nothing in the
// overlay path ever reads the Swordsman side; see promise.mjs.

import { H } from './hash.mjs';

const DOMAIN_RDID = 'arworld/r-did/v0';

export function avatar(avatarId, secret) {
  return { avatarId, secret };
}

// Deterministic to the holder, unlinkable across relationships to everyone else.
export function rdid(node, counterpartyAvatarId) {
  return H(DOMAIN_RDID, node.secret, counterpartyAvatarId);
}
