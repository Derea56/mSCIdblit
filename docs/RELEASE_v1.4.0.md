# mSCIdblit v1.4.0 mechanism-graph release

This release freezes a new register-backed Module 20B–24B mechanism graph
snapshot. It incorporates the completed high-confidence Module 20A
ligand–receptor promotion pass and organizes Module 20B into conservative
receptor-family groupings while preserving the independent evidence and
context annotations used for later weighting.

## Release identity

- Project version: `mSCIdblit v1.4.0`
- Mechanism graph version: `v1.4.0`
- Graph release identifier: `module20_24_mechanism_graph:2026-09-01`
- Release date: `2026-09-01`
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_01/`
- Prior mechanism-graph snapshot: `data/processed/mechanism_graph_module20_24_v2026_08_30/`

This is a register-backed mechanism-graph release. It does not claim that
every graph edge is SCI-specific and does not replace the separate canonical
database release without a database materialization pass.

## High-confidence LR promotion audit

The Module 20A external review queue contains 310 rows with
`confidence_decision=high`. All 310 resolve to Module 20B edges with
`confidence_tier=high` and `exportable=true`. The release graph contains 309
of these as traversable edges.

The one excluded row is intentionally retained as a register-backed boundary:

| Module 20A row | Module 20B edge | Pair | Reason |
|---|---|---|---|
| `M20A-EXT-0600` | `M20B-E002375` | `Ncam1 → Ncam1` | Self-loop excluded by the normalized graph contract; source and target are the same entity. |

No LR-only row was converted into a relay, transcription-factor, program,
cellular-output, or SCI-context claim. The ABC evidence tier and L0–L4
context fields remain independent of the graph export gate.

## Bundle counts

| Measure | Count |
|---|---:|
| Nodes | 2,787 |
| Traversable edges | 3,161 |
| Evidence-source rows | 4,494 |
| Role assignments | 4,340 |
| Pathway summaries | 958 |
| Non-exportable boundary edges | 9,815 |
| Boundary groups | 16 |

| Module | Register edges | Exported edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,118 | 7,630 | 4,788 |
| 21B | 111 | 111 | 60 | 0 |
| 22B | 5,733 | 714 | 5,906 | 5,019 |
| 23B | 1,075 | 1,069 | 1,501 | 6 |
| 24B | 151 | 149 | 224 | 2 |

The 20B exported edges are now organized into 14 labels: ECM/integrin
adhesion (252), RTK growth-factor (109), GPCR (82), axon-guidance/adhesion
(82), TGF-beta/BMP (79), WNT/Frizzled (47), synaptic/cell-adhesion (40),
scavenger/uptake-associated (38), cytokine (27), Notch (10), innate-immune
(10), Hedgehog (8), purinergic/neuroreceptor (2), and pathway not established
(332). These are receptor-family groupings, not assertions of complete
downstream cascades.

## Validation

The graph validator passed with zero errors, including unique identifiers,
resolved node and evidence-source references, pathway summaries, role
compatibility, exportability, and self-loop exclusion.

The mSCS bundle importer also completed successfully in a temporary import
directory. The release therefore preserves the provenance gate requiring
evidence anchors for traversable graph sources.

The Module 20B stratification layer is recorded in
`data/processed/module20b_pathway_family_layer_v1/` and its SHA-256 is stored
in `bundle_metadata.json`. The source Module 20B register remains unchanged.

The previously reviewed public-TF candidate and validated-edge files remain a
separate evidence layer. They were not added as traversable edges in this
release because their current source rows do not contain the importer-required
paper/observation/claim anchors. No provenance requirement was relaxed to
force their inclusion.

## Rebuild commands

```bash
python3 scripts/export_module20_24_mechanism_graph.py \
  --output-dir data/processed/mechanism_graph_module20_24_v2026_09_01
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_01
```
