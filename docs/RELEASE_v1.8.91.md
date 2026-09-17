# mSCIdblit mechanism graph release v1.8.91

Release date: 2026-09-17

This release adds the 86th selective primary-literature expansion batch for
Module 21B downstream curation. The overlay retains ten newly curated
ligand–receptor output annotations as source-linked evidence routes for mSCS
plausibility analysis. Five routes retain a bounded receptor-to-intracellular
continuation, while five routes retain direct ligand–receptor–output evidence
with the intracellular and transcriptional layers explicitly unassayed.

The routes cover Urocortin-2/3–CRHR2, ANP/BNP–NPR1/GC-A, CNP–NPR2/GC-B,
guanylin/uroguanylin–GUCY2C/GC-C, PTH/PTHrP–PTH1R, and TGF-alpha–EGFR.
Representative primary support includes Urocortin-3/CRHR2-selective cAMP
signaling ([PMID:11416224](https://pubmed.ncbi.nlm.nih.gov/11416224/)),
natriuretic-peptide receptor selectivity and cGMP production
([PMID:1309330](https://pubmed.ncbi.nlm.nih.gov/1309330/),
[PMID:2570358](https://pubmed.ncbi.nlm.nih.gov/2570358/)),
disulfide-dependent guanylin and uroguanylin activation of GC-C
([PMID:9309586](https://pubmed.ncbi.nlm.nih.gov/9309586/)),
PTH1R proximal signaling and endocytosis
([PMID:15016722](https://pubmed.ncbi.nlm.nih.gov/15016722/)),
PTHrP/PTH1R Gs/Gq, beta-arrestin and ERK signaling
([PMID:23516330](https://pubmed.ncbi.nlm.nih.gov/23516330/)),
Urocortin-2/CRHR2-selective functional responses
([PMID:11226328](https://pubmed.ncbi.nlm.nih.gov/11226328/)), and
TGF-alpha-dependent EGFR phosphorylation and proliferation
([PMID:2755700](https://pubmed.ncbi.nlm.nih.gov/2755700/)).

The graph topology is unchanged: no graph edges, causal edges, or database
confidence scores are created. All ten records remain non-causal evidence
routes with `evidence_route_not_causal` traversal status, and the TF and target
gene fields remain unasserted. mSCS can use the retained output and
intracellular evidence as route-plausibility inputs while applying its own
confidence logic.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,641
- Cumulative literature-expansion rows: 594
- Unique downstream queue candidates with literature coverage: 577
- Remaining downstream queue candidates: 2,754, including 1,689 P1 candidates
- Literature route tiers: 15 full routes; 22 with ligand–receptor–intracellular–TF and missing target output; 238 with ligand–receptor–intracellular–output and missing TF; 62 with ligand–receptor–TF–output and missing intracellular continuation; and 257 ligand–receptor–output routes missing intracellular and TF layers

The release is an evidence-layer update only. The remaining queue is intended
for continued selective review, prioritizing routes where primary studies can
add an output or a bounded intracellular continuation without overclaiming
terminal transcriptional effects.
