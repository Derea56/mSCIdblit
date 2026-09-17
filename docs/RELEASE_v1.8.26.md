# mSCIdblit Module 20B–24B mechanism graph v1.8.26

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-021`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion021/`

This twenty-first selective literature-expansion release adds five
source-linked ligand–receptor-to-transcription-factor/output annotations.
Each preserves the missing intracellular continuation and terminal target
gene as unresolved evidence layers for mSCS plausibility analysis:

- HHLA2 → KIR3DL3 → NF-κB → inhibitory immune-cell output
- Tenascin-R FBG domain → TLR4 → NF-κB → sterile-inflammatory output
- Tenascin-W FBG domain → TLR4 → NF-κB → sterile-inflammatory output
- 12(S)-HETE → GPR31/12-HETER → NF-κB → PC-3 functional output
- TFF2 → LINGO3 → STAT3 → mucosal barrier-repair output

The HHLA2/KIR3DL3 entry preserves human checkpoint and SHP-1/2 context. The
tenascin entries remain FBG-domain and TLR4-assay specific. The 12(S)-HETE
entry preserves stereochemistry, GPR31/12-HETER nomenclature and the
recombinant/PC-3 model boundary. The TFF2/LINGO3 interaction remains weak and
non-exclusive, with additional receptor-complex components possible. None of
these routes asserts a causal graph edge or a database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,152 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 105 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 15 |
| Cumulative L→R→intracellular→output annotations missing TF | 28 |
| Cumulative L→R→TF→output annotations missing intracellular | 38 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.25. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 34244312 and PMCID
PMC9744578 (HHLA2/KIR3DL3 inhibitory signaling), PMID 29150600, PMCID
PMC5693923 and DOI 10.1038/s41598-017-13704-0 (tenascin FBG/TLR4 signaling),
PMID 21712392 and PMCID PMC3190773 (12(S)-HETE/GPR31 signaling), and PMID
33941035, PMCID PMC8647134 and DOI 10.1080/00365521.2021.1917650
(TFF2/LINGO3 mucosal repair).
