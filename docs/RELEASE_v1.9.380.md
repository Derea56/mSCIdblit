# mSCIdblit release v1.9.380

This release continues the all-ligand full-sequence promotion pass with a
provenance-reconciled tranche of 28 primary-locator-backed evidence routes
spanning three ligand node IDs: Il15, Il34, and PGE2/prostaglandin E2. The
routes retain ligand, receptor, intracellular continuation, transcription
factor, and target-gene layers as composed evidence for mSCS plausibility
analysis. Their summaries explicitly identify the component-evidence nature
of the route; no single paper is asserted to demonstrate every handoff.

The generator produced 30 candidates. Two IL13 candidates were excluded
because their source queue IDs did not match the queue IDs on their evidence
records. The remaining rows were retained only when a stable primary locator
and source-record pairing were present. These additions remain evidence-layer
annotations: they do not create graph edges, causal assertions, traversal
permissions, or confidence scores.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,154 → 597,182
- Route nodes: 2,506,347 → 2,506,487
- Route edges: 2,304,960 → 2,305,072
- Literature-expansion rows: 31,040 → 31,068
- Full-sequence curation candidates: 15,519 (unchanged after deduplication)
- Unique ligands in the curation queue: 1,869 (unchanged)
- Target-gene-expression layer rows in the queue: 820 (unchanged)
- Review priorities: 9,755 P1, 1,875 P2, and 3,889 P3 candidates
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged at 255 edge-chain instances and
144 unique four-node topologies. This is expected: the promotion adds
source-linked route evidence and does not assert new causal graph handoffs.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion621/`
