# Module 21A batch 229 review summary

This batch reviews exactly the 25 supplied queued pairs in the submitted order
using the exact 13-column schema:

`review_id, pair, status, stable_citations, species, cell_type_model, assay_or_perturbation, relation_type, evidence_layer, pathway_branch, confidence, limitations, terminal_TF`

Only `module21a_batch229_review.tsv` and this summary were written. Shared
Module21A registers, Module20A ledgers, the frozen manifest, SQL, and existing
files were not modified.

## Disposition

| status | count |
|---|---:|
| `reviewed_relay_candidate` | 17 |
| `reviewed_binding_only` | 1 |
| `reviewed_function_only` | 4 |
| `reviewed_unresolved` | 2 |
| `no_evidence_boundary` | 1 |
| **total** | **25** |

The unresolved rows are Sema3g–NRP2/PLXNA2, where Plexin-A2 evidence is only
family-level or mixed-ligand, and Sema6b–PLXNA2, where the primary evidence
supports the reverse PLXNA2-to-SEMA6B signaling orientation. Sftpa1–TLR2 is an
explicit no-evidence boundary because its queue anchor is a computational
single-cell prediction rather than an exact binding or perturbation study.

## Evidence handling

Ligand–receptor binding or activation, receptor-proximal relay, and downstream
pathway or cellular function are recorded as separate evidence layers. The
Sema4d–ERBB2, Sema4d–MET, and Sema5a–MET rows retain receptor-complex or
transactivation edges and explicitly do not claim direct ligand binding to the
receptor-tyrosine-kinase partner. The Sftpd–TLR4 row is an inhibitory
SFTPD–TLR4/MD-2 complex edge, not productive TLR4 activation. Family-level
SFTPA, SEMA3, and Plexin evidence was not used to promote unresolved exact
pairs.

## Provisional terminal-TF handoffs

Measured downstream transcriptional endpoints support these provisional values:

- Sema3g–NRP2/PLXNA1: `MYC;YAP`
- Sfrp2–FZD5: `NFATC3`
- Shh–BOC: `NKX2-2;OLIG2`
- Shh–CDON: `GLI1`
- Shh–GAS1: `NKX2-2`
- Shh–HHIP: `GLI1`

Every other `terminal_TF` value is the literal `null`. No TF was inferred from
generic pathway membership, phosphorylation alone, expression/co-occurrence,
or cellular function without an explicitly measured transcriptional endpoint.

## Validation

- Exact requested row count: 25 data rows.
- Exact requested ID and pair order: preserved.
- Exact 13-column tab-delimited schema: used.
- Required fields: populated for every row, including unresolved and
  no-evidence boundaries.
- Confidence vocabulary: restricted to `high`, `medium-high`, `medium`,
  `medium-low`, and `low`.
- Literal `null`: used for all unassigned terminal-TF fields.
- Frozen manifest SHA-256 verified unchanged:
  `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`
  for `work/module20_db_seed/evidence_escalation_router/module20a_lr_release_manifest.json`.
