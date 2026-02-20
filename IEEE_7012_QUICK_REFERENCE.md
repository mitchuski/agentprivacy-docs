# IEEE 7012-2025 Quick Reference
## Machine Readable Personal Privacy Terms for 0xagentprivacy

**Version:** 1.0  
**Date:** January 29, 2026  
**Standard Published:** January 20, 2026  
**Status:** ✅ CANONICAL REFERENCE

---

## Overview

IEEE Std 7012™-2025 establishes the foundational standard for machine-readable personal privacy terms. This standard inverts the traditional notice-and-consent model: individuals propose terms as first parties, organizations respond as second parties.

The Swordsman browser agent implements IEEE 7012 as its core agreement layer.

**Standard Host:** Customer Commons (customercommons.org/p7012)  
**Working Group Chair:** Doc Searls  
**Vice Chair:** Justin Byrd  
**Editor:** Mary Hodder

---

## Core Principles

### The Inversion

| Traditional Model | IEEE 7012 Model |
|-------------------|-----------------|
| Organization writes terms | Individual proposes terms |
| Individual accepts or leaves | Organization accepts, negotiates, or declines |
| Unilateral imposition | Bilateral agreement |
| "Notice and consent" | "Propose and respond" |
| Attack pattern | Invitation pattern |

### Promise Theory Alignment

IEEE 7012 implements the **invitation pattern** from Promise Theory:

- **Invitation Pattern:** Acceptance relationship established BEFORE specific proposals
- **Attack Pattern:** Extraction without prior consent (surveillance default)

The Swordsman presents terms BEFORE any data exchange. Site must accept terms to proceed.

---

## Canonical Definitions

*Note: These are paraphrased interpretations for 0xagentprivacy context. See official IEEE documentation for authoritative definitions.*

| Term | Definition | 0xagentprivacy Mapping |
|------|------------|------------------------|
| **Agent** | An actor working on behalf of a person to represent them and present proposed terms to entities | Swordsman browser agent |
| **Agreement** | A compound set of terms or clauses, proposed and offered before formal contract | MyTerms negotiation output |
| **Contract** | A mutual agreement creating enforceable obligations between parties | Signed bilateral record |
| **Entity** | Any organization with which a person makes contractual agreement (always organization) | Second party / service provider |
| **First Party** | The individual (always a person, never organization) | First Person 😊 |
| **Second Party** | The entity (always an organization) | Service provider |
| **Policy** | Set of obligations for communication and cooperation (per ISO 22600-2:2014) | Privacy policy framework |
| **Proposer** | A person who advances terms and agreements to another party | First Person via Swordsman |
| **DPV** | Data Privacy Vocabulary - W3C machine-readable metadata standard | Semantic interoperability layer |
| **Machine-readable** | Terms that can be processed by computer systems | JSON-LD, RDF, HTTP headers |

---

## Agreement Taxonomy

### Service Delivery Agreements (SD)

These agreements govern what a service provider may do with data during service delivery.

| Code | Name | Description |
|------|------|-------------|
| **SD-BASE** | Service Delivery Only | Service delivery only. No analytics, tracking, or profiling. |
| **SD-BASE-DP** | + Data Portability | Service delivery with data portability rights included. |
| **SD-BASE-A** | + Analytics | Analytics by second party permitted. No tracking or profiling. |
| **SD-BASE-AT** | + Analytics + Tracking | Analytics and tracking by second party permitted. No profiling. |
| **SD-BASE-ATP** | + Full Profiling | Full analytics, tracking, and profiling by second party permitted. |
| **SD-BASE-ATP-S3P** | + Third Party Sharing | Full profiling plus anonymized data sharing with third parties. |

**Hierarchy:** SD-BASE is most restrictive → SD-BASE-ATP-S3P is most permissive

### Personal Data Contribution Agreements (PDC)

These agreements govern intentional data contributions by the First Person.

| Code | Name | Description |
|------|------|-------------|
| **PDC-INTENT** | Intentcasting | Going to market with structured requirements. First Person declares what they seek; entities respond. |
| **PDC-AI** | AI Training | Contributing data for AI model training. Explicit consent for machine learning use. |
| **PDC-GOOD** | Public Good | Contributing data for public benefit purposes. Research, commons, collective intelligence. |

---

## Technical Specifications

### Machine-Readable Formats

IEEE 7012 specifies multiple formats for interoperability:

| Format | Use Case | Notes |
|--------|----------|-------|
| **HTTP Headers** | Real-time negotiation | MRPAZ protocol for request/response |
| **JSON / JSON-LD** | API integration | Structured data with semantic context |
| **RDF / Turtle** | Semantic web | Linked data compatibility |
| **Bitwise (CONTRACT ZONE)** | Compact encoding | Efficient binary representation |

### HTTP Header Protocol (MRPAZ)

The MRPAZ protocol enables real-time term negotiation via HTTP headers:

```
Request:
P7012-Terms: SD-BASE
P7012-Version: 1.0

Response:
P7012-Accept: SD-BASE
P7012-Status: ACCEPTED
```

---

## 0xagentprivacy Implementation Mapping

| IEEE 7012 Element | 0xagentprivacy Component |
|-------------------|--------------------------|
| Individual Agent | Swordsman browser extension |
| Entity Agent | Website MyTerms responder |
| Agreement-chooser | MyTerms configuration UI |
| Proposer function | Swordsman's automatic term presentation |
| Recorder function | Chronicle system (bilateral proof storage) |
| HTTP MRPAZ headers | Cookie-slashing protocol integration |
| CONTRACT ZONE | Bitwise term encoding for efficiency |
| Customer Commons | Neutral agreement registry host |

---

## Integration with Dual-Agent Architecture

### Why IEEE 7012 Matters for Privacy

The standard provides the **agreement layer** that makes dual-agent architecture enforceable:

| Layer | Function | Standard |
|-------|----------|----------|
| **Agreement** | What terms govern interaction | IEEE 7012 |
| **Protection** | Enforce boundaries | Swordsman ⚔️ |
| **Delegation** | Execute authorized actions | Mage 🧙 |
| **Verification** | Prove compliance | ZKP / VRCs |

Without the agreement layer, the Swordsman has no terms to enforce. IEEE 7012 gives the blade meaning that persists.

### The Blade and The Contract

*"The blade slashes surveillance. The contract binds behavior."*

- **Slashing alone is insufficient:** Cookies respawn, trackers return
- **Contracts create persistence:** Violation is breach, not just technical failure
- **Both serve the First Person:** Destruction without agreement is endless war; agreement without enforcement is mere hope

---

## Customer Commons

IEEE 7012 agreements are hosted by **Customer Commons**, a neutral nonprofit that:

- Maintains the official agreement registry
- Profits from neither individuals nor organizations
- Provides permanence and trust through neutrality
- Enables verification without centralized control

This neutral hosting is essential—it prevents capture by either side of the agreement.

---

## Resources

### Official Sources

- **IEEE Standard:** IEEE Std 7012™-2025
- **Customer Commons:** customercommons.org/p7012
- **W3C DPV:** w3.org/ns/dpv (Data Privacy Vocabulary)

### 0xagentprivacy Documentation

- **Whitepaper v4.8:** §4.X The MyTerms Foundation
- **Glossary v2.3:** Section 9 - IEEE 7012-2025 Standard
- **Spellbook:** Integration with MyTerms Swordsman

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | January 29, 2026 | Initial release aligned with IEEE 7012-2025 publication |

---

*"The cookie crumbles, the contract remembers. Slash what violates, bind what agrees."*

**⚔️📜 | 😊**
