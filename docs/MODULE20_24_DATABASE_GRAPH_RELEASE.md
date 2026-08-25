# Module 20B–24B database-backed graph release

Release identifier: `module20_24_database_graph_final:2026-08-25`

This is the final database-backed companion to the register-backed Module
20B–24B graph. It was materialized into PostgreSQL, passed the database role
gate, exported through `scripts/export_mechanism_bundle.py`, and imported into
mSCS.

## Release bundle

The bundle is at
`data/processed/mechanism_bundle_module20_24_db_v2026_08_25/`.

| Measure | Count |
|---|---:|
| Database entities | 2,784 |
| Explicit role assignments | 4,333 |
| Database pathways | 945 |
| Database edges | 3,151 |
| Register edge mappings | 3,151 |
| Register evidence rows | 4,377 |

Role counts are 2,784 `signaling_cascade`, 725 `ligand`, 706 `receptor`, 51
`transcription_factor`, and 67 `target_gene` assignments. The roles are
many-to-many, so the baseline cascade role coexists with specialized roles.

## Database setup and release sequence

Apply the base schema and migrations in this order:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 -f schema/schema.sql
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 -f schema/mechanism_roles_layer.sql
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 -f schema/mechanism_register_layer.sql
```

Load the validated register-backed graph, then derive any missing canonical
roles and run both release gates:

```bash
python3 scripts/load_mechanism_graph_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL"
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/materialize_mechanism_roles.sql
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/validate_mechanism_roles.sql
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/validate_mechanism_database_release.sql
```

Export the database-backed mSCS bundle:

```bash
python3 scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir data/processed/mechanism_bundle_module20_24_db_v2026_08_25 \
  --require-sources \
  --bundle-name module20_24_database_graph_final
```

The database graph preserves register evidence in
`SignalingEdgeRegisterSource`. Those register IDs are emitted as
`REGISTER:<evidence_id>` provenance anchors in the mSCS edge-source file; they
are not fabricated `Paper`, `Observation`, or `AuthorClaim` foreign keys.

## Integrity boundary

Sixteen self-loop register rows are retained as non-exportable boundaries. The
normalized database requires distinct source and target entities, so these rows
are never inserted into `SignalingEdge` or the traversable mSCS bundle.
