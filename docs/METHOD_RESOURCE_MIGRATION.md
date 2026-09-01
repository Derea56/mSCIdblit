# Method-resource migration contract

`mSCIdblit` now has an additive intake layer for the frozen communication
resources used by `mSCS`. The layer centralizes provenance and canonical pair
identity without treating membership in LIANA, CellChat, or NicheNet as
biological validation.

## Confirmed frozen resources

The inspected mSCS snapshot is
`phase2_external_snapshot_2026-08-05`. It contains:

- LIANA `mouseconsensus`: 3,989 LR rows;
- CellChatDB.mouse: 3,379 interaction rows, including explicit complex and
  cofactor fields;
- NicheNet v2 mouse: a 5,668-row LR network and a dense ligand-target prior;
- a 9,099-pair mSCS union registry derived from those three LR sources.

No frozen Tensor-cell2cell resource was present in the inspected method-resource
directory. Tensor is therefore recorded as a migration gap, not projected from
an assumed source.

## Data layers

The additive schema is `schema/method_resource_layer.sql`.

- `MethodResource` records source file identity, release/version metadata,
  checksums, original format/columns, usage, and retention state.
- `CanonicalCommunicationRecord` stores the exact-string, species-scoped
  deduplicated LR identity. Normalization is whitespace trimming only; no
  synonym, orthology, or biological validation inference is performed.
- `MethodResourceRecord` preserves one row per source-resource LR record and
  its complete native fields in JSON. LIANA and NicheNet rows without a native
  source identifier use explicit generated row locators, never fabricated
  biological identifiers.
- `MethodResourceComplexComponent` stores explicit CellChat component fields.
  Components are never inferred from punctuation in a ligand or receptor name.
- `MethodResourceAnnotation` keeps pathway, cofactor, annotation, and source
  labels separate from curated evidence.
- `MethodResourceProjection` records each native-input or compatibility view.
- `MethodResourceNumericArtifact` records the NicheNet matrix path, checksum,
  dtype, layout, shape, and axes without expanding the dense matrix into a
  lossy or impractical relational table.

The method-resource layer does not create `Paper`, `Observation`,
`AuthorClaim`, `SignalingEdge`, or mechanism-edge evidence links.

## Reproducible import and benchmark

Run the importer from the mSCIdblit repository:

```bash
python3 scripts/import_method_resources.py
python3 scripts/benchmark_method_resource_equivalence.py
```

The generated artifacts are under
`data/processed/method_resource_migration_v1/`. They include the source
manifest, canonical records, source-record crosswalk, complex components,
annotations, native projections, numeric-artifact metadata, materialization
SQL, and JSON reports.

The current resource-level benchmark reports ten lossless checksum matches,
two exact checksum-pinned reference-only comparisons, zero source-only rows,
zero projection-only rows, and zero records changed by the whitespace-only
normalization. The reference-only comparisons are the large NicheNet v2
ligand-target RDS file and the 221 MiB neutral ligand-target binary matrix.

This is resource-level equivalence only. It does not claim analytical or
method-output equivalence, which additionally requires matching software
versions, parameters, and input data.

## Combined mSCS release bundle

After the mechanism graph and method-resource migration artifacts exist, build
the combined release snapshot:

```bash
python3 scripts/build_mscs_release_bundle.py
```

The resulting bundle contains the mechanism graph, method-resource intake
tables and SQL, native projections, checksums, crosswalks, transformation
reports, and migration gaps in one immutable directory. The original mSCS
files remain untouched. Large NicheNet binaries remain available through their
exact source paths and SHA-256 values until a distribution-safe artifact store
is selected.

## Migration safety

The current mSCS method resources must not be deleted or overwritten. Before
retirement, the next migration pass must:

1. place the large NicheNet binaries in a release-capable artifact store or
   otherwise provide an immutable release-pinned copy;
2. make the mSCS loader consume the combined mSCIdblit bundle;
3. run existing mSCS smoke tests against the native projections;
4. review any source/version/checksum differences; and
5. retain compatibility fields only for the documented transition period.
