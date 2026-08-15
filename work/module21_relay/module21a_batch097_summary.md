# Module 21A batch 097 review

Reviewed the exact filtered priority-8 queue ordinal slice 1726–1750 from `module20a_external_review_queue.tsv`. The slice contains 25 rows with IDs `M20A-EXT-0807` through `M20A-EXT-0839` and the explicit gaps present in the source queue. The requested apolipoprotein and apelin families were kept as exact submitted pairs; no rows were substituted from adjacent queue ordinals.

## Disposition

- 25 exact queue rows reviewed and matched to the source IDs/pairs.
- 2 `reviewed_relay_candidate`: APOB–ENO1 and APOB–TLR4.
- 2 `reviewed_binding_only`: APOB–OLR1, limited to modified apoB-containing LDL/LOX-1 recognition, and APOB–MTTP, a direct intracellular VLDL-assembly association rather than a cell-surface receptor relay.
- 21 `reviewed_unresolved`: all APLN–ADRA2A/GRM7/MTNR1A rows; all APOA1/APOA2/APOA4 rows in this slice; and APOB–ADRB2, CALCR, GM5506, ITGAM, ITGB2, LRP2, LRP8, TLR6, VLDLR, and APOC2–LDLR.
- No terminal TF was promoted. NF-kB in APOB–ENO1 and the TLR4/MyD88/SYK/PI3K-AKT branch is retained as pathway-level evidence only; no direct TF-occupancy result was identified.

## Evidence boundaries

The strongest direct evidence was for APOB interacting with cell-surface ENO1 in rheumatoid-arthritis monocytes/PBMCs, with p38 MAPK and NF-kB-dependent cytokine output (PMID 29997113; DOI 10.1136/annrheumdis-2018-213444). Aggregated apoB-containing LDL activated a TLR4-dependent macrophage catabolic relay through MyD88, SYK, PI3K, and AKT in primary mouse macrophage models (PMID 31597445; PMCID PMC6928397). These are particle/context-specific findings: they do not establish free APOB as a universal TLR4 ligand.

LOX-1/OLR1 evidence was retained as binding-only because the primary literature concerns oxidized or otherwise modified apoB-containing LDL, not unmodified free APOB (PMID 9693095; PMCID PMC1219654). APOB–MTTP was retained separately as a direct intracellular assembly/transport association measured by co-immunoprecipitation in HepG2 cells (PMID 8626595); it is not a receptor-proximal relay.

The apelin rows remain unresolved because the primary apelin studies support APLNR/APJ, not ADRA2A, GRM7, or MTNR1A. The apolipoprotein receptor rows remain unresolved where the literature supports a different receptor or apolipoprotein: LDLR recognition is centered on apoB/apoE; apoA-II evidence recovered for SR-BI/CD36; apoA-IV hepatocyte uptake was assigned to a receptor distinct from apoB/E-dependent receptors; LRP8 evidence is for Reelin/apoE; and VLDLR Lp(a) uptake is mediated through the apo(a)-containing particle context. The search boundary was documented in each row with exact-pair PubMed queries where no qualifying primary record was found.

## Integrity checks

- TSV header has all 13 requested columns.
- 25 rows; review IDs unique; exact filtered queue IDs and pair labels match.
- Stable citations are recorded for every row; unresolved rows retain source/search boundaries rather than pathway inference.
- Module 20A ledgers, shared Module 21A registers, integration outputs, and frozen manifest were not modified.
- Frozen manifest SHA-256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

This batch remains isolated and is not integrated into the shared Module 21A registers.
