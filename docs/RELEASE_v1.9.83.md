# mSCIdblit v1.9.83

## Gap-driven primary-literature expansion

This release adds receptor-specific WNT5A output routes:

- WNT5A > TLR2 > MyD88/noncanonical NF-kB/AP-1 relay > IL-10/IL-8 and tolerance output
- WNT5A > TLR4 > MyD88/noncanonical NF-kB/AP-1 relay > IL-10/IL-8 and tolerance output

The primary study supports direct WNT5A binding to TLR2/TLR4, MyD88-dependent
noncanonical NF-kB/AP-1 signaling, and species-divergent cytokine and tolerance
outputs in human and mouse myeloid systems (PMID:31098409; PMCID:PMC6509336).
Because the study does not establish one terminal target-gene link, these remain
intracellular/output annotations rather than strict full target-gene routes.

All routes remain evidence-layer annotations: non-causal, non-traversable and
without database confidence scores. No new graph edges are asserted.

## Release counts

- Route evidence records: 19,474 -> 19,476
- Strict full-route annotations: 71 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion178`.
