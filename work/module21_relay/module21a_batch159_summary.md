# Module 21A Batch 159 review

Scope: exact filtered queue ordinals 3426–3450, 25 rows. The raw review is in [`module21a_batch159_review.tsv`](module21a_batch159_review.tsv). This batch was reviewed against primary research with stable PMID, PMCID, DOI, or article-URL locators. Module20A files and shared registers were read-only inputs; they were not modified, and no commit was made.

## Disposition

- 13 `reviewed_unresolved` rows: no exact pair-specific evidence or only indirect/family-level evidence.
- 4 `reviewed_function_only` rows: exact receptor or receptor-complex function is supported, but no complete intracellular relay was resolved.
- 1 `reviewed_relay_candidate` row: receptor-proximal SEMA6D–PLXNA1/TREM2/TYROBP–SYK evidence in human iPSC-derived microglia.
- 7 `reviewed_scavenging_only` rows: uptake, clearance, or complex internalization without assigning signaling.
- No terminal TF was assigned to the SEMA6D–TREM2/TYROBP row because the primary study did not provide a TF-specific output. TBX21, GATA3, and RORC are retained only for the separately assayed Sema4A–Plexin-D1 human CD4+ T-cell perturbation.

## Exact reviewed rows

| review_id | pair | status |
|---|---|---|
| M20A-EXT-3080 | Sema3g NRP2_PLXNA3 | reviewed_unresolved |
| M20A-EXT-3081 | Sema3g NRP2_PLXNA4 | reviewed_function_only |
| M20A-EXT-3082 | Sema4a NRP1_PLXNA1 | reviewed_unresolved |
| M20A-EXT-3083 | Sema4a NRP1_PLXNA2 | reviewed_unresolved |
| M20A-EXT-3084 | Sema4a NRP1_PLXNA3 | reviewed_unresolved |
| M20A-EXT-3085 | Sema4a NRP1_PLXNA4 | reviewed_unresolved |
| M20A-EXT-3086 | Sema4a Plxnd1 | reviewed_function_only |
| M20A-EXT-3087 | Sema4b Dcbld2 | reviewed_function_only |
| M20A-EXT-3093 | Sema4d Plxnb3 | reviewed_unresolved |
| M20A-EXT-3094 | Sema4f Nrp2 | reviewed_unresolved |
| M20A-EXT-3096 | Sema5a Plxna3 | reviewed_unresolved |
| M20A-EXT-3098 | Sema5b Plxna3 | reviewed_unresolved |
| M20A-EXT-3100 | Sema6d Kdr_Plxna1 | reviewed_function_only |
| M20A-EXT-3101 | Sema6d Plxna1_Trem2_Tyrobp | reviewed_relay_candidate |
| M20A-EXT-3104 | Serpina1a Lrp1 | reviewed_scavenging_only |
| M20A-EXT-3105 | Serpina1b Lrp1 | reviewed_scavenging_only |
| M20A-EXT-3106 | Serpina1c Lrp1 | reviewed_scavenging_only |
| M20A-EXT-3107 | Serpina1d Lrp1 | reviewed_scavenging_only |
| M20A-EXT-3108 | Serpina1e Lrp1 | reviewed_scavenging_only |
| M20A-EXT-3109 | Serpina7 Slc16a2 | reviewed_unresolved |
| M20A-EXT-3110 | Serpinc1 Gpc1 | reviewed_unresolved |
| M20A-EXT-3111 | Serpinc1 Lrp1 | reviewed_unresolved |
| M20A-EXT-3112 | Serpine1 Itgb5 | reviewed_unresolved |
| M20A-EXT-3114 | Serpine1 Lrp2 | reviewed_scavenging_only |
| M20A-EXT-3115 | Serpine1 Plaur | reviewed_scavenging_only |

## Evidence-layer boundary

Binding or receptor activation is recorded separately from receptor-proximal relay and downstream pathway/function. Family-level or neighboring-ligand evidence is not promoted to the requested exact pair. In particular:

- Sema3G supports an NRP2/PLXNA4 synaptic branch, while the tested PLXNA3 perturbation did not support the queued PLXNA3 edge. Primary source: [PMID 30685224](https://pubmed.ncbi.nlm.nih.gov/30685224/).
- Sema4A has direct binding and functional evidence for Plexin-D1, including a primary BIAcore binding assay and receptor perturbation; the same primary binding panel did not support Plexin-A or neuropilin binding. [PMID 17318185](https://pubmed.ncbi.nlm.nih.gov/17318185/). A separate human CD4+ T-cell Plexin-D1-neutralization study measured [TBX21/GATA3/RORC outputs](https://pubmed.ncbi.nlm.nih.gov/32971928/), which are not treated as evidence for the unresolved NRP1/Plexin-A rows.
- Sema6D–Plexin-A1 is supported in cardiac and neuronal systems, with VEGFR2/KDR as a region-specific associated receptor in the cardiac study. [PMID 14977921](https://pubmed.ncbi.nlm.nih.gov/14977921/). The SEMA6D–PLXNA1/TREM2/TYROBP row is supported at the receptor-proximal SYK/function layer in human iPSC-derived microglia, but no terminal TF was assigned. [PMCID PMC12766863](https://pmc.ncbi.nlm.nih.gov/articles/PMC12766863/).
- Sema5A/Sema5B and Plexin-A1/Plexin-A3 are jointly implicated in retinal and axon-fasciculation phenotypes, but the ligand and receptor subunits are not isolated in those experiments. [PMCID PMC3164552](https://pmc.ncbi.nlm.nih.gov/articles/PMC3164552/), [PMCID PMC10423052](https://pmc.ncbi.nlm.nih.gov/articles/PMC10423052/). Direct Sema5A binding evidence is for Plexin-B3, not Plexin-A3. [PMID 15218527](https://pubmed.ncbi.nlm.nih.gov/15218527/).
- LRP1 and LRP2 entries are limited to serpin/protease-complex uptake and degradation. The alpha1-antitrypsin LRP1 study tested complexes rather than native free serpin, [PMID 8626456](https://pubmed.ncbi.nlm.nih.gov/8626456/); the LRP2 studies tested uPA–PAI-1 complexes in renal and pulmonary models, [PMID 8344937](https://pubmed.ncbi.nlm.nih.gov/8344937/), [PMID 7673355](https://pubmed.ncbi.nlm.nih.gov/7673355/). These are scavenging layers, not signaling relays.
- The Serpine1–Plaur evidence is a uPA-bridged ternary complex with LRP-dependent uptake and uPAR recycling, not a demonstrated direct binary PAI-1–PLAUR signaling edge. [PMID 7510679](https://pubmed.ncbi.nlm.nih.gov/7510679/), [PMCID PMC1169872](https://pmc.ncbi.nlm.nih.gov/articles/PMC1169872/).
- Protein C–EPCR/PAR1, GPC1–VEGF/KDR, and SERPINA7/MCT8 hormone-carrier/transport observations remain separate comparator branches; they do not establish the queued Serpinc1–Gpc1, Serpinc1–Lrp1, or Serpina7–Slc16a2 pairs. [PMID 17823308](https://pubmed.ncbi.nlm.nih.gov/17823308/), [PMID 10196157](https://pubmed.ncbi.nlm.nih.gov/10196157/), [PMID 61964](https://pubmed.ncbi.nlm.nih.gov/61964/), [PMCID PMC2934670](https://pmc.ncbi.nlm.nih.gov/articles/PMC2934670/).

All unresolved/no-evidence and model limitations are populated in the TSV rather than being left implicit.
