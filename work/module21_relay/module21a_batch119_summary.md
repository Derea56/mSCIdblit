# Module 21A batch 119 review

Batch 119 covers exactly the 25 requested rows `M20A-EXT-1655` through `M20A-EXT-1695`.

## Disposition

- 9 `reviewed_relay_candidate`: FGF13-SCN5A, FGF13-SCN8A, FGF15-KLB, FGF2-CD44, FGF2-ITGB3, FGF2-SDC1, FGF2-SDC2, FGF2-SDC4, and FGF7-NRP1.
- 3 `reviewed_binding_only`: FGF4-NRP1, FGFR3-EphA4, and FGFR4-EphA4.
- 1 `reviewed_function_only`: FGF23-PHEX.
- 12 `reviewed_unresolved`: FGF13-EGFR, FGF13-FGFR2, FGF13-FGFR3, FGF13-FGFR4, FGF14-FGFR2, FGF6-SDC4, FGF7-FGFR3, FGF7-FGFR4, FGFR4-PTPRR, FGFR4-TNFRSF10B, FGG-ITGA5, and FGG-ITGB1.

## Evidence notes

FGF13/14 were treated as fibroblast-growth-factor homologous factors with established intracellular channel biology. Direct FGF13 binding and functional modulation were supported for Nav1.5/SCN5A and Nav1.6/SCN8A, while the newer secretion study established recombinant FHF binding and signaling through FGFR1, not the exact EGFR, FGFR2, FGFR3, FGFR4, or FGF14-FGFR2 rows.

FGF15-KLB was retained as a receptor-complex/co-receptor relay in the FGF15-KLB-FGFR4 endocrine axis. FGF2-CD44, FGF2-ITGB3, and FGF2-SDC1/2/4 preserve heparan-sulfate or integrin receptor-complex identity; SDC1 and SDC2 evidence comes from grouped syndecan experiments and is not represented as a unique protein-core interface. FGF7-NRP1 is supported by NRP1 knockdown, co-immunoprecipitation and downstream ERK/p38/AKT/Rb assays in human adipose-derived stem cells. FGF4-NRP1 is retained as biochemical binding-only because the primary study did not establish a cellular FGF4-NRP1 relay.

FGF23-PHEX is functional-only: PHEX perturbation changes FGF23 expression and phosphate-homeostasis phenotypes, but multiple primary studies found no validated PHEX cleavage of intact FGF23. FGFR3/4-EphA4 are receptor-receptor cytoplasmic crosstalk edges, not ligand-receptor edges; exact FGFR3/4 downstream claims were therefore kept conservative. FGG-ITGA5/ITGB1 remain unresolved because primary fibrinogen mapping assigns endothelial alpha-5-beta-1 binding primarily to an A-alpha-chain RGD site rather than the FGG gamma chain.

## Search boundary and validation

Searches covered exact gene/protein pairs across PubMed, PMC, publisher pages, Reactome and pathway-resource comparators, with primary research prioritized. Family-level FGF receptor specificity, expression/co-occurrence, grouped proteoglycan annotations, receptor-family crosstalk, and whole-fibrinogen binding were not promoted to unsupported exact molecular edges. No terminal transcription factor was assigned in this batch.

- Exactly 25 data rows and 13 tab-delimited columns.
- Review IDs and pair labels match the requested exact batch.
- Fields contain no embedded tabs or newlines.
- Only `module21a_batch119_review.tsv` and `module21a_batch119_summary.md` were written; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.
