# Module 21A batch 192 summary

Batch 192 covers exactly 25 queued Module20A external-review pairs:
`M20A-CELLCHAT-REMAINING-0151`–`0154`, `-0218`, and `-0248`–`-0267`.

## Review disposition

- `reviewed_relay_candidate`: 11
- `reviewed_function_only`: 1
- `reviewed_unresolved`: 1
- `reviewed_binding_only`: 2
- `no_evidence_boundary`: 10
- Total: 25 rows

## Evidence interpretation

- The four ADO source-composite rows retain mature-adenosine ADORA1/2A/2B/3 receptor relays as receptor-proximal evidence, while NT5E/CD73 production and SLC29A1/2 nucleoside handling remain separate source/context evidence. No direct source-composite-to-receptor interaction was inferred.
- CCL19/CCR7 and CCL21/CCR7 have direct receptor-proximal and functional signaling support. Ccl21a/CCR7 is supported at the level of a Ccl21a-specific CCR7-dependent thymic migration function, but not by an isolated purified binding assay.
- Ccl21d/e/f were retained as explicit paralog no-evidence boundaries. Family-level CCL21 or annotation/orthology evidence was not transferred to the exact paralog pairs.
- CCL26/CCR3, CCL3/CCR5, CCL6/CCR1, CCL7/CCR1, and CCL7/CCR2 were supported by primary receptor or receptor-dependent functional studies. CCL5/ACKR1 and CCL7/ACKR1 were retained as binding-only atypical-receptor/scavenging branches because ACKR1 lacks canonical G-protein relay evidence.
- Ccl27a/CCR3, Ccl3/5/6/7–Ccr1l1, Ccl6/CCR2, and Ccl6/CCR3 remain explicit no-evidence boundaries. The systematic Ccr1l1 study tested a broad mouse chemokine panel and excluded the relevant ligands; disease-network or family-level predictions were not promoted.
- BMP8B supports ligand-level SMAD2/3 and SMAD1/5/9 pathway outputs through multiple receptor contexts, including ACVR2B in some reporter contexts, but the exact ACVR1–ACVR2B complex was not selectively reconstituted or perturbed. It remains `reviewed_unresolved` rather than a direct receptor-complex claim.

## Search boundaries

Searches covered exact pair and alias terms across PubMed, PMC, publisher/DOI pages, NCBI Gene records, and targeted receptor-family searches for adenosine GPCRs, CCR7/CCL21 paralogs, CCR3/CCL26/CCL27, CCR1l1, ACKR1/DARC, canonical CC chemokine receptors, and BMP8B receptor complexes. Expression-only, pathway-database-only, single-cell ligand-receptor inference, generic family membership, and receptor orthology were not counted as direct molecular evidence.

## Validation

- Exactly 25 data rows are present in the TSV.
- Review IDs and exact pair labels are unique and match the requested queue items.
- All 13 required columns are present and populated; `terminal_TF` is `null` for all rows.
- Confidence values use the existing controlled vocabulary: `low`, `low-medium`, `medium`, or `medium-high`.
- No shared Module21A ledgers, Module20A ledgers, frozen manifest, or SQL materializations were modified.
