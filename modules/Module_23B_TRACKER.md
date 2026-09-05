# Module 23B: ECM and Mechanotransduction Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 23A into queryable matrix-to-receptor and adhesion-to-TF graph records.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Second-pass promotion batch (2026-09-04)

The B023 second-pass batch promotes two existing MMRN2-CLEC14A edges and adds five source-linked B edges for MMRN2-CD93, MMRN2-CD248, and the three separated SLIT2 C-terminal LG-domain–glycosylated DAG1 layers. The B register now contains 1,080 edges and the B evidence register contains 1,506 evidence rows; the boundary register is unchanged at 289 rows. These are audit-layer promotions only: canonical signaling tables and simulator outputs remain untouched. Non-SCI vascular/pericyte and developmental spinal-cord comparator limits are explicit.

The subsequent source-backed promotion gate moved 701 additional B edges from `staged`/`staged_primary_review` to `reviewed_supported`. Each passed the one-to-one A mapping and primary-paper evidence gate; the single remaining staged A/B candidate, EFNA3–EPHA2, is held as `held_unresolved_exact_directness` and remains non-exportable. The B register therefore has 773 `reviewed_supported` edges while retaining the directness exception explicitly.

## Consolidation Goals

- preserve extracellular matrix composition and receptor context
- distinguish contact-mediated signaling from soluble ligand signaling
- retain cell-type and compartment boundaries

## Handoff Goal

Provide exportable edges for matrix-sensitive receiver-state transitions in astrocytes, fibroblasts, endothelial cells, and related compartments.
## Review-led expansion: B024 (2026-09-04)

B024 promotes six new 23B edges paired one-to-one with Module 23A: decorin-to-EGFR binding/activation, decorin anti-scarring and axon-growth function in acute rat SCI, and biglycan CD14 binding, TLR2/TLR4/MyD88 relay, TLR2/TLR4–P2X4/P2X7–NLRP3 inflammasome relay, and macrophage inflammatory output. These are audit-layer promotions with review and primary-source lineage; non-SCI comparator scope, intact soluble biglycan, receptor-complex context, and function-only versus receptor-proximal distinctions are retained. Canonical signaling tables and simulator outputs remain untouched.

## Review-led expansion: B025 (2026-09-04)

B025 promotes seven new 23B edges paired one-to-one with Module 23A: three tenascin-C FBG/TLR4 layers covering direct binding, TLR4-dependent NF-kappaB/proximal signaling, and macrophage/microglial inflammatory function; and four low-molecular-weight hyaluronan layers covering TLR4-MyD88, TLR4-TRIF/TBK1/IRF3, cPLA2alpha/COX2-eicosanoid, and IFN-beta outputs. Review-led primary evidence and local-source lineage are recorded in the B evidence and promotion registers. FBG-domain and fragment-size specificity, adaptor separation, endotoxin controls, non-SCI comparator scope, and the absence of direct HA-TLR4 binding or terminal-TF transfer remain explicit; canonical signaling tables and simulator outputs remain untouched.
