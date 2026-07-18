---
title: "The Moving Ceiling"
subtitle: "every static privacy guarantee has a shelf life · the first V6 result · a Privacy is Value essay"
series: "Privacy is Value"
version: "draft v3 for sync.soulbis.com · sequel to The Last Premine"
date: "2026-07"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "privacy_value_v6.md §5, §25, §27 · CONJECTURE_REGISTER_V6.md (head C93)"
---

# The Moving Ceiling

Last month, in [The Last Premine](https://sync.soulbis.com/p/privacy-is-value-the-last-premine), I read two events through one lens: a four-year-old flaw in a shielded pool found in a day, and an open benchmark counting down a quantum horizon. That essay ended with a call, for the V6 form of the equation to come into the light.

This is the first answer. And it starts by finishing that essay's last sentence.

The Last Premine closed on a new norm: the release of a frontier model is now a security event for every cryptographic protocol on earth. True, and incomplete. Here is the completion, and the verdict of this essay up front:

it is also a privacy event for every archive on earth. including yours.

## two clocks, briefly

For anyone arriving fresh, the instances in one breath each; the full telling, with the people and the graph that made the difference, is in the branch.

An Orchard circuit flaw slept for four years under expert eyes, then was found within a day of a sharper model reaching the one auditor equipped to point it. The circuit never changed. The reader did. And a withheld quantum result, published only as a proof that it exists, was independently reconstructed in about two months, the existence-claim itself pricing the search. Method perfectly hidden; timeline compressed anyway.

Two protected objects sat still. Two capabilities moved. That is all this essay needs from them, because the point of this essay is that the same shape governs something much closer to you than a circuit or a curve.

## the ceiling, written down

V6 gives the shape a formula, and it is short enough to carry.

Reconstruction, the question of whether an adversary can rebuild your private state from what you have emitted, is a ratio. On the bottom: the entropy of what you are protecting, fixed by you, because you emitted what you emitted. On top: the effective extraction capacity of the strongest decoder alive at time t. The bottom never moves. The top only climbs.

R(t) = adversary capacity at time t / your fixed private entropy

While R(t) stays below one, reconstruction fails and the ceiling holds. But the ceiling is not a ceiling. It is a ceiling with a rate of climb, and so every guarantee written against it inherits an expiry, the shelf life:

t* = the last moment at which the ceiling still holds

And this is the one place in the essay where you do not have to take the prose's word for the shape. The ceiling has an instrument now, on [the atlas](https://agentprivacy.ai/model/atlas), the model's new visual runtime: drag the frontier growth rate and watch t* slide toward you, with the conjecture's live confidence and status pulled from the register beside it, never embedded in the picture. The page is an open path you read. The atlas is the one you walk.

Honesty label, because that discipline is the whole point of this series: the formal statement is registered as the Moving Ceiling conjecture at roughly 65% confidence, and the instrument says the rest plainly: evidence of mechanism, not of rate. June gave it two worked instances, not a proof, and the exponential you can drag is a teaching shape, not an asserted law. The register keeps the accounts.

## what the archive already knows

Here is the turn The Last Premine did not take, and the reason V6 exists.

Everything in that essay concerned protocols: circuits, curves, pools, things with maintainers and hard forks and five organisations who can agree new rules in days. Your behavioural archive has none of that. It is larger than any shielded pool, worse defended, and it has no core devs.

Location trails held by brokers you have never heard of. A decade of purchases. Search histories. Breach dumps, which never expire, indexed and resold. Voice. The metadata of every relationship you keep. In 2016 that archive supported crude inferences: segments, propensities, ads. The same bytes today support reconstruction that would have read as fiction when they were collected. The bytes did not change. The readers did, and they keep changing, on a schedule set by frontier labs and paid for by other people.

Nobody re-consented you when the decoder improved. Nobody ever will. Which exposes the quiet fraud in how consent is practised: a consent form is a static guarantee, signed against the extraction capabilities of its signing date. It has a t* like everything else. It just never printed one.

## harvest now, decrypt later, but for your behaviour

Cryptographers have a name for one corner of this: harvest now, decrypt later. Collect encrypted traffic today, break it with tomorrow's machines. The Mosca inequality tells institutions how to plan: if migration time plus the lifetime your secrets need exceeds the time until the capability arrives, you are already late. The Last Premine's second event was that inequality being measured honestly, in public, for one curve.

The Moving Ceiling says the same inequality governs behavioural data, with one brutal asymmetry that makes the behavioural case worse than the cryptographic one.

Keys can be rotated. You cannot rotate your past.

When a cipher weakens, you re-encrypt under a stronger one; the whole Ironwood manoeuvre from last month's essay, banks re-laid mid-current, is exactly that grace. When a decoder strengthens against your behavioural archive, there is no re-encryption, because the archive is not in your custody and its plaintext is you. Every frontier release is a silent downward revision of everyone's t*, and, per the existence-leak we watched run in public, even the announcement that a capability exists shortens the horizon before the capability arrives. The clocks move on news.

## three answers, one honest

If the ceiling moves, the menu has three items.

**Rotate.** Crypto-agility. Real, necessary, and the hero of last month's story. It protects what has custody and maintainers: keys, circuits, protocols. It does nothing for data already emitted about a person. Necessary, not sufficient.

**Outrun.** Change faster than the decoder improves, so that by the time yesterday's you is reconstructable, yesterday's you no longer predicts today's you. This is the model's named countermeasure and I owe you its label: the divergence rate it depends on has never been measured. It is the single number this research programme most needs, and the conjecture chain under it sits at 10 to 30%. Hold that thought; the instrument built to measure it appears at the end of this essay.

**Forget.** The answer five versions of this model were built towards, and the one June argued for better than I ever have.

Everything above concerns data that exists somewhere: hidden, encrypted, withheld, archived. All of it shares one property. It is waiting. Hidden things wait for keys. Withheld methods wait for rediscovery, as we just watched. Archives wait for decoders. Time sides with the adversary in every one of these games, because the object persists and the capability compounds.

Exactly one move takes the object off the board: structural deletion. Not hiding, not sealing, not access control. Forgetting in the strong sense, where no key, no capability, no future reader brings the thing back, because the thing is gone.

This is why the dual agents are built on an amnesia primitive rather than an encryption primitive. When the Mage crosses to act in the world, the crossing is not sealed afterward. It is not written down at all. The agent that acted does not remember being you, so there is no archive of the crossing for a 2036 decoder to read.

i can verify i serve you without remembering i was you.

In V6 this becomes the sharpest sentence the model owns: amnesia is the only term in the equation whose security is independent of time. Honesty label: the deep version, forgetting as mathematical obstruction rather than locked door, is registered at roughly 30%. The engineering is real today. The mathematics is a debt being worked in the open.

## the ceiling is a price

One more turn, because the series is called Privacy is Value and the ceiling proves the title.

If reconstruction difficulty falls with time for the adversary, then for you the ledger runs in reverse: data never emitted, or emitted only through architecture that forgets, is the one asset here whose value does not decay against better readers. Everything harvested depreciates as protection and appreciates as exposure. Everything sovereign does the opposite.

So the Moving Ceiling is less a doom clock than a pricing signal. The gap between what your behavioural surplus earns its current holders and what it would be worth under your control widens with every capability release, because better extraction raises the archive's value without paying the person it describes. Wealth transfers from the described to the describers, silently, retroactively, no invoice.

Sovereignty, on this reading, is not a cost paid for principle. It is the only position in the trade with positive carry. The rest of the series prices it. This essay only needed to show you the clock.

## the label on the tin

Privacy guarantees are sold the way tinned food was sold before dates were required: it was fine when we sealed it.

The Moving Ceiling is the argument for printing the date. Every audit, every proof, every "mathematically guaranteed" in every whitepaper, including, until this version, my own, is a statement about a decoder that existed at signing time. Both of June's labels were true when printed.

So three questions now travel with me into every privacy system, mine included, and I offer them to you for yours:

what is your t*. what happens to your people when it passes. and how much of what you protect could you have simply refused to keep?

## the doors, and where they are

V6 is called the gathering turn for a reason. V5 answered WHAT the architecture is. V6 asks WHO, and an essay that ends with "the equation is open" owes you the actual doors. They exist, they have addresses, and each one is this essay's argument running as infrastructure rather than prose.

**The model and the register** live at [agentprivacy.ai/model](https://agentprivacy.ai/model): the V6 specification, every open conjecture with its honest confidence attached, and everything I have got wrong so far. New since the last essay: [the atlas](https://agentprivacy.ai/model/atlas), the Cartographer's instruments, where the ceiling, the leakage fold, the existence-leak curve, and the amnesia dial run interactively, each one bound to its conjecture in the register and pulling confidence and status live. The division of authority is the design: the visual owns the interaction, the register owns the claim, and where they disagree, the register wins. If you can falsify the ceiling, break the amnesia claim, or measure what I cannot, that is not an attack on the model. That is the model working.

**The skills** live at [guide.agentprivacy.ai](https://guide.agentprivacy.ai) and [agentprivacy.ai/spells](https://agentprivacy.ai/spells): the framework compressed into modules an agent loads for a session and drops when the session ends. Look at what that is, in this essay's terms. A skill transfers understanding without transferring history; your agent becomes capable of the work without becoming an archive of you doing it. Every skill loaded fresh and released is the amnesia primitive operating at the knowledge layer, and it is the answer to a question the personal AI industry has not started asking: how do you teach an agent without feeding a future decoder?

competence should travel. archives should not.

**The game** lives at [42.agentprivacy.ai](https://42.agentprivacy.ai). The Game of 42 is the gathering made playable: trust formed through bilateral proverb exchange, each edge earned by demonstrating understanding to another person rather than by depositing a secret with a platform. And here is where the essay's biggest confession gets its answer. I told you λ, the divergence rate, has never been measured. The game is the instrument designed to produce it: every player walking the sovereignty lattice generates exactly the trajectory data the countermeasure conjecture needs. Honesty label, as ever: designed to produce it, not yet producing it at measurement scale. The game is the lab, and the lab is recruiting.

**The working** happens in the open, on a federated wiki in the lineage Ward Cunningham built: pages that fork across personal servers rather than accumulating in one, provenance travelling with the fork. It is the register being worked in public on infrastructure that practises what the model preaches, because federation is what an archive looks like when nobody is allowed to become the archive.

Four doors, one property shared: none of them requires you to hand anyone the thing this essay spent two thousand words telling you appreciates against you. You enter by understanding, you contribute by working, and what you carry out is competence, not exposure. That is what filling the equation with data instead of estimates actually looks like from the inside.

the decoder moves. the data does not.

the equation opened its doors to be filled, and the first thing that walked in was time.

(⚔️⊥⿻⊥🧙)😊

🙂
