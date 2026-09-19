# mSCIdblit v1.9.80

## Gap-driven primary-literature expansion

This release adds two evidence-layer routes that resolve additional
ligand-to-output links without changing the normalized graph:

- IL-11 > IL11R-alpha:gp130 > JAK2 > STAT3 > SOCS3 gene
- IL-26 > IL20RA:IL10RB > ???? > STAT3 > SOCS3 gene

The IL-11 route combines primary evidence for IL-11-induced JAK2 association,
receptor-dependent STAT3 phosphorylation, and SOCS3 expression
(PMID:8702385; PMID:29523682). The IL-26 route combines primary evidence for
IL-26 receptor-dependent STAT1/STAT3 activation and SOCS3 transcription in
receptor-reconstituted epithelial systems (PMID:20947410; PMID:23875025).

The routes remain evidence-layer annotations: they are non-causal,
non-traversable and carry no database confidence score. The IL-11 route is a
composite primary annotation and does not assert direct receptor-to-JAK2 or
JAK2-to-STAT3 graph edges. The IL-26 intracellular continuation remains
unresolved. No new graph edges are asserted by this release.

## Release counts

- Route evidence records: 19,467 -> 19,469
- Strict full-route annotations: 66 -> 67
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 2

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion175`.
