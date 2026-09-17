# mSCIdblit Module 20B–24B mechanism graph v1.8.75

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-070`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion070/`

This seventieth selective literature-expansion release adds six bounded
ligand–receptor route annotations:

- CXCL8 → CXCR1 → receptor activation/calcium output
- CXCL8 → CXCR2 → receptor activation/calcium and neutrophil-recruitment output
- CXCL1 → CXCR2 → receptor activation and neutrophil-recruitment output
- SDC2 → CD148 → SRC pY529 → beta1-integrin adhesion/cytoskeletal output
- C4BP alpha chain → CD40 → B-cell activation output
- CD55 → CD97 → cell-adhesion output

These are retained evidence routes, not causal graph edges. The five output-only
annotations intentionally leave intracellular, transcription-factor and
terminal target-gene layers unresolved. The SDC2 route includes the graph-linked
CD148-to-SRC continuation but still has no TF or terminal target gene. Species,
cell-system and assay boundaries are retained, and no database confidence score
or SCI-specific transfer is asserted.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,480 |
| Literature-expansion annotations in this batch | 6 |
| Cumulative literature-expansion annotations | 433 |
| Unique covered queue candidates | 418 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 92 |
| Cumulative L→R→TF→output annotations missing intracellular | 60 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,913 |
| Unused P1 queue candidates remaining | 1,848 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include CXCL8 receptor activation and calcium
mobilization (PMID 20630874), CXCL1/CXCR2 activation and recruitment (PMIDs
23479735 and 32881070), syndecan-2/CD148 signaling (PMID 21813734), C4BP/CD40
B-cell activation (PMID 12818164), and CD55/CD97 adhesion (PMID 9064337).
