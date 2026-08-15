# Module 21A pair relay review batches 090–091

- Scope: exact filtered priority-8 queue rows 1551–1600, 50 ligand/receptor-pair rows.
- Batch 090 outcomes: 5 receptor-proximal relay candidates, 3 function-only, 1 binding-only, and 16 unresolved; direct T3–THRA/THRB nuclear-receptor endpoints were retained.
- Batch 091 outcomes: 11 receptor-proximal relay candidates, 2 function-only, 5 binding-only, and 7 unresolved; AR assignments for testosterone rows and STAT5A/STAT5B for TSLP–IL7R/CRLF2 were retained where exact receptor-pathway evidence supported them.
- Source-processing labels (DIO3, steroid enzymes, TBXAS1, and related context) were not treated as direct receptor components.
- Teneurin/latrophilin adhesion, nicotinic channels, TAM receptors, thromboxane, NKG2D, and cytokine pathways remained distinct.
- Six batch 091 records were schema-corrected and re-integrated after an omitted assay-column shift; required fields now pass validation.
- Frozen Module20A manifest and LR ledgers were not modified.

The raw review files are `module21a_batch090_review.tsv` and `module21a_batch091_review.tsv`. Integration followed exact queue-ID/pair-label and required-field validation.
