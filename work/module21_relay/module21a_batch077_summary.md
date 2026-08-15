# Module 21A batch 077 review summary

## Scope

Reviewed exactly the filtered priority-8 queue ordinal rows 1226–1250 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. These map to review IDs `M20A-CELLCHAT-REMAINING-1358` through `M20A-CELLCHAT-REMAINING-1382` and contain the LGALS9/P4HB and LGALS9/PTPRC rows, LIF/LIFR-gp130, LPA/ADGRE5, SALM/LAR-RPTP, NGL/netrin-G, LRRTM4/PTPRS, LTα1β2/LTBR, and leukotriene source-processing rows.

Searches covered PubMed, PMC, publisher pages, Reactome, and exact-symbol boundary searches. Stable PMID, PMCID, DOI, Reactome, and query URLs are retained in the TSV. Source-processing labels LTA4H, LTC4S, GGT1, and DPEP1 were treated as biosynthetic/metabolic context; receptor activation was assigned only to the mature lipid ligand.

## Disposition

| Disposition | Count | Main result |
|---|---:|---|
| `reviewed_relay_candidate` | 20 | Exact LIFR-gp130, LPAR1-ADGRE5 heteromer, SALM/LAR-RPTP, NGL/netrin-G, LRRTM4/GPC4/PTPRS, LTBR-NF-κB, BLT, and CysLT receptor-complex/pathway edges. |
| `reviewed_binding_only` | 1 | LGALS9 binding to cell-surface P4HB/PDI with a cellular migration output, but no canonical receptor-proximal kinase relay. |
| `reviewed_function_only` | 0 | No row was promoted solely from an unanchored functional output. |
| `reviewed_unresolved` | 4 | LGALS9-PTPRC, LPAR2/3-ADGRE5, and LRRC4C-PTPRF exact-pair boundaries. |

Two rows contain directly measured TF-level endpoints: LIF/LIFR-gp130 to STAT3 and LTα1β2/LTBR to the canonical/noncanonical NF-κB branches (RELA and RELB). No TF was assigned to neuronal adhesion, BLT, or CysLT rows without exact receptor-pathway evidence.

## Accuracy boundaries retained

- LIF was assigned to the assembled LIFR-gp130 complex and JAK/STAT3 branch; the receptor token was not treated as an isolated LIFR-only edge.
- Only LPAR1/CD97 (ADGRE5) was promoted. The primary heteromerization study did not test LPAR2 or LPAR3, so those exact rows remain unresolved.
- LRFN4/5 (SALM3/5) and LRRC4B/NGL-3 interactions with LAR-RPTPs were kept as trans-synaptic adhesion/receptor-complex edges. No direct phosphatase substrate or terminal TF was inferred.
- LRRC4/NTNG2 and LRRC4C/NTNG1 were retained as distinct netrin-G branches. LRRC4C/PTPRF was not promoted from LRRC4B/PTPRF evidence.
- LRRTM4/PTPRS was represented as a GPC4/heparan-sulfate-dependent receptor-complex edge; the evidence does not support a simple binary LRRTM4-PTPRS molecular interaction.
- LTα1β2/LTBR canonical RelA/p50 and noncanonical RelB/p52 pathways were retained as distinct downstream branches.
- For leukotriene rows, LTA4H, LTC4S, GGT1, and DPEP1 are source-processing context only. The mature ligands LTB4, LTC4, LTD4, and LTE4 are the receptor-active species. LTE4/CysLT1 was marked as a weaker/partial-agonist branch.

## Validation

- 25 rows written; 13 columns present on every row.
- Exact filtered queue IDs and canonical pair labels match the requested ordinal slice.
- Review IDs are unique and all required evidence fields are populated.
- Frozen Module 20A LR release manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Files changed

- `work/module21_relay/module21a_batch077_review.tsv`
- `work/module21_relay/module21a_batch077_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified. This batch is isolated and ready for validation/approval before integration.
