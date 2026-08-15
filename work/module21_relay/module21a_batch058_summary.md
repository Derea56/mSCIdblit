# Module 21A batch 058 review summary

Batch scope: exact Module20A priority-8 rows `M20A-CELLCHAT-REMAINING-0843` through `-0867` inclusive. The batch contains Glu-SLC17A7_GLS2 receptor-complex rows `0843–0856` and Glu-SLC17A8_GLS receptor-complex rows `0857–0867`.

No Module20A ledgers, frozen manifest, shared Module21A registers, coverage tables, handoff tables, or pathway-reuse registries were modified. This batch writes only its review TSV and this summary.

## Classification

- 25/25 exact queue rows reviewed.
- 23 `reviewed_relay_candidate` rows: direct primary glutamate receptor activation, receptor-complex electrophysiology, or proximal metabotropic G-protein coupling was located for the specified NMDA, AMPA, kainate, or mGlu receptor entry.
- 2 `reviewed_unresolved` rows: exact GluK3/GluK4 and GluK3/GluK5 heteromeric channel activation was not directly tested in the located primary comparative assays.
- 0 terminal TF assignments. Ion-channel conductance, receptor subtype identity, G-protein coupling, second-messenger readouts, and receptor-complex pharmacology were not promoted to transcription-factor endpoints.

## Evidence handling

NMDA, AMPA, and kainate rows are kept as receptor-complex or receptor-proximal relay evidence. Glutamate-evoked current, concentration-response, conductance, desensitization, permeation, and subunit-specific pharmacology were not conflated with downstream kinase, cellular-function, or TF claims. NMDA complexes preserve the GRIN1/GRIN2A-D nodes; AMPA rows preserve GRIA1-4; kainate rows preserve GRIK1-3 homomers and the directly tested GRIK1/4-5 and GRIK2/4-5 heteromers.

Metabotropic rows preserve the GPCR branch separately from ionotropic receptor complexes. GRM1 and GRM5 support Gq/11 with Gi/o branches, while GRM2-4 and GRM6-8 support predominantly Gi/o coupling. Group III cellular cAMP or microglial context was retained only where it was part of the cited primary evidence and was not used to infer a TF.

The two unresolved rows preserve the exact-complex boundary. Primary kainate comparisons directly tested GluK1/GluK4, GluK1/GluK5, GluK2/GluK4, and GluK2/GluK5; they did not directly test the submitted GluK3/GluK4 or GluK3/GluK5 assemblies. Family-level or non-exact heteromer evidence remains in limitations only.

`SLC17A7`, `SLC17A8`, `GLS`, and `GLS2` remain CellChat source-context labels. The receptor assays used exogenous L-glutamate or receptor agonists and did not demonstrate that each composite source label itself was the experimentally manipulated ligand-release unit. No physical binding of the transporter or glutaminase proteins was inferred.

## Search boundary and primary sources

Searches covered exact receptor-subunit assemblies, canonical GluA/GluK/GluN/mGlu aliases, glutamate-evoked currents, receptor-complex assembly, AMPA/kainate/NMDA subtype pharmacology, and mGlu G-protein coupling across PubMed, PMC/Europe PMC, publisher records, and pathway context resources. Pathway/database co-membership, family-only evidence, review-only evidence, and source-composite expression were not promoted as exact-pair proof.

Representative primary sources include NMDA receptor subunit pharmacology and electrophysiology (`PMID:7476914`, `PMID:9463421`, `PMID:9625862`, `PMID:9380752`, `PMID:18635641`, `PMID:10835034`); metabotropic receptor coupling and cellular cAMP assays (`PMID:37546908`, `PMID:25193666`, `PMID:12657674`, `PMID:8183235`, `PMID:9144651`, `PMID:10216218`, `PMID:10449793`); AMPA receptor activation and subunit electrophysiology (`PMID:37921875`, `PMID:19409270`, `PMID:20980546`, `PMID:34731330`, `PMID:20590632`, `PMID:24349437`); and kainate receptor homomer/heteromer function (`PMID:25139762`, `PMID:20026616`, `PMID:20007474`, `PMID:18761361`, `PMID:20837679`, `PMID:32999066`).

## Validation

- 25 unique review IDs.
- Exact queue membership, order, and canonical pair labels match Module20A rows `-0843` through `-0867`.
- Required fields are populated for every row: stable citations, species/model, assay/perturbation, relation type, evidence layer, pathway branch, confidence, limitations, and terminal-TF field.
- Evidence layers distinguish `ligand_receptor_binding_or_activation` for unresolved exact-pair boundaries from `receptor_proximal_relay` for directly tested receptor activation or coupling.
- No terminal TF field is populated.
- Frozen Module20A manifest SHA256 remains `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.

## Output

The exact batch TSV is [module21a_batch058_review.tsv](/Users/derea/Documents/SCI/mSCIdblit/work/module21_relay/module21a_batch058_review.tsv).
