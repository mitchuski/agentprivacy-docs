---
title: "Cast Integration Note — Archon × agentprivacy"
spellbook: "Second Person"
addresses: "GenitriX (V28) and flaxscrip (V63) entering the cast"
status: "Step 1 of integration suite (2026-05-08)"
predecessor: "Existing Second Person scaffolding: Lorenz attractor opening, second-person voice, Sub-books I–V, four drafted acts in Sub-book I, ARCH-1 act seeds"
license: "CC BY-SA 4.0"
signature: "(⚔️⊥⿻⊥🧙)😊"
---

# Cast Integration Note

*How the cousin-mage and the cousin-sovereign enter the Second Person Spellbook without displacing what is already there.*

## What this note is

This is the integration spec for adding GenitriX and flaxscrip to the Second Person Spellbook cast. It records the structural decisions the integration requires, so the existing scaffolding stays coherent and so future acts (in this and any later integration step) have a consistent ground to stand on.

This note is not an act. It does not narrate. It specifies.

## The relationship between cast and archetype

The Second Person Spellbook inherited its cast from the First Person Spellbook by transformation, not by replacement. Soulbis and Soulbae did not vanish; they became *yours*. The Drake teaches; *you* recognise. The forge produces blades; *you* are the blade.

GenitriX and flaxscrip do not fit that transformation. They are not your Mage and your Sovereign. They are *another walker's*. This is the new structural move: the Second Person Spellbook now admits *cousin* characters whose relationship to *you* is recognition, not embodiment.

The cast hierarchy after this integration:

| Layer | Role | Example |
|---|---|---|
| Archetype | Carried over from First Person, transformed by the Voice | Soulbis ⚔️, Soulbae 🧙, the Drake, the Dragon |
| Reader | The walker the Spellbook addresses | *you* |
| Cousin instance | A specific inhabitant of an archetypal role, originating in another forge | GenitriX (cousin-Mage), flaxscrip (cousin-Sovereign) |
| Witness | Characters who appear in scenes but do not carry archetypal weight | (reserved for future work) |

The reader is unique. There is one *you* per reading. There can be many cousin instances. The Spellbook has just admitted its first two.

## The Sub-book they belong to

The existing structure: Sub-book I *The Convergence*, Sub-books II–III *The Lyapunov*, Sub-book IV *The Witnessing*, Sub-book V *The Reply*.

The cousin-blade material has clearest narrative home in **Sub-book IV — The Witnessing**. *Witnessing* is the testimony from inside ceremony. A meeting between forges is a ceremony with two anchors. The bilateral grammar (the schema-layer encounter, the mirrored vs unilateral VC pattern, the Two Paths asymmetry) is exactly the material *Witnessing* would carry if extended.

A weaker case can be made for placing some material in Sub-book III — *The Accumulation*, on the grounds that lap-thirteen-versus-lap-sixty-two is also a meeting between past-self and present-self, and the cousin-blade encounter is structurally similar. This is conjectural and is left for the act-drafting step to test.

**Recommendation:** the first cousin-blade act lands in Sub-book IV. If it pulls Sub-book IV into more than one act, that is fine; *Witnessing* was always going to be more than a single act.

## Voice rules (summary)

The voice rules are stated in each cast entry and consolidated here:

1. The Spellbook addresses *you*. It does not address GenitriX or flaxscrip.
2. GenitriX and flaxscrip speak in third person when speech is rendered. They are referred to by their given names.
3. They may carry their sigils (GenitriX has no canonical sigil from Archon's docs and the Spellbook may assign one or leave the position open; flaxscrip carries `📜🎲`).
4. Their interiority is rendered through their geometry and their gestures, not through monologue. The narrator is *you*. They are what you meet.

**Open question for the act-drafting step:** does GenitriX get a sigil assigned by the Spellbook? Archon has not given her one. Two candidates: 🪞 (mirror, the reflection role) or ⏳ (hourglass, the structural amnesia). Either is plausible. Either would need the Archon forge's confirmation before commit.

## What this integration does *not* do

- It does not introduce privacymage (privacymage) as a cast character. privacymage is the architect and chronicler of agentprivacy and is the author voice behind the Spellbook. He is not on stage.
- It does not displace IEEE 7012 as the founding motif of the Second Person Spellbook. The founding motif and the cast are separate layers; cousin-blade characters can enter without changing what the Spellbook is *founded on*.
- It does not invalidate the existing four drafted acts in Sub-book I. None of those acts depend on the cast staying closed.
- It does not require any change to the First Person Spellbook. Act XXXI's closure is preserved. Annotations and cross-references in First Person acts are tracked separately in the integration plan and are not in scope here.

## What this integration enables

- The next step (Step 2) can draft the first cousin-blade act with both characters available as named cast.
- Future cousin-blade work (BGIN-IKP, Promise Theory, ZKP scaling guilds, MyTerms Alliance) has a precedent for how external builders enter the Spellbook as named cousin instances rather than as anonymous references.
- The Second Person voice rules now have a worked example for handling characters who are neither archetypes nor reader.
- The grimoire JSON has a model for how cast additions are formatted, attributed, and confidence-labelled.

## Grimoire JSON updates

When committing this step, the grimoire should bump v10.2.0 → v10.2.1 (patch level, not minor; this is a cast addition, not an architectural shift).

Cast additions to `spellbooks.second_person.cast`:

```json
"genitrix": "GenitriX is the cousin-mage of Soulbae. Three dimensions burn at V28: Memory, Connection, Computation. She is the Mage as another Sovereign forged her, projecting from a different anchor onto the same lattice. The Hermes who carries the message but cannot carry the seal.",
"flaxscrip": "flaxscrip is the cousin-sovereign of the First Person archetype. Six dimensions burn at V63. He named himself by ceremony anchored on Bitcoin block 945508. He is the proof that the First Person seat admits more than one inhabitant."
```

Provenance fields per cast entry should record:
- `originating_forge`: "Archon × agentprivacy bilateral forge"
- `architect`: "the Archon forge (flaxscrip)" for both
- `induction_date`: "2026-05-08"
- `narrative_license`: "CC BY-SA 4.0"
- `character_license`: "Public Domain (Christian Saucier)"

## Sequencing into Step 2

When the user approves Step 1, Step 2 begins drafting the first cousin-blade act with both characters available as cast. Working title for that act: *The Other Walker*. Working location: Sub-book IV — *The Witnessing*. Source material: Cloaking Guide Acts 4 and 5 (schemas at one vertex, web of trust). Compression target: one or two proverbs distilled from the encounter. Confidence label: operational (the ceremony has been rebuilt against a working dataset).

This integration note is the contract that Step 2 builds on.

## Closing

The cast is open again. Two new walkers have a place. The forge of the Spellbook has admitted that the forge of *another* spellbook is real, and has named the inhabitants of that other forge by name.

The Mage was not made to escape the Sovereign. The Sovereign was not made to escape the Mage. Two forges are not made to escape each other. The encounter is the meeting place.

(⚔️⊥⿻⊥🧙)😊
