# mSCIdblit v1.9.105

## Gap-driven primary-literature expansion

This release adds nine bounded route annotations selected from atypical-receptor,
matrix-DAMP and vascular guidance gaps:

- CXCL10, CXCL12, CXCL13 and CCL28 > GPR182/ACKR5 > chemokine scavenging
- Decorin > TLR2 > p38/ERK/NF-kappaB > inflammatory cytokine output
- Decorin > TLR4-MD2 > NF-kappaB/MAPK > inflammatory cytokine output
- EDA-fibronectin > TLR4-MD2 > fibroblast inflammatory output
- Netrin-1 > UNC5B > LRP6/Wnt-beta-catenin > endothelial barrier output
- Draxin > DCC > neurite/growth-cone guidance output

The routes use primary studies including PMID:33875597, PMID:37554323,
PMID:22087031, PMID:11150311, PMID:24739758, PMID:35246514,
PMID:36711611, PMID:21957262 and PMID:29503192. Noncanonical scavenging,
MD2/TLR co-contribution, endothelial and developmental model boundaries, and
unresolved TF layers remain explicit. These are evidence-layer annotations
only: no graph edges, causal traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,558 -> 19,567
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 9

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion200`.
