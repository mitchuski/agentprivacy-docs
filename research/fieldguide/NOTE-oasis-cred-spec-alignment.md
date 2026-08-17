# Note — where OASIS could align with the updated DTG Credentials Core Spec

**For:** Max, and whoever owns `TrustGraphController` on the ONODE side
**From:** Mitch — same team, wearing the ToIP DTG ZKP co-chair hat
**Date:** 2026-08-15
**Status:** observations, not asks. Nothing here blocks the two-avatar desk demo.

Working from *Decentralized Trust Graph Credentials — Core Specification*, **Version 1.0,
Working Draft** (ToIP DTGWG; editors Leon, Miller, Turk, Kolpondinos, Reed), read from the
copy vendored in my lab at `dtgwg-cred-spec-main/`. I have **not** diffed that copy against
the live published version — check <https://trustoverip.github.io/dtgwg-cred-spec/> before
acting on any clause below.

The short version: **we have already built several things the spec names.** In most cases
the alignment is a rename plus a field, not a rewrite. Where I flag a real change, I say what
it buys.

---

## 0. The most useful reframe: you are doing pairwise, and that is fine

I previously told you (counter-spec §7) that because OASIS avatars are not personhood-anchored,
the Field Guide graph is "a pseudonym graph, not a personhood graph." That is true, but I framed
it as a shortfall and the spec does not.

> "Community membership is **not** a precondition for issuing, holding, or presenting a VRC; two
> entities that do not share (or do not hold) a VMC can still exchange VRCs, and the resulting
> edges are valid trust attestations standing on their cryptographic signatures and on whatever
> real-world context the parties bring to them." — §Community-Anchored Zero-Knowledge Proof

The spec defines **two** constructions. ONODE is squarely in the first:

| | Pairwise (VRC-based) | Community-anchored (VMC-based) |
|---|---|---|
| Needs a VTC? | **No** | Yes — both parties hold VMCs from the same C-DID |
| What ONODE has | this one | not this one |
| Carries personhood? | no, and the spec says so plainly | yes, when the VMCs qualify as PHCs |

So the correct statement is not "OASIS falls short of the trust graph." It is **"OASIS implements
the pairwise construction and does not claim community-level assurance."** The spec is explicit
that pairwise "does not by itself confer any community-level assurance (e.g., personhood)."

This also corrects something on my side: my lab's `runtime 07` gates every edge on personhood
anchoring, which models only the *community-anchored* construction. Your deployment is what showed
me that. I have filed it as a refinement upstream.

**If OASIS ever does want personhood**, the path is named: a VTC whose governance requires members
to be real humans with exactly one membership, issuing VMCs that qualify as PHCs. That is a
governance undertaking, not a code change, and nothing below depends on it.

---

## 1. `peerAvatarId` → an R-DID *(the one I would fix first)*

**Spec:** "**IMPORTANT**: The valid application of this specification requires that each entity
MUST generate a new, unique R-DID for every single entity they connect with, even within the same
community." (§Unilateral Relationship Identification) — and Privacy Considerations 2: "Reusing an
R-DID across counterparties creates unintended correlation."

**Today:** `GET /poi/nearby` returns `peerAvatarId` — one stable guid — to every peer.

**Change:** mint an R-DID per counterparty at edge formation and return that. The avatar guid stops
crossing the wire.

**What it buys:** two people who have both met the same player currently receive the same handle for
them and can join their views. This is the single change that closes that.

**Bonus, and it is a real one:** the spec says a relationship is canonically identified by *two*
independent identifiers — Source R-DID and Target R-DID — and that "semantic statements, metadata,
or private context regarding the relationship MAY be anchored solely to the controller's own R-DID,
without requiring the resolution or inclusion of the counterparty's identifier." That is a
spec-blessed home for per-edge state you already want.

## 2. `peerDisplayName` → a VPC asserting a P-DID

**Spec:** Privacy Considerations 3 — "Correlation across relationships should occur only through the
holder's deliberate assertion of a persona (via a VPC) or an M-DID — **never as a side effect of
credential structure**." A VPC "enables one party to a DTG edge relationship to assert a persona to
the counterparty… Persona DIDs enable individuals to control intentional correlation separately from
their M-DIDs."

