# Evidence review: batch 002 ranks 16–20

Reviewed 20 exact TFLink regulator–target–species pairs from `public_tf_evidence_collection_batch_002.tsv`.

## Outcome

- 20/20 remain `candidate_only` search leads.
- 0 exact primary pair citations.
- 0 exact corroborating pair citations.
- 0 pairs had defensible direct binding, downstream perturbation direction, target-cell evidence, or directly tested upstream relay evidence.
- 0 rows are exportable; no canonical files and no Module 22B records were changed.

`no_exact_pair_support_found_in_bounded_search` means that no qualifying exact regulator–target–species experiment was located in the bounded PubMed/PMC search. It is not a claim that no evidence exists anywhere.

## Pair-level review

All rows have the same pair-level evidence status:

| Rank | Regulator | Species | Queued targets | Exact pair status | Cell / binding / downstream / relay | Disposition |
|---:|---|---|---|---|---|---|
| 16 | ZNF792 | human | A2M, ACKR2, ACVR1, ADAM17 | no exact support | NE / NF / NF / NT | retain as search leads only |
| 17 | ASCL2 | human | ACKR2, ACKR3, ACTR2, ADA | no exact support | NE / NF / NF / NT | retain as search leads only |
| 18 | OSR2 | human | ACKR2, ACVR1, ADAM17, ADCYAP1 | no exact support | NE / NF / NF / NT | retain as search leads only |
| 19 | ZSCAN9 | human | A2M, ABCA1, ACKR2, ACVR1 | no exact support | NE / NF / NF / NT | retain as search leads only |
| 20 | ZBTB6 | human | ACKR2, ACVR1, ACVR1C, ADAM10 | no exact support | NE / NF / NF / NT | retain as search leads only |

Status legend: `NE` = target-cell presence not established for the exact pair; `NF` = exact binding/association or downstream evidence not found; `NT` = upstream relay not directly tested.

The pair-level records include the exact PubMed query URL, source record ID, target module assignment, excluded near matches, and an explicit `exportable=false` / `canonical_write_performed=false` guard.

## Regulator-level evidence kept separate

These papers support regulator identity or regulatory capacity, but not the queued edges:

- **ZNF792:** no qualifying primary functional regulator paper was located in the bounded search. Broad annotation and omics mentions were not counted as mechanistic evidence.
- **ASCL2:** human ASCL2 is expressed in trophoblast/intestinal contexts, and ASCL2 directly binds and represses the CDX2 promoter in colorectal cancer cells; independent mouse myoblast work supports E-box competition and transcriptional regulation. See [PMC4741583](https://pmc.ncbi.nlm.nih.gov/articles/PMC4741583/), [PMC5394758](https://pmc.ncbi.nlm.nih.gov/articles/PMC5394758/), and [PMID 9175731](https://pubmed.ncbi.nlm.nih.gov/9175731/).
- **OSR2:** OSR2 has human reprogramming/EMT evidence, and the human C2H2-ZF functional-diversity study includes GFP-tagged OSR2 ChIP-seq in HEK293 cells. Mouse palatal mesenchyme work combines mutant RNA-seq, ChIP-qPCR, and promoter reporters at non-queued developmental targets. See [PMID 35385105](https://pubmed.ncbi.nlm.nih.gov/35385105/), [PMID 27852650](https://pubmed.ncbi.nlm.nih.gov/27852650/), [GSE76494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76494), and [PMC5652858](https://pmc.ncbi.nlm.nih.gov/articles/PMC5652858/).
- **ZSCAN9:** no qualifying primary functional regulator program was located. Expression, annotation, co-occurrence, and database records were not counted as evidence.
- **ZBTB6:** human breast-cancer work reports ZBTB6 binding and repression of the ARHGAP6 promoter with perturbation and reporter assays; the C2H2-ZF study also provides a GFP-tagged ZBTB6 HEK293 ChIP-seq dataset. These are regulator-level or non-queued-target findings. See [PMC11938789](https://pmc.ncbi.nlm.nih.gov/articles/PMC11938789/), [PMID 27852650](https://pubmed.ncbi.nlm.nih.gov/27852650/), and [GSE76494](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE76494).

## Excluded near matches

- HIF1A–ACKR2 promoter binding/induction was not transferred to ZNF792, ASCL2, OSR2, ZSCAN9, or ZBTB6.
- PRC2/EZH2–ACVR1 repression and other ACVR1 pathway studies were not transferred to queued regulators.
- PLK2–ADAM17 physical interaction/activation and ADAM10/Notch biology were not treated as transcription-factor regulation.
- OSR2 developmental targets and ASCL2 targets such as CDX2 were not treated as evidence for different queued targets.
- ZBTB6–ARHGAP6 is a real non-queued regulatory edge, but it does not support ZBTB6–ACKR2, ACVR1, ACVR1C, or ADAM10.
- Co-expression, motif-only predictions, broad omics lists, cross-species observations, and target-only studies were excluded from promotion.

## Files

- [Pair review TSV](./public_tf_evidence_review_batch002_ranks16_20.tsv)
- [Regulator evidence register](./public_tf_evidence_review_batch002_ranks16_20_regulator_register.tsv)
- [Summary JSON](./ranks16_20_evidence_review_summary.json)
