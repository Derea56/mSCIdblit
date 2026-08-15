# Module 21A batch 072 review summary

## Scope

- Exact review IDs reviewed: `M20A-CELLCHAT-REMAINING-1193` through `M20A-CELLCHAT-REMAINING-1217`.
- The queue has an ordinal/index mismatch: physical rows 1101–1125 are Glu/SLC1A6–SLC1A7 entries, while the explicit review-ID range requested here is the H2-M/H2-O/H2-Q partition. This batch follows the explicit review-ID range and contains exactly 25 rows.
- Scope: H2-M11, H2-M2, H2-M5, H2-M9, H2-Oa, H2-Q1, H2-Q10, H2-Q2, H2-Q4, H2-Q6, and H2-Q7 paired with Cd8a, Cd8b1, or Kir3dl1 as present in the frozen queue.

## Disposition

- `reviewed_relay_candidate`: 0
- `reviewed_function_only`: 1 (`H2-Oa–Cd4`)
- `reviewed_binding_only`: 2 (`H2-Q10–Cd8a`, `H2-Q10–Cd8b1`)
- `reviewed_unresolved`: 22
- Terminal TF assignments: 0

## Evidence findings

1. H2-Q10 is the only submitted ligand with an exact positive CD8 binding result. Primary mouse studies show H2-Q10 tetramer binding to liver CD8alpha/beta T cells and ART2.2/NAD-dependent binding in CD8 transfectants, with a demonstrated CD8beta requirement. This was retained as binding-only; the assay does not establish a CD8A- or CD8B1-isolated relay or terminal TF.
2. H2-Oa is an obligate alpha-chain component of the H2-O/H2-Ob nonclassical MHC-II complex. Targeted H2-Oa loss changes MHC-II peptide editing and CD4 single-positive thymocyte selection, so the exact pair has functional-output evidence. The evidence is not direct H2-Oa–CD4 binding and was not promoted to a receptor-proximal relay.
3. H2-Q7 has exact primary evidence for a Q7-encoded Qa-2 alpha3-domain defect in CD8 binding and CD8-dependent CTL activation, plus Qa-2-family dependence of CD8alphaalpha intestinal IEL selection. These are negative/complex-level boundaries rather than a positive mature H2-Q7–mouse CD8A edge; the row remains unresolved.
4. H2-M2 surface expression, H2-M5/H2-M-region classification, and H2-M9/H2-M11 H2-Mv/VNO association were retained as context only. V2R association, expression, antigen presentation, and generic MHC-I/CD8 family evidence were not converted into direct CD8 edges.
5. KIR3DL1 evidence is human and HLA-Bw4-specific. No mouse H2-Q1, H2-Q2, H2-Q4, H2-Q6, or H2-Q10 cross-species KIR3DL1 binding or exact receptor-expression/perturbation study was found.

## Search boundaries

Searches covered exact H2 gene names and aliases, PubMed, PMC, publisher pages, mouse MHC-Ib/Qa-2/H2-Mv literature, recombinant protein and cell-adhesion assays, tetramer/SPR studies, targeted mouse perturbations, and human KIR3DL1/HLA-Bw4 controls. Family-level annotations, co-expression/cell-chat outputs, generic pathway assignments, and cross-species receptor results were retained only to document limitations and were not promoted to direct molecular edges.

## Validation

- Exactly 25 data rows; one row per requested review ID.
- Review IDs unique.
- Queue IDs and canonical pair labels match the frozen queue for all 25 rows.
- All required TSV fields are populated.
- No terminal TF assignments were made.
- Shared Module 21A registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.

## Files changed

- `work/module21_relay/module21a_batch072_review.tsv`
- `work/module21_relay/module21a_batch072_summary.md`

## Stable primary citations used

- PMID 34478713 / PMCID PMC8517849 — H2-Q10 binding to CD8alpha/beta with ART2.2/NAD and CD8beta dependence.
- PMID 31992596 — defined murine MHC-Ib/CD8alphaalpha ligand hierarchy, including H2-Q10.
- PMID 11069069 — targeted H2-Oa disruption, MHC-II peptide editing, and CD4 single-positive selection.
- PMCID PMC9124240 — H2-O/H2-Ob obligate complex and peptide-editing function.
- DOI 10.1084/jem.178.6.2139 — Q7-encoded Qa-2 alpha3-domain CD8-binding defect and CD8-dependent CTL limitation.
- PMID 11085754 — Qa-2-dependent CD8alphaalpha intestinal IEL selection.
- PMID 15045471 — H2-M2 surface expression with function left unresolved.
- PMID 18322080 / PMID 12628182 / PMID 16089503 — H2-Mv/VNO and V2R association context.
- PMID 12370253 / PMID 21471246 / PMID 21746965 — human KIR3DL1/HLA-Bw4 binding and inhibitory NK function.
- PMID 19625641 / PMID 10809759 — defined MHC-I/CD8 structural and binding comparators, not submitted H2 products.
