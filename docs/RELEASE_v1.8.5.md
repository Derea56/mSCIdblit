# mSCIdblit Module 20B–24B mechanism graph v1.8.5

Release date: 2026-09-16
Graph identifier: module20_24_mechanism_graph:2026-09-16-evidence-contract
Bundle: data/processed/mechanism_graph_module20_24_v2026_09_16_evidence_contract/

This release adds mechanism_evidence_v1 to the retained route, downstream
queue, and downstream evidence records. The contract standardizes output
classes, evidence polarity, negative-evidence status, directness, context
qualifiers, effect polarity, source scope, and explicit missing layers.
Original labels, summaries, limitations, and provenance identifiers remain
unchanged.

The contract is evidence-native: mSCIdblit does not emit a composite biological
confidence score. mSCS uses these fields, together with the observed cell
context, to calculate route plausibility.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,047 |
| Downstream evidence records | 4,730 |
| Direct LR→TF→output records missing target-gene expression | 96 |
| Intracellular→TF→output records missing target-gene expression | 117 |
| Receptor-proximal queues still missing an LR pair | 4 |

Generic functional readouts remain outputs and are not promoted to target-gene
claims. Negative or contradictory source scopes are retained as evidence
qualifiers; the current snapshot contains no newly asserted negative route
claim solely from the schema addition.

The bundle passes validate_module20_24_mechanism_graph.py with zero errors.
