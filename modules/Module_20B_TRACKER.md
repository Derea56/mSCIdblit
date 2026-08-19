# Module 20B: Ligand-Receptor Interaction Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 20A corpus rows into queryable ligand-receptor graph records suitable for simulator export.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Consolidation Goals

- distinguish direct ligand-receptor edges from pathway context
- encode receptor-complex composition cleanly
- preserve mouse versus human support at the source-row level
- retain negative or boundary evidence without forcing unsupported edges into the graph
- assign export priority for simulator use

## Required Output Types

- atomic observations supporting or limiting ligand-receptor edges
- directed ligand-receptor `SignalingEdge` rows
- receptor-complex membership records
- `SignalingEdgeSource` rows with:
  - `support_kind`
  - `species_support`
  - `source_scope`
  - `confidence_tier`
- boundary notes for cell-state, compartment, or injury-phase restrictions

## Query Readiness Rules

- every simulator-exportable edge must have at least one `SignalingEdgeSource`
- species support must never be implicit
- review-only edges must remain distinguishable from primary-supported edges
- receptor-complex edges should be queryable without collapsing all subunits into one node

## Handoff Goal

Produce a graph layer where `mSCS` can ask:

- which ligands could have reached astrocytes at `1 dpi`?
- which receptor complexes were plausibly available on astrocytes?
- which of those edges are mouse-supported versus human-supported?
