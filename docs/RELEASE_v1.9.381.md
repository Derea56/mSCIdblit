# mSCIdblit release v1.9.381

This release adds one primary-literature full functional-output route for
CCL7/MCP-3: CCL7/MCP-3 → CCR2 → JAK1/JAK2/TYK2 → STAT3 → dormant
colorectal-cancer micrometastatic-cell reactivation. The primary study reports
CCL7/CCR2 binding or co-localization, JAK/STAT3 activation, and the functional
reactivation output (PMID:33986252; PMCID:PMC8119947; DOI:
10.1038/s41419-021-03698-5).

The route is retained as evidence-layer support for mSCS plausibility analysis.
The receptor-to-JAK and JAK-to-STAT3 handoffs remain unasserted graph edges,
and no terminal target-gene expression claim, causal assertion, traversal
permission, or confidence score is created. The cancer-metastasis model
context is retained and no SCI transfer is inferred.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,182 → 597,183
- Route nodes: 2,506,487 → 2,506,491
- Route edges: 2,305,072 → 2,305,075
- Literature-expansion rows: 31,068 → 31,069
- Full-sequence curation candidates: 15,519 → 15,520
- Unique ligands in the curation queue: 1,869 (unchanged)
- Target-gene-expression layer rows in the queue: 820 (unchanged)
- Review priorities: 9,756 P1, 1,875 P2, and 3,889 P3 candidates
- Coverage summary: 183 full functional-output, 173 full target-gene,
  1,452 partial downstream, and 805 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged from v1.9.380 because this
addition is an evidence-layer route and does not assert new causal graph
handoffs.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion622/`
