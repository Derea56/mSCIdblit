# Module 23B: ECM and Mechanotransduction Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 23A into queryable matrix-to-receptor and adhesion-to-TF graph records.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Second-pass promotion batch (2026-09-04)

The B023 second-pass batch promotes two existing MMRN2-CLEC14A edges and adds five source-linked B edges for MMRN2-CD93, MMRN2-CD248, and the three separated SLIT2 C-terminal LG-domain–glycosylated DAG1 layers. The B register now contains 1,080 edges and the B evidence register contains 1,506 evidence rows; the boundary register is unchanged at 289 rows. These are audit-layer promotions only: canonical signaling tables and simulator outputs remain untouched. Non-SCI vascular/pericyte and developmental spinal-cord comparator limits are explicit.

## Consolidation Goals

- preserve extracellular matrix composition and receptor context
- distinguish contact-mediated signaling from soluble ligand signaling
- retain cell-type and compartment boundaries

## Handoff Goal

Provide exportable edges for matrix-sensitive receiver-state transitions in astrocytes, fibroblasts, endothelial cells, and related compartments.
