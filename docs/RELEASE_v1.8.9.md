# mSCIdblit Module 20B–24B mechanism graph v1.8.9

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-004`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion004/`

This fourth selective literature-expansion release adds five source-linked
partial route annotations for mSCS plausibility analysis:

- DLL1 → NOTCH2 → NICD2 → RBPJ/CSL reporter and cleavage output
- IL34 → CSF1R → microglial proliferation/neuroprotective output
- CX3CL1 → CX3CR1 → Gi/PI3K/Ca/MAPK continuation → adhesion/chemotaxis output
- tenascin-C/TNC → TLR4 → NF-κB → cytokine output
- IL37 → IL18R1/IL1R8 → inflammatory-output suppression

These annotations intentionally preserve different evidence depths. They may
support ligand–receptor-to-output plausibility even when intracellular or
transcription-factor layers are absent; unresolved layers remain explicit
gaps for downstream evaluation.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,067 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 20 |
| Cumulative full literature-supported route annotations | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 8 |
| Cumulative L→R→output-only annotations | 3 |

The batch also includes one L→R→intracellular→TF→output annotation with the
target-gene layer unresolved and one L→R→TF→output annotation with the
intracellular layer unresolved. The graph topology and causal edge counts are
unchanged from v1.8.8. This is an evidence-layer overlay: it preserves source
locators, assay context, effect direction, and limitations, but does not add
causal graph edges or database confidence scores. mSCS receives these route
annotations and remains responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 10958687 (DLL1/NOTCH2
cleavage and RBP-J reporter output), PMID 21872563 and PMID 22579672
(IL34/CSF1R functional and receptor evidence), PMID 11432847 and PMID
11781291 (CX3CL1/CX3CR1 intracellular continuation and migration-related
outputs), PMID 29150600 (tenascin-C/TLR4 NF-κB and cytokine output), and PMID
25729923 (IL37/IL18R1–IL1R8 inflammatory-output suppression).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
