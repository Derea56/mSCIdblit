# Module 21A batch 206 summary

## Scope

This batch reviews exactly the 25 requested queued Module 20A pairs
`M20A-EXT-1378` through `M20A-EXT-1402`. Ligand and receptor labels are
preserved verbatim, including the composite labels `Crlf2_Il7r_Tslp`,
`Csf1_Il34`, and `ITGA3_ITGB1`.

Only the batch-206 review TSV and this summary were written. No Module 20A
ledger, Module 21A ledger, saturation register, Module 22A handoff, frozen
manifest, or SQL artifact was edited.

## Disposition

- 4 `reviewed_relay_candidate` rows: Crp–Olr1, Csf1_Il34–Csf1r,
  Csf2–Sdc2, and Cspg4–ITGA3_ITGB1.
- 2 `reviewed_binding_only` rows: Crisp2–Catsper1 and Crtam–Cadm1.
- 19 `no_evidence_boundary` rows: the remaining CRH receptor/accessory
  candidates, the directionally mismatched CRLF2/TSLP receptor-complex row,
  and noncognate CSF1/CSF2/CSF3 receptor, SIRPA, and integrin candidates.
- All `terminal_TF` values are the literal `null`; no explicit terminal TF
  endpoint was established in this batch.

## Positive evidence

- **CRISP2–CATSPER1:** a mouse loss-of-function study combines fertility and
  sperm-motility phenotyping with yeast two-hybrid and immunoprecipitation
  evidence for CRISP2 association with the CATSPER1 channel subunit. This is
  a direct membrane-protein complex association, not a conventional secreted
  ligand/receptor activation edge.
- **CRP–OLR1/LOX-1:** primary binding and receptor-dependence studies support
  direct CRP–LOX-1 binding, with OLR1-dependent complement, ROS, vascular
  permeability, and endothelial inflammatory outputs. No intrinsic-kinase
  relay was inferred for this scavenger receptor.
- **CRTAM–CADM1:** primary T-cell studies support direct CADM1–CRTAM adhesion
  and CADM1-dependent modulation of TCR-coincident IFN-gamma/IL-22 outputs and
  mucosal T-cell residency. The submitted direction is retained, while the
  biological directionality and CRTAM/Scrib dependence are documented as
  limitations.
- **CSF1/IL34–CSF1R:** primary functional and structural studies support the
  two named ligands as independent CSF1R ligands, CSF1R phosphorylation, ERK
  signaling, and myeloid proliferation/differentiation. The composite queue
  label is not treated as a single dual-ligand molecule or simultaneous
  ternary activation event.
- **CSF2–SDC2:** primary osteoblast work demonstrates GM-CSF binding to SDC2,
  SDC2 association with CSF2RA, SDC2 tyrosine phosphorylation, and reduced
  ERK1 activation/mitogenesis after SDC2 depletion. SDC2 is recorded as a
  heparan-sulfate co-receptor, not as a standalone cytokine receptor.
- **CSPG4/NG2–ITGA3/ITGB1:** primary endothelial studies support a
  galectin-3–alpha3beta1 multimolecular complex engaged by soluble/shed NG2,
  beta1-integrin-dependent motility and network formation, and corneal
  angiogenesis. The bridge through galectin-3 and the composite receptor
  label are retained; isolated direct CSPG4 contact with alpha3beta1 was not
  asserted.

## Search boundaries and unresolved cases

Exact-pair searches used submitted symbols and principal aliases across
PubMed, PMC, publisher records, and citation trails. For negative rows,
cognate receptor literature is cited only to define the boundary: CRH is
supported through CRHR1/2 rather than the submitted GPCR/accessory candidates;
TSLP is the ligand for the CRLF2/IL7R receptor complex rather than CRLF2;
CSF1, CSF2, and CSF3 have distinct primary receptor systems; and CD47–SIRPA
or matrix/integrin biology was not reassigned to CSF1 or CSF2. No family-level
pathway, expression, orthology, or shared-cell phenotype was promoted to an
exact direct molecular edge.

## Validation

- 25 data rows plus the required header.
- Exact 13-column schema:
  `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`.
- Review IDs and pair labels are unique and exactly aligned to the requested
  order.
- All fields are populated; confidence values use the established Module 21A
  vocabulary (`low` and `medium-high`).
- Every terminal-TF field is literal `null`.
- No ledger update, SQL materialization, or commit was performed.
