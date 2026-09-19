# mSCIdblit v1.9.78

## Gap-driven primary-literature expansion

This release upgrades one IL-23 receptor route with a named intracellular
continuation and target-gene output:

- IL-23 > IL12RB1:IL23R > JAK2/TYK2 > STAT3 > IL17A

The route is supported by primary studies reporting IL-23 receptor-associated
JAK2/TYK2 and STAT3 activation together with IL-23-dependent IL17A or
RORgammaT output (PMID:27193299; PMID:23673666; PMID:19542449;
PMID:28878115). It remains an evidence-layer route rather than a causal graph
traversal. The p19/p40 IL-23 branch, shared IL-12Rbeta1 component, multi-STAT
signaling and T-cell-state limitations are preserved. No database confidence
score is added.

## Release counts

- Route evidence records: 19,458 -> 19,459
- Strict full-route annotations: 58 -> 59
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 1

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion173`.
