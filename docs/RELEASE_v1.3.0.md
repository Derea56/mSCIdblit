# mSCIdblit v1.3.0 evidence-expanded mechanism-graph release

This release freezes the current canonical database materialization after the
Module 20B–24B artifact-provenance promotion pass. It expands exact paper,
experiment, observation, claim, link, and edge-source coverage while
preserving the existing graph topology and every ABC evidence grade and L0–L4
context level.

## Release identity

- Project version: `mSCIdblit v1.3.0`
- Mechanism graph version: `v1.3.0`
- Graph release identifier: `module20_24_database_graph:v1.3.0`
- Release date: `2026-08-31`
- Frozen bundle: `data/processed/mechanism_bundle_module20_24_db_v1_3_0/`
- Prior database-backed release: `mSCIdblit v1.2.0`

## Canonical bundle counts

| Measure | v1.2.0 | v1.3.0 | Change |
|---|---:|---:|---:|
| Nodes | 3,065 | 3,065 | 0 |
| Node-role assignments | 4,980 | 4,980 | 0 |
| Traversable graph edges | 3,399 | 3,399 | 0 |
| Edge-source rows | 10,024 | 12,213 | +2,189 |

The edge topology is intentionally unchanged: this pass added verified
provenance and source-defined evidence units to existing register-backed
relationships. It did not invent new graph endpoints or convert unresolved
rows into edges. The edge-source count is 21.8% higher than v1.2.0.

## Promotion result

The local artifact adjudication bridge identified 580 unique extraction IDs
with `supporting_validated_claim`. Of these, 444 were already represented in
canonical source notes and 136 were novel. Exact content-level BioC and HTML
metadata recovery admitted 65 of the 136 novel extraction IDs to the Phase-2
materializer. The resulting local database write added:

- 38 exact `Paper` records;
- 65 source-defined `Experiment` records;
- 65 `Observation` records;
- 65 `AuthorClaim` records;
- 65 `EvidenceLink` records; and
- 128 `SignalingEdgeSource` records, including paper-anchored provenance and
  Phase-2 source-unit links.

The remaining 71 novel supporting extraction IDs remain staged because their
canonical Paper anchors cannot yet be materialized from exact local source
metadata. They are not discarded and no identifiers were inferred.

## Public-TF companion layer

The release bundle includes the reviewed public-TF evidence layer as an
explicit noncanonical companion:

- 4,174 reviewed candidate rows across A–E evidence tiers;
- 3 explicitly adjudicated validated-edge candidates representing 2 unique
  mouse TF–target pairs; and
- D/E, unresolved, catalog-only, and noncanonical rows retained as
  non-traversable evidence rather than canonical database edges.

The public-TF layer preserves its independent evidence tier and context-level
fields. Its candidate relationships are not silently merged into the
canonical database graph. The three validated candidates remain available for
an explicitly separate graph-overlay decision.

## Validation

The release passed:

- `scripts/validate_mechanism_roles.sql`;
- `scripts/validate_mechanism_database_release.sql`;
- `scripts/validate_regulon_layer.sql`;
- `scripts/validate_nfkb1_core_regulon.sql`; and
- the database export reference audit for node, role, edge, source, and
  source-to-edge relationships.

The reproducible export is:

```bash
python3 scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir data/processed/mechanism_bundle_module20_24_db_v1_3_0 \
  --bundle-name module20_24_database_graph \
  --graph-version 1.3.0 \
  --release-status frozen \
  --min-export-priority low \
  --require-sources
```

The raw artifact archive remains local working material and is not included
in the public release. Unresolved and low-tier evidence remains queryable in
the database and staging ledgers for later screening.
