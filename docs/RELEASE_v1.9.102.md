# mSCIdblit v1.9.102

## Gap-driven primary-literature expansion

This release adds five bounded route annotations selected from receptor-entry
gaps:

- HMGB1 > RAGE/heparan sulfate > ERK1/2/p38 > endothelial sprouting
- Haptoglobin–hemoglobin > CD163 > HO-1-associated scavenging output
- SEMA3A > NRP1:PLXNA1 > Plexin/Rab5 relay > growth-cone collapse
- SEMA3A > NRP1:PLXNA2 > neuronal repulsion output
- BMP10 > endoglin-associated receptor context > endothelial output

The routes use primary studies including PMID:21990362, PMID:23671278,
PMID:23781295, PMID:10520994, PMID:22723296, PMID:25161316,
PMID:23104057, PMID:10781943, PMID:21737454 and PMID:17068149. Holoreceptor
composition, accessory-receptor semantics, cell-model boundaries, unresolved
intracellular relays and SCI transfer limitations remain explicit. These are
evidence-layer annotations only: no graph edges, causal traversals or
confidence scores are asserted.

## Release counts

- Route evidence records: 19,539 -> 19,544
- Strict full-route annotations: 77 (unchanged)
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion197`.
