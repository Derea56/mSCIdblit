# mSCIdblit v1.9.84

## Gap-driven primary-literature expansion

This release adds two bounded ligand–receptor signaling routes identified by
targeted review of the unresolved P1 queue:

- CXCL12 > CXCR4 > ERK/AKT-associated NF-kB relay > SHH expression
- HGF (cleaved two-chain form) > MET > ERK/AKT/STAT3 relay > FOXM1 and
  cell-cycle output

The CXCL12 route is supported by primary human pancreatic-cancer experiments
showing CXCL12/CXCR4-dependent ERK and AKT activation, NF-kB activation, and
SHH expression (PMID:22995914; PMCID:PMC3493952). The HGF route is supported
by primary pancreatic-cancer experiments showing HGF/MET-dependent ERK1/2,
AKT, and STAT3 activation, FOXM1 induction and transcriptional activity, and
associated cell-cycle gene output (PMID:26876216; PMCID:PMC4985506).

Both routes remain evidence-layer annotations: non-causal, non-traversable,
and without database confidence scores. Neither route asserts a terminal
target-gene edge or transfers tumor-context evidence to spinal-cord injury.
No graph edges are asserted.

## Release counts

- Route evidence records: 19,476 -> 19,478
- Strict full-route annotations: 71 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion179`.
