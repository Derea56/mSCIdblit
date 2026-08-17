# Module 24A: Complement, Coagulation, Lipid, and Protease Signaling - Pathway-Graph Corpus Building Tracker

## Overview

This module curates extracellular inflammatory relay systems that are often underrepresented in classic cytokine pathway maps but are highly relevant to SCI tissue-state transitions.

**Status**: ACTIVE / FIRST-PASS QUEUE BUILT / MEDIUM-HIGH PRIORITY FOR `mSCS`.

## Priority Signaling Axes

- complement receptors and effectors
- coagulation and kinin signaling
- protease-activated receptors
- lipid mediators and related receptors
- extracellular protease systems that remodel signaling environments

## Handoff Goal

Provide a curated mechanism layer for noncanonical extracellular relay systems that may help explain vascular, glial, and fibroinflammatory state shifts after SCI.

## First-Pass Queue (2026-08-17)

The initial review queue is maintained at:

- `work/module24a/module24a_extraction_queue.tsv`
- `work/module24a/module24a_batch_plan.tsv`

The queue contains 171 targets in four batches:

- 31 ConnectomeDB complement candidates;
- 26 ConnectomeDB DAMP/purinergic/TLR-boundary candidates;
- 29 CellChatDB complement candidates and 9 CellChatDB DAMP/purinergic candidates after excluding chemokine-only overlap;
- 55 Guide to Pharmacology noncanonical receptor candidates, including complement peptide, tachykinin, P2Y/P2X, and related receptors;
- 10 Module 18 read-only reuse candidates for C1q/lipid, TREM2/debris, ATP/P2X7, P2Y12/adenosine, extracellular-trap/LL37, and CCN1/SDC4 branches;
- 11 explicit search-gap targets for coagulation/PAR, kinin, complement anaphylatoxin, eicosanoid, sphingolipid, resolution-lipid, and extracellular protease systems.

The queue is a candidate inventory, not an evidence register. It preserves release or mediator identity, receptor or target engagement, protease processing, receptor-proximal relay, and downstream pathway/function as separate extraction layers. Chemokine-only and generic TLR overlap is retained only when it defines a boundary for 24A; it is not silently promoted into a 24A direct edge.

Batch 001 validation retained 13 supported edges from primary SCI and comparator studies, covering C1q/lipid-debris function, TREM2/debris sensing, ATP/P2X7R, P2Y12R/adenosine repair, LL37/P2X7R, LTB4/BLT1, leukotriene pharmacology, RvD1/RvD3 function, and activated-protein-C/histone adjacency. Three no-evidence boundary records document unresolved kinin, PAR, and protease-to-PAR searches. No direct PAR edge was promoted, and no Module 20A–23A ledger was modified.

Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. Batch 003 added DAMP/TLR boundary relays, ATP/P2X4 pharmacology, chemokine receptor downstream function, tenascin-C/TLR4 context, decorin/protease adjacency, and reverse-direction TLR4-to-MMP9 pathway context. The integrated first pass contains 24 supported edges and 9 explicit no-evidence boundaries; no PAR edge was promoted and Module 20A LR classifications were not altered.
