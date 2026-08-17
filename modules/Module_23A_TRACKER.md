# Module 23A: ECM, Integrin, Adhesion, and Mechanotransduction Signaling - Pathway-Graph Corpus Building Tracker

## Overview

This module curates matrix, adhesion, and mechanosensing relay logic relevant to scar organization, vessel remodeling, astrocyte/fibroblast states, and mechanically sensitive CNS responses after SCI.

**Status**: ACTIVE / FIRST-PASS QUEUE BUILT / MEDIUM-HIGH PRIORITY FOR `mSCS`.

## Priority Signaling Axes

- integrins and focal adhesion signaling
- FAK/SRC relays
- cadherin and adhesion signaling
- YAP/TAZ/TEAD
- mechanosensitive matrix-response pathways
- matricellular ligands and receptor interactions

## Handoff Goal

Provide a mechanotransduction layer so `mSCS` can eventually reason about tissue-state signaling that is not reducible to classic soluble cytokines.

## First-Pass Queue (2026-08-17)

The initial review queue is maintained at:

- `work/module23a/module23a_extraction_queue.tsv`
- `work/module23a/module23a_batch_plan.tsv`

The queue contains 1,092 review targets:

- 435 CellChatDB ECM-Receptor candidates;
- 182 ConnectomeDB guidance/ECM adhesion candidates;
- 464 Module 21A pathway-reuse candidates covering existing FAK/SRC, ILK, cadherin, laminin, collagen, tenascin, THBS, SPP1, VCAM, EDIL3, and related adhesion branches;
- 11 SCI-specific mechanism targets seeded from prior scar, stiffness, integrin, matricellular, and ECM-glycan work.

The queue is a candidate inventory, not an evidence register. Database rows remain provenance-only until primary research validation. Each target explicitly separates the three extraction layers: ligand/receptor binding or activation, receptor-proximal relay, and downstream pathway or cellular function. The queue also retains an explicit boundary for the conflicting chronic-scar mechanics anchors M1A-P026 and M1A-P027.

Review is organized into 22 batches of at most 50 targets. P1 targets prioritize integrin, syndecan, CD44, dystroglycan, validated 21A FAK/SRC/ILK branches, and SCI-specific mechanics branches. P2/P3 targets remain queued for broader receptor-specific and guidance/adhesion review. No Module 20A, 21A, or 22A evidence ledger is modified by queue construction.

Batch 001 anchor validation has retained seven evidence-backed context, relay, or functional edges in the new 23A audit registers. These include β1-integrin/N-cadherin astrocyte relay context, stiffness–β1-integrin/ILK response, fibronectin-EDA scar function, chronic ECM/GAG mechanics, α9-integrin/kindlin-1 sensory regeneration, and glycan/ECM-myeloid function. None is promoted as a direct molecular binding edge without a qualifying binding assay.

The integrated B002/B003 review added 21 supported direct, receptor-proximal, and downstream ECM/adhesion records, including PECAM1-alphaVbeta3, uPA-alphaMbeta2, POSTN, Reelin, Sema7A, SPP1, TIMP1-LRP1, Agrin-DAG1, CHAD, collagen-I beta1, and collagen-IV family anchors. Non-SCI direct-binding studies remain mechanistic anchors only; family-level evidence is not transferred to chain-specific or untested SCI pairs. Three bounded no-evidence records preserve unresolved receptor assignments. Module 20A, 21A, and 22A ledgers remain unchanged.
