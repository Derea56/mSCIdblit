# mSCIdblit Module 20B–24B mechanism graph v1.8.81

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-076`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion076/`

This seventy-sixth selective literature-expansion release adds ten bounded
neuroendocrine GPCR evidence routes: SST-14/SST-28–SSTR3–GNAI,
SST-14/SST-28–SSTR5–GNAI, calcitonin–CALCR–GNAS, CRH–CRHR2–GNAS,
neurokinin A–TACR2–GNAQ/GNA11, neurokinin B–TACR3–GNAQ/GNA11,
melatonin–MTNR1A–GNAI, melatonin–MTNR1B–GNAI, and
prokineticin-1–PROKR1/PKR1 or PROKR2/PKR2–GNAQ/GNA11.

Each annotation retains a primary ligand–receptor claim, a graph-linked
receptor-proximal continuation, and a measured second-messenger or cellular
functional output. The TF and terminal target-gene layers remain open for
mSCS. These are evidence-layer routes, not causal graph edges, and no
database confidence score or SCI-specific transfer is asserted. Context
boundaries include cloned or transfected-cell assays, receptor isoforms,
peptide analogues, independent PLC/PLA2 coupling, ligand-processing effects,
and species- or tissue-specific pharmacology.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,540 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 493 |
| Unique covered queue candidates | 477 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 150 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,854 |
| Unused P1 queue candidates remaining | 1,789 |

Primary studies represented include SSTR3 cloning and cAMP coupling
([PMID 1337145](https://pubmed.ncbi.nlm.nih.gov/1337145/)), SSTR5 cloning
and cAMP inhibition ([PMID 7908405](https://pubmed.ncbi.nlm.nih.gov/7908405/)),
calcitonin-receptor isoform signaling
([PMID 7769107](https://pubmed.ncbi.nlm.nih.gov/7769107/)), CRHR2 cloning
and adenylyl-cyclase activation
([PMID 7846062](https://pubmed.ncbi.nlm.nih.gov/7846062/)), NK2 receptor
PLC/PLA2 outputs ([PMID 9826060](https://pubmed.ncbi.nlm.nih.gov/9826060/)),
NK3 receptor phosphoinositide turnover
([PMID 8117304](https://pubmed.ncbi.nlm.nih.gov/8117304/)), melatonin MT1/MT2
cAMP inhibition ([PMID 10696085](https://pubmed.ncbi.nlm.nih.gov/10696085/)),
and prokineticin receptor calcium/cAMP responses
([PMID 15772293](https://pubmed.ncbi.nlm.nih.gov/15772293/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
