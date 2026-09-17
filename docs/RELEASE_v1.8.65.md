# mSCIdblit Module 20B–24B mechanism graph v1.8.65

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-060`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion060/`

This sixtieth selective literature-expansion release adds seven source-linked
WNT5A receptor/output annotations:

- WNT5A → FZD3 → PI3K/AKT-dependent adhesion readout
- WNT5A → CD146/MCAM → DVL/JNK-dependent protrusion and migration readout
- WNT5A → FZD2 → ROR1/ROR2-dependent Rac activation readout
- WNT5A → FZD5 → PC3-cell proliferation/apoptosis readout
- WNT5A → LRP6 → inhibition of noncanonical WNT5A/Rac1 signaling
- WNT5A → PTK7 → PTK7/ROR2-dependent JNK/AP-1 and cell-movement readout
- WNT5A → RYK → RYK-dependent cortical-axon chemorepulsion readout

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores. Receptor and
coreceptor requirements remain explicit; the batch does not assert an
intracellular continuation, transcription factor, or target gene for any of
the seven routes. The functional readouts remain traversable as plausible
ligand → receptor → output evidence, subject to mSCS evaluation.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,441 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 394 |
| Unique covered queue candidates | 379 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 218 |
| Unused downstream queue candidates remaining | 2,952 |
| Unused P1 queue candidates remaining | 1,888 |

Graph topology and causal edge counts are unchanged from v1.8.64. The bundle
passes `validate_module20_24_mechanism_graph.py` with zero errors and preserves
all prior `LITEXP` overlay records.

Primary studies represented include WNT5A/FZD3 adhesion and PI3K/AKT signaling
(PMID 17804197; DOI 10.1016/j.cellsig.2007.07.023), WNT5A/CD146 signaling
(PMID 24335906; DOI 10.1038/ncomms3803), WNT5A/FZD2 noncanonical signaling
(PMID 19910923; PMCID PMC2808370), WNT5A/FZD5/RYK prostate-cancer readouts
(PMID 29930766; PMCID PMC6007469), WNT5A/LRP6 antagonism (PMID 19056682),
PTK7/ROR2 planar-cell-polarity signaling (PMID 26499793; PMCID PMC4683276),
and RYK-dependent axon guidance (PMID 16723543; PMCID PMC6675257).
