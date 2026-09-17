# mSCIdblit mechanism graph release v1.9.8

Release date: 2026-09-17

This release adds the 103rd selective primary-literature expansion batch for
Module 21B downstream curation. The evidence overlay adds ten source-linked
routes for mSCS plausibility analysis across cytokine, chemokine, and
purinergic signaling. Three routes cover previously unexpanded queue
candidates; seven add further evidence to queue candidates covered by earlier
overlays.

The batch includes IL-1β and IL-18 receptor-complex to MYD88 continuations;
IL-6 receptor-complex to JAK1/STAT3; IFN-γ receptor-complex to JAK2; GM-CSF
receptor-complex to JAK2/STAT5; IL-7 receptor-complex to JAK1/STAT5; TGF-β3
receptor-complex to SMAD2; CXCL13–CXCR5 and CXCL16–CXCR6 to G-protein
continuations; and ATP–P2Y2 to GNAQ/GNA11. Primary locators retained in the
bundle include PMID:9820540, PMID:9792649, PMID:11412113, PMID:8649432,
PMID:1460041, PMID:7875201, PMID:18243111, PMID:11688722, PMID:11290797,
PMID:17363916, PMID:10839197, and the associated DOI/PMCID locators.

Three routes retain TF-support evidence (IL-6/STAT3, GM-CSF/STAT5, and
IL-7/STAT5) but no terminal target gene. Seven retain receptor-proximal
intracellular continuation and output evidence without asserting a TF. All
ten remain non-causal evidence routes with `evidence_route_not_causal`
traversal status. No graph edges, causal edges, or database confidence
scores are created.

Verified bundle counts:

- Nodes: 11,952
- Edges: 14,722
- Edge-source records: 14,998
- Signaling route-evidence rows: 16,811
- Cumulative literature-expansion route rows: 764
- Unique downstream queue candidates with literature coverage: 741
- Remaining downstream queue candidates: 2,590
- Remaining P1 candidates: 1,545
- Literature route tiers added: 7 receptor–intracellular–output routes and 3 receptor–intracellular–TF–output routes missing terminal target genes

The release is an evidence-layer update only. mSCS can use the retained
receptor, intracellular, TF-support, and output evidence as route-plausibility
inputs while applying its own confidence logic.
