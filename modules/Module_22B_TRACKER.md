# Module 22B: TF Target-Program Evidence Consolidation - Graph Evidence Linkage and Query Readiness

## Overview

This module converts Module 22A curation into exportable receiver-program logic.

**Status**: CANONICAL POST-CURATION MATERIALIZED / DATABASE COUNTS RECONCILED.

The evidence-backed public TF-target review set is now materialized in the
local canonical database as supported `RegulonMember` records and typed
`regulates_target_gene` edges. The write covers 221 deduplicated pairs across
198 species-qualified TF entries. See
`docs/MODULE22B_CANONICAL_MATERIALIZATION_2026-08-26.md` for the write audit.
The previously referenced initial-database comparison directory is not present
in this checkout. An independent local PostgreSQL reconciliation on
2026-09-01 confirmed the 221 deduplicated pairs across 198 species-qualified
TF entries; no comparison result from the missing artifact is claimed here.

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
