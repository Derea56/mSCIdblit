# mSCIdblit v1.9.110

## Gap-driven primary-literature expansion

This release adds 17 bounded route annotations selected from canonical
ligand–receptor gaps with primary functional support:

- CXCL13 > CXCR5; CXCL9/10/11 > CXCR3; CXCL6 > CXCR1/CXCR2; CXCL2 > CXCR2
- CXCL16 > CXCR6; CXCL11 > ACKR3/CXCR7; CCL20 > CCR6; CCL19 > CCR7
- CX3CL1 > CX3CR1 and ATP > P2X7/P2RX7
- TSP1 > CD36 and latent TGF-β1/LAP > αVβ6
- MFG-E8/lactadherin > αVβ3 and αVβ5

The routes use primary studies including PMID:10025398, PMID:10821695,
PMID:11259614, PMID:11290797, PMID:11688722, PMID:11943809,
PMID:12000961, PMID:15937099, PMID:17363734, PMID:23640500,
PMID:25395671, PMID:25614627 and PMID:32541785. Nucleotide priming,
membrane-versus-soluble ligand forms, ligand redundancy, atypical-receptor
behavior, opsonin bridging and context-specific inhibitory direction remain
explicit. These are evidence-layer annotations only: no graph edges, causal
traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,605 -> 19,622
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 17

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion205`.
