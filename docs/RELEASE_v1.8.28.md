# mSCIdblit Module 20B–24B mechanism graph v1.8.28

Release date: 2026-09-17  
Graph identifier: `module20_24_mechanism_graph:2026-09-16-literature-expansion-023`  
Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_16_literature_expansion023/`

This twenty-third selective literature-expansion release adds five
source-linked ligand–receptor downstream annotations. Three entries add a
receptor-proximal continuation and transcription-factor-associated output;
two entries add a ligand–receptor–transcription-factor/output bridge while
retaining the intracellular continuation as unresolved. No entry asserts a
terminal target gene:

- BAFF → BAFFR → TRAF3 → NF-κB reporter output
- Acetylated LDL → MSR1 → TRAF6 → NF-κB reporter/inflammatory output
- TNF → TNFR2 with IL17RD/Sef heteromeric modulation → TRAF2 → NF-κB reporter output
- IL-11 → IL11Rα:gp130 → STAT3 phosphorylation output
- IL-4 → IL4Rα:IL2Rγ → STAT6 phosphorylation/DNA-binding output

The BAFFR entry preserves the atypical PVPAT motif and noncanonical TRAF3
semantics. The MSR1 entry preserves the inhibitory TRAF6 signaling-control
context rather than treating it as a generic uptake relay. The TNFR2 entry
retains IL17RD/Sef as a heteromeric receptor modulator, not as a ligand or
autonomous receptor. The IL-11 and IL-4 entries preserve direct STAT output
evidence while leaving JAK/other intracellular ordering and terminal target
genes unresolved. None of these routes asserts a causal graph edge or a
database confidence score.

| Artifact | Count |
|---|---:|
| Nodes | 11,952 |
| Traversable edges | 14,722 |
| Linked edge-source rows | 14,998 |
| Evidence-route records | 16,162 |
| Literature-expansion annotations in this batch | 5 |
| Cumulative literature-expansion annotations | 115 |
| Cumulative full literature-supported route annotations | 10 |
| Cumulative L→R→intracellular→TF→output annotations missing target gene | 18 |
| Cumulative L→R→intracellular→output annotations missing TF | 33 |
| Cumulative L→R→TF→output annotations missing intracellular | 40 |
| Cumulative L→R→output-only annotations | 14 |

The graph topology and causal edge counts are unchanged from v1.8.27. The
bundle passes `validate_module20_24_mechanism_graph.py` with zero errors.

Primary studies reviewed for this batch include PMID 15585864 and PMID
15644327 (BAFFR PVPAT–TRAF3/noncanonical NF-κB), PMID 21460221 and PMCID
PMC3099696 (MSR1–TRAF6 inflammatory signaling control), PMID 25378394 and
PMCID PMC4294508 (TNFR2–IL17RD/Sef heteromer and TRAF2/NF-κB), PMID 11141475
and PMCID PMC1850253 (IL-11Rα/gp130–STAT3 phosphorylation), and PMID 9492265
and PMID 9712048 (IL-4 receptor–STAT6 activation).
