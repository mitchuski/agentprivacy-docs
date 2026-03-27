# ZK Swordsman Blade Forge: Agent Build Instructions

**For:** AI Agents / Autonomous Builders
**Project:** ZK Swordsman Blade Forge v3.0
**Date:** March 27, 2026

---

## Overview

This document provides step-by-step instructions for an agent to build and extend the ZK Swordsman Blade Forge project. The project maps three converging frameworks:

1. **UOR (Universal Object Reference)** — algebraic ring structure
2. **64-Tetrahedra Lattice** — geometric compute space
3. **Zero Knowledge Proofs** — cryptographic witness structures

The "Blade Forge" metaphor unifies these: blades are ZK statements, forgings are witnesses, and the lattice is the forge.

---

## Step 1: Understand the Core Structure

### 1.1 Read the Main Document

```
READ: zk_swordsman_blade_forge_v3_0.md
```

Key concepts to extract:
- 64 vertices = 2^6 binary hypercube
- 6 dimensions: Protection, Delegation, Memory, Connection, Computation, Value
- Pascal's triangle distribution: 1-6-15-20-15-6-1 across strata
- Toroidal topology creates infinite path multiplicity

### 1.2 Internalize the Correspondence Table

| UOR | Geometry | ZK | Forge |
|-----|----------|-----|-------|
| Ring element | Vertex | Statement | Blade |
| Derivation | Traversal | Witness | Forging |
| Stratum | Hamming layer | Constraint degree | Edge count |

---

## Step 2: Create Directory Structure

```bash
mkdir blades
mkdir forge_circuits
mkdir uor_mappings
mkdir tests
mkdir docs
```

Purpose:
- `blades/` — Individual blade type specifications (64 total, one per vertex)
- `forge_circuits/` — ZK circuit implementations (PlonK, R1CS, etc.)
- `uor_mappings/` — UOR coordinate system definitions
- `tests/` — Verification and coherence tests
- `docs/` — Extended documentation

---

## Step 3: Generate Blade Specifications

### 3.1 Create Blade Template

For each vertex in the 64-lattice, create a blade specification file:

```markdown
# Blade: [vertex_address]

**Address:** (d1, d2, d3, d4, d5, d6)
**Stratum:** [popcount]
**Type:** [Null/Single/Twin/Triple/Quad/Penta/Full]

## Active Edges
- [ ] d1: Protection
- [ ] d2: Delegation
- [ ] d3: Memory
- [ ] d4: Connection
- [ ] d5: Computation
- [ ] d6: Value

## Adjacent Blades
[List vertices reachable in one XOR operation]

## UOR Properties
- Datum: [raw value interpretation]
- Spectrum: [which basis bits set]
- Content Hash: [Braille IRI if computed]

## ZK Use Cases
[Privacy patterns this blade configuration enables]
```

### 3.2 Generate All 64 Blades

```python
# Pseudocode for blade generation
for i in range(64):
    address = format(i, '06b')  # 6-bit binary
    stratum = bin(i).count('1')  # popcount
    create_blade_file(address, stratum)
```

Priority order:
1. Stratum 0: `(0,0,0,0,0,0)` — Null blade
2. Stratum 6: `(1,1,1,1,1,1)` — Full sovereignty blade
3. Stratum 2: `(1,1,0,0,0,0)` — Swordsman+Mage twin blade
4. Stratum 3: All 20 triple-edge configurations
5. Remaining strata

---

## Step 4: Define UOR Mappings

### 4.1 Create Ring Definition

File: `uor_mappings/ring_definition.md`

```markdown
# UOR Ring for Blade Forge

## Algebra
Z/(2^6)Z — 64-element modular ring

## Signature
- neg(x): Arithmetic complement
- bnot(x): Bitwise complement (antipodal jump)
- xor(x,y): Symmetric difference
- and(x,y): Intersection (toward null)
- or(x,y): Union (toward full)

## Core Identity
neg(bnot(x)) = succ(x)

## Verification
For all x in [0,63]:
  neg(bnot(x)) mod 64 == (x + 1) mod 64
```

### 4.2 Map Operations to Blade Transformations

File: `uor_mappings/operation_table.md`

Create lookup table showing:
- Input blade -> Output blade for each operation
- Edge traversals required
- Stratum changes

---

## Step 5: Implement Forge Circuits

### 5.1 Define Constraint System

File: `forge_circuits/adjacency_constraints.md`

