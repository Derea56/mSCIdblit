# Module 22A Pending Candidate Disposition

This ledger records the disposition of every pending Module 22A handoff
that remains unlinked after the high-confidence linkage audit. It is a
local-register review, not a claim that these candidates have no relevant
literature. Each row preserves the source handoff's search boundary and
limitation text so a future primary-source search can resume without
silently broadening the evidence gate.

## Review scope

- Pending handoffs before linkage: 274
- Handoffs represented by the linkage audit: 105 (103 were pending handoffs)
- Unlinked pending handoffs reviewed here: 171
- Distinct local evidence packets represented: 156
- Evidence-packet mapping completeness: 100% (no candidate lacked a local packet)
- Disposition for every row: `not_promoted_under_current_strict_gate`

The strict gate requires an exact handoff-to-22B match, an exportable
high-confidence 22B edge, and exportable high-confidence evidence or a
reviewed primary extraction. No row below satisfied all three conditions
in the current register. The tags are lexical summaries of observed local
boundary/limitation text; multiple tags may apply to one row.

## Blocker-tag counts

| Tag | Rows |
|---|---:|
| `exact_pair_or_family_review_required` | 147 |
| `ligand_or_family_specificity_boundary` | 53 |
| `model_or_context_boundary` | 100 |
| `molecular_form_boundary` | 1 |
| `program_or_function_level_boundary` | 36 |
| `receptor_or_composite_boundary` | 77 |
| `tf_or_target_assignment_unresolved` | 61 |

## Source-packet confidence counts

These counts summarize the confidence field already recorded in the
Module 21A evidence-detail register; they are not new confidence calls.

| Recorded source confidence | Rows |
|---|---:|
| `high` | 93 |
| `low` | 16 |
| `low-medium` | 1 |
| `medium` | 40 |
| `medium-high` | 21 |

## Candidate ledger

The complete machine-readable ledger is [the TSV disposition file](../work/module22a_22b_promotion_audit/module22a_pending_candidate_dispositions.tsv). The table below lists every candidate and its local blocker tags; the TSV retains the full boundary and limitation text.

