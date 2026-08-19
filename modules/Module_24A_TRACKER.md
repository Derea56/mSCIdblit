# Module 24A: Complement, Coagulation, Lipid, and Protease Signaling - Pathway-Graph Corpus Building Tracker

## Overview

This module curates extracellular inflammatory relay systems that are often underrepresented in classic cytokine pathway maps but are highly relevant to SCI tissue-state transitions.

**Status**: ACTIVE / FIRST-PASS QUEUE BUILT / AUDIT SQL STAGED / MEDIUM-HIGH PRIORITY FOR `mSCS`.

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

Batch 001 validation initially retained 13 supported edges from primary SCI and comparator studies, covering C1q/lipid-debris function, TREM2/debris sensing, ATP/P2X7R, P2Y12R/adenosine repair, LL37/P2X7R, LTB4/BLT1, leukotriene pharmacology, RvD1/RvD3 function, and activated-protein-C/histone adjacency. The B001 coagulation/kinin/complement tranche then added APC-EPCR/PAR1, bradykinin-BDKRB2, C3a-C3aR1, C5a-C5aR1, and thrombin-PAR1, while retaining thrombin-PAR3/PAR4 as comparator-only. Factor Xa-to-PAR2, BDKRB1, and noncognate complement assignments remain explicit no-evidence boundaries. No Module 20A–23A ledger was modified.

Batch 002 added engineered CR2-Crry fragment-targeting and CR2-associated injury-function context while retaining intact C3-to-CR2, intact C3-to-CR3, intact C3-to-CR4, and C4b-to-CR2 as unresolved. Batch 003 added DAMP/TLR boundary relays, ATP/P2X4 pharmacology, chemokine receptor downstream function, tenascin-C/TLR4 context, decorin/protease adjacency, and reverse-direction TLR4-to-MMP9 pathway context. The integrated first pass contains 31 supported edges before the B001 coagulation/kinin/complement tranche, and Module 20A LR classifications were not altered.

Batch 004 added CX3CL1/CX3CR1, CXCL1/CXCR2, CXCL10/CXCR3, CXCL3/CXCR2, and CCN1/SDC4 evidence while retaining comparator-only and unresolved chemokine cases separately. With the B001 tranche, the integrated first pass contains 42 supported edges and 15 explicit no-evidence boundaries; PAR1 is supported, PAR3/PAR4 remains comparator-only, factor Xa-to-PAR2 remains unresolved, and Module 20A LR classifications were not altered. Legacy Module 18 audit rows were assigned non-queue `M24A-LEGACY-*` identifiers to prevent collision with the live 24A queue.

B001 follow-on validation added hemokinin/tachykinin receptor pharmacology, substance P/Tacr1 SCI function, UDP-sugar/P2Y14 comparator pharmacology, and FAM3D/TAFA5 FPR1/FPR2 comparator relays. Duplicate Guide-to-Pharmacology seeds were linked to existing edges rather than duplicated. Tac1/Tac4 precursor candidates were normalized to peptide-derived pathway records rather than direct precursor-protein interactions. Hc-to-C5aR1 and noncognate complement assignments remain unresolved. B001 is complete: all 50 queue candidates are reviewed. The integrated first pass contains 66 supported edges and 18 explicit no-evidence boundaries; Module 20A LR classifications were not altered.

