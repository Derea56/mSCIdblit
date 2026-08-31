# mSCIdblit v1.2.0 canonical mechanism-graph release

This release freezes the current canonical database materialization after the
Modules 20B–24B evidence-unit and endpoint audit. It preserves independent
evidence grades and context levels, retains unresolved cases explicitly, and
exports only database-backed graph edges with source coverage.

## Release identity

- Project version: `mSCIdblit v1.2.0`
- Mechanism graph version: `v1.2.0`
- Graph release identifier: `module20_24_database_graph:v1.2.0`
- Release date: `2026-08-31`
- Frozen bundle: `data/processed/mechanism_bundle_module20_24_db_v1_2_0/`
- Prior database-backed release: `mSCIdblit v1.0.0`

## Bundle contents

| Artifact | Purpose |
|---|---|
| `mechanism_nodes.tsv` | Canonical graph nodes and labels |
| `mechanism_node_roles.tsv` | Explicit many-to-many mechanism roles |
| `mechanism_edges.tsv` | Source-covered traversable mechanism edges |
| `mechanism_edge_sources.tsv` | Paper/register provenance and evidence metadata |
| `bundle_metadata.json` | Frozen release identity, filters, and counts |

## Frozen counts

| Measure | Count |
|---|---:|
| Nodes | 3,065 |
| Node-role assignments | 4,980 |
| Edges | 3,399 |
| Edge-source rows | 10,024 |

Every exported edge has at least one source row. Node, edge, and source IDs
are unique; endpoint and source references resolve; and the bundle contains
no self-loop edges. The nine unresolved 22B endpoint cases remain in the
canonical register/evidence layer as U/L0 records and do not receive invented
graph endpoints.

## Evidence and species-field boundaries

The bundle preserves the database's evidence and provenance records. The
exporter applies only the output normalization required by the downstream
`mSCS` controlled vocabulary: explicit mouse-plus-human-comparator register
labels are represented as `mixed`, unsupported species labels remain blank,
and non-controlled confidence prose remains blank. Each raw value is retained
in the source row's `notes`; canonical database fields are unchanged.

## Validation

The release passed:

- `scripts/validate_mechanism_roles.sql`;
- `scripts/validate_mechanism_database_release.sql`;
- `scripts/validate_regulon_layer.sql`;
- the database-native bundle structural audit; and
- the `mSCS` `import_mechanism_bundle.py` contract check into an isolated
  materialization directory.

The database-native exporter is reproducible with:

```bash
python3 scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir data/processed/mechanism_bundle_module20_24_db_v1_2_0 \
  --bundle-name module20_24_database_graph \
  --graph-version 1.2.0 \
  --release-status frozen \
  --min-export-priority low \
  --require-sources
```

The additive public-TF candidate/validated layer remains separately documented
and does not silently become canonical database edges in this release. Only
rows materialized into the canonical mechanism tables are included in this
database-backed bundle.
