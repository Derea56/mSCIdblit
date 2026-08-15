# Module 21A batch 089 review summary

Batch 089 covers the exact filtered priority-8 queue ordinal rows 1526–1550 from `work/module20_db_seed/evidence_escalation_router/module20a_external_review_queue.tsv`. The slice contains 25 rows and follows the explicit queue IDs `M20A-CELLCHAT-REMAINING-1672` through `-1697`; review ID `-1677` is absent from the filtered queue, so the ordinal slice—not a contiguous ID assumption—was used.

## Disposition

- 7 `reviewed_relay_candidate`
  - Sema3C–PLXND1.
  - Sema4A–TIMD2.
  - Sema6D–PLXNA1, PLXNA1_KDR, and PLXNA1_TREM2 complexes.
  - SLURP2–CHRNA3 within an α3β2 nAChR complex.
  - SLURP2–CHRNA4 within an α4β2 nAChR complex.
- 2 `reviewed_binding_only`
  - SIGLEC1–SPN/CD43 sialic-acid-dependent adhesion.
  - SLURP2 association with CHRNA5-containing cortical receptor material without an exact functional complex assay.
- 16 `reviewed_unresolved`
  - SFTPD–ADGRE5.
  - SIRPB1A/B/C–CD47.
  - All nine SLURP1 subunit rows in this slice.
  - SLURP2–CHRNA1, CHRNA10, and CHRNA2.
- 0 function-only promotions.
- 0 terminal TF assignments.

## Evidence boundaries

The semaphorin records preserve receptor-complex boundaries. Sema6D–PLXNA1 was kept distinct from the PLXNA1–KDR/VEGFR2 and PLXNA1–TREM2–DAP12 complexes. Sema3C evidence supports PLXND1-dependent guidance in a neuropilin-containing context, but no terminal transcription factor was inferred.

The SFTPD–ADGRE5 search found established CD97/ADGRE5 ligands such as CD55/DAF but no qualifying exact SFTPD assay. SIGLEC1–SPN was retained as a glycan-dependent adhesion/counterreceptor edge based on CD43/sialophorin binding; no intracellular relay or TF was inferred from adhesion alone.

For SIRPB1A/B/C–CD47, primary SIRP-family studies establish that human SIRPβ1 has negligible or absent CD47 binding, while SIRPα and SIRPγ bind CD47. Those results were retained as an exact-pair boundary and were not transferred to the mouse SIRPB1A/B/C paralogs.

The SLURP1 rows were not promoted from the positive α7/CHRNA7 literature because CHRNA7 is not one of the exact queue pairs in this batch. SLURP2 evidence was promoted only where the primary study tested α3β2 or α4β2 complexes; CHRNA1, CHRNA2, CHRNA10 and other untested subunits remain unresolved. CHRNA5 was retained as binding-only because affinity purification detected the subunit but did not define a stoichiometric functional receptor complex.

## Search boundary

Searches covered PubMed, PMC, publisher pages, and Reactome for exact ligand/receptor names, receptor-complex variants, and primary functional assays. Search terms included Sema3C–Plexin-D1, Sema4A–Tim-2, Sema6D–Plexin-A1/KDR/TREM2, SFTPD–CD97/ADGRE5, Siglec-1–CD43/SPN, SIRPβ1–CD47, and SLURP1/2 with each queued nicotinic subunit. Family-level, expression-only, review-only, or untested-subunit evidence was recorded as a limitation rather than promoted to a direct edge.

## Files and integrity

- Added isolated review file: `work/module21_relay/module21a_batch089_review.tsv`.
- Added this summary: `work/module21_relay/module21a_batch089_summary.md`.
- No shared Module 21A registers, integration outputs, Module20A LR ledgers, or frozen manifest were modified.
- Batch TSV validation: 25 rows, 13 columns per row, unique review IDs, all required fields populated, and exact queue ID/pair mapping passed.
- Frozen manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
