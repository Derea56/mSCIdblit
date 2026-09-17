# mSCIdblit Module 20B–24B mechanism graph v1.8.86

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-081`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion081/`

This eighty-first selective literature-expansion release adds ten bounded GPCR
ligand–receptor–intracellular-continuation–second-messenger routes. The routes
cover motilin–MLNR/GPR38–GNAQ/GNA11, NPY–Y2R–GNAI/O/Z,
pancreatic polypeptide–Y4R–GNAI/O/Z, 7alpha,25-dihydroxycholesterol–GPR183–
GNAI/O/Z, thrombin–PAR1–GNAQ/GNA11, galanin–GALR2–GNAQ/GNA11,
C3a–C3aR–GNAI/O/Z, ATP–P2Y1–GNAQ/GNA11, OEA–GPR119–GNAS, and
secretin–SCTR–GNAS.

The annotations preserve receptor-specific calcium, phosphoinositide, cAMP,
G-protein, chemotaxis, and functional signaling outputs. The NPY/Y2R and
PP/Y4R routes retain inhibitory cAMP polarity; the remaining routes are
recorded as activating in the cited receptor assays. TF and terminal
target-gene layers remain open for mSCS.

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Several routes come
from cloned or transfected receptor systems, and GPR183 additionally has
immune-cell migration evidence. Receptor coupling is therefore not treated
as proof of a universal tissue-specific pathway or terminal gene response.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,590 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 543 |
| Unique covered queue candidates | 527 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 200 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,804 |
| Unused P1 queue candidates remaining | 1,739 |

Primary studies represented include motilin/MLNR
([PMID 14504130](https://pubmed.ncbi.nlm.nih.gov/14504130/)), NPY/Y2R
([PMID 36525977](https://pubmed.ncbi.nlm.nih.gov/36525977/)), PP/Y4R
([PMID 7592911](https://pubmed.ncbi.nlm.nih.gov/7592911/)), GPR183
([PMID 21796212](https://pubmed.ncbi.nlm.nih.gov/21796212/)), PAR1
([PMID 15878870](https://pubmed.ncbi.nlm.nih.gov/15878870/)), GALR2
([PMID 9685625](https://pubmed.ncbi.nlm.nih.gov/9685625/)), P2Y1
([PMID 11717356](https://pubmed.ncbi.nlm.nih.gov/11717356/)), GPR119
([PMID 16517404](https://pubmed.ncbi.nlm.nih.gov/16517404/)), and SCTR
([PMID 1646711](https://pubmed.ncbi.nlm.nih.gov/1646711/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
