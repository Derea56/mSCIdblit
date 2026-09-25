# mSCIdblit release v1.9.384

This release adds one primary-literature target-gene route for IFN-lambda1:
IFN-lambda1 → IFNLR1/IL10RB receptor system → TYK2-dependent STAT signaling →
ISGF3 → ISG15 expression. A primary human B-cell study reports IFN-lambda1
responsiveness, IFNLR1-dependent signaling, STAT1 phosphorylation, and ISG15
induction (PMID:34706932; PMCID:PMC8612983; DOI:
10.4049/jimmunol.2100339).

The route is retained as evidence-layer support for mSCS plausibility analysis.
The IFNLR1-to-relay and relay-to-ISGF3 handoffs remain unasserted graph edges;
the ISGF3-to-ISG15 layer is retained as graph evidence. No causal traversal,
SCI transfer, or database confidence score is created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,186 → 597,187
- Route nodes: 2,506,503 → 2,506,508
- Route edges: 2,305,084 → 2,305,088
- Literature-expansion rows: 31,072 → 31,073
- Full-sequence curation candidates: 15,523 → 15,524
- Unique ligands in the curation queue: 1,870 → 1,871
- Target-gene-expression layer rows in the queue: 821 → 822
- Review priorities: 9,757 P1, 1,876 P2, and 3,891 P3 candidates
- Coverage summary: 183 full functional-output, 175 full target-gene,
  1,452 partial downstream, and 803 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged from v1.9.383 because this
addition is an evidence-layer route and does not assert new causal graph
handoffs.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion625/`
