# Module 21A pair relay review batches 086–087

- Scope: exact filtered priority-8 queue rows 1451–1500, 50 ligand/receptor-pair rows.
- Batch 086 outcomes: 15 receptor-proximal relay candidates, 3 binding-only, and 7 unresolved; one NR1I2/PXR pathway candidate was retained for pregnenolone–NR1I2 with source-enzyme limitations.
- Batch 087 outcomes: 9 receptor-proximal relay candidates, 8 function-only retinoid receptor outputs, 1 binding-only, and 7 unresolved.
- Retinoid rows were corrected and revalidated after a five-row TSV field-separation defect; pathway, confidence, limitations, and terminal-TF fields now align with the declared schema.
- Source-processing labels (CYP11A1, ALDH1A1/2/3, PTGES-family enzymes, and related context) were not treated as direct receptor subunits or direct molecular edges.
- Stable citations, species/model, assay or perturbation, relation type, evidence layer, pathway branch, confidence, and limitations were retained in the detail register.
- Frozen Module20A manifest and LR ledgers were not modified.

The raw review files are `module21a_batch086_review.tsv` and `module21a_batch087_review.tsv`. Integration followed exact queue-ID/pair-label and required-field validation, including repair/revalidation of the malformed retinoid rows.
