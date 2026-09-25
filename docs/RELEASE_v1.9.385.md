# mSCIdblit release v1.9.385

This release adds two primary-literature evidence routes for unresolved ligand
coverage.

NGF is extended from a receptor-proximal/downstream-output route to a target-
gene route: NGF → NTRK1/TrkA → ERK1/2 → CREB → Bdnf promoter IV/BDNF
expression. The route composes primary neuronal studies supporting NGF/TrkA,
ERK and CREB activation, and BDNF induction (PMID:9528766; PMID:9334420;
PMCID:PMC6573719; PMID:15207334). The receptor-to-ERK and ERK-to-CREB
handoffs remain unasserted as direct graph edges; the CREB-to-Bdnf promoter-IV
edge is retained from existing graph evidence.

AMH is added as an intracellular-to-output route: AMH → AMHR2 → SMAD1/5/8 →
Fshb and Inhbb expression. The primary gonadotrope study measured AMH-
associated SMAD1/5/8 phosphorylation and Fshb/Inhbb transcripts but did not
establish a named terminal TF or direct promoter handoff (PMID:27030385;
PMCID:PMC4815011). The route therefore remains partial and evidence-only.

Neither route creates a graph edge, causal traversal permission, SCI transfer,
or database confidence score.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,187 → 597,189
- Route nodes: 2,506,508 → 2,506,517
- Route edges: 2,305,088 → 2,305,095
- Literature-expansion rows: 31,073 → 31,075
- Full-sequence curation candidates: 15,524 → 15,525
- Unique ligands in the curation queue: 1,871 → 1,872
- Target-gene-expression layer rows in the queue: 822 → 823
- Review priorities: 9,757 P1, 1,877 P2, and 3,891 P3 candidates
- Coverage summary: 182 full functional-output, 176 full target-gene,
  1,453 partial downstream, and 802 ligand–receptor-only ligand rows

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion626/`
