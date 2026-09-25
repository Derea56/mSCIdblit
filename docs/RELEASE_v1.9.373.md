# mSCIdblit release v1.9.373

This release adds three primary-literature ephrin-A1 evidence routes across
the existing graph forms: Efna1/EPHA2 and EFNA1/EPHA2 with PI3K-Akt/ERK and
epithelial migration outputs, plus Efna1/EPHA1 with Lck/Pyk2/PI3K/Vav1/Rho and
T-cell migration. The separate ligand node forms remain distinct.

No causal graph edges, confidence scores, or traversal permissions are
created. The all-ligand curation queue is regenerated with the added
intracellular evidence routes.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,400 → 596,403
- Route nodes: 2,502,583 → 2,502,592
- Route edges: 2,301,950 → 2,301,956
- Literature-expansion rows: 30,286 → 30,289
- Full-sequence curation candidates: 15,507 → 15,510
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,755 (unchanged)
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary locators: [PMID:22247486](https://pubmed.ncbi.nlm.nih.gov/22247486/)
and [PMID:17634955](https://pubmed.ncbi.nlm.nih.gov/17634955/).

Validation passed. The inherited warning remains that some evidence sources
lack stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion614/`
