# Module 21A batch 203 summary

## Scope

This batch reviews exactly the 25 currently queued Module 20A external-review
pairs submitted for batch 203. Pair labels are preserved verbatim. The review
keeps ligand–receptor binding or activation, receptor-proximal relay, and
downstream pathway or cellular-function evidence in separate evidence layers.
Only the two batch-203 artifacts were written; no Module 20A or Module 21A
ledger, frozen manifest, saturation register, or SQL file was edited.

## Disposition

- 25 exact pair rows were written.
- 14 rows are `reviewed_relay_candidate`.
- 10 rows are `reviewed_binding_only`.
- 1 row is `reviewed_function_only`.
- No row was assigned `no_evidence_boundary` or `reviewed_unresolved` because
  each submitted pair had at least a primary binding, receptor-complex, or
  pair-specific functional anchor after alias and fragment searches.
- One provisional Module22A endpoint was recorded: `STAT3` for the
  CLCF1-CRLF1/CNTFR-IL6ST composite cytokine receptor branch. All other
  `terminal_TF` fields are the literal `null` because the primary evidence did
  not establish a sufficiently specific terminal transcription-factor endpoint.

## Positive relay and receptor-complex evidence

The batch contains direct or receptor-complex evidence for CLCF1-CRLF1 with the
CNTFR/LIFR/IL6ST-gp130 complex; CLEC11A/Osteolectin with ITGA11/ITGB1;
podoplanin with CLEC1B/CLEC-2; CLEC4G/LSECtin with LAG3; CNTN1 with PTPRZ1
and NrCAM-associated neuronal complexes; CNTN2/TAG1 with NRP1; CNTN6 with
NOTCH1; collagen XI with ITGA1/ITGB1 and ITGA2/ITGB1; collagen XIII with
ITGA11/ITGB1 and ITGA1/ITGB1; collagen XIV with a proteoglycan form of CD44;
collagen XVI with ITGA1/ITGB1 and ITGA2/ITGB1; the endostatin domain of
COL18A1 with GPC1, GPC4, ITGA5/ITGB1 and KDR/VEGFR2; and collagen I with DDR1.

The CNTN3-, CNTN4- and CNTN6-PTPRG rows and CNTN4-APLP1 are retained as
binding-only rows because the primary studies establish direct extracellular
complex formation without a selective downstream intracellular readout for
the exact pair. COL10A1-ITGA2/ITGB1, COL16A1-integrin rows, and COL14A1-CD44
are similarly not promoted to a kinase relay when the primary evidence is
adhesion, focal-adhesion recruitment, or glycan-dependent recognition only.

## Fragment, composite, and context limitations

Several Module20A labels represent molecular complexes or precursor proteins
rather than the active experimental species. CLCF1-CRLF1 is a composite
secreted cytokine; CLEC1B is commonly named CLEC-2; and the COL18A1 rows are
mostly supported by its proteolytic endostatin domain rather than intact
full-length collagen XVIII. Collagen XI and collagen I are multichain fibrillar
ligands, and some downstream results include DDR2 or other receptor crosstalk.
The contactin/PTPRG and contactin/amyloid studies establish extracellular
binding and cell-surface complexes but do not by themselves identify a
terminal TF. These limitations are recorded per row and pathway-level or
functional evidence was not used to invent unsupported direct molecular edges.

## Search boundary

Searches covered exact submitted symbols plus principal aliases (CLCF1/CLF,
CRLF1, CNTFR, gp130/IL6ST; CLEC-2; LSECtin; F3/contactin, TAG1/NB-3; PTPRG,
PTPRZ1, NrCAM; endostatin, collagen XIII/XIV/XVI; DDR1/KDR/Flk-1) across
PubMed, PMC, publisher full-text pages, and pathway/interaction records used
only to locate primary papers. Primary research was retained when available.
Where a result depended on glycosaminoglycan chains, a receptor complex,
fragmented collagen, or family-level comparator evidence, the row keeps the
appropriate binding/function layer and states the boundary rather than
promoting it to a universal direct relay.

## Validation target

The TSV should contain exactly 25 data rows, the exact 13-column schema,
unique review IDs and pair labels, populated required fields, allowed
confidence values, and literal `null` in every unvalidated terminal-TF field.
