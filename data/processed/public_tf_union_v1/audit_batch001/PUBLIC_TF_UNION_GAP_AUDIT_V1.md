# Public TF/regulon union v1 independent gap audit

Status: complete. This report compares independent raw-snapshot parsing with the additive `external_tf_*` layer and the frozen mSCIdblit tables.

## Counts

| Source/species | Raw records | Raw TFs | Raw simple pairs | Materialized simple pairs | Raw pairs not materialized | Raw pairs overlapping frozen regulon |
|---|---:|---:|---:|---:|---:|---:|
| OmniPath_DoRothEA:human | 15,267 | 367 | 15,116 | 15,116 | 0 | 20 |
| OmniPath_DoRothEA:mouse | 14,075 | 328 | 13,197 | 13,197 | 0 | 13 |
| TRRUST:human | 9,396 | 795 | 8,426 | 8,426 | 0 | 20 |
| TRRUST:mouse | 7,057 | 827 | 6,490 | 6,490 | 0 | 17 |

Frozen counts after materialization: `signalingentity`=2,792, `signalingentityrole`=4,358, `signalingedge`=3,172, `regulon`=45, `regulonmember`=107, `regulonmembersource`=162.

## Gap classes

- TF coverage categories: {'absent_tf_node': 2180, 'tf_node_missing_explicit_tf_role': 58, 'tf_node_and_role_present': 79}.
- Unresolved raw identity rows: 830; examples are retained in the JSON report and `unresolved_identity_queue.tsv`.
- Downstream view: {'records_with_unresolved_target_identity': 509, 'records_with_unresolved_tf_identity': 329, 'records_with_target_absent_from_frozen_graph': 37279, 'records_with_target_node_but_missing_explicit_target_role': 6205, 'records_with_explicit_target_role': 1802}.
- Upstream gap categories: {'tf_node_unmapped': 2180, 'upstream_path_present': 61, 'upstream_path_absent': 76}. The upstream view uses exact frozen entity symbol matches only and does not infer ligand-to-TF activation.
- Priority-TF identity verification statuses: {'database_curated_unverified': 11, 'primary_reference_verified': 13, 'context_limited_reference': 8}. `database_curated_unverified` rows remain unpromoted.
- Direction-conflict groups: 435; the report includes the first 50 named examples.

## Direction conflicts

The following are source-level disagreements, not merged assertions:

| Species | TF | Target | Source/effect assertions |
|---|---|---|---|
| human | ddit3 | tnfrsf10b | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| mouse | gata2 | spi1 | TRRUST:activating_target, TRRUST:repressing_target |
| human | ahr | cyp1a1 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | ar | cdkn1a | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | ar | klk3 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | bach1 | hmox1 | OmniPath_DoRothEA:repressing_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | cebpb | ptgs2 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | creb1 | ifng | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | ctcf | app | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | ctcf | myc | OmniPath_DoRothEA:repressing_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | e2f1 | birc5 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | e2f1 | kif2c | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | e2f1 | tert | OmniPath_DoRothEA:repressing_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | e2f1 | tp53 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | e2f4 | brca1 | OmniPath_DoRothEA:repressing_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | egr1 | alox5 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | egr1 | vegfa | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | esr1 | cdkn1a | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | ets1 | parp1 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | fli1 | tgfbr2 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | fos | mmp9 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | fos | nos2 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | foxo1 | igfbp1 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | gata1 | epo | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |
| human | gli1 | bcl2 | OmniPath_DoRothEA:activating_target, TRRUST:activating_target, TRRUST:repressing_target |

## Referential integrity and release separation

Referential-integrity checks: `{'identity_source_fk': 0, 'record_source_fk': 0, 'reference_record_fk': 0, 'member_regulon_fk': 0, 'member_record_fk': 0, 'verification_record_fk': 0, 'regulon_member_count_mismatch': 0, 'non_excluded_external_rows': 0, 'non_excluded_external_members': 0}`.

All external records and members are export-gated with `export_priority = 'exclude'`. Existing frozen mechanism tables were not updated by the loader.

## Reproduction

```bash
python3 scripts/audit_public_tf_union_v1.py \
  --trrust-human /private/tmp/trrust_human.tsv \
  --trrust-mouse /private/tmp/trrust_mouse.tsv \
  --dorothea-human /private/tmp/omnipath_dorothea_human.tsv \
  --dorothea-mouse /private/tmp/omnipath_dorothea_mouse.tsv \
  --output-dir data/processed/public_tf_union_v1
```
