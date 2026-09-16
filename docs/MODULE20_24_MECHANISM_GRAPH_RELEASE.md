# Module 20B–24B mechanism graph release reference

The current release is documented in
[`RELEASE_v1.7.0.md`](RELEASE_v1.7.0.md). The v1.6.0 and v1.5.0 snapshots below
are retained as implementation and historical baseline references.

Current release identifier: `module20_24_mechanism_graph:2026-09-15`

Current bundle: `data/processed/mechanism_graph_module20_24_v2026_09_15/`.
It contains the machine-readable full-chain audit in
`full_signaling_chain_audit.tsv` and `full_signaling_chain_audit.json`, plus
the possible-path layer in `mechanism_possible_signaling_paths.tsv` and the
generalized evidence-route layer in `mechanism_signaling_route_evidence.tsv`.

The current bundle has 10,381 nodes, 13,085 traversable edges, 13,361 linked
source rows, 15,712 node-role assignments, 10,500 pathway summaries, and 96
boundary groups. The full-chain audit reports 90 evidence-backed edge-chain
instances and 57 unique four-node topologies, while retaining 5,947
evidence-backed partial path fragments with explicit missing-link annotations.
Two strict possible missing-relay paths are also retained as non-causal
hypotheses: `Ado>Adora2b>????>????>Vegfa`. The generalized route-evidence
table retains 10,986 tiered records, including one route-linked record for each
of the 4,692 Module 21B downstream evidence records. Generic ligand–receptor/
output routes whose output is not assigned a `target_gene` role remain labels,
so mSCS can score entry, intracellular, TF, and output evidence independently
without treating the route as a causal graph path.
The Module 21B downstream curation queue retains 3,298 evidence-backed rows
with downstream/functional annotations but no linked output route. It preserves
exact source evidence and separates likely LR entries, receptor-proximal
intracellular claims, and topology-ambiguous rows for manual conversion into
explicit route evidence. All queue-linked evidence records retain the queue and
record IDs used to join those route candidates back to their source claims.
Its companion evidence-record table contains explicit generic-output,
intracellular-cascade, TF, and target-gene candidate records while retaining
929 claims that require manual interpretation.
See the v1.7.0 release note for the complete counts and interpretation
boundaries.

Historical v1.6.0 release identifier: `module20_24_mechanism_graph:2026-09-10`

## Historical v1.6.0 reference

This is a conservative, register-backed mechanism graph snapshot for mSCIdblit
Modules 20B–24B. It is designed for inspection and simulator import while
preserving the evidence gate: only rows marked `exportable=true` in the
validated edge registers become traversable graph edges.

The v1.6.0 release emitted the required mSCS mechanism-bundle columns and was
validated by running mSCS's `import_mechanism_bundle.py` into a temporary active
release directory. The mSCS checkout was not modified by that verification.

## Release contents

The bundle is at
`data/processed/mechanism_graph_module20_24_v2026_09_10/`.

| Artifact | Purpose |
|---|---|
| `mechanism_nodes.tsv` | mSCS-compatible node table plus curated labels and audit fields; composite labels are preserved. |
| `mechanism_node_roles.tsv` | Explicit many-to-many mSCS role assignments with provenance: ligand, receptor, transcription factor, target gene, and signaling cascade. |
| `mechanism_edges.tsv` | mSCS-compatible directed, typed, evidence-gated pathway edges plus module, context, confidence, and exportability fields. |
| `mechanism_edge_sources.tsv` | mSCS-compatible evidence provenance fields plus evidence-register IDs, source locators, summaries, limitations, and citation notes. |
| `mechanism_pathways.tsv` | Pathway-level edge, node, and evidence counts. |
| `mechanism_boundary_summary.tsv` | Aggregate view of non-exportable edge boundaries. |
| `bundle_metadata.json` | Release policy, counts, module coverage, and accuracy contract. |
| `validation_report.json` | Machine-generated graph integrity report. |

## Release counts

| Module | Register edges | Exported edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,145 | 7,630 | 4,761 |
| 21B | 8,171 | 8,089 | 8,120 | 82 |
| 22B | 10,694 | 5,726 | 10,784 | 4,968 |
| 23B | 1,230 | 1,224 | 1,674 | 6 |
| 24B | 151 | 149 | 224 | 2 |
| **Total graph** | — | **16,333** | **17,765 linked source rows** | **9,819** |

