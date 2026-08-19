# Module 21B: Secreted-Signal Relay Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 21A relay curation into queryable intracellular pathway graphs.

**Status**: AUDIT LAYER GENERATED / SQL MATERIALIZATION PENDING.

## Consolidation Goals

- preserve pathway branches rather than overcompressing them
- distinguish direct perturbation support from review-supported routing
- make receptor-to-TF traversal queryable
- preserve cell-type, ligand, and species boundaries

## Required Output Types

- relay `SignalingEdge` rows downstream of receptors
- pathway membership rows for non-edge nodes
- perturbation-backed branch records
- contradiction and boundary annotations

## Handoff Goal

Allow `mSCS` to query, for example:

- if astrocytes express `Osmr`, what downstream TF branches are most defensible?
- if multiple ligands converge on `Stat3`, which upstream routes remain distinguishable?
