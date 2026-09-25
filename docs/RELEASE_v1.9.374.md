# mSCIdblit release v1.9.374

This release extends the all-ligand evidence layer with eight primary-literature
route records across IL-11 and IL-36α. The IL-11 records preserve the
IL-11Rα/gp130→STAT3-associated response and IL33, CCL20, CXCL8, and IL6
gene-expression outputs reported in primary human fibroblasts. The IL-36α
records preserve IL-36R/IL-1RAcP→MyD88/IRAK/NF-κB/MAPK evidence and CXCL1,
CCL5, CXCL8, and CCL20 transcriptional outputs reported in primary keratinocyte
systems.

These are source-linked evidence routes for mSCS plausibility analysis. The
receptor-to-relay, relay-to-TF, and TF-to-target handoffs remain explicitly
unasserted where the cited studies used complementary experiments. No causal
graph edges, confidence scores, or traversal permissions are created.

Queue deduplication yields two new unique curation signatures; the other six
records retain additional route provenance for already represented evidence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,403 → 596,411
- Route nodes: 2,502,592 → 2,502,632
- Route edges: 2,301,956 → 2,301,988
- Literature-expansion rows: 30,289 → 30,297
- Full-sequence curation candidates: 15,510 → 15,512
- Unique ligands in the curation queue: 1,869 (unchanged)
- P1 review candidates: 9,755 (unchanged)
- Coverage summary: 182 full functional-output, 173 full target-gene,
  1,453 partial downstream, and 805 ligand–receptor-only ligand rows

Primary sources: [IL-11 fibroblast signaling and transcriptional response](https://pubmed.ncbi.nlm.nih.gov/36012165/),
[IL-36α keratinocyte inflammatory outputs](https://pubmed.ncbi.nlm.nih.gov/24829417/),
[IL-36 receptor-complex activation](https://pubmed.ncbi.nlm.nih.gov/29180446/),
and [IL-11 receptor/STAT3 signaling](https://pubmed.ncbi.nlm.nih.gov/11141475/).

Validation passed. The inherited warning remains that some evidence sources lack
stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion615/`
