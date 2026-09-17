# mSCIdblit Module 20B–24B mechanism graph v1.8.50

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-17-literature-expansion-045`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion045/`

This forty-fifth selective literature-expansion release adds eight unused P1
candidates as source-linked `ligand → receptor → output` annotations for
GABA-A receptor assemblies:

- GABA → GABRA5:GABRB3:GABRG2 → receptor-gating and tonic-current output
- GABA → GABRA2:GABRB3:GABRG2 → receptor-gating and whole-cell-current output
- GABA → GABRA6:GABRB3:GABRD → receptor-gating and tonic-current output
- GABA → GABRA1:GABRB3:GABRG2 → receptor-gating and chloride-current output
- GABA → GABRA4:GABRB2:GABRD → receptor-gating and single-channel-current output
- GABA → GABRA6:GABRB2:GABRG2 → receptor-gating and whole-cell-current output
- GABA → GABRA2:GABRB2:GABRG2 → receptor-gating and chloride-current output
- GABA → GABRA3:GABRB3:GABRG2S → receptor-gating and single-channel-current output

These records remain evidence-layer annotations for mSCS route plausibility.
They do not create causal graph edges or database confidence scores, and they
do not assert SCI-specific effects. Recombinant expression systems, receptor
assembly, species, extrasynaptic or splice contexts, and assay boundaries are
retained; intracellular continuation, TF, and target-gene layers remain
unresolved in all eight records.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,331 |
| Literature-expansion annotations in this batch | 8 |
| Cumulative literature-expansion annotations | 284 |
| Unique covered queue candidates | 269 |
| Cumulative L→R→intracellular→TF→target-gene annotations | 15 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 22 |
| Cumulative L→R→intracellular→output annotations missing TF | 85 |
| Cumulative L→R→TF→output annotations missing intracellular | 53 |
| Cumulative L→R→output-only annotations | 109 |
| Unused downstream queue candidates remaining | 3,062 |
| Unused P1 queue candidates remaining | 1,995 |

The graph topology and causal edge counts are unchanged from v1.8.49. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors and
preserves all prior `LITEXP` overlay records. The alpha5beta3gamma2 annotation
uses the verified primary locator PMCID:PMC3652748 / PMID:23634821; the queue's
inherited PMID:22579672 is not the PMID for that article.

Primary studies represented in this batch include PMID 23634821 (alpha5beta3gamma2
and alpha6beta3delta extrasynaptic functional outputs), PMID 22711532
(alpha2beta3gamma2 and alpha6beta3delta), PMID 19556611 (alpha1beta3gamma2),
PMID 18227274 (alpha4beta2delta), PMID 17395622 (alpha6beta2gamma2), PMID
10719214 (alpha2beta2gamma2), and PMID 20038526 (alpha3beta3gamma2S).
