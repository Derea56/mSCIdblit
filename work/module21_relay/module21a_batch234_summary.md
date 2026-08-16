# Module 21A batch 234 review summary

Date: 2026-08-15

Scope: exactly the 25 queued Module21A pairs supplied for batch 234, in supplied order. Evidence was restricted to primary PubMed/PMC/publisher records and stable PMID, PMCID, DOI, or URL citations. The frozen manifest was checked at `work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json`.

## Outcome

Status counts:

- `reviewed_relay_candidate`: 8
- `reviewed_function_only`: 3
- `no_evidence_boundary`: 14
- Total: 25

Confidence counts:

- `high`: 4
- `medium`: 7
- `low`: 14

The 14 `no_evidence_boundary` rows are the exact WNT6/FZD/LRP5-6 and WNT7A/FZD10, FZD1, or FZD2/LRP5-6 composites in IDs 0473-0486. Exact-composite searches did not locate qualifying primary binding, activation, reconstitution, receptor-proximal, or pair-specific downstream evidence. Family-level FZD/LRP findings, generic beta-catenin results, expression, pathway co-membership, database inference, and structurally related WNT complexes were not transferred.

The exact WNT5B/FZD1/LRP6 row (M20A-EXT-3507) was retained as `reviewed_function_only`: FZD1 co-IP and Fzd1/Lrp6 loss-of-function support an exact-composite-dependent renal fibroblast response, but the full ternary contact and stoichiometry were not directly resolved. WNT7A/RECK (M20A-EXT-3524) is a separate direct ligand/co-receptor and signalosome result and was not transferred to the unresolved WNT7A composite rows.

The WNT5A/PTK7 record preserves an important primary-assay boundary: one Xenopus study detected PTK7 with WNT3A/WNT8 but not WNT5A, while later work directly reported WNT5A-PTK7 association and PTK7-dependent JNK/motility outputs. The two records were not collapsed into a ligand-family inference.

## Terminal transcriptional endpoints

Four rows contain provisional terminal endpoints because the cited primary studies explicitly measured them:

- `AP-1 (provisional)`: WNT5A/PTK7
- `CREB (provisional)`: WNT5A/ROR1
- `TCF/LEF family (provisional)`: WNT7A/RECK-associated reporter output
- `HES5 (provisional)`: GDF5/BMPR1B_BMPR2 neuronal model

The remaining 21 rows contain literal `null`. Beta-catenin stabilization/translocation, SMAD phosphorylation, receptor cleavage, chemotaxis, adhesion, uptake-like handling, and functional outputs were not converted into terminal TF assignments unless an explicit downstream transcriptional endpoint was measured.

## Layering decisions

Binding/activation, receptor-proximal relay, and downstream pathway/function are separated in `evidence_layer`. CX3CL1/CX3CR1 preserves the distinction between membrane-tethered adhesion and soluble chemotaxis: adhesion did not require the PTX-sensitive G-protein branch, whereas migration did. CXCL16/CXCR6 preserves membrane versus soluble ligand behavior and reports function without inventing an intracellular relay. Chemokine receptor promiscuity, GAG presentation, ligand processing, and model dependence are retained as limitations.

For WNT3/ROR2, physical association and WNT-responsive output are recorded, while unchanged ROR2 autophosphorylation leaves direct receptor activation/proximal relay unresolved. For WNT3/RYK, the cleavage-dependent RYK intracellular-domain relay is recorded separately from the WNT3 association and neuronal function. For GDF5/BMPR1B_BMPR2, direct binding, type-II receptor support, SMAD1/5/8 signaling, and the measured HES5 endpoint are retained without assuming invariant receptor stoichiometry across lineages.

## Validation

- TSV header is exactly the requested 13-column schema: `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`.
- The TSV contains exactly 25 data rows, with IDs and pairs in the supplied order.
- Required fields are populated; confidence values are restricted to `high`, `medium`, or `low`.
- Stable-citation fields contain only PMID, PMCID, DOI, or URL identifiers.
- No tabs occur inside fields and no row has extra or missing columns.
- The frozen manifest SHA256 is `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Only `work/module21_relay/module21a_batch234_review.tsv` and this summary were written for batch 234; shared registers, Module20A files, the manifest, SQL, and existing files were not modified.
