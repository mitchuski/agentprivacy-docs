---
theme: privacy is value
arc position: V6 arc, essay 1 of 3 (follows *The Last Premine*)
status: pre-release, one human gate open
register: narrative / public essay
word count: ~2,350
reading time: 10 minutes
pipeline: markdown → WeasyPrint → sync.soulbis.com
---

# The Moving Ceiling

*every guarantee is a statement about the reader who existed when it was signed.*

The week I finished this essay, Anthropic published *Discovering cryptographic weaknesses with Claude*: one of its models had found flaws in two cryptographic designs that years of expert review had missed, and warned, in the same breath, that its own researchers might drown in checking what the machine now reports.

I have spent five versions of an equation arguing one thing. The threat to everything you have ever hidden is not that your secrets change, but that the readers keep getting better. Signing information is a door to opening trust, and once you know there is a lock and a key, mathematics decides when it may be picked. That week the largest maker of readers on earth printed the receipt.

This essay is the clock.

Last month, in *The Last Premine*, I read two events through one lens: a four-year-old flaw in a shielded pool found in a day, and an open benchmark counting down a quantum horizon. That essay ended with a call, for the V6 form of the equation to come into the light.

This is the first answer, and it starts by finishing that essay's last sentence.

*The Last Premine* closed on a new norm: the release of a frontier model is now a security event for every cryptographic protocol on earth. True, and incomplete. Here is the completion, and the verdict of this essay up front.

**it is also a privacy event for every archive on earth. including yours.**

## two clocks, briefly

*the object sat still. the reader moved.*

For anyone arriving fresh, the instances in one breath each. The full telling, with the people and the graph that made the difference, is in the branch.

An Orchard circuit flaw slept for four years under expert eyes, then was found within a day of a sharper model reaching the one auditor equipped to point it. The circuit never changed. The reader did.

A withheld quantum result, published only as a proof that it exists, was independently reconstructed in about two months. The existence claim itself priced the search. Method perfectly hidden, timeline compressed anyway.

Two protected objects sat still. Two capabilities moved. That is all this essay needs from them, because the same shape governs something much closer to you than a circuit or a curve.

## the ceiling, written down

*the bottom is fixed by you. the top is not.*

V6 gives the shape a formula, and it is short enough to carry.

Reconstruction, the question of whether an adversary can rebuild your private state from what you have emitted, is a ratio. On the bottom: the entropy of what you are protecting, fixed by you, because you emitted what you emitted. On top: the effective extraction capacity of the strongest decoder alive at time *t*, armed with everything else it has read about the world.

The bottom never moves. The top only climbs, and here is the part that matters. It climbs even when your archive gains nothing, because what grows is the reader's background. Every corpus that links to yours, every breach dump, every genealogy upload, every side record, shrinks what is still uncertain about you given the rest. The theory paper behind this essay now proves that form: your disclosed record never says more than it said, and the protection still expires, because it matters less against a reader who already knows the neighbourhood.

> R(t) = adversary capacity at time t / your fixed private entropy

While R(t) stays below one, reconstruction fails and the ceiling holds. But the ceiling is not a ceiling. It is a ceiling with a rate of climb, and so every guarantee written against it inherits an expiry, a shelf life.

> t\* = the last moment at which the ceiling still holds

This is the one place in the essay where you do not have to take the prose's word for the shape. The ceiling has an instrument now, on the atlas, the model's new visual runtime. Drag the frontier growth rate and watch t\* slide toward you. The page is an open path you read. The atlas is the one you walk.

The formal statement is registered as the Moving Ceiling conjecture at roughly 65% confidence, and the instrument says the rest plainly: evidence of mechanism, not of rate. June gave it two worked instances, not a proof, and the exponential you can drag is a teaching shape, not an asserted law.

As I write this, July has added a third, and this one the frontier lab published about itself. A model finding an improved key-recovery attack on a post-quantum signature scheme, and a faster attack on a reduced-round cipher. Neither of any practical impact on deployed systems today, by the lab's own statement. Both invisible to years of expert review.

One year, that disclosure notes, from models that could not read the simplest cipher to models finding what the experts missed.

Read that sentence as exactly what it is. The clearest public anecdote yet for the ceiling's rate of climb, and still an anecdote, not a law. The register keeps the accounts.

## what the archive already knows

*it is larger than any shielded pool, and it has no core devs.*

Here is the turn *The Last Premine* did not take, and the reason V6 exists.

Everything in that essay concerned protocols: circuits, curves, pools, things with maintainers and hard forks and five organisations who can agree new rules in days.

Your behavioural archive has none of that.

Location trails held by brokers you have never heard of. A decade of purchases. Search histories. Breach dumps, which never expire, indexed and resold. Voice. The metadata of every relationship you keep.

