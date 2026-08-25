# Module 20B–24B NFKB1 database graph correction

Release identifier: `module20_24_database_graph_nfkb1:2026-08-25`

This is a database-backed companion release that corrects the TNF–NF-kappaB
branch without replacing the original register-backed source records.

## Release bundle

The bundle is at
`data/processed/mechanism_bundle_module20_24_db_v2026_08_25_nfkb1/`.

| Measure | Count |
|---|---:|
| Nodes | 2,792 |
| Explicit node roles | 4,358 |
| Edges | 3,172 |
| Evidence sources | 4,398 |
| NFKB1 core target-gene edges | 17 |
| NFKB1 regulon memberships | 17 |

Role counts are 2,792 `signaling_cascade`, 725 `ligand`, 706 `receptor`, 52
`transcription_factor`, and 83 `target_gene` assignments. Roles are
many-to-many, so a target gene can also retain another role such as ligand.

## Validation

The local PostgreSQL database passed:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f scripts/validate_mechanism_roles.sql \
  -f scripts/validate_mechanism_database_release.sql \
  -f scripts/validate_regulon_layer.sql \
  -f scripts/validate_nfkb1_core_regulon.sql
```

The bundle was imported into mSCS in a temporary release directory with 2,792
nodes, 4,358 node-role assignments, 3,172 edges, and 4,398 evidence sources.

## Interpretation boundary

The corrected graph contains:

```text
TNF → TNFR1/TNFR2 → IKK-NFKB1-RELA → NFKB1 → core target genes
```

The receptor-to-composite edge is `supports_cascade`, and the composite-to-TF
edge is `contains_component`; neither is a direct TNFR-to-NFKB1 activation or
binding claim. The 17-gene NFKB1 core summary is human, literature-curated,
and not exhaustive or TNF-specific. Conflicting target modes are retained as
context-dependent.

See [`NFKB1_TNF_LAYER.md`](NFKB1_TNF_LAYER.md) for the query and
[`REGULON_MODELING_LAYER.md`](REGULON_MODELING_LAYER.md) for the general
signal-to-regulon contract.
