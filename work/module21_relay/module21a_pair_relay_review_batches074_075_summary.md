# Module 21A pair relay review batches 074–075

- Scope: 64 exact queue IDs from the filtered priority-8 slice: batch 074 IDs 1243–1281 (39 rows) and batch 075 IDs 1282–1329 (25 rows). Explicit review IDs, rather than raw physical line numbers, were authoritative.
- Batch 074 outcomes: 25 receptor-proximal relay candidates, 1 binding-only, 4 function-only, and 9 unresolved.
- Batch 075 outcomes: 16 receptor-proximal relay candidates, 5 binding-only, and 4 unresolved.
- Terminal TF candidates were retained only where the exact receptor complex and downstream pathway were supported: type I/III interferon STAT1/STAT2/IRF9, cytokine STAT branches, and insulin-receptor FOXO1/CREB, with source/isoform and receptor-complex limitations recorded in the raw TSV.
- Predicted, processed, or source-context labels were not treated as direct mature ligand/receptor edges.
- Stable citations, species/model, assay or perturbation, relation type, evidence layer, pathway branch, confidence, and limitations were retained in the detail register.
- Frozen Module20A manifest and LR ledgers were not modified.

The raw review files are `module21a_batch074_review.tsv` and `module21a_batch075_review.tsv`. Integration followed exact queue-ID/pair-label and required-field validation.
