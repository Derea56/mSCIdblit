# mSCIdblit v1.8.0 mechanism-graph release

This release freezes the Module 20B–24B mechanism graph together with the
Module 21B downstream-claim route layer. It is a conservative, evidence-backed
snapshot: only exportable graph edges are traversable, while incomplete and
generic signaling evidence remains available to mSCS for plausibility scoring.

## Release identity

- Project version: `mSCIdblit v1.8.0`
- Mechanism graph version: `v1.8.0`
- Graph release identifier: `module20_24_mechanism_graph:2026-09-16`
- Release date: `2026-09-16`
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16/`
- Prior comparison snapshot: `data/processed/mechanism_graph_module20_24_v2026_09_15/`

The exact input-register SHA-256 values are recorded in `bundle_metadata.json`.

## Bundle counts

| Measure | v1.8.0 |
|---|---:|
| Nodes | 10,381 |
| Traversable edges | 13,085 |
| Evidence-source rows | 13,361 |
| Node-role assignments | 15,712 |
| Pathway summaries | 10,500 |
| Boundary groups | 96 |
| Receptor-role nodes | 2,383 |

The bundle also contains 2,990 typed entity forms, 13 conditional entity
transitions, 250 review-only output-bridge candidates, and 1,074 validated
output-bridge records. Conditional bridges and entity transitions remain outside
causal graph traversal.

## Signaling route evidence

The full-chain audit retains 90 strict ligand→receptor→TF→target edge-chain
instances and 5,947 partial fragments. The generalized route table contains
10,986 non-causal evidence routes. This includes 5,894 ligand–receptor entry
routes and 4,692 Module 21B downstream evidence routes.

Every one of the 3,298 Module 21B queue records and all 4,692 downstream
evidence records is linked into the route table through
`source_queue_id` and `source_evidence_record_id`. The linked evidence covers
generic outputs/readouts, text-level TF and target-gene mentions,
receptor-proximal intracellular candidates, and unresolved claims. Generic
outputs remain labels rather than invented molecular nodes, and all route rows
remain explicitly non-causal.

The downstream queue remains a manual-curation layer. Its records are classified
as likely LR entries, receptor-proximal claims needing an upstream LR pair, or
topology-ambiguous claims; these classifications prioritize review and do not
assert missing mechanisms.

## Validation and mSCS intake

The graph validator passes with zero errors for identifier uniqueness, node and
edge resolution, evidence retention, pathway summaries, role compatibility,
exportability, and route-to-queue/evidence linkage. The only validator warning
is the existing locator warning for evidence sources without stable public
anchors.

The matching mSCS importer accepts the route table, queue, and downstream
evidence records. mSCS inference can use LR-linked generic outputs and TF
annotations as plausibility evidence while leaving target-gene expression
unassessed when no target feature is supplied.

Rebuild and validate from the `mSCIdblit` repository root:

```bash
python3 scripts/export_module20_24_mechanism_graph.py \
  --output-dir data/processed/mechanism_graph_module20_24_v2026_09_16
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_16
python3 scripts/audit_full_signaling_chains.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_16 \
  --compare-bundle data/processed/mechanism_graph_module20_24_v2026_09_15
```
