# mSCIdblit v1.9.113

## Gap-driven primary-literature expansion

This release adds 14 bounded receptor-proximal annotations:

- MAIR-II > FcRγ adaptor assembly, alongside its existing DAP12 branch
- CD300H > DAP12 and DAP10 adaptor associations
- CD229/Ly9 phosphosite relays to GRB2 or SAP, and CD84 pY299 > SHP2
- FCRL3 pY662 > SHIP1 and pY692 > SHP1 or SHP2
- CD36 complex > TLR4:TLR6 assembly and inflammatory reporter output
- IL-4Rα I4R-motif > IRS2/Akt and proliferation output
- PILRA/FDF03 > SHP2, EPOR pY343 > APS, and DDR1 pY881 > p85

The routes use primary studies including PMID:10374881, PMID:10903717,
PMID:11389028, PMID:15096483, PMID:15879090, PMID:17202337,
PMID:19843936, PMID:20037584, PMID:22057045, PMID:26221034 and
PMID:8995447. Phosphosite numbering, adaptor competition, receptor-chimera
systems, ligand and cell-type boundaries remain explicit. These are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,648 -> 19,662
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 14

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion208`.
