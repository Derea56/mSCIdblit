# mSCIdblit release v1.9.379

This release applies the conservative all-ligand source-linked promotion pass
to the current mechanism graph. It adds 735 primary-locator-backed evidence
routes spanning nine ligand node IDs. Each route retains ligand, receptor,
intracellular continuation, transcription-factor, and target-gene layers while
leaving unresolved handoffs explicit. The additions are evidence-layer
annotations for mSCS plausibility analysis; they do not create graph edges,
causal assertions, traversal permissions, or confidence scores.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,419 → 597,154
- Route nodes: 2,502,672 → 2,506,347
- Route edges: 2,302,020 → 2,304,960
- Literature-expansion rows: 30,305 → 31,040
- Full-sequence curation candidates: 15,515 → 15,519
- Unique ligands in the curation queue: 1,869 (unchanged)
- Target-gene-expression layer rows in the queue: 816 → 820
- Review priorities: 9,755 P1, 1,875 P2, and 3,889 P3 candidates
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged at 255 edge-chain instances and
144 unique four-node topologies. This is expected: the promotion adds
source-linked route evidence and does not assert new causal graph handoffs.
The queue increases by only four because the 735 route annotations are
deduplicated by route signature for curation.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion620/`
