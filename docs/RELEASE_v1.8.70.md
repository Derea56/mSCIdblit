# mSCIdblit Module 20B–24B mechanism graph v1.8.70

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-065`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion065/`

This sixty-fifth selective literature-expansion release adds one
source-linked TGFB1–ALK1 endothelial route. The primary study supports
ALK1-associated SMAD1/5 phosphorylation and increased endothelial
proliferation and migration, while showing that ALK5 and TGFBR2 are required
for optimal ALK1 activation.

The route is retained as:

`TGFB1 → ACVRL1/ALK1 → ???? → SMAD1/5/8 → endothelial proliferation/migration`

The intracellular adaptor ordering and terminal target gene remain unresolved.
The record therefore adds TF/output evidence without asserting a complete
intracellular cascade, a causal graph edge, a database confidence score, or
SCI transfer. The ALK5/TGFBR2 cofactor and opposing SMAD2/3-branch context are
preserved.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,463 |
| Literature-expansion annotations in this batch | 1 |
| Cumulative literature-expansion annotations | 416 |
| Unique covered queue candidates | 401 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 55 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,930 |
| Unused P1 queue candidates remaining | 1,865 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary study: Goumans et al., “Activin receptor-like kinase (ALK)1 is an
antagonistic mediator of lateral TGFβ/ALK5 signaling,” PMID 14580334, DOI
10.1016/S1097-2765(03)00386-1.
