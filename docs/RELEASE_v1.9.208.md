# mSCIdblit release v1.9.208

Release date: 2026-09-22

Graph identifier: `module20_24_mechanism_graph:2026-09-22-graph-supported-route-expansion-325`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_21_literature_expansion325/`

## TSV-first graph-supported evidence routes

This release materializes conservative evidence-route compositions from the
validated graph. Each added route requires an exact exported ligand–receptor
edge and compatible graph components with a shared pathway anchor or exact
shared evidence identifier. The composer does not create graph edges, assign
database confidence, or assert causal traversal through an unobserved link.

The release adds 313,750 route records across 1,413 exact ligand–receptor
edges. The route table contains 333,678 records in total. Of the added rows,
6 contain an asserted intracellular-component→TF edge; 309,273 retain an
intracellular component and TF/output evidence while explicitly marking that
link as `intracellular_to_tf_edge_not_asserted`. This is the intended evidence
layer for mSCS plausibility scoring, not a claim that every assembled route is
a fully demonstrated molecular chain.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,678 |
| L→R→output records | 8,693 |
| L→R→TF→output records | 516 |
| L→R→intracellular→output records | 3,228 |
| L→R→intracellular→TF→output records | 308,818 |
| Full graph edge-chain instances | 141 |
| Unique full-chain topologies | 95 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

The graph itself is unchanged from the preceding release. The increase is in
the evidence-route layer, which preserves the distinction between direct graph
edges, compatible co-evidence, and missing causal links. All route rows remain
`causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`.

The primary route artifact is the compressed TSV
`mechanism_signaling_route_evidence.tsv.gz`. Parquet materialization is
deliberately deferred until the route composition and consumer contract are
stable; the uncompressed TSV is approximately 608 MB and the gzip artifact is
approximately 35 MB. The logical table name remains
`mechanism_signaling_route_evidence.tsv` for readers and importers.

Validation passed with zero errors. The validator retained the existing warning
that some evidence sources do not have stable public locators. The compressed
TSV was
imported successfully into mSCS, whose active mechanism manifest now records
333,678 signaling-route evidence rows for this release. mSCS route and
retention tests passed 16 tests. No Parquet artifact was generated.
