# Module 21A batch 078 review summary

## Scope

Reviewed exactly the filtered priority-8 queue ordinal rows 1251–1275 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. The 25 selected rows are review IDs `M20A-CELLCHAT-REMAINING-1383` through `M20A-CELLCHAT-REMAINING-1406`, plus `M20A-CELLCHAT-REMAINING-1409`; IDs 1407–1408 are not present in this filtered ordinal slice. The review covers LTE4/CysLT receptor rows, LXA4/FPR-family rows, MAdCAM1–α4β7, MAG and MPZ self-association, melatonin receptors, MIF–CD74/CD44, MPZL1 self-association, and norepinephrine–α1A.

Searches covered PubMed, PMC, publisher pages, and exact-symbol boundary searches. Stable PMIDs, PMCID, DOIs, and bounded PubMed query URLs are retained in the TSV. DPEP1/2/3, ALOX5/12, ASMT, DBH, and SLC18A1 were treated as biosynthetic, processing, or transport context rather than mature receptor-active ligands.

## Disposition

| Disposition | Count | Main result |
|---|---:|---|
| `reviewed_relay_candidate` | 12 | LTE4–CYSLTR1/2, LXA4–FPR2/ALX, MAdCAM1–α4β7, melatonin–MT1/MT2, MIF–CD74/CD44, and norepinephrine–ADRA1A. |
| `reviewed_binding_only` | 3 | MAG homodimerization, MPZ homophilic adhesion, and MPZL1 extracellular homodimerization. |
| `reviewed_function_only` | 0 | No unanchored functional result was promoted. |
| `reviewed_unresolved` | 10 | LXA4 at Fpr-rs3/4/6/7 and FPR3 across ALOX12/ALOX5 context rows. |

## Accuracy boundaries retained

- LTE4 was treated as the mature ligand. DPEP1/2/3 were retained only as leukotriene-processing context. CYSLTR2 support comes from receptor pharmacology showing LTE4 potency in calcium mobilization; CYSLTR1 support comes from LTE4-induced ILC2 responses inhibited by montelukast.
- LXA4 was promoted only for FPR2/ALX. FPR-RS3/4/6/7 and FPR3 were left unresolved because FPR2 family biology was not transferred to untested exact subtypes. ALOX5/12 were retained as biosynthetic context.
- MAdCAM1–α4β7 was kept as an integrin receptor-complex edge, with outside-in FAK/paxillin signaling distinct from endothelial cytokine induction of MAdCAM1.
- MAG, MPZ, and MPZL1 self-pairs were kept distinct from heterophilic or carbohydrate-mediated interactions. Direct self-association was recorded, but no canonical receptor-proximal kinase or terminal TF was inferred for the binding-only rows.
- Melatonin–MTNR1A/B retained receptor-specific Gi/o and Gq/11-to-ERK branches. ASMT is a melatonin-biosynthesis enzyme and was not treated as a ligand. Target-gene induction was not promoted to a terminal TF.
- MIF–CD74/CD44 was represented as a receptor complex requiring CD44 for Src-dependent ERK signaling; MIF–CD74/CXCR4 was not merged into this exact pair.
- NE-DBH_SLC18A1–ADRA1A was represented using mature norepinephrine. DBH and SLC18A1 were kept as synthesis/vesicular transport context, and generic adrenergic TF reporter findings were not transferred.

## Validation

- 25 rows written; all rows have the required 13 columns.
- Review IDs are unique and all evidence fields are populated.
- Exact filtered queue IDs and canonical pair labels match the requested ordinal slice.
- No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.

## Files changed

- `work/module21_relay/module21a_batch078_review.tsv`
- `work/module21_relay/module21a_batch078_summary.md`

This batch remains isolated and ready for validation/approval before integration.
