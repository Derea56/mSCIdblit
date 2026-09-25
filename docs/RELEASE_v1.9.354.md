# mSCIdblit release v1.9.354

This release adds three primary-literature TNF receptor evidence routes:
TNF→TNFR1→NF-κB/RELA→IL6, TNF→TNFR2→NF-κB/RELA→IL6, and
TNF→TNFR2→NF-κB→ICAM1. The receptor-specific branches, intracellular
continuation, transcription-factor layer, and target-gene outputs remain
source-linked evidence layers; unresolved handoffs are not promoted to causal
graph edges.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,350 → 596,353
- Route nodes: 2,502,366 → 2,502,381
- Route edges: 2,301,783 → 2,301,795
- Literature-expansion rows: 30,236 → 30,239
- Full-sequence curation candidates: 15,467 → 15,468
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 (unchanged)
- P3 review candidates: 3,871 → 3,872

Primary locators are retained in each route record, including TNFR2 receptor
aggregation and NF-κB studies, TNF-induced astrocyte transcription studies,
and ICAM1/IL6 promoter studies. Validation passed with no errors; the inherited
warning remains that some evidence sources lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion594/`
