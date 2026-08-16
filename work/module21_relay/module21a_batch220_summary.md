# Module 21A batch 220 review summary

This batch reviews exactly the 25 user-specified queued Module20A pairs in the
submitted order, using the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Only the batch TSV and this summary were written. Module20A ledgers, the
frozen LR manifest, shared Module21A registers, and SQL/materialized outputs
were not modified.

## Disposition

- 25 data rows with exact IDs and pair labels; 13 columns per row.
- 18 `reviewed_relay_candidate` rows: IL-24, IL-33, IL-34, both IL-4
  receptor-complex forms, IL-5, IL-6, IL-7, IL-9, insulin/IGF1R,
  insulin/INSR, INSL3/RXFP2, INSL5/RXFP4, JAG1/CD46, KISS1/KISS1R,
  KITL/KIT, L1CAM/EGFR, and LEP/LEPR.
- 7 `reviewed_binding_only` rows: INHBA/ENG, INSL5/RXFP3, L1CAM/alpha5beta1,
  L1CAM/alphaVbeta3, LAMA1/alpha1, LAMA2/alpha1, and LAMA5/BCAM.
- No `reviewed_unresolved` or `no_evidence_boundary` rows were required in
  this exact batch because each pair had either a qualifying direct binding
  record or a bounded receptor-complex/pathway record.
- Eight rows carry provisional terminal-TF candidates for Module22A
  validation: STAT3 for IL-24, IL-6, and LEP; STAT6 for both IL-4 receptor
  forms; STAT5 for IL-5 and IL-7; and STAT1/STAT3/STAT5 for IL-9. All other
  `terminal_TF` values are literal `null`.

## Evidence-layer handling

Direct ligand/receptor binding or activation, receptor-proximal relay, and
downstream pathway or cellular function were kept distinct in the
`evidence_layer` field.

- IL-24, IL-33, IL-34, the IL-4/5/6/7/9 receptor complexes, INSL3/RXFP2,
  INSL5/RXFP4, KISS1/KISS1R, KITL/KIT, L1CAM/EGFR, and LEP/LEPR have
  receptor-proximal and downstream assay support in addition to the upstream
  receptor context.
- INHBA/ENG is retained as an accessory association within an activin
  receptor complex. Endoglin was not treated as a standalone INHBA signaling
  receptor because the primary biochemical study requires a ligand-binding
  kinase receptor.
- INSL5/RXFP3 is retained as a low-affinity/antagonist boundary and not as a
  productive INSL5 relay. L1CAM/integrin and laminin/integrin or BCAM rows
  retain direct adhesion/binding evidence without importing generic integrin
  FAK, Src, MAPK, or TF claims that were not isolated for the submitted pair.
- JAG1/CD46 retains the demonstrated CD46-Notch crosstalk and immune output,
  but HES1/RBPJ transcript changes are not promoted to a terminal-TF
  assignment.

## Search boundary and limitations

Searches covered exact symbols and aliases across PubMed, PMC/Europe PMC,
publisher pages, structural/biochemical reports, and pathway/context
comparators. Primary research was prioritized. Receptor-chain nomenclature
was reconciled for IL-20/IL-22, common-gamma cytokine receptors, relaxin
family receptors, integrin heterodimers, laminin alpha chains, and Lutheran/
BCAM. Evidence from cognate ligand families, generic GPCR or integrin
pathways, and expression/co-occurrence predictions was not transferred to
an exact pair without a matching assay.

The strongest limitations are engineered or heterologous receptor systems for
several cytokine and GPCR studies, cell-state dependence of insulin/IGF1R and
KIT signaling, glycosaminoglycan dependence of IL-34/PTPRZ1 binding, and
complex/matrix presentation requirements for the adhesion rows. These
limitations are recorded per row in the TSV.

## Validation

The packet was checked for exactly 25 rows, exact requested order and labels,
unique review IDs and pair labels, populated required fields, no embedded tabs
or extra columns, allowed status/confidence vocabulary, and literal `null`
values wherever no terminal endpoint was assigned. No SQL or shared-register
materialization was performed.
