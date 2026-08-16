# Module 21A batch 235 review summary

Batch 235 contains exactly the 25 queued Module21A pairs `M20A-LIANA-REMAINING-0487` through `M20A-LIANA-REMAINING-0511`, in the supplied order. The review applies exact-composite evidence rules for WNT7A/B–FZD–LRP5/6 pairs; family-level, generic WNT/β-catenin, or unmatched FZD/LRP evidence was not transferred to an exact composite.

Frozen manifest: `work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json`

Frozen manifest SHA-256: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`

## Disposition counts

| status | rows |
|---|---:|
| reviewed_relay_candidate | 5 |
| reviewed_function_only | 1 |
| reviewed_unresolved | 5 |
| no_evidence_boundary | 14 |
| **total** | **25** |

Confidence counts: `high` 2, `medium` 4, `low` 19.

## Evidence boundaries

- Primary WNT7B work supports cell-surface FZD1/FZD10 binding and cooperative canonical activation in an LRP5 context (PMID:15923619; PMCID:PMC1140585; DOI:10.1128/MCB.25.12.5022-5030.2005).
- Primary WNT7A work supports the native FZD5-LRP6 response and a separate LRP5 co-transfection reporter effect; the queued FZD5-LRP5 row therefore remains function-only (DOI:10.1074/jbc.M300191200).
- GPR124-dependent WNT7A/B signaling supports an exact FZD4-LRP5 functional relay, while the tested FZD4-LRP6 arm was not promoted; WNT7A/B–FZD4-LRP5 rows are relay candidates and FZD4-LRP6 remains unresolved/no-evidence (PMID:25373781; PMCID:PMC4223636; DOI:10.1016/j.devcell.2014.08.018).
- WNT7A directly binds FZD8 and LRP5/LRP6 ectodomains separately, but this does not establish either exact FZD8-LRP5 or FZD8-LRP6 ternary composite. A later WNT7 core-complex study also separates the FZD-independent GPR124-RECK-LRP5/6 core from FZD-dependent signaling (PMID:30304675; PMCID:PMC6338448; PMID:40914247; PMCID:PMC12514574; DOI:10.1016/j.jbc.2025.110682).
- WNT7A-FZD9 noncanonical ERK5/PPARγ findings are preserved as a comparator layer only; LRP5/6 was not established for the queued composites (PMID:16835228; PMCID:PMC3800035).
- No direct interaction was inferred from pathway/function evidence. Receptor-complex, binding/activation, receptor-proximal relay, downstream pathway/function, and no-evidence layers remain distinct.

## Terminal TF and unresolved outcomes

All 25 `terminal_TF` values are the literal string `null`; no exact queued composite had an explicitly measured downstream TF/transcriptional endpoint eligible for assignment. TCF/LEF reporter, TOPFLASH, β-catenin stabilization, and the FZD9 comparator PPARγ result were not converted into terminal_TF assignments. `reviewed_no_downstream_evidence` count: 0; unresolved and no-evidence rows are explicitly retained in their respective statuses.

## Validation

- TSV has the exact 13-column schema and 25 data rows.
- IDs and pairs match the supplied 25-row order exactly.
- All 25 rows have 13 populated fields; no tabs occur inside fields and no extra columns are present.
- Confidence vocabulary is limited to `high`, `medium`, and `low`; batch row 0502 is normalized to `high`.
- Rows 0505–0509 and 0511 have literal `null` terminal_TF values; all other rows do as well.
- Frozen manifest SHA-256 matches the required value above.
- Only `work/module21_relay/module21a_batch235_review.tsv` and this summary were written for batch 235; shared registers, Module20A files, the manifest, SQL, and existing unrelated files were not modified.
