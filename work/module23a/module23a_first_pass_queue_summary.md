# Module 23A First-Pass Queue Summary

Date: 2026-08-17

## Scope

Module 23A is being used for ECM, integrin, adhesion, and mechanotransduction evidence. The queue is an audit-layer inventory only. It does not promote any database row or pathway annotation to a mechanistic edge.

## Candidate inventory

| Source stream | Targets | Treatment |
|---|---:|---|
| CellChatDB.mouse ECM-Receptor priority seed | 435 | Retained as matrix-to-receptor candidates; exact complex and primary evidence required |
| ConnectomeDB mouse guidance/ECM review slice | 182 | Retained as adhesion/ECM candidates; Module 20A LR evidence is reusable context only |
| Module 21A pathway-reuse candidates | 464 | Read-only reuse seeds for existing FAK/SRC, ILK, cadherin, laminin, collagen, tenascin, THBS, SPP1, VCAM, EDIL3, and related adhesion branches |
| SCI-specific prior-module mechanism anchors | 11 | Retained as primary-paper extraction targets for stiffness, β1-integrin/ILK, N-cadherin, fibronectin-EDA, periostin, alpha9 integrin, OPN, and ECM glycan branches |
| **Total** | **1,092** | **22 batches; maximum 50 targets per batch** |

## Evidence-layer boundary

Every queue target is reviewed separately for:

1. ligand/receptor binding or activation;
2. receptor-proximal relay;
3. downstream pathway or cellular function.

Pathway-only or functional observations do not establish a direct molecular interaction. Mechanical stiffness, ECM abundance, cell-of-origin, and scaffold/bridge observations remain separate from receptor binding unless the paper supplies a direct assay or a causal perturbation.

## Search boundary

The database sources are candidate generators. The Module 21A rows are read-only reuse seeds, not copied evidence. Primary research papers, stable PubMed/PMC/DOI records, and exact assay/perturbation details are required for promotion. The queue deliberately includes no-evidence and boundary-review targets so that absent evidence is recorded rather than silently inferred. Module 20A frozen LR classifications, Module 21A registers, and Module 22A evidence files are read-only inputs for this first pass.

The queue does not assert YAP/TAZ/TEAD for generic ECM or integrin candidates. Those TFs are extracted only where directly measured; the existing laminin-511/521–α6Bβ1–TAZ/TEAD reuse branch remains context-specific and is not transferred to all α6β1 rows.

## Batch 001 anchor audit

Six high-priority SCI anchors were reviewed and recorded in `module23a_batch001_primary_anchor_audit.tsv`. They remain audit notes rather than promoted evidence records:

- M1A-P003: β1-integrin/N-cadherin blockade supports an adhesion-linked astrocyte phenotype, but no purified binding or FAK/SRC assay was found.
- M1A-P007: fibronectin-EDA deletion supports a fibrotic-scar phenotype, but no receptor or relay was demonstrated.
- M1A-P026: chronic hemisection scar softening and ECM/GAG dysregulation, with no receptor signaling assay.
- M1A-P027: stiffness-associated β1-integrin/ILK readouts in astrocytes, without direct binding or definitive FAK/SRC activation.
- M5A-P015: α9-integrin/kindlin-1 and laminin/tenascin-C bridge localization with sensory regeneration, without biochemical binding or FAK/SRC validation.
- M5A-P038: ECM/glycan and myeloid/functional changes, without a tested glycan–receptor relay or TF assay.

Current disposition: 1,092 queued targets. Batch 001 contributed 7 validated evidence records and 7 context/relay/function edges. Batch 002 contributed 17 validated evidence records covering 13 queue targets, including direct molecular anchors and SCI-specific relay/function evidence. Batch 003 contributed 4 validated evidence records covering collagen-II and collagen-IV family context. Across the integrated pass there are 28 supported edges and 3 explicit no-evidence boundary records; direct binding claims remain family- and model-specific and are not transferred to untested SCI receptor pairs.

## Audit-layer registers

The following schemas now contain the integrated first-pass audit layer:

- `module23a_evidence_register.tsv` — 28 supported evidence records plus 3 explicit no-evidence boundaries;
- `module23a_edge_register.tsv` — 28 supported direct, receptor-proximal, pathway, or functional edges;
- `module23a_perturbation_register.tsv` — remains empty pending perturbation normalization;
- `module23a_saturation_matrix.tsv` — retains the initial anchor rows and is being expanded with reviewed queue targets.

This preserves the distinction between a review target and validated evidence. Records will be added only after the exact source, species/model, assay or perturbation, relation type, pathway branch, confidence, and limitations are checked.

## Known contradiction

M1A-P026 reports chronic hemisection scar softening, while M1A-P027 reports chronic contusion lesion/rim stiffening. These are retained as a model-, time-, and sample-preparation-dependent mechanics boundary; they must not be collapsed into one universal stiffness direction.
