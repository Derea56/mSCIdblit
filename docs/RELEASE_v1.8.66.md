# mSCIdblit Module 20B–24B mechanism graph v1.8.66

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-061`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion061/`

This sixty-first selective literature-expansion release adds six
source-linked C1q/complement-component-1q receptor/output annotations:

- C1q → CD33/SIGLEC3 → LAIR1-associated inhibitory ITIM phosphorylation
- C1q → MEGF10/SR-F3 → apoptotic-cell engulfment
- C1q → SCARF1/SR-F1 → apoptotic-cell capture and uptake
- C1q → LAIR2/CD306 → soluble-decoy inhibition of LAIR1 phosphorylation
- C1q → CD93/C1qRp → phagocytic/antigen-uptake context
- C1q → C1R → C1r/C1s classical-complement complex assembly and activity

These records are evidence-layer annotations for mSCS route plausibility. They
do not create causal graph edges or database confidence scores. Multivalent
C1q bridging, soluble-decoy behavior, and the distinction between CD91,
calreticulin/CD91, and other scavenger-receptor contexts remain explicit. The
batch does not assert an intracellular continuation, transcription factor, or
target gene for any route.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,447 |
| Literature-expansion annotations in this batch | 6 |
| Cumulative literature-expansion annotations | 400 |
| Unique covered queue candidates | 385 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 54 |
| Cumulative L→R→output-only annotations | 224 |
| Unused downstream queue candidates remaining | 2,946 |
| Unused P1 queue candidates remaining | 1,881 |

Graph topology and causal edge counts are unchanged from v1.8.65. The bundle
passes `validate_module20_24_mechanism_graph.py` with zero errors and preserves
all prior `LITEXP` overlay records.

Primary studies represented include C1q/CD33/LAIR1 inhibitory crosslinking
(PMID 28325905; PMCID PMC5412647), C1q/MEGF10 efferocytosis (PMID 27170117;
PMCID PMC4863057), C1q/SCARF1 apoptotic-cell recognition (PMID 23892722;
PMCID PMC3752698), C1q/LAIR2 decoy competition (PMID 23093673; PMCID
PMC3503216), C1qRp/CD93 expression-cloning evidence (PMID 11781389), and
C1q/C1r/C1s classical-complement assembly (PMID 19473974; PMCID PMC2740559;
PMID 457626).
