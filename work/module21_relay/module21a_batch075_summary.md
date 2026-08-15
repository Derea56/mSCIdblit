# Module 21A batch 075 review summary

## Scope

Reviewed exactly the priority-8 filtered queue slice ordinal rows 1176–1200 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. These map to review IDs `M20A-CELLCHAT-REMAINING-1282` through `M20A-CELLCHAT-REMAINING-1329`, including the IL11–IL9 cytokine-receptor rows, Ins1–Insr, and VCAM1/ADGRE5/ADGRA2 adhesion rows. The raw physical queue file contains other rows at those line numbers; the filtered priority-8 slice is the authoritative batch partition used by the Module 21A queue workflow.

Searches covered PubMed records, PMC full text, publisher pages, and structural/primary receptor studies. Stable PMID, PMCID, and DOI locators are retained in the TSV. Pathway reuse was limited to exact receptor-complex composition where the primary source matched the submitted subtype and evidence scope.

## Disposition

| Disposition | Count | Main result |
|---|---:|---|
| `reviewed_relay_candidate` | 16 | Exact cytokine receptor complexes, receptor-proximal JAK/STAT or integrin adhesion relays, and insulin-receptor pathway evidence. |
| `reviewed_binding_only` | 5 | Isolated receptor components, decoy/processed ectodomain binding, or exact adhesion binding without a validated downstream relay. |
| `reviewed_function_only` | 0 | No row was promoted solely from a functional output without a qualifying binding or receptor-complex basis. |
| `reviewed_unresolved` | 4 | IL11 complex-2 composition, IL13/IL4R/IL13RA2, IL4/IL4R/IL13RA2, and exact ADGRE5–ITGAV/ITGB1 subtype evidence. |

Eleven rows contain direct terminal-TF or TF-level pathway assignments: STAT3, STAT4, STAT6, STAT1/3/4/5, or FOXO1/CREB as recorded per row. Incomplete IL15RA–IL2RB and IL2RA–IL2RB subcomplexes do not receive terminal TF assignments because IL2RG is required for the complete signaling receptor. The Ins1–Insr assignment is explicitly limited by the fact that most primary assays use mature insulin rather than an isoform-purified Ins1-only preparation.

## Accuracy boundaries retained

- IL11 complex 1 was matched to the resolved IL-11–IL-11RA–gp130 composition; complex 2 was left unresolved because its submitted composition is not defined by the primary structural studies.
- IL12AB–IL12RB1/IL12RB2 was promoted using exact receptor-complex structural and functional evidence, including STAT4 activation.
- IL13RA1 and IL13RA2 alone remain component/decoy binding records. IL13RA1-dependent STAT6 evidence is assigned only to the complete IL4R–IL13RA1 complex.
- IL15RA–IL2RB and IL2RA–IL2RB are retained as assembly/receptor-proximal intermediates, with explicit common-gamma-chain limitations.
- IL23, IL27, IL31, IL4, IL7 and IL9 rows preserve receptor subtype distinctions and do not transfer family-level pathways across complexes.
- VCAM1 is the ligand for alpha4/alpha9 integrins; the submitted receptor-first orientation is preserved and documented rather than silently rewritten. Alpha4beta7 VCAM1 evidence is binding/adhesion only because signaling assays used different ligand contexts.
- ADGRA2/GPR124 evidence is restricted to the proteolytically processed TEM5 ectodomain binding alphaVbeta3; the full-length RECK/WNT7/Frizzled branch remains distinct.
- ADGRE5/CD97 evidence supports alphaVbeta3 contribution and alpha5beta1 as a dominant counterreceptor, but not the submitted alphaVbeta1 subtype; that row remains unresolved.

## Files changed

- `work/module21_relay/module21a_batch075_review.tsv`
- `work/module21_relay/module21a_batch075_summary.md`

No shared Module 21A registers, Module 20A ledgers, frozen manifest, or integration outputs were modified. This batch is ready for validation and approval before integration.
