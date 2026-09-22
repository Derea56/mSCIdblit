# mSCIdblit release v1.9.150

Release date: 2026-09-21

Graph identifier: `module20_24_mechanism_graph:2026-09-21-literature-expansion-262`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion262/`

## Evidence overlay and route coverage

This release attaches reviewed primary-evidence supplements from the public
ligand–receptor comparison to existing graph edges. It does not create new
graph edges, causal routes, or composite confidence scores. The evidence and
route layers remain available for mSCS to evaluate as plausible signaling
routes with context-dependent confidence.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Edge-source rows | 17,242 |
| Evidence-route records | 16,247 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |
| Public-LR candidate rows audited | 7,737 |
| Public-LR rows with primary locators and graph matches | 1,115 |
| Intracellular/TF gap pairs prioritized for follow-up | 5,950 |

The route-evidence categories are:

| Category | Records |
|---|---:|
| L→R→output | 2,638 |
| L→R→TF→output | 336 |
| L→R→intracellular→output | 2,376 |
| L→R→intracellular→TF→output | 117 |
| L→R entry only | 9,306 |

The strict full-chain audit retains 141 evidence-backed edge-chain instances
and 95 unique four-node topologies. The public-LR overlay contributes 2,165
source rows across 1,267 existing graph edges; it is evidence-only and leaves
the edge count unchanged.

The mSCS-facing coverage report is
`release_coverage_report.md`, the prioritization queue is
`mechanism_route_gap_priorities.tsv`, and the import manifest is
`mscs_import_manifest.json` in the release bundle.

Validation:

```bash
python3 scripts/validate_module20_24_mechanism_graph.py \
  --bundle-dir data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion262
```

The bundle passes validation with zero errors and was imported successfully
through mSCS's `import_mechanism_bundle.py` into a temporary active release.
