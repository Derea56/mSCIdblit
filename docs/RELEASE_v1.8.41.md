# mSCIdblit Module 20B–24B mechanism graph v1.8.41

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-036`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion036/`

This thirty-sixth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations. These
records deliberately preserve the intracellular and TF layers as unresolved:

- IL34 → CSF1R → myeloid proliferation output
- disulfide HMGB1 → MD-2:TLR4 → macrophage cytokine-release output
- DLL1 → NOTCH2 → cleavage/translocation/reporter output
- CXCL12 → CXCR4 → GPCR and cell-migration output
- mature HGF → MET → phosphorylation and cell-migration output
- CX3CL1 → CX3CR1 → leukocyte adhesion/migration output
- GM-CSF/CSF2 → CSF2RA:CSF2RB → myeloid activation/proliferation output
- VEGF165 → NRP1:KDR → endothelial functional output

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
| Evidence-route records | 16,259 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 212 |
| Unique covered queue candidates | 197 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 37 |
| Unused downstream queue candidates remaining | 3,134 |
| Unused P1 queue candidates remaining | 2,067 |

The graph topology and causal edge counts are unchanged from v1.8.40. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies represented in this batch include PMID 22579672 (IL34-CSF1R),
PMID 20547845 (HMGB1-TLR4/MD-2), PMID 10958687 (DLL1-NOTCH2), PMID 28325822
(CXCL12-CXCR4), PMID 15218027 (mature HGF-MET), PMID 25395671
(CX3CL1-CX3CR1), PMID 1460041 and PMID 11721371 (GM-CSF receptor complex),
and PMID 15920019 (VEGF165-NRP1/KDR).