| Handoff | Pair | Terminal TF field | Blocker tags |
|---|---|---|---|
| M22A-HANDOFF-000003 | 22HC-CYP11A1 Nr1h4 | NR1H4 (FXR) | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000184 | Aldo-CYP11B2 Nr3c2 | NR3C2 | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000185 | Amh AMHR2_ACVR1 | SMAD1;SMAD5;SMAD8 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000186 | Androstenedione-CYP17A1 Ar | AR | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000215 | Bmp8a Bmpr1b_acvr2a | SMAD1/5/8;SMAD4 candidates | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-000217 | Bmp8b Acvr1_acvr2a | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000219 | Bmp8b Acvr1_bmpr2 | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000220 | Bmp8b Bmpr1a_acvr2a | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000221 | Bmp8b Bmpr1a_acvr2b | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000222 | Bmp8b Bmpr1a_bmpr2 | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000223 | Bmp8b Bmpr1b_acvr2a | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000224 | Bmp8b Bmpr1b_acvr2b | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000225 | Bmp8b Bmpr1b_bmpr2 | SMAD1/5/8;SMAD2/3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000227 | Btc Egfr | AP-1;ELK1 candidates | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-000228 | Btc Erbb4 | AP-1;ELK1 candidates | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-000326 | CGA_TSHB Tshr | ATF2 | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000327 | Cholesterol-CEL Rora | RORA | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000328 | Cholesterol-CEL Rorc | RORC | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000329 | Cholesterol-DHCR7 Rora | RORA | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000333 | Clcf1 CNTFR_LIFR | STAT3 | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000379 | Cort-CYP11B1 Nr3c1 | NR3C1 | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000380 | Cort-CYP11B1 Nr3c2 | NR3C2 | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000441 | E2-CYP19A1 Esr2 | ESR2 | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000445 | E2-HSD17B1 Esr2 | ESR2 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000481 | GABA-GAD1_SLC32A1 Gabbr1 | CREB | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000482 | GABA-GAD1_SLC32A1 Gabbr2 | CREB | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000498 | GABA-GAD1_SLC6A1 Gabbr1 | CREB | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000499 | GABA-GAD1_SLC6A1 Gabbr2 | CREB | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000726 | Gdf11 Tgfbr1_acvr2b | SMAD2/3 candidate | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-000731 | Gdf5 Bmpr1b_acvr2a | SMAD1/5/8 candidate | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001297 | IL23 complex IL23R_IL12RB1 | STAT3;STAT4 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001317 | Inhbb Acvr1b_acvr2a | SMAD2;SMAD3 | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001318 | Inhbb Acvr1b_acvr2b | SMAD2;SMAD3 | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001319 | Inhbb Acvr1c_acvr2a | SMAD2;SMAD3 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001320 | Inhbb Acvr1c_acvr2b | SMAD2;SMAD3 | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001407 | Mstn Tgfbr1_acvr2a | SMAD2;SMAD3 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001599 | Pregnenolone-CYP11A1 Nr1i2 | NR1I2/PXR | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001646 | RA-ALDH1A3 RARA_RXRA_CRABP2 | RARA | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001647 | RA-ALDH1A3 RARB_CRABP2 | RARB | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001648 | RA-ALDH1A3 RARB_RXRB_CRABP2 | RARB | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001649 | RA-ALDH1A3 RARG_CRABP2 | RARG | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001650 | RA-ALDH1A3 RARG_RXRG_CRABP2 | RARG | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001651 | RA-ALDH1A3 Rorb | RORB | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001708 | T3-DIO3 Thra | THRA | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001709 | T3-DIO3 Thrb | THRB | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001733 | Testosterone-AKR1D1 Ar | AR | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001734 | Testosterone-HSD17B12 Ar | AR | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001735 | Testosterone-HSD17B3 Ar | AR | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001770 | Wnt5b Fzd3 | ATF2 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001796 | Wnt5a Mcam | JUN/AP-1 candidate | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-001798 | Amh AMHR2_BMPR1B | SMAD1/5/9;SMAD4 candidate | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary` |
| M22A-HANDOFF-001801 | Artn GFRA3_RET | ELK1/AP-1 candidates | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-001803 | Bmp10 ACVRL1_ACVR2A | SMAD1/5/9;SMAD4 candidates | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001804 | Bmp10 ACVRL1_BMPR2 | SMAD1/5/9;SMAD4 candidates | `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-001805 | Bmp15 BMPR1B_BMPR2 | SMAD1/5/8;SMAD4 candidates | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary` |
| M22A-HANDOFF-001821 | Bmp5 BMPR1A_ACVR2A | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001822 | Bmp5 BMPR1A_ACVR2B | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001823 | Bmp5 BMPR1A_BMPR2 | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001824 | Bmp5 BMPR1B_ACVR2A | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001825 | Bmp5 BMPR1B_ACVR2B | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001826 | Bmp5 BMPR1B_BMPR2 | SMAD1/5/8;SMAD4 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001835 | Btc EGFR_ERBB2 | AP-1;ELK1 candidates | `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-001865 | Fgf15 Fgfr4 | FOXO1 candidate | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001873 | Fgf18 Fgfr2 | ETV4/ETV5 candidates | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001874 | Fgf18 Fgfr4 | ETV4/ETV5 candidates | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001881 | Fgf21 Fgfr1 | EGR1; c-FOS candidates | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001884 | Fgf23 Fgfr1 | EGR1 candidate | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001890 | Fgf5 Fgfr1 | CREB; c-FOS; STAT3 candidates | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-001897 | Fgf6 Fgfr4 | MyoD; myogenin candidates | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-001906 | Ifna9 IFNAR1_IFNAR2 | STAT1/2; IRF9 candidates | `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001907 | Ifnab IFNAR1_IFNAR2 | STAT1/2; IRF9 candidates | `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001909 | Ifne IFNAR1_IFNAR2 | STAT/ISGF3 candidates | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001910 | Ifng IFNGR1_IFNGR2 | STAT1 candidate | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001911 | Ifnk IFNAR1_IFNAR2 | STAT/ISGF3 candidates | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-001921 | Wnt5a Fzd6 | beta-catenin candidate | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `model_or_context_boundary` |
| M22A-HANDOFF-001922 | Agrn Dag1 | SOX9 candidate | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `model_or_context_boundary` |
| M22A-HANDOFF-001927 | Col1a1 Cd44 | STAT3 candidate | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-002112 | Dmp1 ITGAV_ITGB3 | c-Jun | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary` |
| M22A-HANDOFF-002154 | Lama3 ITGA6_ITGB4 | NF-kB p65 candidate | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-002171 | Lama5 ITGA6_ITGB1 | TAZ; TEAD candidates | `tf_or_target_assignment_unresolved`; `model_or_context_boundary` |
| M22A-HANDOFF-002199 | Lamb3 ITGA6_ITGB4 | NF-kB p65 candidate | `receptor_or_composite_boundary`; `tf_or_target_assignment_unresolved` |
| M22A-HANDOFF-002326 | Dspp ITGAV_ITGB1 | ELK1 | `tf_or_target_assignment_unresolved`; `molecular_form_boundary` |
| M22A-HANDOFF-002544 | Amh Acvr1_Amhr2 | SMAD1;SMAD5;SMAD8 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-002565 | Angptl4 Cdh11 | CTNNB1 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-002684 | B2m Hfe | HIF1A | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-002960 | Clcf1_Crlf1 Cntfr_Il6st | STAT3 | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-002974 | Cntf Il6ra | STAT3 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003269 | Ecm1 Itgb4 | SOX2 | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003306 | Efna4 Epha10 | NANOG | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003348 | Epo Ephb4 | STAT3 | `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003389 | Fam3c Lifr | STAT3 | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003401 | Fbn1 Itgb6 | SMAD3 | `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003527 | Gast Cckbr | CREB | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003540 | Gdf10 Bmpr2 | SMAD1;SMAD5;SMAD8 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003707 | Gpc3 Cd81 | HHEX | `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003852 | Icam1 Egfr | STAT3 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003912 | Il12b_Il23a Il12rb1_Il23r | STAT3;STAT4 | `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003963 | Il20 Il20rb_Il22ra1 | STAT3 | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-003980 | Il4 Il13ra2_Il4ra | STAT6 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004133 | Lgals8 Itga3 | STAT1 | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004225 | Mdk Notch2 | STAT3 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004232 | Mdk Tspan1 | STAT1A | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004248 | Mif Egfr | JUN | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004267 | Mmp9 Tlr9 | RELA | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004273 | Mst1 Mst1r | STAT1;RELA | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004275 | Mstn ACVR1B_ACVR2B | SMAD2;SMAD3 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004277 | Mstn Acvr2b_Tgfbr1 | SMAD2;SMAD3 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004337 | Nodal ACVR1C_ACVR2A_CFC1 | SMAD2;SMAD3 | `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004338 | Nodal Acvr1c_Acvr2b | SMAD2;SMAD3 | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004502 | Pglyrp1 Trem1 | STAT3 | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004584 | Prlh Prlhr | CREB | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004595 | Pros1 Axl | RELA | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004611 | Psen1 Notch1 | RBPJ/CSL | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004612 | Psen1 Notch2 | RBPJ/CSL | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004613 | Psen1 Notch3 | RBPJ/CSL | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004614 | Psen1 Notch4 | RBPJ/CSL | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004629 | Pth Lrp6 | CTNNB1 | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004642 | Pth2 Pth2r | SOX9 | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004666 | Ptn Ptprz1 | ERF | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004706 | Rln1 Rxfp1 | CREB | `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004728 | Rspo1 Lgr4 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004729 | Rspo1 Lgr5 | TCF/LEF family | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004730 | Rspo1 Lgr6 | TCF/LEF family | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004731 | Rspo1 Lrp6 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004732 | Rspo1 Rnf43 | TCF/LEF family | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004733 | Rspo1 Znrf3 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004734 | Rspo2 Lgr4 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004735 | Rspo2 Lgr5 | TCF/LEF family | `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004737 | Rspo2 Rnf43 | TCF/LEF family | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004738 | Rspo2 Znrf3 | TCF/LEF family | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004739 | Rspo3 Lgr4 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004740 | Rspo3 Lgr5 | TCF/LEF family | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004743 | Rspo3 Rnf43 | TCF/LEF family | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004745 | Rspo3 Znrf3 | TCF/LEF family | `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004751 | Rspo4 Rnf43 | TCF/LEF family | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004752 | Rspo4 Znrf3 | TCF/LEF family | `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004764 | S100a1 Tlr4 | RELA | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004790 | Saa2 Fpr2 | EGR1 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004853 | Sema3g NRP2_PLXNA1 | MYC;YAP | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004861 | Sema4a Plxnd1 | TBX21; GATA3; RORC | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004899 | Sfrp2 Fzd5 | NFATC3 | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004911 | Shh Cdon | GLI1 | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004915 | Shh Hhip | GLI1 | `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004919 | Shh Scube2 | GLI1 (provisional) | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004944 | Slurp1 Chrna7 | RELA (provisional) | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004953 | Sost Lrp4 | TCF/LEF family (provisional) | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004954 | Sost Lrp5 | TCF/LEF family (provisional) | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004955 | Sost Lrp6 | TCF/LEF family (provisional) | `tf_or_target_assignment_unresolved`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004966 | Spon2 Itgam | RELA (provisional) | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-004967 | Spon2 Itgb2 | RELA (provisional) | `receptor_or_composite_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005068 | Thbs2 Notch3 | HES1;HES5 (provisional) | `ligand_or_family_specificity_boundary`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005098 | Tnf Notch1 | RELA | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005130 | Tpsb2 F2rl1 | BCL6 | `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005172 | Ucn2 Crhr2 | FOS (provisional) | `ligand_or_family_specificity_boundary`; `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005191 | Vcan Tlr2 | RelB | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005275 | Wnt5a Ptk7 | AP-1 (provisional) | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005277 | Wnt5a Ror1 | CREB (provisional) | `tf_or_target_assignment_unresolved`; `program_or_function_level_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005299 | Wnt7a Reck | TCF/LEF family (provisional) | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005311 | Bdnf Ngfr | JUN | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005319 | Bmp8a Acvr1_acvr2a | SMAD1;SMAD5;SMAD9 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005321 | Bmp8a Acvr1_bmpr2 | SMAD1;SMAD5;SMAD9 | `ligand_or_family_specificity_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005378 | Dll4 Notch1 | HES1;HEY1 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005381 | Edil3 Itgb3 | RUNX2 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005450 | Gdf5 Bmpr1b_bmpr2 | HES5 (provisional) | `tf_or_target_assignment_unresolved`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005508 | Retn Tlr4 | RELA/p65 | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005509 | Rspo1 Fzd8 | TCF/LEF family | `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005510 | Rspo3 Fzd8 | TCF/LEF family | `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005512 | S100a8 Tlr4 | RELA/p65 | `receptor_or_composite_boundary`; `model_or_context_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005514 | S100a9 Tlr4 | RELA/p65 | `receptor_or_composite_boundary`; `ligand_or_family_specificity_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005516 | Saa1 Tlr2 | RELA/p65 | `receptor_or_composite_boundary`; `exact_pair_or_family_review_required` |
| M22A-HANDOFF-005525 | Sema6a Plxna2 | NFATC1 (RANKL-coupled osteoclast model) | `model_or_context_boundary`; `exact_pair_or_family_review_required` |
