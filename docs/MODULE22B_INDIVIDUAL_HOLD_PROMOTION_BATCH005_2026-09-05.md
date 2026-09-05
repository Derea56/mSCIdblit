# Module 22B individual hold promotion batch 005 — 2026-09-05

This bounded tranche searched the unresolved SMAD2 and SMAD3 lanes as
standalone TF-to-target relationships. Four exact source/target identities were
recovered from primary studies and added to the working registers. The
upstream MSTN handoff holds remain unchanged; none of these rows claims that
the submitted receptor complex activated the TF.

| TF | target | tier | primary source | context |
| --- | --- | --- | --- | --- |
| SMAD3 | ASIC3 | high, direct repression | PMID:18466073 | rat nucleus-pulposus/intervertebral-disc comparator; spinal-tissue-adjacent, not traumatic SCI |
| SMAD3 | PAX6 | high, direct activation | PMID:30594196; PMCID:PMC6311080 | human NSCLC comparator |
| SMAD3 | AR | high, direct activation | PMID:36727462; PMCID:PMC10085708 | human prostate-cancer comparator |
| SMAD2 | MIXL1 | medium-high, cooperative regulatory support | PMID:27965357; PMCID:PMC5270477 | human embryonic-stem-cell comparator |

The audit ledger is
`work/module22b_tf_regulon_promotion_audit/module22b_individual_hold_promotion_batch005.tsv`.
The four searches are appended to
`docs/MODULE22B_INDIVIDUAL_HOLD_SEARCH_LOG_2026-09-03.tsv`.

## Register accounting

| Measure | Before | After |
| --- | ---: | ---: |
| Module 22B edge rows | 10,690 | 10,694 |
| Module 22B evidence rows | 10,780 | 10,784 |
| Exportable target-gene rows | 5,037 | 5,041 |
| High-confidence target-gene rows | 4,407 | 4,410 |
| Medium-high target-gene rows | 594 | 595 |
| Low-confidence rows | 4,991 | 4,991 |
| Module 22A no-evidence-boundary holds in the audited scope | 4,957 | 4,957 |

The primary studies support the standalone target claims at the recorded
species and models. They do not upgrade the original ligand/receptor-to-TF
handoffs, and canonical SQL/database materialization remains unchanged.