The graph contains 10,656 node labels and 8,891 pathway labels. Of the 17,765
linked evidence-source rows, 14,739 retain stable PMID, PMCID, DOI, or HTTP
locators in the release bundle; 1,450 are marked local-only or unresolved and
retain their evidence summaries and limitations without exposing local paths.

The role table contains 14,856 assignments: 10,656 baseline
`signaling_cascade` assignments, 742 `ligand`, 729 `receptor`, 288
`transcription_factor`, and 2,441 `target_gene` assignments. Role assignments are
many-to-many; a node can therefore be both a signaling-cascade participant and
a specialized endpoint. `node_type` remains the legacy single-valued mSCS
field and uses `signaling_effector` for generic relay, complex, and program
labels rather than inventing a new legacy type.

## Accuracy check

Run the exporter and validator from the repository root:

```bash
python3 scripts/export_module20_24_mechanism_graph.py
python3 scripts/validate_module20_24_mechanism_graph.py
```

The validator checks:

- unique node, edge, and source IDs;
- source/target node references;
- evidence-source references for every exported edge;
- pathway summary consistency;
- metadata count consistency; and
- absence of non-exportable edges from the traversable graph;
- role vocabulary, role provenance, role-to-node resolution, and complete
  `signaling_cascade` coverage; and
- canonical role-edge compatibility (`binds_receptor` for ligand-receptor
  edges and the three target-gene relation types for TF-target edges).

The historical v1.6.0 release passed with zero errors; the validator reported the
local-only/unresolved locator count as a warning, not as a graph-integrity
failure.

Validate the mSCS import contract with the mSCS virtual environment (which
provides its optional Parquet dependency):

```bash
rm -rf /private/tmp/mscs_module20_24_import_check
PYTHONPATH=/Users/derea/Documents/SCI/mSCS/src \
  /Users/derea/Documents/SCI/mSCS/.venv/bin/python \
  /Users/derea/Documents/SCI/mSCS/src/mscs/import_mechanism_bundle.py \
  data/processed/mechanism_graph_module20_24_v2026_09_10 \
  --mechanism-dir /private/tmp/mscs_module20_24_import_check --export-tsv
```

The verified import retained 2,787 nodes, 4,345 node-role assignments, 3,167
edges, and 4,393 evidence sources. The bundle is a mechanism snapshot, not a claim that the
register-backed labels are already canonical database entities; the metadata
therefore keeps `canonical_database_materialization=false`.

The database-side role contract is defined in
[`MECHANISM_ROLE_CONTRACT.md`](MECHANISM_ROLE_CONTRACT.md). Apply
`schema/mechanism_roles_layer.sql` after the base schema, populate roles only
from evidence-backed entity mappings (or derive the canonical edge roles with
`scripts/materialize_mechanism_roles.sql`), and run
`scripts/validate_mechanism_roles.sql` before a database-native export.

Regulon modeling is deliberately not inferred into this release. The
database-native, evidence-gated extension is documented in
[`REGULON_MODELING_LAYER.md`](REGULON_MODELING_LAYER.md) and applied through
`schema/regulon_layer.sql` when separately curated TF-target memberships are
ready.

## Interpretation boundaries

- A graph edge is exportable only because the register passed its evidence and
  curation gate; this is not a claim of universal biology or SCI-specific
  applicability.
- Non-exportable, unresolved, low-evidence, and layer-conflicted candidates
  remain summarized as boundaries and are not traversable edges.
- Composite receptor, ligand, pathway, and program labels are preserved rather
  than split into unsupported molecular claims.
- The cross-module synthesis remains an audit-layer interpretation; canonical
  database materialization and source-anchor resolution remain separate release
  gates.

The broader narrative synthesis is in
[`CROSS_MODULE_SYNTHESIS_20_24.md`](CROSS_MODULE_SYNTHESIS_20_24.md), while the
machine-readable graph contract is captured in `bundle_metadata.json`.

The PostgreSQL-materialized companion release is documented in
[`MODULE20_24_DATABASE_GRAPH_RELEASE.md`](MODULE20_24_DATABASE_GRAPH_RELEASE.md).