**Today:** a global profile display name ships on every overlay pin — correlation as a side effect of
structure, which is the exact thing that clause forbids.

**Change:** the name a peer sees is asserted *per edge*, as a Persona Credential (`type` includes
`"PersonaCredential"`) identified by a P-DID.

**Note for me as much as you:** I proposed exactly this in the counter-spec §0.2 and called it
`presentAs`, having not yet read this part of the spec. It already has a name and a credential type.
Use theirs.

## 3. `TrustLinkHolon` → two directional VRCs

**Spec:** "DTG edge credentials are issued **in pairs, one in each direction**, to form a DTG edge
connecting two DTG nodes." A VRC "represents one half of a bidirectional peer-to-peer trust
relationship."

**Today:** one symmetric row per pair (and one symmetric object in my model too).

**Change:** two credentials, one per direction, each anchored to its issuer's own R-DID.

**What it buys:** asymmetric disclosure becomes natural rather than bolted on. I show you one face
and grant you one audience; you show me another. On a single symmetric row those two facts fight for
the same fields.

## 4. Co-location → a VWC, not a gate baked into the edge

This is the one I would most want you to look at, because it improves the design rather than just
renaming it.

**Spec:** a VWC (`"WitnessCredential"`) is an annotation credential that "enables one party to a DTG
edge trust relationship to issue a verifiable assertion about the authenticity of another DTG edge…
For example: both parties provided: a) proof to the VTA that they were at the same event at the same
time, and/or b) proof of biometric liveness at the time of relationship formation."

**Today / in my counter-spec:** proximity is a gate inside the meet — the edge refuses to form unless
the two devices are within 50 m.

**Change:** let the edge form on consent, and mint a **VWC** carrying the co-location assertion as an
annotation on it.

**What it buys:** it fixes the honest weakness I flagged in counter-spec §7. Co-location is asserted
by a phone's own GPS, so two colluding players can mint an edge from anywhere. Baked into the edge,
that weakness silently contaminates the edge's meaning. As an annotation it is **separable**: the
edge claims consent, the VWC claims proximity with its own provenance and its own assurance, and a
verifier can weigh them independently or ignore the VWC entirely. Better liveness evidence later
(the second half of that spec example) upgrades the annotation without touching a single edge.

## 5. Give the meet a `taskContext` / `threadId`

**Spec:** "a VWC MUST be bound to the trust task exchange in which it was issued via the `taskContext`
property." And the outcome-interpretability rule: "A verifier MUST NOT interpret a
`taskContext`-bearing credential as proof that the associated trust task or ceremony completed unless
the matching trust task outcome evidence is also present and verified. That outcome evidence MUST be
reachable by the verifier."

**Today:** the meet exchange has a nonce and an offer tag, which is nearly a `threadId` already.

**Change:** name it a `threadId`, carry it on the exchange, and make the outcome evidence reachable —
either travelling with the presentation or locatable from the `threadId`.

**What it buys:** protection against what the spec calls **context collapse** — a credential presented
outside the exchange it was issued in, read as evidence a ceremony completed. For you concretely: a
witness assertion from one meet must not be presentable as if it belonged to another.

## 6. `POST /witness` → a **relationship invitation** (OOBI), and mind the name collision

**Spec:** a *relationship invitation* is "a process by which two or more entities exchange DTG
verifiable identifiers (VIDs) in order to form a cryptographically verifiable connection, such as by
scanning a **QR code (in person or remotely)** or clicking a deep link… Also known as an out-of-band
introduction (OOBI)."

That is the meet rite, described by the spec, including the QR.

**Careful:** a *DTG invitation credential* (VIC) is a **different thing** — it is issued by a VTN,
VTC, or VTC member to invite a **new member** and automate onboarding. Do not name the peer-to-peer
meet an invitation credential; you would be claiming membership semantics you do not have.

**Change:** describe `/witness` as a relationship invitation / OOBI in the API docs. Cheap, and it
stops the next reader assuming VIC.

## 7. `GET /card/{tokenSlug}` → this is an **r-card**

**Spec:** an r-card (relationship card) is "a VDS containing a combination of human-readable and
machine-readable data describing the publisher. R-cards are **typically exchanged in conjunction with
VRCs**… One use of r-cards is to serve as a modern, self-updating version of a vCard. **The open
standard specification for r-cards will be a deliverable of the DTGWG.**"

