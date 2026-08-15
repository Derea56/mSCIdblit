# Module 21A Batch 200 review summary

Batch 200 reviews exactly the 25 supplied currently queued Module20A pairs using the established 13-column schema in `module21a_batch200_review.tsv`. Only this TSV and this summary are written by the batch; shared Module20A/21A ledgers and the frozen LR manifest are untouched.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 9 |
| `reviewed_function_only` | 6 |
| `reviewed_scavenging_only` | 8 |
| `reviewed_binding_only` | 2 |
| `reviewed_unresolved` | 2 |
| **total** | **27** |

## Evidence decisions

- ANGPTL4–ITGA5/ITGB1 and ANGPTL4–ITGAV/ITGB3 were retained as distinct integrin branches. The alpha5beta1 study supports Rac1/PAK activation and endothelial-junction disruption, while the alphaVbeta3 study supports VEGFR2/Src modulation and barrier stabilization. ANGPTL4–SDC4 remains unresolved because heparan-sulfate or syndecan-family evidence does not establish the submitted SDC4 core-protein edge.
- ANXA2–ROBO4 was promoted as a receptor-proximal relay candidate because direct association, Robo4-paxillin complex formation, ARF6 regulation, and endothelial-permeability outputs were measured. ANXA1–FPR1 was kept function-only: a recent primary study supports interaction and dendritic-cell/tumor outputs but does not define a purified receptor relay; FPR2 evidence was not transferred.
- APLN–APLNR and AVP–AVPR1A/AVPR1B were retained as GPCR relay candidates with receptor coupling, second-messenger, kinase, or receptor-dependent functional evidence. No terminal TF was assigned to the AVP rows; STAT3 was retained only for APOA1–ABCA1 because ABCA1-dependent STAT3 phosphorylation and its anti-inflammatory function were directly measured.
- APOA1–ABCA1 and APOA4–LRP1 were retained as transporter/receptor-complex relay records with their noncanonical biology stated explicitly. APOA1–ABCA1 supports JAK2/STAT3 plus lipid export; APOA4–LRP1 supports PI3K-AKT and adipocyte glucose uptake.
- APOB/APOE lipoprotein edges with LDLR, LRP6, LSR, SORL1, and VLDLR were kept as binding, endocytic, clearance, or lipidation functions rather than kinase pathways. APOB–LRP1 remains unresolved because LRP1 literature supports apoE- or lipase-associated remnants rather than isolated apoB/LDL binding. APOE–LRP4, APOE–LRP6, and APOE–LRP8 retain binding/function evidence without a direct receptor-specific kinase endpoint.
- APOB–TREM2 is binding-only, and APOE–TREM2 is function-only, preserving the TREM2-TYROBP receptor-complex context without inferring a SYK relay that was not measured for the exact ligand edge. APOE–SDC2 is binding-only because the strongest exact evidence uses apoE-bearing HBV material and does not isolate free apoE binding to the SDC2 core protein.

## Search boundary and validation

Searches covered exact ligand/receptor symbols and aliases across PubMed, PMC, publisher pages, and relevant receptor/pathway literature, prioritizing primary binding, perturbation, receptor-coupling, uptake, and functional studies. Reviews, expression-only observations, generic LDLR-family or syndecan-family annotations, comparator ligands, and pathway-only results were not promoted to direct exact-pair relay edges. Particle-associated apolipoprotein evidence is identified as such in the limitations.

Before any ledger integration, this packet must pass: 25 data rows; exact alignment to the supplied IDs and pair labels; unique review IDs and pair labels; exact 13-column schema; populated required fields; confidence vocabulary `high|medium-high|medium|medium-low|low`; and `terminal_TF` either an explicit endpoint or literal `null`. No Module20A or shared Module21A ledger files were modified.
