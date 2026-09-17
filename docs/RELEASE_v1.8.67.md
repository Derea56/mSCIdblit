# mSCIdblit Module 20B–24B mechanism graph v1.8.67

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-062`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion062/`

This sixty-second selective literature-expansion release adds three
source-linked WNT7A receptor/output annotations:

- WNT7A → ADGRA2/GPR124:RECK:LRP5/6 → beta-catenin and TCF-reporter activation
- WNT7A → FZD10 → noncanonical JNK/c-Jun and proliferation output
- WNT7A → FZD7 → Vangl2/planar-cell-polarity and satellite-cell division output

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores. The
GPR124-RECK-LRP5/6 coreceptor architecture, FZD10 co-immunoprecipitation
context, and FZD7/Vangl2 planar-cell-polarity context remain explicit. The
batch does not assert an intracellular continuation, transcription factor, or
target gene for any route.

Two additional WNT7A queue rows—direct RECK binding/stabilization and FZD5
binding—remain held because their current source records do not contain a
promotable downstream evidence-record link.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,450 |
| Literature-expansion annotations in this batch | 3 |
| Cumulative literature-expansion annotations | 403 |
| Unique covered queue candidates | 388 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 227 |
| Unused downstream queue candidates remaining | 2,943 |
| Unused P1 queue candidates remaining | 1,878 |

Graph topology and causal edge counts are unchanged from v1.8.66. The bundle
passes `validate_module20_24_mechanism_graph.py` with zero errors and preserves
all prior `LITEXP` overlay records.

Primary studies represented include WNT7A/GPR124-RECK-LRP5/6 signaling (PMID
40914247; PMCID PMC12514574; DOI 10.1016/j.jbc.2025.110682), WNT7A/FZD10
noncanonical signaling (PMID 18567805; DOI 10.1158/1541-7786.MCR-08-0039),
and WNT7A/FZD7 satellite-cell planar-cell-polarity signaling (PMID 19497282;
PMCID PMC2743383; DOI 10.1016/j.stem.2009.03.013).
