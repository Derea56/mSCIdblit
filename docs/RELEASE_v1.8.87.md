# mSCIdblit Module 20B–24B mechanism graph v1.8.87

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-082`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion082/`

This eighty-second selective literature-expansion release adds eleven bounded
GPCR ligand–receptor–intracellular-continuation–second-messenger routes. The
routes cover PGI2–IP–GNAS, alpha-MSH–MC4R–GNAS, PGE2–EP3–GNAI,
PGE2–EP4–GNAS, U46619–TP–GNAQ/GNA11, 2-AG–CB1–GNAI/O/Z,
TIP39–PTH2R–GNAS, fMLF–FPR1–GNAI2/GNAI3, protons–GPR65–GNAS,
TRH–TRHR–GNAQ/GNA11, and GnRH–GNRHR–GNAQ/GNA11.

The annotations preserve receptor-specific cAMP, calcium, phosphoinositide,
ion-channel, and G-protein outputs. The PGE2–EP3, NPY-family, and other
inhibitory cAMP branches retain their measured polarity; the remaining routes
are recorded as activating in the cited receptor assays. TF and terminal
target-gene layers remain open for mSCS.

These are evidence-layer routes, not causal graph edges; no database
confidence score or SCI-specific transfer is asserted. Several routes come
from cloned or transfected receptor systems, and receptor coupling can vary
with receptor isoform, ligand form, cell type, and assay context. These
annotations therefore do not establish a universal tissue-specific pathway or
terminal gene response.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,601 |
| Literature-expansion annotations in this batch | 11 |
| Cumulative literature-expansion annotations | 554 |
| Unique covered queue candidates | 538 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 211 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,793 |
| Unused P1 queue candidates remaining | 1,728 |

Primary studies represented include prostacyclin/IP, melanocortin, PGE2/EP3
([PMID 8135729](https://pubmed.ncbi.nlm.nih.gov/8135729/)), thromboxane,
2-AG/CB1 ([PMID 9915812](https://pubmed.ncbi.nlm.nih.gov/9915812/)),
TIP39/PTH2R ([PMID 12559132](https://pubmed.ncbi.nlm.nih.gov/12559132/)),
fMLF/FPR1, proton/GPR65, TRH/TRHR, and GnRH/GNRHR receptor-coupling studies.
Direct primary evidence supports receptor-specific cAMP, calcium,
phosphoinositide, ion-channel, or G-protein outputs for the selected routes,
including PGE2–EP3 inhibitory cAMP signaling and TIP39–PTH2R cAMP and calcium
signaling.

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records.
