# Module 21A LR handoff and extraction scope

Generated from frozen LR manifest `module20a-lr-release-2026-08-14` at
`2026-08-14T13:01:57+00:00`.

## Frozen Module 20A boundary

- Comparison universe: **6116** rows
- Source-backed LR union: **5906** unique pairs
- Comparison-only rows excluded from LR release: **210**
- CellChat-full pairs: **3379**
- LIANA-consensus pairs: **3989**
- Source commit: `83cef801a7e0436916f0623e0c33a46df9050908`

The frozen LR release is an input boundary for Module 21A. It does not imply
that a ligand–receptor pair activates every downstream relay edge. Module 21A
must separately extract intracellular evidence and preserve assay, species,
cell-model, branch, and perturbation context.

## Existing seed

The first-pass Module 21A packet contains 57 relay edges, 14 grouped evidence
records, and 17 perturbation records across nine priority families. It remains
an audit-layer seed until node identity and branch semantics are reconciled.

## Extraction order

1. Reconcile receptor-complex names in the Module 20A release with Module 21A
   receptor entry nodes.
2. Extract primary evidence for the explicit family gaps in
   `module21a_extraction_queue.tsv`.
3. Keep direct molecular edges separate from pathway-complex and functional
   output edges.
4. Record negative or boundary evidence explicitly; do not fill gaps by
   pathway analogy.
5. Materialize SQL only after the evidence and node-identity audit passes.

The queue is intentionally family-level for this pass. Each extracted edge
should retain a stable evidence ID and link back to the LR snapshot only as
its upstream receptor/ligand context.
