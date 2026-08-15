# Module 21A batch 056 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0793` through `-0817` inclusive. This was an isolated, read-only review pass. No Module20A ledgers, frozen manifest, or shared Module21A registers were modified.

## Classification

- 25/25 exact queue rows reviewed.
- 23 `reviewed_relay_candidate` rows: directly tested glutamate-activated NMDA, AMPA, kainate, or metabotropic glutamate receptor entries.
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 heteromers were not directly tested in the located primary comparative studies.
- 0 terminal TF assignments. Ion-channel currents, G-protein coupling, receptor assembly, and receptor subtype pharmacology were not promoted to transcription-factor endpoints.

## Evidence handling

The NMDA, AMPA, and kainate records are receptor-complex or receptor-proximal relay evidence. Glutamate-evoked current, concentration-response, desensitization, conductance, permeation, and subtype-selective pharmacology were kept distinct from downstream kinase, pathway, cellular-function, or TF claims. The metabotropic records use primary G-protein coupling assays: mGlu1/mGlu5 showed Gq/11 and Gi/o branches, while mGlu2/3/4/6/7/8 showed Gi/o-dominant coupling. The group III microglia study supplied cellular cAMP/function context for mGlu4/6/8 but was not used to infer a TF.

The two unresolved records preserve the exact-pair boundary. GluK4 and GluK5 require a partner, and the primary comparative studies directly tested GluK1/GluK4, GluK1/GluK5, GluK2/GluK4, and GluK2/GluK5, but not the submitted GluK3/GluK4 or GluK3/GluK5 assemblies. GluK3 homomer studies do not establish either queued heteromer.

`SLC17A6`, `SLC17A7`, `GLS`, and `GLS2` remain CellChat source-context labels. The receptor assays used exogenous glutamate or receptor agonists and did not demonstrate that the composite source label itself was the experimentally manipulated ligand-release unit. Source-context evidence was therefore not substituted for receptor activation, and no source-to-receptor molecular edge beyond the directly tested glutamate receptor evidence was inferred.

## Search boundary

Primary PubMed records were searched for exact receptor-subunit assemblies, canonical GluA/GluK/GluN/mGlu aliases, glutamate-evoked currents, receptor-complex assembly, and mGlu G-protein coupling. Representative primary sources include NMDA receptor subunit pharmacology and electrophysiology (PMIDs 7476914, 9463421, 18635641, 9625862, 9380752, and 10835034), mGlu coupling and cellular cAMP/function (PMIDs 37546908, 25193666, and 12657674), recombinant AMPA receptor activation (PMIDs 37921875, 19409270, and 20980546), kainate heteromer function (PMIDs 25139762, 20026616, and 20837679), and GluK3 homomer function (PMIDs 20007474 and 18761361). Reactome/KEGG or family-level resources were not promoted as exact-pair evidence.

## Validation

- 25 unique review IDs.
- Exact queue membership and canonical pair labels match rows `-0793` through `-0817` in order.
- Required fields are populated for every row, including stable citations, species/model, assay, relation type, evidence layer, branch, confidence, limitations, and terminal-TF field.
- Evidence layers distinguish `ligand_receptor_binding_or_activation` for unresolved exact-pair boundaries from `receptor_proximal_relay` for directly tested receptor activation/coupling.
- Frozen Module20A manifest remains unchanged.

## Output

The exact batch TSV is [module21a_batch056_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch056_review.tsv).
