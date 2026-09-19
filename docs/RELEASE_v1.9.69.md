# mSCIdblit v1.9.69

## Gap-driven primary-literature expansion

This release adds three evidence-layer route annotations:

- BAFF > TACI > NF-kB > AICDA
- TWEAK > Fn14 > NF-kB > IL8
- LEP > LEPR > STAT3 > SOCS3

The BAFF/TACI route is supported by primary mouse and human B-cell work
linking TACI to MyD88/IRAK4/NF-kB signaling and AID/AICDA-associated class
switching (PMID:20676093). The TWEAK/Fn14 route is supported by primary
receptor-binding and cell-signaling work showing NF-kB activation with IL8
induction (PMID:22081603). The leptin route is supported by primary studies
showing leptin-induced SOCS3 expression and LEPR-associated STAT3/SOCS3
feedback (PMID:10514492; PMID:11018044).

These are intentionally traversable partial routes: the intracellular relay
between each receptor and the listed transcription factor is not resolved in
this release. The BAFF/TACI evidence includes BAFF/APRIL ligand context, and
the TWEAK evidence is sensitive to ligand oligomerization. None of the routes
asserts SCI transfer, causal graph traversal, or a database confidence score.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated.

## Release counts

- Route evidence records: 19,438 -> 19,441
- Strict full-route annotations: 42 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion164`.
