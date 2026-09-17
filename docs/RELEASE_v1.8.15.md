# mSCIdblit Module 20B–24B mechanism graph v1.8.15

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-010`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion010/`

This tenth selective literature-expansion release adds five source-linked
route annotations that extend intracellular coverage:

- BDNF → NTRK2/TrkB → PLCG1 → CREB → CaMKIV/CREB phosphorylation and hippocampal plasticity output, with the terminal gene unresolved
- CSF1 → CSF1R/c-Fms → SFK → STAT5 → Akt/ERK/STAT5 activation and internalization output, with the terminal gene unresolved
- IL-17A → IL-17RA/IL-17RC → ACT1/CIKS → inflammatory-gene transcriptional output, with TF and terminal gene unresolved
- SEMA3A → NRP1/PLXNA2 → FYN/CDK5 → growth-cone and dendrite-orientation output, with TF and terminal gene unresolved
- G-CSF → CSF3R → SHC1 → receptor-proximal phosphorylation/association output, with TF and terminal gene unresolved

The annotations preserve receptor-complex or phosphosite context, assay model,
perturbation context, species or tissue limits, and the distinction between a
measured readout and an inferred missing link. Unresolved layers are not
interpreted as biological absence. Each route remains an evidence record for
mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,097 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 50 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 9 |
| Cumulative L→R→intracellular→output annotations missing TF | 13 |
| Cumulative L→R→TF→output annotations missing intracellular | 13 |
| Cumulative L→R→output-only annotations | 4 |

The graph topology and causal edge counts are unchanged from v1.8.14. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 12367511 (BDNF-TrkB-PLCG1-
CREB); PMID 15297464 (CSF1R Y559/SFK); PMID 17035243 and PMID 17277779
(IL-17 receptor-ACT1); PMID 12372285 (SEMA3A-Plexin-A2/Fyn/Cdk5); and PMID
9824671 (G-CSF receptor-SHC1).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
