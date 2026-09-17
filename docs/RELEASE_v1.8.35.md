# mSCIdblit Module 20B–24B mechanism graph v1.8.35

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-030`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion030/`

This thirtieth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → ???? → transcription factor
→ output` annotations. The batch expands direct receptor-to-transcriptional or
functional-readout coverage across innate, damage-associated and metabolic
signaling:

- PLAP-1/asporin → TLR2 → NF-kB-associated inflammatory inhibition output
- PLAP-1/asporin → TLR4 → NF-kB-associated inflammatory inhibition output
- WNT5A → TLR2 → NF-kB/AP-1-associated cytokine and tolerance output
- WNT5A → TLR4 → NF-kB/AP-1-associated cytokine and tolerance output
- CD24 → Siglec-G → NF-kB-associated DAMP-response inhibition output
- extracellular NAPRT → TLR4 → NF-kB-associated inflammatory output
- SAA1 → TLR4/MD2 → NF-kB-associated inflammatory output
- leptin → LepRb → STAT5-associated phosphorylation/transcriptional output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges, database confidence scores or SCI-specific
claims. The intracellular continuation and terminal target-gene layers remain
explicitly unassayed in all eight records. All eight source queue identifiers
are unique within the cumulative literature-expansion set.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,211 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 164 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 55 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 19 |
| Unused downstream queue candidates remaining | 3,182 |

The graph topology and causal edge counts are unchanged from v1.8.34. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 26399972 (asporin/TLR2
and TLR4 inflammatory inhibition), PMID 31098409 (WNT5A/TLR2 and TLR4
MyD88-NF-kB/AP-1 signaling), PMID 19264983 (CD24/Siglec-G DAMP-response
suppression), PMID 31511522 (extracellular NAPRT/TLR4 inflammation), PMID
35247611 (SAA1/TLR4-MD2/NF-kB signaling), and PMID 17726024
(LepRb Tyr1077/STAT5 signaling).
