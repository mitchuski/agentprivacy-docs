---
name: overlay-key-minting
description: Convert woven overlay threads into understanding cards (understanding-compression format, cohere-gated) whose principles line is the thread's PROVERB — the moving-understanding-as-key surface for the V6 research programme. Use after WEAVE.md exists for a run.
scope: overlays/keys/ only; gate = ~/.claude/skills/understanding-compression/understanding.py
---

# overlay-key-minting

A thread becomes a key when its understanding compresses to a proverb
that can regenerate it. This skill fuses the two house systems:

- **understanding-compression** supplies the card format and the
  round-trip cohere gate (invariant → maths/principles/actions +
  markets/plurality/intents + recheck).
- **understanding-as-key (RPP)** supplies the reading: the *principles*
  line of each card IS the thread's proverb, mintable as a recovery
  key; the *recheck* is the ceremony's convergence test — if
  compressing an expansion regenerates the invariant, the understanding
  opens the lock.

## Card recipe, per woven thread

- `key`: the thread's slug · `title`: the thread's name
- `invariant`: ONE sentence a physicist, a regulator and a bard would
  agree is the same claim. Take it from the thread's formal twin, not
  its poetry.
- `compressions.maths`: the actual quantity/relation (the theorem
  inequality, the bound, the count) from the anchors.
- `compressions.principles`: **the proverb, verbatim from the corpus if
  one exists, minted-and-marked if not.** This is the key.
- `compressions.actions`: the Monday act (usually the thread's
  casting-forward direction made concrete).
- `expansions.markets`: who pays/earns; often the grant/standards
  expression of the same thread.
- `expansions.plurality`: >=2 communities, in-register tellings — the
  natural pairs here are (researcher, mage), (regulator, guild),
  (developer, swordsman). Same invariant every telling.
- `expansions.intents`: why the thread exists; the casting-forward
  direction belongs here in full.
- `recheck`: honestly compress ONE expansion back; `matches: true`
  only if it truly recovers the invariant (the gate also measures term
  overlap — do not pad, fix drift by tightening the expansion).

## Gate (blocking)

```
python ~/.claude/skills/understanding-compression/understanding.py \
    cohere --cards overlays/keys/cards.json
```

Non-zero exit blocks the run's close. A card that fails is a thread
that was not actually understood; return it to the weave.

## RPP posture

Cards are OVERLAY keys: visibility 100% (declared ceremony class) by
construction, since the corpus is the first person's own. Inscribing
any proverb onchain, into spellweb, or into a VRC ceremony is a
first-person act outside this lane.
