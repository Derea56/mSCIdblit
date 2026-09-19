# mSCIdblit v1.9.64

## Gap-driven primary-literature expansion

This release adds two source-linked route annotations for an unresolved
FGF/STAT5 output family:

- FGF2 > FGFR3 > SH2B1/SH2-Bbeta > STAT5 > PLF1
- FGF8b > FGFR3 > SH2B1/SH2-Bbeta > STAT5 > PLF1

Primary studies report FGF2- and FGF8b-dependent STAT5 activation in mouse
brain microvascular endothelial cells, PLF1/proliferin induction, and STAT5
occupancy at the PLF1 promoter (PMID:19176400; PMID:22199350;
PMCID:PMC3307309). The output studies do not identify FGFR3 as the relevant
receptor subtype or establish every intermediate in one assay. The release
therefore retains these as composite evidence routes with explicit
receptor-subtype and assay-boundary limitations; the target-gene output is
supported, but no new TF-target graph edge is asserted.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated. Continued work should search unresolved output tiers,
receptor-subtype-specific studies, and target-gene evidence that can be joined
without overstating the underlying experiments.

All additions remain evidence-layer routes: causal status is not asserted,
graph traversal is not asserted, and no database confidence score is created.

## Release counts

- Route evidence records: 19,426 -> 19,428
- Strict full-route annotations: 31 -> 33
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion159`.
