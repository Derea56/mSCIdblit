# Module 20B–24B Forward Path

This document defines the current boundary between the mSCIdblit evidence
release and downstream mSCS route evaluation.

## Current source release

Use the `mSCIdblit-v1.9.386` tag and the bundle

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion627/`

with release ID

`module20_24_mechanism_graph:2026-09-25-literature-expansion-627`.

The release validator is the gate for the source bundle. The bundle contains
the complete core graph plus the evidence-route overlays required for mSCS.

## Responsibility boundary

### mSCIdblit owns

- canonical nodes, roles, validated graph edges, pathways, and edge provenance;
- primary-literature route annotations and stable source locators where available;
- explicit `known_layers`, `missing_layers`, `route_tier`, and
  `intracellular_status` values;
- normalized route nodes and route edges that preserve shared intermediates;
- curation queues, coverage summaries, boundary summaries, and repair ledgers;
- release lineage, source hashes, schema validation, and evidence-contract checks.

mSCIdblit does not create causal edges or assign the confidence used by the
simulator. Evidence-only routes remain explicitly non-causal.

### mSCS owns

- import and parquet materialization of every release layer;
- route plausibility scoring and context filtering;
- receiver-cell, species, compartment, and injury-context weighting;
- aggregation of overlapping routes and shared-intermediate perturbations;
- confidence estimates and downstream simulation eligibility;
- reporting when a route is supported only by a partial or model-limited chain.

## Required mSCS intake

The route-aware importer must consume the core tables and these evidence
tables, supporting both `.tsv` and `.tsv.gz` forms:

- `mechanism_signaling_route_evidence`
- `mechanism_route_nodes`
- `mechanism_route_edges`
- `mechanism_literature_expansion`
- `mechanism_full_sequence_curation_queue`
- `mechanism_downstream_curation_queue`
- `mechanism_downstream_evidence_records`
- `mechanism_ligand_route_coverage`
- `mechanism_boundary_summary`
- `bundle_metadata`
- `validation_report`

The importer must preserve the distinction between validated graph edges and
evidence-only route edges. In the current release, route evidence is marked
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`; mSCS must interpret these rows
as scored plausibility inputs rather than silently promoting them to graph
edges.

## Near-term sequence

1. Complete the route-aware mSCS intake and make the current release manifest
   resolve to `mSCIdblit-v1.9.386` rather than an older snapshot.
2. Add import tests for compressed tables, expected row counts, release
   provenance, and preservation of missing-link fields.
3. Add route queries by ligand, receptor, intracellular intermediate, TF,
   target gene, and output. Include shared-intermediate queries for MYD88,
   STAT3, NF-kB, ERK, and JNK.
4. Use mSCS route scoring to determine plausible signaling and confidence;
   keep those derived scores outside the mSCIdblit source tables.
5. Return evidence gaps to mSCIdblit as prioritized curation targets. Favor
   missing TF/target-gene links, unresolved intracellular continuations,
   absent stable locators, and high-use shared intermediates.
6. Cut a new mSCIdblit release only when new evidence changes the source
   bundle, its provenance, or its validation counts. Do not create a release
   solely to store downstream mSCS confidence scores.

## Release gate

Before publishing a new mechanism release, run the mSCIdblit validator, verify
that every evidence row retains provenance and explicit causal/traversal
status, test the exact bundle with the route-aware mSCS importer, and update
the release document and manifest together.
