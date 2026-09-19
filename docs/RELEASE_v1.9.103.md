# mSCIdblit v1.9.103

## Gap-driven primary-literature expansion

This release adds five bounded route annotations selected from receptor-entry
gaps:

- LIGHT > HVEM > NIK-associated STAT3 phosphorylation > transcriptional output
- LIGHT > LTbetaR > NIK-associated STAT3 phosphorylation > transcriptional output
- FasL > FAS > FADD/caspase-8/caspase-3 relay > apoptosis
- WNT5A > ROR2 > JNK > migration or convergent-extension output
- EDA > EDAR > NF-kappaB/RELB > ectodermal-appendage transcriptional output

The routes use primary studies including PMID:17543278, PMID:12839624,
PMID:17101698, PMID:18667433, PMID:19619491, PMID:22451941,
PMID:30037996 and PMID:36765055. Receptor-branch ambiguity, cell-model
boundaries, unresolved terminal TF-target edges and SCI transfer limitations
remain explicit. These are evidence-layer annotations only: no graph edges,
causal traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,544 -> 19,549
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion198`.
