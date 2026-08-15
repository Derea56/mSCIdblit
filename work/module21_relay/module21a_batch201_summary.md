# Module 21A batch 201 summary

## Scope

This batch reviews exactly 25 currently queued Module 20A external-review pairs,
preserving the submitted pair labels. The review separates ligand–receptor
binding or activation, receptor-proximal relay, and downstream pathway or
cellular-function evidence. No Module 20A or Module 21A ledgers were edited.

## Disposition

- 25 exact pair rows were written.
- 16 rows are `reviewed_relay_candidate`.
- 4 rows are `reviewed_binding_only`.
- 1 row is `reviewed_function_only`.
- 2 rows are `reviewed_scavenging_only`.
- 2 rows are `no_evidence_boundary`.
- No terminal TF endpoint was assigned; every `terminal_TF` value is the literal
  `null` because the reviewed primary studies did not establish a sufficiently
  specific endpoint for Module 22A.

## Positive relay and complex evidence

Primary evidence supports AVP–AVPR2 cAMP and beta-arrestin/ERK branches;
BMP2–ACVR1, BMP2–ACTR2A, and BMP2–RGMB receptor-complex contexts;
CALCA-derived CGRP through CALCR–RAMP1 or CALCRL–RAMP1 complexes; CCKAR and
CCKBR calcium/PKC branches; CCL11 partial agonism at CCR2; CCL17–CCR8;
processing-dependent CCL4–CCR1; CCL5–GPR75; CCL5–SDC4/PKCalpha;
CD177–PECAM1; and CD200–CD200R1.

## Boundary and limitation cases

BMP10–BMPR1A remains unresolved because primary structural evidence resolves
BMP10 with BMPRII/ALK1, while BMPR1A is only detected or discussed in a cardiac
model without pair-specific perturbation. BMP2–GPC1 is retained at the HSPG
boundary because the primary studies test heparan sulfate/proteoglycan classes,
not GPC1 specifically. CCL11–CXCR3 is binding/decoy evidence without agonism;
CCL12–ACKR2 and CCL20–ACKR4 are atypical scavenging branches; CCL2–CCR1 is a
weak binding-context boundary; CCL5–SDC1 lacks a defined SDC1-only relay; and
CD200–CD200R2 plus CD22–PTPRC remain context-dependent receptor-family or
glycan-mediated cases. These findings were not promoted to unsupported direct
molecular edges.

## Search boundary

Searches covered PubMed-indexed primary studies and available PMC or publisher
records for the exact ligand/receptor names and aliases, including AVPR2/V2R,
ACVR2A/ActRIIA, ACVR1/ALK2, RGMB/RGMb, CALCRL/CLR, RAMP1, CCKAR/CCKBR,
ACKR2/ACKR4, GPR75, syndecans, PECAM1/CD31, CD200R paralogs, CD45/PTPRC, and
the relevant processed chemokine forms. Where only receptor-family, glycan,
scavenging, or comparator evidence was found, the row records that boundary
explicitly rather than transferring pathway evidence to the exact pair.

## Validation target

The TSV must contain the exact 13-column schema, exactly 25 rows, unique review
IDs and pair labels, populated required fields, allowed confidence values, and
literal `null` for every unvalidated terminal TF field.
