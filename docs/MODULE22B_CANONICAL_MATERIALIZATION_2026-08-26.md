# Module 22B canonical materialization — 2026-08-26

The evidence-backed public TF-target review set was promoted from staging into
the local canonical database after identity, role, regulon, and release gates
were run.

## Materialized scope

The write combines the completed new-TF evidence lane with the previously
reviewed priority and batch lanes. Overlapping pair rows were deduplicated by
species, TF symbol, and target symbol.

| Measure | Count |
|---|---:|
| Unique promoted TF-target pairs | 221 |
| Human pairs | 167 |
| Mouse pairs | 54 |
| Species-qualified TF entries | 198 |
| Normalized TF symbols | 191 |
| Pairs with at least one corroborating PMID | 200 |
| Primary-only pairs retained with explicit limits | 21 |
| Staged polarity conflicts resolved conservatively as context-dependent | 10 |

The 154-pair completed new-TF lane contributes 154 of the unique pairs. The
remaining 67 pairs come from earlier priority and batch review lanes; 24 of
those were overlapping priority/batch records and were retained once.

## Canonical write

The write added or reused canonical endpoint identities and explicit roles,
then created the following queryable layers:

| Layer | Result |
|---|---:|
| New endpoint identities | 373 |
| New/updated TF or target roles | 369 |
| Species-qualified Module 22B regulons | 198 |
| Supported Module 22B regulon members | 221 |
| Primary/corroborating regulon source rows | 425 |
| Canonical target-gene edge rows added | 220 |

One pair reused an existing exact canonical target-gene edge; therefore 221
stage mappings correspond to 220 newly allocated edge IDs. All 221 reviewed
memberships remain represented in the canonical `Regulon` layer.

Canonical confidence is `medium`/reasonable rather than universal high
confidence. Pair-level primary evidence, corroboration where available,
species, context, polarity conflicts, and abstract-level limitations remain
explicit. TF-target membership does not infer upstream ligand or receptor
activation.

## Validation

The following gates passed with zero issues:

- mechanism entity-role validation;
- regulon-layer validation;
- canonical database release validation.

The frozen v1.0 release bundle was not overwritten. The new post-22B snapshot
contains 3,057 nodes, 4,964 node roles, 3,392 edges, and 4,930 edge-source
records.

## Comparison with initial public databases

The initial snapshot contains 20,156 simple TF-target pairs in human TRRUST +
OmniPath/DoRothEA and 19,087 in mouse. The reviewed Module 22B layer overlaps
167 human pairs and 54 mouse pairs, corresponding to 0.8% and 0.3% of the
respective broad initial pair inventories. These percentages are discovery
coverage comparisons, not biological completeness scores.

See the reproducible [Module 22B database comparison](../data/processed/module22b_database_comparison_v1/MODULE22B_DATABASE_COMPARISON_V1.md)
and its [JSON summary](../data/processed/module22b_database_comparison_v1/comparison_summary.json).

## Reproduction inputs

- [normalized 22B write stage](../work/module22b_consolidation/materialization_round_2026_08_26/module22b_promoted_pairs.tsv)
- [stage manifest](../work/module22b_consolidation/materialization_round_2026_08_26/module22b_materialization_manifest.json)
- [stage builder](../scripts/build_module22b_materialization_stage.py)
- [materialization script](../scripts/materialize_module22b_tf_promotions.py)
- [post-22B canonical bundle](../data/processed/mechanism_bundle_module20_24_22b_db_v2026_08_26/)
- [pre-write PostgreSQL backup](/private/tmp/mscidblit_22b_prewrite_20260826.dump)
