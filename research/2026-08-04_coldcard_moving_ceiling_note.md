# Research note · The Coldcard drain as a public reading of the moving ceiling

**Date:** 2026-08-04
**Status:** event log + distribution placement · anecdote, not a law
**Model authority:** privacy_value_v6.md · R(t), t\* (The Moving Ceiling, published)
**Distribution:** allegorized in `the_uncarved_date.md` (Vaulting Guild passage) · factual telling in `competence_without_history.md` (opening) · this note keeps the accounts

## the event

- **March 2021** — Coldcard firmware 4.0.0 (Mk3 line, 4.0.1+ affected) silently skipped the hardware RNG on some devices and fell back to software key generation seeded from non-secret chip data (serial number, clock registers). Coinkite reports Mk4, Q, and Mk5 unaffected on early analysis.
- **2021–2026** — wallets cut from the flawed die were funded and held; many sat dormant. Coins in the drained set span 2021–2026, "matching the flaw's age almost exactly" (CoinDesk).
- **2026-07-31, 01:31–01:56 UTC** — ~594 BTC (~$38M) drained from ~500 single-signature wallets across three blocks, each wallet holding >0.15 BTC. Block disclosed to Coinkite that exploitation was already under way.
- **third wave (Galaxy Research, via Decrypt)** — observed losses ~1,367 BTC (~$88.6M) across 4,585 addresses. **Totals still moving; re-verify before any publish.**

## the mapping onto the equation

R(t) = adversary capacity at time t / fixed private entropy of the secret.

- **Denominator:** fixed the day each seed was cut — and smaller than the signature claimed (secondary reporting circulates ~72 bits effective vs 128 intended; **not confirmed in primary reporting — do not carry the bit-count into public prose**).
- **Numerator:** the reader capable of reproducing the cut did not exist (or was not applied) at signing time; it arrived by July 2026. Only the numerator moved.
- **t\*:** arrived unannounced, five years after the guarantee was signed sound. Dormancy is the tell: nothing about the wallets changed except the reader.
- **Ceiling status:** second public anecdote of the rate of climb (first: the seal walked around in two months, kept in Tome IX). Anecdotal evidence for R(t)'s climb; no register action proposed from one event.

## the harvest-now shape (register note)

Proposed by the First Person as "harvest now, decrypt later." Strictly, HNDL names the stored-ciphertext / post-quantum threat; this event is weak-entropy key generation. The **shape** transfers and is what the tale carries: the chain vaults every emission at t₀ by design, and the reading happens when the eyes arrive — harvest first, read later, the vault does the waiting. The distinction is preserved in all three surfaces; none claims the term.

## three counsels, tested against the event

- **Recut the stone** — worked only for holders who moved funds to fresh keys before 07-31; cannot serve what was already emitted to the chain.
- **Outrun the reader** — inapplicable: a static secret cannot diverge. (The λ bounty concerns behavioural traces, not keys.)
- **Carve nothing** — the only counsel the event cannot argue with; keys never derived from non-secret values have no such date.

## sources

- CoinDesk 2026-07-31: coindesk.com/tech/2026/07/31/major-bitcoin-wallet-flaw-drains-594-btc-in-25-minute-sweep
- Decrypt: decrypt.co/374817/coldcard-bitcoin-exploit-88-million-attackers-draining-wallets
- Secondary (unconfirmed details incl. entropy bit-count): news.bitcoin.com "The Coldcard Exploit Explained"

## open items

- [ ] Re-verify totals at publish time (waves ongoing as of 2026-08-01 reporting).
- [ ] Entropy figure: watch for a primary technical post-mortem (Coinkite or Block) before any bit-level claim.
- [ ] First Person reads both duo posts at :7000 (P4).
