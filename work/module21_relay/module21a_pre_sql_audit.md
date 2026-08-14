# Module 21A pre-SQL audit

Date: 2026-08-14

## Result

`PASS` for audit-layer staging. SQL materialization remains deferred.

## Counts

- Main saturation register: 102 edges, 46 grouped evidence records, 51 perturbations.
- Separate Q001 seed packet: 8 edges, 4 evidence records, 3 perturbations.
- Combined edge packet: 110 unique edges.
- Evidence-layer register: 45 rows.
- Unresolved register: 10 explicit cases.
- Evidence layers: 21 receptor-proximal relay rows and 24 downstream pathway/function rows.
- Edge classes: 6 direct molecular, 22 receptor-complex/pathway, and 17 functional-output rows.

## Checks passed

- Main and seed edge IDs are unique across both packets.
- Main, seed, evidence-layer, perturbation, and unresolved identifiers are unique within their registers.
- Every main and seed edge has supporting evidence.
- Every main edge has a valid evidence-layer row with a valid evidence ID.
- Every evidence record points only to an existing edge.
- Cross-packet edge keys are unique using source, relation, target, pathway, ligand context, cell-type context, and species context.
- Direct molecular, receptor-complex/pathway, and functional-output classes remain distinct.
- Receptor-complex and pathway nodes remain explicit; no pathway or function record was promoted to a direct molecular interaction.
- All nine queue items remain explicitly marked `completed_bounded`.
- Module 20A node reconciliation is read-only and recorded separately; no Module 20A ledger or classification was changed.
- Frozen Module 20A manifest SHA-256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Staging posture

The audit layer is ready for a reviewable SQL staging design, but unresolved receiver-state branches, composite receptor semantics, and Module 20A node aliases must remain attached as qualifiers. No simulator-facing SQL rows have been created.

