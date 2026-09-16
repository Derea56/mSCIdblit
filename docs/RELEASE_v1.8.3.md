# mSCIdblit Module 20B–24B mechanism graph v1.8.3

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-tf-coverage`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_tf_coverage/`

This release extends v1.8.2 with a conservative receptor-identity alias layer
for receptor-proximal evidence. It links modified receptor labels, such as
phosphosite and receptor-complex forms, to already-exported ligand–receptor
entries only when a curated receptor identity matches. These links remain
context-bound evidence routes; they do not add causal graph edges or assume
that every ligand for a receptor produces the same response.

The release also materializes co-observed intracellular, TF, and output
evidence from the same curation queue record. Generic assay/readout terms are
retained as outputs, while target-gene expression remains explicitly missing
unless a target-gene record is present.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Strict edge-chain instances | 141 |
| Strict four-node topologies | 95 |
| Partial chain records | 6,118 |
| Evidence-route records | 15,469 |
| Receptor-identity-alias route records | 1,681 |
| Co-observed intracellular→TF→output records | 124 |
| Receptor-proximal records still missing an LR pair | 735 |

The route layer contains 2,061 intracellular-plus-output records missing TF
support, 74 intracellular-plus-TF records missing a terminal output, and 124
co-observed intracellular-plus-TF-plus-output records missing target-gene
expression. The strict complete-chain count remains 141 because these additions
are evidence routes rather than newly asserted causal edges.

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
The mSCS import contract accepts the new route tier, and mSCS can traverse an
explicit receptor-proximal continuation edge when its endpoints resolve.
