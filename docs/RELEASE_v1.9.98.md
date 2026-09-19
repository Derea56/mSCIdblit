# mSCIdblit v1.9.98

## Gap-driven primary-literature expansion

This release adds three bounded ligand–receptor/output annotations selected
from the remaining P1 downstream queue:

- ATP > P2X7/P2RX7 > ATP-primed microglial IL-1beta release
- Osteopontin/SPP1 > alphaVbeta3 integrin > CD44 surface stabilization and hyaluronan adhesion
- TSP1/THBS1 > CD36 > inhibition of endothelial migration, tube formation and vessel sprouting

The routes use primary studies including PMID:11943809, PMID:15325806 and
PMID:23640500. Receptor dependence, priming requirements, intracellular
relays, terminal target-gene links, context and SCI transfer limitations
remain explicit for each route. The records are evidence-layer annotations
only: no graph edges, causal traversals or confidence scores are asserted.

## Release counts

- Route evidence records: 19,527 -> 19,530
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion193`.
