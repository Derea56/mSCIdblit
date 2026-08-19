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

Current disposition: 1,092 queued targets. Batch 001 currently contributes 66 validated evidence records: 40 supported context/relay/function edges and 26 explicit subunit/complex or direct-binding no-evidence boundaries. The Q0007–Q0036 slices preserve ANGPTL2 and CCN4 alpha5beta1 complex resolution, record APOC3 only as a functional LDLR/LRP1 clearance axis, separate APOE and cell-surface CALR LRP1 evidence into binding, receptor-proximal, and functional layers, retain CD40LG at Mac-1 alphaMbeta2/I-domain resolution, retain processed DSP at ITGB6 resolution, keep EDIL3-LFA1 and EDIL3-alphaV complexes at functional or assembled-complex resolution, add EGFL7-alphaVbeta3 binding/FAK-Akt/angiogenic function, preserve FBLN2 as an existing function-only beta3-complex anchor, restrict FGA evidence to the Aalpha RGD motif engaging assembled alphaIIbbeta3, retain FGG gammaC structural binding at assembled alphaIIbbeta3 resolution, reuse FN1-alphaVbeta3 and processed irisin-alphaVbeta5 canonical branches without duplication, add extracellular HSP90alpha-LRP1/Akt motility, released gp96-LRP1/CD91 APC signaling, context-specific Hsp70-LRP1/CD91 evidence with conflicting affinity literature, and ICAM5-alpha5beta1 neuronal adhesion/function. FGB free-chain, FN1 free-ITGB3, full-length FNDC5/free-subunit, HSPA4-LRP1, and generic free-ITGB1 candidates remain bounded. Batch 002 contributed 17 validated evidence records covering 13 queue targets. Batch 003 contributed 4 validated evidence records covering collagen-II and collagen-IV family context. Batches 004–006 added 31 validated evidence records spanning collagen-VI/IX, fibronectin, COMP/DMP1, perlecan/dystroglycan, and laminin receptor contexts. Batches 007–009 added 70 validated evidence records spanning assembled laminin complexes, NPNT/Reelin, thrombospondins, tenascin/vitronectin/VWF, stiffness, activated A2M/LRP1, and PACAP/PAC1. Batch 010 added 56 validated evidence records spanning GPCR, angiopoietin, chemokine, adhesion, processed ECM-fragment, ephrin, FN1, irisin, and perlecan branches. Batch 011 added 72 validated evidence records spanning 63 supported molecular/relay/function edges and 8 explicit source-context boundaries. Batch 012 added 103 validated evidence records spanning 45 supported complex, relay, pathway, and functional edges plus 4 exact-pair boundaries. Batch 013 added 32 validated evidence records spanning 26 supported Eph/ephrin edges plus 6 explicit no-evidence boundaries. Batch 014 added 40 validated evidence records spanning Eph/ephrin, semaphorin receptor complexes, and SCI downstream ECM anchors. Batch 015 added 57 validated evidence records spanning 53 supported collagen/matrix edges and 4 explicit boundaries. Batch 016 added 150 validated evidence records spanning 129 supported edges and 21 explicit boundaries. Batch 017 added 150 validated evidence records spanning 107 supported edges and 35 explicit boundaries, with three declared aliases deduplicated and evidence retained on canonical edges. Batch 018 added 80 validated evidence records spanning 76 supported laminin/matrix edges and 4 explicit boundaries. Batch 019 added 134 validated evidence records spanning 108 staged edges and 26 explicit boundaries; nine exact duplicate edge-content rows across earlier batches were consolidated during final integration with evidence retained. Batch 020 added 150 validated evidence records spanning 102 supported edges and 48 explicit boundaries. Batch 021 added 68 validated evidence records spanning 32 supported edges and 36 explicit boundaries. Batch 022 added 107 validated evidence records spanning 99 supported edges and 8 explicit boundaries. A legacy B008 repair re-pointed 19 evidence rows to canonical edges and added 9 layer-specific edges, eliminating all 29 stale edge references. Across the integrated pass there are 1,055 supported edges, 1,147 supported evidence records, and 277 explicit no-evidence or source-context boundary records; direct binding claims remain family-, complex-, processed-ligand-, motif-, and model-specific and are not transferred to untested SCI receptor pairs.

## Audit-layer registers

