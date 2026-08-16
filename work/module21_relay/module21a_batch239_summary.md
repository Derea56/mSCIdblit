# Module 21A batch 239 review summary

Batch 239 contains exactly the 16 queued Module21A pairs supplied by the user, in the supplied order. Evidence was restricted to primary PubMed, PMC, and publisher records, with stable PMID, PMCID, and DOI identifiers only in `stable_citations`. WNT9B-FZD-LRP5/6 rows apply the exact-composite rule: FZD-family results, LRP5/6 family interchangeability, generic beta-catenin reporters, unmatched ternary constructs, and comparator ligands were not transferred to a queued composite.

Frozen manifest: `work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json`

Frozen manifest SHA-256: `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`

## Disposition counts

| status | rows |
|---|---:|
| reviewed_relay_candidate | 1 |
| reviewed_function_only | 1 |
| reviewed_unresolved | 5 |
| reviewed_no_downstream_evidence | 0 |
| no_evidence_boundary | 9 |
| **total** | **16** |

Confidence counts: `low` 12, `medium` 3, `high` 1, `medium-high` 0.

## Evidence boundaries

- Primary WNT9B-FZD mapping reports canonical reporter activity through FZD4, FZD5, FZD8, and FZD10 in a human HEK293T receptor-rescue system (PMID:28733458; PMCID:PMC5636703; DOI:10.1096/fj.201700144R). It does not resolve the queued LRP5-versus-LRP6 partner for those exact FZD branches.
- Mouse nephron-progenitor-like M15 experiments identify FZD5 and LRP6 as required for strong WNT9B/RSPO1 TOPFlash responsiveness; FZD5 addition increases the response, LRP6 knockdown reduces it, and LRP5 does not rescue LRP6 knockdown (PMID:30978219; PMCID:PMC6461349; DOI:10.1371/journal.pone.0215139). This supports exact functional WNT9B-FZD5-LRP6 dependence and is recorded as `reviewed_function_only`, not direct ternary binding.
- Recombinant protein work shows strong WNT9B-LRP6 binding and only weak WNT9B-FZD8 binding, while the reconstituted FZD8-WNT-LRP6 ternary complex is WNT3A-FZD8-LRP6, not WNT9B-FZD8-LRP6 (PMID:20093360; PMCID:PMC2838336; DOI:10.1074/jbc.M109.092130). Therefore WNT9B-FZD8-LRP6 remains unresolved and the WNT3A ternary result is not transferred.
- FZD2, FZD3, FZD6, FZD7, and FZD9 queued composites had no qualifying exact WNT9B-FZD-LRP5/6 assay; these are explicitly recorded as `no_evidence_boundary`. No row was promoted from expression, family membership, or unmatched LRP/FZD evidence.
- XCL1-XCR1 is directly supported by receptor identification and binding, pertussis-toxin-sensitive chemotaxis, calcium mobilization, primary XCR1-positive DC assays, in-vivo immune function, and an XCL1-XCR1-Gi structural/activation study (PMID:9632725; DOI:10.1074/jbc.273.26.16551; PMID:19913446; DOI:10.1016/j.immuni.2009.08.027; PMID:39565315; PMCID:PMC11621518; DOI:10.1073/pnas.2405732121).

Binding/activation, receptor-proximal relay, and downstream pathway/function are separated in `evidence_layer`. No exact queued WNT9B composite had a qualifying terminal transcription-factor endpoint. All 16 `terminal_TF` values are the literal `null`; the XCL1-XCR1 immune readouts are functional outputs, not measured terminal-TF annotations.

## Validation

- TSV header exactly matches `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`.
- TSV contains exactly 16 data rows; IDs and pairs match the supplied order exactly.
- All 16 rows contain 13 populated fields; no tabs occur inside fields and no row has missing or extra columns.
- `confidence` is limited to `low`, `medium`, `medium-high`, and `high`; observed values are `low`, `medium`, and `high`.
- `stable_citations` contains only PMID, PMCID, and DOI identifiers.
- All 16 `terminal_TF` fields are literal `null`.
- Frozen manifest SHA-256 matches the required value above.
- Only `work/module21_relay/module21a_batch239_review.tsv` and this summary were written; shared registers, Module20A files, the manifest, SQL, and existing unrelated files were not modified.
