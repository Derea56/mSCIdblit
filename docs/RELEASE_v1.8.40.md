# mSCIdblit Module 20B–24B mechanism graph v1.8.40

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-035`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion035/`

This thirty-fifth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations. These
records deliberately preserve the intracellular and TF layers as unresolved:

- GDNF → GFRA1:RET → receptor-complex activation output
- IL7 → IL7RA:IL2RG → cytokine-responsive reporter output
- NRG1-beta → ERBB3 → phosphorylation/AKT/ERK output
- PROS1 → MERTK → phosphatidylserine-dependent efferocytosis output
- SCF → KIT → ligand-induced receptor activation output
- DKK1 → LRP6 → Wnt-Frizzled reporter inhibition output
- GAS6 → MERTK → phosphorylation/MAPK output
- latent TGF-β1/LAP → αVβ8 → astrocyte/endothelial reporter output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores, and they do
not assert SCI-specific effects. Receptor activation, reporter, and cellular
functional outputs are not treated as evidence of a particular intracellular
relay, TF, or target gene.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,251 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 204 |
| Unique covered queue candidates | 189 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 29 |
| Unused downstream queue candidates remaining | 3,142 |
| Unused P1 queue candidates remaining | 2,075 |

The graph topology and causal edge counts are unchanged from v1.8.39. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 15722196 and PMID
10545102 (GDNF-GFRA1-RET), PMID 7875201 (IL7 receptor reconstitution), PMID
20682778 and PMID 34759323 (NRG1-ERBB3), PMID 18250462 (PROS1-MERTK), PMID
17255936 and PMID 17662946 (SCF-KIT), PMID 11448771 (DKK1-LRP6), PMID 9160883
(GAS6-MERTK), and PMID 15920172 (latent TGF-β1/αVβ8 activation).
