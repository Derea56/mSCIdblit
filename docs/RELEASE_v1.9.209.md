# mSCIdblit release v1.9.209

Release date: 2026-09-23

Graph identifier: `module20_24_mechanism_graph:2026-09-23-il1b-tf-route-pilot-327`

Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_23_literature_expansion327/`

## IL1B TF-family route pilot

This release adds four evidence-layer route records for IL1B. The routes use
the existing receptor-proximal chain:

```text
IL1B → IL1R1/IL1RAP → MYD88 → IRAK4 → IRAK1 → TRAF6 → TAK1 → NF-kappaB branch
```

The routes connect that chain to four existing IL1B-associated transcriptional
outputs: `ICAM1`, `IL6`, `CCL20`, and `CXCL1`. NF-kB is represented as a
supported transcription-factor family layer. The exact IKK-to-NFKB1/RELA
ordering, TF occupancy, and direct TF-to-target edges remain unasserted and are
carried in `missing_layers` and `route_linkage_status`.

All four rows remain `causal_status=not_asserted` and
`traversal_status=evidence_route_not_causal`. They are intended for mSCS route
plausibility and confidence evaluation, not as new causal graph edges or
database confidence scores.

| Artifact | Count |
|---|---:|
| Graph nodes | 11,988 |
| Traversable graph edges | 14,801 |
| Evidence-route records | 333,682 |
| IL1B evidence-route records | 90 |
| New IL1B TF-family-supported routes | 4 |
| IL1B TF-family-supported outputs | 4 |
| Downstream curation queue rows | 3,384 |
| Downstream evidence records | 4,806 |

The primary route artifact is the compressed TSV
`mechanism_signaling_route_evidence.tsv.gz`. mSCS imports it transparently as
the logical `mechanism_signaling_route_evidence.tsv` table.

Validation passed with zero errors; the existing stable-locator warning remains.
The release imported into mSCS successfully, and the focused mSCS route,
retention, inference, and enumeration tests passed 16 tests.

The source curation packet is
`work/module_b_consolidation/module21b/module21b_il1b_tf_route_curation.json`.
