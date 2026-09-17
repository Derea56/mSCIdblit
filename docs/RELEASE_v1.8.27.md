# mSCIdblit Module 20B–24B mechanism graph v1.8.27

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-022`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion022/`

This twenty-second selective literature-expansion release adds five
source-linked ligand–receptor–intracellular-continuation/output annotations.
The transcription-factor and terminal target-gene layers remain unresolved:

- VEGFA → VEGFR2 → PLCγ1 → endothelial MAPK/DNA-synthesis output
- WNT5A → ROR2:FZD7 → DVL2 → RAC1/AP-1 reporter output
- Ephrin-A1 → EPHA4 → Ephexin1-RhoA → axon/growth-cone output
- GAS6 → MERTK → PI3K p85 → phagocytic output
- Tenascin-C FNIII-BD → CNTN1 → PLC signaling → neurite-outgrowth output

The VEGFA entry preserves VEGFR2 Y1175 dependence. The WNT5A entry retains
the multicomponent ROR2:FZD7 topology and does not equate the AP-1 reporter
with a single terminal transcription factor. The ephrin-A1 entry preserves
the neuronal Ephexin1/RhoA cytoskeletal context. The GAS6 entry preserves
MERTK receptor-level PIK3R1/p85 association and possible GRB2 mediation. The
tenascin-C entry preserves FNIII-BD, contactin/beta1-integrin and
calcium/PLC/PKC/CaMK boundaries. None of these routes asserts a causal graph
edge or a database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,157 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 110 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 15 |
| Cumulative L→R→intracellular→output annotations missing TF | 33 |
| Cumulative L→R→TF→output annotations missing intracellular | 38 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.26. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 11387210 and PMCID
PMC125481 (VEGFR2 Y1175–PLCγ endothelial signaling), PMID 20457807
(WNT5A/ROR2:FZD7/DVL2), PMID 10366629 and PMID 15848799 (ephrin-A1/EPHA4
and Ephexin1/RhoA), PMID 9160883 and PMCID PMC3563642 (GAS6/MERTK and
PIK3R1/p85 phagocytic signaling), and PMID 19394429 (tenascin-C/contactin
and PLC-linked neurite outgrowth).