In 2016 that archive supported crude inferences: segments, propensities, ads. The same bytes today support reconstruction that would have read as fiction when they were collected. The bytes did not change. The readers did, and so did everything else the readers had read. Each new corpus that links to yours sharpens what your old bytes give up.

And they keep changing, on a schedule set by frontier labs and paid for by other people.

Nobody re-consented you when the decoder improved. Nobody ever will. Which exposes the quiet fraud in how consent is practised. A consent form is a static guarantee, signed against the extraction capabilities of its signing date.

It has a t\* like everything else. It just never printed one.

## harvest now, decrypt later, but for your behaviour

*keys can be rotated. you cannot rotate your past.*

Cryptographers have a name for one corner of this: harvest now, decrypt later. Collect encrypted traffic today, break it with tomorrow's machines. The Mosca inequality tells institutions how to plan. If migration time plus the lifetime your secrets need exceeds the time until the capability arrives, you are already late. *The Last Premine*'s second event was that inequality being measured honestly, in public, for one curve.

The Moving Ceiling says the same inequality governs behavioural data, with one brutal asymmetry that makes the behavioural case worse than the cryptographic one.

When a cipher weakens, you re-encrypt under a stronger one. Ironwood, a bank being re-laid mid-current, as last month's essay put it, is exactly that grace, and this week it stopped being a plan. The [work is public now](https://github.com/zcash/ironwood), in Lean, and the target is precise: soundness of the Action circuit shared by the Orchard and Ironwood pools, machine-checked before the upgrade that activates the new pool. The circuit whose four-year-old flaw opened this essay is the circuit now being proved.

When a decoder strengthens against your behavioural archive, there is no re-encryption, because the archive is not in your custody and its plaintext is you.

Every frontier release is a silent downward revision of everyone's t\*. And, per the existence leak we watched run in public, even the announcement that a capability exists shortens the horizon before the capability arrives. The clocks move on news.

## three answers, one honest

*exactly one move takes the object off the board.*

If the ceiling moves, the menu has three items.

**Rotate.** Crypto-agility. Real, necessary, and the hero of last month's story. It protects what has custody and maintainers: keys, circuits, protocols. It does nothing for data already emitted about a person. Necessary, not sufficient.

**Outrun.** Change faster than the decoder improves, so that by the time yesterday's you is reconstructable, yesterday's you no longer predicts today's you. This is the model's named countermeasure, and I owe you its label: the divergence rate it depends on has never been measured. It is the single number this research programme most needs, and the conjecture chain under it sits at 10 to 30%. Hold that thought. The instrument built to measure it appears at the end of this essay.

**Forget.** The answer five versions of this model were built towards, and the one June argued for better than I ever have.

Everything above concerns data that exists somewhere: hidden, encrypted, withheld, archived. All of it shares one property. It is waiting. Hidden things wait for keys. Withheld methods wait for rediscovery, as we just watched. Archives wait for readers with richer backgrounds. Time sides with the adversary in every one of these games, because the object persists while the reader's advantage accumulates.

Exactly one move takes the object off the board: structural deletion. Not hiding, not sealing, not access control. Forgetting in the strong sense, where no key, no capability, no future reader brings the thing back, because the thing is gone.

This is why the dual agents are built on an amnesia primitive rather than an encryption primitive. When the Mage crosses to act in the world, the crossing is not sealed afterward. It is not written down at all. The agent that acted does not remember being you, so there is no archive of the crossing for a 2036 decoder to read.

> i can verify i serve you without remembering i was you.

In V6 this becomes the sharpest sentence the model owns. Amnesia is the only term in the equation whose security is independent of time. The deep version, forgetting as mathematical obstruction rather than locked door, is registered at roughly 30%. The mathematics is a debt being worked in the open.

## the ceiling is a price

*everything harvested depreciates as protection and appreciates as exposure.*

One more turn, because the series is called Privacy is Value and the ceiling proves the title.

If reconstruction difficulty falls with time for the adversary, then for you the ledger runs in reverse. Data never emitted, or emitted only through architecture that forgets, is the one asset here whose value does not decay against better readers. Everything harvested depreciates as protection and appreciates as exposure. Everything sovereign does the opposite.

So the Moving Ceiling is less a doom clock than a pricing signal. The gap between what your behavioural surplus earns its current holders and what it would be worth under your control widens with every capability release, because better extraction raises the archive's value without paying the person it describes.

Wealth transfers from the described to the describers. Silently, retroactively, no invoice.

Sovereignty, on this reading, is not a cost paid for principle. It is the only position in the trade with positive carry. The rest of the series prices it. This essay only needed to show you the clock.

## the label on the tin

*it was fine when we sealed it.*

