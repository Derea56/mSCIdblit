# mSCIdblit release v1.9.356

This release adds a primary-literature TGFB1→TGFBR1/TGFBR2→SMAD3→SMAD3/4→SMAD7
inhibitory-feedback route. The route captures SMAD7 as a target-gene output,
which is important for interpreting pathway attenuation and perturbations of
the TGF-beta response.

This is evidence-layer data only. It does not create graph edges, causal
assertions, confidence scores, or a claim that one experiment demonstrates the
complete sequence.

## Release counts

- Graph nodes: 11,988 (unchanged)
- Graph edges: 14,831 (unchanged)
- Edge-source records: 15,107 (unchanged)
- Signaling route-evidence rows: 596,354 → 596,355
- Route nodes: 2,502,386 → 2,502,391
- Route edges: 2,301,799 → 2,301,803
- Literature-expansion rows: 30,240 → 30,241
- Full-sequence curation candidates: 15,468 (unchanged; the route shares an existing ligand/receptor/relay/TF signature)
- Unique ligands in the curation queue: 1,867 (unchanged)
- P1 review candidates: 9,727 (unchanged)

Primary locators include [PMID:10559222](https://pubmed.ncbi.nlm.nih.gov/10559222/),
[PMID:9311995](https://pubmed.ncbi.nlm.nih.gov/9311995/), and
[PMID:20207738](https://pubmed.ncbi.nlm.nih.gov/20207738/). Validation passed
with no errors; the inherited warning remains that some evidence sources lack
stable public locators.

Bundle:

`data/processed/mechanism_graph_module20_24_v2026_09_25_literature_expansion596/`
