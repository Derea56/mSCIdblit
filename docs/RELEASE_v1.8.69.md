# mSCIdblit Module 20B–24B mechanism graph v1.8.69

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-064`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion064/`

This sixty-fourth selective literature-expansion release adds six
source-linked CCN1/CYR61 receptor/output annotations:

- CCN1 → Mac-1 αMβ2 → activated-monocyte adhesion
- CCN1 → α6β1 integrin/HSPG → fibroblast and endothelial adhesion/tubule formation
- CCN1 → αVβ5 integrin → fibroblast migration and mitogenesis
- CCN1 → αVβ3 integrin → endothelial adhesion, migration, and angiogenesis
- CCN1 → αIIbβ3 integrin → activation-dependent platelet adhesion
- CCN1 → αDβ2 integrin → macrophage/foam-cell-context adhesion

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores. Integrin
subunit specificity, peptide or motif dependence, HSPG participation, cell
activation state, and the distinction between direct binding and
integrin-perturbation evidence remain explicit. The batch does not assert an
intracellular continuation, transcription factor, or target gene for any route.

The related CCN1–TLR2 and CCN1–TLR4 queue rows remain held because their
current source records contain no promotable downstream evidence-record row.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,462 |
| Literature-expansion annotations in this batch | 6 |
| Cumulative literature-expansion annotations | 415 |
| Unique covered queue candidates | 400 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 239 |
| Unused downstream queue candidates remaining | 2,931 |
| Unused P1 queue candidates remaining | 1,866 |

Graph topology and causal edge counts are unchanged from v1.8.68. The bundle
passes `validate_module20_24_mechanism_graph.py` with zero errors and preserves
all prior `LITEXP` overlay records.

Primary studies represented include CCN1-H2/Mac-1 monocyte adhesion (PMID
12736251), CCN1-alpha6beta1/HSPG adhesion (PMIDs 10821835 and 12826661),
CCN1-alphaVbeta5 fibroblast migration (PMID 11287419), CCN1-alphaVbeta3
endothelial binding and angiogenesis (PMIDs 9446626 and 15308622),
CCN1-alphaIIbbeta3 platelet adhesion (PMID 10446209), and CCN1-alphaDbeta2
adhesion (PMID 16239428; PMCID PMC1367263).
