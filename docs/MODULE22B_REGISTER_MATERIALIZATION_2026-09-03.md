# Module 22B register-backed materialization stage — 2026-09-03

The current Module 22B materialization stage is built from the working
registers, not from the earlier 221-row public-TF staging lanes:

- `work/module_b_consolidation/module22b/module22b_edge_register.tsv`
- `work/module_b_consolidation/module22b/module22b_evidence_register.tsv`

Run the stage builder with:

```text
python3 scripts/build_module22b_register_materialization_stage.py
```

It writes the ignored stage directory
`work/module22b_consolidation/materialization_round_register_2026_09_03/`.
The stage contains 4,178 unique human or mouse `target_gene` pairs: 2,462
human and 1,716 mouse. The 80 exportable target-gene rows without an explicit
species remain in the working registers but are excluded from canonical
materialization because the write gate requires species-aware endpoints.
Program, phenotype, unresolved, and no-evidence-boundary rows are not silently
converted into target-gene edges.

The stage includes 3,761 source-register `high` rows and 417 `medium-high`
rows. Its canonical confidence field is `medium`, preserving the source
register confidence and limitations in `notes`. Of the staged rows, 3,941
have PMID evidence and 4,178 have an external public-record key. The latter
allows signed database-curated support to remain queryable without fabricating
a PubMed citation.

The write script reads `module22b_materialization_manifest.json` and derives
the expected row count and materialization version from that manifest. A safe
SQL-generation check is:

```text
python3 scripts/materialize_module22b_tf_promotions.py --dry-run
```

No PostgreSQL write is performed by the stage builder or by the dry run.
Canonical writes remain a separate, explicitly invoked operation.
