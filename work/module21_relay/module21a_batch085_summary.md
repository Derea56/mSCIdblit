# Module 21A batch 085 review summary

Batch 085 covers exact filtered priority-8 queue ordinals 1426–1450: 25 review IDs (`M20A-CELLCHAT-REMAINING-1564` through `-1595`, with the queue gaps preserved).

## Disposition

- 18 `reviewed_relay_candidate`
  - PGD2-AKR1C3→PTGDR2/CRTH2 and PTGFR/FP
  - PGE2-PTGES, PGE2-PTGES2, and PGE2-PTGES3→PTGER1/2/3/4
  - PGF2α-CBR1 and PGF2α-PRXL2B→PTGFR/FP
  - PGI2-PTGIS→PTGIR/IP
  - PPIA→BSG/CD147
- 6 `reviewed_binding_only`
  - Pcdhgb8, Pcdhgc3, Pcdhgc4, and Pcdhgc5 homophilic adhesion
  - Pecam1–Cd177 heterophilic adhesion
  - Pecam1–Pecam1 homophilic adhesion
- 1 `reviewed_unresolved`
  - Pecam1–Cd38; no exact direct interaction or receptor-proximal relay was validated in the bounded search
- 0 `reviewed_function_only`
- 0 terminal TF assignments

## Evidence handling

The prostanoid synthases and processing enzymes (AKR1C3, PTGES/PTGES2/PTGES3, CBR1, PRXL2B, and PTGIS) are recorded only as source-processing context. The promoted relay is the mature lipid-to-receptor branch, with subtype-specific prostanoid receptor coupling kept separate. No enzyme-to-receptor direct molecular interaction was inferred.

The clustered protocadherin and PECAM1 self/heterophilic rows remain binding or adhesion evidence only. Neuronal, endothelial-barrier, neutrophil, platelet, ocular, implantation, and chemotaxis phenotypes are recorded as context or limitations and were not converted into terminal TF edges.

## Search boundary

The bounded search covered PubMed records, PMC full-text records where available, and stable publisher/DOI records. Primary evidence was prioritized for receptor binding, subtype-selective second-messenger assays, receptor perturbation, cell aggregation, mutagenesis, and source-enzyme perturbation. For Pecam1–Cd38, the search found PECAM1 homophilic and other heterophilic adhesion studies but no exact direct pair assay; this remains explicitly unresolved rather than inferred from co-expression or shared immune-cell context.

## Validation

- One row per requested queue ID: 25 rows.
- Required 13-column schema present on every row.
- Review IDs are unique and preserve the queue gaps.
- Module20A ledgers, frozen manifest, shared registers, and integration outputs were not modified.
