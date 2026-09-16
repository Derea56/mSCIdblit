# mSCIdblit v1.7.0 mechanism-graph release

This release freezes the current validated Module 20B–24B register snapshot
used by the exporter. It adds a reproducible audit of complete ligand-to-target
signaling chains while retaining the evidence gate: only exportable, resolved,
non-self-loop edges are traversable graph edges.

## Release identity

- Project version: `mSCIdblit v1.7.0`
- Mechanism graph version: `v1.7.0`
- Graph release identifier: `module20_24_mechanism_graph:2026-09-15`
- Release date: `2026-09-15`
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_15/`
- Prior comparison snapshot: `data/processed/mechanism_graph_module20_24_v2026_09_10/`

The exact input-register SHA-256 values are recorded in
`bundle_metadata.json`. This is a register-backed graph release, not a claim
that every edge is SCI-specific or a replacement for canonical PostgreSQL
materialization.

## Bundle counts

| Measure | v1.6.0 | v1.7.0 | Change |
|---|---:|---:|---:|
| Nodes | 10,656 | 10,381 | -275 |
| Traversable edges | 16,333 | 13,085 | -3,248 |
| Evidence-source rows | 17,765 | 13,361 | -4,404 |
| Node-role assignments | 14,856 | 15,712 | +856 |
| Pathway summaries | 8,891 | 10,500 | +1,609 |
| Boundary groups | 98 | 96 | -2 |

| Module | Register edges | Traversable edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,124 | 5,906 | 4,782 |
| 21B | 9,954 | 9,872 | 9,904 | 82 |
| 22B | 5,733 | 714 | 5,906 | 5,019 |
| 23B | 1,230 | 1,226 | 1,630 | 4 |
| 24B | 151 | 149 | 200 | 2 |

The bundle also contains 2,990 typed entity forms, 13 conditional entity
transitions, 250 review-only output-bridge candidates, and 1,074 validated
output-bridge records. Output bridges and entity transitions remain excluded
from causal graph traversal.

## Full signaling-chain audit

The audit defines a full chain as three exported, role-compatible edges:

1. ligand-role source `--binds_receptor-->` receptor-role target;
2. receptor-role source `--any exported relay-->` transcription-factor-role
   target; and
3. transcription-factor-role source
   `--induces/represses/regulates_target_gene-->` target-gene-role target.

Pathway labels are not required to match because receptor-proximal and
target-gene evidence currently use separate module pathway namespaces. Review
bridges and typed transitions are excluded because the graph contract marks
them as conditional or non-causal.

| Audit measure | v1.6.0 | v1.7.0 |
|---|---:|---:|
| Evidence-backed edge-chain instances | 1,055 | 90 |
| Unique four-node topologies | 1,041 | 57 |
| Distinct receptor–TF pairs | 6 | 14 |
| Distinct ligand–receptor–TF routes | 7 | 18 |
| Same-pathway complete chains | 0 | 0 |

The current 90 chain instances are all `21B>21B>22B` module sequences. Their
terminal relations are 65 `induces_target_gene`, 9 `represses_target_gene`,
and 16 `regulates_target_gene`. The lower chain count relative to v1.6.0 is a
release-snapshot difference: the current bundle has different register
composition and role projection (including 51 transcription-factor-role and
67 target-gene-role nodes versus 288 and 2,441 in v1.6.0). It should not be
interpreted as a biological loss without first harmonizing those inputs.

The audit retains incomplete, evidence-backed path fragments instead of
dropping them. It contains 6,037 direct path records in total: 90 complete and
5,947 partial. The partial records comprise 5,863 ligand–receptor fragments
without a downstream receptor-to-TF link, 20 ligand–receptor-to-TF fragments
without a TF-to-target-gene link, and 64 TF-to-target-gene fragments without
the upstream ligand-to-receptor and receptor-to-TF links. Each partial row
records its `chain_status=partial` and explicit `missing_steps`; it does not
infer the missing mechanism.

The machine-readable outputs are `full_signaling_chain_audit.tsv` and
`full_signaling_chain_audit.json` in the release bundle. The TSV therefore
contains both complete chains and retained partial fragments.

The bundle also contains `mechanism_possible_signaling_paths.tsv`. This
hypothesis layer currently retains two strict
`ligand>receptor>????>????>target_gene_expression` paths:
Ado→Adora2b→????→????→Vegfa. Both have role-compatible ligand–receptor
evidence and a validated target-gene output bridge. The unknown intracellular
continuation and TF are explicitly not asserted and are not traversable as
causal edges.

The generalized `mechanism_signaling_route_evidence.tsv` artifact retains
6,070 non-causal evidence routes for downstream plausibility scoring. It
contains 5,894 ligand–receptor entry routes, 90 ligand–receptor–TF–target
routes whose intracellular continuation is collapsed or unresolved, 20
ligand–receptor–TF fragments without a target output, 64 TF–target output
fragments without an upstream ligand route, and the 2 output-bridge routes
above. These tiers preserve known evidence and explicit missing layers without
turning unknown links into graph edges.

## Validation and reproducibility

The graph validator passed with zero errors for identifier uniqueness, node and
evidence resolution, pathway summaries, role compatibility, exportability, and
self-loop exclusion. It reported only the existing warning that some evidence
sources lack stable public locators.

Rebuild and validate from the `mSCIdblit` repository root:

```bash
python3 scripts/export_module20_24_mechanism_graph.py \
  --output-dir data/processed/mechanism_graph_module20_24_v2026_09_15
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_15
python3 scripts/audit_full_signaling_chains.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_15 \
  --compare-bundle data/processed/mechanism_graph_module20_24_v2026_09_10
```

The audit command writes both chain reports and updates the bundle manifest
with the possible-path artifact and its count; it does not increase the
traversable edge count.

The bundle remains a conservative snapshot. Canonical database materialization,
stable source-anchor resolution, and explicit intercellular continuation remain
separate release gates.
