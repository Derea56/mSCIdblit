# mSCIdblit v1.9.111

## Gap-driven primary-literature expansion

This release adds 11 bounded evidence annotations:

- WNT5A > ROR2/FZD7 > Dishevelled/Rac1/AP-1 output
- Podoplanin > CLEC-2 > platelet activation output
- BTLA phosphosite set > SHP1/SHP2 inhibitory recruitment
- IL-4Rα Y497 > IRS1 phosphorylation and proliferation
- IL-2Rβ Y392/Y510 > STAT5 activation and DNA binding
- Ly49A ITIM > SHP1 and G6B-B ITIM/ITSM > SHP1 inhibitory relays
- E-cadherin juxtamembrane domain > p120-catenin adhesion stability
- RAGE cytoplasmic tail > DIAPH1/Rac1/Cdc42 migration output
- LILRB1/HLA-G-associated receptor-proximal > SHP2 inhibitory output

The routes use primary studies including PMID:7543676, PMID:8124718,
PMID:10457220, PMID:10629228, PMID:14652006, PMID:18215137,
PMID:18922799, PMID:20457807 and PMID:21887223. Site-set dependence,
receptor-complex context, ligand identity, cell-model boundaries and missing
terminal target-gene layers remain explicit. These are evidence-layer
annotations only: no graph edges, causal traversals or confidence scores are
asserted.

## Release counts

- Route evidence records: 19,622 -> 19,633
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 11

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion206`.
