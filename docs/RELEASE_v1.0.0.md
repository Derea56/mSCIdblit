# mSCIdblit v1.0.0 frozen mechanism-graph release

Release status: `frozen`

This is the first explicit semantic version for the database-backed mechanism
graph. The release freezes the current evidence-gated graph and its generalized
TF/regulon layer for reproducible mSCS imports.

## Version identifiers

- Project version: `mSCIdblit v1.0.0`
- Mechanism graph version: `v1.0.0`
- Graph release identifier: `module20_24_database_graph:v1.0.0`
- Git tag: `mechanism-graph-2026-08-25-generalized`
- Frozen release tag: `mSCIdblit-v1.0.0`
- Release date: `2026-08-25`

The prior date-based tag remains valid as a historical alias. The semantic tag
is the preferred reproducibility anchor for this frozen graph; its tagged
commit is the authoritative versioned source state.

## Frozen bundle

The versioned bundle is:

`data/processed/mechanism_bundle_module20_24_db_v1_0_0/`

It contains:

| Measure | Count |
|---|---:|
| Nodes | 2,792 |
| Explicit node roles | 4,358 |
| Edges | 3,172 |
| Evidence sources | 4,398 |
| Explicit TF sources with target edges | 44 |
| Unique TF-target pairs | 90 |
| Generic release-scoped regulons | 44 |

The bundle metadata records `graph_version: 1.0.0`,
`release_status: frozen`, and release ID
`module20_24_database_graph:v1.0.0`.

## Reproducible export

```bash
python3 scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir data/processed/mechanism_bundle_module20_24_db_v1_0_0 \
  --require-sources \
  --bundle-name module20_24_database_graph \
  --graph-version 1.0.0 \
  --release-status frozen
```

The database release gates and the mSCS import were passed before freezing this
release. Future evidence additions should increment the graph version and
produce a new bundle rather than modifying this snapshot in place.
