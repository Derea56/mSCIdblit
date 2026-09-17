# mSCIdblit Module 20B–24B mechanism graph v1.8.85

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-080`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion080/`

This eightieth selective literature-expansion release adds ten bounded GPCR
ligand–receptor–intracellular-continuation–second-messenger routes. The routes
cover ghrelin–GHSR1A–GNAQ/GNA11, VIP–VPAC1/VPAC2–GNAS,
PACAP–PAC1–GNAS, NPY–Y1R–GNAI/O/Z, CCK–CCK1R–GNAQ/GNA11,
adenosine–A2A/A2B–GNAS, angiotensin II–AT1–GNAQ/GNA11, and
vasopressin–V1a–GNAQ/GNA11.

The annotations preserve receptor-specific cAMP, calcium, phosphoinositide,
adenylate-cyclase, CRE-reporter, and pertussis-toxin-sensitive outputs. NPY
retains inhibitory cAMP polarity; the remaining routes are recorded as
activating in the cited receptor assays. TF and terminal target-gene layers
remain open for mSCS.

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Most evidence comes
from cloned or transfected receptor systems, so receptor coupling is not
treated as proof of a universal tissue-specific pathway or terminal gene
response. CRE-reporter activity is retained as a functional output readout and
is not converted into a TF-to-target-gene edge.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,580 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 533 |
| Unique covered queue candidates | 517 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 190 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,814 |
| Unused P1 queue candidates remaining | 1,749 |

Primary studies represented include ghrelin/GHSR1A activation
([PMID 11087562](https://pubmed.ncbi.nlm.nih.gov/11087562/)), VIP/VPAC1
([PMID 1675791](https://pubmed.ncbi.nlm.nih.gov/1675791/)), VIP/VPAC2
([PMID 7733904](https://pubmed.ncbi.nlm.nih.gov/7733904/)), NPY/Y1R
([PMID 1321422](https://pubmed.ncbi.nlm.nih.gov/1321422/)), CCK1R
([PMID 18776046](https://pubmed.ncbi.nlm.nih.gov/18776046/)), adenosine/A2A
([PMID 8297372](https://pubmed.ncbi.nlm.nih.gov/8297372/)), adenosine/A2B
([PMID 1325798](https://pubmed.ncbi.nlm.nih.gov/1325798/)), angiotensin II/AT1
([PMID 8047068](https://pubmed.ncbi.nlm.nih.gov/8047068/)), and vasopressin/V1a
([PMID 8106369](https://pubmed.ncbi.nlm.nih.gov/8106369/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
