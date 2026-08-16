# Module 21A batch 230 review summary

This batch reviews exactly the 25 supplied queued pairs in the submitted order
using the exact 13-column tab-delimited schema. Only the batch 230 TSV and this
summary were written.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 15 |
| `reviewed_function_only` | 10 |
| **total** | **25** |

No pair was assigned `no_evidence_boundary`: every queued pair had at least one
primary pair-specific citation in the evidence gathered for this batch. The
rows still record unresolved relay boundaries and no-downstream cases explicitly
in `limitations` and `pathway_branch`. In particular, SLPI-PLSCR1/4, SNCA-LAG3,
SPON1-APP/LRP8, and the SPP1 integrin rows retain membrane-complex, uptake,
processing, adhesion, or functional evidence without inventing a canonical
intracellular relay. The SOSTDC1-LRP4 row preserves extracellular Wnt/BMP
integration and does not convert a downstream Shh developmental effect into a
direct SOSTDC1-Shh interaction.

## Evidence handling

Binding or activation, receptor-proximal relay, and downstream pathway/function
are separated in `evidence_layer`. Receptor-complex and subunit rows preserve
the complex: SPON2-ITGAM and SPON2-ITGB2 are both explicitly interpreted as
Mac-1 alphaM-beta2 subunit edges, and SPON1-APP/LRP8 retains the APP/ApoER2
complex. Uptake, secretase processing, adhesion, migration, and antiviral
function are not promoted to direct intracellular signaling evidence.

The strongest direct binary or receptor-complex evidence is represented for
SHH-SCUBE2, SLIT1-ROBO2, SLIT3-ROBO1/ROBO4, SLURP1-CHRNA7, SNCA-PFF-LAG3,
SOST-LRP5/LRP6, SOSTDC1-LRP4/LRP6, SPON1-LRP8, SPON2-Mac-1, and the SPP1
receptor rows. Where the evidence is primarily a functional or uptake endpoint,
the status is `reviewed_function_only` rather than a claim of a resolved relay.

## Provisional terminal-TF handoffs

Only explicitly measured transcriptional or nuclear endpoints were retained:

- `GLI1 (provisional)` for SHH-SCUBE2, where Gli1 qRT-PCR was measured.
- `RELA (provisional)` for SLURP1-CHRNA7 and both SPON2-Mac-1 subunit rows,
  where nuclear NF-kB p65 was measured in the cited contexts.
- `TCF/LEF family (provisional)` for SOST-LRP4/LRP5/LRP6, representing the
  measured Wnt reporter endpoint rather than an inferred target gene.

Every other `terminal_TF` value is the literal `null`. No TF was inferred from
generic pathway membership, phosphorylation, expression, uptake, adhesion,
migration, processing, or cellular function alone.

## Validation

- Exactly 25 data rows are present.
- Exact requested review-ID and pair order is preserved.
- The header and every data row have exactly 13 tab-delimited columns.
- Required fields are populated for every row, including function-only and
  unresolved-relay cases.
- Confidence values are restricted to `high`, `medium-high`, `medium`,
  `medium-low`, and `low`.
- Stable citations use only PMID, PMCID, DOI, or URL forms.
- Literal `null` is used for every unassigned `terminal_TF` value.
- The frozen manifest SHA-256 is
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
