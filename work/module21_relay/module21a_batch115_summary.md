# Module 21A batch 115 review

Batch 115 covers the 25 exact requested rows `M20A-EXT-1433`, `M20A-EXT-1434`, `M20A-EXT-1436` through `M20A-EXT-1452`, `M20A-EXT-1455`, `M20A-EXT-1461`, `M20A-EXT-1462`, `M20A-EXT-1474`, `M20A-EXT-1476`, `M20A-EXT-1477`, and `M20A-EXT-1483`.

## Disposition

- 4 `reviewed_relay_candidate`: CXCL12-beta3-containing integrin activation, DCN-ERBB4/STAT3/Sema3A functional relay, and DHH-PTCH1-SMO and DHH-PTCH2-SMO receptor-complex relays.
- 1 `reviewed_binding_only`: direct Dsc3-Dsg3 heterophilic desmosomal adhesion.
- 20 `reviewed_unresolved`: noncanonical CXCL13/CXCL16/CXCL2/CXCL5 receptor claims, the contradictory CXCL17-GPR35 claim, exact DKK4-LRP5, DMP1-PHEX, and DNAJB11-PRTG.
- No terminal TF assignments were made. Hedgehog and STAT3 observations were retained as pathway or functional evidence without promoting a TF endpoint for these exact rows.

## Evidence notes

- CXCL12-ITGB3 is supported by direct chemokine binding and allosteric activation of beta3-containing integrin complexes, including soluble and cell-surface alphaIIbbeta3 assays, plus independent CXCR4-dependent platelet alphaIIbbeta3 activation. The receptor-complex identity is preserved; the evidence does not claim that isolated ITGB3 is a chemokine GPCR.
- CXCL17-GPR35 remains unresolved because the initial CXCR8/GPR35 report is contradicted by later AP-TGF-alpha, beta-arrestin, IP1, BRET, antagonist, knockdown, and transfectant studies. The later negative evidence prevents promotion to a direct receptor edge.
- Decorin-ERBB4 retains a receptor-proximal/functional relay because ErbB4 blocking antibody and siRNA, together with STAT3 inhibition and Sema3A output measurements, support ErbB4-dependent regulation. The primary perturbation study was not treated as an isolated direct binding assay.
- DHH-PTCH1-SMO and DHH-PTCH2-SMO retain the receptor-complex distinction. PTCH1/2 bind hedgehog ligands and associate with SMO, while DHH-specific functional models support Smoothened-dependent or Ptch2-dependent outputs. No terminal GLI TF was inferred.
- DKK4-LRP5 remains unresolved because the direct DKK4 binding work tested LRP6 E1E2; family-level LRP5/6 statements were not substituted for an exact LRP5 assay. DMP1-PHEX remains unresolved because direct DMP1 cleavage/activity assays were negative or inconclusive despite shared bone-mineralization pathway phenotypes. DNAJB11-PRTG had no exact experimental edge recovered.
- Dsc3-Dsg3 is retained as direct binding-only evidence. Family-wide SPR and bead-aggregation assays measured this pair as the weakest but specific heterophilic desmosomal cadherin interaction; no intracellular pathway or TF was inferred.

## Search boundary and controls

Searches covered exact gene/protein pair queries across PubMed, PMC, publisher pages, and pathway/interaction resources, with primary research prioritized. Canonical chemokine receptor comparators were used only to define boundaries: CXCL13-CXCR5, CXCL16-CXCR6, CXCL2/CXCL5-CXCR2, and CXCL17's unresolved receptor status. Family-level receptor annotations, co-expression, network associations, and downstream functional observations were not converted into direct molecular interactions. Receptor complexes were kept intact, especially beta3-containing integrin and PTCH-SMO complexes. Every terminal_TF field is `null`.

## Validation

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch115_review.tsv` and `module21a_batch115_summary.md` are written by this batch; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
