# Release pathway queries

`query_pathway.py` provides a read-only query path over a materialized
mSCIdblit PostgreSQL release. It executes one SQL statement and returns a JSON
object containing separate layers for:

- canonical pathways, entities, roles, and pathway membership;
- traversable mechanism edges and both forms of edge provenance;
- cross-cutting external evidence links and modality-native observations;
- canonical method-resource communications, exact native records, and
  method-native annotations.

The query does not alter the database, create edges, promote evidence, or
collapse method-resource membership into biological validation.

## Example

```bash
python3 /Users/derea/Documents/SCI/mSCIdblit/scripts/query_pathway.py IL1B \
  --database-url "$MSCIDBLIT_DATABASE_URL" \
  --output /tmp/mscidblit_il1b_query.json
```

The query term is a case-insensitive literal substring. For example, `IL1B`
matches release entities and observations containing `IL1B` or `Il1b`, and
method-resource records whose canonical ligand/receptor fields or annotations
contain that term. SQL wildcard characters are not interpreted as wildcards;
the utility safely quotes the term before sending the single statement to
`psql`.

By default, the command also scans only these known local public-TF staging
files and returns matching rows under `staged_public_tf`:

- `data/processed/public_tf_union_v1/module_curation/new_tf_materialized/priority_tf_agent_decisions.tsv`
- `data/processed/public_tf_union_v1/source_regulon_members.tsv`

Those rows are explicitly labeled `staged_evidence_only` and
`not_materialized_by_this_query`. Use `--no-local-staging` for a release-only
query. The local scan is bounded per file with `--max-staged-rows` (default
1000) and reports when truncation occurs.

The command also scans the two exact modality-import snapshots and returns
matching rows under `local_evidence_snapshots`:

- `data/processed/mscs_modality_evidence_import_v1/evidence_source_records.tsv`
- `data/processed/mscs_modality_evidence_import_v1/evidence_observation_details.tsv`

These are labeled `local_import_snapshot`. They are separate from
`modality_observations`, which reports rows actually present in the database.
This distinction is important for v1.4.0: the schema is present in the dump,
but the modality import rows remain in the exact local snapshots. Use
`--no-local-evidence` to omit them; `--max-local-evidence-rows` bounds the
returned rows per file. The local snapshots are not silently merged into the
database result.

## Output semantics

`mechanism_edges` are canonical release graph rows. Their linked
`mechanism_edge_sources` and `register_evidence` retain evidence tier,
species/context scope, source locator, limitations, and release flags.

`linked_external_evidence` and `modality_observations` expose the additive
crosswalk and measurement layers. Numeric values remain in their native,
reported, or transcribed fields, and the imported `native_fields_json` snapshot
is retained in the result. Matching also checks that native snapshot so a
canonical symbol such as `IL1B` can retrieve a source row recorded as
`IL-1beta` or another source-native label without renaming the stored value.
These records do not become graph edges.

`local_evidence_snapshots` is a transparent fallback for exact imported
evidence that has not yet been materialized into the queried database. It is
not merged into the database result or presented as a release-table row.

`method_communications`, `method_resource_records`, and
`method_resource_annotations` preserve the tool-input layer. Their presence
means that a resource contains a relationship or annotation, not that
mSCIdblit has independently validated the biology.

The JSON includes per-layer counts so callers can distinguish an empty result
from a query layer that was not requested. The database URL is never included
in the output.

## Tests

The unit tests cover read-only SQL construction and the bounded staging scan:

```bash
python3 -m pytest /Users/derea/Documents/SCI/mSCIdblit/tests/test_query_pathway.py
```
