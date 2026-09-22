# mSCIdblit release v1.9.193

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-literature-expansion-307`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion307/`

## Source-reviewed downstream evidence

This release adds five evidence-only route annotations from primary studies to
the unresolved downstream queue. The annotations retain output/readout claims
without assigning ligand–receptor topology, intracellular intermediates,
transcription factors, target genes, causal status, or database confidence.

| Evidence record | Primary-supported readout |
|---|---|
| EDA/TNFSF27–EDAR/TNFRSF27 | NF-κB luciferase activation and ectodermal developmental phenotype |
| FGF8b–FGFR3c | Mid–hindbrain patterning and developmental gene-expression readout |
| CTHRC1–FZD5 | Wnt/PCP activation and canonical-Wnt suppression |
| YAP1–AXIN1/Axin | Wnt response regulation |
| WWTR1/TAZ–AXIN1/Axin | Wnt response regulation |

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 19,656 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Remaining queue records after literature overlays | 65 |
| L→R→output route category | 4,394 |

Validation passed with zero errors, and the bundle imported successfully through
mSCS's `import_mechanism_bundle.py`. The graph core remains unchanged; the
five additions are evidence-layer routes for plausibility analysis.
