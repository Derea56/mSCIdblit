# mSCIdblit v1.9.106

## Gap-driven primary-literature expansion

This release adds six bounded route annotations selected from signaling gaps
where primary studies provide intracellular, transcriptional, functional or
inhibitory downstream support:

- SEMA4A > Plexin-B3 > Rnd1/R-Ras-associated contraction and growth-cone collapse
- DLL4 > NOTCH3 > receptor proteolysis-associated inflammatory transcription
- GDF11 > ACVR2B/ALK5 > SMAD2/3-associated reporter and developmental output
- IL-33 > soluble ST2 > decoy-mediated inhibition of ST2L-dependent output
- CCL26 > CCR2 > antagonism of CCR2 chemotaxis and receptor signaling
- ROS1 phospho-state > SHP-1 > receptor dephosphorylation and growth suppression

The routes use primary studies including PMID:20043131, PMID:17533181,
PMID:31315975, PMID:16845371, PMID:24244313, PMID:17623648,
PMID:15039444, PMID:11559700, PMID:11266449 and PMCID:PMC2199605.
Receptor-complex composition, model-specific outputs, inhibitory direction and
unresolved TF or target-gene layers remain explicit. These are evidence-layer
annotations only: no graph edges, causal traversals or confidence scores are
asserted.

## Release counts

- Route evidence records: 19,567 -> 19,573
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 6

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion201`.