You have already built this and called it a share card. Two consequences:

1. Your Phase B "share the Mage card after a Witness" flow is **exactly** the spec's "r-cards are
   typically exchanged in conjunction with VRCs." You independently landed on the spec's own pattern.
2. Because the r-card spec is a *forthcoming DTGWG deliverable*, this is the cheapest possible moment
   to align field names. I can flag the draft to you when it moves. Diverging now costs a migration
   later; matching now costs nothing.

## 8. Credentials as W3C VC Data Model v2.0

**Spec:** "All DTG implementations MUST support v2.0 credential verification and SHOULD support v2.0
credential issuance." Base structure: `@context` MUST include `https://www.w3.org/ns/credentials/v2`
and `https://firstperson.network/credentials/dtg/v1`; `type` MUST include `"VerifiableCredential"`,
`"DTGCredential"`, and exactly one concrete subtype (`RelationshipCredential`, `MembershipCredential`,
`InvitationCredential`, `PersonaCredential`, `EndorsementCredential`, `WitnessCredential`).

**Today:** ONODE holons are holons, not VCs.

**Change:** anything that crosses a trust boundary — the edge credentials, the witness annotation —
gets issued as a v2.0 VC with those context and type arrays. Internal Knowledge holons
(`PoiDiscovery`) do not need this; they are your storage, not an interop surface.

## 9. Expiry and revocation — the gap I already owed you

**Spec:** verifiers "must reject credentials outside their `validFrom`/`validUntil` window… and should
check applicable revocation status via the governing trust registry."

**Today:** neither my model nor ONODE has an expiry or a revocation path on a link. A meet from four
years ago weighs what a meet from Tuesday weighs, and there is no unfriend.

**Change:** `validFrom` / `validUntil` on the edge credentials, and a revocation status source. This
is the same gap I flagged as erosion, now with a spec-shaped place to put it.

## 10. Direction of travel, not today's work

- **ZKP by default.** "Implementations SHOULD make ZKP presentation the default behavior so that users
  obtain privacy preservation without having to opt in." Your card and overlay responses are plain
  JSON today. Nobody expects otherwise at this stage — but the spec's default is the opposite of the
  usual one, and it is worth knowing now rather than at v2.
- **M-DID reuse is explicitly a bootstrap state.** "Reuse of an M-DID across multiple relationships is
  allowed for bootstrapping… Migration from M-DID-based to R-DID-based edges is **recommended**
  post-bootstrapping." A stable `avatarId` on every edge is precisely that bootstrap state — which
  means item 1 is not me inventing a rule, it is the spec's own recommended migration.
- **You are a cloud VTA.** The spec expects a person's credentials and keys to live in a personal
  network vault "under the exclusive control of that person," who "may sometimes choose to delegate
  use of their credentials or keys to a VTA." OASIS holding everything server-side is the delegated
  cloud-VTA pattern, which is permitted — but it is worth stating explicitly somewhere, because right
  now it is implicit and a reader could assume the stronger property.
- **DTG node types include AI agents.** Not a change; just worth knowing that the spec already
  anticipates agent nodes, which is where the agentprivacy side of my work meets yours.

---

## What I would actually do, in order

1. **R-DID instead of `peerAvatarId`** (§1) — closes a real correlation hole, small change.
2. **VWC for co-location** (§4) — improves the design, not just the vocabulary.
3. **VPC for the peer-visible name** (§2) — completes §1; without it the name re-joins what the R-DID split.
4. **`threadId` on the meet** (§5) — cheap now, awkward to retrofit.
5. Everything else as and when.

Items 1–3 are one coherent change, not three: they are the same privacy property approached from the
identifier, the assurance, and the label.

**Where the evidence is:** `runtimes/meet-overlay/` (54 properties), `runtimes/lab-bridge/` (10,
importing the task force lab directly). Properties `D2`, `D3`, `D4` are the correlation hole in §1–2;
`prop:M6` is the co-location gate that §4 proposes to move out of the edge.

Everything above is observation from one reading of one vendored copy. Where I am wrong about a
clause, the spec wins and I would like to know.
