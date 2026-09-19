# mSCIdblit v1.9.125

This release adds ten bounded primary-literature ligand–receptor–output annotations to the Module 21b mechanism evidence layer. The routes preserve receptor-to-output evidence for downstream use by mSCS while leaving intracellular continuation, transcription-factor, target-gene, and causal assertions unasserted unless directly curated.

## Added routes

- APOE → SORL1/SorLA: receptor-mediated binding and endocytosis (PMID:11294867).
- OSTN/osteocrin → NPR3/NPR-C: clearance modulation, cGMP, and bone-growth output (PMID:17951249; PMID:34260913).
- Tryptamine → GPRC5A: receptor-proximal beta-arrestin recruitment (PMID:37248411).
- Alpha-synuclein preformed fibrils → LAG3/CD223: receptor-dependent uptake, transmission, and neurotoxicity (PMID:27708076).
- IGFBP3 → TMEM219: stem/beta-cell apoptosis and homeostasis output (PMID:26431183; PMID:26216267).
- AHSG/Fetuin-A → INSR: receptor autophosphorylation, IRS-1, and mitogenic-signaling inhibition (PMID:11026561; PMID:7906861; PMID:2766355).
- eCIRP → TREM1: DAP12/Syk-associated and inflammatory cytokine output (PMID:32027618).
- Endothelin-1 → EDNRA/ETA: phosphatidylinositol-hydrolysis output (PMID:8336519).
- Endothelin-1 → EDNRB/ETB: phosphatidylinositol-hydrolysis output (PMID:8336519).
- Dopamine → DRD2/D2: pertussis-toxin-sensitive adenylyl-cyclase inhibition (PMID:2571073).

## Bundle accounting

- Route evidence records: 19,767 → 19,777 (+10).
- Graph nodes: 11,952 (unchanged).
- Graph edges: 14,722 (unchanged).
- Downstream evidence queue: 3,331 (unchanged).
- Literature-expansion rows: 10.
- Bundle: `data/processed/mechanism_graph_module20_24_v2026_09_19_literature_expansion220`.

These additions are evidence routes rather than causal graph edges. They are therefore traversable by downstream evidence-aware consumers as plausible ligand-to-output observations, but they do not assert a complete intracellular relay or transcriptional mechanism.
