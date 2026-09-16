# mSCIdblit Module 20B–24B mechanism graph v1.8.1

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-reconciled`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_reconciled/`

This patch release rebuilds the mechanism graph from the reconciled `main`
baseline. It retains the remote Module 21B additions and incorporates the
pending Module 20B and 22B–24B curation decisions without carrying forward
the stale generated `v2026_09_01` snapshot.

## Graph contents

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Node-role assignments | 17,332 |
| Pathway summaries | 10,881 |
| Boundary groups | 96 |
| Output-bridge candidates | 342 |
| Validated output bridges | 1,166 |

The strict audit finds 141 evidence-backed edge-chain instances and 95 unique
four-node topologies. It retains 6,118 partial chain records with explicit
missing-link annotations, plus two strict possible missing-relay hypotheses.

The generalized route-evidence layer contains 11,118 records, including 5,931
ligand–receptor entry-only records and 4,737 downstream evidence records linked
to 3,331 curation-queue records. The downstream evidence records include
generic-output, intracellular-cascade, transcription-factor, target-gene, and
unresolved-claim categories. Generic outputs remain non-causal labels so mSCS
can evaluate evidence layers independently.

## Validation

`validate_module20_24_mechanism_graph.py` passes with zero errors. The bundle
retains the warning that some evidence sources do not have stable locators;
those rows preserve their summaries and limitations.

The prior v1.8.0 bundle remains available at
`data/processed/mechanism_graph_module20_24_v2026_09_16/` for comparison.
