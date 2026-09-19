# mSCIdblit v1.9.68

## Gap-driven primary-literature expansion

This release adds four evidence-layer route annotations:

- IL-21 > IL21R:IL2RG > JAK1/JAK3 > STAT5 > SOCS3
- TSLP > TSLPR/IL7RA > JAK2 > STAT5 > CISH
- BMP9 > ACVR1/ALK2 > SMAD1/5/8 > ID1
- NODAL > CRIPTO/ACVR1B/ACVR2B > SMAD2 > NANOG

The IL-21 route is supported by primary human B-cell work showing IL-21-induced
SOCS3 expression is reduced after STAT5B loss (PMID:35469842). The TSLP route
uses primary receptor-reconstitution work showing TSLP-dependent STAT5 DNA
complex formation and CIS/CISH transcription (PMID:10570284). The BMP9 route
uses primary IOSE397 work showing ALK2/type-II-receptor-dependent SMAD1/5/8
signaling with Id1 output (PMID:2892305; PMCID:PMC2892305). The NODAL route
records a ligand/receptor-to-SMAD2-to-NANOG bridge from mouse developmental
work (PMID:24929238), while explicitly leaving the intracellular handoff
unresolved.

These annotations preserve model, receptor-subtype, cofactor, and assay
boundaries. The first three are complete evidence-layer routes under the
database's five-layer schema; the NODAL entry is intentionally retained as a
traversable ligand > receptor > TF > output route with a missing intracellular
layer. None asserts SCI transfer, causal graph traversal, or a database
confidence score.

The broader downstream curation queue still contains 3,331 records. Candidate
list exhaustion remains a workflow boundary, not evidence that signaling
literature is saturated. Continued work should search unresolved output tiers,
receptor-subtype-specific studies, and target-gene evidence that can be joined
without overstating the underlying experiments.

## Release counts

- Route evidence records: 19,434 -> 19,438
- Strict full-route annotations: 39 -> 42
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 4

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion163`.
