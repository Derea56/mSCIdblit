# Module 21A batch 113 review

Batch 113 covers the 25 exact requested rows `M20A-EXT-1315` through `M20A-EXT-1339`.

## Disposition

- 2 `reviewed_relay_candidate`: COL5A1-SDC3 and COL5A2-DDR1.
- 6 `reviewed_binding_only`: COL5A1-alpha10beta1, COL5A1-alpha1beta1, COL5A1-alpha2beta1, COL5A2-alpha10beta1, COL5A2-alpha1beta1, and COL5A2-alpha2beta1.
- 17 `reviewed_unresolved`: all COL4A4/COL4A5/COL4A6 rows, COL5A1/COL5A2-alpha11beta1, all COL5A3 rows, COL6A1-ITGA6, and both COL7A1 rows.
- No terminal TF assignments were made. The reviewed positives end at adhesion, receptor-proximal ERK/DDR1/Shc/MAPK, or matrix-remodeling outputs; no exact TF endpoint was validated.

## Evidence notes

- COL5A1-SDC3 is supported by primary Schwann-cell adhesion work using a recombinant type-V collagen N-terminal domain, heparin inhibition, SDC3 affinity capture, cytoskeletal assembly, tyrosine phosphorylation, and ERK1/2 activation. The historical alpha4(V) nomenclature and queue/HPRD mapping to COL5A1 are recorded as a limitation.
- COL5A2-DDR1 is supported by primary DDR collagen-receptor studies and the experimentally validated COL5A2-DDR1 record in ConnectomeDB. Collagen-V-family binding and DDR1 phosphorylation/Shc docking were retained as a receptor-proximal relay, while the original assays were not treated as a unique isolated COL5A2 motif assay.
- Collagen-V alpha10beta1, alpha1beta1, and alpha2beta1 rows retain direct subtype-binding or adhesion evidence from recombinant integrin-domain and cell-blocking assays. The alpha1(V)/alpha2(V) chain-specific behavior in the primary collagen-V study was preserved, but no unmeasured intracellular relay or TF was inferred.
- COL5A3 integrin/SDC3 rows remain unresolved because the positive collagen-V studies used native type-V preparations or alpha1(V)/alpha2(V) chains, not isolated alpha3(V)/COL5A3.
- COL4A4/COL4A5/COL4A6 rows remain unresolved because the closest direct CD47 and beta3 evidence is specific to the alpha3(IV) NC1 domain; it was not transferred to the alpha3alpha4alpha5 or alpha5alpha5alpha6 networks. No exact CD93 interaction was recovered.
- COL6A1-ITGA6 remains unresolved because collagen-VI receptor studies identify other collagen-binding integrins, while ITGA6 expression does not establish a direct COL6A1-alpha6beta1 edge. COL7A1 rows remain unresolved because the direct collagen-VII study identified alpha2beta1, not alpha10beta1 or alpha11beta1.

## Search boundary and controls

Searches covered exact gene/receptor queries across PubMed, PMC, publisher pages, Reactome, and pathway/interaction resources, with primary research prioritized. Family-level collagen-receptor evidence was retained only as a bounded citation or limitation and was not used to infer an exact chain-specific interaction. Receptor complexes were kept intact: `Itga10_Itgb1`, `Itga11_Itgb1`, `Itga1_Itgb1`, and `Itga2_Itgb1` were not split into standalone receptor claims. No pathway or functional observation was converted into a direct molecular edge, and no terminal TF was assigned.

## Validation

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines; terminal TF is `null` for every row.
- This batch writes only `module21a_batch113_review.tsv` and `module21a_batch113_summary.md`; shared registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
