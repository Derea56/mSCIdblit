# Module 21A batch 064 review

Reviewed the exact 25 frozen Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0993` through `-1017` inclusive. This batch is standalone: no shared Module21A registers, Module20A ledgers, or frozen release manifest were modified.

## Results

- 25/25 exact queue rows written with unique review IDs.
- 23 `reviewed_relay_candidate` rows:
  - 4 NMDA receptor complexes: GRIN1/GRIN2A-D.
  - 8 metabotropic glutamate receptors: Grm1-Grm8.
  - 4 AMPA receptor subtypes: Gria1-Gria4.
  - 7 kainate entries: Grik1, Grik1/Grik4, Grik1/Grik5, Grik2, Grik2/Grik4, Grik2/Grik5, and Grik3.
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 assemblies.
- 0 terminal TF assignments. Receptor subtype identity, ion-channel gating, G-protein coupling, and second-messenger readouts were not promoted to TF evidence.

## Evidence handling

Ionotropic and metabotropic branches remain distinct:

- NMDA, AMPA, and promoted kainate rows use receptor-proximal ligand-gated ion-channel evidence from recombinant activation, concentration-response, patch-clamp, two-electrode voltage-clamp, ligand-binding, and heteromer-specific pharmacology.
- Grm1-Grm8 rows use receptor-proximal metabotropic evidence with Gq/11 or Gi/o coupling and PLC/Ca2+ or cAMP branches. Group-level native-cell observations are retained as context and are not treated as subtype-exclusive when the perturbation was not subtype selective.
- GluK4/GluK5 assembly and heteromeric function are preserved as receptor-complex evidence. GluK3/GluK4 and GluK3/GluK5 remain unresolved because the reviewed primary assays did not unambiguously isolate those exact complexes.

SLC1A2/GLS2 and SLC1A3/GLS are retained as CellChat source-context labels only. The cited assays tested mature glutamate or receptor-selective agonists on receptor preparations; they did not establish either source composite as the physical ligand or as a direct intracellular relay. NMDA rows retain the glycine co-agonist requirement.

## Search boundaries and limitations

The search covered exact CellChat labels and receptor aliases (GRIA/GluA, GRIK/GluK, GRIN/GluN, and GRM/mGlu) across PubMed/PMC and publisher-linked primary records. Primary evidence was prioritized for recombinant receptor pharmacology, whole-cell/outside-out or single-channel patch clamp, two-electrode voltage clamp, ligand-binding/occupancy, heteromer-specific gating, and subtype G-protein coupling. Reviews, expression-only records, pathway databases, transporter/glutaminase identity, family-only pharmacology, and subtype identity alone were not used to promote a downstream edge or terminal TF.

Representative primary sources include:

- [GluK3-containing receptor electrophysiology, PMID 20007474](https://pubmed.ncbi.nlm.nih.gov/20007474/)
- [Kainate heteromer pharmacology, PMID 25139762](https://pubmed.ncbi.nlm.nih.gov/25139762/)
- [GluK2/GluK4 and GluK2/GluK5 electrophysiology, PMID 20026616](https://pubmed.ncbi.nlm.nih.gov/20026616/)
- [NMDA receptor subunit-composition pharmacology, PMID 9380752](https://pubmed.ncbi.nlm.nih.gov/9380752/)
- [Recombinant NR1/NR2C electrophysiology, PMID 18635641](https://pubmed.ncbi.nlm.nih.gov/18635641/)
- [Metabotropic glutamate receptor coupling panel, PMID 37546908](https://pubmed.ncbi.nlm.nih.gov/37546908/)
- [AMPA receptor subtype pharmacology, PMID 11054828](https://pubmed.ncbi.nlm.nih.gov/11054828/)

Output: `module21a_batch064_review.tsv`