The following schemas now contain the integrated first-pass audit layer:

Latest B001 amendment: Q0032–Q0041 added 20 validated records in total across the two completed slices. Q0032–Q0036 added 12 supported edges and one HSPA4-LRP1/CD91 boundary; Q0037–Q0041 added eight supported edges and three free-subunit/complex boundaries. The B001 total is now 77 validated records: 48 supported edges and 29 explicit boundaries. The Q0037–Q0041 slice resolves ISG15 to assembled LFA-1, JAM3 to assembled Mac-1, and LAMA3 to assembled laminin-332–alpha3beta1, while preserving free-subunit and absent-kinase-relay limits. Across the integrated pass there are 1,063 supported edges, 1,155 supported evidence records, and 280 explicit no-evidence or source-context boundary records.

Final B001 amendment: Q0042–Q0050 completed the batch. Q0042–Q0046 added nine supported assembled-complex edges and five free-subunit boundaries for LGALS3, MFGE8, and alpha8beta1/alphaVbeta5 contexts. Q0047 added the MMP9 hemopexin-domain–LRP1 binding, ERK/Akt relay, and Schwann-cell function layers. Q0048–Q0049 reused canonical NPNT-alpha8beta1 records with free-subunit boundaries, and Q0050 reused canonical PECAM1-alphaVbeta3 binding with a free-ITGAV boundary. B001 is complete: 97 validated records, 60 supported edges, and 37 explicit boundaries. Across the integrated pass there are 1,075 supported edges, 1,167 supported evidence records, and 288 explicit no-evidence or source-context boundary records.

- `module23a_evidence_register.tsv` — 1,167 supported evidence records plus 288 explicit no-evidence or source-context boundaries;
- `module23a_edge_register.tsv` — 1,075 supported direct, receptor-proximal, pathway, or functional edges;
- `module23a_perturbation_register.tsv` — remains empty pending perturbation normalization;
- `module23a_saturation_matrix.tsv` — retains the initial anchor rows and is being expanded with reviewed queue targets.

This preserves the distinction between a review target and validated evidence. Records will be added only after the exact source, species/model, assay or perturbation, relation type, pathway branch, confidence, and limitations are checked.

## Known contradiction

M1A-P026 reports chronic hemisection scar softening, while M1A-P027 reports chronic contusion lesion/rim stiffening. These are retained as a model-, time-, and sample-preparation-dependent mechanics boundary; they must not be collapsed into one universal stiffness direction.

## Matrix reconciliation amendment (2026-08-18)

The extraction queue status field was not advanced when the earlier B002–B009 evidence integrations were made. The validated saturation matrix is therefore used as the completion ledger for these batches until queue-status bookkeeping is normalized. Candidate-level rows were added for the previously grouped bounded-search targets: B002 adds 38 explicit boundaries, B003 adds 46, B004 adds 46, B005 adds 46, B006 adds 31, B007 adds 40, B008 adds 29, and B009 adds 31. B001–B009 now have all 450 queue targets represented in the saturation matrix; B007 also adds one validated primary-search boundary record for isolated laminin chains. No Module 20A–22A ledger was changed. The full 1,092-target queue is now represented in the matrix; B010–B022 retain their existing candidate rows and batch-specific statuses for the next audit pass.

## Later-batch status promotion amendment (2026-08-18)

The staged matrix statuses for B016, B017, B018, B019, B020, and B022 were reviewed against their existing layer-separated evidence and promoted without changing edge content. Binding-only, relay-unresolved, downstream-only, complex-limited, pair-limited, and alias cases remain encoded in the layer fields and status values; no staged matrix rows remain. The integrated audit layer now contains 1,092 unique candidate rows, 1,075 unique edges, and 1,456 unique evidence records. All materialized edges have supporting evidence and no evidence row points to a stale edge ID.

## Queue completion amendment (2026-08-18)

All 22 batches are now explicitly marked `reviewed_first_pass` in `module23a_extraction_queue.tsv`. The queue, saturation matrix, and evidence/edge registers reconcile at 1,092 candidates, 1,075 edges, and 1,456 evidence records, with zero staged candidates, zero duplicate IDs, zero unsupported edges, and zero stale evidence references. This completes the 23A first-pass batch workflow; unresolved biology remains represented as bounded matrix/evidence cases rather than being promoted into unsupported edges.
