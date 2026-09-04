# Module 22B materialization status

This document consolidates the historical 2026-08-26 canonical-materialization
report with the current 2026-09-03 register-backed materialization instructions.
The register-backed stage is the current working entrypoint; the earlier
canonical snapshot is retained below as historical provenance.

## Current register-backed stage

The stage is built from the current Module 22B working registers:

- `work/module_b_consolidation/module22b/module22b_edge_register.tsv`
- `work/module_b_consolidation/module22b/module22b_evidence_register.tsv`

The current stage contains 4,178 unique human or mouse `target_gene` pairs:
2,462 human and 1,716 mouse. Eighty exportable target-gene rows without an
explicit species remain in the working registers but are excluded by the
species-aware materialization gate. Program, phenotype, unresolved, and
no-evidence-boundary rows are not silently converted into target-gene edges.

The stage includes 3,761 source-register `high` rows and 417 `medium-high`
rows. It records 3,941 rows with PMID evidence and 4,178 with an external
public-record key. The canonical confidence field is `medium`, while source
confidence and limitations remain in the notes.

## Historical canonical snapshot

The 2026-08-26 write recorded 221 unique reviewed TF-target pairs: 167 human
and 54 mouse. It represented 198 species-qualified TF entries, 191 normalized
TF symbols, 200 pairs with at least one corroborating PMID, and 21 primary-only
pairs with explicit limits. The write added 220 new canonical target-gene edge
rows because one exact edge already existed; all 221 memberships remained in
the canonical regulon layer.

That snapshot passed entity-role, regulon-layer, and canonical-release
validation. It did not overwrite the frozen v1.0 release bundle. These counts
describe the historical snapshot and should not be substituted for the current
register-backed stage counts above.

## Reproduction and boundaries

Build the current stage with:

```text
python3 scripts/build_module22b_register_materialization_stage.py
```

Generate SQL without a database write with:

```text
python3 scripts/materialize_module22b_tf_promotions.py --dry-run
```

The write step remains separate and explicitly invoked. General TF-target
evidence does not establish that a particular Module 22A ligand/receptor route
activated the TF in an SCI receiver cell. Receptor-complex ambiguity, species,
model, polarity, program-level, and target-gene limitations remain explicit in
the working registers.
