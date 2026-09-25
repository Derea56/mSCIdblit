# mSCIdblit release v1.9.378

This release adds three primary-literature evidence routes: CNTF through the
CNTF receptor complex and JAK2-STAT3 to BCL2, IL-22 through IL-22R and
JAK1-STAT3 to SOCS3, and IL-13 through the type-II IL-13 receptor and
TYK2-STAT6 to ARG1.

These are source-linked evidence routes for mSCS plausibility analysis. The
receptor-to-relay, relay-to-TF, and TF-to-target handoffs remain explicitly
unasserted where the cited studies use complementary experiments or models. No
causal graph edges, confidence scores, or traversal permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,416 → 596,419
- Route nodes: 2,502,657 → 2,502,672
- Route edges: 2,302,008 → 2,302,020
- Literature-expansion rows: 30,302 → 30,305
- Full-sequence curation candidates: 15,515 (unchanged after deduplication)
- Unique ligands in the curation queue: 1,869 (unchanged)
- Review priorities: 9,755 P1, 1,875 P2, and 3,885 P3 candidates
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary sources: [CNTF/JAK2-STAT3 and BCL2 in oligodendrocytes](https://pubmed.ncbi.nlm.nih.gov/27060559/),
[CNTF/JAK2-STAT3 neuroprotection](https://pubmed.ncbi.nlm.nih.gov/29171438/),
[IL-22 receptor/STAT3/SOCS3 signaling](https://pubmed.ncbi.nlm.nih.gov/15120652/),
[IL-13 receptor JAK1/TYK2/STAT6 signaling](https://pubmed.ncbi.nlm.nih.gov/9278458/),
and [IL-13Rα1-dependent STAT6/Arg1 induction](https://pubmed.ncbi.nlm.nih.gov/25766112/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion619/`
