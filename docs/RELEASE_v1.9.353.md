# mSCIdblit release v1.9.353

This release adds a primary-literature PGE2→EP2→PKA→CREB→IL6 gene-expression
route. The route connects the existing PGE2/EP2 graph layer to existing PKA,
CREB, and IL6 nodes while retaining the intermediate handoffs as
source-supported evidence rather than asserted graph edges.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,349 → 596,350
- Route nodes: 2,502,361 → 2,502,366
- Route edges: 2,301,779 → 2,301,783
- Literature-expansion rows: 30,235 → 30,236
- Full-sequence curation candidates: 15,466 → 15,467
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 (unchanged)
- P3 review candidates: 3,870 → 3,871

Primary locators for the route are PMID:21209948, PMID:15855407, and
PMID:15121014. Validation passed with no errors; the inherited warning remains
that some evidence sources lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion593/`
