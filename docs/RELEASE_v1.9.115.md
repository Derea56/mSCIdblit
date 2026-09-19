# mSCIdblit v1.9.115

## Gap-driven primary-literature expansion

This release adds five bounded functional-output annotations:

- three true TGFA → EGFR → output routes for astrocyte proliferation,
  migration, and a growth-supportive phenotype after spinal-cord injury
- CD22-dependent microglial phagocytosis as receptor-to-output evidence
- MERTK-dependent astrocyte synapse elimination as receptor-to-output evidence

The TGFA routes reuse the existing validated TGFA-EGFR receptor edge and add
the independently curated SCI output layer. Primary evidence includes the
TGF-alpha SCI studies (PMID:22016551 and PMID:18647603), CD22 blockade and
microglial phagocytosis (PMID:30944478), and astrocyte MERTK-dependent
synapse elimination (PMID:24270812). Intracellular intermediates, TFs and
terminal target genes remain unasserted where not directly measured.

## Release counts

- Route evidence records: 19,672 -> 19,677
- Graph nodes: 11,952 (unchanged)
- Graph edges: 14,722 (unchanged)
- Downstream curation queue records: 3,331 (unchanged)
- Literature-expansion rows in this release: 5

The release bundle is
`data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion210`.
