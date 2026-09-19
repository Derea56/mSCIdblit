# mSCIdblit v1.9.100

## Gap-driven primary-literature expansion

This release adds three bounded ligand–receptor/output annotations selected
from the remaining P1 downstream queue:

- CD47 > SIRPalpha > SHP-1-associated inhibition of macrophage phagocytosis
- WNT5A > ROR2/FZD7 complex > DVL2/Rac1 > AP-1 reporter activation
- Tenascin-C FBG domain > TLR4 complex > NF-kB-associated reporter and cytokine output

The routes use primary studies including PMID:18657508, PMID:11283158,
PMID:20457807 and PMID:29150600. Cell-surface geometry, multicomponent
receptor topology, domain/fragment scope, terminal target-gene links and SCI
transfer limitations remain explicit for each route. The records are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,531 -> 19,534
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion195`.
