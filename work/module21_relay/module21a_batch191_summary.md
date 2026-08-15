# Module 21A Batch 191 review summary

Batch 191 reviews exactly the filtered Module20A external-review queue
ordinals **4226–4250** in the established priority-8 order. The raw artifact
is `module21a_batch191_review.tsv` and uses the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 9 |
| `reviewed_binding_only` | 2 |
| `reviewed_function_only` | 6 |
| `reviewed_unresolved` | 5 |
| `no_evidence_boundary` | 3 |
| **total** | **25** |

Confidence counts: medium-high 6; medium 10; low-medium 6; low 3. Every
`terminal_TF` value is the literal `null`.

## Exact queue alignment

The 25 rows are the supplied filtered priority-8 sequence:

| filtered ordinal | review ID range | pair range |
|---:|---|---|
| 4226–4250 | `M20A-EXT-3229`–`M20A-EXT-3253` | `Tdgf1 Acvr2b` through `Tgfb1 Itgb3` |

The submitted pair labels were preserved exactly, including receptor-complex
labels (`Acvr1_Tgfbr1_Tgfbr2`, `Acvr1_Tgfbr2`, and `Itgav_Itgb6`) and component
labels (`Itgb1`, `Itgb3`).

## Evidence decisions

- **Positive receptor-proximal or relay candidates.** Cripto/TDGF1–GPC1 is
  supported by direct association and Src/MAPK/PI3K-AKT activation. TFF2–CXCR4
  is supported by CXCR4-dependent calcium/MAPK and cell-response assays, but
  not purified affinity. TFPI–F3 and TFPI–LRP1 retain the TF/FVIIa inhibitory
  complex and LRP-dependent internalization branch. TG–ASGR1, TGFA–ERBB4,
  TGFB1–ENG, and latent TGFB1-LAP–ITGAV_ITGB6 retain receptor or co-receptor
  context with downstream functional readouts. The TGFB1–ACVR1/TGFBR1/TGFBR2
  row retains the defined ACVR1/TGFBR1 receptor cross-talk branch.

- **Binding-only or extracellular function.** TFF1–MUC5AC and TFF2–MUC6 are
  mucin/glycan association records, not intracellular receptor relays.
  TFPI–VLDLR and TG–LRP2 are retained as uptake/clearance functions where a
  standalone intracellular relay was not demonstrated.

- **Unresolved exact composites or cross-talk rows.** TDGF1–ACVR2B reflects
  Cripto’s Nodal co-receptor role in ACVR2B-containing complexes, not direct
  TDGF1–ACVR2B ligand binding. TFF3–CXCR4 remains unresolved because a direct
  CXCR4 pharmacology study was negative while other functional work treated
  CXCR4 as a hypothesis. TGFA–ERBB3 is retained only as EGFR-dependent ErbB3
  complex signaling. TGFB1–ACVR1/TGFBR2 is limited to a mutant-ACVR1/FOP
  context, and TGFB1–ITGB3 is supported only for the alpha-v-beta3 heterodimer,
  not isolated ITGB3.

- **Explicit no-evidence boundaries.** TFF3–ACKR3, TFPI–SDC4, and TG–TPO
  remain unassigned. ACKR3/CXCL12, TFPI-heparan-sulfate/LRP/VLDLR, and
  TSH-regulated TG/TPO comparator findings were not transferred to the exact
  submitted pairs.

## Layer and terminal-TF boundary

Binding or activation, receptor-proximal relay, and downstream pathway or
cellular function were recorded separately. Direct molecular interaction was
not inferred from pathway cross-talk, receptor-expression priming, reporter
output, uptake, or phenotype alone. No terminal TF met the explicit evidence
boundary in this batch; SMAD, MAPK, AKT, Src, ERK, and transcriptional outputs
remain pathway/function annotations rather than Module22A terminal-TF calls.

## Validation and write boundary

- 25 data rows, all unique review IDs and pair labels.
- Exact alignment to filtered queue ordinals 4226–4250.
- Exact 13-column schema on every row.
- All required fields populated; confidence vocabulary valid.
- All terminal-TF values are literal `null`.
- Only `module21a_batch191_review.tsv` and this summary were written.
- Shared Module21A ledgers, Module20A files, frozen manifests, Module22A
  handoff tables, and SQL/materialization outputs were not modified. No commit
  was created.
