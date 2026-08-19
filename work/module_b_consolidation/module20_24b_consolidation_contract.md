# Module 20B–24B consolidation contract

This audit-layer contract converts the frozen A-module registers into
query-ready B-layer records without changing the A-layer source of truth.

## Shared rules

- Every B edge retains its stable A edge identifier.
- Every B evidence row retains its stable A evidence identifier and source
  locator.
- `exportable=true` requires at least one non-boundary evidence row.
- Direct molecular, receptor-proximal/pathway, downstream/function, program,
  phenotype, comparator, and negative-evidence layers remain distinct.
- Species, cell/model, compartment, injury context, confidence, and limitations
  are copied rather than inferred.
- Boundary and low-confidence records remain queryable but are excluded from
  the supported simulator edge set.
- Receptor complexes and assembled systems remain raw contextual entities until
  explicit subunit evidence is available; subunits are not inferred from
  punctuation or family names.

## Module-specific handling

| Module | B-layer treatment |
|---|---|
| 20B | Converts the 5,906 frozen LR rows into edge/source records. High- and medium-confidence frozen LR rows are exportable; low, uncertain, no-evidence, and non-LR classifications remain audit boundaries. Complex-coverage annotations are retained separately. |
| 21B | Converts receptor-proximal relay edges and evidence into pathway-graph records. It does not promote ligand-receptor evidence into intracellular relay evidence. |
| 22B | Converts TF binding, TF-target regulation, program association, and phenotype association into distinct edge layers. No-evidence TF handoffs remain boundaries. |
| 23B | Converts ECM, adhesion, and mechanotransduction edges while preserving soluble versus contact-mediated context and matrix/adhesion entities. |
| 24B | Converts complement, coagulation, kinin, lipid, and protease edges while preserving fragments, activators, receptor systems, inhibitors, and pathway/function limitations. |

## Current materialization boundary

The generated files under `work/module_b_consolidation/module20b` through
`module24b` are audit-layer TSVs. They are not yet inserted into the canonical
`SignalingEdge` or `SignalingEdgeSource` tables. SQL staging and the final
simulator bundle export are the next validation steps.
