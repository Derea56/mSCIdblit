# mSCIdblit v1.9.95

## Gap-driven primary-literature expansion

This release adds five bounded ligand–receptor/output annotations selected from
the remaining P1 downstream queue:

- IL-4 > IL-4Rα:IL-2Rγ > oligodendrocyte differentiation and remyelination
- C5a > C5aR1/CD88 > microglial synaptic pruning and engulfment
- TGF-α > EGFR > STAT3-associated oligodendrocyte-lineage protection
- IGF-1 > IGF1R > layer V cortical-neuron survival
- IGF-1 > IGF1R > developmental CNS myelination and myelin-associated gene expression

The routes use primary studies including PMID:31226122, PMID:38278523,
PMID:30834805, PMID:23525041 and PMID:28963396. Receptor dependence,
intracellular relays, TF-target links, developmental or injury context and
SCI transfer limitations remain explicit for each route. The records are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,514 -> 19,519
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion190`.
