---
title: "Competence Without History"
subtitle: "the gathering turn has doors: the atlas, the skills, the game, the wiki · a Privacy is Value essay"
series: "Privacy is Value"
version: "draft v3 for sync.soulbis.com · post 3 of the gathering arc · A7 voice and overlap pass 2026-07-02"
date: "2026-07"
author: "privacymage"
license: "CC BY-SA 4.0"
model_authority: "privacy_value_v6.md · CONJECTURE_REGISTER_V6.md (head C96)"
tier: P
---

# Competence Without History

Two essays ago I showed you a clock: every static privacy guarantee has a shelf life, and yours is being revised downward by other people's release schedules. One essay ago the City gave its counsel, and the counsel had three lines, of which only the third owes nothing to time.

This essay is the practical one. It answers the question the clock leaves ringing: fine, the decoder moves and the data does not, so where exactly do I stand?

Here is the verdict up front. The model has doors now, four of them, all live, and they share one property that took me five versions of an equation to be able to say in a sentence:

you enter by understanding, and you leave with competence, not exposure.

That property is not a slogan. It is a design constraint enforced at every door, and this essay is the tour that shows you the enforcement.

## the first door: the atlas

The Privacy Value Model has lived, until now, as documents: a formal specification, a register of open conjectures, essays like this one. As of this summer the model also runs, at [agentprivacy.ai/model/atlas](https://agentprivacy.ai/model/atlas), as the Cartographer's instruments.

Each instrument is one claim from the register, made draggable. The moving ceiling from the last essay is there; that essay already put your hands on it, so this tour moves past. The existence-leak curve is there, the shape of [The Last Premine](https://sync.soulbis.com/p/privacy-is-value-the-last-premine)'s second story, a withheld result priced by its own proof of existence. The temporal decay curves. The amnesia dial. The three-axis gate, where you can collapse any one axis and watch the whole product go to zero, which teaches multiplicative gating faster than any paragraph I have written about it.

And one instrument getting its first public airing here: the leakage fold. In 2025 and 2026 the multi-agent privacy field measured something that looks, at first glance, like an attack on this model: when AI agents pass outputs to one another, leakage compounds, up to (2^N − 1)ε for a chain of N agents, and the big measurement study found multi-agent systems leaking through the unmonitored channels between agents more than anywhere else. Read carefully, that is this model's thesis in the adversary's units. Policy separation asks the inter-agent channel to behave, and compounds exponentially. Amnesia separation deletes the channel, and the conjecture on the register says it caps linearly: at five agents, the difference between 31ε and 5ε. The fold instrument lets you drag the per-hop leakage and watch the two curves peel apart across N. Honesty label, always: the exponential side is proven as a bound and evidenced empirically in the literature; the linear side is registered at roughly 55% and is an engineering claim awaiting a deployed measurement. The benchmark to test it is in this research programme's work plan, pre-registered, and the result will be filed whichever way it falls.

Now the design decision that makes the atlas worth an essay section rather than a link. Every instrument displays its conjecture's confidence and status pulled live from the register, never painted into the picture. The visual owns the interaction. The register owns the claim. Where they disagree, the register wins. I think of this as the beginning of a genre: honest interactive publishing, where the picture is allowed to be persuasive because it is not allowed to be the authority.

## the second door: the skills

At [guide.agentprivacy.ai](https://guide.agentprivacy.ai) and [agentprivacy.ai/spells](https://agentprivacy.ai/spells) the model exists in a third form, and for the personal AI future this may be the most important one: as skills, compressed modules of the framework that an agent loads for a session and drops when the session ends.

Sit with what that is. The clock essay's whole problem, in one clause, is data that persists, waiting for better readers. The whole promise of personal AI is an agent that knows your frameworks, your context, your ways of working. The industry's default answer is to resolve that tension by ignoring it: feed the agent everything, let it remember, and hope the archive it becomes is never read by anything stronger than today's decoders. The last essay told you exactly how that ends.

A skill is the other answer. It transfers understanding without transferring history. An agent loads the sovereignty-lattice skill, or the amnesia-protocol skill, or the promise-theory skill, does the work of the session competently, and releases it, carrying nothing forward. The knowledge was compressed by a person who understood it, travels as compression, and decompresses into competence at the point of use. Nothing about you accumulates in the middle. This is the amnesia primitive operating at the knowledge layer, and it answers a question the industry has not started asking: how do you teach an agent without feeding a future decoder?

competence should travel. archives should not.

There is a deeper layer here for the identity-minded, and it points at where this research programme goes next. How do you know a skill was actually understood, by an agent or a person, rather than merely stored? You ask for it back compressed differently: a proverb, formed fresh, that could only come from comprehension. Compression as proof of understanding is the Relationship Proverb Protocol, the model's oldest invention, and the skills are quietly its distribution network. Every spell on the spells page is an exercise in exactly this: meaning compressed by one mind, decompressed by another, the match proving the transfer. That primitive is heading for formal adversarial testing (can a frontier model fake a passing proverb without the source? what is the replay surface?), because an invention you will not attack is a belief, not a protocol.

## the third door: the game

The gathering turn is called that because V6 opens the model outward: V5 answered WHAT the architecture is, V6 asks WHO. At [42.agentprivacy.ai](https://42.agentprivacy.ai) the WHO becomes playable.

The Game of 42 fills forty-two positions of governance, six home bases of seven, not by application, election, or purchase, but by ceremony: bilateral proverb exchange, each trust edge earned by demonstrating understanding to another person and receiving their demonstration in return. No stored secret anywhere in the loop. Your standing in the game is the graph of who has proven comprehension with you, which is a sentence I invite you to compare with how standing works on every platform you currently use.

And the game is more than the invitation. The last essay made a confession: the countermeasure it called outrun rests on a divergence rate, λ, that has never been measured. The game is the instrument built to produce it. Every player walking the sovereignty lattice, ceremony by ceremony, generates a real trajectory: exactly the data from which a divergence rate gets its first estimate. Honesty label: designed as the instrument, not yet producing at measurement scale. The lab is built. The lab is recruiting. That is not a metaphor; it is a sample-size problem, and you are the sample.

## the fourth door: the wiki

The working of all this happens in the open, on a federated wiki in the lineage Ward Cunningham built, seeded at [guide.agentprivacy.ai](https://guide.agentprivacy.ai). Federated wiki has one property that makes it the only publishing infrastructure this model could honestly use: pages fork across personal servers rather than accumulating on one, and the provenance travels with the fork. Nobody hosts the conversation; everybody hosts their copy of it, changed as they see fit, attributed as they found it.

That is what an archive looks like when nobody is allowed to become the archive. The register gets worked there in public, conjecture by conjecture, and when your fork of a page diverges from mine, that divergence is not a synchronisation failure. It is the plurality the model is named for, running on disk.

## one lock, four doors

Now the property I promised, and why it is a design constraint rather than a vibe.

Every one of these doors is opened the same way. The atlas asks you to engage a claim before it will show you its confidence moving. The skills ask an agent to decompress understanding at the point of use. The game admits you by proverb, never by payment or credential. The wiki admits you by fork, which is to say by doing the work on your own ground. In every case the key is demonstrated understanding, and in no case does entering require depositing the thing the first essay told you appreciates against you.

Understanding as key, the whole way down. It is the only key that cannot be phished from a database, because it is not in one; the only key that improves the holder by being used; and, per everything the clock essay argued, one of the few assets in this landscape whose value survives the arrival of better decoders, because a decoder reading your traces still has not done the understanding.

Honesty ledger for the whole tour, in one place: the atlas is live and register-bound (operational). The skills are live; the claim that skill-based transfer strictly dominates archive-based personalisation for privacy is architectural, argued, not yet benchmarked, and carries no register number yet. The game is live; its measurement function is anticipated, sample-limited, and the number it exists to produce is still owed. The wiki is live and is infrastructure, not a claim. The register keeps all accounts at [agentprivacy.ai/model](https://agentprivacy.ai/model).

The clock told you what time does to everything you leave behind. The counsel told you the only counsel time cannot argue with. This essay's addition is smaller and more usable: there are places now where participating costs you understanding instead of exposure, and they have addresses.

you enter by understanding. you leave with more than you brought. and less of you stays behind.

(⚔️⊥⿻⊥🧙)😊

🙂
