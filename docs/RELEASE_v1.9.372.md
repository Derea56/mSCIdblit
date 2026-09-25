# mSCIdblit release v1.9.372

This release adds three primary-literature intracellular evidence routes:
CSF1→CSF1R→MEK/ERK/Akt activity in myeloid progenitors, and the two existing
Ntn1 graph representations→DCC→FAK/Src→axon attraction and outgrowth. The
routes deepen existing partial ligand records without merging distinct graph
node identities.

No causal graph edges, confidence scores, or traversal permissions are
created. The all-ligand curation queue is regenerated with the added
intracellular evidence routes.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,397 → 596,400
- Route nodes: 2,502,574 → 2,502,583
- Route edges: 2,301,944 → 2,301,950
- Literature-expansion rows: 30,283 → 30,286
- Full-sequence curation candidates: 15,506 → 15,507
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,755 (unchanged)
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators: [PMID:10958675](https://pubmed.ncbi.nlm.nih.gov/10958675/)
and [PMID:15494734](https://pubmed.ncbi.nlm.nih.gov/15494734/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion613/`
