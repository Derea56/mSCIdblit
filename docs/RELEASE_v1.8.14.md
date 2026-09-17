# mSCIdblit Module 20B–24B mechanism graph v1.8.14

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-009`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion009/`

This ninth selective literature-expansion release adds five source-linked
route annotations for mSCS plausibility analysis:

- FAM3C/ILEI → LIFR → STAT3 phosphorylation and mammary epithelial/tumor-cell functional output, with the intracellular relay and terminal gene unresolved
- IL-26 → IL-20RA/IL-10RB → STAT1/STAT3 activation and cytokine-response output, with the intracellular relay and terminal gene unresolved
- WNT5A → ROR1 → NF-κB reporter activation, with the intracellular relay and terminal gene unresolved
- GDF11 → ACVR2B/ALK4 → SMAD3-dependent reporter activation, with the intracellular relay and terminal gene unresolved
- Synaptamide → ADGRF1/GPR110 → cAMP/CREB activation and neuronal neurite/synaptogenesis output, with the intracellular relay and terminal gene unresolved

The annotations preserve receptor-complex identity, assay model, perturbation
context, species or tissue limits, and the distinction between a measured
readout and an inferred missing link. Unresolved layers are not interpreted as
biological absence. Each route remains an evidence record for mSCS rather than
a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,092 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 45 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 7 |
| Cumulative L→R→intracellular→output annotations missing TF | 10 |
| Cumulative L→R→TF→output annotations missing intracellular | 13 |
| Cumulative L→R→output-only annotations | 4 |

The cumulative category counts are derived from the nine bounded literature
expansion inputs. The L→R→intracellular→output count is corrected to 10 here;
the v1.8.13 release note reported 11 for that category.

The graph topology and causal edge counts are unchanged from v1.8.13. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 30692635 and PMID 37927213
(FAM3C/ILEI-LIFR); PMID 14764663 and DOI 10.4049/jimmunol.172.4.2006
(IL-26 receptor and STAT1/STAT3 output); PMID 18287027 (WNT5A-ROR1); PMID
16845371 (GDF11 receptor usage and SMAD3 reporter); and PMID 27759003, PMID
32144388, and DOI 10.1038/s42003-020-0831-6 (synaptamide-ADGRF1/GPR110).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
