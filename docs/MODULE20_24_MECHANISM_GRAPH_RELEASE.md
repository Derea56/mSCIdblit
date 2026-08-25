# Module 20B–24B mechanism graph release

Release identifier: `module20_24_mechanism_graph:2026-08-25`

This is a conservative, register-backed mechanism graph snapshot for mSCIdblit
Modules 20B–24B. It is designed for inspection and simulator import while
preserving the evidence gate: only rows marked `exportable=true` in the
validated edge registers become traversable graph edges.

## Release contents

The bundle is at
`data/processed/mechanism_graph_module20_24_v2026_08_25/`.

| Artifact | Purpose |
|---|---|
| `mechanism_nodes.tsv` | All curated source and target labels used by exported edges; composite labels are preserved. |
| `mechanism_edges.tsv` | Directed, typed, evidence-gated pathway edges with module, context, confidence, and exportability fields. |
| `mechanism_edge_sources.tsv` | Evidence-register provenance, source locators, summaries, limitations, and citation notes for every exported edge. |
| `mechanism_pathways.tsv` | Pathway-level edge, node, and evidence counts. |
| `mechanism_boundary_summary.tsv` | Aggregate view of non-exportable edge boundaries. |
| `bundle_metadata.json` | Release policy, counts, module coverage, and accuracy contract. |
| `validation_report.json` | Machine-generated graph integrity report. |

## Release counts

| Module | Register edges | Exported edges | Evidence rows | Non-exportable edges |
|---|---:|---:|---:|---:|
| 20B | 5,906 | 1,110 | 7,586 | 4,796 |
| 21B | 111 | 111 | 54 | 0 |
| 22B | 5,733 | 723 | 5,906 | 5,010 |
| 23B | 1,075 | 1,072 | 1,467 | 3 |
| 24B | 151 | 151 | 200 | 0 |
| **Total graph** | — | **3,167** | **4,393 linked source rows** | **9,809** |

The graph contains 2,787 node labels and 949 pathway labels. Of the 4,393
linked evidence-source rows, 3,256 retain stable PMID, PMCID, DOI, or HTTP
locators in the release bundle; 1,137 are marked local-only or unresolved and
retain their evidence summaries and limitations without exposing local paths.

## Accuracy check

Run the exporter and validator from the repository root:

```bash
python3 scripts/export_module20_24_mechanism_graph.py
python3 scripts/validate_module20_24_mechanism_graph.py
```

The validator checks:

- unique node, edge, and source IDs;
- source/target node references;
- evidence-source references for every exported edge;
- pathway summary consistency;
- metadata count consistency; and
- absence of non-exportable edges from the traversable graph.

The current release passes with zero errors; the validator reports the
local-only/unresolved locator count as a warning, not as a graph-integrity
failure.

## Interpretation boundaries

- A graph edge is exportable only because the register passed its evidence and
  curation gate; this is not a claim of universal biology or SCI-specific
  applicability.
- Non-exportable, unresolved, low-evidence, and layer-conflicted candidates
  remain summarized as boundaries and are not traversable edges.
- Composite receptor, ligand, pathway, and program labels are preserved rather
  than split into unsupported molecular claims.
- The cross-module synthesis remains an audit-layer interpretation; canonical
  database materialization and source-anchor resolution remain separate release
  gates.

The broader narrative synthesis is in
[`CROSS_MODULE_SYNTHESIS_20_24.md`](CROSS_MODULE_SYNTHESIS_20_24.md), while the
machine-readable graph contract is captured in `bundle_metadata.json`.
