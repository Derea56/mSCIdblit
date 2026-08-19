# Module 22B: TF Target-Program Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 22A curation into exportable receiver-program logic.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Consolidation Goals

- standardize target-program labels
- separate direct TF-target edges from broader TF-state associations
- preserve contradictions across contexts
- allow receiver-state explanation without pretending every program is equally direct

## Required Output Types

- TF-to-target `SignalingEdge` rows where warranted
- TF-to-program association records
- phenotype-linked TF outcome summaries
- export-ready labels for receiver programs

## Handoff Goal

Provide the downstream layer that lets `mSCS` rank plausible explanations for why astrocytes move from one observed state to another.
