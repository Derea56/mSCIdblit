# mSCIdblit release v1.9.377

This release adds three primary-literature evidence routes: IL-34 through
CSF1R and JNK/AP-1 to cFos, IL-9 through IL-9R and JAK1/JAK3-STAT5 to BCL3,
and PDGF-BB through PDGFRB/PLCγ1-ERK-Elk-1 to cFos.

These are source-linked evidence routes for mSCS plausibility analysis. The
receptor-to-relay, relay-to-TF, and TF-to-target handoffs remain explicitly
unasserted where the cited studies use complementary experiments or models. No
causal graph edges, confidence scores, or traversal permissions are created.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,413 → 596,416
- Route nodes: 2,502,642 → 2,502,657
- Route edges: 2,301,996 → 2,302,008
- Literature-expansion rows: 30,299 → 30,302
- Full-sequence curation candidates: 15,513 → 15,515
- Unique ligands in the curation queue: 1,869 (unchanged)
- Review priorities: 9,755 P1, 1,875 P2, and 3,885 P3 candidates
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary sources: [IL-34/CSF1R JNK/AP-1 and c-Fos promoter
activation](https://pubmed.ncbi.nlm.nih.gov/33800170/), [IL-9 regulation of
BCL3 through Jak/STAT](https://pubmed.ncbi.nlm.nih.gov/10361130/), [IL-9-dependent
STAT5 and PIM1 signaling](https://pubmed.ncbi.nlm.nih.gov/10919676/), [IL-9
receptor/JAK3 signaling](https://pubmed.ncbi.nlm.nih.gov/16763206/), [PDGF-BB
PLCγ1/ERK/Elk-1 and c-fos](https://pubmed.ncbi.nlm.nih.gov/21285289/), [PDGF
receptor-mediated c-fos promoter activation](https://pubmed.ncbi.nlm.nih.gov/1310326/),
and [PDGF-BB ERK1/2 activation](https://pubmed.ncbi.nlm.nih.gov/9299466/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion618/`
