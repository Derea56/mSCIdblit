# Module 21A batch 073 review summary

## Scope

- Exactly 25 requested review IDs were reviewed: `M20A-CELLCHAT-REMAINING-1218` through `M20A-CELLCHAT-REMAINING-1242`.
- The queue has an ordinal mismatch: literal ordinal rows 1126–1150 contain Glu/SLC1A7 rows and have review IDs 1126–1150. The explicit review-ID range and the specified H2-Q7/Q8/Q9/T-ps/T10/T18/T22/T23/T24/T25/T26/T27/T3 content resolve to queue ordinals 1218–1242. This batch follows the explicit IDs and family specification.
- MHC-I antigen presentation/association was kept separate from CD8 coreceptor binding and from CD94/NKG2 receptor signaling. No terminal TF was assigned.

## Disposition

- `reviewed_relay_candidate`: 2
- `reviewed_binding_only`: 3
- `reviewed_function_only`: 0
- `reviewed_unresolved`: 20
- Terminal TF assignments: 0

## Evidence findings

1. **H2-T23/Qa-1b–CD94/NKG2A** is the clearest receptor-proximal relay candidate. Primary mouse work directly demonstrated Qa-1b recognition by CD94/NKG2A and inhibition of NK target-cell lysis (`PMID:9815261`, `PMCID:PMC2212405`). The exact receptor is a heterodimer and requires peptide-loaded Qa-1b/Qdm context; no unique downstream TF was inferred.
2. **H2-T23/Qa-1b–CD94/NKG2C** has direct binding evidence (`PMID:10601355`, `PMCID:PMC2195720`), but the cited study described activating cytoplasmic features without a matched downstream activation assay. It remains binding-only.
3. **H2-T3/TL–CD8alphaalpha** has direct binding and receptor-proximal modulation evidence. TL tetramers preferentially bind CD8alphaalpha, and the TL/CD8alphaalpha complex modifies Lck-dependent T-cell signaling (`PMID:11729321`, `PMID:12594948`, `PMID:15749886`). The edge is recorded as a receptor-complex interaction, not an isolated CD8A molecular contact.
4. **H2-T18/TL–CD8alphaalpha** and **H2-T22–CD8alphaalpha** have binding evidence but were not promoted to relay edges. The H2-T18 assignment is limited by TL/T3-T18 allele terminology; H2-T22 was directly tested with recombinant tetramers/SPR (`PMID:31992596`, `PMCID:PMC7062157`). CD8B1 rows remain unresolved because CD8alphaalpha evidence does not establish an isolated CD8B1 edge.
5. **H2-Q7/Q8/Q9** evidence was not converted into direct CD8 edges. Q7 alpha-3-domain studies reported defective CD8 binding (`PMID:8245786`, `PMCID:PMC2191298`), while Q9 antiviral studies establish peptide-MHC/TCR recognition by CD8 T cells rather than direct CD8 coreceptor binding (`PMID:18541714`, `PMCID:PMC2442642`). Q8 was not isolated in a matched CD8 assay.
6. **H2-T10** evidence concerns gamma-delta TCR recognition and selection, not CD8A/CD8B1 (`PMCID:PMC2196254`, `PMCID:PMC5828614`). H2-T-ps was retained as transcript/pseudogene context without evidence for a translated receptor ligand (`PMCID:PMC9851994`). H2-T24/T25/T26/T27 had no exact primary CD8 binding assay located; family-level H2-T or expression evidence was not promoted.

## Search boundaries

Searches covered PubMed, PMC full text, publisher pages, and primary structural, biochemical, tetramer, transfectant, and cell-based studies. Queries used exact H2-Q/H2-T symbols, Qa-2/Qa-1b/TL aliases, CD8alpha/CD8beta, CD94/NKG2A/NKG2C, KLRD1/KLRC1/KLRC2, gamma-delta TCR, allele terms, and cross-species controls. No direct edge was inferred from generic MHC-I antigen presentation, transcript expression, family-level receptor biology, or downstream cellular function.

## Files changed

- `work/module21_relay/module21a_batch073_review.tsv`
- `work/module21_relay/module21a_batch073_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified.

