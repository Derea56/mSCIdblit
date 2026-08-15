# Module 21A batch 055 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0768` through `-0792` inclusive. This was an isolated review pass. No Module20A ledgers, the frozen Module20A manifest, or shared Module21A registers were modified.

## Classification

- 25/25 exact queue rows reviewed.
- 23 `reviewed_relay_candidate` rows: direct primary receptor-complex pharmacology/electrophysiology or receptor-proximal G-protein coupling was located for the specified NMDA, AMPA, kainate, or metabotropic glutamate receptor entry.
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 heteromers were not directly tested in the located primary comparative studies.
- 0 terminal TF assignments. Ion-channel currents, G-protein coupling, receptor assembly, and receptor subtype pharmacology were not promoted to transcription-factor endpoints.

## Evidence handling

The NMDA, AMPA, and kainate rows are receptor-complex or receptor-proximal relay evidence. Direct glutamate-evoked current, concentration-response, desensitization, conductance, or subtype-selective pharmacology was kept distinct from any downstream signaling claim. The metabotropic rows use primary heterologous G-protein coupling assays: mGlu1/mGlu5 showed Gq/11 and Gi/o coupling, while mGlu2/3/4/6/7/8 showed Gi/o-dominant coupling in the cited panel. The group III microglia study supplied a cellular cAMP/function context for mGlu4/6/8 but was not used to infer a TF.

The two unresolved records preserve the exact-pair boundary. GluK4 and GluK5 require a partner, and primary studies directly tested GluK1/GluK4, GluK1/GluK5, GluK2/GluK4, and GluK2/GluK5, but not the submitted GluK3/GluK4 or GluK3/GluK5 assemblies. Family-level statements were retained only as limitations.

`SLC17A6`, `GLS`, and `GLS2` remain CellChat source labels. The receptor assays used exogenous glutamate or receptor agonists and did not demonstrate that the composite source label itself was the experimentally manipulated ligand-release unit. No source-label evidence was substituted for receptor activation.

## Search boundary

Primary PubMed records were searched for exact receptor-subunit assemblies, canonical gene aliases, glutamate-evoked currents, receptor-complex assembly, and mGlu G-protein coupling. Representative primary sources include NMDA receptor subunit pharmacology and electrophysiology (PMIDs 7476914, 9463421, 18635641, 9625862), mGlu coupling (PMIDs 37546908 and 25193666), group III microglial cAMP assays (PMID 12657674), recombinant AMPA receptor activation (PMID 37921875), kainate heteromer function (PMIDs 25139762 and 20026616), and GluK3 homomer function (PMIDs 20007474 and 18761361). Pathway/family resources were not promoted as exact-pair evidence.

## Validation

- 25 unique review IDs.
- Exact queue membership and canonical pair labels match rows `-0768` through `-0792` in order.
- Required fields are populated for every row, including stable citations, species/model, assay, relation type, evidence layer, branch, confidence, limitations, and terminal-TF field.
- Evidence layers distinguish `ligand_receptor_binding_or_activation` for unresolved exact-pair boundaries from `receptor_proximal_relay` for directly tested receptor activation/coupling.
- Frozen Module20A manifest remains unchanged.

## Output

The exact batch TSV is [module21a_batch055_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch055_review.tsv).
