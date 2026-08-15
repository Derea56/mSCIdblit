# Module 21A batch 202 summary

## Scope

This batch reviews exactly the 25 queued Module20A external-review pairs
specified for batch 202, preserving the submitted pair labels and writing no
Module20A or Module21A ledgers. Evidence was searched across PubMed, PMC,
publisher records, and primary structural or biochemical studies. The review
separates ligand–receptor binding or activation, receptor-proximal relay, and
downstream pathway or cellular-function evidence.

## Disposition

- 25 exact pair rows were written.
- 13 rows are `reviewed_relay_candidate`.
- 8 rows are `reviewed_binding_only`.
- 4 rows are `no_evidence_boundary`.
- No terminal TF endpoint was assigned; every `terminal_TF` value is the
  literal `null`.

## Positive relay evidence

Primary studies support receptor-proximal or pathway-linked evidence for
CD274–PDCD1; CD28–CD80 and CD28–CD86 in both label orientations; CD38–PECAM1;
CD47–SIRPA; CD48–CD2; CD48–CD244; CDH1–CDH2; CDH1–ITGAE_ITGB7; CKLF–CCR4;
and the CLCF1–CNTFR_IL6ST_LIFR receptor complex. These rows retain the
appropriate receptor-complex, integrin/cadherin, GPCR, or immune-checkpoint
branch and do not promote pathway outputs to direct molecular edges.

## Binding/function-only and boundary cases

CD274–CD80 is retained as a direct cis-binding checkpoint interaction without
a pair-specific intracellular relay. CD34–SELL is supported only for a
specialized sulfated/sialylated CD34 glycoform. CD34–SELP is an explicit
boundary because P-selectin binding on CD34+ progenitors was assigned to
PSGL1, not the CD34 protein. CD80/CD86–CTLA4 rows document binding and
trans-endocytosis, which is cell-extrinsic ligand removal rather than a
resolved intracellular CTLA-4 relay. CDH1–ITGA2_ITGB1, CDH1–KLRG1, and
CEACAM1–HAVCR2 retain direct or functional evidence without an isolated
pair-specific intracellular cascade. CEACAM16–TECTA/TECTB remain boundaries
because cochlear co-localization and hearing phenotypes did not demonstrate
direct pair binding. The historical CD72–CD5 ligand assignment remains
unresolved because later recombinant and productive cell-surface assays did
not reproduce it. CLCF1–CRLF1 is recorded as a composite cytokine-subunit
formation edge; its signaling relay belongs to the distinct
CNTFR/IL6ST/LIFR receptor complex.

## Search boundary

Searches used exact gene/protein names and aliases including PD-L1/B7-H1,
B7-1/B7-2, PD-1, SHPS-1/SIRPα, 2B4/CD244, CD31/PECAM-1, CD103/αEβ7,
KLRG1, TIM-3, CKLF1, CLC/CLF, CNTFRα, gp130/IL6ST, LIFRβ, and CRLF1.
Primary papers were preferred; PMC and publisher records were used when they
provided the stable full text or bibliographic record. Where a study tested
an expressing cell population, receptor family, glycoform, comparator, or
functional phenotype rather than the exact pair, that limitation is recorded
as a boundary and the row was not promoted to a direct molecular relay.

## Validation target

The TSV must contain the exact 13-column schema, exactly 25 data rows, unique
review IDs and pair labels, populated required fields, allowed confidence
values, exact submitted pair labels, and literal `null` for every unvalidated
terminal TF field.
