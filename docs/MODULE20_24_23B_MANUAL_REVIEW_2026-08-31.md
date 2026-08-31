# Module 23B manual source-unit review report

Read-only review of the eight explicitly profiled Module 23B candidates in
`docs/MODULE20_24_23B_RECOVERY_REVIEW_2026-08-31.md`. Repository and database
files were not modified.

## Counts and gate rule

| Disposition | Count |
|---|---:|
| Candidates reviewed | 8 |
| Observation gate PASS and registered-claim gate PASS | 4 |
| At least one gate failed; excluded from overlay | 4 |
| Rows emitted in source-unit overlay | 4 |
| Additional candidates reviewed | 0 |

`PASS` requires a stable paper anchor, an independently verified atomic
observation at an exact source locus/figure, and a separately verified author
or program claim that supports the registered edge at the registered scope.
Contextual or functional evidence was not converted into a direct molecular,
TF-target, or receptor-subunit claim. Existing evidence grades and context
levels were preserved: B/L1 for EVID-000002 and EVID-000007, B/L4 for
EVID-000250, and B/L2 for EVID-000878.

## Candidate dispositions

| Candidate; registered edge | Artifact(s) reviewed | Observation gate | Claim gate | Disposition and rationale |
|---|---|---|---|---|
| `M23B-EVID-000002`; `M23B-E000001` | `retry_C23B_batch285_Tamaru_36336030_fulltext.pdf` and `.txt` | PASS | PASS | `source_supported_atomic_candidate`; Results §§3.2-3.5, Figs. 2-5, Discussion, and Conclusion directly support the collagen-I-associated beta1-integrin/N-cadherin scar-recruitment pathway in mouse astrocyte and T9 contusion SCI experiments. Overlay row retained as `M23B-P2-R-RECOVERY-TAMARU-FULLTEXT-000001`. No alpha-subunit, purified-binding, kinase-relay, or TF claim was added. |
| `M23B-EVID-000007`; `M23B-E000006` | `retry_C23B_batch286_PMC12048928_alpha9_kindlin1.html` | PASS | PASS | `source_supported_atomic_candidate`; Results and figure-linked text (especially Figs. 2, 4, 6-8) verify the joint AAV-alpha9-integrin plus kindlin-1 intervention, bridge crossing, rostral sensory-axon extension, cFOS/VGLUT readouts, and sensory behavior. Overlay row retained as `M23B-P2-R-000007`. The no-alpha9-only-arm limitation is preserved. |
| `M23B-EVID-000009`; `M23B-E000008` | `retry_C23B_batch062_PMC2199946_PECAM1_alphaVbeta3.html`, `retry_C23B_EVID009_PMC2199946_full.html`, `retry_external_PMC2199946.html`, BioC JSON, XML, and PDF-gate HTML | FAIL: retained local artifacts stop at the abstract/PDF gate; no exact Results or figure locus was available for this review | FAIL for import-ready source-unit materialization; the abstract claim is not independently verifiable at full-text locus | Excluded. The abstract supports the reported CD31 domain-2, alphaVbeta3-specific inhibition, and precipitation claim, but the local full-text-like candidates are not full text. Preserve alphaVbeta3 complex scope; do not promote an ITGB3-single-subunit edge. |
| `M23B-EVID-000025`; `M23B-E000024` | `retry_external_pubmed_28628111.xml` | FAIL: abstract-bounded; exact atomic assay and figure locus unavailable | FAIL for the exact registered edge: the abstract states an integrin-N-cadherin pathway but does not isolate ITGA1 or provide the required full-text locus | Excluded. The abstract supports a mouse SCI pathway/function lead, not a ready source unit for a collagen-I-ITGA1beta1 direct edge. The existing receptor-proximal/pathway scope is not upgraded. |
| `M23B-EVID-000250`; `M23B-E000176` | `retry_C23B085_PMC3755723_ncbi.xml` | PASS | PASS | `source_supported_atomic_candidate`; Results, Figs. 2-4, Discussion, and Conclusion verify Col1alpha1-positive perivascular fibroblast accumulation and persistence in the fibrotic scar after mouse T8 contusion, with vascular localization and distinction from NG2-positive pericytes. Overlay row uses existing phase-2 queue extraction `M20_24-P2-002705`. The claim is retained at cellular-source/ECM-scar level, not as a direct biochemical deposition, receptor, mechanotransduction, or TF claim. |
| `M23B-EVID-000346`; `M23B-E000249` | `retry_C23B055_ptn_sdc3_pmids.xml`, `retry_C23B_PMC2064262_PTN_syndecan3_full.html`, `retry_C23B055_pmc2064262_ptn_sdc3_full.xml`, and BioC JSON | FAIL: the direct-binding paper PMID 8175719 is available locally only as an abstract; the full-text artifact is a related 2006 functional paper | FAIL for a single import-ready direct-binding source unit; the full-text comparator does not replace the missing direct-binding article locus | Excluded. The abstract reports affinity isolation and solid-phase PTN/HB-GAM-N-syndecan binding, and the related full text supports neural migration/Src context, but the exact direct-binding source unit remains abstract-only. Preserve syndecan-3/heparan-sulfate and matrix-presentation boundaries. |
| `M23B-EVID-000083`; `M23B-E000058` | `retry_PMID17598176.html` | FAIL: PubMed abstract only; species and exact source locus remain unresolved | FAIL for import-ready materialization; the abstract does not verify the complete registered axon-sorting relay at full-text locus | Excluded. The abstract is a review lead for laminin-2, alpha7beta1/dystroglycan, and FAK association, but no full-text source-unit verification was available. |
| `M23B-EVID-000878`; `M23B-E000655` | `retry_C23B172_PMC4578660_LRFN4_PTPRD_fulltext.html` plus matching BioC JSON | PASS | PASS | `source_supported_atomic_candidate`; Results and Figs. 1-3 verify SALM3/LRFN4 binding to PTPdelta/LAR-RPTPs, splice-insert dependence, and reduced SALM3-induced synapsin-I clustering after LAR-RPTP knockdown. Overlay row uses existing phase-2 queue extraction `M20_24-P2-004122`. The contextual layer and B/L2 grade are preserved; no PTPRD exclusivity, downstream kinase, SCI transfer, or TF claim was added. |

## Overlay output

`/private/tmp/module20_24_23b_source_unit_overlay.tsv` contains only the four
PASS/PASS rows above and retains the selected phase-2 identifiers exactly.
The TSV header is the exact 25-field header of
`module20_24_integrated_phase2_extractions.tsv`.
