# mSCIdblit Module 20B–24B mechanism graph v1.8.18

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-013`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion013/`

This thirteenth selective literature-expansion release adds five
source-linked signaling route annotations:

- CSF1 → CSF1R/c-Fms → PI3K p85/p110 → PIP3 and macrophage spreading/invasion output, with TF and target-gene layers unresolved
- Netrin-1 → DCC → FAK/PTK2 → axon-attraction and neurite-outgrowth output, with TF and target-gene layers unresolved
- Netrin-1 → UNC5B → PIKE-L/CENTG1-PI3K → neuronal survival output, with TF and target-gene layers unresolved
- Slit2 → Robo1 → SRGAP1-Cdc42 → neuronal migration-repulsion output, with TF and target-gene layers unresolved
- Glutamate → oligodendroglial AMPA receptor → exosome-release output, with intracellular, TF and target-gene layers unresolved

The annotations preserve receptor aliases, receptor-proximal signaling or
functional readouts, assay model, perturbation context, and species or tissue
limits. The glutamate route demonstrates the output-only form: a measured
ligand–receptor-to-release relationship is retained without assigning an
unmeasured intracellular cascade. Each route remains an evidence record for
mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,112 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 65 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 14 |
| Cumulative L→R→intracellular→output annotations missing TF | 17 |
| Cumulative L→R→TF→output annotations missing intracellular | 14 |
| Cumulative L→R→output-only annotations | 10 |

The graph topology and causal edge counts are unchanged from v1.8.17. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 10958675 and PMID
23648053 (CSF1R-PI3K signaling); PMID 15494734 (Netrin-1-DCC-FAK/Src);
PMID 18469807 (Netrin-1-UNC5B-PIKE-L/PI3K); PMID 11672528
(Slit-Robo1-srGAP1-Cdc42); and PMID 23874151 with PMCID PMC3706306 and DOI
10.1371/journal.pbio.1001604 (glutamate/AMPA-receptor-dependent
oligodendroglial exosome release).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
