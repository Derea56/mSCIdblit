# mSCIdblit v1.9.79

## Gap-driven primary-literature expansion

This release adds evidence routes for cytokine signaling gaps that were
already represented by ligand–receptor pairs and downstream graph layers:

- IL-9 > IL9RA:IL2RG > JAK1 > STAT5 > PIM1
- IL-9 > IL9RA:IL2RG > JAK1 > STAT3 > PIM1
- IL-13 > IL4RA:IL13RA1 > TYK2 > STAT6 > ARG1
- IL-13 > IL4RA:IL13RA1 > TYK2 > STAT6 > RETNLA
- IL-13 > IL4RA:IL13RA1 > TYK2 > STAT6 > CCL11
- CNTF > CNTFR-alpha-gp130-LIFR > JAK2 > STAT3 > BCL2
- CNTF > CNTFR-alpha-gp130-LIFR > JAK2 > STAT3 > SOCS3
- IL-11 > IL11R-alpha:gp130 > STAT3 > SOCS3, with the receptor-proximal
  intracellular continuation retained as unresolved

The IL-9 routes use primary receptor and receptor-mutant studies reporting
JAK1/STAT activation and PIM1 induction (PMID:8756628; PMID:10464327;
PMID:9535918; PMID:9261146). The IL-13 routes combine primary receptor/JAK/STAT
studies with IL13RA1- and STAT6-dependent macrophage output measurements
(PMID:11058569; PMID:23124025; PMID:25766112). The CNTF routes combine primary
receptor-complex, JAK2/STAT3 and neural-lineage output studies
(PMID:8390097; PMID:8385113; PMID:7500350; PMID:27060559; PMID:23845766). The
IL-11 partial route is supported by primary IL-11 receptor/STAT3 and SOCS3
expression studies (PMID:10948192; PMID:11141475; PMID:16709613).

All routes remain evidence-layer annotations: they are non-causal,
non-traversable and carry no database confidence score. Context, multi-branch
signaling and cross-model limitations are retained; no new graph edges are
asserted by this release.

## Release counts

- Route evidence records: 19,459 -> 19,467
- Strict full-route annotations: 59 -> 66
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 8

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion174`.
