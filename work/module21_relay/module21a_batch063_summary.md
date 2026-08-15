# Module 21A batch 063 review

Reviewed the exact 25 Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0968` through `-0992` inclusive. No shared Module21A registers, Module20A ledgers, or frozen manifest were modified.

## Results

- 25/25 exact queue rows written with unique review IDs.
- 23 `reviewed_relay_candidate` rows:
  - 4 NMDA receptor complexes: GRIN1/GRIN2A-D.
  - 8 metabotropic glutamate receptors: Grm1-Grm8.
  - 4 AMPA receptor subtypes: Gria1-Gria4.
  - 5 kainate entries with direct receptor activation or heteromeric electrophysiology: Grik1, Grik1/Grik4, Grik1/Grik5, Grik2, Grik2/Grik4, Grik2/Grik5, and Grik3. (The count is seven kainate rows; the total of 23 comprises 5 + 8 + 4 + 7.)
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 assemblies.
- 0 terminal TF assignments. Subtype identity, ion-channel gating, G-protein coupling, or second-messenger readouts were not promoted to TF evidence.

## Evidence handling

Ionotropic and metabotropic branches remain separate:

- NMDA, AMPA, and the promoted kainate rows are receptor-proximal ion-channel evidence from recombinant activation, concentration-response, patch-clamp, two-electrode voltage-clamp, or ligand-binding/occupancy assays.
- Grm1-Grm8 rows are receptor-proximal metabotropic evidence with Gq/11 or Gi/o coupling and PLC/Ca2+ or cAMP branches. Cellular microglia/retinal observations are retained as context and were not treated as subtype-exclusive where the pharmacology was group-level.
- GluK4/GluK5 assembly and heteromeric function were preserved as receptor-complex evidence. GluK3/GluK4 and GluK3/GluK5 were not promoted because the reviewed primary electrophysiology did not unambiguously isolate those exact complexes.

## Search boundaries and limitations

The search used exact pair labels and receptor aliases (GRIA/GluA, GRIK/GluK, GRIN/GluN, and GRM/mGlu), PubMed/PMC records, publisher-linked primary papers, and the repository’s prior bounded low-evidence packet as a lead list. Primary sources included recombinant receptor pharmacology, patch-clamp or two-electrode voltage-clamp recordings, ligand-binding/occupancy assays, structural receptor studies, and subtype G-protein coupling assays. Pathway databases and family-level reviews were not used to promote an exact edge.

For every row, `SLC1A2` and `GLS`/`GLS2` are retained only as CellChat source-context labels. They were not treated as the physical glutamate ligand, a receptor subunit, or a direct intracellular relay. NMDA rows retain the glycine co-agonist requirement. No downstream kinase-to-TF endpoint was directly established in this batch.

Representative primary sources:

- [GluK3/GluK5 structures and assembly, PMID 20951142](https://pubmed.ncbi.nlm.nih.gov/20951142/)
- [Kainate heteromer pharmacology, PMID 25139762](https://pubmed.ncbi.nlm.nih.gov/25139762/)
- [GluK2/GluK4 and GluK2/GluK5 electrophysiology, PMID 20026616](https://pubmed.ncbi.nlm.nih.gov/20026616/)
- [GluK3 receptor electrophysiology, PMID 20007474](https://pubmed.ncbi.nlm.nih.gov/20007474/)
- [NMDA receptor ligand gating, PMID 39085540](https://pubmed.ncbi.nlm.nih.gov/39085540/)
- [Metabotropic glutamate receptor coupling panel, PMID 37546908](https://pubmed.ncbi.nlm.nih.gov/37546908/)

Output: `module21a_batch063_review.tsv`
