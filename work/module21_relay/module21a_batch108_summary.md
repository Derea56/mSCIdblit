# Module 21A batch 108 review

Batch 108 covers the exact filtered priority-8 queue ordinal slice 2001–2025. The 25 TSV rows match review IDs `M20A-EXT-1144` through `M20A-EXT-1174`, preserving the queue's intervening ID gaps and exact pair labels.

## Disposition

- 10 `reviewed_relay_candidate`: CDH1–IGF1R, CDH1–PTPRM, CEACAM1–EGFR, CFC1–ACVR1B, CFC1–ACVR2A, CFH–ITGAM/Mac-1, CFP–NCR1/NKp46, CGA–FSHR, CGA–LHCGR, and CGA–TSHR.
- 0 `reviewed_binding_only`.
- 0 `reviewed_function_only`.
- 15 `reviewed_unresolved`.
- 2 terminal-TF handoffs: FOXH1 for the two CFC1-containing Nodal receptor-complex rows. These are pathway-complex endpoints, not direct CFC1-to-TF molecular edges.

## Evidence notes

- CDH1–IGF1R has direct association and receptor-facilitating evidence in preimplantation/trophectoderm and epithelial breast-cell systems, with context-dependent IGF1R/AKT survival effects.
- CDH1–PTPRM is a direct E-cadherin/PTPmu adhesion-complex association supported by co-immunoprecipitation, reconstitution, cytoplasmic-domain mapping and phosphorylation-dependent dissociation. CDH1–PTPRF was not promoted because LAR/PTPRF evidence is mediated through beta-catenin/cadherin complexes rather than a demonstrated direct E-cadherin contact.
- CEACAM1–EGFR is retained as a receptor-proximal regulatory edge: EGFR phosphorylates CEACAM1, and CEACAM1 can sequester Shc to modulate Ras/MAPK output. CEACAM2 was not substituted for CEACAM1, and CEACAM1–TIM-3 evidence was not transferred to CEACAM2–HAVCR2.
- CFC1 rows are explicitly receptor-complex edges. CFC1/Cryptic can participate in Nodal complexes with ACVR1B/ALK4 and type-II activin receptors, leading through SMAD2/3-SMAD4 and FOXH1. The ACVR2A row is not a claim of isolated CFC1–ACVR2A binary binding; recent purified co-receptor studies show weak or absent standalone type-II-receptor interaction, so the required Nodal/type-II/type-I complex context is preserved.
- CFH–ITGAM is supported as CFH binding to the ITGAM/ITGB2 Mac-1 complex with neutrophil adhesion and oxidative activation. CFP–NCR1 is supported by direct properdin/NKp46 binding, reporter activation and NCR1-dependent antibacterial protection.
- CGA–FSHR, CGA–LHCGR and CGA–TSHR are retained only as intact glycoprotein-hormone complex relays. The common alpha chain makes receptor contacts in the assembled heterodimer and can contribute to receptor activation, but free CGA alone is not treated as a standalone ligand. No CGA edge was inferred for ADCYAP1R1, ADRB2, ADRB3, GPR20, GPR84, PTH1R, RAMP2 or RAMP3.

## Search boundary

Searches covered exact pair queries and cognate-family boundaries across PubMed, PMC full text, publisher pages and receptor-complex literature. Primary research was preferred. For unresolved rows, the TSV records exact-pair search URLs plus the nearest relevant primary comparator where useful. Generic glycoprotein-hormone, GPCR, RAMP, adhesion, complement or family-level pathway evidence was not promoted to an exact direct edge. No Module 20A ledger, frozen manifest, shared Module 21A register or integration output was modified.

## Files changed

- `work/module21_relay/module21a_batch108_review.tsv`
- `work/module21_relay/module21a_batch108_summary.md`
