# mSCIdblit public signaling-database comparison v2

This report compares `module20_24_mechanism_graph:2026-09-19-literature-expansion-242` with the frozen public-resource snapshot `mscs_phase2_external_snapshot_2026-08-05`. It is an inventory audit, not a biological completeness score. Complexes are compared first as component sets; public-only rows remain candidates and are not added as graph edges.

## Executive summary

- mSCIdblit contains 5,931 ligand–receptor edge rows, 5,742 unique label pairs, and 5,680 component-normalized pairs.
- The route-evidence layer contains 20,196 records and covers 3,331 of 3,331 queue IDs with literature-linked evidence.
- The comparison emits 7,753 unique public-only LR candidates for review; these are not causal graph additions.
- Primary-evidence gate: 1,827 candidates have a locator-like public note requiring verification, and 5,926 have no primary locator in the frozen public snapshot. None is automatically verified.
- The first review batch contains 25 candidates ranked by independent public-source support and primary-locator density; this is a work queue, not a confidence score.
- Exact label overlap is intentionally conservative. Component-normalized overlap is the preferred ligand–receptor comparison, especially for heteromeric receptors.

## Ligand–receptor comparison

| Source | Raw rows | mSCIdblit pairs | Public pairs | Component overlap | mSCIdblit coverage of public | Public coverage of mSCIdblit | Public-only component pairs |
|---|---:|---:|---:|---:|---:|---:|---:|
| CellChatDB.mouse | 3,379 | 5,680 | 3,359 | 712 | 21.2% | 12.5% | 2,647 |
| NicheNet.neutral_v1 | 5,668 | 5,680 | 5,606 | 834 | 14.9% | 14.7% | 4,772 |
| LIANA.mouseconsensus | 3,989 | 5,680 | 3,982 | 1,146 | 28.8% | 20.2% | 2,836 |
| master_LR_union | 9,099 | 5,680 | 9,023 | 1,270 | 14.1% | 22.4% | 7,753 |

## Representational depth

| Resource/layer | LR pairs/rows | Intracellular continuation | TF layer | Target/output layer | Context/evidence fields |
|---|---:|---:|---:|---:|---|
| mSCIdblit route evidence | 20,196 | 438 distinct intermediates | 61 distinct TFs | 110 target genes; 1,987 outputs | 19,427 contextualized records |
| CellChatDB.mouse | 3,359 | not represented as route layer | not represented as route layer | not represented as route layer | cofactors: 577; evidence: 3,379 rows |
| NicheNet.neutral_v1 | 5,606 | target-prior network, not explicit relay chain | not explicit in LR table | target-gene matrix available in snapshot | source/database fields in LR table |
| LIANA.mouseconsensus | 3,982 | not represented | not represented | not represented | pair inventory fields only |

This is the key distinction: mSCIdblit carries an evidence-bearing route layer beyond the public LR inventories. NicheNet contributes downstream ligand–target priors, while Reactome, OmniPath, and TF resources are needed for the next intracellular and TF edge comparison.

## mSCIdblit route detail

| Route tier | Records |
|---|---:|
| `ligand_receptor_entry_only` | 6,701 |
| `ligand_receptor_output_annotation_missing_intracellular_and_tf` | 4,005 |
| `ligand_receptor_intracellular_output_missing_tf` | 2,951 |
| `ligand_receptor_intracellular_claim_unresolved` | 2,300 |
| `ligand_receptor_downstream_claim_unresolved` | 1,208 |
| `downstream_output_annotation_unlinked_topology` | 818 |
| `receptor_intracellular_output_annotation_missing_ligand_receptor_and_tf` | 508 |
| `receptor_intracellular_claim_unresolved` | 401 |
| `ligand_receptor_output_missing_intracellular_and_tf` | 227 |
| `ligand_receptor_intracellular_tf_output_missing_target_gene` | 160 |
| `ligand_receptor_tf_target_missing_intracellular` | 153 |
| `ligand_receptor_tf_output_annotation_missing_intracellular` | 149 |
| `downstream_claim_unresolved_topology` | 141 |
| `ligand_receptor_tf_output_missing_target_gene` | 96 |
| `explicit_ligand_receptor_intracellular_tf_target` | 78 |
| `ligand_receptor_tf_annotation_missing_intracellular_and_output` | 70 |
| `ligand_receptor_intracellular_tf_missing_output` | 67 |
| `tf_target_output_only` | 63 |
| `receptor_intracellular_tf_annotation_missing_ligand_receptor_and_output` | 42 |
| `downstream_tf_annotation_unlinked_topology` | 27 |
| `ligand_receptor_tf_missing_intracellular_and_output` | 20 |
| `ligand_receptor_tf_target_annotation_missing_intracellular` | 11 |

### Literature-linked output classes

| Output class | Records |
|---|---:|
| `unknown` | 922 |
| `cellular_functional_readout` | 808 |
| `phosphorylation_or_activation_readout` | 501 |
| `gene_expression_or_transcription` | 328 |
| `generic_functional_readout` | 258 |
| `second_messenger_readout` | 217 |
| `reporter_readout` | 142 |
| `secreted_protein_or_release` | 125 |
| `target_gene_expression` | 95 |
| `phagocytosis_or_engulfment` | 92 |
| `translocation_or_localization_readout` | 89 |
| `cleavage_or_processing_readout` | 72 |

## Interpretation

- Public-only pairs are candidates for evidence review, not proof that mSCIdblit is incomplete. Differences can arise from species scope, complex representation, source inclusion, evidence thresholds, and inferred versus directly curated interactions.
- mSCIdblit adds information that LR-only resources do not represent in the same row: receptor-proximal continuation, TF and target-gene annotations, output classes, context, assay/perturbation, source locators, and explicit non-causal traversal status.
- A fair next comparison is therefore not only pair overlap. It should compare how many public LR pairs can be connected to intracellular, TF, and output evidence in mSCIdblit, and how many mSCIdblit routes are absent from each public resource because that resource stops at a different layer.

## Reproduction

```bash
python3 scripts/compare_release_public_databases_v2.py
```

The JSON summary contains input hashes, counts, denominators, and route-tier details. `public_only_lr_candidates.tsv` is a review queue only; `primary_evidence_review_queue.tsv` contains only locator-bearing candidates that still require manual primary-paper verification; `primary_evidence_top25.tsv` is the first ranked review batch.
