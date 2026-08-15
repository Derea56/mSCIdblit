# Module 21A batch 054 review summary

Batch scope: exact priority-8 queue IDs `M20A-CELLCHAT-REMAINING-0743` through `-0767`, inclusive. The output contains 25/25 exact queue rows. No Module 20A ledgers, frozen manifest, or shared Module 21A registers were modified.

## Classification

- 6 `reviewed_function_only` connexin channel records: Cx46/Cx43, Cx46/Cx46, Cx40/Cx40, Cx45/Cx43, Cx45/Cx40, and Cx45/Cx45. These are direct gap-junction channel-function records, not secreted-ligand/receptor relays.
- 7 `reviewed_unresolved` connexin records: all rows involving mouse Gja6/Cx33 plus the exact Cx46/Cx40 and Cx46/Cx45 searches. Family-level connexin compatibility was not transferred to an exact pair.
- 1 `reviewed_relay_candidate` NRXN1beta-Cbln1-Grid2/GluD2 receptor-complex record. Binding, stoichiometry, synaptogenic assays, and complex-stabilized channel electrophysiology support a receptor-complex/pathway edge.
- 11 `reviewed_relay_candidate` mature ionotropic glutamate-receptor records: four AMPA subunit rows (`Gria1`–`Gria4`) and seven kainate rows (`Grik1`, `Grik1_Grik4`, `Grik1_Grik5`, `Grik2`, `Grik2_Grik4`, `Grik2_Grik5`, `Grik3`). Primary recombinant electrophysiology directly measured glutamate-evoked currents for the listed receptor subunits or complexes.
- 0 terminal TF assignments. Gap-junction conductance, Grid2 complex function, and ionotropic receptor currents do not establish a terminal transcription factor.

## Evidence handling

Connexin evidence was kept in `downstream_pathway_function` and represented channel formation, junctional conductance, dye/electrical coupling, and voltage gating. It was not treated as an extracellular ligand-receptor interaction. The Gja6 symbol was checked as mouse Cx33; no exact Cx33 pair assay was found in the bounded primary-literature search.

For `Glu-NRXN1_CBLN1 -> Grid2`, the evidence supports the assembled NRXN1beta-Cbln1-GluD2 trans-synaptic complex. The channel-gating study used glycine/D-serine after complex stabilization, so it was not converted into a claim of glutamate gating or a TF endpoint.

For `Glu-SLC17A6_GLS`, the mature signaling molecule was treated as glutamate. SLC17A6/VGLUT2 and GLS were retained as vesicular transport/biosynthetic context labels and were not treated as the molecular ligand or as receptor subunits. AMPA and kainate rows therefore record receptor-proximal glutamate-to-channel relay evidence while explicitly limiting the source-composite LR interpretation. Receptor complexes were preserved for GluK1/GluK4, GluK1/GluK5, GluK2/GluK4, and GluK2/GluK5.

## Primary evidence and search boundary

Primary gap-junction support included Cx43/Cx46 electrophysiology (PMID 20664797), Cx40/Cx45/Cx43 heterotypic gating (PMID 17189315), and Cx45/Cx43 gating (PMID 12011467). Primary Grid2-complex support included NRXN1beta-Cbln1-GluD2 assembly and synaptogenic assays (PMID 22457515, PMID 22117778) plus complex-stabilized delta-receptor channel electrophysiology (PMID 34936451). Primary AMPA support used whole-cell glutamate responses from homomeric GluR1–4 receptors (PMID 14645491). Primary kainate support used recombinant GluK1/GluK2 homomers and GluK1/GluK2 plus GluK4/GluK5 heteromers (PMID 25139762, PMID 20026616), with GluK3 fast glutamate-application electrophysiology (PMID 20007474).

Searches covered exact gene/protein aliases, connexin-number aliases, receptor complex notation, PubMed, PMC, publisher pages, and electrophysiology/complex-study terms. Database and family-level hits were retained only as search boundaries; no family-level result was promoted to an unresolved exact pair.

## Output

The exact TSV is `work/module21_relay/module21a_batch054_review.tsv`. This is intentionally review-only; no shared-register or SQL materialization changes were made.
