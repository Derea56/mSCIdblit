# mSCIdblit Module 20B–24B mechanism graph v1.8.33

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-028`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion028/`

This twenty-eighth selective literature-expansion release adds eight unused
P1 queue candidates as source-linked `ligand → receptor → intracellular
continuation → output` annotations. The batch expands receptor-proximal
coverage for PDGFRB, Dectin-2, Mincle and CSF3R while explicitly leaving
transcription-factor and target-gene layers unresolved:

- PDGF-BB → PDGFRB → GRB2, SHP2 and ABL2 → Ras/MAPK, migration or activation
  readouts
- mannan → Dectin-2 → FcRγ → inflammatory/phagocytic output
- TDM → Mincle → FcRγ → macrophage-activation/phagocytic output
- G-CSF → CSF3R → GRB2 or SHP2 → receptor-proximal phosphorylation/signaling
  output

These records are deliberately evidence-layer annotations for mSCS route
plausibility. They do not create causal graph edges, database confidence
scores or SCI-specific claims. All eight source queue identifiers are unique
within the cumulative literature-expansion set.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,195 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 148 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 47 |
| Cumulative L→R→TF→output annotations missing intracellular | 45 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,198 |

The graph topology and causal edge counts are unchanged from v1.8.32. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 7935391 (PDGFRB pY716
and Grb2), PMID 10391677, PMID 7691811, PMID 7688466 and PMID 10318871 (PDGFRB
SHP2 docking and outputs), PMID 34144039 (PDGFRB pY771 and Abl2), PMID 17050534
and PMID 19703985 (Dectin-2/FcRγ signaling), PMID 23921530, PMID 20008526 and
PMID 20164423 (Mincle/FcRγ receptor context), and PMID 9824671
(CSF3R/Grb2/SHP2 receptor-proximal binding).
