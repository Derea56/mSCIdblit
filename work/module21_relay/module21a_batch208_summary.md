# Module 21A batch 208 summary

## Scope

This batch reviews exactly the 25 queued Module20A external-review pairs
specified for batch 208: M20A-EXT-1475, -1478, -1479, -1480, -1481, -1482,
-1484, -1488, -1489, -1492, -1493, -1496, -1497, -1499, -1500, -1502,
-1503, -1508, -1510, -1511, -1512, -1513, -1514, -1516, and -1521. Pair
labels are preserved verbatim. Only this review TSV and summary were written;
no Module20A or Module21A ledgers, frozen manifest, saturation register, or
SQL file was edited.

## Disposition

- 25 exact pair rows were written.
- 10 rows are `reviewed_relay_candidate`: DKK4-LRP6, Draxin-DCC,
  EBI3-IL12A/IL12RB2-gp130, EBI3-IL27/IL27RA-gp130, EDN1-EDNRA,
  EDN1-EDNRB, EDN2-EDNRA, EDN2-EDNRB, EFNA1-EPHA2, and EFNA1-EPHA8.
- 15 rows are `reviewed_binding_only`: the seven desmocollin-desmoglein
  adhesion pairs, EDN3-EDNRA, EDN3-EDNRB, EFNA1-EPHA1/3/4/5/6, and
  EFNA3-EPHA1.
- The endothelin records are included in the relay count only where exact
  receptor activation or receptor-dependent function was demonstrated;
  EDN3-EDNRA and EDN3-EDNRB remain binding/selectivity-only.
- Provisional terminal-TF assignments are limited to `STAT1;STAT4` for the
  IL-35 receptor-complex row and `STAT1;STAT3` for the IL-27 receptor-complex
  row. All other `terminal_TF` values are the literal `null`.

## Positive evidence

The batch contains exact DKK4-LRP6 co-immunoprecipitation and WNT/beta-catenin
functional evidence; direct Draxin-DCC binding with DCC-dependent neurite and
growth-cone phenotypes; pairwise heterophilic Dsc-Dsg adhesion across all seven
requested desmosomal pairs; IL-35 signaling through IL12RB2-gp130 with a
STAT1:STAT4 effector complex; and IL-27 signaling through IL27RA-gp130 with
STAT1/STAT3 outputs. The primary desmosomal study tested all Dsg:Dsc pairwise
combinations rather than inferring the seven rows from a family-level rule.

Endothelin evidence is peptide- and receptor-specific: EDN1 supports EDNRA
and EDNRB relay records, EDN2 supports EDNRA function and EDNRB activation in
a heterologous receptor system with a mammalian EDNRB negative boundary, and
EDN3 is retained at binding/selectivity only. EFNA1-EPHA2 and EFNA1-EPHA8 have
exact activation evidence; EFNA1-EPHA1/3/4/5/6 and EFNA3-EPHA1 remain binding
records because receptor-family binding was not promoted to pair-specific
downstream signaling.

## Search boundary and limitations

Searches covered exact submitted symbols and principal aliases across PubMed,
PMC, publisher pages, and primary biochemical, structural, receptor-reconstitution,
and cell-perturbation studies. Direct molecular binding, receptor-complex relay,
and downstream functional evidence are kept in separate layer annotations.
Desmosomal cadherins are adhesion molecules rather than canonical intracellular
signaling receptors, so their records remain binding-only. Ephrin-A ligands are
membrane-associated and activation depends on cell contact, clustering, receptor
context, and avidity. Endothelin receptor usage varies with species and tissue;
the EDN2-EDNRB retinal result is explicitly retained as a negative context
boundary. No direct TF endpoint was inferred from pathway or phenotype evidence
alone.

## Validation target

The TSV must contain exactly 25 data rows, the exact 13-column schema, unique
review IDs and pair labels, populated required fields, allowed confidence values,
exact requested pair order, and literal `null` in every unvalidated terminal-TF
field. No materialized ledger edge is created in this batch.
