# mSCIdblit release v1.9.210

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-normalized-route-artifacts-328`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion328/`

## Normalized signaling-route artifacts

This release retains the compact route-evidence table and adds normalized
companion tables for every evidence route:

- `mechanism_route_nodes.tsv.gz` lists the ordered node sequence for each
  route, preserving shared intermediates across ligands and outputs.
- `mechanism_route_edges.tsv.gz` lists asserted graph components, explicit
  missing route links, and separate output-observation edges.

Missing route links remain `not_asserted` and
`evidence_route_not_causal`. An output observation that is not contiguous with
the mechanistic path is retained as `output_observation`; it is not converted
into a TF-target or causal edge.

For the IL1B pilot, the IL1B→IL6 normalized route preserves:

```text
IL1B → IL1R1/IL1RAP → MYD88 → IRAK4 → IRAK1 → TRAF6
→ TAK1/MAP3K7 → NF-kappaB branch → NF-kB → IL6 gene
```

The `NF-kappaB branch → NF-kB` and `NF-kB → IL6 gene` transitions remain
explicit missing-link records, while the direct IL1B→IL6 observation is kept
separately. This supports shared-node perturbation analysis without claiming
that every route segment has direct primary evidence.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,686 |
| Normalized route-node records | 1,290,701 |
| Normalized route-edge records | 1,273,888 |
| IL1B evidence-route records | 90 |
| IL1B TF-family-supported routes | 4 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

All normalized artifacts remain evidence-layer data. They do not create graph
edges, causal assertions, or database confidence scores. mSCS imports both
tables into its columnar mechanism release and retains compressed TSV exports
when requested.

Validation passed with zero errors; the existing stable-locator warning
remains. The mSCS import completed successfully, including the normalized
route tables. The mSCIdblit pytest suite could not be run because this
checkout has no pytest installation; the normalized-route behavior was
validated by direct module execution and the release validator.
