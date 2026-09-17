# mSCIdblit Module 20B–24B mechanism graph v1.8.76

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-071`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion071/`

This seventy-first selective literature-expansion release adds ten bounded
route annotations. Eight add receptor-proximal continuations: CCL1–CCR8–Gi,
ATP–P2Y2–Gq, ADP–P2Y12–Gi, C5a–C5AR1–Gi, 2prime3prime-cGAMP–STING–TBK1,
APRIL–TACI–MyD88, IL1A–IL1R1/IL1RAcP–MyD88, and ANXA1–FPR2–Gi. Two additional
annotations retain IFNL3–IFNLR1:IL10RB evidence with separate STAT1 and STAT2
observations.

These are retained evidence routes, not causal graph edges. The continuation
links are source-supported receptor-proximal observations and may come from
separate experiments or receptor contexts; they are therefore available to
mSCS for plausibility evaluation but do not assert a single complete causal
chain. All routes remain without terminal target genes, and no database
confidence score or SCI-specific transfer is asserted.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,490 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 443 |
| Unique covered queue candidates | 427 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 100 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,904 |
| Unused P1 queue candidates remaining | 1,839 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include CCL1–CCR8 activation and migration ([PMIDs
38040762 and 23878309](https://pubmed.ncbi.nlm.nih.gov/38040762/)), ATP–P2Y2
calcium signaling (PMID 10839197), ADP–P2Y12 Gi signaling (PMID 11196645),
C5a–C5AR1 calcium signaling (PMID 1472004), 2prime3prime-cGAMP–STING binding
(PMID 23747010), APRIL–TACI–MyD88 signaling (PMID 20676093), IL-1 receptor
accessory-protein signaling (PMID 9820540), and IFN-lambda receptor/STAT
observations (PMIDs 28329704 and 23258595).
