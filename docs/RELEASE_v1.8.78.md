# mSCIdblit Module 20B–24B mechanism graph v1.8.78

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-073`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion073/`

This seventy-third selective literature-expansion release adds ten bounded
receptor-proximal evidence routes: CCL8–CCR5–GNAZ, CD30L–CD30–TRAF2,
BAFF–BCMA–TRAF2, proBDNF–p75NTR–TRAF6, Fetuin-A–TLR4–TRAM,
collagen III–GPR56–GNA12, laminin-211–GPR126–GNAS, histamine–HRH4–GNAI,
AVP–AVPR1B–Gq/11, and adenosine–ADORA3–GNAI.

Each annotation retains measured receptor or cellular output while leaving the
TF and terminal target-gene layers open for mSCS. These are evidence-layer
routes, not causal graph edges, and no database confidence score or
SCI-specific transfer is asserted. Context boundaries include antagonist or
biased-receptor behavior, co-receptor requirements, receptor cleavage or
mechanical-force dependence, and heterologous-cell or developmental models.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,510 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 463 |
| Unique covered queue candidates | 447 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 120 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,884 |
| Unused P1 queue candidates remaining | 1,819 |

Primary studies represented include CCL8/CCR5 calcium and receptor signaling
([PMID 11930329](https://pubmed.ncbi.nlm.nih.gov/11930329/)), CD30L/CD30
binding and functional output ([PMID 11754357](https://pubmed.ncbi.nlm.nih.gov/11754357/)),
BAFF/BCMA B-cell survival ([PMID 10880534](https://pubmed.ncbi.nlm.nih.gov/10880534/)),
proBDNF/p75NTR/sortilin apoptosis ([PMID 15930396](https://pubmed.ncbi.nlm.nih.gov/15930396/)),
Fetuin-A/TLR4 inflammatory signaling ([PMID 22842477](https://pubmed.ncbi.nlm.nih.gov/22842477/)),
collagen III/GPR56 RhoA signaling ([PMID 24949629](https://pubmed.ncbi.nlm.nih.gov/24949629/)),
laminin-211/GPR126 function ([PMID 25695270](https://pubmed.ncbi.nlm.nih.gov/25695270/)),
HRH4 cloning and coupling ([PMID 11181941](https://pubmed.ncbi.nlm.nih.gov/11181941/)),
V1b cloning and calcium signaling ([PMID 7929452](https://pubmed.ncbi.nlm.nih.gov/7929452/)),
and ADORA3 cloning and cAMP inhibition ([PMID 1323836](https://pubmed.ncbi.nlm.nih.gov/1323836/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
