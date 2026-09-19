# mSCIdblit v1.9.101

## Gap-driven primary-literature expansion

This release adds five bounded route annotations selected from receptor-entry
and incomplete-output gaps in the downstream queue:

- JAG2 > NOTCH2 > NICD2/RBPJ > reporter activation
- IL17F > IL17RA:IL17RC > chemokine secretion
- BMP9 > ACVRL1/type-II receptor complex > SMAD1/5/8 > ID1/BRE output
- NODAL > ACVR1C/ALK7:ACVR2B > SMAD2/3 > reporter output
- FGF10 > FGFR2b > MAPK-associated epithelial functional output

The routes use primary studies including PMID:10958687, PMID:17911633,
PMID:18684971, PMID:17068149, PMID:19366699, PMID:11485994,
PMID:11024047, PMID:12591959, PMID:32127497 and PMID:24960693. Receptor
complex composition, membrane presentation, cell-model boundaries, terminal
target-gene gaps and SCI transfer limitations remain explicit. These are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,534 -> 19,539
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion196`.
