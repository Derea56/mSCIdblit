# Module 20B odd source-unit review — 2026-09-01

## Scope and freeze

This lane reviewed the already-screened odd-suffix Module 20B Phase-2 candidate set from the local resolver/integrated packet. No external lookup, PostgreSQL write, shared-script edit, schema edit, release-export edit, or candidate-search expansion was performed. The stable-ID rule was a trailing numeric suffix; no ambiguous suffix row was included.

The source packet contained 2,111 integrated Module 20B rows. The frozen odd-lane screen contained 20 candidate rows, and all 20 had a local path recorded in the packet. Six pre-existing rows in the separate J overlay were not modified or duplicated here. This overlay contains 20 rows: 2 included as bounded primary support and 18 explicitly excluded.

## Outcome counts

| disposition | count |
|---|---:|
| included_bounded_primary_support | 1 |
| included_exact_direct_binding_support | 1 |
| excluded_edge_mismatch | 1 |
| excluded_no_verified_local_full_text | 3 |
| excluded_artifact_identity_mismatch | 4 |
| excluded_unresolved_exact_pair | 1 |
| excluded_unresolved_no_pair_specific_evidence | 1 |
| excluded_review_not_completed_before_freeze | 8 |
| **total** | **20** |

The two included rows are:

- M20B-P2-R-001797 / PMID 24312319: exact local PMCID PMC3842941 full text; Results/Figures/Discussion support an AMH–AMHR2/BMPR1A–SMAD1/5–Id3 receptor-complex/pathway branch in mouse immature granulosa cells. Grade B, context L1; not treated as purified binding.
- M20B-P2-R-002665 / PMID 22568954: exact local PMCID PMC3499309 full text plus Figure 1; the recombinant ELISA panel reports 2.6 ± 0.28 nM apparent KD for mEphrin-A4–hEphA2. Grade B, context L1; bounded to Fc-reagent direct binding.

## Blockers and exclusions

- One source-unit identity mismatch: GDF15 evidence was for GFRAL–RET rather than the registered GDF15–TGFBR2 edge.
- Three rows lacked a locally verified full-text body at the cited identity (abstract/metadata-only or mixed local files).
- Four local artifacts were identity-mismatched or mixed relative to the resolver-approved paper.
- One exact full text did not establish the registered Slitrk4–PTPRS pair; one bounded packet explicitly retained COMP–CD36 as unresolved with nearby THBS1–CD36 evidence non-transferable.
- Eight rows remained in the frozen screen but their exact source-unit Results/Discussion/figure adjudication was not completed before the requested stop. They are explicitly excluded and carry grade U; no evidence was upgraded by inference.

Boundary/context-only, negative, unresolved, and non-exact rows remain excluded rather than being promoted.

## Provenance and focused validation

- Input: work/cross_module_synthesis/canonical_evidence_review/module20_24_integrated_phase2_extractions.tsv
- Resolver: work/cross_module_synthesis/canonical_evidence_review/module20_24_phase2_paper_identity_resolution.tsv
- Register: work/module_b_consolidation/module20b/module20b_edge_register.tsv
- New overlay: work/cross_module_synthesis/canonical_evidence_review/phase2_L_20B_odd_source_unit_overlay.tsv
- Checks: unique header; 20 data rows; unique extraction IDs; odd trailing numeric suffix for every row; integrated IDs and paper keys preserved; resolver-approved PMID/status present for every row; local artifact path exists for every row; register-edge lookup present for every row; disposition counts reconcile to 20.
- Repository safety: only the two new lane-specific files were written; shared scripts, schemas, PostgreSQL, release exports, and existing overlays were not modified.
