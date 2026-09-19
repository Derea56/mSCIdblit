# mSCIdblit v1.9.65

## Gap-driven primary-literature expansion

This release adds one source-linked route annotation for a TNC/TGF-beta
output:

- TNC > TGFB1 > ALK1 > SMAD2/3 > COL1A1

Primary fibroblast studies report TNC-associated TGF-beta receptor/SMAD2/3
activation and increased type-I-collagen expression, including COL1A1
(PMID:33217999; PMCID:PMC7698786; PMID:32650003). The source studies do not
identify ALK1 specifically and do not establish direct SMAD2/3 occupancy at
the COL1A1 promoter in the TNC treatment experiment. The route is therefore
retained as a composite evidence path with receptor-subtype, cell-type, and
promoter-mechanism boundaries explicit.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated. Continued work should search unresolved output tiers,
receptor-subtype-specific studies, and target-gene evidence that can be joined
without overstating the underlying experiments.

All additions remain evidence-layer routes: causal status is not asserted,
graph traversal is not asserted, and no database confidence score is created.

## Release counts

- Route evidence records: 19,428 -> 19,429
- Strict full-route annotations: 33 -> 34
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 1

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion160`.
