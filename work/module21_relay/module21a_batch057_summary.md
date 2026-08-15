# Module 21A batch 057 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0818` through `-0842` inclusive. This was an isolated review pass. No Module20A ledgers, the frozen Module20A manifest, or shared Module21A registers were modified.

## Classification

- 25/25 exact queue rows reviewed.
- 23 `reviewed_relay_candidate` rows: primary glutamate receptor pharmacology, receptor-complex assembly, electrophysiology, or proximal G-protein coupling was located for the specified NMDA, AMPA, kainate, or metabotropic receptor entry.
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 heteromers were not directly tested in the located primary comparative studies.
- 0 terminal TF assignments. Ion-channel currents, G-protein coupling, receptor assembly, and receptor subtype pharmacology were not promoted to transcription-factor endpoints.

## Evidence handling

NMDA, AMPA, and kainate entries are receptor-complex or receptor-proximal relay evidence. Direct glutamate-evoked currents, concentration-response relationships, conductance, desensitization, and subtype-selective pharmacology were kept distinct from downstream kinase or TF claims. The NMDA entries preserve the NR1/NR2A-D complex nodes; the AMPA entries preserve GluA1-4; the kainate entries preserve homomeric GluK1-3 and the tested GluK1/2-GluK4/5 heteromers.

The metabotropic entries are receptor-proximal relay evidence based on primary heterologous G-protein coupling. mGlu1 and mGlu5 support Gq/11 with Gi/o branches, while mGlu2/3/4/6/7/8 support predominantly Gi/o coupling. The group III microglia study contributes cellular cAMP/function context but was not used to infer a TF.

The two unresolved records preserve the exact-pair boundary. GluK4 and GluK5 require a partner, and the located primary studies directly tested GluK1/GluK4, GluK1/GluK5, GluK2/GluK4, and GluK2/GluK5, but not the submitted GluK3/GluK4 or GluK3/GluK5 assemblies. Family-level and non-exact heteromer evidence remains in limitations only.

`SLC17A7`, `GLS`, and `GLS2` remain CellChat source-context labels. The receptor assays used exogenous glutamate or receptor agonists and did not demonstrate that the composite source label itself was the experimentally manipulated ligand-release unit. No source-label evidence was substituted for receptor activation.

## Search boundary and primary sources

Searches covered exact receptor-subunit assemblies, canonical gene aliases, glutamate-evoked currents, receptor-complex assembly, AMPA/kainate/NMDA subtype pharmacology, and mGlu G-protein coupling across PubMed, PMC, publisher records, and pathway context resources. Pathway/database co-membership was not promoted as exact-pair evidence.

Representative primary sources include NMDA receptor subunit pharmacology and electrophysiology ([PMID 7476914](https://pubmed.ncbi.nlm.nih.gov/7476914/), [PMID 9463421](https://pubmed.ncbi.nlm.nih.gov/9463421/), [PMID 18635641](https://pubmed.ncbi.nlm.nih.gov/18635641/), [PMID 9625862](https://pubmed.ncbi.nlm.nih.gov/9625862/)); mGlu coupling ([PMID 37546908](https://pubmed.ncbi.nlm.nih.gov/37546908/), [PMID 25193666](https://pubmed.ncbi.nlm.nih.gov/25193666/)); group III cellular cAMP assays ([PMID 12657674](https://pubmed.ncbi.nlm.nih.gov/12657674/)); recombinant AMPA receptor activation ([PMID 37921875](https://pubmed.ncbi.nlm.nih.gov/37921875/), [PMID 19409270](https://pubmed.ncbi.nlm.nih.gov/19409270/)); kainate heteromer function ([PMID 25139762](https://pubmed.ncbi.nlm.nih.gov/25139762/), [PMID 20026616](https://pubmed.ncbi.nlm.nih.gov/20026616/)); and GluK3 homomer function ([PMID 20007474](https://pubmed.ncbi.nlm.nih.gov/20007474/), [PMID 18761361](https://pubmed.ncbi.nlm.nih.gov/18761361/)).

## Validation

- 25 unique review IDs.
- Exact queue membership, order, and canonical pair labels match Module20A rows `-0818` through `-0842`.
- Required fields are populated for every row, including stable citations, species/model, assay, relation type, evidence layer, branch, confidence, limitations, and terminal-TF field.
- Evidence layers distinguish `ligand_receptor_binding_or_activation` for unresolved exact-pair boundaries from `receptor_proximal_relay` for directly tested receptor activation/coupling.
- Frozen Module20A manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Output

The exact batch TSV is [module21a_batch057_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch057_review.tsv).
