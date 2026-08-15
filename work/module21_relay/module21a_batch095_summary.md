# Module 21A batch 095 review summary

## Scope

- Reviewed exact filtered priority-8 queue ordinals 1676–1700 from work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv.
- The slice contains 25 exact queue rows with IDs M20A-EXT-0710 through M20A-EXT-0749 and intentional gaps. Queue ID and pair-key matching passed.
- Output is isolated in module21a_batch095_review.tsv; shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.

## Disposition

- 25 exact rows reviewed.
- 2 reviewed_relay_candidate: ADM2–CALCR at the CALCR/RAMP complex level; AGRN–ITGB1 as alpha-v-beta1 integrin-dependent agrin adhesion/signaling modulation.
- 23 reviewed_unresolved.
- 0 reviewed_binding_only.
- 0 reviewed_function_only.
- 0 terminal TF assignments.

## Promoted evidence

1. **ADM2–CALCR:** mouse calcitonin receptor/RAMP complex pharmacology supports an AM2/intermedin receptor-proximal cAMP relay in recombinant COS7 cells. The edge is explicitly complex-level; the RAMP component and species context remain required. Primary support: PMCID PMC8776895. Human primary-cell work used as a comparator supports AM2 signaling through CALCRL/RAMP complexes, not CALCR monomer: DOI 10.1038/s42003-021-02293-w.
2. **AGRN–ITGB1:** primary agrin adhesion and AChR-clustering experiments support integrin-dependent modulation involving alpha-v-beta1, with beta1 blockade/perturbation. This is retained as a receptor-proximal complex relay, not a standalone ITGB1 molecular interaction. Primary support: PMID 9367446; neuromuscular-junction boundary support: PMID 15371519.

## Unresolved and no-evidence boundaries

- ADM and ADM2 rows involving GPR20, GPR84, MRGPRB1, PTH1R, TSHR, VIPR1, ADCYAP1R1, ADRB2, ADRB3, and DCLK3 lacked primary exact-pair activation evidence in the searched literature.
- ADM–GPR182 was not promoted: early homology-based adrenomedullin-receptor assignment was later refuted; current primary work supports GPR182/ACKR5 chemokine scavenging. Primary boundary sources: PMID 9367907; PMCID PMC10405735.
- ADM–MRGPRX2 was not promoted because the positive study concerns proadrenomedullin N-terminal peptides PAMP-12/PAMP-20, not mature ADM: PMID 15823563.
- ADM–RAMP1 was not promoted because RAMP1 is a cofactor and the canonical mature-ADM complexes are CLR/CALCRL–RAMP2/3; CLR–RAMP1 is the CGRP receptor context: PMID 16373602; PMID 12196109.
- AGRN–LRP1 and AGRN–LRP2 were not promoted. Agrin receptor evidence identifies LRP4/MuSK, while LRP1 and LRP2/megalin studies in the search addressed distinct integrin-adhesion or multiligand-endocytosis biology: PMCID PMC2743173; PMID 29116364; PMID 9122201; PMID 38771880.
- AGRP–MC1R and AGRP–MC5R were not promoted. Primary melanocortin studies place native AgRP activity at MC4R/MC3R and report little/no MC1R or MC5R pharmacology: PMID 20831872; PMID 11708914.
- AGRP–SDC1 was not promoted. AgRP/heparan-sulfate and syndecan-3 processing literature does not establish direct binding or relay through syndecan-1: PMID 28264929; PMID 16384863.

## Validation

- Header matches the requested 13-column schema.
- 25 rows; all rows have 13 fields and required fields populated.
- Review IDs are unique.
- Exact queue IDs and pair keys match the requested filtered slice.
- Frozen Module20A LR manifest SHA256 remains 02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e.

## Search boundary

Searches covered PubMed, PMC, and publisher pages, prioritizing primary receptor pharmacology, recombinant complex assays, primary-cell signaling, adhesion/perturbation studies, and receptor-family boundary papers. No pathway-level or functional-output result was used to infer a direct molecular interaction, and no terminal TF was assigned without exact downstream evidence.
