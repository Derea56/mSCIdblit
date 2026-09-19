# mSCIdblit v1.9.59

This release begins a gap-driven literature follow-up after completion of the
existing downstream candidate queue. Three source-linked route annotations were
added for gaps where the database already contained the ligand, receptor and
signaling context but lacked a linked terminal output.

- IL-21 → IL21R/IL2RG → JAK1/JAK3 → STAT3 → IL2RA/CD25
- IL-10 → IL10RA/IL10RB → JAK1/TYK2 → STAT3 → IL1RN
- IL-15 → IL2RB/IL2RG → JAK1/JAK3 → STAT5 → anti-apoptotic survival output

The first two routes have direct primary target-gene support. The IL-15 route
retains the reported BCL2/BCL2L1-associated survival output but does not assert
a direct STAT5-to-single-target-gene edge. All three remain evidence-layer
routes; no causal graph edges or mSCIdblit confidence scores are created.

- Route evidence: 19,408 → 19,411 records
- Explicit ligand–receptor–intracellular–TF–target routes: 15 → 17
- Intracellular–TF/output routes missing target-gene identity: 143 → 144
- Graph topology: 11,952 nodes and 14,722 edges, unchanged
- Downstream curation queue: 3,331 records, unchanged

Primary locators added:

- PMID:24159173; PMCID:PMC3854113
- PMID:15218058; DOI:10.1189/jlb.1003526
- PMID:20440074

The corresponding bundle is
`mechanism_graph_module20_24_v2026_09_16_literature_expansion154`.
