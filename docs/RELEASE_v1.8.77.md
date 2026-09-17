# mSCIdblit Module 20B–24B mechanism graph v1.8.77

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-072`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion072/`

This seventy-second selective literature-expansion release adds ten bounded
evidence routes. The routes retain ligand–receptor interactions together with
receptor-proximal intracellular observations, while deliberately leaving the
transcription-factor and terminal-output layers open for mSCS evaluation. The
batch includes CXCL11–ACKR3–β-arrestin, CCL26–CCR1/CCR5 inhibitory routes,
CCL16–CCR1, OX40L–OX40–TRAF2, TL1A–DR3–TRADD, fibrinogen–TLR4–TRAM, collagen
IV–GPR126–GNAS, tryptase–PAR2–Gq/11, and UTS2B–UTS2R–Gi/o evidence.

These are retained evidence routes, not causal graph edges. The continuation
links may come from separate experiments or receptor contexts; they are
therefore available to mSCS for plausibility evaluation but do not assert a
single complete causal chain. The CCL26 routes are represented as inhibitory
or antagonist evidence rather than productive activation. No database
confidence score, causal edge, terminal target gene, or SCI-specific transfer
is asserted.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,500 |
| Literature-expansion annotations in this batch | 10 |
| Cumulative literature-expansion annotations | 453 |
| Unique covered queue candidates | 437 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 110 |
| Cumulative L→R→TF→output annotations missing intracellular | 62 |
| Cumulative L→R→output-only annotations | 244 |
| Unused downstream queue candidates remaining | 2,894 |
| Unused P1 queue candidates remaining | 1,829 |

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors
and preserves all prior `LITEXP` overlay records. Primary studies represented
include ACKR3/chemokine arrestin and scavenging observations ([PMID
27875312](https://pubmed.ncbi.nlm.nih.gov/27875312/)), TL1A/DR3 signaling ([PMID
22017439](https://pubmed.ncbi.nlm.nih.gov/22017439/)), collagen-IV/GPR126
signaling ([PMID 25118328](https://pubmed.ncbi.nlm.nih.gov/25118328/)), and
tryptase/PAR2 signaling ([PMID 11606310](https://pubmed.ncbi.nlm.nih.gov/11606310/));
the remaining route annotations retain their queue-level primary locators and
context limitations.
