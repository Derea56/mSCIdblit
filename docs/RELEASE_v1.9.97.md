# mSCIdblit v1.9.97

## Gap-driven primary-literature expansion

This release adds five bounded ligand–receptor/output annotations selected
from the remaining P1 downstream queue:

- HMGB1 (disulfide isoform) > MD-2/TLR4 > NF-kB-associated macrophage TNF release
- Netrin-1 > DCC > FAK/Src-associated axon attraction and outgrowth
- DLL1 > NOTCH2 > cleavage/nuclear translocation > RBP-Jkappa reporter activation
- IL-37 > IL-18Ralpha/IL-1R8 > anti-inflammatory signaling and transcriptional program
- SLIT2 > ROBO1 > srGAP1-Cdc42 > neuronal migration repulsion

The routes use primary studies including PMID:20547845, PMID:15494734,
PMID:10958687, PMID:25729923 and PMID:11672528. Receptor dependence,
intracellular relays, terminal target-gene links, developmental or injury
context and SCI transfer limitations remain explicit for each route. The
records are evidence-layer annotations only: no graph edges, causal
traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,522 -> 19,527
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion192`.
