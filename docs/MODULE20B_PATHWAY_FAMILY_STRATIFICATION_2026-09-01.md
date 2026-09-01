# Module 20B pathway-family stratification — 2026-09-01

Module 20B currently uses one broad register pathway label because it is a
ligand–receptor intake layer. This review layer organizes the register into
conservative receptor-family groupings without changing the register or
promoting downstream mechanisms.

## Scope and policy

The reproducible classifier is
`scripts/stratify_module20b_pathway_families.py`. It reads
`work/module_b_consolidation/module20b/module20b_edge_register.tsv` and writes:

- `data/processed/module20b_pathway_family_layer_v1/module20b_pathway_family_layer.tsv`
- `data/processed/module20b_pathway_family_layer_v1/module20b_pathway_family_layer_summary.json`

An edge receives a family grouping only when it is in the direct molecular
evidence layer, has medium or high confidence, and its registered receptor
endpoint has an explicit family-defining nomenclature. All other rows are
assigned `pathway_not_established`.

The family labels are organizational labels, not claims that the cited source
demonstrated a complete downstream pathway. ABC evidence grades, L0–L4 context
levels, exportability, and all source provenance remain unchanged. No relay,
transcription-factor/program, cellular-output, or SCI-context claim is inferred.

## Current families

- TGF-beta/BMP receptor family
- Cytokine receptor family
- Notch receptor family
- Hedgehog receptor family
- WNT/Frizzled receptor family
- Innate-immune receptor family
- RTK growth-factor receptor family
- GPCR receptor family
- ECM/integrin adhesion receptor family
- Axon-guidance/adhesion receptor family
- Synaptic/cell-adhesion receptor family
- Scavenger/uptake-associated receptor family
- Purinergic/neuroreceptor family
- Pathway not established

This layer should be reviewed before changing the graph's `pathway_name`
values. If accepted, the next graph export can use these family labels while
retaining a separate field or note that they are receptor-family groupings,
not fully adjudicated downstream cascades.
