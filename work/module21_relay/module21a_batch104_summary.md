# Module 21A batch 104 review summary

Batch 104 reviewed the exact filtered priority-8 queue ordinal slice 1901–1925 from `module20a_external_review_queue.tsv`.

## Scope and validation

- 25/25 exact queue rows written to `module21a_batch104_review.tsv`.
- Review IDs matched exactly: `M20A-EXT-1009` through `M20A-EXT-1035`, with the queue's explicit gaps preserved.
- Pair labels matched the queue snapshot exactly.
- TSV schema has 13 columns; all required fields are populated; review IDs are unique.
- Status counts: 3 `reviewed_relay_candidate`, 3 `reviewed_function_only`, 1 `reviewed_binding_only`, and 18 `reviewed_unresolved`.
- No terminal TF was promoted. STAT3/STAT5 in the mutant CALR–MPL record are receptor-proximal signaling endpoints, not 22A terminal-TF assignments.
- Frozen Module 20A LR manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Shared registers, Module 20A ledgers, and integration outputs were not modified.

## Promoted evidence

- `C4b–CD46`: complement-fragment binding and membrane-cofactor activity for factor-I-dependent C4b/C3b cleavage; this is complement chemistry/function, not an intracellular CD46 TF relay.
- `CADM1–CRTAM`: direct CADM1/Necl-2–CRTAM adhesion with activated NK/CD8 functional output, including cytotoxicity and IFN-gamma release; cooperating activating receptors remain unresolved.
- `CADM3–CADM1`: direct extracellular heterophilic adhesion supported by quantitative SPRi; no downstream pathway or TF was assigned.
- `CALML3–KCNQ1`: intracellular channel-complex assembly and electrophysiologic modulation, including KCNQ1 current/PIP2-depletion behavior.
- `CALR–ITGA3` and `CALR–ITGAV`: intracellular integrin-alpha associations with adhesion or matrix-remodeling outputs; these are not extracellular calreticulin ligand claims.
- `mutant CALR–MPL`: direct mutant-CALR/MPL binding and MPL–JAK2–STAT3/STAT5 oncogenic relay in hematopoietic models; wild-type CALR and canonical thrombopoietin signaling were not conflated with this record.

## Unresolved and no-evidence boundaries

- C4a/C4b–NRP1, C4b–C3AR1, and C4b–C5AR2 remain unresolved. C4a lacks a defined cognate receptor in the reviewed complement literature; C3AR1 and C5AR2 evidence is for C3a and C5a/C5a-desArg, respectively.
- C920025E04Rik–CD8A/CD8B1 remains unresolved; transcript expression or CD8-associated dataset occurrence was not treated as molecular interaction evidence.
- All exact CALCA rows in this slice remain unresolved. The search separated CALCA precursor processing from mature calcitonin/alpha-CGRP and preserved the required CLR/GPCR plus RAMP composition. Evidence for PACAP, VIP, PTH, beta-adrenergic, orphan-GPR84/GPR20, or TSHR branches was not transferred to CALCA.
- CALCA–RAMP1/2/3 remains unresolved because the primary receptor studies require a complete CLR/CALCRL–RAMP complex and mature peptide; RAMP alone is not the complete receptor.
- CALR–ITGA2B remains unresolved. The platelet study supported CALR association with alpha2beta1/GPVI and explicitly found the adhesion effect independent of alphaIIbbeta3, so alpha2/alpha3 integrin evidence was not assigned to ITGA2B.

## Scope note

The exact filtered slice ended at `M20A-EXT-1035` (`Calr Mpl`). CALR pairs with MTNR1A, SCARF1, or TSHR mentioned in the broader family description were not present in these 25 exact rows and were not added to batch 104; they require their own queue-ordinal review.

Primary search boundaries covered PubMed, PMC, publisher pages, Reactome/pathway context where useful for triangulation, and exact-symbol queries. Pathway databases were used only as context and were not used to promote an exact molecular edge without primary support.
