# mSCIdblit release v1.9.355

This release adds a primary-literature norepinephrine→ADRB2→GNAS→CREB→BDNF
promoter-IV route. It preserves promoter-IV activity as a distinct target-gene
output alongside the existing BDNF exon-IV and exon-VI transcript routes.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,353 → 596,354
- Route nodes: 2,502,381 → 2,502,386
- Route edges: 2,301,795 → 2,301,799
- Literature-expansion rows: 30,239 → 30,240
- Full-sequence curation candidates: 15,468 (unchanged; the new route shares an existing ligand/receptor/relay/TF signature)
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 (unchanged)

Primary locators are PMID:28983964, PMID:22593004, PMID:17681645, and
PMID:15056290. Validation passed with no errors; the inherited warning remains
that some evidence sources lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion595/`
