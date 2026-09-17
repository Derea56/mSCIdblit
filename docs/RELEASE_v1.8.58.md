# mSCIdblit Module 20B–24B mechanism graph v1.8.58

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-053`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion053/`

This fifty-third selective literature-expansion release completes the currently
identified WNT3A P1 receptor-proximal candidates by adding two source-linked
`ligand → receptor/partner → output` annotations:

- WNT3A → Biglycan/BGN → extracellular WNT3A retention, LRP6 phosphorylation and beta-catenin/TCF reporter output
- WNT3A → PTK7/CCK4 → extracellular association and inhibited canonical beta-catenin reporter output

Biglycan is retained as an extracellular WNT3A-binding/modulatory partner rather
than being treated as a conventional signaling receptor. PTK7 is retained as a
catalytically inactive, context-dependent WNT co-receptor/antagonist. Both
records remain evidence-layer annotations for mSCS route plausibility. They do
not create causal graph edges or database confidence scores, and they do not
assert SCI-specific effects. Intracellular continuation, TF and target-gene
layers remain unresolved in both records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,389 |
| Literature-expansion annotations in this batch | 2 |
| Cumulative literature-expansion annotations | 342 |
| Unique covered queue candidates | 327 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 167 |
| Unused downstream queue candidates remaining | 3,004 |
| Unused P1 queue candidates remaining | 1,937 |

The graph topology and causal edge counts are unchanged from v1.8.57. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records.

Primary studies represented in this batch are the biglycan/WNT3A/LRP6 study
(PMID 21969569; PMCID PMC3193219; DOI 10.1073/pnas.1110629108) and the
PTK7/Otk-WNT3A canonical-inhibition study (PMID 21772251; PMCID PMC3173783;
DOI 10.1038/emboj.2011.236).
