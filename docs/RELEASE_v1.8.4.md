# mSCIdblit Module 20B–24B mechanism graph v1.8.4

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-tf-output-coverage`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_tf_output_coverage/`

This release extends v1.8.3 by recognizing explicitly curated ligand–receptor
binding, activation, assembly, and entry-receptor relations when the exported
endpoint roles support a ligand-to-receptor interpretation. This resolves
direct evidence routes that were previously left as topology-ambiguous. The
remaining ambiguous records are retained for review when the relation is not a
direct ligand–receptor event or the source/target roles do not support that
interpretation.

The release also retains queue-level co-observed TF and output evidence for
direct ligand–receptor routes. Generic assay/readout terms remain outputs, not
target-gene edges, and all evidence routes remain non-causal.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Strict edge-chain instances | 141 |
| Strict four-node topologies | 95 |
| Partial chain records | 6,118 |
| Evidence-route records | 16,047 |
| Receptor-identity-alias route records | 2,135 |
| Direct LR→TF→output records missing target-gene expression | 96 |
| Intracellular→TF→output records missing target-gene expression | 117 |
| Receptor-proximal queues still missing an LR pair | 4 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
The strict causal graph is unchanged; mSCS receives the expanded evidence
layer for confidence scoring and route plausibility.

The four remaining receptor-proximal queues concern CRIT/SjTOR/ShTOR
complement C2-binding inhibitors and synapse-localized CRRY. They are retained
as evidence claims but are not promoted to cell-surface ligand–receptor routes
because their reported interactions are extracellular complement regulation,
not intracellular continuation through a signaling receptor.

These dispositions are recorded in `mechanism_gap_review.tsv` with the primary
locators retained in the bundle.
