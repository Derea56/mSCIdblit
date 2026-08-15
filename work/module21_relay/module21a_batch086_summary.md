# Module 21A batch 086 review summary

Batch 086 covers the exact filtered priority-8 queue ordinal rows 1451–1475, review IDs `M20A-CELLCHAT-REMAINING-1596` through `-1620`.

## Disposition

- 15 `reviewed_relay_candidate`
  - PPY–NPY4R
  - pregnenolone–NR1I2/PXR
  - Prnp–ADGRG6/GPR126
  - PROC–PROCR/F2R and PROC–PROCR/HSP90AA1
  - all eight progesterone–CatSper complex rows
  - PTPRS–NTRK3
  - PVR–CD226
- 3 `reviewed_binding_only`
  - PPY–NPY6R/PP2-family binding
  - PTPRC/CD45–CD22 glycan-dependent recognition
  - PTPRM homophilic adhesion
- 7 `reviewed_unresolved`
  - PPY–PGR15L
  - all five exact Prss3l–PAR/PARD3 rows
  - PTPRC–MRC1
- 0 `reviewed_function_only`
- 1 terminal-TF assignment: `NR1I2/PXR` for the direct pregnenolone-to-PXR branch.

## Evidence handling

The NPY4R record has structural PP-bound Gi1 evidence. The NPY6R-family record has mouse PP binding but no matched proximal second-messenger assay; human NPY6R functional status remains a species boundary. PGR15L remains unresolved because no direct PPY assay was located.

Pregnenolone is treated as the mature steroid ligand and CYP11A1 as source-processing context. The original PXR work supports pregnenolone-family steroid activation of NR1I2/PXR, which is itself a ligand-activated transcription factor; this is kept distinct from CYP11A1 catalysis.

Prnp–ADGRG6 is supported by direct PrP flexible-tail binding/agonism, cAMP assays, receptor deletion, and Schwann-cell myelination outputs. For PROC, the PROCR/F2R row records activated-protein-C-dependent EPCR/PAR1 cleavage and signaling, while the PROCR/HSP90AA1 row records ligand-stimulated cytoplasmic complex formation in mammary stem cells. The source-processing or zymogen labels were not promoted as direct receptor components.

The eight progesterone–CatSper rows are deliberately represented as assembled-channel receptor-proximal relay evidence. Human sperm patch-clamp and CatSper loss-of-function work establish progesterone-sensitive CatSper currents and the requirement for channel subunits, but do not establish a direct progesterone contact with each submitted alpha/auxiliary subunit pair. HSD3B1 is source-processing context only, and no terminal TF is inferred.

PRSS3L is the exact mouse queued source. Human PRSS3/mesotrypsin PAR studies, including conflicting PAR1/PAR2 context, were not transferred to Prss3l. PARD3 was kept separate from PAR3/F2RL2. PTPRC–CD22 is retained as glycan-dependent binding with context-dependent CD45 contribution, not as a PTPRC-specific downstream relay. PTPRC–MRC1 has no validated exact-pair evidence. PTPRM homophilic binding and PTPRS–NTRK3 transsynaptic organization are kept distinct from unrelated RPTP family members.

## Search boundary and validation

The bounded search covered PubMed, PMC, publisher/DOI pages, Reactome for the PTPRS–NTRK3 pathway annotation, and stable gene records for exact source-identity checks. Primary binding, structural, electrophysiology, genetic perturbation, and receptor-proximal studies were prioritized. Family-level, co-expression, inferred CellChat, and source-enzyme evidence was not used to manufacture exact molecular edges.

- 25 rows written, one per requested review ID.
- Required 13-column schema present.
- Review IDs are unique and match the exact filtered queue slice.
- No shared registers, Module20A ledgers, frozen manifest, or integration outputs were modified.
- Batch remains isolated and is not integrated into the Module 21A registers.
