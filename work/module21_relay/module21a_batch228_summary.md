# Module 21A batch 228 review

Batch 228 was reviewed as the exact 25-pair queue supplied for this task, in the supplied order. The review TSV uses the prior standalone 13-column schema and keeps ligand-receptor binding/activation, receptor-proximal relay, and downstream pathway or cellular function as separate evidence-layer values. Receptor-complex assignments are recorded as complex edges; pathway or function evidence was not used to claim a direct binary interaction.

Status counts:

- reviewed_relay_candidate: 18
- reviewed_binding_only: 3
- reviewed_function_only: 2
- reviewed_unresolved: 2

The two unresolved rows are Saa2 Tlr2 and Sema3f NRP2_PLXNA2. Saa2 Tlr2 remains limited by isoform/preparation and contamination concerns without purified exact-pair affinity evidence. Sema3f NRP2_PLXNA2 has conflicting reconstitution versus later ligand/receptor-specificity evidence and was not promoted by family analogy.

Terminal TF handoffs are present only where a measured transcriptional endpoint was explicit:

- Rspo3 Znrf3 -> TCF/LEF family
- Rspo4 Rnf43 -> TCF/LEF family
- Rspo4 Znrf3 -> TCF/LEF family
- S100a1 Tlr4 -> RELA
- Saa2 Fpr2 -> EGR1

All other `terminal_TF` values are the literal `null`.

Validation completed:

- 25 data rows, one header row, and the exact 13 requested columns.
- Queue IDs and exact pair labels match the batch-228 input in order.
- Required fields are populated; `terminal_TF` is either an explicitly supported endpoint or literal `null`.
- Confidence values are restricted to `low`, `medium`, `medium-high`, or `high`.
- The frozen Module 20A manifest was read-only checked at SHA256 `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Only this TSV and this summary were written for batch 228; shared registers, ledgers, manifest, SQL, and existing files were not modified.
