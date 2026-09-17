# mSCIdblit Module 20B–24B mechanism graph v1.8.62

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-057`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion057/`

This fifty-seventh selective literature-expansion release adds seven source-
linked glycine ligand–receptor annotations:

- Glycine → GluN1/GluN2D NMDA receptor → co-agonist/channel activation
- Glycine → alpha2beta glycine receptor → strychnine-sensitive chloride-channel output
- Glycine → GluN1/GluN2C NMDA receptor → co-agonist/channel activation
- Glycine → GluN1/GluN2A/GluN2C triheteromer → channel activation
- Glycine → GlyRalpha4 → strychnine-sensitive channel output
- Glycine → GluN1/GluN2A/GluN3A triheteromer → endothelial current, calcium, barrier and actin output
- Glycine → GPR158 → Cache-domain binding, RGS7-Gbeta5/cAMP and neuronal-excitability output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. The evidence distinguishes glycine
co-agonism at NMDA receptors, inhibitory glycine-receptor channel gating,
endothelial barrier responses and noncanonical GPR158 metabotropic signaling.
Intracellular continuation, TF and target-gene layers remain unresolved in all
seven records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,420 |
| Literature-expansion annotations in this batch | 7 |
| Cumulative literature-expansion annotations | 373 |
| Unique covered queue candidates | 358 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 198 |
| Unused downstream queue candidates remaining | 2,973 |
| Unused P1 queue candidates remaining | 1,906 |

The graph topology and causal edge counts are unchanged from v1.8.61. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented include GluN1/GluN2D (PMID 22641781), alpha2beta
glycine receptors (PMID 15301692), GluN1/GluN2C (PMID 18635641; PMCID
PMC2614009), GluN1/GluN2A/GluN2C triheteromers (PMID 30056832), GlyRalpha4
(PMID 10762330), glycine-responsive endothelial NMDARs (PMID 35951110), and
GPR158 mGlyR (PMID 36996198; PMCID PMC10751545; DOI 10.1126/science.add7150).
