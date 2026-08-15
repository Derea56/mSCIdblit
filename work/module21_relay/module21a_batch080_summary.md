# Module 21A batch 080 review summary

Batch 080 covers the exact filtered priority-8 queue ordinal slice 1301–1325, review IDs `M20A-CELLCHAT-REMAINING-1435` through `M20A-CELLCHAT-REMAINING-1459`.

## Disposition

- 25/25 exact queue IDs and canonical pair labels reviewed.
- 12 `reviewed_relay_candidate` rows: ADRB3, NODAL/ACVR1C–ACVR2B–CFC1, NPR1, NPY4R, NRG1 ERBB2/3, NRG1 ERBB2/4, NRG1 ERBB4, NRG1 ITGA6/ITGB4, NRG1 ITGAV/ITGB3, NRG2 ERBB3, NRG2 ERBB4, and NRG3 ERBB4.
- 9 `reviewed_binding_only` rows: NECTIN1–CD96, NECTIN1–NECTIN3, NECTIN1–NECTIN4, NECTIN2–CD226, NECTIN2–TIGIT, NECTIN3–NECTIN2, NECTIN3–PVR, NEGR1 self-binding, and NRG1–ERBB3.
- 4 `reviewed_unresolved` rows: NECTIN1–CADM3, NECTIN3–TIGIT, NPY–NPY6R, and NPY–PGR15L.
- 1 terminal-TF candidate: FOXH1 for the NODAL–ACVR1C/ACVR2B/CFC1 receptor-complex branch. No generic NRG/ErbB, Nectin, adrenergic, NPR1, or NPY TF was promoted.

## Evidence boundaries

- Nectin rows were kept as direct adhesion or immune-receptor binding records unless the exact pair had a pair-specific intracellular assay. Nectin3–TIGIT remains unresolved because primary recognition work supports TIGIT binding to PVR and Nectin2 but not Nectin3. Nectin1–CADM3 was not promoted from family-level or integrated interaction annotations.
- NODAL was retained as a receptor-complex/pathway edge, not a binary ACVR1C-only edge. The evidence supports CFC1/Cripto-assisted ACVR2B–ACVR1C/ALK7 signaling and a SMAD2/3–SMAD4/FoxH1 transcriptional branch; FOXH1 is supported by direct Nodal pathway and chromatin/developmental studies.
- NPPB–NPR1 was promoted to the receptor-proximal membrane-guanylyl-cyclase/cGMP branch with mouse sensory-circuit functional evidence and conserved human expression support.
- NPY–NPY4R was promoted from expression-cloning binding and cAMP/Ca2+ assays. NPY–NPY6R was not promoted because the matched primary physiology supports PP as the major Npy6r ligand and human NPY6R is a pseudogene. PGR15L was only localized as an orphan/ciliary GPCR; NPY2R/PYY3-36 experiments were not transferred to PGR15L.
- NRG1/2/3–ErbB records preserve receptor-complex and isoform boundaries. NRG1–ERBB3 is binding-only because complete relay requires a kinase-competent heterodimer partner. Integrin alpha6beta4 and alphaVbeta3 records retain the direct NRG1-integrin cross-talk evidence separately from canonical ErbB receptor complexes. No terminal TF was inferred from generic ErbB pathway biology.

## Primary-source coverage

Primary evidence included Nectin ectodomain and immune-receptor binding studies (PMIDs 12011057, 24116228, 23677581, 30759143), NEGR1 homophilic binding and aggregation (PMID 25057311), NODAL receptor/coreceptor and FoxH1/SMAD studies (PMIDs 12052855, 18089557, 11358868, 25359723), NPPB–NPR1 itch/cGMP work (PMID 31292265; PMCID PMC7218920), NPY4R expression cloning (DOI 10.1074/jbc.270.45.26762), NPY6R/PP boundary work (DOI 10.1016/j.cmet.2013.11.019), PGR15L ciliary localization (PMID 24316073), ErbB receptor-complex studies (PMIDs 9742126, 16203964, 16978839, 34759323, 16338790, 17945187, 9275162), and direct NRG1-integrin binding/cross-talk (PMID 20682778).

## Files and isolation

- Review TSV: `work/module21_relay/module21a_batch080_review.tsv`
- This summary: `work/module21_relay/module21a_batch080_summary.md`
- No shared Module 21A registers, coverage/handoff ledgers, Module20A files, frozen manifest, or integration outputs were modified.
