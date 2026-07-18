# Ledger entry format (append-only)

[LNNN][WP-nn or SUITE][P-gate or CANON-LEVEL][YYYY-MM-DD][role]
FINDING: what, where (file:line where applicable)
EVIDENCE: source/check output
PROPOSED: resolution
STATUS: open | accepted | rejected | resolved(date, by, how)

Rules: IDs sequential, never reused. CANON-LEVEL entries block nothing downstream
unless load-bearing (A0 marks). Resolution of CANON-LEVEL happens in the register
process, never in a rehydration (GR-10).
