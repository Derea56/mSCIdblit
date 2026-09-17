# mSCIdblit Module 20B–24B mechanism graph v1.8.83

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-078`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion078/`

This seventy-eighth selective literature-expansion release adds ten bounded
ligand–receptor–intracellular-continuation–output annotations. The routes
cover APRIL–BCMA–TRAF2, TNF–TNFR2–TRAF2/NF-kappaB, PGLYRP1–TREM1–DAP12,
S100A12–TLR4–TRAM, PRG4/lubricin–TLR4–TRAM, SLURP1–alpha7-nAChR–calcium,
Norrin–FZD4–DVL2, CTRP9–AdipoR1–APPL1, and adiponectin–AdipoR1 or AdipoR2–APPL1.

The annotations preserve measured activation, inhibitory, reporter,
phosphorylation, cellular-function, and gene-expression outputs. They retain
the two AdipoR branches separately and preserve the inhibitory PRG4 and SLURP1
contexts. The alpha7 and AdipoR records connect receptor-specific literature
to existing receptor-proximal continuation evidence while explicitly marking
the resulting route as composite. TF and terminal target-gene layers remain
open for mSCS.

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Context boundaries
include tumor, innate-immune, joint, epithelial, retinal, vascular, metabolic,
recombinant, reporter, and species-specific systems. In particular, a measured
receptor output does not establish a terminal TF or target gene, and a shared
receptor continuation is not treated as proof that every ligand uses the same
downstream mechanism.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,560 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 513 |
| Unique covered queue candidates | 497 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 170 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,834 |
| Unused P1 queue candidates remaining | 1,769 |

Primary studies represented include APRIL/BCMA signaling in myeloma
([PMID 27127303](https://pubmed.ncbi.nlm.nih.gov/27127303/)), TNFR2/TRAF2
NF-kappaB signaling ([PMID 7544915](https://pubmed.ncbi.nlm.nih.gov/7544915/)),
PGLYRP1 recognition by TREM1
([PMID 25595774](https://pubmed.ncbi.nlm.nih.gov/25595774/)), S100A12/TLR4
activation ([PMID 23611140](https://pubmed.ncbi.nlm.nih.gov/23611140/)),
PRG4/TLR4 regulation ([PMID 26752378](https://pubmed.ncbi.nlm.nih.gov/26752378/)),
SLURP1/alpha7-nAChR interaction
([PMID 26905431](https://pubmed.ncbi.nlm.nih.gov/26905431/)), Norrin/FZD4
signaling ([PMID 24186977](https://pubmed.ncbi.nlm.nih.gov/24186977/)), and
adiponectin receptor cloning and output
([PMID 12802337](https://pubmed.ncbi.nlm.nih.gov/12802337/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
