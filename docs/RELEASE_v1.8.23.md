# mSCIdblit Module 20B–24B mechanism graph v1.8.23

Release date: 2026-09-16  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-018`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion018/`

This eighteenth selective literature-expansion release adds five
source-linked ligand–receptor-to-output annotations. One includes a
source-supported intracellular continuation but no resolved transcription
factor; one includes intracellular and transcription-factor support but no
resolved target gene; and three preserve ligand–receptor-to-output evidence
with transcription-factor support while leaving the intracellular relay
unresolved:

- SFTPD → SIRPA → SHP1 → inhibitory phagocytosis/engulfment output
- FAM19A1/TAFA1 → GPR1 → ERK1/2 neural-stem-cell signaling → STAT3 → cellular functional output
- Secreted serglycin → CD44 → NF-κB → microglial neuroinflammatory output
- SPARC → endoglin → SMAD2 → pericyte migration output
- NODAL → Cripto/ACVR1B:ACVR2B receptor complex → SMAD2/3 → phosphorylation/reporter output

The SFTPD/SIRPA annotation preserves the inhibitory SHP1-linked branch. The
FAM19A1/GPR1 route is a neural-stem-cell comparator with ERK/STAT3 support.
The serglycin/CD44 route is retained as an ischemic-stroke microglial
comparator, without transferring that context to traumatic spinal cord
injury. The SPARC/endoglin annotation describes modulation of endoglin/TGF-β
activity rather than autonomous receptor signaling. The NODAL/Cripto route
preserves receptor assembly and SMAD2/3 activation evidence. Each route
remains an evidence record for mSCS rather than a causal graph assertion.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,137 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 90 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 15 |
| Cumulative L→R→intracellular→output annotations missing TF | 26 |
| Cumulative L→R→TF→output annotations missing intracellular | 27 |
| Cumulative L→R→output-only annotations | 12 |

The graph topology and causal edge counts are unchanged from v1.8.22. This is
an evidence-layer overlay: it retains source locators, assay context, effect
direction, and limitations, but does not add causal graph edges or database
confidence scores. mSCS receives these route annotations and remains
responsible for context-aware plausibility scoring.

Primary studies reviewed for this batch include PMID 22511785/PMCID
PMC3365977/DOI 10.1074/jbc.M111.324533, PMID 14531999/DOI
10.1016/S0092-8674(03)00758-X, and PMCID PMC2453510 (SFTPD/SIRPA/SHP1);
PMID 29799787/DOI 10.1096/fj.201800020RRR (FAM19A1/GPR1 and
ERK/STAT3); PMID 7535771, PMCID PMC10826034, PMID 38287411/DOI
10.1186/s12974-024-03026-6 (serglycin/CD44 and microglial NF-κB);
PMID 21708981/PMCID PMC3216331/DOI 10.1083/jcb.201011143
(SPARC/endoglin/SMAD2); and PMID 18089557 and PMID 11024047
(NODAL/Cripto/SMAD2/3).

The bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.
