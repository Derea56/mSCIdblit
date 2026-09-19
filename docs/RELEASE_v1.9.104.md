# mSCIdblit v1.9.104

## Gap-driven primary-literature expansion

This release adds nine bounded route annotations selected from receptor-entry
gaps:

- NRG4 > ERBB4 > downstream growth signaling
- EFNA5 > EPHB2 > receptor-proximal guidance signaling > growth-cone collapse
- EPGN > EGFR > mitogenic output
- IL17AF > IL17RA:IL17RC > ACT1-associated signaling > chemokine secretion
- PlGF > FLT1 > receptor autophosphorylation and endothelial activity
- VEGFB > FLT1 > uPA/PAI-1 expression and activity
- SEMA7A > alphaVbeta1 integrin > macrophage IL-10 production
- GDF15 > GFRAL:RET > metabolic physiology
- FGF8b > FGFR2c > developmental patterning output

The routes use primary studies including PMID:10348342, PMID:15107857,
PMID:10769020, PMID:15611079, PMID:16384934, PMID:18684971,
PMID:20231694, PMID:22198947, PMID:8822205, PMID:9751730,
PMID:28846097, PMID:28846098, PMID:28846099 and PMID:31535977. Isoform,
receptor-complex, species and cell-model boundaries remain explicit. These
are evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,549 -> 19,558
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 9

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion199`.
