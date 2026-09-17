# mSCIdblit Module 20B–24B mechanism graph v1.8.32

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-027`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion027/`

This twenty-seventh selective literature-expansion release adds ten
source-linked route annotations. Five connect a ligand–receptor input through
an intracellular continuation and transcription factor to a documented target
gene output:

- BDNF → TrkB → PLCγ1/CaMK-associated continuation → CREB → Bdnf promoter IV
- IL-2 → IL-2 receptor complex → JAK1/JAK3 → STAT5 → CISH
- EPO → EPOR → JAK2 → STAT5 → CISH
- Growth hormone → GHR → JAK2 → STAT5 → SOCS2
- Prolactin → PRLR → JAK2 → STAT5 → SOCS2

The remaining annotations add receptor-proximal intracellular and output
evidence for IL-9 → IL-9R → JAK1/JAK3 → STAT1/3/5, TPO → MPL → JAK2 →
STAT5-like activation, IL-17A → IL17RA:IL17RC → ACT1/CIKS → inflammatory
gene output, CD40L → CD40 → TRAF6 → NF-κB/JNK/p38/Akt output, and CSF1 →
CSF1R → SFK → STAT5-associated output.

These annotations preserve model, isoform, receptor-site and assay boundaries.
They are evidence-layer records for mSCS plausibility analysis: they do not
create causal graph edges, database confidence scores or SCI-specific claims.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,187 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 140 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 39 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 19 |

The graph topology and causal edge counts are unchanged from v1.8.31. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 12367511 and PMID
31915257 (BDNF/TrkB/PLCG1/CREB), PMID 8580378 and PMID 9129017
(IL-2/JAK/STAT5/CISH), PMID 8343951 (EPOR/JAK2), PMID 9231797 (GHR/JAK2/STAT5),
PMID 7515493 and PMID 7925280 (PRLR/JAK2/STAT5), PMID 9535918 and PMID
9261146 (IL-9R/JAK/STAT), PMID 7796811 (MPL/JAK2/STAT5), PMID 17035243 and
PMID 17277779 (IL-17R/ACT1), PMID 9718306 and PMID 16260598 (CD40/TRAF6),
and PMID 15297464 (CSF1R/SFK/STAT5-associated output).
