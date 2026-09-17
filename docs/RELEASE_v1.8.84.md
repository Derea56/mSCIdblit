# mSCIdblit Module 20B–24B mechanism graph v1.8.84

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-079`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion079/`

This seventy-ninth selective literature-expansion release adds ten bounded
GPCR ligand–receptor–G-protein–second-messenger routes. The routes cover
GIP–GIPR–GNAS, GLP-2–GLP2R–GNAS, GHRH–GHRHR–GNAS,
somatostatin–SSTR4–GNAI, MCH–MCHR1–GNAI/O/Z, MCH–MCHR2–GNAQ/GNA11,
dopamine–DRD5–GNAQ/GNA11, UDP–P2Y6–GNAQ/GNA11, UDP-glucose–P2Y14–GNAI,
and ADP–P2Y13–GNAI.

The annotations preserve measured cAMP, calcium, phosphoinositide, PLC,
receptor-coupling, and pertussis-toxin-sensitive outputs. The SSTR4 route
retains inhibitory cAMP polarity; the remaining routes are recorded as
activating in the cited receptor assays. TF and terminal target-gene layers
remain open for mSCS.

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Most evidence comes
from cloned or transfected receptor systems, so receptor coupling is not
treated as proof of a universal tissue-specific pathway or terminal gene
response.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,570 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 523 |
| Unique covered queue candidates | 507 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 180 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,824 |
| Unused P1 queue candidates remaining | 1,759 |

Primary studies represented include GIP receptor activation
([PMID 7589426](https://pubmed.ncbi.nlm.nih.gov/7589426/)), GLP-2 receptor
activation ([PMID 9990065](https://pubmed.ncbi.nlm.nih.gov/9990065/)), GHRH
receptor signaling ([PMID 1333056](https://pubmed.ncbi.nlm.nih.gov/1333056/)),
MCH receptor coupling ([PMID 10559938](https://pubmed.ncbi.nlm.nih.gov/10559938/)),
MCHR2 signaling ([PMID 11416225](https://pubmed.ncbi.nlm.nih.gov/11416225/)),
and P2Y13 activation ([PMID 11546776](https://pubmed.ncbi.nlm.nih.gov/11546776/)).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
