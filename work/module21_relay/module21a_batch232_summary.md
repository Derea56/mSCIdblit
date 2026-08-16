# Module 21A batch 232 review summary

Scope: exactly the 25 queued Module20A pairs supplied for batch 232, in the supplied order. The review used primary PubMed/PMC/publisher records and records only stable PMID, PMCID, or DOI citations in the TSV.

## Disposition

| status | rows |
|---|---:|
| reviewed_relay_candidate | 12 |
| reviewed_function_only | 6 |
| reviewed_no_downstream_evidence | 2 |
| reviewed_scavenging_only | 3 |
| reviewed_unresolved | 2 |
| no_evidence_boundary | 0 |
| total | 25 |

The review keeps direct binding/activation, receptor-proximal relay, and downstream pathway/function as separate semicolon-delimited evidence layers. Integrin and receptor-complex subunits are not promoted to standalone receptors. THBS2–NOTCH3, THPO–MPL, THY1–alphaVbeta3, TIMP1–CD63, TIMP2–alpha3beta1, TNC–EGFR, TRH–TRHR, TSLP–CRLF2/IL7R, and urocortin–CRHR1/2 rows retain relay evidence where the primary assays support it.

## Explicit boundaries

- `M20A-EXT-3304` TIMP3–AGTR2 is unresolved: direct interaction was reported, but AGTR2-specific productive signaling was not established.
- `M20A-EXT-3336` APRIL/TRDL-1–FAS is unresolved: co-precipitation and Jurkat cell death suggest an alternate ligand relationship, but purified receptor affinity, receptor-specific blockade, and FADD/DISC recruitment were not shown.
- `M20A-EXT-3298` THY1–ITGAX_ITGB2 and `M20A-EXT-3317` TNC–PTPRZ1 have direct binding evidence but no qualifying downstream receptor output in the primary records reviewed.
- `M20A-EXT-3332` TRAIL–TNFRSF11B/OPG and the transferrin–TFR2/TFR1 rows are retained as decoy/cargo uptake layers, not kinase relays.
- No row was assigned `no_evidence_boundary`; all 25 had at least some primary pair-level evidence. No pathway/function-only observation was used to infer a direct interaction.

## Terminal TF handoff

All terminal TF entries are explicitly provisional measured endpoints; none is a finalized TF-program assignment.

- `M20A-EXT-3293`: HES1; HES5
- `M20A-EXT-3295`: STAT5
- `M20A-EXT-3362`: CREB
- `M20A-EXT-3388`: STAT5
- `M20A-EXT-3397`: FOS

Unique provisional TF values: HES1, HES5, STAT5, CREB, FOS. The other 20 rows use literal `null`.

## Validation

- TSV has the exact 13-column header: `review_id,pair,status,stable_citations,species,cell_type_model,assay_or_perturbation,relation_type,evidence_layer,pathway_branch,confidence,limitations,terminal_TF`.
- Exactly 25 data rows are present, with unique review IDs and exact requested order/pair labels.
- Required fields are non-empty; terminal TF is either a measured provisional endpoint or literal `null`.
- Confidence values use the controlled batch vocabulary: `high`, `medium-high`, or `medium`.
- Stable citations are limited to PMID, PMCID, and DOI identifiers; no tabs, embedded newlines, extra columns, or unsupported citation types are present.
- Frozen Module20A manifest was not modified and retains SHA-256 `02e77740cdd46dc7835fbfe356835feeb2a0c692a3c6a5962831f6de1786288e`.
- Only `module21a_batch232_review.tsv` and `module21a_batch232_summary.md` were written for this task; shared registers, Module20A files, manifest, SQL, and existing files were not modified.
