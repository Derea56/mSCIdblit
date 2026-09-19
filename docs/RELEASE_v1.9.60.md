# mSCIdblit v1.9.60

## Gap-driven primary-literature expansion

This release adds six source-linked route annotations to the Module 20B-24B
mechanism evidence snapshot. The additions target unresolved cytokine routes
where the existing registers already contained ligand-receptor, receptor-
proximal, transcription-factor, or target-gene evidence.

Added evidence-layer routes:

- IL4 > IL4RA:IL2RG > JAK1/JAK3 > STAT6 > CCL17/TARC
- IL4 > IL4RA:IL2RG > JAK1/JAK3 > STAT6 > SOCS1
- IL15 > IL15RA:IL2RB:IL2RG > JAK1/JAK3 > STAT5 > BCL2
- IL15 > IL15RA:IL2RB:IL2RG > JAK1/JAK3 > STAT5 > IL2RA
- IL3 > IL3RA:CSF2RB > JAK2 > STAT5 > BCL2L1
- IL3 > IL3RA:CSF2RB > JAK2 > STAT5 > CISH

Primary locators include PMID:17134490, PMID:14634100, PMID:29105654,
PMID:10435632, PMID:9129017, and PMID:14627821. These annotations preserve
the source study's species, cell-type, stimulation, receptor-presentation, and
assay qualifiers. They remain evidence-layer routes: causal status is not
asserted, graph traversal is not asserted, and no database confidence score is
created.

## Release counts

- Route evidence records: 19,411 -> 19,417
- Strict full-route annotations: 17 -> 23
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 6

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion155`.

