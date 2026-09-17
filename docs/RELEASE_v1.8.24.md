# mSCIdblit Module 20B–24B mechanism graph v1.8.24

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-019`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion019/`

This nineteenth selective literature-expansion release adds five
source-linked ligand–receptor-to-output annotations. Two include a
source-supported receptor-proximal intracellular continuation but no
transcription factor; one includes a source-reported transcription-factor
associated output while leaving the intracellular relay unresolved; and two
preserve ligand–receptor-to-output evidence without assigning either layer:

- CD47 → SIRPA → SHP1 → inhibitory macrophage-phagocytosis output
- CD200 → CD200R1 → DOK2/RasGAP → inhibitory MAPK and myeloid degranulation/cytokine output
- C1q → LAIR1 → ITIM-phosphorylation and immune-tolerance output
- C1q → TREM2 → complement-suppressive microglial synaptic-engulfment output
- SP-D → MD-2:TLR4 → NF-κB → attenuated TNF-α secretion output

The CD47/SIRPα and CD200/CD200R1 entries retain distinct inhibitory
checkpoint mechanisms: SHP1-associated signaling for SIRPα and the
non-ITIM DOK2/RasGAP relay for CD200R1. The C1q/LAIR1 entry preserves
collagen-like-region binding and ITIM phosphorylation without inferring the
downstream phosphatase order. The C1q/TREM2 entry retains the
neurodegeneration comparator and does not import the separate TREM2-DAP12
branch. The SP-D/TLR4 entry records NF-κB and TNF-α attenuation as an LPS
antagonism route, not productive TLR4 activation. Each route remains an
evidence record for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,142 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 95 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 15 |
| Cumulative L→R→intracellular→output annotations missing TF | 28 |
| Cumulative L→R→TF→output annotations missing intracellular | 28 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.23. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 18657508 and PMID
11283158 (CD47/SIRPα/SHP1 and macrophage phagocytosis); PMID 15557172 and
DOI 10.4049/jimmunol.173.11.6786 (CD200/CD200R1/DOK2 and myeloid
inhibition); PMID 23093673/PMCID PMC3503216/DOI 10.1073/pnas.1212753109
and PMID 34066122/PMCID PMC8151509/DOI 10.3390/ijms22105125
(C1q/LAIR1); PMID 37442133/DOI 10.1016/j.immuni.2023.06.016
(C1q/TREM2); and PMID 18990700/DOI 10.1074/jbc.M807268200
(SP-D/MD-2:TLR4, NF-κB and TNF-α output).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
