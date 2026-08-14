# CellChat missing-candidate citation-audit contract

Audit every candidate by opening the cited primary source(s). Confirm exact
ligand-receptor identity, assay, species, receptor complex/chain, and whether
the result is binding, adhesion, receptor activation, or receptor-dependent
function rather than family/pathway/expression-only evidence.

Return exactly one row per input in identical order with header:
`pair_key	pair_label_canonical	final_verdict	source_locators	species_support	support_kind	evidence_summary	limitations	audit_notes`

Allowed final verdicts: `approve_candidate`, `retain_low`, `no_evidence`,
`reject_pair`, `needs_manual_review`. Do not edit canonical ledgers.
