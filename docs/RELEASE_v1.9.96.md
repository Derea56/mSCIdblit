# mSCIdblit v1.9.96

## Gap-driven primary-literature expansion

This release adds three bounded ligand–receptor/output annotations selected
from the remaining P1 downstream queue:

- MFG-E8/lactadherin > αVβ5 integrin > DOCK180/Rac1-associated microglial phagocytosis
- TGF-β1 > TGFBR1:TGFBR2 context > Mfge8-associated microglial engulfment
- Microglia-derived LRRC15 > CD248 > JAK/STAT-associated astrocyte-progenitor astrogenesis

The routes use primary studies including PMID:18670887, PMCID:PMC2832904,
PMID:37979054, PMID:25130376 and PMID:38101413. Receptor dependence,
intracellular relays, TF-target links, developmental or injury context and
SCI transfer limitations remain explicit for each route. The records are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,519 -> 19,522
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 3

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion191`.
