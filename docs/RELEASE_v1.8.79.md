# mSCIdblit Module 20B–24B mechanism graph v1.8.79

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-074`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion074/`

This seventy-fourth selective literature-expansion release adds ten bounded
GPCR evidence routes: histamine–HRH1–GNAQ/GNA11, histamine–HRH3–GNAI/O/Z,
GLP-1–GLP1R–GNAS, glucagon–GCGR–GNAS, urotensin II–UTS2R–GNAI/O/Z,
anandamide–CB1–GNAI, anandamide–CB2–GNAI/O/Z,
norepinephrine–ADRB1–GNAS, orexin–OX1R–GNAQ, and medium-chain fatty
acids–GPR84–GNAI/O/Z.

Each annotation retains a primary ligand–receptor claim, a graph-linked
receptor-proximal continuation, and a measured receptor, second-messenger, or
cellular-functional output. The TF and terminal target-gene layers remain open
for mSCS. These are evidence-layer routes, not causal graph edges, and no
database confidence score or SCI-specific transfer is asserted. Context
boundaries include cloned or recombinant receptor systems, tissue-specific
assays, non-exclusive GPCR coupling, and behavioral or inflammatory outputs.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,520 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 473 |
| Unique covered queue candidates | 457 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 130 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,874 |
| Unused P1 queue candidates remaining | 1,809 |

Primary studies represented include HRH1 cloning and electrophysiological
response ([PMID 1722337](https://pubmed.ncbi.nlm.nih.gov/1722337/)), HRH3
cloning and cAMP inhibition ([PMID 10347254](https://pubmed.ncbi.nlm.nih.gov/10347254/)),
GLP1R cloning and adenylyl-cyclase stimulation
([PMID 1326760](https://pubmed.ncbi.nlm.nih.gov/1326760/)), GCGR cloning and
second-messenger response ([PMID 8384375](https://pubmed.ncbi.nlm.nih.gov/8384375/)),
UTS2R cloning and calcium mobilization
([PMID 10581185](https://pubmed.ncbi.nlm.nih.gov/10581185/)), CB1 and CB2
cloning and cAMP inhibition ([PMID 8768742](https://pubmed.ncbi.nlm.nih.gov/8768742/);
[PMID 7565624](https://pubmed.ncbi.nlm.nih.gov/7565624/)), beta1-adrenergic
cardiac cAMP pharmacology ([PMID 2575531](https://pubmed.ncbi.nlm.nih.gov/2575531/)),
orexin receptor discovery and feeding output
([PMID 9491897](https://pubmed.ncbi.nlm.nih.gov/9491897/)), and GPR84
medium-chain-fatty-acid signaling ([PMID 16966319](https://pubmed.ncbi.nlm.nih.gov/16966319/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
