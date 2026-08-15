# Module 21A evidence review — Batch 164

Batch 164 covers the exact 25 filtered queue rows at ordinals 3551–3575. The raw review is in [`module21a_batch164_review.tsv`](./module21a_batch164_review.tsv) and uses the exact 13-column schema:

`review_id`, `pair`, `status`, `stable_citations`, `species`, `cell_type_model`, `assay_or_perturbation`, `relation_type`, `evidence_layer`, `pathway_branch`, `confidence`, `limitations`, `terminal_TF`

## Review boundary

This is a bounded Module 21A relay review. Direct binding/activation, receptor-proximal relay, and downstream pathway/function were recorded as separate evidence layers. Computational ligand-receptor scores, co-expression, pathway membership, paralog evidence, and reverse-direction cytokine relationships were not promoted to direct exact-pair interactions. Every row has a populated limitations field. `terminal_TF=null` is used for the 23 rows without an assigned terminal TF; `RELA` is retained only for the two source-supported p65-mediated function rows, TNF–FAS and TNF–NOTCH1.

No Module20A file, shared register, integrated register, or other shared artifact was modified. No commit was made.

## Outcome summary

| Status | Count | Rows |
|---|---:|---|
| `reviewed_relay_candidate` | 6 | TLN1–ITGB3, TLN1–ITGB5, TNC–ITGA2, TNF–TRADD, TNF–TRAF2, TNFSF10–RIPK1 |
| `reviewed_function_only` | 7 | TIMP2–CD44, TNC–ITGA5, TNF–FAS, TNF–FLT4, TNF–NOTCH1, TNF–PTPRS, TNF–TRPM2 |
| `reviewed_unresolved` | 12 | THBS2–NOTCH4, TIMP1–FGFR2, TIMP3–CD44, TIMP3–DDR1, TIMP3–MET, TNC–PTPRB, TNF–CELSR2, TNF–FFAR2, TNF–ICOS, TNF–SEMA4C, TNF–TNFRSF21, TNFSF10–CCR6 |
| **Total** | **25** | Exact requested queue rows |

## Evidence-layer notes

- **Binding/activation:** TLN1–ITGB3 and TLN1–ITGB5 have direct talin-head/cytoplasmic integrin-tail evidence. TNC–ITGA2 has direct tenascin interaction evidence for the alpha2beta1 heterodimer in endothelial adhesion assays. These are intracellular adaptor-to-integrin or matrix-to-heterodimer results, not interchangeable extracellular ligand-receptor claims.
- **Receptor-proximal relay:** TNF–TRADD and TNF–TRAF2 are supported as TNF–TNFR1 complex relays through adaptor recruitment; neither TRADD nor TRAF2 was treated as a direct TNF-binding partner. TNFSF10–RIPK1 is retained as a downstream death-receptor-complex relay candidate, with the same direct-binding limitation.
- **Downstream pathway/function:** TIMP2–CD44, TNC–ITGA5, TNF–FAS, TNF–FLT4, TNF–NOTCH1, TNF–PTPRS, and TNF–TRPM2 retain indirect functional evidence only. For example, TIMP2 binds MT1-MMP while CD44 organizes MT1-MMP localization, and TNF-associated FLT4 biology is mediated through a VEGF-C/lymphangiogenic context rather than direct TNF–FLT4 activation.
- **Unresolved/no-evidence:** The unresolved rows preserve explicit no-evidence boundaries where the named pair was not supported by a qualifying primary exact-pair assay. Comparator papers were retained only to define the nearby canonical branch or explain why transfer would be invalid.

## Representative primary sources

- Direct talin–integrin-tail evidence: [PMID 10497155](https://pubmed.ncbi.nlm.nih.gov/10497155/), [PMID 22210111](https://pubmed.ncbi.nlm.nih.gov/22210111/), [PMCID PMC9234671](https://pmc.ncbi.nlm.nih.gov/articles/PMC9234671/).
- Tenascin–alpha2beta1 endothelial adhesion: [PMID 7693733](https://pubmed.ncbi.nlm.nih.gov/7693733/).
- TIMP2/CD44/MT1-MMP functional separation: [PMID 23984338](https://pubmed.ncbi.nlm.nih.gov/23984338/).
- TNF–FAS sensitization through NF-kB-mediated FAS induction: [PMID 30185788](https://pubmed.ncbi.nlm.nih.gov/30185788/).
- TNF–NOTCH1 inflammatory crosstalk: [PMID 31105691](https://pubmed.ncbi.nlm.nih.gov/31105691/).
- TNF–TRADD/TRAF2 receptor-complex relay: [PMID 7758105](https://pubmed.ncbi.nlm.nih.gov/7758105/), [PMID 8565075](https://pubmed.ncbi.nlm.nih.gov/8565075/), [PMID 10911999](https://pubmed.ncbi.nlm.nih.gov/10911999/).
- TNFSF10/TRAIL–RIPK1/JNK functional relay: [PMID 23051914](https://pubmed.ncbi.nlm.nih.gov/23051914/).