The tetrahedral adjacency matrix defines valid single-step transitions:
- Two vertices are adjacent if they differ by exactly one bit (Hamming distance 1)
- This creates the R1CS constraint: `hamming(v1 XOR v2) == 1`

### 5.2 Create ZK Circuit Skeleton

File: `forge_circuits/blade_proof.circom` (or equivalent)

```
// Prove: "I have a blade at stratum K without revealing which"
template BladeStratumProof(k) {
    signal private input blade;  // 6-bit private witness
    signal output valid;

    // Constraint 1: blade is valid (0-63)
    // Constraint 2: popcount(blade) == k
    // Output: valid = 1 if constraints satisfied
}
```

### 5.3 Implement Path Verification

File: `forge_circuits/forging_path.circom`

```
// Prove: "I know a forging path from origin to target"
template ForgingPathProof(maxSteps) {
    signal private input path[maxSteps];  // sequence of operations
    signal private input origin;
    signal input target;  // public
    signal output valid;

    // Verify each step is valid operation
    // Verify final position == target
}
```

---

## Step 6: Build Test Suite

### 6.1 Coherence Tests

File: `tests/coherence_tests.md`

```markdown
# Coherence Test Suite

## Test 1: Ring Closure
For all x in [0,63]: neg(bnot(x)) mod 64 in [0,63]

## Test 2: Stratum Preservation
popcount(x) == stratum implies vertex in correct layer

## Test 3: Adjacency Validity
For all edges (v1,v2): hamming(v1,v2) == 1

## Test 4: Toroidal Wrap
Verify paths wrapping through boundary maintain vertex properties

## Test 5: Full Reachability
From any vertex, succ^n reaches all 64 vertices for n in [1,64]
```

### 6.2 ZK Verification Tests

File: `tests/zk_tests.md`

```markdown
# ZK Verification Tests

## Test 1: Stratum Proof
- Prover has blade at stratum 3
- Verifier learns only "stratum 3" not which of 20 blades

## Test 2: Path Independence
- Two different forgings of same blade
- Both produce valid proofs
- Proofs are indistinguishable to verifier

## Test 3: Soundness
- Invalid blade (stratum claimed != actual)
- Proof must fail verification
```

---

## Step 7: Document the Holographic Bound

### 7.1 96/64 Analysis

File: `docs/holographic_bound.md`

Key points to document:
- 96 edges on torus surface
- 64 vertices in lattice bulk
- Ratio 96/64 = 1.5 = P^1.5 (privacy exponent)
- Privacy value flows on boundary (edges), not bulk (vertices)

### 7.2 Open Conjectures

File: `docs/open_conjectures.md`

Track:
- C6: Is 96/64 = 1.5 structural or coincidental?
- Gap mapping to tetrahedral internal tension
- Golden ratio in optimal balance point

---

## Step 8: Integration with Parent Documents

### 8.1 Reference Chain

Ensure links to:
- Privacy is Value V5 (parent equation)
- PVM V5 Formal Specification
- Swordsman Mage Whitepaper V6
- Zero Knowledge Spellbook

### 8.2 Version Synchronization

When parent documents update:
1. Check for changes to core equation
2. Verify blade mappings still align
3. Update correspondence table if needed

---

## Step 9: Extension Points

### 9.1 Future Work Flags

- [ ] Implement actual ZK circuits (Circom/Noir/Halo2)
- [ ] Generate all 64 blade specification files
- [ ] Create visual lattice representation
- [ ] Build forging path simulator
- [ ] Connect to UOR Prism implementation
- [ ] Compute actual Braille IRIs for each vertex

### 9.2 Agent Handoff Protocol

When passing to another agent:
1. Summarize current state
2. List completed steps
3. Identify next priority task
4. Note any blockers or open questions

---

## Quick Reference: Key Formulas

```
Vertices: 2^6 = 64
Strata distribution: C(6,k) for k in [0,6]
Core identity: neg(bnot(x)) = succ(x)
Edge count (torus): 96
Holographic ratio: 96/64 = 1.5
Privacy exponent: P^1.5
```

---

## Completion Checklist

- [ ] Step 1: Read and internalize main document
- [ ] Step 2: Create directory structure
- [ ] Step 3: Generate blade specifications (priority blades first)
- [ ] Step 4: Define UOR mappings
- [ ] Step 5: Implement forge circuits (skeleton)
- [ ] Step 6: Build test suite
- [ ] Step 7: Document holographic bound
- [ ] Step 8: Verify parent document integration
- [ ] Step 9: Mark extension points for future work

---

*"Each step in this document is a hammer strike. Follow them, and the forge will light."*
