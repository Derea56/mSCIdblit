# mSCIdblit release v1.9.383

This release adds two primary-literature adiponectin evidence routes. The
ADIPOR1 branch retains adiponectin → ADIPOR1 → APPL1/AMPK → fatty-acid uptake
and oxidation. The ADIPOR2 branch retains adiponectin → ADIPOR2 →
APPL1/Src/Ras/ERK → PPARalpha-associated lipid oxidation. The primary studies
support these receptor-specific downstream observations in cardiomyocyte,
vascular, hepatic, and receptor-expression systems (PMID:20739511; PMCID:
PMC2980363; PMID:18842004; PMCID:PMC2665882).

These are evidence-layer routes for mSCS plausibility analysis. The exact
receptor-to-relay and relay-to-output handoffs remain unasserted graph edges;
the ADIPOR1 branch has no resolved transcription-factor layer, and neither
branch asserts a terminal target gene. No causal traversal, SCI transfer, or
database confidence score is created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 597,184 → 597,186
- Route nodes: 2,506,496 → 2,506,503
- Route edges: 2,305,079 → 2,305,084
- Literature-expansion rows: 31,070 → 31,072
- Full-sequence curation candidates: 15,521 → 15,523
- Unique ligands in the curation queue: 1,869 → 1,870
- Target-gene-expression layer rows in the queue: 821 (unchanged)
- Review priorities: 9,757 P1, 1,876 P2, and 3,890 P3 candidates
- Coverage summary: 183 full functional-output, 174 full target-gene,
  1,452 partial downstream, and 804 ligand–receptor-only ligand rows

The strict graph-chain audit remains unchanged from v1.9.382 because these
additions are evidence-layer routes and do not assert new causal graph
handoffs.

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators; those rows retain their limitations for review.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion624/`
