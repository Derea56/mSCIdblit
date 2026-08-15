# Module 21A batch 207 summary

## Scope

This batch reviews exactly the 25 requested queued Module20A external-review
pairs: M20A-EXT-1403, -1404, -1405, -1406, -1407, -1435, -1442, -1453,
-1454, -1456, -1457, -1458, -1459, -1460, -1463, -1464, -1465, -1466,
-1467, -1468, -1469, -1470, -1471, -1472, and -1473. Pair labels are
preserved verbatim. Only this review TSV and summary were written; no
Module20A or Module21A ledger, frozen manifest, saturation register, or SQL
file was edited.

## Disposition

- 25 exact pair rows were written.
- 19 rows are `reviewed_relay_candidate`.
- 5 rows are `reviewed_binding_only`.
- 1 row is `reviewed_scavenging_only`.
- 1 provisional Module22A endpoint is recorded: `STAT3` for Ctf1–Il6st_Lifr,
  because primary cardiomyocyte perturbation studies explicitly identify
  STAT3 as the gp130 downstream effector mediating the hypertrophic response.
  All other `terminal_TF` fields are the literal `null`.

## Positive evidence

The batch contains direct or bounded primary evidence for CT-1 engagement of
the gp130/LIFR complex; CTHRC1 binding to FZD3, FZD5, FZD6 and ROR2 in a
Wnt-containing PCP complex; CXCL12 binding/signaling through SDC4; CXCL14
binding and functional engagement of CXCR4; CYTL1 as a CCR2B ligand; decorin
binding and modulating EGFR, MET and TLR4; DHH binding to BOC, CDON and HHIP;
and DKK1–4 interactions with the requested KREMEN and LRP receptors.

Direct extracellular binding, receptor-complex relay, and pathway or cellular
outputs are kept in separate evidence-layer annotations. DHH–HHIP is retained
as a scavenging/sequestration edge rather than an activating relay. DHH–BOC
and DHH–CDON are binding-only because the cited structural work establishes
the exact ligand–coreceptor interactions but does not isolate a DHH-specific
intracellular perturbation. DKK2–KREMEN1, DKK3–KREMEN1 and DKK4–KREMEN1 are
also retained at the binding layer where functional effects are stronger for
KREMEN2 or otherwise context-dependent.

## Search boundary and limitations

Searches covered exact submitted symbols and principal aliases across PubMed,
PMC, publisher pages and primary structural, biochemical and cell-based
literature. For DKK proteins, family-level receptor studies were used only
when the exact ligand/receptor pair was tested; DKK2 agonism versus antagonism
and KREMEN-dependent effects remain context-dependent. For CT-1, CXCL14,
CYTL1, decorin and Hedgehog proteins, species, recombinant-domain, receptor
complex and cell-model limitations are preserved in each row. No direct TF
endpoint was inferred from pathway or phenotype evidence alone.

## Validation target

The TSV must contain exactly 25 data rows, the exact 13-column schema, unique
review IDs and pair labels, populated required fields, allowed confidence
values, exact requested pair order, and literal `null` in every unvalidated
terminal-TF field. No materialized ledger edge is created in this batch.
