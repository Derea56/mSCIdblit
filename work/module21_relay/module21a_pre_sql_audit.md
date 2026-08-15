# Module 21A pre-SQL audit

Date: 2026-08-14

## Result

`PASS` for audit-layer staging. SQL materialization remains deferred.

## Counts

- Main saturation register: 111 edges, 54 grouped evidence records, and 54 perturbations.
- Evidence-layer register: 111 one-to-one edge assignments.
- Unresolved register: 20 explicit cases.
- Evidence layers: 70 receptor-proximal relay, 35 downstream pathway/function, and 6 ligand-receptor binding/activation assignments.
- Edge classes: 23 direct molecular, 17 receptor-complex/pathway, 52 pathway-complex, and 19 functional-output rows.

## Checks passed

- Main and seed edge IDs are unique across both packets.
- Main, seed, evidence-layer, perturbation, and unresolved identifiers are unique within their registers.
- Every main and seed edge has supporting evidence.
- Every edge has exactly one evidence-layer row with a valid evidence ID.
- Every evidence record points only to an existing edge.
- Cross-packet edge keys are unique using source, relation, target, pathway, ligand context, cell-type context, and species context.
- Direct molecular, receptor-complex/pathway, and functional-output classes remain distinct.
- Receptor-complex and pathway nodes remain explicit; no pathway or function record was promoted to a direct molecular interaction.
- All ten queue items were independently reviewed; queue status remains `ACTIVE_SATURATED_FIRST_PASS` pending final export/materialization approval.
- Four independent read-only accuracy reviews covered Q001-Q010. Corrections narrowed receptor/kinase claims, corrected species and assay boundaries, demoted unsupported directness, and added unresolved cases for unresolved SCI receiver and paralog branches.
- Mixed evidence records now use `source_scope=pathway_membership` when they span direct, receptor-complex, pathway, or functional layers; the evidence-layer register remains the edge-level classification authority.
- Module 20A node reconciliation is read-only and recorded separately; no Module 20A ledger or classification was changed.
- Frozen Module 20A manifest SHA-256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Staging posture

The audit layer is ready for a reviewable SQL staging design, but unresolved receiver-state branches, composite receptor semantics, and Module 20A node aliases must remain attached as qualifiers. No simulator-facing SQL rows have been created.
