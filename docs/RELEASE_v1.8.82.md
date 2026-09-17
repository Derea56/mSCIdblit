# mSCIdblit Module 20B–24B mechanism graph v1.8.82

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-077`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion077/`

This seventy-seventh selective literature-expansion release adds ten bounded
non-GPCR receptor-proximal evidence routes. The routes cover collagen III or
X through GP6/GPVI or DDR2, CD70 through CD27, surfactant proteins through
OSCAR or SIRPA, extracellular HSP70 through CD40, trehalose dimycolate through
CLEC4E/Mincle, ANGPTL2 through LILRB2, and dengue virion through CLEC5A. The
annotations connect measured outputs to existing FCER1G, SHC1, TRAF2, PTPN6,
TRAF6, or TYROBP continuations where the graph contains them.

These records preserve receptor-proximal functional, phosphorylation,
reporter, phagocytosis, or secreted-protein readouts while leaving TF and
terminal target-gene layers open for mSCS. They are evidence-layer routes,
not causal graph edges; no database confidence score or SCI-specific transfer
is asserted. Context boundaries include recombinant or transfected systems,
receptor isoforms, adaptor dependence, inhibitory polarity, species or tissue
boundaries, and outputs that do not establish a terminal transcriptional event.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,550 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 503 |
| Unique covered queue candidates | 487 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 160 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,844 |
| Unused P1 queue candidates remaining | 1,779 |

Primary studies represented include GPVI recognition of collagen III
([PMID 18305222](https://pubmed.ncbi.nlm.nih.gov/18305222/)), collagen-dependent
DDR2 activation ([PMID 18201965](https://pubmed.ncbi.nlm.nih.gov/18201965/)),
HSP70-CD40 uptake and p38 activation
([PMID 12356871](https://pubmed.ncbi.nlm.nih.gov/12356871/)), Mincle recognition
of trehalose dimycolate ([PMID 20008526](https://pubmed.ncbi.nlm.nih.gov/20008526/)),
ANGPTL2-LILRB2 signaling ([PMID 22660330](https://pubmed.ncbi.nlm.nih.gov/22660330/)),
and CLEC5A/DAP12-dependent dengue cytokine release
([PMID 18496526](https://pubmed.ncbi.nlm.nih.gov/18496526/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
