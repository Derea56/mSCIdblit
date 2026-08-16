# Module 21A batch 237 review summary

Batch 237 contains exactly the 25 queued Module21A pairs supplied by the user, in the supplied order. The review applies the exact-composite rule for WNT8A/B–FZD–LRP5/6: family-level, generic beta-catenin, unmatched FZD/LRP, and ortholog/comparator findings were not transferred to an exact ternary pair.

Frozen manifest: `work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json`

Frozen manifest SHA-256: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`

## Disposition counts

| status | rows |
|---|---:|
| reviewed_relay_candidate | 0 |
| reviewed_function_only | 0 |
| reviewed_unresolved | 10 |
| reviewed_no_downstream_evidence | 0 |
| no_evidence_boundary | 15 |
| **total** | **25** |

Confidence counts: `medium` 10, `low` 15, `high` 0, `medium-high` 0.

## Evidence boundaries

- The primary WNT-FZD mapping study reports WNT8A and WNT8B canonical reporter activity through FZD5 and FZD8 in human HEK293T cells, but it does not establish an LRP5-versus-LRP6 partner for the queued ternary composites (PMID:28733458; PMCID:PMC5636703; DOI:10.1096/fj.201700144R).
- Primary LRP5/LRP6 ligand profiling places WNT8A and WNT8B in an LRP6-responsive group, but the experiments do not identify the queued FZD subtype in the same exact composite (PMID:33545636; PMCID:PMC7919854; DOI:10.1016/j.bbrc.2021.01.068).
- WNT8A-LRP6 synaptogenic and LRP6-phosphorylation results support a binary/component branch only; no FZD subtype was resolved in that study (PMID:24316074; PMCID:PMC3924421; DOI:10.1016/j.celrep.2013.11.008).
- Xenopus Wnt8b-Fzd7 and zebrafish Wnt8b-Fzd3a/Fz8a developmental studies provide receptor or genetic/function component evidence, not exact WNT8B-FZD-LRP5/6 ternary composites (PMID:10906785; DOI:10.1002/1097-0177(2000)9999:9999<::AID-DVDY1017>3.0.CO;2-9; PMID:23438515; DOI:10.1016/j.brainres.2013.02.028; DOI:10.1242/dev.129.19.4443).
- The exact ternary structural comparator Wnt8-Fzd8-LRP6 is engineered Xenopus Wnt8 rather than WNT8A or WNT8B, so it was retained only as a limitation and not transferred (PMID:36893265; PMCID:PMC10089208; DOI:10.1073/pnas.2218238120).
- No exact queued composite had a qualifying receptor-proximal relay or pair-specific downstream function. No downstream-only disposition was therefore used.

## Terminal TF and unresolved outcomes

All 25 `terminal_TF` values are the literal string `null`. No exact queued WNT8A/B-FZD-LRP5/6 composite had an explicitly measured downstream TF/transcriptional endpoint eligible for a provisional annotation. The Xenopus `siamois` endpoint and reporter outputs were not converted into terminal_TF assignments because they were component/comparator evidence rather than an exact queued ternary-composite endpoint.

## Validation

- TSV has the exact 13-column schema and 25 data rows.
- IDs and pairs match the supplied 25-row order exactly.
- All 25 rows have 13 populated fields; `terminal_TF` is populated with literal `null` in every row.
- Confidence vocabulary is limited to `low`, `medium`, `medium-high`, and `high`.
- No tabs occur inside fields and no extra columns are present.
- Frozen manifest SHA-256 matches the required value above.
- Only `work/module21_relay/module21a_batch237_review.tsv` and this summary were written; shared registers, Module20A files, the manifest, SQL, and existing unrelated files were not modified.
