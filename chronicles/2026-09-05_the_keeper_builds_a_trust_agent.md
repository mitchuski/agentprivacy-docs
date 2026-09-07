# 2026-09-05 · The keeper builds a trust agent

*Family-B chronicle (agentprivacy-docs telling). Compresses to the master chronicle
`agentprivacy_master/docs/chronicles/2026-09-05_the-keeper-builds-a-trust-agent.md` — unsigned; the First Person's read comes
first. Nothing committed, no domain changed, no system component installed, no mnemonic seen.*

## What moved

**An agentic runtime stood up the first pieces of the City's Verifiable Trust Agent on the keeper's own machine.**
OpenVTC's Verifiable Trust Infrastructure (the reference implementation of the ToIP Decentralized Trust Graph
working group's specifications, begun in Rust by Affinidi's Glenn Gore and DTGWG member Geoff Turk) was cloned with its
setup guides; the Rust toolchain moved from 1.91 to 1.98; and the four operator tools — `pnm` (the personal network
manager, the keeper's hand on a VTA), `cnm` (the community manager), `vta-mcp` (the MCP bridge an agent client drives a
VTA through) and `didcomm-test` — were built in release mode and placed on the keeper's PATH. The VTA and VTC services
themselves wait on one Visual Studio component, named for the keeper to add.

**Three builds, three Windows facts.** The first build failed because the VTA's WebAuthn dependency needs OpenSSL
development libraries; a static OpenSSL 3.6.4 was built with vcpkg in three and a half minutes. The second failed because
the services' Rego policy engine insists on Visual Studio's Spectre-mitigated libraries, absent from Build Tools 2019.
The third built only what depends on neither, and succeeded. On Linux none of the three facts exists, which is one
more reason the plan puts the services on the Pi or a VPS and only `pnm` on this machine.

**A reader in which the keeper makes the choices.** `mages_city/deploy/viewer/`: six decisions with the consequence of
each option written beside it (DNS profile, edge host, VTI host, how the services run, secrets backend, the first
community trust anchors); the steps rewrite themselves from the choices; the Pi 4's job in six cells; the first trust
edges in the only order they can exist; what was verified, each fact with its source and date. A zero-dependency server
autosaves the keeper's choices into the repository, so the decisions are a file, not a browser's memory. The keeper made
the first set the same evening.

## What was decided, and what each choice costs

The recommended path is managed DNS at Cloudflare with one tunnel and Workers for the front; the Pi 4 as the always-on
edge for the tunnel, the farm, the Portal and later the gate; the Rust services on the Pi 5 or a small VPS; bare binaries
under systemd; the platform credential manager for secrets; the keeper's own VTA as the first anchor. Each alternative
carries a named cost: a sovereign zone costs a public inbound door and a secondary nameserver; this PC as the edge dies
with the session; a VPS is one more machine; Kubernetes is announced upstream but unpublished; a cloud KMS puts the root
keys with a provider.

Two shapes arrived during the evening. Naming agents as `<mage>.vta.mages.city` by BIND9 on graph permission fits the
Namekeeper exactly but sits outside Cloudflare's universal certificate and the tunnel, so it means delegating the `vta.`
child zone and terminating TLS at the keeper's own edge. The keeper's later reading dissolves the tradeoff: **city for
the agent, world for the community, earth for the network** — `mages.city` the agent layer, `mages.world` the community
that admits and decides, `mages.earth` the shared mediator, DID host and governance frame — each a single-level zone.

## What the corpus and the registries said

The DTG vocabulary carried the reading without strain: Verifiable Trust Agent, Community, Network. At the registries,
all four names delegated to GoDaddy at the first check; by the second, `mages.city` and `mages.world` delegated to
Cloudflare, with `mages.earth` and `agentprivacy.org` still propagating. The registries, not the dashboards, were
where the runtime read it.

## What the runtime refused

The 24-word mnemonic the setup wizard mints (the keeper runs the wizard); the elevated system install (the exact command
is written, not run); any write to a zone; any commit; and two claims it could not verify, that the crates build on
64-bit ARM and that a Kubernetes path exists upstream. One error is recorded against the runtime itself: a build's exit
code masked by a pipe, read as success for four minutes, caught by looking for the binaries rather than trusting the
code, and turned into a rule for every detached job after it.

*The inversion: asked about a server, the evening answered that the server is the easy part; the stand-up needed the
decisions written down, and its one secret held by the keeper alone.*
