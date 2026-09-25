# mSCIdblit release v1.9.382

This release adds one primary-literature target-gene evidence route for
GPNMB/osteactivin soluble extracellular domain: GPNMB → CD44 → p38/STAT3 →
IL-33 expression. The primary mouse tumor study reports GPNMB binding to CD44,
increased p38 and STAT3 phosphorylation, and GPNMB/CD44-associated IL-33
expression and release (PMID:32728200; PMCID:PMC8027814; DOI:
10.1038/s41423-020-0501-0).

The route is retained as evidence-layer support for mSCS plausibility analysis.
The receptor-to-p38, p38-to-STAT3, and STAT3-to-IL33 handoffs remain
unasserted graph edges. The source may reflect parallel or complementary
pathway readouts, so no end-to-end causal chain, traversal permission, or
confidence score is created. The tumor-model context is retained and no SCI
transfer is inferred.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,183 → 597,184
- Route nodes: 2,506,491 → 2,506,496
- Route edges: 2,305,075 → 2,305,079
- Literature-expansion rows: 31,069 → 31,070
- Full-sequence curation candidates: 15,520 → 15,521
- Unique ligands in the curation queue: 1,869 (unchanged)
- Target-gene-expression layer rows in the queue: 820 → 821
- Review priorities: 9,756 P1, 1,875 P2, and 3,890 P3 candidates
- Coverage summary: 183 full functional-output, 174 full target-gene,
  1,451 partial downstream, and 805 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged from v1.9.381 because this
addition is an evidence-layer route and does not assert new causal graph
handoffs.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion623/`