Privacy guarantees are sold the way tinned food was sold before dates were required.

The Moving Ceiling is the argument for printing the date. Every audit, every proof, every "mathematically guaranteed" in every whitepaper, including, until this version, my own, is a statement about a decoder that existed at signing time. Both of June's labels were true when printed.

Someone has started printing it. The Ironwood verification effort states, as an explicit part of the work rather than an afterthought, that it will document the scope of what is and is not formally verified. That sentence is the label. It is the discipline this essay is asking for, arriving in public the same week, from the pool the essay's first instance was found in.

And it is the strongest objection to everything above, so let me put it at its full strength rather than at mine. A machine-checked soundness proof is the one guarantee whose value does not decay against better readers. Within its stated model it holds against every adversary, including ones that do not exist yet, because it is not an argument about difficulty. The ceiling does not move on a theorem.

What moves is the boundary of the model. The t\* migrates to the gap between what was proved and what was deployed: the assumptions, the compiler, the hardware, the parts of the system the proof did not reach. Which is exactly why the scope note matters more than the proof does. A verification without a stated boundary is a tin with no date on it, and a more convincing one for being true.

So three questions now travel with me into every privacy system, mine included, and I offer them to you for yours.

What is your t\*. What happens to your people when it passes. And how much of what you protect could you have simply refused to keep?

## the doors

*competence an agent can carry without becoming an archive of you.*

An essay that ends with "the equation is open" owes you actual doors, and they exist.

The model and its register live at [agentprivacy.ai/model](https://agentprivacy.ai/model), with the Cartographer's instruments at the atlas, where the ceiling you just read about runs interactively.

The framework travels as loadable skills at [guide.agentprivacy.ai](https://guide.agentprivacy.ai) and [agentprivacy.ai/spells](https://agentprivacy.ai/spells).

The gathering is playable at [42.agentprivacy.ai](https://42.agentprivacy.ai), and, keeping the promise from the outrun section, the Game of 42 is the instrument built to produce λ, the number this essay admitted is missing.

The lab is built and recruiting. The working happens in the open, on a federated wiki, on infrastructure with no single archive.

Each of those doors deserves more than a sentence, and gets it. The full tour, including one instrument this essay deliberately held back, is the next essay in this arc.

If you can measure a divergence rate, falsify the ceiling, or break the amnesia claim, that is not an attack on the model. That is the model working.

## coda: the model, working

*one seat builds. one seat is rewarded only for breaking the build.*

That invitation was already accepted, from inside.

This essay's argument is that the reader moves, not the archive. So the programme grew moving readers of its own and aimed them at its own papers first. Role-bound sessions, one seat drafting, one attacking, one repairing, one auditing, each booted fresh with no memory of the last, fenced by rules none of them can edit, with the written record as the only thread between them.

This week that runtime carried one paper up the whole ladder. A sceptical reviewer found a proposition false as stated and built the counterexample to prove it. The same-day repair adopted the reviewer's own construction into the paper as one of its results. Along the way the harness caught some of its own earlier runs passing vacuously and corrected its evidence trail on the record. A theorem-shaped result survived all of it. One agent building, one trying to break the build: that is now the standard path for what V6 ships.

The shape has a sibling I will only point at here. The exam drawn by hashing the work itself, so neither seat can rig it. Pointed not at our own papers but at live cryptographic circuits, read blind, from compiled artefacts alone, no source. Real structure found in real cryptography, and, the part this series exists to earn, a discipline strict enough that you can trust the finding without reading every line yourself, because the workers were never able to collude and the record proves it.

I am aware of what that paragraph does. This essay's second instance is an existence claim pricing a search, and I have just made one. Deliberately, with the timeline that costs me. The result stays out of this essay until it has been independently reproduced, and the pointer is all you get until then. Watch the register, not the prose.

I wrote that in the same week a frontier lab published its own model doing this kind of work. At a measured price, with its own no-impact caveat, and with a warning worth keeping: that its researchers may drown in checking what the machine reports.

That warning is the whole game. The frontier showed the reader can find the weakness. The end of this arc is the harder claim: the architecture that lets a person stake their name on a machine's cryptographic finding without having personally re-derived it.

And the ladder stops one rung short of publication, by design. The runtime cannot do the first-person read, where the person whose name is on the work reads it all the way down and accepts what it claims. Everything in this story accumulates against you. The one thing that compounds for you is the record of who answers for the claim. Reputation is the only stock in the model that grows by being tended.

Then a venue built for scrutiny. Then prose built for reading.

*the readers multiply.*
*the signature does not.*
*the decoder moves.*
*the data does not.*

*the equation opened its doors to be filled, and the first thing that walked in was time.*

(⚔️⊥⿻⊥🧙)😊 🙂

—privacymage
