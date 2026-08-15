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

## Current extraction progress

After batches 180–181, all 5,906 frozen Module20A pairs remain represented in
the audit coverage and Module22A handoff tables. The current audit layer has
2,106 reusable pathway groups and 4,422 detailed evidence records. Exactly
4,501 pairs have been reviewed and 1,405 remain queued; 170 pair-level rows
carry provisional terminal-TF candidates for separate Module22A validation.

Batches 176–177 added 50 reviewed rows: 34 relay candidates, 2 binding-only
rows, 8 explicit no-evidence boundaries, and 6 unresolved rows. Batches 178–179
added a further 50 reviewed rows: 36 relay candidates, 5 binding-only rows,
1 function-only row, 7 explicit no-evidence boundaries, and no unresolved rows.
Eight
provisional TF handoffs are now represented in these two batch windows:
STAT3 for IL10–IL10RA/IL10RB; RELA/p65 for RETN–TLR4, S100A8–TLR4,
S100A9–TLR4, and SAA1–TLR2; TCF/LEF for RSPO1/3–FZD8; and NFATC1 for
SEMA6A–PLXNA2. Batches 180–181 added a further 50 reviewed rows: 20 relay candidates, 3
binding-only rows, 3 function-only rows, 11 explicit no-evidence boundaries,
and 10 unresolved rows. No new terminal-TF assignment was added. The batch
evidence includes FGF receptor-specificity, FGG–integrin, irisin–integrin,
GDF/BMP/Activin receptor-complex, GDF15–GFRAL, HGF–MET, IL-10/IL-17/IL-20/IL-1/
IL-25, TNF/TNFSF, VEGF/WNT, and INHBC boundary cases. Receptor-complex,
pathway, and functional outputs remain distinct, and no direct molecular edge
was inferred from a pathway-only or functional-only result.
