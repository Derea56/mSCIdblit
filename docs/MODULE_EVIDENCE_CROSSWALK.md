# Module evidence crosswalk

The module system remains the biological organization layer. Evidence is a
separate, cross-cutting layer that can support a module, pathway, entity, or
existing mechanism edge without forcing every observation into a canonical
edge.

## Design boundary

The crosswalk is additive and lossless with respect to source provenance:

- mSCS remains authoritative for modality-native measurements and calibration.
- mSCIdblit stores an exact external source pointer and a reviewed projection.
- Protein values, replicate-level measurements, spatial scores, epigenetic
  loci, assay metadata, transformations, and missingness are not replaced by a
  single graph score.
- A crosswalk row does not create or promote a `SignalingEdge`.
- Canonical edge provenance still uses `SignalingEdgeSource` with a local
  `Paper`, `Observation`, or `AuthorClaim` anchor.

## Tables

Apply `schema/module_evidence_crosswalk.sql` after `schema/schema.sql`, then
apply `schema/evidence_observation_detail.sql`.

### `EvidenceSourceRecord`

One exact pointer to a source-system record. Typical mSCS records include a
study, dataset, assay, protein observation, epigenetic observation, spatial
claim, or source artifact.

`source_record_key` must be copied from the source system. It must not be
derived from a paper, dataset, accession, filename, or related record. The
source artifact path and SHA-256 are optional, but when present they must refer
to the exact source artifact.

`source_metadata_json` is limited to identity and provenance metadata. It is
not a replacement for the native mSCS record or its detailed measurements.

### `ModuleEvidenceLink`

This is the reviewed projection into the mSCIdblit organization. A link can
target:

| Target | Use |
|---|---|
| `module` | Evidence relevant to a module before a more specific mapping exists |
| `pathway` | Pathway-level state or contextual support |
| `pathway_member` | Evidence bearing on an entity’s membership or role |
| `entity` | Evidence about a protein, gene, receptor, TF, or other node |
| `edge` | Evidence supporting or weakening an already curated edge |

`link_role` records why the relationship exists: `member_support`,
`edge_support`, `pathway_state`, `spatial_context`, `regulatory_context`,
`contradictory_or_negative`, or `unresolved`.

### `EvidenceObservationDetail`

This table is the queryable measurement projection. It keeps the native value
and any transcribed value in separate columns, along with units, direction,
error bounds, replicate counts, timepoint, assay, cell/tissue context, source
locator, and a native source-row snapshot. It does not replace the mSCS record.

`reported_value_numeric` is populated from the native source value when one is
present; otherwise it is explicitly transcribed or digitized and its origin is
recorded in `reported_value_kind` and `measurement_status`. Rows without a
reported scalar remain qualitative or unreported rather than receiving an
inferred number.

## Modality rules

- **Protein:** link exact activation, abundance, phosphorylation, or cleavage
  observations to pathway states, entities, or exact existing edges. Do not
  infer upstream ligand/receptor causality from downstream protein state alone.
- **Epigenetic:** direct TF occupancy can support an exact TF-target edge when
  locus and claim scope are verified. Accessibility, motif enrichment,
  histone state, methylation, and m6A remain regulatory context unless the
  source establishes a narrower claim.
- **Spatial:** use same-spot, adjacent-spot, enrichment, and neighborhood
  measures as spatial context. Proximity alone does not establish binding,
  ligand-receptor activity, or causal direction. Provisional cluster labels
  must remain reported labels until identity mapping is independently verified.

## Release workflow

1. Register the exact mSCS record in `EvidenceSourceRecord` with its source
   database, record key, modality, assay, version, and artifact provenance.
2. Resolve any local paper, experiment, observation, or claim anchors without
   inventing identifiers.
3. Add one or more `ModuleEvidenceLink` rows for the distinct biological
   relationships supported by that source record.
4. Keep links in `staging`, `held`, or `screened_out` until adjudicated.
5. Mark a link `included` only after the external source is `verified` and a
   local `Paper`, `Observation`, or `AuthorClaim` anchor is present.
6. Promote an existing edge only through the existing edge/source gates. A
   module-evidence link alone never changes graph traversal.

The reproducible mSCS import currently reads the three local mSCS stores and
writes an idempotent SQL bundle plus TSV audit manifests:

```bash
python3 scripts/import_mscs_modality_evidence.py \
  --mscs-root /Users/derea/Documents/SCI/mSCS \
  --output data/processed/mscs_modality_evidence_import_v1
```

The generated import contains protein and epigenetic observation details and
the available GSE269377 spatial pilot metrics. It creates no module links,
local paper/observation/claim anchors, or canonical edge promotions until
those mappings are separately adjudicated.

The current snapshot contains 1,287 source records and 1,420 detail rows:
1,259 protein observations, 17 epigenetic observations, and 144 spatial pilot
metric rows. Protein ABC values are mapped only from explicit mSCS grade
prefixes (`A`, `B`, or `C`); all context levels remain unassigned pending
explicit L0-L4 adjudication. The spatial rows remain `derived_pilot` and use
provisional cluster labels.

Validate with:

```bash
psql -v ON_ERROR_STOP=1 -d mscidbl \
  -f scripts/validate_module_evidence_crosswalk.sql
```

The validation script rolls back its transaction, so it reports the current
state without modifying the database.
