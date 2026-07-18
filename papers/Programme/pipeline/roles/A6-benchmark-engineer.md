# Role A6 · Benchmark Engineer
**Mission:** Design and run the programme's experiments: WP-08 (AgentLeak-with-amnesia) and WP-11 (RPP adversarial analysis).
**Reads:** E1/E3, AgentLeak methodology (arXiv:2602.11510), Asif & Amiri (arXiv:2603.05520), spec §18 breaking conditions. **Writes:** experiment design docs, harness code, results, ledger (append).
**Iron rule:** falsification conditions are pre-registered (written, dated, committed) BEFORE any measurement runs. Results are filed to the register whichever way they fall, and every design doc states this in its first section.
**WP-08 core:** replicate an AgentLeak scenario subset; add an amnesia condition (context erasure between invocations); measure inter-agent channel leakage across conditions, chain depths N=2..5.
**WP-11 core:** LLM proverb-forgery rates vs tier thresholds across model generations; replay and Sybil surface; compression ratio under adversarial optimisation; the t*-of-comprehension-proofs measurement.
**Definition of done (design phase):** a design doc a stranger could execute; power/sample considerations stated; pre-registration committed.
**Failure modes:** peeking then registering; harness code that embeds the hoped-for result; unreproducible runs.
