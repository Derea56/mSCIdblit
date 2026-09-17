# mSCIdblit Module 20B–24B mechanism graph v1.8.68

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-063`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion063/`

This sixty-third selective literature-expansion release adds six
source-linked osteopontin/SPP1 receptor/output annotations:

- Osteopontin → αVβ1 integrin → RGD-dependent cell adhesion
- Osteopontin → αVβ5 integrin → RGD-dependent cell adhesion
- Osteopontin → αVβ6 integrin → RGD-dependent cell adhesion
- Osteopontin → α4β1 integrin → leukocyte adhesion
- Osteopontin → α8β1 integrin → RGD-dependent cell adhesion
- Osteopontin → ICOSL/B7-H2 → migration and metastasis-associated output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores. Integrin
subunit specificity, RGD and divalent-cation dependence, OPN cleavage state,
and the distinction between ICOSL and ICOS remain explicit. The batch does not
assert an intracellular continuation, transcription factor, or target gene for
any route.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,456 |
| Literature-expansion annotations in this batch | 6 |
| Cumulative literature-expansion annotations | 409 |
| Unique covered queue candidates | 394 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 233 |
| Unused downstream queue candidates remaining | 2,937 |
| Unused P1 queue candidates remaining | 1,872 |

Graph topology and causal edge counts are unchanged from v1.8.67. The bundle
passes `validate_module20_24_mechanism_graph.py` with zero errors and preserves
all prior `LITEXP` overlay records.

Primary studies represented include osteopontin-alphaVbeta1 and -alphaVbeta5
binding/adhesion (PMID 7592829), osteopontin-alphaVbeta6 binding (PMID
16005200), osteopontin-alpha4beta1 leukocyte adhesion (PMID 9547293),
osteopontin-alpha8beta1 binding (PMID 9614184; PMCID PMC25364), and secreted
osteopontin-ICOSL binding and migration/metastasis output (PMID 33106594;
PMCID PMC7588454; DOI 10.1038/s42003-020-01333-1).
