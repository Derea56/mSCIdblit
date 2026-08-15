# Module 21A batch 069 review summary

- Scope: exactly queue rows 1026–1050, review IDs `M20A-CELLCHAT-REMAINING-1118` through `-1142`.
- Reviewed: 25 exact rows; 23 `reviewed_relay_candidate` and 2 `reviewed_unresolved`.
- Unresolved boundary: `GRIK3_GRIK4` and `GRIK3_GRIK5`; primary studies support GluK3 ligand-binding properties and GluK4/GluK5 partner-dependent assemblies, but the exact GluK3-containing heteromers were not isolated sufficiently for promotion.
- Relay additions: recombinant NMDA receptor activation (GRIN1/GRIN2A-D), mGlu1–8 receptor-proximal G-protein coupling, AMPA GluA1–4 activation, and kainate GluK1–3 plus GluK1/2-GluK4/5 heteromer activation.
- Evidence layers: the two unresolved GluK3 complex rows retain ligand/receptor binding-or-activation evidence; promoted rows are receptor-proximal relay. No downstream functional-output edge or terminal TF was promoted.
- Source-context boundary: `SLC1A7/GLS` and `SLC1A7/GLS2` are retained only as glutamate-source labels. The cited assays tested mature glutamate or receptor-selective agonists on receptor preparations; they did not establish either source composite as the physical ligand or as a direct intracellular relay.
- Search boundary: exact CellChat labels and receptor aliases were checked against PubMed-indexed primary studies and publisher-linked records for subunit composition, glutamate activation, electrophysiology, ligand binding, heteromer-specific gating, and subtype G-protein coupling. Representative primary records include PMID 20951142/21907808/25139762 for kainate composition and gating; PMID 7476914/9463421/9625862/18635641 for NMDA activation; PMID 25193666/37546908 for mGlu receptor coupling; and PMID 19409270/21516102/21946847/37921875/32452760 for AMPA receptor activation. Reviews, expression-only records, source-processing annotations, family-only pharmacology, and subtype identity alone were not used to promote a downstream edge or TF.
- Shared registers, Module 20A ledgers, frozen manifest, and integration outputs were not modified.

Output: `module21a_batch069_review.tsv`
