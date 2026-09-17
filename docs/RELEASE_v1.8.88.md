# mSCIdblit Module 20B–24B mechanism graph v1.8.88

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-083`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion083/`

This eighty-third selective literature-expansion release adds ten unique
ligand–receptor route annotations. The batch covers INSL3–RXFP2/LGR8,
LTB4–BLT2, sweet and umami TAS1R heteromers, thrombin–PAR3, thrombin–PAR4,
2-AG–CB2, PACAP–VPAC1, PACAP–VPAC2, and alpha-MSH–MC1R. Six routes connect to
existing receptor-proximal G-protein continuation edges; four remain explicit
L→R→output evidence because no intracellular continuation was asserted.

The annotations preserve receptor-specific cAMP, phosphoinositide, calcium,
chemotaxis, reporter, ERK, arrestin, and phospholipase-D readouts. PAR4
proteolytic activation and phosphoinositide signaling are supported by a
cloned-receptor primary study ([PMID 9618465](https://pubmed.ncbi.nlm.nih.gov/9618465/));
BLT2 receptor activation and calcium/chemotaxis evidence are represented by
[PMID 10934230](https://pubmed.ncbi.nlm.nih.gov/10934230/), and RXFP2/INSL3
partial-agonist cAMP evidence by
[PMID 15649866](https://pubmed.ncbi.nlm.nih.gov/15649866/). The taste-receptor
annotations use the cloned sweet/umami receptor study
([PMID 11917125](https://pubmed.ncbi.nlm.nih.gov/11917125/)).

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Several routes come
from cloned or transfected receptor systems, and receptor coupling can vary
with receptor isoform, ligand form, cell type, and assay context. TF and
terminal target-gene layers remain open for mSCS.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,611 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 564 |
| Unique covered queue candidates | 542 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 217 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 248 |
| Unused downstream queue candidates remaining | 2,789 |
| Unused P1 queue candidates remaining | 1,724 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records. Batch 083 was checked against
all prior batch inputs to ensure that each newly selected queue candidate is
unique.
