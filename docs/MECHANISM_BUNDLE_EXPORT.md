# Mechanism Bundle Export for `mSCS`

`mSCIdblit` is the curation source of truth. `mSCS` should consume exported graph bundles rather than querying the database directly.

## Purpose

The export command materializes four simulator-facing files:

- `mechanism_nodes.tsv`
- `mechanism_node_roles.tsv`
- `mechanism_edges.tsv`
- `mechanism_edge_sources.tsv`

plus:

- `bundle_metadata.json`

This preserves:

- edge-level pathway structure
- node-level gene and compartment identity
- explicit many-to-many ligand, receptor, transcription-factor, target-gene,
  and signaling-cascade roles
- source-level provenance for mouse, human, or mixed support
- release-level supported-pathway metadata for clean replacement in `mSCS`

The bundle's `species_support` and `confidence_tier` fields use the controlled
vocabularies enforced by the `mSCS` importer. Register-backed provenance may
contain source-specific free text, so the exporter normalizes only values that
cannot be represented in those vocabularies and preserves the exact raw value
in the row's `notes`. Explicit `mouse; human comparator` and
`mouse;human comparator` labels map to `mixed`; unsupported species labels
(for example, `zebrafish`) remain blank rather than being assigned a false
mouse or human category. Non-controlled confidence prose also remains blank
with its raw value retained in `notes`. Canonical database fields are not
modified by this export normalization.

Apply `schema/mechanism_roles_layer.sql` and
`schema/mechanism_register_layer.sql` after `schema/schema.sql` before using
the database-native loader/exporter. `SignalingEntityRole` is the role authority;
`SignalingEntity.entity_type` remains a legacy single-valued compatibility
field. After loading canonical `SignalingEntity` and `SignalingEdge` rows, run
`scripts/materialize_mechanism_roles.sql`, then run the role release gate before
export:

```bash
psql "$MSCIDBLIT_DATABASE_URL" -v ON_ERROR_STOP=1 \
  -f /Users/derea/Documents/SCI/mSCIdblit/scripts/validate_mechanism_roles.sql
```

For a validated TSV graph release, use
`scripts/load_mechanism_graph_bundle.py`. It resolves endpoints by stable bundle
node IDs, preserves register evidence in `SignalingEdgeRegisterSource`, and
does not fabricate `Paper`/`Observation` foreign keys for unresolved source
anchors.

## Export Script

Use:

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/export_mechanism_bundle.py --database-url "$MSCIDBLIT_DATABASE_URL"
```

## Combined method-resource release

`export_mechanism_bundle.py` remains the database-backed graph exporter. To
package that graph with the canonical method-resource intake and native
projections, first run the method-resource importer and then use:

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/build_mscs_release_bundle.py \
  --graph-bundle-dir /Users/derea/Documents/SCI/mSCIdblit/data/processed/mechanism_graph_module20_24_v2026_09_01 \
  --method-migration-dir /Users/derea/Documents/SCI/mSCIdblit/data/processed/method_resource_migration_v1 \
  --output-dir /Users/derea/Documents/SCI/mSCIdblit/data/processed/mscs_release_bundle_v1_4_0_method_resources_v1
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/validate_mscs_release_bundle.py
```

The combined bundle contains the graph snapshot and method-resource tables,
native projections, checksums, crosswalks, and migration reports. Configure an
mSCS transition run to read native resources from its
`method_resources/method_native/` directory after the resource-level benchmark
passes. The current bundle still records the large NicheNet RDS and neutral
matrix as exact source references; it is not yet a self-contained replacement
for the mSCS NicheNet scoring resource.

## Recommended Strict Mouse-First Export

For the first `mSCS` astrocyte transition build, start with a conservative bundle:

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/export_mechanism_bundle.py \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output-dir /Users/derea/Documents/SCI/mSCIdblit/data/processed/mechanism_bundle_strict_mouse \
  --species-support mouse \
  --species-support both \
  --cell-type-context astrocytes \
  --min-export-priority medium \
  --require-sources \
  --bundle-name astro_strict_mouse_v1
```

## Filters

- `--species-context`: filters `SignalingEdge.species_context`
- `--species-support`: filters `SignalingEdgeSource.species_support`
- `--cell-type-context`: filters `SignalingEdge.cell_type_context`
- `--injury-context`: filters `SignalingEdge.injury_context`
- `--pathway-name`: filters `SignalingPathway.pathway_name`
- `--min-export-priority`: keeps `high`, `medium`, or `low` edges and drops weaker rows
- `--require-sources`: excludes edges that do not retain any source rows after filtering

## Output ID Rules

The exporter rewrites numeric database identifiers into stable simulator bundle IDs:

- nodes: `NODE00001`
- edges: `EDGE00001`
- edge sources: `SRC00001`

This keeps simulator bundles self-contained while preserving `paper_id`, `observation_id`, and `claim_id` as traceable back-references.

## Release Replacement Rule

Treat each mechanism bundle as an authoritative supported-pathway snapshot for one `mSCIdblit` release.
When a later export contains a larger or cleaner pathway set, `mSCS` should replace the previous supported set wholesale on import rather than carrying forward stale edges from older bundles.

## Scientific Boundaries

- Do not collapse mouse and human support into one unlabeled edge.
- Do not export tracker prose directly into the simulator.
- Do not treat review-only support as equivalent to primary experiment support.
- If a pathway step is only supported in human, preserve that fact in `mechanism_edge_sources.tsv`.
- If a curation pass has not yet produced explicit `SignalingEdgeSource` rows, prefer `--require-sources` for strict exports so weakly anchored edges do not silently enter simulation.
