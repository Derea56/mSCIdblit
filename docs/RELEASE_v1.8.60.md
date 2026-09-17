# mSCIdblit Module 20B–24B mechanism graph v1.8.60

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-055`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion055/`

This fifty-fifth selective literature-expansion release adds seven source-linked
tenascin-C (`TNC`) ligand–receptor/partner annotations with bounded adhesion,
neurite, ERK, matrix-binding or glial outputs:

- TNC → alpha2beta1 integrin → endothelial adhesion and spreading
- TNC → alphaVbeta3 integrin → endothelial adhesion and spreading
- TNC → alpha8beta1 integrin → neuronal adhesion and neurite outgrowth
- TNC → alpha7beta1 integrin → neuronal adhesion and neurite outgrowth
- TNC → EGFR → ERK activation and mitogenic output
- TNC → phosphacan/PTPRZ1 → neural-matrix binding and adhesion modulation
- TNC → RPTPbeta/PTPRB → glial adhesion and spreading

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. The studies span extracellular matrix,
integrin, receptor and developmental-cell contexts; intracellular continuation,
TF and target-gene layers remain unresolved in all seven records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,406 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 359 |
| Unique covered queue candidates | 344 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 184 |
| Unused downstream queue candidates remaining | 2,987 |
| Unused P1 queue candidates remaining | 1,920 |

The graph topology and causal edge counts are unchanged from v1.8.59. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include tenascin-C/integrin endothelial adhesion
(PMID 7693733), alpha8beta1 neuronal adhesion (PMID 7541634), alpha7beta1
neurite outgrowth (PMID 14715956), Ten14/EGFR ERK signaling (PMID 11470832;
PMCID PMC2150768), phosphacan binding (PMID 9182584), and RPTPbeta/PTPRB glial
adhesion (PMID 11313993).
