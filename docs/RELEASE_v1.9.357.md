# mSCIdblit release v1.9.357

This release adds four primary-literature TGFB2→TGFBR1/TGFBR2→SMAD2/3-SMAD4
evidence routes for microglial homeostasis-marker expression: CX3CR1, TMEM119,
P2RY12, and SALL1. These routes preserve the full proposed sequence so mSCS
can use the evidence as a plausible signaling route while retaining the
unasserted receptor-to-relay, relay-to-TF, and TF-to-target handoffs.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,355 → 596,359
- Route nodes: 2,502,391 → 2,502,411
- Route edges: 2,301,803 → 2,301,819
- Literature-expansion rows: 30,241 → 30,245
- Full-sequence curation candidates: 15,468 (unchanged; the routes share an existing ligand/receptor/relay/TF signature)
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 (unchanged)

Primary locator: [PMID:31653855](https://pubmed.ncbi.nlm.nih.gov/31653855/) and
[PMCID:PMC6857135](https://pmc.ncbi.nlm.nih.gov/articles/PMC6857135/).
Validation passed with no errors; the inherited warning remains that some
evidence sources lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion597/`