B002 opening-tranche validation covered Q0051-Q0071. Duplicate tachykinin/P2Y14 and Module 18 reuse seeds were linked to existing edges. New validated branches include PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2. BLT2, MMP2/MMP9-to-receptor, GPR32, and generic trypsin/plasmin/kallikrein-to-PAR substitutions remain explicit boundaries. B002 has 29 candidates remaining; the integrated first pass contains 73 supported edges and 22 explicit no-evidence boundaries. Module 20A LR classifications were not altered.
B002 opening-tranche validation covered Q0051-Q0071. Duplicate tachykinin/P2Y14 and Module 18 reuse seeds were linked to existing edges. New validated branches include PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2. BLT2, MMP2/MMP9-to-receptor, GPR32, and generic trypsin/plasmin/kallikrein-to-PAR substitutions remain explicit boundaries. The completed Q0072-Q0100 tranche added Gal-9/TIM-3, resistin-TLR4, ApoC3 particle clearance, C1QL2-NRXN3, C1QTNF5-MFRP, Cripto coreceptor complexes, CYTL1-CCR2, FLRT3 homophilic adhesion, IL17D-CD93, IL-1/IL-36 accessory-chain complexes, LEAP2-GHSR antagonism, and PCDHGC3 barrier function. Module23A FLRT3-ADGRL3/UNC5B and ApoC3-LRP1 records were reused read-only; direct-pair and accessory-chain limits remain explicit. B002 is complete: all 50 queue candidates are reviewed. The integrated first pass contains 100 supported edges and 28 explicit no-evidence boundaries. Module 20A LR classifications were not altered.
B002 opening-tranche validation covered Q0051-Q0071. Duplicate tachykinin/P2Y14 and Module 18 reuse seeds were linked to existing edges. New validated branches include PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2. BLT2, MMP2/MMP9-to-receptor, GPR32, and generic trypsin/plasmin/kallikrein-to-PAR substitutions remain explicit boundaries. The completed Q0072-Q0100 tranche added Gal-9/TIM-3, resistin-TLR4, ApoC3 particle clearance, C1QL2-NRXN3, C1QTNF5-MFRP, Cripto coreceptor complexes, CYTL1-CCR2, FLRT3 homophilic adhesion, IL17D-CD93, IL-1/IL-36 accessory-chain complexes, LEAP2-GHSR antagonism, and PCDHGC3 barrier function. Module23A FLRT3-ADGRL3/UNC5B and ApoC3-LRP1 records were reused read-only; direct-pair and accessory-chain limits remain explicit. B003 validation then added PCDHGC5, PIANP/PILRA, PTPRD/IL1RAP synaptic complex, WNT5A-ROR2-VANGL2 complex, ANXA2-TLR2, CIRBP-TLR4, decorin-TLR2, DEFB2-TLR4, ficolin-A/TLR4 pathway, HMGB1-TIM-3/TLR2, galectin-9/TLR4 modulation, and comparator chemokine receptor pharmacology while retaining S100/TLR and ATP channel reuses/boundaries. B002 and B003 are complete: all 100 queue candidates are reviewed. The integrated first pass contains 130 supported edges and 31 explicit no-evidence boundaries. Module 20A LR classifications were not altered.
B002 opening-tranche validation covered Q0051-Q0071. Duplicate tachykinin/P2Y14 and Module 18 reuse seeds were linked to existing edges. New validated branches include PGE2-EP2/EP4, S1P-S1PR1/2/3, and Klk6-PAR1/PAR2. BLT2, MMP2/MMP9-to-receptor, GPR32, and generic trypsin/plasmin/kallikrein-to-PAR substitutions remain explicit boundaries. The completed Q0072-Q0100 tranche added Gal-9/TIM-3, resistin-TLR4, ApoC3 particle clearance, C1QL2-NRXN3, C1QTNF5-MFRP, Cripto coreceptor complexes, CYTL1-CCR2, FLRT3 homophilic adhesion, IL17D-CD93, IL-1/IL-36 accessory-chain complexes, LEAP2-GHSR antagonism, and PCDHGC3 barrier function. Module23A FLRT3-ADGRL3/UNC5B and ApoC3-LRP1 records were reused read-only; direct-pair and accessory-chain limits remain explicit. B003 validation then added PCDHGC5, PIANP/PILRA, PTPRD/IL1RAP synaptic complex, WNT5A-ROR2-VANGL2 complex, ANXA2-TLR2, CIRBP-TLR4, decorin-TLR2, DEFB2-TLR4, ficolin-A/TLR4 pathway, HMGB1-TIM-3/TLR2, galectin-9/TLR4 modulation, and comparator chemokine receptor pharmacology while retaining S100/TLR and ATP channel reuses/boundaries. B004 queue synchronization is complete: all 171 queue candidates are reviewed, no duplicate edges were added, and the 31 explicit no-evidence boundaries remain. The integrated first pass contains 130 supported edges and 31 explicit no-evidence boundaries. Module 20A LR classifications were not altered.
